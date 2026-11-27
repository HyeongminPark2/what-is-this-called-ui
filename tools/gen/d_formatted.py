# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fm(shown, raw, label="", note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:block;border:1px solid ' + c + ';border-radius:4px;background:var(--surface);'
            'padding:3px 6px;font-size:8.5px;font-family:var(--mono);overflow:hidden;text-overflow:ellipsis;'
            'white-space:nowrap">' + shown + '</span>'
            '<span style="font-size:7.5px;color:var(--fg-muted);font-family:var(--mono)">보낼 값 ' + raw + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">보이는 값 — 하이픈·공백이 들어간 꼴</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">보낼 값 — 숫자만 남긴다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">붙여넣은 기호는 알아서 걸러낸다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">서식을 넣을 때 커서가 맨 뒤로 튀기 쉽다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">자릿수를 다 채우면 다음 칸으로 넘기기도 한다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">지우기(Backspace)에서 기호를 건너뛴다</div>
                </div>
              </div>'''

D = dict(
  slug="formatted", ko="자동 서식 입력", en="Formatted input · input mask",
  desc="치는 동안 하이픈·공백을 넣어 주는 칸. 커서 튐, 붙여넣기 걸러내기, 보낼 값 분리.",
  lede="서식은 <b>보이는 것</b>일 뿐입니다. 보낼 때는 <b>숫자만</b> 남겨야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>기호가 섞인 값 붙여넣기</b>'를 눌러 보세요 — 걸러내기를 끄면
          데모가 <b>서버로 갈 값이 어떻게 지저분한지</b>를 그대로 보여 줍니다.<br>
          서식은 보이는 것일 뿐이고, 보낼 때는 숫자만 남겨야 합니다 —
          데모가 둘을 나란히 적습니다.<br>
          치는 동안 서식을 넣으면 <b>커서가 튀기</b> 쉽습니다. 데모가 커서 자리도 같이 적습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자동 서식 입력, 입력 마스크, 서식 입력"),
    ("영어", "formatted input, input mask, masked input"),
    ("같이 쓰는 말",
     "정해진 꼴로 칸을 채우게 하는 것을 <b>입력 마스크</b>(input mask), "
     "치는 동안 서식이 들어가는 것을 <b>라이브 포매팅</b>이라 합니다. "
     "자릿수를 다 채우면 다음 칸으로 넘기는 동작은 <b>오토 탭</b>(auto-tab)입니다."),
    ("자주 잘못 부름",
     "<b>자리글</b> — <a href=\"placeholder.html\">자리글</a>은 <b>치면 사라지는 안내</b>입니다.<br>"
     "<b>입력 검증</b> — <a href=\"validation.html\">입력 검증</a>은 <b>맞는지 보는</b> 일이고, 이건 <b>꼴을 맞춰 주는</b> 일입니다.<br>"
     "<b>숫자 입력</b> — <a href=\"numberinput.html\">숫자 입력</a>에는 하이픈이 없습니다."),
  ]),
  axes=ax("자동 서식 입력"),
  oneline="<b>보이는 값과 보낼 값을 나누세요.</b> 서식은 화면의 일입니다.",
  states=states([
    (fm("123-45-67890", "1234567890", "", "서식이 들어갔다", True), "기본", "<b>보이는 값</b>과 보낼 값"),
    (fm("123-45-678", "123456780", "", "아직 덜 찼다", None), "치는 중", "자릿수를 <b>세어 준다</b>"),
    (fm("123-45-67890 (주)", "12345678900", "", "기호가 그대로 들어갔다", False),
     "안 걸러냄", "<b>서버가 거절한다</b>"),
    (fm("1234 5678 9012 3456", "1234567890123456", "", "카드는 네 자리씩", True),
     "다른 꼴", "<b>종류마다</b> 다르다"),
    (one(txt('<span style="display:block;font-size:8px">123-45-6|7890</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">커서가 맨 뒤로 튀면 못 고친다</span>'),
         "커서 튐", False, "", "152px"),
     "커서 튐", "<b>가운데를 못 고친다</b>"),
    (fm("010-1234-5678", "01012345678", "", "앞의 0 이 살아 있다", True),
     "앞의 0", "<b><code>text</code></b> 라서 안 사라진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보이는 값", "서식 포함", "읽기 좋게"),
    ("보낼 값", "숫자만", "<b>화면이</b> 벗긴다"),
    ("붙여넣기", "걸러내기", "공백·괄호·점"),
    ("커서", "튀기 쉬움", "<b>친 숫자 개수</b>로 되돌린다"),
    ("오토 탭", "다 채우면", "다음 칸으로"),
    ("Backspace", "기호 건너뛰기", "하이픈에서 <b>멈추지 않게</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>커서가 튀는 것</b>이 이 부품의 가장 흔한 버그입니다 —
          값을 다시 쓰면 커서가 맨 뒤로 가서,
          가운데 한 글자를 고치려던 사람은 <b>매번 끝으로 끌려갑니다</b>.
          고치는 법은 간단합니다 — 서식을 넣기 전에
          <b>커서 앞의 숫자가 몇 개였는지</b>를 세어 두고,
          새 값에서 같은 개수만큼 지난 자리로 커서를 돌려놓으면 됩니다.<br>
          <b>오토 탭</b>은 편해 보이지만 조심해야 합니다 —
          자동으로 넘어간 뒤 Backspace 를 누르면
          <b>앞 칸으로 못 돌아가는</b> 구현이 많습니다.</p>''',
  do=ul([
    "<b>보이는 값과 보낼 값</b>을 나누기",
    "붙여넣은 <b>기호를 걸러내기</b>",
    "서식을 넣은 뒤 <b>커서를 되돌리기</b>",
  ]),
  dont=ul([
    "기호가 섞인 채로 <b>서버에 보내기</b>",
    "커서를 <b>맨 뒤로</b> 보내기",
    "<code>type=\"number\"</code> 에 서식 넣기 — <b>값이 사라진다</b>",
    "자리글로 서식을 흉내 내기 — <b>치면 사라진다</b>",
  ]),
  instead='서식 없는 숫자는 <a href="numberinput.html">숫자 입력</a>, 맞는지 보는 일은 <a href="validation.html">입력 검증</a>, 안내 글은 <a href="placeholder.html">자리글과 헬퍼 텍스트</a>, 오류 문구는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (fm("123-45-67890", "1234567890", "", "", True, "150px"), "사업자번호", "<b>세 자리씩</b>"),
    (fm("010-1234-5678", "01012345678", "", "", True, "150px"), "전화번호", "앞의 0 이 <b>살아야</b> 한다"),
    (fm("1234 5678 9012 3456", "1234567890123456", "", "", True, "150px"), "카드번호", "<b>네 자리씩</b>"),
  ]),
  code_lede="숫자만 뽑아 다시 꼴을 만들고, <b>커서를 되돌립니다</b>.",
  code='''<span class="t">const</span> digits = s =&gt; s.replace(/[^\\d]/g, <span class="s">''</span>);
<span class="t">const</span> fmt = raw =&gt; [raw.slice(<span class="a">0</span>, <span class="a">3</span>), raw.slice(<span class="a">3</span>, <span class="a">5</span>), raw.slice(<span class="a">5</span>, <span class="a">10</span>)]
  .filter(Boolean).join(<span class="s">'-'</span>);

input.addEventListener(<span class="s">'input'</span>, () =&gt; {
  <span class="c">// 커서 앞의 숫자가 몇 개였는지 세어 둔다</span>
  <span class="t">const</span> before = digits(input.value.slice(<span class="a">0</span>, input.selectionStart)).length;
  input.value = fmt(digits(input.value).slice(<span class="a">0</span>, <span class="a">10</span>));
  <span class="c">// 같은 개수만큼 지난 자리로 커서를 되돌린다</span>
  <span class="t">let</span> pos = <span class="a">0</span>, seen = <span class="a">0</span>;
  <span class="t">while</span> (pos &lt; input.value.length &amp;&amp; seen &lt; before) {
    <span class="t">if</span> (/\\d/.test(input.value[pos])) seen++;
    pos++;
  }
  input.setSelectionRange(pos, pos);
});''',
  keys=kbd([
    ("<code>inputmode=\"numeric\"</code>", "폰에서 <b>숫자 자판</b>이 뜬다"),
    ("Backspace", "하이픈에서 <b>멈추지 않게</b> 한 칸 더 지운다"),
    ("붙여넣기", "<code>paste</code> 에서 <b>기호를 걸러</b> 낸다"),
    ("<code>autocomplete</code>", "<code>tel</code>·<code>cc-number</code> 처럼 <b>뜻을 적어</b> 둔다"),
    ("<code>maxlength</code>", "서식 글자까지 세니 <b>넉넉하게</b> 둔다"),
    ("확인하는 법", "가운데 한 글자를 고쳐 보고 <b>커서가 튀는지</b> 본다"),
  ]),
  backend=rows([
    ("숫자만 받는다", "<code>\"123-45-67890\"</code> 이 아니라 <code>\"1234567890\"</code> 으로 보냅니다."),
    ("관대하게 받기", "그래도 서버는 <b>기호가 섞여 와도</b> 걸러서 받는 편이 안전합니다."),
    ("검증은 서버에서", "사업자번호 체크섬 같은 것은 <b>서버가</b> 봐야 믿을 수 있습니다."),
  ]),
  plat_lede="<b>직접 만드는 쪽</b>이 대부분입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     fm("123-45-67890", "1234567890", "", "", True, "110px"),
     "표준 마스크가 없어 직접 만듭니다 — <b>커서 처리</b>가 늘 어렵습니다."),
    ("iOS", "직접 만듦",
     '''              <div class="phone" role="img" aria-label="iOS 서식 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:29px;font-size:5px;font-family:var(--mono)">123-45-6789</div></div></div>''',
     "역시 직접 만듭니다. <code>textField(shouldChangeCharactersIn:)</code> 에서 다듬습니다."),
    ("안드로이드", "VisualTransformation",
     '''              <div class="phone" role="img" aria-label="안드로이드 서식 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:11px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:29px;font-size:5px;font-family:var(--mono)">123-45-6789</div></div></div>''',
     "Compose 의 <b>VisualTransformation</b> 이 값과 보이는 꼴을 <b>아예 나눕니다</b>."),
  ]),
  plat_note="안드로이드 Compose 의 <b>VisualTransformation</b> 은 이 항목의 핵심을 언어 차원에서 푼 드문 예입니다 — <b>값은 숫자만</b>, <b>보이는 것은 서식</b>으로 나누고 커서 자리까지 맞춰 줍니다. 웹에서 직접 만들 때도 이 구조를 흉내 내면 — 값과 보이는 꼴을 따로 들고, 커서는 숫자 개수로 계산 — 버그가 확 줄어듭니다.",
  siblings=siblings("formatted"),
  related='''        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="placeholder.html"><b>자리글과 헬퍼 텍스트</b><em>14부</em></a></li>''',
)
