# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sheetbox(top, note="", w="150px", h="76px", warn=False):
    col = "var(--danger)" if warn else "var(--fg-muted)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<div style="height:' + h + ';position:relative;border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">'
            '<div style="position:absolute;left:0;right:0;top:' + top + ';bottom:-8px;background:var(--surface);'
            'border-top:1px solid var(--line);border-radius:7px 7px 0 0;padding:4px">'
            '<span style="display:block;width:22px;height:3px;border-radius:2px;background:var(--line-strong);margin:0 auto"></span></div></div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + col + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">pointerdown — 잡는다 (setPointerCapture)</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + sheetbox("40%", "", "220px", "64px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">끄는 동안 손가락을 그대로 따라간다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">문턱 — 절반을 넘겼나</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">속도 — 빠르게 튕겼나 (0.5px/ms)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">touch-action 을 안 적으면 브라우저가 먼저 가져간다</div>
                </div>
              </div>'''

D = dict(
  slug="gesture", ko="제스처", en="Gesture",
  desc="끌고 놓는 조작을 다루는 항목입니다. 손가락을 따라가기, 거리와 속도로 판단하기, 되돌릴 방법 남기기를 보여 줍니다.",
  lede="제스처는 손가락을 <b>따라가는</b> 움직임입니다. 보여 주기 위한 연출이 아니라 사용자가 직접 하는 <b>조작</b>이어서 지켜야 할 규칙이 더 엄격합니다.",
  axes_lede="움직임은 화면에서 무엇이 바뀌었는지 사용자에게 <b>알려 주는</b> 역할을 합니다. 아래 네 가지를 따져 보면 움직임을 다루는 항목들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>시트를 아래로 끌어 보세요. 조금 끌었다 놓으면 <b>제자리로</b> 돌아오고, 절반을 넘기거나
          <b>빠르게 튕기면</b> 닫힙니다.<br>
          <b>속도도 본다</b>를 끄면 짧게 탁 튕겨 닫는 동작이 듣지 않습니다.
          <b>손가락을 따라간다</b>를 끄면 규칙은 같은데도 <b>내가 조작하고 있다는 느낌</b>이 사라지는데,
          이것으로 제스처에서 따라가기가 왜 중요한지 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "제스처, 끌기, 쓸어넘기기, 당겨서 새로고침"),
    ("영어", "gesture, drag, swipe, pan, fling, pull-to-refresh"),
    ("같이 쓰는 말",
     "천천히 끄는 것을 <b>팬</b>·<b>드래그</b>, 빠르게 튕기는 것을 <b>스와이프</b>·<b>플링</b>이라고 합니다. "
     "닫을지 말지 판단하는 기준 거리는 <b>스레시홀드</b>(threshold), 손을 놓은 뒤에도 미끄러지듯 이어지는 움직임은 <b>관성</b>(momentum)이라고 부릅니다. "
     "손을 뗐을 때 가까운 자리에 맞춰 멈추는 것은 <b>스냅</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>애니메이션</b> — 제스처는 애니메이션이 아니라 <b>입력</b>입니다. 애니메이션은 손을 뗀 뒤에만 나옵니다.<br>"
     "<b>스크롤</b> — 제스처가 브라우저 기본 스크롤과 <b>같은 입력을 두고 겹치면</b> 제스처와 스크롤이 모두 제대로 동작하지 않습니다.<br>"
     "<b>터치 이벤트</b> — <code>touchstart</code>는 손가락 입력만 받지만, <b>포인터 이벤트</b>는 마우스·펜·손가락을 한 코드로 받습니다."),
  ]),
  axes=ax("제스처"),
  oneline="<b>끄는 동안 손가락을 따라가지 않으면 제스처라고 할 수 없습니다.</b> 또 끈 거리만 보고 판단하면 끝까지 끌어야만 닫히는 조작이 되므로 <b>속도도</b> 함께 봅니다.",
  s4_title="끄는 네 토막", s4_hint="손을 떼기 전과 뒤",
  states=states([
    (sheetbox("28%", "잡기 전 — 제자리"), "쉬는 중", "손잡이(그립)가 <b>끌 수 있다</b>는 것을 알려 줍니다"),
    (sheetbox("44%", "끄는 중 — 손가락을 따라간다"), "끄는 중", "손가락을 <b>1:1로 따라갑니다.</b> 제스처에서 가장 중요한 부분입니다"),
    (sheetbox("34%", "조금 끌고 놓음 → 제자리"), "문턱 못 넘음", "<b>제자리로 돌아옵니다.</b> 사용자가 마음을 바꿀 수 있도록 되돌릴 방법이 늘 있어야 합니다"),
    (sheetbox("72%", "절반 넘김 → 닫힘"), "문턱 넘음", "끈 거리로 판단합니다. 흔히 <b>절반</b>을 기준으로 씁니다"),
    (sheetbox("40%", "빠르게 튕김 → 닫힘"), "빠르게 튕김", "끈 거리가 짧아도 <b>속도가 빠르면</b> 닫습니다"),
    (sheetbox("28%", "끝까지 끌어야만 닫힌다", "150px", "76px", True), "속도를 안 볼 때", "짧게 튕겨도 닫히지 않아서 <b>답답합니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잡기", "pointerdown", "<code>setPointerCapture</code>를 걸면 손가락이 요소 <b>밖으로 나가도</b> 이벤트를 계속 받습니다"),
    ("따라가기", "1:1", "끄는 동안 손가락과 똑같이 움직입니다. <b>따라가지 않으면 사용자는 조작하고 있다고 느끼지 못합니다</b>"),
    ("놓기", "pointerup", "손을 놓은 이 시점에 <b>처음으로</b> 애니메이션이 나옵니다"),
    ("문턱", "절반", "끈 거리로 판단합니다. 문턱이 너무 작으면 <b>실수로 닫힙니다</b>"),
    ("속도", "0.5px/ms", "짧게 튕겨도 닫히게 합니다. <b>거리만 보면 답답</b>합니다"),
    ("브라우저와의 자리 다툼", "touch-action", "이 속성을 적지 않으면 <b>브라우저 스크롤이 먼저</b> 입력을 가져갑니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>제스처는 화면에 보이지 않습니다.</b> 예를 들어 쓸어넘겨 지우기는 화면 어디에도 표시가 없고,
          마우스나 키보드로는 할 수 없습니다.
          그래서 제스처로 할 수 있는 일은 <b>반드시 버튼으로도</b> 할 수 있어야 합니다.
          시트에는 닫기 버튼과 <kbd>Esc</kbd>를, 쓸어넘겨 지우기에는 메뉴 안의 '삭제'를 함께 둡니다.
          제스처는 자주 하는 일을 <b>빨리 하는 방법</b>일 뿐, 그 일을 하는 유일한 방법이 되어서는 안 됩니다.</p>''',
  do=ul([
    "시트, 카드 넘기기, 당겨서 새로고침처럼 <b>손으로 다루는 느낌</b>이 필요할 때",
    "자주 하는 동작을 <b>빨리 하는 방법</b>을 줄 때",
    "폰에서 <b>엄지가 닿기 어려운</b> 버튼을 대신할 때",
  ]),
  dont=ul([
    "제스처로<b>만</b> 할 수 있는 일을 만들 때. 같은 일을 하는 버튼도 함께 둡니다",
    "되돌릴 수 없는 일을 한 번 쓸어서 처리할 때. <b>실수로 지워집니다</b>",
    "브라우저 스크롤과 <b>같은 방향</b>으로 끄는 제스처를 만들 때",
    "PC에서 끌어야만 할 수 있는 일을 만들 때. <b>마우스로 끌기는 불편</b>합니다",
  ]),
  instead='손을 놓은 뒤의 움직임은 <a href="spring.html">스프링</a>, 들어오고 나가는 움직임의 짝은 <a href="enterexit.html">진입과 퇴장</a>, 같은 일을 버튼으로 하는 방법은 <a href="../items/sheet.html">바텀시트</a>·<a href="../items/dialog.html">다이얼로그</a>.',
  cases=cases([
    (sheetbox("44%", "", "150px"), "끌어 닫는 시트", "가장 흔한 제스처입니다. <b>손잡이</b>가 끌 수 있다는 것을 알려 줍니다"),
    ('''              <div style="width:100%;max-width:150px;position:relative;height:40px;border:1px solid var(--line);border-radius:6px;overflow:hidden;background:var(--danger)">
                <div style="position:absolute;inset:0 32% 0 0;background:var(--surface);display:flex;align-items:center;padding:0 7px;font-size:9.5px">모란상회</div>
                <span style="position:absolute;right:8px;top:12px;font-size:9px;color:#fff">삭제</span>
              </div>''',
     "쓸어넘겨 지우기", "<b>되돌리기</b>를 함께 제공해야 쓸 수 있습니다"),
    ('''              <div style="width:100%;max-width:150px;height:56px;position:relative;border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">
                <span style="position:absolute;left:50%;top:8px;transform:translateX(-50%);width:16px;height:16px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--accent)"></span>
                <div style="position:absolute;left:0;right:0;top:30px;bottom:0;background:var(--surface);border-top:1px solid var(--line)"></div>
              </div>''',
     "당겨서 새로고침", "<b>당긴 만큼</b> 표시가 커집니다. 손가락을 따라가지 않으면 사용자는 동작하는지 알 수 없습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="포인터 이벤트 하나로 마우스·펜·손가락 입력을 모두 받고, <code>touch-action</code>을 반드시 적습니다.",
  code='''.sheet { <span class="a">touch-action</span>: none; }   <span class="c">/* 브라우저 스크롤에 안 뺏긴다 */</span>

sheet.addEventListener(<span class="s">'pointerdown'</span>, e =&gt; {
  sheet.setPointerCapture(e.pointerId);      <span class="c">// 밖으로 나가도 계속 받는다</span>
  start = e.clientY - y; lastY = e.clientY; lastT = performance.now();
});

sheet.addEventListener(<span class="s">'pointermove'</span>, e =&gt; {
  <span class="k">const</span> dt = performance.now() - lastT;
  v = (e.clientY - lastY) / Math.max(dt, <span class="a">1</span>);   <span class="c">// px/ms</span>
  lastY = e.clientY; lastT = performance.now();
  move(e.clientY - start);                   <span class="c">// 1:1 로 따라간다</span>
});

sheet.addEventListener(<span class="s">'pointerup'</span>, () =&gt; {
  (y &gt; H / <span class="a">2</span> || v &gt; <span class="a">0.5</span>) ? close() : snapBack();   <span class="c">// 거리 또는 속도</span>
});''',
  keys=kbd([
    ("<code>touch-action</code>", "<code>none</code>이나 <code>pan-y</code>를 적습니다. 적지 않으면 <b>브라우저가 먼저</b> 입력을 가져갑니다"),
    ("<code>setPointerCapture</code>", "손가락이 상자 밖으로 나가도 이벤트가 계속 옵니다. <b>걸지 않으면 중간에 끊깁니다</b>"),
    ("<code>pointercancel</code>", "전화가 오거나 브라우저가 입력을 가로채면 이 이벤트가 옵니다. 이때는 <b>제자리로 되돌려야</b> 합니다"),
    ("키보드 길을 반드시", "<kbd>Esc</kbd>로 닫기와 <b>닫기 버튼</b>을 둡니다. 제스처는 키보드로 대신할 수 없습니다"),
    ("<code>user-select: none</code>", "끄는 동안 글자가 선택되어 파랗게 칠해지는 것을 막습니다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>", "따라가기는 <b>그대로 둡니다</b>. 사용자의 손가락이 만든 움직임이라 멀미를 일으키지 않기 때문입니다"),
  ]),
  backend=rows([
    ("쓸어서 지우기는 되돌릴 수 있어야", "실수가 잦은 조작이라 <b>바로 지우지 않고</b> 되돌릴 시간을 둡니다. 보통 5초쯤 기다렸다가 실제 삭제 요청을 보냅니다."),
    ("당겨서 새로고침이 연타된다", "몇 번을 당겨도 요청은 <b>하나만</b> 나가게 막습니다. 그러지 않으면 같은 요청이 여러 번 연달아 갑니다."),
    ("끄는 중에는 요청하지 않는다", "손을 떼기 전까지는 <b>아무것도 확정되지 않았기</b> 때문에, 끄는 도중의 값으로 서버에 요청하지 않습니다."),
    ("끊긴 제스처", "앱이 배경으로 가면 <code>pointercancel</code>만 오고 <code>pointerup</code>은 오지 않습니다. 그래서 제스처가 끊겼을 때는 <b>되돌리는 쪽</b>을 기본으로 둡니다."),
  ]),
  plat_lede="폰에서는 제스처가 기본 조작이지만, <b>PC에서는 보조 수단</b>입니다.",
  plats=plats([
    ("웹", "Pointer Events",
     sheetbox("44%", "", "105px", "60px"),
     "마우스·펜·손가락 입력을 한 코드로 받습니다. 구현할 때는 <b>브라우저 기본 동작과 입력이 겹치지 않게</b> 하는 일이 가장 큽니다."),
    ("iOS", "UIGestureRecognizer",
     '''              <div class="phone" role="img" aria-label="iOS 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"><span style="display:block;width:14px;height:2px;background:var(--line-strong);margin:4px auto;border-radius:2px"></span></div></div></div>''',
     "제스처마다 전용 인식기가 있고, 인식기끼리 <b>어느 쪽이 먼저 입력을 받을지</b> 정하는 규칙까지 있습니다. 화면 가장자리에서 쓸면 뒤로 갑니다."),
    ("안드로이드", "GestureDetector",
     '''              <div class="phone" role="img" aria-label="안드로이드 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"><span style="display:block;width:14px;height:2px;background:var(--line-strong);margin:4px auto;border-radius:2px"></span></div></div></div>''',
     "<b>양쪽 가장자리</b>에서 쓸면 모두 뒤로 가기 때문에, 가장자리에서 끄는 제스처를 만들면 시스템 뒤로가기와 겹칩니다."),
  ]),
  plat_note="\"카톡처럼 쓸어서 답장\" 같은 요청은 제스처 자체를 만드는 일보다 <b>함께 챙겨야 할 일이</b> 더 많습니다. 되돌리기, 키보드로 하는 방법, 스크롤과 입력이 겹치는 문제, 가장자리 뒤로가기와의 충돌까지 모두 처리해야 합니다. 제스처를 넣기로 했다면 <b>같은 일을 하는 버튼</b>을 먼저 만들고 그 위에 제스처를 더하는 순서가 안전합니다.",
  siblings=siblings("gesture"),
  related='''        <li><a href="spring.html"><b>스프링</b><em>9부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>''',
)
