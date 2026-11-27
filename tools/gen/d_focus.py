# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def btn(style="", label="저장", w=""):
    return ('              <div style="display:grid;place-items:center;padding:6px">'
            '<span style="display:inline-block;padding:7px 13px;border-radius:6px;border:1px solid var(--line-strong);'
            'background:var(--surface);font-size:12px;' + style + '">' + label + '</span></div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px;justify-items:start">
                  <div class="pin-out" data-pin="1" style="display:inline-block;padding:8px 14px;border-radius:6px;border:1px solid var(--line-strong);background:var(--surface);font-size:12.5px;outline:2px solid var(--accent);outline-offset:2px">저장하기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">:focus-visible   — 키보드로 왔을 때만</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">outline-offset   — 글자에 안 붙게 띄운다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">outline: none   — 지우면 키보드로 못 쓴다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">tabindex="0" / "-1"   — 순서에 넣기 / 빼기</div>
                  <div class="pin-out" data-pin="6" style="display:inline-block;background:var(--accent);color:#fff;border-radius:5px;padding:5px 10px;font-size:11px;font-weight:700">본문으로 건너뛰기</div>
                </div>
              </div>'''

D = dict(
  slug="focus", ko="포커스", en="Focus · focus indicator",
  desc="포커스가 무엇인지, 포커스 테두리를 왜 지우면 안 되는지 보여 주고 포커스 순서와 건너뛰기 링크까지 다루는 항목입니다.",
  lede="포커스는 키보드가 <b>지금 가리키고 있는 요소</b>입니다. 마우스를 쓰지 못하는 사람은 포커스 표시를 보고 화면의 어디에서 작업하고 있는지 알기 때문에, 포커스 표시가 마우스 커서 역할을 합니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><kbd>Tab</kbd>을 눌러 보세요. 포커스가 어디로 갔는지, 그리고 <b>테두리가 보이는지</b>가 기록에 남습니다.<br>
          테두리를 <b>아예 없애기</b>로 바꾸면 포커스는 그대로 옮겨 가는데도 <b>화면에는 아무 표시가 나타나지 않습니다</b>.
          CSS에 <code>outline: none</code> 한 줄을 넣으면 이렇게 됩니다.<br>
          맨 앞의 <b>건너뛰기 링크</b>는 평소에는 숨어 있다가 <b>처음 Tab을 눌렀을 때만</b> 나타납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포커스, 초점, 포커스 링, 포커스 표시"),
    ("영어", "focus, focus ring, focus indicator, focus order"),
    ("같이 쓰는 말",
     "포커스를 받은 요소를 둘러싼 테두리는 <b>포커스 링</b>(focus ring · indicator), "
     "Tab을 누를 때 포커스가 옮겨 가는 순서는 <b>포커스 순서</b>(focus order · tab order)라고 부릅니다. "
     "페이지 맨 앞에 숨겨 둔 링크는 <b>건너뛰기 링크</b>(skip link), "
     "포커스를 받을 수 있는 요소는 <b>포커서블</b>(focusable) 요소라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>호버</b> — 호버는 마우스를 올려 둔 상태이고, 포커스는 <b>키보드가 가리키는 상태</b>입니다. "
     "두 상태를 같은 모양으로 그리면 사용자는 지금 어느 쪽인지 알 수 없습니다.<br>"
     "<b>선택</b> — 마우스로 글자를 끌어서 칠한 것은 포커스가 아니라 선택(selection)입니다.<br>"
     "<b><code>:focus</code>와 <code>:focus-visible</code></b> — <code>:focus</code>는 <b>마우스로 눌렀을 때도</b> 적용되고, <code>:focus-visible</code>은 키보드로 포커스가 왔을 때만 적용됩니다."),
  ]),
  axes=ax("포커스"),
  oneline="포커스 테두리는 키보드로 화면을 쓰는 사람에게 <b>지금 어느 요소에 있는지</b> 알려 주는 표시입니다. 이 테두리를 지우면 키보드만 쓰는 사람은 어느 요소를 누르게 될지 모르는 채로 화면을 다뤄야 합니다.",
  s4_title="상태", s4_hint="같은 버튼, 다른 표시",
  states=states([
    (btn(), "평소", "아무 표시도 없습니다"),
    (btn("background:var(--bg)"), "호버", "<b>마우스</b>를 올려 둔 상태입니다"),
    (btn("outline:2px solid var(--accent);outline-offset:2px"), "포커스", "<b>키보드</b>가 가리키는 상태입니다. 테두리가 또렷하게 보여야 합니다"),
    (btn("outline:1px dotted var(--line-strong)"), "희미한 테두리", "테두리가 있기는 하지만 너무 흐려서 <b>잘 보이지 않습니다.</b> 사용자에게는 테두리가 없는 것과 거의 같습니다"),
    (btn(""), "지운 테두리", "<code>outline: none</code>으로 테두리를 지운 상태입니다. 포커스가 <b>어디 있는지 알 수 없습니다</b>"),
    (btn("outline:2px solid var(--accent);outline-offset:2px;opacity:.45"), "비활성",
     "비활성 버튼은 <b>포커스를 받지 않습니다.</b> 포커스를 받으면 사용자는 버튼이 왜 눌리지 않는지 알 수 없기 때문입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("포커스된 것", "focused element", "키보드가 지금 가리키는 요소입니다. 포커스된 요소는 <b>화면에 한 번에 하나만</b> 있습니다"),
    ("테두리 조건", ":focus-visible", "키보드로 포커스가 왔을 때만 테두리를 그립니다. 마우스로 클릭할 때는 그리지 않으므로 <b>화면이 지저분해지지 않습니다</b>"),
    ("띄우기", "outline-offset", "테두리가 요소 가장자리에 바싹 붙으면 잘 보이지 않기 때문에 <b>2px쯤 띄웁니다</b>"),
    ("지우기", "outline: none", "포커스 테두리를 지우는 이 한 줄이 <b>가장 흔한 접근성 사고</b>입니다"),
    ("순서에 넣기·빼기", "tabindex", "<code>0</code>은 요소를 포커스 순서에 넣고, <code>-1</code>은 순서에서 빼되 코드로는 포커스를 보낼 수 있게 합니다"),
    ("건너뛰기 링크", "skip link", "평소에는 숨어 있다가 처음 Tab을 누를 때 나타납니다. 이 링크를 누르면 <b>메뉴가 서른 개라도 한 번에 건너뛰고</b> 본문으로 갑니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>outline: none</code>을 쓰고 싶어지는 이유는 대개 <b>브라우저의 기본 테두리가 투박해 보여서</b>입니다.
          이럴 때는 테두리를 지우지 말고 <b>다른 테두리로 바꿔 그리면</b> 됩니다.
          <code>:focus-visible</code>로 키보드 포커스일 때만 그리도록 조건을 좁히고, 색과 두께를 브랜드에 맞추는 방식입니다.
          테두리를 지운 채로 두면 화면은 깔끔해 보여도 키보드로는 쓸 수 없게 됩니다.</p>''',
  do=ul([
    "버튼, 링크, 입력칸, 탭처럼 <b>누를 수 있는 모든 요소</b>에 포커스 테두리를 그릴 때",
    "키보드로 옮겨 간 요소가 <b>화면 밖에 있어서 스크롤</b>해 보여 줘야 할 때",
    "화면 위에 고정된 머리말이 포커스된 요소를 가릴 수 있을 때. <code>scroll-margin-top</code>으로 그만큼 띄웁니다",
    "본문 앞에 긴 메뉴가 있을 때. 페이지 맨 앞에 <b>건너뛰기 링크</b>를 둡니다",
  ]),
  dont=ul([
    "<b><code>outline: none</code></b>으로 테두리를 지울 때. 지우지 말고 다른 테두리로 바꿔 그립니다",
    "포커스를 호버와 <b>똑같이</b> 그릴 때. 사용자가 둘 중 어느 쪽인지 알 수 없습니다",
    "<code>tabindex</code>에 <b>1 이상</b>의 값을 줄 때. 화면에 보이는 순서와 포커스 순서가 어긋납니다",
    "비활성 요소에 포커스를 줄 때. 사용자는 그 요소가 왜 눌리지 않는지 알 수 없습니다",
  ]),
  instead='모달 안에 가두는 일은 <a href="focustrap.html">포커스 트랩</a>, 키로 눌리는지는 <a href="keyboard.html">키보드 조작</a>, 이름은 <a href="name.html">이름 붙이기</a>.',
  cases=cases([
    (btn("outline:2px solid var(--accent);outline-offset:2px", "저장하기"),
     "버튼", "포커스 테두리가 가장 흔하게 쓰이는 자리입니다. 테두리 <b>두께가 2px 이상</b>이어야 잘 보입니다"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:8px;outline:2px solid var(--accent);outline-offset:-2px">
                <span style="font-size:11.5px;font-weight:600">정산 요청 #4821</span>
              </div>''',
     "목록의 줄", "테두리를 줄의 <b>안쪽</b>에 그립니다. 바깥쪽에 그리면 테두리가 위아래 줄을 덮기 때문입니다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:5px">
                <span style="background:var(--accent);color:#fff;border-radius:5px;padding:5px 10px;font-size:11px;font-weight:700;justify-self:start">본문으로 건너뛰기</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">평소엔 숨어 있다</span>
              </div>''',
     "건너뛰기 링크", "처음 Tab을 누를 때만 나타나고, 누르면 <b>메뉴 전체를 건너뛰고</b> 본문으로 갑니다"),
  ]),
  s8_title="최소 코드와 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="브라우저의 기본 테두리는 <b>지우지 말고 원하는 모양으로 바꿔 그립니다.</b> 그리고 <code>:focus-visible</code>로 키보드 포커스일 때만 그리도록 조건을 좁힙니다.",
  code='''<span class="c">/* 지우지 말고 바꿔 그린다 */</span>
<span class="t">:focus-visible</span> {
  <span class="a">outline</span>: <span class="a">2px</span> solid <span class="t">var</span>(<span class="a">--accent</span>);
  <span class="a">outline-offset</span>: <span class="a">2px</span>;
}

<span class="c">/* 목록의 줄은 안쪽에 그려서 옆 줄을 덮지 않게 한다 */</span>
<span class="t">.row</span>:focus-visible { <span class="a">outline-offset</span>: -<span class="a">2px</span>; }

<span class="c">/* 붙박이 머리말에 가리지 않게 */</span>
<span class="t">:target</span>, [<span class="a">tabindex</span>] { <span class="a">scroll-margin-top</span>: <span class="a">72px</span>; }

<span class="c">&lt;!-- 건너뛰기 링크는 문서 맨 앞에 둔다 --&gt;</span>
&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"skip"</span> <span class="a">href</span>=<span class="s">"#main"</span>&gt;본문으로 건너뛰기&lt;/<span class="t">a</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "다음 요소로 포커스가 옮겨 갑니다. 옮겨 가는 순서는 <b>화면에 보이는 순서</b>와 같아야 합니다"),
    ("<kbd>Shift</kbd>+<kbd>Tab</kbd>", "이전 요소로 돌아갑니다"),
    ("<code>:focus-visible</code>", "키보드로 포커스가 왔을 때만 테두리를 그리고, 마우스로 클릭했을 때는 그리지 않습니다"),
    ("<code>tabindex=\"0\"</code>", "원래 포커스를 받지 못하던 요소를 포커스 순서에 넣습니다. <b>1 이상의 값은 쓰지 않습니다</b>"),
    ("<code>tabindex=\"-1\"</code>", "Tab으로는 갈 수 없지만 <code>.focus()</code>로는 포커스를 보낼 수 있습니다"),
    ("<code>:focus-within</code>", "<b>자식 요소</b>에 포커스가 있을 때 부모 요소의 모양을 바꿉니다"),
  ]),
  backend=rows([
    ("순서는 DOM 순서다", "Tab 순서는 DOM 순서를 따르기 때문에 <code>order</code>나 <code>grid-area</code>로 <b>보이는 자리를 바꿔도 Tab 순서는 바뀌지 않습니다.</b> 그래서 서버가 내려주는 순서대로 DOM을 그리는 쪽이 안전합니다."),
    ("화면이 바뀐 뒤", "목록을 다시 그리거나 라우팅으로 화면을 바꾸면 <b>포커스가 body로 돌아갑니다.</b> 이때 포커스를 새 화면의 제목으로 옮겨 줘야 사용자가 어느 화면으로 왔는지 알 수 있습니다."),
    ("지운 줄의 포커스", "포커스가 있던 항목을 지우면 포커스도 함께 사라지므로, 포커스를 <b>다음 줄이나 목록 자체</b>로 옮깁니다. <a href=\"../items/chip.html\">칩</a>에서 다룬 것과 같은 문제입니다."),
    ("자동 검사", "Playwright로 <kbd>Tab</kbd>을 눌러 가며 <code>document.activeElement</code>를 기록하면 <b>포커스 순서와 테두리를 CI에서</b> 확인할 수 있습니다."),
  ]),
  plat_lede="iOS와 안드로이드에는 <b>키보드 말고도</b> 포커스를 옮기는 방법이 더 있습니다.",
  plats=plats([
    ("웹", ":focus-visible",
     btn("outline:2px solid var(--accent);outline-offset:2px", "저장"),
     "브라우저가 기본 테두리를 그려 주는데, <b>이 테두리를 지우는 것이 가장 흔한 사고</b>입니다."),
    ("iOS", "VoiceOver · 포커스",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.accessibilityFocused<br>@FocusState</div>''',
     "키보드 외에도 <b>VoiceOver 커서</b>와 스위치 제어로 포커스를 옮깁니다. 키보드 포커스와 VoiceOver 커서가 따로 움직이므로 둘 다 챙겨야 합니다."),
    ("안드로이드", "TalkBack · 포커스",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FocusRequester<br>Modifier.focusable( )</div>''',
     "iOS와 마찬가지로 <b>TalkBack 커서</b>와 키보드 포커스가 따로 움직입니다. TV와 크롬북에서는 키보드 포커스가 주된 조작 수단입니다."),
  ]),
  plat_note="웹에서 \"포커스\"는 보통 <b>키보드 포커스</b> 하나를 뜻하지만, 앱에서는 <b>스크린 리더 커서</b>와 키보드 포커스가 따로 움직입니다. 그래서 \"포커스를 여기로 옮겨 주세요\"라는 요청을 받으면 둘 중 어느 쪽을 말하는지 확인해야 합니다.",
  siblings=siblings("focus"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/chip.html"><b>칩</b><em>5부</em></a></li>''',
)
