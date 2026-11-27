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
  desc="들어올 때와 나갈 때는 길이도 곡선도 달라야 한다. 나온 자리로 돌아가기, 나간 뒤 지우기, 초점 순서.",
  lede="들어올 때와 나갈 때를 <b>따로</b> 정하는 일. 같게 맞추면 닫을 때마다 <b>한 박자 붙잡힙니다</b>.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>열고 닫기를 되풀이해 보세요. 기본값은 <b>들어올 때 260ms ease-out</b>,
          <b>나갈 때 180ms ease-in</b>입니다.<br>
          <b>같게 맞추기</b>를 켜면 닫는 데도 260ms 가 걸립니다 — 볼 일이 끝난 것을
          기다리는 느낌이 어떤지 바로 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "진입과 퇴장, 들고 남, 등장과 사라짐"),
    ("영어", "enter / exit, entrance / exit transition, in / out"),
    ("같이 쓰는 말",
     "리액트 쪽에서는 <code>enter</code>·<code>enter-active</code>·<code>exit</code> 같은 클래스 이름으로 나타납니다. "
     "Vue 는 <code>v-enter-from</code>·<code>v-leave-to</code>입니다. "
     "요즘 CSS 는 <code>@starting-style</code>과 <code>transition-behavior: allow-discrete</code>로 "
     "<b>자바스크립트 없이</b>도 들고 남을 그릴 수 있습니다."),
    ("자주 잘못 부름",
     "<b>트랜지션</b> — CSS <code>transition</code>은 수단이고, 진입·퇴장은 <b>설계</b>입니다.<br>"
     "<b>페이드</b> — 투명도는 여러 방법 중 하나입니다. 자리·크기도 함께 움직입니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 부품, 이쪽은 그 부품이 <b>어떻게 들고 나는지</b>입니다."),
  ]),
  axes=ax("진입과 퇴장"),
  oneline="<b>나가는 쪽을 더 짧게.</b> 들어오는 것은 어디서 왔는지 보여 줘야 하지만, 나가는 것은 이미 볼 일이 끝났습니다.",
  s4_title="들고 나는 네 토막", s4_hint="같은 부품, 다른 시간",
  states=states([
    (stage(panel("100%", "0")), "닫힘", "아래에 숨어 있다. <code>display:none</code>은 <b>아직</b>"),
    (stage(DIM + panel("72%", ".6")), "들어오는 중", "<b>260ms ease-out</b> — 빨리 떠나 천천히 멎는다"),
    (stage(DIM + panel("46%", "1")), "열림", "자리 잡음. 초점은 <b>이미</b> 안으로 옮겨져 있다"),
    (stage(DIM + panel("78%", ".5")), "나가는 중", "<b>180ms ease-in</b> — 더 짧다"),
    (stage(panel("100%", "0")), "나간 뒤", "그제야 <code>display:none</code>. <b>먼저 지우면</b> 연출이 없다"),
    (stage('<span style="position:absolute;left:8px;top:8px;font-size:9px;color:var(--fg-muted)">모션 줄이기</span>' + panel("46%", "1")),
     "줄이기에서", "<b>자리 이동 없이</b> 그냥 나타나고 사라진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("들어오는 길이", "260ms ease-out", "<b>어디서 왔는지</b>를 보여 줄 시간"),
    ("나가는 길이", "180ms ease-in", "<b>더 짧게.</b> 볼 일이 끝난 것을 기다리게 하지 않는다"),
    ("돌아갈 자리", "나온 쪽", "누른 버튼 쪽으로 돌아가면 <b>어디로 갔는지</b> 알 수 있다"),
    ("가림막", "투명도만", "자리는 안 움직인다. <code>linear</code>로 충분하다"),
    ("지우는 때", "연출 뒤", "<code>transitionend</code>나 <code>setTimeout</code>. <b>먼저 지우면 안 보인다</b>"),
    ("초점", "기다리지 않는다", "열릴 때는 바로 안으로, 닫힐 때는 바로 부른 버튼으로"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>초점은 연출을 기다리지 않습니다.</b>
          '애니메이션이 끝나면 초점을 옮기자'로 짜면 키보드 사용자는 그 시간 동안
          아무 데도 못 갑니다 — <kbd>Tab</kbd> 을 눌러도 배경으로 빠집니다.
          <b>자리는 천천히, 초점은 즉시</b>가 맞습니다.
          <a href="../items/focustrap.html">포커스 트랩</a>도 같은 이유로 열자마자 걸어 둡니다.</p>''',
  do=ul([
    "<b>떴다 사라지는 모든 것</b> — 모달·시트·토스트·드롭다운",
    "목록에서 <b>줄이 지워질</b> 때 — 그냥 사라지면 뭐가 지워졌는지 모른다",
    "화면이 통째로 바뀔 때",
  ]),
  dont=ul([
    "들어오는 것과 나가는 것을 <b>같게</b> — 닫을 때 붙잡힌다",
    "나가는 연출이 끝나기를 기다렸다 <b>초점 옮기기</b>",
    "<code>display:none</code>을 먼저 걸기 — <b>연출이 통째로 안 보인다</b>",
    "<b>들어올 때만</b> 만들고 나갈 때는 툭 사라지게 두기 — 절반만 한 것이다",
  ]),
  instead='곡선 자체는 <a href="easing.html">이징</a>, 길이는 <a href="duration.html">지속 시간</a>, 여러 줄이 차례로면 <a href="stagger.html">차례로 들어오기</a>.',
  cases=cases([
    (stage(DIM + panel("46%"), "150px"), "아래에서 올라옴", "<a href=\"../items/sheet.html\">바텀시트</a>. 나온 쪽으로 돌아간다"),
    (stage('<div style="position:absolute;left:14%;right:14%;top:22%;bottom:30%;background:var(--surface);border:1px solid var(--line);border-radius:6px;box-shadow:var(--e2)"></div>', "150px"),
     "가운데서 커짐", "<a href=\"../items/modal.html\">모달</a>. <b>0.96 → 1</b> 정도만. 크게 키우면 덮쳐 온다"),
    (stage('<div style="position:absolute;left:8px;right:8px;top:8px;background:var(--fg);color:var(--surface);border-radius:5px;padding:4px 6px;font-size:9px">저장했습니다</div>', "150px"),
     "위에서 미끄러져 들어옴", "<a href=\"../items/toast.html\">토스트</a>. 저절로 나가므로 <b>퇴장이 더 중요</b>하다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 전환의 계약서",
  code_lede="두 상태를 따로 적고, <b>나간 뒤에</b> 지웁니다.",
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
    ("초점을 먼저 옮긴다", "열 때는 안으로, 닫을 때는 <b>부른 버튼</b>으로. 연출을 기다리지 않는다"),
    ("<code>transitionend</code>는 안 올 수 있다", "값이 안 바뀌거나 길이가 0 이면 안 온다. <code>setTimeout</code> 보험을 같이 건다"),
    ("<code>@starting-style</code>", "요즘 CSS. <code>display:none</code>에서 나타나는 것도 자바스크립트 없이 그릴 수 있다"),
    ("<code>&lt;dialog&gt;.close()</code>", "바로 사라진다. 퇴장 연출을 보려면 <b>끝난 뒤</b>에 부른다"),
    ("<kbd>Esc</kbd>", "닫는 연출 중에도 먹어야 한다. 연출 중엔 잠그고 싶겠지만 <b>잠그면 갇힌다</b>"),
    ("<code>aria-hidden</code>", "나가는 중에도 켜 둔다. <b>보이지만 읽히지 않는</b> 구간이 짧게 있는 편이 낫다"),
  ]),
  backend=rows([
    ("닫히는 중에 다시 열리면", "연출이 끝나며 <code>hidden</code>을 거는 타이머가 <b>새로 연 것</b>까지 숨깁니다. 열 때 타이머를 <b>취소</b>합니다."),
    ("저장하고 닫는 순서", "'저장 → 응답 → 닫기'면 느립니다. <a href=\"../items/optimistic.html\">낙관적 UI</a>로 <b>먼저 닫고</b> 실패하면 되돌리는 쪽이 보통 낫습니다."),
    ("닫힘을 서버가 모른다", "사용자가 연출 도중 떠나면 요청이 끊깁니다. 중요한 저장은 <code>keepalive</code>나 <code>sendBeacon</code>으로 보냅니다."),
  ]),
  plat_lede="세 곳 모두 <b>나가는 쪽이 더 짧습니다.</b> 이름만 다릅니다.",
  plats=plats([
    ("웹", "transition · @starting-style",
     stage(DIM + panel("46%"), "105px", "62px"),
     "상태를 둘 적고 클래스로 오갑니다. <b>지우는 때</b>를 직접 챙겨야 하는 것이 웹의 숙제입니다."),
    ("iOS", "present / dismiss",
     '''              <div class="phone" role="img" aria-label="iOS 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:rgba(20,22,26,.3)"></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:52%;background:var(--surface);border-radius:8px 8px 0 0"></div></div></div>''',
     "<code>present</code>·<code>dismiss</code>가 짝입니다. 시트는 <b>끌어서 닫기</b>가 기본으로 붙습니다."),
    ("안드로이드", "Material motion",
     '''              <div class="phone" role="img" aria-label="Material 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;bottom:14px;background:var(--surface);border-radius:6px;box-shadow:var(--e2)"></div></div></div>''',
     "<b>enter 는 길게, exit 는 짧게</b>를 규격에 못 박았습니다. 공유 축 전환(shared axis)도 표준으로 있습니다."),
  ]),
  plat_note="\"모달 띄울 때 스르륵\"이라는 요청에는 <b>닫는 쪽</b>이 빠져 있기 쉽습니다. 들어오는 것만 만들면 닫을 때 툭 사라져 절반만 한 모양이 되고, 둘을 같은 값으로 맞추면 닫을 때마다 붙잡힙니다. <b>들어옴 260 · 나감 180</b>을 기본으로 적어 두면 이 대화가 짧아집니다.",
  siblings=siblings("enterexit"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>''',
)
