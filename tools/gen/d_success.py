# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">'저장했습니다'처럼 무엇이 됐는지 적음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">누른 곳 가까이에 띄움</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">role="status"를 달아 소리로도 알림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">다음 할 일 '영수증 보기'를 붙임</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">알리지 않으면 같은 요청을 또 보냄</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">토스트는 몇 초 뒤 사라져 놓치기 쉬움</div>
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
  desc="작업이 끝났다는 것을 알리는 세 가지 방법과, 알리지 않았을 때 생기는 중복 제출을 보여 주는 항목입니다.",
  lede="성공 확인은 사용자가 요청한 작업이 끝났다고 알려 주는 표시입니다. 알려 주지 않으면 사용자는 <b>작업이 됐는지 알 수 없어서</b> 버튼을 다시 누릅니다. 알림은 <b>사용자가 누른 곳 가까이</b>에 띄우는 것이 기본입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>저장</b>을 눌러 보세요. 아무것도 알리지 않으면 저장됐는지 알 수 없어서 다시 누르게 되는데,
          데모는 <b>같은 요청을 몇 번 보냈는지</b> 셉니다.<br>
          <b>토스트</b>는 몇 초 뒤 사라져서 놓치기 쉽고, <b>누른 자리에 글</b>을 띄우면 글이 남아 있어서 확실하게 알 수 있으며,
          <b>화면 전환</b>은 바뀐 결과 화면 자체가 알림 역할을 합니다.
          어느 방법을 쓰든 <code>role="status"</code>로 <b>스크린 리더에도</b> 알려야 하며,
          데모는 스크린 리더에 알렸는지도 함께 적습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "성공 확인, 완료 알림, 성공 피드백"),
    ("영어", "success feedback, confirmation, success message"),
    ("같이 쓰는 말",
     "화면 구석에 잠깐 뜨는 띠는 <b>토스트</b>나 <b>스낵바</b>, "
     "누른 자리 옆에 남는 글은 <b>인라인 메시지</b>, "
     "작업이 끝났다고 알리는 화면 한 장은 <b>완료 화면</b>(confirmation page)이라고 부릅니다. "
     "스크린 리더가 바뀐 내용을 읽어 주는 영역은 <b>라이브 리전</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 화면 <b>부품</b>의 이름이고, 성공 확인은 그 부품으로 이루려는 <b>목적</b>입니다.<br>"
     "<b>알림</b> — <a href=\"notifications.html\">알림 센터</a>는 쌓인 소식을 <b>나중에 모아 보는</b> 곳이고, 성공 확인은 작업 직후 바로 보여 줍니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 작업이 <b>끝나기 전에</b> 결과를 먼저 보여 주고, 성공 확인은 끝난 뒤에 알립니다."),
  ]),
  s4_title="성공을 알리는 방법", s4_hint="방법마다 다른, 알림을 놓칠 가능성",
  states=states([
    (msg("inline", "저장했습니다", "누른 곳 옆에 남음", True), "누른 자리에 글로 알릴 때", "글이 남아 있어서 <b>놓치지 않습니다</b>"),
    (msg("toast", "저장했습니다", "몇 초 뒤 사라짐", None), "토스트로 알릴 때", "몇 초 뒤 사라지므로 <b>놓칠 수 있습니다</b>"),
    (msg("screen", "저장했습니다", "결과 화면 자체가 알림", True, "152px", "11월 설정이 바뀌었습니다"),
     "결과 화면으로 넘어갈 때", "결제처럼 <b>큰 작업</b>을 마쳤을 때 씁니다"),
    (msg("none", "(아무 일도 일어나지 않은 것처럼 보임)", "다시 누르게 됨", False), "아무것도 알리지 않을 때", "사용자가 같은 요청을 <b>또 보내게</b> 됩니다"),
    (msg("toast", "저장했습니다 · 되돌리기", "되돌리기를 붙임", True), "되돌리기를 함께 붙일 때", "되돌리기를 붙여 방금 한 일을 <b>무를 수 있게</b> 합니다"),
    (msg("inline", "저장했습니다 · 영수증 보기", "다음 할 일을 알려 줌", True), "다음 할 일을 함께 붙일 때", "사용자가 <b>이어서 할 일</b>로 가는 링크를 붙입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이 됐는지", "한 줄로 적음", "'저장했습니다'처럼 무엇이 됐는지 한 줄로 적습니다"),
    ("알림 위치", "누른 곳 가까이", "화면 구석에는 사용자의 <b>눈이 잘 가지 않습니다</b>"),
    ("<code>role=\"status\"</code>", "소리로도 알림", "스크린 리더가 <b>읽던 내용을 마친 뒤</b> 읽어 줍니다"),
    ("다음 할 일", "있으면 붙임", "'영수증 보기'처럼 이어서 할 일이 있으면 붙입니다"),
    ("알리지 않았을 때", "중복 제출", "알리지 않으면 사용자가 같은 요청을 <b>또 보냅니다</b>"),
    ("토스트", "몇 초 뒤 사라짐", "토스트가 사라진 뒤에는 <b>다시 볼 방법이 없습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          성공을 알리지 않으면 사용자가 같은 요청을 다시 보내는 <b>중복 제출</b>이 생깁니다.
          결제나 신청처럼 두 번 처리되면 안 되는 일에서는 중복 제출이 곧 사고로 이어집니다.
          그래서 서버에도 <b>같은 요청을 두 번 받아도 한 번만 처리</b>하는 장치가 필요합니다.<br>
          스크린 리더로 듣는 사람은 <b>화면이 바뀌어도 알 수 없습니다</b>.
          <code>role="status"</code>가 없으면 '저장했습니다'가 화면에 떠도 아무것도 읽어 주지 않습니다.
          반대로 <code>role="alert"</code>를 쓰면 스크린 리더가 읽던 내용을 끊고 바로 읽기 때문에,
          성공처럼 급하지 않은 알림에는 <b>맞지 않습니다</b>.</p>''',
  do=ul([
    "성공 알림을 <b>누른 곳 가까이</b>에 남길 때",
    "<code>role=\"status\"</code>로 <b>스크린 리더에도</b> 알릴 때",
    "되돌릴 수 있으면 <b>되돌리기</b>를, 이어서 할 일이 있으면 <b>그 일로 가는 링크</b>를 붙일 때",
  ]),
  dont=ul([
    "<b>아무것도 알리지 않을 때</b>. 사용자가 같은 요청을 또 보냅니다",
    "성공 알림에 <code>role=\"alert\"</code>를 쓸 때. 스크린 리더가 <b>읽던 내용을 끊습니다</b>",
    "토스트만 띄우고 <b>누른 자리에는 아무 표시도</b> 남기지 않을 때",
    "'성공' 한 낱말만 적을 때. <b>무엇이</b> 됐는지까지 적습니다",
  ]),
  instead='화면 구석에 뜨는 띠 부품 자체는 <a href="toast.html">토스트</a> 항목에서, 실패를 알리는 방법은 <a href="error.html">에러 상태</a> 항목에서 다룹니다. 방금 한 일을 무르게 하는 방법은 <a href="undo.html">되돌리기</a>에, 스크린 리더가 소리로 읽어 주게 하는 장치는 <a href="live.html">라이브 리전</a>에 정리되어 있습니다.',
  do_title="성공을 알릴 때 지킬 것", dont_title="성공을 알릴 때 피할 것", instead_title="함께 보면 좋은 항목",
  cases=cases([
    (msg("inline", "저장했습니다", "", True), "설정을 저장했다고 알리기", "저장 버튼 옆 <b>그 자리</b>에 알립니다"),
    (msg("screen", "주문이 접수됐습니다", "", True, "150px", "주문번호 2411-0042"),
     "결제 완료를 화면 한 장으로 알리기", "완료 <b>화면 한 장</b>으로 알립니다"),
    (msg("toast", "1건을 보관했습니다 · 되돌리기", "", True), "목록에서 보관한 뒤 되돌리기 붙이기", "<b>토스트에 되돌리기를 붙여</b> 알립니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="알림을 누른 자리에 남기고, <code>role=\"status\"</code>를 붙여 스크린 리더도 읽게 합니다.",
  code='''&lt;<span class="t">form</span>&gt;
  …
  &lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"ok"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✓&lt;/<span class="t">span</span>&gt; 저장했습니다
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/receipts/2411"</span>&gt;영수증 보기&lt;/<span class="t">a</span>&gt;
  &lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">form</span>&gt;

<span class="c">// 두 번 보내지 않도록 보내는 동안 단추를 잠근다</span>
btn.disabled = <span class="t">true</span>;
<span class="t">await</span> save();
btn.disabled = <span class="t">false</span>;
ok.textContent = <span class="s">'저장했습니다'</span>;   <span class="c">// role="status" 가 읽어 준다</span>''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "성공 알림은 <b>급하지 않으므로</b> 스크린 리더가 읽던 내용을 마친 뒤 읽게 합니다"),
    ("<code>role=\"alert\"</code>", "실패에만 씁니다. 스크린 리더가 <b>읽던 내용을 끊고</b> 바로 읽기 때문입니다"),
    ("성공 메시지와 초점", "성공 메시지로 <b>초점을 옮기지 않습니다</b>. 초점을 옮기면 사용자가 하던 일이 끊깁니다"),
    ("결과 화면으로 넘어갈 때", "바뀐 화면의 <b>제목으로</b> 초점을 옮깁니다"),
    ("보내는 동안 버튼 잠그기", "보내는 동안 버튼을 잠가 <b>두 번 보내는 것</b>을 막습니다"),
    ("확인하는 방법", "화면을 끄고 스크린 리더 <b>소리만</b> 들으며, 저장됐다는 말이 들리는지 확인합니다"),
  ]),
  backend=rows([
    ("같은 요청을 두 번 받아도 한 번만 처리하기", "요청에 <b>멱등 키</b>(Idempotency-Key)를 받아 두면 같은 요청이 두 번 와도 한 번만 처리할 수 있습니다."),
    ("응답에 결과 id 담아 주기", "저장한 것의 <code>id</code>를 응답에 담아 주면 화면에서 <b>'영수증 보기'</b> 같은 다음 동작으로 가는 링크를 만들 수 있습니다."),
    ("일부만 성공했을 때", "열 건 가운데 여덟 건만 처리됐다면 <b>처리된 건수</b>를 응답에 담아야 화면에 결과를 정확하게 적을 수 있습니다."),
  ]),
  plat_lede="성공 알림을 <b>어디에 남기는지</b>는 플랫폼마다 조금씩 다릅니다.",
  plats=plats([
    ("웹", "직접 만듦",
     msg("inline", "저장했습니다", "", True, "110px"),
     "누른 자리에 남기는 방식을 기본으로 삼습니다. <code>role=\"status\"</code>를 빠뜨리기 쉽습니다."),
    ("iOS", "화면 전환 · 햅틱",
     '''              <div class="phone" role="img" aria-label="iOS 성공 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:30px;transform:translateX(-50%);width:14px;height:14px;border-radius:999px;background:#1a7f37"></div>
                <div style="position:absolute;left:8px;right:8px;top:50px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "토스트 부품이 없어서 <b>화면 전환</b>이나 작은 표시로 알리고, <b>햅틱</b> 진동으로도 알립니다."),
    ("안드로이드", "Snackbar",
     '''              <div class="phone" role="img" aria-label="안드로이드 스낵바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;bottom:6px;height:11px;border-radius:3px;background:var(--fg);opacity:.9"></div></div></div>''',
     "<b>스낵바</b>가 표준이고, 스낵바에 되돌리기를 붙이는 경우도 흔합니다."),
  ]),
  plat_note="iOS에 토스트가 없는 것은 <b>화면 구석에 띄우는 알림을 쓰지 않기로</b> 한 선택이고, 그 대신 화면을 바꾸거나 햅틱으로 알립니다. 웹에서는 햅틱을 거의 쓸 수 없어서 <b>화면과 소리</b>로만 알려야 하기 때문에, 누른 자리에 알림을 남기는 일이 더 중요합니다. 안드로이드의 스낵바는 쓰기 편하지만 <b>몇 초 뒤 사라지는</b> 약점이 있으므로, 중요한 결과는 누른 자리에도 남기는 편이 안전합니다.",
  siblings=siblings("success"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>
        <li><a href="undo.html"><b>되돌리기</b><em>8부</em></a></li>''',
)
