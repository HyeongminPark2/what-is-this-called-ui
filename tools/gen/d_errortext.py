# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇이 — 정산을 저장하지 못했습니다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">왜 — 다른 사람이 2분 전에 고쳤습니다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">어떻게 — 바뀐 내용을 보고 다시 저장해 주세요</div>
                  <div class="pin-out" data-pin="4" style="max-width:220px">''' + btn('바뀐 내용 보기') + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">적은 내용은 남아 있다고 말해 준다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">ERR_CONNECTION_TIMED_OUT — 우리만 읽는 글자</div>
                </div>
              </div>'''

D = dict(
  slug="errortext", ko="오류 문구", en="Error message",
  desc="무엇이 안 됐고 왜 그런지, 그리고 어떻게 하면 되는지. 셋 중 마지막이 가장 자주 빠진다.",
  lede="오류 문구는 <b>무엇이 · 왜 · 어떻게</b> 세 가지입니다. 가장 중요한 <b>어떻게</b>가 가장 자주 빠집니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>상황을 바꿔 가며 <b>흔한 문구</b>와 <b>고친 문구</b>를 견줘 보세요.
          아래에 고친 문구를 셋으로 뜯어 놓았습니다.<br>
          <b>사과를 길게 넣기</b>를 켜면 문장이 길어지는데 <b>할 수 있는 일은 하나도 안 늘어납니다</b> —
          그 차이가 글자 수로 나옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오류 문구, 에러 메시지, 실패 안내"),
    ("영어", "error message, error copy, inline error"),
    ("같이 쓰는 말",
     "칸 밑에 붙는 것이 <b>인라인 에러</b>, 화면 전체를 덮는 것이 <b>에러 상태</b>·<b>에러 화면</b>입니다. "
     "사람이 읽는 문구와 따로 두는 기계용 글자를 <b>에러 코드</b>라 하고, "
     "문제를 미리 막는 쪽을 <b>오류 예방</b>(error prevention)이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>에러 상태</b> — <a href=\"../items/error.html\">에러 상태</a>는 <b>화면의 모습</b>이고, 이쪽은 <b>거기 적는 말</b>입니다.<br>"
     "<b>검증</b> — <a href=\"validation.html\">입력 검증</a>은 판단하는 쪽, 문구는 <b>전하는</b> 쪽입니다.<br>"
     "<b>경고</b> — 경고는 아직 안 일어난 일을 알리고, 오류는 <b>이미 안 된 일</b>을 말합니다."),
  ]),
  axes=ax("오류 문구"),
  oneline="<b>사용자가 지금 할 수 있는 일</b>을 적으세요. 그게 없으면 문구가 아니라 통보입니다.",
  s4_title="상황별로", s4_hint="할 수 있는 일이 있나",
  states=states([
    (ba('네트워크 오류가 발생했습니다. (ERR_CONNECTION_TIMED_OUT)',
        '정산 내역을 불러오지 못했습니다. 연결을 확인하고 다시 시도해 주세요.',
        '코드는 우리만 읽는다'),
     "연결이 끊김", "<b>다시 시도</b> 버튼을 함께"),
    (ba('유효하지 않은 값입니다.',
        '사업자번호는 - 없이 10자리를 적어 주세요.',
        '무엇이 어떻게 틀렸는지 적는다'),
     "값이 틀림", "<a href=\"validation.html\">검증</a>은 <b>칸 밑에</b> 붙인다"),
    (ba('접근이 거부되었습니다. (403)',
        '이 정산은 가맹점 관리자만 볼 수 있습니다.',
        '왜 막혔는지, 누구에게 말해야 하는지'),
     "권한이 없음", "<b>없는 것</b>처럼 보이게 두지 않는다"),
    (ba('알 수 없는 오류가 발생했습니다.',
        '저희 쪽 문제로 저장하지 못했습니다. 적으신 내용은 남아 있습니다.',
        '내용이 날아갔는지를 먼저 말해 준다'),
     "서버가 터짐", "우리 잘못일 때만 <b>짧게 사과</b>한다"),
    (ba('저장에 실패했습니다.',
        '다른 사람이 2분 전에 이 정산을 고쳤습니다. 바뀐 내용을 보고 다시 저장할지 정해 주세요.',
        '왜인지 모르면 다시 눌러도 또 실패한다'),
     "남이 먼저 고침", "가장 설명이 필요한 경우"),
    (one('이용에 불편을 드려 대단히 죄송합니다. 보다 나은 서비스를 위해 노력하겠습니다. 오류가 발생했습니다.',
         "사과만 긴 문구", False, "길어졌지만 할 수 있는 일은 그대로"),
     "사과가 긴 것", "<b>사과는 할 일을 대신하지 못한다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이", "안 된 일", "'정산을 저장하지 못했습니다'. <b>명사가 아니라 문장</b>으로"),
    ("왜", "짐작 가능한 이유", "모르면 <b>억지로 지어내지</b> 않는다"),
    ("어떻게", "지금 할 수 있는 일", "<b>가장 중요하고 가장 자주 빠진다</b>"),
    ("버튼", "다시 시도 · 바꾼 내용 보기", "할 일이 한 번의 누름이면 <b>버튼으로</b>"),
    ("안심", "내용은 남아 있습니다", "적은 것이 날아갔는지부터 궁금하다"),
    ("코드", "우리만 읽는 글자", "보여 주려면 <b>작게, 복사할 수 있게</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>사과는 자주 할수록 값이 떨어집니다.</b>
          '불편을 드려 죄송합니다'가 모든 오류에 붙어 있으면
          사람들은 그 줄을 건너뛰고 읽습니다.
          정말 <b>우리 잘못</b>일 때(서버가 터짐, 데이터를 잃음)만
          <b>짧게 한 번</b> 적고, 나머지는 할 수 있는 일로 채우는 쪽이 낫습니다.
          사용자가 잘못 적었을 때는 사과할 일도 아닙니다 —
          <b>'틀렸다'보다 '이렇게 적어 주세요'</b>로 쓰면 탓하는 느낌도 사라집니다.</p>''',
  do=ul([
    "<b>지금 할 수 있는 일</b>을 적기",
    "값이 틀렸으면 <b>어떻게 적어야 하는지</b>까지",
    "우리 잘못이면 <b>짧게 한 번</b> 사과하고 넘어가기",
  ]),
  dont=ul([
    "코드만 보여 주기 — <code>ERR_...</code>는 우리만 읽는다",
    "‘알 수 없는 오류’ — <b>우리도 모른다</b>는 말일 뿐이다",
    "모든 오류에 긴 사과 — <b>건너뛰고 읽게</b> 된다",
    "‘잘못 입력하셨습니다’ — <b>탓하는 말</b> 대신 고치는 법을 적는다",
  ]),
  instead='화면 전체가 실패면 <a href="../items/error.html">에러 상태</a>, 칸 하나면 <a href="validation.html">입력 검증</a>, 지나가도 되면 <a href="../items/toast.html">토스트</a>.',
  cases=cases([
    (one('사업자번호는 - 없이 10자리를 적어 주세요', "칸 밑에", True, "<a href=\"validation.html\">검증</a>과 같은 자리"), "인라인", "가장 가까운 자리에 붙인다"),
    (one('목록을 불러오지 못했습니다<br><span style="color:var(--fg-muted);font-size:9px">연결을 확인해 주세요</span><br>' + btn('다시 시도'),
         "화면 전체", True, "버튼까지 한 벌"), "화면 가득", "<a href=\"../items/error.html\">에러 상태</a>로 이어진다"),
    (one('저장하지 못했습니다 · <span style="color:var(--accent)">다시 시도</span>', "지나가는 알림", True, "짧게, 되돌릴 길과 함께"),
     "토스트", "급하지 않은 실패"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 문구의 계약서",
  code_lede="오류는 <b>끊고 읽어도 되는</b> 급한 말입니다.",
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
  keys=kbd([
    ("<code>role=\"alert\"</code>", "읽던 것을 <b>끊고</b> 말한다. 오류는 끊어도 될 만큼 급하다"),
    ("<code>aria-describedby</code>", "칸과 문구를 묶는다. 안 묶으면 <b>칸 이름만</b> 읽힌다"),
    ("초점을 옮긴다", "제출 뒤에는 <b>첫 틀린 칸</b>으로. 안 그러면 어디가 문제인지 못 찾는다"),
    ("색만으로 하지 않는다", "빨간 테두리에 <b>✕ 와 문장</b>을 함께"),
    ("코드는 복사할 수 있게", "문의할 때 쓴다. <b>작게, 선택 가능하게</b>"),
    ("<code>alert</code>를 남발하지 않는다", "안 급한 것까지 끊고 읽으면 <b>전부 무시하게</b> 된다"),
  ]),
  backend=rows([
    ("사람용과 기계용을 따로", "<code>{\"code\":\"CONFLICT\",\"message\":\"…\"}</code>. <b>코드로 분기</b>하고 문구는 화면이 고릅니다."),
    ("문구를 서버가 다 쓰지 않는다", "서버 문구를 그대로 띄우면 <b>말투가 섞이고</b> 번역도 안 됩니다."),
    ("어느 칸인지 함께", "<code>{\"field\":\"no\"}</code>가 있어야 그 칸에 붙일 수 있습니다."),
    ("5xx 와 4xx 를 가른다", "우리 잘못(5xx)에만 사과합니다. <b>사용자 잘못에 사과하면</b> 이상합니다."),
    ("로그에는 자세히", "사용자에게는 짧게, 로그에는 <b>추적할 수 있을 만큼</b>. 둘을 같은 글로 쓰지 않습니다."),
  ]),
  plat_lede="<b>어디에 띄우느냐</b>가 갈립니다.",
  plats=plats([
    ("웹", "인라인 · 배너 · 토스트",
     one('- 없이 10자리를 적어 주세요', "", True, "", "110px"),
     "칸 밑, 화면 위 배너, 지나가는 토스트. <b>급한 정도에 따라</b> 고릅니다."),
    ("iOS", "Alert",
     '''              <div class="phone" role="img" aria-label="iOS 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:7px;right:7px;top:28px;background:var(--surface);border-radius:6px;border:1px solid var(--line);padding:4px;text-align:center;font-size:5px">저장하지 못했습니다<br><span style="color:var(--fg-muted)">잠시 뒤 다시 시도해 주세요</span></div></div></div>''',
     "알림창을 띄우는 일이 많습니다. <b>끊고 말하는</b> 방식이라 자주 쓰면 밉습니다."),
    ("안드로이드", "스낵바 · 인라인",
     '''              <div class="phone" role="img" aria-label="안드로이드 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--ink-900);color:#fff;border-radius:4px;padding:3px;font-size:5px;display:flex"><span style="flex:1">저장하지 못했습니다</span><span style="color:#9ec1ff">다시</span></div></div></div>''',
     "<b>스낵바 + 다시 시도</b>가 규격입니다. 칸 오류는 칸 밑에 둡니다."),
  ]),
  plat_note="오류 문구는 <b>개발자가 급할 때 쓰는 말</b>이 그대로 남는 자리입니다 — '처리 중 오류가 발생했습니다'는 대개 임시로 적어 둔 것이 배포까지 간 것입니다. 기능을 만들 때 <b>'이 실패는 사용자가 뭘 하면 되나'</b>를 한 줄 적어 두면, 나중에 문구를 모아 고치는 일이 사라집니다.",
  siblings=siblings("errortext"),
  related='''        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="../items/live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
