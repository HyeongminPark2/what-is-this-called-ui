# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:14px 26px 18px;display:flex;gap:40px">
                  <span data-pin="2" style="flex:1;text-align:center">
                    <span class="pin-out" data-pin="3" style="position:relative;display:block;width:20px;height:20px;border-radius:6px;background:var(--accent);margin:0 auto 6px">
                      <span class="pin-tr" data-pin="4" style="position:absolute;top:-5px;right:-7px;background:var(--danger);color:#fff;border-radius:99px;font-size:8px;font-weight:800;padding:0 4px">3</span>
                    </span>
                    <span class="pin-out" data-pin="5" style="font-size:10px;color:var(--accent);font-weight:700">거래</span>
                  </span>
                  <span style="flex:1;text-align:center">
                    <span style="display:block;width:20px;height:20px;border-radius:6px;background:var(--line-strong);margin:0 auto 6px"></span>
                    <span style="font-size:10px;color:var(--fg-muted)">정산</span>
                  </span>
                </div>
                <div class="pin-out" data-pin="6" style="height:16px"></div>
              </div>'''

D = dict(
  slug="bottomnav", ko="바텀 탭바", en="Tab bar · Bottom navigation",
  desc="바텀 탭바가 무엇이고 탭·사이드바와 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="폰 화면 <b>아래에 늘 붙어 있는</b> 메뉴. 앱 전체를 서너 갈래로 나누고, 엄지가 닿는 자리에 둡니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>거래를 여러 번 눌러 보세요.</b> 처음 누르면 그 화면으로 가고, <b>이미 그 화면이면 맨 위로</b> 올라갑니다 —
          탭바의 숨은 약속입니다. 탭마다 <b>스크롤 위치를 따로 기억</b>하는 것도 확인해 보세요.<br>
          칸은 <b>3~5개</b>까지입니다. 그 이상은 손가락이 닿기 어렵고 글자가 잘립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "바텀 탭바, 하단 탭, 탭바, 하단 내비게이션"),
    ("영어", "tab bar (iOS), bottom navigation (Android), bottom nav"),
    ("같이 쓰는 말", "칸 하나가 <b>탭</b>, 빨간 숫자가 <b>배지</b>, 넓은 화면에서 옆으로 서는 것을 <b>레일</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>탭</b> — 이름이 같지만 <a href=\"tabs.html\">화면 안의 탭</a>은 <b>한 화면의 다른 면</b>이고, 탭바는 <b>앱 전체</b>를 오갑니다.<br>"
     "<b>푸터</b> — 푸터는 스크롤 끝에 나오는 정보 영역입니다. 탭바는 늘 떠 있습니다.<br>"
     "<b>툴바</b> — 툴바는 동작을 모읍니다. 탭바는 길을 나눕니다."),
  ]),
  axes=ax("바텀 탭바"),
  oneline="바텀 탭바는 앱을 <b>서너 갈래</b>로 나눕니다. 갈래가 여섯을 넘으면 더 쪼갤 게 아니라 <b>구조를 다시 짤 때</b>입니다.",
  states=states([
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span></div>', bars="684", label="기본 탭바"), "기본", "고른 칸만 색이 다르다. <b>늘 하나는 골라져 있다</b>"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px;position:relative"><span style="position:absolute;top:-2px;right:-3px;background:var(--danger);color:#fff;border-radius:99px;font-size:3.5px;padding:0 2px">3</span></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span></div>', bars="684", label="배지가 붙은 탭바"), "배지", "처리할 것이 몇 건인지. 숫자가 없으면 점만 찍기도 한다"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 1px 5px"><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">홈</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">거래</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">정산</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">가맹…</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">내정…</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">더보…</span></div><div style="position:absolute;left:5px;bottom:18px;font-size:4.5px;color:var(--danger);font-weight:700">여섯 — 글자가 잘림</div>', bars="684", label="칸이 너무 많은 탭바"), "너무 많음", "다섯을 넘기면 글자가 잘린다. <b>구조를 다시 짤 때</b>"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span></div><div style="position:absolute;left:5px;bottom:18px;font-size:4.5px;color:var(--accent);font-weight:700">같은 탭 → 맨 위로</div>', bars="684", label="같은 탭을 다시 누른 모습"), "같은 탭 다시", "<b>맨 위로 올라간다.</b> 한 번 더 누르면 그 탭의 첫 화면으로"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px;transform:translateY(100%)"></div><div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:5px;bottom:6px;font-size:4.5px;color:var(--fg-muted)">몰입 화면 — 탭바를 감춤</div>', bars="", label="탭바를 감춘 모습"), "감춤", "영상·지도 같은 몰입 화면. <b>돌아올 길</b>을 꼭 남긴다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:22%;border-right:1px solid var(--line);padding:5px 2px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--accent)">거래</div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:5px auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--fg-muted)">정산</div></div>', bars="", label="넓은 화면에서 레일이 된 모습"), "넓은 화면", "같은 항목이 <b>레일</b>로 옆에 선다. 더 넓으면 사이드바"),
  ]),
  anat=ANAT,
  pins=pins([
    ("탭바", "tab bar", "화면 아래에 고정. 스크롤해도 남는다"),
    ("탭 하나", "tab", "과녁은 <b>48px 이상</b>. 칸을 균등하게 나눈다"),
    ("아이콘", "icon", "골랐을 때 <b>채운 모양</b>, 아닐 때 <b>선 모양</b>으로 가르는 것이 관례"),
    ("배지", "badge", "처리할 것이 몇 건인지. 아이콘 오른쪽 위"),
    ("이름", "label", "<b>아이콘만 두지 않는다.</b> 아이콘만으로는 뜻이 안 전해진다"),
    ("세이프 에어리어", "safe area inset", "홈 인디케이터에 가리지 않게 <b>아래에 더 두는</b> 빈 자리"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          탭바의 숨은 규칙 두 가지 — <b>탭마다 자기 화면 스택과 스크롤 위치를 기억</b>하고,
          <b>같은 탭을 다시 누르면 맨 위로</b> 갑니다. 둘 다 그림에는 안 보이지만 없으면 바로 불편합니다.</p>''',
  do=ul([
    "앱의 <b>주 갈래가 3~5개</b>일 때",
    "갈래 사이를 자주 오갈 때 — 한 번에 닿습니다",
    "폰에서 엄지로 쓰는 화면",
  ]),
  dont=ul([
    "갈래가 여섯을 넘을 때 — 글자가 잘립니다. <b>구조를 다시 짭니다</b>",
    "'더 보기' 칸으로 나머지를 몰아넣기 — 거기 든 것은 거의 안 쓰입니다",
    "동작(글쓰기·저장)을 탭으로 넣기 — 탭은 <b>길</b>입니다. 그건 FAB 가 할 일입니다",
    "아이콘만 두기 — 뜻이 안 전해집니다",
  ]),
  instead='넓은 화면이면 <a href="sidebar.html">사이드바</a>, 한 화면 안이면 <a href="tabs.html">탭</a>, 주 동작이면 FAB(5부), 숨겨도 되는 길이면 <a href="drawer.html">드로어</a>.',
  cases=cases([
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">홈</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">검색</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">내 정보</span></span></div>', bars="684", tall=False, label="세 칸 탭바 재현"),
     "세 칸", "가장 안전한 수. 글자가 잘릴 일이 없다"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">홈</span></span><span style="flex:1;text-align:center"><span style="display:block;width:12px;height:12px;border-radius:50%;background:var(--accent);margin:-6px auto 1px;color:#fff;font-size:7px;line-height:12px">＋</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">내 정보</span></span></div>', bars="684", tall=False, label="가운데 동작 버튼 재현"),
     "가운데 동작", "글쓰기 같은 주 동작을 가운데에. <b>길이 아니라 동작</b>이라 모양을 달리한다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:22%;border-right:1px solid var(--line);padding:5px 2px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--accent)">홈</div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:5px auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--fg-muted)">검색</div></div>', bars="", tall=False, label="레일 재현"),
     "레일", "태블릿 폭. 같은 항목이 옆으로 선다"),
  ]),
  code_lede="<code>&lt;nav&gt;</code>와 <code>aria-current</code>면 됩니다. 어려운 건 <b>탭마다 상태를 따로 기억하는 일</b>입니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"주 메뉴"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/tx"</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;&lt;/<span class="t">span</span>&gt;거래
  &lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">// 탭마다 스크롤 위치를 따로 기억한다</span>
