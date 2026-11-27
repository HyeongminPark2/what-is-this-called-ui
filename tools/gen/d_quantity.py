# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def q(v, label, note="", ok=None, w="152px", minus=True, plus=True, size=22, ro=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    def b(t, on):
        return ('<span style="display:grid;place-items:center;width:' + str(size) + 'px;height:' + str(size) +
                'px;font-size:9px;color:' + ('var(--fg)' if on else 'var(--fg-faint)') + '">' + t + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:start">'
            '<span style="display:inline-flex;align-items:stretch;border:1px solid ' + c + ';border-radius:4px;'
            'overflow:hidden;background:var(--surface)">' + b('−', minus)
            + '<span style="display:grid;place-items:center;width:34px;border-left:1px solid var(--line);'
              'border-right:1px solid var(--line);font-size:8.5px;font-family:var(--mono);'
            + ('background:var(--bg);color:var(--fg-muted);' if ro else '') + '">' + v + '</span>'
            + b('＋', plus) + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">− · ＋는 한두 번 고칠 때 빠름</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">가운데 칸에는 쳐서도 넣을 수 있어야 함</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">1에서 −, 최대에서 ＋는 꺼 둠</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단추는 손가락에 맞게 44px 이상</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">값이 바뀌면 소리로도 알림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">0으로 내리면 빼는지 미리 정해 둠</div>
                </div>
              </div>'''

D = dict(
  slug="quantity", ko="수량 스테퍼", en="Quantity stepper · number stepper",
  desc="−와 ＋ 단추로 수를 고치는 수량 스테퍼에서 쳐서 넣기, 끝값 처리, 터치 타깃을 다루는 항목입니다.",
  lede="수량 스테퍼는 −와 ＋ 단추로 수를 하나씩 고치는 부품이라서 <b>한두 번 고칠 때</b>만 빠릅니다. 1에서 24까지 올리려면 ＋를 스물세 번 눌러야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>목표까지 ＋만 눌러 보기</b>'를 눌러 보세요. 데모가 <b>몇 번 눌러야 하는지</b>를 세어 적어 주는데,
          같은 수를 가운데 칸에 쳐서 넣으면 <b>한 번</b>에 끝납니다.<br>
          그래서 가운데 칸은 <b>읽기 전용으로 두지 않습니다</b>. 체크를 끄면 칸이 잠겨서 큰 수를 넣을 방법이 없어집니다.<br>
          단추는 <b>44px</b>은 되어야 손가락으로 정확히 누를 수 있습니다. 또 <b>1에서 −</b>, <b>최대에서 ＋</b>는 꺼 두어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "수량 스테퍼, 수량 조절기, 숫자 스테퍼"),
    ("영어", "quantity stepper, number stepper, spinner"),
    ("같이 쓰는 말",
     "iOS에서는 <b>Stepper</b>, 안드로이드와 웹에서는 <b>수량 선택기</b>라고 부르기도 합니다. "
     "<code>&lt;input type=\"number\"&gt;</code>에 브라우저가 붙여 주는 작은 화살표는 <b>스피너</b>라고 합니다. "
     "7부의 <a href=\"stepper.html\">스테퍼</a>와는 <b>이름만 같고 전혀 다른 부품</b>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>스테퍼(단계)</b> — <a href=\"stepper.html\">7부의 스테퍼</a>는 수를 고치는 부품이 아니라 <b>흐름의 단계</b>를 보여 주는 부품입니다.<br>"
     "<b>슬라이더</b> — <a href=\"slider.html\">슬라이더</a>는 손잡이를 끌어 <b>범위 안에서</b> 값을 고릅니다.<br>"
     "<b>숫자 입력</b> — <a href=\"numberinput.html\">숫자 입력</a>은 −·＋ 단추 없이 <b>칸만</b> 있는 부품입니다."),
  ]),
  states=states([
    (q("1", "", "1에서는 −가 꺼짐", True, "152px", False, True), "최소값에 닿았을 때", "더 줄일 수 없으므로 <b>−가 꺼집니다</b>"),
    (q("3", "", "두 단추가 모두 눌림", True), "평소 상태", "두 단추가 모두 눌리고, 가운데 칸에도 <b>쳐서 넣을 수 있습니다</b>"),
    (q("99", "", "최대에서는 ＋가 꺼짐", True, "152px", True, False), "최대값에 닿았을 때", "더 늘릴 수 없으므로 <b>＋가 꺼집니다</b>"),
    (q("24", "", "가운데 칸이 잠김", False, "152px", True, True, 22, True), "가운데 칸을 잠갔을 때", "단추로만 고쳐야 해서 <b>큰 수를 넣기 어렵습니다</b>"),
    (q("3", "", "단추가 24px라 누르기 어려움", False, "152px", True, True, 13), "단추가 너무 작을 때", "<b>44px에 못 미쳐서</b> 손가락으로 누르기 어렵습니다"),
    (q("0", "", "0이면 빼는 것인지 정해 둠", None, "152px", False, True), "0으로 내렸을 때", "0이 빼기를 뜻하는지 <b>미리 정해</b> 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("− · ＋", "한두 번 고칠 때", "한두 번 고칠 때 씁니다. 그보다 많이 바꿀 때는 <b>쳐서 넣는 편이</b> 빠릅니다"),
    ("가운데 칸", "쳐서 넣는 자리", "큰 수를 넣을 수 있도록 <b>잠그지 않습니다</b>"),
    ("끝값", "단추 끄기", "1에서는 −를, 최대에서는 ＋를 끕니다"),
    ("크기", "44px 이상", "손가락으로 정확히 누를 수 있도록 44px 이상으로 둡니다"),
    ("소리", "바뀐 값 알리기", "<code>aria-live</code>나 <code>role=\"status\"</code>로 바뀐 값을 읽어 줍니다"),
    ("0", "빼기인지 정하기", "0으로 내렸을 때 어떻게 할지 <b>미리 정합니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>0으로 내렸을 때</b> 어떻게 할지 정해 두지 않으면 사용자가 원하지 않은 결과가 생깁니다.
          장바구니에서는 수량 0이 대개 상품을 '빼기'라는 뜻인데,
          아무 안내 없이 상품이 사라지면 사용자는 자기가 무엇을 했는지 알 수 없습니다.
          그래서 <b>수량이 1일 때 − 자리를 휴지통 단추로 바꾸는</b> 꼴을 흔히 쓰고,
          이렇게 하면 사용자가 누르기 전에 무슨 일이 일어날지 알 수 있습니다.<br>
          꺼진 단추를 <code>disabled</code>로 두면 <b>초점도 받지 않고 스크린 리더도 읽지 않기</b> 때문에,
          사용자는 단추가 왜 안 눌리는지 알 방법이 없습니다.
          <code>aria-disabled</code>로 두고 <b>이유를 알려 주는</b> 편이 낫습니다.</p>''',
  do=ul([
    "가운데 칸에 <b>쳐서 넣을 수</b> 있게 하기",
    "단추를 <b>44px</b> 이상으로 두기",
    "값이 바뀌면 스크린 리더로 <b>소리로도</b> 알리기",
  ]),
  dont=ul([
    "가운데 칸을 <b>잠그기</b>. 큰 수를 넣으려면 단추를 수십 번 눌러야 합니다",
    "최소값과 최대값에서도 단추를 <b>눌리게</b> 두기",
    "0이 되었을 때 <b>안내 없이</b> 상품을 빼기",
    "단추를 <b>작게</b> 만들기. 손가락으로 정확히 누르기 어렵습니다",
  ]),
  instead='−·＋ 단추 없이 칸만 두려면 <a href="numberinput.html">숫자 입력</a>을 쓰고, 정해진 범위 안에서 값을 고르게 하려면 <a href="slider.html">슬라이더</a>를 씁니다. 수가 아니라 흐름의 단계를 보여 주려는 것이라면 <a href="stepper.html">스테퍼</a>가 맞습니다. 단추 크기를 얼마로 잡을지는 <a href="touchtarget.html">터치 타깃</a>에서 다룹니다.',
  cases=cases([
    (q("2", "", "", True, "150px"), "장바구니 수량 고치기", "수량을 <b>한두 번</b>만 고치는 경우가 많습니다"),
    (q("1", "", "", True, "150px", False, True), "예약 인원수 고르기", "최소값을 1명으로 두고 1에서는 −를 끕니다"),
    (q("12", "", "", True, "150px"), "묶음 수량 넣기", "큰 수는 가운데 칸에 <b>쳐서</b> 넣습니다"),
  ]),
  code_lede="입력 칸 하나와 단추 두 개로 만듭니다. 끝값에서는 단추를 <code>aria-disabled</code>로 두고 왜 안 눌리는지 알려 줍니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"qty"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-label</span>=<span class="s">"하나 줄이기"</span>
          <span class="a">aria-disabled</span>=<span class="s">"true"</span>&gt;−&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"qty"</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">value</span>=<span class="s">"1"</span>
         <span class="a">aria-label</span>=<span class="s">"수량"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-label</span>=<span class="s">"하나 늘리기"</span>&gt;＋&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;수량 1&lt;/<span class="t">p</span>&gt;

.qty button { <span class="a">min-width</span>: <span class="a">44px</span>; <span class="a">min-height</span>: <span class="a">44px</span>; }''',
  keys=kbd([
    ("↑ ↓", "칸에서 값을 하나씩 올리고 내립니다"),
    ("숫자 키", "숫자를 바로 쳐 넣습니다. 값을 넣는 <b>가장 빠른</b> 방법입니다"),
    ("<code>aria-label</code>", "−와 ＋ 단추가 <b>무엇을 하는지</b> 적습니다"),
    ("<code>role=\"status\"</code>", "바뀐 값을 <b>소리로</b> 알립니다"),
    ("<code>aria-disabled</code>", "<code>disabled</code>와 달리 <b>초점을 받기</b> 때문에 이유를 알려 줄 수 있습니다"),
    ("확인하는 방법", "화면을 끄고 ＋를 눌러 <b>바뀐 값이 들리는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("최대 수량을 서버가 알려 주기", "재고나 구매 한도가 있으면 서버가 최대 수량을 내려 줘야 화면이 끝값에서 <b>＋를 끌 수</b> 있습니다."),
    ("수량 0의 뜻을 API에서 정하기", "수량 0이 '빼기'인지 '0개 주문'인지 <b>API에서 정해</b> 두어야 화면도 그 뜻에 맞춰 동작할 수 있습니다."),
    ("＋를 빠르게 연달아 누를 때", "＋를 연달아 누를 때마다 요청을 보내면 서버로 요청이 몰립니다. 그래서 <b>디바운스</b>를 두거나 마지막 값만 보냅니다."),
  ]),
  plat_lede="어느 플랫폼에서나 단추를 <b>작게 만들고 싶어지는</b> 부품이라서 크기를 따로 챙겨야 합니다.",
  plats=plats([
    ("웹", "직접 만들어 씀",
     q("2", "", "", True, "110px"),
     "<code>type=\"number\"</code>에 붙는 화살표는 <b>너무 작아서</b> 보통 직접 만듭니다."),
    ("iOS", "Stepper",
     '''              <div class="phone" role="img" aria-label="iOS 스테퍼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;font-size:6px">수량</div>
                <div style="position:absolute;right:5px;top:26px;width:26px;height:11px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "정식 부품이 있습니다. 다만 <b>입력 칸이 없어서</b> 큰 수를 넣는 데는 맞지 않습니다."),
    ("안드로이드", "직접 만들어 씀",
     '''              <div class="phone" role="img" aria-label="안드로이드 수량 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:34px;height:12px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "지침에 정해진 부품이 없어서 생김새가 <b>앱마다 다릅니다</b>. 단추 크기만은 48dp를 지킵니다."),
  ]),
  plat_note="iOS의 <code>Stepper</code>에는 <b>입력 칸이 없어서</b> '수량 24' 같은 값을 넣기 어렵고, 애플도 큰 수를 받을 때는 다른 꼴을 씁니다. 단추만 있는 스테퍼의 한계가 잘 드러나는 예입니다. 웹에서 만들 때는 두 단추 사이에 <b>입력 칸을 꼭 넣어 두면</b> 큰 수도 쉽게 넣을 수 있습니다.",
  siblings=siblings("quantity"),
  related='''        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>
        <li><a href="slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="stepper.html"><b>스테퍼</b><em>7부</em></a></li>''',
)
