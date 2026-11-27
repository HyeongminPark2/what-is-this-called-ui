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
  desc="언제 검사하고 어떻게 알릴지. 치는 중·떠날 때·제출할 때의 차이와, 오류 메시지를 칸에 붙이는 법.",
  lede="틀린 값을 알려 주는 일. 어려운 쪽은 '무엇이 틀렸나'가 아니라 <b>언제 말할 것인가</b>입니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>검사 시점을 바꿔 가며 칸에 글자를 쳐 보세요.<br>
          <b>칠 때마다</b>는 두 글자만 쳐도 빨개져 재촉당하는 느낌이 들고,
          <b>떠날 때</b>는 조용하되 늦지 않고, <b>제출할 때만</b>은 다 쓰고 나서야 한꺼번에 혼납니다.<br>
          제출을 눌러 보면 <b>첫 오류 칸으로 초점이 옮겨 가는</b> 것도 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "검증, 유효성 검사, 입력 확인"),
    ("영어", "validation, form validation, constraint validation"),
    ("같이 쓰는 말",
     "칠 때마다 검사하는 것이 <b>실시간 검증</b>(live·inline validation), "
     "보낼 때 한꺼번에 하는 것이 <b>제출 검증</b>입니다. "
     "브라우저가 <code>required</code>·<code>pattern</code>으로 해 주는 것을 "
     "<b>제약 검증 API</b>(Constraint Validation API)라 합니다."),
    ("자주 잘못 부름",
     "<b>오류 메시지</b> — <a href=\"../items/error.html\">오류 메시지</a>는 결과를 보여 주는 쪽, 검증은 <b>판단하는</b> 쪽입니다.<br>"
     "<b>인증</b>(authentication) — 사람이 맞는지 확인하는 일과 완전히 다릅니다. 영어로도 다른 단어입니다.<br>"
     "<b>폼</b> — <a href=\"form.html\">폼 설계</a>의 한 부분이지 폼 자체가 아닙니다."),
  ]),
  axes=ax("입력 검증"),
  oneline="검증의 원칙은 하나입니다 — <b>다 치기 전에 틀렸다고 하지 않는다.</b> 그리고 <b>한 번 틀린 뒤에는 고치는 즉시 풀어 준다.</b>",
  s4_title="상태", s4_hint="시점이 곧 상태다",
  states=states([
    (fld('사업자번호', '', '- 없이 10자리'), "치기 전", "<b>미리</b> 규칙을 알려 준다. 틀린 뒤보다 낫다"),
    (fld('사업자번호', '124'), "치는 중", "<b>아무 말도 하지 않는다.</b> 아직 다 안 쳤다"),
    (fld('사업자번호', '124', '10자리를 채워 주세요', 'err'), "떠날 때", "칸을 벗어나면 그때 말한다. 이게 기본값이다"),
    (fld('사업자번호', '1248100998', '확인됨', 'ok'), "고쳐짐", "한번 틀린 칸은 <b>고치는 즉시</b> 풀어 준다"),
    (fld('사업자번호', '1248100998', '확인하는 중…', 'warn'), "서버에 물어보는 중", "중복 확인 같은 것. <b>기다리는 티</b>를 낸다"),
    (fld('사업자번호', '1248100998', '이미 등록된 번호입니다', 'err'), "서버가 거절", "브라우저가 못 잡는 것. <b>같은 자리</b>에 같은 모양으로 붙인다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("치는 중엔 조용히", "on input: 안 함", "두 글자 쳤는데 빨개지면 <b>재촉</b>으로 느낀다"),
    ("떠날 때 검사", "on blur", "다 쳤다고 볼 수 있는 시점. 기본으로 삼는다"),
    ("메시지는 칸 밑", "같은 자리", "칸에서 멀면 <b>어느 칸 얘기인지</b> 모른다"),
    ("기계에게 알리기", "aria-invalid / describedby", "빨간 테두리는 <b>눈으로만</b> 보인다"),
    ("고치면 즉시 풀기", "re-validate on input", "한번 틀린 칸만. 이때는 칠 때마다 검사해도 안 거슬린다"),
    ("제출하면 초점 이동", "focus first error", "오류가 화면 밖에 있으면 <b>아무 일도 안 일어난 것</b>처럼 보인다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          규칙은 <b>비대칭</b>입니다 — 처음에는 <b>떠날 때</b> 검사하고,
          한번 틀린 칸은 <b>칠 때마다</b> 검사합니다.
          처음부터 칠 때마다 검사하면 다 치기 전에 빨개져 재촉당하는 느낌이 들고,
          고친 뒤에도 떠날 때까지 빨간 채로 두면 <b>고쳤는데도 틀렸다고 하는</b> 것처럼 보입니다.
          대부분의 폼 라이브러리가 이 두 단계를 기본값으로 둡니다.</p>''',
  do=ul([
    "<b>형식이 정해진</b> 값 — 번호 자릿수, 날짜, 전자우편",
    "<b>서버만 아는</b> 조건 — 중복, 잔액, 권한",
    "되돌리기 어려운 동작 직전",
  ]),
  dont=ul([
    "치는 도중에 빨갛게 — <b>다 치기 전에 틀렸다고 하지 않는다</b>",
    "'올바른 값을 입력하세요' — <b>무엇이 어떻게</b> 틀렸는지 적는다",
    "색만으로 알리기 — 테두리 빨강만으로는 못 보는 사람이 있다",
    "브라우저 검사만 믿기 — <b>서버가 다시</b> 검사해야 한다",
  ]),
  instead='보여 주기만 하면 <a href="../items/error.html">오류 메시지</a>, 확인만 받으면 <a href="../items/dialog.html">다이얼로그</a>, 결과를 알리면 <a href="../items/toast.html">토스트</a>.',
  cases=cases([
    (fld('사업자번호', '124', '10자리를 채워 주세요', 'err', '150px'), "칸 밑에", "가장 흔하고 가장 안전하다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--danger);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b style="display:block;margin-bottom:3px">2개 칸을 확인해 주세요</b>
                <span style="color:var(--accent);text-decoration:underline;display:block">사업자번호 — 10자리</span>
                <span style="color:var(--accent);text-decoration:underline;display:block">계좌 — 은행을 고르세요</span>
              </div>''',
     "맨 위 요약", "긴 폼에서. <b>눌러서 그 칸으로</b> 갈 수 있어야 한다"),
    (fld('비밀번호', '••••••', '8자 이상 · 숫자 포함', '', '150px'), "미리 알려 주기", "<b>틀리기 전에</b> 규칙을 보여 주는 쪽이 늘 낫다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 검증의 계약서",
  code_lede="<code>aria-invalid</code>로 틀렸음을, <code>aria-describedby</code>로 <b>무엇이</b> 틀렸는지를 칸에 붙입니다.",
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
    ("<code>aria-invalid=\"true\"</code>", "'잘못된 값'으로 읽힌다. 고쳐지면 <b>지운다</b>"),
    ("<code>aria-describedby</code>", "메시지를 칸에 묶는다. 칸에 초점이 가면 메시지까지 읽힌다"),
    ("제출 뒤 <kbd>Tab</kbd> 없이", "첫 오류 칸에 <b>초점을 옮긴다.</b> 안 그러면 어디가 문제인지 찾아 헤맨다"),
    ("색 + 글자", "빨간 테두리에 <b>✕ 와 문장</b>을 함께. 색만으로는 안 된다"),
    ("<code>required</code>·<code>pattern</code>", "브라우저가 알아서 막아 준다. 다만 메시지가 <b>영어</b>일 수 있다"),
    ("<code>novalidate</code>", "직접 메시지를 그리려면 브라우저 기본 말풍선을 끈다"),
  ]),
  backend=rows([
    ("서버가 최종 판단", "브라우저 검사는 <b>안내</b>일 뿐입니다. <code>curl</code> 한 줄이면 다 건너뜁니다."),
    ("같은 규칙을 두 곳에 쓰지 않는다", "앞뒤가 따로 놀면 '화면은 통과했는데 서버가 거절'이 됩니다. 규칙을 <b>한 곳에 적고</b> 양쪽이 쓰게 합니다."),
    ("오류는 칸 이름과 함께", "<code>{\"field\":\"no\",\"message\":\"10자리여야 합니다\"}</code>. 문장만 보내면 어느 칸에 붙일지 모릅니다."),
    ("중복 확인은 경합한다", "'쓸 수 있는 번호'를 확인한 뒤 저장 사이에 남이 가져갈 수 있습니다. <b>저장할 때 다시</b> 확인하고 DB 에 유일 제약을 겁니다."),
    ("확인 요청을 아낀다", "칠 때마다 서버에 물으면 요청이 쏟아집니다. <a href=\"search.html\">검색</a>과 같은 디바운스를 겁니다."),
  ]),
  plat_lede="메시지를 <b>어디에 띄우냐</b>가 갈립니다.",
  plats=plats([
    ("웹", "Constraint Validation",
     fld('번호', '124', '10자리', 'err', '115px'),
     "브라우저 기본 말풍선이 있지만 <b>모양을 못 바꾸고</b> 사라집니다. 보통 꺼 두고 직접 그립니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 검증 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px"><div style="font-size:6px;border-bottom:1px solid var(--danger);padding-bottom:2px">124</div><div style="font-size:5px;color:var(--danger);margin-top:2px">10자리를 채워 주세요</div></div></div></div>''',
     "칸 밑 빨간 글씨가 기본입니다. 저장을 누르면 <b>알림창</b>으로 알리는 앱도 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 검증 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-bottom:1px solid var(--danger);padding:4px"><div style="font-size:5px;color:var(--danger)">사업자번호</div><div style="font-size:6px">124</div></div>
                <div style="position:absolute;left:5px;top:48px;font-size:5px;color:var(--danger)">✕ 10자리를 채워 주세요</div></div></div>''',
     "<b>서포팅 텍스트</b>가 그 자리에서 오류 문구로 바뀌고 칸 이름까지 빨갛게 됩니다."),
  ]),
  plat_note="\"검증 붙여 주세요\"는 <b>앞뒤 두 벌</b>을 뜻합니다. 화면 검사는 친절함이고 서버 검사는 방어인데, 둘의 규칙이 어긋나면 '화면은 통과했는데 저장이 안 되는' 민원이 납니다. 규칙을 어디에 적어 둘지를 먼저 정하는 편이 낫습니다.",
  siblings=siblings("validation"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
