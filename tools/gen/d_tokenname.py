# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--blue-500<span style="color:var(--fg-faint)"> ← 원시 층, 값에 붙인 이름</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">--color-text-danger<span style="color:var(--fg-faint)"> ← 의미 층, 쓰임에 붙인 이름</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">--btn-bg<span style="color:var(--fg-faint)"> ← 부품 층, 한 부품만의 이름</span></div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">화면에서는 <b>의미 층만</b> 씀</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">--blue는 어두운 모드에서 <b>이름과 색이 어긋남</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">갈래-쓰임-자리-상태<span style="color:var(--fg-faint)"> ← 이름의 차례</span></div>
                </div>
              </div>'''

D = dict(
  slug="tokenname", ko="토큰 이름 짓기", en="Token naming",
  desc="토큰 이름을 값이 아니라 쓰임으로 짓는 방법과, 원시·의미·부품 세 층, 이름을 이루는 낱말의 차례를 보여 주는 항목입니다.",
  lede="토큰 이름에는 <b>값이 아니라 쓰임</b>을 적습니다. 예를 들어 <code>--blue</code>라는 이름은 어두운 모드에서 값이 다른 색으로 바뀌면 <b>실제 색과 맞지 않게</b> 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모는 토큰 이름을 <b>세 가지 규칙으로 따져 봅니다</b>. ①이름에 값이 들어 있는지,
          ②무엇에 쓰는지가 드러나는지, ③어느 층의 이름인지를 보고, 이름을 직접 넣어 보면 그 자리에서 판정해 줍니다.<br>
          '어두운 모드로 바꾸기'를 켜면 <code>--blue</code>의 실제 값이 나오는데, 이름은 파랑인데 실제 색은 파랑이 아닙니다.
          <b>이름에 값을 넣으면</b> 이런 일이 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "토큰 이름 짓기, 네이밍 규칙, 토큰 체계"),
    ("영어", "token naming, design token taxonomy"),
    ("같이 쓰는 말",
     "값에 붙인 이름은 <b>원시</b>(primitive · global · core), "
     "쓰임에 붙인 이름은 <b>의미</b>(semantic · alias), "
     "한 부품에서만 쓰는 이름은 <b>부품</b>(component) 토큰입니다. "
     "의미 토큰이 원시 토큰을 가리키는 구조는 <b>별칭</b>(alias)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>변수</b> — CSS 변수는 값을 <b>저장하는 수단</b>이고, 토큰은 그 값을 어디에 쓸지 정한 <b>규칙</b>입니다. CSS 변수는 토큰을 코드로 옮길 때 쓰는 방법 가운데 하나입니다.<br>"
     "<b>테마</b> — 테마는 토큰에 넣을 <b>값 한 벌</b>이고, 토큰 이름은 테마가 바뀌어도 그대로여야 합니다.<br>"
     "<b>클래스 이름</b> — BEM 같은 규칙은 <b>마크업</b>에 붙이는 이름이고, 토큰 이름은 <b>값</b>에 붙이는 이름입니다."),
  ]),
  s4_title="토큰의 세 층과 잘못 지은 이름", s4_hint="층마다 이름이 가리키는 것",
  states=states([
    (nm("--blue-500", "값에 붙인 이름", "원시", None),
     "원시 층", "<b>화면 코드에서는 직접 쓰지 않습니다</b>"),
    (nm("--color-text-danger", "쓰임에 붙인 이름", "의미", True),
     "의미 층", "화면 코드에서는 <b>이 층만</b> 씁니다"),
    (nm("--btn-bg", "한 부품만의 이름", "부품", True),
     "부품 층", "그 부품만 <b>다른 값을 써야 할 때</b> 만듭니다"),
    (nm("--red", "어디에 쓰는지 없음", "원시", False),
     "쓰임이 빠진 이름", "쓰임이 정해져 있지 않아 <b>아무 데나</b> 쓰이게 됩니다"),
    (nm("--color-primary", "무엇의 primary인지 모호함", "의미", False),
     "쓰임이 모호한 이름", "글자색인지 바탕색인지 <b>알 수 없습니다</b>"),
    (nm("--font-14", "값이 숫자로 들어 있음", "원시", False),
     "값이 들어간 이름", "값을 16으로 바꾸면 <b>이름과 값이 어긋납니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("원시", "<code>--blue-500</code>", "값에 붙인 이름입니다"),
    ("의미", "<code>--color-text-danger</code>", "<b>쓰임</b>에 붙인 이름입니다"),
    ("부품", "<code>--btn-bg</code>", "한 부품에서만 쓰는 이름입니다"),
    ("쓰는 층", "의미만", "화면 코드에는 <b>의미 층만</b> 나와야 합니다"),
    ("색 이름이 든 토큰", "<code>--blue</code>", "어두운 모드에서는 실제 색이 <b>파랑이 아닙니다</b>"),
    ("차례", "갈래-쓰임-자리-상태", "<code>color-text-danger-hover</code>처럼 짓습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          토큰을 세 층으로 나누는 이유는 <b>바꿀 자리를 한 곳으로 모으기</b> 위해서입니다.
          브랜드 파랑이 바뀌면 원시 토큰 한 줄만 고치면 되고,
          오류 글자색을 더 진하게 하고 싶으면 의미 토큰 한 줄만 고치면 됩니다.<br>
          하지만 <b>층을 섞어 쓰면</b> 이 이점이 모두 사라집니다.
          화면 코드에 <code>--blue-500</code>이 한 번이라도 나오면
          그 자리는 어두운 모드로 바꿔도 색이 바뀌지 않습니다.
          그래서 지킬 규칙은 <b>화면 코드에서는 의미 층만 쓴다</b>는 것 하나입니다.</p>''',
  do_title="토큰 이름을 지을 때 지킬 것",
  dont_title="토큰 이름을 지을 때 피할 것",
  do=ul([
    "이름에 <code>text</code>·<code>bg</code>·<code>border</code> 같은 <b>쓰임</b>을 적기",
    "차례를 <b>갈래-쓰임-자리-상태</b>로 고정하기",
    "화면 코드에서는 <b>의미 층만</b> 쓰기",
  ]),
  dont=ul([
    "<code>--blue</code>·<code>--red</code>처럼 색 이름 쓰기. 어두운 모드에서 <b>이름과 실제 색이 어긋납니다</b>",
    "<code>--font-14</code>처럼 값 넣기. 값을 바꾸면 <b>이름과 값이 어긋납니다</b>",
    "<code>--color-primary</code> 하나로 여러 자리를 채우기. <b>글자색인지 바탕색인지</b> 알 수 없습니다",
    "부품 토큰을 <b>먼저</b> 만들기. 부품마다 값을 따로 정하게 되어 의미 층이 비게 됩니다",
  ]),
  instead_title="함께 보면 좋은 항목",
  instead='토큰에 넣을 색 값은 <a href="color.html">색 토큰</a> 항목에서, 값을 두 벌로 두는 방법은 <a href="dark.html">다크 모드</a> 항목에서 다룹니다. 크기의 단은 <a href="typescale.html">타입 스케일</a> 항목과 <a href="spacing.html">간격 체계</a> 항목에서 설명합니다.',
  cases=cases([
    (nm("--color-bg-surface", "바탕 · 카드 면", "의미", True), "카드 바탕색에 이름 붙이기", "쓰임이 분명합니다"),
    (nm("--color-border-muted", "테두리 · 흐린 선", "의미", True), "흐린 테두리 색에 이름 붙이기", "쓰임에 더해 자리까지 이름에 적혀 있습니다"),
    (nm("--space-4", "간격 · 4번째 단", "의미", True), "간격 단에 이름 붙이기", "값이 아니라 간격 체계의 <b>단</b>을 가리킵니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="이름을 코드로 옮기는 방법",
  keys_heads="<th>이름의 부분과 점검 방법</th><th>들어가는 낱말과 설명</th>",
  code_lede="원시 토큰을 먼저 정의하고 의미 토큰이 원시 토큰을 가리키게 한 뒤, 화면 코드에서는 의미 토큰만 씁니다.",
  code='''<span class="c">/* 1층 원시. 값에 붙인 이름이라 화면에서 직접 쓰지 않는다 */</span>
:root {
  --blue-500: <span class="a">#1f6feb</span>;
  --red-500: <span class="a">#cf222e</span>;
  --gray-200: <span class="a">#e4e6eb</span>;
}

<span class="c">/* 2층 의미. 쓰임에 붙인 이름이고, 테마가 바뀌면 여기만 바꾼다 */</span>
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
    ("첫째, 갈래", "<code>color</code>·<code>space</code>·<code>radius</code>·<code>shadow</code>"),
    ("둘째, 쓰임", "<code>text</code>·<code>bg</code>·<code>border</code>·<code>icon</code>"),
    ("셋째, 자리", "<code>danger</code>·<code>muted</code>·<code>brand</code>"),
    ("넷째, 상태", "<code>hover</code>·<code>active</code>·<code>disabled</code>. 이름의 <b>맨 뒤</b>에 붙입니다"),
    ("토큰을 찾는 방법", "이름이 <code>--color-</code>로 시작하면 편집기 <b>자동완성</b>에서 색 토큰끼리 묶여 나옵니다"),
    ("확인하는 방법", "화면 코드에서 <code>--blue</code>나 <code>-500</code>을 <b>검색</b>해 봅니다"),
  ]),
  backend=rows([
    ("화면 쪽에서 쓰는 규칙", "토큰은 화면 쪽에서 쓰는 규칙입니다. 다만 <b>이름 짓는 원칙</b>은 서버에도 그대로 들어맞습니다."),
    ("서버 상태 이름과 같은 원리", "서버가 <code>status</code>를 <code>red</code>가 아니라 <code>failed</code>로 보내는 것과 같은 원리로, <b>값이 아니라 뜻</b>을 이름으로 삼습니다."),
  ]),
  plat_lede="토큰을 <b>층으로 나누는 생각</b>은 세 플랫폼이 같습니다.",
  plats=plats([
    ("웹", "CSS 변수",
     nm("--color-text-danger", "", "의미", True, "110px"),
     "<code>:root</code>에 정의하고 <code>var()</code>로 씁니다. 테마는 속성 선택자로 바꿉니다."),
    ("iOS", "Color Set",
     '''              <div class="phone" role="img" aria-label="iOS 색 자산 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:10px;border-radius:3px;background:var(--accent)"></div></div></div>''',
     "자산 묶음에 <b>이름</b>을 하나 두고 그 안에 밝은 값과 어두운 값을 함께 담습니다. 이 구조는 의미 층과 같습니다."),
    ("안드로이드", "Material 역할",
     '''              <div class="phone" role="img" aria-label="안드로이드 색 역할 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:10px;border-radius:3px;background:var(--accent)"></div></div></div>''',
     "<code>primary</code>·<code>onPrimary</code>·<code>surface</code>처럼 <b>역할 이름</b>이 규격에 미리 정해져 있습니다."),
  ]),
  plat_note="Material의 <b>역할 이름</b>은 의미 층을 OS가 미리 정해 준 것입니다. 그래서 이름을 고민할 일은 줄지만, 정해진 역할 밖의 이름을 만들기는 어렵습니다. 반대로 웹에서는 이름을 <b>전부 직접 지어야</b> 해서 자유로운 대신 이름이 쉽게 엉킵니다. 그러므로 이름의 차례를 갈래-쓰임-자리-상태처럼 <b>한 줄로 적어 두고</b> 새 토큰을 만들 때마다 그 차례에 맞춰 보는 편이, 규칙을 길게 써 두는 것보다 잘 지켜집니다.",
  siblings=siblings("tokenname"),
  related='''        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="dark.html"><b>다크 모드</b><em>2부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="spacing.html"><b>간격 체계</b><em>2부</em></a></li>''',
)
