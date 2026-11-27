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
  desc="조사 고르기, 주어 생략, 번역투 걷어내기. 영어 화면을 그대로 옮기면 남는 자국들.",
  lede="영어로 짠 화면을 한국어로 옮기면 <b>자국이 남습니다</b>. 조사와 번역투가 그 대부분입니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이름을 바꿔 쳐 보세요 — <b>받침이 있느냐</b>에 따라 조사가 통째로 바뀝니다.
          영어에는 없는 문제라 번역된 화면에 <b>‘모란상회을(를)’</b> 같은 말이 남습니다.<br>
          <b>조사를 하나로 박아 두기</b>를 켜면 그 꼴이 됩니다. 아래에는 영어를 그대로 옮겼을 때
          남는 말들을 전후로 묶어 두었습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "한국어 UI, 국문 문구, 현지화"),
    ("영어", "Korean UI copy, localization (l10n), internationalization (i18n)"),
    ("같이 쓰는 말",
     "여러 나라 말로 바꿀 수 있게 만드는 일이 <b>국제화</b>(i18n), "
     "실제로 한 나라 말로 옮기는 일이 <b>현지화</b>(l10n)입니다. "
     "문장을 조각내 이어 붙이는 것을 <b>문자열 연결</b>이라 하고, "
     "말마다 어순이 달라 이 방식이 잘 깨집니다."),
    ("자주 잘못 부름",
     "<b>번역</b> — 글을 옮기는 일이고, UI 문구는 <b>다시 쓰는</b> 일에 가깝습니다.<br>"
     "<b>다국어</b> — 말을 여럿 지원하는 것과 한국어를 <b>잘 쓰는</b> 것은 다른 일입니다.<br>"
     "<b>한글</b> — <a href=\"../items/hangul.html\">한글 조판</a>은 <b>글자를 어떻게 흘릴지</b>, 이쪽은 <b>무슨 말을 쓸지</b>입니다."),
  ]),
  axes=ax("한국어 UI"),
  oneline="<b>소리 내어 읽어 보세요.</b> 입으로 안 나오는 말이면 화면에도 쓰지 않습니다.",
  s4_title="자주 남는 자국", s4_hint="영어를 그대로 옮기면",
  states=states([
    (ba('모란상회을(를) 삭제하시겠습니까?', '‘모란상회’를 지울까요?', '받침을 보고 조사를 고른다'),
     "조사", "<b>받침</b>에 따라 을/를·이/가·은/는"),
    (ba('귀하의 계정이 성공적으로 생성되었습니다.', '계정을 만들었습니다.', 'Successfully 를 옮긴 말이다'),
     "‘성공적으로’", "한국어에서는 <b>안 쓰는 말</b>이다"),
    (ba('당신의 설정이 저장되지 않았습니다.', '설정을 저장하지 못했습니다.', 'your 를 옮긴 말이다'),
     "‘당신의’", "한국어는 <b>주어를 생략</b>한다"),
    (ba('이 작업을 수행할 수 없습니다.', '지금은 이 일을 할 수 없습니다.', 'perform 의 번역투'),
     "‘수행’", "<b>쉬운 말</b>로 바꾼다"),
    (ba('삭제하시겠습니까?', '삭제할까요?', '길고 딱딱하다'),
     "‘-하시겠습니까’", "화면에서는 <b>짧은 쪽</b>이 읽힌다"),
    (ba('3 items selected', '3건 선택됨', '복수형을 억지로 옮기지 않는다'),
     "복수형", "한국어에는 <b>복수형이 없다</b>. ‘들’을 붙이지 않는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("받침 있음", "을 · 이 · 은 · 과 · 으로", "마지막 글자에 받침이 있을 때"),
    ("받침 없음", "를 · 가 · 는 · 와 · 로", "없을 때"),
    ("받침 판별", "% 28 ≠ 0", "유니코드로 <b>한 줄이면 된다</b>"),
    ("주어 생략", "‘당신의’를 지운다", "한국어는 <b>주어 없이도</b> 문장이 선다"),
    ("어절", "keep-all", "띄어쓰기에서 줄을 바꾼다 — <a href=\"../items/hangul.html\">한글 조판</a>"),
    ("괄호 조사", "을(를)", "<b>틀리지는 않지만</b> 읽기 나쁘다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>문장을 조각내 이어 붙이면 어순에서 깨집니다.</b>
          <code>'삭제' + name + '하시겠습니까'</code> 같은 식으로 짜면
          영어로 바꿀 때 어순이 맞지 않습니다.
          반대로 영어 틀(<code>'Delete ' + name + '?'</code>)을 그대로 쓰면
          한국어에서 조사가 들어갈 자리가 사라집니다.
          <b>문장 전체를 한 덩어리로 두고 자리만 비워 두는</b> 방식
          (<code>'‘{name}’을(를) 지울까요?'</code>)이
          두 말 모두에서 덜 깨집니다 — 그리고 그 괄호를 없애는 것이
          조사 함수 하나가 하는 일입니다.</p>''',
  do=ul([
    "이름이 들어가는 문장에 <b>조사 함수</b> 쓰기",
    "<b>소리 내어</b> 읽어 보고 안 나오는 말 지우기",
    "문장을 <b>한 덩어리</b>로 두고 자리만 비우기",
  ]),
  dont=ul([
    "‘을(를)’·‘이(가)’ — <b>함수 한 줄이면</b> 없앨 수 있다",
    "‘당신의’·‘귀하의’ — 한국어는 주어를 생략한다",
    "‘~들’로 복수 만들기 — <b>한국어에는 복수형이 없다</b>",
    "문장을 조각내 <b>이어 붙이기</b>",
  ]),
  instead='글자를 어떻게 흘릴지는 <a href="../items/hangul.html">한글 조판</a>, 말투는 <a href="voice.html">말투와 높임</a>, 숫자는 <a href="numbertext.html">숫자와 단위</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>const f = (c.charCodeAt(0)</span>
                <span>&nbsp;&nbsp;- 0xAC00) % 28 !== 0;</span>
                <span style="color:var(--accent)">return f ? '을' : '를';</span>
              </div>''',
     "조사 함수", "<b>세 줄이면 끝난다</b>"),
    (one('‘Starbucks’<b>를</b> 지울까요?', "외래어", False, "받침을 모르니 표를 따로 둔다"),
     "한글이 아닐 때", "소리 나는 대로 판단해야 한다"),
    (one('3건 선택됨', "복수형", True, "‘3개의 항목들이’가 아니다"),
     "건수", "<b>단위 하나</b>로 끝낸다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 말의 계약서",
  code_lede="조사는 <b>받침 하나</b>로 갈립니다.",
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
    ("조사 함수 한 벌", "을/를 · 이/가 · 은/는 · 과/와 · 으로/로. <b>다섯이면 거의 다 덮는다</b>"),
    ("한글이 아니면", "외래어·숫자는 <b>소리</b>로 판단해야 한다. 표를 따로 두거나 괄호로 둔다"),
    ("<code>word-break: keep-all</code>", "어절 안에서 줄이 끊기지 않는다 — <a href=\"../items/hangul.html\">한글 조판</a>"),
    ("문장 전체를 키로", "<code>t('store.delete.confirm', {name})</code>. 조각을 이어 붙이지 않는다"),
    ("스크린 리더", "괄호 조사는 <b>'을괄호를괄호'</b>처럼 읽힌다. 없애는 쪽이 낫다"),
    ("폭", "같은 뜻이라도 한국어가 영어보다 <b>짧거나 길다.</b> 버튼 폭을 두 말로 재 본다"),
  ]),
  backend=rows([
    ("문구를 서버가 완성하지 않는다", "서버가 조사까지 붙여 보내면 <b>말을 바꿀 때마다 배포</b>해야 합니다. 이름만 주고 문장은 화면이 만듭니다."),
    ("정렬은 말에 따라 다르다", "한국어 가나다순은 <b>단순 코드 순서가 아닙니다.</b> <code>localeCompare('ko')</code>를 씁니다."),
    ("검색도 마찬가지", "'모란'으로 '모란상회'를 찾으려면 <b>형태소나 n-gram</b>이 필요합니다 — <a href=\"search.html\">검색</a>."),
    ("문구 키를 쪼개지 않는다", "<code>'delete' + '.' + type</code> 식으로 키를 만들면 <b>어떤 문구가 있는지</b> 아무도 못 셉니다."),
  ]),
  plat_lede="조사 문제는 <b>한국어를 쓰는 모든 곳</b>에 똑같이 있습니다.",
  plats=plats([
    ("웹", "직접 함수로",
     one('‘모란상회’<b>를</b> 지울까요?', "", True, "", "110px"),
     "표준이 없어 <b>직접 만듭니다.</b> 몇 줄이면 되고, 한 번 만들면 계속 씁니다."),
    ("iOS", "Stringsdict",
     '''              <div class="phone" role="img" aria-label="iOS 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">‘모란상회’를<br>지울까요?</div></div></div>''',
     "복수형 규칙은 OS 가 다루지만 <b>조사는 안 다룹니다.</b> 역시 직접 만듭니다."),
    ("안드로이드", "strings.xml",
     '''              <div class="phone" role="img" aria-label="안드로이드 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">‘모란상회’를<br>지울까요?</div></div></div>''',
     "<code>%s</code> 자리만 바꿔 줍니다. 조사는 <b>코드에서</b> 골라 넣어야 합니다."),
  ]),
  plat_note="\"한국어 지원해 주세요\"가 <b>글자를 옮기는 일</b>로만 잡히면 '모란상회을(를)'이 그대로 남습니다. 이름이 들어가는 문구가 몇 개인지 세어 보고 <b>조사 함수 한 벌</b>을 먼저 만들어 두는 것이, 나중에 문구를 하나씩 고치는 것보다 훨씬 쌉니다.",
  siblings=siblings("koreanui"),
  related='''        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="voice.html"><b>말투와 높임</b><em>14부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="../items/truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
