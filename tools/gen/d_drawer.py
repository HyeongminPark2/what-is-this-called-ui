# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" data-pin="1" style="background:rgba(14,16,20,.5);border-radius:var(--r2);padding:12px 60px 12px 12px;min-height:200px">
                <div data-pin="2" style="background:var(--surface);border-radius:8px;padding:12px 26px 16px;box-shadow:var(--e3)">
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;padding-bottom:10px">
                    <b style="flex:1;font-size:13px">메일</b>
                    <span style="color:var(--fg-muted);font-size:14px">&times;</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-size:11.5px;line-height:2.1;color:var(--fg-muted)">
                    <span class="pin-out" data-pin="5" style="display:block;background:var(--accent-soft);color:var(--accent);font-weight:700;border-radius:5px;padding:2px 8px;margin-bottom:2px">받은 메일</span>
                    보낸 메일<br>임시 보관
                  </div>
                  <div class="pin-out" data-pin="6" style="border-top:1px solid var(--line);margin:10px 0;height:1px"></div>
                  <div style="font-size:11.5px;color:var(--fg-muted)">설정</div>
                </div>
              </div>'''

D = dict(
  slug="drawer", ko="드로어", en="Drawer · Side panel",
  desc="드로어가 무엇인지, 사이드바나 바텀시트, 모달과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="드로어는 화면 <b>옆에서 밀려 나오는</b> 판입니다. 넓은 화면에서는 사이드바로 늘 보여 주던 내용을, 화면이 좁아 자리가 모자랄 때 숨겨 두었다가 필요할 때 꺼내 쓰는 방식입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>☰를 눌러 보세요.</b> 드로어가 왼쪽에서 밀려 나오고 뒤쪽 화면은 막힙니다. <kbd>Esc</kbd>를 누르거나 오른쪽 빈 곳을 누르면 닫히고,
          포커스가 <b>☰</b>로 돌아갑니다. ☰ 버튼은 <b>햄버거 버튼</b>이라고 부르는데, 이 이름은 드로어를 <b>여는 버튼</b>의 이름이지
          드로어의 이름이 아닙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "드로어, 서랍, 사이드 패널"),
    ("영어", "drawer, side panel, off-canvas"),
    ("같이 쓰는 말", "뒤쪽 화면을 막고 떠 있는 것은 <b>임시 드로어</b>(temporary), 넓은 화면에서 늘 붙어 있는 것은 <b>고정</b>(permanent) 드로어, 아이콘만 남기고 폭을 좁힌 것은 <b>레일</b>(rail)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>사이드바</b> — 늘 보이면 사이드바이고, 숨어 있다가 밀려 나오면 드로어입니다. 같은 내용이 화면 폭에 따라 사이드바가 되기도 하고 드로어가 되기도 합니다.<br>"
     "<b>햄버거 메뉴</b> — ☰는 드로어를 <b>여는 버튼</b>의 별명이고, 그 버튼을 눌러 나온 판이 드로어입니다.<br>"
     "<b>슬라이드 메뉴</b> — 말은 통하지만 문서에는 드로어로 적어야 오해가 없습니다."),
  ]),
  states=states([
    (mini(trigger("☰ 메뉴"), bars="684", label="드로어가 닫힌 화면"), "닫혀 있을 때", "☰ 버튼만 보입니다"),
    (mini(drawer("메일", ["받은 메일", "보낸 메일"]).replace('class="mini__drawer"', 'class="mini__drawer" style="transform:translateX(-45%)"'), bars="684", label="드로어가 밀려 나오는 중"), "옆에서 밀려 나오는 중", "0.25초 동안 옆에서 밀려 들어옵니다"),
    (mini(drawer("메일", ["받은 메일", "보낸 메일", "임시 보관"]), bars="684", label="드로어가 열린 모습"), "열려서 뒤를 막았을 때", "뒤쪽 화면이 어두워지고 클릭할 수 없게 됩니다"),
    (mini('<div class="mini__drawer" style="box-shadow:none;border-right:1px solid var(--line);width:46%;background:var(--bg)"><b>메일</b><i class="on">받은 메일</i><i>보낸 메일</i><i>임시 보관</i></div>', bars="68", label="넓은 화면에서 고정된 모습"), "넓은 화면에 고정했을 때", "화면이 넓어지면 늘 보이는 <b>사이드바</b>가 되고, 뒤쪽 화면을 막지 않습니다"),
    (mini('<div class="mini__drawer" style="box-shadow:none;border-right:1px solid var(--line);width:20%;background:var(--bg);padding:7px 4px"><div style="width:11px;height:11px;border-radius:3px;background:var(--accent);margin:0 auto 6px"></div><div style="width:11px;height:11px;border-radius:3px;background:var(--line-strong);margin:0 auto 6px"></div><div style="width:11px;height:11px;border-radius:3px;background:var(--line-strong);margin:0 auto"></div></div>', bars="68", label="아이콘만 남은 레일 모습"), "아이콘만 남긴 레일", "아이콘만 남기고 폭을 좁힌 상태입니다. 자리를 아끼면서도 각 화면으로 가는 버튼은 남겨 둡니다"),
    (mini(drawer("필터", ["상태", "기간", "금액"], side="right"), bars="684", label="오른쪽에서 나온 드로어"), "오른쪽에서 열 때", "내비게이션은 왼쪽에, 지금 보는 내용에 대한 <b>보조 작업</b>은 오른쪽에 두는 것이 관례입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크림", "scrim · backdrop", "임시 드로어에만 있고 고정 드로어에는 없습니다"),
    ("패널", "panel · drawer surface", "화면 한쪽 변에 붙고 <b>화면 높이를 다 씁니다</b>. 높이를 다 쓴다는 점이 시트와 다릅니다"),
    ("헤더 · 닫기", "header", "무엇을 하는 판인지 알려 주고, 닫기 버튼을 눈에 띄게 둡니다"),
    ("내비 목록", "nav list", "링크를 누르면 드로어가 닫힙니다. 닫지 않으면 드로어가 이동한 화면을 가립니다"),
    ("현재 위치 표시", "current · selected", "지금 보고 있는 화면을 표시합니다. 스크린 리더에는 <code>aria-current=\"page\"</code>로 알립니다"),
    ("구분선", "divider", "항목 묶음을 나눕니다. 묶음마다 제목을 다는 것보다 선 하나가 덜 눈에 띕니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          드로어가 열릴 때 뒤쪽 화면을 <b>덮을지</b>(overlay), <b>옆으로 밀어낼지</b>(push)도 정해야 합니다.
          보통 좁은 화면에서는 덮고, 넓은 화면에서는 밀어냅니다.</p>''',
  do=ul([
    "좁은 화면에서 보조 내비게이션으로 쓰던 사이드바를 접어 둘 때",
    "필터 묶음이 길어서 목록을 보면서 조건을 바꾸게 할 때. 오른쪽 드로어를 씁니다",
    "목록 옆에서 한 건을 자세히 보거나 고칠 때",
  ]),
  dont=ul([
    "이 화면의 주요 동작을 담을 때. 드로어에 숨겨 두면 사용자가 찾지 못해 쓰지 않게 됩니다",
    "짧게 한 번 확인받을 때. 이때는 모달을 씁니다",
    "넓은 화면에서 늘 필요한 내용일 때. 접어 두지 말고 사이드바로 고정합니다",
    "iOS에서 왼쪽 드로어를 쓸 때. 화면 왼쪽 가장자리에서 밀어 뒤로 가는 시스템 동작과 부딪칩니다",
  ]),
  instead='짧게 한 번 확인받는 일이라면 <a href="modal.html">모달</a>을 쓰고, 손가락으로 선택지를 고르게 할 때는 <a href="sheet.html">바텀시트</a>가 맞습니다. 누른 요소 바로 옆에 붙어 떠야 하면 <a href="popover.html">팝오버</a>를 씁니다.',
  cases=cases([
    (mini(drawer("메일", ["받은 메일", "보낸 메일", "임시 보관"]), bars="684", tall=False, label="모바일 내비 드로어 재현"),
     "좁은 화면에서 내비게이션 접어 두기", "좁은 화면에서 사이드바를 접어 둔 것으로, 왼쪽에 두는 것이 관례입니다"),
    (mini(drawer("필터", ["상태 · 전체", "기간 · 오늘"], side="right"), bars="684", tall=False, label="필터 드로어 재현"),
     "목록 옆에서 필터 바꾸기", "목록을 보면서 조건을 바꿀 수 있게 오른쪽에서 나옵니다"),
    (mini('<div class="mini__drawer" style="left:auto;right:0;width:66%;border-radius:6px 0 0 6px"><b>TX-8812</b><i>모란상회 · ₩48,000</i><i>승인 14:02</i><i style="margin-top:6px;color:var(--accent);font-weight:700">환불하기</i></div>', bars="684", tall=False, label="상세 편집 드로어 재현"),
     "목록을 떠나지 않고 한 건 고치기", "목록에서 한 건을 열어 고칩니다. 목록 화면을 떠나지 않으므로 뒤로 돌아갈 필요가 없습니다"),
  ]),
  code_lede="드로어도 바텀시트와 같은 <code>&lt;dialog&gt;</code> 요소로 만들고, <code>margin</code>과 높이만 다르게 줍니다. 화면 옆에 붙이고 높이를 꽉 채우면 드로어가 됩니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"drawer"</span>&gt;☰&lt;/<span class="t">button</span>&gt;

