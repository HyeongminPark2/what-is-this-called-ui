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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">보기 단추는 눈으로 확인할 유일한 방법</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">세기 막대는 규칙이 아니라 안내</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">붙여넣기를 막으면 관리자를 못 쓰게 됨</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">autocomplete로 관리자가 알아보게 함</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">갈래 강제는 짧고 뻔한 것을 통과시킴</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">규칙은 치기 전에 적어 둠</div>
                </div>
              </div>'''

D = dict(
  slug="password", ko="비밀번호 칸", en="Password field",
  desc="글자를 가린 채 받는 비밀번호 칸에서 보기 단추와 붙여넣기, 길이 규칙과 갈래 규칙의 차이를 다루는 항목입니다.",
  lede="비밀번호 칸을 만들 때는 <b>무엇을 막지 않을지</b>가 핵심입니다. 예를 들어 보안을 위해 붙여넣기를 막으면 사용자가 더 약한 비밀번호를 쓰게 되어 오히려 보안이 약해집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>붙여넣기를 막으면</b> 비밀번호 관리자를 쓸 수 없어서 사용자가 오히려 약한 비밀번호를 고르게 됩니다.
          체크를 끄고 붙여넣어 보면 데모가 막힌 횟수를 세어 줍니다.<br>
          대문자·숫자·기호를 모두 넣게 하는 <b>갈래 강제</b>는 <code>Passw0rd!</code> 같은 <b>짧고 뻔한</b> 비밀번호는 통과시키면서
          길고 센 한국어 문장은 막습니다. 데모가 같은 비밀번호를 두 규칙으로 각각 판정해 보여 줍니다.<br>
          <b>보기 단추</b>는 사용자가 친 비밀번호를 눈으로 확인할 수 있는 유일한 방법입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "비밀번호 칸, 암호 입력, 패스워드 필드"),
    ("영어", "password field, password input, masked input"),
    ("같이 쓰는 말",
     "글자를 점으로 가리는 것은 <b>마스킹</b>, 단추를 눌러 가린 글자를 드러내는 것은 <b>보기 토글</b>(reveal)이라고 부릅니다. "
     "비밀번호 세기를 막대로 보여 주는 것은 <b>스트렝스 미터</b>, "
     "여러 낱말을 이어 만든 긴 비밀번호는 <b>패스프레이즈</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>텍스트 필드</b> — <a href=\"field.html\">텍스트 필드</a>와 같은 태그를 쓰지만 <code>type</code>이 다릅니다.<br>"
     "<b>PIN</b> — 네 자리 숫자 비밀번호는 비밀번호 칸이 아닌 <b>다른 부품</b>으로 만드는 편이 낫습니다.<br>"
     "<b>OTP</b> — 일회용 번호를 받는 칸에는 <code>autocomplete=\"one-time-code\"</code>를 씁니다."),
  ]),
  axes=ax("비밀번호 칸"),
  oneline="<b>비밀번호의 세기는 길이로 판단하세요.</b> 대문자·숫자·기호 같은 갈래를 강제하면 규칙만 겨우 맞춘 짧고 뻔한 비밀번호가 늘어납니다.",
  states=states([
    (pw("••••••••••••", 3, "", "길어서 셈", True, "152px", "보기", "12자라 길이 규칙 통과"),
     "길고 센 비밀번호", "비밀번호가 <b>길수록</b> 셉니다"),
    (pw("Passw0rd!", 1, "", "갈래는 맞췄지만 뻔함", False, "152px", "보기", "9자인데도 갈래 규칙 통과"),
     "짧고 뻔한 비밀번호", "뻔한 비밀번호인데도 <b>갈래 규칙</b>은 통과시킵니다"),
    (pw("그냥길게적은한국어문장입니다", 4, "", "갈래 규칙에 막힘", False, "152px", "보기", "14자인데도 갈래 규칙 미달"),
     "갈래 규칙이 긴 문장을 막을 때", "대문자·숫자·기호가 없다는 이유로 길고 <b>센 비밀번호를 막습니다</b>"),
    (pw("mypassword123", 2, "", "보기를 눌러 눈으로 확인함", True, "152px", "숨기기"),
     "보기 단추를 눌렀을 때", "친 비밀번호를 <b>눈으로</b> 확인할 수 있습니다"),
    (pw("(붙여넣기 막힘)", 0, "", "관리자가 만든 긴 비밀번호를 못 씀", False),
     "붙여넣기를 막았을 때", "관리자가 만든 긴 비밀번호를 못 쓰게 되어 <b>오히려 약해집니다</b>"),
    (pw("••••••••••••••••••••", 4, "", "관리자가 만든 20자", True, "152px", "보기", "autocomplete로 알아봄"),
     "비밀번호 관리자로 채웠을 때", "관리자가 만든 무작위 비밀번호를 쓰는 것이 <b>가장 센</b> 방법입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보기 단추", "눈으로 확인하기", "친 비밀번호를 눈으로 확인할 수 있는 <b>유일한</b> 방법입니다"),
    ("세기 막대", "규칙이 아닌 안내", "세기를 알려 주는 안내이고, 통과 여부를 정하는 규칙이 <b>아닙니다</b>"),
    ("붙여넣기", "막지 않기", "붙여넣기를 열어 두어야 <b>비밀번호 관리자</b>를 쓸 수 있습니다"),
    ("<code>autocomplete</code>", "관리자가 알아봄", "<code>new-password</code>를 적어 두면 관리자가 새 비밀번호 칸으로 알아봅니다"),
    ("갈래 강제", "오히려 약해짐", "짧고 뻔한 비밀번호가 오히려 통과합니다"),
    ("규칙", "미리 적기", "규칙은 사용자가 치기 전에 보여 주고, 틀린 뒤에 처음 알리지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>대문자·숫자·기호를 꼭 넣으라</b>는 규칙은 오래 쓰였지만 지금은 권하지 않습니다.
          사람들이 <code>Password1!</code>이나 <code>Qwer1234!</code>처럼
          규칙을 <b>최소한으로만 맞춘 비밀번호</b>를 만들기 때문입니다.
          그보다는 <b>길이</b>를 기준으로 삼고, <b>이미 유출된 비밀번호 목록</b>과 대조하는 편이 실제로 비밀번호를 세게 만듭니다.<br>
          <b>붙여넣기를 막는 것</b>도 보안을 위한 조치처럼 보이지만,
          관리자가 만들어 주는 <b>20자짜리 무작위 비밀번호</b>를 쓸 수 없게 되기 때문에
          사용자는 결국 외우기 쉬운 약한 비밀번호를 고르게 됩니다.</p>''',
  do=ul([
    "비밀번호 세기를 <b>길이</b>로 판단하기",
    "<b>보기 단추</b>를 두고 <code>aria-pressed</code>로 눌린 상태 알리기",
    "<code>autocomplete=\"new-password\"</code>를 적어 <b>관리자가 알아보게</b> 하기",
  ]),
  dont=ul([
    "<b>붙여넣기 막기</b>. 비밀번호 관리자를 쓸 수 없게 됩니다",
    "대문자·숫자·기호 갈래를 <b>강제</b>하기. 규칙만 맞춘 짧고 뻔한 비밀번호가 늘어납니다",
    "규칙을 사용자가 <b>틀린 뒤에</b> 처음 알리기",
    "최대 길이를 <b>짧게</b> 두기. 20자짜리 비밀번호도 못 넣는 칸이 많습니다",
  ]),
  instead='글자를 가릴 필요가 없는 한 줄 글이면 <a href="field.html">텍스트 필드</a>를 씁니다. 비밀번호 규칙을 어떻게 검사할지는 <a href="validation.html">입력 검증</a>에서, 로그인 화면 전체를 어떻게 짤지는 <a href="login.html">로그인</a>에서, 틀렸을 때 보여 줄 문구는 <a href="errortext.html">오류 문구</a>에서 다룹니다.',
  cases=cases([
    (pw("••••••••••••", 3, "", "", True, "150px", "보기"), "새 비밀번호 만들기", "새로 만드는 비밀번호는 <b>길이</b>로 판단합니다"),
    (pw("••••••••", 2, "", "", True, "150px", "보기", "autocomplete=\"current-password\""),
     "로그인할 때 비밀번호 넣기", "이미 있는 비밀번호를 넣는 칸이라서 <b>세기 막대를 두지 않습니다</b>"),
    (pw("1 2 3 4 5 6", 0, "", "", None, "150px", ""), "일회용 번호 받기", "비밀번호 칸보다 <b>다른 부품</b>이 맞습니다"),
  ]),
  code_lede="<code>autocomplete</code>를 알맞게 적는 것만으로 비밀번호 관리자가 칸을 알아보고 채워 주기 때문에, 코드에서 가장 큰 차이를 만드는 부분입니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"pw"</span>&gt;새 비밀번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"pw"</span> <span class="a">type</span>=<span class="s">"password"</span>
       <span class="a">autocomplete</span>=<span class="s">"new-password"</span>      <span class="c">&lt;!-- 로그인이면 current-password --&gt;</span>
       <span class="a">minlength</span>=<span class="s">"12"</span> <span class="a">aria-describedby</span>=<span class="s">"pw-rule"</span>&gt;
&lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-pressed</span>=<span class="s">"false"</span>
        <span class="a">aria-label</span>=<span class="s">"비밀번호 보기"</span>&gt;보기&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"pw-rule"</span>&gt;12자 이상이면 되고, 길수록 셉니다&lt;/<span class="t">p</span>&gt;

<span class="c">// ✕ 붙여넣기를 이렇게 막지 않는다</span>
input.addEventListener(<span class="s">'paste'</span>, e =&gt; e.preventDefault());''',
  keys=kbd([
    ("<code>autocomplete</code>", "새 비밀번호 칸에는 <code>new-password</code>, 로그인 칸에는 <code>current-password</code>를 <b>구분해</b> 적습니다"),
    ("<code>aria-pressed</code>", "보기 단추가 <b>눌린 상태</b>인지 알립니다"),
    ("<code>aria-describedby</code>", "비밀번호 규칙 안내를 칸과 <b>연결해</b> 둡니다"),
    ("Caps Lock", "Caps Lock이 켜져 있으면 <b>알려 주는</b> 편이 좋습니다"),
    ("<code>minlength</code>", "브라우저가 <b>길이를 검사</b>해 줍니다"),
    ("확인하는 방법", "비밀번호 관리자로 <b>채워 보고, 직접 붙여넣어</b> 봅니다"),
  ]),
  backend=rows([
    ("화면과 서버의 규칙 맞추기", "화면에서 검사하는 규칙과 서버의 규칙이 다르면, 화면에서는 <b>통과했는데 서버에서 거절</b>당하는 일이 생깁니다."),
    ("유출된 비밀번호 목록과 대조하기", "널리 유출된 비밀번호 목록과 대조하는 방법이 <b>갈래 규칙보다 훨씬</b> 효과가 큽니다."),
    ("최대 길이를 넉넉하게 두기", "최대 길이를 짧게 두지 말고 <b>64자 이상</b>을 받는 편이 안전합니다."),
    ("로그인에 실패했을 때 알리는 문구", "로그인에 실패하면 '아이디 또는 비밀번호가 다릅니다'라고 적어 둘 중 <b>어느 쪽이 틀렸는지 숨깁니다</b>. 자세한 내용은 <a href=\"login.html\">로그인</a> 항목에 있습니다."),
  ]),
  plat_lede="앱에서는 <b>비밀번호 관리자와 자동 채움</b>을 운영 체제가 맡습니다.",
  plats=plats([
    ("웹", "type=\"password\"",
     pw("••••••••••••", 3, "", "", True, "110px", "보기"),
     "<code>autocomplete</code>를 알맞게 적어 두면 <b>브라우저의 비밀번호 관리자</b>가 알아서 채워 줍니다."),
    ("iOS", "SecureField + 키체인",
     '''              <div class="phone" role="img" aria-label="iOS 비밀번호 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<b>키체인</b>이 강한 비밀번호를 만들어 자판 위에 띄워 줍니다."),
    ("안드로이드", "자동 채움 서비스",
     '''              <div class="phone" role="img" aria-label="안드로이드 자동 채움 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<b>Autofill</b> 서비스가 같은 일을 하는데, 칸에 자동 채움 힌트를 적어 두어야 비밀번호 칸으로 알아봅니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>비밀번호 관리자가 일하기 쉽도록</b> 바뀌어 왔습니다. 사람이 외워서 만든 비밀번호보다 기계가 만든 긴 비밀번호가 훨씬 세기 때문입니다. 그런데 <b>붙여넣기를 막으면</b> 관리자가 만든 비밀번호를 넣을 수 없으니 플랫폼이 가는 방향과 반대로 가게 됩니다. 요즘은 비밀번호 자체를 없애는 <b>패스키</b>로 옮겨 가는 중이라서, 새로 만드는 화면이라면 패스키 로그인을 함께 두는 것도 생각해 볼 만합니다.",
  siblings=siblings("password"),
  related='''        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="login.html"><b>로그인</b><em>13부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
