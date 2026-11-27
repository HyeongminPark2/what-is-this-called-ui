# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def num(txt, tag, ok=None, note="", w="152px"):
    return one('<span style="font-family:var(--mono);font-size:11px;font-variant-numeric:tabular-nums">' + txt + '</span>',
               tag, ok, note, w)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">표 안 — 1,284,000원. 자릿수를 맞춘다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">요약 타일 — 128만 원. 크게 줄여 읽힌다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">단위를 꼭 붙인다 — 원인가 건인가</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">0건 · 1건 — 그대로 적는다. 복수형이 없다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">소수점은 한 자리까지 — 33.3%</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">1.28M — 한국어는 만 단위로 끊어 읽는다</div>
                </div>
              </div>'''

D = dict(
  slug="numbertext", ko="숫자와 단위 쓰기", en="Writing numbers & units",
  desc="자리에 따라 끊는 법. 만·억 단위, 단위 붙이기, 0건과 1건, 퍼센트 반올림.",
  lede="같은 값도 <b>어디에 적느냐</b>에 따라 다르게 씁니다. 그리고 <b>단위 없는 숫자</b>는 아무것도 알려 주지 않습니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>값과 자리를 바꿔 보세요 — <b>표 안</b>에서는 자릿수를 맞춰 세로로 견주게,
          <b>요약 타일</b>에서는 크게 줄여 읽히게 적습니다.<br>
          한국어는 <b>만·억</b>으로 끊어 읽으므로 ‘1.2M’보다 <b>‘128만 원’</b>이 훨씬 빨리 읽힙니다.
          아래에는 건수·비율에서 자주 틀리는 것을 모아 두었습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자릿수 구분, 천 단위 쉼표, 단위 표기, 반올림"),
    ("영어", "number formatting, thousands separator, abbreviation, rounding"),
    ("같이 쓰는 말",
     "세 자리마다 찍는 쉼표가 <b>천 단위 구분</b>이고, "
     "큰 수를 줄이는 것이 <b>약어 표기</b>(abbreviation)입니다. "
     "브라우저가 말에 맞춰 적어 주는 장치가 <code>Intl.NumberFormat</code>이고, "
     "화폐·퍼센트·단위까지 다룹니다."),
    ("자주 잘못 부름",
     "<b>숫자 꼴</b> — <a href=\"../items/numerals.html\">숫자 꼴</a>은 <b>글자의 생김새</b>(등폭 숫자)입니다. 이쪽은 <b>무엇을 적을지</b>입니다.<br>"
     "<b>포맷팅</b> — 넓은 말이라 날짜·시간까지 섞입니다. <a href=\"datetime.html\">날짜와 시간</a>은 따로입니다.<br>"
     "<b>단위</b> — 길이·무게의 단위계와는 다릅니다. 화면에서는 <b>원·건·%</b>가 대부분입니다."),
  ]),
  axes=ax("숫자와 단위 쓰기"),
  oneline="<b>단위를 꼭 붙이고, 자리에 맞게 끊으세요.</b> 그리고 한국어에서는 K·M 이 아니라 <b>만·억</b>입니다.",
  s4_title="자리별로", s4_hint="같은 값, 다른 적기",
  states=states([
    (num('1,284,000원', "표 안", True, "자릿수를 맞춰 세로로 견준다"), "표", "<a href=\"../items/numerals.html\">등폭 숫자</a>와 함께 쓴다"),
    (num('128만 원', "요약 타일", True, "크게 줄여 한눈에 읽힌다"), "요약", "<a href=\"../items/stat.html\">스탯</a>에서"),
    (num('약 128만 원', "문장 속", True, "읽는 대로 적는다"), "문장", "쉼표 숫자를 문장에 넣으면 <b>안 읽힌다</b>"),
    (num('1,284,000', "단위 없이", False, "원인지 건인지 모른다"), "단위 빠짐", "<b>가장 흔한 실수</b>"),
    (num('1.28M', "영어식 줄임", False, "한국어는 만 단위로 끊어 읽는다"), "K · M", "<b>한 번 더 계산</b>해야 한다"),
    (num('0건', "없을 때", True, "빈칸이나 ‘-’ 로 두지 않는다"), "0", "<a href=\"emptytext.html\">빈 상태 문구</a>와 함께"),
  ]),
  anat=ANAT,
  pins=pins([
    ("표 안", "1,284,000원", "자릿수를 맞춰 <b>세로로 견주게</b>"),
    ("요약 타일", "128만 원", "크게 줄여 <b>한눈에</b>"),
    ("단위", "원 · 건 · %", "<b>반드시 붙인다.</b> 없으면 뜻이 없다"),
    ("건수", "0건 · 1건", "한국어에는 <b>복수형이 없다</b>"),
    ("소수점", "한 자리까지", "33.3%. 더 적으면 <b>틀린 인상</b>을 준다"),
    ("K · M", "쓰지 않는다", "한국어는 <b>만·억</b>으로 끊는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>반올림은 합계를 깨뜨립니다.</b>
          33.33% · 33.33% · 33.33% 를 각각 한 자리로 반올림하면 33.3 × 3 = 99.9 가 되어
          <b>100%가 안 됩니다</b>.
          비율을 여럿 늘어놓는 화면(차트 범례, 구성비 표)에서는
          <b>가장 큰 항목에 나머지를 몰아주거나</b>,
          '합이 100%가 안 될 수 있습니다'를 작게 적어 둡니다.
          <b>작은 값을 0으로 만들지 않는</b> 것도 같은 줄기입니다 —
          0.4%를 0%로 적으면 '없다'는 말이 되어 버립니다.</p>''',
  do=ul([
    "<b>단위를 꼭</b> 붙이기 — 원 · 건 · %",
    "표에서는 자릿수를 맞추고 <b>오른쪽 정렬</b>",
    "요약에서는 <b>만·억</b>으로 줄이기",
  ]),
  dont=ul([
    "단위 없는 숫자 — <b>무엇의 숫자인지 모른다</b>",
    "<b>K · M</b> 쓰기 — 한국어 독자는 한 번 더 계산한다",
    "0 을 ‘-’ 나 빈칸으로 — <b>0건이라고 적는다</b>",
    "작은 값을 0 으로 반올림 — <b>없는 것처럼</b> 보인다",
  ]),
  instead='글자의 생김새는 <a href="../items/numerals.html">숫자 꼴</a>, 요약 한 칸은 <a href="../items/stat.html">스탯</a>, 비율 그림은 <a href="chart.html">차트 고르기</a>.',
  cases=cases([
    (num('9,827,500원<br>1,284,000원<br>&nbsp;&nbsp;&nbsp;11,100원', "표", True, "오른쪽 정렬 + 등폭 숫자"),
     "표 안의 금액", "<b>세로로 견주라고</b> 만든 자리"),
    (num('24.7억', "요약 타일", True, "큰 글자로 줄여 읽힌다"), "요약 타일", "<b>정확한 값은 표에</b> 있다"),
    (num('33.3% · 33.3% · 33.4%', "비율", True, "합이 100이 되게 맞췄다"), "구성비", "<b>반올림이 합을 깨뜨린다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 숫자의 계약서",
  code_lede="<code>Intl.NumberFormat</code>이 말과 화폐를 함께 다룹니다.",
  code='''<span class="c">// 표 안 — 자릿수를 끊고 단위를 붙인다</span>
<span class="k">new</span> Intl.NumberFormat(<span class="s">'ko-KR'</span>, { style: <span class="s">'currency'</span>, currency: <span class="s">'KRW'</span> })
  .format(<span class="a">1284000</span>);          <span class="c">// '₩1,284,000'</span>

<span class="c">// 요약 — 만 · 억으로 줄인다 (Intl 은 한국어 단위를 자동으로 주지 않는다)</span>
<span class="k">function</span> short(n) {
  <span class="k">if</span> (n &gt;= <span class="a">1e8</span>) <span class="k">return</span> (n / <span class="a">1e8</span>).toFixed(<span class="a">1</span>).replace(<span class="s">/\\.0$/</span>, <span class="s">''</span>) + <span class="s">'억'</span>;
  <span class="k">if</span> (n &gt;= <span class="a">1e4</span>) <span class="k">return</span> (n / <span class="a">1e4</span>).toFixed(<span class="a">0</span>) + <span class="s">'만'</span>;
  <span class="k">return</span> n.toLocaleString(<span class="s">'ko-KR'</span>);
}

<span class="c">/* 표에서는 오른쪽 정렬 + 등폭 숫자 */</span>
<span class="t">td</span>.num { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }''',
  keys=kbd([
    ("<code>Intl.NumberFormat</code>", "쉼표·화폐·퍼센트를 말에 맞춰 적어 준다. <b>직접 쉼표를 찍지 않는다</b>"),
    ("<code>notation: 'compact'</code>", "영어는 <code>1.2M</code>, 한국어는 <code>128만</code>. 다만 <b>단위 선택이 아쉬울 때</b>가 있어 직접 쓰기도 한다"),
    ("<code>tabular-nums</code>", "표에서 자릿수를 맞춘다 — <a href=\"../items/numerals.html\">숫자 꼴</a>"),
    ("스크린 리더", "<code>1,284,000</code>은 '백이십팔만 사천'으로 읽힌다. <b>단위가 없으면</b> 무엇인지 모른다"),
    ("<code>&lt;bdi&gt;</code>", "말이 섞인 줄에서 숫자 방향이 뒤집히는 것을 막는다"),
    ("입력칸에는 쉼표를 넣지 않는다", "<code>type=\"text\"</code> + <code>inputmode=\"numeric\"</code>으로 받고 <b>보낼 때 숫자로</b> 바꾼다"),
  ]),
  backend=rows([
    ("돈은 정수로", "원 단위는 <b>소수점 없는 정수</b>로 다룹니다. 부동소수점으로 두면 0.1 + 0.2 가 안 맞습니다."),
    ("반올림을 한곳에서", "화면과 서버가 따로 반올림하면 <b>합계가 어긋납니다</b>. 어디서 할지 정해 둡니다."),
    ("단위를 함께 보낸다", "<code>{\"amount\":1284000,\"currency\":\"KRW\"}</code>. 숫자만 오면 화면이 <b>짐작</b>해야 합니다."),
    ("집계값의 자릿수", "평균·비율은 <b>몇 자리까지</b>인지 정해 보냅니다. 안 정하면 화면마다 다르게 보입니다."),
    ("큰 수", "자바스크립트는 아주 큰 정수를 <b>정확히 못 다룹니다</b>. ID 는 문자열로 보냅니다."),
  ]),
  plat_lede="<b>만·억으로 끊는 것</b>은 한국어 화면에서만 할 일입니다.",
  plats=plats([
    ("웹", "Intl.NumberFormat",
     num('1,284,000원', "", True, "", "110px"),
     "말과 화폐를 함께 다룹니다. <b>만·억 줄임</b>은 손을 좀 봐야 합니다."),
    ("iOS", "NumberFormatter",
     '''              <div class="phone" role="img" aria-label="iOS 금액 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:7px;text-align:right;font-variant-numeric:tabular-nums">1,284,000원</div></div></div>''',
     "지역 설정을 따라갑니다. 표에서는 <b>등폭 숫자</b>를 켜야 자릿수가 맞습니다."),
    ("안드로이드", "NumberFormat",
     '''              <div class="phone" role="img" aria-label="안드로이드 금액 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:7px;text-align:right;font-variant-numeric:tabular-nums">1,284,000원</div></div></div>''',
     "같은 방식입니다. <b>CompactDecimalFormat</b>이 '128만'을 만들어 줍니다."),
  ]),
  plat_note="시안에 <b>‘1.2M’</b>이라고 적혀 있으면 영어 템플릿을 그대로 쓴 것입니다. 한국어 독자는 머릿속에서 한 번 더 바꿔야 해서 읽는 속도가 느려지고, 금액이 클수록 더합니다. <b>‘만·억으로 적습니다’</b>를 한 줄 정해 두면 이 왕복이 사라집니다.",
  siblings=siblings("numbertext"),
  related='''        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="../items/stat.html"><b>스탯</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>''',
)