pos[current] = body.scrollTop;
body.scrollTop = pos[next] || <span class="a">0</span>;

<span class="c">// 같은 탭을 다시 누르면 맨 위로</span>
<span class="a">if</span> (next === current) body.scrollTo(<span class="a">{</span> top: <span class="a">0</span>, behavior: <span class="s">'smooth'</span> <span class="a">}</span>);

<span class="c">/* 홈 인디케이터에 가리지 않게 */</span>
<span class="t">padding-bottom</span>: <span class="a">calc</span>(10px + env(safe-area-inset-bottom));''',
  keys=kbd([
    ("<code>aria-current</code>", "지금 탭에 <code>\"page\"</code>. 색만으로는 안 전해진다"),
    ("아이콘", "<code>aria-hidden</code>으로 숨기고 <b>글자를 읽히게</b> 한다"),
    ("과녁", "48px 이상. 아래 끝에 붙어 있어 더 누르기 쉬운 자리이기도 하다"),
    ("배지", "'읽지 않음 3건'처럼 <b>뜻까지</b> 읽히게 라벨을 붙인다"),
    ("<kbd>Tab</kbd>", "칸마다 한 번씩. 보통 서너 번이라 부담이 적다"),
  ]),
  backend=rows([
    ("탭 = 독립된 스택", "탭마다 자기 화면 기록과 스크롤 위치를 들고 있습니다. 하나의 전역 스택으로 다루면 <b>탭을 옮길 때마다 처음으로</b> 돌아가 불편해집니다."),
    ("배지 = 폴링 또는 푸시", "모든 화면에 떠 있는 숫자라 자주 갱신해야 합니다. 폴링이면 주기를, 푸시면 연결을 관리해야 합니다 — <b>가장 자주 부르는 API</b>가 되기 쉽습니다."),
    ("첫 탭 = 첫 질의", "앱을 열면 첫 탭의 데이터가 곧바로 필요합니다. 나머지 탭은 <b>열 때</b> 부르되, 자주 오가면 캐시를 둡니다."),
    ("갈래 수 = 제품 구조", "탭이 여섯 개가 되는 건 보통 화면 문제가 아니라 <b>제품이 뭘 하는 것인지</b>가 흐려진 신호입니다."),
  ]),
  plat_lede="iOS 와 안드로이드가 각각 다른 이름으로 <b>가장 강하게 규정한</b> 부품입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent)">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span></div>', bars="684", label="웹 하단 내비 재현"),
     "모바일 웹에서 앱처럼 보이려고 씁니다. 브라우저 주소창과 겹치지 않게 <code>env(safe-area-inset-bottom)</code>이 필요합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:8px;display:flex;border-top:1px solid var(--line);padding:4px 2px"><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:#0a84ff;margin:0 auto 1px"></span><span style="font-size:5px;color:#0a84ff">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:5px;color:var(--fg-muted)">정산</span></span></div>', "iOS 탭 바 재현"),
     "<b>탭 바</b>(Tab bar) · <b>2~5개</b>를 권하고, 같은 탭 다시 누르기·탭별 스택이 시스템 관례로 굳어 있습니다. iOS 에서 \"탭\"은 이것을 뜻합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;bottom:8px;display:flex;padding:5px 2px"><span style="flex:1;text-align:center"><span style="display:block;width:22px;height:11px;border-radius:99px;background:var(--accent-soft);margin:0 auto 1px;position:relative"><span style="position:absolute;left:50%;top:2px;transform:translateX(-50%);width:7px;height:7px;border-radius:2px;background:var(--accent)"></span></span><span style="font-size:5px;color:var(--accent);font-weight:700">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:5px;color:var(--fg-muted)">정산</span></span></div>', "안드로이드 내비게이션 바 재현"),
     "<b>내비게이션 바</b>(Navigation bar) · <b>3~5개</b>. 고른 칸의 아이콘 뒤에 <b>알약 모양 배경</b>이 깔리는 것이 M3 의 표시 방식입니다."),
  ]),
  plat_note="안드로이드에서 <b>\"내비게이션 바\"</b>는 이 하단 메뉴를 뜻하고, <b>iOS 에서 같은 말은 화면 위 앱바</b>를 뜻합니다. <b>위아래가 정반대</b>라, 플랫폼이 섞인 자리에서 가장 크게 어긋나는 이름입니다 — '아래 탭바'처럼 자리를 붙여 말하는 편이 안전합니다.",
  siblings=siblings("bottomnav"),
  related='''        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><span class="na"><b>FAB</b><em>5부</em></span></li>
        <li><span class="na"><b>세이프 에어리어</b><em>11부</em></span></li>
        <li><span class="na"><b>배지</b><em>5부</em></span></li>''',
)
