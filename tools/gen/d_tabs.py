# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:0 26px 18px">
                  <div class="pin-out" data-pin="1" style="display:flex;gap:40px;border-bottom:1px solid var(--line);padding:16px 0 0 26px">
                    <span class="pin-out" data-pin="2" style="font-size:11.5px;color:var(--accent);font-weight:800;padding-bottom:9px;border-bottom:2px solid var(--accent);margin-bottom:-1px">개요</span>
                    <span data-pin="3" style="font-size:11.5px;color:var(--fg-muted);padding-bottom:9px">거래</span>
                    <span class="pin-tr" data-pin="4" style="font-size:11.5px;color:var(--fg-muted);padding-bottom:9px">문의 <b style="background:var(--danger);color:#fff;border-radius:99px;padding:0 5px;font-size:9px">3</b></span>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-size:11px;color:var(--fg-muted);padding-top:18px">고른 탭의 내용이 여기 나옵니다 — 위의 가맹점 이름은 안 바뀝니다</div>
                </div>
              </div>'''

D = dict(
  slug="tabs", ko="탭", en="Tabs",
  desc="탭이 무엇인지, 세그먼티드 컨트롤·화면 이동과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="탭은 <b>같은 대상의 여러 면</b>을 번갈아 보여 주는 버튼 줄입니다. 탭을 눌러도 화면은 그대로이고, 그 아래 내용 묶음만 바뀝니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><kbd>Tab</kbd>으로 탭 줄에 들어온 뒤 <kbd>←</kbd><kbd>→</kbd>로 탭을 옮기고, <kbd>Tab</kbd>을 한 번 더 누르면 <b>내용으로</b> 넘어갑니다.
          탭이 다섯 개여도 <kbd>Tab</kbd>을 다섯 번 누를 필요 없이 한 번에 지나가는데, 이 방식을 <b>로빙 탭인덱스</b>라고 합니다.<br>
          여기서는 모든 탭이 '모란상회'에 관한 내용이라서 <b>위의 가맹점 이름이 바뀌지 않습니다.</b> 이름까지 바뀐다면 그건 탭이 아니라 화면 이동입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "탭, 탭 메뉴, 탭 바"),
    ("영어", "tabs, tab list"),
    ("같이 쓰는 말", "탭 줄 전체는 <b>탭 리스트</b>, 칸 하나는 <b>탭</b>, 탭을 눌렀을 때 보이는 내용은 <b>탭 패널</b>이라고 부릅니다. 탭이 넘쳐서 가로로 밀어 보는 것은 <b>스크롤 가능 탭</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>세그먼티드 컨트롤</b> — 세그먼티드 컨트롤은 <b>값</b>을 고르는 부품이고, 탭은 보여 줄 <b>내용 묶음</b>을 바꾸는 부품입니다. 탭과 가장 자주 헷갈리는 부품입니다.<br>"
     "<b>바텀 탭바</b> — 이름은 비슷하지만 바텀 탭바는 <b>앱 전체</b>의 화면 사이를 오가고, 탭은 한 화면 안에서 내용만 바꿉니다.<br>"
     "<b>아코디언</b> — 탭은 한 번에 내용 하나만 보이지만, 아코디언은 여러 칸을 동시에 펼칠 수 있습니다."),
  ]),
  axes=ax("탭"),
  oneline="탭은 <b>한 화면 안</b>에서 내용을 바꿉니다. 누른 뒤에도 제목과 주소, 브레드크럼이 그대로면 탭이고, 이것들이 바뀌면 화면 이동입니다.",
  states=states([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div></div>', bars="", label="기본 탭"), "기본", "고른 탭에 밑줄이 있습니다. 탭은 <b>늘 하나가 골라져 있습니다</b>"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span></div><div style="font-size:5.5px;color:var(--fg-muted);margin-top:4px">TX-8812 · ₩48,000</div></div>', bars="", label="다른 탭으로 옮긴 모습"), "옮김", "아래 내용만 바뀝니다. 밑줄이 옆 탭으로 움직이는 애니메이션을 넣으면 어느 탭에서 어느 탭으로 옮겼는지 보입니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--fg-muted);display:flex;gap:2px">문의<b style="background:var(--danger);color:#fff;border-radius:99px;padding:0 2px;font-size:4.5px">3</b></span></div></div>', bars="", label="배지가 붙은 탭"), "배지", "처리할 것이 있는 탭에 건수를 붙입니다. 숫자는 탭 이름보다 작게 씁니다"),
    (mini('<div style="margin-top:9px;padding:0 6px;overflow:hidden"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px;white-space:nowrap"><span style="font-size:5.5px;color:var(--accent);font-weight:800">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span><span style="font-size:5.5px;color:var(--fg-muted)">문의</span><span style="font-size:5.5px;color:var(--fg-muted)">설정</span><span style="font-size:5.5px;color:var(--fg-muted)">이력</span></div><div style="font-size:4.5px;color:var(--fg-muted);margin-top:3px">→ 옆으로 밀어 봅니다</div></div>', bars="", label="넘치는 탭"), "넘침", "넘치는 탭을 <b>잘라서 숨기지 않습니다.</b> 가로로 밀 수 있게 두고, 끝 탭이 잘려 보이게 해서 더 있다는 것을 알립니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-faint);opacity:.5">정산 🔒</span></div></div>', bars="", label="비활성 탭"), "비활성", "권한이 없는 탭입니다. 숨길지 흐리게 둘지 정해야 합니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span></div><div style="margin-top:5px;display:grid;gap:3px"><div class="skl" style="height:5px;width:70%"></div><div class="skl" style="height:5px;width:50%"></div></div></div>', bars="", label="탭 내용 로딩"), "내용 로딩", "탭 줄은 그대로 두고 <b>내용만</b> 뼈대 모양으로 보여 줍니다. 탭 줄까지 사라지면 사용자가 어느 탭을 눌렀는지 알 수 없습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("탭 리스트", "tablist", "탭 줄 전체가 하나의 부품이며, <code>role=\"tablist\"</code>를 답니다"),
    ("고른 탭", "selected tab", "밑줄과 글자색으로 표시합니다. 탭은 <b>늘 하나가 골라져 있어서</b> 아무것도 고르지 않은 상태가 없습니다"),
    ("안 고른 탭", "tab", "글자가 충분히 읽혀야 하고, 누를 수 있는 탭이라는 것이 보여야 합니다"),
    ("배지", "badge", "처리할 것이 몇 건인지 보여 줍니다. 처리할 것이 없으면 두지 않습니다"),
    ("탭 패널", "tabpanel", "고른 탭의 내용입니다. 탭을 옮기면 <b>이 영역만 바뀝니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          탭은 <b>다섯 개 정도</b>까지가 알맞습니다. 그보다 많으면 탭 줄을 가로로 밀어야 하는데, 밀어야 보이는 탭은
          끝에 있는 것일수록 사용자가 거의 누르지 않습니다. 탭이 여섯 개를 넘으면 사이드바로 옮기거나 묶음을 다시 나눌지 검토합니다.</p>''',
  do=ul([
    "가맹점의 개요·거래·정산처럼 <b>같은 대상</b>의 여러 면을 번갈아 볼 때",
    "내용 묶음이 서로 독립적이고 <b>동시에 볼 필요가 없을</b> 때",
    "묶음이 2~5개일 때",
  ]),
  dont=ul([
    "내용을 <b>나란히 비교해야</b> 할 때. 탭은 한 번에 하나만 보여 줍니다",
    "같은 목록을 조건으로 거를 때. 세그먼티드 컨트롤을 씁니다",
    "아예 다른 화면으로 갈 때. 사이드바나 탭바를 씁니다",
    "탭 안에 또 탭을 넣을 때. 지금 어느 탭의 어느 탭을 보고 있는지 금세 헷갈립니다",
  ]),
  instead='같은 목록을 거르면 <a href="segmented.html">세그먼티드</a>, 화면을 옮기면 <a href="sidebar.html">사이드바</a>·<a href="bottomnav.html">바텀 탭바</a>, 동시에 펼쳐야 하면 아코디언(2부).',
  cases=cases([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div></div>', bars="", tall=False, label="상세 화면 탭 재현"),
     "상세 화면", "탭을 가장 흔하게 쓰는 곳입니다. 한 대상의 여러 면을 나눠 보여 줍니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:4px"><span style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:1px 5px;font-weight:700">전체</span><span style="font-size:5.5px;color:var(--fg-muted);border-radius:99px;padding:1px 5px">미처리</span></div></div>', bars="", tall=False, label="알약형 탭 재현"),
     "알약형", "밑줄 대신 알약 모양으로 고른 탭을 표시합니다. 세그먼티드 컨트롤과 더 헷갈리므로 탭이라는 역할이 분명히 드러나게 합니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:5px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">코드</span><span style="font-size:5.5px;color:var(--fg-muted)">미리보기</span></div><div style="font-size:4.5px;color:var(--fg-muted);margin-top:4px;font-family:var(--mono)">const x = 1;</div></div>', bars="", tall=False, label="코드/미리보기 탭 재현"),
     "코드 · 미리보기", "같은 내용을 두 방식으로 봅니다. 한 대상의 여러 면을 보여 준다는 탭의 쓰임에 가장 잘 맞습니다"),
  ]),
  code_lede="핵심은 <b>로빙 탭인덱스</b>입니다. 고른 탭 하나만 <kbd>Tab</kbd> 순서에 넣기 때문에 탭 줄 전체를 <kbd>Tab</kbd> 한 번에 지나가고, 탭 줄 안에서는 화살표로 움직입니다.",
  code='''&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"tablist"</span> <span class="a">aria-label</span>=<span class="s">"가맹점 상세"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"tab"</span> <span class="a">id</span>=<span class="s">"t1"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>
          <span class="a">aria-selected</span>=<span class="s">"true"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>&gt;개요&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"tab"</span> … <span class="a">aria-selected</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"-1"</span>&gt;거래&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"tabpanel"</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">aria-labelledby</span>=<span class="s">"t1"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>&gt;…&lt;/<span class="t">div</span>&gt;

<span class="c">// 고른 탭만 tabindex=0. 그래서 탭 줄 전체를 Tab 한 번에 지나간다</span>
tabs.forEach(t =&gt; t.tabIndex = (t === sel) ? <span class="a">0</span> : -<span class="a">1</span>);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "탭 줄 <b>전체를 한 번에</b> 지나가고, 한 번 더 누르면 내용으로 갑니다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "탭을 옮기며, <b>옮기는 즉시</b> 내용이 바뀝니다"),
    ("<kbd>Home</kbd><kbd>End</kbd>", "첫 탭이나 마지막 탭으로 갑니다"),
    ("<code>aria-controls</code>", "탭과 내용을 연결합니다. 스크린 리더는 '탭 2/5'처럼 읽습니다"),
    ("패널", "<code>tabindex=\"0\"</code>을 줘서 포커스가 내용으로 들어갈 수 있게 합니다"),
  ]),
  backend=rows([
    ("탭 = 같은 리소스의 다른 표현", "탭들은 보통 같은 ID를 가진 리소스의 서로 다른 필드를 보여 줍니다. 모든 탭의 데이터를 한 번에 받아 두면 탭을 바로 바꿀 수 있고, 탭마다 따로 받으면 첫 화면을 빨리 띄울 수 있습니다. <b>어느 쪽이 나은지는 탭 수와 데이터 크기를 보고 정합니다.</b>"),
    ("주소에 담을 것인가", "<code>/merchant/12?tab=tx</code>처럼 고른 탭을 주소에 담으면 링크로 공유할 수 있고 뒤로가기도 탭 단위로 됩니다. 주소에 담지 않으면 새로고침할 때마다 첫 탭으로 돌아갑니다."),
    ("지연 로드", "열어 보지 않은 탭의 데이터는 요청하지 않는 것이 기본입니다. 다만 <b>한 번 연 탭의 데이터를 기억</b>해 두면 탭을 오갈 때 다시 받지 않아 빨라집니다."),
    ("배지 숫자", "탭마다 건수를 보여 주려면 아직 열지 않은 탭의 건수도 알아야 합니다. 탭마다 따로 묻기보다 요약 응답 하나로 묶어 받으면 요청 수가 줄어듭니다."),
  ]),
  plat_lede="웹과 안드로이드에는 '한 화면 안의 탭'이 분명히 있지만, iOS는 같은 자리에 다른 부품을 씁니다.",
  plats=plats([
    ("웹", "표준 부품 없음 · ARIA 패턴",
     mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span></div></div>', bars="", label="웹 탭 재현"),
     "<b>탭</b> · 기본 부품은 없지만 <b>ARIA 패턴</b>이 정해져 있습니다. 고른 탭에 밑줄을 긋는 모양이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px"><span style="display:flex;background:color-mix(in srgb,var(--line) 70%,transparent);border-radius:7px;padding:2px;gap:2px"><span style="flex:1;background:var(--surface);border-radius:5px;font-size:7px;text-align:center;padding:3px 0;font-weight:600">개요</span><span style="flex:1;font-size:7px;text-align:center;padding:3px 0;color:var(--fg-muted)">거래</span></span></div>', "iOS 세그먼티드 컨트롤 재현"),
     "화면 안에서 내용을 바꿀 때는 <b>세그먼티드 컨트롤</b>을 씁니다. iOS에서 '탭'은 <b>화면 아래 탭 바</b>를 뜻하기 때문에 웹에서 말하는 탭과 뜻이 전혀 다릅니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:28px;display:flex;border-bottom:1px solid var(--line)"><span style="flex:1;text-align:center;font-size:7.5px;color:var(--accent);font-weight:700;padding:4px 0;border-bottom:2px solid var(--accent)">개요</span><span style="flex:1;text-align:center;font-size:7.5px;color:var(--fg-muted);padding:4px 0">거래</span></div>', "안드로이드 탭 재현"),
     "<b>탭</b>(Tabs) · 화면 위에 두는 Primary와 그 안쪽에 두는 Secondary, 두 층으로 나뉩니다. 탭이 넘칠 때 가로로 밀어 보는 <b>스크롤 가능 탭</b>도 표준에 들어 있습니다."),
  ]),
  plat_note="iOS에서 <b>\"탭\"은 화면 아래 탭 바</b>를 뜻하고, 화면 안에서 내용을 바꾸는 부품은 <b>세그먼티드 컨트롤</b>이라고 부릅니다. 그래서 \"여기를 탭으로 나눠 주세요\"라는 요청이 iOS 개발자에게는 \"앱 전체 구조를 바꾸자\"는 뜻으로 들릴 수 있습니다.",
  siblings=siblings("tabs"),
  related='''        <li><a href="../items/segmented.html"><b>세그먼티드 컨트롤</b><em>4부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>배지</b><em>5부</em></span></li>
        <li><span class="na"><b>아코디언</b><em>2부</em></span></li>''',
)
