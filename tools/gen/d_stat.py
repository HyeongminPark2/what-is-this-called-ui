# -*- coding: utf-8 -*-
from ax5 import ax
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
  desc="스탯 타일의 구성과 증감 표시, '올라간다고 다 초록이 아니다'를 실물과 해부도로 보여주는 항목.",
  lede="숫자 하나를 크게 보여 주는 칸. 대시보드 맨 위에 줄지어 있는 그것입니다. <b>일은 숫자가 아니라 비교</b>입니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>숫자만 보여 주기</b>를 켜 보세요. ₩1,284,000이 많은 건지 적은 건지 알 수가 없습니다.
          스탯 타일의 일은 숫자를 띄우는 게 아니라 <b>비교할 것을 함께 주는 것</b>입니다.<br>
          <b>환불액</b> 타일만 올라가는데 빨간색인 것도 보세요. 방향이 아니라 <b>좋은 쪽인지</b>로 색을 정합니다 —
          이탈률·환불액·오류 수는 올라가면 나쁩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스탯 타일, 지표 카드, 요약 숫자, KPI 카드"),
    ("영어", "stat tile, metric card, KPI card, scorecard, big number"),
    ("같이 쓰는 말",
     "큰 숫자를 <b>빅 넘버</b>(big number), 지난 기간과의 차이를 <b>델타</b>(delta · change · trend), "
     "타일 안의 작은 꺾은선을 <b>스파크라인</b>(sparkline)이라 합니다. "
     "여러 타일이 늘어선 줄은 <b>스탯 바</b> 또는 <b>스코어카드</b>입니다."),
    ("자주 잘못 부름",
     "<b>카드</b> — 생김새는 카드지만, <b>숫자 하나</b>가 주인공이라 따로 부릅니다.<br>"
     "<b>차트</b> — 스파크라인이 붙어도 <b>읽는 것은 숫자</b>입니다. 축도 눈금도 없습니다.<br>"
     "<b>프로그레스 바</b> — 프로그레스는 <b>끝이 정해진</b> 진행이고, 스탯은 그냥 값입니다."),
  ]),
  axes=ax("스탯 타일"),
  oneline="스탯 타일은 <b>'그래서 좋은 거야 나쁜 거야'</b>에 답해야 합니다. 비교할 것이 없으면 숫자를 크게 쓴 것뿐입니다.",
  s4_title="상태", s4_hint="그림 한 장으로는 못 배운다",
  states=states([
    (tile("이번 주 매출", "₩1,284,000", "▲ 12.4%", "up"), "오름 · 좋음", "<b>초록</b>. 매출·가입처럼 올라가면 좋은 것"),
    (tile("환불액", "₩96,000", "▲ 31.2%", "down"), "오름 · 나쁨", "<b>빨강</b>. 방향이 아니라 <b>좋은 쪽인지</b>로 정한다"),
    (tile("평균 처리 시간", "1.8일", "— 변화 없음", "flat", spark=False), "변화 없음", "<b>0%</b>가 아니라 '변화 없음'으로 적는다"),
    ('''              <div style="width:100%;max-width:160px;border:1px solid var(--line);border-radius:9px;background:var(--surface);padding:10px 12px;display:grid;gap:5px">
                <span class="skl" style="height:9px;width:55%"></span>
                <span class="skl" style="height:18px;width:80%"></span>
                <span class="skl" style="height:8px;width:45%"></span>
              </div>''',
     "로딩", "<b>같은 높이의</b> 뼈대. 숫자가 늦게 오면 대시보드 전체가 덜컥거린다"),
    (tile("이번 주 매출", "—", "데이터 없음", "flat", spark=False), "값 없음",
     "<b>0 이 아니다.</b> 0건인 것과 못 불러온 것은 다른 이야기다"),
    (tile("이번 주 매출", "₩12.8억", "▲ 12.4%", "up"), "큰 수",
     "자릿수가 넘치면 <b>단위를 줄인다</b>. 정확한 값은 호버나 상세에서"),
  ]),
  anat=ANAT,
  pins=pins([
    ("타일", "tile · metric card", "숫자 하나와 그 맥락을 담는 칸. 보통 넷이 한 줄로 늘어선다"),
    ("라벨", "label", "무슨 숫자인지. <b>기간이 들어가야</b> 한다 — '매출'이 아니라 '이번 주 매출'"),
    ("값", "value", "가장 큰 글자. <code>tabular-nums</code>로 자릿수를 맞춰야 타일끼리 안 흔들린다"),
    ("증감", "delta · change", "지난 기간 대비. <b>화살표와 색과 숫자</b> 셋이 같은 말을 해야 한다"),
    ("추세선", "sparkline", "최근 흐름. 축도 눈금도 없다 — <b>모양만</b> 읽는 그림이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라벨에 <b>기간이 없으면</b> 타일은 거짓말을 하기 쉽습니다. '매출 ₩1,284,000'은 오늘인지 이번 주인지
          누적인지 알 수 없습니다. 증감도 마찬가지라 '▲12.4%' 옆에는 <b>무엇과 견준 것인지</b>가
          반드시 붙어야 합니다 — 지난주 대비인지, 작년 같은 주 대비인지, 목표 대비인지.</p>''',
  do=ul([
    "화면 맨 위에서 <b>지금 상태를 한눈에</b> 보여 줄 때",
    "숫자가 <b>서넛</b>일 때 — 여덟 개가 넘으면 아무것도 안 보입니다",
    "비교할 기준(지난주·목표·추세)이 <b>있을</b> 때",
  ]),
  dont=ul([
    "비교할 것이 없는데 숫자만 크게 쓰는 것 — <b>그냥 글자</b>입니다",
    "값이 자주 바뀌는데 소수점까지 보여 주는 것 — 읽을 수가 없습니다",
    "여덟 개 이상 늘어놓는 것 → 표가 낫습니다",
    "<b>올라가면 무조건 초록</b>으로 칠하는 것",
  ]),
  instead='끝이 정해진 진행이면 <a href="../items/progress.html">프로그레스 바</a>, 값들을 견주려면 차트(10부), 건별로 보려면 <a href="listitem.html">리스트 아이템</a>.',
  cases=cases([
    ('''              <div style="display:flex;gap:7px;width:100%">
                ''' + tile("매출", "₩1.28M", "▲ 12%", "up", spark=False, w="80px") +
       tile("건수", "42", "▲ 5", "up", spark=False, w="80px") +
       tile("환불", "₩96K", "▲ 31%", "down", spark=False, w="80px") + '''
              </div>''',
     "대시보드 맨 위", "<b>세넷이 한 줄</b>. 가장 흔한 자리"),
    (tile("이번 달 목표", "68%", "₩6.8억 / ₩10억", "flat", spark=False),
     "목표 대비", "비교 기준이 <b>지난 기간이 아니라 목표</b>일 때"),
    ('''              <div style="width:100%;max-width:170px;border:1px solid var(--line);border-radius:9px;background:var(--surface);padding:10px 12px;display:grid;gap:3px">
                <span style="font-size:10.5px;color:var(--fg-muted)">이번 주 매출</span>
                <span style="font-size:20px;font-weight:800;font-variant-numeric:tabular-nums">₩1,284,000</span>
                <span style="font-size:10px;color:var(--accent);text-decoration:underline">자세히 보기 ›</span>
              </div>''',
     "눌러서 들어가기", "타일이 <b>상세 화면의 입구</b>가 되기도 한다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 부품의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="큰 숫자와 작은 라벨은 <b>읽는 순서가 반대</b>입니다 — 눈은 숫자를 먼저 보지만, 스크린 리더는 적힌 순서대로 읽습니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"stat"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"stat__label"</span> <span class="a">id</span>=<span class="s">"l1"</span>&gt;이번 주 매출&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">strong</span> <span class="a">class</span>=<span class="s">"stat__value"</span> <span class="a">aria-labelledby</span>=<span class="s">"l1"</span>&gt;₩1,284,000&lt;/<span class="t">strong</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"stat__delta up"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;▲&lt;/<span class="t">span</span>&gt; 12.4% 지난주 대비
  &lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="t">.stat__value</span> { <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">// 방향이 아니라 '좋은 쪽인가'로 색을 고른다</span>
<span class="t">const</span> tone = delta === <span class="a">0</span> ? <span class="s">'flat'</span>
  : (delta &gt; <span class="a">0</span>) === (metric.goodDirection === <span class="s">'up'</span>) ? <span class="s">'up'</span> : <span class="s">'down'</span>;''',
  keys=kbd([
    ("라벨에 기간을 넣는다", "'매출'이 아니라 '<b>이번 주</b> 매출'. 없으면 어떤 숫자인지 알 수 없다"),
    ("증감에 기준을 적는다", "'▲12.4%' 뒤에 <b>지난주 대비</b>가 붙어야 뜻이 생긴다"),
    ("<code>tabular-nums</code>", "자릿수를 맞춘다. 안 맞추면 값이 바뀔 때마다 타일이 흔들린다"),
    ("색은 좋은 쪽으로", "환불·이탈·오류는 <b>올라가면 빨강</b>이다. 지표마다 방향을 데이터에 적어 둔다"),
    ("화살표는 숨긴다", "<code>aria-hidden</code> — '▲'가 '검은 위쪽 삼각형'으로 읽히면 방해만 된다"),
    ("없는 값은 — 으로", "0 으로 채우지 않는다. <b>0건과 모름은 다른 이야기</b>다"),
  ]),
  backend=rows([
    ("집계는 미리 해 둔다", "타일 하나가 전체 테이블을 훑는 질의면 대시보드를 열 때마다 <b>초 단위로 느려집니다.</b> 보통 시간별·일별로 미리 모아 둔 표에서 읽습니다."),
    ("기준 시각", "'이번 주'가 월요일부터인지 일요일부터인지, <b>어느 시간대 기준</b>인지로 숫자가 달라집니다. 서버와 화면이 같은 기준을 써야 합니다."),
    ("증감 계산", "지난주가 0이면 증가율이 <b>무한대</b>가 됩니다. 0 → N 은 비율 대신 '신규'로 적는 식의 규칙이 필요합니다."),
    ("반올림", "₩1,284,000을 '₩1.28M'으로 줄일지, 어디서 반올림할지를 정합니다. <b>화면마다 다르면</b> 같은 숫자가 달라 보입니다."),
    ("타일 네 개 = 요청 네 번?", "묶어서 <b>한 번에</b> 받는 편이 낫습니다. 하나가 느리면 그 타일만 뼈대로 두고 나머지를 먼저 보여 줍니다."),
  ]),
  plat_lede="세 플랫폼 모두 정해진 부품이 없습니다 — 제품마다 직접 만듭니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     tile("이번 주 매출", "₩1.28M", "▲ 12%", "up", spark=False, w="120px"),
     "대시보드마다 직접 만듭니다. 이름도 스탯·메트릭·KPI 로 갈립니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 요약 숫자 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:8px;padding:7px">
                  <span style="font-size:6.5px;color:var(--fg-muted);display:block">이번 주 매출</span>
                  <span style="font-size:12px;font-weight:800;display:block">₩1.28M</span></div>
              </div></div>''',
     "부품은 없지만 <b>위젯</b>과 건강·배터리 화면의 관례가 사실상 기준입니다. 숫자는 크게, 라벨은 아주 작게."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 요약 숫자 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;border:1px solid var(--line);border-radius:10px;padding:7px">
                  <span style="font-size:6.5px;color:var(--fg-muted);display:block">이번 주 매출</span>
                  <span style="font-size:12px;font-weight:800;display:block">₩1.28M</span></div>
              </div></div>''',
     "<b>Card</b> 안에 타입 스케일(<code>displaySmall</code> 등)로 숫자를 키운 것입니다. 전용 부품은 없습니다."),
  ]),
  plat_note="정해진 부품이 없어서 <b>이름부터 팀마다 다릅니다</b> — 스탯 타일·지표 카드·KPI·요약 숫자가 모두 같은 것입니다. 처음 이야기할 때 \"숫자 하나를 크게 보여 주는 칸\"이라고 풀어 말하면 헛걸음이 줄어듭니다.",
  siblings=siblings("stat"),
  related='''        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>차트 고르기</b><em>10부</em></span></li>''',
)
