# -*- coding: utf-8 -*-
from ax4 import ax
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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">쳐서 넣는 칸 — 먼 날짜를 한 번에</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">자주 쓰는 날 단추 — 오늘 · 어제 · 7일 전</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">고른 날 · 오늘 — 서로 다르게 보인다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">못 고르는 날은 흐리게 두고 막는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">달 넘기기 — 먼 날짜일수록 품이 든다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">화살표 키로 날짜 사이를 옮긴다</div>
                </div>
              </div>'''

D = dict(
  slug="datepicker", ko="날짜 선택기", en="Date picker",
  desc="달력으로 날짜를 고르는 부품. 쳐서 넣기·자주 쓰는 날 단추·못 고르는 날 처리.",
  lede="달력만 두면 <b>먼 날짜가 멀어집니다</b>. 쳐서 넣는 칸과 자주 쓰는 날 단추를 같이 두는 것이 요령입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>달력만 두면 먼 날짜를 고를 때 몇 번이나 넘겨야 합니다 —
          데모가 <b>달을 몇 번 넘겼는지</b> 세서 적습니다. 쳐서 넣으면 <b>한 번</b>입니다.<br>
          <b>자주 쓰는 날 단추</b>(오늘 · 어제 · 7일 전)는 대부분의 경우를 한 번에 끝냅니다.<br>
          고를 수 없는 날은 <b>흐리게 두고 막아야</b> 합니다 — 누를 수 있게 두면
          고른 뒤에 '안 된다'는 말을 듣게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "날짜 선택기, 데이트 피커, 달력"),
    ("영어", "date picker, calendar picker, date input"),
    ("같이 쓰는 말",
     "시작과 끝을 함께 고르는 것은 <b>날짜 범위 선택기</b>(date range picker)이고, "
     "'지난 7일' 같은 미리 정해 둔 것은 <b>프리셋</b>입니다. "
     "HTML 에는 <code>&lt;input type=\"date\"&gt;</code> 가 있어 브라우저가 달력을 띄워 줍니다."),
    ("자주 잘못 부름",
     "<b>날짜 범위</b> — <a href=\"daterange.html\">날짜 범위</a>는 <b>두 날짜</b>를 다룹니다.<br>"
     "<b>시간 선택기</b> — <a href=\"timepicker.html\">시간 선택기</a>는 <b>시각</b>을 고릅니다.<br>"
     "<b>달력 화면</b> — 일정을 보는 달력은 <b>보기</b>이지 고르는 부품이 아닙니다."),
  ]),
  axes=ax("날짜 선택기"),
  oneline="<b>칸에 쳐서도 넣을 수 있게 하세요.</b> 달력만으로는 먼 날짜가 너무 멉니다.",
  states=states([
    (cal(12, 14, 0, "", "고른 날과 오늘이 다르게 보인다", True), "기본", "<b>고른 날 · 오늘</b>"),
    (cal(12, 14, 10, "", "지난 정산 기간은 막혔다", True), "막힌 날", "<b>흐리게</b> 두고 막는다"),
    (cal(12, 14, 0, "", "다 눌린다 — 고른 뒤에 거절당한다", False), "안 막음", "<b>고른 뒤</b>에야 안다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">2026-12-25</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">한 번에 넣었다</span>'),
         "쳐서 넣기", True, "", "152px"),
     "쳐서 넣기", "<b>먼 날짜</b>에 쓴다"),
    (one(txt('<span style="display:flex;gap:3px;flex-wrap:wrap">'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">오늘</span>'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">어제</span>'
             '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;font-size:7px">7일 전</span></span>'),
         "자주 쓰는 날", True, "대부분을 한 번에 끝낸다", "152px"),
     "자주 쓰는 날", "<b>한 번</b>에 끝난다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">달을 7번 넘겼다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">쳐서 넣으면 한 번이다</span>'),
         "먼 날짜", False, "", "152px"),
     "먼 날짜", "<b>품이 는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("쳐서 넣기", "먼 날짜", "<b>한 번</b>에 끝난다"),
    ("자주 쓰는 날", "오늘 · 어제", "대부분을 덮는다"),
    ("고른 날 · 오늘", "다르게", "둘을 <b>섞지 않는다</b>"),
    ("막힌 날", "흐리게", "<b>누르기 전에</b> 알린다"),
    ("달 넘기기", "품이 듦", "먼 날짜일수록"),
    ("화살표 키", "날짜 사이", "키보드로도 고른다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>브라우저 기본 <code>&lt;input type="date"&gt;</code></b> 를 먼저 보세요 —
          쳐서 넣기·키보드·폰 자판까지 공짜로 따라옵니다.
          직접 만들면 그 전부를 손으로 붙여야 하고, 대개 몇 개는 빠집니다.<br>
          직접 만들어야 하는 이유는 보통 <b>자주 쓰는 날 단추</b>나
          <b>막힌 날 표시</b> 때문인데, 그때도 <b>칸은 그대로 두고</b>
          달력만 얹는 꼴이면 둘 다 얻을 수 있습니다.</p>''',
  do=ul([
    "<b>쳐서도 넣을 수</b> 있게 하기",
    "<b>자주 쓰는 날 단추</b> 두기",
    "못 고르는 날은 <b>흐리게 두고 막기</b>",
  ]),
  dont=ul([
    "달력만 두기 — <b>먼 날짜</b>가 멀어진다",
    "못 고르는 날을 <b>눌리게</b> 두기",
    "날짜 꼴을 <b>자리마다 다르게</b> 쓰기 — <a href=\"datetime.html\">날짜와 시간 쓰기</a>를 따른다",
    "달력을 <b>폰에서 작게</b> 욱여넣기 — 44px 이 안 나온다",
  ]),
  instead='두 날짜면 <a href="daterange.html">날짜 범위</a>, 시각이면 <a href="timepicker.html">시간 선택기</a>, 적는 꼴은 <a href="datetime.html">날짜와 시간 쓰기</a>, 겹쳐 뜨면 <a href="popover.html">팝오버</a>.',
  cases=cases([
    (cal(12, 14, 10, "", "", True, "150px"), "정산 시작일", "<b>지난 기간</b>은 막는다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">1990-05-02</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">생년월일은 쳐서</span>'),
         "생년월일", True, "달력으로는 수백 번 넘겨야 한다", "150px"),
     "생년월일", "<b>달력이 최악</b>인 자리"),
    (cal(14, 14, 0, "", "", True, "150px"), "예약일", "<b>오늘부터</b>만 고르게"),
  ]),
  code_lede="브라우저 기본을 쓰고, 모자란 것만 얹습니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"from"</span>&gt;정산 시작일&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"from"</span> <span class="a">type</span>=<span class="s">"date"</span>
       <span class="a">min</span>=<span class="s">"2026-11-10"</span> <span class="a">max</span>=<span class="s">"2026-12-31"</span> <span class="a">value</span>=<span class="s">"2026-11-12"</span>&gt;

