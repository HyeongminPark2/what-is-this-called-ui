# -*- coding: utf-8 -*-
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def num(txt, tag, ok=None, note="", w="152px"):
    return one('<span style="font-family:var(--mono);font-size:11px;font-variant-numeric:tabular-nums">' + txt + '</span>',
               tag, ok, note, w)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">표 안에서는 1,284,000원처럼 자릿수를 맞춤</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">요약 타일에서는 128만 원처럼 줄여 적음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">원인지 건인지 알도록 단위를 꼭 붙임</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">복수형이 없어 0건 · 1건도 그대로 적음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">소수점은 33.3%처럼 한 자리까지</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한국어는 만 단위로 끊어 읽으므로 1.28M은 맞지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="numbertext", ko="숫자와 단위 쓰기", en="Writing numbers & units",
  desc="숫자를 놓는 자리에 따라 끊어 적는 방법을 다룹니다. 만·억 단위와 단위 붙이기, 0건과 1건, 퍼센트 반올림까지 함께 봅니다.",
  lede="같은 값이라도 <b>어디에 적는지</b>에 따라 표기가 달라집니다. 또 <b>단위 없는 숫자</b>만으로는 무엇을 센 값인지 알 수 없습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>값과 자리를 바꿔 보세요. <b>표 안</b>에서는 세로로 견주기 쉽도록 자릿수를 맞춰 적고,
          <b>요약 타일</b>에서는 한눈에 읽히도록 크게 줄여 적습니다.<br>
          한국어는 <b>만·억</b> 단위로 끊어 읽기 때문에 ‘1.2M’보다 <b>‘128만 원’</b>이 훨씬 빨리 읽힙니다.
          아래에는 건수와 비율을 적을 때 자주 틀리는 것을 모아 두었습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자릿수 구분, 천 단위 쉼표, 단위 표기, 반올림"),
    ("영어", "number formatting, thousands separator, abbreviation, rounding"),
    ("같이 쓰는 말",
     "세 자리마다 찍는 쉼표를 <b>천 단위 구분</b>이라 하고, "
     "큰 수를 짧게 줄여 적는 것을 <b>약어 표기</b>(abbreviation)라고 합니다. "
     "브라우저에서 언어에 맞춰 숫자를 적어 주는 기능은 <code>Intl.NumberFormat</code>이며, "
     "화폐·퍼센트·단위까지 다룹니다."),
    ("자주 잘못 부르는 이름",
     "<b>숫자 꼴</b> — <a href=\"../items/numerals.html\">숫자 꼴</a>은 등폭 숫자처럼 <b>글자의 생김새</b>를 다루고, 이 항목은 숫자로 <b>무엇을 적을지</b>를 다룹니다.<br>"
     "<b>포맷팅</b> — 날짜·시간 표기까지 아우르는 넓은 말입니다. <a href=\"datetime.html\">날짜와 시간</a> 표기는 따로 다룹니다.<br>"
     "<b>단위</b> — 여기서 말하는 단위는 길이·무게의 단위계와 다르며, 화면에서는 <b>원·건·%</b>가 대부분입니다."),
  ]),
  s4_title="놓이는 자리별 숫자 표기", s4_hint="같은 값을 자리에 맞게 다르게 적기",
  states=states([
    (num('1,284,000원', "표 안", True, "자릿수를 맞춰 세로로 견줌"), "표 안의 금액", "<a href=\"../items/numerals.html\">등폭 숫자</a>와 함께 씁니다"),
    (num('128만 원', "요약 타일", True, "크게 줄여 한눈에 읽힘"), "요약 타일의 금액", "<a href=\"../items/stat.html\">스탯</a>에서 씁니다"),
    (num('약 128만 원', "문장 속", True, "읽는 대로 적음"), "문장 속의 금액", "쉼표로 끊은 긴 숫자를 문장에 넣으면 <b>잘 읽히지 않습니다</b>"),
    (num('1,284,000', "단위 없이", False, "원인지 건인지 알 수 없음"), "단위를 빠뜨린 숫자", "<b>가장 흔한 실수</b>입니다"),
    (num('1.28M', "영어식 줄임", False, "한국어는 만 단위로 끊어 읽음"), "K · M으로 줄인 숫자", "읽는 사람이 만 단위로 <b>한 번 더 계산</b>해야 합니다"),
    (num('0건', "없을 때", True, "빈칸이나 ‘-’로 두지 않음"), "0건일 때", "<a href=\"emptytext.html\">빈 상태 문구</a>와 함께 씁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("표 안", "1,284,000원", "자릿수를 맞춰 <b>세로로 견주기 쉽게</b> 적습니다"),
    ("요약 타일", "128만 원", "크게 줄여 <b>한눈에</b> 읽히게 적습니다"),
    ("단위", "원 · 건 · %", "<b>반드시 붙입니다.</b> 단위가 없으면 무엇을 센 숫자인지 알 수 없습니다"),
    ("건수", "0건 · 1건", "한국어에는 <b>복수형이 없으므로</b> 0건도 1건도 그대로 적습니다"),
    ("소수점", "한 자리까지", "33.3%처럼 한 자리까지 적습니다. 자릿수를 더 적으면 <b>틀린 인상</b>을 줍니다"),
    ("K · M", "쓰지 않음", "한국어는 <b>만·억</b> 단위로 끊어 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>비율을 하나씩 반올림하면 합계가 맞지 않을 수 있습니다.</b>
          예를 들어 33.33% · 33.33% · 33.33%를 각각 소수점 한 자리로 반올림하면 33.3 × 3 = 99.9가 되어
          <b>합이 100%가 되지 않습니다</b>.
          차트 범례나 구성비 표처럼 비율을 여럿 늘어놓는 화면에서는
          <b>가장 큰 항목에 나머지를 몰아주거나</b>,
          '합이 100%가 안 될 수 있습니다'라는 문구를 작게 적어 둡니다.
          반올림할 때는 <b>작은 값을 0으로 만들지 않는</b> 것도 중요합니다.
          0.4%를 0%로 적으면 그 항목이 '없다'는 뜻으로 읽히기 때문입니다.</p>''',
  do=ul([
    "원 · 건 · % 같은 <b>단위를 꼭</b> 붙이기",
    "표에서는 자릿수를 맞추고 <b>오른쪽 정렬</b>하기",
    "요약에서는 <b>만·억</b>으로 줄이기",
  ]),
  do_title="숫자와 단위를 적을 때 지킬 것", dont_title="숫자와 단위를 적을 때 피할 것",
  instead_title="숫자와 단위 쓰기와 함께 보면 좋은 항목",
  dont=ul([
    "단위 없이 숫자만 적을 때. <b>무엇을 센 숫자인지 알 수 없습니다</b>",
    "<b>K · M</b>으로 줄일 때. 한국어 독자는 만 단위로 한 번 더 계산해야 합니다",
    "0을 ‘-’나 빈칸으로 둘 때. <b>0건이라고 적습니다</b>",
    "작은 값을 0으로 반올림할 때. 그 항목이 <b>없는 것처럼</b> 보입니다",
  ]),
  instead='숫자 글자의 생김새는 <a href="../items/numerals.html">숫자 꼴</a>에서, 요약 숫자 하나를 크게 보여 주는 칸은 <a href="../items/stat.html">스탯</a>에서, 비율을 그림으로 보여 주는 방법은 <a href="chart.html">차트 고르기</a>에서 다룹니다.',
  cases=cases([
    (num('9,827,500원<br>1,284,000원<br>&nbsp;&nbsp;&nbsp;11,100원', "표", True, "오른쪽 정렬 + 등폭 숫자"),
     "표 안의 금액", "금액을 <b>세로로 견주어 보는</b> 자리입니다"),
    (num('24.7억', "요약 타일", True, "큰 글자로 줄여 읽힘"), "요약 타일의 큰 금액", "줄여 적어도 됩니다. <b>정확한 값은 표에</b> 따로 있습니다"),
    (num('33.3% · 33.3% · 33.4%', "비율", True, "합이 100이 되게 맞춤"), "구성비의 반올림 맞추기", "각각 반올림하면 <b>합이 100이 되지 않을 수</b> 있어 맞춰 줍니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="<code>Intl.NumberFormat</code>은 언어와 화폐에 맞는 표기를 함께 처리합니다.",
  code='''<span class="c">// 표 안에서는 자릿수를 끊고 단위를 붙인다</span>
<span class="k">new</span> Intl.NumberFormat(<span class="s">'ko-KR'</span>, { style: <span class="s">'currency'</span>, currency: <span class="s">'KRW'</span> })
  .format(<span class="a">1284000</span>);          <span class="c">// '₩1,284,000'</span>

<span class="c">// 요약에서는 만 · 억으로 줄인다 (Intl 은 한국어 단위를 자동으로 주지 않는다)</span>
<span class="k">function</span> short(n) {
  <span class="k">if</span> (n &gt;= <span class="a">1e8</span>) <span class="k">return</span> (n / <span class="a">1e8</span>).toFixed(<span class="a">1</span>).replace(<span class="s">/\\.0$/</span>, <span class="s">''</span>) + <span class="s">'억'</span>;
  <span class="k">if</span> (n &gt;= <span class="a">1e4</span>) <span class="k">return</span> (n / <span class="a">1e4</span>).toFixed(<span class="a">0</span>) + <span class="s">'만'</span>;
  <span class="k">return</span> n.toLocaleString(<span class="s">'ko-KR'</span>);
}

<span class="c">/* 표에서는 오른쪽 정렬 + 등폭 숫자 */</span>
<span class="t">td</span>.num { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }''',
  keys_heads="<th>지킬 규칙과 마크업</th><th>지키는 방법과 이유</th>",
  keys=kbd([
    ("<code>Intl.NumberFormat</code>", "쉼표·화폐·퍼센트를 언어에 맞춰 적어 주므로 <b>쉼표를 직접 찍지 않습니다</b>"),
    ("<code>notation: 'compact'</code>", "영어로는 <code>1.2M</code>, 한국어로는 <code>128만</code>처럼 줄여 줍니다. 다만 고르는 <b>단위가 화면에 맞지 않을 때</b>가 있어 직접 만들어 쓰기도 합니다"),
    ("<code>tabular-nums</code>", "표에서 숫자 폭을 같게 해 자릿수를 맞춥니다(<a href=\"../items/numerals.html\">숫자 꼴</a>)"),
    ("스크린 리더로 읽을 때", "<code>1,284,000</code>은 '백이십팔만 사천'으로 읽히는데, <b>단위가 없으면</b> 듣는 사람은 무엇을 센 숫자인지 알 수 없습니다"),
    ("<code>&lt;bdi&gt;</code>", "여러 언어가 섞인 줄에서 숫자의 표시 방향이 뒤집히는 것을 막습니다"),
    ("입력칸에는 쉼표를 넣지 않기", "<code>type=\"text\"</code>에 <code>inputmode=\"numeric\"</code>을 붙여 받고, <b>보낼 때 숫자로</b> 바꿉니다"),
  ]),
  backend=rows([
    ("돈은 정수로 다루기", "원 단위 금액은 <b>소수점 없는 정수</b>로 다룹니다. 부동소수점으로 계산하면 0.1 + 0.2 같은 간단한 덧셈도 정확히 맞지 않기 때문입니다."),
    ("반올림은 한곳에서 하기", "화면과 서버가 각자 반올림하면 <b>합계가 서로 어긋나므로</b>, 반올림을 어디서 할지 정해 둡니다."),
    ("단위를 함께 보내기", "<code>{\"amount\":1284000,\"currency\":\"KRW\"}</code>처럼 금액과 단위를 함께 보냅니다. 숫자만 오면 화면이 단위를 <b>짐작</b>해야 합니다."),
    ("집계값의 자릿수 정하기", "평균이나 비율은 소수점 <b>몇 자리까지</b> 보낼지 정해 둡니다. 정하지 않으면 화면마다 다른 자릿수로 보입니다."),
    ("큰 정수 ID는 문자열로 보내기", "자바스크립트는 아주 큰 정수를 <b>정확히 다루지 못하므로</b> ID는 문자열로 보냅니다."),
  ]),
  plat_lede="큰 수를 <b>만·억으로 끊는 것</b>은 한국어 화면에서만 따로 챙겨야 하는 일입니다.",
  plats=plats([
    ("웹", "Intl.NumberFormat",
     num('1,284,000원', "", True, "", "110px"),
     "언어와 화폐에 맞는 표기를 함께 처리하지만, <b>만·억으로 줄이는 표기</b>는 직접 손봐야 할 때가 있습니다."),
    ("iOS", "NumberFormatter",
     '''              <div class="phone" role="img" aria-label="iOS 금액 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:7px;text-align:right;font-variant-numeric:tabular-nums">1,284,000원</div></div></div>''',
     "기기의 지역 설정을 따릅니다. 표에서는 <b>등폭 숫자</b>를 켜야 자릿수가 맞습니다."),
    ("안드로이드", "NumberFormat",
     '''              <div class="phone" role="img" aria-label="안드로이드 금액 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:7px;text-align:right;font-variant-numeric:tabular-nums">1,284,000원</div></div></div>''',
     "iOS와 같은 방식으로 지역 설정을 따르고, <b>CompactDecimalFormat</b>이 '128만' 같은 줄임 표기를 만들어 줍니다."),
  ]),
  plat_note="시안에 <b>‘1.2M’</b>이라고 적혀 있다면 영어 템플릿을 그대로 쓴 경우입니다. 한국어 독자는 이 숫자를 머릿속에서 만 단위로 한 번 더 바꿔야 해서 읽는 속도가 느려지고, 금액이 클수록 더 느려집니다. 표기 규칙에 <b>‘만·억으로 적습니다’</b> 한 줄을 정해 두면 이렇게 바꿔 읽는 수고가 없어집니다.",
  siblings=siblings("numbertext"),
  related='''        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="../items/stat.html"><b>스탯</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>''',
)
