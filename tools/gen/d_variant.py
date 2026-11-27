# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def mat(cells, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;'
            'display:flex;gap:4px;flex-wrap:wrap">' + cells + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def chip(label, tone="primary", size="md", off=False):
    bg = {'primary': 'var(--accent)', 'ghost': 'transparent', 'danger': 'var(--danger)'}[tone]
    fg = '#fff' if tone != 'ghost' else 'var(--fg)'
    bd = 'border:1px solid var(--line-strong);' if tone == 'ghost' else 'border:0;'
    pad = {'sm': '2px 7px', 'md': '4px 10px', 'lg': '6px 13px'}[size]
    fs = {'sm': '8px', 'md': '9px', 'lg': '10.5px'}[size]
    return ('<span style="background:' + bg + ';color:' + fg + ';' + bd + 'border-radius:4px;padding:' + pad +
            ';font-size:' + fs + (';opacity:.45' if off else '') + '">저장</span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">축은 크기 · 강조 · 상태, 축마다 값 개수를 셈</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">칸 수는 축마다 값 개수를 모두 곱한 수</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">축을 하나 늘리면 칸이 몇 배로 늘어남</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">코드에서는 같은 축과 값을 props로 씀</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">상태(호버·누름)는 배리언트로 안 만들기도 함</div>
                </div>
              </div>'''

D = dict(
  slug="variant", ko="배리언트와 프롭", en="Variants & props",
  desc="같은 부품에 미리 정해 둔 변형을 다루고, 변형의 축을 하나 늘릴 때마다 칸 수가 곱으로 늘어나는 모습을 보여 주는 항목입니다.",
  lede="배리언트는 같은 부품에 미리 <b>정해 둔 변형</b>입니다. 크기나 강조 같은 변형의 축을 하나 늘릴 때마다 만들어야 할 칸이 <b>곱으로</b> 늘어납니다.",
  axes_lede="15부에서 다루는 현장 용어는 화면 부품의 이름 대신 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지를 물어보면 이 용어들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>축을 켜고 끄면서 칸 수가 어떻게 바뀌는지 보세요. 축이 늘 때마다 <b>9 → 18 → 54</b>로 늘어납니다.<br>
          <b>시안에서는 54칸을 손으로 만들어야 하고, 고칠 때마다 54칸을 모두 손대야 합니다.</b>
          배리언트를 미리 설계해야 하는 이유가 이 작업량입니다. 같은 변형이 코드에서는 <code>props</code> 세 개로 끝납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배리언트, 변형, 프롭, 속성"),
    ("영어", "variant, variant property, props, component set"),
    ("같이 쓰는 말",
     "변형의 축을 <b>프로퍼티</b>(property), 그 축의 값을 <b>배리언트</b>라고 부릅니다. "
     "같은 부품의 변형을 모아 둔 것은 <b>컴포넌트 세트</b>입니다. "
     "코드 쪽에서는 같은 개념을 <b>props</b>라고 부르고, "
     "클래스 이름으로 적으면 <code>btn--primary</code> 같은 <b>모디파이어</b>(BEM)가 됩니다."),
    ("자주 잘못 부르는 이름",
     "<b>상태</b> — 호버나 누름은 사용자의 조작으로 <b>생기는</b> 것이고, 배리언트는 화면을 만드는 쪽이 <b>골라서 정하는</b> 것입니다.<br>"
     "<b>컴포넌트</b> — <a href=\"component.html\">컴포넌트</a>는 부품 자체를 가리키고, 배리언트는 <b>그 부품 안의 변형</b>을 가리킵니다.<br>"
     "<b>스타일</b> — 색이나 글꼴만 바뀌는 변형뿐 아니라 <b>구조가 바뀌는 변형</b>도 배리언트입니다."),
  ]),
  axes=ax("배리언트와 프롭"),
  oneline="<b>축을 늘리기 전에 칸 수를 곱해 보세요.</b> 3×3×2는 18칸이지만, 값이 세 개인 축을 하나만 더해도 54칸이 됩니다.",
  s4_title="축 수에 따라 늘어나는 칸", s4_hint="축을 하나씩 더할 때의 칸 수",
  states=states([
    (mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "152px", "축 1개 · 3칸"),
     "크기 축만 둘 때", "작게, 보통, 크게의 세 칸입니다"),
    (mat(chip('저장', 'primary') + chip('저장', 'ghost') + chip('저장', 'danger'), "152px", "축 2개 · 9칸"),
     "강조 축을 더했을 때", "3 × 3 = <b>9칸</b>이 됩니다"),
    (mat(chip('저장', 'primary') + chip('저장', 'primary', 'md', True) + chip('저장', 'ghost') + chip('저장', 'ghost', 'md', True), "152px", "축 3개 · 18칸"),
     "상태 축까지 더했을 때", "3 × 3 × 2 = <b>18칸</b>이 됩니다"),
    (mat(''.join(chip('저장', t, s) for t in ['primary', 'ghost', 'danger'] for s in ['sm', 'md']), "152px", "축 4개 · 54칸", False),
     "아이콘 축까지 더했을 때", "3 × 3 × 2 × 3 = <b>54칸</b>이 됩니다"),
    (card('<span style="font-size:9px">호버 · 누름 · 초점</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">사용자 조작으로 생겨 CSS에 맡김</span>', "152px", "축에서 뺌"),
     "상태를 축에서 빼기", "상태를 <b>:hover 같은 CSS에 맡기면</b> 칸이 늘지 않습니다"),
    (card('<span style="font-size:9px">아이콘 버튼은 따로</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">모양이 많이 다르면 부품을 쪼갬</span>', "152px", "축을 줄이는 다른 방법"),
     "부품을 둘로 쪼개기", "모양이 많이 다르면 <b>한 부품에 모두 넣지 않고</b> 따로 만듭니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("축", "크기 · 강조 · 상태", "축마다 <b>값이 몇 개</b>인지 셉니다"),
    ("칸", "축의 곱", "칸 수는 축마다 값 개수를 곱한 수입니다. 3 × 3 × 2 = 18"),
    ("칸 수 증가", "+1 축 = ×N", "축을 하나 더하면 칸 수가 그 축의 값 개수만큼 <b>몇 배</b>로 늘어납니다"),
    ("코드에서는", "props", "시안의 축은 코드의 <code>props</code>에 해당합니다"),
    ("상태 빼기", ":hover · :active", "사용자의 조작으로 <b>생기는</b> 상태는 CSS에 맡깁니다"),
    ("부품 쪼개기", "다른 부품으로", "모양이 많이 다르면 다른 부품으로 <b>따로 만듭니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>축을 줄이는 방법은 두 가지</b>입니다.
          첫째는 <b>상태를 빼는</b> 것입니다. 호버와 누름, 초점은 사용자의 조작으로 생기기 때문에
          시안에 칸으로 둘 필요가 없고, 코드에서는 CSS가 처리합니다.
          둘째는 <b>부품을 쪼개는</b> 것입니다. 아이콘만 있는 버튼은
          크기와 여백, 접근성 규칙이 모두 달라서 같은 부품의 변형으로 두면
          예외 조건이 계속 늘어납니다.
          <b>'이게 정말 같은 부품인가'</b>를 한 번 물어보는 것만으로 축 하나를 없앨 수 있는 경우가 흔합니다.</p>''',
  do_title="배리언트를 설계할 때 지킬 것",
  dont_title="배리언트를 설계할 때 피할 것",
  do=ul([
    "축을 늘리기 전에 칸 수를 <b>곱해 봅니다</b>",
    "<b>상태</b>는 축에서 빼고 CSS에 맡깁니다",
    "모양이 많이 다르면 <b>부품을 쪼갭니다</b>",
  ]),
  dont=ul([
    "축을 다섯 개나 둘 때. 칸이 <b>백 칸</b>을 넘습니다",
    "호버와 누름을 칸으로 만들 때. 상태 축이 하나 늘어 <b>칸이 두 배</b>가 됩니다",
    "모양이 많이 다른 것까지 한 부품에 모두 넣을 때. 예외 조건이 <b>계속 늘어납니다</b>",
    "쓰지 않을 칸을 만들 때. '혹시 몰라서' 만든 칸이 <b>절반을 차지</b>하기도 합니다",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='부품 자체는 <a href="component.html">컴포넌트와 인스턴스</a>에서, 값 묶음은 <a href="designsystem.html">디자인 시스템</a>에서, 상자 안의 배치는 <a href="autolayout.html">오토 레이아웃</a>에서 다룹니다.',
  cases=cases([
    (mat(chip('저장', 'primary') + chip('저장', 'ghost') + chip('저장', 'danger'), "150px", "강조 3"),
     "강조 축은 세 가지로", "<b>주, 약하게, 위험</b>의 세 가지면 충분합니다"),
    (mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "150px", "크기 3"),
     "크기 축도 세 가지로", "<b>표 안, 본문, 주 동작</b>에 맞춰 세 가지를 둡니다"),
    (card('<span style="font-size:9px;font-weight:700">쓰지 않는 칸</span>'
          '<span style="font-size:8.5px;color:var(--danger)">위험 × 작게 × 꺼짐</span>'
          '<span style="font-size:8px;color:var(--fg-muted)">만들어 뒀지만 아무도 안 씀</span>', "150px"),
     "아무도 안 쓰는 칸 찾기", "만들어 둔 칸의 <b>절반이 이런 칸</b>인 경우가 많습니다"),
  ]),
  s8_title="코드와 맞춰 보기", s8_hint="시안의 축과 코드의 props",
  code_lede="시안의 축은 코드의 <code>props</code>가 되고, 호버나 누름 같은 <b>상태는 CSS</b>가 처리합니다.",
  code='''<span class="c">// 축 = props. 세 개면 코드로는 세 줄이다</span>
&lt;<span class="t">Button</span> <span class="a">size</span>=<span class="s">"md"</span> <span class="a">tone</span>=<span class="s">"primary"</span> <span class="a">disabled</span>={<span class="k">false</span>} /&gt;

<span class="c">/* 상태는 축이 아니다 — CSS 가 만든다 */</span>
.btn:hover        { <span class="a">background</span>: color-mix(in srgb, <span class="a">var</span>(--accent) <span class="a">86%</span>, #000); }
.btn:active       { <span class="a">transform</span>: translateY(<span class="a">1px</span>); }
.btn:focus-visible{ <span class="a">outline</span>: <span class="a">3px</span> solid <span class="a">var</span>(--accent); }
.btn[disabled]    { <span class="a">opacity</span>: .<span class="a">45</span>; <span class="a">cursor</span>: not-allowed; }

<span class="c">// 모양이 많이 다르면 쪼갠다 — 조건이 안 붙는다</span>
&lt;<span class="t">IconButton</span> <span class="a">icon</span>=<span class="s">"trash"</span> <span class="a">label</span>=<span class="s">"삭제"</span> /&gt;''',
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("상태는 <b>CSS</b>로 처리하기", "호버, 누름, 초점, 비활성은 CSS로 처리합니다. 이것들을 축으로 만들면 <b>칸만 늘어납니다</b>"),
    ("<code>:focus-visible</code>", "포커스 표시는 <b>키보드로 옮겼을 때만</b> 보여야 해서 배리언트로는 만들 수 없습니다"),
    ("<code>disabled</code>를 축으로 둘 때", "모양이 아주 다르면 칸으로 두기도 합니다. 그래도 누를 수 없게 하는 <b>동작은 CSS와 속성</b>이 맡습니다"),
    ("이름은 쓰임에 따라 짓기", "<code>tone=\"danger\"</code>가 <code>color=\"red\"</code>보다 낫습니다. <b>다크 모드에서는 위험 색이 빨강이 아닐 수도</b> 있기 때문입니다"),
    ("쪼갠 부품에도 접근성 챙기기", "<code>IconButton</code>에는 글자가 없으니 <code>aria-label</code>이 <b>꼭 필요합니다</b>(<a href=\"../items/name.html\">이름 붙이기</a> 참고)"),
    ("안 쓰는 칸 찾기", "코드에서는 <b>검색으로</b> 실제로 쓰인 조합을 셀 수 있습니다"),
  ]),
  backend=rows([
    ("시안과 코드의 축 이름 맞추기", "시안의 <code>강조</code>와 코드의 <code>tone</code>처럼 축 이름이 다르면, 이야기할 때마다 <b>두 이름을 옮겨 가며</b> 맞춰야 합니다."),
    ("축의 값 이름도 맞추기", "시안의 값이 <code>주/약하게/위험</code>이고 코드의 값이 <code>primary/secondary/danger</code>면, 둘을 짝지은 <b>대응표를 하나 더</b> 관리해야 합니다."),
    ("안 쓰는 조합 지우기", "실제로 쓰인 조합을 세어 보면 만들어 둔 조합의 <b>절반이 쓰이지 않는</b> 경우가 많으니, 쓰지 않는 조합은 지웁니다."),
  ]),
  plat_lede="플랫폼마다 이름은 달라도 정해 둔 변형을 <b>props</b>처럼 골라 쓰는 방식은 같습니다.",
  plats=plats([
    ("웹", "props · modifier",
     mat(chip('저장', 'primary') + chip('저장', 'ghost'), "110px"),
     "<code>props</code>나 <code>btn--ghost</code> 같은 클래스로 변형을 고르고, <b>상태는 CSS가</b> 처리합니다."),
    ("iOS", "ButtonStyle",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 변형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:3px;padding:2px 5px;font-size:5px">저장</span><span style="border:1px solid var(--line);border-radius:3px;padding:2px 5px;font-size:5px">취소</span></div></div></div>''',
     "<code>.buttonStyle(.borderedProminent)</code>처럼 <b>이름이 붙은 스타일</b>을 골라 씁니다."),
    ("안드로이드", "Material 버튼",
     '''              <div class="phone" role="img" aria-label="Material 버튼 변형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:2px 6px;font-size:5px">저장</span><span style="border:1px solid var(--line);border-radius:999px;padding:2px 6px;font-size:5px">취소</span></div></div></div>''',
     "<b>Filled · Outlined · Text</b>처럼 버튼의 변형이 규격에 정해져 있습니다."),
  ]),
  plat_note="시안에서 <b>칸이 50개 넘는 컴포넌트 세트</b>를 받으면 대개 축을 줄일 여지가 있습니다. 상태를 뺄 수 있는지, 부품을 쪼갤 수 있는지 두 가지만 물어봐도 칸 수가 절반으로 줄어듭니다. 코드 쪽에서도 마찬가지로, <b>props가 다섯 개 넘는 컴포넌트</b>는 대개 둘로 나눠야 할 부품을 하나로 합쳐 둔 것입니다.",
  siblings=siblings("variant"),
  related='''        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>''',
)
