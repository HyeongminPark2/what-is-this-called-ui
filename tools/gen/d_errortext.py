# -*- coding: utf-8 -*-
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇이 — 정산을 저장하지 못했습니다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">왜 — 다른 사람이 2분 전에 고쳤습니다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">어떻게 — 바뀐 내용을 보고 다시 저장해 주세요</div>
                  <div class="pin-out" data-pin="4" style="max-width:220px">''' + btn('바뀐 내용 보기') + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">적은 내용이 남아 있다고 알려 줌</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">ERR_CONNECTION_TIMED_OUT은 개발자만 읽는 글자</div>
                </div>
              </div>'''

D = dict(
  slug="errortext", ko="오류 문구", en="Error message",
  desc="오류 문구에 무엇이 안 됐고 왜 그런지, 어떻게 하면 되는지를 적는 방법을 다룹니다. 셋 가운데 마지막 것이 가장 자주 빠집니다.",
  lede="오류 문구에는 <b>무엇이 · 왜 · 어떻게</b> 세 가지를 적습니다. 그 가운데 사용자가 다음에 할 일을 알려 주는 <b>어떻게</b>가 가장 중요한데도 가장 자주 빠집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>상황을 바꿔 가며 <b>흔한 문구</b>와 <b>고친 문구</b>를 견줘 보세요.
          아래에는 고친 문구를 무엇이 · 왜 · 어떻게로 나눠 놓았습니다.<br>
          <b>사과를 길게 넣기</b>를 켜면 문장은 길어지지만 <b>사용자가 할 수 있는 일은 하나도 늘지 않습니다</b>.
          늘어난 길이는 글자 수로 보여 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오류 문구, 에러 메시지, 실패 안내"),
    ("영어", "error message, error copy, inline error"),
    ("같이 쓰는 말",
     "입력 칸 밑에 붙는 오류는 <b>인라인 에러</b>, 화면 전체를 덮는 오류는 <b>에러 상태</b>·<b>에러 화면</b>이라고 합니다. "
     "사람이 읽는 문구와 따로 두는 기계용 글자는 <b>에러 코드</b>라고 하고, "
     "오류가 생기지 않게 미리 막는 일은 <b>오류 예방</b>(error prevention)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>에러 상태</b> — <a href=\"../items/error.html\">에러 상태</a>는 오류가 났을 때의 <b>화면 모습</b>이고, 오류 문구는 <b>그 화면에 적는 말</b>입니다.<br>"
     "<b>검증</b> — <a href=\"validation.html\">입력 검증</a>은 값이 맞는지 판단하는 일이고, 오류 문구는 판단 결과를 사용자에게 <b>전하는</b> 일입니다.<br>"
     "<b>경고</b> — 경고는 아직 일어나지 않은 일을 미리 알리고, 오류는 <b>이미 실패한 일</b>을 알립니다."),
  ]),
  s4_title="오류 상황별 문구 비교", s4_hint="사용자가 할 수 있는 일을 알려 주는지",
  states=states([
    (ba('네트워크 오류가 발생했습니다. (ERR_CONNECTION_TIMED_OUT)',
        '정산 내역을 불러오지 못했습니다. 연결을 확인하고 다시 시도해 주세요.',
        '코드는 만드는 쪽만 읽음'),
     "연결이 끊겼을 때", "<b>다시 시도</b> 버튼을 함께 둡니다"),
    (ba('유효하지 않은 값입니다.',
        '사업자번호는 - 없이 10자리를 적어 주세요.',
        '무엇이 어떻게 틀렸는지 적음'),
     "입력한 값이 틀렸을 때", "<a href=\"validation.html\">검증</a> 문구는 틀린 <b>칸 밑에</b> 붙입니다"),
    (ba('접근이 거부되었습니다. (403)',
        '이 정산은 가맹점 관리자만 볼 수 있습니다.',
        '왜 막혔고 누구에게 말해야 하는지 적음'),
     "볼 권한이 없을 때", "볼 권한이 없을 뿐인데 내용이 <b>없는 것</b>처럼 보이게 두지 않습니다"),
    (ba('알 수 없는 오류가 발생했습니다.',
        '저희 쪽 문제로 저장하지 못했습니다. 적으신 내용은 남아 있습니다.',
        '내용이 사라졌는지부터 알려 줌'),
     "서버 쪽에서 실패했을 때", "우리 쪽 잘못일 때만 <b>짧게 사과</b>합니다"),
    (ba('저장에 실패했습니다.',
        '다른 사람이 2분 전에 이 정산을 고쳤습니다. 바뀐 내용을 보고 다시 저장할지 정해 주세요.',
        '이유를 모르면 다시 눌러도 또 실패함'),
     "다른 사람이 먼저 고쳤을 때", "왜 실패했는지 설명이 가장 많이 필요한 경우입니다"),
    (one('이용에 불편을 드려 대단히 죄송합니다. 보다 나은 서비스를 위해 노력하겠습니다. 오류가 발생했습니다.',
         "사과만 긴 문구", False, "길어졌지만 할 수 있는 일은 그대로"),
     "사과만 길게 적은 문구", "사과를 길게 적어도 <b>할 일을 알려 주지는 못합니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이", "안 된 일", "'정산을 저장하지 못했습니다'처럼 <b>명사로 끝내지 않고 문장으로</b> 적습니다"),
    ("왜", "짐작 가능한 이유", "이유를 모르면 <b>억지로 지어내지</b> 않습니다"),
    ("어떻게", "지금 할 수 있는 일", "<b>가장 중요한데도 가장 자주 빠지는</b> 부분입니다"),
    ("버튼", "다시 시도 · 바꾼 내용 보기", "할 일이 한 번 누르면 끝나는 동작이면 <b>버튼으로</b> 줍니다"),
    ("안심", "내용은 남아 있습니다", "사용자는 적어 둔 내용이 사라졌는지부터 궁금해하므로 그것을 먼저 알려 줍니다"),
    ("코드", "우리만 읽는 글자", "코드를 보여 줄 때는 <b>작게, 복사할 수 있게</b> 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>사과 문장을 모든 오류에 붙이면 사용자가 읽지 않게 됩니다.</b>
          '불편을 드려 죄송합니다'가 오류마다 똑같이 붙어 있으면
          사람들은 그 줄을 건너뛰고 읽기 때문입니다.
          서버가 터졌거나 데이터를 잃었을 때처럼 정말 <b>우리 잘못</b>일 때만
          <b>짧게 한 번</b> 사과하고, 나머지 자리는 사용자가 할 수 있는 일로 채우는 편이 낫습니다.
          사용자가 값을 잘못 적었을 때는 사과할 필요가 없습니다. 이때는
          <b>'틀렸다'보다 '이렇게 적어 주세요'</b>로 쓰면 사용자를 탓하는 느낌도 들지 않습니다.</p>''',
  do=ul([
    "<b>지금 할 수 있는 일</b>을 적기",
    "값이 틀렸으면 <b>어떻게 적어야 하는지</b>까지 적기",
    "우리 잘못이면 <b>짧게 한 번</b> 사과하고 넘어가기",
  ]),
  do_title="오류 문구를 쓸 때 지킬 것", dont_title="오류 문구에서 피할 것",
  instead_title="오류가 난 자리에 따라 함께 볼 항목",
  dont=ul([
    "오류 코드만 보여 줄 때. <code>ERR_...</code>는 개발자만 알아볼 수 있습니다",
    "‘알 수 없는 오류’라고 적을 때. 사용자에게는 <b>만든 쪽도 원인을 모른다</b>는 말로만 들립니다",
    "모든 오류에 긴 사과를 붙일 때. 사용자가 그 줄을 <b>건너뛰고 읽게</b> 됩니다",
    "‘잘못 입력하셨습니다’라고 적을 때. 사용자를 <b>탓하는 말</b> 대신 고치는 방법을 적습니다",
  ]),
  instead='화면 전체를 불러오지 못했으면 <a href="../items/error.html">에러 상태</a>를, 입력 칸 하나가 틀렸으면 <a href="validation.html">입력 검증</a>을 봅니다. 잠깐 알리고 지나가도 되는 실패라면 <a href="../items/toast.html">토스트</a>를 씁니다.',
  cases=cases([
    (one('사업자번호는 - 없이 10자리를 적어 주세요', "칸 밑에", True, "<a href=\"validation.html\">검증</a>과 같은 자리"), "칸 밑에 붙이는 인라인 오류", "틀린 칸에서 가장 가까운 자리에 붙입니다"),
    (one('목록을 불러오지 못했습니다<br><span style="color:var(--fg-muted);font-size:9px">연결을 확인해 주세요</span><br>' + btn('다시 시도'),
         "화면 전체", True, "버튼까지 함께"), "화면 전체를 바꾸는 오류", "화면 전체가 <a href=\"../items/error.html\">에러 상태</a>로 바뀌는 경우입니다"),
    (one('저장하지 못했습니다 · <span style="color:var(--accent)">다시 시도</span>', "지나가는 알림", True, "짧게, 다시 시도 버튼과 함께"),
     "토스트로 잠깐 알리는 오류", "급하지 않은 실패를 잠깐 알릴 때 씁니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="오류는 스크린 리더가 읽던 내용을 <b>끊고 바로 읽어도 될 만큼</b> 급한 정보입니다.",
  code='''<span class="c">&lt;!-- 칸 하나의 오류 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"no"</span> <span class="a">aria-invalid</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"no-err"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"no-err"</span>&gt;- 없이 10자리를 적어 주세요&lt;/<span class="t">p</span>&gt;

<span class="c">&lt;!-- 화면 전체의 오류 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;
  &lt;<span class="t">h2</span>&gt;목록을 불러오지 못했습니다&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span>&gt;연결을 확인하고 다시 시도해 주세요.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">button</span>&gt;다시 시도&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"code"</span>&gt;오류 코드 E-4821&lt;/<span class="t">p</span>&gt;   <span class="c">&lt;!-- 문의할 때 쓰는 번호 --&gt;</span>
&lt;/<span class="t">div</span>&gt;''',
  keys_heads="<th>지킬 규칙과 마크업</th><th>지키는 방법과 이유</th>",
  keys=kbd([
    ("<code>role=\"alert\"</code>", "스크린 리더가 읽던 내용을 <b>끊고</b> 바로 읽어 줍니다. 오류는 그렇게 끊어도 될 만큼 급한 정보입니다"),
    ("<code>aria-describedby</code>", "입력 칸과 오류 문구를 연결합니다. 연결하지 않으면 스크린 리더가 <b>칸 이름만</b> 읽어 줍니다"),
    ("제출한 뒤 초점 옮기기", "제출한 뒤에는 초점을 <b>첫 번째 틀린 칸</b>으로 옮깁니다. 그러지 않으면 사용자가 어디가 문제인지 찾기 어렵습니다"),
    ("색만으로 알리지 않기", "빨간 테두리만 두지 않고 <b>✕ 표시와 문장</b>을 함께 적습니다"),
    ("오류 코드는 복사할 수 있게 두기", "오류 코드는 사용자가 문의할 때 씁니다. <b>작게 적되 선택해서 복사할 수 있게</b> 둡니다"),
    ("<code>alert</code>를 남발하지 않기", "급하지 않은 내용까지 끊고 읽어 주면, 사용자가 결국 <b>알림을 전부 무시하게</b> 됩니다"),
  ]),
  backend=rows([
    ("사람이 읽는 문구와 기계용 코드 나누기", "<code>{\"code\":\"CONFLICT\",\"message\":\"…\"}</code>처럼 코드와 메시지를 나눠 보냅니다. 화면은 <b>코드로 분기</b>하고, 보여 줄 문구는 화면 쪽에서 고릅니다."),
    ("문구를 서버가 다 쓰지 않기", "서버가 보낸 문구를 그대로 띄우면 화면 문구와 <b>말투가 섞이고</b>, 다른 언어로 번역하기도 어렵습니다."),
    ("어느 칸의 오류인지 함께 보내기", "<code>{\"field\":\"no\"}</code>처럼 어느 칸의 오류인지 함께 보내야 화면이 그 칸 밑에 문구를 붙일 수 있습니다."),
    ("5xx와 4xx 구별하기", "서버 쪽 잘못인 5xx 오류에만 사과합니다. 4xx처럼 <b>사용자 쪽 잘못에 사과하면</b> 어색합니다."),
    ("로그에는 자세히 남기기", "사용자에게는 짧게 보여 주고, 로그에는 원인을 <b>추적할 수 있을 만큼</b> 자세히 남깁니다. 두 가지를 같은 글로 쓰지 않습니다."),
  ]),
  plat_lede="플랫폼마다 오류를 <b>어디에 띄우는지</b>가 다릅니다.",
  plats=plats([
    ("웹", "인라인 · 배너 · 토스트",
     one('- 없이 10자리를 적어 주세요', "", True, "", "110px"),
     "칸 밑 문구, 화면 위 배너, 잠깐 떴다 사라지는 토스트 가운데 <b>급한 정도에 따라</b> 고릅니다."),
    ("iOS", "Alert",
     '''              <div class="phone" role="img" aria-label="iOS 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:7px;right:7px;top:28px;background:var(--surface);border-radius:6px;border:1px solid var(--line);padding:4px;text-align:center;font-size:5px">저장하지 못했습니다<br><span style="color:var(--fg-muted)">잠시 뒤 다시 시도해 주세요</span></div></div></div>''',
     "오류를 알림창으로 띄우는 일이 많습니다. 하던 일을 <b>끊고 알리는</b> 방식이라 너무 자주 띄우면 사용자가 성가셔합니다."),
    ("안드로이드", "스낵바 · 인라인",
     '''              <div class="phone" role="img" aria-label="안드로이드 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--ink-900);color:#fff;border-radius:4px;padding:3px;font-size:5px;display:flex"><span style="flex:1">저장하지 못했습니다</span><span style="color:#9ec1ff">다시</span></div></div></div>''',
     "<b>스낵바에 다시 시도 버튼</b>을 붙이는 것이 표준 방식입니다. 입력 칸의 오류는 칸 밑에 둡니다."),
  ]),
  plat_note="오류 문구에는 <b>개발자가 급하게 적어 둔 말</b>이 그대로 남기 쉽습니다. '처리 중 오류가 발생했습니다' 같은 문구는 대개 개발 중에 임시로 적은 것이 그대로 배포된 경우입니다. 기능을 만들 때 <b>'이 실패가 나면 사용자가 무엇을 하면 되나'</b>를 한 줄 적어 두면, 나중에 문구를 모아 다시 고칠 일이 없습니다.",
  siblings=siblings("errortext"),
  related='''        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="../items/live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
