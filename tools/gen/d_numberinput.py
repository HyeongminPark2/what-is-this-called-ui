# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ni(val, unit="원", label="", note="", ok=None, w="152px", inside=False, spin=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:flex;gap:5px;align-items:center">'
            '<span style="flex:1;min-width:0;display:flex;align-items:center;border:1px solid ' + c + ';'
            'border-radius:4px;background:var(--surface);padding:3px 6px">'
            '<span style="flex:1;text-align:right;font-size:8.5px;font-family:var(--mono)">' + val
            + ('<span style="color:var(--fg-muted)"> ' + unit + '</span>' if inside and unit else '') + '</span>'
            + ('<span style="display:grid;font-size:5px;color:var(--fg-muted);line-height:1">▲<br>▼</span>' if spin else '')
            + '</span>'
            + ('<span style="font-size:8px;color:var(--fg-muted)">' + unit + '</span>' if unit and not inside else '')
            + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">text + inputmode="numeric" — 안전한 기본</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">type="number" — 휠로 값이 바뀐다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">쉼표를 넣으면 값이 빈 문자열이 된다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단위는 칸 밖에 — 값만 깨끗하게</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">숫자는 오른쪽 맞춤 · tabular-nums</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">세어서 쓰지 않는 숫자는 text 로</div>
                </div>
              </div>'''

D = dict(
  slug="numberinput", ko="숫자 입력", en="Number input",
  desc="숫자를 받는 칸. type=number의 함정, inputmode, 쉼표와 단위를 두는 자리.",
  lede="<code>type=\"number\"</code> 는 쉬워 보이지만 <b>함정이 많습니다</b> — 휠로 값이 바뀌고 쉼표를 삼킵니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모가 지금 칸의 <b>읽히는 값</b>을 그대로 적습니다 —
          <code>type="number"</code> 에 쉼표를 넣으면 <b>빈 문자열</b>이 됩니다.<br>
          그래서 돈·전화번호처럼 <b>세어서 쓰지 않는 숫자</b>는
          <code>text</code> 에 <code>inputmode="numeric"</code> 을 두는 편이 안전합니다 —
          폰에서 숫자 자판이 뜨는 것은 똑같습니다.<br>
          <b>단위</b>는 칸 밖에 두어야 값만 깨끗하게 남습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "숫자 입력, 숫자 칸"),
    ("영어", "number input, numeric input"),
    ("같이 쓰는 말",
     "브라우저가 띄우는 작은 화살표는 <b>스피너</b>, 폰 자판을 숫자로 바꾸는 것은 "
     "<code>inputmode</code> 입니다. 세 자리마다 쉼표를 넣는 것은 <b>천 단위 구분</b>, "
     "자릿수를 고르게 맞추는 글꼴 설정은 <b>tabular-nums</b> 입니다."),
    ("자주 잘못 부름",
     "<b>수량 스테퍼</b> — <a href=\"quantity.html\">수량 스테퍼</a>는 <b>− · ＋</b>가 붙은 쪽입니다.<br>"
     "<b>자동 서식 입력</b> — <a href=\"formatted.html\">자동 서식 입력</a>은 <b>하이픈을 넣어 주는</b> 쪽입니다.<br>"
     "<b>슬라이더</b> — <a href=\"slider.html\">슬라이더</a>는 <b>범위에서</b> 고릅니다."),
  ]),
  axes=ax("숫자 입력"),
  oneline="<b>세어서 쓰지 않는 숫자는 <code>text</code> 로.</b> 돈·전화번호·카드번호가 그렇습니다.",
  states=states([
    (ni("1,284,000", "원", "", "쉼표가 보이고 값은 깨끗하다", True), "<code>text</code> + inputmode", "<b>안전한 기본</b>"),
    (ni("1284000", "원", "", "스피너가 붙는다", None, "152px", False, True), "<code>type=number</code>", "화살표가 <b>너무 작다</b>"),
    (ni("(빈 값)", "원", "", "쉼표를 넣으면 값이 사라진다", False, "152px", False, True), "쉼표를 넣으면", "<b>빈 문자열</b>이 된다"),
    (ni("1,284,000 원", "", "", "값과 단위가 섞였다", False, "152px", True), "단위가 칸 안에", "<b>값이 지저분해진다</b>"),
    (ni("1,284,000", "원", "", "오른쪽 맞춤 · 자릿수 고정", True), "맞춤", "<b>자릿수가 안 흔들린다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">굴리다 값이 바뀌었다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">type=number 의 기본 동작</span>'),
         "휠", False, "", "152px"),
     "휠", "<b>스크롤하다</b> 틀어진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>text</code> + inputmode", "안전한 기본", "폰 자판은 <b>똑같이</b> 뜬다"),
    ("<code>type=number</code>", "휠 사고", "스크롤하다 값이 바뀐다"),
    ("쉼표", "값이 사라짐", "<code>number</code> 에서는 <b>빈 문자열</b>"),
    ("단위", "칸 밖에", "값만 <b>깨끗하게</b>"),
    ("맞춤", "오른쪽 · tabular", "자릿수가 <b>안 흔들린다</b>"),
    ("세어 쓰는 숫자", "<code>number</code> 도 괜찮다", "수량 · 나이"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>type="number"</code> 가 <b>아주 쓸모없는 것은 아닙니다</b> —
          수량이나 나이처럼 <b>세어서 쓰는 작은 수</b>에는 화살표와 범위 검사가 편합니다.
          문제는 <b>돈·전화번호·카드번호</b>처럼 '숫자로 생겼지만 계산하지 않는 값'에 쓸 때입니다.
          그런 값에는 쉼표·하이픈이 들어가고, 앞의 0 이 뜻을 가지며, 자릿수가 깁니다 —
          전부 <code>number</code> 가 잘 못 다루는 것들입니다.<br>
          가르는 질문은 하나입니다 — <b>이 값을 더하거나 뺄 일이 있나</b>.
          없으면 <code>text</code> 입니다.</p>''',
  do=ul([
    "세어 쓰지 않는 숫자는 <b><code>text</code> + <code>inputmode=\"numeric\"</code></b>",
    "단위는 <b>칸 밖에</b> 두기",
    "<b>오른쪽 맞춤 + <code>tabular-nums</code></b> 로 자릿수 맞추기",
  ]),
  dont=ul([
    "돈에 <code>type=\"number\"</code> 쓰기 — <b>쉼표가 값을 지운다</b>",
    "전화번호에 <code>type=\"number\"</code> 쓰기 — <b>앞의 0</b>이 사라진다",
    "단위를 <b>칸 안에</b> 넣기",
    "휠로 값이 바뀌게 두기 — 굴리다 <b>틀어진다</b>",
  ]),
  instead='− ＋ 가 붙으면 <a href="quantity.html">수량 스테퍼</a>, 하이픈이 들어가면 <a href="formatted.html">자동 서식 입력</a>, 범위면 <a href="slider.html">슬라이더</a>, 적는 꼴은 <a href="numbertext.html">숫자와 단위 쓰기</a>.',
  cases=cases([
    (ni("1,284,000", "원", "", "", True, "150px"), "금액", "<b><code>text</code></b> 가 맞다"),
    (ni("3", "개", "", "", True, "150px", False, True), "수량", "<code>number</code> 도 괜찮다"),
    (ni("010-1234-5678", "", "", "", True, "150px"), "전화번호", "<b>숫자가 아니다</b>"),
  ]),
  code_lede="세어 쓰지 않는 숫자는 <code>text</code> 로 두고, 읽을 때 숫자만 뽑습니다.",
  code='''<span class="c">&lt;!-- 돈 · 전화번호 · 카드번호 — 계산하지 않는 숫자 --&gt;</span>
&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"amount"</span>&gt;정산 금액&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"amount"</span> <span class="a">type</span>=<span class="s">"text"</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span>
       <span class="a">autocomplete</span>=<span class="s">"off"</span> <span class="a">value</span>=<span class="s">"1,284,000"</span>&gt;
&lt;<span class="t">span</span>&gt;원&lt;/<span class="t">span</span>&gt;          <span class="c">&lt;!-- 단위는 칸 밖에 --&gt;</span>

<span class="c">// 보낼 때는 숫자만 남긴다</span>
<span class="t">const</span> raw = input.value.replace(/[^\\d]/g, <span class="s">''</span>);

input { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">/* type=number 를 쓴다면 휠만은 막는다 */</span>
el.addEventListener(<span class="s">'wheel'</span>, e =&gt; el === document.activeElement &amp;&amp; e.preventDefault());''',
  keys=kbd([
    ("<code>inputmode=\"numeric\"</code>", "폰에서 <b>숫자 자판</b>이 뜬다 — <code>type</code> 과 무관하다"),
    ("<code>inputmode=\"decimal\"</code>", "소수점이 필요하면 이쪽"),
    ("↑ ↓", "<code>type=number</code> 에서만 값이 바뀐다"),
    ("<code>pattern</code>", "<code>text</code> 에서도 <b>모양 검사</b>를 걸 수 있다"),
    ("<code>autocomplete=\"off\"</code>", "금액 칸에 <b>옛 값</b>이 뜨지 않게"),
    ("확인하는 법", "칸에 커서를 두고 <b>휠을 굴려</b> 본다"),
  ]),
  backend=rows([
    ("숫자만 받는다", "<code>\"1,284,000\"</code> 이 아니라 <code>1284000</code> 으로 보냅니다 — 서식은 화면의 일입니다."),
    ("돈은 정수로", "소수점 실수로 다루면 <b>반올림 오차</b>가 생깁니다 — 원 단위 정수나 문자열이 안전합니다."),
    ("범위", "<code>min</code>·<code>max</code> 를 서버가 주면 화면이 <b>미리 막을 수</b> 있습니다."),
  ]),
  plat_lede="<b>숫자 자판</b>을 띄우는 방법이 다릅니다.",
  plats=plats([
    ("웹", "inputmode",
     ni("1,284,000", "원", "", "", True, "110px"),
     "<code>type</code> 과 <code>inputmode</code> 가 <b>따로</b>라 골라 쓸 수 있습니다."),
    ("iOS", "keyboardType",
     '''              <div class="phone" role="img" aria-label="iOS 숫자 자판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;right:3px;bottom:3px;height:20px;border-radius:3px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "<code>.numberPad</code> · <code>.decimalPad</code> 를 <b>칸마다</b> 고릅니다."),
    ("안드로이드", "inputType",
     '''              <div class="phone" role="img" aria-label="안드로이드 숫자 자판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;right:3px;bottom:3px;height:20px;border-radius:3px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "<code>numberDecimal</code> 같은 값으로 정합니다 — 역시 <b>칸마다</b>."),
  ]),
  plat_note="앱 쪽은 <b>자판 종류</b>와 <b>값의 타입</b>이 처음부터 따로입니다 — 숫자 자판을 띄워도 값은 문자열로 받습니다. 웹의 <code>inputmode</code> 가 생긴 것도 같은 생각이고, 덕분에 <b>type=text 에 숫자 자판</b>이라는 조합이 가능해졌습니다. 이 조합이 돈·전화번호에 가장 잘 맞습니다.",
  siblings=siblings("numberinput"),
  related='''        <li><a href="quantity.html"><b>수량 스테퍼</b><em>4부</em></a></li>
        <li><a href="formatted.html"><b>자동 서식 입력</b><em>4부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>''',
)
