# -*- coding: utf-8 -*-
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def scr(inner, w="152px", foot=""):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<div style="padding:5px 8px;border-bottom:1px solid var(--line);background:var(--bg);font-size:9px;font-weight:700">로그인</div>'
            '<div style="padding:7px 8px;display:grid;gap:5px">' + inner + '</div>'
            + ('<div style="padding:6px 8px;border-top:1px solid var(--line);font-size:9px;color:var(--fg-muted)">' + foot + '</div>' if foot else '')
            + '</div>')

def fld(lab, val="", err="", w="100%"):
    return ('<div style="display:grid;gap:2px"><span style="font-size:8.5px;color:var(--fg-muted)">' + lab + '</span>'
            '<div style="border:1px solid ' + ('var(--danger)' if err else 'var(--line)') + ';border-radius:4px;'
            'background:var(--surface);padding:3px 6px;font-size:9.5px">' + (val or '&nbsp;') + '</div>'
            + ('<span style="font-size:8px;color:var(--danger)">' + err + '</span>' if err else '') + '</div>')

BTN = '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">로그인</span>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">autocomplete="username" · "current-password"</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + fld('비밀번호', '••••••').strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">'아이디 또는 비밀번호'로 묶어 어느 쪽이 틀렸는지 숨김</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">'비밀번호를 잊으셨나요?'는 늘 같은 자리에 둠</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">로그인 상태 유지는 오래 가는 쿠키로 처리</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자동완성을 끄면 더 쉬운 비밀번호를 쓰게 됨</div>
                </div>
              </div>'''

D = dict(
  slug="login", ko="로그인", en="Sign in",
  desc="내가 누구인지 증명하는 화면입니다. 오류 문구로 계정이 있는지 흘리지 않는 법, 자동완성, 비밀번호를 잊었을 때 되찾는 길까지 다룹니다.",
  lede="로그인은 누구나 한 번쯤 만들어 본 화면이지만, 오류 문구나 응답 시간 같은 사소한 곳으로 <b>계정 정보가 가장 자주 새어 나가는</b> 화면이기도 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>로그인에 성공하는 값은 <b>hong / 1234</b>입니다. 일부러 틀린 값을 넣고 눌러 보세요.<br>
          <b>오류를 자세히 말하기</b>를 켜면 '없는 아이디'와 '비밀번호가 틀렸습니다'를 나눠서 보여 줍니다.
          친절해 보이지만, 어떤 아이디가 가입되어 있는지 <b>밖에 알려 주는</b> 셈입니다.<br>
          <b>자동완성 끄기</b>를 켜면 비밀번호 관리자가 칸을 채우지 못합니다. 보안을 위해 껐는데도
          사용자는 직접 외워 칠 수 있는 <b>더 쉬운 비밀번호</b>를 쓰게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "로그인, 사인인, 인증"),
    ("영어", "sign in, log in, authentication"),
    ("같이 쓰는 말",
     "누구인지 확인하는 일을 <b>인증</b>(authentication), 무엇을 할 수 있는지 정하는 일을 <b>인가</b>(authorization)라고 합니다. "
     "둘 다 auth로 줄여 쓰기 때문에 자주 섞입니다. "
     "로그인한 상태를 이어 가는 것을 <b>세션</b>이라 하고, 그 상태를 증명하는 값으로 <b>쿠키</b>나 <b>토큰</b>을 씁니다. "
     "아이디만 먼저 받는 방식은 <b>단계 로그인</b>(identifier-first)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>가입</b> — 계정을 만드는 화면과 이미 있는 계정으로 들어오는 화면은 <b>서로 다른 화면</b>입니다. 한 화면에 섞어 두면 어느 쪽 목적도 분명하게 드러나지 않습니다.<br>"
     "<b>인증</b> — 휴대폰 인증 같은 본인 확인은 로그인과 다른 절차입니다.<br>"
     "<b>로그인 유지</b> — '자동 로그인'과 '로그인 상태 유지'가 섞여 쓰이기 때문에, <b>무엇을 얼마나 오래</b> 유지하는지 적어 두는 편이 낫습니다."),
  ]),
  do_title="로그인 화면을 만들 때 지킬 것",
  dont_title="로그인 화면을 이렇게 만들면 안 되는 경우",
  instead_title="로그인 화면에서 다루지 않는 일",
  s4_title="로그인 화면의 상태", s4_hint="여섯 가지 모두 만들어야 하는 상태",
  states=states([
    (scr(fld('아이디') + fld('비밀번호') + BTN, "152px", "비밀번호를 잊으셨나요?"), "아무것도 입력하지 않았을 때", "<b>비밀번호 찾기</b> 링크는 처음부터 보여야 합니다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') + BTN), "자동완성으로 채워졌을 때", "<b>자동완성</b>이 칸을 채워 준 모습입니다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••', '아이디 또는 비밀번호가 올바르지 않습니다') + BTN),
     "틀렸을 때 바르게 알린 문구 ✓", "아이디와 비밀번호 가운데 <b>무엇이</b> 틀렸는지 말하지 않습니다"),
    (scr(fld('아이디', 'kim', '없는 아이디입니다') + fld('비밀번호', '••••') + BTN),
     "틀렸을 때 계정을 드러낸 문구 ✕", "그 아이디로 된 <b>계정이 없다고 알려 준</b> 셈입니다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') +
         '<span style="display:block;text-align:center;background:var(--fg-muted);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">확인 중…</span>'),
     "서버의 확인을 기다리는 중", "버튼을 잠가서 <b>두 번 눌리는 일</b>을 막습니다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••', '5회 틀렸습니다 · 1분 뒤 다시') + BTN),
     "여러 번 틀려서 잠겼을 때", "로그인을 잠시 <b>잠그되, 왜 잠겼는지</b> 알려 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자동완성 힌트", "autocomplete", "<code>username</code>·<code>current-password</code>를 적습니다. <b>비밀번호 관리자는 이 값을 보고</b> 칸을 채웁니다"),
    ("비밀번호 칸", "type=\"password\"", "<b>보기</b> 버튼을 함께 둡니다. 입력한 글자를 눈으로 확인하면 오타가 줄어듭니다"),
    ("오류 문구", "어느 쪽이 틀렸는지 밝히지 않음", "'아이디 또는 비밀번호'로 묶어 말해서 <b>계정이 있는지도 드러내지 않습니다</b>"),
    ("비밀번호 찾기 링크", "늘 같은 자리에 둠", "<b>틀린 뒤에야 나타나면</b> 늦기 때문에 처음부터 보이게 둡니다"),
    ("로그인 상태 유지", "오래 가는 쿠키", "끄면 브라우저를 닫을 때 로그인이 풀립니다. <b>공용 PC</b>에서는 끌 수 있도록 사용자가 고르게 합니다"),
    ("자동완성 끄기", "하지 말아야 할 일", "자동완성을 막으면 사용자가 <b>외우기 쉬운 비밀번호</b>를 쓰게 됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          어떤 계정이 가입되어 있는지 밖에서 알아내는 일을 <b>계정 열거</b>(account enumeration)라고 하는데, 오류 문구 하나만으로도 가능해집니다.
          '없는 아이디입니다'를 보여 주면 아이디 목록을 차례로 넣어 보는 것만으로
          <b>어떤 계정이 있는지</b> 가려낼 수 있기 때문입니다.
          비밀번호 찾기 화면도 같은 이유로 '메일을 보냈습니다'라는 문구를
          <b>계정이 없어도 똑같이</b> 보여 주어야 합니다.
          아이디를 먼저 받는 단계 로그인은 편하지만 같은 약점이 있으므로,
          이 방식을 쓰려면 계정이 없어도 <b>다음 단계로 똑같이 넘어가게</b> 만들어야 합니다.</p>''',
  do=ul([
    "<b>자동완성 힌트</b>를 적습니다. 한 줄만 적어도 효과가 가장 큽니다",
    "오류는 <b>한 문장으로</b> 묶어서 보여 줍니다",
    "<b>비밀번호 찾기</b> 화면과 <b>가입</b> 화면으로 가는 링크를 늘 둡니다",
  ]),
  dont=ul([
    "<code>autocomplete=\"off\"</code>를 적을 때. 비밀번호 관리자를 막아 <b>오히려 보안이 약해집니다</b>",
    "붙여넣기를 막을 때. 비밀번호 관리자를 쓸 수 없게 됩니다",
    "비밀번호 글자 수나 기호 규칙을 <b>로그인 화면에서</b> 따질 때. 그 검사는 가입 화면에서 할 일입니다",
    "'없는 아이디입니다'라고 알릴 때. 공격자가 <b>계정 목록</b>을 만들 수 있게 됩니다",
  ]),
  instead='계정을 새로 만드는 일은 가입 화면이 맡습니다. 입력한 값을 검사하는 방법은 <a href="validation.html">입력 검증</a>에서, 입력 칸을 묶어 배치하는 방법은 <a href="form.html">폼 설계</a>에서 다룹니다.',
  cases=cases([
    (scr(fld('아이디', 'hong') + BTN, "150px", "다음 →"), "아이디부터 받는 단계 로그인", "아이디를 먼저 받는 방식인데, <b>계정 열거에 약합니다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="display:block;text-align:center;border:1px solid var(--line);border-radius:4px;padding:4px 0;font-size:9px">소셜 계정으로 계속</span>
                <span style="display:block;text-align:center;border:1px solid var(--line);border-radius:4px;padding:4px 0;font-size:9px">메일로 링크 받기</span>
              </div>''',
     "비밀번호 없이 로그인하기", "비밀번호가 없으니 <b>잊어버릴 것도 없습니다.</b> 요즘 늘어나는 방식입니다"),
    (scr(fld('인증번호', '••••••') + BTN, "150px", "남은 시간 2:31"), "2단계 인증으로 한 번 더 확인하기", "인증번호의 <b>남은 시간</b>과 다시 받기 버튼을 함께 둡니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="입력 칸을 <code>&lt;form&gt;</code>으로 감싸고, 각 칸에 <b>자동완성 힌트</b>를 적습니다.",
  code='''&lt;<span class="t">form</span> <span class="a">method</span>=<span class="s">"post"</span> <span class="a">action</span>=<span class="s">"/login"</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"id"</span>&gt;아이디&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"id"</span> <span class="a">name</span>=<span class="s">"username"</span> <span class="a">autocomplete</span>=<span class="s">"username"</span> <span class="a">required</span>&gt;

  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"pw"</span>&gt;비밀번호&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"pw"</span> <span class="a">name</span>=<span class="s">"password"</span> <span class="a">type</span>=<span class="s">"password"</span>
         <span class="a">autocomplete</span>=<span class="s">"current-password"</span> <span class="a">required</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-pressed</span>=<span class="s">"false"</span>&gt;보기&lt;/<span class="t">button</span>&gt;

  &lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;아이디 또는 비밀번호가 올바르지 않습니다&lt;/<span class="t">p</span>&gt;

  &lt;<span class="t">button</span>&gt;로그인&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/forgot"</span>&gt;비밀번호를 잊으셨나요?&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">form</span>&gt;''',
  keys=kbd([
    ("<kbd>Enter</kbd>", "<code>&lt;form&gt;</code> 안에 있으면 엔터로 제출됩니다. div로 감싸면 <b>엔터를 눌러도 제출되지 않습니다</b>"),
    ("<code>autocomplete</code>", "로그인 화면에는 <code>username</code>·<code>current-password</code>를, 가입 화면에는 <code>new-password</code>를 씁니다"),
    ("<code>role=\"alert\"</code>", "스크린 리더가 읽던 것을 <b>끊고 오류를 읽습니다.</b> 틀렸다는 사실은 그만큼 급하게 알려야 하는 내용입니다"),
    ("보기 버튼에 <code>aria-pressed</code> 달기", "비밀번호가 지금 보이는 상태인지 알립니다. <b>버튼 이름만으로는</b> 알 수 없기 때문입니다"),
    ("<kbd>CapsLock</kbd>이 켜져 있을 때", "CapsLock이 켜져 있으면 알려 줍니다. <code>getModifierState('CapsLock')</code>로 확인합니다"),
    ("초점을 둘 자리", "화면을 열면 <b>아이디 칸</b>에, 틀리면 <b>틀린 칸</b>에 초점을 둡니다"),
  ]),
  backend=rows([
    ("응답 시간 맞추기", "없는 아이디에는 빨리, 있는 아이디에는 느리게 답하면 <b>응답 시간만으로도</b> 계정이 있는지 알 수 있게 됩니다. 그래서 두 경우의 응답 시간을 비슷하게 맞춥니다."),
    ("비밀번호는 해시로 저장하기", "비밀번호는 원래 값으로 되돌릴 수 없는 해시(bcrypt·argon2)로 저장합니다. 복호화할 수 있는 <b>암호화가 아니라 해시</b>입니다."),
    ("비밀번호를 틀린 횟수 제한하기", "한 계정에 비밀번호를 계속 넣어 보지 못하게 막되, <b>IP 기준</b>도 함께 봅니다. 한쪽 기준만 보면 다른 쪽을 바꿔 가며 피해 갈 수 있습니다."),
    ("로그인하면 세션을 새로 발급하기", "로그인에 성공하면 <b>세션 ID를 새로 바꿉니다.</b> 바꾸지 않으면 공격자가 미리 심어 둔 세션 ID가 로그인 뒤에도 그대로 쓰이는데, 이를 세션 고정이라고 합니다."),
    ("세션 쿠키에 붙일 속성", "<code>HttpOnly</code>·<code>Secure</code>·<code>SameSite</code>를 붙입니다. 자바스크립트로 토큰을 읽을 수 있으면 페이지에 끼어든 스크립트도 토큰을 가져갈 수 있어서 <b>토큰으로 지키는 의미가 없어집니다</b>."),
    ("비밀번호 찾기에서도 똑같이 답하기", "비밀번호 찾기에서도 계정이 없을 때 '메일을 보냈습니다'로 <b>똑같이</b> 답합니다."),
  ]),
  plat_lede="플랫폼마다 로그인 화면이 <b>OS의 비밀번호 관리자</b>와 얼마나 잘 맞물리는지가 다릅니다.",
  plats=plats([
    ("웹", "&lt;form&gt; + autocomplete",
     scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') + BTN, "112px"),
     "브라우저와 1Password·키체인은 <code>autocomplete</code> 속성을 보고 칸을 채웁니다. 웹에서는 <b>이 속성 하나로</b> 자동 채움이 정해집니다."),
    ("iOS", "AutoFill · 패스키",
     '''              <div class="phone" role="img" aria-label="iOS 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">hong</div>
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--bg);border-radius:4px;padding:3px;font-size:6px;text-align:center">🔑 hong · 암호 채우기</div></div></div>''',
     "키체인이 저장된 계정을 키보드 위에 띄워 줍니다. 요즘은 <b>패스키</b>로 비밀번호 자체를 없애는 쪽으로 옮겨 가고 있습니다."),
    ("안드로이드", "Autofill Framework",
     '''              <div class="phone" role="img" aria-label="안드로이드 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">hong</div>
                <div style="position:absolute;left:5px;right:5px;top:44px;background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">Google 비밀번호 관리자</div></div></div>''',
     "<code>autofillHints</code>로 같은 일을 합니다. 앱 안의 웹뷰에서는 <b>웹과 같은 속성</b>을 씁니다."),
  ]),
  plat_note="\"보안을 위해 자동완성과 붙여넣기를 막아 주세요\"는 지금도 자주 받는 요청이지만, 실제로는 <b>보안이 더 약해집니다</b>. 비밀번호 관리자를 쓸 수 없으면 사용자가 외울 수 있는 짧은 비밀번호를 고르게 되고, 그쪽이 훨씬 위험하기 때문입니다. 영국 NCSC를 비롯한 여러 기관이 <b>붙여넣기를 막지 말라</b>고 권고하고 있으니, 이런 요청을 받으면 그 권고를 근거로 되물어보는 편이 빠릅니다.",
  siblings=siblings("login"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>''',
)
