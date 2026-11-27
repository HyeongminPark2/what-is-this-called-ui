# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px">
                  <div style="display:flex;align-items:center;gap:40px;flex-wrap:wrap">
                    <span data-pin="2" style="font-size:11px;color:var(--fg-muted)">위키</span>
                    <span data-pin="3" style="font-size:11px;color:var(--fg-faint)">›</span>
                    <span data-pin="4" style="font-size:11px;color:var(--fg-muted);border:1px solid var(--line-strong);border-radius:4px;padding:1px 7px">…</span>
                    <span class="pin-tr" data-pin="5" style="font-size:11px;color:var(--fg-muted)">결제</span>
                  </div>
                  <div class="pin-out" data-pin="6" style="font-size:11px;font-weight:700;margin-top:18px">회고 초안</div>
                </div>
              </div>'''

D = dict(
  slug="breadcrumb", ko="브레드크럼", en="Breadcrumb",
  desc="브레드크럼이 무엇인지, 뒤로가기·탭과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="브레드크럼은 지금 있는 곳까지의 <b>계층 전체</b>를 한 줄로 보여 주는 링크 줄입니다. 각 칸이 상위 단계로 가는 링크라서 위로 올라가는 길도 함께 제공합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 바꿔 보세요. <b>7단계</b>에서는 가운데 단계들이 <b>…</b> 하나로 접힙니다.
          처음과 끝 칸은 늘 남기고 가운데를 줄이는 것이 관례입니다.<br>
          마지막 칸은 <b>링크가 아닙니다.</b> 지금 보고 있는 화면이라서 눌러도 갈 곳이 없기 때문입니다(<code>aria-current="page"</code>).</p>
        </div>''',
  names=rows([
    ("한국어", "브레드크럼, 빵부스러기, 경로 표시, 이동 경로"),
    ("영어", "breadcrumb, breadcrumb trail"),
    ("같이 쓰는 말", "칸 사이의 기호는 <b>구분자</b>(separator), 가운데 단계를 줄이는 것은 <b>접기</b>(truncation), 마지막 칸은 <b>현재 항목</b>이라고 부릅니다. 브레드크럼이라는 이름은 헨젤과 그레텔 이야기에서 길에 떨어뜨린 빵부스러기에서 왔습니다."),
    ("자주 잘못 부르는 이름",
     "<b>뒤로가기</b> — 뒤로가기는 <b>어떻게 왔는지</b>(이력)를 따라가고, 브레드크럼은 <b>어디에 있는지</b>(계층)를 보여 줍니다. 그래서 검색으로 들어왔든 메뉴로 들어왔든 브레드크럼은 같습니다.<br>"
     "<b>스테퍼</b> — 스테퍼는 1-2-3처럼 순서가 있는 <b>단계 진행</b>을 보여 줍니다.<br>"
     "<b>내비게이션</b> — 브레드크럼은 갈 곳을 새로 고르는 메뉴가 아니라 <b>지금 위치</b>를 알리는 표시입니다."),
  ]),
  axes=ax("브레드크럼"),
  oneline="브레드크럼은 <b>이력</b>이 아니라 <b>계층</b>을 보여 줍니다. 그래서 검색으로 깊은 곳에 바로 들어와도 메뉴를 따라 들어왔을 때와 같은 줄이 나와야 합니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5.5px;color:var(--fg-muted)">위키 › 팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="짧은 브레드크럼"), "짧음", "두세 단계일 때가 가장 읽기 좋습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted);line-height:1.8">위키 › 팀 문서 › 플랫폼 › 결제 › <b style="color:var(--fg)">회고</b></div>', bars="", label="다섯 단계"), "다섯 단계", "다섯 단계 정도가 한 줄에 들어가는 한계입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">…</span> › 결제 › <b style="color:var(--fg)">회고</b></div>', bars="", label="접힌 브레드크럼"), "접힘", "가운데 단계를 <b>…</b>로 줄이고, 처음과 끝 칸은 남깁니다"),
    (mini('<div style="margin-top:9px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 ›</div><div style="padding:0 6px;font-size:5px;color:var(--fg-muted)">팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="두 줄로 넘어간 브레드크럼"), "줄바꿈", "좁은 화면에서는 넘치는 칸을 <b>잘라 숨기지 말고</b> 가운데를 접거나 줄을 바꿉니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › 팀 문서 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">결제 ▾</span> › <b style="color:var(--fg)">회고</b></div>', bars="", label="형제 목록이 열리는 브레드크럼"), "형제 열기", "칸을 누르면 목록이 열려 <b>같은 층의 다른 항목</b>으로 바로 갈 수 있게 한 변형입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div class="skl" style="height:5px;width:60%"></div></div>', bars="", label="로딩 중 브레드크럼"), "로딩", "계층 정보는 리소스 데이터에서 나옵니다. 데이터를 아직 받지 못했을 때는 뼈대 모양으로 보여 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("브레드크럼", "breadcrumb", "<code>&lt;nav aria-label=\"현재 위치\"&gt;</code>로 감쌉니다"),
    ("상위 항목", "ancestor link", "누르면 그 단계로 갑니다. 현재 항목을 뺀 칸은 <b>모두 링크</b>여야 합니다"),
    ("구분자", "separator", "› 나 / 를 씁니다. <b>장식일 뿐이므로 스크린 리더가 읽지 않게</b> 합니다"),
    ("접힘", "truncation", "줄이 길면 가운데 단계를 줄입니다. 누르면 다시 펼쳐지게 두는 편이 좋습니다"),
    ("바로 위", "parent", "사용자가 가장 많이 누르는 칸으로, 사실상 '위로 가기' 버튼 역할을 합니다"),
    ("현재 항목", "current page", "<b>링크로 두지 않고</b> <code>aria-current=\"page\"</code>를 붙입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          화면 제목과 브레드크럼의 마지막 칸은 <b>같은 말</b>인 경우가 많습니다.
          이럴 때는 마지막 칸을 빼고 제목이 그 역할을 대신하게 해도 됩니다. 그러면 사용자가 같은 말을 두 번 읽지 않아도 됩니다.</p>''',
  do=ul([
    "위키, 파일, 카테고리처럼 계층이 <b>세 단을 넘는</b> 구조일 때",
    "검색이나 링크로 <b>깊은 곳에 바로</b> 들어오는 일이 잦을 때",
    "위로 한 단만 올라가는 일이 잦을 때. 바로 위 칸이 '위로' 버튼 역할을 합니다",
  ]),
  dont=ul([
    "계층이 한두 단뿐일 때. 화면 제목만으로 충분합니다",
    "이동 이력을 보여 주려고 할 때. 이력은 뒤로가기가 맡습니다",
    "단계 진행을 보여 주려고 할 때. 스테퍼(위저드)를 씁니다",
    "마지막 칸을 링크로 둘 때. 지금 보고 있는 화면이라 눌러도 갈 곳이 없습니다",
  ]),
  instead='단계 진행이면 스테퍼(7부), 같은 화면의 다른 면이면 <a href="tabs.html">탭</a>, 길을 새로 고르면 <a href="sidebar.html">사이드바</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">홈 › 가구 › 소파 › <b style="color:var(--fg)">리넨 3인</b></div>', bars="", tall=False, label="쇼핑몰 브레드크럼 재현"),
     "쇼핑몰", "상품의 카테고리 계층을 보여 줍니다. 검색으로 상품에 바로 들어온 사람에게 특히 쓸모가 있습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">…</span> › <b style="color:var(--fg)">회고 초안</b></div>', bars="", tall=False, label="문서 도구 브레드크럼 재현"),
     "문서 도구", "폴더가 깊어서 가운데 단계를 접어야 하는 경우가 대부분입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">결제 › <b style="color:var(--fg)">거래 내역</b></div>', bars="", tall=False, label="관리 도구 브레드크럼 재현"),
     "관리 도구", "사이드바가 이미 위치를 알려 주므로 두 단 정도로 짧게 둡니다"),
  ]),
  code_lede="목록 마크업에 <code>aria-label</code>과 <code>aria-current</code>만 붙이면 됩니다. 구분자는 <b>CSS로</b> 넣어서 스크린 리더가 읽지 않게 합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"현재 위치"</span>&gt;
  &lt;<span class="t">ol</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wiki"</span>&gt;위키&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wiki/team"</span>&gt;팀 문서&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">span</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;회고 초안&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ol</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">/* 구분자는 CSS로 넣는다. 장식이라 스크린 리더가 읽으면 안 된다 */</span>
li + li::before <span class="a">{</span> <span class="t">content</span>: <span class="s">"›"</span>; <span class="t">color</span>: var(--fg-faint); <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "칸마다 포커스가 한 번씩 거쳐 갑니다. 보통 서너 번이면 지나가서 부담이 적습니다"),
    ("<code>aria-label</code>", "<code>\"현재 위치\"</code>처럼 이름을 붙여 두면 내비게이션이 여러 개일 때 서로 구별됩니다"),
    ("<code>aria-current</code>", "마지막 칸에 <code>\"page\"</code> 값을 달고, 링크로 두지 않습니다"),
    ("구분자", "CSS <code>::before</code>로 넣습니다. 글자로 넣으면 스크린 리더가 칸마다 '꺾쇠'를 읽습니다"),
    ("접힘", "<b>…</b>은 버튼으로 만들어서 눌러 펼칠 수 있게 합니다"),
  ]),
  backend=rows([
    ("브레드크럼 = 계층 질의", "브레드크럼을 그리려면 리소스의 <b>조상 목록</b>이 필요합니다. 상세 응답에 <code>ancestors: [...]</code>를 함께 내려 주면 화면이 따로 요청하지 않아도 됩니다."),
    ("이력이 아니다", "사용자가 어떤 경로로 들어왔든 같은 줄이 나와야 하므로 세션이나 리퍼러 정보에 기대지 않습니다. <b>리소스 하나만 알면 그릴 수 있어야</b> 합니다."),
    ("깊이 제한", "계층이 깊어질수록 조상을 찾는 질의가 비싸집니다. 그래서 리소스에 전체 경로를 <b>미리 저장</b>(materialized path)해 두는 방법을 흔히 씁니다."),
    ("이름이 바뀔 때", "상위 폴더 이름이 바뀌면 브레드크럼에 보이는 이름도 바뀌어야 합니다. 경로를 캐시해 뒀다면 이때 캐시를 무효화해야 합니다."),
  ]),
  plat_lede="브레드크럼은 데스크톱 웹에서 쓰는 부품이라서 모바일 지침에서는 거의 다루지 않습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › 팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="웹 브레드크럼 재현"),
     "<b>브레드크럼</b> · 마크업 규칙이 널리 합의돼 있고, 구조화 데이터로 표시해 두면 검색 결과에도 그대로 나옵니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:4px 7px;border-bottom:1px solid var(--line);display:flex;font-size:8px"><span style="color:#0a84ff">‹ 결제</span><b style="flex:1;text-align:center">회고</b></div>', "iOS 뒤로 버튼 재현"),
     "<b>없습니다.</b> 대신 '‹ 결제'처럼 <b>뒤로 버튼에 상위 화면 이름</b>을 붙여 바로 위 한 단만 보여 줍니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:5px 7px;display:flex;gap:5px;font-size:8px"><span>←</span><b style="flex:1">회고 초안</b></div><div style="position:absolute;left:7px;top:36px;font-size:6.5px;color:var(--fg-muted)">결제 › 회고 초안</div>', "안드로이드 경로 표시 재현"),
     "표준 부품은 없습니다. 보통 위로 가기(Up) 버튼으로 대신하고, 경로가 꼭 필요하면 제목 아래에 <b>경로를 글로</b> 적습니다."),
  ]),
  plat_note="모바일에서는 가로 자리가 모자라기 때문에 브레드크럼을 거의 쓰지 않고, 그 역할을 <b>뒤로 버튼 하나</b>가 대신합니다. 다만 뒤로 버튼은 바로 위 <b>한 단</b>만 알려 주므로, 계층이 깊은 앱에서는 지금 어디쯤 있는지를 화면 제목으로 보완해야 합니다.",
  siblings=siblings("breadcrumb"),
  related='''        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><span class="na"><b>스테퍼(위저드)</b><em>7부</em></span></li>
        <li><span class="na"><b>말줄임</b><em>3부</em></span></li>
        <li><span class="na"><b>시스템 백</b><em>11부</em></span></li>''',
)
