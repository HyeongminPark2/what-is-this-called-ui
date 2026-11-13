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
  const PARTS = {
    '6부': ['modal', 'dialog', 'sheet', 'drawer', 'popover', 'tooltip', 'toast'],
    '8부': ['spinner', 'skeleton', 'progress', 'optimistic', 'empty', 'error'],
  };
  const ITEMS = Object.values(PARTS).flat();
  const partOf = s => Object.keys(PARTS).find(k => PARTS[k].includes(s));

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

      // 해부도 번호가 잘리거나 겹치지 않는가
      const nos = [...document.querySelectorAll('.anat .pinno')];
      nos.forEach(n => {
        const q = n.getBoundingClientRect();
        if (q.width < 14 || q.height < 14) bad.push(`해부도 ${n.textContent}번이 찌그러짐 (${Math.round(q.width)}×${Math.round(q.height)})`);
        for (let el = n.parentElement; el && el !== document.body; el = el.parentElement) {
          if (getComputedStyle(el).overflow === 'visible') continue;
          const b2 = el.getBoundingClientRect();
          if (q.left < b2.left - 0.5 || q.top < b2.top - 0.5 || q.right > b2.right + 0.5 || q.bottom > b2.bottom + 0.5) {
            bad.push(`해부도 ${n.textContent}번이 '${(el.className || el.tagName).toString().split(' ')[0]}'에 잘림`);
            break;
          }
        }
      });
      nos.forEach((a, i) => nos.slice(i + 1).forEach(b2 => {
        const q = a.getBoundingClientRect(), w = b2.getBoundingClientRect();
        if (q.right > w.left + 1 && q.left < w.right - 1 && q.bottom > w.top + 1 && q.top < w.bottom - 1) {
          bad.push(`해부도 ${a.textContent}번과 ${b2.textContent}번이 겹침`);
        }
      }));

      // 페이지 안 이동 링크가 실제로 가리키는 곳이 있는가
      document.querySelectorAll('.jump a').forEach(a => {
        if (!document.querySelector(a.getAttribute('href'))) bad.push(`이동 링크가 가리키는 곳 없음: ${a.getAttribute('href')}`);
      });

      const h = document.documentElement.scrollHeight;
      if (h > 12000) bad.push(`페이지가 비정상적으로 김: ${h}px`);
      return bad.slice(0, 5);
    });
    r.forEach(x => fail.push(`${slug}: ${x}`));

    // 형제 링크 = 같은 부의 항목에서 자기만 뺀 것
    const want = PARTS[partOf(slug)].filter(x => x !== slug).map(x => x + '.html').sort();
    const sib = await page.$$eval('.siblings ol:first-of-type a[href$=".html"]',
      as => as.map(a => a.getAttribute('href')).sort());
    if (JSON.stringify(sib) !== JSON.stringify(want)) {
      fail.push(`${slug}: 형제 링크가 [${sib}] (기대 [${want}])`);
    }

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


  // ── 8부 데모 ──
  // 스피너 — 짧은 일에는 안 뜨고, 긴 일에는 뜬다
  page = await demo('spinner');
  await page.locator('[data-ms="180"]').click(); await page.waitForTimeout(260);
  if (await page.locator('.spn').count() !== 0) fail.push('스피너: 0.3초 안에 끝나는데 떴다');
  await page.waitForTimeout(400);
  if (!(await page.locator('#log').textContent()).includes('안 띄웠습니다')) fail.push('스피너: 짧은 경우 기록이 틀리다');
  await page.locator('[data-ms="1400"]').click(); await page.waitForTimeout(500);
  if (await page.locator('.spn').count() !== 1) fail.push('스피너: 긴 일인데 안 떴다');
  await page.waitForTimeout(1600);
  if (await page.locator('.spn').count() !== 0) fail.push('스피너: 끝났는데 안 사라졌다');
  await page.close();

  // 스켈레톤 — 덜컥거림이 0 이고, 스피너로 바꾸면 덜컥거린다
  page = await demo('skeleton');
  await page.locator('#skl').click(); await page.waitForTimeout(300);
  if (await page.locator('.skl').count() < 4) fail.push('스켈레톤: 자리를 안 잡았다');
  await page.waitForTimeout(1600);
  let sh2 = await page.locator('#shift').textContent();
  if (!sh2.includes('덜컥거림 없음')) fail.push(`스켈레톤: 덜컥거렸다 (${sh2.trim()})`);
  await page.locator('#spn').click(); await page.waitForTimeout(1900);
  sh2 = await page.locator('#shift').textContent();
  if (!sh2.includes('px 덜컥거림')) fail.push('스피너 비교: 덜컥거림이 안 잡혔다');
  await page.close();

  // 프로그레스 — 결정형 → 비결정형 → 실패 후 다시 시도
  page = await demo('progress', 900, 820);
  await page.locator('#go').click(); await page.waitForTimeout(700);
  const pv = await page.locator('.prg').first().getAttribute('aria-valuenow');
  if (!pv || +pv <= 0) fail.push('프로그레스: 퍼센트가 안 올라간다');
  await page.waitForTimeout(1800);
  if (await page.locator('.prg--ind').count() !== 1) fail.push('프로그레스: 비결정형으로 안 바뀐다');
  if (await page.locator('.prg--ind').getAttribute('aria-valuenow') !== null) fail.push('프로그레스: 비결정형인데 값이 남아 있다');
  if (await page.locator('.prg--err').count() !== 1) fail.push('프로그레스: 실패한 것이 빨개지지 않는다');
  if (await page.locator('.st.no .ui-btn').count() !== 1) fail.push('프로그레스: 실패 자리에 다시 시도가 없다');
  await page.waitForTimeout(2400);
  if (await page.locator('.st.ok').count() !== 2) fail.push('프로그레스: 성공 표시가 둘이 아니다');
  await page.close();

  // 낙관적 UI — 기다리지 않고 바뀌고, 거절당하면 되돌아간다
  page = await demo('optimistic');
  const star = page.locator('.star').first();
  await star.click(); await page.waitForTimeout(60);
  if (await star.getAttribute('aria-pressed') !== 'true') fail.push('낙관적: 즉시 안 바뀐다');
  if (await page.locator('.spn').count() !== 0) fail.push('낙관적: 스피너가 떴다 (기다림이 보이면 안 된다)');
  const badStar = page.locator('.star[data-fail]');
  await badStar.click(); await page.waitForTimeout(60);
  if (await badStar.getAttribute('aria-pressed') !== 'true') fail.push('낙관적: 실패할 것도 일단 바뀌어야 한다');
  await page.waitForTimeout(900);
  if (await badStar.getAttribute('aria-pressed') !== 'false') fail.push('낙관적: 거절당했는데 안 되돌아간다');
  if (await page.locator('.tst').count() !== 1) fail.push('낙관적: 되돌린 이유를 안 알려 준다');
  await page.close();

  // 빈 상태 — 세 가지가 서로 다른 말을 한다
  page = await demo('empty', 900, 700);
  const says = [];
  for (const k of ['first', 'search', 'cleared']) {
    await page.locator(`.seg2 button[data-k="${k}"]`).click();
    await page.waitForTimeout(150);
    if (await page.locator('.empty h3').count() !== 1) fail.push(`빈 상태(${k}): 제목이 없다`);
    says.push(await page.locator('.empty').textContent());
  }
  if (new Set(says).size !== 3) fail.push('빈 상태: 세 가지가 같은 말을 한다');
  if (!says[0].includes('만들기')) fail.push('빈 상태(처음): 첫 걸음이 없다');
  if (!says[1].includes('조건')) fail.push('빈 상태(검색): 조건을 풀 길이 없다');
  await page.close();

  // 에러 — 네 단계가 각각 다른 자리에 붙는다
  page = await demo('error', 900, 760);
  if (await page.locator('.field-err').count() !== 1) fail.push('에러(칸): 칸 아래 설명이 없다');
  if (await page.locator('#b').getAttribute('aria-invalid') !== 'true') fail.push('에러(칸): aria-invalid 가 없다');
  await page.locator('.seg2 button[data-k="form"]').click(); await page.waitForTimeout(150);
  if (await page.locator('.alert[role="alert"]').count() !== 1) fail.push('에러(폼): 폼 위 경고가 없다');
  await page.locator('.seg2 button[data-k="page"]').click(); await page.waitForTimeout(150);
  if (await page.locator('.err-page .code').count() !== 1) fail.push('에러(화면): 오류 화면이 아니다');
  await page.locator('.seg2 button[data-k="offline"]').click(); await page.waitForTimeout(150);
  if (await page.locator('.offline').count() !== 1) fail.push('에러(연결): 꼭대기 띠가 없다');
  if (await page.locator('.ui-btn[disabled]').count() !== 1) fail.push('에러(연결): 보내기가 비활성이 아니다');
  await page.close();

  await browser.close();

  console.log('── 콘솔 에러 ──');
  console.log(errors.length ? errors.join('\n') : '없음');
  console.log('── 검사 ──');
  console.log(fail.length ? fail.map(f => '✗ ' + f).join('\n') : '✓ 전부 통과');
  process.exit(fail.length || errors.length ? 1 : 0);
})();
