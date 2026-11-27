# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">받침이 있으면 을 · 이 · 은 · 과 · 으로</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">받침이 없으면 를 · 가 · 는 · 와 · 로</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">(code − 0xAC00) % 28 ≠ 0 — 받침이 있다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">주어를 지운다 — ‘당신의 설정’이 아니라 ‘설정’</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">어절은 띄어쓰기로 — word-break: keep-all</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘모란상회을(를)’ — 조사를 하나로 박은 자국</div>
                </div>
              </div>'''

D = dict(
  slug="koreanui", ko="한국어 UI", en="Korean UI copy",
  desc="받침에 맞게 조사를 고르고, 주어를 생략하고, 번역투를 걷어 내는 방법을 다룹니다. 영어 화면을 그대로 옮겼을 때 남는 어색한 표현을 모았습니다.",
  lede="영어로 짠 화면을 한국어로 옮기면 <b>어색한 표현이 남습니다</b>. 대부분은 받침에 맞지 않는 조사와, 영어 문장 구조를 그대로 옮긴 번역투입니다.",
  axes_lede="화면에 적는 문구는 사용자가 <b>무엇을 하면 되는지</b> 알려 주려고 씁니다. 아래 네 가지를 물어보면 문구마다 알려야 할 것과 자주 틀리는 곳, 고치는 기준이 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이름을 바꿔 쳐 보세요. 마지막 글자에 <b>받침이 있는지</b>에 따라 뒤에 붙는 조사가 모두 바뀝니다.
          영어에는 없는 문제라서 번역한 화면에 <b>‘모란상회을(를)’</b> 같은 말이 남습니다.<br>
          <b>조사를 하나로 박아 두기</b>를 켜면 그런 문구가 어떻게 보이는지 볼 수 있습니다. 아래에는 영어를 그대로 옮겼을 때
          남는 말을 고치기 전과 고친 뒤로 나란히 놓았습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "한국어 UI, 국문 문구, 현지화"),
    ("영어", "Korean UI copy, localization (l10n), internationalization (i18n)"),
    ("같이 쓰는 말",
     "여러 나라 말로 바꿀 수 있게 만드는 일이 <b>국제화</b>(i18n)이고, "
     "실제로 한 나라 말로 옮기는 일이 <b>현지화</b>(l10n)입니다. "
     "문장을 조각내 이어 붙이는 것은 <b>문자열 연결</b>이라고 하는데, "
     "언어마다 어순이 달라서 이렇게 만든 문장은 다른 언어로 옮길 때 자주 깨집니다."),
    ("자주 잘못 부르는 이름",
     "<b>번역</b> — 번역은 글을 다른 언어로 옮기는 일이지만, UI 문구를 한국어로 만드는 일은 <b>다시 쓰는</b> 일에 가깝습니다.<br>"
     "<b>다국어</b> — 여러 언어를 지원하는 것과 한국어 문구를 <b>잘 쓰는</b> 것은 서로 다른 일입니다.<br>"
     "<b>한글</b> — <a href=\"../items/hangul.html\">한글 조판</a>은 <b>글자를 어떻게 배치하고 줄을 바꿀지</b>를 다루고, 한국어 UI는 <b>어떤 말을 쓸지</b>를 다룹니다."),
  ]),
  axes=ax("한국어 UI"),
  oneline="<b>문구를 소리 내어 읽어 보세요.</b> 말로 했을 때 어색한 문장이면 화면에도 쓰지 않습니다.",
  s4_title="자주 남는 어색한 표현", s4_hint="영어를 그대로 옮기면",
  states=states([
    (ba('모란상회을(를) 삭제하시겠습니까?', '‘모란상회’를 지울까요?', '받침을 보고 조사를 고른다'),
     "조사", "앞말의 <b>받침</b>에 따라 을/를·이/가·은/는을 골라 붙입니다"),
    (ba('귀하의 계정이 성공적으로 생성되었습니다.', '계정을 만들었습니다.', 'Successfully 를 옮긴 말이다'),
     "‘성공적으로’", "한국어 화면 문구에서는 <b>쓰지 않는 말</b>입니다"),
    (ba('당신의 설정이 저장되지 않았습니다.', '설정을 저장하지 못했습니다.', 'your 를 옮긴 말이다'),
     "‘당신의’", "한국어는 문맥으로 알 수 있으면 <b>주어를 생략</b>합니다"),
    (ba('이 작업을 수행할 수 없습니다.', '지금은 이 일을 할 수 없습니다.', 'perform 의 번역투'),
     "‘수행’", "<b>쉬운 말</b>로 바꿉니다"),
    (ba('삭제하시겠습니까?', '삭제할까요?', '길고 딱딱하다'),
     "‘-하시겠습니까’", "화면에서는 <b>짧은 쪽</b>이 더 잘 읽힙니다"),
    (ba('3 items selected', '3건 선택됨', '복수형을 억지로 옮기지 않는다'),
     "복수형", "한국어에는 <b>복수형이 없으므로</b> ‘들’을 붙이지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("받침 있음", "을 · 이 · 은 · 과 · 으로", "앞말의 마지막 글자에 받침이 있을 때 씁니다"),
    ("받침 없음", "를 · 가 · 는 · 와 · 로", "마지막 글자에 받침이 없을 때 씁니다"),
    ("받침 판별", "% 28 ≠ 0", "유니코드 값으로 계산하면 <b>한 줄로 판별할 수 있습니다</b>"),
    ("주어 생략", "‘당신의’를 지운다", "한국어는 <b>주어 없이도</b> 문장이 성립합니다"),
    ("어절", "keep-all", "어절 중간이 아니라 띄어쓰기 자리에서 줄을 바꿉니다(<a href=\"../items/hangul.html\">한글 조판</a>)"),
    ("괄호 조사", "을(를)", "문법으로는 <b>틀리지 않지만</b> 읽기에 불편합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>문장을 조각내 이어 붙이면 언어마다 다른 어순 때문에 문장이 깨집니다.</b>
          <code>'삭제' + name + '하시겠습니까'</code>처럼 짜 두면
          영어로 바꿀 때 어순이 맞지 않습니다.
          반대로 영어 틀(<code>'Delete ' + name + '?'</code>)을 그대로 쓰면
          한국어에서는 조사가 들어갈 자리가 없습니다.
          <b>문장 전체를 한 덩어리로 두고 이름이 들어갈 자리만 비워 두는</b> 방식
          (<code>'‘{name}’을(를) 지울까요?'</code>)이
          두 언어 모두에서 덜 깨집니다. 이렇게 만든 문장에 남는 '을(를)' 괄호는
          조사 함수 하나로 없앨 수 있습니다.</p>''',
  do=ul([
    "이름이 들어가는 문장에 <b>조사 함수</b> 쓰기",
    "<b>소리 내어</b> 읽어 보고 어색한 말 지우기",
    "문장을 <b>한 덩어리</b>로 두고 자리만 비우기",
  ]),
  dont=ul([
    "‘을(를)’·‘이(가)’를 그대로 둘 때. <b>함수 한 줄이면</b> 없앨 수 있습니다",
    "‘당신의’·‘귀하의’를 붙일 때. 한국어는 주어를 생략합니다",
    "‘~들’을 붙여 복수를 만들 때. <b>한국어에는 복수형이 없습니다</b>",
    "문장을 조각내 <b>이어 붙일 때</b>",
  ]),
  instead='글자를 어떻게 흘릴지는 <a href="../items/hangul.html">한글 조판</a>, 말투는 <a href="voice.html">말투와 높임</a>, 숫자는 <a href="numbertext.html">숫자와 단위</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>const f = (c.charCodeAt(0)</span>
                <span>&nbsp;&nbsp;- 0xAC00) % 28 !== 0;</span>
                <span style="color:var(--accent)">return f ? '을' : '를';</span>
              </div>''',
     "조사 함수", "<b>세 줄로</b> 만들 수 있습니다"),
    (one('‘Starbucks’<b>를</b> 지울까요?', "외래어", False, "받침을 모르니 표를 따로 둔다"),
     "한글이 아닐 때", "받침을 계산할 수 없으므로 읽을 때 나는 소리로 판단해야 합니다"),
    (one('3건 선택됨', "복수형", True, "‘3개의 항목들이’가 아니다"),
     "건수", "‘건’ 같은 <b>단위 하나</b>로 적습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="조사는 앞말에 <b>받침이 있는지</b>만 보면 고를 수 있습니다.",
  code='''<span class="c">// 마지막 글자에 받침이 있나</span>
