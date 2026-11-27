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
  desc="사이드바 내비게이션이 무엇이고 드로어·바텀 탭바와 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="화면 <b>옆에 늘 붙어 있는</b> 메뉴. 지금 어디인지와 갈 수 있는 곳이 한눈에 남아, 항목이 열 개를 넘어도 버팁니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>사이드바는 <b>늘 보입니다.</b> 같은 내용이 좁은 화면에서 숨었다 나오면 그건 <a href="drawer.html">드로어</a>입니다.<br>
          <b>아이콘만 보기</b>를 눌러 보세요. 자리를 아끼되 길은 남기는 <b>레일</b>(rail)이 됩니다 —
          다만 아이콘만으로는 뜻이 안 전해져서 툴팁이나 글자를 같이 둬야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "사이드바, 측면 내비게이션, 좌측 메뉴"),
    ("영어", "sidebar navigation, side nav, navigation rail"),
    ("같이 쓰는 말", "아이콘만 남겨 좁힌 것을 <b>레일</b>(rail), 하위 항목이 펼쳐지는 것을 <b>접이식</b>(collapsible), 묶음 제목을 <b>섹션 헤더</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>드로어</b> — 늘 보이면 사이드바, 숨었다 밀려 나오면 드로어입니다. <b>같은 내용이 폭에 따라 둘 사이를 오갑니다.</b><br>"
     "<b>메뉴</b> — 메뉴는 동작을 고르는 것이고 사이드바는 화면을 옮깁니다.<br>"
     "<b>패널</b> — 패널은 보조 내용을 담는 칸이고, 사이드바는 길을 담습니다."),
  ]),
  axes=ax("사이드바"),
  oneline="사이드바는 <b>늘 보이는 길</b>입니다. 자리를 내주는 대신 '지금 어디인지'와 '어디로 갈 수 있는지'를 계속 보여 줍니다.",
  states=states([
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin-bottom:3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", label="기본 사이드바"), "기본", "현재 위치가 강조돼 있다. <b>늘 보인다</b>"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:20%;background:var(--bg);border-right:1px solid var(--line);padding:5px 3px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto"></div></div>', bars="", label="레일"), "레일", "아이콘만. 자리를 아끼되 <b>길은 남긴다</b>"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">운영 ▾</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin:2px 0 0 5px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;margin-left:5px">정산</div></div>', bars="", label="접이식 사이드바"), "접이식", "묶음을 펼치고 접는다. 깊이는 <b>두 단</b>까지"),
    (mini('<div class="mini__scrim" style="padding:0"><div class="mini__drawer"><b>메뉴</b><i class="on">거래 내역</i><i>정산</i></div></div>', bars="684", label="좁은 화면에서 드로어가 된 모습"), "좁은 화면", "같은 내용이 <b>드로어</b>로 바뀐다. 부품이 달라진 게 아니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;display:flex"><span style="flex:1">거래 내역</span><span>584</span></div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;display:flex"><span style="flex:1">정산</span><span style="background:var(--danger);color:#fff;border-radius:99px;padding:0 3px;font-size:4.5px">12</span></div></div>', bars="", label="숫자가 붙은 사이드바"), "숫자 · 배지", "개수는 흐리게, <b>처리할 것</b>은 빨갛게. 둘을 섞지 않는다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-faint);padding:1px 3px;opacity:.5">정산 🔒</div></div>', bars="", label="권한이 없는 항목"), "권한 없음", "숨길지 흐리게 둘지. <b>흐리게 두면 있다는 건 알게 된다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("사이드바", "sidebar", "화면 높이를 다 쓴다. 보통 200~260px"),
    ("섹션 헤더", "section header", "항목이 일곱을 넘으면 묶는다. 작고 조용하게"),
    ("현재 항목", "current item", "<b>배경과 색으로</b> 알린다. <code>aria-current=\"page\"</code>도 같이"),
    ("아이콘", "icon", "눈이 빨리 찾게 돕는다. 레일에서는 이것만 남는다"),
    ("이름", "label", "짧게. 한 줄을 넘기면 묶음을 다시 생각할 때다"),
    ("숫자", "count · badge", "개수나 처리할 것. 없으면 안 둔다"),
    ("다른 항목", "item", "과녁은 40px 이상. 글자뿐 아니라 줄 전체가 눌려야 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          사이드바는 <b>모든 화면에 같이 나옵니다.</b> 그래서 항목 하나를 더하는 결정은
          화면 하나를 더하는 것보다 무겁습니다 — 열 개가 넘어가면 묶음을 먼저 손봐야 합니다.</p>''',
  do=ul([
    "갈 곳이 <b>다섯 개를 넘을</b> 때 — 탭바로는 못 담습니다",
    "넓은 화면에서 길을 늘 보여 주고 싶을 때",
    "계층이 두 단인 내비게이션 — 묶음과 항목",
  ]),
  dont=ul([
    "좁은 화면에서 그대로 두기 — 내용 볼 자리가 없어집니다. <b>드로어로 접습니다</b>",
    "항목을 스무 개 넘게 늘어놓기 — 묶거나 검색을 답니다",
    "동작(저장·삭제)을 섞어 넣기 — 사이드바는 <b>길</b>만 담습니다",
    "깊이 세 단 이상 — 접었다 폈다 하다가 길을 잃습니다",
  ]),
  instead='좁은 화면이면 <a href="drawer.html">드로어</a>, 폰이면 <a href="bottomnav.html">바텀 탭바</a>, 같은 화면의 다른 면이면 <a href="tabs.html">탭</a>, 동작이면 <a href="popover.html">드롭다운 메뉴</a>.',
  cases=cases([
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5px;color:var(--fg-muted);margin-bottom:2px">운영</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", tall=False, label="관리 도구 사이드바 재현"),
     "관리 도구", "가장 흔한 자리. 묶음 제목으로 나눈다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:20%;background:var(--bg);border-right:1px solid var(--line);padding:5px 3px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 4px"></div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto"></div></div>', bars="", tall=False, label="레일 재현"),
     "레일", "작업 화면에서 자리를 아낄 때. 툴팁이 꼭 필요하다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:46%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">▾ 팀 문서</div><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px;margin-left:5px">회고 초안</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px;margin-left:5px">온보딩</div></div>', bars="", tall=False, label="트리형 사이드바 재현"),
     "트리형", "문서 도구에서. 사실상 <b>트리뷰</b>가 된다"),
  ]),
  code_lede="<code>&lt;nav&gt;</code>와 <code>aria-current</code> 두 가지가 핵심입니다. 지금 어디인지를 <b>색 말고도</b> 알려야 합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"주 메뉴"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/tx"</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;거래 내역&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settle"</span>&gt;정산&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">/* 좁아지면 드로어로 바꾼다 — 같은 마크업, 다른 모양 */</span>
@media (max-width: 860px) <span class="a">{</span>
  .nav-side <span class="a">{</span> <span class="t">position</span>: fixed; <span class="t">transform</span>: translateX(-100%); <span class="a">}</span>
<span class="a">}</span>

<span class="c">/* 레일에서는 이름을 숨기되 title 로 남긴다 */</span>
.nav-side.is-rail .tx <span class="a">{</span> <span class="t">display</span>: none; <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "항목마다 한 번씩 지난다. 그래서 <b>'본문으로 건너뛰기'</b> 링크가 꼭 필요하다"),
    ("<code>aria-current</code>", "<code>\"page\"</code>로 지금 위치를 알린다. 색만으로는 안 전해진다"),
    ("<code>&lt;nav aria-label&gt;</code>", "내비게이션이 여럿이면 이름을 붙여 가른다 — '주 메뉴', '보조 메뉴'"),
    ("레일", "아이콘만 남으면 <code>aria-label</code>이나 툴팁이 반드시 있어야 한다"),
    ("접이식", "펼침 여부를 <code>aria-expanded</code>로 알린다"),
  ]),
  backend=rows([
    ("사이드바 = 라우팅 표", "화면 구조를 그대로 비춥니다. 항목과 주소가 1대1이라, <b>사이드바를 고치는 일은 라우팅을 고치는 일</b>입니다."),
    ("숫자 = 추가 질의", "'거래 584'를 보여 주려면 개수를 따로 세야 합니다. 모든 화면에 뜨는 값이라 <b>캐시하거나 근사치</b>로 둡니다 — 정확한 COUNT 는 비쌉니다."),
    ("권한 = 메뉴 필터", "볼 수 없는 화면은 서버가 내려 주지 않거나 플래그를 함께 줍니다. 화면에서만 숨기면 주소를 치고 들어옵니다."),
    ("현재 위치 = 라우트 매칭", "<code>/tx/8812</code>에서도 '거래 내역'이 켜져야 합니다. 정확히 같은 주소가 아니라 <b>접두사로</b> 맞춥니다."),
  ]),
  plat_lede="데스크톱의 부품이라 모바일 지침에서는 레일이나 드로어로 바뀝니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;left:0;top:0;bottom:0;width:42%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">거래 내역</div><div style="font-size:5.5px;color:var(--fg-muted);padding:1px 3px">정산</div></div>', bars="", label="웹 사이드바 재현"),
     "<b>사이드바</b> · 관리 도구의 기본 짜임입니다. 좁아지면 드로어로 접는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;top:14px;bottom:0;width:46%;background:var(--bg);border-right:1px solid var(--line);padding:5px 4px"><div style="font-size:7px;background:var(--accent-soft);color:var(--accent);border-radius:5px;padding:2px 4px">거래</div><div style="font-size:7px;color:var(--fg-muted);padding:2px 4px">정산</div></div>', "iPadOS 사이드바 재현"),
     "<b>사이드바</b>(Sidebar) · <b>아이패드와 맥</b>의 부품입니다. 아이폰에는 없고 <b>탭 바</b>로 풉니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;top:14px;bottom:0;width:24%;background:var(--bg);border-right:1px solid var(--line);padding:5px 2px"><div style="width:9px;height:9px;border-radius:3px;background:var(--accent);margin:0 auto 2px"></div><div style="font-size:4.5px;text-align:center;color:var(--accent)">거래</div><div style="width:9px;height:9px;border-radius:3px;background:var(--line-strong);margin:5px auto 2px"></div><div style="font-size:4.5px;text-align:center;color:var(--fg-muted)">정산</div></div>', "안드로이드 내비게이션 레일 재현"),
     "<b>내비게이션 레일</b>(Navigation rail) · 태블릿 폭에서 쓰는 좁은 세로 띠이고, 더 넓으면 <b>드로어</b>를 고정해 둡니다."),
  ]),
  plat_note="같은 내용이 폭에 따라 <b>탭바 → 레일 → 사이드바</b>로 바뀝니다. 셋을 다른 부품으로 그리면 항목이 서로 안 맞게 되기 쉽습니다 — <b>항목 목록을 하나로 두고</b> 폭마다 모양만 바꾸는 쪽이 안전합니다.",
  siblings=siblings("sidebar"),
  related='''        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><span class="na"><b>트리뷰</b><em>7부</em></span></li>
        <li><span class="na"><b>배지</b><em>5부</em></span></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
