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
  desc="브레드크럼이 무엇이고 뒤로가기·탭과 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="지금 있는 곳의 <b>계층 전체</b>를 한 줄로 보여 주고, 위로 올라가는 길을 함께 주는 줄.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 바꿔 보세요. <b>7단계</b>에서는 가운데가 <b>…</b>로 접힙니다 —
          처음과 끝은 늘 남기고 가운데를 줄이는 것이 관례입니다.<br>
          마지막 칸은 <b>링크가 아닙니다.</b> 지금 그 화면에 있으니 누를 곳이 없습니다(<code>aria-current="page"</code>).</p>
        </div>''',
  names=rows([
    ("한국어", "브레드크럼, 빵부스러기, 경로 표시, 이동 경로"),
    ("영어", "breadcrumb, breadcrumb trail"),
    ("같이 쓰는 말", "사이의 기호를 <b>구분자</b>(separator), 가운데를 줄이는 것을 <b>접기</b>(truncation), 마지막 칸을 <b>현재 항목</b>이라 합니다. 헨젤과 그레텔의 빵부스러기에서 온 이름입니다."),
    ("자주 잘못 부름",
     "<b>뒤로가기</b> — 뒤로가기는 <b>어떻게 왔는지</b>(이력)이고, 브레드크럼은 <b>어디에 있는지</b>(계층)입니다. 검색으로 들어왔어도 브레드크럼은 같습니다.<br>"
     "<b>스테퍼</b> — 스테퍼는 <b>단계 진행</b>을 보여 줍니다. 1-2-3처럼 순서가 있는 것.<br>"
     "<b>내비게이션</b> — 길을 새로 고르는 것이 아니라 <b>지금 위치</b>를 알리는 것입니다."),
  ]),
  axes=ax("브레드크럼"),
  oneline="브레드크럼은 <b>계층</b>이지 <b>이력</b>이 아닙니다. 검색으로 바로 들어와도 같은 줄이 나와야 맞습니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5.5px;color:var(--fg-muted)">위키 › 팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="짧은 브레드크럼"), "짧음", "두세 단계. 가장 읽기 좋다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted);line-height:1.8">위키 › 팀 문서 › 플랫폼 › 결제 › <b style="color:var(--fg)">회고</b></div>', bars="", label="다섯 단계"), "다섯 단계", "여기까지가 한 줄에 들어가는 한계"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">…</span> › 결제 › <b style="color:var(--fg)">회고</b></div>', bars="", label="접힌 브레드크럼"), "접힘", "가운데를 <b>…</b>로. 처음과 끝은 남긴다"),
    (mini('<div style="margin-top:9px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 ›</div><div style="padding:0 6px;font-size:5px;color:var(--fg-muted)">팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="두 줄로 넘어간 브레드크럼"), "줄바꿈", "좁은 화면. <b>잘라 숨기지 말고</b> 접거나 줄을 바꾼다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › 팀 문서 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">결제 ▾</span> › <b style="color:var(--fg)">회고</b></div>', bars="", label="형제 목록이 열리는 브레드크럼"), "형제 열기", "칸을 누르면 <b>같은 층의 다른 것</b>으로 바로 갈 수 있게 하는 변형"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div class="skl" style="height:5px;width:60%"></div></div>', bars="", label="로딩 중 브레드크럼"), "로딩", "계층은 리소스에서 나온다. 아직 모를 때는 뼈대로"),
  ]),
  anat=ANAT,
  pins=pins([
    ("브레드크럼", "breadcrumb", "<code>&lt;nav aria-label=\"현재 위치\"&gt;</code>로 감싼다"),
    ("상위 항목", "ancestor link", "누르면 그 층으로 간다. <b>전부 링크</b>여야 한다"),
    ("구분자", "separator", "› 나 /. <b>장식이라 스크린 리더에는 안 읽히게</b> 한다"),
    ("접힘", "truncation", "길면 가운데를 줄인다. 누르면 펼쳐지게 두는 편이 낫다"),
    ("바로 위", "parent", "가장 많이 눌리는 칸. 사실상 '위로 가기' 버튼이다"),
    ("현재 항목", "current page", "<b>링크가 아니다.</b> <code>aria-current=\"page\"</code>를 붙인다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          제목과 브레드크럼의 마지막 칸이 <b>같은 말</b>이 되는 경우가 많습니다.
          그러면 마지막 칸을 빼고 제목으로 대신해도 됩니다 — 같은 말을 두 번 읽히지 않습니다.</p>''',
  do=ul([
    "계층이 <b>세 단을 넘는</b> 구조 — 위키, 파일, 카테고리",
    "검색이나 링크로 <b>깊은 곳에 바로</b> 들어오는 일이 잦을 때",
    "위로 한 단만 올라가는 일이 잦을 때 — 사실상 '위로' 버튼이 됩니다",
  ]),
  dont=ul([
    "계층이 한두 단뿐일 때 — 제목만으로 충분합니다",
    "이력을 보여 주려고 쓰기 — 그건 뒤로가기입니다",
    "단계 진행을 보여 주려고 쓰기 → 스테퍼(위저드)",
    "마지막 칸을 링크로 두기 — 지금 그 화면입니다",
  ]),
  instead='단계 진행이면 스테퍼(7부), 같은 화면의 다른 면이면 <a href="tabs.html">탭</a>, 길을 새로 고르면 <a href="sidebar.html">사이드바</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">홈 › 가구 › 소파 › <b style="color:var(--fg)">리넨 3인</b></div>', bars="", tall=False, label="쇼핑몰 브레드크럼 재현"),
     "쇼핑몰", "카테고리 계층. 검색으로 들어온 사람에게 특히 값지다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › <span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 2px">…</span> › <b style="color:var(--fg)">회고 초안</b></div>', bars="", tall=False, label="문서 도구 브레드크럼 재현"),
     "문서 도구", "폴더가 깊어 접기가 거의 필수가 된다"),
    (mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">결제 › <b style="color:var(--fg)">거래 내역</b></div>', bars="", tall=False, label="관리 도구 브레드크럼 재현"),
     "관리 도구", "두 단이면 짧게. 사이드바가 이미 위치를 알려 준다"),
  ]),
  code_lede="목록 마크업에 <code>aria-label</code>과 <code>aria-current</code>를 붙이면 끝입니다. 구분자는 <b>CSS 로</b> 넣어 안 읽히게 합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"현재 위치"</span>&gt;
  &lt;<span class="t">ol</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wiki"</span>&gt;위키&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wiki/team"</span>&gt;팀 문서&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">span</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;회고 초안&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ol</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">/* 구분자는 CSS 로 — 장식이라 읽히면 안 된다 */</span>
