# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def rs(lo, hi, label="", note="", ok=None, w="152px", fields=True, flipped=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    left, right = min(lo, hi), max(lo, hi)
    bar = ('<span style="position:relative;display:block;height:4px;border-radius:999px;background:var(--bg);margin:7px 4px">'
           '<span style="position:absolute;top:0;bottom:0;left:' + str(left / 5) + '%;width:' + str((right - left) / 5) + '%;'
           'border-radius:999px;background:' + ('var(--danger)' if flipped else 'var(--accent)') + '"></span>'
           '<span style="position:absolute;top:-4px;left:' + str(left / 5) + '%;width:11px;height:11px;margin-left:-5px;'
           'border-radius:999px;background:var(--surface);border:2px solid var(--accent)"></span>'
           '<span style="position:absolute;top:-4px;left:' + str(right / 5) + '%;width:11px;height:11px;margin-left:-5px;'
           'border-radius:999px;background:var(--surface);border:2px solid var(--accent)"></span></span>')
    f = ('<span style="display:flex;gap:4px;align-items:center;font-size:7.5px;font-family:var(--mono)">'
         '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;background:var(--surface)">' + str(lo) + '</span>'
         '<span style="color:var(--fg-muted)">~</span>'
         '<span style="border:1px solid var(--line);border-radius:3px;padding:1px 5px;background:var(--surface)">' + str(hi) + '</span>'
         '<span style="color:var(--fg-muted)">만원</span></span>') if fields else ''
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:block;border:1px solid ' + c + ';border-radius:4px;background:var(--surface);padding:4px 6px">'
            + bar + '</span>' + f
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">손잡이 둘 — 최소와 최대</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">서로 지나치면 최소가 최대보다 커진다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">숫자 칸 — 눈금에 없는 값도 넣는다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">눈금 — 넣을 수 있는 값의 가짓수를 정한다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">두 손잡이가 겹치면 어느 쪽인지 모른다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">Tab 으로 둘을 갈라서 다룬다</div>
                </div>
              </div>'''

D = dict(
  slug="rangeslider", ko="범위 슬라이더", en="Range slider",
  desc="두 손잡이로 범위를 고르는 부품. 손잡이가 지나치는 문제와 눈금의 한계.",
  lede="손잡이가 <b>둘</b>이라 슬라이더의 문제가 전부 두 배가 됩니다 — 특히 <b>서로 지나칠 때</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>손잡이를 서로 지나치게 두면 <b>최소가 최대보다 큰</b> 값이 만들어집니다 —
          체크를 끄고 끌어 보면 데모가 <b>뒤집힌 상태</b>를 잡아 적습니다.<br>
          슬라이더만으로는 <b>정확한 값</b>을 못 넣습니다. 눈금을 50만원으로 키우면
          데모가 <b>끌어서 넣을 수 있는 값의 가짓수</b>를 세서 보여 줍니다.
          숫자 칸은 <b>눈금에 없는 값</b>도 넣을 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "범위 슬라이더, 구간 슬라이더, 두 손잡이 슬라이더"),
    ("영어", "range slider, dual slider, two-thumb slider"),
    ("같이 쓰는 말",
     "손잡이를 <b>섬</b>(thumb), 칠해진 구간을 <b>트랙 필</b>이라 합니다. "
     "두 손잡이가 서로 못 넘어가게 막는 것을 <b>크로싱 방지</b>, "
     "둘이 겹쳤을 때 어느 쪽을 잡을지 정하는 것을 <b>핸들 우선순위</b>라 부릅니다."),
    ("자주 잘못 부름",
     "<b>슬라이더</b> — <a href=\"slider.html\">슬라이더</a>는 손잡이가 <b>하나</b>입니다.<br>"
     "<b>날짜 범위</b> — <a href=\"daterange.html\">날짜 범위</a>는 <b>날짜</b>를 다룹니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터와 패싯</a>은 <b>화면 전체</b>의 설계입니다."),
  ]),
  axes=ax("범위 슬라이더"),
  oneline="<b>숫자 칸을 같이 두세요.</b> 끌어서는 원하는 값이 없을 때가 많습니다.",
  states=states([
    (rs(100, 300, "", "보통", True), "기본", "<b>두 손잡이</b>"),
    (rs(380, 120, "", "최소가 최대보다 크다", False, "152px", True, True), "뒤집힘", "<b>막아야</b> 한다"),
    (rs(200, 210, "", "두 손잡이가 겹쳤다", None), "겹침", "<b>어느 쪽인지</b> 모른다"),
    (rs(0, 500, "", "전체 범위", True), "다 고름", "조건이 <b>없는 것</b>과 같다"),
    (rs(420, 450, "", "눈금에 없는 값 — 칸으로 넣었다", True), "숫자 칸", "<b>정확히</b> 넣는다"),
    (rs(100, 300, "", "칸이 없다 — 눈금 값만 된다", False, "152px", False), "칸 없음", "<b>50 단위</b>만 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("손잡이 둘", "최소 · 최대", "문제가 <b>두 배</b>"),
    ("지나침", "뒤집힘", "<b>밀어내거나</b> 막는다"),
    ("숫자 칸", "정확한 값", "눈금에 <b>없는 값</b>도"),
    ("눈금", "가짓수", "클수록 <b>못 넣는 값</b>이 는다"),
    ("겹침", "모호함", "어느 쪽을 잡았는지"),
    ("Tab", "둘을 갈라서", "키보드는 <b>따로</b> 다룬다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          범위 슬라이더는 <b>손가락으로 대충 정할 때</b> 좋고,
          <b>정확한 값을 넣을 때</b> 나쁩니다 — 둘 다 필요한 경우가 대부분이라
          <b>숫자 칸을 같이 두는</b> 것이 거의 늘 답입니다.<br>
          두 손잡이가 겹쳤을 때도 정해 둬야 합니다 —
          겹친 자리에서 오른쪽으로 끌면 <b>어느 손잡이가 따라올지</b>를
          정하지 않으면 사용자가 원하는 쪽이 안 움직입니다.
          보통 <b>끄는 방향 쪽 손잡이</b>를 잡는 것이 덜 놀랍습니다.</p>''',
  do=ul([
    "<b>숫자 칸</b>을 같이 두기",
    "두 손잡이가 <b>서로 못 넘게</b> 하거나 <b>밀어내게</b> 하기",
    "각 손잡이에 <b>이름</b> 붙이기 — '최소 금액' · '최대 금액'",
  ]),
  dont=ul([
    "슬라이더만 두기 — <b>정확한 값</b>을 못 넣는다",
    "뒤집힌 값을 <b>그대로 보내기</b>",
    "눈금을 너무 <b>크게</b> 두기 — 원하는 값이 없어진다",
    "손잡이에 <b>이름을 안 붙이기</b> — 소리로는 둘이 구별이 안 된다",
  ]),
  instead='손잡이가 하나면 <a href="slider.html">슬라이더</a>, 날짜면 <a href="daterange.html">날짜 범위</a>, 칸으로만 받으면 <a href="numberinput.html">숫자 입력</a>, 거르기 화면은 <a href="filter.html">필터와 패싯</a>.',
  cases=cases([
    (rs(100, 300, "", "", True, "150px"), "금액 범위", "<b>대충</b> 정할 때"),
    (rs(20, 60, "", "", True, "150px"), "나이대", "눈금이 <b>촘촘해도</b> 된다"),
    (rs(0, 500, "", "", True, "150px"), "조건 없음", "<b>전체</b>면 조건을 지운다"),
  ]),
  code_lede="<code>&lt;input type=\"range\"&gt;</code> 둘을 겹쳐 쓰고, 숫자 칸을 같이 둡니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"range"</span>&gt;
  &lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"range"</span> <span class="a">id</span>=<span class="s">"lo"</span> <span class="a">min</span>=<span class="s">"0"</span> <span class="a">max</span>=<span class="s">"500"</span>
         <span class="a">value</span>=<span class="s">"100"</span> <span class="a">aria-label</span>=<span class="s">"최소 금액"</span>&gt;
  &lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"range"</span> <span class="a">id</span>=<span class="s">"hi"</span> <span class="a">min</span>=<span class="s">"0"</span> <span class="a">max</span>=<span class="s">"500"</span>
         <span class="a">value</span>=<span class="s">"300"</span> <span class="a">aria-label</span>=<span class="s">"최대 금액"</span>&gt;
