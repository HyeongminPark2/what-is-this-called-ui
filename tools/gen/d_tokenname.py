# -*- coding: utf-8 -*-
from ax2 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def nm(name, why, level, ok=None, w="150px"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;'
            'border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:6px 8px">'
            '<span style="font-family:var(--mono);font-size:10px;color:var(--fg)">' + name + '</span>'
            '<span style="font-size:9px;color:' + ('var(--danger)' if ok is False else 'var(--fg-muted)') + '">' + why + '</span>'
            '<span style="font-size:8.5px;color:var(--fg-faint)">' + level + '</span></div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--blue-500<span style="color:var(--fg-faint)"> ← 원시 : 값에 붙인 이름</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">--color-text-danger<span style="color:var(--fg-faint)"> ← 의미 : 쓰임에 붙인 이름</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">--btn-bg<span style="color:var(--fg-faint)"> ← 부품 : 한 부품만의 이름</span></div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">화면에서는 <b>의미 층만</b> 쓴다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">--blue 를 어두운 모드에 쓰면 <b>이름이 거짓</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">갈래-쓰임-자리-상태<span style="color:var(--fg-faint)"> ← 이름의 차례</span></div>
                </div>
              </div>'''

D = dict(
  slug="tokenname", ko="토큰 이름 짓기", en="Token naming",
  desc="토큰 이름을 값이 아니라 쓰임으로 짓는 법. 원시·의미·부품 세 층과 이름의 차례.",
  lede="토큰 이름은 <b>값이 아니라 쓰임</b>을 적습니다. <code>--blue</code>는 어두운 모드가 오는 순간 <b>거짓말</b>이 됩니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이름을 <b>규칙 셋으로 매깁니다</b> — ①값이 이름에 박혀 있나
          ②무엇에 쓰는지가 있나 ③어느 층인가. 직접 넣어 보면 그 자리에서 매겨 줍니다.<br>
          '어두운 모드로'를 켜면 <code>--blue</code> 의 실제 값이 나옵니다.
          파랑이라고 적혀 있는데 파랑이 아닙니다 — <b>값을 이름에 박으면</b> 벌어지는 일입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "토큰 이름 짓기, 네이밍 규칙, 토큰 체계"),
    ("영어", "token naming, design token taxonomy"),
    ("같이 쓰는 말",
     "값에 붙인 이름이 <b>원시</b>(primitive · global · core), "
     "쓰임에 붙인 이름이 <b>의미</b>(semantic · alias), "
     "한 부품만 쓰는 이름이 <b>부품</b>(component)입니다. "
     "의미 토큰이 원시를 가리키는 구조를 <b>별칭</b>(alias)이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>변수</b> — CSS 변수는 <b>담는 그릇</b>이고, 토큰은 <b>그 안의 약속</b>입니다. 토큰을 변수로 옮겨 담을 뿐입니다.<br>"
     "<b>테마</b> — 테마는 <b>값 한 벌</b>이고, 이름은 테마가 바뀌어도 그대로여야 합니다.<br>"
     "<b>클래스 이름</b> — BEM 같은 규칙은 <b>마크업</b>의 이름이고 이건 <b>값</b>의 이름입니다."),
  ]),
  axes=ax("토큰 이름 짓기"),
  oneline="<b>이름만 보고 어디에 쓰는지 알 수 있으면 됩니다.</b> 값이 적혀 있으면 이미 틀렸습니다.",
  s4_title="층", s4_hint="이름이 가리키는 것이 다르다",
  states=states([
    (nm("--blue-500", "값에 붙인 이름", "원시", None),
     "원시", "<b>화면에서 직접 쓰지 않는다</b>"),
    (nm("--color-text-danger", "쓰임에 붙인 이름", "의미", True),
     "의미", "<b>여기만</b> 쓴다"),
    (nm("--btn-bg", "한 부품만의 이름", "부품", True),
     "부품", "그 부품이 <b>남다를 때만</b>"),
    (nm("--red", "어디에 쓰는지가 없다", "원시", False),
     "쓰임 없음", "<b>어디에나</b> 쓰이게 된다"),
    (nm("--color-primary", "무엇의 primary 인가", "의미", False),
     "두루뭉술", "글자? 바탕? <b>모른다</b>"),
    (nm("--font-14", "값이 숫자로 박힘", "원시", False),
     "값이 박힘", "16 으로 바꾸면 <b>이름이 거짓</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("원시", "<code>--blue-500</code>", "값에 붙인 이름"),
    ("의미", "<code>--color-text-danger</code>", "<b>쓰임</b>에 붙인 이름"),
    ("부품", "<code>--btn-bg</code>", "한 부품만의 이름"),
    ("쓰는 층", "의미만", "화면 코드에는 <b>의미 층만</b> 나온다"),
    ("거짓 이름", "<code>--blue</code>", "어두운 모드에서 <b>파랑이 아니다</b>"),
    ("차례", "갈래-쓰임-자리-상태", "<code>color-text-danger-hover</code>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          세 층을 두는 이유는 <b>바꿀 자리를 한 곳으로 모으기</b> 위해서입니다.
          브랜드 파랑이 바뀌면 원시 한 줄만 고치면 되고,
          '오류 글자색을 더 진하게'는 의미 한 줄만 고치면 됩니다.<br>
          대신 <b>층을 섞어 쓰면</b> 이 이점이 통째로 사라집니다.
          화면 코드에 <code>--blue-500</code>이 한 번이라도 나오면
          그 자리는 어두운 모드를 따라오지 않습니다.
          규칙은 하나입니다 — <b>화면에서는 의미 층만</b>.</p>''',
  do=ul([
    "이름에 <b>쓰임</b>을 적기 — <code>text</code>·<code>bg</code>·<code>border</code>",
    "차례를 <b>갈래-쓰임-자리-상태</b>로 고정하기",
    "화면 코드에서는 <b>의미 층만</b> 쓰기",
  ]),
  dont=ul([
    "<code>--blue</code>·<code>--red</code> — 어두운 모드에서 <b>이름이 거짓</b>이 된다",
    "<code>--font-14</code> — 값을 바꾸는 순간 <b>이름이 거짓</b>이 된다",
    "<code>--color-primary</code> 하나로 버티기 — <b>글자인지 바탕인지</b> 모른다",
    "부품 토큰을 <b>먼저</b> 만들기 — 의미 층이 비어 버린다",
  ]),
  instead='값 자체는 <a href="color.html">색 토큰</a>, 두 벌로 두는 법은 <a href="dark.html">다크 모드</a>, 크기 단은 <a href="typescale.html">타입 스케일</a>·<a href="spacing.html">간격 체계</a>.',
  cases=cases([
    (nm("--color-bg-surface", "바탕 · 카드 면", "의미", True), "바탕", "쓰임이 분명하다"),
    (nm("--color-border-muted", "테두리 · 흐린 선", "의미", True), "선", "자리까지 적혀 있다"),
    (nm("--space-4", "간격 · 4번째 단", "의미", True), "간격", "값이 아니라 <b>단</b>을 가리킨다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 이름의 계약서",
  code_lede="원시를 깔고, 의미가 그것을 가리키고, 화면은 의미만 씁니다.",
  code='''<span class="c">/* 1층 원시 — 값에 붙인 이름. 화면에서 직접 안 쓴다 */</span>
:root {
  --blue-500: <span class="a">#1f6feb</span>;
  --red-500: <span class="a">#cf222e</span>;
  --gray-200: <span class="a">#e4e6eb</span>;
}

<span class="c">/* 2층 의미 — 쓰임에 붙인 이름. 테마가 바뀌면 여기만 갈아 끼운다 */</span>
:root {
  --color-text-danger: <span class="a">var</span>(--red-500);
  --color-border-muted: <span class="a">var</span>(--gray-200);
}
[data-theme="dark"] {
  --color-text-danger: <span class="a">#ff7b72</span>;   <span class="c">/* 이름은 그대로다 */</span>
}

<span class="c">/* 화면은 의미 층만 쓴다 */</span>
.field-error { <span class="a">color</span>: <span class="a">var</span>(--color-text-danger); }

<span class="c">/* ✕ 어두운 모드를 안 따라온다 */</span>
.field-error { <span class="a">color</span>: <span class="a">var</span>(--red-500); }''',
  keys=kbd([
    ("갈래", "<code>color</code>·<code>space</code>·<code>radius</code>·<code>shadow</code>"),
    ("쓰임", "<code>text</code>·<code>bg</code>·<code>border</code>·<code>icon</code>"),
    ("자리", "<code>danger</code>·<code>muted</code>·<code>brand</code>"),
    ("상태", "<code>hover</code>·<code>active</code>·<code>disabled</code> — <b>맨 뒤</b>"),
    ("찾는 법", "<code>--color-</code> 로 시작하면 <b>자동완성</b>이 묶어 준다"),
    ("확인하는 법", "화면 코드에서 <code>--blue</code>·<code>-500</code> 을 <b>검색</b>해 본다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "토큰은 화면 안의 약속입니다. 다만 <b>이름 짓는 버릇</b>은 그대로 통합니다."),
    ("같은 원리", "<code>status</code> 를 <code>red</code> 가 아니라 <code>failed</code> 로 보내는 것과 같은 이야기입니다 — <b>값이 아니라 뜻</b>을 이름으로 둡니다."),
  ]),
  plat_lede="<b>층을 나누는 생각</b>은 어디서나 같습니다.",
  plats=plats([
    ("웹", "CSS 변수",
     nm("--color-text-danger", "", "의미", True, "110px"),
     "<code>:root</code> 에 깔고 <code>var()</code> 로 씁니다. 테마는 속성 선택자로 갈아 끼웁니다."),
    ("iOS", "Color Set",
     '''              <div class="phone" role="img" aria-label="iOS 색 자산 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:10px;border-radius:3px;background:var(--accent)"></div></div></div>''',
     "자산 묶음에 <b>이름</b>을 두고 밝은·어두운 값을 같이 담습니다 — 구조가 의미 층과 같습니다."),
    ("안드로이드", "Material 역할",
     '''              <div class="phone" role="img" aria-label="안드로이드 색 역할 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:10px;border-radius:3px;background:var(--accent)"></div></div></div>''',
     "<code>primary</code>·<code>onPrimary</code>·<code>surface</code> 처럼 <b>역할 이름</b>이 아예 정해져 있습니다."),
  ]),
  plat_note="Material 의 <b>역할 이름</b>은 의미 층을 OS 가 미리 정해 준 것입니다 — 고민할 거리가 줄지만 그 틀 밖으로 나가기 어렵습니다. 웹은 반대로 <b>전부 직접 지어야</b> 해서 자유롭고 또 쉽게 엉킵니다. 그래서 이름의 차례를 <b>한 줄로 적어 두고</b>(갈래-쓰임-자리-상태) 새 토큰을 만들 때마다 그 줄에 맞춰 보는 것이, 규칙을 길게 쓰는 것보다 잘 지켜집니다.",
  siblings=siblings("tokenname"),
  related='''        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="dark.html"><b>다크 모드</b><em>2부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="spacing.html"><b>간격 체계</b><em>2부</em></a></li>''',
)
