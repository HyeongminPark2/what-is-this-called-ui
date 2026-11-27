# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def pw(val, bars=2, label="", note="", ok=None, w="152px", eye="보기", kind=""):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    col = 'var(--danger)' if bars <= 1 else ('#9a6700' if bars == 2 else 'var(--accent)')
    b = ''.join('<span style="flex:1;height:3px;border-radius:999px;background:'
                + (col if i < bars else 'var(--bg)') + '"></span>' for i in range(4))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:flex;gap:4px;align-items:stretch">'
            '<span style="flex:1;min-width:0;border:1px solid ' + c + ';border-radius:4px;background:var(--surface);'
            'padding:3px 6px;font-size:8px;font-family:var(--mono);overflow:hidden;text-overflow:ellipsis;'
            'white-space:nowrap">' + val + '</span>'
            '<span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);'
            'padding:3px 6px;font-size:7.5px;color:var(--accent);white-space:nowrap">' + eye + '</span></span>'
            '<span style="display:flex;gap:2px">' + b + '</span>'
            + ('<span style="font-size:7.5px;color:var(--fg-muted)">' + kind + '</span>' if kind else '')
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">보기 단추 — 눈으로 확인할 유일한 길</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">세기 막대 — 규칙이 아니라 안내</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">붙여넣기를 막지 않는다 — 관리자를 못 쓰게 된다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">autocomplete — 관리자가 알아보게 한다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">갈래 강제는 짧고 뻔한 것을 통과시킨다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">규칙은 치기 전에 적어 둔다</div>
                </div>
              </div>'''

D = dict(
  slug="password", ko="비밀번호 칸", en="Password field",
  desc="가려진 글을 받는 칸. 보기 단추, 붙여넣기, 길이 대 갈래 규칙.",
  lede="비밀번호 칸의 핵심은 <b>무엇을 막지 않느냐</b>입니다 — 붙여넣기를 막으면 오히려 약해집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>붙여넣기를 막으면</b> 비밀번호 관리자를 못 쓰게 되어 오히려 약한 비밀번호를 쓰게 됩니다 —
          체크를 끄고 붙여넣어 보면 데모가 막힌 횟수를 셉니다.<br>
          <b>갈래 강제</b>(대문자·숫자·기호)는 <code>Passw0rd!</code> 같은 <b>짧고 뻔한</b> 것을 통과시키고,
          길고 센 한국어 문장을 막습니다 — 데모가 두 규칙으로 각각 매겨 보여 줍니다.<br>
          <b>보기 단추</b>는 눈으로 확인할 유일한 길입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "비밀번호 칸, 암호 입력, 패스워드 필드"),
    ("영어", "password field, password input, masked input"),
    ("같이 쓰는 말",
     "글자를 점으로 가리는 것을 <b>마스킹</b>, 눌러서 드러내는 것을 <b>보기 토글</b>(reveal)이라 합니다. "
     "세기를 막대로 보여 주는 것은 <b>스트렝스 미터</b>, "
     "여러 낱말을 이어 만든 긴 것은 <b>패스프레이즈</b>입니다."),
    ("자주 잘못 부름",
     "<b>텍스트 필드</b> — <a href=\"field.html\">텍스트 필드</a>와 같은 태그지만 <code>type</code> 이 다릅니다.<br>"
     "<b>PIN</b> — 네 자리 숫자는 <b>다른 부품</b>으로 만드는 편이 낫습니다.<br>"
     "<b>OTP</b> — 일회용 번호는 <code>autocomplete=\"one-time-code\"</code> 를 씁니다."),
  ]),
  axes=ax("비밀번호 칸"),
  oneline="<b>길이를 보세요.</b> 갈래를 강제하면 짧고 뻔한 것만 늘어납니다.",
  states=states([
    (pw("••••••••••••", 3, "", "길어서 세다", True, "152px", "보기", "12자 — 길이 규칙 통과"),
     "길고 센 것", "<b>길이</b>가 세기다"),
    (pw("Passw0rd!", 1, "", "갈래는 맞췄지만 뻔하다", False, "152px", "보기", "9자 — 갈래 규칙 통과"),
     "짧고 뻔한 것", "<b>갈래 규칙</b>이 통과시킨다"),
    (pw("그냥길게적은한국어문장입니다", 4, "", "갈래 규칙이 이걸 막는다", False, "152px", "보기", "14자 — 갈래 규칙 미달"),
     "갈래 강제", "<b>센 것을 막는다</b>"),
    (pw("mypassword123", 2, "", "보기로 눈으로 확인한다", True, "152px", "숨기기"),
     "보기 켬", "<b>눈으로</b> 확인"),
    (pw("(붙여넣기 막힘)", 0, "", "관리자가 넣어 주는 긴 것을 못 쓴다", False),
     "붙여넣기 막음", "<b>오히려 약해진다</b>"),
    (pw("••••••••••••••••••••", 4, "", "관리자가 만든 20자", True, "152px", "보기", "autocomplete 로 알아본다"),
     "관리자와 함께", "<b>가장 센</b> 길"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보기 단추", "눈으로", "확인할 <b>유일한</b> 길"),
    ("세기 막대", "안내", "규칙이 <b>아니다</b>"),
    ("붙여넣기", "막지 않기", "<b>관리자</b>를 쓰게 한다"),
    ("<code>autocomplete</code>", "관리자가 알아봄", "<code>new-password</code>"),
    ("갈래 강제", "역효과", "짧고 뻔한 것이 통과"),
    ("규칙", "미리 적기", "치고 나서 말하지 않는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>대문자·숫자·기호를 꼭 넣으라</b>는 규칙은 오래 쓰였지만,
          지금은 권하지 않습니다 —
          사람들이 그 규칙을 <b>가장 적게 만족하는 방식</b>으로 만들기 때문입니다
          (<code>Password1!</code>, <code>Qwer1234!</code>).
          대신 <b>길이</b>를 보고, <b>이미 털린 비밀번호 목록</b>과 맞춰 보는 쪽이 실제로 셉니다.<br>
          <b>붙여넣기를 막는 것</b>은 보안을 위해 하는 일처럼 보이지만,
          관리자가 만들어 주는 <b>20자짜리 무작위 비밀번호</b>를 못 쓰게 만들어
          오히려 사람이 외울 수 있는 약한 것을 쓰게 합니다.</p>''',
  do=ul([
    "<b>길이</b>를 기준으로 삼기",
    "<b>보기 단추</b> 두고 <code>aria-pressed</code> 로 상태 알리기",
    "<code>autocomplete=\"new-password\"</code> 로 <b>관리자가 알아보게</b> 하기",
  ]),
  dont=ul([
    "<b>붙여넣기 막기</b> — 관리자를 못 쓰게 된다",
    "갈래를 <b>강제</b>하기 — 짧고 뻔한 것만 늘어난다",
    "규칙을 <b>틀린 뒤에</b> 알리기",
    "최대 길이를 <b>짧게</b> 두기 — 20자도 못 넣는 칸이 많다",
  ]),
  instead='한 줄 글이면 <a href="field.html">텍스트 필드</a>, 검사 규칙은 <a href="validation.html">입력 검증</a>, 로그인 화면 전체는 <a href="login.html">로그인</a>, 오류 문구는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (pw("••••••••••••", 3, "", "", True, "150px", "보기"), "새 비밀번호", "<b>길이</b>를 본다"),
    (pw("••••••••", 2, "", "", True, "150px", "보기", "autocomplete=\"current-password\""),
     "로그인", "<b>세기 막대를 안 둔다</b>"),
    (pw("1 2 3 4 5 6", 0, "", "", None, "150px", ""), "일회용 번호", "<b>다른 부품</b>이 맞다"),
  ]),
  code_lede="<code>autocomplete</code> 를 제대로 적는 것이 가장 큰 차이를 냅니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"pw"</span>&gt;새 비밀번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"pw"</span> <span class="a">type</span>=<span class="s">"password"</span>
       <span class="a">autocomplete</span>=<span class="s">"new-password"</span>      <span class="c">&lt;!-- 로그인이면 current-password --&gt;</span>
       <span class="a">minlength</span>=<span class="s">"12"</span> <span class="a">aria-describedby</span>=<span class="s">"pw-rule"</span>&gt;
&lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-pressed</span>=<span class="s">"false"</span>
        <span class="a">aria-label</span>=<span class="s">"비밀번호 보기"</span>&gt;보기&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"pw-rule"</span>&gt;12자 이상이면 됩니다 — 길수록 셉니다&lt;/<span class="t">p</span>&gt;

<span class="c">// ✕ 이렇게 막지 않는다</span>
input.addEventListener(<span class="s">'paste'</span>, e =&gt; e.preventDefault());''',
  keys=kbd([
    ("<code>autocomplete</code>", "<code>new-password</code> · <code>current-password</code> 를 <b>가려서</b> 적는다"),
    ("<code>aria-pressed</code>", "보기 단추가 <b>눌린 상태</b>인지 알린다"),
    ("<code>aria-describedby</code>", "규칙을 칸과 <b>묶어</b> 둔다"),
    ("Caps Lock", "켜져 있으면 <b>알려 주는</b> 것이 친절하다"),
    ("<code>minlength</code>", "브라우저가 <b>길이를 검사</b>해 준다"),
    ("확인하는 법", "비밀번호 관리자로 <b>넣어 보고 붙여넣어</b> 본다"),
  ]),
  backend=rows([
    ("규칙은 서버가 정한다", "화면이 아는 규칙과 서버의 규칙이 다르면 <b>통과했는데 거절</b>당합니다."),
    ("털린 목록", "널리 털린 비밀번호 목록과 맞춰 보면 <b>갈래 규칙보다 훨씬</b> 효과가 큽니다."),
    ("최대 길이", "짧게 두지 않습니다 — <b>64자 이상</b>을 받는 편이 안전합니다."),
    ("실패 메시지", "'아이디 또는 비밀번호가 다릅니다'로 <b>어느 쪽인지 숨깁니다</b> — <a href=\"login.html\">로그인</a> 참고."),
  ]),
  plat_lede="<b>관리자와 자동 채움</b>을 OS 가 맡습니다.",
  plats=plats([
    ("웹", "type=\"password\"",
     pw("••••••••••••", 3, "", "", True, "110px", "보기"),
     "<code>autocomplete</code> 를 제대로 적으면 <b>브라우저 관리자</b>가 알아서 돕습니다."),
    ("iOS", "SecureField + 키체인",
     '''              <div class="phone" role="img" aria-label="iOS 비밀번호 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<b>키체인</b>이 강한 비밀번호를 만들어 주고 자판 위에 띄워 줍니다."),
    ("안드로이드", "자동 채움 서비스",
     '''              <div class="phone" role="img" aria-label="안드로이드 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<b>Autofill</b> 서비스가 같은 일을 합니다 — 칸에 힌트를 적어 둬야 알아봅니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>비밀번호 관리자를 돕는 쪽</b>으로 갑니다 — 사람이 외우는 것보다 기계가 만든 긴 것이 훨씬 세기 때문입니다. 그래서 <b>붙여넣기를 막는 것</b>은 이 흐름을 거스르는 일이 됩니다. 요즘은 아예 비밀번호를 없애는 <b>패스키</b>로 가는 중이라, 새로 만드는 화면이라면 그쪽을 같이 두는 것도 생각해 볼 만합니다.",
  siblings=siblings("password"),
  related='''        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="login.html"><b>로그인</b><em>13부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
