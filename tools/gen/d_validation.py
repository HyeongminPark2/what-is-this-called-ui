# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fld(lab, val="", msg="", kind="", w="160px"):
    col = {"err": "var(--danger)", "ok": "var(--accent)", "warn": "var(--warn)"}.get(kind, "var(--line)")
    mc = {"err": "var(--danger)", "ok": "var(--accent)", "warn": "var(--warn)"}.get(kind, "var(--fg-muted)")
    ico = {"err": "✕ ", "ok": "✓ ", "warn": "! "}.get(kind, "")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:2px">'
            '<span style="font-size:9px;color:var(--fg-muted)">' + lab + '</span>'
            '<div style="border:1px solid ' + col + ';border-radius:5px;background:var(--surface);padding:4px 7px;font-size:10.5px;'
            + ('color:var(--fg-muted)' if not val else '') + '">' + (val or '&nbsp;') + '</div>'
            + ('<span style="font-size:8.5px;color:' + mc + '">' + ico + msg + '</span>' if msg else '') + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">치는 동안엔 가만둔다 — 다 치기 전에 틀렸다고 하지 않는다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">칸을 떠날 때(blur) 검사한다</div>
                  <div class="pin-out" data-pin="3" style="max-width:220px">''' + fld('사업자번호', '124', '10자리를 채워 주세요', 'err', '220px').strip() + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-invalid="true" + aria-describedby="no-err"</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한번 틀린 칸은 <b>고치는 즉시</b> 다시 검사한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">제출하면 <b>첫 오류 칸으로 초점</b>을 옮긴다</div>
                </div>
              </div>'''

