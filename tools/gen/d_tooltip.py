# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:16px 10px 10px;text-align:center">
                <div style="display:inline-block;position:relative">
                  <div data-pin="1" style="position:relative;background:var(--ink-900);border-radius:6px;padding:7px 26px;color:#fff;box-shadow:var(--e2)">
                    <span class="pin-out" data-pin="2" style="font-size:11.5px">되돌리기 · Ctrl+Z</span>
                  </div>
                  <span class="pin-tr" data-pin="3" style="display:block;width:0;height:0;margin:0 auto;border:6px solid transparent;border-top-color:var(--ink-900)"></span>
                </div>
                <div class="pin-tr" data-pin="4" style="height:10px;width:62px;margin:0 auto"></div>
                <div data-pin="5" style="display:inline-grid;place-items:center;width:40px;height:40px;border-radius:6px;border:1px solid var(--line-strong);background:var(--surface);font-size:15px">↺</div>
              </div>'''

D = dict(
  slug="tooltip", ko="툴팁", en="Tooltip",
  desc="툴팁이 무엇인지, 팝오버와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="툴팁은 마우스를 올린 대상 옆에 <b>짧은 설명 한 줄</b>을 띄우는 작은 상자입니다. 안에는 누를 수 있는 것이 없고, 마우스를 올려야 뜨기 때문에 손가락으로 쓰는 터치 화면에서는 <b>뜨지 않습니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>버튼에 마우스를 올리고 잠깐 기다려 보세요.</b> 마우스가 0.4초 동안 머물러야 툴팁이 뜨는데, 화면을 가로질러 지나가는 마우스에까지 툴팁이 뜨지 않도록 일부러 둔 지연입니다.
          반면 <kbd>Tab</kbd>으로 포커스를 옮기면 기다리지 않고 <b>바로</b> 뜹니다. 키보드 포커스는 우연히 지나가는 일이 없으니 지연을 둘 이유가 없기 때문입니다.</p>
        </div>
        <div class="note note--warn touch-only" style="margin-bottom:0">
          <p><b>지금 보는 기기는 호버를 지원하지 않습니다.</b> 터치 화면에는 마우스를 올려 둔 상태가 없어서 툴팁이 뜰 계기가 생기지 않습니다.
          따라서 툴팁에만 적어 둔 내용은 모바일 사용자에게 전혀 보이지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "툴팁, 말풍선, 도움말 풍선"),
    ("영어", "tooltip"),
    ("같이 쓰는 말", "툴팁이 뜨기까지 기다리는 시간은 <b>지연</b>(delay), 대상을 가리키는 뾰족한 부분은 <b>꼬리</b>(tail·arrow)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>팝오버</b> — 안에 버튼이나 링크처럼 누를 것이 들어 있으면 툴팁이 아니라 팝오버입니다. 툴팁 안에 버튼을 넣으면 마우스를 버튼 쪽으로 옮기는 사이에 툴팁이 사라지기 때문에 그 버튼은 누를 수 없습니다.<br>"
     "<b>팝업</b> — 화면 위에 뜨는 것을 모두 팝업이라고 부르면 툴팁과 팝오버, 모달을 서로 구별할 수 없게 됩니다.<br>"
     "<b>title 속성</b> — <code>title=\"…\"</code> 속성을 달면 브라우저가 <b>기본 툴팁</b>을 띄워 주지만, 지연 시간과 모양을 바꿀 수 없고 모바일에서는 뜨지 않습니다."),
  ]),
  states=states([
    (mini('<div style="margin-top:10px"><span class="mini__trigger">↺</span></div>', bars="684", label="툴팁이 없는 상태"), "평소 상태", "툴팁 없이 아이콘만 보입니다"),
    (mini('<div style="margin-top:10px"><span class="mini__trigger" style="border-color:var(--accent)">↺</span></div><div style="position:absolute;left:8px;top:40px;font-size:7.5px;color:var(--fg-muted)">0.4초 대기…</div>', bars="684", label="툴팁이 뜨기를 기다리는 중"), "뜨기를 기다리는 중", "마우스가 지나가기만 할 때는 뜨지 않도록 0.3~0.5초 기다립니다"),
    (mini('<div style="margin-top:10px"><span class="mini__trigger">↺</span></div>' + tip("되돌리기 · Ctrl+Z", "left:6px;top:12px"), bars="684", label="호버로 뜬 툴팁"), "마우스를 올려 띄웠을 때", "마우스를 치우면 바로 사라집니다"),
    (mini('<div style="margin-top:10px"><span class="mini__trigger" style="outline:2px solid var(--accent);outline-offset:1px">↺</span></div>' + tip("되돌리기 · Ctrl+Z", "left:6px;top:12px"), bars="684", label="키보드 포커스로 뜬 툴팁"), "키보드로 포커스를 옮겼을 때", "<kbd>Tab</kbd>으로 포커스가 오면 <b>바로</b> 뜹니다. 지연은 마우스에만 둡니다"),
    (mini('<div style="margin-top:10px;text-align:right"><span class="mini__trigger">⇪</span></div>' + tip("원본 올리기", "right:4px;top:12px"), bars="684", label="가장자리에서 밀린 툴팁"), "화면 가장자리에 있을 때", "화면 밖으로 나갈 것 같으면 안쪽으로 옮겨 띄웁니다"),
    (mini('<div style="margin-top:10px"><span class="mini__trigger">↺</span></div><div style="position:absolute;left:6px;top:40px;font-size:7.5px;color:var(--danger);font-weight:700">호버가 없어 뜨지 않음</div>', bars="684", label="터치 기기에서 뜨지 않는 모습"), "터치 기기에서", "호버가 없어서 <b>뜨지 않습니다.</b> 툴팁에만 적은 내용은 읽을 수 없습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("상자", "tooltip · bubble", "한두 줄에 맞춥니다. 두 줄을 넘기는 내용은 툴팁에 담기에 너무 깁니다"),
    ("글", "label", "대상의 <b>이름이나 단축키</b>를 적습니다. 설명이 길어지면 화면에 직접 적는 편이 낫습니다"),
    ("꼬리", "tail · arrow", "툴팁이 어느 대상을 설명하는지 가리킵니다"),
    ("간격", "offset", "트리거와 툴팁 사이의 거리입니다. 너무 가까우면 마우스 포인터가 툴팁 글자를 가립니다"),
    ("트리거", "trigger", "툴팁이 설명하는 대상입니다. <code>aria-describedby</code>로 트리거와 툴팁을 연결합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않지만 툴팁에서 특히 중요한 요소가 <b>지연</b>(delay)입니다. 마우스가 대상 위에 머문 시간을 재서
          0.3~0.5초가 지난 뒤에 툴팁을 띄웁니다. 이 값이 너무 짧으면 마우스가 지나갈 때마다 툴팁이 떴다 사라져 화면이 산만해집니다.
          반대로 너무 길면 사용자가 기다리지 않고 마우스를 옮겨 버려서, 툴팁이 있다는 것조차 모르고 지나가게 됩니다.</p>''',
  do=ul([
    "아이콘만 있는 버튼의 <b>이름</b>을 알려 줄 때",
    "말줄임으로 잘린 글자의 전체를 보여 줄 때",
    "비활성 버튼이 <b>왜</b> 못 눌리는지 알려 줄 때",
    "단축키처럼 알면 편하지만 몰라도 쓰는 데 지장이 없는 정보를 덧붙일 때",
  ]),
  dont=ul([
    "꼭 알아야 하는 정보를 담을 때. 모바일에서는 툴팁이 뜨지 않아서 볼 방법이 없습니다",
    "설명이 길거나 여러 줄일 때. 화면에 직접 적거나 팝오버를 씁니다",
    "안에 링크나 버튼을 넣을 때. 마우스를 옮기는 사이에 툴팁이 사라져 누를 수 없으니 팝오버를 씁니다",
    "버튼에 이미 적힌 글자를 툴팁으로 한 번 더 보여 줄 때",
  ]),
  instead='안에 누를 것이 들어가야 하면 <a href="popover.html">팝오버</a>를 쓰고, 꼭 읽혀야 하는 내용이면 화면에 직접 적거나 <a href="placeholder.html">헬퍼 텍스트</a>로 보여 줍니다. 작업 결과를 알리는 용도라면 <a href="toast.html">토스트</a>가 맞습니다.',
  cases=cases([
    (mini('<div style="margin-top:10px;display:flex;gap:4px;justify-content:center"><span class="mini__trigger">↺</span><span class="mini__trigger">↻</span><span class="mini__trigger">⇪</span></div>' + tip("되돌리기", "left:12px;top:12px"), bars="684", tall=False, label="아이콘 버튼 툴팁 재현"),
     "아이콘 버튼의 이름 알려 주기", "툴팁을 가장 흔하게 쓰는 자리입니다. 아이콘만으로는 버튼 이름을 알기 어렵기 때문입니다"),
    (mini('<div style="margin-top:10px"><span style="display:block;border:1px dashed var(--line-strong);border-radius:3px;padding:4px 6px;font-size:8px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis">2026년 4분기 결제 서버 마이그…</span></div>' + tip("2026년 4분기 결제 서버 마이그레이션", "left:2px;top:14px"), bars="684", tall=False, label="잘린 글자 툴팁 재현"),
     "잘린 글자 전체 보여 주기", "말줄임표로 잘린 글자 전체를 보여 줍니다. 글자가 실제로 잘렸을 때만 띄웁니다"),
    (mini('<div style="margin-top:10px"><span class="mini__trigger" style="opacity:.45">게시</span></div>' + tip("검수가 끝나야 눌립니다", "left:2px;top:12px"), bars="684", tall=False, label="비활성 이유 툴팁 재현"),
     "버튼이 비활성인 이유 알려 주기", "버튼을 왜 누를 수 없는지 알려 줍니다. 비활성 버튼은 포커스를 받지 못하므로 툴팁을 버튼을 감싼 요소에 겁니다"),
  ]),
  code_lede="<code>title</code> 속성을 쓰면 간단하지만 지연 시간과 모양을 바꿀 수 없고 모바일에서는 뜨지 않습니다. 그래서 툴팁을 직접 만들 때는 <code>aria-describedby</code>로 트리거와 툴팁을 연결해 스크린 리더도 설명을 읽을 수 있게 합니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-describedby</span>=<span class="s">"t1"</span>&gt;↺&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">span</span> <span class="a">id</span>=<span class="s">"t1"</span> <span class="a">role</span>=<span class="s">"tooltip"</span> <span class="a">hidden</span>&gt;되돌리기 · Ctrl+Z&lt;/<span class="t">span</span>&gt;

