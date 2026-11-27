# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
  desc="제목만 보이고 본문은 접어 두는 부품. 찾기에 안 걸리는 문제와 한 번에 하나만 열기.",
  lede="긴 글을 <b>제목만 남기고</b> 접습니다. 대신 접힌 글은 <b>찾기에 안 걸립니다</b>.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>접힌 글은 화면에서 보이지 않습니다. 그래서 브라우저의 찾기(Ctrl+F)도 못 찾습니다 —
          찾는 말을 넣어 보면 데모가 <b>지금 보이는 글에서 몇 건</b>,
          <b>접힌 글 속에 몇 건</b>인지 나눠서 셉니다.<br>
          긴 약관이나 문서를 통째로 접어 두면 <b>검색으로 영영 못 찾는</b> 글이 됩니다.
          <b>한 번에 하나만 열기</b>는 비교를 막습니다 —
          꼭 필요한 자리가 아니면 <b>여러 개가 같이 열리게</b> 두는 편이 낫습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "접히는 글, 아코디언, 펼침, 더 보기"),
    ("영어", "accordion, disclosure, collapsible, expander"),
    ("같이 쓰는 말",
     "하나만 접었다 펴는 것은 <b>디스클로저</b>(disclosure), "
     "여럿을 묶어 한 번에 하나만 열리게 한 것이 좁은 뜻의 <b>아코디언</b>입니다. "
     "HTML 에는 <code>&lt;details&gt;</code>·<code>&lt;summary&gt;</code> 가 있어 "
     "자바스크립트 없이도 됩니다."),
    ("자주 잘못 부름",
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 <b>한 번에 하나만</b> 보이고 자리를 안 늘립니다.<br>"
     "<b>트리뷰</b> — <a href=\"treeview.html\">트리뷰</a>는 <b>길을 펴는</b> 것이고 이건 <b>내용을 펴는</b> 것입니다.<br>"
     "<b>드롭다운</b> — 드롭다운은 <b>위에 떠서</b> 자리를 안 차지합니다."),
  ]),
  axes=ax("접히는 글"),
  oneline="<b>접기 전에 물어보세요 — 이 글을 찾아야 하는 사람이 있나.</b> 있으면 접으면 안 됩니다.",
  states=states([
    (acc(Q, "하나 펴짐", "제목은 늘 보인다", True), "기본", "<b>하나만</b> 펴 둔다"),
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "카드 2.8% 입니다.", True), ("환불은", "", False)],
         "여럿 펴짐", "비교할 수 있다", True),
     "여럿 열림", "<b>나란히</b> 볼 수 있다"),
    (acc([("정산은 언제", "", False), ("수수료는", "", False), ("환불은", "", False)], "다 접힘", "찾기로는 안 잡힌다", False),
     "다 접힘", "<b>본문이 안 보인다</b>"),
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "", False)], "한 번에 하나", "다른 걸 열면 이게 접힌다", False),
     "하나만 열림", "<b>비교를 막는다</b>"),
    (acc([("정산 안내", "접기에는 너무 중요한 글입니다.", True)], "안 접는 글", "찾아야 하는 글은 펴 둔다", True),
     "접지 말 것", "<b>중요한 글</b>은 편다"),
    (acc([("ㄱ", "", False), ("ㄴ", "", False), ("ㄷ", "", False), ("ㄹ", "", False)], "너무 많음", "제목만 스무 줄", False),
     "항목이 많음", "<b>목록처럼</b> 보인다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("제목", "<code>&lt;button&gt;</code>", "<b>누를 수 있어야</b> 한다"),
    ("<code>aria-expanded</code>", "폈나 접었나", "삼각형의 <b>소리 버전</b>"),
    ("<code>aria-controls</code>", "무엇을 여나", "제목과 본문을 <b>묶는다</b>"),
    ("접힌 글", "안 찾아짐", "<b>검색의 사각지대</b>"),
    ("하나만 열기", "비교 막힘", "<b>꼭 필요할 때만</b>"),
    ("<code>&lt;details&gt;</code>", "기본 제공", "스크립트 <b>없이도</b> 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          접기는 <b>화면을 깔끔하게 만드는 가장 쉬운 방법</b>이라 과하게 쓰입니다.
          그런데 접는 순간 그 글은 <b>Ctrl+F 로도, 페이지 검색으로도</b> 안 잡힙니다 —
          '분명 어딘가에 적혀 있었는데'가 벌어지는 자리입니다.
          그래서 <b>찾아야 하는 글</b>(약관의 핵심, 수수료율, 환불 규정)은 접지 않습니다.<br>
          크롬 계열에는 <code>hidden="until-found"</code> 가 생겨
          <b>찾기에 걸리면 저절로 펴지게</b> 할 수 있습니다 —
          아직 모든 브라우저에 있지는 않지만, 접어야 한다면 이 길을 먼저 봅니다.</p>''',
  do=ul([
    "제목을 <b><code>&lt;button&gt;</code></b> 으로 두고 <code>aria-expanded</code> 붙이기",
    "<b>여러 개가 같이</b> 열리게 두기",
    "찾아야 하는 글은 <b>접지 않기</b>",
  ]),
  dont=ul([
    "<code>&lt;div&gt;</code> 에 <code>onclick</code> 만 달기 — <b>키보드로 못 연다</b>",
    "기본값으로 <b>전부 접어</b> 두기 — 무엇이 있는지도 모른다",
    "<b>한 번에 하나만</b> 열리게 하기(이유 없이) — 비교를 막는다",
    "항목을 스무 개씩 두기 — 그건 <b>목록</b>이지 아코디언이 아니다",
  ]),
  instead='한 번에 하나만 보이면 <a href="tabs.html">탭</a>, 길을 펴면 <a href="treeview.html">트리뷰</a>, 위에 떠서 열리면 <a href="popover.html">팝오버</a>, 긴 문서의 길잡이는 <a href="anchornav.html">앵커 내비</a>.',
  cases=cases([
    (acc([("정산은 언제", "매주 수요일에 보냅니다.", True), ("수수료는", "", False)], "자주 묻는 질문", "", True),
     "자주 묻는 질문", "<b>가장 맞는</b> 자리"),
    (acc([("자세한 조건 보기", "최소 주문 금액 10,000원", True)], "더 보기", "", True),
     "'더 보기'", "<b>곁들이 설명</b>을 접는다"),
    (acc([("고급 설정", "", False)], "고급 설정", "", True),
     "고급 설정", "대부분 <b>안 건드리는</b> 값들"),
  ]),
  code_lede="가장 쉬운 길은 <code>&lt;details&gt;</code> 입니다. 모양을 많이 바꿔야 할 때만 직접 만듭니다.",
  code='''<span class="c">&lt;!-- 스크립트 없이도 되고 키보드도 저절로 된다 --&gt;</span>
&lt;<span class="t">details</span>&gt;
  &lt;<span class="t">summary</span>&gt;정산은 언제 들어오나요&lt;/<span class="t">summary</span>&gt;
  &lt;<span class="t">p</span>&gt;매주 수요일에 지난주 매출을 한 번에 보냅니다.&lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">details</span>&gt;

<span class="c">&lt;!-- 직접 만들 때 — 제목은 반드시 button --&gt;</span>
&lt;<span class="t">h3</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>&gt;
    수수료는 얼마인가요
  &lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">h3</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">hidden</span>&gt;카드 2.8%, 계좌이체 1.2% 입니다.&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("Enter · Space", "펴고 접는다 — <code>&lt;button&gt;</code> 이면 <b>저절로</b> 된다"),
    ("Tab", "제목마다 멈춘다. <b>접힌 본문</b>은 건너뛴다"),
    ("↑ ↓", "제목 사이를 옮긴다(아코디언 묶음일 때)"),
    ("<code>aria-expanded</code>", "펴짐 상태. <b>제목 쪽</b>에 붙인다"),
    ("<code>hidden=\"until-found\"</code>", "브라우저 찾기에 걸리면 <b>저절로 펴진다</b>"),
    ("확인하는 법", "Ctrl+F 로 <b>접힌 본문의 낱말</b>을 찾아 본다"),
  ]),
  backend=rows([
    ("본문을 미리 준다", "펼 때마다 받아 오면 <b>찾기도 인쇄도</b> 안 됩니다 — 짧은 글은 처음부터 같이 보냅니다."),
    ("긴 글만 나중에", "본문이 아주 길면 펼 때 받아 오되, <b>받는 중</b> 표시를 둡니다."),
    ("펴진 상태", "어느 항목이 펴져 있었는지는 <b>주소</b>에 담으면 공유할 수 있습니다."),
  ]),
  plat_lede="<b>웹에는 전용 태그</b>가 있고, 앱에는 비슷한 꼴이 있습니다.",
  plats=plats([
    ("웹", "&lt;details&gt;",
     acc([("정산은 언제", "매주 수요일", True)], "", "", True, "110px"),
     "태그 하나로 끝납니다 — <b>키보드와 소리까지</b> 저절로 됩니다."),
    ("iOS", "DisclosureGroup",
     '''              <div class="phone" role="img" aria-label="iOS 접히는 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:8px;right:5px;top:36px;height:5px;border-radius:2px;background:var(--bg)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<code>DisclosureGroup</code> 이 같은 일을 합니다. 설정 화면에서 자주 보입니다."),
    ("안드로이드", "Expandable",
     '''              <div class="phone" role="img" aria-label="안드로이드 접히는 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:3px;background:var(--bg)"></div></div></div>''',
     "Material 에 <b>펼쳐지는 카드</b>가 있습니다. 펴고 접을 때 높이가 부드럽게 움직입니다."),
  ]),
  plat_note="<code>&lt;details&gt;</code> 는 웹에서 드물게 <b>공짜로 잘 만들어진</b> 부품입니다 — 키보드·소리·브라우저 찾기까지 따라옵니다. 모양을 크게 바꿔야 해서 직접 만들 때도, 그 동작을 <b>흉내 내야 할 목록</b>으로 삼으면 빠뜨리는 것이 줄어듭니다. 앱 쪽은 펴고 접을 때 <b>높이 움직임</b>에 신경을 쓰는데, 웹에서도 <a href=\"reducedmotion.html\">모션 줄이기</a>를 켠 사람에게는 그 움직임을 꺼야 합니다.",
  siblings=siblings("accordion"),
  related='''        <li><a href="tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="treeview.html"><b>트리뷰</b><em>7부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="anchornav.html"><b>앵커 내비</b><em>7부</em></a></li>''',
)
