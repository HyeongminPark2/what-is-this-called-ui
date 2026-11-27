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
  desc="끌고 놓는 조작. 손가락을 따라가기, 거리와 속도로 판단하기, 되돌릴 길 남기기.",
  lede="손가락을 <b>따라가는</b> 움직임. 연출이 아니라 <b>조작</b>이라 규칙이 더 엄격합니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>시트를 아래로 끌어 보세요. 조금 끌었다 놓으면 <b>제자리로</b>, 절반을 넘기거나
          <b>빠르게 튕기면</b> 닫힙니다.<br>
          <b>속도도 본다</b>를 끄면 짧게 탁 튕겨 닫는 동작이 안 먹힙니다.
          <b>손가락을 따라간다</b>를 끄면 같은 규칙인데도 <b>내가 조작하고 있다는 느낌</b>이 사라집니다 —
          제스처에서 따라가기가 왜 핵심인지 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "제스처, 끌기, 쓸어넘기기, 당겨서 새로고침"),
    ("영어", "gesture, drag, swipe, pan, fling, pull-to-refresh"),
    ("같이 쓰는 말",
     "천천히 끄는 것이 <b>팬</b>·<b>드래그</b>, 빠르게 튕기는 것이 <b>스와이프</b>·<b>플링</b>입니다. "
     "판단 기준이 되는 거리가 <b>스레시홀드</b>(threshold), 놓은 뒤 미끄러지는 것이 <b>관성</b>(momentum)입니다. "
     "손을 뗐을 때 가까운 자리로 붙는 것을 <b>스냅</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>애니메이션</b> — 제스처는 <b>입력</b>입니다. 애니메이션은 손을 뗀 뒤에만 나옵니다.<br>"
     "<b>스크롤</b> — 브라우저가 이미 하는 스크롤과 <b>싸우면</b> 둘 다 망가집니다.<br>"
     "<b>터치 이벤트</b> — <code>touchstart</code>는 손가락만, <b>포인터 이벤트</b>는 마우스·펜·손가락을 한 코드로 받습니다."),
  ]),
  axes=ax("제스처"),
  oneline="<b>끄는 동안 따라가지 않으면 제스처가 아닙니다.</b> 그리고 거리만 보면 '끝까지 끌어야 하는' 조작이 됩니다 — <b>속도도</b> 봅니다.",
  s4_title="끄는 네 토막", s4_hint="손을 떼기 전과 뒤",
  states=states([
    (sheetbox("28%", "잡기 전 — 제자리"), "쉬는 중", "손잡이(그립)가 <b>끌 수 있음</b>을 알린다"),
    (sheetbox("44%", "끄는 중 — 손가락을 따라간다"), "끄는 중", "<b>1:1 로 따라간다.</b> 이게 제스처의 핵심"),
    (sheetbox("34%", "조금 끌고 놓음 → 제자리"), "문턱 못 넘음", "<b>제자리로 돌아온다.</b> 되돌릴 길이 늘 있어야 한다"),
    (sheetbox("72%", "절반 넘김 → 닫힘"), "문턱 넘음", "거리로 판단. <b>절반</b>이 흔한 기준"),
    (sheetbox("40%", "빠르게 튕김 → 닫힘"), "빠르게 튕김", "거리는 짧아도 <b>속도가 빠르면</b> 닫는다"),
    (sheetbox("28%", "끝까지 끌어야만 닫힌다", "150px", "76px", True), "속도를 안 볼 때", "짧게 튕겨도 안 닫혀 <b>답답하다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잡기", "pointerdown", "<code>setPointerCapture</code>로 <b>밖으로 나가도</b> 계속 받는다"),
    ("따라가기", "1:1", "끄는 동안 그대로 움직인다. <b>안 따라가면 조작이 아니다</b>"),
    ("놓기", "pointerup", "여기서 <b>처음으로</b> 애니메이션이 나온다"),
    ("문턱", "절반", "거리로 판단. 너무 작으면 <b>실수로 닫힌다</b>"),
    ("속도", "0.5px/ms", "짧게 튕겨도 닫히게. <b>거리만 보면 답답</b>하다"),
    ("브라우저와의 자리 다툼", "touch-action", "안 적으면 <b>스크롤이 먼저</b> 가져간다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>제스처는 숨어 있습니다.</b> 쓸어넘겨 지우기는 보이지 않고,
          마우스로도 키보드로도 할 수 없습니다.
          그래서 제스처로 되는 일은 <b>반드시 버튼으로도</b> 되어야 합니다 —
          시트에는 닫기 버튼과 <kbd>Esc</kbd>, 쓸어넘겨 지우기에는 메뉴 안의 '삭제'가 함께 있어야 합니다.
          제스처는 <b>빠른 길</b>이지 유일한 길이 아닙니다.</p>''',
  do=ul([
    "<b>손으로 다루는 느낌</b>이 필요한 것 — 시트, 카드 넘기기, 당겨서 새로고침",
    "자주 하는 동작의 <b>빠른 길</b>",
    "폰에서 <b>엄지로 닿기 어려운</b> 버튼을 대신할 때",
  ]),
  dont=ul([
    "제스처로<b>만</b> 되는 일 — 버튼도 함께 둔다",
    "되돌릴 수 없는 일을 한 번 쓸어서 — <b>실수로 지워진다</b>",
    "브라우저 스크롤과 <b>같은 방향</b>으로 다투기",
    "PC 에서 끌기만으로 되는 일 — <b>마우스로는 불편</b>하다",
  ]),
  instead='놓은 뒤의 움직임은 <a href="spring.html">스프링</a>, 들고 나는 짝은 <a href="enterexit.html">진입과 퇴장</a>, 버튼으로 되는 길은 <a href="../items/sheet.html">바텀시트</a>·<a href="../items/dialog.html">다이얼로그</a>.',
  cases=cases([
    (sheetbox("44%", "", "150px"), "끌어 닫는 시트", "가장 흔하다. <b>손잡이</b>가 끌 수 있음을 알린다"),
    ('''              <div style="width:100%;max-width:150px;position:relative;height:40px;border:1px solid var(--line);border-radius:6px;overflow:hidden;background:var(--danger)">
                <div style="position:absolute;inset:0 32% 0 0;background:var(--surface);display:flex;align-items:center;padding:0 7px;font-size:9.5px">모란상회</div>
                <span style="position:absolute;right:8px;top:12px;font-size:9px;color:#fff">삭제</span>
              </div>''',
     "쓸어넘겨 지우기", "<b>되돌리기</b>가 붙어야 쓸 수 있다"),
    ('''              <div style="width:100%;max-width:150px;height:56px;position:relative;border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">
                <span style="position:absolute;left:50%;top:8px;transform:translateX(-50%);width:16px;height:16px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--accent)"></span>
                <div style="position:absolute;left:0;right:0;top:30px;bottom:0;background:var(--surface);border-top:1px solid var(--line)"></div>
              </div>''',
     "당겨서 새로고침", "<b>당긴 만큼</b> 표시가 자란다. 안 따라가면 작동을 모른다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 제스처의 계약서",
  code_lede="포인터 이벤트 하나로 마우스·펜·손가락을 다 받고, <code>touch-action</code>을 반드시 적습니다.",
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
    ("<code>touch-action</code>", "<code>none</code>·<code>pan-y</code>. 안 적으면 <b>브라우저가 먼저</b> 가져간다"),
    ("<code>setPointerCapture</code>", "손가락이 상자 밖으로 나가도 이벤트가 계속 온다. <b>없으면 중간에 끊긴다</b>"),
    ("<code>pointercancel</code>", "전화가 오거나 브라우저가 가로채면 온다. <b>제자리로 되돌려야</b> 한다"),
    ("키보드 길을 반드시", "<kbd>Esc</kbd>로 닫기, <b>닫기 버튼</b>. 제스처는 키보드로 흉내 낼 수 없다"),
    ("<code>user-select: none</code>", "끄는 동안 글자가 잡혀 파랗게 되는 것을 막는다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>", "따라가기는 <b>그대로 둔다</b> — 내 손가락이 만든 움직임이라 멀미를 일으키지 않는다"),
  ]),
  backend=rows([
    ("쓸어서 지우기는 되돌릴 수 있어야", "실수가 잦은 조작이라 <b>바로 지우지 말고</b> 되돌릴 틈을 둡니다. 보통 5초쯤 뒤에 진짜로 보냅니다."),
    ("당겨서 새로고침이 연타된다", "몇 번을 당겨도 요청은 <b>하나만</b> 나가게 막습니다. 안 그러면 같은 요청이 줄줄이 갑니다."),
    ("끄는 중에는 요청하지 않는다", "손을 떼기 전까지는 <b>아무 일도 확정되지 않았습니다.</b> 중간 값으로 서버를 부르지 않습니다."),
    ("끊긴 제스처", "앱이 배경으로 가면 <code>pointercancel</code>만 오고 <code>pointerup</code>은 안 옵니다. <b>되돌리는 쪽</b>이 기본값이어야 합니다."),
  ]),
  plat_lede="폰에서는 당연한 것이고, <b>PC 에서는 보조</b>입니다.",
  plats=plats([
    ("웹", "Pointer Events",
     sheetbox("44%", "", "105px", "60px"),
     "마우스·펜·손가락을 한 코드로 받습니다. <b>브라우저 기본 동작과의 자리 다툼</b>이 가장 큰 일거리입니다."),
    ("iOS", "UIGestureRecognizer",
     '''              <div class="phone" role="img" aria-label="iOS 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"><span style="display:block;width:14px;height:2px;background:var(--line-strong);margin:4px auto;border-radius:2px"></span></div></div></div>''',
     "제스처마다 전용 인식기가 있고 <b>서로 양보하는 규칙</b>까지 정해져 있습니다. 가장자리에서 쓸면 뒤로가기입니다."),
    ("안드로이드", "GestureDetector",
     '''              <div class="phone" role="img" aria-label="안드로이드 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"><span style="display:block;width:14px;height:2px;background:var(--line-strong);margin:4px auto;border-radius:2px"></span></div></div></div>''',
     "<b>양쪽 가장자리</b>가 전부 뒤로가기라, 가장자리에서 끄는 제스처를 만들면 부딪힙니다."),
  ]),
  plat_note="\"카톡처럼 쓸어서 답장\"류 요청은 <b>만드는 품보다 뒤처리가</b> 많습니다 — 되돌리기, 키보드 길, 스크롤과의 다툼, 가장자리 뒤로가기와의 충돌까지가 한 벌입니다. 제스처를 넣기로 했으면 <b>같은 일을 하는 버튼</b>을 먼저 만들고 제스처를 얹는 순서가 안전합니다.",
  siblings=siblings("gesture"),
  related='''        <li><a href="spring.html"><b>스프링</b><em>9부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>''',
)