li + li::before <span class="a">{</span> <span class="t">content</span>: <span class="s">"›"</span>; <span class="t">color</span>: var(--fg-faint); <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "칸마다 한 번씩. 보통 서너 번이라 부담이 적다"),
    ("<code>aria-label</code>", "<code>\"현재 위치\"</code>처럼 이름을 붙인다. 내비게이션이 여럿일 때 가려진다"),
    ("<code>aria-current</code>", "마지막 칸에 <code>\"page\"</code>. 링크로 두지 않는다"),
    ("구분자", "CSS <code>::before</code>로 넣는다. 글자로 넣으면 '꺾쇠'가 전부 읽힌다"),
    ("접힘", "<b>…</b>은 버튼으로 둬서 펼칠 수 있게 한다"),
  ]),
  backend=rows([
    ("브레드크럼 = 계층 질의", "리소스의 <b>조상 목록</b>이 필요합니다. 상세 응답에 <code>ancestors: [...]</code>를 같이 내려 주면 화면이 따로 묻지 않아도 됩니다."),
    ("이력이 아니다", "어떻게 들어왔든 같은 줄이 나옵니다. 세션이나 리퍼러에 기대지 않습니다 — <b>리소스만 알면 그릴 수 있어야</b> 합니다."),
    ("깊이 제한", "계층이 깊어질수록 조상 질의가 비싸집니다. 경로를 리소스에 <b>미리 저장</b>(materialized path)해 두는 방법이 흔합니다."),
    ("이름이 바뀔 때", "상위 폴더 이름이 바뀌면 브레드크럼도 바뀝니다. 캐시해 뒀다면 무효화 대상입니다."),
  ]),
  plat_lede="데스크톱 웹의 부품입니다. 모바일 지침에는 사실상 자리가 없습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;font-size:5px;color:var(--fg-muted)">위키 › 팀 문서 › <b style="color:var(--fg)">회고</b></div>', bars="", label="웹 브레드크럼 재현"),
     "<b>브레드크럼</b> · 마크업 규칙이 널리 합의돼 있고, 검색 결과에도 그대로 쓰입니다(구조화 데이터)."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:4px 7px;border-bottom:1px solid var(--line);display:flex;font-size:8px"><span style="color:#0a84ff">‹ 결제</span><b style="flex:1;text-align:center">회고</b></div>', "iOS 뒤로 버튼 재현"),
     "<b>없습니다.</b> 대신 <b>뒤로 버튼에 상위 이름</b>을 붙여 한 단만 보여 줍니다 — '‹ 결제'."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:16px;padding:5px 7px;display:flex;gap:5px;font-size:8px"><span>←</span><b style="flex:1">회고 초안</b></div><div style="position:absolute;left:7px;top:36px;font-size:6.5px;color:var(--fg-muted)">결제 › 회고 초안</div>', "안드로이드 경로 표시 재현"),
     "표준 부품은 없고, 필요하면 제목 아래에 <b>경로를 글로</b> 적습니다. 보통 위로 가기(Up) 버튼으로 대신합니다."),
  ]),
  plat_note="모바일에는 브레드크럼이 거의 없습니다. 가로 자리가 모자라서이고, 그 자리를 <b>뒤로 버튼 하나</b>가 대신합니다. 다만 뒤로 버튼은 <b>한 단</b>만 알려 주므로, 계층이 깊은 앱에서는 '어디쯤 있는지'를 제목으로 보완해야 합니다.",
  siblings=siblings("breadcrumb"),
  related='''        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><span class="na"><b>스테퍼(위저드)</b><em>7부</em></span></li>
        <li><span class="na"><b>말줄임</b><em>3부</em></span></li>
        <li><span class="na"><b>시스템 백</b><em>11부</em></span></li>''',
)
