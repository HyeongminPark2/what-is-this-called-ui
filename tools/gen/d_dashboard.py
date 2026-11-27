# -*- coding: utf-8 -*-
from ax13 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L13 = "화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다."

def tile(name, val, delta, cmp_, link, big=False, w="72px", bad=False):
    col = 'var(--danger)' if bad else ('#1a7f37' if delta.startswith('+') else ('var(--danger)' if delta.startswith('-') else 'var(--fg-muted)'))
    sign = '▲' if delta.startswith('+') else ('▼' if delta.startswith('-') else '—')
    return ('<span style="display:grid;gap:1px;border:1px solid var(--line);border-radius:5px;'
            'background:var(--surface);padding:5px 6px;min-width:0;' + ('grid-column:1/-1;' if big else '') + '">'
            '<span style="font-size:7px;color:var(--fg-muted)">' + name + '</span>'
            '<span style="font-size:' + ('15px' if big else '11px') + ';font-weight:700">' + val + '</span>'
            + ('<span style="font-size:7px;color:' + col + '">' + sign + ' ' + delta.lstrip('+-') +
               ' <span style="color:var(--fg-faint)">' + cmp_ + '</span></span>' if delta else '')
            + ('<span style="font-size:7px;color:var(--accent)">' + link + ' ›</span>' if link else '')
            + '</span>')

