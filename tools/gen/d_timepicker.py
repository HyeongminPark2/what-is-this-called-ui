# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def tl(items, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = ''.join('<span style="display:block;padding:2px 6px;font-size:7.5px;font-family:var(--mono);'
                  + ('background:var(--accent-soft);color:var(--accent);' if on else
                     ('color:var(--fg-faint);' if off else '')) + '">' + t + '</span>'
                  for t, on, off in items)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:4px;max-height:62px;overflow:hidden">' + out + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">쓰는 간격을 정한다 — 예약 30분, 알람 1분</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">쳐서도 넣을 수 있게</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">24시간제 — 12시가 낮인지 밤인지 안 헷갈린다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">안 되는 시간은 흐리게 두고 막는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">목록이 길면 지금 시각 가까이로 굴려 둔다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">시간대가 있으면 같이 적는다</div>
                </div>
              </div>'''

D = dict(
  slug="timepicker", ko="시간 선택기", en="Time picker",
  desc="시각을 고르는 부품. 간격 정하기, 24시간제, 안 되는 시간 막기.",
  lede="시간은 <b>가짓수가 많습니다</b>. 다 늘어놓지 말고 <b>쓰는 간격</b>을 먼저 정해야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>간격을 1분으로 바꿔 보세요 — 데모가 <b>목록에 든 줄 수</b>를 세서 적습니다
          (1분 간격이면 <b>1,440줄</b>입니다).<br>
          그래서 쓰는 간격을 정해 두는 것이 핵심입니다 — 예약이면 30분, 알람이면 1분.
          그리고 <b>쳐서도 넣을 수 있어야</b> 합니다.<br>
          <b>오전/오후</b>로 적으면 '12시'가 낮인지 밤인지 헷갈립니다 —
          한국에서는 <b>24시간제</b>가 덜 헷갈립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시간 선택기, 타임 피커, 시각 고르기"),
    ("영어", "time picker, time input"),
    ("같이 쓰는 말",
     "돌려 맞추는 꼴은 <b>휠</b>(wheel picker), 시계판을 누르는 꼴은 <b>클록 다이얼</b>입니다. "
     "HTML 에는 <code>&lt;input type=\"time\"&gt;</code> 이 있고, "
     "날짜와 시각을 같이 고르는 것은 <code>datetime-local</code> 입니다."),
    ("자주 잘못 부름",
     "<b>날짜 선택기</b> — <a href=\"datepicker.html\">날짜 선택기</a>는 <b>날</b>을 고릅니다.<br>"
     "<b>지속 시간</b> — '30분 동안'은 시각이 아니라 <b>길이</b>라 다른 부품입니다.<br>"
     "<b>타이머</b> — 타이머는 <b>흘러가는 것</b>이지 고르는 것이 아닙니다."),
  ]),
  axes=ax("시간 선택기"),
  oneline="<b>쓰는 간격을 먼저 정하세요.</b> 1분 간격 목록은 1,440줄입니다.",
  states=states([
    (tl([("14:00", False, False), ("14:30", True, False), ("15:00", False, False)], "", "30분 간격 — 48줄", True),
     "알맞은 간격", "<b>예약은 30분</b>"),
    (tl([("00:00", False, False), ("00:01", False, False), ("00:02", False, False)], "", "1분 간격 — 1,440줄", False),
     "너무 촘촘함", "<b>굴려서 못 찾는다</b>"),
    (tl([("08:30", False, True), ("09:00", True, False), ("09:30", False, False)], "", "영업 시간 밖은 막혔다", True),
     "막힌 시간", "<b>흐리게</b> 두고 막는다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">14:30</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">쳐서 한 번에</span>'),
         "쳐서 넣기", True, "", "152px"),
     "쳐서 넣기", "<b>굴리지 않아도</b> 된다"),
    (tl([("오전 12:00", False, False), ("오후 12:00", True, False)], "", "둘 중 어느 쪽이 정오인가", False),
     "오전/오후", "<b>12시가 헷갈린다</b>"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">14:30 (KST)</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">시간대가 섞이면 적는다</span>'),
         "시간대", True, "", "152px"),
     "시간대", "섞이면 <b>적는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("간격", "먼저 정하기", "예약 30분 · 알람 1분"),
    ("쳐서 넣기", "같이 두기", "굴리지 않아도 된다"),
    ("24시간제", "덜 헷갈림", "<b>12시 문제</b>가 없다"),
    ("막힌 시간", "흐리게", "누르기 전에 알린다"),
    ("첫 자리", "지금 가까이", "목록이 길면 <b>굴려 둔다</b>"),
    ("시간대", "섞이면 적기", "'(KST)'"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>오전 12시 · 오후 12시</b>는 한국어에서 특히 헷갈립니다 —
          '오전 12시'를 자정으로 읽는 사람과 정오로 읽는 사람이 둘 다 있습니다.
          그래서 예약·마감처럼 <b>틀리면 안 되는 자리</b>에서는
          24시간제(<code>00:00</code>·<code>12:00</code>)가 안전합니다.<br>
          목록이 길 때는 <b>열었을 때 어디를 보여 주느냐</b>도 중요합니다 —
          00:00 부터 보여 주면 대부분 한참 굴려야 합니다.
          <b>지금 시각이나 고른 값 근처</b>로 굴려 두면 그 수고가 사라집니다.</p>''',
  do=ul([
    "<b>쓰는 간격</b>을 정하기 — 예약 30분, 알람 1분",
    "<b>24시간제</b>로 적기",
    "열었을 때 <b>지금 시각 가까이</b>를 보여 주기",
  ]),
  dont=ul([
    "1분 간격 목록을 <b>그냥 늘어놓기</b>",
    "<b>오전/오후</b>로 적고 12시를 쓰기",
    "안 되는 시간을 <b>눌리게</b> 두기",
    "시간대가 섞이는데 <b>안 적기</b>",
  ]),
  instead='날이면 <a href="datepicker.html">날짜 선택기</a>, 적는 꼴은 <a href="datetime.html">날짜와 시간 쓰기</a>, 범위면 <a href="daterange.html">날짜 범위</a>, 값 고르기 일반은 <a href="select.html">셀렉트</a>.',
  cases=cases([
    (tl([("14:00", False, False), ("14:30", True, False)], "", "", True, "150px"), "예약", "<b>30분</b> 간격"),
    (tl([("07:00", True, False), ("07:01", False, False)], "", "", True, "150px"), "알람", "<b>1분</b>이 필요하다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">18:00 마감</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">24시간제로 못박는다</span>'),
         "마감 시각", True, "", "150px"),
     "마감", "<b>틀리면 안 되는</b> 자리"),
  ]),
  code_lede="브라우저 기본이 폰 자판까지 맡아 줍니다. 간격은 <code>step</code> 으로 정합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"t"</span>&gt;방문 시간&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"t"</span> <span class="a">type</span>=<span class="s">"time"</span>
       <span class="a">min</span>=<span class="s">"09:00"</span> <span class="a">max</span>=<span class="s">"18:00"</span>
       <span class="a">step</span>=<span class="s">"1800"</span>&gt;   <span class="c">&lt;!-- 1800초 = 30분 --&gt;</span>

