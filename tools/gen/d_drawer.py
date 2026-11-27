# -*- coding: utf-8 -*-
from parts import *
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

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
  desc="드로어가 무엇이고 사이드바·바텀시트·모달과 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="화면 <b>옆에서 밀려 나오는</b> 판. 넓은 화면에서 늘 보이는 사이드바와 같은 내용을, 자리가 모자랄 때 숨겼다 꺼내 쓰는 것입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>☰ 를 눌러 보세요.</b> 왼쪽에서 밀려 나오고 뒤가 막힙니다. <kbd>Esc</kbd>나 오른쪽 빈 곳을 누르면 닫히고,
          포커스가 <b>☰</b>로 돌아갑니다. ☰ 자체는 <b>햄버거 버튼</b>이라 부르는데, 그건 <b>여는 버튼</b>의 이름이지
          드로어의 이름이 아닙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "드로어, 서랍, 사이드 패널"),
    ("영어", "drawer, side panel, off-canvas"),
    ("같이 쓰는 말", "뒤를 막고 떠 있으면 <b>임시 드로어</b>(temporary), 넓은 화면에서 늘 붙어 있으면 <b>고정</b>(permanent), 아이콘만 남겨 좁힌 것은 <b>레일</b>(rail)."),
    ("자주 잘못 부름",
     "<b>사이드바</b> — 늘 보이면 사이드바, 숨었다 밀려 나오면 드로어입니다. 같은 내용이 폭에 따라 둘 사이를 오갑니다.<br>"
     "<b>햄버거 메뉴</b> — ☰ 는 <b>여는 버튼</b>의 별명입니다. 열려 나온 판이 드로어입니다.<br>"
     "<b>슬라이드 메뉴</b> — 통하기는 하지만 문서에는 드로어로 적는 편이 안전합니다."),
  ]),
  axes=axis_table("드로어"),
  oneline="드로어인지는 <b>옆에서 밀려 나오느냐</b>로 정해집니다. 늘 보이면 사이드바이고, 숨었다 나오면 드로어입니다.",
  states=states([
    (mini(trigger("☰ 메뉴"), bars="684", label="드로어가 닫힌 화면"), "닫힘", "☰ 만 보인다"),
    (mini(drawer("메일", ["받은 메일", "보낸 메일"]).replace('class="mini__drawer"', 'class="mini__drawer" style="transform:translateX(-45%)"'), bars="684", label="드로어가 밀려 나오는 중"), "밀려 나오는 중", "0.25초. 옆에서 들어온다"),
    (mini(drawer("메일", ["받은 메일", "보낸 메일", "임시 보관"]), bars="684", label="드로어가 열린 모습"), "열림 · 막음", "뒤가 어두워지고 클릭이 막힌다"),
    (mini('<div class="mini__drawer" style="box-shadow:none;border-right:1px solid var(--line);width:46%;background:var(--bg)"><b>메일</b><i class="on">받은 메일</i><i>보낸 메일</i><i>임시 보관</i></div>', bars="68", label="넓은 화면에서 고정된 모습"), "고정", "넓어지면 늘 보이는 <b>사이드바</b>가 된다. 뒤를 안 막는다"),
    (mini('<div class="mini__drawer" style="box-shadow:none;border-right:1px solid var(--line);width:20%;background:var(--bg);padding:7px 4px"><div style="width:11px;height:11px;border-radius:3px;background:var(--accent);margin:0 auto 6px"></div><div style="width:11px;height:11px;border-radius:3px;background:var(--line-strong);margin:0 auto 6px"></div><div style="width:11px;height:11px;border-radius:3px;background:var(--line-strong);margin:0 auto"></div></div>', bars="68", label="아이콘만 남은 레일 모습"), "레일", "아이콘만 남기고 좁힌 상태. 자리를 아끼되 길은 남긴다"),
    (mini(drawer("필터", ["상태", "기간", "금액"], side="right"), bars="684", label="오른쪽에서 나온 드로어"), "오른쪽", "내비게이션은 왼쪽, 지금 보는 것에 대한 <b>보조 작업</b>은 오른쪽이 관례다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크림", "scrim · backdrop", "임시 드로어에만 있다. 고정 드로어에는 없다"),
    ("패널", "panel · drawer surface", "한쪽 변에 붙고 <b>화면 높이를 다 쓴다</b>. 이 점이 시트와 다르다"),
    ("헤더 · 닫기", "header", "어디로 가는 판인지. 닫기를 눈에 보이게 둔다"),
    ("내비 목록", "nav list", "링크를 누르면 드로어는 닫힌다. 안 닫으면 어디로 갔는지 가린다"),
    ("현재 위치 표시", "current · selected", "지금 보고 있는 곳. <code>aria-current=\"page\"</code> 로도 알린다"),
    ("구분선", "divider", "묶음을 가른다. 선 하나가 제목 하나보다 조용하다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          드로어가 열릴 때 뒤쪽 화면을 <b>덮는지</b>(overlay) <b>옆으로 미는지</b>(push)도 고르는 축입니다.
          좁은 화면은 덮기, 넓은 화면은 밀기가 보통입니다.</p>''',
  do=ul([
    "보조 내비게이션 — 좁은 화면에서 사이드바를 접어 둘 때",
    "긴 필터 묶음 — 목록을 보면서 조건을 바꾸게 (오른쪽 드로어)",
    "목록 옆에서 한 건을 자세히 보거나 고칠 때",
  ]),
  dont=ul([
    "이 화면의 주요 동작 — 숨겨 두면 안 쓰게 됩니다",
    "짧은 확인 한 번 → 모달",
    "넓은 화면에서 늘 필요한 것 → 접지 말고 사이드바로 고정합니다",
    "왼쪽 드로어 + iOS — 시스템의 가장자리 스와이프 뒤로가기와 부딪칩니다",
  ]),
  instead='짧은 확인이면 <a href="modal.html">모달</a>, 손가락으로 고르는 것이면 <a href="sheet.html">바텀시트</a>, 누른 것 옆에 붙어야 하면 <a href="popover.html">팝오버</a>.',
  cases=cases([
    (mini(drawer("메일", ["받은 메일", "보낸 메일", "임시 보관"]), bars="684", tall=False, label="모바일 내비 드로어 재현"),
     "내비 드로어", "좁은 화면에서 사이드바를 접어 둔 것. 왼쪽이 관례"),
    (mini(drawer("필터", ["상태 · 전체", "기간 · 오늘"], side="right"), bars="684", tall=False, label="필터 드로어 재현"),
     "필터 드로어", "목록을 보면서 조건을 바꾼다. 오른쪽에서 나온다"),
    (mini('<div class="mini__drawer" style="left:auto;right:0;width:66%;border-radius:6px 0 0 6px"><b>TX-8812</b><i>모란상회 · ₩48,000</i><i>승인 14:02</i><i style="margin-top:6px;color:var(--accent);font-weight:700">환불하기</i></div>', bars="684", tall=False, label="상세 편집 드로어 재현"),
     "상세 패널", "목록에서 한 건을 열어 고친다. 뒤로 가지 않아도 된다"),
  ]),
  code_lede="바텀시트와 같은 <code>&lt;dialog&gt;</code>인데 <code>margin</code>과 높이만 다릅니다. 옆에 붙이고 높이를 꽉 채우면 드로어입니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"drawer"</span>&gt;☰&lt;/<span class="t">button</span>&gt;

&lt;<span class="t">dialog</span> <span class="a">class</span>=<span class="s">"drw"</span> <span class="a">id</span>=<span class="s">"drawer"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;메일&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">nav</span>&gt;…&lt;/<span class="t">nav</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 왼쪽 변에 붙이고 높이를 꽉 채운다 — 시트와 갈리는 곳 */</span>
dialog.drw <span class="a">{</span> <span class="t">margin</span>: 0 auto 0 0; <span class="t">height</span>: 100%; <span class="t">max-height</span>: 100%; <span class="a">}</span>

<span class="c">// 여는 버튼의 상태를 같이 알린다</span>
btn.setAttribute(<span class="s">'aria-expanded'</span>, <span class="s">'true'</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "닫힌다"),
    ("<kbd>Tab</kbd>", "임시 드로어 안에서만 돈다. 고정 드로어는 안 가둔다"),
    ("링크 누름", "드로어가 닫힌다. 안 닫으면 이동한 화면을 자기가 가린다"),
    ("여는 버튼", "<code>aria-expanded</code> 가 열림/닫힘을 따라간다"),
    ("닫힐 때", "포커스가 ☰ 로 돌아간다"),
  ]),
  backend=rows([
    ("열림 상태를 URL 에", "<code>?panel=filters</code> 처럼 주소에 담으면 <b>뒤로가기로 닫히고</b> 링크로 공유됩니다. 상태를 어디에 둘지의 문제라, 세션 vs 토큰과 같은 결정입니다."),
    ("보조 리소스", "드로어 내용은 주 화면과 다른 리소스인 경우가 많습니다. 주 화면 응답에 끼워 넣지 말고 열 때 따로 가져오면 첫 화면이 빨라집니다."),
    ("임시 vs 고정 = 같은 데이터, 다른 표시", "폭에 따라 모양만 바뀌고 데이터는 같습니다. 응답을 둘로 나누지 않습니다."),
  ]),
  plat_lede="드로어는 안드로이드에서 굳은 말이라 iOS 에는 대응하는 표준 부품이 없습니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini(drawer("메일", ["받은 메일", "보낸 메일"]), bars="684", label="웹 드로어 재현"),
     "<b>드로어</b> · 좁은 화면에서는 임시, 넓어지면 고정 사이드바로 바뀌는 쓰임이 가장 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-sheet"><div class="ios-sheet__stack"><div class="ios-sheet__group"><span>받은 메일</span><span>보낸 메일</span><span>임시 보관</span></div></div></div>', "iOS 시트로 대체한 모습"),
     "<b>대응하는 표준이 없습니다.</b> 같은 일을 <b>시트</b>나 화면 전환으로 합니다. 왼쪽 드로어는 <b>가장자리 스와이프 뒤로가기</b>와 부딪쳐 권하지 않습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;background:rgba(0,0,0,.4)"></div><div style="position:absolute;left:0;top:0;bottom:0;width:68%;background:var(--surface);border-radius:0 14px 14px 0;padding:8px"><b style="font-size:9px;display:block;margin-bottom:5px">메일</b><i style="display:block;font-style:normal;font-size:8.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:3px 7px;margin-bottom:3px">받은 메일</i><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:3px 7px">보낸 메일</i></div>', "안드로이드 내비게이션 드로어 재현"),
     "<b>내비게이션 드로어</b>(Navigation drawer) · 이 부품의 <b>원산지</b>입니다. Modal / Standard / Dismissible 로 나누고, 좁힌 것은 <b>내비게이션 레일</b>이라 부릅니다."),
  ]),
  plat_note="\"드로어 넣어 주세요\"는 안드로이드 개발자에게는 바로 통하지만 iOS 쪽에는 그런 부품이 없습니다. 역할(보조 내비게이션)로 말하고, iOS 에서는 <b>탭 바나 시트</b>로 어떻게 바꿀지 같이 정해야 합니다.",
  siblings=siblings("drawer"),
  related='''        <li><span class="na"><b>사이드바 내비게이션</b><em>7부</em></span></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>
        <li><span class="na"><b>포커스 트랩</b><em>12부</em></span></li>
        <li><span class="na"><b>시스템 백</b><em>11부</em></span></li>''',
)
