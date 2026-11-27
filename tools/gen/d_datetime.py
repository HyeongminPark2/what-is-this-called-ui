# -*- coding: utf-8 -*-
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(txt, tag, ok=None, note="", w="152px"):
    return one('<span style="font-family:var(--mono)">' + txt + '</span>', tag, ok, note, w)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">일주일 안은 3시간 전 · 어제 · 5일 전</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">올해 안은 11월 7일(금) 오전 9:12</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">해를 넘기면 2025년 3월 2일(일)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;time datetime="2026-11-14T09:12"&gt;는 기계용</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">날짜만으로는 언제쯤인지 알기 어려워 요일을 적음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘8개월 전’만으로는 언제인지 알 수 없음</div>
                </div>
              </div>'''

D = dict(
  slug="datetime", ko="날짜와 시간 쓰기", en="Writing dates & times",
  desc="상대 시간과 절대 시간을 각각 언제 쓰는지, 요일과 오전·오후, 기계가 읽는 형식까지 함께 다룹니다.",
  lede="같은 시각이라도 지금부터 <b>얼마나 지났는지</b>에 따라 적는 방법이 달라집니다. 예를 들어 ‘3분 전’은 언제인지 바로 알 수 있지만, ‘8개월 전’만 보고는 정확히 언제인지 알기 어렵습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 <b>얼마나 지난 시각</b>인지 바꿔 보세요. 그 시각에 맞는 표기법이 표에서 <b>밝게 표시</b>됩니다.<br>
          <b>상대 시간</b>은 방금 일어난 일을 읽기 쉽게 보여 주지만 오래된 일에 쓰면 언제인지 알기 어렵고,
          <b>절대 시간</b>은 언제나 정확하지만 방금 일어난 일에 쓰기에는 번거롭습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "상대 시간, 절대 시간, 타임스탬프"),
    ("영어", "relative time, absolute time, timestamp, fuzzy time"),
    ("같이 쓰는 말",
     "'3분 전'처럼 지금을 기준으로 적는 것을 <b>상대 시간</b>·<b>퍼지 타임</b>이라 하고, "
     "'11월 14일 09:12'처럼 날짜와 시각을 그대로 적는 것을 <b>절대 시간</b>이라고 합니다. "
     "기계가 읽는 형식은 <b>ISO 8601</b>(<code>2026-11-14T09:12+09:00</code>)이고, "
     "브라우저가 언어에 맞춰 날짜와 시간을 적어 주는 기능이 <code>Intl.RelativeTimeFormat</code>·<code>Intl.DateTimeFormat</code>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>타임스탬프</b> — 흔히 기계가 저장하는 숫자(1763…)를 가리키는 말이라서, 화면에 적는 날짜·시간 글자와는 다릅니다.<br>"
     "<b>날짜 선택기</b> — 날짜를 고르는 부품이고, 이 항목은 날짜를 <b>적는 법</b>을 다룹니다.<br>"
     "<b>숫자 꼴</b> — <a href=\"../items/numerals.html\">숫자 꼴</a>은 숫자의 <b>자릿수를 맞추는</b> 조판을 다룹니다."),
  ]),
  s4_title="지난 시간에 따른 표기", s4_hint="얼마나 지났는지에 따라 달라지는 표기",
  states=states([
    (row('방금', "1분 안", True, "초는 적지 않음"), "1분이 안 지났을 때", "'37초 전'은 필요 이상으로 <b>자세합니다</b>"),
    (row('3시간 전', "하루 안", True, "상대 시간이 읽기 쉬움"), "오늘 있었던 일", "<b>알림·댓글</b>에 잘 맞습니다"),
    (row('어제 오후 4:20', "하루 전", True, "‘1일 전’보다 ‘어제’"), "어제 있었던 일", "평소 <b>사람이 쓰는 말</b>로 적습니다"),
    (row('11월 7일(금) 오전 9:12', "올해 안", True, "해는 빼고 요일을 넣음"), "올해 안의 일", "요일이 있으면 언제쯤인지 <b>쉽게 떠올릴 수 있습니다</b>"),
    (row('2025년 3월 2일(일)', "해를 넘김", True, "해까지 적음"), "해를 넘긴 일", "<b>계약·영수증</b>은 언제나 이 형식으로 적습니다"),
    (row('8개월 전', "오래된 것", False, "언제인지 알 수 없음"), "오래된 일에도 상대 시간을 쓰면", "언제인지 알 수 없어서 <b>쓸모가 없어집니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("일주일 안", "상대 시간", "방금 · 3시간 전 · 어제 · 5일 전"),
    ("올해 안", "해를 생략", "11월 7일(금) 오전 9:12"),
    ("해를 넘기면", "해까지", "2025년 3월 2일(일)"),
    ("기계용", "&lt;time datetime&gt;", "<b>정렬·검색·보조기기</b>가 이 값을 읽습니다"),
    ("요일", "(금)", "날짜만으로는 <b>평일인지 주말인지</b> 알기 어렵습니다"),
    ("오래된 상대 시간", "8개월 전", "<b>언제인지 알 수 없습니다.</b> 가장 흔한 실수입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>화면에 적는 시각은 서버가 아니라 보는 사람의 시간대를 기준으로 합니다.</b>
          서버가 UTC로 저장하고 보내는 것은 맞지만,
          화면에 적을 때는 <b>보는 사람의 시간대</b>로 바꿔야 합니다.
          시간대 변환이 어긋나면 '11월 14일 오전 9시에 한 일'이 다른 시간대의 사용자에게는
          <b>11월 13일</b>로 보입니다. 정산·마감처럼 날짜가 경계가 되는 화면에서는
          이 하루 차이가 그대로 민원으로 이어집니다.
          마감 시각처럼 서버 시각을 기준으로 삼아야 하는 화면에는
          <b>'한국 시간 기준'</b>이라고 글자로 적어 둡니다.</p>''',
  do=ul([
    "<b>일주일 안</b>이면 상대 시간으로 적기",
    "올해 안이면 <b>해를 생략</b>하고 요일을 넣기",
    "화면 글자는 상대 시간으로, <code>datetime</code>·<code>title</code>에는 <b>절대</b> 시간으로 적기",
  ]),
  do_title="날짜와 시간을 적을 때 지킬 것", dont_title="날짜와 시간을 적을 때 피할 것",
  instead_title="날짜와 시간 쓰기와 함께 보면 좋은 항목",
  dont=ul([
    "오래된 일에 상대 시간을 쓸 때. <b>‘8개월 전’</b>만으로는 언제인지 알 수 없습니다",
    "<code>2026-11-14T09:12:00Z</code>처럼 기계용 형식을 그대로 보여 줄 때",
    "요일을 뺄 때. <b>평일인지 주말인지</b> 알기 어렵습니다",
    "보는 사람의 시간대로 바꾸지 않을 때. <b>날짜가 하루 어긋날</b> 수 있습니다",
  ]),
  instead='숫자의 자릿수를 맞추는 조판은 <a href="../items/numerals.html">숫자 꼴</a>에서, 금액을 적는 법은 <a href="numbertext.html">숫자와 단위</a>에서 다룹니다. 기간을 고르게 하는 입력 부품은 날짜 선택기입니다.',
  cases=cases([
    (one('모란상회 <b>3분 전</b>', "알림 목록", True, "최근 것뿐이라 상대 시간이 맞음"), "알림 목록의 시각", "<a href=\"notifications.html\">알림 센터</a>에서 씁니다"),
    (one('2026년 11월 7일(금) ~ 11월 13일(목)', "정산 기간", True, "해까지 적고 요일을 넣음"), "정산 기간 적기", "날짜 <b>경계가 중요한</b> 화면입니다"),
    (one('<span style="font-family:var(--mono)">2026.11.07</span>', "표 안", True, "자리가 좁을 때"), "표 안의 날짜", "<a href=\"table.html\">데이터 테이블</a>에서는 자릿수를 맞춰 적습니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="<code>&lt;time&gt;</code>의 속성에는 기계가 읽을 값을, 안쪽 글자에는 사람이 읽을 표기를 적습니다.",
  code='''&lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-14T09:12:00+09:00"</span>
      <span class="a">title</span>=<span class="s">"2026년 11월 14일(토) 오전 9:12"</span>&gt;3분 전&lt;/<span class="t">time</span>&gt;

<span class="c">// 브라우저가 말에 맞춰 적어 준다</span>
<span class="k">const</span> rtf = <span class="k">new</span> Intl.RelativeTimeFormat(<span class="s">'ko'</span>, { numeric: <span class="s">'auto'</span> });
rtf.format(-<span class="a">1</span>, <span class="s">'day'</span>);        <span class="c">// '어제'  ← numeric:'auto' 덕분</span>

<span class="k">new</span> Intl.DateTimeFormat(<span class="s">'ko-KR'</span>, {
  dateStyle: <span class="s">'long'</span>, timeStyle: <span class="s">'short'</span>,
  timeZone: <span class="s">'Asia/Seoul'</span>
}).format(d);                   <span class="c">// '2026년 11월 14일 오전 9:12'</span>''',
  keys_heads="<th>지킬 규칙과 마크업</th><th>지키는 방법과 이유</th>",
  keys=kbd([
    ("<code>&lt;time datetime&gt;</code>", "보조기기와 검색 엔진은 이 속성 값을 읽으므로, 화면에 보이는 <b>글자는 사람이 읽기 좋게</b> 자유롭게 적어도 됩니다"),
    ("<code>numeric: 'auto'</code>", "이 옵션을 켜면 '1일 전'이 <b>'어제'</b>로 바뀌어 평소 쓰는 말에 가까워집니다"),
    ("<code>title</code>에 정확한 시각 넣기", "상대 시간에 마우스를 올리면 정확히 <b>언제인지</b> 볼 수 있습니다. 다만 <a href=\"hover.html\">폰에서는 보이지 않습니다</a>"),
    ("상대 시간 갱신하기", "'3분 전'은 화면을 <b>그린 시점</b>을 기준으로 계산한 값입니다. 오래 켜 두는 화면에서는 주기적으로 갱신하거나 절대 시간으로 적습니다"),
    ("<code>timeZone</code>을 적기", "적지 않으면 <b>기기 설정</b>을 따르므로, 기준 시간대가 정해진 화면에서는 직접 적어 줍니다"),
    ("<code>Intl</code>을 쓰기", "날짜 계산을 직접 만들면 <b>윤년·서머타임·달력</b> 차이를 처리하다가 틀리기 쉽습니다"),
  ]),
  backend=rows([
    ("서버는 UTC로 저장하고 보내기", "저장할 때도 보낼 때도 <b>시간대 정보가 들어간 형식</b>(ISO 8601)을 씁니다. 'YYYY-MM-DD HH:mm'만 보내면 받는 쪽은 어느 시간대의 시각인지 알 수 없습니다."),
    ("시간대 변환은 화면에서 하기", "보는 사람의 시간대로 바꾸는 것은 <b>화면 쪽 일</b>입니다. 서버가 미리 바꿔 보내면 같은 응답이라도 사람마다 따로 캐시해야 합니다."),
    ("날짜 경계의 기준 시간대 정하기", "'11월 7일 정산'이 시간대에 따라 누군가에게는 6일이 될 수 있으므로, <b>기준 시간대</b>를 정하고 화면에도 적어 둡니다."),
    ("상대 시간을 서버가 만들지 않기", "서버가 '3분 전'을 계산해 보내면, 응답이 캐시된 뒤로는 <b>캐시된 순간</b>을 기준으로 한 값이 바뀌지 않고 그대로 보입니다."),
    ("정렬은 원래 값으로 하기", "정렬은 표시용 글자가 아니라 <b>원래 값</b>으로 합니다. '어제'와 '3시간 전' 같은 글자로는 순서를 정할 수 없습니다."),
  ]),
  plat_lede="세 플랫폼 모두 날짜와 시간을 <b>언어에 맞게 적어 주는 기능</b>이 있습니다.",
  plats=plats([
    ("웹", "Intl",
     one('3분 전', "", True, "", "110px"),
     "<code>Intl.RelativeTimeFormat</code>·<code>DateTimeFormat</code>이 있어서 표기 함수를 <b>직접 만들 일이 거의 없습니다</b>."),
    ("iOS", "RelativeDateTimeFormatter",
     '''              <div class="phone" role="img" aria-label="iOS 시간 표시 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px;display:flex"><span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">3분 전</span></div></div></div>''',
     "OS가 언어와 지역 설정에 맞춰 적어 줍니다. 목록에서는 시각을 <b>오른쪽 끝</b>에 두는 것이 관례입니다."),
    ("안드로이드", "DateUtils",
     '''              <div class="phone" role="img" aria-label="안드로이드 시간 표시 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px;display:flex"><span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">3분 전</span></div></div></div>''',
     "<code>getRelativeTimeSpanString</code>이 같은 일을 하고, 24시간제 여부도 OS 설정을 따릅니다."),
  ]),
  plat_note="\"시간은 '몇 분 전'으로 보여 주세요\"라는 요청을 그대로 구현하면 <b>1년 된 글도 '12개월 전'</b>으로 보입니다. 요청을 받을 때 <b>'오래된 것은 어떻게 적습니까'</b>라고 한 번 물어보면 대개 그 자리에서 상대 시간과 절대 시간을 나누는 기준이 정해지고, 코드는 그 기준대로 짜면 됩니다.",
  siblings=siblings("datetime"),
  related='''        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
