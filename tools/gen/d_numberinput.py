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
  desc="숫자를 받는 칸에서 type=number가 일으키는 문제와 inputmode, 쉼표와 단위를 두는 자리를 다루는 항목입니다.",
  lede="<code>type=\"number\"</code>는 숫자 칸을 쉽게 만들어 주는 것처럼 보이지만 <b>문제가 많습니다</b>. 마우스 휠을 굴리면 값이 바뀌고, 쉼표가 들어가면 값 전체가 사라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모가 지금 칸에서 <b>읽히는 값</b>을 그대로 적어 줍니다.
          <code>type="number"</code> 칸에 쉼표를 넣으면 값이 <b>빈 문자열</b>로 바뀌는 것을 볼 수 있습니다.<br>
          그래서 돈이나 전화번호처럼 <b>세어서 쓰지 않는 숫자</b>는
          <code>text</code> 칸에 <code>inputmode="numeric"</code>을 다는 편이 안전합니다.
          이렇게 해도 폰에서는 똑같이 숫자 자판이 뜹니다.<br>
          <b>단위</b>는 칸 밖에 두어야 칸에 숫자 값만 남습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "숫자 입력, 숫자 칸"),
    ("영어", "number input, numeric input"),
    ("같이 쓰는 말",
     "브라우저가 칸 옆에 띄우는 작은 화살표는 <b>스피너</b>, 폰 자판을 숫자 자판으로 바꾸는 속성은 "
     "<code>inputmode</code>입니다. 세 자리마다 쉼표를 넣는 것은 <b>천 단위 구분</b>, "
     "숫자마다 폭을 같게 맞추는 글꼴 설정은 <b>tabular-nums</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>수량 스테퍼</b> — 칸 양옆에 <b>− · ＋</b> 단추가 붙어 있으면 <a href=\"quantity.html\">수량 스테퍼</a>입니다.<br>"
     "<b>자동 서식 입력</b> — 치는 동안 <b>하이픈을 넣어 주는</b> 칸은 <a href=\"formatted.html\">자동 서식 입력</a>입니다.<br>"
     "<b>슬라이더</b> — <a href=\"slider.html\">슬라이더</a>는 숫자를 치지 않고 손잡이를 끌어 <b>범위 안에서</b> 고릅니다."),
  ]),
  axes=ax("숫자 입력"),
  oneline="<b>세어서 쓰지 않는 숫자는 <code>text</code> 칸으로 받으세요.</b> 돈, 전화번호, 카드번호가 여기에 해당합니다.",
  states=states([
    (ni("1,284,000", "원", "", "쉼표가 보이고 값은 깨끗하다", True), "<code>text</code> + inputmode", "쉼표를 보여 주면서 값도 지킬 수 있는 <b>안전한 기본</b>입니다"),
    (ni("1284000", "원", "", "스피너가 붙는다", None, "152px", False, True), "<code>type=number</code>", "스피너 화살표가 붙는데 <b>너무 작아서</b> 누르기 어렵습니다"),
    (ni("(빈 값)", "원", "", "쉼표를 넣으면 값이 사라진다", False, "152px", False, True), "쉼표를 넣으면", "값이 <b>빈 문자열</b>이 됩니다"),
    (ni("1,284,000 원", "", "", "값과 단위가 섞였다", False, "152px", True), "단위가 칸 안에", "값에 단위 글자가 섞여서 <b>숫자만 뽑기 번거롭습니다</b>"),
    (ni("1,284,000", "원", "", "오른쪽 맞춤 · 자릿수 고정", True), "맞춤", "값이 바뀌어도 <b>자릿수 위치가 흔들리지 않습니다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">굴리다 값이 바뀌었다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">type=number 의 기본 동작</span>'),
         "휠", False, "", "152px"),
     "휠", "칸 위에서 <b>스크롤하다가</b> 값이 바뀝니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>text</code> + inputmode", "안전한 기본", "<code>number</code>와 <b>똑같이</b> 폰에서 숫자 자판이 뜹니다"),
    ("<code>type=number</code>", "휠 사고", "칸 위에서 스크롤하다가 값이 바뀝니다"),
    ("쉼표", "값이 사라짐", "<code>number</code> 칸에 쉼표를 넣으면 값이 <b>빈 문자열</b>이 됩니다"),
    ("단위", "칸 밖에", "단위를 칸 밖에 두어야 칸에 <b>숫자 값만</b> 남습니다"),
    ("맞춤", "오른쪽 · tabular", "오른쪽으로 맞추고 숫자 폭을 고정해 자릿수가 <b>흔들리지 않게</b> 합니다"),
    ("세어 쓰는 숫자", "<code>number</code> 도 괜찮다", "수량이나 나이처럼 세어서 쓰는 수에는 <code>number</code>를 써도 됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          수량이나 나이처럼 <b>세어서 쓰는 작은 수</b>에는 <code>type="number"</code>의 화살표와 범위 검사가 편리합니다.
          문제가 생기는 것은 <b>돈·전화번호·카드번호</b>처럼 숫자로 이루어져 있지만 계산하지는 않는 값에 쓸 때입니다.
          이런 값에는 쉼표나 하이픈이 들어가고, 맨 앞의 0도 값의 일부이며, 자릿수가 깁니다.
          세 가지 모두 <code>number</code> 칸이 제대로 다루지 못하는 것들입니다.<br>
          어느 쪽을 쓸지는 <b>이 값을 더하거나 뺄 일이 있는지</b> 물어보면 정할 수 있습니다.
          계산할 일이 없으면 <code>text</code> 칸을 씁니다.</p>''',
  do=ul([
    "세어서 쓰지 않는 숫자를 <b><code>text</code> + <code>inputmode=\"numeric\"</code></b>으로 받기",
    "단위를 <b>칸 밖에</b> 두기",
    "<b>오른쪽 맞춤 + <code>tabular-nums</code></b>로 자릿수 맞추기",
  ]),
  dont=ul([
    "금액에 <code>type=\"number\"</code> 쓰기. <b>쉼표를 넣으면 값이 지워집니다</b>",
    "전화번호에 <code>type=\"number\"</code> 쓰기. 숫자로 읽히면서 <b>앞의 0</b>이 사라집니다",
    "단위를 <b>칸 안에</b> 넣기",
    "휠로 값이 바뀌게 두기. 화면을 스크롤하다가 값이 <b>바뀌어 버립니다</b>",
  ]),
  instead='− ＋ 단추가 붙으면 <a href="quantity.html">수량 스테퍼</a>, 하이픈이 들어가면 <a href="formatted.html">자동 서식 입력</a>, 범위 안에서 고르면 <a href="slider.html">슬라이더</a>, 숫자를 화면에 적는 형식은 <a href="numbertext.html">숫자와 단위 쓰기</a>.',
  cases=cases([
    (ni("1,284,000", "원", "", "", True, "150px"), "금액", "쉼표가 들어가므로 <b><code>text</code></b> 칸이 맞습니다"),
    (ni("3", "개", "", "", True, "150px", False, True), "수량", "세어서 쓰는 작은 수라서 <code>number</code>를 써도 괜찮습니다"),
    (ni("010-1234-5678", "", "", "", True, "150px"), "전화번호", "숫자로 이루어져 있지만 계산하는 <b>수가 아닙니다</b>"),
  ]),
  code_lede="세어서 쓰지 않는 숫자는 <code>text</code> 칸으로 받고, 값을 읽을 때 숫자만 뽑아 씁니다.",
  code='''<span class="c">&lt;!-- 돈 · 전화번호 · 카드번호처럼 계산하지 않는 숫자 --&gt;</span>
&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"amount"</span>&gt;정산 금액&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"amount"</span> <span class="a">type</span>=<span class="s">"text"</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span>
       <span class="a">autocomplete</span>=<span class="s">"off"</span> <span class="a">value</span>=<span class="s">"1,284,000"</span>&gt;
&lt;<span class="t">span</span>&gt;원&lt;/<span class="t">span</span>&gt;          <span class="c">&lt;!-- 단위는 칸 밖에 --&gt;</span>

<span class="c">// 보낼 때는 숫자만 남긴다</span>
<span class="t">const</span> raw = input.value.replace(/[^\\d]/g, <span class="s">''</span>);

input { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">/* type=number를 쓴다면 휠만은 막는다 */</span>
el.addEventListener(<span class="s">'wheel'</span>, e =&gt; el === document.activeElement &amp;&amp; e.preventDefault());''',
  keys=kbd([
    ("<code>inputmode=\"numeric\"</code>", "<code>type</code>과 상관없이 폰에서 <b>숫자 자판</b>이 뜹니다"),
    ("<code>inputmode=\"decimal\"</code>", "소수점을 넣어야 하면 이 값을 씁니다"),
    ("↑ ↓", "<code>type=number</code> 칸에서만 값이 바뀝니다"),
    ("<code>pattern</code>", "<code>text</code> 칸에서도 <b>형식 검사</b>를 걸 수 있습니다"),
    ("<code>autocomplete=\"off\"</code>", "금액 칸에 전에 넣었던 <b>옛 값</b>이 뜨지 않게 합니다"),
    ("확인하는 법", "칸에 커서를 두고 <b>휠을 굴려</b> 값이 바뀌는지 봅니다"),
  ]),
  backend=rows([
    ("숫자만 받는다", "서버에는 <code>\"1,284,000\"</code>이 아니라 <code>1284000</code>으로 보냅니다. 쉼표 같은 서식은 화면에서 붙입니다."),
    ("돈은 정수로", "금액을 소수점 실수로 다루면 <b>반올림 오차</b>가 생기기 때문에, 원 단위 정수나 문자열로 다루는 편이 안전합니다."),
    ("범위", "서버가 <code>min</code>·<code>max</code>를 내려 주면 화면에서 범위 밖의 값을 <b>미리 막을 수</b> 있습니다."),
  ]),
  plat_lede="<b>숫자 자판</b>을 띄우는 방법은 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "inputmode",
     ni("1,284,000", "원", "", "", True, "110px"),
     "<code>type</code>과 <code>inputmode</code>가 <b>따로</b> 있어서 둘을 골라 조합할 수 있습니다."),
    ("iOS", "keyboardType",
     '''              <div class="phone" role="img" aria-label="iOS 숫자 자판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;right:3px;bottom:3px;height:20px;border-radius:3px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "<code>.numberPad</code>나 <code>.decimalPad</code>를 <b>칸마다</b> 골라 지정합니다."),
    ("안드로이드", "inputType",
     '''              <div class="phone" role="img" aria-label="안드로이드 숫자 자판 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;right:3px;bottom:3px;height:20px;border-radius:3px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "<code>numberDecimal</code> 같은 값으로 자판 종류를 정하며, 이 역시 <b>칸마다</b> 지정합니다."),
  ]),
  plat_note="앱에서는 처음부터 <b>자판 종류</b>와 <b>값의 타입</b>을 따로 정하기 때문에, 숫자 자판을 띄워도 값은 문자열로 받습니다. 웹에 <code>inputmode</code>가 생긴 것도 같은 생각에서 나왔고, 그 덕분에 <b>type=text 칸에 숫자 자판</b>을 띄우는 조합을 쓸 수 있게 되었습니다. 돈이나 전화번호를 받을 때는 이 조합이 가장 잘 맞습니다.",
  siblings=siblings("numberinput"),
  related='''        <li><a href="quantity.html"><b>수량 스테퍼</b><em>4부</em></a></li>
        <li><a href="formatted.html"><b>자동 서식 입력</b><em>4부</em></a></li>
        <li><a href="numbertext.html"><b>숫자와 단위 쓰기</b><em>14부</em></a></li>
        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>''',
)