def board(tiles, w="152px", note="", ok=None, cols=3):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;grid-template-columns:repeat(' + str(cols) + ',1fr);gap:4px;'
            'border:1px solid ' + c + ';border-radius:6px;background:var(--bg);padding:5px">' + ''.join(tiles) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">으뜸 지표 하나 — 가장 크게</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">견줄 값 — '지난주 대비 +12%'</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">다음 할 일 — '밀린 정산 3건 보기 ›'</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">기준 시각 — '11월 14일 09:00 기준'</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">지표를 늘릴수록 으뜸이 묻힌다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">빈 상태 — 쌓인 게 없을 때의 화면</div>
                </div>
              </div>'''

D = dict(
  slug="dashboard", ko="대시보드", en="Dashboard",
  desc="지금 괜찮은지 한눈에 판단하는 화면. 지표 수, 견줄 값, 다음 할 일로 이어 주기.",
  lede="대시보드가 답해야 하는 질문은 하나입니다 — <b>지금 괜찮은가</b>. 숫자를 늘릴수록 그 답이 멀어집니다.",
  axes_lede=L13,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>지표를 늘려 보세요. 데모가 <b>맨 위 칸이 전체에서 차지하는 몫</b>을 재서
          으뜸 지표가 묻혔는지 알려 줍니다 — 열두 개가 되면 어느 것부터 볼지 정할 수 없습니다.<br>
          숫자 하나는 아무 뜻이 없습니다. <b>지난주 대비</b> 같은 견줄 값이 붙어야
          좋은지 나쁜지 압니다. 그리고 대시보드는 <b>보는 데서 끝나면 안 됩니다</b> —
          지표마다 '밀린 정산 3건 보기' 같은 다음 할 일로 이어 줘야 일이 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대시보드, 현황판, 요약 화면"),
    ("영어", "dashboard, overview, summary screen"),
    ("같이 쓰는 말",
     "숫자 하나를 담은 칸이 <b>스탯 타일</b>(stat tile · KPI card), "
     "그 안의 작은 꺾은선이 <b>스파크라인</b>(sparkline)입니다. "
     "맨 위에 하나만 크게 두는 지표를 <b>으뜸 지표</b>(north star · primary metric)라 부르고, "
     "숫자 밑에 붙는 '지난주 대비'를 <b>견줄 값</b>(comparison)이라 합니다."),
    ("자주 잘못 부름",
     "<b>리포트</b> — 리포트는 <b>깊이 파는</b> 화면이고 대시보드는 <b>훑는</b> 화면입니다.<br>"
     "<b>데이터 테이블</b> — <a href=\"table.html\">데이터 테이블</a>은 <b>줄 단위로 다루는</b> 화면입니다.<br>"
     "<b>차트</b> — <a href=\"chart.html\">차트 고르기</a>는 그 안에 들어가는 <b>부품</b>입니다."),
  ]),
  axes=ax("대시보드"),
  oneline="<b>지표 다섯 개를 넘기면 의심하세요.</b> 숫자를 더하는 대신 '그래서 무엇을 하라'를 더합니다.",
  s4_title="상태", s4_hint="숫자만으로는 못 읽는다",
  states=states([
    (board([tile("이번 주 정산액", "1,284만", "+12%", "지난주 대비", "밀린 정산 보기", True),
            tile("밀린 건수", "3건", "-2건", "어제", ""),
            tile("오류율", "0.4%", "+0.1%p", "지난주", ""),
            tile("처리 시간", "1.8일", "-0.3일", "지난주", "")], "152px", "으뜸 하나 + 셋", True),
     "좋은 꼴", "<b>으뜸이 가장 크다</b>"),
    (board([tile("정산액", "1,284만", "", "", ""),
            tile("밀린 건수", "3건", "", "", ""),
            tile("오류율", "0.4%", "", "", ""),
            tile("처리 시간", "1.8일", "", "", ""),
            tile("신규 가게", "12곳", "", "", ""),
            tile("환불액", "47만", "", "", "")], "152px", "숫자만 있다", False),
     "견줄 값 없음", "<b>좋은지 나쁜지</b> 모른다"),
    (board([tile("정산액", "1,284만", "+12%", "지난주", ""),
            tile("밀린", "3건", "-2건", "어제", ""),
            tile("오류율", "0.4%", "+0.1%p", "지난주", ""),
            tile("시간", "1.8일", "-0.3일", "지난주", ""),
            tile("신규", "12곳", "+3곳", "지난주", ""),
            tile("환불", "47만", "-8%", "지난주", ""),
            tile("카드", "62%", "+1%p", "지난달", ""),
            tile("문의", "9건", "-4건", "어제", ""),
            tile("계산서", "48장", "0장", "지난달", "")], "152px", "열두 개면 다 비슷해 보인다", False),
     "너무 많음", "<b>으뜸이 묻힌다</b>"),
    (board([tile("이번 주 정산액", "1,284만", "+12%", "지난주 대비", "밀린 정산 3건 보기", True)],
           "152px", "지표마다 할 일이 붙는다", True, 1),
     "할 일로 이어짐", "<b>보는 데서 안 끝난다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">아직 정산이 없습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">첫 가게 등록하기 ›</span>'),
         "빈 상태", True, "숫자가 0 인 화면도 설계한다", "152px"),
     "빈 상태", "<b>0 이 아니라 안내</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">11월 14일 09:00 기준</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">한 시간마다 새로 집계</span>'),
         "기준 시각", True, "언제 숫자인지 적는다", "152px"),
     "기준 시각", "<b>실시간이 아니면</b> 적는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("으뜸 지표", "하나", "<b>가장 크게</b> 둔다"),
    ("견줄 값", "지난주 대비", "숫자에 <b>뜻</b>을 준다"),
    ("다음 할 일", "링크", "보는 데서 <b>안 끝난다</b>"),
    ("기준 시각", "언제 숫자인가", "실시간이 아니면 <b>적는다</b>"),
    ("지표 수", "다섯 안팎", "늘릴수록 <b>으뜸이 묻힌다</b>"),
    ("빈 상태", "0 인 화면", "<b>처음 쓰는 사람</b>이 보는 화면이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          대시보드를 만들 때 가장 흔한 요청이 <b>'이 숫자도 넣어 주세요'</b>입니다.
          하나씩 보면 다 맞는 말인데, 쌓이면 <b>아무도 안 보는 화면</b>이 됩니다.
          그래서 지표를 더하기 전에 <b>'이 숫자가 나쁘면 무엇을 하나'</b>를 물어보는 것이 좋습니다 —
          답이 없으면 그 숫자는 대시보드가 아니라 리포트에 있을 자리입니다.<br>
          '지난주 대비'를 고를 때도 기준이 필요합니다. 주말이 끼는 업무라면
          <b>지난주 같은 요일</b>과 견주는 쪽이 맞고, 그 기준을 화면에 적어 둬야 합니다.</p>''',
  do=ul([
    "<b>으뜸 지표 하나</b>를 정하고 가장 크게 두기",
    "숫자마다 <b>견줄 값</b>과 <b>다음 할 일</b> 붙이기",
    "<b>기준 시각</b>을 화면에 적기",
  ]),
  dont=ul([
    "지표를 <b>칸이 남아서</b> 더 넣기",
    "숫자만 두고 <b>견줄 값을 빼기</b> — 좋은지 나쁜지 모른다",
    "<b>빈 상태</b>를 안 만들기 — 처음 쓰는 사람에게는 0 뿐이다",
    "실시간이 아닌데 <b>실시간처럼</b> 보이게 두기",
  ]),
  instead='깊이 파는 화면은 <a href="table.html">데이터 테이블</a>, 그림 고르기는 <a href="chart.html">차트 고르기</a>, 숫자 칸 자체는 <a href="stat.html">스탯 타일</a>, 숫자 표기는 <a href="numbertext.html">숫자와 단위 쓰기</a>.',
  cases=cases([
    (board([tile("이번 주 정산액", "1,284만", "+12%", "지난주 대비", "내역 보기", True)], "150px", "", True, 1),
     "정산 현황", "<b>으뜸 하나</b>로 시작"),
    (board([tile("오늘 주문", "128건", "+9건", "어제", ""),
            tile("준비 중", "14건", "+2건", "어제", ""),
            tile("지연", "2건", "+2건", "어제", "")], "150px", "", True),
     "운영 화면", "<b>지금 일어나는</b> 것"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">아직 쌓인 게 없습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">첫 주문 받아 보기 ›</span>'),
         "빈 상태", True, "", "150px"),
     "처음 쓰는 사람", "<b>0 대신 안내</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="숫자 칸은 <b>링크를 품은 덩어리</b>로 둡니다. 읽는 차례가 곧 중요도입니다.",
  code='''&lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"lead"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"lead"</span>&gt;이번 주 정산액&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"big"</span>&gt;&lt;<span class="t">strong</span>&gt;1,284만&lt;/<span class="t">strong</span>&gt;원&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">p</span>&gt;지난주 대비 &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"up"</span>&gt;+12%&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settlements?status=pending"</span>&gt;밀린 정산 3건 보기&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">section</span>&gt;

&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"asof"</span>&gt;&lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-14T09:00"</span>&gt;11월 14일 09:00&lt;/<span class="t">time</span>&gt; 기준&lt;/<span class="t">p</span>&gt;

<span class="c">/* 숫자는 자릿수가 흔들리지 않게 */</span>
.big strong { <span class="a">font-variant-numeric</span>: tabular-nums; }''',
  keys=kbd([
    ("Tab", "<b>으뜸 지표의 링크</b>가 먼저 오게 마크업 순서를 둔다"),
    ("<code>&lt;h2&gt;</code>", "지표 이름이 제목이다 — <b>제목만 훑어</b> 지나갈 수 있다"),
    ("<code>&lt;time&gt;</code>", "기준 시각은 기계도 읽게 적는다"),
    ("<code>tabular-nums</code>", "값이 바뀌어도 <b>자릿수가 안 흔들린다</b>"),
    ("<code>aria-live</code>", "저절로 새로 고치는 숫자에만. <b>남발하면</b> 계속 읽어 댄다"),
    ("확인하는 법", "제목만 따라 훑어서 <b>중요한 차례</b>가 맞는지 본다"),
  ]),
  backend=rows([
    ("기준 시각을 같이", "<code>as_of: \"2026-11-14T09:00\"</code> 가 있어야 화면이 '언제 숫자'인지 적을 수 있습니다."),
    ("견줄 값도 서버에서", "화면이 두 번 물어 빼기보다 <code>delta</code> 를 같이 주는 편이 <b>기준이 하나</b>로 유지됩니다."),
    ("무거운 집계", "대시보드 질의는 보통 무겁습니다 — <b>미리 집계해 둔 표</b>를 읽게 하고, 주기를 화면에 적습니다."),
    ("0 과 없음", "<code>0</code> 과 <code>null</code> 은 다릅니다 — 0 은 '없었다', null 은 '아직 모른다'입니다."),
  ]),
  plat_lede="<b>PC 화면의 패턴</b>입니다. 폰에서는 한 줄씩 쌓습니다.",
  plats=plats([
    ("웹", "격자",
     board([tile("정산액", "1,284만", "+12%", "지난주", "", True), tile("밀린", "3건", "-2건", "어제", "")], "110px", "", True, 2),
     "폭이 넓으니 <b>격자</b>로 둡니다. 폰 폭에서는 한 줄씩 쌓습니다."),
    ("iOS", "위젯 · 요약 화면",
     '''              <div class="phone" role="img" aria-label="iOS 요약 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:20px;border-radius:4px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:48px;height:12px;border-radius:4px;background:var(--bg)"></div></div></div>''',
     "홈 화면 <b>위젯</b>이 같은 자리입니다 — 숫자 하나와 다음 할 일 하나가 들어갑니다."),
    ("안드로이드", "카드 쌓기",
     '''              <div class="phone" role="img" aria-label="안드로이드 대시보드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:18px;border-radius:4px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:14px;border-radius:4px;background:var(--bg)"></div></div></div>''',
     "<b>카드</b>를 한 줄씩 쌓습니다. 맨 위 카드가 으뜸 지표를 맡습니다."),
  ]),
  plat_note="iOS 위젯의 제약이 좋은 연습입니다 — <b>숫자 하나와 할 일 하나</b>만 들어갑니다. 대시보드를 설계할 때 '이 화면을 위젯 한 칸으로 줄이면 무엇이 남나'를 물어보면 으뜸 지표가 저절로 정해집니다. 폰 폭에서는 격자를 접고 <b>한 줄씩 쌓되 차례는 중요도대로</b> 두는 것이 안전합니다.",
  siblings=siblings("dashboard"),
  related='''        <li><a href="stat.html"><b>스탯 타일</b><em>5부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
