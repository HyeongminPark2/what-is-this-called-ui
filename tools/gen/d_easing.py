# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

A = "var(--accent)"
def curve(path, w="128px", label=""):
    return ('              <svg viewBox="0 0 120 120" role="img" aria-label="' + label + '" '
            'style="width:100%;max-width:' + w + ';height:auto;display:block;background:var(--bg);'
            'border:1px solid var(--line);border-radius:6px">'
            '<line x1="0" y1="120" x2="120" y2="0" stroke="var(--line-strong)" stroke-width="1" stroke-dasharray="3 3"/>'
            '<path d="' + path + '" fill="none" stroke="' + A + '" stroke-width="3" stroke-linecap="round"/></svg>')

LIN = "M 0,120 L 120,0"
EASE = "M 0,120 C 30,90 42,0 120,0"
OUT = "M 0,120 C 26,12 36,0 120,0"
IN_ = "M 0,120 C 84,120 94,108 120,0"
INOUT = "M 0,120 C 50,120 70,0 120,0"
BOUNCE = "M 0,120 C 24,10 34,-14 60,6 C 74,16 78,-4 120,0"

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:150px">''' + curve(OUT, "150px", "ease-out 곡선").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가로축은 시간 0에서 1</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">세로축은 간 거리 0에서 1</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가파른 곳일수록 빠름</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">cubic-bezier(.22, .9, .3, 1)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">대각선은 linear, 속도가 일정함</div>
                </div>
              </div>'''

D = dict(
  slug="easing", ko="이징 곡선", en="Easing",
  desc="같은 거리를 같은 시간 동안 움직여도 속도를 어떻게 나눠 쓰느냐에 따라 느낌이 달라집니다. 대표적인 곡선 네 가지와 각각을 쓰는 자리를 보여 주는 항목입니다.",
  lede="이징 곡선은 움직이는 동안 속도를 <b>어떻게 나눠 쓸지</b> 정하는 곡선입니다. 거리와 시간이 같아도 곡선이 다르면 움직임의 <b>느낌</b>이 달라집니다.",
  axes_lede="움직임은 무엇이 바뀌었는지 <b>알려 주는</b> 수단입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 공이 <b>같은 거리를 같은 시간 동안</b> 달립니다. 속도를 나눠 쓰는 방식만 다른데도
          움직임의 느낌은 완전히 다릅니다.<br>
          줄 이름을 누르면 오른쪽에 그 줄의 곡선이 그려지는데, 그래프의 <b>가로가 시간, 세로가 간 거리</b>입니다.
          대각선이 <code>linear</code>이고, 곡선이 대각선에서 멀어질수록 빨라지고 느려지는 차이가 커집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "이징, 가속 곡선, 완급"),
    ("영어", "easing, timing function, easing curve"),
    ("같이 쓰는 말",
     "CSS에서는 <code>transition-timing-function</code>과 <code>animation-timing-function</code> 속성으로 정합니다. "
     "곡선을 네 숫자로 적는 방식을 <b>큐빅 베지에</b>(cubic-bezier), "
     "연속으로 움직이지 않고 몇 단계로 끊어 가는 방식을 <b>스텝</b>(steps)이라고 부릅니다. "
     "디자인 도구에서는 <b>이즈 인/아웃</b>이라고 부르고 그래프로 보여 줍니다."),
    ("자주 잘못 부르는 이름",
     "<b>지속 시간</b> — <a href=\"duration.html\">지속 시간</a>은 움직임이 '얼마나' 걸리는지, 이징은 '<b>어떻게</b>' 움직이는지를 정합니다. 두 값은 따로 정합니다.<br>"
     "<b>딜레이</b> — 딜레이는 움직임의 시작을 늦추는 값으로, <a href=\"stagger.html\">차례로 들어오기</a>에서 씁니다.<br>"
     "<b>스프링</b> — <a href=\"spring.html\">스프링</a>은 곡선이 아니라 <b>물리 계산</b>으로 움직임을 만들기 때문에 끝나는 시점이 미리 정해져 있지 않습니다."),
  ]),
  axes=ax("이징 곡선"),
  oneline="<b>들어오는 것에는 ease-out, 나가는 것에는 ease-in</b>을 씁니다. 이 규칙만 지켜도 대부분의 화면에서 움직임이 자연스러워집니다.",
  s4_title="대표적인 곡선 여섯 가지", s4_hint="대각선에서 벗어난 정도에 따라 달라지는 느낌",
  states=states([
    (curve(LIN, "128px", "linear 곡선"), "linear", "처음부터 끝까지 속도가 같아서 <b>기계적으로</b> 보입니다"),
    (curve(EASE, "128px", "ease 곡선"), "ease", "브라우저 기본값입니다. 무난하지만 <b>끝부분이 길게</b> 늘어집니다"),
    (curve(OUT, "128px", "ease-out 곡선"), "ease-out", "빠르게 출발해 천천히 멈춥니다. <b>들어오는 것</b>에 씁니다"),
    (curve(IN_, "128px", "ease-in 곡선"), "ease-in", "천천히 출발해 빠르게 사라집니다. <b>나가는 것</b>에 씁니다"),
    (curve(INOUT, "128px", "ease-in-out 곡선"), "ease-in-out", "시작과 끝이 모두 느립니다. <b>제자리로 돌아오는</b> 것에 씁니다"),
    (curve(BOUNCE, "128px", "튀는 곡선"), "튀는 곡선", "목표를 지나쳤다가 돌아옵니다. 재미있지만 <b>읽기를 방해</b>합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("곡선", "timing function", "<b>가로가 시간, 세로가 간 거리</b>입니다. 이것만 알면 그래프를 읽을 수 있습니다"),
    ("가로축", "0 → 1", "움직임이 시작해서 끝날 때까지를 0에서 1로 나타냅니다. <b>실제 시간 길이와는 상관없습니다</b>"),
    ("세로축", "0 → 1", "출발점에서 도착점까지를 0에서 1로 나타냅니다. 값이 <b>1을 넘으면</b> 목표를 지나쳤다가 돌아온다는 뜻입니다"),
    ("가파른 구간", "빠른 구간", "곡선이 가파른 곳일수록 빠르게 움직입니다"),
    ("네 숫자", "cubic-bezier", "곡선 모양을 정하는 손잡이 두 개의 좌표입니다. <b>앞의 두 숫자가 출발 쪽, 뒤의 두 숫자가 도착 쪽</b>을 정합니다"),
    ("대각선", "linear", "속도가 변하지 않습니다. 실제 물체는 이렇게 움직이지 않아서 <b>기계적으로</b> 보입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          현실의 물체는 <b>갑자기 멈추지 않고</b> 서서히 속도를 줄입니다. 그래서 끝에서 속도가 뚝 끊기는
          <code>linear</code> 움직임은 물체보다는 기계의 움직임으로 보여 어색합니다.
          반대로 <b>계속 도는 것</b>(스피너)과 <b>진행 막대</b>에는 <code>linear</code>가 맞습니다.
          이런 요소는 속도가 바뀌면 작업이 꾸준히 진행되는 것이 아니라 중간에 막혔다가 풀린 것처럼 보이기 때문입니다.</p>''',
  do_title="이징 곡선을 정해서 쓰는 경우",
  dont_title="이징 곡선을 고를 때 피할 것",
  instead_title="이징 곡선 대신 쓰거나 함께 정할 것",
  do=ul([
    "자리·크기·투명도가 <b>바뀌는 모든 것</b>에 쓸 기본 곡선을 정해 둘 때",
    "들어오는 것에 <b>ease-out</b>, 나가는 것에 <b>ease-in</b>을 줄 때",
    "제자리로 돌아오는 것에 <b>ease-in-out</b>을 줄 때",
  ]),
  dont=ul([
    "<code>linear</code>를 기본 곡선으로 둘 때. <code>linear</code>는 <b>도는 것과 진행 막대</b>에만 씁니다",
    "항목마다 곡선을 따로 정할 때. 토큰으로 <b>두세 개만</b> 정해 두고 돌려 씁니다",
    "본문이나 목록에 <b>튀는 곡선</b>을 쓸 때. 글을 읽으려는 사이에 또 움직여서 읽기 어렵습니다",
    "들어오는 것에 ease-in을 쓸 때. 출발이 느려서 <b>굼떠 보이는데</b>, 이런 실수가 가장 흔합니다",
  ]),
  instead='끝나는 시점을 정하지 않고 손으로 민 듯한 움직임을 내려면 <a href="spring.html">스프링</a>을 씁니다. 움직임이 얼마나 걸릴지는 <a href="duration.html">지속 시간</a>에서, 들어오고 나가는 움직임을 짝짓는 방법은 <a href="enterexit.html">진입과 퇴장</a>에서 다룹니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:5px">
                <div style="height:22px;border-radius:999px;background:var(--bg);border:1px solid var(--line);position:relative"><span style="position:absolute;top:3px;right:4px;width:14px;height:14px;border-radius:50%;background:var(--accent)"></span></div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--accent)">--ease-out: cubic-bezier(.22,.9,.3,1)</span>
              </div>''',
     "곡선을 토큰으로 정해 두기", "곡선도 <a href=\"../items/color.html\">색</a>처럼 <b>이름을 붙인 토큰</b>으로 정해 두고 씁니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9.5px;color:var(--fg-muted)">들어올 때</span>''' + curve(OUT, "100%", "ease-out").strip() + '''
                <span style="font-size:9.5px;color:var(--fg-muted)">나갈 때</span>''' + curve(IN_, "100%", "ease-in").strip() + '''
              </div>''',
     "들어올 때와 나갈 때 곡선 짝짓기", "들어올 때와 나갈 때의 곡선을 한 벌로 정해 두면 화면마다 <b>헷갈리지 않습니다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:5px;place-items:center">
                <span style="width:22px;height:22px;border-radius:50%;border:3px solid var(--line);border-top-color:var(--accent);display:block"></span>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">animation: spin 1s linear infinite</span>
              </div>''',
     "linear를 써야 하는 자리", "도는 것과 진행 막대에 씁니다. 이런 요소는 <b>속도가 변하면 고장 난 것처럼</b> 보입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="곡선을 <b>이름 붙인 토큰</b>으로 정의해 두고, 들어올 때와 나갈 때에 짝지어 씁니다.",
  code=''':root {
  <span class="a">--ease-out</span>: cubic-bezier(.22, .9, .3, <span class="a">1</span>);   <span class="c">/* 들어올 때 */</span>
  <span class="a">--ease-in</span>:  cubic-bezier(.7, <span class="a">0</span>, .84, <span class="a">0</span>);    <span class="c">/* 나갈 때 */</span>
  <span class="a">--ease-both</span>: cubic-bezier(.4, <span class="a">0</span>, .2, <span class="a">1</span>);    <span class="c">/* 제자리로 */</span>
}