<span class="c">// 직접 목록을 만들 때 — 간격이 곧 줄 수다</span>
<span class="t">const</span> rows = [];
<span class="t">for</span> (<span class="t">let</span> m = <span class="a">0</span>; m &lt; <span class="a">24</span> * <span class="a">60</span>; m += step) rows.push(m);
<span class="c">// step 30 → 48줄 · step 1 → 1440줄</span>''',
  keys=kbd([
    ("↑ ↓", "시·분을 하나씩 올리고 내린다"),
    ("← →", "시와 분 사이를 옮긴다"),
    ("숫자 키", "바로 쳐 넣는다 — <b>가장 빠른</b> 길"),
    ("<code>step</code>", "간격을 <b>초 단위</b>로 적는다 (1800 = 30분)"),
    ("<code>min</code>·<code>max</code>", "브라우저가 <b>범위를 막아</b> 준다"),
    ("확인하는 법", "목록을 열고 <b>지금 시각이 보이는지</b> 본다"),
  ]),
  backend=rows([
    ("시각만", "시간대 없이 <code>\"14:30\"</code> 으로 주고받는 쪽이 <b>날짜와 섞이지</b> 않습니다."),
    ("시각 + 날짜", "둘이 함께면 <b>ISO 8601</b>(<code>2026-11-12T14:30+09:00</code>)로 주는 편이 안전합니다."),
    ("되는 시간", "영업 시간이나 예약 가능 슬롯을 주면 화면이 <b>막을 수</b> 있습니다."),
  ]),
  plat_lede="<b>고르는 방식</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "input type=\"time\"",
     tl([("14:00", False, False), ("14:30", True, False)], "", "", True, "110px"),
     "브라우저마다 생김새가 다르지만 <b>쳐서 넣기</b>는 어디서나 됩니다."),
    ("iOS", "DatePicker(.hourAndMinute)",
     '''              <div class="phone" role="img" aria-label="iOS 시간 휠 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:28px;height:18px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:12px;right:12px;top:34px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>휠</b>이 기본입니다. 손가락으로는 빠른데 <b>먼 시각</b>은 여전히 느립니다."),
    ("안드로이드", "TimePicker",
     '''              <div class="phone" role="img" aria-label="안드로이드 시계판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:38px;transform:translate(-50%,-50%);width:26px;height:26px;border-radius:999px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:50%;top:38px;transform:translate(-50%,-50%);width:3px;height:3px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "<b>시계판</b>을 눌러 고르고, <b>쳐서 넣기</b>로 바꾸는 단추가 있습니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>쳐서 넣는 길</b>을 결국 같이 둡니다 — 휠이든 시계판이든 <b>먼 시각</b>에는 느리기 때문입니다. 웹에서 직접 만든다면 그 교훈만 가져오면 됩니다: 목록이나 휠을 만들더라도 <b>칸을 없애지 않는 것</b>. 안드로이드 시계판은 보기에 재미있지만 <b>정확히 14:37</b> 같은 값에는 쓰기 어렵습니다.",
  siblings=siblings("timepicker"),
  related='''        <li><a href="datepicker.html"><b>날짜 선택기</b><em>4부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="select.html"><b>셀렉트</b><em>4부</em></a></li>
        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>''',
)
