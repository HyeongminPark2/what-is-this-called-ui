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
  desc="포커스가 무엇이고 왜 테두리를 지우면 안 되는지, 순서와 건너뛰기 링크까지 다루는 항목.",
  lede="키보드가 <b>지금 가리키는 곳</b>. 마우스를 못 쓰는 사람에게는 이것이 곧 커서입니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><kbd>Tab</kbd>을 눌러 보세요. 어디에 포커스가 갔는지, <b>테두리가 보이는지</b>를 기록합니다.<br>
          테두리를 <b>아예 없애기</b>로 바꾸면 포커스는 움직이는데 <b>화면에서는 아무것도 안 보입니다</b> —
          <code>outline: none</code> 한 줄이 하는 일입니다.<br>
          맨 앞의 <b>건너뛰기 링크</b>는 평소엔 숨어 있다가 <b>첫 Tab 에만</b> 나타납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포커스, 초점, 포커스 링, 포커스 표시"),
    ("영어", "focus, focus ring, focus indicator, focus order"),
    ("같이 쓰는 말",
     "포커스를 둘러싼 테두리를 <b>포커스 링</b>(focus ring · indicator), "
     "Tab 으로 도는 순서를 <b>포커스 순서</b>(focus order · tab order)라 합니다. "
     "맨 앞의 숨은 링크는 <b>건너뛰기 링크</b>(skip link), "
     "포커스를 받을 수 있는 요소는 <b>포커서블</b>(focusable)입니다."),
    ("자주 잘못 부름",
     "<b>호버</b> — 호버는 마우스를 올린 것, 포커스는 <b>키보드가 가리키는 것</b>입니다. "
     "같은 모양으로 만들면 어느 쪽인지 알 수 없습니다.<br>"
     "<b>선택</b> — 글을 드래그한 것은 selection 입니다.<br>"
     "<b><code>:focus</code>와 <code>:focus-visible</code></b> — 앞은 <b>마우스로 눌러도</b> 걸리고, 뒤는 키보드로 왔을 때만입니다."),
  ]),
  axes=ax("포커스"),
  oneline="포커스 테두리는 <b>지워도 되는 장식이 아닙니다.</b> 지우면 키보드만 쓰는 사람에게 화면이 통째로 안 보이게 됩니다.",
  s4_title="상태", s4_hint="같은 버튼, 다른 표시",
  states=states([
    (btn(), "평소", "아무 표시 없음"),
    (btn("background:var(--bg)"), "호버", "<b>마우스</b>를 올린 상태"),
    (btn("outline:2px solid var(--accent);outline-offset:2px"), "포커스", "<b>키보드</b>가 가리키는 상태. 또렷해야 한다"),
    (btn("outline:1px dotted var(--line-strong)"), "희미한 테두리", "있긴 한데 <b>안 보인다.</b> 없는 것과 비슷하다"),
    (btn(""), "지운 테두리", "<code>outline: none</code>. <b>어디 있는지 알 수 없다</b>"),
    (btn("outline:2px solid var(--accent);outline-offset:2px;opacity:.45"), "비활성",
     "비활성은 <b>포커스를 안 받는다</b> — 받으면 왜 안 눌리는지 알 수 없다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("포커스된 것", "focused element", "키보드가 지금 가리키는 하나. <b>화면에 꼭 하나</b>만 있다"),
    ("테두리 조건", ":focus-visible", "키보드로 왔을 때만 그린다. 마우스 클릭에는 안 그려 <b>지저분해지지 않는다</b>"),
    ("띄우기", "outline-offset", "글자에 바싹 붙으면 안 보인다. <b>2px 쯤 띄운다</b>"),
    ("지우기", "outline: none", "<b>이 한 줄이 가장 흔한 접근성 사고</b>다"),
    ("순서에 넣기·빼기", "tabindex", "<code>0</code>은 순서에 넣고, <code>-1</code>은 빼되 코드로는 보낼 수 있게 한다"),
    ("건너뛰기 링크", "skip link", "평소엔 숨고 첫 Tab 에만 나타난다. <b>메뉴 서른 개를 건너뛴다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>outline: none</code>을 쓰고 싶어지는 이유는 대개 <b>기본 테두리가 투박해서</b>입니다.
          답은 지우는 것이 아니라 <b>갈아 끼우는 것</b>입니다 —
          <code>:focus-visible</code>로 조건을 좁히고, 색과 두께를 브랜드에 맞추면 됩니다.
          지운 채로 두면 '예뻐 보이는 대신 못 쓰는 화면'이 됩니다.</p>''',
  do=ul([
    "<b>누를 수 있는 모든 것</b> — 버튼, 링크, 입력칸, 탭",
    "키보드로 간 곳이 <b>화면 밖이면 스크롤</b>해서 보여 줍니다",
    "붙박이 머리말이 가릴 수 있으면 <code>scroll-margin-top</code>으로 띄웁니다",
    "긴 메뉴가 있으면 <b>건너뛰기 링크</b>를 맨 앞에",
  ]),
  dont=ul([
    "<b><code>outline: none</code></b> — 대신 갈아 끼웁니다",
    "호버와 <b>똑같이</b> 그리는 것 — 어느 쪽인지 알 수 없습니다",
    "<code>tabindex</code>에 <b>1 이상</b>을 주는 것 — 순서가 뒤엉킵니다",
    "비활성에 포커스를 주는 것 — 왜 안 눌리는지 알 수 없습니다",
  ]),
  instead='모달 안에 가두는 일은 <a href="focustrap.html">포커스 트랩</a>, 키로 눌리는지는 <a href="keyboard.html">키보드 조작</a>, 이름은 <a href="name.html">이름 붙이기</a>.',
  cases=cases([
    (btn("outline:2px solid var(--accent);outline-offset:2px", "저장하기"),
     "버튼", "가장 흔한 자리. <b>두께 2px 이상</b>이라야 보인다"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:8px;outline:2px solid var(--accent);outline-offset:-2px">
                <span style="font-size:11.5px;font-weight:600">정산 요청 #4821</span>
              </div>''',
     "목록의 줄", "테두리를 <b>안쪽</b>에 그린다. 바깥이면 옆 줄을 덮는다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:5px">
                <span style="background:var(--accent);color:#fff;border-radius:5px;padding:5px 10px;font-size:11px;font-weight:700;justify-self:start">본문으로 건너뛰기</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">평소엔 숨어 있다</span>
              </div>''',
     "건너뛰기 링크", "첫 Tab 에만 나타난다. <b>메뉴를 통째로 건너뛴다</b>"),
  ]),
  s8_title="최소 코드와 키보드", s8_hint="이 화면의 계약서",
  code_lede="기본 테두리를 <b>지우지 말고 갈아 끼웁니다.</b> 조건은 <code>:focus-visible</code>로 좁힙니다.",
  code='''<span class="c">/* 지우지 말고 갈아 끼운다 */</span>
<span class="t">:focus-visible</span> {
  <span class="a">outline</span>: <span class="a">2px</span> solid <span class="t">var</span>(<span class="a">--accent</span>);
  <span class="a">outline-offset</span>: <span class="a">2px</span>;
}

<span class="c">/* 목록의 줄은 안쪽에 — 옆 줄을 덮지 않게 */</span>
<span class="t">.row</span>:focus-visible { <span class="a">outline-offset</span>: -<span class="a">2px</span>; }

<span class="c">/* 붙박이 머리말에 가리지 않게 */</span>
<span class="t">:target</span>, [<span class="a">tabindex</span>] { <span class="a">scroll-margin-top</span>: <span class="a">72px</span>; }

<span class="c">&lt;!-- 건너뛰기 링크 — 문서 맨 앞 --&gt;</span>
&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"skip"</span> <span class="a">href</span>=<span class="s">"#main"</span>&gt;본문으로 건너뛰기&lt;/<span class="t">a</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "다음 누를 것으로. <b>화면에 보이는 순서</b>와 같아야 한다"),
    ("<kbd>Shift</kbd>+<kbd>Tab</kbd>", "뒤로"),
    ("<code>:focus-visible</code>", "키보드로 왔을 때만 그린다. 마우스 클릭에는 안 그려진다"),
    ("<code>tabindex=\"0\"</code>", "원래 못 받던 것을 순서에 넣는다. <b>1 이상은 쓰지 않는다</b>"),
    ("<code>tabindex=\"-1\"</code>", "Tab 으로는 못 가지만 <code>.focus()</code>로는 보낼 수 있다"),
    ("<code>:focus-within</code>", "<b>안쪽에</b> 포커스가 있을 때 부모를 꾸민다"),
  ]),
  backend=rows([
    ("순서는 DOM 순서다", "<code>order</code>나 <code>grid-area</code>로 <b>보이는 자리를 바꿔도 Tab 순서는 안 바뀝니다.</b> 서버가 내려주는 순서를 그대로 그리는 쪽이 안전합니다."),
    ("화면이 바뀐 뒤", "목록을 다시 그리거나 라우팅으로 화면을 바꾸면 <b>포커스가 body 로 떨어집니다.</b> 새 화면의 제목으로 옮겨 줘야 '어디로 왔는지'가 전달됩니다."),
    ("지운 줄의 포커스", "항목을 지우면 그 자리의 포커스가 사라집니다. <b>다음 줄이나 목록 자체</b>로 옮깁니다 — <a href=\"../items/chip.html\">칩</a>에서 다룬 것과 같은 문제입니다."),
    ("자동 검사", "Playwright 로 <kbd>Tab</kbd>을 눌러 가며 <code>document.activeElement</code>를 기록하면 <b>순서와 테두리를 CI 에서</b> 확인할 수 있습니다."),
  ]),
  plat_lede="두 OS 에는 <b>키보드 말고도</b> 포커스를 옮기는 방법이 더 있습니다.",
  plats=plats([
    ("웹", ":focus-visible",
     btn("outline:2px solid var(--accent);outline-offset:2px", "저장"),
     "브라우저가 기본 테두리를 그려 줍니다. <b>지우는 것이 가장 흔한 사고</b>입니다."),
    ("iOS", "VoiceOver · 포커스",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.accessibilityFocused<br>@FocusState</div>''',
     "키보드 외에 <b>VoiceOver 커서</b>와 스위치 제어가 있습니다. 포커스가 두 갈래라 둘 다 챙겨야 합니다."),
    ("안드로이드", "TalkBack · 포커스",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FocusRequester<br>Modifier.focusable( )</div>''',
     "역시 <b>TalkBack 커서</b>와 키보드 포커스가 따로입니다. TV·크롬북에서는 키보드 포커스가 주인공입니다."),
  ]),
  plat_note="웹에서 \"포커스\"는 보통 <b>키보드 하나</b>를 뜻하지만, 앱에서는 <b>스크린 리더 커서</b>와 키보드 포커스가 따로 움직입니다. \"포커스를 여기로 옮겨 주세요\"가 어느 쪽인지 확인해야 합니다.",
  siblings=siblings("focus"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/chip.html"><b>칩</b><em>5부</em></a></li>''',
)
