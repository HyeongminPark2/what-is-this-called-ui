# -*- coding: utf-8 -*-
from ax10 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def cal(start, end, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    cells = ''.join('<span style="aspect-ratio:1;display:grid;place-items:center;font-size:7.5px;border-radius:2px;'
                    + ('background:var(--accent);color:#fff;font-weight:700' if d in (start, end) else
                       'background:var(--accent-soft)' if start < d < end else '')
                    + '">' + str(d) + '</span>' for d in range(1, 29))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:6px;'
            'display:grid;grid-template-columns:repeat(7,1fr);gap:1px">' + cells + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">자주 쓰는 기간은 오늘 · 지난 7일 · 이번 달</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">달력은 그 뒤에, 대부분 버튼으로 고름</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">고른 범위를 한 줄로 다시 적음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">끝날을 포함한다고 화면에 적음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">서버에는 &lt; 다음 날 00:00으로 보냄</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">같은 날짜인데 하루가 적게 잡히는 오류</div>
                </div>
              </div>'''

D = dict(
  slug="daterange", ko="날짜 범위", en="Date range",
  desc="기간을 고르는 화면에서 자주 쓰는 기간 버튼이 달력보다 빠른 이유와, 끝날을 포함하는지에 따라 기간이 하루 달라지는 문제를 다루는 항목입니다.",
  lede="날짜 범위는 조회할 기간을 고르는 장치입니다. 대부분은 달력보다 <b>자주 쓰는 기간</b> 버튼으로 더 빨리 고를 수 있고, <b>끝날을 포함하는지</b>를 놓치면 기간이 하루 어긋나기 쉽습니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>달력에서 시작일과 끝날을 눌러 보세요. 실제로는 달력까지 가지 않고 <b>자주 쓰는 기간</b> 버튼만으로
          고르는 경우가 대부분입니다.<br>
          <b>끝날을 포함한다고 적기</b>를 꺼 보면 같은 날짜를 골라도 <b>하루 적은 기간</b>이 됩니다.
          화면에 적어 두지 않으면 사용자도 개발자도 알아채기 어려운 차이입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "날짜 범위, 기간 선택, 조회 기간"),
    ("영어", "date range, date range picker, period selector"),
    ("같이 쓰는 말",
     "미리 만들어 둔 기간 버튼은 <b>프리셋</b>(preset)·<b>퀵 레인지</b>, "
     "달력 두 장을 나란히 둔 것은 <b>듀얼 캘린더</b>라고 부릅니다. "
     "끝날을 포함하는지는 <b>경계 포함/제외</b>(inclusive / exclusive)라고 하는데, "
     "서버 질의에서는 보통 <code>&gt;= 시작</code>, <code>&lt; 끝+1일</code> 꼴로 적습니다."),
    ("자주 잘못 부르는 이름",
     "<b>날짜 선택기</b> — 날짜 선택기는 하루를 고르는 부품이고, 날짜 범위는 <b>두 날짜와 그 사이</b>를 다룹니다.<br>"
     "<b>필터</b> — 날짜 범위도 <a href=\"filter.html\">필터</a>의 한 갈래이지만, 정해진 값을 고르는 필터와는 <b>고르는 방식</b>이 전혀 다릅니다.<br>"
     "<b>기간</b> — '기간'이라는 말은 '3개월'처럼 길이를 뜻하기도 하고 '11월 1~7일'처럼 구간을 뜻하기도 하므로 어느 쪽인지 가려야 합니다."),
  ]),
  axes=ax("날짜 범위"),
  oneline="<b>자주 쓰는 기간 버튼을 먼저 두고, 달력은 그 뒤에 둡니다.</b> 그리고 끝날을 포함하는지 화면에 적어 두세요.",
  s4_title="기간을 고르는 과정", s4_hint="대부분은 버튼만으로 고릅니다",
  states=states([
    (one('<div style="display:flex;gap:3px;flex-wrap:wrap">'
         + ''.join('<span style="border:1px solid var(--line);border-radius:999px;padding:2px 7px;font-size:8px">' + t + '</span>'
                   for t in ['오늘', '지난 7일', '이번 달', '지난 달'])
         + '</div>', "자주 쓰는 기간", True, "대부분 이 버튼으로 고름"),
     "자주 쓰는 기간 버튼", "버튼 한 번으로 고를 수 있어서 <b>달력보다 빠릅니다</b>"),
    (cal(0, 0, "152px", "아직 고르지 않음"), "아직 고르지 않았을 때", "<b>무엇을 고르는 칸인지</b>만 보입니다"),
    (cal(3, 3, "152px", "시작일만 고름"), "시작일만 골랐을 때", "다음에 누르는 날짜가 <b>끝날</b>이 됩니다"),
    (cal(3, 9, "152px", "11월 3일 ~ 9일 · 7일간", True), "시작일과 끝날을 모두 골랐을 때", "시작일과 끝날 사이가 <b>칠해집니다</b>"),
    (one(txt('11월 1일 ~ 11월 7일 · <b>7일간</b><br><span style="color:var(--fg-muted)">끝날 포함</span>', "9.5px"), "범위 다시 적기", True, "고른 범위를 한 줄로 적음"),
     "고른 범위를 다시 적은 확인 줄", "고른 범위가 <b>며칠간인지</b>까지 적습니다"),
    (one(txt('11월 1일 ~ 11월 7일 · <b>6일간</b><br><span style="color:var(--danger)">끝날 제외</span>', "9.5px"), "끝날을 빼면", False, "같은 날짜인데 하루가 적음"),
     "끝날을 빼고 계산했을 때", "끝날을 빼면 같은 날짜라도 하루가 줄어드는데, 화면에 <b>적어 두지 않으면 알 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("프리셋", "오늘 · 지난 7일", "<b>대부분은 이 버튼만으로 고릅니다.</b> 그래서 달력보다 먼저 둡니다"),
    ("달력", "프리셋 다음", "정확한 날짜를 골라야 할 때만 씁니다"),
    ("확인 줄", "며칠간", "고른 범위를 <b>글로 다시</b> 적어 보여 줍니다"),
    ("끝날 포함", "화면에 적기", "<b>놓치기 쉬운 부분입니다.</b> 화면에 적지 않으면 끝날이 포함되는지 아무도 알 수 없습니다"),
    ("서버로 보내는 끝 경계", "&lt; 다음 날 00:00", "자료에 시·분·초가 붙어 있어도 끝날의 자료가 <b>빠지지 않습니다</b>"),
    ("하루 차이", "끝날 누락", "정산·마감 화면에서는 이 하루 때문에 <b>금액이 틀립니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          기간의 경계는 <b>두 군데에서 틀리기 쉽습니다</b>.
          하나는 <b>끝날을 포함하느냐</b>이고,
          다른 하나는 <b>시각이 붙은 자료</b>를 다룰 때입니다.
          '11월 7일까지'를 <code>&lt;= 11월 7일</code>로 적으면
          11월 7일 자료 가운데 시각이 <code>00:00</code>인 것만 들어오기 때문에
          <b>7일 낮에 생긴 자료가 모두 빠집니다</b>.
          <code>&lt; 11월 8일 00:00</code>으로 적으면 두 문제가 함께 해결되고,
          <a href="datetime.html">시간대</a>까지 맞추면 날짜가 하루 어긋나는 일도 없어집니다.</p>''',
  do_title="날짜 범위를 만들 때 지킬 것",
  dont_title="날짜 범위를 만들 때 피할 것",
  instead_title="날짜 범위 대신 쓸 것과 함께 볼 항목",
  do=ul([
    "<b>자주 쓰는 기간</b> 버튼을 달력보다 먼저 보여 주기",
    "고른 범위가 <b>며칠간인지</b>까지 적기",
    "끝날을 <b>포함한다고</b> 화면에 적기",
  ]),
  dont=ul([
    "달력만 두기. <b>대부분은 기간 버튼만으로 고를 수 있습니다</b>",
    "끝날 포함 여부를 적지 않기. 사용자와 서버가 생각하는 기간이 <b>하루 어긋납니다</b>",
    "시작일이 끝날보다 뒤인데도 <b>바로잡지 않고 두기</b>",
    "기간 제한을 두지 않기. <b>3년치</b>를 한 번에 조회하면 서버가 응답하지 못할 만큼 느려집니다",
  ]),
  instead='하루만 고르면 되는 경우에는 날짜 선택기를 쓰고, 기간 말고 다른 조건까지 함께 거르려면 <a href="filter.html">필터와 패싯</a>을 씁니다. 고른 날짜를 화면에 어떻게 적을지는 <a href="datetime.html">날짜와 시간 쓰기</a>에서 다룹니다.',
  cases=cases([
    (one('<div style="display:flex;gap:3px;flex-wrap:wrap">'
         + ''.join('<span style="border:1px solid var(--line);border-radius:999px;padding:2px 7px;font-size:8px">' + t + '</span>'
                   for t in ['오늘', '지난 7일', '이번 달'])
         + '</div>', "정산 화면", True, "대부분 이 세 버튼으로 고름"),
     "정산 화면에 기간 버튼 두기", "기간 버튼 한 줄이 날짜 범위에서 <b>효과가 가장 큰 부분</b>입니다"),
    (cal(3, 9, "150px", "달력에서 직접"), "정해진 날짜를 달력으로 고르기", "마감이나 감사처럼 <b>날짜가 정해진</b> 경우에 달력으로 직접 고릅니다"),
    (one(mono('?from=2026-11-01&to=2026-11-07', 'var(--accent)'), "주소에 담기", True, "공유·새로고침에도 유지됨"),
     "기간을 주소에 담기", "<a href=\"searchresults.html\">검색 결과 화면</a>과 같은 이유로 기간을 주소에 담습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="날짜 범위를 만들 때 꼭 갖출 것",
  code_lede="두 날짜는 한 묶음으로 묻고, 서버에는 끝 경계를 <b>다음 날 0시 미만</b>으로 열어 보냅니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;조회 기간&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"from"</span>&gt;시작&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"from"</span> <span class="a">type</span>=<span class="s">"date"</span> <span class="a">max</span>=<span class="s">"2026-11-07"</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"to"</span>&gt;끝&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"to"</span> <span class="a">type</span>=<span class="s">"date"</span> <span class="a">min</span>=<span class="s">"2026-11-01"</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;11월 1일 ~ 11월 7일 · 7일간 (끝날 포함)&lt;/<span class="t">p</span>&gt;

<span class="c">-- 끝을 다음 날 0시 미만으로 보내면 시각이 붙은 자료도 빠지지 않는다</span>
WHERE created_at &gt;= <span class="s">'2026-11-01 00:00'</span>
  AND created_at &lt;  <span class="s">'2026-11-08 00:00'</span>''',
  keys=kbd([
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "시작과 끝 두 칸이 <b>한 묶음</b>이라는 것을 알립니다"),
    ("<code>min</code>·<code>max</code>", "시작일이 끝날보다 뒤로 가지 못하게 합니다. 한쪽을 <b>고른 뒤</b> 다른 쪽의 제한을 갱신합니다"),
    ("<code>role=\"status\"</code>", "'7일간'처럼 기간이 바뀐 것을 알립니다. <b>달력만 칠해지면</b> 화면을 보지 못하는 사람은 알 수 없습니다"),
    ("<code>type=\"date\"</code>를 먼저 검토하기", "OS 달력은 <b>키보드와 스크린 리더</b>를 이미 지원하므로 먼저 검토합니다"),
    ("달력을 직접 만들 때", "<kbd>←</kbd><kbd>→</kbd>로 날짜를, <kbd>PageUp</kbd>으로 달을 옮길 수 있어야 합니다"),
    ("기간 버튼은 <code>&lt;button&gt;</code>으로 만들기", "버튼을 눌러 범위가 바뀌면 <code>status</code>로 알립니다"),
  ]),
  backend=rows([
    ("끝 경계를 다음 날 0시 미만으로 받기", "<code>&gt;= from</code>, <code>&lt; to+1일</code>로 받으면 <b>시각이 붙은 자료</b>도 빠지지 않습니다."),
    ("날짜를 자르는 시간대", "'11월 7일'이 어느 시간대 기준인지 정합니다. 자세한 내용은 <a href=\"datetime.html\">날짜와 시간 쓰기</a>에 있습니다."),
    ("조회할 수 있는 최대 기간", "3년치를 한 번에 조회하면 서버가 응답하지 못할 만큼 느려집니다. 조회할 수 있는 <b>최대 기간</b>을 정하고 화면에도 적습니다."),
    ("날짜 열의 색인", "<code>created_at</code>에 색인이 없으면 기간이 넓어질수록 느려집니다."),
    ("기간을 주소에 담기", "<code>?from=&to=</code>로 주소에 담아 두면 공유, 새로고침, 뒤로가기를 해도 같은 기간이 유지됩니다."),
  ]),
  plat_lede="세 플랫폼은 <b>OS 달력</b>을 그대로 쓸 수 있느냐가 다릅니다.",
  plats=plats([
    ("웹", "type=\"date\" 또는 직접",
     cal(3, 9, "110px"),
     "브라우저 달력은 따로 만들 필요가 없지만 <b>모양을 바꿀 수 없고</b> 범위도 고를 수 없어서, 직접 만드는 경우가 많습니다."),
    ("iOS", "DatePicker",
     '''              <div class="phone" role="img" aria-label="iOS 날짜 선택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;height:40%;background:var(--bg);border-radius:4px"></div></div></div>''',
     "OS가 달력과 휠을 제공하지만 <b>범위</b> 선택은 직접 만들어야 합니다."),
    ("안드로이드", "DateRangePicker",
     '''              <div class="phone" role="img" aria-label="Material 범위 선택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;bottom:6px;background:var(--bg);border-radius:4px"></div></div></div>''',
     "M3에는 <b>범위 전용 부품</b>이 있고, 전체 화면으로 열리는 것이 기본입니다."),
  ]),
  plat_note="\"기간으로 조회되게 해 주세요\"라는 요청에는 <b>끝날 포함 여부</b>가 거의 언제나 빠져 있습니다. 정산이나 매출처럼 숫자가 걸린 화면에서는 이 하루가 그대로 금액 차이가 되어, 나중에 \"숫자가 안 맞아요\"라는 문의로 돌아옵니다. 만들 때 <b>화면 문구와 질의 조건을 함께</b> 정해 적어 두면 이런 문의를 주고받을 일이 없어집니다.",
  siblings=siblings("daterange"),
  related='''        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
