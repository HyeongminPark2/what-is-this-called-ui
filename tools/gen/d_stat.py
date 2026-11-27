# -*- coding: utf-8 -*-
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def tile(label, value, delta="", tone="up", spark=True, w="160px"):
    colors = {"up": "#1f8a4c", "down": "var(--danger)", "flat": "var(--fg-muted)"}
    d = ('<span style="font-size:11px;font-weight:700;color:%s;display:block">%s <span style="font-weight:500;color:var(--fg-muted)">지난주 대비</span></span>'
         % (colors[tone], delta)) if delta else ''
    sp = ('<svg viewBox="0 0 100 26" preserveAspectRatio="none" style="height:22px;width:100%;margin-top:3px" aria-hidden="true">'
          '<polyline points="0,22 17,17 33,19 50,12 67,13 83,7 100,3" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round"/></svg>') if spark else ''
    return ('              <div style="width:100%%;max-width:%s;border:1px solid var(--line);border-radius:9px;'
            'background:var(--surface);padding:10px 12px;display:grid;gap:2px">'
            '<span style="font-size:10.5px;color:var(--fg-muted);display:block">%s</span>'
            '<span style="font-size:20px;font-weight:800;line-height:1.15;font-variant-numeric:tabular-nums;display:block">%s</span>'
            '%s%s</div>') % (w, label, value, d, sp)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:16px 10px 16px 0">
                <div style="padding-left:26px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 12px 13px">
                    <div style="padding-left:26px;display:grid;gap:9px">
                      <div class="pin-out" data-pin="2" style="font-size:11px;color:var(--fg-muted)">이번 주 매출</div>
                      <div class="pin-out" data-pin="3" style="font-size:22px;font-weight:800;line-height:1.1;font-variant-numeric:tabular-nums">₩1,284,000</div>
                      <div class="pin-out" data-pin="4" style="font-size:11px;font-weight:700;color:#1f8a4c">▲ 12.4% <span style="font-weight:500;color:var(--fg-muted)">지난주 대비</span></div>
                      <div class="pin-out" data-pin="5" style="line-height:0">
                        <svg viewBox="0 0 100 26" preserveAspectRatio="none" style="height:24px;width:100%;max-width:180px" aria-hidden="true"><polyline points="0,22 17,17 33,19 50,12 67,13 83,7 100,3" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round"/></svg>
                      </div>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="stat", ko="스탯 타일", en="Stat tile · metric card · KPI card",
  desc="스탯 타일의 구성과 증감 표시, 그리고 값이 올라간다고 늘 초록으로 칠하면 안 되는 이유를 실물과 해부도로 보여 주는 항목입니다.",
  lede="스탯 타일은 숫자 하나를 크게 보여 주는 칸으로, 대시보드 맨 위에 여러 개가 나란히 놓이는 경우가 많습니다. 숫자 자체보다 <b>그 숫자를 무엇과 비교해 보여 주느냐</b>가 중요합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>숫자만 보여 주기</b>를 켜 보세요. ₩1,284,000이 많은 건지 적은 건지 알 수 없습니다.
          그래서 스탯 타일에는 숫자와 함께 <b>비교할 기준을 같이 보여 주어야</b> 합니다.<br>
          <b>환불액</b> 타일은 값이 올라갔는데도 빨간색으로 칠해진 것도 보세요. 색은 값이 오르내리는 방향이 아니라 <b>그 변화가 좋은 쪽인지</b>로 정합니다.
          이탈률, 환불액, 오류 수는 올라가면 나쁜 지표이기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스탯 타일, 지표 카드, 요약 숫자, KPI 카드"),
    ("영어", "stat tile, metric card, KPI card, scorecard, big number"),
    ("같이 쓰는 말",
     "큰 숫자는 <b>빅 넘버</b>(big number), 지난 기간과의 차이는 <b>델타</b>(delta · change · trend),  "
     "타일 안의 작은 꺾은선은 <b>스파크라인</b>(sparkline)이라고 부릅니다.  "
     "여러 타일이 늘어선 줄은 <b>스탯 바</b> 또는 <b>스코어카드</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>카드</b> — 생김새는 카드와 같지만, <b>숫자 하나</b>를 보여 주는 것이 목적이라서 따로 부릅니다.<br>"
     "<b>차트</b> — 스파크라인이 붙어 있어도 사용자가 <b>읽는 것은 숫자</b>입니다. 스파크라인에는 축도 눈금도 없습니다.<br>"
     "<b>프로그레스 바</b> — 프로그레스 바는 <b>끝이 정해진</b> 진행 정도를 보여 주고, 스탯 타일은 끝이 없는 값 하나를 보여 줍니다."),
  ]),
  s4_title="상태", s4_hint="값과 변화에 따라 달라지는 타일 모습",
  states=states([
    (tile("이번 주 매출", "₩1,284,000", "▲ 12.4%", "up"), "좋은 지표가 올랐을 때", "매출이나 가입자 수처럼 올라가면 좋은 지표는 <b>초록</b>으로 칠합니다"),
    (tile("환불액", "₩96,000", "▲ 31.2%", "down"), "나쁜 지표가 올랐을 때", "올라갔지만 나쁜 변화라서 <b>빨강</b>으로 칠합니다. 색은 방향이 아니라 <b>좋은 쪽인지</b>로 정합니다"),
    (tile("평균 처리 시간", "1.8일", "— 변화 없음", "flat", spark=False), "지난 기간과 같을 때", "<b>0%</b>라고 적지 않고 '변화 없음'으로 적습니다"),
    ('''              <div style="width:100%;max-width:160px;border:1px solid var(--line);border-radius:9px;background:var(--surface);padding:10px 12px;display:grid;gap:5px">
                <span class="skl" style="height:9px;width:55%"></span>
                <span class="skl" style="height:18px;width:80%"></span>
                <span class="skl" style="height:8px;width:45%"></span>
              </div>''',
     "값을 불러오는 중", "실제 타일과 <b>같은 높이의</b> 뼈대를 그립니다. 높이가 다르면 숫자가 늦게 들어올 때 대시보드 전체가 위아래로 밀립니다"),
    (tile("이번 주 매출", "—", "데이터 없음", "flat", spark=False), "값이 없을 때",
     "값을 <b>0으로 적지 않습니다.</b> 0건인 것과 값을 불러오지 못한 것은 서로 다른 상태입니다"),
    (tile("이번 주 매출", "₩12.8억", "▲ 12.4%", "up"), "숫자가 칸보다 클 때",
     "자릿수가 칸을 넘으면 <b>단위를 줄여</b> 적고, 정확한 값은 호버나 상세 화면에서 보여 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("타일", "tile · metric card", "숫자 하나와 그 숫자를 이해하는 데 필요한 정보를 담는 칸입니다. 보통 네 개가 한 줄로 늘어섭니다"),
    ("라벨", "label", "무슨 숫자인지 알려 줍니다. '매출'이 아니라 '이번 주 매출'처럼 <b>기간을 넣어야</b> 합니다"),
    ("값", "value", "타일에서 가장 큰 글자입니다. <code>tabular-nums</code>로 숫자 폭을 맞춰야 값이 바뀌어도 타일 안의 글자가 흔들리지 않습니다"),
    ("증감", "delta · change", "지난 기간과 비교한 변화입니다. <b>화살표, 색, 숫자</b> 세 가지가 모두 같은 방향을 가리켜야 합니다"),
    ("추세선", "sparkline", "최근 흐름을 보여 줍니다. 축도 눈금도 없어서 <b>선의 모양만</b> 읽는 그림입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라벨에 <b>기간이 없으면</b> 사용자가 숫자를 잘못 읽기 쉽습니다. '매출 ₩1,284,000'만으로는 오늘 매출인지, 이번 주 매출인지,
          누적 매출인지 알 수 없기 때문입니다. 증감도 마찬가지여서 '▲12.4%' 옆에는 지난주 대비인지, 작년 같은 주 대비인지,
          목표 대비인지처럼 <b>무엇과 견준 값인지</b>를 반드시 적어야 합니다.</p>''',
  do=ul([
    "화면 맨 위에서 <b>지금 상태를 한눈에</b> 보여 줄 때",
    "보여 줄 숫자가 <b>서너 개</b>일 때. 여덟 개가 넘으면 어느 숫자도 눈에 들어오지 않습니다",
    "지난주 값, 목표, 추세처럼 비교할 기준이 <b>있을</b> 때",
  ]),
  dont=ul([
    "비교할 기준 없이 숫자만 크게 쓸 때. 그러면 <b>큰 글자로 적은 숫자</b>와 다를 것이 없습니다",
    "값이 자주 바뀌는데 소수점 아래까지 보여 줄 때. 숫자가 계속 바뀌어 읽을 수 없습니다",
    "타일을 여덟 개 이상 늘어놓을 때. 그만큼 많으면 표가 더 낫습니다",
    "값이 <b>올라가면 무조건 초록</b>으로 칠할 때",
  ]),
  instead='끝이 정해진 일의 진행 정도라면 <a href="../items/progress.html">프로그레스 바</a>를 쓰고, 여러 값을 서로 견주려면 차트(10부)를 씁니다. 숫자 하나가 아니라 건마다 따로 보여 주려면 <a href="listitem.html">리스트 아이템</a>이 맞습니다.',
  cases=cases([
    ('''              <div style="display:flex;gap:7px;width:100%">
                ''' + tile("매출", "₩1.28M", "▲ 12%", "up", spark=False, w="80px") +
       tile("건수", "42", "▲ 5", "up", spark=False, w="80px") +
       tile("환불", "₩96K", "▲ 31%", "down", spark=False, w="80px") + '''
              </div>''',
     "대시보드 맨 위에 늘어놓기", "타일 <b>서너 개를 한 줄로</b> 늘어놓습니다. 스탯 타일을 가장 흔히 쓰는 자리입니다"),
    (tile("이번 달 목표", "68%", "₩6.8억 / ₩10억", "flat", spark=False),
     "목표와 견주어 보여 주기", "비교 기준이 <b>지난 기간이 아니라 목표</b>일 때 씁니다"),
    ('''              <div style="width:100%;max-width:170px;border:1px solid var(--line);border-radius:9px;background:var(--surface);padding:10px 12px;display:grid;gap:3px">
                <span style="font-size:10.5px;color:var(--fg-muted)">이번 주 매출</span>
                <span style="font-size:20px;font-weight:800;font-variant-numeric:tabular-nums">₩1,284,000</span>
                <span style="font-size:10px;color:var(--accent);text-decoration:underline">자세히 보기 ›</span>
              </div>''',
     "눌러서 상세 화면으로 들어가기", "타일을 누르면 <b>상세 화면으로 이동</b>하게 만들기도 합니다"),
  ]),
  s8_title="최소 마크업과 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="큰 숫자와 작은 라벨은 <b>눈으로 볼 때와 들을 때 순서가 반대</b>입니다. 눈은 큰 숫자를 먼저 보지만, 스크린 리더는 코드에 적힌 순서대로 라벨부터 읽습니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"stat"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"stat__label"</span> <span class="a">id</span>=<span class="s">"l1"</span>&gt;이번 주 매출&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">strong</span> <span class="a">class</span>=<span class="s">"stat__value"</span> <span class="a">aria-labelledby</span>=<span class="s">"l1"</span>&gt;₩1,284,000&lt;/<span class="t">strong</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"stat__delta up"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;▲&lt;/<span class="t">span</span>&gt; 12.4% 지난주 대비
  &lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="t">.stat__value</span> { <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">// 오르내리는 방향이 아니라 '좋은 쪽인가'로 색을 고른다</span>
<span class="t">const</span> tone = delta === <span class="a">0</span> ? <span class="s">'flat'</span>
  : (delta &gt; <span class="a">0</span>) === (metric.goodDirection === <span class="s">'up'</span>) ? <span class="s">'up'</span> : <span class="s">'down'</span>;''',
  keys=kbd([
    ("라벨에 기간 넣기", "'매출'이 아니라 '<b>이번 주</b> 매출'로 적습니다. 기간이 없으면 어떤 숫자인지 알 수 없습니다"),
    ("증감에 비교 기준 적기", "'▲12.4%' 뒤에 <b>지난주 대비</b>처럼 기준을 붙여야 숫자의 뜻이 분명해집니다"),
    ("<code>tabular-nums</code>로 숫자 폭 맞추기", "숫자마다 폭을 같게 맞춥니다. 맞추지 않으면 값이 바뀔 때마다 글자 폭이 달라져 타일 안의 숫자가 흔들립니다"),
    ("색은 좋은 쪽인지로 고르기", "환불, 이탈, 오류는 <b>올라가면 빨강</b>으로 칠합니다. 지표마다 어느 방향이 좋은지를 데이터에 적어 둡니다"),
    ("화살표는 스크린 리더에서 숨기기", "<code>aria-hidden</code>을 붙입니다. '▲'를 스크린 리더가 '검은 위쪽 삼각형'으로 읽으면 내용을 듣는 데 방해만 됩니다"),
    ("없는 값은 0 대신 —로 적기", "값이 없을 때 0으로 채우지 않습니다. <b>0건인 것과 값을 모르는 것은 서로 다른 상태</b>입니다"),
  ]),
  backend=rows([
    ("미리 집계해 둔 값 읽기", "타일 하나를 채우려고 테이블 전체를 훑는 질의를 쓰면 대시보드를 열 때마다 <b>몇 초씩 기다려야 합니다.</b> 그래서 보통은 시간별, 일별로 미리 집계해 둔 표에서 값을 읽습니다."),
    ("기간을 나누는 기준 시각", "'이번 주'가 월요일부터인지 일요일부터인지, <b>어느 시간대를 기준</b>으로 하는지에 따라 숫자가 달라집니다. 그래서 서버와 화면이 같은 기준을 써야 합니다."),
    ("지난 값이 0일 때의 증감 계산", "지난주 값이 0이면 증가율이 <b>무한대</b>가 됩니다. 그래서 0에서 N으로 늘었을 때는 비율 대신 '신규'라고 적는 식의 규칙이 필요합니다."),
    ("단위를 줄이고 반올림하는 규칙", "₩1,284,000을 '₩1.28M'으로 줄일지, 몇째 자리에서 반올림할지를 정해 둡니다. 이 규칙이 <b>화면마다 다르면</b> 같은 숫자가 화면마다 다르게 보입니다."),
    ("타일 네 개를 한 번에 받기", "타일마다 따로 요청하기보다 묶어서 <b>한 번에</b> 받는 편이 낫습니다. 그중 값 하나가 늦게 오면 그 타일만 뼈대로 두고 나머지 타일을 먼저 보여 줍니다."),
  ]),
  plat_lede="세 플랫폼 모두 스탯 타일이라는 정해진 부품이 없어서, 제품마다 직접 만듭니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     tile("이번 주 매출", "₩1.28M", "▲ 12%", "up", spark=False, w="120px"),
     "대시보드마다 직접 만들고, 이름도 스탯, 메트릭, KPI 등으로 제각각입니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 요약 숫자 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:8px;padding:7px">
                  <span style="font-size:6.5px;color:var(--fg-muted);display:block">이번 주 매출</span>
                  <span style="font-size:12px;font-weight:800;display:block">₩1.28M</span></div>
              </div></div>''',
     "정해진 부품은 없지만 <b>위젯</b>과 건강·배터리 화면의 관례가 사실상 기준 역할을 합니다. 숫자는 크게, 라벨은 아주 작게 씁니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 요약 숫자 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;border:1px solid var(--line);border-radius:10px;padding:7px">
                  <span style="font-size:6.5px;color:var(--fg-muted);display:block">이번 주 매출</span>
                  <span style="font-size:12px;font-weight:800;display:block">₩1.28M</span></div>
              </div></div>''',
     "전용 부품은 없고, <b>Card</b> 안에서 타입 스케일(<code>displaySmall</code> 등)로 숫자를 키워 만듭니다."),
  ]),
  plat_note="정해진 부품이 없어서 <b>부르는 이름부터 팀마다 다릅니다</b>. 스탯 타일, 지표 카드, KPI, 요약 숫자는 모두 같은 부품을 가리킵니다. 그래서 처음 이야기할 때 \"숫자 하나를 크게 보여 주는 칸\"이라고 풀어 말하면 서로 다른 것을 떠올리는 일이 줄어듭니다.",
  siblings=siblings("stat"),
  related='''        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>''',
)
