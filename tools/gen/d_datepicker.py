# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def cal(sel=12, today=14, blockBefore=0, label="", note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    cells = ''.join('<span style="font-size:6px;color:var(--fg-muted);text-align:center">' + d + '</span>'
                    for d in ['일', '월', '화', '수', '목', '금', '토'])
    cells += '<span></span>' * 0
    for d in range(1, 31):
        off = d < blockBefore
        st = ''
        if d == sel: st = 'background:var(--accent);color:#fff;'
        elif d == today: st = 'box-shadow:inset 0 0 0 1px var(--accent);'
        elif off: st = 'color:var(--fg-faint);'
        cells += ('<span style="display:grid;place-items:center;aspect-ratio:1;font-size:6.5px;'
                  'border-radius:2px;' + st + '">' + str(d) + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);padding:5px">'
            '<span style="display:block;font-size:7px;font-weight:700;margin-bottom:3px">2026년 11월</span>'
            '<span style="display:grid;grid-template-columns:repeat(7,1fr);gap:1px">' + cells + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">쳐서 넣는 칸으로 먼 날짜도 한 번에</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">자주 쓰는 날 단추(오늘 · 어제 · 7일 전)</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">고른 날과 오늘은 서로 다르게 표시</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">못 고르는 날은 흐리게 두고 막음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">먼 날짜일수록 달을 여러 번 넘겨야 함</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">화살표 키로 날짜 사이를 옮김</div>
                </div>
              </div>'''

D = dict(
  slug="datepicker", ko="날짜 선택기", en="Date picker",
  do_title="날짜 선택기를 만들 때 지킬 것", dont_title="날짜 선택기를 만들 때 피할 것", instead_title="다른 부품이 맞는 경우와 함께 볼 항목",
  desc="달력으로 날짜를 고르는 부품과, 쳐서 넣기·자주 쓰는 날 단추·못 고르는 날을 다루는 방법을 보여 주는 항목입니다.",
  lede="날짜 선택기는 달력에서 날짜를 골라 넣는 부품입니다. 그런데 달력만 두면 <b>먼 날짜를 고를 때 달을 여러 번 넘겨야</b> 하므로, 쳐서 넣는 칸과 자주 쓰는 날 단추를 함께 두는 것이 요령입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>달력만 두면 먼 날짜를 고를 때 달을 몇 번이나 넘겨야 합니다.
          데모가 <b>달을 몇 번 넘겼는지</b> 세어 적는데, 칸에 쳐서 넣으면 <b>한 번</b>에 끝납니다.<br>
          <b>자주 쓰는 날 단추</b>(오늘 · 어제 · 7일 전)를 두면 대부분의 경우를 한 번에 고를 수 있습니다.<br>
          고를 수 없는 날은 <b>흐리게 두고 막아야</b> 합니다. 누를 수 있게 두면
          사용자는 날짜를 고른 뒤에야 '안 된다'는 말을 듣게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "날짜 선택기, 데이트 피커, 달력"),
    ("영어", "date picker, calendar picker, date input"),
    ("같이 쓰는 말",
     "시작과 끝을 함께 고르는 부품은 <b>날짜 범위 선택기</b>(date range picker)라고 하고, "
     "'지난 7일'처럼 미리 정해 둔 선택지는 <b>프리셋</b>이라고 부릅니다. "
     "HTML 에는 <code>&lt;input type=\"date\"&gt;</code> 가 있어 브라우저가 달력을 띄워 줍니다."),
    ("자주 잘못 부르는 이름",
     "<b>날짜 범위</b> — <a href=\"daterange.html\">날짜 범위</a>는 시작과 끝, <b>두 날짜</b>를 다룹니다.<br>"
     "<b>시간 선택기</b> — <a href=\"timepicker.html\">시간 선택기</a>는 날짜가 아니라 <b>시각</b>을 고릅니다.<br>"
     "<b>달력 화면</b> — 일정을 보는 달력은 날짜를 고르는 부품이 아니라 일정을 <b>보여 주는</b> 화면입니다."),
  ]),
  states=states([
    (cal(12, 14, 0, "", "고른 날과 오늘이 다르게 보임", True), "평소 상태", "<b>고른 날과 오늘</b>을 다르게 표시합니다"),
    (cal(12, 14, 10, "", "지난 정산 기간은 막혀 있음", True), "못 고르는 날을 막았을 때", "<b>흐리게</b> 두고 고를 수 없게 막습니다"),
    (cal(12, 14, 0, "", "다 눌려서 고른 뒤에야 거절됨", False), "못 고르는 날을 막지 않았을 때", "막지 않으면 사용자는 날짜를 <b>고른 뒤</b>에야 안 된다는 것을 압니다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">2026-12-25</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">한 번에 넣음</span>'),
         "쳐서 넣기", True, "", "152px"),
     "날짜를 쳐서 넣을 때", "<b>먼 날짜</b>를 넣을 때 씁니다"),
    (one(txt('<span style="display:flex;gap:3px;flex-wrap:wrap">'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">오늘</span>'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">어제</span>'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">7일 전</span></span>'),
         "자주 쓰는 날", True, "대부분 한 번에 끝남", "152px"),
     "자주 쓰는 날 단추를 둘 때", "단추를 누르면 <b>한 번</b>에 끝납니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">달을 7번 넘김</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">쳐서 넣으면 한 번에 끝남</span>'),
         "먼 날짜", False, "", "152px"),
     "먼 날짜를 달력으로 고를 때", "달력으로 고르면 <b>손이 많이 갑니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("쳐서 넣기", "먼 날짜에 알맞음", "먼 날짜도 <b>한 번</b>에 넣을 수 있습니다"),
    ("자주 쓰는 날", "오늘 · 어제", "대부분의 경우를 이 단추로 고를 수 있습니다"),
    ("고른 날과 오늘", "다르게 표시", "두 표시가 <b>헷갈리지 않게</b> 다르게 그립니다"),
    ("막힌 날", "흐리게 표시", "고를 수 없다는 것을 <b>누르기 전에</b> 알립니다"),
    ("달 넘기기", "먼 날짜일수록 여러 번", "먼 날짜일수록 여러 번 넘겨야 합니다"),
    ("화살표 키", "날짜 사이 이동", "키보드로도 날짜를 고를 수 있게 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          먼저 <b>브라우저 기본 <code>&lt;input type="date"&gt;</code></b> 로 충분한지 보세요.
          이것을 쓰면 쳐서 넣기, 키보드 조작, 폰 자판까지 따로 만들지 않아도 따라옵니다.
          반면 직접 만들면 이 기능을 하나하나 붙여야 하고, 대개 몇 가지는 빠뜨립니다.<br>
          날짜 선택기를 직접 만드는 이유는 보통 <b>자주 쓰는 날 단추</b>나
          <b>막힌 날 표시</b>가 필요해서인데, 이때도 <b>기본 입력 칸은 그대로 두고</b>
          달력만 그 위에 얹으면 기본 칸의 기능과 직접 만든 기능을 함께 쓸 수 있습니다.</p>''',
  do=ul([
    "<b>쳐서도 넣을 수</b> 있게 하기",
    "<b>자주 쓰는 날 단추</b> 두기",
    "못 고르는 날은 <b>흐리게 두고 막기</b>",
  ]),
  dont=ul([
    "달력만 두기. <b>먼 날짜</b>를 고르려면 달을 여러 번 넘겨야 합니다",
    "못 고르는 날을 <b>눌리게</b> 두기",
    "날짜 형식을 <b>자리마다 다르게</b> 쓰기. <a href=\"datetime.html\">날짜와 시간 쓰기</a>를 따릅니다",
    "달력을 <b>폰 화면에 작게</b> 욱여넣기. 날짜 칸 하나가 44px 이 되지 않습니다",
  ]),
  instead='시작과 끝 두 날짜를 고르게 하려면 <a href="daterange.html">날짜 범위</a>를, 날짜가 아니라 시각을 고르게 하려면 <a href="timepicker.html">시간 선택기</a>를 씁니다. 고른 날짜를 화면에 적는 형식은 <a href="datetime.html">날짜와 시간 쓰기</a>에서, 달력을 칸 위에 겹쳐 띄우는 방식은 <a href="popover.html">팝오버</a>에서 다룹니다.',
  cases=cases([
    (cal(12, 14, 10, "", "", True, "150px"), "지난 기간을 막은 정산 시작일", "이미 <b>지난 기간</b>은 고를 수 없게 막습니다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">1990-05-02</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">생년월일은 쳐서 넣음</span>'),
         "생년월일", True, "달력으로는 수백 번 넘겨야 함", "150px"),
     "생년월일은 쳐서 넣기", "<b>달력으로 고르기가 가장 불편한</b> 자리입니다"),
    (cal(14, 14, 0, "", "", True, "150px"), "오늘부터 고르는 예약일", "<b>오늘부터</b>만 고를 수 있게 합니다"),
  ]),
  code_lede="브라우저 기본 입력 칸을 쓰고, 모자란 기능만 그 위에 얹습니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"from"</span>&gt;정산 시작일&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"from"</span> <span class="a">type</span>=<span class="s">"date"</span>
       <span class="a">min</span>=<span class="s">"2026-11-10"</span> <span class="a">max</span>=<span class="s">"2026-12-31"</span> <span class="a">value</span>=<span class="s">"2026-11-12"</span>&gt;

