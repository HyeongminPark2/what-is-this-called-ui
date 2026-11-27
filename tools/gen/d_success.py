# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

HOW = table(
  ["어디에 뜨나", "얼마나 남나", "놓칠 수 있나", "되돌릴 길을 붙이나"],
  [["토스트", "화면 구석", "몇 초", "<b>놓치기 쉽다</b>", "붙이기 좋다"],
   ["그 자리에 글", "<b>누른 곳 옆</b>", "다음 동작까지", "안 놓친다", "붙일 수 있다"],
   ["화면 전환", "<b>화면 전체</b>", "다음 화면까지", "안 놓친다", "다음 할 일을 둔다"],
   ["아무것도 안 함", "—", "—", "<b>됐는지 모른다</b>", "없다"]],
  me="성공 확인")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">무엇이 됐는지 — '저장했습니다'</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">어디에 뜨나 — 누른 곳 가까이</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">role="status" — 소리로도</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">다음 할 일 — '영수증 보기'</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">안 알리면 같은 일을 또 보낸다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">토스트는 몇 초 뒤 사라진다 — 놓치면 끝</div>
                </div>
              </div>'''

def msg(kind, text, note="", ok=None, w="152px", sub=""):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if kind == 'toast':
        inner = ('<span style="display:block;border-radius:5px;background:var(--fg);color:var(--surface);'
                 'padding:4px 8px;font-size:8px">' + text + '</span>')
    elif kind == 'inline':
        inner = ('<span style="display:flex;gap:5px;align-items:center;border-radius:4px;'
                 'background:color-mix(in srgb, #1a7f37 12%, var(--surface));color:#1a7f37;'
                 'border:1px solid color-mix(in srgb, #1a7f37 35%, transparent);padding:3px 7px;font-size:8px">'
                 '<span aria-hidden="true">✓</span>' + text + '</span>')
    elif kind == 'screen':
        inner = ('<span style="display:grid;gap:3px;place-items:center;padding:5px 0">'
                 '<span style="display:grid;place-items:center;width:18px;height:18px;border-radius:999px;'
                 'background:#1a7f37;color:#fff;font-size:9px">✓</span>'
                 '<span style="font-size:8.5px;font-weight:700">' + text + '</span>'
                 + ('<span style="font-size:7.5px;color:var(--fg-muted)">' + sub + '</span>' if sub else '')
                 + '</span>')
    else:
        inner = ('<span style="display:block;font-size:8px;color:var(--fg-muted);text-align:center;padding:6px 0">'
                 + text + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);padding:6px">'
            + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

D = dict(
  slug="success", ko="성공 확인", en="Success feedback",
  desc="일이 됐다는 것을 알리는 방법 셋과, 안 알렸을 때 생기는 중복 제출.",
  lede="안 알리면 <b>됐는지 알 수 없어</b> 다시 누릅니다. 알리는 자리는 <b>누른 곳 가까이</b>가 기본입니다.",
  axes_lede="성공을 알리는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>저장</b>을 눌러 보세요. 아무것도 안 알리면 됐는지 알 수 없어 다시 누르게 됩니다 —
          데모가 <b>같은 일을 몇 번 보냈는지</b> 셉니다.<br>
          <b>토스트</b>는 몇 초 뒤 사라져 놓치기 쉽고, <b>그 자리에 글</b>은 남아 있어 확실하며,
          <b>화면 전환</b>은 결과 화면 자체가 알림이 됩니다.
          어느 쪽이든 <code>role="status"</code> 로 <b>소리로도</b> 알려야 합니다 —
          데모가 그 여부도 같이 적습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "성공 확인, 완료 알림, 성공 피드백"),
    ("영어", "success feedback, confirmation, success message"),
    ("같이 쓰는 말",
     "화면 구석에 잠깐 뜨는 띠가 <b>토스트</b>·<b>스낵바</b>, "
     "누른 자리 옆에 남는 글이 <b>인라인 메시지</b>, "
     "끝났다고 알리는 화면 한 장이 <b>완료 화면</b>(confirmation page)입니다. "
     "소리로 알리는 자리를 <b>라이브 리전</b>이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 <b>부품</b>이고 성공 확인은 <b>목적</b>입니다.<br>"
     "<b>알림</b> — <a href=\"notifications.html\">알림 센터</a>는 <b>나중에 보는</b> 것입니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 <b>되기 전에</b> 먼저 보여 줍니다."),
  ]),
  axes=HOW,
  oneline="<b>누른 곳 가까이에 남겨 두세요.</b> 구석에서 몇 초 떴다 사라지면 못 본 사람이 생깁니다.",
  s4_title="알리는 법", s4_hint="놓칠 수 있는가가 갈린다",
  states=states([
    (msg("inline", "저장했습니다", "누른 곳 옆에 남는다", True), "그 자리에 글", "<b>안 놓친다</b>"),
    (msg("toast", "저장했습니다", "몇 초 뒤 사라진다", None), "토스트", "<b>놓칠 수 있다</b>"),
    (msg("screen", "저장했습니다", "결과 화면 자체가 알림", True, "152px", "11월 설정이 바뀌었습니다"),
     "화면 전환", "<b>큰 일</b>에 쓴다"),
    (msg("none", "(아무 일도 안 일어난 듯 보인다)", "다시 누르게 된다", False), "안 알림", "<b>또 보내게</b> 된다"),
    (msg("toast", "저장했습니다 · 되돌리기", "되돌릴 길을 붙였다", True), "되돌리기와 함께", "<b>무를 수 있게</b>"),
    (msg("inline", "저장했습니다 · 영수증 보기", "다음 할 일을 준다", True), "다음 할 일", "<b>이어서 할 것</b>을 준다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이 됐는지", "한 줄", "'저장했습니다'"),
    ("어디에", "누른 곳 가까이", "구석은 <b>눈이 안 간다</b>"),
    ("<code>role=\"status\"</code>", "소리로", "<b>하던 말이 끝난 뒤</b> 읽는다"),
    ("다음 할 일", "있으면 붙임", "'영수증 보기'"),
    ("안 알림", "중복 제출", "같은 일을 <b>또 보낸다</b>"),
    ("토스트", "사라짐", "놓치면 <b>끝</b>이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          성공을 안 알리면 <b>중복 제출</b>이 생깁니다 —
          결제나 신청처럼 두 번 가면 안 되는 일에서는 이게 바로 사고입니다.
          그래서 서버 쪽에도 <b>같은 요청을 두 번 받아도 한 번만 처리</b>하는 장치가 필요합니다.<br>
          소리로 듣는 사람에게는 <b>화면이 바뀌어도 모릅니다</b> —
          <code>role="status"</code> 가 없으면 '저장했습니다'가 떠도 아무 소리가 안 납니다.
          반대로 <code>role="alert"</code> 를 쓰면 하던 말을 끊고 읽어 버려,
          성공 같은 급하지 않은 알림에는 <b>맞지 않습니다</b>.</p>''',
  do=ul([
    "<b>누른 곳 가까이</b>에 남기기",
    "<code>role=\"status\"</code> 로 <b>소리로도</b> 알리기",
    "되돌릴 수 있으면 <b>되돌리기</b>를, 이어 할 일이 있으면 <b>그 길</b>을 붙이기",
  ]),
  dont=ul([
    "<b>아무것도 안 알리기</b> — 같은 일을 또 보낸다",
    "성공에 <code>role=\"alert\"</code> 쓰기 — <b>하던 말을 끊는다</b>",
    "토스트만 띄우고 <b>자리에는 아무 자국도</b> 안 남기기",
    "'성공' 한 낱말만 쓰기 — <b>무엇이</b> 됐는지 적는다",
  ]),
  instead='띠 부품 자체는 <a href="toast.html">토스트</a>, 실패는 <a href="error.html">에러 상태</a>, 되돌리기는 <a href="undo.html">되돌리기</a>, 소리로 알리는 장치는 <a href="live.html">라이브 리전</a>.',
  cases=cases([
    (msg("inline", "저장했습니다", "", True), "설정 저장", "<b>그 자리</b>에"),
    (msg("screen", "주문이 접수됐습니다", "", True, "150px", "주문번호 2411-0042"),
     "결제 완료", "<b>화면 한 장</b>으로"),
    (msg("toast", "1건을 보관했습니다 · 되돌리기", "", True), "목록 동작", "<b>토스트 + 되돌리기</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 알림의 계약서",
  code_lede="자리에 남기고 <code>role=\"status\"</code> 로 소리를 더합니다.",
  code='''&lt;<span class="t">form</span>&gt;
  …
  &lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"ok"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✓&lt;/<span class="t">span</span>&gt; 저장했습니다
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/receipts/2411"</span>&gt;영수증 보기&lt;/<span class="t">a</span>&gt;
  &lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">form</span>&gt;

<span class="c">// 두 번 보내지 않게 — 보내는 동안 단추를 잠근다</span>
btn.disabled = <span class="t">true</span>;
<span class="t">await</span> save();
btn.disabled = <span class="t">false</span>;
ok.textContent = <span class="s">'저장했습니다'</span>;   <span class="c">// role="status" 가 읽어 준다</span>''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "성공은 <b>급하지 않다</b> — 하던 말이 끝난 뒤 읽는다"),
    ("<code>role=\"alert\"</code>", "실패에만 쓴다 — <b>하던 말을 끊는다</b>"),
    ("초점", "성공 메시지로 <b>초점을 옮기지 않는다</b> — 하던 일이 끊긴다"),
    ("화면 전환", "바뀐 화면의 <b>제목으로</b> 초점을 옮긴다"),
    ("단추 잠금", "보내는 동안 잠가 <b>두 번 보내기</b>를 막는다"),
    ("확인하는 법", "화면을 끄고 <b>소리만</b> 들어 본다 — 됐다는 말이 들리는가"),
  ]),
  backend=rows([
    ("두 번 받아도 한 번만", "<b>멱등 키</b>(Idempotency-Key)를 받으면 같은 요청이 두 번 와도 한 번만 처리합니다."),
    ("결과를 담아 준다", "저장한 것의 <code>id</code> 를 돌려주면 화면이 <b>'영수증 보기'</b> 같은 다음 길을 만들 수 있습니다."),
    ("부분 성공", "열 건 중 여덟 건만 됐다면 <b>그 숫자</b>를 돌려줘야 화면이 제대로 적습니다."),
  ]),
  plat_lede="<b>어디에 남기느냐</b>가 플랫폼마다 조금씩 다릅니다.",
  plats=plats([
    ("웹", "직접 만듦",
     msg("inline", "저장했습니다", "", True, "110px"),
     "자리에 남기는 쪽을 기본으로 삼습니다. <code>role=\"status\"</code> 를 빠뜨리기 쉽습니다."),
    ("iOS", "화면 전환 · 햅틱",
     '''              <div class="phone" role="img" aria-label="iOS 성공 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:30px;transform:translateX(-50%);width:14px;height:14px;border-radius:999px;background:#1a7f37"></div>
                <div style="position:absolute;left:8px;right:8px;top:50px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "토스트가 없어 <b>화면 전환</b>이나 작은 표시로 알립니다. <b>햅틱</b>으로 손끝에도 알립니다."),
    ("안드로이드", "Snackbar",
     '''              <div class="phone" role="img" aria-label="안드로이드 스낵바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;bottom:6px;height:11px;border-radius:3px;background:var(--fg);opacity:.9"></div></div></div>''',
     "<b>스낵바</b>가 표준이고 되돌리기를 붙이는 것도 흔합니다."),
  ]),
  plat_note="iOS 에 토스트가 없는 것은 <b>화면 구석의 알림을 안 쓰겠다</b>는 선택입니다 — 대신 화면을 바꾸거나 손끝으로 알립니다. 웹에는 햅틱이 거의 없으니 <b>눈과 소리</b> 둘로만 알려야 하고, 그래서 자리에 남기는 쪽이 더 중요해집니다. 안드로이드의 스낵바는 편하지만 <b>몇 초 뒤 사라진다</b>는 약점이 그대로 있어서, 중요한 결과는 자리에도 남기는 편이 안전합니다.",
  siblings=siblings("success"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>
        <li><a href="undo.html"><b>되돌리기</b><em>8부</em></a></li>''',
)
