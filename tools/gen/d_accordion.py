# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다."

def acc(items, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for title, body, isopen in items:
        out.append('<span style="display:block;border-top:1px solid var(--line)">'
                   '<span style="display:flex;align-items:center;gap:5px;padding:4px 6px;font-size:8.5px">'
                   '<span style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + title + '</span>'
                   '<span style="margin-left:auto;font-size:7px;color:var(--fg-muted)">' + ('▲' if isopen else '▼') + '</span></span>'
                   + ('<span style="display:block;padding:0 6px 5px;font-size:7.5px;color:var(--fg-muted)">' + body + '</span>' if isopen else '')
                   + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

Q = [("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "", False), ("환불은", "", False)]

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">제목은 &lt;button&gt; — 누를 수 있어야 한다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">aria-expanded — 폈나 접었나</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">aria-controls — 무엇을 여는가</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">접힌 글은 브라우저 찾기로도 안 잡힌다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">한 번에 하나만 열면 비교를 막는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">&lt;details&gt; — 자바스크립트 없이도 된다</div>
                </div>
              </div>'''

D = dict(
  slug="accordion", ko="접히는 글", en="Accordion · disclosure",
  desc="제목만 보이고 본문은 접어 두는 부품을 다루며, 접힌 글이 찾기에 걸리지 않는 문제와 한 번에 하나만 여는 방식의 단점을 보여 주는 항목입니다.",
  lede="접히는 글은 긴 글을 <b>제목만 남기고</b> 접어 두는 부품입니다. 화면은 짧아지지만, 접힌 글은 브라우저 <b>찾기에 걸리지 않습니다</b>.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>접힌 글은 화면에 보이지 않기 때문에 브라우저의 찾기(Ctrl+F)로도 찾을 수 없습니다.
          찾는 말을 넣어 보면 데모가 <b>지금 보이는 글에서 몇 건</b>,
          <b>접힌 글 속에서 몇 건</b>이 나오는지 나눠서 셉니다.<br>
          긴 약관이나 문서를 통째로 접어 두면 그 글은 <b>검색으로 끝내 찾을 수 없게</b> 됩니다.
          또 <b>한 번에 하나만 열기</b>를 켜면 두 항목을 펴 놓고 비교할 수 없으므로,
          꼭 필요한 자리가 아니라면 <b>여러 개가 함께 열리게</b> 두는 편이 낫습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "접히는 글, 아코디언, 펼침, 더 보기"),
    ("영어", "accordion, disclosure, collapsible, expander"),
    ("같이 쓰는 말",
     "하나만 접었다 펴는 것은 <b>디스클로저</b>(disclosure), "
     "여럿을 묶어 한 번에 하나만 열리게 한 것은 좁은 뜻의 <b>아코디언</b>이라고 부릅니다.  "
     "HTML에는 <code>&lt;details&gt;</code>·<code>&lt;summary&gt;</code> 태그가 있어서  "
     "자바스크립트 없이도 만들 수 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 <b>한 번에 하나만</b> 보이고 화면 높이를 늘리지 않습니다.<br>"
     "<b>트리뷰</b> — <a href=\"treeview.html\">트리뷰</a>는 하위 항목이 이어진 <b>계층을 펴는</b> 것이고, 접히는 글은 <b>본문 내용을 펴는</b> 것입니다.<br>"
     "<b>드롭다운</b> — 드롭다운은 다른 내용 <b>위에 떠서</b> 열리므로 페이지의 자리를 차지하지 않습니다."),
  ]),
  axes=ax("접히는 글"),
  oneline="<b>글을 접기 전에 이 글을 찾아야 하는 사람이 있는지 먼저 물어보세요.</b> 그런 사람이 있다면 접으면 안 됩니다.",
  states=states([
    (acc(Q, "하나 펴짐", "제목은 늘 보인다", True), "기본", "처음에는 <b>하나만</b> 펴 둡니다"),
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "카드 2.8% 입니다.", True), ("환불은", "", False)],
         "여럿 펴짐", "비교할 수 있다", True),
     "여럿 열림", "여러 항목을 <b>나란히</b> 놓고 볼 수 있습니다"),
    (acc([("정산은 언제", "", False), ("수수료는", "", False), ("환불은", "", False)], "다 접힘", "찾기로는 안 잡힌다", False),
     "다 접힘", "제목만 보이고 <b>본문은 보이지 않습니다</b>"),
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "", False)], "한 번에 하나", "다른 걸 열면 이게 접힌다", False),
     "하나만 열림", "다른 항목을 열면 이전 항목이 접혀서 <b>비교할 수 없습니다</b>"),
    (acc([("정산 안내", "접기에는 너무 중요한 글입니다.", True)], "안 접는 글", "찾아야 하는 글은 펴 둔다", True),
     "접지 말 것", "<b>중요한 글</b>은 펴 둡니다"),
    (acc([("ㄱ", "", False), ("ㄴ", "", False), ("ㄷ", "", False), ("ㄹ", "", False)], "너무 많음", "제목만 스무 줄", False),
     "항목이 많음", "제목만 길게 늘어서서 <b>목록처럼</b> 보입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("제목", "<code>&lt;button&gt;</code>", "<b>누를 수 있어야</b> 합니다"),
    ("<code>aria-expanded</code>", "폈나 접었나", "펼침 삼각형이 보여 주는 상태를 <b>스크린 리더에 알립니다</b>"),
    ("<code>aria-controls</code>", "무엇을 여나", "제목과 본문을 <b>연결합니다</b>"),
    ("접힌 글", "안 찾아짐", "브라우저 찾기로 <b>찾을 수 없습니다</b>"),
    ("하나만 열기", "비교 막힘", "<b>꼭 필요할 때만</b> 씁니다"),
    ("<code>&lt;details&gt;</code>", "기본 제공", "스크립트 <b>없이도</b> 동작합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          글을 접는 것은 <b>화면을 깔끔하게 만드는 가장 쉬운 방법</b>이라서 지나치게 많이 쓰입니다.
          그런데 글을 접으면 그 글은 <b>Ctrl+F로도, 페이지 검색으로도</b> 찾을 수 없게 되고,
          사용자는 분명 어딘가에 적혀 있던 내용을 찾지 못해 헤매게 됩니다.
          그래서 약관의 핵심, 수수료율, 환불 규정처럼 <b>찾아야 하는 글</b>은 접지 않습니다.<br>
          크롬 계열에는 <code>hidden="until-found"</code>가 생겨서
          접힌 글이 <b>찾기에 걸리면 저절로 펴지게</b> 할 수 있습니다.
          아직 모든 브라우저가 지원하지는 않지만, 글을 꼭 접어야 한다면 이 방법을 먼저 검토합니다.</p>''',
  do=ul([
    "제목을 <b><code>&lt;button&gt;</code></b> 으로 두고 <code>aria-expanded</code>를 붙이기",
    "<b>여러 개가 같이</b> 열리게 두기",
    "찾아야 하는 글은 <b>접지 않기</b>",
  ]),
  dont=ul([
    "<code>&lt;div&gt;</code>에 <code>onclick</code>만 달기. <b>키보드로 열 수 없습니다</b>",
    "처음부터 <b>모두 접어</b> 두기. 사용자는 안에 무엇이 있는지도 알 수 없습니다",
    "이유 없이 <b>한 번에 하나만</b> 열리게 하기. 여러 항목을 비교할 수 없게 됩니다",
    "항목을 스무 개씩 두기. 그 정도면 아코디언이 아니라 <b>목록</b>으로 만듭니다",
  ]),
  instead='한 번에 하나만 보이면 <a href="tabs.html">탭</a>, 길을 펴면 <a href="treeview.html">트리뷰</a>, 위에 떠서 열리면 <a href="popover.html">팝오버</a>, 긴 문서의 길잡이는 <a href="anchornav.html">앵커 내비</a>.',
  cases=cases([
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "", False)], "자주 묻는 질문", "", True),
     "자주 묻는 질문", "접히는 글이 <b>가장 잘 맞는</b> 자리입니다"),
    (acc([("자세한 조건 보기", "최소 주문 금액 10,000원", True)], "더 보기", "", True),
     "'더 보기'", "본문에 덧붙이는 <b>보조 설명</b>을 접어 둡니다"),
    (acc([("고급 설정", "", False)], "고급 설정", "", True),
     "고급 설정", "대부분의 사용자가 <b>건드리지 않는</b> 값들을 접어 둡니다"),
  ]),
  code_lede="가장 쉬운 방법은 <code>&lt;details&gt;</code>를 쓰는 것입니다. 모양을 많이 바꿔야 할 때만 직접 만듭니다.",
  code='''<span class="c">&lt;!-- 스크립트 없이 동작하고 키보드 조작도 저절로 된다 --&gt;</span>
&lt;<span class="t">details</span>&gt;
  &lt;<span class="t">summary</span>&gt;정산은 언제 들어오나요&lt;/<span class="t">summary</span>&gt;
  &lt;<span class="t">p</span>&gt;매주 수요일에 지난주 매출을 한 번에 보냅니다.&lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">details</span>&gt;

<span class="c">&lt;!-- 직접 만들 때 제목은 반드시 button 으로 --&gt;</span>
&lt;<span class="t">h3</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>&gt;
    수수료는 얼마인가요
  &lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">h3</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">hidden</span>&gt;카드 2.8%, 계좌이체 1.2% 입니다.&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("Enter · Space", "펴고 접습니다. 제목이 <code>&lt;button&gt;</code>이면 <b>저절로</b> 됩니다"),
    ("Tab", "포커스가 제목마다 멈추고, <b>접힌 본문</b>은 건너뜁니다"),
    ("↑ ↓", "아코디언 묶음일 때 제목 사이를 오갑니다"),
    ("<code>aria-expanded</code>", "펼침 상태를 알리며, 본문이 아니라 <b>제목 쪽</b>에 붙입니다"),
    ("<code>hidden=\"until-found\"</code>", "브라우저 찾기에 걸리면 접힌 글이 <b>저절로 펴집니다</b>"),
    ("확인하는 법", "Ctrl+F로 <b>접힌 본문 속 낱말</b>을 찾아봅니다"),
  ]),
  backend=rows([
    ("본문을 미리 준다", "본문을 펼 때마다 서버에서 받아 오면 아직 받지 않은 글은 <b>찾기도 인쇄도</b> 할 수 없습니다. 그래서 짧은 글은 처음부터 제목과 함께 보냅니다."),
    ("긴 글만 나중에", "본문이 아주 길 때만 펼 때 받아 오고, 그동안 <b>받는 중</b>이라는 표시를 둡니다."),
    ("펴진 상태", "어느 항목이 펴져 있었는지를 <b>주소</b>에 담아 두면 같은 상태로 공유할 수 있습니다."),
  ]),
  plat_lede="<b>웹에는 전용 태그</b>가 있고, 앱에는 비슷한 부품이 있습니다.",
  plats=plats([
    ("웹", "&lt;details&gt;",
     acc([("정산은 언제", "매주 수요일", True)], "", "", True, "110px"),
     "태그 하나로 만들 수 있고, <b>키보드 조작과 스크린 리더 지원</b>도 저절로 됩니다."),
    ("iOS", "DisclosureGroup",
     '''              <div class="phone" role="img" aria-label="iOS 접히는 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:8px;right:5px;top:36px;height:5px;border-radius:2px;background:var(--bg)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<code>DisclosureGroup</code>이 같은 일을 하고, 설정 화면에서 자주 볼 수 있습니다."),
    ("안드로이드", "Expandable",
     '''              <div class="phone" role="img" aria-label="안드로이드 접히는 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:3px;background:var(--bg)"></div></div></div>''',
     "Material에 <b>펼쳐지는 카드</b>가 있고, 펴고 접을 때 높이가 부드럽게 바뀝니다."),
  ]),
  plat_note="<code>&lt;details&gt;</code>는 웹에서 드물게 <b>따로 손대지 않아도 잘 동작하는</b> 부품으로, 키보드 조작과 스크린 리더 지원, 브라우저 찾기까지 함께 따라옵니다. 모양을 크게 바꿔야 해서 직접 만들 때도 <code>&lt;details&gt;</code>의 동작을 <b>똑같이 구현할 목록</b>으로 삼으면 빠뜨리는 것이 줄어듭니다. 앱에서는 펴고 접을 때 <b>높이가 바뀌는 움직임</b>에 신경을 쓰는데, 웹에서도 <a href=\"reducedmotion.html\">모션 줄이기</a>를 켠 사용자에게는 그 움직임을 꺼야 합니다.",
  siblings=siblings("accordion"),
  related='''        <li><a href="tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="treeview.html"><b>트리뷰</b><em>7부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="anchornav.html"><b>앵커 내비</b><em>7부</em></a></li>''',
)