&lt;<span class="t">dialog</span> <span class="a">class</span>=<span class="s">"drw"</span> <span class="a">id</span>=<span class="s">"drawer"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;메일&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">nav</span>&gt;…&lt;/<span class="t">nav</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 왼쪽 변에 붙이고 높이를 꽉 채운다. 시트와 다른 부분 */</span>
dialog.drw <span class="a">{</span> <span class="t">margin</span>: 0 auto 0 0; <span class="t">height</span>: 100%; <span class="t">max-height</span>: 100%; <span class="a">}</span>

<span class="c">// 여는 버튼의 상태를 같이 알린다</span>
btn.setAttribute(<span class="s">'aria-expanded'</span>, <span class="s">'true'</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "드로어가 닫힙니다"),
    ("<kbd>Tab</kbd>", "임시 드로어에서는 포커스가 드로어 안에서만 돌고, 고정 드로어에서는 포커스를 가두지 않습니다"),
    ("안의 링크를 눌렀을 때", "드로어가 닫힙니다. 닫지 않으면 드로어가 이동한 화면을 가립니다"),
    ("여는 버튼의 상태", "드로어가 열리고 닫힐 때마다 <code>aria-expanded</code> 값도 함께 바꿉니다"),
    ("드로어가 닫힐 때", "포커스가 ☰ 버튼으로 돌아갑니다"),
  ]),
  backend=rows([
    ("열림 상태를 URL에 담기", "열림 상태를 <code>?panel=filters</code>처럼 주소에 담으면 <b>뒤로가기로 드로어를 닫을 수 있고</b>, 열린 상태 그대로 링크로 공유할 수도 있습니다. 상태를 어디에 둘지 고르는 문제라서 세션과 토큰 가운데 무엇을 쓸지 정하는 것과 비슷합니다."),
    ("주 화면과 따로 불러오는 보조 리소스", "드로어 내용은 주 화면과 다른 리소스인 경우가 많습니다. 그래서 주 화면 응답에 함께 넣지 말고 드로어를 열 때 따로 가져오면 첫 화면이 빨리 뜹니다."),
    ("임시와 고정은 데이터가 같고 표시만 다름", "임시 드로어와 고정 드로어는 화면 폭에 따라 모양만 바뀔 뿐 데이터는 같습니다. 그러므로 서버 응답을 두 가지로 나눌 필요가 없습니다."),
  ]),
  plat_lede="드로어는 안드로이드에서 자리 잡은 이름이라 iOS에는 이에 대응하는 표준 부품이 없습니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini(drawer("메일", ["받은 메일", "보낸 메일"]), bars="684", label="웹 드로어 재현"),
     "<b>드로어</b> · 좁은 화면에서는 임시 드로어로 띄우고, 화면이 넓어지면 고정 사이드바로 바꾸는 경우가 가장 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-sheet"><div class="ios-sheet__stack"><div class="ios-sheet__group"><span>받은 메일</span><span>보낸 메일</span><span>임시 보관</span></div></div></div>', "iOS 시트로 대체한 모습"),
     "<b>대응하는 표준 부품이 없어서</b> 같은 일을 <b>시트</b>나 화면 전환으로 처리합니다. 왼쪽 드로어는 화면 가장자리에서 밀어 뒤로 가는 <b>가장자리 스와이프</b>와 부딪치기 때문에 권하지 않습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;background:rgba(0,0,0,.4)"></div><div style="position:absolute;left:0;top:0;bottom:0;width:68%;background:var(--surface);border-radius:0 14px 14px 0;padding:8px"><b style="font-size:9px;display:block;margin-bottom:5px">메일</b><i style="display:block;font-style:normal;font-size:8.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:3px 7px;margin-bottom:3px">받은 메일</i><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:3px 7px">보낸 메일</i></div>', "안드로이드 내비게이션 드로어 재현"),
     "<b>내비게이션 드로어</b>(Navigation drawer) · 드로어라는 이름이 <b>처음 자리 잡은 곳</b>입니다. Modal, Standard, Dismissible로 나누고, 폭을 좁힌 것은 <b>내비게이션 레일</b>이라고 부릅니다."),
  ]),
  plat_note="\"드로어 넣어 주세요\"라는 말은 안드로이드 개발자에게는 바로 통하지만, iOS에는 드로어라는 부품이 없어서 통하지 않습니다. 그래서 보조 내비게이션처럼 역할로 말하고, iOS에서는 <b>탭 바나 시트</b> 가운데 무엇으로 바꿀지 함께 정해야 합니다.",
  siblings=siblings("drawer"),
  related='''        <li><a href="sidebar.html"><b>사이드바 내비게이션</b><em>7부</em></a></li>
        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>
        <li><a href="focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
