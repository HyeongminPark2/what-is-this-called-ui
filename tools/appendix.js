/* 부록 색인을 항목 카드에서 뽑아 다시 만든다.
   손으로 적어 두면 항목이 늘 때마다 반드시 어긋나므로, 카드가 진짜이고 색인은 그 그림자다.
   쓰는 법:  node tools/appendix.js        (레포 뿌리에서) */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const ITEMS = path.join(ROOT, 'items');

const pick = (html, re) => { const m = html.match(re); return m ? m[1].trim() : ''; };
const strip = s => s.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();

const rows = fs.readdirSync(ITEMS).filter(f => f.endsWith('.html')).map(f => {
  const html = fs.readFileSync(path.join(ITEMS, f), 'utf8');
  const crumb = pick(html, /class="crumb">[\s\S]*?#toc">(\d+부[^<]*)</);
  return {
    slug: f.replace(/\.html$/, ''),
    ko: strip(pick(html, /<h1>([\s\S]*?)<\/h1>/)),
    en: strip(pick(html, /<p class="en">([\s\S]*?)<\/p>/)),
    part: crumb,
    partNo: +(crumb.match(/^(\d+)/) || [0, 0])[1],
    desc: pick(html, /<meta name="description" content="([^"]*)"/)
  };
});

if (rows.some(r => !r.ko || !r.part)) {
  console.error('뽑지 못한 항목이 있다:', rows.filter(r => !r.ko || !r.part).map(r => r.slug));
  process.exit(1);
}

// 가나다순 — localeCompare('ko') 를 쓴다. 코드 순서로 하면 한글이 뒤섞인다
rows.sort((a, b) => a.ko.localeCompare(b.ko, 'ko'));

// 첫 글자를 자모로 — ㄱㄴㄷ 묶음을 만들려고
const CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
             'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];
const DOUBLE = { 'ㄲ': 'ㄱ', 'ㄸ': 'ㄷ', 'ㅃ': 'ㅂ', 'ㅆ': 'ㅅ', 'ㅉ': 'ㅈ' };
function head(ko) {
  const c = ko.charCodeAt(0);
  if (c >= 0xAC00 && c <= 0xD7A3) {
    const ch = CHO[Math.floor((c - 0xAC00) / 588)];
    return DOUBLE[ch] || ch;
  }
  if (/[A-Za-z]/.test(ko[0])) return ko[0].toUpperCase();
  return '#';
}

const groups = [];
rows.forEach(r => {
  const h = head(r.ko);
  let g = groups.find(x => x.h === h);
  if (!g) groups.push(g = { h, items: [] });
  g.items.push(r);
});

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const body = groups.map(g =>
  '    <section class="ix__g">\n' +
  `      <h2 id="g-${encodeURIComponent(g.h)}">${esc(g.h)}</h2>\n` +
  '      <ul class="ix__list">\n' +
  g.items.map(r =>
    `        <li data-slug="${r.slug}" data-ko="${esc(r.ko)}" data-en="${esc(r.en.toLowerCase())}" data-part="${esc(r.part)}">\n` +
    `          <a href="items/${r.slug}.html"><b>${esc(r.ko)}</b><em>${esc(r.en)}</em></a>\n` +
    `          <span class="ix__part">${esc(r.part)}</span>\n` +
    `          <span class="ix__desc">${esc(r.desc)}</span>\n` +
    '        </li>'
  ).join('\n') +
  '\n      </ul>\n    </section>'
).join('\n');

const jump = groups.map(g => `<a href="#g-${encodeURIComponent(g.h)}">${esc(g.h)}</a>`).join('');

const page = `<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>색인 — 이름표</title>
<meta name="description" content="이름표에 실린 ${rows.length}개 항목을 가나다순으로 모은 색인. 한국어 이름과 영어 이름으로 찾을 수 있다.">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/card.css">
<link rel="stylesheet" href="assets/demo.css">
</head>
<body>
<a class="skip" href="#main">본문으로</a>

<header class="topbar">
  <a class="brand" href="index.html">이름표<small>화면 속 그게 뭔지 알려주는 도감</small></a>
  <nav>
    <a href="index.html#map">화면 지도</a>
    <a href="index.html#pairs">혼동 쌍</a>
    <a href="index.html#toc">목차</a>
  </nav>
</header>

<main id="main" class="wrap">
  <div class="card-head">
    <p class="crumb"><a href="index.html">이름표</a> › 색인</p>
    <h1>색인</h1>
    <p class="en">Index</p>
    <p class="lede" style="margin-top:var(--s3)">${rows.length}개 항목을 가나다순으로. <b>이름을 이미 아는 사람</b>을 위한 뒷문입니다 — 이름을 모르면 <a href="index.html#map">화면 지도</a>로 들어가세요.</p>
  </div>

  <div class="ix__bar">
    <label class="sr-only" for="q">색인 검색</label>
    <input id="q" class="ui-input" type="search" placeholder="한국어·영어 이름으로 거르기 — 예: 모달, modal">
    <p class="ruler" id="count" role="status"></p>
  </div>

  <nav class="ix__jump" aria-label="자모로 건너뛰기">${jump}</nav>

  <div class="ix" id="ix">
${body}
  </div>

  <p class="ix__none" id="none" hidden>맞는 항목이 없습니다. <button type="button" class="ui-btn ui-btn--ghost" id="clear">검색어 지우기</button></p>
</main>

<footer class="foot">
  <p><a href="index.html">← 이름표</a> · 직접 그린 재현만 씁니다. 남의 제품 화면 캡처는 쓰지 않습니다.</p>
</footer>

<script>
(function () {
  var q = document.getElementById('q');
  var all = [].slice.call(document.querySelectorAll('.ix__list li'));
  var groups = [].slice.call(document.querySelectorAll('.ix__g'));
  var count = document.getElementById('count');
  var none = document.getElementById('none');

  function run() {
    var t = (q.value || '').trim().toLowerCase();
    var n = 0;
    all.forEach(function (li) {
      var hit = !t ||
        li.dataset.ko.toLowerCase().indexOf(t) >= 0 ||
        li.dataset.en.indexOf(t) >= 0 ||
        li.dataset.part.indexOf(t) >= 0;
      li.hidden = !hit;
      if (hit) n++;
    });
    groups.forEach(function (g) {
      g.hidden = !g.querySelector('li:not([hidden])');
    });
    count.textContent = t ? n + '개' : all.length + '개 항목';
    count.dataset.n = String(n);
    none.hidden = n !== 0;
  }
  q.addEventListener('input', run);
  document.getElementById('clear').addEventListener('click', function () { q.value = ''; run(); q.focus(); });
  run();
})();
</script>
</body>
</html>
`;

fs.writeFileSync(path.join(ROOT, 'appendix.html'), page);
console.log('appendix.html — ' + rows.length + '개 항목, ' + groups.length + '묶음');
