# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(style, inner="", w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--accent)")
    items = inner or ('<i style="display:block;background:var(--accent);border-radius:3px;min-width:20px;min-height:20px"></i>' * 3)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px dashed ' + col + ';border-radius:5px;background:var(--bg);padding:7px;display:flex;' + style + '">'
            + items + '</div>'
            + ('<span style="font-family:var(--mono);font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

I = '<i style="display:block;background:var(--accent);border-radius:3px;min-width:20px;min-height:20px"></i>'
IF = '<i style="display:block;background:var(--accent);border-radius:3px;min-height:20px;flex:1"></i>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">오토 레이아웃 = display: flex</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가로 · 세로 = flex-direction: row · column</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">간격 = gap · 패딩 = padding</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">채우기(Fill) = flex: 1</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">감싸기(Hug) = width: fit-content</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">절대 위치 = position: absolute — 흐름에서 뺀다</div>
                </div>
              </div>'''

D = dict(
  slug="autolayout", ko="오토 레이아웃", en="Auto layout",
  desc="시안 도구의 자동 배치 기능인 오토 레이아웃이 CSS 플렉스박스와 같은 개념이고 부르는 이름만 다르다는 것을 대응표로 보여 주는 항목입니다.",
  lede="<b>오토 레이아웃은 플렉스박스입니다.</b> 시안 도구와 CSS에서 부르는 이름만 다를 뿐 같은 개념이라서, 두 이름을 짝지은 대응표 하나만 있으면 디자이너와 개발자의 대화가 짧아집니다.",
  axes_lede="15부에서 다루는 현장 용어는 화면 부품의 이름 대신 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지를 물어보면 이 용어들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>조작기를 움직이면 같은 설정이 아래에 <b>CSS 코드로</b> 그대로 나옵니다. 이름만 다를 뿐 같은 설정이기 때문입니다.<br>
          이 대응표를 알고 있으면 <b>“여백이 자동이에요”</b>는 <code>gap</code>이고
          <b>“채우기로 해 주세요”</b>는 <code>flex: 1</code>이라는 것을 바로 알아들을 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오토 레이아웃, 자동 배치, 스택"),
    ("영어", "auto layout, stack, frame"),
    ("같이 쓰는 말",
     "자식 요소를 한 방향으로 줄 세우는 상자를 <b>오토 레이아웃 프레임</b>이라고 합니다. "
     "자식이 남은 자리를 모두 쓰게 하는 설정은 <b>채우기</b>(Fill), 내용만큼만 차지하게 하는 설정은 <b>감싸기</b>(Hug), "
     "크기를 값으로 정해 두는 설정은 <b>고정</b>(Fixed)입니다. "
     "다른 도구에서는 <b>스택</b>(Stack)이라고 부르며, SwiftUI의 <code>HStack</code>·<code>VStack</code>도 같은 개념입니다."),
    ("자주 잘못 부르는 이름",
     "<b>그리드</b> — <a href=\"../items/grid.html\">CSS 그리드</a>는 가로와 세로 두 방향으로 배치하지만, 오토 레이아웃은 <b>한 방향</b>으로 배치하므로 그리드가 아니라 플렉스에 가깝습니다.<br>"
     "<b>프레임</b> — 그냥 상자를 뜻하기도 하고, 오토 레이아웃을 적용한 상자를 뜻하기도 합니다.<br>"
     "<b>레이아웃 그리드</b> — 화면을 세로 단으로 나눠 보여 주는 안내선이라서 오토 레이아웃과는 전혀 다른 기능입니다."),
  ]),
  axes=ax("오토 레이아웃"),
  oneline="<b>대응표 한 장만 있으면 시안의 말을 CSS로 바로 옮길 수 있습니다.</b> 채우기는 <code>flex: 1</code>, 감싸기는 <code>fit-content</code>, 간격은 <code>gap</code>입니다.",
  s4_title="설정별로", s4_hint="CSS 로는 무엇인가",
  states=states([
    (box('gap:6px', I + I + I, "152px", "flex-direction: row"), "가로", "<code>row</code>에 해당하며, 플렉스의 기본값입니다"),
    (box('flex-direction:column;gap:6px', I + I + I, "152px", "flex-direction: column"), "세로", "<code>column</code>에 해당합니다"),
    (box('gap:18px', I + I + I, "152px", "gap: 18px"), "간격", "<code>gap</code>에 해당합니다. <b>여백을 자동으로</b> 해 달라는 말은 대개 이 설정을 가리킵니다"),
    (box('gap:6px;align-items:center;min-height:56px', I + '<i style="display:block;background:var(--accent);border-radius:3px;min-width:20px;min-height:34px"></i>' + I, "152px", "align-items: center"),
     "맞춤", "<code>align-items</code>와 <code>justify-content</code>에 해당합니다"),
    (box('gap:6px', I + IF + I, "152px", "가운데 칸에 flex: 1"), "채우기", "<b>Fill</b>로 두면 남은 자리를 모두 씁니다"),
    (box('gap:6px;flex-wrap:wrap', I + I + I + I + I + I + I + I, "152px", "flex-wrap: wrap"), "줄바꿈", "<b>Wrap</b>으로 두면 넘치는 자식이 다음 줄로 내려갑니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("오토 레이아웃", "display: flex", "자식 요소를 <b>한 방향</b>으로 줄 세웁니다"),
    ("방향", "row · column", "가로로 늘어놓을지 세로로 쌓을지 정합니다"),
    ("간격 · 패딩", "gap · padding", "간격은 자식 사이의 빈틈, 패딩은 상자 <b>안쪽</b>의 여백입니다"),
    ("채우기", "flex: 1", "남은 자리를 모두 씁니다. 디자이너와 개발자 사이에서 <b>가장 자주 오가는 말</b>입니다"),
    ("감싸기", "fit-content", "내용만큼만 자리를 차지합니다"),
    ("절대 위치", "position: absolute", "배치 흐름에서 <b>빼내어</b> 겹쳐 놓습니다. 배지·뱃지 같은 것에 씁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          잘 드러나지 않는 쓸모는 <b>시안의 오토 레이아웃이 그대로 마크업 구조가 된다</b>는 점입니다.
          시안에서 상자를 묶은 방식이 코드에서 <code>&lt;div&gt;</code>를 묶을 방식과
          거의 그대로 겹치기 때문입니다.
          그래서 시안이 오토 레이아웃으로 잘 짜여 있으면 마크업을 빨리 만들 수 있지만,
          절대 위치로 늘어놓은 시안은 개발자가 <b>구조를 다시 생각해서</b> 만들어야 합니다.
          \"이 시안 오토 레이아웃으로 되어 있나요\"라는 질문으로
          개발 일정을 가늠할 수 있는 것도 이 때문입니다.</p>''',
  do=ul([
    "시안의 묶음을 <b>그대로 마크업</b>으로 옮길 때",
    "<b>대응표</b>를 옆에 두고 디자이너와 이야기할 때",
    "채우기, 감싸기, 고정 가운데 <b>무엇인지</b> 물어볼 때",
  ]),
  dont=ul([
    "절대 위치로 늘어놓은 시안을 코드에서도 그대로 흉내 낼 때",
    "오토 레이아웃을 <a href=\"../items/grid.html\">그리드</a>와 섞어 부를 때",
    "간격을 <code>margin</code>으로 줄 때. <code>gap</code>을 써야 배치가 덜 깨집니다",
    "'알아서 되게' 해 달라는 말로 넘어갈 때. <b>Fill인지 Hug인지</b> 물어봐야 합니다",
  ]),
  instead='두 방향이 필요하면 <a href="../items/grid.html">그리드</a>, 한 방향이면 <a href="../items/flex.html">플렉스</a>, 간격 값은 <a href="../items/spacing.html">간격 체계</a>.',
  cases=cases([
    (box('gap:6px;align-items:center', I + IF + I, "150px", "아이콘 · 글 · 버튼"), "줄 하나", "<b>가운데 칸만 Fill</b>로 두는 것이 가장 흔한 형태입니다"),
    (box('flex-direction:column;gap:5px', I + I, "150px", "세로로 쌓기"), "카드 안", "제목과 설명, 버튼을 세로로 쌓습니다"),
    (box('gap:6px;flex-wrap:wrap', I + I + I + I + I, "150px", "넘치면 다음 줄"), "칩 묶음", "칩이 넘치면 다음 줄로 내려가야 하므로 <b>Wrap</b>이 필요합니다"),
  ]),
  s8_title="대응표", s8_hint="시안의 말과 CSS 짝짓기",
  code_lede="시안 도구에서 부르는 이름과 CSS 속성을 짝지어 두면 다음과 같습니다.",
  code='''<span class="c">/* 오토 레이아웃 = 플렉스 */</span>
.frame {
  <span class="a">display</span>: flex;                 <span class="c">/* 오토 레이아웃 */</span>
  <span class="a">flex-direction</span>: row;          <span class="c">/* 가로 · 세로 */</span>
  <span class="a">gap</span>: <span class="a">12px</span>;                    <span class="c">/* 간격 */</span>
  <span class="a">padding</span>: <span class="a">16px</span>;                <span class="c">/* 패딩 */</span>
  <span class="a">align-items</span>: center;          <span class="c">/* 맞춤 (세로축) */</span>
  <span class="a">justify-content</span>: space-between; <span class="c">/* 맞춤 (가로축) */</span>
  <span class="a">flex-wrap</span>: wrap;              <span class="c">/* 줄바꿈 */</span>
}

.child-fill { <span class="a">flex</span>: <span class="a">1</span>; <span class="a">min-width</span>: <span class="a">0</span>; }   <span class="c">/* 채우기 (Fill) */</span>
.child-hug  { <span class="a">width</span>: fit-content; }      <span class="c">/* 감싸기 (Hug) */</span>
.child-fix  { <span class="a">width</span>: <span class="a">120px</span>; }           <span class="c">/* 고정 (Fixed) */</span>
.badge      { <span class="a">position</span>: absolute; }       <span class="c">/* 절대 위치 */</span>''',
  keys=kbd([
    ("<code>min-width: 0</code>을 잊지 않는다", "<b>Fill</b>로 둔 칸에 <code>min-width: 0</code>이 없으면 긴 글이 들어갔을 때 칸 밖으로 넘칩니다(<a href=\"../items/flex.html\">플렉스</a> 참고)"),
    ("<code>gap</code>이 <code>margin</code>보다 낫다", "첫 칸과 마지막 칸을 따로 처리할 필요가 없고, 줄바꿈이 일어나도 간격이 깨지지 않습니다"),
    ("순서가 곧 <b>읽는 순서</b>", "<code>order</code>나 <code>row-reverse</code>로 보이는 순서만 바꾸면 <b>키보드로 옮겨 가는 순서와 어긋납니다</b>"),
    ("<code>position: absolute</code>", "배치 흐름에서 빠지므로 <b>자리를 차지하지 않습니다</b>. 배지나 닫기 버튼에 씁니다"),
    ("터치 타깃", "간격을 좁게 잡으면 <a href=\"touchtarget.html\">손가락이 옆 버튼까지 누르게 됩니다</a>"),
    ("반응형", "같은 오토 레이아웃이라도 화면 폭에 따라 <b>방향이 바뀌어야</b> 할 때가 있습니다(<a href=\"breakpoint.html\">브레이크포인트</a> 참고)"),
  ]),
  backend=rows([
    ("구조가 곧 마크업", "시안에서 상자를 묶은 방식이 코드의 <code>&lt;div&gt;</code> 묶음과 겹치기 때문에, <b>오토 레이아웃으로 짜인 시안</b>을 받으면 개발이 빨라집니다."),
    ("데이터 길이", "시안은 대개 짧은 글로 그려져 있습니다. 실제 데이터의 <b>길이</b>로 한 번 채워 보면 어느 칸을 Fill로, 어느 칸을 Hug로 둬야 하는지 드러납니다."),
  ]),
  plat_lede="자식을 <b>한 방향으로 줄 세우는</b> 배치 방식은 어느 플랫폼에나 있습니다.",
  plats=plats([
    ("웹", "flexbox",
     box('gap:5px', I + I, "110px", "display: flex"),
     "<code>gap</code>과 <code>flex: 1</code> 같은 속성이 시안의 설정과 <b>거의 1대1</b>로 대응합니다."),
    ("iOS", "HStack · VStack",
     '''              <div class="phone" role="img" aria-label="SwiftUI 스택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">HStack(spacing: 12)</div></div></div>''',
     "<code>HStack</code>·<code>VStack</code>·<code>Spacer()</code>를 쓰며, <b>Spacer가 justify-content</b> 역할을 합니다."),
    ("안드로이드", "Row · Column",
     '''              <div class="phone" role="img" aria-label="Compose 행렬 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Row(horizontalArrangement = …)</div></div></div>''',
     "Compose의 <code>Row</code>·<code>Column</code>·<code>weight(1f)</code>를 쓰며, <b>weight가 flex: 1</b>에 해당합니다."),
  ]),
  plat_note="개발자가 \"오토 레이아웃이 뭐예요\"라고 묻는다면 디자이너와 개발자가 <b>같은 것을 다른 이름</b>으로 부르고 있다는 뜻입니다. 대응표를 한 번 맞춰 두면 '여백 자동', '채우기', '감싸기' 같은 말을 바로 코드로 옮길 수 있고, 시안 리뷰에서도 <b>구조 이야기</b>를 할 수 있게 됩니다.",
  siblings=siblings("autolayout"),
  related='''        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>''',
)
