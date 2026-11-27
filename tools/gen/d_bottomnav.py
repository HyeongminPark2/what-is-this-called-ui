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
  desc="바텀 탭바가 무엇인지, 탭·사이드바와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="바텀 탭바는 폰 화면 <b>아래에 늘 붙어 있는</b> 메뉴입니다. 앱 전체를 서너 개의 주요 영역으로 나누고, 폰을 쥔 손의 엄지가 닿는 화면 아래에 둡니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>거래를 여러 번 눌러 보세요.</b> 처음 누르면 거래 화면으로 가고, <b>이미 거래 화면에 있으면 목록 맨 위로</b> 올라갑니다.
          화면에 따로 적혀 있지는 않지만 사용자들이 당연하게 기대하는 탭바 동작입니다. 탭마다 <b>스크롤 위치를 따로 기억</b>하는 것도 확인해 보세요.<br>
          칸은 <b>3~5개</b>까지 둡니다. 그보다 많으면 칸이 좁아져 손가락으로 누르기 어렵고 글자가 잘립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "바텀 탭바, 하단 탭, 탭바, 하단 내비게이션"),
    ("영어", "tab bar (iOS), bottom navigation (Android), bottom nav"),
    ("같이 쓰는 말", "칸 하나는 <b>탭</b>, 칸 위의 빨간 숫자는 <b>배지</b>, 넓은 화면에서 같은 메뉴를 화면 옆에 세로로 세운 것은 <b>레일</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>탭</b> — 이름은 같지만 <a href=\"tabs.html\">화면 안의 탭</a>은 <b>한 화면 안에서 다른 내용</b>을 보여 주고, 탭바는 <b>앱 전체</b>의 주요 영역 사이를 오갑니다.<br>"
     "<b>푸터</b> — 푸터는 스크롤 끝에 나오는 정보 영역이고, 탭바는 스크롤과 상관없이 늘 화면 아래에 떠 있습니다.<br>"
     "<b>툴바</b> — 툴바는 실행할 동작 버튼을 모아 두고, 탭바는 앱을 갈 곳 몇 개로 나눠 둡니다."),
  ]),
  axes=ax("바텀 탭바"),
  oneline="바텀 탭바는 앱을 <b>서너 개의 주요 영역</b>으로 나눕니다. 영역이 여섯 개를 넘으면 칸을 더 좁게 나눌 것이 아니라 <b>앱 구조를 다시 짜야 합니다</b>.",
  states=states([
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span></div>', bars="684", label="기본 탭바"), "가장 흔한 기본 모습", "고른 칸만 색이 다릅니다. 탭바는 <b>늘 한 칸이 골라져 있습니다</b>"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px;position:relative"><span style="position:absolute;top:-2px;right:-3px;background:var(--danger);color:#fff;border-radius:99px;font-size:3.5px;padding:0 2px">3</span></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span></div>', bars="684", label="배지가 붙은 탭바"), "처리할 건수를 붙일 때", "처리할 것이 몇 건인지 보여 줍니다. 건수를 보여 줄 필요가 없으면 점만 찍기도 합니다"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 1px 5px"><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">홈</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">거래</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">정산</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">가맹…</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">내정…</span><span style="flex:1;text-align:center;font-size:4px;color:var(--fg-muted);overflow:hidden">더보…</span></div><div style="position:absolute;left:5px;bottom:18px;font-size:4.5px;color:var(--danger);font-weight:700">여섯 칸이면 글자가 잘림</div>', bars="684", label="칸이 너무 많은 탭바"), "칸이 너무 많을 때", "다섯 칸을 넘기면 글자가 잘립니다. 이럴 때는 <b>앱 구조를 다시 짜야 합니다</b>"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">거래</span></span></div><div style="position:absolute;left:5px;bottom:18px;font-size:4.5px;color:var(--accent);font-weight:700">다시 누르면 맨 위로</div>', bars="684", label="같은 탭을 다시 누른 모습"), "같은 탭을 다시 눌렀을 때", "지금 탭을 다시 누르면 <b>목록 맨 위로 올라갑니다.</b> 한 번 더 누르면 그 탭의 첫 화면으로 돌아갑니다"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px;transform:translateY(100%)"></div><div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:5px;bottom:6px;font-size:4.5px;color:var(--fg-muted)">몰입 화면이라 탭바를 감춤</div>', bars="", label="탭바를 감춘 모습"), "몰입 화면에서 감출 때", "영상이나 지도처럼 화면 전체를 쓰는 몰입 화면에서는 탭바를 감춥니다. 이때도 <b>원래 화면으로 돌아갈 버튼</b>은 꼭 남깁니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:22%;border-right:1px solid var(--line);padding:5px 2px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--accent)">거래</div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:5px auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--fg-muted)">정산</div></div>', bars="", label="넓은 화면에서 레일이 된 모습"), "넓은 화면에서", "같은 항목이 <b>레일</b>이 되어 화면 옆에 세로로 섭니다. 화면이 더 넓으면 사이드바로 바뀝니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("탭바", "tab bar", "화면 아래에 고정돼 있어서 스크롤해도 그 자리에 남습니다"),
    ("탭 하나", "tab", "누르는 영역은 <b>48px 이상</b>으로 잡고, 칸 폭은 모두 같게 나눕니다"),
    ("아이콘", "icon", "고른 칸은 <b>속을 채운 아이콘</b>, 고르지 않은 칸은 <b>선으로만 그린 아이콘</b>으로 구별하는 것이 관례입니다"),
    ("배지", "badge", "처리할 것이 몇 건인지 보여 주며, 아이콘 오른쪽 위에 붙입니다"),
    ("이름", "label", "아이콘만으로는 어떤 화면인지 알기 어려우므로 <b>아이콘만 두지 않고</b> 이름을 함께 적습니다"),
    ("세이프 에어리어", "safe area inset", "화면 아래 홈 인디케이터에 탭이 가리지 않도록 <b>아래에 더 두는</b> 여백입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          탭바에는 그림에 보이지 않는 규칙이 두 가지 있습니다. 하나는 <b>탭마다 그 탭에서 열어 둔 화면 기록과 스크롤 위치를 따로 기억</b>하는 것이고,
          다른 하나는 <b>지금 탭을 다시 누르면 맨 위로</b> 올라가는 것입니다. 두 규칙 모두 눈에 띄지는 않지만, 빠지면 사용자가 곧바로 불편을 느낍니다.</p>''',
  do=ul([
    "앱의 <b>주요 영역이 3~5개</b>일 때",
    "주요 영역 사이를 자주 오갈 때. 어느 화면에서든 한 번 눌러서 갈 수 있습니다",
    "폰에서 엄지로 조작하는 화면일 때",
  ]),
  dont=ul([
    "주요 영역이 여섯 개를 넘을 때. 글자가 잘리므로 <b>앱 구조를 다시 짭니다</b>",
    "'더 보기' 칸 하나에 나머지 영역을 몰아넣을 때. 그 안에 든 화면은 사용자가 거의 찾아 쓰지 않습니다",
    "글쓰기·저장 같은 동작을 탭으로 넣을 때. 탭은 <b>다른 화면으로 가는 링크</b>이고, 주요 동작은 FAB에 둡니다",
    "아이콘만 둘 때. 아이콘만으로는 어떤 화면인지 알기 어렵습니다",
  ]),
  instead='넓은 화면에서는 같은 항목을 <a href="sidebar.html">사이드바</a>로 보여 주고, 한 화면 안에서 내용만 바꾸려면 <a href="tabs.html">탭</a>을 씁니다. 글쓰기 같은 주요 동작은 FAB(5부)에 두고, 늘 보일 필요가 없는 길은 <a href="drawer.html">드로어</a>에 넣습니다.',
  cases=cases([
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent);font-weight:700">홈</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">검색</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">내 정보</span></span></div>', bars="684", tall=False, label="세 칸 탭바 재현"),
     "세 칸으로 나누기", "가장 안전한 칸 수입니다. 칸이 넓어서 글자가 잘릴 일이 없습니다"),
    (mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">홈</span></span><span style="flex:1;text-align:center"><span style="display:block;width:12px;height:12px;border-radius:50%;background:var(--accent);margin:-6px auto 1px;color:#fff;font-size:7px;line-height:12px">＋</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">내 정보</span></span></div>', bars="684", tall=False, label="가운데 동작 버튼 재현"),
     "가운데 칸에 주요 동작 두기", "글쓰기 같은 주요 동작을 가운데 칸에 둡니다. 다른 화면으로 가는 탭이 아니라 <b>동작 버튼</b>이므로 다른 칸과 모양을 다르게 합니다"),
    (mini('<div style="position:absolute;left:0;top:0;bottom:0;width:22%;border-right:1px solid var(--line);padding:5px 2px"><div style="width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--accent)">홈</div><div style="width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:5px auto 1px"></div><div style="font-size:4px;text-align:center;color:var(--fg-muted)">검색</div></div>', bars="", tall=False, label="레일 재현"),
     "태블릿에서 레일로 바꾸기", "태블릿 폭에서는 같은 항목이 화면 옆에 세로로 섭니다"),
  ]),
  code_lede="마크업은 <code>&lt;nav&gt;</code>와 <code>aria-current</code>면 충분합니다. 구현에서 까다로운 부분은 <b>탭마다 스크롤 위치 같은 상태를 따로 기억하는 일</b>입니다.",
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

<span class="c">/* 홈 인디케이터에 가리지 않게 아래 여백을 더 둔다 */</span>
<span class="t">padding-bottom</span>: <span class="a">calc</span>(10px + env(safe-area-inset-bottom));''',
  keys=kbd([
    ("<code>aria-current</code>", "지금 탭에 <code>\"page\"</code> 값을 답니다. 색만으로는 스크린 리더에 전해지지 않습니다"),
    ("탭의 아이콘", "<code>aria-hidden</code>으로 스크린 리더에서 숨기고, <b>이름 글자를 읽게</b> 합니다"),
    ("누르는 영역의 크기", "48px 이상으로 잡습니다. 화면 아래 끝에 붙어 있어서 손가락으로 누르기 쉬운 자리이기도 합니다"),
    ("배지 숫자를 읽어 줄 때", "숫자만 읽히지 않도록 '읽지 않음 3건'처럼 <b>무슨 숫자인지까지</b> 라벨에 담습니다"),
    ("<kbd>Tab</kbd>", "칸마다 포커스가 한 번씩 거쳐 갑니다. 보통 서너 번이면 지나가서 부담이 적습니다"),
  ]),
  backend=rows([
    ("탭마다 따로 두는 화면 기록", "탭마다 자기 화면 기록과 스크롤 위치를 따로 저장합니다. 모든 탭을 전역 스택 하나로 다루면 <b>탭을 옮길 때마다 그 탭의 첫 화면으로</b> 돌아가서 불편해집니다."),
    ("배지 숫자를 폴링이나 푸시로 받기", "배지 숫자는 모든 화면에 떠 있어서 자주 갱신해야 합니다. 폴링으로 받으면 요청 주기를, 푸시로 받으면 연결을 관리해야 하는데, 어느 쪽이든 <b>가장 자주 호출되는 API</b>가 되기 쉽습니다."),
    ("앱을 열 때 첫 탭부터 요청하기", "앱을 열면 첫 탭의 데이터가 곧바로 필요합니다. 나머지 탭의 데이터는 그 탭을 <b>열 때</b> 요청하고, 탭을 자주 오가는 앱이면 캐시를 둡니다."),
    ("탭 수에 드러나는 제품 구조", "탭이 여섯 개로 늘어나는 것은 대개 화면 설계의 문제가 아닙니다. <b>제품이 무엇을 하는 서비스인지</b>가 흐려졌을 때 이런 일이 생깁니다."),
  ]),
  plat_lede="바텀 탭바는 iOS와 안드로이드가 서로 다른 이름으로 부르면서, 두 플랫폼 모두 <b>특히 자세하게 규칙을 정해 둔</b> 부품입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);padding:3px 2px 5px"><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--accent);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--accent)">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:8px;height:8px;border-radius:2px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:4.5px;color:var(--fg-muted)">정산</span></span></div>', bars="684", label="웹 하단 내비 재현"),
     "모바일 웹을 앱처럼 보이게 하려고 씁니다. 브라우저 주소창과 겹치지 않도록 <code>env(safe-area-inset-bottom)</code>으로 아래 여백을 둬야 합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:8px;display:flex;border-top:1px solid var(--line);padding:4px 2px"><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:#0a84ff;margin:0 auto 1px"></span><span style="font-size:5px;color:#0a84ff">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:5px;color:var(--fg-muted)">정산</span></span></div>', "iOS 탭 바 재현"),
     "<b>탭 바</b>(Tab bar) · 칸은 <b>2~5개</b>를 권합니다. 같은 탭을 다시 누르면 맨 위로 가는 동작과 탭마다 화면 기록을 따로 두는 방식이 시스템 관례로 자리 잡았습니다. iOS에서 \"탭\"이라고 하면 이 탭 바를 뜻합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;bottom:8px;display:flex;padding:5px 2px"><span style="flex:1;text-align:center"><span style="display:block;width:22px;height:11px;border-radius:99px;background:var(--accent-soft);margin:0 auto 1px;position:relative"><span style="position:absolute;left:50%;top:2px;transform:translateX(-50%);width:7px;height:7px;border-radius:2px;background:var(--accent)"></span></span><span style="font-size:5px;color:var(--accent);font-weight:700">거래</span></span><span style="flex:1;text-align:center"><span style="display:block;width:10px;height:10px;border-radius:3px;background:var(--line-strong);margin:0 auto 1px"></span><span style="font-size:5px;color:var(--fg-muted)">정산</span></span></div>', "안드로이드 내비게이션 바 재현"),
     "<b>내비게이션 바</b>(Navigation bar) · 칸은 <b>3~5개</b>입니다. M3에서는 고른 칸의 아이콘 뒤에 <b>알약 모양 배경</b>을 깔아 표시합니다."),
  ]),
  plat_note="안드로이드에서 <b>\"내비게이션 바\"</b>는 이 하단 메뉴를 뜻하지만, <b>iOS에서는 같은 말이 화면 위 앱바</b>를 뜻합니다. 같은 이름이 <b>화면 위와 아래로 정반대 자리</b>를 가리키기 때문에, 두 플랫폼 개발자가 함께 일할 때 가장 크게 엇갈리는 이름입니다. 그래서 '아래 탭바'처럼 위치를 붙여 말하는 편이 안전합니다.",
  siblings=siblings("bottomnav"),
  related='''        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><span class="na"><b>FAB</b><em>5부</em></span></li>
        <li><a href="safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="badge.html"><b>배지</b><em>5부</em></a></li>''',
)