<span class="c">&lt;!-- 자주 쓰는 날은 단추로 — 대부분을 한 번에 끝낸다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"group"</span> <span class="a">aria-label</span>=<span class="s">"자주 쓰는 날"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">data-days</span>=<span class="s">"0"</span>&gt;오늘&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">data-days</span>=<span class="s">"-7"</span>&gt;7일 전&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 직접 만든 달력이라면 칸은 그대로 두고 달력만 얹는다</span>
input.addEventListener(<span class="s">'change'</span>, () =&gt; sync(input.value));''',
  keys=kbd([
    ("← → ↑ ↓", "날짜 사이를 옮긴다 — 위아래는 <b>한 주</b>"),
    ("PageUp · PageDown", "<b>한 달</b>씩 넘긴다"),
    ("Home · End", "그 주의 <b>처음 · 마지막</b>"),
    ("Esc", "달력을 닫고 초점을 <b>칸으로</b>"),
    ("<code>min</code>·<code>max</code>", "못 고르는 날을 <b>브라우저가</b> 막아 준다"),
    ("확인하는 법", "마우스를 안 쓰고 <b>세 달 뒤</b> 날짜를 골라 본다"),
  ]),
  backend=rows([
    ("시간대", "날짜만 쓰는 값은 <code>2026-11-12</code> 처럼 <b>시간대 없이</b> 주고받습니다 — UTC 로 바꾸면 하루가 밀립니다."),
    ("고를 수 있는 범위", "<code>min</code>·<code>max</code> 를 서버가 주면 화면이 <b>막을 수</b> 있습니다."),
    ("공휴일", "막아야 할 날 목록이 있으면 <b>달력에 표시</b>할 수 있습니다."),
  ]),
  plat_lede="<b>OS 가 띄우는 달력</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "input type=\"date\"",
     cal(12, 14, 10, "", "", True, "110px"),
     "브라우저마다 생김새가 다릅니다 — 그래서 직접 만드는 일이 잦습니다."),
    ("iOS", "DatePicker",
     '''              <div class="phone" role="img" aria-label="iOS 날짜 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;height:22px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;right:8px;top:31px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>휠</b>이나 달력 중 고를 수 있습니다. 휠은 먼 날짜에 특히 느립니다."),
    ("안드로이드", "DatePicker",
     '''              <div class="phone" role="img" aria-label="안드로이드 날짜 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;bottom:8px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:28px;width:5px;height:5px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "달력과 <b>쳐서 넣기</b>를 오가는 단추가 지침에 들어 있습니다."),
  ]),
  plat_note="Material 의 날짜 선택기에 <b>달력 ↔ 쳐서 넣기 전환 단추</b>가 들어 있는 것은 이 항목의 핵심을 그대로 담은 설계입니다 — 가까운 날짜는 달력이, 먼 날짜는 치기가 빠릅니다. 웹에서도 직접 만든다면 <b>그 전환을 흉내</b> 내거나, 아예 <b>칸과 달력을 같이</b> 보여 주면 됩니다.",
  siblings=siblings("datepicker"),
  related='''        <li><a href="daterange.html"><b>날짜 범위</b><em>10부</em></a></li>
        <li><a href="timepicker.html"><b>시간 선택기</b><em>4부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="popover.html"><b>팝오버</b><em>6부</em></a></li>''',
)