.sheet            { <span class="a">transition</span>: transform <span class="a">180ms</span> <span class="a">var</span>(--ease-in); }
.sheet[data-open] { <span class="a">transition</span>: transform <span class="a">260ms</span> <span class="a">var</span>(--ease-out); }

<span class="c">/* 도는 것만 linear */</span>
.spinner { <span class="a">animation</span>: spin <span class="a">1s</span> linear infinite; }''',
  keys_heads="<th>알아 둘 규칙</th><th>자세한 내용</th>",
  keys=kbd([
    ("곡선을 적지 않았을 때", "<code>transition: transform 200ms</code>처럼 곡선을 적지 않으면 <code>ease</code>가 적용됩니다"),
    ("<code>cubic-bezier</code>의 네 숫자", "<b>x1 y1 x2 y2</b> 순서입니다. x는 0~1을 벗어날 수 없지만 y는 벗어나도 되고, y가 1을 넘으면 목표를 지나쳤다가 돌아옵니다"),
    ("<code>steps(n)</code>", "연속으로 움직이지 않고 n단계로 끊어서 갑니다. 스프라이트 애니메이션이나 숫자 카운터에 씁니다"),
    ("속성마다 곡선을 <b>따로</b> 주기", "<code>transition: transform 260ms var(--ease-out), opacity 180ms linear</code>처럼 속성마다 다른 곡선을 줄 수 있습니다"),
    ("<code>linear</code>는 도는 것에만 쓰기", "스피너와 진행 막대에 씁니다. 그 밖의 자리에서는 대부분 맞지 않습니다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>를 켰을 때", "곡선은 그대로 둬도 됩니다. 줄여야 하는 것은 움직이는 <b>거리와 지속 시간</b>입니다"),
  ]),
  backend=rows([
    ("곡선은 화면 쪽에서만 처리", "이징은 모두 화면 쪽에서 처리합니다. 다만 <b>움직임이 끝나기를 기다렸다가</b> 요청을 보내면 응답도 그만큼 늦게 오기 때문에, 요청은 움직임을 시작할 때 먼저 보냅니다."),
    ("응답이 애니메이션보다 먼저 왔을 때", "데이터가 50ms 만에 와도 애니메이션이 400ms 걸리면 사용자는 400ms를 기다립니다. 화면이 느리게 느껴질 때 <b>원인이 서버가 아닐 수도 있습니다.</b>"),
    ("성능 지표에 들어가는 연출 시간", "화면이 뜨기까지 걸린 시간을 재는 지표(LCP 등)에는 애니메이션 시간도 들어갑니다. 그래서 <b>요소가 늦게 나타나는 연출</b>은 점수를 깎습니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>빠르게 출발해 천천히 멈추는 움직임</b>을 권합니다.",
  plats=plats([
    ("웹", "cubic-bezier",
     curve(OUT, "100px", "웹 ease-out"),
     "곡선을 네 숫자로 직접 적습니다. 이름이 붙은 곡선은 <code>ease</code>·<code>ease-in</code>·<code>ease-out</code>·<code>ease-in-out</code> 네 가지뿐입니다."),
    ("iOS", "UIView · SwiftUI",
     curve(OUT, "100px", "iOS easeOut"),
     "<code>.easeOut</code>이 있지만 요즘은 <b>스프링을 기본</b>으로 씁니다. 시스템 애니메이션도 대부분 스프링입니다."),
    ("안드로이드", "Material 3",
     curve(INOUT, "100px", "Material emphasized"),
     "<b>emphasized</b>, <b>standard</b>처럼 이름이 붙은 곡선을 정해 두었습니다. 들어오는 움직임에는 <code>emphasized decelerate</code>를 권합니다."),
  ]),
  plat_note="\"애니메이션 좀 자연스럽게 해 주세요\"라는 요청의 절반은 <b>이징</b> 문제이고 나머지 절반은 <a href=\"duration.html\">길이</a> 문제입니다. 곡선 토큰을 세 개 정해 두고 그것만 쓰게 하면 화면마다 다르게 움직이는 문제가 거의 사라집니다. 처음에 토큰을 정하는 데는 한 시간 정도면 되지만, 화면이 늘어난 뒤에 하나하나 맞추려면 한 주가 걸리기도 합니다.",
  siblings=siblings("easing"),
  related='''        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>
        <li><a href="spring.html"><b>스프링</b><em>9부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>''',
)
