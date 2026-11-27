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
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">막대의 밑은 <b>0</b>에서 시작, 자르면 차이가 부풀어 보임</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">눈금에 만 원인지 건인지 단위를 적음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">색은 뜻이 있을 때만, 네 색이면 넷을 외워야 함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">&lt;table&gt;을 같이 두어 스크린 리더로도 읽게 함</div>
                </div>
              </div>'''

D = dict(
  slug="chart", ko="차트 고르기", en="Choosing a chart",
  desc="무엇을 묻느냐에 따라 차트 종류가 정해진다는 것을 비교·추세·분포·비율의 네 가지 질문과 숫자를 잘못 읽게 만드는 흔한 그림들로 보여 주는 항목입니다.",
  lede="차트를 고를 때는 <b>질문부터</b> 정합니다. 데이터에 무엇을 묻는지가 정해지면 어떤 그림을 그릴지는 거의 저절로 정해집니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>묻고 싶은 것을 골라 보세요. <b>질문에 맞는 그림</b>과 <b>흔히 잘못 고르는 그림</b>이 나란히 나옵니다.<br>
          <b>축을 0에서 자르기</b>를 켜 보면 같은 숫자인데도 막대 길이가 <b>세 배쯤 달라 보입니다</b>.
          보고서에서 숫자를 부풀려 보이게 하는 가장 흔한 방법입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "차트, 그래프, 도표, 시각화"),
    ("영어", "chart, graph, plot, data visualization"),
    ("같이 쓰는 말",
     "막대그래프는 <b>바 차트</b>, 막대를 눕힌 것은 <b>가로 막대</b>(horizontal bar), "
     "꺾은선은 <b>라인 차트</b>, 선 아래를 칠한 것은 <b>에어리어</b>, "
     "점으로 찍은 것은 <b>산점도</b>(scatter), 원을 나눈 것은 <b>파이</b>·<b>도넛</b>이라고 부릅니다. "
     "선 그래프를 작게 줄여 글 속에 넣은 것은 <b>스파크라인</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>그래프</b> — 일상에서는 차트와 같은 말로 쓰지만, 전산에서 '그래프'는 <b>점과 선으로 이루어진 연결 구조</b>를 뜻하기도 합니다.<br>"
     "<b>대시보드</b> — 대시보드는 차트 여러 개를 모아 둔 <b>화면</b>을 가리킵니다.<br>"
     "<b>인포그래픽</b> — 인포그래픽은 데이터보다 <b>설명</b>을 전하는 데 중심을 두기 때문에, 차트와는 정확도를 따지는 기준이 다릅니다."),
  ]),
  axes=ax("차트 고르기"),
  oneline="차트를 고르기 전에 무엇을 묻는지 <b>한 문장</b>으로 적으세요. 같은 데이터라도 '누가 제일 큰가'를 물으면 막대, '언제부터 늘었나'를 물으면 꺾은선처럼 맞는 그림이 달라집니다.",
  s4_title="질문에 따라 고르는 차트", s4_hint="그림보다 질문을 먼저 정합니다",
  states=states([
    (bars([62, 44, 80, 30], 2), "누가 제일 큰가", "<b>막대</b>를 씁니다. 사람의 눈은 길이를 가장 정확하게 견줍니다"),
    (line([20, 28, 26, 44, 52, 70]), "언제부터 늘었나", "<b>선</b>을 씁니다. 시간을 가로축에 놓고 왼쪽에서 오른쪽으로 읽습니다"),
    (dots(), "둘이 같이 움직이나", "<b>산점도</b>를 씁니다. 점이 한곳에 뭉치면 점을 반투명하게 해서 겹친 정도가 보이게 합니다"),
    (pie(), "전체의 몇 할인가", "<b>파이</b>를 씁니다. 다만 조각이 <b>두세 개</b>일 때만 알아보기 쉽습니다"),
    (stacked(), "묶음 안이 어떻게 나뉘나", "<b>쌓은 막대</b>를 씁니다. 다만 기준선이 같은 맨 아래 조각만 막대끼리 견주기 쉽습니다"),
    (line([30, 32, 31, 34, 33, 36], area=True), "흐름만 대강 보려면", "<b>스파크라인</b>을 씁니다. 눈금 없이 글 옆에 작게 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("제목", "무엇의 무엇인가", "'매출'이 아니라 <b>'11월 가맹점별 매출'</b>처럼 무엇을 어떻게 나눈 값인지 적습니다"),
    ("그림", "막대·선·점", "<b>질문에 맞는</b> 모양 하나를 고릅니다"),
    ("0 기준선", "막대는 필수", "막대 아래를 자르면 작은 차이가 <b>세 배</b>쯤으로 부풀어 보입니다"),
    ("눈금과 단위", "원? 만 원? 건?", "눈금 숫자만 있고 단위가 없으면 값이 얼마나 큰지 읽을 수 없습니다"),
    ("색", "뜻이 있을 때만", "강조할 항목 하나만 진한 색으로 칠하고 나머지는 회색으로 둡니다"),
    ("표도 함께", "&lt;table&gt;", "그림은 <b>눈으로만</b> 읽을 수 있으므로 숫자 표를 함께 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>막대는 0에서 시작해야 합니다.</b> 막대그래프는 길이로 크기를 읽는 그림이라
          아래를 잘라 내면 눈으로 읽는 길이의 비율이 실제 값의 비율과 달라집니다.
          예를 들어 100·102·104를 98부터 그리면 겨우 2% 차이가 <b>두 배 차이</b>처럼 보입니다.
          선 그래프는 값의 '변화'를 읽는 그림이라 축을 잘라도 되지만,
          이때는 <b>축을 잘랐다는 표시를</b> 해 둡니다.</p>''',
  do_title="차트를 쓰는 경우",
  dont_title="차트를 쓰지 않거나 피해야 하는 경우",
  instead_title="차트 대신 다른 것을 써야 하는 경우",
  do=ul([
    "숫자들 사이의 <b>관계</b>를 한눈에 보여 줘야 할 때",
    "<b>흐름이나 크기 차이</b>가 표로는 잘 보이지 않을 때",
    "보는 사람이 <b>정확한 값보다 경향</b>을 알고 싶어 할 때",
  ]),
  dont=ul([
    "값이 <b>서너 개</b>뿐일 때. 숫자로 적는 편이 더 빨리 읽힙니다",
    "<b>정확한 값</b>이 필요할 때. <a href=\"table.html\">데이터 테이블</a>이 맞습니다",
    "조각이 다섯 개를 넘는 파이를 그릴 때. <b>막대로 바꿉니다</b>",
    "3차원으로 그리거나 기울인 그림을 쓸 때. 보기에만 좋을 뿐 <b>크기를 왜곡</b>합니다",
  ]),
  instead='정확한 값을 읽어야 하면 <a href="table.html">데이터 테이블</a>로 보여 주고, 값 하나만 크게 보여 주면 되는 경우에는 <a href="../items/stat.html">스탯</a>을 씁니다. 비율 하나만 보여 줄 때는 <a href="../items/progress.html">프로그레스</a> 막대가 더 알아보기 쉽습니다.',
  cases=cases([
    (bars([62, 44, 80, 30], 2, "150px"), "강조할 막대 하나만 칠하기", "말하려는 막대만 진하게 칠하고 나머지는 회색으로 둡니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px">
                <div style="font-size:9px;color:var(--fg-muted)">이번 달 매출</div>
                <div style="font-size:15px;font-weight:700;font-variant-numeric:tabular-nums">24.7억</div>
                ''' + line([30, 32, 31, 36, 34, 40], "100%", True).strip() + '''
              </div>''',
     "스탯과 스파크라인을 함께 두기", "값 하나와 그 값의 <b>흐름</b>을 함께 보여 줍니다. 대시보드에서 가장 흔한 칸입니다"),
    ('''              <div style="width:100%;max-width:150px">
                ''' + bars([100, 102, 104], None, "100%").strip() + '''
                <span style="display:block;font-size:8.5px;color:var(--danger);margin-top:3px">같은 숫자도 98부터 그리면 두 배로 보임</span>
              </div>''',
     "막대를 0에서 시작하기", "실제 차이가 작으면 그림에서도 <b>차이가 작게 보여야 맞습니다</b>"),
  ]),
  s8_title="최소 마크업과 접근성", s8_hint="차트를 만들 때 꼭 갖출 것",
  code_lede="차트는 <b>그림</b>이므로 무엇을 보여 주는지 이름을 붙이고, 숫자는 표로 한 벌 더 둡니다.",
  code='''&lt;<span class="t">figure</span>&gt;
  &lt;<span class="t">figcaption</span>&gt;11월 가맹점별 매출 (단위: 만 원)&lt;/<span class="t">figcaption</span>&gt;

  &lt;<span class="t">svg</span> <span class="a">role</span>=<span class="s">"img"</span>
       <span class="a">aria-label</span>=<span class="s">"막대그래프. 새벽상사가 80으로 가장 높다"</span>&gt;…&lt;/<span class="t">svg</span>&gt;

  &lt;<span class="t">table</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;      <span class="c">&lt;!-- 숫자를 읽을 수 있게 표를 함께 둔다 --&gt;</span>
    &lt;<span class="t">tr</span>&gt;&lt;<span class="t">th</span>&gt;모란상회&lt;/<span class="t">th</span>&gt;&lt;<span class="t">td</span>&gt;62&lt;/<span class="t">td</span>&gt;&lt;/<span class="t">tr</span>&gt;
  &lt;/<span class="t">table</span>&gt;
&lt;/<span class="t">figure</span>&gt;

<span class="c">/* 그림은 칸을 따르되 찌그러지지 않게 */</span>
<span class="t">svg</span> { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">height</span>: auto; }   <span class="c">/* viewBox + xMidYMid meet */</span>''',
  keys=kbd([
    ("<code>role=\"img\"</code>와 <code>aria-label</code>", "<b>그림이 무엇을 보여 주는지</b> 한 문장으로 적습니다. '차트'라고만 적으면 스크린 리더 사용자는 아무 정보도 얻지 못합니다"),
    ("<code>&lt;figcaption&gt;</code>", "제목과 <b>단위</b>를 적습니다. 눈으로 보는 사람에게도 필요한 정보입니다"),
    ("화면에서 숨긴 <code>&lt;table&gt;</code>", "스크린 리더 사용자가 정확한 값을 읽을 수 있는 유일한 방법입니다. <code>sr-only</code>로 화면에서 숨겨 둬도 됩니다"),
    ("색만으로 구분하지 않기", "선은 색과 함께 <b>모양</b>(점선·실선)을 다르게 하거나 선 옆에 이름을 직접 붙여 구분합니다"),
    ("<code>preserveAspectRatio</code>", "기본값은 <code>xMidYMid meet</code>입니다. <code>none</code>으로 두면 칸 비율에 맞춰 늘어나 <b>원이 타원</b>이 됩니다"),
    ("그려지는 움직임 끄기", "막대나 선이 자라나며 그려지는 연출은 <code>prefers-reduced-motion</code>이 켜져 있으면 끕니다"),
  ]),
  backend=rows([
    ("집계는 서버에서 하기", "10만 건을 그대로 보내 브라우저가 더하게 하면 느립니다. 서버가 <b>미리 더한 값</b>을 보냅니다."),
    ("묶는 구간은 서버가 정해 보내기", "일별로 묶을지 주별로 묶을지는 <b>서버가 정해서</b> 보내야 화면마다 눈금이 달라지지 않습니다. 기간이 길면 서버가 알아서 더 큰 단위로 묶습니다."),
    ("거래가 없는 날을 0으로 채우기", "거래가 없는 날은 데이터베이스에 행이 아예 없어서, 그대로 그리면 <b>날짜를 건너뛴 선</b>이 됩니다. 그래서 빈 날짜에는 0을 채워 보냅니다."),
    ("날짜를 자르는 시간대", "'11월 1일'을 서버 시간대로 자르느냐 보는 사람의 시간대로 자르느냐에 따라 숫자가 달라집니다. 응답에 <b>어느 시간대 기준인지 적어</b> 보냅니다."),
    ("점이 너무 많을 때", "1년치 분 단위 데이터는 50만 점이 넘습니다. 서버에서 점을 <b>솎아</b>(downsample) 보내고, 사용자가 확대하면 그 구간만 자세히 다시 받습니다."),
  ]),
  plat_lede="차트는 표준 부품이 드물어서 <b>대부분 라이브러리</b>를 씁니다.",
  plats=plats([
    ("웹", "SVG / Canvas",
     bars([62, 44, 80], 2, "110px"),
     "점이 수천 개를 넘으면 SVG가 느려지므로, 그때는 <b>캔버스</b>로 바꿉니다."),
    ("iOS", "Swift Charts",
     '''              <div class="phone" role="img" aria-label="iOS 차트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <svg viewBox="0 0 40 24" style="position:absolute;left:4px;right:4px;top:30px;width:calc(100% - 8px)" aria-hidden="true"><rect x="4" y="10" width="6" height="12" fill="#2f6df6"/><rect x="14" y="6" width="6" height="16" fill="#2f6df6"/><rect x="24" y="14" width="6" height="8" fill="#2f6df6"/></svg></div></div>''',
     "2022년부터 <b>OS 기본 차트</b>가 생겼고, 다크 모드와 글자 크기 설정을 알아서 따릅니다."),
    ("안드로이드", "라이브러리",
     '''              <div class="phone" role="img" aria-label="안드로이드 차트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <svg viewBox="0 0 40 24" style="position:absolute;left:4px;right:4px;top:30px;width:calc(100% - 8px)" aria-hidden="true"><polyline points="4,20 12,14 20,16 28,8 36,6" fill="none" stroke="#2f6df6" stroke-width="1.5"/></svg></div></div>''',
     "OS 기본 차트가 없어서 외부 라이브러리를 쓰고, Compose로 <b>직접 그리는</b> 경우도 많습니다."),
  ]),
  plat_note="\"차트 하나 넣어 주세요\"라는 요청을 받으면 <b>무엇을 묻는 그림인지</b>부터 물어보세요. '매출 차트'만으로는 무엇을 그릴지 정할 수 없습니다. '지난달보다 어느 가맹점이 늘었나'처럼 질문이 구체적이어야 막대를 쓸지 선을 쓸지 정해지고, 그래야 서버가 어떤 모양으로 집계해 보낼지도 정해집니다.",
  siblings=siblings("chart"),
  related='''        <li><a href="../items/stat.html"><b>스탯</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스</b><em>8부</em></a></li>
        <li><a href="../items/color.html"><b>색 역할</b><em>2부</em></a></li>''',
)
