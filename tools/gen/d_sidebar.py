# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:14px 26px 16px">
                  <div class="pin-out" data-pin="2" style="font-size:9.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--fg-muted);font-weight:700;margin-bottom:16px">운영</div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:40px;background:var(--accent-soft);border-radius:5px;padding:8px 10px;margin-bottom:18px">
                    <span data-pin="4" style="width:15px;height:15px;border-radius:4px;background:var(--accent);flex:none"></span>
                    <span class="pin-out" data-pin="5" style="flex:1;font-size:11.5px;color:var(--accent);font-weight:700">거래 내역</span>
                    <span class="pin-tr" data-pin="6" style="font-size:10px;color:var(--fg-muted)">584</span>
                  </div>
                  <div class="pin-out" data-pin="7" style="display:flex;align-items:center;gap:40px;padding:0 10px">
                    <span style="width:15px;height:15px;border-radius:4px;background:var(--line-strong);flex:none"></span>
                    <span style="font-size:11.5px;color:var(--fg-muted)">정산</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="sidebar", ko="사이드바 내비게이션", en="Sidebar navigation",
  desc="사이드바 내비게이션이 무엇인지, 드로어·바텀 탭바와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="사이드바 내비게이션은 화면 <b>옆에 늘 붙어 있는</b> 메뉴입니다. 지금 어디인지와 갈 수 있는 곳이 한눈에 보이고, 세로로 늘어놓기 때문에 항목이 열 개를 넘어도 모두 담을 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>사이드바는 <b>늘 화면에 보입니다.</b> 같은 메뉴가 좁은 화면에서 숨어 있다가 버튼을 눌러야 나오면 그건 사이드바가 아니라 <a href="drawer.html">드로어</a>입니다.<br>
          <b>아이콘만 보기</b>를 눌러 보세요. 이름을 숨기고 아이콘만 남겨 폭을 줄인 <b>레일</b>(rail)로 바뀌는데,
          아이콘만으로는 어느 화면인지 알기 어려우므로 툴팁이나 글자를 함께 둬야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "사이드바, 측면 내비게이션, 좌측 메뉴"),
    ("영어", "sidebar navigation, side nav, navigation rail"),
    ("같이 쓰는 말", "아이콘만 남겨 폭을 좁힌 것은 <b>레일</b>(rail), 하위 항목을 펼치고 접을 수 있는 것은 <b>접이식</b>(collapsible), 항목 묶음의 제목은 <b>섹션 헤더</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>드로어</b> — 늘 보이면 사이드바이고, 숨어 있다가 옆에서 밀려 나오면 드로어입니다. <b>같은 메뉴가 화면 폭에 따라 사이드바가 되기도 하고 드로어가 되기도 합니다.</b><br>"
     "<b>메뉴</b> — 메뉴는 실행할 동작을 고르는 부품이고, 사이드바는 다른 화면으로 옮겨 가는 부품입니다.<br>"
     "<b>패널</b> — 패널은 보조 내용을 담는 칸이고, 사이드바는 다른 화면으로 가는 링크를 담습니다."),
  ]),
  axes=ax("사이드바"),
  oneline="사이드바는 <b>늘 보이는 내비게이션</b>입니다. 화면 폭 일부를 차지하는 대신 '지금 어디인지'와 '어디로 갈 수 있는지'를 계속 보여 줍니다.",
  states=states([
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin-bottom:3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", label="기본 사이드바"), "기본", "현재 위치가 강조돼 있고, 메뉴가 <b>늘 보입니다</b>"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:20%;background:var(--bg);border-right:1px solid var(--line);padding:5px 3px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto"></div></div>', bars="", label="레일"), "레일", "아이콘만 남겨 폭을 줄이면서도 <b>다른 화면으로 가는 링크는 그대로 둡니다</b>"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">운영 ▾</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin:2px 0 0 5px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;margin-left:5px">정산</div></div>', bars="", label="접이식 사이드바"), "접이식", "묶음을 펼치고 접을 수 있습니다. 깊이는 <b>두 단</b>까지만 둡니다"),
    (mini('<div class="mini__scrim" style="padding:0"><div class="mini__drawer"><b>메뉴</b><i class="on">거래 내역</i><i>정산</i></div></div>', bars="684", label="좁은 화면에서 드로어가 된 모습"), "좁은 화면", "같은 메뉴가 <b>드로어</b> 모양으로 바뀝니다. 메뉴 내용은 그대로이고 보이는 방식만 달라집니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;display:flex"><span style="flex:1">거래 내역</span><span>584</span></div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;display:flex"><span style="flex:1">정산</span><span style="background:var(--danger);color:#fff;border-radius:99px;padding:0 3px;font-size:4.5px">12</span></div></div>', bars="", label="숫자가 붙은 사이드바"), "숫자 · 배지", "단순한 개수는 흐리게, <b>처리할 것</b>은 빨갛게 표시하고 두 표시를 섞어 쓰지 않습니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-faint);padding:1px 3px;opacity:.5">정산 🔒</div></div>', bars="", label="권한이 없는 항목"), "권한 없음", "권한이 없는 항목은 숨길지 흐리게 둘지 정해야 합니다. <b>흐리게 두면 그런 화면이 있다는 사실은 사용자가 알게 됩니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("사이드바", "sidebar", "화면 높이 전체를 씁니다. 폭은 보통 200~260px입니다"),
    ("섹션 헤더", "section header", "항목이 일곱 개를 넘으면 묶음으로 나누고 묶음마다 제목을 붙입니다. 항목보다 작고 흐린 글자로 씁니다"),
    ("현재 항목", "current item", "<b>배경과 글자색으로</b> 현재 위치를 알리고, <code>aria-current=\"page\"</code>도 함께 답니다"),
    ("아이콘", "icon", "항목을 눈으로 빨리 찾게 해 줍니다. 레일에서는 아이콘만 남습니다"),
    ("이름", "label", "짧게 씁니다. 이름이 한 줄을 넘기면 묶음을 다시 나눌 때가 된 것입니다"),
    ("숫자", "count · badge", "항목의 개수나 처리할 건수를 보여 줍니다. 보여 줄 숫자가 없으면 두지 않습니다"),
    ("다른 항목", "item", "누르는 영역은 40px 이상으로 잡습니다. 글자만이 아니라 줄 전체가 눌려야 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          사이드바는 <b>모든 화면에 함께 나옵니다.</b> 그래서 사이드바에 항목 하나를 더하면 그 항목이 모든 화면에 보이게 되므로,
          화면 하나를 새로 만드는 것보다 더 신중하게 정해야 합니다. 항목이 열 개를 넘기면 새 항목을 더하기 전에 묶음부터 다시 나눕니다.</p>''',
  do=ul([
    "갈 곳이 <b>다섯 개를 넘을</b> 때. 탭바로는 다 담을 수 없습니다",
    "넓은 화면에서 내비게이션을 늘 보여 주고 싶을 때",
    "묶음과 항목, 두 단으로 된 내비게이션을 둘 때",
  ]),
  dont=ul([
    "좁은 화면에서도 그대로 둘 때. 사이드바가 자리를 차지해 내용을 볼 자리가 없어지므로 <b>드로어로 바꿉니다</b>",
    "항목을 스무 개 넘게 늘어놓을 때. 묶음으로 나누거나 검색을 붙입니다",
    "저장·삭제 같은 동작을 섞어 넣을 때. 사이드바에는 <b>다른 화면으로 가는 링크</b>만 담습니다",
    "깊이가 세 단 이상일 때. 묶음을 여러 번 접었다 펴다 보면 지금 어디에 있는지 놓칩니다",
  ]),
  instead='좁은 화면이면 <a href="drawer.html">드로어</a>, 폰이면 <a href="bottomnav.html">바텀 탭바</a>, 같은 화면의 다른 면이면 <a href="tabs.html">탭</a>, 동작이면 <a href="popover.html">드롭다운 메뉴</a>.',
  cases=cases([
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5px;color:var(--fg-muted);margin-bottom:2px">운영</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", tall=False, label="관리 도구 사이드바 재현"),
     "관리 도구", "사이드바를 가장 흔하게 쓰는 곳입니다. 항목을 묶음 제목으로 나눕니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:20%;background:var(--bg);border-right:1px solid var(--line);padding:5px 3px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto"></div></div>', bars="", tall=False, label="레일 재현"),
     "레일", "작업 화면에서 자리를 아낄 때 씁니다. 아이콘만 남으므로 툴팁이 꼭 필요합니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:46%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">▾ 팀 문서</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin-left:5px">회고 초안</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;margin-left:5px">온보딩</div></div>', bars="", tall=False, label="트리형 사이드바 재현"),
     "트리형", "문서 도구에서 씁니다. 문서 계층을 펼치고 접기 때문에 사실상 <b>트리뷰</b>와 같습니다"),
  ]),
  code_lede="핵심은 <code>&lt;nav&gt;</code>와 <code>aria-current</code> 두 가지입니다. 색을 구별하기 어려운 사용자나 스크린 리더 사용자도 알 수 있도록, 지금 어디인지를 <b>색 말고도</b> 알려야 합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"주 메뉴"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/tx"</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;거래 내역&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settle"</span>&gt;정산&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">/* 좁아지면 드로어로 바꾼다. 마크업은 같고 모양만 다르다 */</span>
@media (max-width: 860px) <span class="a">{</span>
  .nav-side <span class="a">{</span> <span class="t">position</span>: fixed; <span class="t">transform</span>: translateX(-100%); <span class="a">}</span>
<span class="a">}</span>

<span class="c">/* 레일에서는 이름을 숨기되 title 로 남긴다 */</span>
.nav-side.is-rail .tx <span class="a">{</span> <span class="t">display</span>: none; <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "항목마다 포커스가 한 번씩 거쳐 갑니다. 본문에 닿기까지 오래 걸리므로 <b>'본문으로 건너뛰기'</b> 링크가 꼭 필요합니다"),
    ("<code>aria-current</code>", "<code>\"page\"</code> 값으로 지금 위치를 알립니다. 색만으로는 스크린 리더에 전해지지 않습니다"),
    ("<code>&lt;nav aria-label&gt;</code>", "내비게이션이 여러 개이면 '주 메뉴', '보조 메뉴'처럼 이름을 붙여 구별합니다"),
    ("레일", "아이콘만 남으면 <code>aria-label</code>이나 툴팁이 반드시 있어야 합니다"),
    ("접이식", "묶음이 펼쳐졌는지를 <code>aria-expanded</code>로 알립니다"),
  ]),
  backend=rows([
    ("사이드바 = 라우팅 표", "사이드바는 앱의 화면 구조를 그대로 보여 줍니다. 항목과 주소가 1대1로 대응하기 때문에 <b>사이드바를 고치는 일은 라우팅을 고치는 일</b>이 됩니다."),
    ("숫자 = 추가 질의", "'거래 584'처럼 개수를 보여 주려면 개수를 따로 세는 질의가 필요합니다. 이 값은 모든 화면에 뜨는데 정확한 COUNT는 비용이 크기 때문에 <b>캐시하거나 근사치</b>로 보여 줍니다."),
    ("권한 = 메뉴 필터", "사용자가 볼 수 없는 화면은 서버가 메뉴 목록에서 빼고 내려 주거나, 권한 플래그를 함께 내려 줍니다. 화면에서 항목만 숨기면 사용자가 주소를 직접 입력해 그 화면에 들어올 수 있습니다."),
    ("현재 위치 = 라우트 매칭", "<code>/tx/8812</code> 같은 상세 화면에서도 '거래 내역' 항목이 켜져 있어야 합니다. 그래서 현재 주소와 항목 주소가 정확히 같은지가 아니라 <b>접두사가 같은지</b>로 비교합니다."),
  ]),
  plat_lede="사이드바는 넓은 데스크톱 화면을 전제로 한 부품이라서, 모바일 지침에서는 레일이나 드로어로 바뀝니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", label="웹 사이드바 재현"),
     "<b>사이드바</b> · 관리 도구에서 기본으로 쓰는 화면 구성입니다. 화면이 좁아지면 드로어로 바꾸는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;top:14px;bottom:0;width:46%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:7px;background:var(--accent-soft);color:var(--accent);border-radius:5px;padding:2px 4px">거래</div><div style="font-size:7px;color:var(--fg-muted);padding:2px 4px">정산</div></div>', "iPadOS 사이드바 재현"),
     "<b>사이드바</b>(Sidebar) · <b>아이패드와 맥</b>에서 쓰는 부품입니다. 아이폰에는 사이드바가 없고 같은 역할을 <b>탭 바</b>가 맡습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;top:14px;bottom:0;width:24%;background:var(--bg);border-right:1px solid var(--line);padding:5px 2px"><div style="width:9px;height:9px;border-radius:3px;background:var(--accent);margin:0 auto 2px"></div><div style="font-size:4.5px;text-align:center;color:var(--accent)">거래</div><div style="width:9px;height:9px;border-radius:3px;background:var(--line-strong);margin:5px auto 2px"></div><div style="font-size:4.5px;text-align:center;color:var(--fg-muted)">정산</div></div>', "안드로이드 내비게이션 레일 재현"),
     "<b>내비게이션 레일</b>(Navigation rail) · 태블릿 폭에서 쓰는 좁은 세로 띠입니다. 화면이 더 넓으면 <b>드로어</b>를 화면에 고정해 사이드바처럼 씁니다."),
  ]),
  plat_note="같은 메뉴가 화면 폭이 넓어짐에 따라 <b>탭바, 레일, 사이드바</b> 순서로 바뀝니다. 세 가지를 따로 만들면 한쪽에만 항목을 더하는 식으로 서로 어긋나기 쉬우므로, <b>항목 목록은 하나로 두고</b> 폭마다 모양만 바꾸는 편이 안전합니다.",
  siblings=siblings("sidebar"),
  related='''        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><span class="na"><b>트리뷰</b><em>7부</em></span></li>
        <li><span class="na"><b>배지</b><em>5부</em></span></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
