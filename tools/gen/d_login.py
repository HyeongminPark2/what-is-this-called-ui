# -*- coding: utf-8 -*-
from ax13 import ax
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
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">아이디 또는 비밀번호가 올바르지 않습니다 — 갈라 말하지 않는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">비밀번호를 잊으셨나요? — 늘 같은 자리에</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">로그인 상태 유지 — 오래 가는 쿠키</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자동완성을 끄면 더 쉬운 비밀번호를 쓰게 된다</div>
                </div>
              </div>'''

D = dict(
  slug="login", ko="로그인", en="Sign in",
  desc="내가 누구인지 증명하는 화면. 오류 문구로 계정 존재를 흘리지 않기, 자동완성, 잊음 복구까지.",
  lede="가장 많이 만들어 본 화면인데 <b>가장 자주 새는</b> 화면이기도 합니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>맞는 값은 <b>hong / 1234</b> 입니다. 틀린 값으로 눌러 보세요.<br>
          <b>오류를 자세히 말하기</b>를 켜면 '없는 아이디'와 '비밀번호가 틀렸습니다'를 갈라 말합니다 —
          친절해 보이지만 <b>어떤 아이디가 있는지 알려 주는</b> 셈입니다.<br>
          <b>자동완성 끄기</b>를 켜면 비밀번호 관리자가 못 채웁니다. 보안을 위해 끈 것이
          <b>더 쉬운 비밀번호</b>를 부릅니다.</p>
        </div>''',
  names=rows([
    ("한국어", "로그인, 사인인, 인증"),
    ("영어", "sign in, log in, authentication"),
    ("같이 쓰는 말",
     "'누구인지 확인'이 <b>인증</b>(authentication), '무엇을 할 수 있는지'가 <b>인가</b>(authorization)입니다. "
     "둘 다 auth 로 줄여 써서 자주 섞입니다. "
     "로그인한 상태를 들고 있는 것이 <b>세션</b>, 그 증표가 <b>쿠키</b>나 <b>토큰</b>입니다. "
     "아이디만 먼저 받는 방식을 <b>단계 로그인</b>(identifier-first)이라 합니다."),
    ("자주 잘못 부름",
     "<b>가입</b> — 계정을 만드는 것과 들어오는 것은 <b>다른 화면</b>입니다. 한 화면에 섞으면 둘 다 흐려집니다.<br>"
     "<b>인증</b> — 본인 확인(휴대폰 인증)과 로그인은 다릅니다.<br>"
     "<b>로그인 유지</b> — '자동 로그인'과 '로그인 상태 유지'가 섞여 쓰입니다. <b>무엇이 얼마나 오래</b>인지 적어 두는 편이 낫습니다."),
  ]),
  axes=ax("로그인"),
  oneline="오류 문구로 <b>계정이 있는지 알려 주지 마세요.</b> 그리고 자동완성을 막지 마세요 — 둘 다 '보안'이라는 이름으로 반대로 하는 일이 흔합니다.",
  s4_title="상태", s4_hint="여섯 가지를 다 만들어야 한다",
  states=states([
    (scr(fld('아이디') + fld('비밀번호') + BTN, "152px", "비밀번호를 잊으셨나요?"), "비었을 때", "<b>잊음</b> 링크가 처음부터 보여야 한다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') + BTN), "채워짐", "<b>자동완성</b>이 채워 준 모습"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••', '아이디 또는 비밀번호가 올바르지 않습니다') + BTN),
     "틀림 ✓", "<b>무엇이</b> 틀렸는지 말하지 않는다"),
    (scr(fld('아이디', 'kim', '없는 아이디입니다') + fld('비밀번호', '••••') + BTN),
     "틀림 ✕", "<b>계정이 없다고 알려 준</b> 셈이다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') +
         '<span style="display:block;text-align:center;background:var(--fg-muted);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">확인 중…</span>'),
     "보내는 중", "버튼을 잠근다. <b>두 번 눌림</b>을 막는다"),
    (scr(fld('아이디', 'hong') + fld('비밀번호', '••••', '5회 틀렸습니다 · 1분 뒤 다시') + BTN),
     "여러 번 틀림", "<b>잠그되 왜 잠겼는지</b> 말한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자동완성 힌트", "autocomplete", "<code>username</code>·<code>current-password</code>. <b>비밀번호 관리자가 이걸 본다</b>"),
    ("비밀번호 칸", "type=\"password\"", "<b>보기</b> 버튼을 함께. 눈으로 확인하면 오타가 준다"),
    ("오류 문구", "갈라 말하지 않는다", "'아이디 또는 비밀번호'. <b>계정이 있는지도 숨긴다</b>"),
    ("잊음 링크", "늘 같은 자리", "<b>틀린 뒤에 나타나면</b> 늦다. 처음부터 보인다"),
    ("상태 유지", "오래 가는 쿠키", "끄면 브라우저를 닫을 때 풀린다. <b>공용 PC</b>를 위해 고를 수 있게"),
    ("자동완성 끄기", "하지 않는다", "막으면 <b>외우기 쉬운 비밀번호</b>를 쓰게 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>계정 열거</b>(account enumeration)는 오류 문구 하나로 새어 나갑니다.
          '없는 아이디입니다'를 보여 주면, 아이디 목록을 넣어 보는 것만으로
          <b>어떤 계정이 있는지</b> 알아낼 수 있습니다.
          비밀번호 찾기 화면도 마찬가지라 '메일을 보냈습니다'를
          <b>계정이 없어도 똑같이</b> 보여 주는 쪽이 맞습니다.
          단계 로그인(아이디 먼저)은 편하지만 이 구멍을 열어 두는 설계라,
          쓰려면 <b>다음 단계로 똑같이 넘어가게</b> 만들어야 합니다.</p>''',
  do=ul([
    "<b>자동완성 힌트</b>를 적는다 — 가장 효과 큰 한 줄",
    "오류는 <b>한 문장으로</b> 묶는다",
    "<b>잊음</b>과 <b>가입</b>으로 가는 길을 늘 둔다",
  ]),
  dont=ul([
    "<code>autocomplete=\"off\"</code> — <b>보안을 깎는다</b>",
    "붙여넣기 막기 — 비밀번호 관리자를 못 쓰게 한다",
    "비밀번호 글자 수·기호를 <b>여기서</b> 따지기 — 그건 가입 화면 일이다",
    "'없는 아이디입니다' — <b>계정 목록</b>을 만들어 준다",
  ]),
  instead='계정을 만드는 것은 가입 화면, 값 검사는 <a href="validation.html">입력 검증</a>, 칸 묶음은 <a href="form.html">폼 설계</a>.',
  cases=cases([
    (scr(fld('아이디', 'hong') + BTN, "150px", "다음 →"), "단계 로그인", "아이디를 먼저 받는다. <b>계정 열거에 약하다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="display:block;text-align:center;border:1px solid var(--line);border-radius:4px;padding:4px 0;font-size:9px">소셜 계정으로 계속</span>
                <span style="display:block;text-align:center;border:1px solid var(--line);border-radius:4px;padding:4px 0;font-size:9px">메일로 링크 받기</span>
              </div>''',
     "비밀번호 없는 길", "<b>잊어버릴 것이 없다.</b> 요즘 늘어나는 방식"),
    (scr(fld('인증번호', '••••••') + BTN, "150px", "남은 시간 2:31"), "2단계 인증", "<b>남은 시간</b>과 다시 받기를 함께 둔다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="<code>&lt;form&gt;</code>으로 감싸고 <b>자동완성 힌트</b>를 적습니다.",
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
    ("<kbd>Enter</kbd>", "<code>&lt;form&gt;</code> 안이면 제출된다. div 로 감싸면 <b>엔터가 죽는다</b>"),
    ("<code>autocomplete</code>", "<code>username</code>·<code>current-password</code>. 가입 화면은 <code>new-password</code>"),
    ("<code>role=\"alert\"</code>", "오류를 <b>끊고 읽는다.</b> 틀렸다는 사실은 끊어도 될 만큼 급하다"),
    ("보기 버튼은 <code>aria-pressed</code>", "지금 보이는 상태인지 알린다. <b>버튼 이름만으로는</b> 모른다"),
    ("<kbd>CapsLock</kbd> 경고", "켜져 있으면 알려 준다. <code>getModifierState('CapsLock')</code>"),
    ("초점", "열자마자 <b>아이디 칸</b>으로. 틀리면 <b>틀린 칸</b>으로"),
  ]),
  backend=rows([
    ("응답 시간을 맞춘다", "없는 아이디는 빨리, 있는 아이디는 느리게 답하면 <b>시간만으로도</b> 계정 유무가 새어 나갑니다."),
    ("비밀번호는 해시로", "되돌릴 수 없는 해시(bcrypt·argon2)로 저장합니다. <b>암호화가 아니라 해시</b>입니다."),
    ("틀린 횟수 제한", "한 계정을 계속 두드리지 못하게 막되, <b>IP 기준</b>도 함께 봅니다. 한쪽만 보면 우회됩니다."),
    ("세션을 새로 발급", "로그인에 성공하면 <b>세션 ID 를 바꿉니다.</b> 안 바꾸면 미리 심어 둔 세션이 그대로 쓰입니다(세션 고정)."),
    ("쿠키 속성", "<code>HttpOnly</code>·<code>Secure</code>·<code>SameSite</code>. 자바스크립트로 읽히면 토큰은 <b>없는 것과 같습니다</b>."),
    ("비밀번호 찾기도 같게", "계정이 없어도 '메일을 보냈습니다'로 <b>똑같이</b> 답합니다."),
  ]),
  plat_lede="<b>OS 의 비밀번호 관리자</b>와 얼마나 잘 붙느냐가 갈립니다.",
  plats=plats([
    ("웹", "&lt;form&gt; + autocomplete",
     scr(fld('아이디', 'hong') + fld('비밀번호', '••••••') + BTN, "112px"),
     "브라우저와 1Password·키체인이 <code>autocomplete</code>를 보고 채웁니다. <b>이 속성이 전부</b>입니다."),
    ("iOS", "AutoFill · 패스키",
     '''              <div class="phone" role="img" aria-label="iOS 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">hong</div>
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--bg);border-radius:4px;padding:3px;font-size:6px;text-align:center">🔑 hong · 암호 채우기</div></div></div>''',
     "키체인이 키보드 위에 띄워 줍니다. <b>패스키</b>로 비밀번호 자체를 없애는 쪽으로 가고 있습니다."),
    ("안드로이드", "Autofill Framework",
     '''              <div class="phone" role="img" aria-label="안드로이드 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">hong</div>
                <div style="position:absolute;left:5px;right:5px;top:44px;background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:3px;font-size:6px">Google 비밀번호 관리자</div></div></div>''',
     "<code>autofillHints</code>로 같은 일을 합니다. 웹뷰에서는 <b>웹과 같은 속성</b>이 쓰입니다."),
  ]),
  plat_note="\"보안을 위해 자동완성과 붙여넣기를 막아 주세요\"는 지금도 자주 오는 요청인데, <b>효과가 반대</b>입니다. 관리자를 못 쓰면 외울 수 있는 짧은 비밀번호를 쓰게 되고, 그쪽이 훨씬 위험합니다. 영국 NCSC 를 비롯한 기관들이 <b>붙여넣기를 막지 말라</b>고 권고로 못 박아 두었으니, 그걸 근거로 되물어보는 편이 빠릅니다.",
  siblings=siblings("login"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>''',
)
