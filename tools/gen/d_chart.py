# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

A = "var(--accent)"
M = "var(--fg-muted)"
L = "var(--line)"

def svg(inner, w="150px", vb="0 0 120 56", par='xMidYMid meet'):
    return ('              <svg viewBox="' + vb + '" preserveAspectRatio="' + par + '" role="img" '
            'style="width:100%;max-width:' + w + ';height:auto;display:block" aria-hidden="true">' + inner + '</svg>')

def bars(vals, hi=None, w="150px"):
    out = '<line x1="10" y1="48" x2="116" y2="48" stroke="' + L + '" stroke-width="1"/>'
    bw = 16
    for i, v in enumerate(vals):
        x = 14 + i * (bw + 5)
        h = v * 0.38
        c = A if (hi is None or i == hi) else M
        out += '<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s" rx="1"/>' % (x, 48 - h, bw, h, c)
    return svg(out, w)

def line(vals, w="150px", area=False):
    pts = " ".join("%.1f,%.1f" % (12 + i * (100.0 / (len(vals) - 1)), 48 - v * 0.38) for i, v in enumerate(vals))
    out = '<line x1="10" y1="48" x2="116" y2="48" stroke="' + L + '" stroke-width="1"/>'
    if area:
        out += '<polygon points="12,48 ' + pts + ' 112,48" fill="' + A + '" opacity=".15"/>'
    out += '<polyline points="' + pts + '" fill="none" stroke="' + A + '" stroke-width="2" stroke-linejoin="round"/>'
    return svg(out, w)

def dots(w="150px"):
    pts = [(20, 40), (34, 33), (48, 36), (60, 25), (74, 22), (88, 16), (102, 12), (30, 28), (66, 31)]
    out = '<line x1="10" y1="48" x2="116" y2="48" stroke="' + L + '" stroke-width="1"/><line x1="12" y1="8" x2="12" y2="48" stroke="' + L + '" stroke-width="1"/>'
    out += "".join('<circle cx="%d" cy="%d" r="2.6" fill="%s" opacity=".75"/>' % (x, y, A) for x, y in pts)
    return svg(out, w)

def pie(w="110px"):
    out = ('<circle cx="28" cy="28" r="24" fill="' + M + '" opacity=".25"/>'
           '<path d="M28 28 L28 4 A24 24 0 0 1 48.8 40 Z" fill="' + A + '"/>')
    return svg(out, w, "0 0 56 56")

