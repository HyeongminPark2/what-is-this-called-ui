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
  desc="앱바가 무엇이고 사이드바·탭과 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="화면 <b>꼭대기에 붙어 있는 띠</b>. 지금 어디인지(제목), 어디서 왔는지(뒤로), 여기서 뭘 할 수 있는지(동작)를 한 줄에 담습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>목록을 스크롤해 보세요.</b> 큰 제목이 올라가 사라지면 앱바가 얇아지면서 <b>제목을 받아 갑니다</b> —
          <b>접히는 앱바</b>(collapsing·large title)라 부릅니다. 꼭대기에 붙어 있어서(<b>스티키</b>)
          어디까지 내려가도 돌아갈 길이 남습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "앱바, 헤더, 상단바, 툴바"),
    ("영어", "app bar, header, top bar, navigation bar, toolbar"),
    ("같이 쓰는 말", "스크롤해도 붙어 있으면 <b>스티키 헤더</b>, 내용 위에 투명하게 떠 있으면 <b>오버레이 헤더</b>, 큰 제목이 접히는 것을 <b>접히는 앱바</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>내비게이션 바</b> — iOS 에서는 이게 앱바를 뜻하지만, 웹에서는 <b>메뉴 줄</b>로 알아듣기 쉽습니다.<br>"
     "<b>툴바</b> — 툴바는 <b>동작 버튼만</b> 모은 줄입니다. 제목과 뒤로가기가 있으면 앱바입니다.<br>"
     "<b>탭</b> — 탭은 같은 화면 안의 전환이고, 앱바는 화면의 틀입니다."),
  ]),
  axes=ax("앱바"),
  oneline="앱바는 <b>화면의 틀</b>입니다. 지금 어디인지와 나가는 길을 담되, <b>여기서 가장 자주 하는 일 한둘</b>만 올립니다.",
  states=states([
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;font-weight:700">거래 내역</div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="기본 앱바"), "기본", "제목과 동작. 가장 흔한 모습"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:4px"><span style="color:var(--accent)">‹</span><b>거래 내역</b></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="뒤로가 붙은 앱바"), "뒤로 포함", "하위 화면. <b>어디서 왔는지</b>를 왼쪽에 둔다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);padding:3px 5px;font-size:6px;font-weight:700;box-shadow:0 1px 3px rgba(0,0,0,.14)">거래 내역</div><div class="mini__bg" style="padding-top:16px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w40"></div></div>', bars="", label="접힌 앱바"), "접힘", "스크롤하면 얇아지고 <b>그림자가 생긴다</b> — 아래에 내용이 있다는 신호"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(0,0,0,.35),transparent);padding:4px 5px;font-size:7px;color:#fff;font-weight:700;z-index:2">사진</div><div style="position:absolute;inset:0;background:linear-gradient(145deg,#3a4a6b,#1d2230)"></div>', bars="", label="투명 오버레이 앱바"), "오버레이", "사진 위에 떠 있다. 글자가 묻히지 않게 <b>그라데이션</b>을 깐다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--accent-soft);border-bottom:1px solid var(--accent);padding:4px 5px;font-size:7px;color:var(--accent);font-weight:700;display:flex;gap:4px"><span>✕</span>3건 선택<span style="margin-left:auto">삭제</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="선택 모드 앱바"), "선택 모드", "여러 줄을 고르면 앱바가 통째로 바뀐다. <b>나가는 길(✕)</b>을 꼭 둔다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:3px"><span style="flex:1;background:var(--bg);border-radius:99px;padding:1px 4px;color:var(--fg-faint);font-size:6px">⌕ 검색</span><span style="color:var(--accent)">취소</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="검색 모드 앱바"), "검색 모드", "검색을 누르면 칸이 앱바를 차지한다. 역시 나가는 길이 필요하다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앱바", "app bar", "화면 폭을 다 쓰는 띠. 보통 44~64px 높이"),
    ("뒤로", "back", "<b>왼쪽 첫 자리.</b> 하위 화면이면 거의 언제나 여기 있다"),
    ("제목", "title", "지금 어디인지. 길면 말줄임하되 <b>앞쪽</b>을 남긴다"),
    ("동작", "actions", "여기서 가장 자주 하는 일. <b>둘까지</b>가 적당하다"),
    ("더 보기", "overflow menu", "나머지는 ⋯ 안으로. 자주 안 쓰는 것을 넣는다"),
    ("아래 내용", "content", "앱바 <b>밑으로 지나간다</b>. 그래서 스크롤해도 앱바가 남는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에 없는 것이 <b>세이프 에어리어</b>입니다. 폰에서는 앱바 위에 상태바(시계·배터리)가 겹치므로
          그만큼 위쪽 여백을 더 둬야 합니다 — 안 두면 제목이 시계에 가립니다.</p>''',
  do=ul([
    "화면마다 <b>지금 어디인지</b>를 알려야 할 때",
    "뒤로 갈 길이 필요할 때 — 하위 화면에서는 거의 언제나",
    "이 화면에서 가장 자주 하는 동작 한둘을 둘 때",
  ]),
  dont=ul([
    "버튼을 넷 이상 올리기 — 좁은 화면에서 먼저 무너집니다",
    "제목 없이 아이콘만 두기 — 어디인지 알 수 없습니다",
    "스크롤하면 사라지게 두기 — 돌아갈 길까지 같이 사라집니다",
    "앱바에 주 내비게이션을 전부 넣기 → 사이드바나 탭바가 할 일입니다",
  ]),
  instead='화면 사이를 오가면 <a href="sidebar.html">사이드바</a>나 <a href="bottomnav.html">바텀 탭바</a>, 같은 화면의 다른 면이면 <a href="tabs.html">탭</a>, 어디 있는지만 알리면 <a href="breadcrumb.html">브레드크럼</a>.',
  cases=cases([
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:7px;display:flex;gap:4px"><span style="color:var(--accent)">‹</span><b style="flex:1">거래 내역</b><span style="color:var(--fg-muted)">⋯</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="모바일 앱바 재현"),
     "모바일", "뒤로 · 제목 · 더 보기. 가장 엄격한 형태"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:6.5px;display:flex;gap:4px;align-items:center"><b>Paygate</b><span style="flex:1;background:var(--bg);border-radius:99px;padding:1px 4px;color:var(--fg-faint);font-size:5.5px">⌕ 검색</span><span style="width:9px;height:9px;border-radius:50%;background:var(--accent)"></span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w60"></div></div>', bars="", tall=False, label="데스크톱 앱바 재현"),
     "데스크톱", "로고 · 전역 검색 · 계정. 자리가 넓어 더 담는다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--accent-soft);padding:4px 5px;font-size:6.5px;color:var(--accent);font-weight:700;display:flex;gap:4px"><span>✕</span>3건<span style="margin-left:auto">삭제</span></div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="선택 모드 재현"),
     "선택 모드", "앱바가 통째로 바뀐다. 다른 화면이 아니라 <b>다른 모드</b>다"),
  ]),
  code_lede="<code>position: sticky</code> 한 줄이 앱바의 절반입니다. 나머지 절반은 <b>무엇을 올리지 않을지</b>입니다.",
  code='''&lt;<span class="t">header</span> <span class="a">class</span>=<span class="s">"nav-app"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"뒤로"</span>&gt;‹&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">h1</span>&gt;거래 내역&lt;/<span class="t">h1</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"검색"</span>&gt;⌕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">header</span>&gt;

<span class="c">/* 꼭대기에 붙인다. 아래 내용이 밑으로 지나간다 */</span>
.nav-app <span class="a">{</span> <span class="t">position</span>: sticky; <span class="t">top</span>: 0; <span class="t">z-index</span>: 20; <span class="a">}</span>

<span class="c">/* 폰에서는 상태바만큼 위 여백을 더 둔다 */</span>
<span class="t">padding-top</span>: <span class="a">calc</span>(12px + env(safe-area-inset-top));''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "페이지의 <b>첫 칸들</b>이다. 그래서 '본문으로 건너뛰기' 링크를 앞에 둔다"),
    ("제목", "<code>&lt;h1&gt;</code>으로 두면 스크린 리더의 제목 목록에 잡힌다"),
    ("아이콘 버튼", "글자가 없으면 <code>aria-label</code>이 꼭 필요하다. 툴팁도 같이 두면 좋다"),
    ("<kbd>Esc</kbd>", "선택 모드·검색 모드에서는 Esc 로 빠져나갈 수 있게 한다"),
    ("스티키", "스크롤해도 포커스가 앱바에 닿을 수 있어야 한다. 화면 밖으로 밀어내지 않는다"),
  ]),
  backend=rows([
    ("앱바 = 요청 컨텍스트", "제목·뒤로·동작이 전부 <b>지금 보고 있는 리소스</b>에서 나옵니다. 그 리소스가 없으면 앱바도 채울 수 없으니, 로딩 중에는 뼈대로 둡니다."),
    ("뒤로가기 = 계층 vs 이력", "앱바의 뒤로는 <b>상위 리소스</b>로, 브라우저 뒤로는 <b>이전 화면</b>으로 갑니다. 둘이 다를 수 있다는 걸 모르면 길을 잃는 사용자가 생깁니다."),
    ("동작 개수 = 권한", "권한에 따라 버튼이 줄어듭니다. 숨길지 비활성할지를 정해야 하고, <b>서버가 무엇을 내려 줄지</b>와 묶입니다."),
    ("선택 모드 = 일괄 작업", "고른 것들에 한꺼번에 명령합니다. '전부 선택'이 조건인지 ID 목록인지에 따라 요청 모양이 달라집니다."),
  ]),
  plat_lede="이 부품은 플랫폼마다 이름이 가장 많이 엇갈립니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--surface);border-bottom:1px solid var(--line);padding:4px 5px;font-size:6.5px;font-weight:700">Paygate</div><div class="mini__bg" style="padding-top:18px"><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="웹 헤더 재현"),
     "<b>헤더</b>(header) · <code>&lt;header&gt;</code> 요소가 있지만 모양 규칙은 없습니다. 로고·전역 내비·검색이 함께 올라가는 일이 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:4px 7px;border-bottom:1px solid var(--line);display:flex;gap:4px;font-size:8px"><span style="color:#0a84ff">‹ 뒤로</span><b style="flex:1;text-align:center">거래</b><span style="color:#0a84ff">⋯</span></div>', "iOS 내비게이션 바 재현"),
     "<b>내비게이션 바</b>(Navigation bar) · 제목이 <b>가운데</b>이고 뒤로 버튼에 <b>이전 화면 이름</b>이 붙습니다. 큰 제목(Large title)이 접히는 방식이 표준입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:5px 7px;display:flex;gap:5px;font-size:8px"><span>←</span><b style="flex:1">거래</b><span style="color:var(--fg-muted)">⌕</span><span style="color:var(--fg-muted)">⋮</span></div>', "안드로이드 톱 앱 바 재현"),
     "<b>톱 앱 바</b>(Top app bar) · 제목이 <b>왼쪽</b>입니다. Small / Medium / Large / Center-aligned 네 가지로 정리돼 있습니다."),
  ]),
  plat_note="제목 위치가 <b>iOS 는 가운데, 안드로이드는 왼쪽</b>입니다. 같은 시안을 양쪽에 그대로 쓰면 한쪽은 반드시 어색해집니다. 그리고 iOS 의 \"내비게이션 바\"는 이 앱바를 뜻하지, 웹에서 말하는 메뉴 줄이 아닙니다.",
  siblings=siblings("appbar"),
  related='''        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><span class="na"><b>세이프 에어리어</b><em>11부</em></span></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>''',
)