<span class="k">function</span> hasFinal(word) {
  <span class="k">const</span> c = word[word.length - <span class="a">1</span>].charCodeAt(<span class="a">0</span>);
  <span class="k">if</span> (c &lt; <span class="a">0xAC00</span> || c &gt; <span class="a">0xD7A3</span>) <span class="k">return</span> <span class="k">null</span>;   <span class="c">// 한글이 아니다</span>
  <span class="k">return</span> (c - <span class="a">0xAC00</span>) % <span class="a">28</span> !== <span class="a">0</span>;
}

<span class="k">function</span> josa(word, withFinal, without) {
  <span class="k">const</span> f = hasFinal(word);
  <span class="k">return</span> f === <span class="k">null</span> ? <span class="s">`${</span>withFinal<span class="s">}(${</span>without<span class="s">})`</span> : (f ? withFinal : without);
}

josa(<span class="s">'모란상회'</span>, <span class="s">'을'</span>, <span class="s">'를'</span>);   <span class="c">// '를'</span>
josa(<span class="s">'대림유통'</span>, <span class="s">'을'</span>, <span class="s">'를'</span>);   <span class="c">// '을'</span>

<span class="c">/* 줄은 어절에서 바꾼다 */</span>
<span class="t">body</span> { <span class="a">word-break</span>: keep-all; <span class="a">overflow-wrap</span>: break-word; }''',
  keys=kbd([
    ("조사 함수 한 벌", "을/를 · 이/가 · 은/는 · 과/와 · 으로/로 다섯 쌍이면 화면 문구에 필요한 조사를 <b>거의 다 처리할 수 있습니다</b>"),
    ("한글이 아니면", "외래어나 숫자는 읽을 때 나는 <b>소리</b>로 판단해야 하므로, 표를 따로 두거나 괄호 조사로 둡니다"),
    ("<code>word-break: keep-all</code>", "어절 중간에서 줄이 끊기지 않습니다(<a href=\"../items/hangul.html\">한글 조판</a>)"),
    ("문장 전체를 키로", "<code>t('store.delete.confirm', {name})</code>처럼 문장 전체에 키를 하나 붙이고, 조각을 이어 붙이지 않습니다"),
    ("스크린 리더", "괄호 조사는 <b>'을괄호를괄호'</b>처럼 읽히기 때문에 없애는 편이 낫습니다"),
    ("폭", "같은 뜻이라도 한국어 문구는 영어보다 <b>짧을 때도 길 때도</b> 있으므로, 버튼 폭은 두 언어로 모두 재 봅니다"),
  ]),
  backend=rows([
    ("문구를 서버가 완성하지 않는다", "서버가 조사까지 붙인 문장을 보내면 <b>문구를 바꿀 때마다 서버를 배포</b>해야 합니다. 서버는 이름만 보내고 문장은 화면에서 만듭니다."),
    ("정렬은 말에 따라 다르다", "한국어 가나다순은 <b>단순한 코드 순서와 같지 않으므로</b> <code>localeCompare('ko')</code>로 정렬합니다."),
    ("검색도 마찬가지", "'모란'으로 '모란상회'를 찾으려면 <b>형태소나 n-gram</b> 단위로 찾을 수 있어야 합니다(<a href=\"search.html\">검색</a>)."),
    ("문구 키를 쪼개지 않는다", "<code>'delete' + '.' + type</code>처럼 키를 조합해 만들면 코드에서 키를 검색할 수 없어서 <b>어떤 문구가 있는지</b> 셀 수 없습니다."),
  ]),
  plat_lede="조사 문제는 플랫폼과 상관없이 <b>한국어를 쓰는 모든 화면</b>에서 똑같이 생깁니다.",
  plats=plats([
    ("웹", "직접 함수로",
     one('‘모란상회’<b>를</b> 지울까요?', "", True, "", "110px"),
     "조사를 골라 주는 표준 기능이 없어 <b>직접 만듭니다.</b> 몇 줄이면 되고, 한 번 만들어 두면 계속 쓸 수 있습니다."),
    ("iOS", "Stringsdict",
     '''              <div class="phone" role="img" aria-label="iOS 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">‘모란상회’를<br>지울까요?</div></div></div>''',
     "복수형 규칙은 OS가 처리하지만 <b>조사는 처리하지 않으므로</b> 웹과 마찬가지로 직접 만듭니다."),
    ("안드로이드", "strings.xml",
     '''              <div class="phone" role="img" aria-label="안드로이드 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">‘모란상회’를<br>지울까요?</div></div></div>''',
     "문자열의 <code>%s</code> 자리에 값만 넣어 주기 때문에, 조사는 <b>코드에서</b> 골라 넣어야 합니다."),
  ]),
  plat_note="\"한국어 지원해 주세요\"라는 요청을 <b>글자를 옮기는 일</b>로만 받아들이면 '모란상회을(를)' 같은 문구가 그대로 남습니다. 이름이 들어가는 문구가 몇 개인지 먼저 세어 보고 <b>조사 함수 한 벌</b>을 만들어 두면, 나중에 문구를 하나씩 찾아 고치는 것보다 품이 훨씬 적게 듭니다.",
  siblings=siblings("koreanui"),
  related='''        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="voice.html"><b>말투와 높임</b><em>14부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="../items/truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
