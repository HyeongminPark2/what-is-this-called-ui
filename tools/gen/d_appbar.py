# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

CARD = 'background:var(--surface);border:1px solid var(--line);border-radius:8px'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="%s;display:flex;align-items:center;gap:40px;padding:14px 26px">
                  <span data-pin="2" style="font-size:15px;color:var(--accent);line-height:1">‹</span>
                  <span class="pin-out" data-pin="3" style="flex:1;font-size:12.5px;font-weight:750">거래 내역</span>
                  <span data-pin="4" style="font-size:12px;color:var(--fg-muted)">⌕</span>
                  <span class="pin-tr" data-pin="5" style="font-size:12px;color:var(--fg-muted)">⋯</span>
                </div>
                <div class="pin-out" data-pin="6" style="border-left:1px solid var(--line);border-right:1px solid var(--line);border-bottom:1px solid var(--line);border-radius:0 0 8px 8px;padding:14px 26px;font-size:11px;color:var(--fg-muted)">아래 내용은 이 띠 밑으로 지나갑니다</div>
              </div>''' % CARD

D = dict(
  slug="appbar", ko="앱바 · 헤더", en="App bar · Header · Top bar",
  desc="앱바가 무엇인지, 사이드바·탭과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="앱바는 화면 <b>맨 위에 붙어 있는 가로 띠</b>입니다. 지금 어느 화면인지(제목), 어디서 왔는지(뒤로), 이 화면에서 무엇을 할 수 있는지(동작)를 한 줄에 담습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>목록을 스크롤해 보세요.</b> 큰 제목이 위로 올라가 사라지면 앱바가 얇아지면서 <b>그 제목을 앱바 안에 띄웁니다</b>.
          이런 앱바를 <b>접히는 앱바</b>(collapsing·large title)라고 부릅니다. 앱바는 화면 맨 위에 붙어 있기 때문에(<b>스티키</b>)
          목록을 아무리 내려도 뒤로 버튼이 계속 보입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "앱바, 헤더, 상단바, 툴바"),
    ("영어", "app bar, header, top bar, navigation bar, toolbar"),
    ("같이 쓰는 말", "스크롤해도 맨 위에 붙어 있는 것은 <b>스티키 헤더</b>, 내용 위에 투명하게 떠 있는 것은 <b>오버레이 헤더</b>, 큰 제목이 스크롤에 따라 접히는 것은 <b>접히는 앱바</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>내비게이션 바</b> — iOS에서는 이 말이 앱바를 뜻하지만, 웹에서는 링크를 늘어놓은 <b>메뉴 줄</b>로 알아듣기 쉽습니다.<br>"
     "<b>툴바</b> — 툴바는 <b>동작 버튼만</b> 모아 둔 줄입니다. 제목과 뒤로가기가 함께 있으면 툴바가 아니라 앱바입니다.<br>"
     "<b>탭</b> — 탭은 같은 화면 안에서 내용을 바꿔 보여 주는 부품이고, 앱바는 화면 맨 위에 늘 붙어 있는 틀입니다."),
  ]),
  axes=ax("앱바"),
  oneline="앱바는 모든 화면 맨 위에 붙는 <b>틀</b>입니다. 지금 어느 화면인지와 나가는 길을 담고, 동작 버튼은 <b>이 화면에서 가장 자주 하는 일 한두 개</b>만 올립니다.",
  states=states([
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;font-weight:700">거래 내역</div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="기본 앱바"), "가장 흔한 기본 모습", "제목과 동작 버튼만 있는, 가장 흔한 모습입니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:4px"><span style="color:var(--accent)">‹</span><b>거래 내역</b></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="뒤로가 붙은 앱바"), "뒤로 버튼이 붙었을 때", "하위 화면에서는 <b>어디서 왔는지</b>를 알려 주는 뒤로 버튼을 왼쪽에 둡니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);padding:3px 5px;font-size:6px;font-weight:700;box-shadow:0 1px 3px rgba(0,0,0,.14)">거래 내역</div><div class="mini__bg" style="padding-top:16px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w40"></div></div>', bars="", label="접힌 앱바"), "스크롤해서 접혔을 때", "스크롤하면 앱바가 얇아지고 아래에 <b>그림자가 생깁니다</b>. 그림자는 앱바 밑으로 내용이 지나가고 있다는 표시입니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(0,0,0,.35),transparent);padding:4px 5px;font-size:7px;color:#fff;font-weight:700;z-index:2">사진</div><div style="position:absolute;inset:0;background:linear-gradient(145deg,#3a4a6b,#1d2230)"></div>', bars="", label="투명 오버레이 앱바"), "사진 위에 겹쳐 띄울 때", "앱바가 사진 위에 투명하게 떠 있습니다. 사진 때문에 글자가 안 보이지 않도록 뒤에 어두운 <b>그라데이션</b>을 깝니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--accent-soft);border-bottom:1px solid var(--accent);padding:4px 5px;font-size:7px;color:var(--accent);font-weight:700;display:flex;gap:4px"><span>✕</span>3건 선택<span style="margin-left:auto">삭제</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="선택 모드 앱바"), "여러 줄을 고르는 선택 모드일 때", "목록에서 여러 줄을 고르면 앱바 전체가 선택용으로 바뀝니다. 선택을 끝낼 수 있도록 <b>나가는 버튼(✕)</b>을 꼭 둡니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:3px"><span style="flex:1;background:var(--bg);border-radius:99px;padding:1px 4px;color:var(--fg-faint);font-size:6px">⌕ 검색</span><span style="color:var(--accent)">취소</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="검색 모드 앱바"), "검색 칸을 연 검색 모드일 때", "검색 버튼을 누르면 검색 칸이 앱바 전체를 차지합니다. 이때도 검색을 끝내고 돌아갈 버튼이 필요합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앱바", "app bar", "화면 폭 전체를 차지하는 띠입니다. 높이는 보통 44~64px입니다"),
    ("뒤로", "back", "<b>왼쪽 첫 자리</b>에 둡니다. 하위 화면이면 거의 언제나 이 자리에 있습니다"),
    ("제목", "title", "지금 어느 화면인지 알려 줍니다. 제목이 길면 말줄임표로 줄이되 <b>앞부분</b>을 남깁니다"),
    ("동작", "actions", "이 화면에서 가장 자주 하는 일을 버튼으로 둡니다. <b>두 개까지</b>가 적당합니다"),
    ("더 보기", "overflow menu", "자주 쓰지 않는 나머지 동작은 ⋯ 버튼 안의 메뉴로 넣습니다"),
    ("아래 내용", "content", "스크롤하면 내용이 앱바 <b>밑으로 지나갑니다</b>. 그래서 아무리 스크롤해도 앱바는 그 자리에 남습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 없지만 함께 챙겨야 하는 것이 <b>세이프 에어리어</b>입니다. 폰에서는 앱바 위에 시계와 배터리를 보여 주는 상태바가 겹치기 때문에,
          상태바 높이만큼 위쪽 여백을 더 둬야 합니다. 이 여백을 두지 않으면 앱바 제목이 시계에 가려집니다.</p>''',
  do=ul([
    "화면마다 <b>지금 어디인지</b>를 알려야 할 때",
    "뒤로 갈 길이 필요할 때. 하위 화면에서는 거의 언제나 필요합니다",
    "이 화면에서 가장 자주 하는 동작 한두 개를 둘 때",
  ]),
  dont=ul([
    "버튼을 네 개 이상 올릴 때. 화면이 좁으면 버튼과 제목을 한 줄에 다 놓을 자리가 모자랍니다",
    "제목 없이 아이콘만 둘 때. 지금 어느 화면인지 알 수 없습니다",
    "스크롤하면 앱바가 사라지게 둘 때. 앱바와 함께 뒤로 버튼까지 사라집니다",
    "앱바에 주 내비게이션을 전부 넣을 때. 화면 사이를 오가는 메뉴는 사이드바나 탭바에 둡니다",
  ]),
  instead='여러 화면 사이를 오가는 길이 필요하면 <a href="sidebar.html">사이드바</a>나 <a href="bottomnav.html">바텀 탭바</a>를 쓰고, 같은 화면의 다른 면을 보여 주려면 <a href="tabs.html">탭</a>을 씁니다. 지금 어디에 있는지만 알리면 되는 경우에는 <a href="breadcrumb.html">브레드크럼</a>으로 충분합니다.',
  cases=cases([
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:4px"><span style="color:var(--accent)">‹</span><b style="flex:1">거래 내역</b><span style="color:var(--fg-muted)">⋯</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="모바일 앱바 재현"),
     "모바일 앱의 앱바", "뒤로 버튼과 제목, 더 보기 버튼만 둡니다. 화면이 좁아서 올릴 수 있는 것이 가장 적습니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:6.5px;display:flex;gap:4px;align-items:center"><b>Paygate</b><span style="flex:1;background:var(--bg);border-radius:99px;padding:1px 4px;color:var(--fg-faint);font-size:5.5px">⌕ 검색</span><span style="width:9px;height:9px;border-radius:50%;background:var(--accent)"></span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w60"></div></div>', bars="", tall=False, label="데스크톱 앱바 재현"),
     "데스크톱 웹의 헤더", "로고와 전역 검색 칸, 계정 메뉴를 둡니다. 자리가 넓어서 모바일보다 많이 담습니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--accent-soft);padding:4px 5px;font-size:6.5px;color:var(--accent);font-weight:700;display:flex;gap:4px"><span>✕</span>3건<span style="margin-left:auto">삭제</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="선택 모드 재현"),
     "목록에서 여러 줄을 골랐을 때", "앱바 전체가 바뀌지만 다른 화면으로 넘어간 것이 아니라 같은 화면의 <b>다른 모드</b>입니다"),
  ]),
  code_lede="앱바를 맨 위에 붙이는 일은 <code>position: sticky</code> 한 줄로 끝납니다. 코드보다 신경 써야 할 것은 <b>무엇을 앱바에 올리지 않을지</b> 정하는 일입니다.",
  code='''&lt;<span class="t">header</span> <span class="a">class</span>=<span class="s">"nav-app"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"뒤로"</span>&gt;‹&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">h1</span>&gt;거래 내역&lt;/<span class="t">h1</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"검색"</span>&gt;⌕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">header</span>&gt;

<span class="c">/* 맨 위에 붙인다. 아래 내용은 앱바 밑으로 지나간다 */</span>
.nav-app <span class="a">{</span> <span class="t">position</span>: sticky; <span class="t">top</span>: 0; <span class="t">z-index</span>: 20; <span class="a">}</span>

<span class="c">/* 폰에서는 상태바만큼 위 여백을 더 둔다 */</span>
<span class="t">padding-top</span>: <span class="a">calc</span>(12px + env(safe-area-inset-top));''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "앱바의 버튼들은 페이지에서 <b>가장 먼저</b> 포커스를 받습니다. 그래서 키보드 사용자가 앱바를 건너뛸 수 있도록 '본문으로 건너뛰기' 링크를 맨 앞에 둡니다"),
    ("화면 제목을 달 때", "<code>&lt;h1&gt;</code>으로 두면 스크린 리더의 제목 목록에 나타납니다"),
    ("아이콘만 있는 버튼", "글자가 없는 버튼에는 <code>aria-label</code>이 꼭 필요합니다. 툴팁도 함께 두면 좋습니다"),
    ("<kbd>Esc</kbd>", "선택 모드나 검색 모드에서는 <kbd>Esc</kbd>로 빠져나갈 수 있게 합니다"),
    ("앱바를 맨 위에 붙였을 때", "스크롤한 뒤에도 키보드 포커스가 앱바로 갈 수 있어야 합니다. 앱바를 화면 밖으로 밀어내지 않습니다"),
  ]),
  backend=rows([
    ("지금 보는 리소스로 앱바 채우기", "앱바의 제목과 뒤로 버튼, 동작 버튼은 모두 <b>지금 보고 있는 리소스</b>의 데이터로 채웁니다. 리소스를 아직 받지 못했으면 앱바도 채울 수 없으므로, 로딩 중에는 자리만 잡아 둔 뼈대 모양으로 보여 줍니다."),
    ("계층을 따르는 뒤로와 이력을 따르는 뒤로", "앱바의 뒤로 버튼은 <b>상위 리소스</b>로 가고, 브라우저의 뒤로 버튼은 <b>직전에 본 화면</b>으로 갑니다. 두 목적지가 다를 수 있다는 점을 설계에서 놓치면 사용자가 예상과 다른 화면에 도착합니다."),
    ("권한에 따라 달라지는 동작 개수", "사용자 권한에 따라 보여 줄 버튼이 줄어듭니다. 권한이 없는 버튼을 숨길지 비활성으로 둘지 정해야 하고, 그 결정은 <b>서버가 어떤 동작 목록을 내려 줄지</b>와 함께 정해집니다."),
    ("선택 모드에서 보내는 일괄 작업", "선택 모드에서는 고른 항목 전체에 명령 하나를 보냅니다. '전부 선택'을 검색 조건으로 보낼지 ID 목록으로 보낼지에 따라 요청 형식이 달라집니다."),
  ]),
  plat_lede="앱바는 플랫폼마다 부르는 이름이 특히 많이 엇갈리는 부품입니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:6.5px;font-weight:700">Paygate</div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="웹 헤더 재현"),
     "<b>헤더</b>(header) · <code>&lt;header&gt;</code> 요소는 있지만 모양을 정한 규칙은 없습니다. 로고와 전역 내비게이션, 검색 칸을 함께 올리는 경우가 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:4px 7px;border-bottom:1px solid var(--line);display:flex;gap:4px;font-size:8px"><span style="color:#0a84ff">‹ 뒤로</span><b style="flex:1;text-align:center">거래</b><span style="color:#0a84ff">⋯</span></div>', "iOS 내비게이션 바 재현"),
     "<b>내비게이션 바</b>(Navigation bar) · 제목을 <b>가운데</b>에 두고, 뒤로 버튼 옆에 <b>이전 화면 이름</b>을 적습니다. 스크롤하면 큰 제목(Large title)이 접히는 방식이 표준입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:5px 7px;display:flex;gap:5px;font-size:8px"><span>←</span><b style="flex:1">거래</b><span style="color:var(--fg-muted)">⌕</span><span style="color:var(--fg-muted)">⋮</span></div>', "안드로이드 톱 앱 바 재현"),
     "<b>톱 앱 바</b>(Top app bar) · 제목을 <b>왼쪽</b>에 둡니다. Small / Medium / Large / Center-aligned 네 가지 형태가 정해져 있습니다."),
  ]),
  plat_note="제목 위치는 <b>iOS가 가운데, 안드로이드가 왼쪽</b>입니다. 그래서 같은 시안을 두 플랫폼에 그대로 쓰면 한쪽에서는 어색해 보입니다. 또 iOS에서 말하는 \"내비게이션 바\"는 웹의 메뉴 줄이 아니라 이 앱바를 가리킵니다.",
  siblings=siblings("appbar"),
  related='''        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><a href="safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>''',
)