D = dict(
  slug="validation", ko="입력 검증", en="Validation",
  desc="입력값을 언제 검사하고 어떻게 알릴지를, 치는 중·떠날 때·제출할 때의 차이와 오류 메시지를 칸에 붙이는 법까지 다루는 항목입니다.",
  lede="입력 검증은 사용자가 넣은 값이 틀렸을 때 알려 주는 일입니다. '무엇이 틀렸나'를 판단하는 것보다 <b>언제 알려 줄지</b> 정하는 것이 더 까다롭습니다.",
  axes_lede="데이터를 다루는 화면을 설계할 때는 '건수가 늘면 어떻게 되나'부터 따져야 합니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>검사 시점을 바꿔 가며 칸에 글자를 쳐 보세요.<br>
          <b>칠 때마다</b> 검사하면 두 글자만 쳐도 칸이 빨개져서 사용자가 재촉받는 느낌을 받습니다.
          <b>떠날 때</b> 검사하면 입력하는 동안에는 아무 표시가 없다가 칸을 벗어나는 즉시 알려 줍니다.
          <b>제출할 때만</b> 검사하면 폼을 다 채운 뒤에야 오류를 한꺼번에 보게 됩니다.<br>
          제출을 눌러 보면 <b>첫 번째 오류 칸으로 포커스가 옮겨 가는</b> 것도 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "검증, 유효성 검사, 입력 확인"),
    ("영어", "validation, form validation, constraint validation"),
    ("같이 쓰는 말",
     "글자를 칠 때마다 검사하는 것은 <b>실시간 검증</b>(live·inline validation), "
     "제출할 때 한꺼번에 검사하는 것은 <b>제출 검증</b>이라고 합니다. "
     "브라우저가 <code>required</code>·<code>pattern</code> 같은 속성을 보고 대신 검사해 주는 기능은 "
     "<b>제약 검증 API</b>(Constraint Validation API)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>오류 메시지</b> — <a href=\"../items/error.html\">오류 메시지</a>는 검사 결과를 보여 주는 부분이고, 검증은 값이 맞는지 <b>판단하는</b> 과정입니다.<br>"
     "<b>인증</b>(authentication) — 인증은 사용자가 본인이 맞는지 확인하는 일이라 입력 검증과는 전혀 다른 일이고, 영어로도 다른 단어를 씁니다.<br>"
     "<b>폼</b> — 입력 검증은 <a href=\"form.html\">폼 설계</a>를 이루는 한 부분입니다."),
  ]),
  axes=ax("입력 검증"),
  oneline="입력 검증에서는 <b>사용자가 값을 다 치기 전에 틀렸다고 하지 않습니다.</b> 반대로 <b>한 번 틀렸다고 알린 칸은 사용자가 고치는 즉시 오류 표시를 풉니다.</b>",
  s4_title="상태", s4_hint="검사하는 시점에 따라 달라지는 상태",
  states=states([
    (fld('사업자번호', '', '- 없이 10자리'), "치기 전", "입력 규칙을 <b>미리</b> 알려 줍니다. 틀린 뒤에 알려 주는 것보다 낫습니다"),
    (fld('사업자번호', '124'), "치는 중", "아직 다 입력하지 않았으므로 <b>아무것도 표시하지 않습니다</b>"),
    (fld('사업자번호', '124', '10자리를 채워 주세요', 'err'), "떠날 때", "칸을 벗어나는 시점에 오류를 알립니다. 검사 시점은 이것을 기본으로 삼습니다"),
    (fld('사업자번호', '1248100998', '확인됨', 'ok'), "고쳐짐", "한번 틀린 칸은 사용자가 <b>고치는 즉시</b> 오류 표시를 풉니다"),
    (fld('사업자번호', '1248100998', '확인하는 중…', 'warn'), "서버에 물어보는 중", "중복 확인처럼 서버에 물어야 하는 검사입니다. <b>확인하는 중이라는 표시</b>를 보여 줍니다"),
    (fld('사업자번호', '1248100998', '이미 등록된 번호입니다', 'err'), "서버가 거절", "브라우저에서는 잡을 수 없는 오류입니다. 다른 오류와 <b>같은 자리</b>에 같은 모양으로 붙입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("치는 중엔 조용히", "on input: 안 함", "두 글자만 쳤는데 칸이 빨개지면 사용자는 <b>재촉받는다고</b> 느낍니다"),
    ("떠날 때 검사", "on blur", "칸을 벗어나는 때를 입력을 마친 시점으로 보고, 이때 검사하는 것을 기본으로 삼습니다"),
    ("메시지는 칸 밑", "같은 자리", "메시지가 칸에서 멀리 떨어져 있으면 <b>어느 칸에 대한 말인지</b> 알기 어렵습니다"),
    ("기계에게 알리기", "aria-invalid / describedby", "빨간 테두리는 <b>눈으로만</b> 알 수 있으므로 스크린 리더에도 틀렸음을 알립니다"),
    ("고치면 즉시 풀기", "re-validate on input", "한번 틀린 칸에만 적용합니다. 이미 틀린 칸은 칠 때마다 검사해도 사용자가 거슬려 하지 않습니다"),
    ("제출하면 초점 이동", "focus first error", "오류 칸이 화면 밖에 있으면 제출을 눌러도 <b>아무 일도 일어나지 않은 것</b>처럼 보이므로 첫 오류 칸으로 포커스를 옮깁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          검사 시점은 <b>틀리기 전과 뒤가 다릅니다</b>. 처음에는 <b>떠날 때</b> 검사하고,
          한번 틀린 칸은 그때부터 <b>칠 때마다</b> 검사합니다.
          처음부터 칠 때마다 검사하면 다 치기 전에 칸이 빨개져서 사용자가 재촉받는 느낌을 받습니다.
          반대로 고친 뒤에도 칸을 떠날 때까지 빨간 채로 두면 <b>고쳤는데도 아직 틀렸다고 하는</b> 것처럼 보입니다.
          대부분의 폼 라이브러리가 이 두 단계 방식을 기본값으로 둡니다.</p>''',
  do=ul([
    "번호 자릿수, 날짜, 전자우편처럼 <b>형식이 정해진</b> 값을 받을 때",
    "중복, 잔액, 권한처럼 <b>서버만 알 수 있는</b> 조건을 확인할 때",
    "되돌리기 어려운 동작을 실행하기 직전",
  ]),
  dont=ul([
    "입력하는 도중에 칸을 빨갛게 표시할 때. <b>다 치기 전에는 틀렸다고 하지 않습니다</b>",
    "'올바른 값을 입력하세요'처럼 막연하게 알릴 때. <b>무엇이 어떻게</b> 틀렸는지 적습니다",
    "색만으로 알릴 때. 빨간 테두리만으로는 색을 구별하지 못하는 사람이 오류를 알아챌 수 없습니다",
    "브라우저 검사만 믿을 때. <b>서버가 다시</b> 검사해야 합니다",
  ]),
  instead='오류를 보여 주는 방법은 <a href="../items/error.html">오류 메시지</a>, 확인만 받으려면 <a href="../items/dialog.html">다이얼로그</a>, 처리 결과를 알리려면 <a href="../items/toast.html">토스트</a>를 봅니다.',
  cases=cases([
    (fld('사업자번호', '124', '10자리를 채워 주세요', 'err', '150px'), "칸 밑에", "가장 흔하게 쓰고, 어느 칸의 오류인지 헷갈릴 일이 가장 적은 방식입니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--danger);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b style="display:block;margin-bottom:3px">2개 칸을 확인해 주세요</b>
                <span style="color:var(--accent);text-decoration:underline;display:block">사업자번호 — 10자리</span>
                <span style="color:var(--accent);text-decoration:underline;display:block">계좌 — 은행을 고르세요</span>
              </div>''',
     "맨 위 요약", "긴 폼에서 씁니다. 요약의 각 줄을 <b>누르면 해당 칸으로</b> 갈 수 있어야 합니다"),
    (fld('비밀번호', '••••••', '8자 이상 · 숫자 포함', '', '150px'), "미리 알려 주기", "<b>틀리기 전에</b> 입력 규칙을 보여 주는 편이 언제나 낫습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="검증이 꼭 갖출 것",
  code_lede="칸에 <code>aria-invalid</code>를 달아 값이 틀렸음을 알리고, <code>aria-describedby</code>로 <b>무엇이</b> 틀렸는지 적은 메시지를 연결합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"no"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"no"</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span>
       <span class="a">aria-invalid</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"no-err"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"no-err"</span>&gt;10자리를 채워 주세요&lt;/<span class="t">p</span>&gt;

<span class="c">// 떠날 때 한 번, 그 뒤로는 칠 때마다</span>
input.addEventListener(<span class="s">'blur'</span>, () =&gt; { touched = <span class="k">true</span>; check(); });
input.addEventListener(<span class="s">'input'</span>, () =&gt; { <span class="k">if</span> (touched) check(); });

<span class="c">// 제출하면 첫 오류 칸으로</span>
form.querySelector(<span class="s">'[aria-invalid="true"]'</span>)?.focus();''',
  keys=kbd([
    ("<code>aria-invalid=\"true\"</code>", "스크린 리더가 '잘못된 값'이라고 읽습니다. 값을 고치면 속성을 <b>지웁니다</b>"),
    ("<code>aria-describedby</code>", "메시지를 칸에 연결합니다. 칸에 포커스가 가면 메시지까지 함께 읽습니다"),
    ("제출 뒤 <kbd>Tab</kbd> 없이", "제출하면 첫 오류 칸으로 <b>포커스를 옮깁니다.</b> 옮기지 않으면 사용자가 어느 칸이 문제인지 직접 찾아야 합니다"),
    ("색 + 글자", "빨간 테두리에 <b>✕ 표시와 문장</b>을 함께 붙입니다. 색만으로는 알리지 않습니다"),
    ("<code>required</code>·<code>pattern</code>", "브라우저가 알아서 제출을 막아 주지만, 메시지가 <b>영어</b>로 나올 수 있습니다"),
    ("<code>novalidate</code>", "메시지를 직접 그리려면 이 속성으로 브라우저 기본 말풍선을 끕니다"),
  ]),
  backend=rows([
    ("서버가 최종 판단", "브라우저 검사는 사용자를 돕는 <b>안내</b>입니다. <code>curl</code> 명령 한 줄로 요청을 보내면 브라우저 검사를 모두 건너뛸 수 있으므로 서버가 최종 판단을 내립니다."),
    ("같은 규칙을 두 곳에 쓰지 않는다", "화면과 서버가 규칙을 따로 가지고 있으면 '화면은 통과했는데 서버가 거절'하는 일이 생깁니다. 규칙을 <b>한 곳에 적고</b> 화면과 서버가 함께 쓰게 합니다."),
    ("오류는 칸 이름과 함께", "<code>{\"field\":\"no\",\"message\":\"10자리여야 합니다\"}</code>처럼 보냅니다. 문장만 보내면 화면이 그 메시지를 어느 칸에 붙여야 할지 알 수 없습니다."),
    ("중복 확인은 경합한다", "'쓸 수 있는 번호'라고 확인한 뒤 저장하기 전까지 다른 사람이 그 번호를 먼저 등록할 수 있습니다. 그래서 <b>저장할 때 다시</b> 확인하고, DB에도 유일 제약을 겁니다."),
    ("확인 요청을 아낀다", "글자를 칠 때마다 서버에 물으면 요청이 한꺼번에 많이 몰립니다. <a href=\"search.html\">검색</a>에서처럼 디바운스를 겁니다."),
  ]),
  plat_lede="세 플랫폼은 오류 메시지를 <b>어디에 띄우는지</b>가 다릅니다.",
  plats=plats([
    ("웹", "Constraint Validation",
     fld('번호', '124', '10자리', 'err', '115px'),
     "브라우저 기본 말풍선이 있지만 <b>모양을 바꿀 수 없고</b> 잠시 뒤 사라집니다. 그래서 보통 기본 말풍선은 꺼 두고 메시지를 직접 그립니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 검증 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px"><div style="font-size:6px;border-bottom:1px solid var(--danger);padding-bottom:2px">124</div><div style="font-size:5px;color:var(--danger);margin-top:2px">10자리를 채워 주세요</div></div></div></div>''',
     "칸 밑에 빨간 글씨로 적는 것이 기본이고, 저장을 누른 뒤 <b>알림창</b>으로 알리는 앱도 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 검증 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-bottom:1px solid var(--danger);padding:4px"><div style="font-size:5px;color:var(--danger)">사업자번호</div><div style="font-size:6px">124</div></div>
                <div style="position:absolute;left:5px;top:48px;font-size:5px;color:var(--danger)">✕ 10자리를 채워 주세요</div></div></div>''',
     "칸 밑의 <b>서포팅 텍스트</b>가 그 자리에서 오류 문구로 바뀌고, 칸 이름도 빨간색으로 바뀝니다."),
  ]),
  plat_note="\"검증 붙여 주세요\"라는 요청은 화면과 서버, <b>두 군데에 검사를 만든다는 뜻</b>입니다. 화면 검사는 사용자를 돕기 위한 것이고 서버 검사는 잘못된 데이터를 막기 위한 것인데, 둘의 규칙이 어긋나면 '화면은 통과했는데 저장이 안 된다'는 민원이 들어옵니다. 그래서 규칙을 어디에 적어 둘지부터 정하는 편이 낫습니다.",
  siblings=siblings("validation"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
