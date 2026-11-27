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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">축 — 크기 · 강조 · 상태. 각각 값이 몇 개인가</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">칸 수 = 축의 값을 모두 곱한 것</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">축을 하나 늘리면 칸이 몇 배가 된다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">코드로는 props — 같은 축, 같은 값</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">상태(호버·누름)는 배리언트로 안 만들기도 한다</div>
                </div>
              </div>'''

D = dict(
  slug="variant", ko="배리언트와 프롭", en="Variants & props",
  desc="같은 부품의 정해진 변형. 축을 하나 늘릴 때마다 칸이 곱으로 늘어난다.",
  lede="같은 부품의 <b>정해진 변형</b>. 축을 하나 늘릴 때마다 칸이 <b>곱으로</b> 늘어납니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>축을 켜고 끄며 칸 수를 보세요 — <b>9 → 18 → 54</b> 가 됩니다.<br>
          <b>시안에서 54칸을 손으로 만들고 고칠 때마다 54번 손대는 것</b>이 어떤 일인지가
          배리언트 설계가 중요한 이유입니다. 코드에서는 <code>props</code> 세 개일 뿐입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배리언트, 변형, 프롭, 속성"),
    ("영어", "variant, variant property, props, component set"),
    ("같이 쓰는 말",
     "변형의 축을 <b>프로퍼티</b>(property), 그 축의 값을 <b>배리언트</b>라 부릅니다. "
     "같은 부품의 변형들을 모아 둔 것이 <b>컴포넌트 세트</b>입니다. "
     "코드 쪽에서는 그대로 <b>props</b>이고, "
     "클래스 이름으로 적으면 <code>btn--primary</code> 같은 <b>모디파이어</b>(BEM)입니다."),
    ("자주 잘못 부름",
     "<b>상태</b> — 호버·누름은 <b>사용자가 만드는</b> 것이고, 배리언트는 <b>우리가 고르는</b> 것입니다.<br>"
     "<b>컴포넌트</b> — <a href=\"component.html\">컴포넌트</a>는 부품 자체, 배리언트는 <b>그 안의 변형</b>입니다.<br>"
     "<b>스타일</b> — 색·글꼴만이 아니라 <b>구조가 바뀌는 변형</b>도 배리언트입니다."),
  ]),
  axes=ax("배리언트와 프롭"),
  oneline="<b>축을 늘리기 전에 곱해 보세요.</b> 3×3×2 는 18칸이고, 거기에 하나만 더하면 54칸입니다.",
  s4_title="축을 늘리면", s4_hint="칸이 몇 개가 되나",
  states=states([
    (mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "152px", "축 1개 · 3칸"),
     "크기만", "작게 · 보통 · 크게"),
    (mat(chip('저장', 'primary') + chip('저장', 'ghost') + chip('저장', 'danger'), "152px", "축 2개 · 9칸"),
     "강조를 더하면", "3 × 3 = <b>9칸</b>"),
    (mat(chip('저장', 'primary') + chip('저장', 'primary', 'md', True) + chip('저장', 'ghost') + chip('저장', 'ghost', 'md', True), "152px", "축 3개 · 18칸"),
     "상태를 더하면", "3 × 3 × 2 = <b>18칸</b>"),
    (mat(''.join(chip('저장', t, s) for t in ['primary', 'ghost', 'danger'] for s in ['sm', 'md']), "152px", "축 4개 · 54칸", False),
     "아이콘까지", "3 × 3 × 2 × 3 = <b>54칸</b>"),
    (card('<span style="font-size:9px">호버 · 누름 · 초점</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">사용자가 만드는 것이라 CSS 에 맡긴다</span>', "152px", "축에서 뺀다"),
     "상태는 뺀다", "<b>:hover 로 두면</b> 칸이 안 는다"),
    (card('<span style="font-size:9px">아이콘 버튼은 따로</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">모양이 많이 다르면 부품을 쪼갠다</span>', "152px", "축을 줄이는 또 한 수"),
     "쪼개기", "<b>한 부품에 다 넣지 않는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("축", "크기 · 강조 · 상태", "각각 <b>값이 몇 개</b>인가"),
    ("칸", "축의 곱", "3 × 3 × 2 = 18"),
    ("곱의 무서움", "+1 축 = ×N", "축 하나가 칸을 <b>몇 배</b>로 만든다"),
    ("코드로는", "props", "시안의 축 = 코드의 <code>props</code>"),
    ("상태는 빼기", ":hover · :active", "<b>사용자가 만드는</b> 것은 CSS 에 맡긴다"),
    ("쪼개기", "다른 부품으로", "모양이 많이 다르면 <b>따로 만든다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>축을 줄이는 두 가지 방법</b>이 있습니다.
          하나는 <b>상태를 빼는</b> 것 — 호버·누름·초점은 사용자가 만드는 것이라
          시안에 칸으로 둘 필요가 없고, CSS 가 알아서 합니다.
          다른 하나는 <b>부품을 쪼개는</b> 것 — 아이콘만 있는 버튼은
          크기·여백·접근성 규칙이 다 달라서, 같은 부품의 변형으로 두면
          조건이 덕지덕지 붙습니다.
          <b>'이게 정말 같은 부품인가'</b>를 한 번 물어보면 축 하나가 사라지는 일이 흔합니다.</p>''',
  do=ul([
    "축을 늘리기 전에 <b>곱해 보기</b>",
    "<b>상태</b>는 축에서 빼고 CSS 에 맡기기",
    "모양이 많이 다르면 <b>부품을 쪼개기</b>",
  ]),
  dont=ul([
    "축을 다섯 개 — <b>백 칸</b>이 넘는다",
    "호버·누름을 칸으로 만들기 — <b>칸이 두 배</b>가 된다",
    "한 부품에 다 넣기 — 조건이 <b>덕지덕지</b> 붙는다",
    "안 쓰는 칸 만들기 — '혹시 몰라서'가 <b>절반을 차지</b>한다",
  ]),
  instead='부품 자체는 <a href="component.html">컴포넌트와 인스턴스</a>, 값 묶음은 <a href="designsystem.html">디자인 시스템</a>, 배치는 <a href="autolayout.html">오토 레이아웃</a>.',
  cases=cases([
    (mat(chip('저장', 'primary') + chip('저장', 'ghost') + chip('저장', 'danger'), "150px", "강조 3"),
     "강조", "<b>주 · 약하게 · 위험</b>. 셋이면 충분하다"),
    (mat(chip('저장', 'primary', 'sm') + chip('저장', 'primary') + chip('저장', 'primary', 'lg'), "150px", "크기 3"),
     "크기", "<b>표 안 · 본문 · 주 동작</b>에 맞춰 셋"),
    (card('<span style="font-size:9px;font-weight:700">쓰지 않는 칸</span>'
          '<span style="font-size:8.5px;color:var(--danger)">위험 × 작게 × 꺼짐</span>'
          '<span style="font-size:8px;color:var(--fg-muted)">만들어 뒀지만 아무도 안 쓴다</span>', "150px"),
     "안 쓰는 칸", "<b>절반이 이런 것</b>인 경우가 많다"),
  ]),
  s8_title="코드와 맞춰 보기", s8_hint="이 변형의 계약서",
  code_lede="시안의 축은 코드의 <code>props</code>이고, <b>상태는 CSS</b>가 맡습니다.",
  code='''<span class="c">// 축 = props. 세 개면 코드로는 세 줄이다</span>
&lt;<span class="t">Button</span> <span class="a">size</span>=<span class="s">"md"</span> <span class="a">tone</span>=<span class="s">"primary"</span> <span class="a">disabled</span>={<span class="k">false</span>} /&gt;

<span class="c">/* 상태는 축이 아니다 — CSS 가 만든다 */</span>
.btn:hover        { <span class="a">background</span>: color-mix(in srgb, <span class="a">var</span>(--accent) <span class="a">86%</span>, #000); }
.btn:active       { <span class="a">transform</span>: translateY(<span class="a">1px</span>); }
.btn:focus-visible{ <span class="a">outline</span>: <span class="a">3px</span> solid <span class="a">var</span>(--accent); }
.btn[disabled]    { <span class="a">opacity</span>: .<span class="a">45</span>; <span class="a">cursor</span>: not-allowed; }

<span class="c">// 모양이 많이 다르면 쪼갠다 — 조건이 안 붙는다</span>
&lt;<span class="t">IconButton</span> <span class="a">icon</span>=<span class="s">"trash"</span> <span class="a">label</span>=<span class="s">"삭제"</span> /&gt;''',
  keys=kbd([
    ("상태는 <b>CSS</b>로", "호버·누름·초점·비활성. 축으로 만들면 <b>칸만 는다</b>"),
    ("<code>:focus-visible</code>", "배리언트로는 못 만든다. <b>키보드일 때만</b> 보여야 한다"),
    ("<code>disabled</code>는 축일 수도", "모양이 아주 다르면 칸으로 두기도 한다. 다만 <b>동작은 CSS·속성</b>이 맡는다"),
    ("이름을 쓰임으로", "<code>tone=\"danger\"</code>가 <code>color=\"red\"</code>보다 낫다 — <b>다크 모드에서 빨강이 아닐 수</b> 있다"),
    ("쪼갠 부품에도 접근성", "<code>IconButton</code>은 <code>aria-label</code>이 <b>필수</b>다 — <a href=\"../items/name.html\">이름 붙이기</a>"),
    ("안 쓰는 칸 찾기", "코드에서는 <b>검색으로</b> 쓰인 조합을 셀 수 있다"),
  ]),
  backend=rows([
    ("축 이름을 맞춘다", "시안의 <code>강조</code>와 코드의 <code>tone</code>이 다르면 <b>매번 통역</b>해야 합니다."),
    ("값도 맞춘다", "시안이 <code>주/약하게/위험</code>이고 코드가 <code>primary/secondary/danger</code>면 <b>표를 하나 더</b> 들고 다니게 됩니다."),
    ("안 쓰는 조합 지우기", "쓰인 조합을 세어 보면 <b>절반이 안 쓰이는</b> 경우가 많습니다."),
  ]),
  plat_lede="이름은 달라도 <b>props</b>라는 생각은 같습니다.",
  plats=plats([
    ("웹", "props · modifier",
     mat(chip('저장', 'primary') + chip('저장', 'ghost'), "110px"),
     "<code>props</code>나 <code>btn--ghost</code> 같은 클래스. <b>상태는 CSS 가</b> 맡습니다."),
    ("iOS", "ButtonStyle",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 변형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:3px;padding:2px 5px;font-size:5px">저장</span><span style="border:1px solid var(--line);border-radius:3px;padding:2px 5px;font-size:5px">취소</span></div></div></div>''',
     "<code>.buttonStyle(.borderedProminent)</code>처럼 <b>이름 붙은 스타일</b>을 고릅니다."),
    ("안드로이드", "Material 버튼",
     '''              <div class="phone" role="img" aria-label="Material 버튼 변형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:2px 6px;font-size:5px">저장</span><span style="border:1px solid var(--line);border-radius:999px;padding:2px 6px;font-size:5px">취소</span></div></div></div>''',
     "<b>Filled · Outlined · Text</b> 처럼 변형이 규격에 정해져 있습니다."),
  ]),
  plat_note="시안에서 <b>칸이 50개 넘는 컴포넌트 세트</b>를 받으면 대개 축을 줄일 여지가 있습니다. 상태를 뺄 수 있는지, 쪼갤 수 있는지 두 가지만 물어봐도 절반이 됩니다. 코드 쪽에서도 같은 이익이 있습니다 — <b>props 가 다섯 개 넘는 컴포넌트</b>는 대개 둘로 나눠야 할 것이 하나로 붙어 있는 것입니다.",
  siblings=siblings("variant"),
  related='''        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>''',
)
