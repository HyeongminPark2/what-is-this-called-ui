# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fd(val, kind, note="", ok=None, w="152px", tag=""):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if kind == "off":            # disabled 인 입력 칸
        box = "background:var(--bg);border:1px solid var(--line);color:var(--fg-muted);opacity:.6"
    elif kind == "faint":        # 너무 흐려 못 읽는 칸
        box = "background:var(--bg);border:1px solid var(--line);color:var(--fg-muted);opacity:.22"
    elif kind == "ro":           # readonly 인 입력 칸
        box = "background:var(--bg);border:1px solid var(--line);color:var(--fg)"
    elif kind == "btn-off":      # disabled 인 단추
        box = ("background:var(--accent);border:1px solid var(--accent);color:#fff;opacity:.4;"
               "text-align:center;font-weight:600")
    elif kind == "btn-soft":     # aria-disabled 인 단추 — 눌리기는 한다
        box = ("background:var(--accent);border:1px solid var(--accent);color:#fff;opacity:.62;"
               "text-align:center;font-weight:600")
    else:                        # 보통 입력 칸
        box = "background:var(--surface);border:1px solid var(--line);color:var(--fg)"
    width = "max-width:" + ("78px" if kind.startswith("btn") else w)
    return ('              <div style="width:100%;' + width + ';display:grid;gap:4px;justify-items:stretch">'
            '<span style="display:block;border-radius:4px;padding:4px 7px;font-size:8px;' + box + '">' + val + '</span>'
            + ('<span style="display:inline-block;justify-self:start;font-family:var(--mono);font-size:7px;'
               'border:1px solid ' + c + ';border-radius:3px;padding:0 4px;color:' + c + ';white-space:nowrap">'
               + tag + '</span>' if tag else '')
            + ('<span style="font-size:8.5px;color:var(--fg-muted);white-space:nowrap">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">disabled면 초점이 건너뜀</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">disabled면 값이 폼에 안 실림</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">readonly는 읽히고 복사되고 실림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">aria-disabled는 눌리지만 동작은 안 함</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">왜 못 고치는지를 글로 적음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">흐린 글자는 대비비가 모자라기 쉬움</div>
                </div>
              </div>'''

D = dict(
  slug="disabledstate", ko="비활성과 읽기 전용", en="Disabled vs. read-only",
  desc="칸을 못 고치게 하는 세 가지 방법이 생김새는 비슷해도 하는 일은 전혀 다르다는 점을 다루는 항목입니다.",
  lede="칸을 못 고치게 하는 세 가지 방법은 모두 사용자 눈에 '고칠 수 없는 칸'으로 보이지만, <b>칸의 값이 서버로 가는지</b>는 서로 다릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모에서 '<b>보내 보기</b>'를 눌러 보세요.
          <code>disabled</code>인 칸은 <b>폼을 보낼 때 값이 실리지 않습니다</b>.
          사업자번호를 못 고치게 하려고 <code>disabled</code>를 걸었다가
          <b>사업자번호 값이 아예 서버로 가지 않는</b> 문제가 이 동작 때문에 생깁니다.<br>
          '<b>Tab 으로 훑어보기</b>'는 초점이 몇 군데에 멈추는지 세어 줍니다.
          <code>disabled</code>인 칸은 초점이 건너뛰기 때문에 화면 낭독기로 읽을 수조차 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "비활성, 사용 불가, 읽기 전용, 잠김"),
    ("영어", "disabled, read-only, inert, aria-disabled"),
    ("같이 쓰는 말",
     "<code>disabled</code>는 <b>비활성</b>, <code>readonly</code>는 <b>읽기 전용</b>이라고 부릅니다. "
     "<code>aria-disabled</code>는 <b>눌러도 동작하지 않는</b> 방식이라서 '<b>부드러운 비활성</b>'이라고 부르기도 합니다. "
     "화면의 한 영역을 통째로 꺼 두는 속성은 <code>inert</code>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>잠금</b> — 권한이 없어서 못 쓰는 경우는 <a href=\"permission.html\">권한 없음</a>으로, '왜 안 되는지'를 알려야 하는 다른 문제입니다.<br>"
     "<b>로딩</b> — 불러오기를 기다리는 중이라면 비활성이 아니라 <a href=\"skeleton.html\">스켈레톤</a>이나 <a href=\"spinner.html\">스피너</a>를 씁니다.<br>"
     "<b>숨김</b> — 내용을 안 보이게 접어 두는 것은 <a href=\"accordion.html\">아코디언</a>입니다."),
  ]),
  states=states([
    (fd("모란상회", "on", "고칠 수 있음", True, "152px", "보통"), "평소 상태", "값을 <b>고칠 수 있고 폼과 함께 보냅니다</b>"),
    (fd("123-45-67890", "off", "값이 서버로 안 감", False, "152px", "disabled"), "비활성 칸", "폼을 보낼 때 값이 <b>빠집니다</b>"),
    (fd("123-45-67890", "ro", "읽히고 복사되고 서버로 감", True, "152px", "readonly"), "읽기 전용 칸", "고칠 수는 없지만 <b>값은 서버로 갑니다</b>"),
    (fd("저장", "btn-off", "왜 안 되는지 모름", False, "152px", "disabled"), "비활성 단추", "왜 안 눌리는지 <b>이유를 알 수 없습니다</b>"),
    (fd("저장", "btn-soft", "누르면 이유를 알려 줌", True, "152px", "aria-disabled"), "부드러운 비활성 단추", "누르면 안 되는 <b>이유를 알려 줍니다</b>"),
    (fd("123-45-67890", "faint", "대비비 2.1:1이라 안 보임", False), "너무 흐리게 그렸을 때", "대비비가 모자라 <b>글자를 읽을 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("disabled", "초점 건너뜀", "초점이 가지 않아 화면 낭독기로 <b>읽을 수 없습니다</b>"),
    ("폼 전송", "값이 안 실림", "값이 서버로 가지 않는 문제가 <b>대부분 여기서</b> 생깁니다"),
    ("readonly", "읽힘 · 복사 · 전송", "못 고치게 할 때는 <b>대개 이 속성</b>이 맞습니다"),
    ("aria-disabled", "눌리지만 동작은 안 함", "눌렀을 때 <b>이유를</b> 알려 줄 수 있습니다"),
    ("이유", "글로 적기", "'왜 안 되는지'를 글로 적어 둡니다"),
    ("대비", "흐린 글자", "흐리게 그리면 대비비가 4.5:1 <b>아래</b>로 떨어지기 쉽습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          셋 가운데 무엇을 쓸지는 두 가지를 따져 보면 정할 수 있습니다.
          먼저 <b>값이 서버로 가야 하는지</b> 봅니다. 가야 한다면 <code>readonly</code>를 씁니다.
          다음으로 <b>왜 못 쓰는지 알려야 하는지</b> 봅니다. 알려야 한다면 <code>aria-disabled</code>를 걸고
          사용자가 눌렀을 때 이유를 띄웁니다.<br>
          두 경우에 모두 해당하지 않을 때만 <code>disabled</code>를 쓰는데,
          실제로 그런 경우는 생각보다 훨씬 드뭅니다.</p>''',
  do=ul([
    "값을 보내야 하는 칸에 <b><code>readonly</code></b> 쓰기",
    "단추는 <b><code>aria-disabled</code></b>로 두고 <b>이유를 알려 주기</b>",
    "왜 못 고치는지 <b>칸 옆에 적어 두기</b>",
    "흐리게 그려도 <b>대비비 4.5:1</b>은 지키기",
  ]),
  dont=ul([
    "값이 필요한 칸에 <b><code>disabled</code></b> 걸기. 값이 서버로 <b>가지 않습니다</b>",
    "단추를 아무 설명 없이 <b>그냥 꺼 두기</b>. 사용자는 왜 안 되는지 알 수 없습니다",
    "<b>너무 흐리게</b> 두기. 칸에 무엇이 적혔는지 읽을 수 없습니다",
    "<b>권한 없음</b>을 알려야 할 자리에 비활성 쓰기",
  ]),
  instead='권한이 없어서 안 된다는 이유를 알려야 하면 <a href="permission.html">권한 없음</a>을 보고, 불러오기를 기다리는 중이라면 칸을 끄지 말고 <a href="skeleton.html">스켈레톤</a>을 보여 줍니다. 조건이 갖춰져야 열리는 내용은 <a href="accordion.html">아코디언</a>으로 접어 둘 수 있고, 흐리게 그린 글자가 읽히는지는 <a href="contrast.html">명도 대비</a>에서 따져 봅니다.',
  cases=cases([
    (fd("123-45-67890", "ro", "", True, "148px", "readonly"), "못 고치지만 보내야 하는 값", "고칠 수는 없어도 서버로 <b>보내야</b> 하는 값입니다"),
    (fd("저장", "btn-soft", "", True, "148px", "aria-disabled"), "조건이 아직 갖춰지지 않은 단추", "누르면 아직 안 되는 <b>이유</b>를 알려 줍니다"),
    (fd("예전 메뉴", "off", "", None, "148px", "disabled"), "더는 고를 수 없는 선택지", "보낼 <b>값도 없으므로</b> <code>disabled</code>를 써도 됩니다"),
  ]),
  code_lede="세 방법은 속성 이름만 다른 것이 아니라, 폼을 보낼 때 <b>값이 실리는지</b>도 다릅니다.",
  code='''<span class="c">&lt;!-- 값이 서버로 가야 하면 readonly --&gt;</span>
&lt;<span class="t">input</span> <span class="a">name</span>=<span class="s">"bizno"</span> <span class="a">value</span>=<span class="s">"123-45-67890"</span> <span class="a">readonly</span>&gt;
&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"hint"</span>&gt;사업자번호는 고객센터에서만 바꿉니다&lt;/<span class="t">p</span>&gt;

<span class="c">&lt;!-- 값이 필요 없으면 disabled. 폼에 실리지 않는다 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">name</span>=<span class="s">"old"</span> <span class="a">value</span>=<span class="s">"쓰지 않음"</span> <span class="a">disabled</span>&gt;

<span class="c">&lt;!-- 눌러도 동작하지 않지만 이유를 알려 줄 수 있다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-disabled</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"why"</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"why"</span>&gt;계좌를 먼저 넣어야 저장됩니다&lt;/<span class="t">p</span>&gt;''',
  keys=kbd([
    ("<code>disabled</code>", "<b>Tab이 건너뜁니다</b>. 화면 낭독기로 읽히지 않고 복사도 되지 않습니다"),
    ("<code>readonly</code>", "<b>초점이 갑니다</b>. 화면 낭독기로 읽히고 복사도 됩니다"),
    ("<code>aria-disabled</code>", "<b>초점이 가고 눌리기도</b> 하므로, 동작은 코드로 막고 이유를 띄웁니다"),
    ("<code>inert</code>", "한 영역 <b>전체</b>를 통째로 끕니다. 모달 뒤에 깔린 화면처럼 잠시 손대지 못하게 할 곳에 씁니다"),
    ("확인하는 방법", "Tab만으로 훑어보며 <b>못 고치는 칸의 값을 읽을 수 있는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("disabled인 칸은 요청에서 빠짐", "<code>disabled</code>인 칸은 <b>요청에 아예 들어가지 않습니다</b>. 그래서 서버는 '값을 보내지 않은 경우'와 '빈 값을 보낸 경우'를 구별해야 합니다."),
    ("서버에서도 값 바꾸기를 막기", "화면에서 못 고치게 했더라도 요청은 얼마든지 조작할 수 있으므로, <b>서버에서도</b> 그 칸의 값을 무시하거나 막습니다."),
    ("고칠 수 없는 이유를 서버가 알려 주기", "<code>{editable: false, reason: \"고객센터에서만 변경\"}</code>처럼 <b>왜 고칠 수 없는지</b>를 함께 내려 주면 화면에 그 이유를 적을 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>비활성</b> 상태는 있지만, <b>읽기 전용</b>을 다루는 방식은 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "disabled · readonly",
     fd("123-45-67890", "ro", "", True, "108px", "readonly"),
     "<code>disabled</code>와 <code>readonly</code>가 <b>둘 다</b> 있어서, 둘 중 하나를 잘못 고르는 실수가 생깁니다."),
    ("iOS", "isEnabled · isEditable",
     '''              <div class="phone" role="img" aria-label="iOS 읽기 전용 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:24px;height:17px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:9px;top:28px;width:34px;height:4px;border-radius:2px;background:var(--fg-muted);opacity:.5"></div></div></div>''',
     "<code>isEnabled = false</code>로 두면 <b>회색</b>으로 바뀌고, <code>isEditable = false</code>로 두면 <b>읽기 전용</b>이 됩니다."),
    ("안드로이드", "enabled · readOnly",
     '''              <div class="phone" role="img" aria-label="안드로이드 읽기 전용 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:24px;height:17px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:9px;top:28px;width:34px;height:4px;border-radius:2px;background:var(--fg-muted);opacity:.5"></div></div></div>''',
     "Compose의 <code>TextField</code>에는 <b><code>readOnly</code></b> 속성이 따로 있습니다."),
  ]),
  plat_note="어느 플랫폼에서든 비활성 상태는 <b>흐리게</b> 그려지기 때문에, 여러 상태 가운데 <b>대비비가 가장 먼저 모자라게 되는 상태</b>입니다. 글자를 읽을 수 없으면 사용자는 칸을 고칠 수 없다는 것을 넘어 <b>칸에 무엇이 적혔는지조차 알 수 없게</b> 됩니다. 값을 보여 주려고 칸을 남겨 둔 것이니, 흐리게 그리더라도 대비비 <b>4.5:1</b>은 지키세요.",
  siblings=siblings("disabledstate"),
  related='''        <li><a href="permission.html"><b>권한 없음</b><em>11부</em></a></li>
        <li><a href="contrast.html"><b>명도 대비</b><em>12부</em></a></li>
        <li><a href="accordion.html"><b>아코디언</b><em>7부</em></a></li>
        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>''',
)