def stacked(w="150px"):
    out = '<line x1="10" y1="48" x2="116" y2="48" stroke="' + L + '" stroke-width="1"/>'
    data = [(22, 12), (18, 16), (26, 10), (20, 18)]
    for i, (a, b) in enumerate(data):
        x = 16 + i * 25
        out += '<rect x="%d" y="%.1f" width="16" height="%.1f" fill="%s" rx="1"/>' % (x, 48 - a, a, A)
        out += '<rect x="%d" y="%.1f" width="16" height="%.1f" fill="%s" opacity=".45" rx="1"/>' % (x, 48 - a - b, b, M)
    return svg(out, w)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-size:11.5px;font-weight:700">11월 가맹점별 매출</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + bars([62, 44, 80, 30], 2, "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">막대의 밑은 <b>0</b>에서 시작한다 — 잘라내면 거짓말이 된다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">눈금에 단위를 적는다 — 만 원? 건?</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">색은 뜻이 있을 때만. 네 색 쓰면 넷을 외워야 한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">&lt;table&gt; 를 같이 둔다 — 눈으로 안 보는 사람의 길</div>
                </div>
              </div>'''

D = dict(
  slug="chart", ko="차트 고르기", en="Choosing a chart",
  desc="무엇을 묻느냐로 차트 종류가 정해진다. 비교·추세·분포·비율의 네 질문과 흔한 거짓말들.",
  lede="차트는 <b>질문이 먼저</b>입니다. 무엇을 묻느냐가 정해지면 그릴 그림은 거의 자동으로 정해집니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>묻고 싶은 것을 골라 보세요. <b>맞는 그림</b>과 <b>흔히 잘못 고르는 그림</b>이 나란히 나옵니다.<br>
          <b>축을 0에서 자르기</b>를 켜 보면 같은 숫자가 어떻게 <b>세 배쯤 달라 보이는지</b> 알 수 있습니다 —
          보고서에서 가장 자주 나오는 거짓말입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "차트, 그래프, 도표, 시각화"),
    ("영어", "chart, graph, plot, data visualization"),
    ("같이 쓰는 말",
     "막대그래프가 <b>바 차트</b>, 눕히면 <b>가로 막대</b>(horizontal bar), "
     "선이 <b>라인 차트</b>, 밑을 칠하면 <b>에어리어</b>, "
     "점이 <b>산점도</b>(scatter), 원이 <b>파이</b>·<b>도넛</b>입니다. "
     "작게 줄여 글 속에 넣은 선을 <b>스파크라인</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>그래프</b> — 일상에서는 같은 말이지만 전산에서 '그래프'는 <b>점과 선의 연결 구조</b>를 뜻하기도 합니다.<br>"
     "<b>대시보드</b> — 차트 여럿을 모아 둔 <b>화면</b>이지 차트 자체가 아닙니다.<br>"
     "<b>인포그래픽</b> — 데이터보다 <b>설명</b>이 주인입니다. 정확도 기준이 다릅니다."),
  ]),
  axes=ax("차트 고르기"),
  oneline="차트를 고르기 전에 <b>한 문장</b>으로 물음을 적으세요. '누가 제일 큰가'와 '언제부터 늘었나'는 다른 그림입니다.",
  s4_title="질문별로 고르기", s4_hint="그림이 아니라 물음이 먼저다",
  states=states([
    (bars([62, 44, 80, 30], 2), "누가 제일 큰가", "<b>막대</b>. 길이는 눈이 가장 잘 견준다"),
    (line([20, 28, 26, 44, 52, 70]), "언제부터 늘었나", "<b>선</b>. 시간은 가로로 흐른다"),
    (dots(), "둘이 같이 움직이나", "<b>산점도</b>. 점이 뭉치면 투명도를 준다"),
    (pie(), "전체의 몇 할인가", "<b>파이</b>. 조각이 <b>두셋</b>일 때만"),
    (stacked(), "묶음 안의 구성", "<b>쌓은 막대</b>. 맨 아래 조각만 견주기 쉽다"),
    (line([30, 32, 31, 34, 33, 36], area=True), "대충 흐름만", "<b>스파크라인</b>. 눈금 없이 글 옆에 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("제목", "무엇의 무엇인가", "'매출'이 아니라 <b>'11월 가맹점별 매출'</b>"),
    ("그림", "막대·선·점", "<b>물음에 맞는</b> 모양 하나"),
    ("0 기준선", "막대는 필수", "자르면 작은 차이가 <b>세 배로</b> 보인다"),
    ("눈금과 단위", "원? 만 원? 건?", "숫자만 있으면 크기를 못 읽는다"),
    ("색", "뜻이 있을 때만", "강조할 하나만 진하게. 나머지는 회색으로"),
    ("표도 함께", "&lt;table&gt;", "그림은 <b>눈으로만</b> 읽힌다. 숫자 표를 같이 둔다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>막대의 밑은 0 이어야 합니다.</b> 길이로 크기를 읽는 그림이라
          밑을 잘라내면 눈이 읽는 비율 자체가 거짓이 됩니다.
          100·102·104 를 98 부터 그리면 <b>두 배 차이</b>처럼 보입니다.
          선 그래프는 '변화'를 읽는 그림이라 잘라도 되지만,
          이때는 <b>축에 잘랐다고 적어</b> 둡니다.</p>''',
  do=ul([
    "숫자들의 <b>관계</b>를 한눈에 보여야 할 때",
    "<b>흐름·크기 차이</b>가 표로는 안 보일 때",
    "볼 사람이 <b>정확한 값이 아니라 경향</b>을 원할 때",
  ]),
  dont=ul([
    "값이 <b>서넛</b>일 때 — 그냥 숫자로 적는 게 빠르다",
    "<b>정확한 값</b>이 필요할 때 → <a href=\"table.html\">데이터 테이블</a>",
    "조각이 다섯을 넘는 파이 — <b>막대로 바꾼다</b>",
    "3차원·기울인 그림 — 보기에만 좋고 <b>크기를 왜곡</b>한다",
  ]),
  instead='정확한 값이면 <a href="table.html">데이터 테이블</a>, 값 하나면 <a href="../items/stat.html">스탯</a>, 비율 하나면 <a href="../items/progress.html">프로그레스</a>.',
  cases=cases([
    (bars([62, 44, 80, 30], 2, "150px"), "강조는 하나만", "말하려는 막대만 진하게, 나머지는 회색"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px">
                <div style="font-size:9px;color:var(--fg-muted)">이번 달 매출</div>
                <div style="font-size:15px;font-weight:700;font-variant-numeric:tabular-nums">24.7억</div>
                ''' + line([30, 32, 31, 36, 34, 40], "100%", True).strip() + '''
              </div>''',
     "스탯 + 스파크라인", "값 하나와 <b>흐름</b>을 같이. 대시보드의 기본 칸"),
    ('''              <div style="width:100%;max-width:150px">
                ''' + bars([100, 102, 104], None, "100%").strip() + '''
                <span style="display:block;font-size:8.5px;color:var(--danger);margin-top:3px">같은 숫자를 98부터 그리면 두 배로 보인다</span>
              </div>''',
     "0에서 시작한 막대", "차이가 작으면 <b>작게 보이는 것이 맞다</b>"),
  ]),
  s8_title="최소 마크업과 접근", s8_hint="이 차트의 계약서",
  code_lede="차트는 <b>그림</b>이므로 이름을 붙이고, 숫자는 표로 한 벌 더 둡니다.",
  code='''&lt;<span class="t">figure</span>&gt;
  &lt;<span class="t">figcaption</span>&gt;11월 가맹점별 매출 (단위: 만 원)&lt;/<span class="t">figcaption</span>&gt;

  &lt;<span class="t">svg</span> <span class="a">role</span>=<span class="s">"img"</span>
       <span class="a">aria-label</span>=<span class="s">"막대그래프. 새벽상사가 80으로 가장 높다"</span>&gt;…&lt;/<span class="t">svg</span>&gt;

  &lt;<span class="t">table</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;      <span class="c">&lt;!-- 숫자를 읽을 길 --&gt;</span>
    &lt;<span class="t">tr</span>&gt;&lt;<span class="t">th</span>&gt;모란상회&lt;/<span class="t">th</span>&gt;&lt;<span class="t">td</span>&gt;62&lt;/<span class="t">td</span>&gt;&lt;/<span class="t">tr</span>&gt;
  &lt;/<span class="t">table</span>&gt;
&lt;/<span class="t">figure</span>&gt;

<span class="c">/* 그림은 칸을 따르되 찌그러지지 않게 */</span>
<span class="t">svg</span> { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">height</span>: auto; }   <span class="c">/* viewBox + xMidYMid meet */</span>''',
  keys=kbd([
    ("<code>role=\"img\"</code> + <code>aria-label</code>", "<b>무엇을 말하는 그림인지</b> 한 문장. '차트'라고만 적으면 쓸모없다"),
    ("<code>&lt;figcaption&gt;</code>", "제목과 <b>단위</b>. 눈으로 보는 사람에게도 필요하다"),
    ("숨은 <code>&lt;table&gt;</code>", "정확한 값을 읽을 유일한 길. <code>sr-only</code>로 둬도 된다"),
    ("색만으로 구분하지 않는다", "선은 <b>모양</b>(점선·실선)이나 직접 라벨로도 가른다"),
    ("<code>preserveAspectRatio</code>", "기본은 <code>xMidYMid meet</code>. <code>none</code>으로 두면 <b>원이 타원</b>이 된다"),
    ("움직임", "그리며 자라는 연출은 <code>prefers-reduced-motion</code>에서 끈다"),
  ]),
  backend=rows([
    ("집계는 서버에서", "10만 건을 보내 브라우저가 더하게 하면 느립니다. <b>이미 더한 값</b>을 보냅니다."),
    ("구간을 정해 보낸다", "일별인지 주별인지는 <b>서버가 결정</b>해 보내야 눈금이 흔들리지 않습니다. 기간이 길면 자동으로 묶습니다."),
    ("빈 구간을 채운다", "거래가 없는 날은 행이 아예 없습니다. 그대로 그리면 <b>날짜가 건너뛴 선</b>이 됩니다. 0 을 채워 보냅니다."),
    ("시간대", "'11월 1일'이 서버 기준인지 보는 사람 기준인지에 따라 숫자가 달라집니다. <b>기준을 적어</b> 보냅니다."),
    ("점이 너무 많을 때", "1년치 분당 데이터는 50만 점입니다. 서버에서 <b>솎아</b>(downsample) 보내고, 확대하면 그 구간만 다시 받습니다."),
  ]),
  plat_lede="표준 부품이 없어 <b>어디서나 라이브러리</b>를 씁니다.",
  plats=plats([
    ("웹", "SVG / Canvas",
     bars([62, 44, 80], 2, "110px"),
     "점이 수천 개를 넘으면 SVG 가 느려집니다. 그때 <b>캔버스</b>로 바꿉니다."),
    ("iOS", "Swift Charts",
     '''              <div class="phone" role="img" aria-label="iOS 차트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <svg viewBox="0 0 40 24" style="position:absolute;left:4px;right:4px;top:30px;width:calc(100% - 8px)" aria-hidden="true"><rect x="4" y="10" width="6" height="12" fill="#2f6df6"/><rect x="14" y="6" width="6" height="16" fill="#2f6df6"/><rect x="24" y="14" width="6" height="8" fill="#2f6df6"/></svg></div></div>''',
     "2022년부터 <b>OS 기본 차트</b>가 생겼습니다. 다크 모드와 글자 크기를 알아서 따릅니다."),
    ("안드로이드", "라이브러리",
     '''              <div class="phone" role="img" aria-label="안드로이드 차트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <svg viewBox="0 0 40 24" style="position:absolute;left:4px;right:4px;top:30px;width:calc(100% - 8px)" aria-hidden="true"><polyline points="4,20 12,14 20,16 28,8 36,6" fill="none" stroke="#2f6df6" stroke-width="1.5"/></svg></div></div>''',
     "OS 기본 차트가 없어 외부 라이브러리를 씁니다. Compose 로 <b>직접 그리는</b> 경우도 많습니다."),
  ]),
  plat_note="\"차트 하나 넣어 주세요\"를 받으면 <b>무엇을 묻는 그림인지</b>를 먼저 물으세요. '매출 차트'는 요구사항이 아닙니다 — '지난달 대비 어느 가맹점이 늘었나'여야 막대인지 선인지가 정해지고, 그래야 서버가 어떤 모양으로 집계해 보낼지도 정해집니다.",
  siblings=siblings("chart"),
  related='''        <li><a href="../items/stat.html"><b>스탯</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스</b><em>8부</em></a></li>
        <li><a href="../items/color.html"><b>색 역할</b><em>2부</em></a></li>''',
)
