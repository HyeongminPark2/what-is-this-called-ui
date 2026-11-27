# -*- coding: utf-8 -*-
from ax4 import ax
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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">disabled — 초점이 건너뛴다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">disabled — 값이 폼에 안 실린다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">readonly — 읽히고 복사되고 실린다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">aria-disabled — 눌리지만 안 먹는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">왜 못 고치는지를 글로 적는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">흐린 글자는 대비비가 모자라기 쉽다</div>
                </div>
              </div>'''

D = dict(
  slug="disabledstate", ko="비활성과 읽기 전용", en="Disabled vs. read-only",
  desc="못 고치게 하는 세 가지 방법. 생김새는 비슷한데 하는 일이 전혀 다르다.",
  lede="셋 다 '못 고친다'로 보이지만, <b>값이 서버로 가는지</b>가 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모에서 '<b>보내 보기</b>'를 눌러 보세요 —
          <code>disabled</code> 인 칸은 <b>폼에 안 실립니다</b>.
          사업자번호를 못 고치게 하려고 <code>disabled</code> 를 걸었다가
          <b>값이 통째로 안 가는</b> 사고가 여기서 납니다.<br>
          '<b>Tab 으로 훑어보기</b>'는 초점이 몇 군데 멈추는지 셉니다 —
          <code>disabled</code> 는 건너뛰어서 화면 낭독기로 읽을 수조차 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "비활성, 사용 불가, 읽기 전용, 잠김"),
    ("영어", "disabled, read-only, inert, aria-disabled"),
    ("같이 쓰는 말",
     "<code>disabled</code> 는 <b>비활성</b>, <code>readonly</code> 는 <b>읽기 전용</b>입니다. "
     "<code>aria-disabled</code> 는 <b>눌리지만 안 먹는</b> 쪽이라 '<b>부드러운 비활성</b>'이라 부르기도 합니다. "
     "영역 전체를 통째로 꺼 두는 속성은 <code>inert</code> 입니다."),
    ("자주 잘못 부름",
     "<b>잠금</b> — <a href=\"permission.html\">권한 없음</a>은 '왜 안 되는지'를 알려야 하는 다른 문제입니다.<br>"
     "<b>로딩</b> — 기다리는 중이면 <a href=\"skeleton.html\">스켈레톤</a>이나 <a href=\"spinner.html\">스피너</a>입니다.<br>"
     "<b>숨김</b> — 안 보이게 접어 두는 것은 <a href=\"accordion.html\">아코디언</a>입니다."),
  ]),
  axes=ax("비활성과 읽기 전용"),
  oneline="<b>값을 보내야 하면 <code>readonly</code> 입니다.</b> <code>disabled</code> 는 값을 버립니다.",
  states=states([
    (fd("모란상회", "on", "고칠 수 있다", True, "152px", "보통"), "보통", "<b>고치고 보낸다</b>"),
    (fd("123-45-67890", "off", "값이 안 간다", False, "152px", "disabled"), "비활성", "<b>폼에서 빠진다</b>"),
    (fd("123-45-67890", "ro", "읽히고 복사되고 간다", True, "152px", "readonly"), "읽기 전용", "<b>값이 간다</b>"),
    (fd("저장", "btn-off", "왜 안 되는지 모른다", False, "152px", "disabled"), "비활성 단추", "<b>이유를 못 듣는다</b>"),
    (fd("저장", "btn-soft", "누르면 이유를 말해 준다", True, "152px", "aria-disabled"), "부드러운 비활성", "<b>이유를 말한다</b>"),
    (fd("123-45-67890", "faint", "대비비 2.1:1 — 안 보인다", False), "너무 흐림", "<b>읽히지 않는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("disabled", "초점 건너뜀", "<b>못 읽는다</b>"),
    ("폼 전송", "안 실림", "사고의 <b>진원지</b>"),
    ("readonly", "읽힘 · 복사 · 전송", "<b>대개 이쪽</b>"),
    ("aria-disabled", "눌림 · 안 먹음", "<b>이유를</b> 말한다"),
    ("이유", "글로", "'왜 안 되나'"),
    ("대비", "흐린 글자", "4.5:1 <b>아래</b>로 떨어진다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          고를 때 물을 것은 두 가지입니다.
          <b>값이 서버로 가야 하나</b> — 가야 하면 <code>readonly</code> 입니다.
          <b>왜 못 쓰는지 말해야 하나</b> — 말해야 하면 <code>aria-disabled</code> 를 걸고
          눌렀을 때 이유를 띄웁니다.<br>
          둘 다 아니라면 그때 <code>disabled</code> 입니다 —
          생각보다 훨씬 드뭅니다.</p>''',
  do=ul([
    "값을 보내야 하면 <b><code>readonly</code></b>",
    "단추는 <b><code>aria-disabled</code></b> 로 두고 <b>이유를 말해 주기</b>",
    "왜 못 고치는지 <b>칸 옆에 적어 두기</b>",
    "흐려도 <b>대비비 4.5:1</b> 은 지키기",
  ]),
  dont=ul([
    "값이 필요한 칸에 <b><code>disabled</code></b> 걸기 — 값이 <b>안 간다</b>",
    "단추를 <b>그냥 꺼 두기</b> — 왜 안 되는지 알 길이 없다",
    "<b>너무 흐리게</b> 두기 — 뭐라고 적혔는지 못 읽는다",
    "비활성을 <b>권한 없음</b> 대신 쓰기",
  ]),
  instead='왜 안 되는지 말해야 하면 <a href="permission.html">권한 없음</a>, 기다리는 중이면 <a href="skeleton.html">스켈레톤</a>, 조건이 차야 열리면 <a href="accordion.html">아코디언</a>, 글자가 읽히는지는 <a href="contrast.html">명도 대비</a>.',
  cases=cases([
    (fd("123-45-67890", "ro", "", True, "148px", "readonly"), "못 고치는 값", "<b>보내야</b> 한다"),
    (fd("저장", "btn-soft", "", True, "148px", "aria-disabled"), "조건이 안 찬 단추", "<b>이유</b>를 말한다"),
    (fd("예전 메뉴", "off", "", None, "148px", "disabled"), "정말 없는 선택지", "<b>값도 없다</b>"),
  ]),
  code_lede="셋은 속성이 다를 뿐 아니라 <b>폼에 실리는지</b>가 다릅니다.",
  code='''<span class="c">&lt;!-- 값이 가야 한다: readonly --&gt;</span>
&lt;<span class="t">input</span> <span class="a">name</span>=<span class="s">"bizno"</span> <span class="a">value</span>=<span class="s">"123-45-67890"</span> <span class="a">readonly</span>&gt;
&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"hint"</span>&gt;사업자번호는 고객센터에서만 바꿉니다&lt;/<span class="t">p</span>&gt;

<span class="c">&lt;!-- 값이 필요 없다: disabled — 폼에 안 실린다 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">name</span>=<span class="s">"old"</span> <span class="a">value</span>=<span class="s">"쓰지 않음"</span> <span class="a">disabled</span>&gt;

<span class="c">&lt;!-- 눌리지만 안 먹는다: 이유를 말해 줄 수 있다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-disabled</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"why"</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"why"</span>&gt;계좌를 먼저 넣어야 저장됩니다&lt;/<span class="t">p</span>&gt;''',
  keys=kbd([
    ("<code>disabled</code>", "<b>Tab 이 건너뜁니다</b> — 화면 낭독기로 읽히지 않고 복사도 안 됩니다"),
    ("<code>readonly</code>", "<b>초점이 갑니다</b> — 읽히고 복사됩니다"),
    ("<code>aria-disabled</code>", "<b>초점이 가고 눌립니다</b> — 코드로 막고 이유를 띄웁니다"),
    ("<code>inert</code>", "영역 <b>전체</b>를 통째로 끕니다 — 뒤에 깔린 화면에 씁니다"),
    ("확인하는 법", "Tab 만으로 훑어 <b>못 고치는 칸의 값을 읽을 수 있나</b> 봅니다"),
  ]),
  backend=rows([
    ("폼 전송", "<code>disabled</code> 인 칸은 <b>요청에 아예 없습니다</b> — 서버가 '안 보냈다'와 '빈 값'을 구별해야 합니다."),
    ("서버도 막기", "화면에서 못 고치게 했다고 끝이 아닙니다 — <b>서버에서도</b> 그 칸을 무시하거나 막습니다."),
    ("이유를 내려 주기", "<code>{editable: false, reason: \"고객센터에서만 변경\"}</code> 처럼 <b>왜 안 되는지</b>를 같이 주면 화면이 적을 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>비활성</b>은 있지만 <b>읽기 전용</b>은 제각각입니다.",
  plats=plats([
    ("웹", "disabled · readonly",
     fd("123-45-67890", "ro", "", True, "108px", "readonly"),
     "<b>둘 다</b> 있습니다 — 그래서 고르는 실수가 납니다."),
    ("iOS", "isEnabled · isEditable",
     '''              <div class="phone" role="img" aria-label="iOS 읽기 전용 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:24px;height:17px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:9px;top:28px;width:34px;height:4px;border-radius:2px;background:var(--fg-muted);opacity:.5"></div></div></div>''',
     "<code>isEnabled = false</code> 는 <b>회색</b>이 되고, <code>isEditable = false</code> 는 <b>읽기 전용</b>입니다."),
    ("안드로이드", "enabled · readOnly",
     '''              <div class="phone" role="img" aria-label="안드로이드 읽기 전용 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:24px;height:17px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:9px;top:28px;width:34px;height:4px;border-radius:2px;background:var(--fg-muted);opacity:.5"></div></div></div>''',
     "Compose 의 <code>TextField</code> 에 <b><code>readOnly</code></b> 가 따로 있습니다."),
  ]),
  plat_note="어느 플랫폼이든 비활성은 <b>흐리게</b> 그려집니다 — 그래서 <b>대비비가 가장 먼저 무너지는 상태</b>입니다. 글자가 안 읽히면 '못 고친다'가 아니라 '<b>뭐라고 적혔는지 모른다</b>'가 되고, 그러면 비활성으로 둔 보람이 없습니다. 흐리게 두더라도 <b>4.5:1</b> 은 지키세요.",
  siblings=siblings("disabledstate"),
  related='''        <li><a href="permission.html"><b>권한 없음</b><em>11부</em></a></li>
        <li><a href="contrast.html"><b>명도 대비</b><em>12부</em></a></li>
        <li><a href="accordion.html"><b>아코디언</b><em>7부</em></a></li>
        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>''',
)
