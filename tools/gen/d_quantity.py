# -*- coding: utf-8 -*-
from ax4 import ax
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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">− · ＋ — 한두 번 고칠 때 빠르다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">가운데 칸 — 쳐서도 넣을 수 있어야 한다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">1에서 − · 최대에서 ＋ 는 꺼져 있다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단추는 44px — 손가락이 닿아야 한다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">값이 바뀌면 소리로도 알린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">0 으로 내리면 빼기인가 — 미리 정한다</div>
                </div>
              </div>'''

D = dict(
  slug="quantity", ko="수량 스테퍼", en="Quantity stepper · number stepper",
  desc="− 와 ＋ 로 수를 고치는 부품. 쳐서 넣기, 끝값 처리, 터치 타깃.",
  lede="<b>한두 번 고칠 때</b>만 빠릅니다. 24까지 올리려면 스물세 번을 눌러야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>목표까지 ＋만 눌러 보기</b>'를 눌러 보세요 — 데모가 <b>몇 번 눌러야 하는지</b>를 세서 적습니다.
          쳐서 넣으면 <b>한 번</b>입니다.<br>
          그래서 가운데 칸은 <b>읽기 전용으로 두지 않습니다</b>. 체크를 끄면 칸이 잠겨 큰 수를 넣을 길이 사라집니다.<br>
          단추는 <b>44px</b> 이어야 손가락이 닿습니다. 그리고 <b>1에서 −</b>, <b>최대에서 ＋</b>는 꺼져 있어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "수량 스테퍼, 수량 조절기, 숫자 스테퍼"),
    ("영어", "quantity stepper, number stepper, spinner"),
    ("같이 쓰는 말",
     "iOS 에서는 <b>Stepper</b>, 안드로이드·웹에서는 <b>수량 선택기</b>라 부르기도 합니다. "
     "<code>&lt;input type=\"number\"&gt;</code> 가 브라우저에서 띄우는 작은 화살표는 <b>스피너</b>입니다. "
     "7부의 <a href=\"stepper.html\">스테퍼</a>와는 <b>이름만 같고 전혀 다른 것</b>입니다."),
    ("자주 잘못 부름",
     "<b>스테퍼(단계)</b> — <a href=\"stepper.html\">7부의 스테퍼</a>는 <b>흐름의 단계</b>를 보여 줍니다.<br>"
     "<b>슬라이더</b> — <a href=\"slider.html\">슬라이더</a>는 <b>범위에서</b> 고릅니다.<br>"
     "<b>숫자 입력</b> — <a href=\"numberinput.html\">숫자 입력</a>은 <b>칸만</b> 있는 쪽입니다."),
  ]),
  axes=ax("수량 스테퍼"),
  oneline="<b>가운데 칸을 잠그지 마세요.</b> 큰 수를 넣을 유일한 길입니다.",
  states=states([
    (q("1", "", "1에서 − 는 꺼져 있다", True, "152px", False, True), "최소값", "<b>− 가 꺼진다</b>"),
    (q("3", "", "둘 다 눌린다", True), "보통", "가운데가 <b>쳐진다</b>"),
    (q("99", "", "최대에서 ＋ 가 꺼진다", True, "152px", True, False), "최대값", "<b>＋ 가 꺼진다</b>"),
    (q("24", "", "칸이 잠겨 있다", False, "152px", True, True, 22, True), "칸이 잠김", "<b>큰 수를 못 넣는다</b>"),
    (q("3", "", "단추가 24px — 손가락이 안 닿는다", False, "152px", True, True, 13), "작은 단추", "<b>44px 미달</b>"),
    (q("0", "", "0 이면 빼는 것인가", None, "152px", False, True), "0 으로", "<b>미리 정해</b> 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("− · ＋", "한두 번", "그 이상은 <b>치는 게</b> 빠르다"),
    ("가운데 칸", "쳐서 넣기", "<b>잠그지 않는다</b>"),
    ("끝값", "꺼짐", "1에서 − · 최대에서 ＋"),
    ("크기", "44px", "손가락이 닿아야"),
    ("소리", "값 바뀜 알림", "<code>aria-live</code> 나 <code>role=\"status\"</code>"),
    ("0", "빼기인가", "<b>미리 정한다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>0 으로 내렸을 때</b>를 정해 두지 않으면 사고가 납니다 —
          장바구니에서는 0 이 대개 '빼기'인데,
          말없이 사라지면 '내가 뭘 한 거지'가 됩니다.
          <b>1에서 − 를 누르면 휴지통으로 바뀌는</b> 꼴이 흔하고,
          그게 가장 덜 놀랍습니다.<br>
          꺼진 단추를 <code>disabled</code> 로 두면 <b>초점도 안 받고 소리로도 안 읽힙니다</b> —
          '왜 안 되지'를 알 길이 없습니다.
          <code>aria-disabled</code> 로 두고 <b>이유를 말해 주는</b> 쪽이 낫습니다.</p>''',
  do=ul([
    "가운데 칸을 <b>쳐서 넣을 수</b> 있게 하기",
    "단추를 <b>44px</b> 로 두기",
    "값이 바뀌면 <b>소리로도</b> 알리기",
  ]),
  dont=ul([
    "가운데 칸을 <b>잠그기</b> — 큰 수를 못 넣는다",
    "끝값에서도 <b>눌리게</b> 두기",
    "0 에서 <b>말없이</b> 빼기",
    "단추를 <b>작게</b> 만들기 — 손가락이 안 닿는다",
  ]),
  instead='칸만 있으면 <a href="numberinput.html">숫자 입력</a>, 범위에서 고르면 <a href="slider.html">슬라이더</a>, 흐름의 단계면 <a href="stepper.html">스테퍼</a>, 크기 규칙은 <a href="touchtarget.html">터치 타깃</a>.',
  cases=cases([
    (q("2", "", "", True, "150px"), "장바구니", "<b>한두 번</b> 고친다"),
    (q("1", "", "", True, "150px", False, True), "인원수", "최소 1명"),
    (q("12", "", "", True, "150px"), "묶음 수량", "큰 수는 <b>쳐서</b>"),
  ]),
  code_lede="칸 하나에 단추 둘입니다. 끝값에서는 <code>aria-disabled</code> 로 두고 이유를 말합니다.",
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
    ("↑ ↓", "칸에서 값을 하나씩 올리고 내린다"),
    ("숫자 키", "바로 쳐 넣는다 — <b>가장 빠른</b> 길"),
    ("<code>aria-label</code>", "− 와 ＋ 에 <b>무엇을 하는지</b> 적는다"),
    ("<code>role=\"status\"</code>", "바뀐 값을 <b>소리로</b> 알린다"),
    ("<code>aria-disabled</code>", "<code>disabled</code> 와 달리 <b>초점을 받고</b> 이유를 말할 수 있다"),
    ("확인하는 법", "화면을 끄고 ＋ 를 눌러 <b>값이 들리는지</b> 본다"),
  ]),
  backend=rows([
    ("최대 수량", "재고나 한도가 있으면 서버가 줘야 화면이 <b>＋ 를 끌 수</b> 있습니다."),
    ("0 의 뜻", "0 이 '빼기'인지 '0개 주문'인지 <b>API 가 정해</b> 둬야 화면이 맞출 수 있습니다."),
    ("빠른 연타", "＋ 를 연달아 누르면 요청이 몰립니다 — <b>디바운스</b>하거나 마지막 값만 보냅니다."),
  ]),
  plat_lede="<b>작게 만들고 싶은 유혹</b>이 어디서나 같습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     q("2", "", "", True, "110px"),
     "<code>type=\"number\"</code> 의 화살표는 <b>너무 작아</b> 보통 직접 만듭니다."),
    ("iOS", "Stepper",
     '''              <div class="phone" role="img" aria-label="iOS 스테퍼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;font-size:6px">수량</div>
                <div style="position:absolute;right:5px;top:26px;width:26px;height:11px;border-radius:4px;background:var(--bg);border:1px solid var(--line)"></div></div></div>''',
     "정식 부품입니다. 다만 <b>칸이 없어</b> 큰 수에는 안 맞습니다."),
    ("안드로이드", "직접 만듦",
     '''              <div class="phone" role="img" aria-label="안드로이드 수량 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:34px;height:12px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "지침에 정해진 것이 없어 <b>앱마다 다릅니다</b>. 크기만은 48dp 를 지킵니다."),
  ]),
  plat_note="iOS 의 <code>Stepper</code> 는 <b>칸이 없습니다</b> — 그래서 '수량 24' 같은 값에는 쓰기 어렵고, 애플 스스로도 큰 수에는 다른 꼴을 씁니다. 이 부품의 한계를 보여 주는 좋은 예입니다. 웹에서 만들 때는 <b>칸을 꼭 끼워 두면</b> 그 한계를 넘습니다.",
  siblings=siblings("quantity"),
  related='''        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>
        <li><a href="slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="stepper.html"><b>스테퍼</b><em>7부</em></a></li>''',
)
