# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def stage(inner, w="150px", h="76px"):
    return ('              <div style="width:100%;max-width:' + w + ';height:' + h + ';position:relative;'
            'border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">' + inner + '</div>')

def panel(top="46%", op="1", extra=""):
    return ('<div style="position:absolute;left:0;right:0;top:' + top + ';bottom:0;background:var(--surface);'
            'border-top:1px solid var(--line);border-radius:6px 6px 0 0;padding:5px 7px;opacity:' + op + ';' + extra + '">'
            '<span style="font-size:9.5px;font-weight:700">내보내기</span></div>')

DIM = '<div style="position:absolute;inset:0;background:rgba(20,22,26,.3)"></div>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">들어옴 — 260ms ease-out</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">나감 — 180ms ease-in (더 짧다)</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">나온 자리로 돌아간다 — 버튼 쪽으로</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가림막은 투명도만 — linear</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">나간 뒤에 display:none — 먼저 지우면 연출이 없다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">초점은 연출을 기다리지 않는다</div>
                </div>
              </div>'''

D = dict(
  slug="enterexit", ko="진입과 퇴장", en="Enter / Exit",
  desc="들어올 때와 나갈 때는 길이도 곡선도 달라야 합니다. 나온 자리로 돌아가기, 나간 뒤에 지우기, 초점을 옮기는 순서를 보여 주는 항목입니다.",
  lede="진입과 퇴장은 요소가 들어올 때와 나갈 때의 움직임을 <b>따로</b> 정하는 일입니다. 두 값을 같게 맞추면 닫을 때마다 사용자가 <b>필요 없이 더 기다리게 됩니다</b>.",
  axes_lede="움직임은 화면에서 무엇이 바뀌었는지 사용자에게 <b>알려 주는</b> 역할을 합니다. 아래 네 가지를 따져 보면 움직임을 다루는 항목들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>열고 닫기를 되풀이해 보세요. 기본값은 <b>들어올 때 260ms ease-out</b>,
          <b>나갈 때 180ms ease-in</b>입니다.<br>
          <b>같게 맞추기</b>를 켜면 닫을 때도 260ms가 걸립니다. 이미 다 본 패널이 사라지기를
          기다리는 것이 어떤 느낌인지 바로 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "진입과 퇴장, 들고 남, 등장과 사라짐"),
    ("영어", "enter / exit, entrance / exit transition, in / out"),
    ("같이 쓰는 말",
     "리액트 쪽에서는 <code>enter</code>·<code>enter-active</code>·<code>exit</code> 같은 클래스 이름으로 나타나고, "
     "Vue에서는 <code>v-enter-from</code>·<code>v-leave-to</code>를 씁니다. "
     "요즘 CSS에서는 <code>@starting-style</code>과 <code>transition-behavior: allow-discrete</code>를 쓰면 "
     "<b>자바스크립트 없이</b>도 들어오고 나가는 움직임을 만들 수 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>트랜지션</b> — CSS <code>transition</code>은 움직임을 구현하는 수단이고, 진입과 퇴장은 그 움직임을 어떻게 줄지 정하는 <b>설계</b>입니다.<br>"
     "<b>페이드</b> — 투명도를 바꾸는 것은 여러 방법 가운데 하나일 뿐이고, 보통은 자리와 크기도 함께 움직입니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 부품 이름이고, 진입과 퇴장은 그 부품이 <b>어떻게 들어오고 나가는지</b>를 가리킵니다."),
  ]),
  axes=ax("진입과 퇴장"),
  oneline="<b>나가는 움직임을 더 짧게</b> 줍니다. 들어오는 것은 어디서 왔는지 보여 줘야 하지만, 나가는 것은 사용자가 이미 다 본 것이기 때문입니다.",
  s4_title="들고 나는 네 토막", s4_hint="같은 부품, 다른 시간",
  states=states([
    (stage(panel("100%", "0")), "닫힘", "화면 아래에 숨어 있습니다. <code>display:none</code>은 <b>아직</b> 걸지 않습니다"),
    (stage(DIM + panel("72%", ".6")), "들어오는 중", "<b>260ms ease-out</b>으로 빠르게 출발해 천천히 멈춥니다"),
    (stage(DIM + panel("46%", "1")), "열림", "제자리에 멈췄습니다. 초점은 <b>이미</b> 패널 안으로 옮겨져 있습니다"),
    (stage(DIM + panel("78%", ".5")), "나가는 중", "<b>180ms ease-in</b>으로 들어올 때보다 짧게 나갑니다"),
    (stage(panel("100%", "0")), "나간 뒤", "이때 <code>display:none</code>을 겁니다. <b>먼저 지우면</b> 나가는 연출이 보이지 않습니다"),
    (stage('<span style="position:absolute;left:8px;top:8px;font-size:9px;color:var(--fg-muted)">모션 줄이기</span>' + panel("46%", "1")),
     "줄이기에서", "<b>자리 이동 없이</b> 그냥 나타나고 사라집니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("들어오는 길이", "260ms ease-out", "요소가 <b>어디서 왔는지</b> 보여 줄 시간입니다"),
    ("나가는 길이", "180ms ease-in", "들어올 때보다 <b>더 짧게</b> 줍니다. 이미 다 본 것이 사라지기를 기다리게 하지 않기 위해서입니다"),
    ("돌아갈 자리", "나온 쪽", "누른 버튼 쪽으로 돌아가면 패널이 <b>어디로 갔는지</b> 알 수 있습니다"),
    ("가림막", "투명도만", "자리는 움직이지 않고 투명도만 바뀌므로 <code>linear</code>로 충분합니다"),
    ("지우는 때", "연출 뒤", "<code>transitionend</code>나 <code>setTimeout</code>으로 연출이 끝난 때를 잡아 지웁니다. <b>먼저 지우면 연출이 보이지 않습니다</b>"),
    ("초점", "기다리지 않는다", "열릴 때는 바로 패널 안으로, 닫힐 때는 바로 패널을 연 버튼으로 옮깁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>초점은 연출이 끝나기를 기다리지 않고 옮깁니다.</b>
          '애니메이션이 끝나면 초점을 옮기자'로 짜면 키보드 사용자는 그동안
          아무 데도 갈 수 없고, <kbd>Tab</kbd>을 눌러도 초점이 배경으로 빠집니다.
          그래서 <b>자리는 천천히 옮기고 초점은 바로 옮기는</b> 것이 맞습니다.
          <a href="../items/focustrap.html">포커스 트랩</a>도 같은 이유로 열자마자 걸어 둡니다.</p>''',
  do=ul([
    "모달·시트·토스트·드롭다운처럼 <b>떴다 사라지는 것</b>을 만들 때",
    "목록에서 <b>줄이 지워질</b> 때. 그냥 사라지면 무엇이 지워졌는지 알 수 없습니다",
    "화면이 통째로 바뀔 때",
  ]),
  dont=ul([
    "들어오는 움직임과 나가는 움직임을 <b>같게</b> 맞출 때. 닫을 때마다 필요 없이 기다리게 됩니다",
    "나가는 연출이 끝나기를 기다렸다가 <b>초점을 옮길</b> 때",
    "<code>display:none</code>을 먼저 걸 때. <b>나가는 연출이 통째로 보이지 않습니다</b>",
    "<b>들어올 때만</b> 움직임을 만들고 나갈 때는 툭 사라지게 둘 때. 진입과 퇴장 가운데 절반만 만든 것입니다",
  ]),
  instead='곡선 자체는 <a href="easing.html">이징</a>, 길이는 <a href="duration.html">지속 시간</a>, 여러 줄이 차례로 들어오게 하려면 <a href="stagger.html">차례로 들어오기</a>.',
  cases=cases([
    (stage(DIM + panel("46%"), "150px"), "아래에서 올라옴", "<a href=\"../items/sheet.html\">바텀시트</a>입니다. 닫을 때는 나온 쪽으로 돌아갑니다"),
    (stage('<div style="position:absolute;left:14%;right:14%;top:22%;bottom:30%;background:var(--surface);border:1px solid var(--line);border-radius:6px;box-shadow:var(--e2)"></div>', "150px"),
     "가운데서 커짐", "<a href=\"../items/modal.html\">모달</a>입니다. 크기는 <b>0.96에서 1</b> 정도로만 키웁니다. 많이 키우면 화면 앞으로 튀어나오는 것처럼 보여 부담스럽습니다"),
    (stage('<div style="position:absolute;left:8px;right:8px;top:8px;background:var(--fg);color:var(--surface);border-radius:5px;padding:4px 6px;font-size:9px">저장했습니다</div>', "150px"),
     "위에서 미끄러져 들어옴", "<a href=\"../items/toast.html\">토스트</a>입니다. 사용자가 닫지 않아도 저절로 나가기 때문에 <b>퇴장이 더 중요</b>합니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="들어온 상태와 나간 상태를 따로 적고, 요소는 <b>다 나간 뒤에</b> 지웁니다.",
  code='''.sheet {                      <span class="c">/* 나갈 때 */</span>
  <span class="a">transition</span>: transform <span class="a">180ms</span> <span class="a">var</span>(--ease-in), opacity <span class="a">140ms</span> linear;
  <span class="a">transform</span>: translateY(<span class="a">100%</span>); <span class="a">opacity</span>: <span class="a">0</span>;
}
.sheet[data-open] {           <span class="c">/* 들어올 때 */</span>
  <span class="a">transition</span>: transform <span class="a">260ms</span> <span class="a">var</span>(--ease-out), opacity <span class="a">180ms</span> linear;
  <span class="a">transform</span>: none; <span class="a">opacity</span>: <span class="a">1</span>;
}

<span class="c">// 초점은 기다리지 않는다</span>
sheet.dataset.open = <span class="s">''</span>; firstField.focus();

<span class="c">// 지우는 것은 연출이 끝난 뒤</span>
<span class="k">function</span> close() {
  opener.focus();                        <span class="c">// 먼저</span>
  <span class="k">delete</span> sheet.dataset.open;
  sheet.addEventListener(<span class="s">'transitionend'</span>, () =&gt; { sheet.hidden = <span class="k">true</span>; }, { once: <span class="k">true</span> });
}''',
  keys=kbd([
    ("초점을 먼저 옮긴다", "열 때는 패널 안으로, 닫을 때는 <b>패널을 연 버튼</b>으로 옮깁니다. 연출이 끝나기를 기다리지 않습니다"),
    ("<code>transitionend</code>는 안 올 수 있다", "값이 바뀌지 않았거나 길이가 0이면 이벤트가 오지 않습니다. 그래서 <code>setTimeout</code>을 예비로 같이 걸어 둡니다"),
    ("<code>@starting-style</code>", "요즘 CSS에 들어온 규칙입니다. <code>display:none</code>이던 요소가 나타나는 움직임도 자바스크립트 없이 만들 수 있습니다"),
    ("<code>&lt;dialog&gt;.close()</code>", "부르면 바로 사라집니다. 퇴장 연출을 보여 주려면 연출이 <b>끝난 뒤</b>에 부릅니다"),
    ("<kbd>Esc</kbd>", "닫는 연출 중에도 동작해야 합니다. 연출 중에는 입력을 막고 싶어지지만, <b>막으면 사용자가 그 화면에서 빠져나갈 수 없습니다</b>"),
    ("<code>aria-hidden</code>", "나가는 중에도 켜 둡니다. 화면에는 <b>보이지만 스크린 리더가 읽지 않는</b> 구간이 잠깐 생기는 편이 낫습니다"),
  ]),
  backend=rows([
    ("닫히는 중에 다시 열리면", "닫는 연출이 끝날 때 <code>hidden</code>을 거는 타이머가 남아 있으면 <b>새로 연 패널</b>까지 숨겨 버립니다. 그래서 열 때 그 타이머를 <b>취소</b>합니다."),
    ("저장하고 닫는 순서", "저장하고 응답을 받은 뒤에 닫으면 느립니다. 보통은 <a href=\"../items/optimistic.html\">낙관적 UI</a>로 <b>먼저 닫고</b>, 저장에 실패하면 되돌리는 편이 낫습니다."),
    ("닫힘을 서버가 모른다", "사용자가 연출 도중에 페이지를 떠나면 요청이 끊깁니다. 그래서 중요한 저장은 <code>keepalive</code>나 <code>sendBeacon</code>으로 보냅니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>나가는 움직임을 더 짧게</b> 두고, 부르는 이름만 다릅니다.",
  plats=plats([
    ("웹", "transition · @starting-style",
     stage(DIM + panel("46%"), "105px", "62px"),
     "두 상태를 적어 두고 클래스로 오갑니다. 웹에서는 요소를 <b>지우는 때</b>를 개발자가 직접 챙겨야 합니다."),
    ("iOS", "present / dismiss",
     '''              <div class="phone" role="img" aria-label="iOS 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:rgba(20,22,26,.3)"></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:52%;background:var(--surface);border-radius:8px 8px 0 0"></div></div></div>''',
     "<code>present</code>와 <code>dismiss</code>를 짝으로 씁니다. 시트에는 <b>끌어서 닫기</b>가 기본으로 들어 있습니다."),
    ("안드로이드", "Material motion",
     '''              <div class="phone" role="img" aria-label="Material 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;bottom:14px;background:var(--surface);border-radius:6px;box-shadow:var(--e2)"></div></div></div>''',
     "규격에 <b>enter는 길게, exit는 짧게</b> 하라고 정해 두었습니다. 공유 축 전환(shared axis)도 표준으로 들어 있습니다."),
  ]),
  plat_note="\"모달 띄울 때 스르륵\"이라는 요청에는 <b>닫는 움직임</b>이 빠져 있기 쉽습니다. 들어오는 움직임만 만들면 닫을 때 툭 사라져서 절반만 만든 것처럼 보이고, 둘을 같은 값으로 맞추면 닫을 때마다 필요 없이 기다리게 됩니다. 처음부터 <b>들어옴 260 · 나감 180</b>을 기본값으로 적어 두면 이런 요청을 주고받는 일이 줄어듭니다.",
  siblings=siblings("enterexit"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>''',
)