<span class="c">&lt;!-- 자주 쓰는 날은 단추로 둔다. 대부분을 한 번에 끝낸다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"group"</span> <span class="a">aria-label</span>=<span class="s">"자주 쓰는 날"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">data-days</span>=<span class="s">"0"</span>&gt;오늘&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">data-days</span>=<span class="s">"-7"</span>&gt;7일 전&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 직접 만든 달력이라면 칸은 그대로 두고 달력만 얹는다</span>
input.addEventListener(<span class="s">'change'</span>, () =&gt; sync(input.value));''',
  keys=kbd([
    ("← → ↑ ↓", "날짜 사이를 옮깁니다. 위아래 화살표는 <b>한 주</b>씩 옮깁니다"),
    ("PageUp · PageDown", "<b>한 달</b>씩 넘깁니다"),
    ("Home · End", "그 주의 <b>처음과 마지막</b> 날로 갑니다"),
    ("Esc", "달력을 닫고 초점을 <b>입력 칸으로</b> 돌려보냅니다"),
    ("<code>min</code>·<code>max</code>", "고를 수 없는 날을 <b>브라우저가</b> 막아 줍니다"),
    ("키보드만으로 되는지 확인하는 방법", "마우스를 쓰지 않고 <b>세 달 뒤</b> 날짜를 골라 봅니다"),
  ]),
  backend=rows([
    ("시간대를 붙이지 않기", "날짜만 쓰는 값은 <code>2026-11-12</code> 처럼 <b>시간대 없이</b> 주고받습니다. UTC 로 바꾸면 시차 때문에 날짜가 하루 밀릴 수 있습니다."),
    ("고를 수 있는 범위 알려 주기", "서버가 <code>min</code>·<code>max</code> 를 알려 주면 화면이 그 범위 밖의 날을 <b>막을 수</b> 있습니다."),
    ("공휴일처럼 막을 날 목록 주기", "서버가 막아야 할 날 목록을 주면 그 날을 <b>달력에 표시</b>할 수 있습니다."),
  ]),
  plat_lede="플랫폼마다 <b>OS 가 띄우는 달력</b>의 모양이 다릅니다.",
  plats=plats([
    ("웹", "input type=\"date\"",
     cal(12, 14, 10, "", "", True, "110px"),
     "브라우저마다 생김새가 달라서 직접 만드는 경우가 많습니다."),
    ("iOS", "DatePicker",
     '''              <div class="phone" role="img" aria-label="iOS 날짜 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;height:22px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;right:8px;top:31px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>휠</b>이나 달력 중 고를 수 있습니다. 휠로 먼 날짜를 고르려면 특히 오래 걸립니다."),
    ("안드로이드", "DatePicker",
     '''              <div class="phone" role="img" aria-label="안드로이드 날짜 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;bottom:8px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:28px;width:5px;height:5px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "달력과 <b>쳐서 넣기</b>를 오가는 단추가 지침에 들어 있습니다."),
  ]),
  plat_note="Material 의 날짜 선택기에는 <b>달력 ↔ 쳐서 넣기 전환 단추</b>가 들어 있습니다. 가까운 날짜는 달력으로 고르는 편이 빠르고 먼 날짜는 쳐서 넣는 편이 빠르기 때문인데, 이 항목에서 권하는 방식과 같습니다. 웹에서 날짜 선택기를 직접 만든다면 <b>같은 전환 단추</b>를 두거나, 아예 <b>칸과 달력을 함께</b> 보여 주면 됩니다.",
  siblings=siblings("datepicker"),
  related='''        <li><a href="daterange.html"><b>날짜 범위</b><em>10부</em></a></li>
        <li><a href="timepicker.html"><b>시간 선택기</b><em>4부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="popover.html"><b>팝오버</b><em>6부</em></a></li>''',
)
