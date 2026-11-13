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
    '12부': ['focus', 'focustrap', 'keyboard', 'name', 'screenreader', 'live', 'contrast', 'semantics'],
    '1부': ['box', 'flex', 'grid', 'center', 'overflow', 'sticky', 'container', 'safearea'],
    '2부': ['color', 'dark', 'typescale', 'spacing', 'elevation', 'zindex'],
    '5부': ['card', 'listitem', 'avatar', 'badge', 'chip', 'stat', 'timeline', 'rating'],
    '6부': ['modal', 'dialog', 'sheet', 'drawer', 'popover', 'tooltip', 'toast'],
    '3부': ['weight', 'lineheight', 'letterspacing', 'hangul', 'numerals', 'truncate', 'webfont', 'hierarchy'],
    '4부': ['field', 'select', 'combobox', 'checkbox', 'radio', 'switch', 'segmented', 'slider'],
    '7부': ['appbar', 'sidebar', 'tabs', 'breadcrumb', 'pagination', 'infinite', 'bottomnav'],
    '8부': ['spinner', 'skeleton', 'progress', 'optimistic', 'empty', 'error'],
    '10부': ['table', 'filter', 'search', 'form', 'validation', 'bulk', 'virtual', 'chart'],
    '9부': ['easing', 'duration', 'enterexit', 'cheap', 'spring', 'stagger', 'gesture', 'reducedmotion'],
    '11부': ['breakpoint', 'touchtarget', 'hover', 'systemback', 'dpr', 'viewport', 'softkeyboard', 'platformdiff'],
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
      // 번호가 자기 부품을 벗어나 다른 줄을 가리키고 있지 않은가.
      // spread() 가 겹침을 피해 아래로 밀면 겹치지도 잘리지도 않은 채 '한 칸 밀린' 번호가 생긴다.
      nos.forEach(n => {
        const t = n.parentElement;
        const q = n.getBoundingClientRect(), tr = t.getBoundingClientRect();
        if (!tr.height) return;
        const cy = q.top + q.height / 2;
        if (cy < tr.top - 10 || cy > tr.bottom + 10) {
          bad.push(`해부도 ${n.textContent}번이 가리키는 것 밖으로 밀림 (번호 ${Math.round(cy)}, 부품 ${Math.round(tr.top)}~${Math.round(tr.bottom)})`);
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


  // ── 4부 데모 ──
  // 텍스트 필드 — 첫 틀린 칸으로 포커스, 고치는 즉시 풀림
  page = await demo('field');
  await page.locator('button[type=submit]').click(); await page.waitForTimeout(200);
  if (await page.locator('.f__err').count() !== 2) fail.push('필드: 에러가 두 개가 아니다');
  if (!await page.locator('#nm').evaluate(e => e === document.activeElement)) fail.push('필드: 첫 틀린 칸으로 포커스가 안 간다');
  if (await page.locator('#nm').getAttribute('aria-invalid') !== 'true') fail.push('필드: aria-invalid 가 없다');
  await page.locator('#nm').fill('홍길동'); await page.waitForTimeout(150);
  if (await page.locator('#nm-e').count() !== 0) fail.push('필드: 고쳐도 에러가 안 풀린다');
  await page.locator('#memo').fill('가'.repeat(12)); await page.waitForTimeout(100);
  if (!(await page.locator('#memo-c').textContent()).startsWith('12')) fail.push('필드: 글자 수가 안 센다');
  await page.close();

  // 셀렉트 — 묶음과 229개
  page = await demo('select');
  if (await page.locator('#bank optgroup').count() !== 2) fail.push('셀렉트: 묶음(optgroup)이 없다');
  if (await page.locator('#city option').count() !== 229) fail.push('셀렉트: 229개가 아니다');
  await page.selectOption('#bank', '하나'); await page.waitForTimeout(120);
  if (!(await page.locator('#out').textContent()).includes('하나')) fail.push('셀렉트: 고른 값이 안 반영된다');
  await page.close();

  // 콤보박스 — 걸러짐, 키보드, 없는 값 허용
  page = await demo('combobox');
  await page.locator('#q').click(); await page.waitForTimeout(150);
  if (await page.locator('#q').getAttribute('aria-expanded') !== 'true') fail.push('콤보박스: aria-expanded 가 없다');
  await page.locator('#q').fill('광화문 7호'); await page.waitForTimeout(200);
  const nOpt = await page.locator('.cb__opt').count();
  if (nOpt === 0 || nOpt > 4) fail.push(`콤보박스: 타이핑으로 안 걸러진다 (${nOpt}개)`);
  if (await page.locator('.cb__opt mark').count() === 0) fail.push('콤보박스: 맞은 글자가 강조되지 않는다');
  await page.keyboard.press('ArrowDown'); await page.keyboard.press('Enter'); await page.waitForTimeout(200);
  if (!(await page.locator('#out').textContent()).includes('광화문 7호')) fail.push('콤보박스: 키보드로 못 고른다');
  await page.locator('#q').fill('없는가게'); await page.waitForTimeout(200);
  await page.keyboard.press('Enter'); await page.waitForTimeout(150);
  if ((await page.locator('#out').textContent()).includes('없는가게')) fail.push('콤보박스: 자유 입력이 꺼졌는데 받아들였다');
  await page.locator('#free').check();
  await page.locator('#q').fill('없는가게'); await page.waitForTimeout(200);
  await page.keyboard.press('Enter'); await page.waitForTimeout(150);
  if (!(await page.locator('#out').textContent()).includes('없는가게')) fail.push('콤보박스: 자유 입력을 켰는데 안 받는다');
  await page.close();

  // 체크박스 — 중간 상태, 비활성 제외
  page = await demo('checkbox');
  if (!await page.locator('#all').evaluate(e => e.indeterminate)) fail.push('체크박스: 중간 상태가 아니다');
  await page.locator('#all').click(); await page.waitForTimeout(150);
  if (await page.locator('.kid:checked').count() !== 4) fail.push('체크박스: 전체 선택이 전부를 안 켠다');
  await page.locator('#all').click(); await page.waitForTimeout(150);
  if (await page.locator('.kid:checked').count() !== 1) fail.push('체크박스: 비활성 항목까지 껐다');
  await page.locator('button[type=submit]').click(); await page.waitForTimeout(150);
  if (await page.locator('#err').isHidden()) fail.push('체크박스: 필수 동의 검사가 안 된다');
  await page.close();

  // 라디오 — 하나만, 화살표 이동
  page = await demo('radio');
  await page.locator('button[type=submit]').click(); await page.waitForTimeout(150);
  if (await page.locator('#err').isHidden()) fail.push('라디오: 안 고르고 저장했는데 안 막는다');
  await page.locator('[name=cycle]').first().check(); await page.waitForTimeout(100);
  await page.keyboard.press('ArrowDown'); await page.waitForTimeout(150);
  if (await page.locator('[name=cycle]:checked').getAttribute('value') !== '주 1회') fail.push('라디오: 화살표로 안 옮겨진다');
  if (await page.locator('[name=cycle]:checked').count() !== 1) fail.push('라디오: 둘 이상 골라진다');
  await page.close();

  // 스위치 — 즉시 적용 + 되돌림
  page = await demo('switch');
  await page.locator('#s2').click(); await page.waitForTimeout(80);
  if (await page.locator('#s2').getAttribute('aria-checked') !== 'true') fail.push('스위치: 즉시 안 바뀐다');
  if ((await page.locator('[data-for=s2]').textContent()) !== '켬') fail.push('스위치: 글자 표시가 안 따라간다');
  await page.locator('#s3').click(); await page.waitForTimeout(900);
  if (await page.locator('#s3').getAttribute('aria-checked') !== 'false') fail.push('스위치: 거절당했는데 안 되돌아간다');
  if (await page.locator('.tst').count() !== 1) fail.push('스위치: 되돌린 이유를 안 알려 준다');
  await page.close();

  // 세그먼티드 — 목록을 거른다 / 탭은 화면을 바꾼다
  page = await demo('segmented');
  if (await page.locator('#rows .row').count() !== 5) fail.push('세그먼티드: 처음 목록이 5줄이 아니다');
  await page.locator('#seg [data-v=계좌]').click(); await page.waitForTimeout(150);
  if (await page.locator('#rows .row').count() !== 2) fail.push('세그먼티드: 걸러지지 않는다');
  await page.locator('#seg [data-v=계좌]').focus();
  await page.keyboard.press('ArrowRight'); await page.waitForTimeout(150);
  if (await page.locator('#seg [data-v=전체]').getAttribute('aria-checked') !== 'true') fail.push('세그먼티드: 화살표로 안 옮겨진다');
  await page.locator('#t2').click(); await page.waitForTimeout(150);
  if (await page.locator('#p1').isVisible() || await page.locator('#p2').isHidden()) fail.push('탭: 화면이 안 바뀐다');
  await page.close();

  // 슬라이더 — 숫자 칸과 양방향, 눈금 붙기
  page = await demo('slider');
  await page.locator('#amt').fill('500000'); await page.waitForTimeout(150);
  if (await page.locator('#amtn').inputValue() !== '500,000') fail.push('슬라이더: 숫자 칸이 안 따라간다');
  await page.locator('#amtn').fill('123456'); await page.waitForTimeout(150);
  if (await page.locator('#amt').inputValue() !== '120000') fail.push('슬라이더: 눈금에 안 붙는다');
  await page.locator('#days').focus();
  const d0 = await page.locator('#days').inputValue();
  await page.keyboard.press('ArrowRight'); await page.waitForTimeout(120);
  if (await page.locator('#days').inputValue() === d0) fail.push('슬라이더: 화살표로 안 움직인다');
  await page.close();


  // ── 7부 데모 ──
  page = await demo('appbar');
  if (await page.locator('#bar').evaluate(e => getComputedStyle(e).position) !== 'sticky') fail.push('앱바: 스티키가 아니다');
  await page.locator('#scroll').evaluate(e => e.scrollTop = 260); await page.waitForTimeout(250);
  if (await page.locator('#bar.is-condensed').count() !== 1) fail.push('앱바: 스크롤해도 안 얇아진다');
  await page.locator('#scroll').evaluate(e => e.scrollTop = 0); await page.waitForTimeout(250);
  if (await page.locator('#bar.is-condensed').count() !== 0) fail.push('앱바: 올라와도 안 돌아간다');
  await page.close();

  page = await demo('sidebar');
  await page.locator('.nav-side a').nth(2).click(); await page.waitForTimeout(150);
  if ((await page.locator('#h').textContent()) !== '정산') fail.push('사이드바: 고른 곳이 안 바뀐다');
  if (await page.locator('.nav-side a[aria-current=page]').count() !== 1) fail.push('사이드바: 현재 위치가 하나가 아니다');
  await page.locator('#rail').click(); await page.waitForTimeout(200);
  if (await page.locator('.nav-side.is-rail').count() !== 1) fail.push('사이드바: 레일로 안 바뀐다');
  if (await page.locator('.nav-side a').first().getAttribute('title') === null) fail.push('사이드바: 레일인데 이름을 알 길이 없다');
  await page.close();

  page = await demo('tabs');
  if (await page.locator('[role=tab][tabindex="0"]').count() !== 1) fail.push('탭: Tab 으로 닿는 탭이 하나가 아니다');
  await page.locator('#t1').focus();
  await page.keyboard.press('ArrowRight'); await page.waitForTimeout(150);
  if (await page.locator('#t2').getAttribute('aria-selected') !== 'true') fail.push('탭: 화살표로 안 옮겨진다');
  if (await page.locator('[role=tabpanel]:not([hidden])').count() !== 1) fail.push('탭: 보이는 패널이 하나가 아니다');
  await page.close();

  page = await demo('breadcrumb');
  if (await page.locator('#crumb [aria-current=page]').evaluate(e => e.tagName) === 'A') fail.push('브레드크럼: 마지막이 링크다');
  await page.locator('[data-d="7"]').click(); await page.waitForTimeout(150);
  if (await page.locator('#more').count() !== 1) fail.push('브레드크럼: 길어도 안 접힌다');
  const bcBefore = await page.locator('#crumb a').count();
  await page.locator('#more').click(); await page.waitForTimeout(150);
  if (await page.locator('#crumb a').count() <= bcBefore) fail.push('브레드크럼: 펼쳐지지 않는다');
  await page.close();

  page = await demo('pagination');
  if (await page.locator('.row').count() !== 8) fail.push('페이지네이션: 쪽당 줄 수가 다르다');
  if (await page.locator('.nav-page button[disabled]').count() !== 1) fail.push('페이지네이션: 첫 쪽인데 이전이 안 막혔다');
  await page.locator('.nav-page button[data-go="2"]').first().click(); await page.waitForTimeout(200);
  if (await page.locator('.nav-page button[aria-current=page]').textContent() !== '2') fail.push('페이지네이션: 쪽이 안 바뀐다');
  if (!page.url().includes('page=2')) fail.push('페이지네이션: 주소에 쪽이 안 남는다');
  if (await page.locator('.nav-page .gap').count() === 0) fail.push('페이지네이션: 쪽이 많은데 안 접힌다');
  await page.close();

  page = await demo('infinite');
  await page.waitForTimeout(900);
  const inf0 = await page.locator('.row').count();
  if (inf0 !== 8) fail.push(`무한 스크롤: 첫 묶음이 ${inf0}건`);
  await page.locator('#scroll').evaluate(e => e.scrollTop = e.scrollHeight);
  await page.waitForTimeout(1100);
  if (await page.locator('.row').count() <= inf0) fail.push('무한 스크롤: 끝에 닿아도 안 불러온다');
  await page.locator('#manual').check(); await page.waitForTimeout(250);
  if (await page.locator('#moreBtn').count() !== 1) fail.push('무한 스크롤: 더 보기 버튼으로 안 바뀐다');
  await page.close();

  page = await demo('bottomnav', 500, 760);
  if (await page.locator('.nav-bottom a').count() !== 4) fail.push('바텀 탭바: 칸이 4개가 아니다');
  await page.locator('#body').evaluate(e => e.scrollTop = 200); await page.waitForTimeout(150);
  await page.locator('.nav-bottom [data-k=settle]').click(); await page.waitForTimeout(200);
  if (await page.locator('#body').evaluate(e => e.scrollTop) !== 0) fail.push('바텀 탭바: 새 탭이 맨 위에서 안 시작한다');
  await page.locator('.nav-bottom [data-k=tx]').click(); await page.waitForTimeout(250);
  if (await page.locator('#body').evaluate(e => e.scrollTop) !== 200) fail.push('바텀 탭바: 탭마다 스크롤을 안 기억한다');
  await page.locator('.nav-bottom [data-k=tx]').click(); await page.waitForTimeout(600);
  if (await page.locator('#body').evaluate(e => e.scrollTop) > 5) fail.push('바텀 탭바: 같은 탭을 다시 눌러도 맨 위로 안 간다');
  await page.close();

  // 2부 디자인 토큰 데모 여섯 장
  // 색 토큰 — 2단만 갈아 끼우면 3단이 따라온다
  page = await demo('color', 900, 820);
  const accL = await page.locator('#c-acc').evaluate(e => getComputedStyle(e).backgroundColor);
  if (await page.locator('#c-btn').evaluate(e => getComputedStyle(e).backgroundColor) !== accL)
    fail.push('색 토큰: 3단이 2단을 안 따른다');
  if (await page.locator('#v-acc').textContent() !== 'blue-500') fail.push('색 토큰: 밝은 쪽 연결이 blue-500 이 아니다');
  await page.locator('#dark').check(); await page.waitForTimeout(120);
  if (await page.locator('#v-acc').textContent() !== 'blue-300') fail.push('색 토큰: 어두운 쪽에서 연결이 안 바뀐다');
  const accD = await page.locator('#c-acc').evaluate(e => getComputedStyle(e).backgroundColor);
  if (accD === accL) fail.push('색 토큰: 2단 색이 그대로다');
  if (await page.locator('#c-btn').evaluate(e => getComputedStyle(e).backgroundColor) !== accD)
    fail.push('색 토큰: 3단을 안 건드렸는데 따라오지 않는다');
  if (await page.locator('.tok .tok__val').first().textContent() !== '#2f6df6') fail.push('색 토큰: 1단 원시 값이 바뀌었다');
  await page.close();

  // 다크 모드 — 토큰을 쓴 것만 따라오고, 대비비를 다시 잰다
  page = await demo('dark', 900, 900);
  const bgL = await page.locator('#fake').evaluate(e => getComputedStyle(e).backgroundColor);
  const hardL = await page.locator('#fake .hard').evaluate(e => getComputedStyle(e).backgroundColor);
  if (await page.locator('#toggle').getAttribute('aria-pressed') !== 'false') fail.push('다크 모드: aria-pressed 초기값이 false 가 아니다');
  await page.locator('#toggle').click();
  await page.waitForTimeout(300);          // 바탕색에 transition 이 걸려 있다 — 다 바뀐 뒤에 읽는다
  if (await page.locator('#toggle').getAttribute('aria-pressed') !== 'true') fail.push('다크 모드: aria-pressed 가 안 바뀐다');
  if (await page.locator('#fake').evaluate(e => getComputedStyle(e).backgroundColor) === bgL)
    fail.push('다크 모드: 토큰을 쓴 바탕이 안 어두워진다');
  if (await page.locator('#fake .hard').evaluate(e => getComputedStyle(e).backgroundColor) !== hardL)
    fail.push('다크 모드: 색을 박아 둔 카드가 따라왔다 (보여주려는 실패가 사라졌다)');
  const ratio = parseFloat(await page.locator('#r1').textContent());
  if (!(ratio >= 4.5)) fail.push(`다크 모드: 어두운 쪽 본문 대비비가 AA 미달 (${ratio})`);
  if (await page.locator('#s1').textContent() !== '통과') fail.push('다크 모드: 대비 판정이 통과로 안 뜬다');
  await page.close();

  // 타입 스케일 — 이웃한 단의 비가 일정하고, 규칙을 끄면 들쭉날쭉해진다
  page = await demo('typescale', 900, 760);
  const sizesOf = () => page.$$eval('.scale-row .sample', els => els.map(e => parseFloat(getComputedStyle(e).fontSize)));
  const sz = await sizesOf();
  if (sz.length !== 7) fail.push(`타입 스케일: 단이 ${sz.length}개 (7 기대)`);
  if (!sz.every((v, i) => i === 0 || v > sz[i - 1])) fail.push('타입 스케일: 아래로 갈수록 안 커진다');
  if (Math.abs(sz[2] - 16) > 0.5) fail.push(`타입 스케일: 기준이 16px 이 아니다 (${sz[2]})`);
  const rs = sz.slice(1).map((v, i) => v / sz[i]);
  if (!rs.every(r => Math.abs(r - 1.25) < 0.04)) fail.push('타입 스케일: 이웃한 단의 비가 1.25 가 아니다');
  await page.locator('#chaos').check(); await page.waitForTimeout(120);
  const sc = await sizesOf();
  const rr = sc.slice(1).map((v, i) => v / sc[i]);
  if (Math.max(...rr) - Math.min(...rr) < 0.1) fail.push('타입 스케일: 규칙을 꺼도 비가 그대로다 (보여주려는 실패가 안 보인다)');
  if (!await page.locator('#r').isDisabled()) fail.push('타입 스케일: 규칙을 껐는데 비율을 고를 수 있다');
  await page.close();

  // 간격 체계 — 기본은 8의 배수, 눈대중을 켜면 어긋난다
  page = await demo('spacing', 900, 820);
  const padsOf = () => page.$$eval('.sp-card', els => els.map(e => parseFloat(getComputedStyle(e).paddingTop)));
  if (!(await padsOf()).every(v => v % 8 === 0)) fail.push('간격 체계: 기본 여백이 8의 배수가 아니다');
  await page.locator('#grid').check(); await page.waitForTimeout(100);
  if (await page.locator('#demo').evaluate(e => getComputedStyle(e).backgroundImage) === 'none')
    fail.push('간격 체계: 격자가 안 그려진다');
  await page.locator('#odd').check(); await page.waitForTimeout(100);
  if ((await padsOf()).some(v => v % 8 === 0)) fail.push('간격 체계: 눈대중 값인데 8의 배수다');
  if (!(await page.locator('#ruler').textContent()).includes('8의 배수가 아님')) fail.push('간격 체계: 어긋났다고 안 알려 준다');
  await page.close();

  // 고도 — 단이 올라갈수록 번짐이 커진다(진해지는 게 아니다)
  page = await demo('elevation', 900, 700);
  const blur = await page.$$eval('.elev', els => els.map(e => {
    const m = getComputedStyle(e).boxShadow.match(/(-?[\d.]+)px (-?[\d.]+)px ([\d.]+)px/);
    return m ? parseFloat(m[3]) : 0;
  }));
  if (blur.length !== 5) fail.push(`고도: 단이 ${blur.length}개 (5 기대)`);
  if (blur[0] !== 0) fail.push('고도: 0단에 그림자가 있다');
  if (!blur.every((v, i) => i === 0 || v > blur[i - 1])) fail.push(`고도: 단이 올라가는데 번짐이 안 커진다 (${blur.join('/')})`);
  await page.locator('#flat').check(); await page.waitForTimeout(120);
  if (!await page.$$eval('.elev', els => els.every(e => getComputedStyle(e).boxShadow === 'none')))
    fail.push('고도: 테두리로 바꿨는데 그림자가 남아 있다');
  if (!await page.$$eval('.elev', els => els.every(e => parseFloat(getComputedStyle(e).borderTopWidth) > 0)))
    fail.push('고도: 그림자를 껐는데 테두리가 없다');
  await page.close();

  // z-index — 사다리대로 쌓이고, 아무 값이나 쓰면 모달이 가림막에 덮인다
  page = await demo('zindex', 900, 860);
  for (const [sel, want] of [['.z-head', '100'], ['.z-drop', '300'], ['#scrim', '500'], ['#modal', '600'], ['#toast', '800']]) {
    const got = await page.locator(sel).evaluate(e => getComputedStyle(e).zIndex);
    if (got !== want) fail.push(`z-index: ${sel} 가 ${got} (${want} 기대)`);
  }
  const topLayer = sel => page.evaluate(s => {
    const r = document.querySelector(s).getBoundingClientRect();
    const el = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    const l = el && el.closest('.z-layer');
    return l ? l.className : '(없음)';
  }, sel);
  if (!(await topLayer('#modal')).includes('z-modal')) fail.push('z-index: 모달 한가운데를 찍었는데 모달이 안 잡힌다');
  await page.locator('#chaos').check(); await page.waitForTimeout(120);
  if (await page.locator('#toast').evaluate(e => getComputedStyle(e).zIndex) !== '9999')
    fail.push('z-index: 아무 값이나 쓰기에서 9999 가 안 된다');
  if (!(await topLayer('#modal')).includes('z-scrim')) fail.push('z-index: 모달이 가림막에 안 덮인다 (보여주려는 실패가 안 보인다)');
  if (!await page.locator('#b-toast').evaluate(e => e.classList.contains('bad'))) fail.push('z-index: 9999 가 빨갛게 표시되지 않는다');
  await page.close();

  // 5부 표시 부품 데모 여덟 장
  // 카드 — 안의 버튼이 카드 링크를 같이 누르지 않는다
  page = await demo('card', 900, 900);
  if (await page.locator('.ui-card').count() !== 4) fail.push('카드: 넷이 아니다');
  await page.locator('[data-buy="0"]').click(); await page.waitForTimeout(80);
  if (!(await page.textContent('#log')).includes('장바구니')) fail.push('카드: 안의 버튼이 동작하지 않는다');
  if ((await page.textContent('#log')).includes('상세로')) fail.push('카드: 안의 버튼을 눌렀는데 카드까지 열린다');
  await page.locator('.ui-card').first().click(); await page.waitForTimeout(80);
  if (!(await page.textContent('#log')).includes('상세로')) fail.push('카드: 본문을 눌러도 안 열린다');
  await page.locator('#long').check(); await page.waitForTimeout(100);
  const hA = await page.$$eval('.ui-card', els => els.map(e => Math.round(e.getBoundingClientRect().height)));
  if (new Set(hA).size === 1) fail.push('카드: 긴 제목을 섞었는데 높이가 그대로다 (보여주려는 결과)');
  await page.locator('#clip').check(); await page.waitForTimeout(100);
  if (!await page.locator('.ui-card__title').nth(1).evaluate(e => e.scrollWidth > e.clientWidth + 1))
    fail.push('카드: 한 줄로 자르기를 켰는데 안 잘린다');
  const hB = await page.$$eval('.ui-card', els => els.map(e => Math.round(e.getBoundingClientRect().height)));
  if (new Set(hB).size !== 1) fail.push('카드: 자른 뒤에도 높이가 제각각이다');
  await page.close();

  // 리스트 아이템 — 줄 높이가 일정하고 긴 글은 말줄임
  page = await demo('listitem', 900, 820);
  const h2 = await page.locator('.li').first().evaluate(e => e.getBoundingClientRect().height);
  await page.selectOption('#lines', 'three'); await page.waitForTimeout(100);
  if (!(await page.locator('.li').first().evaluate(e => e.getBoundingClientRect().height) > h2))
    fail.push('리스트: 세 줄인데 두 줄보다 안 높다');
  await page.selectOption('#lines', 'two'); await page.waitForTimeout(100);
  if (!await page.locator('.li__t').nth(2).evaluate(e => e.scrollWidth > e.clientWidth + 1))
    fail.push('리스트: 긴 제목이 말줄임되지 않는다 (min-width:0 을 빠뜨렸는지 본다)');
  const lh = await page.$$eval('.li', els => els.map(e => Math.round(e.getBoundingClientRect().height)));
  if (new Set(lh).size !== 1) fail.push('리스트: 줄 높이가 제각각이다');
  await page.locator('#wrap').check(); await page.waitForTimeout(100);
  const lw = await page.$$eval('.li', els => els.map(e => Math.round(e.getBoundingClientRect().height)));
  if (new Set(lw).size === 1) fail.push('리스트: 접기를 켰는데 높이가 그대로다 (보여주려는 결과)');
  await page.close();

  // 아바타 — 사진이 깨지면 이니셜이 드러나고, 넘치면 +N
  page = await demo('avatar', 900, 820);
  if (await page.locator('#photo i').count() !== 1) fail.push('아바타: 처음에 사진이 없다');
  await page.locator('#broken').check(); await page.waitForTimeout(100);
  if (await page.locator('#photo i').count() !== 0) fail.push('아바타: 깨진 상태인데 사진이 남아 있다');
  if ((await page.textContent('#photo')).trim() !== '길동') fail.push('아바타: 이니셜 바닥이 안 드러난다');
  if (await page.locator('#stack .av').count() !== 3) fail.push('아바타: 세 명인데 그림이 셋이 아니다');
  await page.locator('#n').fill('9'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(100);
  if (await page.locator('#stack .av').count() !== 4) fail.push('아바타: 아홉 명인데 그림이 넷으로 안 줄었다');
  if ((await page.textContent('#stack .more')).trim() !== '+6') fail.push('아바타: 나머지가 +6 이 아니다');
  if (!(await page.getAttribute('#stack', 'aria-label')).includes('참여자 9명'))
    fail.push('아바타: 겹친 무리가 아홉 명으로 안 읽힌다');
  await page.close();

  // 배지 — 99+ 로 줄이고 0이면 사라진다
  page = await demo('badge', 900, 860);
  if ((await page.textContent('#b-num')).trim() !== '3') fail.push('배지: 3건인데 3이 아니다');
  await page.locator('#n').fill('250'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(100);
  if ((await page.textContent('#b-num')).trim() !== '99+') fail.push('배지: 세 자리인데 99+ 로 안 줄인다');
  if (!(await page.getAttribute('.bdg-anchor', 'aria-label')).includes('250건'))
    fail.push('배지: 읽히는 말에 원래 수가 없다');
  if (await page.locator('#b-num').evaluate(e => e.getBoundingClientRect().width) > 40)
    fail.push('배지: 99+ 인데 배지가 길어졌다');
  await page.locator('#n').fill('0'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(100);
  if (!await page.locator('#b-num').isHidden()) fail.push('배지: 0건인데 안 사라진다 (hidden 이 display 에 졌는지 본다)');
  await page.close();

  // 칩 — 필터는 aria-pressed, 입력 칩은 지운 뒤 포커스가 안 날아간다
  page = await demo('chip', 900, 820);
  if (await page.getAttribute('.chip[data-f=all]', 'aria-pressed') !== 'true') fail.push('칩: 처음에 전체가 안 켜져 있다');
  await page.locator('.chip[data-f=wait]').click(); await page.waitForTimeout(80);
  if (await page.getAttribute('.chip[data-f=wait]', 'aria-pressed') !== 'true') fail.push('칩: 누른 칩이 안 켜진다');
  if (await page.getAttribute('.chip[data-f=all]', 'aria-pressed') !== 'false') fail.push('칩: 먼저 켜진 칩이 안 꺼진다');
  if (!(await page.textContent('#res')).includes('7건')) fail.push('칩: 거른 결과가 안 바뀐다');
  await page.locator('#tags [data-del]').first().click(); await page.waitForTimeout(80);
  if (await page.locator('#tags .chip').count() !== 1) fail.push('칩: × 를 눌러도 안 빠진다');
  const af = await page.evaluate(() => document.activeElement.className + '|' + document.activeElement.id);
  if (!(af.includes('chip__x') || af.includes('tagin'))) fail.push(`칩: 지운 뒤 포커스가 날아갔다 (${af})`);
  await page.fill('#tagin', '이영희'); await page.press('#tagin', 'Enter'); await page.waitForTimeout(80);
  if (await page.locator('#tags .chip').count() !== 2) fail.push('칩: Enter 로 안 들어간다');
  await page.press('#tagin', 'Backspace'); await page.waitForTimeout(80);
  if (await page.locator('#tags .chip').count() !== 1) fail.push('칩: 빈 칸에서 Backspace 로 안 빠진다');
  await page.close();

  // 스탯 타일 — 올라가도 나쁜 지표는 색이 뒤집힌다
  page = await demo('stat', 900, 760);
  if (await page.locator('.stat').count() !== 4) fail.push('스탯: 타일이 넷이 아니다');
  if (await page.getAttribute('.stat:nth-child(1)', 'data-tone') !== 'up') fail.push('스탯: 매출 증가가 좋은 쪽이 아니다');
  if (await page.getAttribute('.stat:nth-child(3)', 'data-dir') !== 'up') fail.push('스탯: 환불액 방향이 올라감이 아니다');
  if (await page.getAttribute('.stat:nth-child(3)', 'data-tone') !== 'down')
    fail.push('스탯: 환불액이 올라가는데 색이 안 뒤집혔다 (보여주려는 교훈)');
  if (await page.locator('.stat__spark').count() !== 4) fail.push('스탯: 추세선이 넷이 아니다');
  if (await page.$eval('.stat__value', e => getComputedStyle(e).fontVariantNumeric) !== 'tabular-nums')
    fail.push('스탯: 숫자 자릿수를 안 맞춘다');
  await page.locator('#bare').check(); await page.waitForTimeout(100);
  if (!await page.locator('.stat__delta').first().isHidden()) fail.push('스탯: 숫자만 보기인데 비교가 남아 있다');
  await page.close();

  // 타임라인 — 지금 단계가 하나, 멈추면 그 자리에 이유
  page = await demo('timeline', 900, 760);
  if (await page.locator('.tl > li').count() !== 5) fail.push('타임라인: 단계가 다섯이 아니다');
  if (await page.locator('[aria-current=step]').count() !== 1) fail.push('타임라인: 지금 단계가 하나가 아니다');
  if (await page.getAttribute('[aria-current=step]', 'data-i') !== '2') fail.push('타임라인: 시작 단계가 세 번째가 아니다');
  await page.locator('#next').click(); await page.waitForTimeout(80);
  if (await page.getAttribute('[aria-current=step]', 'data-i') !== '3') fail.push('타임라인: 다음 단계로 안 간다');
  await page.locator('#fail').click(); await page.waitForTimeout(80);
  if (await page.locator('.tl__dot.is-bad').count() !== 1) fail.push('타임라인: 멈춘 자리가 안 빨개진다');
  if (!(await page.textContent('[aria-current=step]')).includes('예금주')) fail.push('타임라인: 멈춘 이유가 그 자리에 없다');
  if (await page.locator('.tl__dot.is-now').count() !== 0) fail.push('타임라인: 멈췄는데 진행 중 표시가 남아 있다');
  await page.close();

  // 별점 — 반올림하지 않고, 입력용은 라디오 그룹
  page = await demo('rating', 900, 860);
  if (await page.textContent('#num') !== '4.3') fail.push('별점: 평균이 4.3 이 아니다');
  const fillW = parseFloat(await page.$eval('#fill', e => e.style.width));
  if (Math.abs(fillW - 86) > 0.2) fail.push(`별점: 4.3 인데 ${fillW}% 를 칠한다 (86% 기대 — 반올림했는지 본다)`);
  if (!(await page.getAttribute('#stars', 'aria-label')).includes('4.3점')) fail.push('별점: 읽기용에 말이 없다');
  if (await page.getAttribute('#input', 'role') !== 'radiogroup') fail.push('별점: 입력용이 라디오 그룹이 아니다');
  await page.locator('#input [data-v="4"]').click(); await page.waitForTimeout(80);
  if (await page.getAttribute('#input [data-v="4"]', 'aria-checked') !== 'true') fail.push('별점: 누른 별이 안 골라진다');
  if (await page.locator('#input button.on').count() !== 4) fail.push('별점: 아래까지 안 칠해진다');
  if (await page.$$eval('#input button', els => els.filter(e => e.tabIndex === 0).length) !== 1)
    fail.push('별점: 탭으로 들어오는 자리가 하나가 아니다(로빙 탭인덱스)');
  await page.press('#input [data-v="4"]', 'ArrowRight'); await page.waitForTimeout(80);
  if (await page.locator('#input button.on').count() !== 5) fail.push('별점: → 로 안 올라간다');
  await page.close();

  // 1부 뼈대 데모 여덟 장
  // 박스 모델 — box-sizing 으로 '적은 값'의 뜻이 바뀐다
  page = await demo('box', 900, 820);
  const W = s2 => page.$eval(s2, e => e.getBoundingClientRect().width);
  if (Math.abs(await W('#bd') - 200) > 1) fail.push('박스 모델: border-box 인데 200px 이 아니다');
  await page.locator('#border-box').uncheck(); await page.waitForTimeout(120);
  if (Math.abs(await W('#bd') - 240) > 1) fail.push('박스 모델: content-box 인데 패딩·테두리가 안 더해진다');
  if (!(await page.textContent('#ruler')).includes('px 큼')) fail.push('박스 모델: 적은 값보다 커졌다고 안 알려 준다');
  await page.locator('#border-box').check();
  await page.locator('#p').fill('32'); await page.dispatchEvent('#p', 'input'); await page.waitForTimeout(120);
  if (Math.abs(await W('#bd') - 200) > 1) fail.push('박스 모델: border-box 인데 패딩을 키우니 바깥이 커졌다');
  if (await W('#ct') > 150) fail.push('박스 모델: 패딩을 키웠는데 내용 칸이 안 줄었다');
  await page.close();

  // 플렉스 — flex:1 과 min-width:0
  page = await demo('flex', 900, 820);
  if (await page.$eval('#lay', e => getComputedStyle(e).display) !== 'flex') fail.push('플렉스: display:flex 가 아니다');
  const mid0 = await page.$eval('#mid', e => e.getBoundingClientRect().width);
  await page.locator('#grow').check(); await page.waitForTimeout(120);
  if (!(await page.$eval('#mid', e => e.getBoundingClientRect().width) > mid0 + 50))
    fail.push('플렉스: flex:1 인데 안 늘어난다');
  await page.locator('#long').check(); await page.waitForTimeout(180);
  if (await page.$eval('#lay', e => e.scrollWidth > e.clientWidth + 2)) fail.push('플렉스: min-width:0 인데 판이 터졌다');
  if (!await page.$eval('#mid', e => e.scrollWidth > e.clientWidth + 1)) fail.push('플렉스: 긴 글이 말줄임되지 않는다');
  await page.selectOption('#dir', 'column'); await page.waitForTimeout(120);
  if (await page.$eval('#lay', e => getComputedStyle(e).flexDirection) !== 'column') fail.push('플렉스: 방향이 안 바뀐다');
  await page.close();

  // 그리드 — 1fr 의 함정과 minmax(0,1fr)
  page = await demo('grid', 900, 820);
  const colw = () => page.$eval('#lay', e => {
    const c = getComputedStyle(e).gridTemplateColumns.split(' ').map(parseFloat).filter(x => !isNaN(x));
    return Math.round(Math.max(...c) - Math.min(...c));
  });
  if (!(await page.$eval('#lay', e => getComputedStyle(e).gridTemplateColumns.split(' ').length) >= 2))
    fail.push('그리드: auto-fit 이 열을 못 만든다');
  await page.selectOption('#mode', 'fixed'); await page.waitForTimeout(120);
  await page.locator('#long').check(); await page.waitForTimeout(180);
  if (!(await colw() > 2)) fail.push('그리드: 1fr 인데 긴 칸이 옆 칸을 안 빼앗는다 (보여주려는 결과)');
  if (!(await page.textContent('#ruler')).includes('어긋났')) fail.push('그리드: 어긋났다고 안 알려 준다');
  await page.locator('#minmax0').check(); await page.waitForTimeout(180);
  if (await colw() !== 0) fail.push('그리드: minmax(0,1fr) 인데 칸이 안 고르다');
  await page.selectOption('#mode', 'side'); await page.waitForTimeout(120);
  if (Math.abs(await page.$eval('#lay > span', e => e.getBoundingClientRect().width) - 240) > 2)
    fail.push('그리드: 고정 사이드바가 240px 이 아니다');
  await page.close();

  // 가운데 맞추기 — 되는 범위가 다르다
  page = await demo('center', 900, 760);
  const centered = () => page.$$eval('.ctr', els => els.filter(c => {
    const box = c.querySelector('.ctr__box').getBoundingClientRect();
    const b = c.querySelector('b').getBoundingClientRect();
    return Math.abs((b.top + b.bottom) / 2 - (box.top + box.bottom) / 2) < 2;
  }).length);
  if (await page.locator('.ctr').count() !== 5) fail.push('가운데: 방법이 다섯이 아니다');
  if (await centered() !== 5) fail.push('가운데: 처음에 다섯 다 맞아 보이지 않는다');
  await page.locator('#two').check(); await page.waitForTimeout(250);
  if (await centered() !== 3) fail.push(`가운데: 두 줄일 때 끝까지 맞는 것이 셋이 아니다 (${await centered()})`);
  if (!(await page.textContent('.ctr--margin .r')).includes('어긋남')) fail.push('가운데: margin:auto 의 세로 어긋남을 안 잡는다');
  await page.close();

  // 넘침 — 네 값과 가로 스크롤 범인
  page = await demo('overflow', 900, 860);
  if (!await page.$eval('.ovf--auto', e => e.scrollHeight > e.clientHeight)) fail.push('넘침: auto 칸이 안 넘친다');
  if (await page.$eval('.ovf--scroll', e => e.scrollHeight > e.clientHeight)) fail.push('넘침: scroll 칸이 넘쳐 버렸다');
  if (await page.$eval('.ovf--scroll', e => getComputedStyle(e).overflow) !== 'scroll') fail.push('넘침: scroll 이 아니다');
  if (!(await page.textContent('#res')).includes('가로 스크롤이 생겼')) fail.push('넘침: 범인이 있는데 안 넘친다 (보여주려는 결과)');
  await page.locator('#fixit').check(); await page.waitForTimeout(180);
  if (!(await page.textContent('#res')).includes('안 넘칩니다')) fail.push('넘침: min-width:0 으로 고쳐도 넘친다');
  await page.close();

  // 스티키 — 굴려도 붙어 있고, 깨뜨리면 사라진다
  page = await demo('sticky', 900, 760);
  if (await page.$eval('#head', e => getComputedStyle(e).position) !== 'sticky') fail.push('스티키: sticky 가 아니다');
  await page.$eval('#stk', e => { e.scrollTop = 120; }); await page.waitForTimeout(180);
  const stkTop = await page.$eval('#stk', e => e.getBoundingClientRect().top);
  if (Math.abs(await page.$eval('#head', e => e.getBoundingClientRect().top) - stkTop) > 2)
    fail.push('스티키: 굴렸는데 머리말이 안 붙어 있다');
  await page.locator('#broken').check(); await page.waitForTimeout(150);
  await page.$eval('#stk', e => { e.scrollTop = 120; }); await page.waitForTimeout(180);
  if (!(await page.$eval('#head', e => e.getBoundingClientRect().top) < stkTop - 50))
    fail.push('스티키: 깨뜨렸는데 머리말이 그대로 붙어 있다 (보여주려는 결과)');
  if (!(await page.textContent('#why')).includes('붙지 않습니다')) fail.push('스티키: 왜 안 되는지 안 알려 준다');
  await page.close();

  // 컨테이너 — 글줄 길이를 재서 알려 준다
  page = await demo('container', 900, 760);
  const innerW = () => page.$eval('#inner', e => e.getBoundingClientRect().width);
  const w0 = await innerW();
  if (!(await page.textContent('#meter')).includes('읽기 좋은 범위')) fail.push('컨테이너: 기본값이 읽기 좋은 폭이 아니다');
  await page.locator('#off').check(); await page.waitForTimeout(180);
  if (!(await innerW() > w0 + 50)) fail.push('컨테이너: 상한을 없앴는데 안 늘어난다');
  if (!(await page.textContent('#meter')).includes('너무 깁니다')) fail.push('컨테이너: 너무 길다고 안 알려 준다');
  if (!await page.isDisabled('#mw')) fail.push('컨테이너: 상한이 없는데 막대가 안 잠긴다');
  await page.close();

  // 세이프 에어리어 — 켜면 안쪽으로 들어온다
  page = await demo('safearea', 900, 820);
  if (!(await page.textContent('#res')).includes('겹칩니다')) fail.push('세이프: 적용 전에 안 겹친다 (보여주려는 결과)');
  const padT = await page.$eval('#top', e => parseFloat(getComputedStyle(e).paddingTop));
  await page.locator('#safeon').check(); await page.waitForTimeout(180);
  if (!(await page.$eval('#top', e => parseFloat(getComputedStyle(e).paddingTop)) > padT + 10))
    fail.push('세이프: 적용해도 상단 바가 안 내려온다');
  if (!(await page.$eval('#bottom', e => parseFloat(getComputedStyle(e).paddingBottom)) > 15))
    fail.push('세이프: 적용해도 탭바가 안 올라온다');
  if (!(await page.textContent('#res')).includes('안전한 자리')) fail.push('세이프: 안전해졌다고 안 알려 준다');
  await page.close();

  // 3부 글자 데모 여덟 장
  // 한글 조판 — keep-all 은 어절을 지키고, break-all 은 쪼갠다
  page = await demo('hangul', 900, 860);
  if (await page.$eval('.kr--keep', e => getComputedStyle(e).wordBreak) !== 'keep-all') fail.push('한글: keep-all 이 아니다');
  await page.locator('#w').fill('150'); await page.dispatchEvent('#w', 'input'); await page.waitForTimeout(300);
  if (!(await page.textContent('#r2')).includes('안 쪼개짐')) fail.push('한글: keep-all 인데 어절이 쪼개진다');
  if (!(await page.textContent('#r3')).includes('군데 쪼개짐')) fail.push('한글: break-all 인데 안 쪼개진다 (보여주려는 결과)');
  if (!(await page.textContent('#r4')).includes('넘침')) fail.push('한글: keep-all 만으로 긴 영문이 안 넘친다 (보여주려는 결과)');
  if (!(await page.textContent('#r5')).includes('안 넘침')) fail.push('한글: overflow-wrap 을 함께 써도 넘친다');
  await page.close();

  // 행간 — 배수라 글자가 커지면 따라 커진다
  page = await demo('lineheight', 900, 760);
  const lhOf = () => page.$eval('#p', e => parseFloat(getComputedStyle(e).lineHeight));
  const lh0 = await lhOf();
  await page.locator('#fs').fill('24'); await page.dispatchEvent('#fs', 'input'); await page.waitForTimeout(150);
  if (!(await lhOf() > lh0 + 5)) fail.push('행간: 배수인데 글자를 키워도 줄 높이가 그대로다');
  await page.locator('#lh').fill('110'); await page.dispatchEvent('#lh', 'input'); await page.waitForTimeout(150);
  if (!(await page.textContent('#meter')).includes('너무 좁습니다')) fail.push('행간: 좁다고 안 알려 준다');
  await page.locator('#lh').fill('175'); await page.dispatchEvent('#lh', 'input'); await page.waitForTimeout(150);
  if (!(await page.textContent('#meter')).includes('본문에 알맞습니다')) fail.push('행간: 본문 범위를 안 알려 준다');
  await page.close();

  // 글자 굵기 — 실제로 다른 단이 몇 개인지 센다
  page = await demo('weight', 900, 760);
  if (await page.locator('.wt-row').count() !== 3) fail.push('굵기: 쓰는 굵기가 셋이 아니다');
  await page.locator('#only3').uncheck(); await page.waitForTimeout(300);
  if (await page.locator('.wt-row').count() !== 9) fail.push('굵기: 전체가 아홉이 아니다');
  if (!/실제로 다른 것은 \d+개/.test(await page.textContent('#note'))) fail.push('굵기: 진짜 단 수를 안 센다');
  await page.close();

  // 숫자 꼴 — 글꼴마다 tabular-nums 가 먹는지 재서 보여 준다
  page = await demo('numerals', 900, 860);
  if (await page.locator('#ftab tbody tr').count() !== 3) fail.push('숫자: 글꼴 셋을 안 잰다');
  const vs = await page.$$eval('#ftab tbody tr td:last-child', els => els.map(e => e.textContent));
  if (!vs.some(v => v.includes('기능 없음'))) fail.push('숫자: 기능 없는 글꼴을 못 가려낸다');
  if (!vs.some(v => v.includes('고름'))) fail.push('숫자: 고른 글꼴을 못 가려낸다');
  await page.selectOption('#font', 'var(--mono)'); await page.waitForTimeout(2600);
  if (!(await page.textContent('#meter')).includes('안 떨립니다')) fail.push('숫자: 등폭 글꼴인데 떨린다');
  await page.close();

  // 자간 — 범위를 판정해 준다
  page = await demo('letterspacing', 900, 760);
  if (!(await page.textContent('#meter')).includes('기본값')) fail.push('자간: 0 을 기본값이라고 안 알려 준다');
  await page.locator('#ls').fill('100'); await page.dispatchEvent('#ls', 'input'); await page.waitForTimeout(150);
  if (!(await page.textContent('#meter')).includes('너무 넓습니다')) fail.push('자간: 넓다고 안 알려 준다');
  if (!(await page.$eval('#body', e => parseFloat(getComputedStyle(e).letterSpacing)) > 0.5)) fail.push('자간: 실제로 안 벌어진다');
  await page.close();

  // 말줄임 — 잘렸는지 재서 알려 준다
  page = await demo('truncate', 900, 820);
  if (!await page.$eval('#one', e => e.scrollWidth > e.clientWidth + 1)) fail.push('말줄임: 한 줄이 안 잘린다');
  if (!await page.getAttribute('#one', 'title')) fail.push('말줄임: 잘린 글에 title 이 없다');
  if (!await page.$eval('#clamp', e => e.scrollHeight > e.clientHeight + 1)) fail.push('말줄임: 여러 줄이 안 잘린다');
  const ch2 = await page.$eval('#clamp', e => e.clientHeight);
  await page.locator('#n').fill('4'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(200);
  if (!(await page.$eval('#clamp', e => e.clientHeight) > ch2)) fail.push('말줄임: 줄 수를 늘려도 안 높아진다');
  await page.close();

  // 웹폰트 — FOIT 와 FOUT 를 둘 다 보여 준다
  page = await demo('webfont', 900, 760);
  await page.locator('#go').click(); await page.waitForTimeout(500);
  if (await page.$eval('#p1', e => getComputedStyle(e).visibility) !== 'hidden') fail.push('웹폰트: FOIT 인데 글이 보인다');
  if (!await page.$eval('#p2', e => getComputedStyle(e).fontFamily.includes('Georgia'))) fail.push('웹폰트: FOUT 인데 대체 글꼴이 아니다');
  await page.waitForTimeout(2400);
  if (await page.$eval('#p1', e => getComputedStyle(e).visibility) !== 'visible') fail.push('웹폰트: 다 받았는데 글이 안 보인다');
  if (!(await page.textContent('#m1')).includes('초')) fail.push('웹폰트: 못 읽은 시간을 안 잰다');
  await page.close();

  // 글자 위계 — 도구를 빼면 층이 줄어든다
  page = await demo('hierarchy', 900, 760);
  const layers = async () => +(await page.textContent('#meter')).match(/구별되는 층 (\d+)/)[1];
  const L0 = await layers();
  if (!(L0 >= 5)) fail.push(`위계: 셋을 다 써도 층이 ${L0}개뿐이다`);
  await page.locator('#color').uncheck(); await page.waitForTimeout(200);
  if (!(await layers() < L0)) fail.push('위계: 색을 꺼도 층이 안 줄어든다');
  await page.locator('#color').check(); await page.locator('#flat').check(); await page.waitForTimeout(200);
  if (await layers() !== 1) fail.push('위계: 전부 같게 했는데 층이 하나가 아니다');
  await page.close();

  // 12부 접근성 데모 여덟 장
  // 포커스 — 테두리를 지우면 안 보인다
  page = await demo('focus', 900, 760);
  await page.locator('.fk').first().focus(); await page.waitForTimeout(120);
  if (!(await page.textContent('#log')).includes('보임')) fail.push('포커스: 기본에서 테두리가 안 보인다');
  await page.selectOption('#ring', 'is-noring'); await page.waitForTimeout(150);
  await page.locator('.fk').nth(1).focus(); await page.waitForTimeout(150);
  if (!(await page.textContent('#log')).includes('안 보임')) fail.push('포커스: outline:none 을 못 잡는다 (보여주려는 결과)');
  if (await page.$eval('.fk--fake', e => e.tabIndex) !== -1) fail.push('포커스: 가짜 버튼이 Tab 에 걸린다');
  if (!await page.$eval('.skip', e => e.getBoundingClientRect().left < -1000)) fail.push('포커스: 건너뛰기 링크가 평소에 보인다');
  await page.locator('.skip').focus(); await page.waitForTimeout(120);
  if (!await page.$eval('.skip', e => e.getBoundingClientRect().left > 0)) fail.push('포커스: 건너뛰기 링크가 포커스에도 안 나타난다');
  await page.close();

  // 포커스 트랩 — showModal 은 가두고 show 는 샌다
  page = await demo('focustrap', 900, 760);
  await page.locator('#open').click(); await page.waitForTimeout(250);
  for (let i = 0; i < 6; i++) { await page.keyboard.press('Tab'); await page.waitForTimeout(60); }
  if ((await page.textContent('#log')).includes('모달 밖')) fail.push('포커스 트랩: showModal 인데 밖으로 샌다');
  await page.locator('#cancel').click(); await page.waitForTimeout(200);
  if (await page.evaluate(() => document.activeElement.id) !== 'open') fail.push('포커스 트랩: 닫은 뒤 부른 버튼으로 안 돌아온다');
  await page.locator('#broken').check();
  await page.locator('#open').click(); await page.waitForTimeout(250);
  for (let i = 0; i < 7; i++) { await page.keyboard.press('Tab'); await page.waitForTimeout(60); }
  if (!(await page.textContent('#log')).includes('모달 밖')) fail.push('포커스 트랩: show() 인데 안 샌다 (보여주려는 결과)');
  await page.close();

  // 키보드 — div 는 Tab 도 Enter 도 안 된다
  page = await demo('keyboard', 900, 760);
  if (await page.$eval('#fake', e => e.tabIndex) !== -1) fail.push('키보드: div+onclick 이 Tab 에 걸린다');
  if (await page.$eval('#half', e => e.tabIndex) !== 0) fail.push('키보드: tabindex 를 줬는데 Tab 이 안 간다');
  await page.locator('#half').focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(180);
  if (!(await page.textContent('#log')).includes('아무 일도 안 일어남'))
    fail.push('키보드: tabindex 만으로 Enter 가 먹는다 (보여주려는 결과)');
  await page.locator('button.kb-fake').focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(180);
  if (!(await page.textContent('#log')).includes('눌림')) fail.push('키보드: 진짜 button 이 Enter 로 안 눌린다');
  await page.close();

  // 이름 — 아이콘만 있으면 이름이 없다
  page = await demo('name', 900, 820);
  const said = await page.$$eval('.said', els => els.map(e => e.textContent));
  if (!said[0].includes('저장')) fail.push('이름: 글자가 이름이 안 된다');
  if (!said[1].includes('이름이 없습니다')) fail.push('이름: 아이콘만인데 이름이 있다고 나온다 (보여주려는 결과)');
  if (!said[2].includes('지우기')) fail.push('이름: aria-label 이 이름이 안 된다');
  if (!said[3].includes('이름이 없습니다')) fail.push('이름: 자리글이 이름으로 잡힌다');
  if (!said[4].includes('계좌번호')) fail.push('이름: label 이 이름이 안 된다');
  await page.close();

  // 스크린 리더 — 상태가 같이 바뀐다
  page = await demo('screenreader', 900, 760);
  if (!(await page.textContent('#tree')).includes('꺼짐')) fail.push('스크린 리더: 처음 상태가 안 나온다');
  await page.locator('#sw').click(); await page.waitForTimeout(180);
  if (await page.getAttribute('#sw', 'aria-checked') !== 'true') fail.push('스크린 리더: aria-checked 가 안 바뀐다');
  if (!(await page.textContent('#tree')).includes('켜짐')) fail.push('스크린 리더: 읽히는 말이 안 바뀐다');
  await page.locator('#more').click(); await page.waitForTimeout(180);
  if (await page.getAttribute('#more', 'aria-expanded') !== 'true') fail.push('스크린 리더: aria-expanded 가 안 바뀐다');
  await page.locator('#strip').check(); await page.waitForTimeout(180);
  if (!(await page.textContent('#tree')).includes('역할·상태 없음')) fail.push('스크린 리더: 빼고 보기가 안 먹는다');
  await page.close();

  // 라이브 리전 — 미리 있는 리전의 내용만 바꾼다
  page = await demo('live', 900, 760);
  if (await page.getAttribute('#r-polite', 'aria-live') !== 'polite') fail.push('라이브: status 리전이 없다');
  if (await page.getAttribute('#r-assertive', 'aria-live') !== 'assertive') fail.push('라이브: alert 리전이 없다');
  await page.locator('[data-go=none]').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#feed')).includes('아무 말도 안 함')) fail.push('라이브: 조용히 바꿔도 뭔가 말한다');
  if (await page.textContent('#r-polite') !== '') fail.push('라이브: 안 알렸는데 리전에 글이 들어갔다');
  await page.locator('[data-go=polite]').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#r-polite')).includes('건입니다')) fail.push('라이브: status 리전이 안 바뀐다');
  await page.locator('[data-go=assertive]').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#feed')).includes('[말을 끊고]')) fail.push('라이브: alert 가 안 끊는다');
  await page.close();

  // 대비비 — 크기에 따라 판정이 갈린다
  page = await demo('contrast', 900, 860);
  const vtxt = await page.textContent('#verdict');
  if (!vtxt.includes('통과')) fail.push('대비비: 큰 글자도 미달이라고 나온다');
  if (!vtxt.includes('미달')) fail.push('대비비: 본문 미달을 안 잡는다 (기준이 다름을 보여주려는 결과)');
  await page.$eval('#fg', e => { e.value = '#14161a'; e.dispatchEvent(new Event('input')); });
  await page.waitForTimeout(180);
  if ((await page.textContent('#verdict')).includes('미달')) fail.push('대비비: 진한 색인데 미달이 남아 있다');
  if (!(await page.textContent('#r4')).includes('미달')) fail.push('대비비: 자리글 회색을 통과로 본다');
  await page.close();

  // 시맨틱 — div 로 바꾸면 구역 목록이 빈다
  page = await demo('semantics', 900, 760);
  if (await page.locator('.land').count() !== 5) fail.push('시맨틱: 구역이 다섯이 아니다');
  if (!(await page.textContent('#tree')).includes('내비게이션')) fail.push('시맨틱: 구역 목록이 안 나온다');
  await page.locator('#div').check(); await page.waitForTimeout(180);
  if (!(await page.textContent('#tree')).includes('구역이 하나도 없습니다'))
    fail.push('시맨틱: div 로 바꿔도 목록이 남아 있다 (보여주려는 결과)');
  await page.close();

  // 10부 데이터 다루는 화면 데모 여덟 장
  // 데이터 테이블 — 정렬·고정 열·줄바꿈
  page = await demo('table', 900, 820);
  if (await page.locator('.dt tbody tr').count() !== 5) fail.push('테이블: 줄이 다섯이 아니다');
  if (await page.getAttribute('.dt th:nth-child(3)', 'aria-sort') !== 'descending')
    fail.push('테이블: 처음 정렬 상태가 aria-sort 로 안 적힌다');
  if (!(await page.textContent('.dt tbody tr:first-child td:first-child')).includes('한빛'))
    fail.push('테이블: 매출 큰 곳이 맨 위가 아니다');
  await page.locator('.sortbtn[data-k=amount]').click(); await page.waitForTimeout(150);
  if (await page.getAttribute('.dt th:nth-child(3)', 'aria-sort') !== 'ascending')
    fail.push('테이블: 다시 눌러도 방향이 안 바뀐다');
  if (!(await page.textContent('#url')).includes('amount')) fail.push('테이블: 정렬이 주소에 안 담긴다');
  if (await page.$eval('.dt tbody td:first-child', e => getComputedStyle(e).position) !== 'sticky')
    fail.push('테이블: 첫 열이 안 고정된다');
  await page.uncheck('#stick'); await page.waitForTimeout(150);
  if (await page.$eval('.dt tbody td:first-child', e => getComputedStyle(e).position) !== 'static')
    fail.push('테이블: 고정을 꺼도 그대로다');
  await page.check('#wrap'); await page.waitForTimeout(150);
  if (await page.$eval('.dt tbody td', e => getComputedStyle(e).whiteSpace) !== 'normal')
    fail.push('테이블: 줄바꿈 허용이 안 먹는다 (보여주려는 결과)');
  await page.close();

  // 필터 — 같은 갈래는 OR, 다른 갈래는 AND
  page = await demo('filter', 900, 820);
  if (await page.locator('.res .r').count() !== 6) fail.push('필터: 조건이 없는데 전부가 아니다');
  await page.locator('#f-status input[value=ok]').check(); await page.waitForTimeout(180);
  if (await page.locator('.res .r').count() !== 3) fail.push('필터: 승인됨 셋이 아니다');
  if (!(await page.textContent('#url')).includes('status=ok')) fail.push('필터: 조건이 주소에 안 담긴다');
  if (await page.locator('#chips .chip').count() !== 1) fail.push('필터: 켠 조건이 칩으로 안 모인다');
  await page.locator('#f-status input[value=wait]').check(); await page.waitForTimeout(180);
  if (await page.locator('.res .r').count() !== 5) fail.push('필터: 같은 갈래가 OR 로 안 더해진다');
  await page.locator('#f-week input[value=w45]').check(); await page.waitForTimeout(180);
  if (await page.locator('.res .r').count() !== 2) fail.push('필터: 다른 갈래가 AND 로 안 좁혀진다');
  await page.locator('#chips .chip').first().click(); await page.waitForTimeout(180);
  if (await page.locator('#chips .chip').count() !== 2) fail.push('필터: 칩을 눌러도 조건이 안 떨어진다');
  await page.close();

  // 검색 — 디바운스와 늦게 온 응답 버리기
  page = await demo('search', 900, 820);
  await page.fill('#q', '모란'); await page.waitForTimeout(700);
  if (!(await page.locator('#list li').count() >= 2)) fail.push('검색: 결과가 안 뜬다');
  if (!(await page.locator('#list mark').count() > 0)) fail.push('검색: 찾은 글자가 강조되지 않는다');
  if (await page.getAttribute('#q', 'aria-expanded') !== 'true') fail.push('검색: 열렸다고 안 알린다');
  const sent1 = +((await page.textContent('#meter')).match(/보낸 요청 (\d+)/) || [0, 0])[1];
  if (sent1 !== 1) fail.push('검색: 디바운스가 켜졌는데 ' + sent1 + '번 보냈다');
  await page.uncheck('#debounce');
  await page.fill('#q', ''); await page.type('#q', '모란', { delay: 40 }); await page.waitForTimeout(900);
  const sent2 = +((await page.textContent('#meter')).match(/보낸 요청 (\d+)/) || [0, 0])[1];
  if (!(sent2 >= 2)) fail.push('검색: 디바운스를 꺼도 한 번만 보낸다 (보여주려는 결과)');
  if (!(await page.textContent('#meter')).includes('버린 응답')) fail.push('검색: 늦은 응답을 안 센다');
  await page.fill('#q', 'zzz'); await page.waitForTimeout(700);
  if (!(await page.textContent('#empty')).includes('없습니다')) fail.push('검색: 빈 결과 안내가 없다');
  await page.close();

  // 폼 — 묶으면 짧아 보이고, 칸이 늘면 완료율이 떨어진다
  page = await demo('form', 900, 820);
  if (await page.locator('.fm fieldset:not([hidden])').count() !== 1) fail.push('폼: 처음에 묶음이 하나가 아니다');
  await page.check('#opt'); await page.waitForTimeout(220);
  if (await page.locator('.fm fieldset:not([hidden])').count() !== 2) fail.push('폼: 선택 묶음이 안 열린다');
  if (!(await page.textContent('#meter')).includes('완료율')) fail.push('폼: 칸이 늘어도 경고가 없다 (보여주려는 결과)');
  await page.check('#flat'); await page.waitForTimeout(220);
  if (await page.$eval('.fm fieldset', e => parseFloat(getComputedStyle(e).borderTopWidth)) !== 0)
    fail.push('폼: 묶음을 풀어도 테두리가 남는다');
  await page.close();

  // 검증 — 떠날 때 검사하고, 틀린 뒤에는 고치는 동안 푼다
  page = await demo('validation', 900, 820);
  await page.fill('#acc', '123'); await page.locator('#email').focus(); await page.waitForTimeout(220);
  if (await page.getAttribute('#acc', 'aria-invalid') !== 'true') fail.push('검증: 칸을 떠나도 검사하지 않는다');
  if (!(await page.textContent('#acc-msg')).includes('10~14자리')) fail.push('검증: 어떻게 고치는지 안 알려 준다');
  await page.fill('#acc', '1234567890'); await page.waitForTimeout(220);
  if (await page.getAttribute('#acc', 'aria-invalid')) fail.push('검증: 고쳤는데도 틀린 채로 남는다');
  await page.selectOption('#when', 'input'); await page.waitForTimeout(180);
  await page.fill('#acc', '12'); await page.waitForTimeout(220);
  if (await page.getAttribute('#acc', 'aria-invalid') !== 'true')
    fail.push('검증: 칠 때마다로 바꿔도 치는 중에 안 빨개진다 (보여주려는 결과)');
  await page.selectOption('#when', 'submit'); await page.waitForTimeout(180);
  await page.fill('#acc', '12');
  await page.locator('.fm button[type=submit]').click(); await page.waitForTimeout(250);
  if (await page.evaluate(() => document.activeElement.id) !== 'acc')
    fail.push('검증: 제출해도 첫 틀린 칸으로 포커스가 안 간다');
  await page.close();

  // 일괄 선택 — 중간 상태와 '이 쪽'·'조건 전체'의 차이
  page = await demo('bulk', 900, 820);
  if (!await page.locator('#bulkbar').isHidden()) fail.push('일괄: 안 골랐는데 막대가 보인다');
  await page.locator('.dt tbody input[data-i="0"]').check(); await page.waitForTimeout(180);
  if (!await page.$eval('#all', e => e.indeterminate)) fail.push('일괄: 일부만 골랐는데 중간 상태가 아니다');
  if (!(await page.textContent('#count')).includes('1건')) fail.push('일괄: 고른 개수가 안 나온다');
  await page.locator('#all').check(); await page.waitForTimeout(180);
  if (await page.locator('.dt tbody tr.is-sel').count() !== 5) fail.push('일괄: 이 쪽이 전부 안 골라진다');
  if (await page.$eval('#all', e => e.indeterminate)) fail.push('일괄: 다 골랐는데 중간 상태가 남는다');
  if (!(await page.textContent('#allhint')).includes('128건 모두')) fail.push('일괄: 조건 전체를 고를 길이 없다');
  await page.locator('#pickall').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#count')).includes('128건')) fail.push('일괄: 조건 전체 128건이 안 잡힌다');
  await page.locator('#approve').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#log')).includes('128건을 승인할까요')) fail.push('일괄: 큰 범위인데 개수를 안 되묻는다');
  await page.close();

  // 가상 스크롤 — 그리는 수는 그대로, 끄면 전부 만들어진다
  page = await demo('virtual', 900, 820);
  const vnodes = () => page.$eval('#sizer', e => e.children.length);
  if (!(await vnodes() < 40)) fail.push('가상: 1만 건인데 떠 있는 요소가 너무 많다');
  await page.$eval('#vs', e => { e.scrollTop = 5000; }); await page.waitForTimeout(250);
  if (!(await vnodes() < 40)) fail.push('가상: 굴리면 요소가 쌓인다');
  if (!(await page.textContent('#sizer')).includes('#9')) fail.push('가상: 굴린 자리의 줄이 안 그려진다');
  await page.locator('#n').fill('1000'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(250);
  await page.check('#off'); await page.waitForTimeout(700);
  if (await vnodes() !== 1000) fail.push('가상: 꺼도 전부 만들어지지 않는다 (보여주려는 결과)');
  if (!(await page.textContent('#meter')).includes('너무 많습니다')) fail.push('가상: 요소가 많다고 경고하지 않는다');
  await page.close();

  // 차트 — 질문이 바뀌면 맞는 그림도 바뀐다
  page = await demo('chart', 900, 820);
  if (await page.locator('.ch').count() !== 4) fail.push('차트: 네 가지를 견주지 않는다');
  if (await page.locator('.ch.is-bad').count() !== 2) fail.push('차트: 비교 질문에서 안 맞는 그림이 둘이 아니다');
  if (!(await page.textContent('.ch:first-child h4')).includes('막대')) fail.push('차트: 비교에 막대가 안 온다');
  await page.selectOption('#q', 'trend'); await page.waitForTimeout(180);
  if (!(await page.textContent('.ch:first-child h4')).includes('꺾은선')) fail.push('차트: 변화에 꺾은선이 안 온다');
  await page.selectOption('#q', 'rel'); await page.waitForTimeout(180);
  if (!(await page.textContent('.ch:first-child h4')).includes('산점도')) fail.push('차트: 관계에 산점도가 안 온다');
  if (await page.locator('.ch.is-bad').count() !== 3) fail.push('차트: 관계 질문에서 안 맞는 그림이 셋이 아니다');
  const pies = await page.$$eval('.ch svg[data-pie]', els => els.map(e => e.getAttribute('preserveAspectRatio')));
  if (pies.some(v => v === 'none')) fail.push('차트: 파이가 찌그러지게 그려진다');
  await page.close();

  // 9부 움직임 데모 여덟 장
  // 이징 — 같은 시간, 다른 곡선
  page = await demo('easing', 900, 820);
  if (await page.locator('.trk__row').count() !== 4) fail.push('이징: 곡선이 넷이 아니다');
  if (!(await page.textContent('#ruler')).includes('600ms')) fail.push('이징: 네 줄이 같은 시간이 아니다');
  if (!(await page.$eval('.trk__row:nth-child(3) .trk__ball', e => getComputedStyle(e).transitionTimingFunction)).includes('cubic-bezier'))
    fail.push('이징: ease-out 줄이 베지에로 안 달린다');
  await page.check('#slow'); await page.waitForTimeout(220);
  if (!(await page.textContent('#ruler')).includes('1200ms')) fail.push('이징: 느리게가 두 배가 아니다');
  await page.locator('.trk__name').nth(0).click(); await page.waitForTimeout(220);
  const easeLin = await page.$eval('#curve .path', e => e.getAttribute('d'));
  await page.locator('.trk__name').nth(2).click(); await page.waitForTimeout(220);
  if (easeLin === await page.$eval('#curve .path', e => e.getAttribute('d')))
    fail.push('이징: 줄을 바꿔도 곡선이 그대로다');
  await page.close();

  // 지속 시간 — 길이만 바꿔도 뜻이 달라진다
  page = await demo('duration', 900, 820);
  if (!(await page.textContent('#verdict')).includes('알맞다')) fail.push('길이: 200ms 를 알맞다고 안 한다');
  await page.locator('#ms').fill('0'); await page.dispatchEvent('#ms', 'input'); await page.waitForTimeout(180);
  if (!(await page.textContent('#verdict')).includes('순간이동')) fail.push('길이: 0ms 를 순간이동이라 안 한다');
  await page.locator('#ms').fill('1000'); await page.dispatchEvent('#ms', 'input'); await page.waitForTimeout(180);
  if (!(await page.textContent('#verdict')).includes('기다리게')) fail.push('길이: 1000ms 를 길다고 안 한다 (보여주려는 결과)');
  await page.locator('#ms').fill('300'); await page.dispatchEvent('#ms', 'input'); await page.waitForTimeout(180);
  if (await page.locator('#tbl tr.now').count() !== 2) fail.push('길이: 지금 길이에 맞는 쓰임이 안 밝아진다');
  await page.close();

  // 진입과 퇴장 — 나가는 쪽이 더 짧다
  page = await demo('enterexit', 900, 820);
  if (!(await page.textContent('#ruler')).includes('더 짧다')) fail.push('진퇴: 나갈 때가 더 짧다고 안 적는다');
  await page.locator('#toggle').click(); await page.waitForTimeout(120);
  if (!(await page.textContent('#log')).includes('260ms')) fail.push('진퇴: 들어올 때가 260ms 가 아니다');
  await page.waitForTimeout(380);
  if (await page.locator('#panel').isHidden()) fail.push('진퇴: 열었는데 안 보인다');
  await page.locator('#toggle').click(); await page.waitForTimeout(120);
  if (!(await page.textContent('#log')).includes('180ms')) fail.push('진퇴: 나갈 때가 180ms 가 아니다');
  await page.waitForTimeout(320);
  if (!await page.locator('#panel').isHidden()) fail.push('진퇴: 다 나갔는데 안 숨는다');
  await page.check('#same'); await page.waitForTimeout(180);
  if (!(await page.textContent('#ruler')).includes('같다')) fail.push('진퇴: 같게 맞춰도 경고가 없다 (보여주려는 결과)');
  await page.close();

  // 무엇을 움직이나 — 배치를 부르는 속성이 실제로 더 비싸다
  page = await demo('cheap', 900, 820);
  if (await page.locator('.cost__row').count() !== 4) fail.push('비용: 네 가지를 안 견준다');
  if (await page.locator('.cost__row.is-bad').count() !== 2) fail.push('비용: 비싼 쪽 표시가 둘이 아니다');
  await page.locator('#run').click(); await page.waitForTimeout(6500);
  const cv = await page.$$eval('.cost__num', els => els.map(e => parseFloat(e.dataset.v || 'NaN')));
  if (!cv.every(v => v > 0)) fail.push('비용: 시간이 안 재어졌다 — ' + JSON.stringify(cv));
  else if (!((cv[2] + cv[3]) / 2 > (cv[0] + cv[1]) / 2))
    fail.push('비용: left · width 가 더 비싸지 않다 (보여주려는 결과) — ' + cv.map(v => v.toFixed(2)).join('/'));
  if (!(await page.textContent('#verdict')).includes('16.7ms')) fail.push('비용: 한 프레임 예산을 안 적는다');
  await page.close();

  // 스프링 — 튕김을 바꾸면 곡선도 말도 바뀐다
  page = await demo('spring', 900, 820);
  if (!(await page.textContent('#ruler')).includes('지나쳤다')) fail.push('스프링: 기본값이 목표를 안 지나친다');
  const sp28 = await page.$eval('#curve .path', e => e.getAttribute('d'));
  await page.locator('#b').fill('0'); await page.dispatchEvent('#b', 'input'); await page.waitForTimeout(220);
  if (!(await page.textContent('#ruler')).includes('지나치지 않는다')) fail.push('스프링: 튕김 0 인데 지나친다고 한다');
  if (sp28 === await page.$eval('#curve .path', e => e.getAttribute('d'))) fail.push('스프링: 튕김을 바꿔도 곡선이 그대로다');
  await page.locator('#b').fill('80'); await page.dispatchEvent('#b', 'input'); await page.waitForTimeout(220);
  if (!(await page.textContent('#ruler')).includes('읽히기 전에')) fail.push('스프링: 튕김이 커도 경고가 없다 (보여주려는 결과)');
  await page.close();

  // 차례로 들어오기 — 간격이 커지면 마지막 줄이 늦어진다
  page = await demo('stagger', 900, 820);
  if (await page.locator('.stg__item').count() !== 8) fail.push('차례로: 여덟 줄이 아니다');
  await page.waitForTimeout(800);
  if (await page.locator('.stg__item.in').count() !== 8) fail.push('차례로: 다 안 들어왔다');
  const dly = await page.$$eval('.stg__item', els => els.map(e => getComputedStyle(e).transitionDelay));
  if (dly[0] === dly[7]) fail.push('차례로: 줄마다 간격이 없다');
  await page.locator('#gap').fill('160'); await page.dispatchEvent('#gap', 'input');
  await page.locator('#n').fill('20'); await page.dispatchEvent('#n', 'input'); await page.waitForTimeout(350);
  if (!(+(await page.getAttribute('#ruler', 'data-last')) > 3000))
    fail.push('차례로: 간격을 키워도 마지막 줄이 안 늦어진다 (보여주려는 결과)');
  if (!(await page.textContent('#ruler')).includes('기다리게')) fail.push('차례로: 길어져도 경고가 없다');
  await page.close();

  // 제스처 — 거리와 속도, 그리고 따라가기
  page = await demo('gesture', 900, 820);
  {
    const bb = await page.locator('#sheet').boundingBox();
    const gx = bb.x + bb.width / 2, gy = bb.y + 16;
    await page.mouse.move(gx, gy); await page.mouse.down();
    for (let i = 1; i <= 6; i++) { await page.mouse.move(gx, gy + i * 5); await page.waitForTimeout(40); }
    await page.mouse.up(); await page.waitForTimeout(380);
    if (!(await page.textContent('#log')).includes('제자리')) fail.push('제스처: 조금 끌었는데 제자리로 안 온다');
    await page.mouse.move(gx, gy); await page.mouse.down();
    for (let i = 1; i <= 10; i++) { await page.mouse.move(gx, gy + i * 11); await page.waitForTimeout(40); }
    await page.mouse.up(); await page.waitForTimeout(380);
    if (!(await page.textContent('#log')).includes('닫음')) fail.push('제스처: 절반을 넘겼는데 안 닫힌다');
    await page.locator('#reset').click(); await page.waitForTimeout(320);
    await page.uncheck('#follow'); await page.waitForTimeout(120);
    await page.mouse.move(gx, gy); await page.mouse.down();
    await page.mouse.move(gx, gy + 40); await page.waitForTimeout(80);
    const midY = await page.$eval('#sheet', e => e.getBoundingClientRect().top);
    const baseY = await page.$eval('#stage', e => e.getBoundingClientRect().bottom - 150);
    if (!(Math.abs(midY - baseY) < 2)) fail.push('제스처: 따라가기를 꺼도 끄는 동안 움직인다 (보여주려는 결과)');
    await page.mouse.up(); await page.waitForTimeout(320);
  }
  await page.close();

  // 모션 줄이기 — 끌 것은 멎고 남길 것은 남는다
  page = await demo('reducedmotion', 900, 820);
  if (await page.locator('.rm').count() !== 6) fail.push('줄이기: 여섯 가지를 안 가른다');
  if (await page.locator('.rm.drop').count() !== 3) fail.push('줄이기: 끄는 것이 셋이 아니다');
  if (await page.locator('.rm.keep').count() !== 3) fail.push('줄이기: 남기는 것이 셋이 아니다');
  await page.check('#rm'); await page.waitForTimeout(450);
  if (await page.$eval('.rm[data-k=mover] .mover', e => getComputedStyle(e).transform) !== 'none')
    fail.push('줄이기: 켜도 가로지르는 이동이 안 멎는다');
  const f1 = await page.$eval('.rm[data-k=fade] .fader', e => +getComputedStyle(e).opacity);
  await page.waitForTimeout(450);
  if (f1 === await page.$eval('.rm[data-k=fade] .fader', e => +getComputedStyle(e).opacity))
    fail.push('줄이기: 투명도 바뀜까지 꺼졌다 (전부 끄면 변화를 못 읽는다)');
  await page.close();

  // 11부 플랫폼 데모 여덟 장
  const setR = async (pg, id, v) => { await pg.locator(id).fill(v); await pg.dispatchEvent(id, 'input'); await pg.waitForTimeout(200); };

  // 브레이크포인트 — 기기 폭으로 끊으면 폰에서 이름이 접힌다
  page = await demo('breakpoint', 980, 860);
  if (await page.getAttribute('#ruler', 'data-cols') !== '1') fail.push('분기점: 390px 에서 한 단이 아니다');
  if (!await page.locator('.stage-w .nav .burger').isVisible()) fail.push('분기점: 좁은데 메뉴가 안 접힌다');
  await setR(page, '#w', '900');
  if (await page.getAttribute('#ruler', 'data-cols') !== '3') fail.push('분기점: 900px 에서 세 단이 아니다');
  if (!await page.locator('.stage-w .nav .item').first().isVisible()) fail.push('분기점: 넓은데 메뉴가 안 펼쳐진다');
  await setR(page, '#w', '390');
  await page.check('#bad'); await page.waitForTimeout(220);
  if (await page.getAttribute('#ruler', 'data-cols') !== '2') fail.push('분기점: 기기 폭 기준인데 390px 이 한 단이다');
  if (!(+(await page.getAttribute('#ruler', 'data-wrapped')) > 0))
    fail.push('분기점: 그 폭에서 가게 이름이 안 접힌다 (보여주려는 결과)');
  await page.close();

  // 터치 타깃 — 보이는 크기는 두고 눌리는 넓이만 키운다
  page = await demo('touchtarget', 980, 860);
  if (await page.getAttribute('#ruler', 'data-bad') !== '3') fail.push('터치: 44px 미달이 셋이 아니다 (보여주려는 결과)');
  await page.check('#pad'); await page.waitForTimeout(280);
  if (await page.getAttribute('#ruler', 'data-bad') !== '0') fail.push('터치: 넓혀도 미달이 남는다');
  {
    const seen = await page.$eval('.tt-wrap .tt', e => e.getBoundingClientRect().width);
    const hit = await page.$eval('.tt-wrap', e => e.getBoundingClientRect().width);
    if (!(seen < hit && hit >= 44)) fail.push(`터치: 보이는 크기 ${seen} / 눌리는 넓이 ${hit} — 따로 놀지 않는다`);
  }
  await page.uncheck('#finger'); await page.waitForTimeout(160);
  if (await page.$eval('.tt-wrap .finger', e => getComputedStyle(e).opacity) !== '0') fail.push('터치: 손가락 원을 못 끈다');
  await page.close();

  // 호버 — 손가락 기기에서는 호버로만 되던 것이 사라진다
  page = await demo('hover', 980, 860);
  if (await page.locator('.hv').count() !== 6) fail.push('호버: 여섯 가지가 아니다');
  await page.check('#nohover'); await page.waitForTimeout(260);
  if (await page.getAttribute('#ruler', 'data-lost') !== '4') fail.push('호버: 사라지는 것이 넷이 아니다 (보여주려는 결과)');
  await page.locator('.hv:not(.fixed)').first().hover(); await page.waitForTimeout(200);
  if (await page.$eval('.hv:not(.fixed) .hidden-bit', e => getComputedStyle(e).opacity) !== '0')
    fail.push('호버: 손가락 기기를 흉내 냈는데 호버가 먹는다');
  if (await page.$eval('.hv.fixed .hidden-bit', e => getComputedStyle(e).opacity) !== '1')
    fail.push('호버: 고친 쪽도 안 보인다');
  await page.close();

  // 시스템 백 — 기록에 안 넣으면 엉뚱한 화면이 사라진다
  page = await demo('systemback', 980, 860);
  if (await page.getAttribute('#histline', 'data-depth') !== '2') fail.push('뒤로: 처음 기록이 둘이 아니다');
  await page.locator('#open').click(); await page.waitForTimeout(180);
  if (await page.getAttribute('#histline', 'data-depth') !== '3') fail.push('뒤로: 기록에 넣었는데 안 쌓인다');
  await page.locator('#back').click(); await page.waitForTimeout(180);
  if (!(await page.textContent('#log')).includes('시트만 닫혔다')) fail.push('뒤로: 시트만 닫히지 않는다');
  if (await page.locator('.layer.l3').count() !== 0) fail.push('뒤로: 시트가 화면에 남아 있다');
  await page.locator('#reset').click(); await page.waitForTimeout(180);
  await page.uncheck('#push'); await page.waitForTimeout(140);
  await page.locator('#open').click(); await page.waitForTimeout(180);
  if (await page.getAttribute('#histline', 'data-depth') !== '2') fail.push('뒤로: 기록에 안 넣었는데 쌓였다');
  await page.locator('#back').click(); await page.waitForTimeout(180);
  if (await page.locator('.layer.l3').count() !== 1)
    fail.push('뒤로: 기록 밖 시트인데 뒤로가 닫아 버린다 (보여주려는 결과)');
  if (!(await page.textContent('#log')).includes('그 아래 화면이 사라졌다')) fail.push('뒤로: 엉뚱한 것이 사라졌다고 안 알린다');
  await page.close();

  // 화면 밀도 — 배율을 올리면 1배짜리 그림이 늘어난다
  page = await demo('dpr', 980, 860);
  if (await page.locator('.dpr').count() !== 5) fail.push('밀도: 다섯 가지가 아니다');
  {
    const w1 = await page.$eval('canvas[data-k=line1]', e => e.width);
    await setR(page, '#r', '3');
    const w3 = await page.$eval('canvas[data-k=line1]', e => e.width);
    if (!(w3 > w1 * 2.5)) fail.push(`밀도: 배율을 올려도 화소 수가 안 는다 (${w1} → ${w3})`);
  }
  if (!(await page.textContent('.dpr[data-k=bitmap1] .num')).includes('늘어남'))
    fail.push('밀도: 1배 그림이 늘어난다고 안 알린다 (보여주려는 결과)');
  if ((await page.textContent('.dpr[data-k=bitmapN] .num')).includes('늘어남'))
    fail.push('밀도: 배율만큼 받은 그림까지 늘어났다고 한다');
  if (!(await page.textContent('.dpr[data-k=hair] .num')).includes('0.33')) fail.push('밀도: 머리카락 선 두께를 안 적는다');
  await page.close();

  // 뷰포트 단위 — 주소창이 있으면 100vh 만 잘린다
  page = await demo('viewport', 980, 860);
  if (!(+(await page.getAttribute('#ruler', 'data-cut')) > 0))
    fail.push('뷰포트: 주소창이 있는데 100vh 가 안 삐져나간다 (보여주려는 결과)');
  {
    const cuts = await page.$$eval('.cap', els => els.map(e => +e.dataset.cut));
    if (!(cuts[0] > 0 && cuts[1] === 0 && cuts[2] === 0)) fail.push('뷰포트: 잘리는 것이 vh 뿐이 아니다 — ' + JSON.stringify(cuts));
  }
  await page.uncheck('#chrome'); await page.waitForTimeout(220);
  if (await page.getAttribute('#ruler', 'data-cut') !== '0') fail.push('뷰포트: 주소창을 숨겨도 잘린다');
  {
    const rows11 = await page.$$eval('#tbl td[data-u]', els => els.map(e => e.textContent));
    if (!(rows11.length === 4 && rows11.every(t => /px$/.test(t)))) fail.push('뷰포트: 네 단위를 못 잰다 — ' + rows11.join('/'));
  }
  if (await page.getAttribute('#tip', 'data-same') !== '1') fail.push('뷰포트: PC 에서 넷이 같다고 안 적는다');
  await page.close();

  // 폰 키보드 — fixed 로 붙인 것은 키보드 뒤에 깔린다
  page = await demo('softkeyboard', 980, 860);
  if (await page.getAttribute('#read', 'data-open') !== '0') fail.push('키보드: 처음부터 올라와 있다');
  await page.locator('#tap').click(); await page.waitForTimeout(220);
  if (await page.getAttribute('#read', 'data-open') !== '1') fail.push('키보드: 눌러도 안 올라온다');
  if (await page.getAttribute('#read', 'data-hidden') !== '1')
    fail.push('키보드: 저장 버튼이 안 가려진다 (보여주려는 결과)');
  if (!(+(await page.getAttribute('#log', 'data-buried')) >= 2)) fail.push('키보드: 아래 입력칸들이 안 가려진다');
  await page.check('#follow'); await page.waitForTimeout(220);
  if (await page.getAttribute('#read', 'data-hidden') !== '0') fail.push('키보드: 따라 올려도 버튼이 가려진다');
  await page.close();

  // 플랫폼 차이 — 질문을 바꾸면 세 곳의 답이 바뀐다
  page = await demo('platformdiff', 980, 860);
  if (await page.locator('.pf').count() !== 3) fail.push('플랫폼: 세 곳을 안 보여 준다');
  if (!(await page.textContent('#q')).includes('어떻게 뒤로 가나')) fail.push('플랫폼: 첫 질문이 다르다');
  {
    const first = await page.textContent('.pf[data-p=ios] .why');
    await page.selectOption('#k', 'alert'); await page.waitForTimeout(220);
    if (!(await page.textContent('.pf[data-p=ios] .why')).includes('취소가 왼쪽')) fail.push('플랫폼: iOS 알림 차례가 틀렸다');
    if (!(await page.textContent('.pf[data-p=android] .why')).includes('오른쪽 아래')) fail.push('플랫폼: 안드로이드 알림 차례가 틀렸다');
    if (first === await page.textContent('.pf[data-p=ios] .why')) fail.push('플랫폼: 질문을 바꿔도 내용이 그대로다');
  }
  await page.close();

  await browser.close();

  console.log('── 콘솔 에러 ──');
  console.log(errors.length ? errors.join('\n') : '없음');
  console.log('── 검사 ──');
  console.log(fail.length ? fail.map(f => '✗ ' + f).join('\n') : '✓ 전부 통과');
  process.exit(fail.length || errors.length ? 1 : 0);
})();
