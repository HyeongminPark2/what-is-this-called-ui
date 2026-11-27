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
  desc="시안 도구의 자동 배치. 플렉스박스와 같은 것이고, 말만 다르다.",
  lede="<b>오토 레이아웃은 플렉스박스입니다.</b> 이름만 다를 뿐 같은 것이라, 대응표 하나면 대화가 짧아집니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>조작기를 움직이면 아래에 <b>그대로 CSS</b> 가 나옵니다 — 이름만 다를 뿐 같은 것입니다.<br>
          이 대응표를 알고 있으면 <b>“여백이 자동이에요”</b>가 <code>gap</code> 이고
          <b>“채우기로 해 주세요”</b>가 <code>flex: 1</code> 이라는 것이 바로 들립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오토 레이아웃, 자동 배치, 스택"),
    ("영어", "auto layout, stack, frame"),
    ("같이 쓰는 말",
     "자식을 한 방향으로 줄 세우는 상자가 <b>오토 레이아웃 프레임</b>입니다. "
     "남은 자리를 다 쓰는 것이 <b>채우기</b>(Fill), 내용만큼만 차지하는 것이 <b>감싸기</b>(Hug), "
     "값을 박는 것이 <b>고정</b>(Fixed)입니다. "
     "다른 도구에서는 <b>스택</b>(Stack)이라 부르고, SwiftUI 의 <code>HStack</code>·<code>VStack</code>도 같은 생각입니다."),
    ("자주 잘못 부름",
     "<b>그리드</b> — <a href=\"../items/grid.html\">CSS 그리드</a>는 두 방향입니다. 오토 레이아웃은 <b>한 방향</b>이라 플렉스에 가깝습니다.<br>"
     "<b>프레임</b> — 그냥 상자를 뜻하기도 하고 오토 레이아웃이 걸린 상자를 뜻하기도 합니다.<br>"
     "<b>레이아웃 그리드</b> — 화면을 세로로 나눈 안내선입니다. 전혀 다른 것입니다."),
  ]),
  axes=ax("오토 레이아웃"),
  oneline="<b>대응표 한 장이면 통역이 끝납니다.</b> 채우기 = <code>flex: 1</code>, 감싸기 = <code>fit-content</code>, 간격 = <code>gap</code>.",
  s4_title="설정별로", s4_hint="CSS 로는 무엇인가",
  states=states([
    (box('gap:6px', I + I + I, "152px", "flex-direction: row"), "가로", "<code>row</code>. 기본값이다"),
    (box('flex-direction:column;gap:6px', I + I + I, "152px", "flex-direction: column"), "세로", "<code>column</code>"),
    (box('gap:18px', I + I + I, "152px", "gap: 18px"), "간격", "<code>gap</code>. <b>여백을 자동으로</b>라는 말이 이것"),
    (box('gap:6px;align-items:center;min-height:56px', I + '<i style="display:block;background:var(--accent);border-radius:3px;min-width:20px;min-height:34px"></i>' + I, "152px", "align-items: center"),
     "맞춤", "<code>align-items</code>·<code>justify-content</code>"),
    (box('gap:6px', I + IF + I, "152px", "가운데 칸에 flex: 1"), "채우기", "<b>Fill</b> — 남은 자리를 다 쓴다"),
    (box('gap:6px;flex-wrap:wrap', I + I + I + I + I + I + I + I, "152px", "flex-wrap: wrap"), "줄바꿈", "<b>Wrap</b> — 넘치면 다음 줄로"),
  ]),
  anat=ANAT,
  pins=pins([
    ("오토 레이아웃", "display: flex", "자식을 <b>한 방향</b>으로 줄 세운다"),
    ("방향", "row · column", "가로냐 세로냐"),
    ("간격 · 패딩", "gap · padding", "사이 빈틈과 <b>안쪽</b> 여백"),
    ("채우기", "flex: 1", "남은 자리를 다 쓴다. <b>가장 자주 오가는 말</b>"),
    ("감싸기", "fit-content", "내용만큼만"),
    ("절대 위치", "position: absolute", "흐름에서 <b>빼낸다</b> — 배지·뱃지 같은 것"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>시안의 오토 레이아웃이 곧 마크업 구조</b>라는 점이 숨은 쓸모입니다.
          시안에서 상자를 어떻게 묶었는지가 <code>&lt;div&gt;</code> 를 어떻게 묶을지와
          거의 그대로 겹칩니다.
          그래서 시안이 오토 레이아웃으로 잘 짜여 있으면 마크업이 빨라지고,
          절대 위치로 늘어놓은 시안은 <b>구조를 다시 생각해서</b> 만들어야 합니다 —
          \"이 시안 오토 레이아웃으로 되어 있나요\"가
          일정을 가늠하는 질문이 되는 이유입니다.</p>''',
  do=ul([
    "시안의 묶음을 <b>그대로 마크업</b>으로 옮기기",
    "<b>대응표</b>를 손에 두고 대화하기",
    "채우기·감싸기·고정 가운데 <b>무엇인지</b> 물어보기",
  ]),
  dont=ul([
    "절대 위치로 늘어놓은 시안을 그대로 흉내 내기",
    "오토 레이아웃을 <a href=\"../items/grid.html\">그리드</a>와 섞어 부르기",
    "간격을 <code>margin</code>으로 — <code>gap</code> 이 더 안 깨진다",
    "'알아서 되게' 로 넘기기 — <b>Fill 인지 Hug 인지</b> 물어본다",
  ]),
  instead='두 방향이 필요하면 <a href="../items/grid.html">그리드</a>, 한 방향이면 <a href="../items/flex.html">플렉스</a>, 간격 값은 <a href="../items/spacing.html">간격 체계</a>.',
  cases=cases([
    (box('gap:6px;align-items:center', I + IF + I, "150px", "아이콘 · 글 · 버튼"), "줄 하나", "<b>가운데만 Fill</b> — 가장 흔한 꼴"),
    (box('flex-direction:column;gap:5px', I + I, "150px", "세로로 쌓기"), "카드 안", "제목 · 설명 · 버튼"),
    (box('gap:6px;flex-wrap:wrap', I + I + I + I + I, "150px", "넘치면 다음 줄"), "칩 묶음", "<b>Wrap</b> 이 필요한 자리"),
  ]),
  s8_title="대응표", s8_hint="이 말의 계약서",
  code_lede="시안에서 부르는 말과 CSS 를 짝지어 둡니다.",
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
    ("<code>min-width: 0</code>을 잊지 않는다", "<b>Fill</b> 로 둔 칸에 긴 글이 들어가면 넘친다 — <a href=\"../items/flex.html\">플렉스</a>"),
    ("<code>gap</code>이 <code>margin</code>보다 낫다", "첫·마지막 칸의 예외가 없고, 줄바꿈에서도 안 깨진다"),
    ("순서가 곧 <b>읽는 순서</b>", "<code>order</code>나 <code>row-reverse</code>로 눈에만 바꾸면 <b>키보드 순서와 어긋난다</b>"),
    ("<code>position: absolute</code>", "흐름에서 빠지므로 <b>자리를 안 차지한다</b>. 배지·닫기 버튼에"),
    ("터치 타깃", "간격을 좁게 잡으면 <a href=\"touchtarget.html\">손가락이 겹친다</a>"),
    ("반응형", "같은 오토 레이아웃이라도 폭에 따라 <b>방향이 바뀌어야</b> 할 때가 있다 — <a href=\"breakpoint.html\">브레이크포인트</a>"),
  ]),
  backend=rows([
    ("구조가 곧 마크업", "시안의 묶음이 <code>&lt;div&gt;</code> 묶음과 겹칩니다. <b>오토 레이아웃으로 짜인 시안</b>이 개발을 빠르게 합니다."),
    ("데이터 길이", "시안은 짧은 글로 그려집니다. <b>실제 길이</b>로 한 번 채워 보면 Fill·Hug 선택이 드러납니다."),
  ]),
  plat_lede="<b>한 방향으로 줄 세우기</b>라는 생각이 어디에나 있습니다.",
  plats=plats([
    ("웹", "flexbox",
     box('gap:5px', I + I, "110px", "display: flex"),
     "<code>gap</code>·<code>flex: 1</code>. 시안의 말과 <b>거의 1대1</b>로 대응합니다."),
    ("iOS", "HStack · VStack",
     '''              <div class="phone" role="img" aria-label="SwiftUI 스택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">HStack(spacing: 12)</div></div></div>''',
     "<code>HStack</code>·<code>VStack</code>·<code>Spacer()</code>. <b>Spacer 가 justify-content</b> 자리입니다."),
    ("안드로이드", "Row · Column",
     '''              <div class="phone" role="img" aria-label="Compose 행렬 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Row(horizontalArrangement = …)</div></div></div>''',
     "Compose 의 <code>Row</code>·<code>Column</code>·<code>weight(1f)</code>. <b>weight 가 flex: 1</b> 입니다."),
  ]),
  plat_note="\"오토 레이아웃이 뭐예요\"는 디자이너와 개발자가 <b>같은 것을 다른 이름</b>으로 부르고 있다는 신호입니다. 대응표를 한 번 맞춰 두면 '여백 자동'·'채우기'·'감싸기' 같은 말이 바로 코드로 옮겨지고, 시안 리뷰에서 <b>구조 이야기</b>를 할 수 있게 됩니다.",
  siblings=siblings("autolayout"),
  related='''        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>''',
)