<span class="c">/* 툴팁은 누를 수 없게 한다. 팝오버와 구현이 갈리는 부분 */</span>
.tip <span class="a">{</span> <span class="t">pointer-events</span>: none; <span class="a">}</span>

<span class="c">// 마우스는 지연을 두고, 키보드는 바로</span>
el.addEventListener(<span class="s">'mouseenter'</span>, () =&gt; timer = setTimeout(show, <span class="a">400</span>));
btn.addEventListener(<span class="s">'focus'</span>, show);

<span class="c">// 비활성 버튼은 포커스를 못 받으니 감싼 요소에 건다</span>
&lt;<span class="t">span</span> <span class="a">tabindex</span>=<span class="s">"0"</span> <span class="a">aria-describedby</span>=<span class="s">"t5"</span>&gt;&lt;<span class="t">button</span> <span class="a">disabled</span>&gt;게시&lt;/<span class="t">button</span>&gt;&lt;/<span class="t">span</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "포커스가 오면 <b>지연 없이</b> 바로 뜹니다"),
    ("<kbd>Esc</kbd>", "툴팁을 닫습니다. 툴팁이 읽으려는 글자를 가릴 때 씁니다"),
    ("마우스를 올렸을 때", "0.3~0.5초 머물러야 뜨고, 마우스를 치우면 바로 사라집니다"),
    ("터치 화면에서", "<b>뜨지 않습니다.</b> 길게 눌러 띄우게 만들 수는 있지만, 사용자 대부분이 그 동작을 모릅니다"),
    ("스크린 리더로 읽을 때", "<code>aria-describedby</code>로 연결해 두면 버튼 이름을 읽은 뒤 툴팁 내용을 설명으로 읽어 줍니다"),
  ]),
  backend=rows([
    ("코드 주석과 같은 역할", "코드 주석이 프로그램 동작에 영향을 주지 않듯, 툴팁도 화면 동작에는 영향을 주지 않고 읽는 사람에게 정보만 줍니다. 그래서 <b>툴팁이 없어도 화면을 쓰는 데 문제가 없어야 합니다.</b> 중요한 전제 조건을 주석에만 적어 두면 놓치기 쉬운 것처럼, 지켜야 할 규칙을 툴팁에만 적어 두면 사용자가 놓칩니다."),
    ("지연은 디바운스와 같은 원리", "툴팁의 지연은 마우스가 지나가는 경우와 머무는 경우를 가르는 디바운스(debounce)입니다. 값이 너무 짧으면 툴팁이 자꾸 떠서 성가시고, 너무 길면 사용자가 툴팁이 뜨기 전에 마우스를 옮겨 버립니다."),
    ("툴팁 때문에 서버에 요청하지 않기", "툴팁을 띄우려고 서버에 요청을 보내야 한다면 대개 설계가 잘못된 것입니다. 툴팁 내용은 화면을 그릴 때 이미 받아 둔 데이터로 채울 수 있어야 합니다."),
  ]),
  plat_lede="툴팁은 <b>마우스를 쓰는 화면을 전제로 한 부품</b>이라서 모바일 디자인 지침에서는 거의 다루지 않습니다.",
  plats=plats([
    ("웹", "표준 지침 없음 · <code>title</code>",
     mini('<div style="margin-top:10px"><span class="mini__trigger">↺</span></div>' + tip("되돌리기", "left:8px;top:12px"), bars="684", label="웹 툴팁 재현"),
     "<b>툴팁</b> · <code>title</code> 속성으로도 띄울 수 있지만 지연 시간과 모양을 바꿀 수 없고 모바일에서는 뜨지 않습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;gap:4px;justify-content:center"><span style="border:1px solid var(--line-strong);border-radius:4px;padding:4px 7px;font-size:8px">↺</span><span style="border:1px solid var(--line-strong);border-radius:4px;padding:4px 7px;font-size:8px">↻</span></div><div style="position:absolute;left:8px;right:8px;bottom:18px;font-size:7.5px;color:var(--fg-muted);text-align:center">아이콘 아래에 이름을 함께 적음</div>', "iOS 에서 글자를 같이 적은 모습"),
     "<b>거의 쓰지 않습니다.</b> 터치 화면에는 호버가 없으므로 아이콘 아래에 <b>이름을 함께 적거나</b>, 길게 눌러 메뉴를 띄우는 방식을 씁니다. macOS에는 help tag라는 이름의 툴팁이 있습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:46px;text-align:center"><span style="border:1px solid var(--line-strong);border-radius:4px;padding:4px 7px;font-size:8px">↺</span></div><div style="position:absolute;left:50%;top:34px;transform:translateX(-50%);background:#2e3238;color:#fff;border-radius:3px;padding:2px 5px;font-size:7.5px">되돌리기</div>', "안드로이드 길게 눌러 뜬 툴팁 재현"),
     "<b>툴팁</b>(Tooltip) · 대상을 <b>길게 누르면</b> 뜹니다. 짧은 글만 담는 plain 툴팁과 설명이 긴 rich 툴팁, 두 가지로 나눕니다."),
  ]),
  plat_note="\"툴팁으로 설명 넣어 주세요\"라는 요청은 데스크톱 화면에서만 의미가 있습니다. 모바일에서는 그렇게 넣은 설명이 <b>아무에게도 보이지 않기</b> 때문입니다. 꼭 읽혀야 하는 내용이라면 화면에 직접 적거나, 누를 수 있는 ⓘ 버튼을 두고 누르면 팝오버로 설명을 띄우는 방식으로 바꿔야 합니다.",
  siblings=siblings("tooltip"),
  related='''        <li><a href="placeholder.html"><b>헬퍼 텍스트</b><em>14부</em></a></li>
        <li><a href="disabledstate.html"><b>비활성 · 숨김 · 읽기 전용</b><em>4부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>
        <li><a href="hover.html"><b>호버가 없는 세계</b><em>11부</em></a></li>''',
)
