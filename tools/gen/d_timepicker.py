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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">예약은 30분, 알람은 1분 간격으로 정함</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">쳐서도 넣을 수 있게 둠</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">24시간제라 12시가 낮인지 밤인지 안 헷갈림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">안 되는 시간은 흐리게 두고 막음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">목록이 길면 지금 시각 근처로 굴려 둠</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">시간대가 섞이면 함께 적음</div>
                </div>
              </div>'''

D = dict(
  slug="timepicker", ko="시간 선택기", en="Time picker",
  desc="시각을 고르는 부품인 시간 선택기에서 간격을 정하는 법과 24시간제, 고를 수 없는 시간을 막는 법을 다루는 항목입니다.",
  lede="하루의 시각은 분 단위로만 세어도 1,440가지라서 <b>가짓수가 많습니다</b>. 그래서 모든 시각을 늘어놓지 말고, 그 화면에서 <b>쓰는 간격</b>부터 정해야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>간격을 1분으로 바꿔 보세요. 데모가 <b>목록에 든 줄 수</b>를 세어 적어 주는데,
          1분 간격이면 <b>1,440줄</b>이나 됩니다.<br>
          그래서 예약이면 30분, 알람이면 1분처럼 쓰는 간격을 정해 두는 것이 핵심이고,
          목록을 굴리지 않고 <b>쳐서도 넣을 수 있어야</b> 합니다.<br>
          또 <b>오전/오후</b>로 적으면 '12시'가 낮인지 밤인지 알기 어렵기 때문에,
          한국에서는 <b>24시간제</b>로 적는 편이 덜 헷갈립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시간 선택기, 타임 피커, 시각 고르기"),
    ("영어", "time picker, time input"),
    ("같이 쓰는 말",
     "돌려서 맞추는 꼴은 <b>휠</b>(wheel picker), 시계판을 눌러 고르는 꼴은 <b>클록 다이얼</b>이라고 부릅니다. "
     "HTML에는 <code>&lt;input type=\"time\"&gt;</code>이 있고, "
     "날짜와 시각을 함께 고를 때는 <code>datetime-local</code>을 씁니다."),
    ("자주 잘못 부르는 이름",
     "<b>날짜 선택기</b> — <a href=\"datepicker.html\">날짜 선택기</a>는 시각이 아니라 <b>날</b>을 고르는 부품입니다.<br>"
     "<b>지속 시간</b> — '30분 동안'은 시각이 아니라 <b>길이</b>를 나타내는 값이라서 다른 부품으로 받습니다.<br>"
     "<b>타이머</b> — 타이머는 시간이 <b>흘러가는 것</b>을 보여 주는 부품이고, 시각을 고르는 부품이 아닙니다."),
  ]),
  axes=ax("시간 선택기"),
  oneline="<b>쓰는 간격을 먼저 정하세요.</b> 1분 간격으로 목록을 만들면 1,440줄이나 되어서 원하는 시각을 굴려 찾기 어렵습니다.",
  states=states([
    (tl([("14:00", False, False), ("14:30", True, False), ("15:00", False, False)], "", "30분 간격이면 48줄", True),
     "간격이 알맞을 때", "<b>예약은 30분</b> 간격이면 하루가 48줄이라 찾기 쉽습니다"),
    (tl([("00:00", False, False), ("00:01", False, False), ("00:02", False, False)], "", "1분 간격이면 1,440줄", False),
     "간격이 너무 촘촘할 때", "1분 간격이면 1,440줄이라 <b>굴려서는 찾기 어렵습니다</b>"),
    (tl([("08:30", False, True), ("09:00", True, False), ("09:30", False, False)], "", "영업 시간 밖은 막힘", True),
     "고를 수 없는 시간이 있을 때", "고를 수 없는 시간은 <b>흐리게</b> 표시하고 누르지 못하게 막습니다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">14:30</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">쳐서 한 번에 넣음</span>'),
         "쳐서 넣기", True, "", "152px"),
     "시각을 쳐서 넣을 때", "시각을 쳐서 넣으면 목록을 <b>굴리지 않아도</b> 됩니다"),
    (tl([("오전 12:00", False, False), ("오후 12:00", True, False)], "", "어느 쪽이 정오인지 헷갈림", False),
     "오전/오후로 적었을 때", "'12시'가 정오인지 자정인지 <b>헷갈립니다</b>"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">14:30 (KST)</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">시간대가 섞이면 함께 적음</span>'),
         "시간대", True, "", "152px"),
     "시간대가 섞일 때", "여러 시간대가 섞이는 화면이면 시간대를 <b>함께 적습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("간격", "가장 먼저 정하기", "예약은 30분, 알람은 1분처럼 쓰임에 맞춰 간격부터 정합니다"),
    ("쳐서 넣기", "입력 칸 함께 두기", "입력 칸을 같이 두면 목록을 굴리지 않고 바로 쳐 넣을 수 있습니다"),
    ("24시간제", "12시가 덜 헷갈림", "'12시'가 낮인지 밤인지 헷갈리는 <b>12시 문제</b>가 생기지 않습니다"),
    ("막힌 시간", "흐리게 표시하기", "고를 수 없는 시간을 흐리게 표시해 누르기 전에 알립니다"),
    ("첫 자리", "지금 시각 근처에서 열기", "목록이 길면 열 때 지금 시각 근처로 <b>굴려 둡니다</b>"),
    ("시간대", "섞일 때 적어 주기", "시간대가 섞이는 화면이면 '(KST)'처럼 시간대를 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>오전 12시 · 오후 12시</b>는 한국어에서 특히 헷갈리는 표기입니다.
          '오전 12시'를 자정으로 읽는 사람도 있고 정오로 읽는 사람도 있기 때문입니다.
          그래서 예약이나 마감처럼 <b>틀리면 안 되는 자리</b>에서는
          24시간제(<code>00:00</code>·<code>12:00</code>)로 적는 편이 안전합니다.<br>
          목록이 길 때는 <b>열었을 때 어디를 보여 주느냐</b>도 중요합니다.
          00:00부터 보여 주면 사용자 대부분이 원하는 시각까지 한참 굴려야 하는데,
          열 때 <b>지금 시각이나 이미 고른 값 근처</b>로 굴려 두면 그 수고를 덜 수 있습니다.</p>''',
  do=ul([
    "예약은 30분, 알람은 1분처럼 <b>쓰는 간격</b>을 정해 두기",
    "시각을 <b>24시간제</b>로 적기",
    "목록을 열었을 때 <b>지금 시각 가까이</b>를 보여 주기",
  ]),
  dont=ul([
    "1분 간격 목록을 <b>그대로 늘어놓기</b>. 1,440줄을 굴려 가며 찾아야 합니다",
    "<b>오전/오후</b> 표기로 12시를 적기. 정오인지 자정인지 헷갈립니다",
    "고를 수 없는 시간을 <b>눌리게</b> 두기. 누른 뒤에야 안 된다는 것을 알게 됩니다",
    "여러 시간대가 섞이는데 시간대를 <b>적지 않기</b>",
  ]),
  instead='시각이 아니라 날을 고르려면 <a href="datepicker.html">날짜 선택기</a>를 쓰고, 기간을 고르려면 <a href="daterange.html">날짜 범위</a>를 씁니다. 날짜와 시각을 어떤 형식으로 적을지는 <a href="datetime.html">날짜와 시간 쓰기</a>에서 다루고, 목록에서 값 하나를 고르는 일반적인 경우에는 <a href="select.html">셀렉트</a>가 맞습니다.',
  cases=cases([
    (tl([("14:00", False, False), ("14:30", True, False)], "", "", True, "150px"), "예약 시간 고르기", "예약 시간은 <b>30분</b> 간격으로 고릅니다"),
    (tl([("07:00", True, False), ("07:01", False, False)], "", "", True, "150px"), "알람 시각 맞추기", "알람은 분까지 맞춰야 하므로 <b>1분</b> 간격이 필요합니다"),
    (one(txt('<span style="display:block;font-size:8px;font-family:var(--mono)">18:00 마감</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">24시간제로 적음</span>'),
         "마감 시각", True, "", "150px"),
     "마감 시각 적기", "<b>틀리면 안 되는</b> 자리라서 24시간제로 적습니다"),
  ]),
  code_lede="브라우저 기본 시간 입력을 쓰면 휴대폰 자판까지 브라우저가 알아서 맞춰 줍니다. 간격은 <code>step</code>으로 정합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"t"</span>&gt;방문 시간&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"t"</span> <span class="a">type</span>=<span class="s">"time"</span>
       <span class="a">min</span>=<span class="s">"09:00"</span> <span class="a">max</span>=<span class="s">"18:00"</span>
       <span class="a">step</span>=<span class="s">"1800"</span>&gt;   <span class="c">&lt;!-- 1800초 = 30분 --&gt;</span>

