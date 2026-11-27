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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">자주 쓰는 기간 — 오늘 · 지난 7일 · 이번 달</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">달력은 그 뒤 — 대부분은 버튼으로 끝난다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">고른 범위를 한 줄로 다시 적는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">끝날을 포함한다고 화면에 적는다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">서버에는 &lt; 다음 날 00:00 으로 보낸다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">같은 날짜인데 하루가 적은 사고</div>
                </div>
              </div>'''

D = dict(
  slug="daterange", ko="날짜 범위", en="Date range",
  desc="기간을 고르는 화면. 자주 쓰는 기간이 달력보다 빠르고, 끝날 포함 여부가 숨은 함정이다.",
  lede="기간을 고르는 일. <b>자주 쓰는 기간</b>이 달력보다 빠르고, <b>끝날을 포함하는가</b>가 숨은 함정입니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>달력에서 시작일과 끝날을 눌러 보세요. <b>자주 쓰는 기간</b> 버튼이
          실제로는 대부분을 끝냅니다.<br>
          <b>끝날을 포함한다고 적기</b>를 꺼 보면 같은 날짜가 <b>하루 적은 기간</b>이 됩니다 —
          화면에 적어 두지 않으면 아무도 모르는 차이입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "날짜 범위, 기간 선택, 조회 기간"),
    ("영어", "date range, date range picker, period selector"),
    ("같이 쓰는 말",
     "미리 만들어 둔 기간 버튼이 <b>프리셋</b>(preset)·<b>퀵 레인지</b>이고, "
     "달력 두 장을 나란히 두는 것이 <b>듀얼 캘린더</b>입니다. "
     "끝날을 포함하는지를 <b>경계 포함/제외</b>(inclusive / exclusive)라 하고, "
     "서버 질의에서는 <code>&gt;= 시작</code>, <code>&lt; 끝+1일</code> 꼴로 적는 것이 보통입니다."),
    ("자주 잘못 부름",
     "<b>날짜 선택기</b> — 하루를 고르는 부품입니다. 범위는 <b>두 날짜와 그 사이</b>를 다룹니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터</a>의 한 갈래이긴 하지만 <b>고르는 방식</b>이 전혀 다릅니다.<br>"
     "<b>기간</b> — '3개월'처럼 길이를 뜻하기도 하고 '11월 1~7일'처럼 구간을 뜻하기도 합니다."),
  ]),
  axes=ax("날짜 범위"),
  oneline="<b>자주 쓰는 기간을 먼저, 달력은 그 뒤에.</b> 그리고 끝날을 포함한다고 화면에 적으세요.",
  s4_title="고르는 네 토막", s4_hint="대부분은 버튼으로 끝난다",
  states=states([
    (one('<div style="display:flex;gap:3px;flex-wrap:wrap">'
         + ''.join('<span style="border:1px solid var(--line);border-radius:999px;padding:2px 7px;font-size:8px">' + t + '</span>'
                   for t in ['오늘', '지난 7일', '이번 달', '지난 달'])
         + '</div>', "자주 쓰는 기간", True, "실제로 대부분을 끝낸다"),
     "프리셋", "<b>달력보다 빠르다</b>"),
    (cal(0, 0, "152px", "아직 안 골랐다"), "비었을 때", "<b>무엇을 고르는지</b>만 보인다"),
    (cal(3, 3, "152px", "시작일을 골랐다"), "하나 골랐을 때", "다음 누름이 <b>끝날</b>이 된다"),
    (cal(3, 9, "152px", "11월 3일 ~ 9일 · 7일간", True), "둘 다 골랐을 때", "사이가 <b>칠해진다</b>"),
    (one(txt('11월 1일 ~ 11월 7일 · <b>7일간</b><br><span style="color:var(--fg-muted)">끝날 포함</span>', "9.5px"), "다시 적기", True, "고른 범위를 한 줄로"),
     "확인 줄", "<b>며칠간인지</b>까지 적는다"),
    (one(txt('11월 1일 ~ 11월 7일 · <b>6일간</b><br><span style="color:var(--danger)">끝날 제외</span>', "9.5px"), "끝날을 빼면", False, "같은 날짜인데 하루가 적다"),
     "숨은 함정", "<b>적어 두지 않으면 모른다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("프리셋", "오늘 · 지난 7일", "<b>대부분을 끝낸다.</b> 달력보다 먼저 둔다"),
    ("달력", "그 뒤", "정확한 날이 필요할 때만"),
    ("확인 줄", "며칠간", "고른 것을 <b>말로 다시</b> 적는다"),
    ("끝날 포함", "화면에 적는다", "<b>숨은 함정.</b> 안 적으면 아무도 모른다"),
    ("서버로는", "&lt; 다음 날 00:00", "시·분·초가 있어도 <b>안 샌다</b>"),
    ("하루 차이", "가장 흔한 사고", "정산·마감에서는 <b>돈이 틀린다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>경계는 두 번 틀립니다.</b>
          한 번은 <b>끝날을 포함하느냐</b>에서,
          또 한 번은 <b>시각이 붙은 자료</b>에서입니다.
          '11월 7일까지'를 <code>&lt;= 11월 7일</code>로 적으면
          시각이 <code>00:00</code>인 것만 들어와
          <b>7일 낮에 생긴 자료가 통째로 빠집니다</b>.
          <code>&lt; 11월 8일 00:00</code>으로 적으면 둘 다 해결되고,
          <a href="datetime.html">시간대</a>까지 맞추면 날짜가 하루 어긋나는 일도 사라집니다.</p>''',
  do=ul([
    "<b>자주 쓰는 기간</b>을 먼저 보여 주기",
    "고른 범위를 <b>며칠간인지</b>까지 적기",
    "끝날을 <b>포함한다고</b> 화면에 쓰기",
  ]),
  dont=ul([
    "달력만 두기 — <b>대부분은 버튼이면 끝난다</b>",
    "끝날 포함 여부를 안 적기 — <b>하루가 어긋난다</b>",
    "시작일이 끝날보다 뒤여도 <b>그냥 두기</b>",
    "기간 제한 없이 — <b>3년치</b>를 한 번에 부르면 서버가 멎는다",
  ]),
  instead='하루만 고르면 날짜 선택기, 조건 전체는 <a href="filter.html">필터와 패싯</a>, 적는 법은 <a href="datetime.html">날짜와 시간 쓰기</a>.',
  cases=cases([
    (one('<div style="display:flex;gap:3px;flex-wrap:wrap">'
         + ''.join('<span style="border:1px solid var(--line);border-radius:999px;padding:2px 7px;font-size:8px">' + t + '</span>'
                   for t in ['오늘', '지난 7일', '이번 달'])
         + '</div>', "정산 화면", True, "거의 이 셋으로 끝난다"),
     "자주 쓰는 기간", "<b>가장 효과 큰 한 줄</b>"),
    (cal(3, 9, "150px", "달력에서 직접"), "정확한 기간", "마감·감사처럼 <b>날이 정해진</b> 경우"),
    (one(mono('?from=2026-11-01&to=2026-11-07', 'var(--accent)'), "주소에 담기", True, "공유·새로고침이 된다"),
     "주소", "<a href=\"searchresults.html\">검색 결과 화면</a>과 같은 이유"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 기간의 계약서",
  code_lede="두 날짜를 묶음으로 묻고, 서버에는 <b>경계를 열어</b> 보냅니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;조회 기간&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"from"</span>&gt;시작&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"from"</span> <span class="a">type</span>=<span class="s">"date"</span> <span class="a">max</span>=<span class="s">"2026-11-07"</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"to"</span>&gt;끝&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"to"</span> <span class="a">type</span>=<span class="s">"date"</span> <span class="a">min</span>=<span class="s">"2026-11-01"</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;11월 1일 ~ 11월 7일 · 7일간 (끝날 포함)&lt;/<span class="t">p</span>&gt;

<span class="c">-- 서버에는 경계를 열어 보낸다 — 시각이 붙어 있어도 안 샌다</span>
WHERE created_at &gt;= <span class="s">'2026-11-01 00:00'</span>
  AND created_at &lt;  <span class="s">'2026-11-08 00:00'</span>''',
  keys=kbd([
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "두 칸이 <b>한 묶음</b>임을 알린다"),
    ("<code>min</code>·<code>max</code>", "시작이 끝보다 뒤로 못 가게. <b>고른 뒤</b> 서로 갱신한다"),
    ("<code>role=\"status\"</code>", "'7일간'이 바뀐 것을 알린다. <b>달력만 칠해지면</b> 안 보이는 사람은 모른다"),
    ("<code>type=\"date\"</code>를 먼저 본다", "OS 달력이 <b>키보드·스크린 리더</b>를 이미 지원한다"),
    ("직접 만든 달력", "<kbd>←</kbd><kbd>→</kbd>로 날짜를, <kbd>PageUp</kbd>으로 달을 옮겨야 한다"),
    ("프리셋은 <code>&lt;button&gt;</code>", "눌러서 범위가 바뀐 것을 <code>status</code>로 알린다"),
  ]),
  backend=rows([
    ("경계를 열어 받는다", "<code>&gt;= from</code>, <code>&lt; to+1일</code>. <b>시각이 붙은 자료</b>가 안 샙니다."),
    ("시간대", "'11월 7일'이 누구 기준인지 정합니다 — <a href=\"datetime.html\">날짜와 시간 쓰기</a>."),
    ("기간 제한", "3년치를 한 번에 부르면 멎습니다. <b>최대 기간</b>을 정하고 화면에도 적습니다."),
    ("색인", "<code>created_at</code>에 색인이 없으면 기간이 넓어질수록 느려집니다."),
    ("주소에 담는다", "<code>?from=&to=</code>. 공유·새로고침·뒤로가기가 한꺼번에 됩니다."),
  ]),
  plat_lede="<b>OS 달력</b>을 쓰느냐가 갈립니다.",
  plats=plats([
    ("웹", "type=\"date\" 또는 직접",
     cal(3, 9, "110px"),
     "브라우저 달력은 공짜지만 <b>모양을 못 바꾸고</b> 범위도 안 됩니다. 그래서 직접 만드는 일이 많습니다."),
    ("iOS", "DatePicker",
     '''              <div class="phone" role="img" aria-label="iOS 날짜 선택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;height:40%;background:var(--bg);border-radius:4px"></div></div></div>''',
     "OS 가 달력과 휠을 줍니다. <b>범위</b>는 직접 만들어야 합니다."),
    ("안드로이드", "DateRangePicker",
     '''              <div class="phone" role="img" aria-label="Material 범위 선택 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;bottom:6px;background:var(--bg);border-radius:4px"></div></div></div>''',
     "M3 에 <b>범위 전용 부품</b>이 있습니다. 전체 화면으로 열리는 것이 기본입니다."),
  ]),
  plat_note="\"기간으로 조회되게\"에는 <b>끝날 포함 여부</b>가 거의 늘 빠져 있습니다. 정산·매출처럼 숫자가 걸린 화면에서는 이 하루가 그대로 금액 차이가 되고, 나중에 \"숫자가 안 맞아요\"로 돌아옵니다. 만들 때 <b>화면 문구와 질의를 같이</b> 적어 두면 이 왕복이 사라집니다.",
  siblings=siblings("daterange"),
  related='''        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="datetime.html"><b>날짜와 시간 쓰기</b><em>14부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
