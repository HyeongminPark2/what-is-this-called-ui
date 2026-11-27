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
  desc="탭이 무엇이고 세그먼티드 컨트롤·화면 이동과 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="<b>같은 대상의 다른 면</b>을 번갈아 보여 주는 줄. 화면을 떠나지 않고 내용 묶음만 바뀝니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><kbd>Tab</kbd>으로 탭 줄에 들어온 뒤 <kbd>←</kbd><kbd>→</kbd>로 옮기고, 한 번 더 <kbd>Tab</kbd>을 누르면 <b>내용으로</b> 넘어갑니다 —
          탭 다섯 개를 Tab 다섯 번으로 지나지 않습니다(<b>로빙 탭인덱스</b>).<br>
          여기서는 전부 '모란상회' 이야기이고 <b>위의 이름이 안 바뀝니다.</b> 이름까지 바뀐다면 그건 화면 이동입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "탭, 탭 메뉴, 탭 바"),
    ("영어", "tabs, tab list"),
    ("같이 쓰는 말", "탭 줄 전체가 <b>탭 리스트</b>, 칸 하나가 <b>탭</b>, 내용이 <b>탭 패널</b>입니다. 넘치면 가로로 미는 것을 <b>스크롤 가능 탭</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>세그먼티드 컨트롤</b> — 세그먼티드는 <b>값</b>을 고르고 탭은 <b>내용 묶음</b>을 바꿉니다. 가장 잦은 혼동입니다.<br>"
     "<b>바텀 탭바</b> — 이름은 닮았지만 탭바는 <b>앱 전체</b>를 오갑니다. 이 탭은 한 화면 안입니다.<br>"
     "<b>아코디언</b> — 아코디언은 여러 개를 동시에 펼칠 수 있습니다."),
  ]),
  axes=ax("탭"),
  oneline="탭은 <b>한 화면 안</b>의 전환입니다. 누른 뒤에도 제목·주소·빵부스러기가 그대로면 탭이고, 바뀌면 화면 이동입니다.",
  states=states([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div></div>', bars="", label="기본 탭"), "기본", "고른 탭에 밑줄. <b>늘 하나는 골라져 있다</b>"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span></div><div style="font-size:5.5px;color:var(--fg-muted);margin-top:4px">TX-8812 · ₩48,000</div></div>', bars="", label="다른 탭으로 옮긴 모습"), "옮김", "내용만 바뀐다. 밑줄이 미끄러지듯 움직이면 어디서 어디로 갔는지 보인다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--fg-muted);display:flex;gap:2px">문의<b style="background:var(--danger);color:#fff;border-radius:99px;padding:0 2px;font-size:4.5px">3</b></span></div></div>', bars="", label="배지가 붙은 탭"), "배지", "처리할 것이 있는 탭. 숫자는 작게"),
    (mini('<div style="margin-top:9px;padding:0 6px;overflow:hidden"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px;white-space:nowrap"><span style="font-size:5.5px;color:var(--accent);font-weight:800">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span><span style="font-size:5.5px;color:var(--fg-muted)">문의</span><span style="font-size:5.5px;color:var(--fg-muted)">설정</span><span style="font-size:5.5px;color:var(--fg-muted)">이력</span></div><div style="font-size:4.5px;color:var(--fg-muted);margin-top:3px">→ 옆으로 밀어 봅니다</div></div>', bars="", label="넘치는 탭"), "넘침", "<b>잘라서 숨기지 않는다.</b> 가로로 밀 수 있게 두고 끝이 잘린 것을 보여 준다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-faint);opacity:.5">정산 🔒</span></div></div>', bars="", label="비활성 탭"), "비활성", "권한이 없는 탭. 숨길지 흐리게 둘지 정한다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--fg-muted)">개요</span><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span></div><div style="margin-top:5px;display:grid;gap:3px"><div class="skl" style="height:5px;width:70%"></div><div class="skl" style="height:5px;width:50%"></div></div></div>', bars="", label="탭 내용 로딩"), "내용 로딩", "탭 줄은 그대로 두고 <b>내용만</b> 뼈대로. 줄까지 사라지면 길을 잃는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("탭 리스트", "tablist", "줄 전체가 하나의 부품이다. <code>role=\"tablist\"</code>"),
    ("고른 탭", "selected tab", "밑줄과 색. <b>늘 하나는 골라져 있다</b> — 아무것도 안 고른 상태가 없다"),
    ("안 고른 탭", "tab", "읽히되 눌러도 된다는 느낌이 있어야 한다"),
    ("배지", "badge", "처리할 것이 몇 건인지. 없으면 안 둔다"),
    ("탭 패널", "tabpanel", "고른 탭의 내용. <b>이것만 바뀐다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          탭은 <b>다섯 개쯤</b>이 한계입니다. 그 이상이면 가로로 밀어야 하고, 밀어야 하는 탭은
          끝에 있는 것이 거의 안 눌립니다. 여섯 개가 넘으면 사이드바나 묶음을 다시 생각할 때입니다.</p>''',
  do=ul([
    "<b>같은 대상</b>의 여러 면을 번갈아 볼 때 — 가맹점의 개요·거래·정산",
    "내용이 서로 독립이고 <b>동시에 볼 필요가 없을</b> 때",
    "묶음이 2~5개일 때",
  ]),
  dont=ul([
    "내용을 <b>나란히 비교해야</b> 할 때 — 탭은 한 번에 하나만 보입니다",
    "같은 목록을 거를 때 → 세그먼티드 컨트롤",
    "아예 다른 화면으로 갈 때 → 사이드바나 탭바",
    "탭 안에 또 탭 — 어디 있는지 금세 알 수 없게 됩니다",
  ]),
  instead='같은 목록을 거르면 <a href="segmented.html">세그먼티드</a>, 화면을 옮기면 <a href="sidebar.html">사이드바</a>·<a href="bottomnav.html">바텀 탭바</a>, 동시에 펼쳐야 하면 아코디언(2부).',
  cases=cases([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div></div>', bars="", tall=False, label="상세 화면 탭 재현"),
     "상세 화면", "가장 흔한 자리. 한 대상의 여러 면"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:4px"><span style="font-size:5.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:1px 5px;font-weight:700">전체</span><span style="font-size:5.5px;color:var(--fg-muted);border-radius:99px;padding:1px 5px">미처리</span></div></div>', bars="", tall=False, label="알약형 탭 재현"),
     "알약형", "밑줄 대신 알약. 세그먼티드와 더 헷갈리니 역할을 분명히"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:5px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">코드</span><span style="font-size:5.5px;color:var(--fg-muted)">미리보기</span></div><div style="font-size:4.5px;color:var(--fg-muted);margin-top:4px;font-family:var(--mono)">const x = 1;</div></div>', bars="", tall=False, label="코드/미리보기 탭 재현"),
     "코드 · 미리보기", "같은 것을 두 방식으로 본다. 탭의 가장 떳떳한 쓰임"),
  ]),
  code_lede="<b>로빙 탭인덱스</b>가 핵심입니다 — 탭 줄 전체가 <kbd>Tab</kbd> 한 번이고, 안에서는 화살표로 움직입니다.",
  code='''&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"tablist"</span> <span class="a">aria-label</span>=<span class="s">"가맹점 상세"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"tab"</span> <span class="a">id</span>=<span class="s">"t1"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>
          <span class="a">aria-selected</span>=<span class="s">"true"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>&gt;개요&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"tab"</span> … <span class="a">aria-selected</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"-1"</span>&gt;거래&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"tabpanel"</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">aria-labelledby</span>=<span class="s">"t1"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>&gt;…&lt;/<span class="t">div</span>&gt;

<span class="c">// 고른 탭만 tabindex=0 — 탭 줄 전체가 Tab 한 번이 된다</span>
tabs.forEach(t =&gt; t.tabIndex = (t === sel) ? <span class="a">0</span> : -<span class="a">1</span>);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "탭 줄 <b>전체를 한 번</b>에 지난다. 한 번 더 누르면 내용으로 간다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "탭을 옮기고 <b>옮기는 즉시</b> 내용이 바뀐다"),
    ("<kbd>Home</kbd><kbd>End</kbd>", "첫 탭·마지막 탭으로"),
    ("<code>aria-controls</code>", "탭과 내용을 이어 둔다. 스크린 리더가 '탭 2/5'로 읽는다"),
    ("패널", "<code>tabindex=\"0\"</code>을 줘서 내용으로 포커스가 들어갈 수 있게 한다"),
  ]),
  backend=rows([
    ("탭 = 같은 리소스의 다른 표현", "보통 같은 ID 의 다른 필드입니다. 한 번에 다 받아 두면 전환이 즉시 되고, 따로 받으면 첫 화면이 가볍습니다 — <b>어느 쪽이 나은지는 탭 수와 크기로 정합니다.</b>"),
    ("주소에 담을 것인가", "<code>/merchant/12?tab=tx</code>로 두면 공유와 뒤로가기가 됩니다. 안 담으면 새로고침 때 늘 첫 탭으로 돌아갑니다."),
    ("지연 로드", "안 열어 본 탭은 안 부르는 것이 기본입니다. 다만 <b>한 번 연 탭은 기억</b>해 두면 오갈 때 빨라집니다."),
    ("배지 숫자", "탭마다 개수를 보여 주려면 열지 않은 탭의 수도 알아야 합니다. 요약 하나로 묶어 받는 편이 요청 수를 줄입니다."),
  ]),
  plat_lede="웹과 안드로이드는 '한 화면 안의 탭'이 또렷하고, iOS 는 그 자리에 다른 부품을 씁니다.",
  plats=plats([
    ("웹", "표준 부품 없음 · ARIA 패턴",
     mini('<div style="margin-top:9px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">개요</span><span style="font-size:5.5px;color:var(--fg-muted)">거래</span></div></div>', bars="", label="웹 탭 재현"),
     "<b>탭</b> · 부품은 없고 <b>ARIA 패턴</b>이 정해져 있습니다. 밑줄 꼴이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px"><span style="display:flex;background:color-mix(in srgb,var(--line) 70%,transparent);border-radius:7px;padding:2px;gap:2px"><span style="flex:1;background:var(--surface);border-radius:5px;font-size:7px;text-align:center;padding:3px 0;font-weight:600">개요</span><span style="flex:1;font-size:7px;text-align:center;padding:3px 0;color:var(--fg-muted)">거래</span></span></div>', "iOS 세그먼티드 컨트롤 재현"),
     "화면 안 전환은 <b>세그먼티드 컨트롤</b>로 합니다. iOS 에서 '탭'은 <b>화면 아래 탭 바</b>를 뜻합니다 — 뜻이 아예 다릅니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;top:28px;display:flex;border-bottom:1px solid var(--line)"><span style="flex:1;text-align:center;font-size:7.5px;color:var(--accent);font-weight:700;padding:4px 0;border-bottom:2px solid var(--accent)">개요</span><span style="flex:1;text-align:center;font-size:7.5px;color:var(--fg-muted);padding:4px 0">거래</span></div>', "안드로이드 탭 재현"),
     "<b>탭</b>(Tabs) · Primary(화면 위)와 Secondary(그 안쪽) 두 층으로 정리돼 있고, 넘치면 미는 <b>스크롤 가능 탭</b>도 표준입니다."),
  ]),
  plat_note="iOS 에서 <b>\"탭\"은 화면 아래 탭 바</b>를 뜻합니다. 화면 안에서 내용을 바꾸는 것은 <b>세그먼티드 컨트롤</b>이라 부릅니다. \"여기 탭으로 나눠 주세요\"가 iOS 쪽에는 \"앱 전체 구조를 바꾸자\"로 들릴 수 있습니다.",
  siblings=siblings("tabs"),
  related='''        <li><a href="../items/segmented.html"><b>세그먼티드 컨트롤</b><em>4부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>배지</b><em>5부</em></span></li>
        <li><span class="na"><b>아코디언</b><em>2부</em></span></li>''',
)