<span class="c">// 직접 목록을 만들 때는 간격에 따라 줄 수가 정해진다</span>
<span class="t">const</span> rows = [];
<span class="t">for</span> (<span class="t">let</span> m = <span class="a">0</span>; m &lt; <span class="a">24</span> * <span class="a">60</span>; m += step) rows.push(m);
<span class="c">// step 30 → 48줄 · step 1 → 1440줄</span>''',
  keys=kbd([
    ("↑ ↓", "시나 분을 하나씩 올리고 내립니다"),
    ("← →", "시 칸과 분 칸 사이를 오갑니다"),
    ("숫자 키", "숫자를 바로 쳐 넣습니다. 시각을 넣는 <b>가장 빠른</b> 방법입니다"),
    ("<code>step</code>", "간격을 <b>초 단위</b>로 적습니다. 1800이면 30분 간격입니다"),
    ("<code>min</code>·<code>max</code>", "브라우저가 <b>범위를 막아</b> 줍니다"),
    ("확인하는 방법", "목록을 열었을 때 <b>지금 시각이 보이는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("시각만 주고받을 때", "시각만 다룰 때는 시간대 없이 <code>\"14:30\"</code>처럼 주고받아야 값이 <b>날짜와 섞이지</b> 않습니다."),
    ("날짜와 시각을 함께 주고받을 때", "날짜와 시각을 함께 다룰 때는 <b>ISO 8601</b> 형식(<code>2026-11-12T14:30+09:00</code>)으로 주는 편이 안전합니다."),
    ("예약할 수 있는 시간을 서버가 알려 주기", "서버가 영업 시간이나 예약 가능한 슬롯을 함께 내려 주면, 화면에서 고를 수 없는 시간을 미리 <b>막을 수</b> 있습니다."),
  ]),
  plat_lede="시각을 <b>고르는 방식</b>은 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "input type=\"time\"",
     tl([("14:00", False, False), ("14:30", True, False)], "", "", True, "110px"),
     "생김새는 브라우저마다 다르지만 <b>쳐서 넣기</b>는 어느 브라우저에서나 됩니다."),
    ("iOS", "DatePicker(.hourAndMinute)",
     '''              <div class="phone" role="img" aria-label="iOS 시간 휠 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:28px;height:18px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:12px;right:12px;top:34px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>휠</b>을 돌려 고르는 방식이 기본입니다. 손가락으로 돌리면 빠르지만, 지금 값에서 <b>먼 시각</b>까지 가려면 여전히 오래 돌려야 합니다."),
    ("안드로이드", "TimePicker",
     '''              <div class="phone" role="img" aria-label="안드로이드 시계판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:38px;transform:translate(-50%,-50%);width:26px;height:26px;border-radius:999px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:50%;top:38px;transform:translate(-50%,-50%);width:3px;height:3px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "<b>시계판</b>을 눌러 고르는 방식이 기본이고, <b>쳐서 넣기</b>로 바꾸는 단추가 따로 있습니다."),
  ]),
  plat_note="세 플랫폼 모두 결국 <b>쳐서 넣는 길</b>을 함께 둡니다. 휠이든 시계판이든 지금 값에서 <b>먼 시각</b>으로 옮기려면 느리기 때문입니다. 웹에서 직접 만들 때도 목록이나 휠을 만들되 <b>입력 칸은 없애지 않으면</b> 됩니다. 안드로이드 시계판은 보기에는 재미있지만 <b>정확히 14:37</b>처럼 분까지 맞춰야 하는 값을 고르기는 어렵습니다.",
  siblings=siblings("timepicker"),
  related='''        <li><a href="datepicker.html"><b>날짜 선택기</b><em>4부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="select.html"><b>셀렉트</b><em>4부</em></a></li>
        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>''',
)
