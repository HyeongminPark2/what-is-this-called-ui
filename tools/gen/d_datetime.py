# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(txt, tag, ok=None, note="", w="152px"):
    return one('<span style="font-family:var(--mono)">' + txt + '</span>', tag, ok, note, w)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">일주일 안 — 3시간 전 · 어제 · 5일 전</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">올해 안 — 11월 7일(금) 오전 9:12</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">해를 넘기면 — 2025년 3월 2일(일)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;time datetime="2026-11-14T09:12"&gt; — 기계용</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">요일을 적는다 — 날짜만으로는 감이 안 온다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘8개월 전’ — 언제인지 알 수 없다</div>
                </div>
              </div>'''

D = dict(
  slug="datetime", ko="날짜와 시간 쓰기", en="Writing dates & times",
  desc="상대 시간과 절대 시간을 언제 쓰나. 요일·오전 오후·기계용 꼴까지.",
  lede="같은 시각도 <b>얼마나 지났느냐</b>에 따라 쓰는 법이 다릅니다. ‘3분 전’과 ‘8개월 전’은 쓸모가 다릅니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 <b>얼마나 지난 시각</b>인지 바꿔 보세요. 표에서 <b>맞는 줄</b>이 밝아집니다.<br>
          <b>상대 시간</b>은 방금 일어난 일에 읽기 쉽지만 오래된 것에는 쓸모없어지고,
          <b>절대 시간</b>은 언제나 맞지만 방금 일에는 번거롭습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "상대 시간, 절대 시간, 타임스탬프"),
    ("영어", "relative time, absolute time, timestamp, fuzzy time"),
    ("같이 쓰는 말",
     "'3분 전'처럼 지금을 기준으로 적는 것이 <b>상대 시간</b>·<b>퍼지 타임</b>, "
     "'11월 14일 09:12'가 <b>절대 시간</b>입니다. "
     "기계가 읽는 꼴이 <b>ISO 8601</b>(<code>2026-11-14T09:12+09:00</code>)이고, "
     "브라우저가 말에 맞춰 적어 주는 장치가 <code>Intl.RelativeTimeFormat</code>·<code>Intl.DateTimeFormat</code>입니다."),
    ("자주 잘못 부름",
     "<b>타임스탬프</b> — 흔히 숫자(1763…)를 가리키는데, 화면에 적는 글자와는 다릅니다.<br>"
     "<b>날짜 선택기</b> — 고르는 부품과 <b>적는 법</b>은 다른 이야기입니다.<br>"
     "<b>숫자 꼴</b> — <a href=\"../items/numerals.html\">숫자 꼴</a>은 <b>자릿수를 맞추는</b> 조판 이야기입니다."),
  ]),
  axes=ax("날짜와 시간 쓰기"),
  oneline="<b>일주일 안이면 상대, 넘으면 절대.</b> 그리고 눈에 보이는 것과 <code>datetime</code> 속성은 따로 둡니다.",
  s4_title="얼마나 지났나", s4_hint="같은 시각, 다른 적기",
  states=states([
    (row('방금', "1분 안", True, "초를 적지 않는다"), "방금", "'37초 전'은 <b>너무 자세하다</b>"),
    (row('3시간 전', "하루 안", True, "상대 시간이 읽기 쉽다"), "오늘", "<b>알림·댓글</b>에 맞는다"),
    (row('어제 오후 4:20', "하루 전", True, "‘1일 전’보다 ‘어제’"), "어제", "<b>사람이 쓰는 말</b>로"),
    (row('11월 7일(금) 오전 9:12', "올해 안", True, "해는 생략하고 요일을 넣는다"), "이번 해", "요일이 있으면 <b>감이 온다</b>"),
    (row('2025년 3월 2일(일)', "해를 넘김", True, "해까지 적는다"), "지난해", "<b>계약·영수증</b>은 늘 이 꼴"),
    (row('8개월 전', "오래된 것", False, "언제인지 알 수 없다"), "상대 시간을 계속 쓰면", "<b>쓸모가 사라진다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("일주일 안", "상대 시간", "방금 · 3시간 전 · 어제 · 5일 전"),
    ("올해 안", "해를 생략", "11월 7일(금) 오전 9:12"),
    ("해를 넘기면", "해까지", "2025년 3월 2일(일)"),
    ("기계용", "&lt;time datetime&gt;", "<b>정렬·검색·보조기기</b>가 쓴다"),
    ("요일", "(금)", "날짜만으로는 <b>평일인지 주말인지</b> 모른다"),
    ("오래된 상대 시간", "8개월 전", "<b>언제인지 알 수 없다.</b> 가장 흔한 실수"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>시간대는 서버가 아니라 보는 사람 기준입니다.</b>
          서버가 UTC 로 저장하고 보내는 것은 맞지만,
          화면에 적을 때는 <b>그 사람의 시간대</b>로 바꿔야 합니다.
          이게 어긋나면 '11월 14일 오전 9시에 한 일'이 누군가에게는
          <b>11월 13일</b>로 보입니다 — 정산·마감처럼 날짜가 경계인 화면에서는
          그 한 칸이 그대로 민원이 됩니다.
          기준이 서버 시각이어야 하는 화면(마감 시각 등)에는
          <b>'한국 시간 기준'</b>을 글자로 적어 둡니다.</p>''',
  do=ul([
    "<b>일주일 안</b>이면 상대 시간으로",
    "올해 안이면 <b>해를 생략</b>하고 요일을 넣기",
    "눈에는 상대, <code>datetime</code>·<code>title</code>에는 <b>절대</b>",
  ]),
  dont=ul([
    "오래된 것에 상대 시간 — <b>‘8개월 전’</b>은 쓸모없다",
    "기계 꼴을 그대로 — <code>2026-11-14T09:12:00Z</code>",
    "요일 빼기 — <b>평일인지 주말인지</b> 모른다",
    "시간대를 안 바꾸기 — <b>날짜가 하루 어긋난다</b>",
  ]),
  instead='자릿수를 맞추는 조판은 <a href="../items/numerals.html">숫자 꼴</a>, 금액은 <a href="numbertext.html">숫자와 단위</a>, 기간을 고르는 부품은 날짜 선택기.',
  cases=cases([
    (one('모란상회 <b>3분 전</b>', "알림 목록", True, "최근 것뿐이라 상대 시간이 맞는다"), "알림", "<a href=\"notifications.html\">알림 센터</a>에서"),
    (one('2026년 11월 7일(금) ~ 11월 13일(목)', "정산 기간", True, "해까지 적고 요일을 넣는다"), "기간", "<b>경계가 중요한</b> 화면"),
    (one('<span style="font-family:var(--mono)">2026.11.07</span>', "표 안", True, "자리가 좁을 때"), "표", "<a href=\"table.html\">데이터 테이블</a>에서 자릿수를 맞춘다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 시각의 계약서",
  code_lede="<code>&lt;time&gt;</code>에 기계용을, 글자에 사람용을 적습니다.",
  code='''&lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-14T09:12:00+09:00"</span>
      <span class="a">title</span>=<span class="s">"2026년 11월 14일(토) 오전 9:12"</span>&gt;3분 전&lt;/<span class="t">time</span>&gt;

<span class="c">// 브라우저가 말에 맞춰 적어 준다</span>
<span class="k">const</span> rtf = <span class="k">new</span> Intl.RelativeTimeFormat(<span class="s">'ko'</span>, { numeric: <span class="s">'auto'</span> });
rtf.format(-<span class="a">1</span>, <span class="s">'day'</span>);        <span class="c">// '어제'  ← numeric:'auto' 덕분</span>

<span class="k">new</span> Intl.DateTimeFormat(<span class="s">'ko-KR'</span>, {
  dateStyle: <span class="s">'long'</span>, timeStyle: <span class="s">'short'</span>,
  timeZone: <span class="s">'Asia/Seoul'</span>
}).format(d);                   <span class="c">// '2026년 11월 14일 오전 9:12'</span>''',
  keys=kbd([
    ("<code>&lt;time datetime&gt;</code>", "보조기기와 검색 엔진이 읽는다. <b>글자는 사람용</b>으로 자유롭게"),
    ("<code>numeric: 'auto'</code>", "'1일 전'이 <b>'어제'</b>가 된다. 한 글자 차이로 훨씬 사람 말이 된다"),
    ("<code>title</code>에 정확한 시각", "상대 시간 위에 올리면 <b>언제인지</b> 볼 수 있다. 다만 <a href=\"hover.html\">폰에서는 안 보인다</a>"),
    ("저절로 안 바뀐다", "'3분 전'은 <b>그린 시점</b>의 말이다. 오래 켜 둔 화면에서는 갱신하거나 절대 시간으로 둔다"),
    ("<code>timeZone</code>을 적는다", "안 적으면 <b>기기 설정</b>을 따른다. 기준이 정해진 화면에서는 명시한다"),
    ("<code>Intl</code>을 쓴다", "직접 만들면 <b>윤년·서머타임·달력</b>에서 깨진다"),
  ]),
  backend=rows([
    ("서버는 UTC 로", "저장도 전달도 <b>시간대를 담은 꼴</b>(ISO 8601)로 합니다. 'YYYY-MM-DD HH:mm'만 보내면 어느 시간대인지 모릅니다."),
    ("화면이 바꾼다", "보는 사람의 시간대로 옮기는 것은 <b>화면 쪽 일</b>입니다. 서버가 미리 바꾸면 캐시가 사람마다 갈라집니다."),
    ("날짜 경계", "'11월 7일 정산'이 누구에게는 6일이 될 수 있습니다. <b>기준 시간대</b>를 정하고 화면에도 적습니다."),
    ("상대 시간을 서버가 만들지 않는다", "'3분 전'을 서버가 계산해 보내면 <b>캐시된 순간</b>에 멈춥니다."),
    ("정렬 키", "표시용 글자가 아니라 <b>원래 값</b>으로 정렬합니다. '어제'와 '3시간 전'은 글자로 못 줄 세웁니다."),
  ]),
  plat_lede="세 곳 모두 <b>OS 가 적어 주는 장치</b>를 가지고 있습니다.",
  plats=plats([
    ("웹", "Intl",
     one('3분 전', "", True, "", "110px"),
     "<code>Intl.RelativeTimeFormat</code>·<code>DateTimeFormat</code>. <b>직접 만들 일이 거의 없습니다</b>."),
    ("iOS", "RelativeDateTimeFormatter",
     '''              <div class="phone" role="img" aria-label="iOS 시간 표시 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px;display:flex"><span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">3분 전</span></div></div></div>''',
     "OS 가 말과 지역에 맞춰 적어 줍니다. <b>목록에서는 오른쪽 끝</b>에 두는 것이 관례입니다."),
    ("안드로이드", "DateUtils",
     '''              <div class="phone" role="img" aria-label="안드로이드 시간 표시 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px;display:flex"><span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">3분 전</span></div></div></div>''',
     "<code>getRelativeTimeSpanString</code>이 같은 일을 합니다. 24시간제 설정도 OS 를 따릅니다."),
  ]),
  plat_note="\"시간은 '몇 분 전'으로 보여 주세요\"를 그대로 받으면 <b>1년 된 글도 '12개월 전'</b>이 됩니다. 받을 때 <b>'오래된 것은 어떻게 적습니까'</b>를 한 번 물어보면 대개 그 자리에서 기준이 정해지고, 그 기준 하나면 코드가 끝납니다.",
  siblings=siblings("datetime"),
  related='''        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