&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">input</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">aria-label</span>=<span class="s">"최소 금액(만원)"</span>&gt; ~
&lt;<span class="t">input</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">aria-label</span>=<span class="s">"최대 금액(만원)"</span>&gt;

<span class="c">/* 겹쳐 놓고 손잡이만 눌리게 한다 */</span>
.range input { <span class="a">position</span>: absolute; <span class="a">width</span>: <span class="a">100%</span>; <span class="a">pointer-events</span>: none; }
.range input::-webkit-slider-thumb { <span class="a">pointer-events</span>: auto; }''',
  keys=kbd([
    ("← →", "값을 한 눈금씩 옮긴다"),
    ("Home · End", "<b>최소 · 최대</b>로 보낸다"),
    ("Tab", "두 손잡이를 <b>갈라서</b> 다룬다 — 겹쳐 있어도 된다"),
    ("<code>aria-label</code>", "손잡이마다 <b>이름</b>을 준다"),
    ("<code>aria-valuetext</code>", "'100만원'처럼 <b>단위까지</b> 읽히게 한다"),
    ("확인하는 법", "키보드만으로 <b>두 손잡이를 모두</b> 움직여 본다"),
  ]),
  backend=rows([
    ("두 값으로", "<code>{min: 100, max: 300}</code> — 뒤집힌 값이 와도 <b>서버가 바로잡는</b> 편이 안전합니다."),
    ("열린 범위", "'300만원 이상'처럼 한쪽이 없는 경우를 <b><code>null</code></b> 로 표현해 둡니다."),
    ("분포", "값의 분포를 주면 <b>막대로 그려</b> 어디에 많은지 보일 수 있습니다."),
  ]),
  plat_lede="<b>기본 부품이 없어</b> 직접 만듭니다.",
  plats=plats([
    ("웹", "range 둘을 겹쳐",
     rs(100, 300, "", "", True, "110px"),
     "<code>input[type=range]</code> 가 하나짜리뿐이라 <b>둘을 겹쳐</b> 만듭니다."),
    ("iOS", "없다 — 직접",
     '''              <div class="phone" role="img" aria-label="iOS 범위 슬라이더 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:32px;height:3px;border-radius:999px;background:var(--bg)"></div>
                <div style="position:absolute;left:14px;right:18px;top:32px;height:3px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "<code>Slider</code> 는 하나짜리뿐입니다 — 범위는 <b>직접</b> 만듭니다."),
    ("안드로이드", "RangeSlider",
     '''              <div class="phone" role="img" aria-label="안드로이드 범위 슬라이더 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:32px;height:3px;border-radius:999px;background:var(--bg)"></div>
                <div style="position:absolute;left:14px;right:18px;top:32px;height:3px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "Material 에 <b>RangeSlider</b> 가 정식으로 있습니다 — 드문 경우입니다."),
  ]),
  plat_note="Material 의 <b>RangeSlider</b> 는 세 플랫폼 가운데 유일한 정식 부품인데, 거기서도 <b>끌어서 정확한 값</b>을 넣는 문제는 그대로입니다. 그래서 Material 지침조차 <b>값을 숫자로 보여 주라</b>고 적어 둡니다. 웹에서 만들 때도 '칸을 같이 둘지'가 아니라 <b>'어디에 둘지'</b>를 고민하는 편이 맞습니다.",
  siblings=siblings("rangeslider"),
  related='''        <li><a href="slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="daterange.html"><b>날짜 범위</b><em>10부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="numberinput.html"><b>숫자 입력</b><em>4부</em></a></li>''',
)
