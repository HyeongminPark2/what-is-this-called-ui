# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">보이는 값에는 하이픈·공백이 들어감</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">보낼 값에는 숫자만 남김</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">붙여넣은 기호는 알아서 걸러 냄</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">서식을 넣을 때 커서가 맨 뒤로 튀기 쉬움</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">자릿수를 다 채우면 다음 칸으로 넘기기도 함</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">지울 때(Backspace) 기호를 건너뜀</div>
                </div>
              </div>'''

D = dict(
  slug="formatted", ko="자동 서식 입력", en="Formatted input · input mask",
  desc="치는 동안 하이픈이나 공백을 넣어 주는 칸에서 커서가 튀는 문제와 붙여넣은 기호 걸러내기, 보낼 값을 따로 두는 법을 다루는 항목입니다.",
  lede="자동 서식 입력은 사용자가 숫자를 치는 동안 하이픈이나 공백을 넣어 읽기 쉽게 보여 주는 칸입니다. 서식은 화면에 <b>보이는 모양</b>에만 쓰고, 서버로 보낼 때는 <b>숫자만</b> 남겨야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>기호가 섞인 값 붙여넣기</b>'를 눌러 보세요. 걸러내기를 끄면
          <b>서버로 갈 값에 기호가 어떻게 섞이는지</b> 데모가 그대로 보여 줍니다.<br>
          서식은 화면에 보이는 모양에만 쓰고, 보낼 때는 숫자만 남겨야 합니다.
          데모가 칸에 보이는 값과 서버로 갈 값을 나란히 적어 줍니다.<br>
          치는 동안 서식을 넣으면 <b>커서가 엉뚱한 자리로 튀기</b> 쉬워서, 데모가 커서 자리도 함께 적어 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자동 서식 입력, 입력 마스크, 서식 입력"),
    ("영어", "formatted input, input mask, masked input"),
    ("같이 쓰는 말",
     "정해진 꼴에 맞춰 칸을 채우게 하는 것은 <b>입력 마스크</b>(input mask), "
     "치는 동안 서식이 들어가는 것은 <b>라이브 포매팅</b>이라고 부릅니다. "
     "자릿수를 다 채우면 다음 칸으로 넘기는 동작은 <b>오토 탭</b>(auto-tab)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>자리글</b> — <a href=\"placeholder.html\">자리글</a>은 서식을 넣어 주지 않고, 사용자가 치기 시작하면 <b>사라지는 안내</b>입니다.<br>"
     "<b>입력 검증</b> — <a href=\"validation.html\">입력 검증</a>은 값이 <b>맞는지 확인하는</b> 일이고, 자동 서식 입력은 값의 <b>모양을 맞춰 주는</b> 일입니다.<br>"
     "<b>숫자 입력</b> — <a href=\"numberinput.html\">숫자 입력</a>은 하이픈 같은 서식을 넣지 않습니다."),
  ]),
  states=states([
    (fm("123-45-67890", "1234567890", "", "서식이 들어감", True), "다 쳤을 때", "칸에는 서식이 든 <b>보이는 값</b>이, 서버에는 숫자만 든 보낼 값이 갑니다"),
    (fm("123-45-678", "123456780", "", "아직 자릿수가 덜 참", None), "치는 중일 때", "몇 자리를 쳤는지 <b>세어 보여 줍니다</b>"),
    (fm("123-45-67890 (주)", "12345678900", "", "기호가 그대로 들어감", False),
     "붙여넣은 기호를 걸러 내지 않았을 때", "기호가 섞인 값을 보내면 <b>서버가 거절합니다</b>"),
    (fm("1234 5678 9012 3456", "1234567890123456", "", "카드번호는 네 자리씩 끊음", True),
     "번호 종류가 다를 때", "서식은 번호 <b>종류마다</b> 다릅니다"),
    (one(txt('<span style="display:block;font-size:8px">123-45-6|7890</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">커서가 맨 뒤로 튀면 고칠 수 없음</span>'),
         "커서 튐", False, "", "152px"),
     "커서가 맨 뒤로 튀었을 때", "커서가 맨 뒤로 튀어서 <b>가운데 글자를 고칠 수 없습니다</b>"),
    (fm("010-1234-5678", "01012345678", "", "앞의 0이 지워지지 않음", True),
     "맨 앞이 0인 번호", "<b><code>text</code></b> 칸이라서 앞의 0이 사라지지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보이는 값", "서식이 들어간 모양", "하이픈이나 공백을 넣어 읽기 쉽게 보여 줍니다"),
    ("보낼 값", "숫자만 남긴 값", "보내기 전에 <b>화면에서</b> 서식 글자를 지웁니다"),
    ("붙여넣기", "기호 걸러 내기", "붙여넣은 값에 섞인 공백·괄호·점을 걸러 냅니다"),
    ("커서", "튀지 않게 되돌리기", "서식을 넣은 뒤 <b>커서 앞에 있던 숫자 개수</b>를 기준으로 커서를 되돌립니다"),
    ("오토 탭", "다 채우면 다음 칸으로", "자릿수를 다 채우면 다음 칸으로 넘어갑니다"),
    ("Backspace", "기호 건너뛰기", "지울 때 하이픈에서 <b>멈추지 않게</b> 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이 부품에서 가장 흔한 버그는 <b>커서가 튀는 것</b>입니다.
          서식을 넣으려고 칸의 값을 통째로 다시 쓰면 커서가 맨 뒤로 가기 때문에,
          가운데 한 글자를 고치려던 사용자는 <b>글자를 칠 때마다 커서가 끝으로 옮겨집니다</b>.
          고치는 방법은 간단합니다. 서식을 넣기 전에
          <b>커서 앞에 숫자가 몇 개 있었는지</b> 세어 두고,
          새 값에서 숫자를 같은 개수만큼 지난 자리로 커서를 돌려놓으면 됩니다.<br>
          <b>오토 탭</b>은 편해 보이지만 조심해서 써야 합니다.
          자동으로 다음 칸으로 넘어간 뒤 Backspace를 눌러도
          <b>앞 칸으로 돌아가지 못하는</b> 구현이 많기 때문입니다.</p>''',
  do=ul([
    "<b>보이는 값과 보낼 값</b>을 나누기",
    "붙여넣은 값에서 <b>기호를 걸러내기</b>",
    "서식을 넣은 뒤 <b>커서를 원래 자리로 되돌리기</b>",
  ]),
  dont=ul([
    "기호가 섞인 값을 그대로 <b>서버에 보내기</b>",
    "서식을 넣을 때마다 커서를 <b>맨 뒤로</b> 보내기",
    "<code>type=\"number\"</code> 칸에 서식 넣기. 하이픈이 들어가면 <b>값이 사라집니다</b>",
    "자리글로 서식을 흉내 내기. 사용자가 치기 시작하면 <b>안내가 사라집니다</b>",
  ]),
  instead='하이픈 같은 서식 없이 숫자만 받으면 되는 칸에는 <a href="numberinput.html">숫자 입력</a>을 씁니다. 값이 맞는지 확인하는 일은 <a href="validation.html">입력 검증</a>에서, 칸 안팎에 적는 안내 글은 <a href="placeholder.html">자리글과 헬퍼 텍스트</a>에서, 값이 틀렸을 때 보여 줄 문구는 <a href="errortext.html">오류 문구</a>에서 다룹니다.',
  cases=cases([
    (fm("123-45-67890", "1234567890", "", "", True, "150px"), "사업자번호 받기", "<b>세 자리씩</b> 끊어 하이픈을 넣습니다"),
    (fm("010-1234-5678", "01012345678", "", "", True, "150px"), "전화번호 받기", "맨 앞의 0이 <b>사라지지 않아야</b> 합니다"),
    (fm("1234 5678 9012 3456", "1234567890123456", "", "", True, "150px"), "카드번호 받기", "<b>네 자리씩</b> 끊어 공백을 넣습니다"),
  ]),
  code_lede="칸의 값에서 숫자만 뽑아 서식을 다시 입힌 뒤, <b>커서를 원래 자리로 되돌립니다</b>.",
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
    ("<code>inputmode=\"numeric\"</code>", "폰에서 <b>숫자 자판</b>이 뜹니다"),
    ("Backspace", "하이픈에서 <b>멈추지 않도록</b> 한 칸 더 지웁니다"),
    ("붙여넣을 때", "<code>paste</code> 이벤트에서 <b>기호를 걸러</b> 냅니다"),
    ("<code>autocomplete</code>", "<code>tel</code>·<code>cc-number</code>처럼 칸에 들어갈 값의 <b>종류를 적어</b> 둡니다"),
    ("<code>maxlength</code>", "하이픈 같은 서식 글자까지 세기 때문에 <b>넉넉하게</b> 둡니다"),
    ("확인하는 방법", "가운데 한 글자를 고쳐 보고 <b>커서가 튀는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("서버에는 숫자만 보내기", "서버에는 <code>\"123-45-67890\"</code>이 아니라 <code>\"1234567890\"</code>으로 보냅니다."),
    ("서버는 기호가 섞인 값도 걸러서 받기", "화면에서 숫자만 보내더라도, 서버는 <b>기호가 섞인 값이 와도</b> 걸러서 받는 편이 안전합니다."),
    ("번호가 맞는지는 서버에서 검사하기", "사업자번호 체크섬 같은 검사는 <b>서버에서</b> 해야 결과를 믿을 수 있습니다."),
  ]),
  plat_lede="자동 서식 입력은 어느 플랫폼에서든 <b>직접 만드는 경우</b>가 대부분입니다.",
  plats=plats([
    ("웹", "직접 만들어 씀",
     fm("123-45-67890", "1234567890", "", "", True, "110px"),
     "표준 마스크 기능이 없어서 직접 만들어야 하고, 그때마다 <b>커서 처리</b>가 까다롭습니다."),
    ("iOS", "직접 만들어 씀",
     '''              <div class="phone" role="img" aria-label="iOS 서식 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:10px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:29px;font-size:5px;font-family:var(--mono)">123-45-6789</div></div></div>''',
     "iOS에서도 직접 만듭니다. <code>textField(shouldChangeCharactersIn:)</code>에서 들어오는 글자를 받아 서식을 입힙니다."),
    ("안드로이드", "VisualTransformation",
     '''              <div class="phone" role="img" aria-label="안드로이드 서식 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:11px;border-radius:3px;border:1px solid var(--line)"></div>
                <div style="position:absolute;left:8px;top:29px;font-size:5px;font-family:var(--mono)">123-45-6789</div></div></div>''',
     "Compose의 <b>VisualTransformation</b>은 저장되는 값과 화면에 보이는 모양을 <b>처음부터 나눠</b> 다룹니다."),
  ]),
  plat_note="안드로이드 Compose의 <b>VisualTransformation</b>은 이 항목에서 다룬 문제를 플랫폼 API로 풀어 둔 드문 예입니다. <b>값에는 숫자만</b> 두고 <b>화면에는 서식을 입힌 모양</b>을 보여 주며, 커서 자리도 둘 사이에서 맞춰 줍니다. 웹에서 직접 만들 때도 같은 구조를 따라 값과 보이는 모양을 따로 들고 커서 자리를 숫자 개수로 계산하면, 커서가 튀는 버그를 크게 줄일 수 있습니다.",
  siblings=siblings("formatted"),
  related='''        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="placeholder.html"><b>자리글과 헬퍼 텍스트</b><em>14부</em></a></li>''',
)
