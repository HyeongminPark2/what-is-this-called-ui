const { chromium } = require('playwright');
const path = require('path');
// 기본은 레포의 파일을 연다. 배포본을 검사하려면 주소를 인자로 준다.
//   node tools/check.js
//   node tools/check.js https://hyeongminpark2.github.io/what-is-this-called-ui/
const ROOT = path.resolve(__dirname, '..');
const BASE = process.argv[2];
const url = f => BASE ? new URL(f, BASE).href : 'file://' + path.join(ROOT, f);

(async () => {
  const browser = await chromium.launch();
  const errors = [];
  const fail = [];

  // ── 1. index.html ─────────────────────
  let page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  page.on('console', m => { if (m.type() === 'error') errors.push('[index] ' + m.text()); });
  page.on('pageerror', e => errors.push('[index pageerror] ' + e.message));
  await page.goto(url('index.html'));
  const modalLinks = await page.locator('a[href="items/modal.html"]').count();
  if (modalLinks < 2) fail.push(`index: 모달 링크 ${modalLinks}개 (지도+혼동쌍+목차 기대)`);
  await page.waitForTimeout(500);

  // ── 화면 지도 ──
  const mapWide = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('.mapfig').forEach(fig => {
      const name = fig.dataset.map;
      const labels = [...fig.querySelectorAll('.lbl[data-t]')];
      const seen = new Set();

      labels.forEach((lbl, i) => {
        const t = fig.querySelector('[data-p="' + lbl.dataset.t + '"]');
        if (!t) { bad.push(`${name}: 이름표 '${lbl.dataset.t}'가 가리킬 대상이 없음`); return; }
        if (seen.has(lbl.dataset.t)) bad.push(`${name}: data-p="${lbl.dataset.t}" 중복`);
        seen.add(lbl.dataset.t);
        if (!t.getBoundingClientRect().width) bad.push(`${name}: '${lbl.dataset.t}' 대상이 안 보임`);
        const a = lbl.querySelector('.no'), n = t.querySelector(':scope > .partno');
        if (!a || !n || a.textContent !== n.textContent || a.textContent !== String(i + 1)) {
          bad.push(`${name}: ${i + 1}번 이름표와 배지 번호가 안 맞음`);
        }
        if (n && getComputedStyle(n).display === 'none') bad.push(`${name}: ${i + 1}번 배지가 안 보임`);
      });

      // 기본 상태에서는 선을 긋지 않는다 — 이게 이번 설계의 요점이다
      const gs = fig.querySelectorAll('.mapfig__lines g').length;
      if (gs !== 0) bad.push(`${name}: 짚지도 않았는데 지시선이 ${gs}개 그려져 있음`);

      // 배지가 조상 어디에서든 잘리지 않는가 (overflow:hidden 인 상자를 모두 거슬러 본다)
      fig.querySelectorAll('.partno').forEach(n => {
        const r = n.getBoundingClientRect();
        for (let el = n.parentElement; el && el !== document.body; el = el.parentElement) {
          const ov = getComputedStyle(el).overflow;
          if (ov === 'visible') continue;
          const b2 = el.getBoundingClientRect();
          if (r.left < b2.left - 0.5 || r.top < b2.top - 0.5 ||
              r.right > b2.right + 0.5 || r.bottom > b2.bottom + 0.5) {
            bad.push(`${name}: ${n.textContent}번 배지가 '${el.className.split(' ')[0]}'(overflow:${ov})에 잘림`);
            break;
          }
        }
      });

      // span 을 블록으로 안 바꾸면 높이·너비가 먹지 않아 납작해진다.
      // 글자 없는 빈 칸(이미지 자리, 띠)이 inline 이면 거의 틀림없이 이 실수다.
      fig.querySelectorAll('.appmock *').forEach(el => {
        if (el.tagName === 'BR') return;
        if (el.textContent.trim() || el.children.length) return;
        if (getComputedStyle(el).display !== 'inline') return;
        const r = el.getBoundingClientRect();
        if (r.height < 4 || r.width < 4) {
          bad.push(`${name}: 빈 '${(el.className || el.tagName).toString().split(' ').pop()}'가 inline 이라 납작함 (${Math.round(r.width)}×${Math.round(r.height)})`);
        }
      });

      // 회전·확대된 요소에 번호를 붙이면 배지까지 같이 변형되어 안 읽힌다
      fig.querySelectorAll('[data-p]').forEach(el => {
        const tr = getComputedStyle(el).transform;
        if (tr && tr !== 'none' && !tr.startsWith('matrix(1, 0, 0, 1')) {
          bad.push(`'${el.dataset.p}'가 변형된 요소라 번호까지 같이 돌아감 (${tr.slice(0, 24)})`);
        }
      });

      // 번호끼리 겹치면 하나가 안 보인다
      const ns = [...fig.querySelectorAll('.partno')];
      ns.forEach((a, i) => ns.slice(i + 1).forEach(b2 => {
        const r = a.getBoundingClientRect(), q = b2.getBoundingClientRect();
        if (r.right > q.left + 1 && r.left < q.right - 1 && r.bottom > q.top + 1 && r.top < q.bottom - 1) {
          bad.push(`${name}: ${a.textContent}번과 ${b2.textContent}번 배지가 겹침`);
        }
      }));

      // 번호 배지가 '다른' 부품을 덮지 않는가 (자기 대상과 그 바깥 상자는 괜찮다)
      const targets = [...fig.querySelectorAll('[data-p]')];
      fig.querySelectorAll('.partno').forEach(n => {
        const own = n.parentElement, nr = n.getBoundingClientRect();
        targets.forEach(t2 => {
          if (t2 === own || t2.contains(own)) return;
          const r2 = t2.getBoundingClientRect();
          // 큰 상자는 빈 곳이 많아 겹쳐도 가리는 게 없다. 작은 조작 부품만 본다.
          if (r2.height >= 30) return;
          // 상자가 스치는 것과 내용을 가리는 건 다르다. 그 부품 넓이의 3분의 1을 넘게
          // 덮을 때만 문제로 본다.
          const ov = Math.max(0, Math.min(nr.right, r2.right) - Math.max(nr.left, r2.left)) *
                     Math.max(0, Math.min(nr.bottom, r2.bottom) - Math.max(nr.top, r2.top));
          if (ov > r2.width * r2.height * 0.35) {
            bad.push(`${name}: ${n.textContent}번 배지가 '${t2.dataset.p}'를 ${Math.round(ov / (r2.width * r2.height) * 100)}% 덮음`);
          }
        });
      });

      // 떠 있는 부품이 목업 밖으로 새지 않는가
      const mock = fig.querySelector('.appmock'), mr = mock.getBoundingClientRect();
      mock.querySelectorAll('*').forEach(el => {
        if (getComputedStyle(el).position !== 'absolute') return;
        if (el.classList.contains('partno')) return;   // 번호는 일부러 바깥에 둔다
        const r = el.getBoundingClientRect();
        if (r.top < mr.top - 1 || r.bottom > mr.bottom + 1 || r.left < mr.left - 1 || r.right > mr.right + 1) {
          bad.push(`${name}: ${el.className.split(' ')[0]}가 목업 밖에 있음`);
        }
      });
    });

    const fab = document.querySelector('.ph__fab'), sheet = document.querySelector('.ph__sheet');
    if (fab && sheet && fab.getBoundingClientRect().bottom > sheet.getBoundingClientRect().top) {
      bad.push('폰: FAB가 바텀시트에 가림');
    }
    return bad.slice(0, 6);
  });
  if (mapWide.length) fail.push(...mapWide);

  // 이름 → 화면: 짚으면 선 하나가 생기고 그 끝이 대상에 닿는가
  const lbl = page.locator('.mapfig[data-map="pc"] .lbl[data-t="table"]');
  await lbl.hover();
  await page.waitForTimeout(150);
  const hov = await page.evaluate(() => {
    const fig = document.querySelector('.mapfig[data-map="pc"]');
    const gs = [...fig.querySelectorAll('.mapfig__lines g')];
    const t = fig.querySelector('[data-p="table"]');
    const out = { n: gs.length, lit: t.classList.contains('is-on'), hit: false };
    if (gs.length === 1) {
      const box = fig.querySelector('.mapfig__lines').getBoundingClientRect();
      const r = t.getBoundingClientRect(), ln = gs[0].querySelector('line');
      const x = parseFloat(ln.getAttribute('x2')) + box.left, y = parseFloat(ln.getAttribute('y2')) + box.top;
      out.hit = x >= r.left - 3 && x <= r.right + 3 && y >= r.top - 3 && y <= r.bottom + 3;
    }
    return out;
  });
  if (hov.n !== 1) fail.push(`이름을 짚었을 때 지시선이 ${hov.n}개 (1 기대)`);
  if (!hov.lit) fail.push('이름을 짚어도 화면의 부분이 안 밝아짐');
  if (hov.n === 1 && !hov.hit) fail.push('지시선 끝이 대상 밖에 찍힘');

  // 화면 → 이름: 부품을 짚으면 목록에서 이름이 밝아지는가 (겹친 것은 안쪽이 이긴다)
  await page.locator('.mapfig[data-map="pc"] [data-p="avatar"]').hover();
  await page.waitForTimeout(150);
  const back = await page.evaluate(() => {
    const on = [...document.querySelectorAll('.mapfig[data-map="pc"] .lbl.is-on')].map(e => e.dataset.t);
    return on;
  });
  if (back.length !== 1 || back[0] !== 'avatar') {
    fail.push(`부품을 짚었을 때 밝아진 이름이 [${back.join(',')}] (avatar 하나만 기대)`);
  }
  await page.mouse.move(2, 2);
  await page.waitForTimeout(150);
  const after = await page.evaluate(() => document.querySelectorAll('.mapfig .is-on, .mapfig__lines g').length);
  if (after !== 0) fail.push('마우스를 치웠는데 강조와 지시선이 남아 있음');

  await page.screenshot({ path: '/tmp/uicheck/1-index-pc.png', fullPage: true });

  await page.setViewportSize({ width: 390, height: 844 });
  const hScroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  if (hScroll > 2) fail.push(`index 390px: 가로 넘침 ${hScroll}px`);
  // 좁은 화면: 선 대신 번호로 잇는다
  const mapNarrow = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('.mapfig').forEach(fig => {
      const name = fig.dataset.map;
      if (getComputedStyle(fig.querySelector('.mapfig__lines')).display !== 'none') {
        bad.push(`${name}: 좁은 화면인데 지시선이 보임`);
      }
      const labels = [...fig.querySelectorAll('.lbl[data-t]')];
      const nos = [...fig.querySelectorAll('.partno')];
      if (nos.length !== labels.length) bad.push(`${name}: 번호 배지 ${nos.length}개 / 이름표 ${labels.length}개`);
      if (nos.length && getComputedStyle(nos[0]).display === 'none') bad.push(`${name}: 번호 배지가 안 보임`);
      // 배지가 스크롤 상자에 잘리지 않는가
      const sc = fig.querySelector('.mapfig__screen').getBoundingClientRect();
      nos.forEach(n => {
        const r = n.getBoundingClientRect();
        if (r.left < sc.left - 0.5 || r.top < sc.top - 0.5) {
          bad.push(`${name}: ${n.textContent}번 배지가 가장자리에 잘림`);
        }
      });

      labels.forEach((lbl, i) => {
        const a = lbl.querySelector('.no'), t = fig.querySelector('[data-p="' + lbl.dataset.t + '"]');
        const bnum = t && t.querySelector(':scope > .partno');
        if (!a || !bnum || a.textContent !== bnum.textContent) {
          bad.push(`${name}: ${i + 1}번 이름표와 배지 번호가 안 맞음`);
        }
      });
    });
    return bad.slice(0, 6);
  });
  if (mapNarrow.length) fail.push(...mapNarrow);

  await page.screenshot({ path: '/tmp/uicheck/2-index-mobile.png', fullPage: true });
  await page.close();

  // ── 2. 항목 카드 — 일곱 장 모두 같은 틀인지 ──
  const ITEMS = ['modal', 'dialog', 'sheet', 'drawer', 'popover', 'tooltip', 'toast'];

  for (const slug of ITEMS) {
    page = await browser.newPage({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 1 });
    page.on('console', m => { if (m.type() === 'error') errors.push(`[${slug}] ` + m.text()); });
    page.on('pageerror', e => errors.push(`[${slug} pageerror] ` + e.message));
    await page.goto(url('items/' + slug + '.html'));
    await page.waitForTimeout(600);

    const r = await page.evaluate(() => {
      const bad = [];
      const slots = document.querySelectorAll('section.slot').length;
      if (slots !== 10) bad.push(`칸이 ${slots}개 (10 기대)`);

      // 해부도: 그림의 번호와 목록이 1대1인가
      const npin = document.querySelectorAll('.anat [data-pin]').length;
      const nlist = document.querySelectorAll('.pin-list li').length;
      if (npin !== nlist) bad.push(`해부도 번호 ${npin}개 vs 목록 ${nlist}개`);
      // 빈 태그(hr·img·input·br)에는 ::before 가 안 그려져 번호가 보이지 않는다
      document.querySelectorAll('.anat [data-pin]').forEach(el => {
        if (['HR', 'IMG', 'INPUT', 'BR', 'EMBED'].includes(el.tagName)) {
          bad.push(`${el.dataset.pin}번이 빈 태그(${el.tagName})라 번호가 안 그려짐`);
        }
      });
      const nums = [...document.querySelectorAll('.anat [data-pin]')].map(e => +e.dataset.pin).sort((x, y) => x - y);
      if (nums.some((v, i) => v !== i + 1)) bad.push(`해부도 번호가 1부터 이어지지 않음: ${nums.join(',')}`);

      // 글이 세로로 쌓이는 붕괴
      document.querySelectorAll('p, span, li, b, td, figcaption').forEach(el => {
        if (!el.textContent.trim() || el.children.length) return;
        const q = el.getBoundingClientRect();
        if (q.width > 0 && q.width < 46 && q.height > 170) bad.push(`글이 세로로 쌓임: ${el.tagName.toLowerCase()}.${(el.className||'').toString().slice(0,20)}`);
      });

      // 그림이 칸 밖으로 잘리는지
      document.querySelectorAll('.shot').forEach(shot => {
        const sr = shot.getBoundingClientRect();
        shot.querySelectorAll(':scope > *').forEach(el => {
          const q = el.getBoundingClientRect();
          if (q.right > sr.right + 1 || q.left < sr.left - 1) bad.push(`그림이 칸 밖으로: ${(el.className||'').toString().slice(0,18)}`);
        });
      });

      // 해부도 번호가 가리키는 것을 덮는지 (작은 것만)
      document.querySelectorAll('.anat [data-pin]').forEach(a => {
        const ar = a.getBoundingClientRect();
        document.querySelectorAll('.anat [data-pin]').forEach(b2 => {
          if (a === b2 || a.contains(b2) || b2.contains(a)) return;
          const br = b2.getBoundingClientRect();
          if (br.height >= 30) return;
          const ov = Math.max(0, Math.min(ar.right, br.right) - Math.max(ar.left, br.left)) *
                     Math.max(0, Math.min(ar.bottom, br.bottom) - Math.max(ar.top, br.top));
          if (ov > br.width * br.height * 0.6) bad.push(`해부도 ${a.dataset.pin}번이 ${b2.dataset.pin}번을 덮음`);
        });
      });

      // 페이지 안 이동 링크가 실제로 가리키는 곳이 있는가
      document.querySelectorAll('.jump a').forEach(a => {
        if (!document.querySelector(a.getAttribute('href'))) bad.push(`이동 링크가 가리키는 곳 없음: ${a.getAttribute('href')}`);
      });

      const h = document.documentElement.scrollHeight;
      if (h > 12000) bad.push(`페이지가 비정상적으로 김: ${h}px`);
      return bad.slice(0, 5);
    });
    r.forEach(x => fail.push(`${slug}: ${x}`));

    // 형제 링크가 일곱 중 자기를 뺀 여섯을 가리키는가
    const sib = await page.$$eval('.siblings a[href$=".html"]', as => as.map(a => a.getAttribute('href')));
    if (sib.length !== 6) fail.push(`${slug}: 형제 링크가 ${sib.length}개 (6 기대)`);
    if (sib.includes(slug + '.html')) fail.push(`${slug}: 형제 목록에 자기 자신이 있음`);

    // ①칸 폭 토글
    await page.locator(`.seg[data-seg="${slug}"] button[data-w="768"]`).click();
    await page.waitForTimeout(430);
    const w = await page.locator('.stage iframe').evaluate(el => Math.round(el.getBoundingClientRect().width));
    if (Math.abs(w - 768) > 4) fail.push(`${slug}: 폭 토글 768 → 실제 ${w}px`);
    if (await page.locator('.preview-open').count() !== 1) fail.push(`${slug}: ①칸에 새 탭 링크 없음`);

    // 폰 폭에서 가로로 넘치지 않는가
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(500);
    const over = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    if (over > 2) fail.push(`${slug}: 390px 가로 넘침 ${over}px`);

    await page.close();
  }

  // ── 3. 데모가 실제로 동작하는가 ──
  const demo = async (f, w, h) => {
    const pg = await browser.newPage({ viewport: { width: w || 900, height: h || 760 } });
    pg.on('pageerror', e => errors.push(`[demo ${f}] ` + e.message));
    pg.on('console', m => { if (m.type() === 'error') errors.push(`[demo ${f}] ` + m.text()); });
    await pg.goto(url('demos/' + f + '.html'));
    await pg.waitForTimeout(250);
    return pg;
  };

  // 모달 — 포커스 갇힘은 iframe 밖에서만 검사할 수 있다
  page = await demo('modal', 1100, 800);
  const opener = page.locator('.js-open').first();
  await opener.click(); await page.waitForTimeout(350);
  const dlg = page.locator('dialog.mdl');
  if (!await dlg.evaluate(el => el.contains(document.activeElement))) fail.push('모달: 열릴 때 포커스가 안 들어감');
  let landed = null, cycled = false;
  for (let i = 0; i < 14; i++) {
    await page.keyboard.press('Tab');
    const where = await dlg.evaluate(el => {
      const a = document.activeElement;
      if (el.contains(a)) return 'in';
      if (!a || a === document.body || a === document.documentElement) return 'doc';
      return a.tagName.toLowerCase();
    });
    if (where === 'in' && i > 2) cycled = true;
    if (where !== 'in' && where !== 'doc') landed = where;
  }
  if (landed) fail.push(`모달: 포커스가 배경 요소(${landed})에 닿음`);
  if (!cycled) fail.push('모달: 포커스 순환이 돌아오지 않음');
  if (!await page.evaluate(() => { const b = document.querySelectorAll('.js-open')[2]; b.focus(); return document.activeElement !== b; }))
    fail.push('모달: 배경이 비활성(inert)이 아님');
  if (await page.evaluate(() => getComputedStyle(document.body).overflow) !== 'hidden') fail.push('모달: 배경 스크롤이 안 잠김');
  await page.keyboard.press('Escape'); await page.waitForTimeout(300);
  if (await dlg.evaluate(el => el.open)) fail.push('모달: Esc 로 안 닫힘');
  if (!await opener.evaluate(el => el === document.activeElement)) fail.push('모달: 닫은 뒤 포커스가 안 돌아옴');
  await page.close();

  // 토스트 — 쌓임 · 되돌리기 · 호버로 타이머 정지 · 저절로 사라짐
  page = await demo('toast');
  await page.locator('.js-del').first().click(); await page.waitForTimeout(200);
  if (await page.locator('.tst').count() !== 1) fail.push('토스트: 안 떴다');
  await page.locator('.js-del').first().click(); await page.waitForTimeout(200);
  if (await page.locator('.tst').count() !== 2) fail.push('토스트: 두 개가 안 쌓인다');
  await page.locator('.tst .tst__act').first().click(); await page.waitForTimeout(350);
  if (await page.locator('.row').count() !== 4) fail.push('토스트: 되돌리기가 안 먹는다');
  await page.locator('.tst').first().hover();
  const t1 = await page.locator('.tst__timer i').first().evaluate(e => e.getBoundingClientRect().width);
  await page.waitForTimeout(700);
  const t2 = await page.locator('.tst__timer i').first().evaluate(e => e.getBoundingClientRect().width);
  if (Math.abs(t1 - t2) > 2) fail.push('토스트: 올려도 타이머가 안 멈춘다');
  await page.mouse.move(5, 5); await page.waitForTimeout(5600);
  if (await page.locator('.tst').count() !== 0) fail.push('토스트: 저절로 안 사라진다');
  await page.close();

  // 바텀시트 — 아래에 붙고 배경이 잠기는가
  page = await demo('sheet', 420, 760);
  await page.locator('.js-more').first().click(); await page.waitForTimeout(400);
  const sh = await page.locator('dialog.sheet').evaluate(el => {
    const q = el.getBoundingClientRect();
    return { open: el.open, gap: Math.round(innerHeight - q.bottom), radius: getComputedStyle(el).borderBottomLeftRadius };
  });
  if (!sh.open) fail.push('시트: 안 열린다');
  if (sh.gap > 2) fail.push('시트: 아래에 안 붙었다');
  if (sh.radius !== '0px') fail.push('시트: 아래 모서리가 깎여 있다');
  if (await page.evaluate(() => getComputedStyle(document.body).overflow) !== 'hidden') fail.push('시트: 배경 스크롤이 안 잠긴다');
  await page.keyboard.press('Escape'); await page.waitForTimeout(250);
  if (await page.locator('dialog.sheet').evaluate(e => e.open)) fail.push('시트: Esc 로 안 닫힌다');
  await page.close();

  // 드로어 — 옆에 붙고 높이를 다 쓰는가
  page = await demo('drawer', 520, 760);
  await page.locator('#open').click(); await page.waitForTimeout(350);
  const dr = await page.locator('dialog.drw').evaluate(el => {
    const q = el.getBoundingClientRect();
    return { left: Math.round(q.left), full: Math.round(q.height) === Math.round(innerHeight) };
  });
  if (dr.left > 2) fail.push('드로어: 왼쪽에 안 붙었다');
  if (!dr.full) fail.push('드로어: 높이가 화면 전체가 아니다');
  if (await page.locator('#open').getAttribute('aria-expanded') !== 'true') fail.push('드로어: aria-expanded 가 안 바뀐다');
  await page.keyboard.press('Escape'); await page.waitForTimeout(250);
  if (!await page.locator('#open').evaluate(e => e === document.activeElement)) fail.push('드로어: 닫은 뒤 포커스가 안 돌아온다');
  await page.close();

  // 팝오버 — 뒤를 안 막고, 가장자리에서 뒤집히는가
  page = await demo('popover', 900, 620);
  await page.locator('#b1').click(); await page.waitForTimeout(200);
  if (await page.locator('#p1').isHidden()) fail.push('팝오버: 안 열린다');
  if (await page.evaluate(() => document.querySelector('.row').closest('[inert]') !== null)) fail.push('팝오버: 뒤쪽이 막혀 있다');
  await page.locator('#b2').click(); await page.waitForTimeout(200);
  if (await page.locator('#p1').isVisible()) fail.push('팝오버: 다른 것을 열어도 이전 게 안 닫힌다');
  await page.locator('#b3').click(); await page.waitForTimeout(200);
  const r3 = await page.locator('#p3').evaluate(el => ({ right: el.getBoundingClientRect().right, vw: innerWidth }));
  if (r3.right > r3.vw + 1) fail.push('팝오버: 오른쪽 것이 화면 밖으로 나간다');
  await page.keyboard.press('Escape'); await page.waitForTimeout(200);
  if (await page.locator('#p3').isVisible()) fail.push('팝오버: Esc 로 안 닫힌다');
  await page.close();

  // 툴팁 — 지연 · 못 누름 · 키보드
  page = await demo('tooltip', 760, 620);
  await page.locator('.icon-btn').first().hover(); await page.waitForTimeout(150);
  if (await page.locator('#t1').isVisible()) fail.push('툴팁: 지연 없이 바로 뜬다');
  await page.waitForTimeout(400);
  if (await page.locator('#t1').isHidden()) fail.push('툴팁: 머물러도 안 뜬다');
  if (await page.locator('#t1').evaluate(e => getComputedStyle(e).pointerEvents) !== 'none') fail.push('툴팁: 마우스를 받는다 (설명만 해야 한다)');
  await page.mouse.move(2, 2); await page.waitForTimeout(200);
  if (await page.locator('#t1').isVisible()) fail.push('툴팁: 치워도 안 사라진다');
  await page.locator('.icon-btn').nth(1).focus(); await page.waitForTimeout(120);
  if (await page.locator('#t2').isHidden()) fail.push('툴팁: 키보드 포커스로 안 뜬다');
  await page.close();

  // 비모달 다이얼로그 — show() 와 showModal() 이 정말 다른가
  page = await demo('dialog', 900, 700);
  await page.locator('#find').click(); await page.waitForTimeout(250);
  const fd = await page.locator('#finder').evaluate(el => ({ open: el.open, modal: el.matches(':modal') }));
  if (!fd.open) fail.push('다이얼로그: 안 열린다');
  if (fd.modal) fail.push('다이얼로그: show() 인데 모달로 열렸다');
  if (await page.locator('mark').count() < 1) fail.push('다이얼로그: 찾기가 안 된다');
  if (await page.evaluate(() => document.getElementById('p1').closest('[inert]') !== null)) fail.push('다이얼로그: 비모달인데 뒤가 막혔다');
  await page.locator('#conf').click(); await page.waitForTimeout(250);
  if (!await page.locator('#leave').evaluate(el => el.matches(':modal'))) fail.push('다이얼로그: showModal() 인데 모달이 아니다');
  await page.close();

  await browser.close();

  console.log('── 콘솔 에러 ──');
  console.log(errors.length ? errors.join('\n') : '없음');
  console.log('── 검사 ──');
  console.log(fail.length ? fail.map(f => '✗ ' + f).join('\n') : '✓ 전부 통과');
  process.exit(fail.length || errors.length ? 1 : 0);
})();
