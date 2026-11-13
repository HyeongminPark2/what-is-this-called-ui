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
      mock.querySelectorAll('.pc__menu, .pc__toast, .ph__fab, .ph__sheet, .ph__tabs').forEach(el => {
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

  // ── 2. 항목 카드 ──────────────────────
  page = await browser.newPage({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 1 });
  page.on('console', m => { if (m.type() === 'error') errors.push('[modal] ' + m.text()); });
  page.on('pageerror', e => errors.push('[modal pageerror] ' + e.message));
  await page.goto(url('items/modal.html'));
  await page.waitForTimeout(600);

  // 글자가 세로로 한 줄씩 쌓이는 붕괴를 잡는다 — 좁은데 터무니없이 긴 글 상자
  const squished = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('p, span, li, b, td, figcaption').forEach(el => {
      if (!el.textContent.trim() || el.children.length) return;
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.width < 46 && r.height > 170) {
        bad.push(`${el.tagName.toLowerCase()}.${(el.className||'').toString().slice(0,24)} ${Math.round(r.width)}x${Math.round(r.height)}`);
      }
    });
    return bad.slice(0, 4);
  });
  if (squished.length) fail.push('글이 세로로 쌓임: ' + squished.join(' / '));

  // 그림이 칸보다 넓어 잘리는지
  const clipped = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('.shot').forEach(shot => {
      const sr = shot.getBoundingClientRect();
      shot.querySelectorAll(':scope > *').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.right > sr.right + 1 || r.left < sr.left - 1) {
          bad.push(`${(el.className||'').toString().slice(0,18)} ${Math.round(r.width)}px > 칸 ${Math.round(sr.width)}px`);
        }
      });
    });
    return bad.slice(0, 5);
  });
  if (clipped.length) fail.push('그림이 칸 밖으로 잘림: ' + clipped.join(' / '));

  const pageH = await page.evaluate(() => document.documentElement.scrollHeight);
  if (pageH > 9000) fail.push(`항목 페이지가 비정상적으로 김: ${pageH}px`);

  const slots = await page.locator('section.slot').count();
  if (slots !== 10) fail.push(`카드 칸 ${slots}개 (10 기대)`);

  const pins = await page.locator('.anat [data-pin]').count();
  const pinItems = await page.locator('.pin-list li').count();
  if (pinItems !== 9) fail.push(`해부도 목록 ${pinItems}개 (9 기대)`);
  if (pins !== pinItems) fail.push(`해부도: 그림 번호 ${pins}개 vs 목록 ${pinItems}개 — 안 맞음`);

  // 폭 토글
  const meta = page.locator('[data-meta="modal"]');
  await page.locator('.seg[data-seg="modal"] button[data-w="768"]').click();
  await page.waitForTimeout(450);
  const w768 = await page.locator('.stage iframe').evaluate(el => Math.round(el.getBoundingClientRect().width));
  if (Math.abs(w768 - 768) > 4) fail.push(`폭 토글 768 → 실제 ${w768}px`);
  if (!(await meta.textContent()).includes('768')) fail.push('폭 표시가 768을 안 보여줌');

  await page.locator('.seg[data-seg="modal"] button[data-w="390"]').click();
  await page.waitForTimeout(450);
  const w390 = await page.locator('.stage iframe').evaluate(el => Math.round(el.getBoundingClientRect().width));
  if (Math.abs(w390 - 390) > 4) fail.push(`폭 토글 390 → 실제 ${w390}px`);
  await page.screenshot({ path: '/tmp/uicheck/3-card-390frame.png', fullPage: true });

  // 폰 폭에서 모달이 바텀시트가 되는지
  let fr = page.frameLocator('.stage iframe');
  await fr.locator('.js-open').first().click();
  await page.waitForTimeout(400);
  const sheet = await fr.locator('dialog.mdl').evaluate(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return { bottom: Math.round(innerHeight - r.bottom), radius: cs.borderBottomLeftRadius, w: Math.round(r.width), vw: innerWidth };
  });
  if (sheet.bottom > 2) fail.push(`390px: 모달이 아래에 안 붙음 (아래 여백 ${sheet.bottom}px)`);
  if (sheet.radius !== '0px') fail.push(`390px: 바텀시트인데 아래 모서리가 ${sheet.radius}`);
  await page.screenshot({ path: '/tmp/uicheck/4-bottomsheet.png' });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  if (await fr.locator('dialog.mdl').evaluate(el => el.open)) fail.push('Esc로 안 닫힘');

  // 넓은 폭 — 가운데 뜨는 모달 + 포커스 갇힘 + 포커스 복귀
  await page.locator('.seg[data-seg="modal"] button[data-w="full"]').click();
  await page.waitForTimeout(450);
  fr = page.frameLocator('.stage iframe');
  await fr.locator('.js-open').first().click();
  await page.waitForTimeout(400);
  const centered = await fr.locator('dialog.mdl').evaluate(el => {
    const r = el.getBoundingClientRect();
    return { bottomGap: Math.round(innerHeight - r.bottom), radius: getComputedStyle(el).borderBottomLeftRadius };
  });
  if (centered.bottomGap < 10) fail.push('넓은 폭인데 모달이 아래에 붙어 있음');
  if (centered.radius === '0px') fail.push('넓은 폭인데 아래 모서리가 안 깎임');
  await page.screenshot({ path: '/tmp/uicheck/5-modal-wide.png' });

  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  // ①칸에 '새 탭에서 열기'가 있는지 — iframe에서 못 보는 것을 대신하는 출구
  if (await page.locator('.preview-open').count() !== 1) fail.push('①칸에 새 탭 링크 없음');

  // 카드 자체를 폰 폭에서
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(500);
  const cardScroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  if (cardScroll > 2) fail.push(`항목 카드 390px: 가로 넘침 ${cardScroll}px`);
  await page.screenshot({ path: '/tmp/uicheck/6-card-mobile.png', fullPage: true });

  await page.close();

  // ── 3. 데모 페이지를 직접 열어 포커스 검사 (iframe 밖에서만 유효) ──
  page = await browser.newPage({ viewport: { width: 1100, height: 800 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => errors.push('[demo pageerror] ' + e.message));
  await page.goto(url('demos/modal.html'));
  const opener = page.locator('.js-open').first();
  await opener.click();
  await page.waitForTimeout(350);

  const dlg = page.locator('dialog.mdl');
  if (!await dlg.evaluate(el => el.contains(document.activeElement))) fail.push('열릴 때 포커스가 모달 안으로 안 들어감');

  // 브라우저는 순환 중 문서(body)를 한 칸 거친다. 중요한 건 '배경의 누를 수 있는 것에
  // 포커스가 닿지 않는가'와 '순환이 모달로 돌아오는가'다.
  let landedOnBackground = null, cameBack = false;
  for (let i = 0; i < 14; i++) {
    await page.keyboard.press('Tab');
    const where = await dlg.evaluate(el => {
      const a = document.activeElement;
      if (el.contains(a)) return 'in';
      if (!a || a === document.body || a === document.documentElement) return 'doc';
      return a.tagName.toLowerCase() + '.' + (a.className || '');
    });
    if (where === 'in' && i > 2) cameBack = true;
    if (where !== 'in' && where !== 'doc') landedOnBackground = where;
  }
  if (landedOnBackground) fail.push(`포커스가 배경 요소에 닿음: ${landedOnBackground}`);
  if (!cameBack) fail.push('포커스 순환이 모달로 돌아오지 않음');

  // 배경이 정말 비활성인지 — 프로그램으로 포커스를 줘도 안 받아야 한다
  const inertOk = await page.evaluate(() => {
    const bg = document.querySelectorAll('.js-open')[2];
    bg.focus();
    return document.activeElement !== bg;
  });
  if (!inertOk) fail.push('배경이 비활성(inert)이 아님 — 뒤쪽 버튼에 포커스가 간다');

  // 배경 스크롤이 잠기는지
  if (await page.evaluate(() => getComputedStyle(document.body).overflow) !== 'hidden') fail.push('배경 스크롤이 안 잠김');

  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  if (await dlg.evaluate(el => el.open)) fail.push('데모: Esc로 안 닫힘');
  if (!await opener.evaluate(el => el === document.activeElement)) fail.push('닫은 뒤 포커스가 부른 버튼으로 안 돌아옴');
  if (await page.evaluate(() => getComputedStyle(document.body).overflow) === 'hidden') fail.push('닫았는데 배경 스크롤이 계속 잠김');

  // 배경(백드롭) 클릭으로 닫히는지
  await opener.click();
  await page.waitForTimeout(300);
  await page.mouse.click(8, 8);
  await page.waitForTimeout(300);
  if (await dlg.evaluate(el => el.open)) fail.push('백드롭 클릭으로 안 닫힘');

  await browser.close();

  console.log('── 콘솔 에러 ──');
  console.log(errors.length ? errors.join('\n') : '없음');
  console.log('── 검사 ──');
  console.log(fail.length ? fail.map(f => '✗ ' + f).join('\n') : '✓ 전부 통과');
  process.exit(fail.length || errors.length ? 1 : 0);
})();
