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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가로 = 시간 0 → 1</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">세로 = 간 거리 0 → 1</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가파른 곳 = 빠른 구간</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">cubic-bezier(.22, .9, .3, 1)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">대각선 = linear — 기계가 미는 움직임</div>
                </div>
              </div>'''

D = dict(
  slug="easing", ko="이징 곡선", en="Easing",
  desc="같은 거리를 같은 시간에 달려도 속도를 어떻게 나눠 쓰느냐로 느낌이 갈린다. 네 곡선과 쓰는 자리.",
  lede="속도를 <b>어떻게 나눠 쓸지</b>를 정하는 곡선. 거리도 시간도 같은데 <b>느낌만</b> 달라집니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 공이 <b>같은 거리를 같은 시간에</b> 달립니다. 다른 것은 속도를 나눠 쓰는 방식뿐인데
          느낌은 완전히 다릅니다.<br>
          줄 이름을 누르면 오른쪽에 그 곡선이 그려집니다 — <b>가로가 시간, 세로가 간 거리</b>입니다.
          대각선이 <code>linear</code>고, 거기서 멀어질수록 '밀고 당기는' 느낌이 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "이징, 가속 곡선, 완급"),
    ("영어", "easing, timing function, easing curve"),
    ("같이 쓰는 말",
     "CSS 에서는 <code>transition-timing-function</code>·<code>animation-timing-function</code>입니다. "
     "곡선을 네 숫자로 적는 것이 <b>큐빅 베지에</b>(cubic-bezier), "
     "뚝뚝 끊어 가는 것이 <b>스텝</b>(steps)입니다. "
     "디자인 도구에서는 <b>이즈 인/아웃</b>이라 부르고 그래프로 보여 줍니다."),
    ("자주 잘못 부름",
     "<b>지속 시간</b> — <a href=\"duration.html\">지속 시간</a>은 '얼마나', 이징은 '<b>어떻게</b>'입니다. 둘은 따로 정합니다.<br>"
     "<b>딜레이</b> — 시작을 늦추는 것은 <a href=\"stagger.html\">차례로 들어오기</a>에서 씁니다.<br>"
     "<b>스프링</b> — <a href=\"spring.html\">스프링</a>은 곡선이 아니라 <b>물리 계산</b>이라 끝나는 때가 정해져 있지 않습니다."),
  ]),
  axes=ax("이징 곡선"),
  oneline="<b>들어오는 것은 ease-out, 나가는 것은 ease-in.</b> 이 한 줄만 지켜도 대부분의 화면이 자연스러워집니다.",
  s4_title="곡선 여섯", s4_hint="대각선에서 얼마나 벗어났나",
  states=states([
    (curve(LIN, "128px", "linear 곡선"), "linear", "처음부터 끝까지 같은 속도. <b>기계가 미는</b> 것 같다"),
    (curve(EASE, "128px", "ease 곡선"), "ease", "브라우저 기본값. 무난하지만 <b>끝이 길다</b>"),
    (curve(OUT, "128px", "ease-out 곡선"), "ease-out", "빨리 떠나 천천히 멎는다. <b>들어오는 것</b>에"),
    (curve(IN_, "128px", "ease-in 곡선"), "ease-in", "천천히 떠나 빨리 사라진다. <b>나가는 것</b>에"),
    (curve(INOUT, "128px", "ease-in-out 곡선"), "ease-in-out", "양끝이 느리다. <b>제자리로 돌아오는</b> 것에"),
    (curve(BOUNCE, "128px", "튀는 곡선"), "튀는 곡선", "목표를 지나쳤다 온다. 재미있지만 <b>읽기를 방해</b>한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("곡선", "timing function", "<b>가로가 시간, 세로가 간 거리.</b> 이 한 줄만 알면 그래프가 읽힌다"),
    ("가로축", "0 → 1", "움직임이 시작해서 끝날 때까지. <b>길이와는 상관없다</b>"),
    ("세로축", "0 → 1", "출발점에서 도착점까지. <b>1을 넘으면</b> 지나쳤다 돌아온다"),
    ("가파른 구간", "빠른 구간", "곡선이 가파른 곳에서 빨리 움직인다"),
    ("네 숫자", "cubic-bezier", "손잡이 두 개의 좌표. <b>첫 둘이 출발, 뒤 둘이 도착</b> 쪽이다"),
    ("대각선", "linear", "속도가 안 변한다. <b>물체가 아니라 기계</b>처럼 보인다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          현실의 물체는 <b>갑자기 멈추지 않습니다.</b> 그래서 <code>linear</code>가 어색합니다 —
          속도가 끝에서 뚝 끊기는 움직임은 물체가 아니라 기계의 움직임으로 읽힙니다.
          반대로 <b>끝없이 도는 것</b>(스피너)과 <b>진행 막대</b>는 <code>linear</code>가 맞습니다.
          속도가 바뀌면 '뭔가 되고 있다'가 아니라 '막혔다 풀렸다'로 읽히기 때문입니다.</p>''',
  do=ul([
    "자리·크기·투명도가 <b>바뀌는 모든 것</b> — 기본값을 한 번 정해 둔다",
    "들어오는 것에 <b>ease-out</b>, 나가는 것에 <b>ease-in</b>",
    "제자리로 돌아오는 것에 <b>ease-in-out</b>",
  ]),
  dont=ul([
    "<code>linear</code>를 기본으로 두는 것 — <b>도는 것과 진행 막대</b>에만",
    "항목마다 다른 곡선 — 토큰으로 <b>두셋만</b> 정해 둔다",
    "<b>튀는 곡선</b>을 본문·목록에 — 읽으려는데 또 움직인다",
    "들어오는 데 ease-in — <b>굼떠 보인다</b>. 가장 흔한 실수다",
  ]),
  instead='끝을 안 정하고 손맛을 내려면 <a href="spring.html">스프링</a>, 얼마나 걸릴지는 <a href="duration.html">지속 시간</a>, 들고 나는 짝은 <a href="enterexit.html">진입과 퇴장</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:5px">
                <div style="height:22px;border-radius:999px;background:var(--bg);border:1px solid var(--line);position:relative"><span style="position:absolute;top:3px;right:4px;width:14px;height:14px;border-radius:50%;background:var(--accent)"></span></div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--accent)">--ease-out: cubic-bezier(.22,.9,.3,1)</span>
              </div>''',
     "토큰으로 둔다", "곡선도 <a href=\"../items/color.html\">색</a>처럼 <b>이름을 붙여</b> 쓴다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9.5px;color:var(--fg-muted)">들어옴</span>''' + curve(OUT, "100%", "ease-out").strip() + '''
                <span style="font-size:9.5px;color:var(--fg-muted)">나감</span>''' + curve(IN_, "100%", "ease-in").strip() + '''
              </div>''',
     "들고 날 때 짝으로", "한 벌로 정해 두면 <b>안 헷갈린다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:5px;place-items:center">
                <span style="width:22px;height:22px;border-radius:50%;border:3px solid var(--line);border-top-color:var(--accent);display:block"></span>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">animation: spin 1s linear infinite</span>
              </div>''',
     "linear 가 맞는 자리", "도는 것·진행 막대. <b>속도가 변하면 고장 같다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 곡선의 계약서",
  code_lede="곡선을 <b>이름 붙인 토큰</b>으로 두고, 들고 나는 쪽에 짝지어 씁니다.",
  code=''':root {
  <span class="a">--ease-out</span>: cubic-bezier(.22, .9, .3, <span class="a">1</span>);   <span class="c">/* 들어올 때 */</span>
  <span class="a">--ease-in</span>:  cubic-bezier(.7, <span class="a">0</span>, .84, <span class="a">0</span>);    <span class="c">/* 나갈 때 */</span>
  <span class="a">--ease-both</span>: cubic-bezier(.4, <span class="a">0</span>, .2, <span class="a">1</span>);    <span class="c">/* 제자리로 */</span>
}

.sheet            { <span class="a">transition</span>: transform <span class="a">180ms</span> <span class="a">var</span>(--ease-in); }
.sheet[data-open] { <span class="a">transition</span>: transform <span class="a">260ms</span> <span class="a">var</span>(--ease-out); }

<span class="c">/* 도는 것만 linear */</span>
.spinner { <span class="a">animation</span>: spin <span class="a">1s</span> linear infinite; }''',
  keys=kbd([
    ("기본값은 <code>ease</code>", "<code>transition: transform 200ms</code>라고만 쓰면 <code>ease</code>가 붙는다"),
    ("<code>cubic-bezier</code>의 네 숫자", "<b>x1 y1 x2 y2</b>. x 는 0~1 을 벗어날 수 없고, y 는 벗어나도 된다 — 그게 '지나침'이다"),
    ("<code>steps(n)</code>", "뚝뚝 끊어 간다. 스프라이트 애니메이션·숫자 카운터에"),
    ("곡선은 <b>속성마다</b> 따로", "<code>transition: transform 260ms var(--ease-out), opacity 180ms linear</code>"),
    ("<code>linear</code>는 도는 것에만", "스피너·진행 막대. 그 밖에는 거의 늘 틀린 선택이다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>에서", "곡선은 그대로 둬도 된다. 줄여야 하는 것은 <b>거리와 길이</b>다"),
  ]),
  backend=rows([
    ("서버는 곡선을 모른다", "이징은 전부 화면 쪽 일입니다. 다만 <b>움직임이 끝나기를 기다렸다</b> 요청을 보내면 응답이 그만큼 늦습니다 — 요청은 먼저 보냅니다."),
    ("응답이 먼저 와도", "데이터가 50ms 에 와도 애니메이션이 400ms 면 사용자는 400ms 를 기다립니다. <b>느린 건 서버가 아닐 수 있습니다.</b>"),
    ("측정에 섞인다", "'화면이 뜨기까지'를 재는 지표(LCP 등)에 애니메이션 시간이 들어갑니다. <b>늦게 나타나는 연출</b>은 점수를 깎습니다."),
  ]),
  plat_lede="세 곳 모두 <b>'빨리 떠나 천천히 멎는다'</b>로 같은 결론에 닿았습니다.",
  plats=plats([
    ("웹", "cubic-bezier",
     curve(OUT, "100px", "웹 ease-out"),
     "네 숫자를 직접 적습니다. 이름 있는 것은 <code>ease</code>·<code>ease-in</code>·<code>ease-out</code>·<code>ease-in-out</code> 넷뿐입니다."),
    ("iOS", "UIView · SwiftUI",
     curve(OUT, "100px", "iOS easeOut"),
     "<code>.easeOut</code>이 있지만 요즘은 <b>스프링이 기본</b>입니다. 시스템 애니메이션이 거의 다 스프링입니다."),
    ("안드로이드", "Material 3",
     curve(INOUT, "100px", "Material emphasized"),
     "<b>emphasized</b>·<b>standard</b>로 이름이 정해져 있습니다. 들어올 때 <code>emphasized decelerate</code>를 권합니다."),
  ]),
  plat_note="\"애니메이션 좀 자연스럽게\"라는 말의 절반은 <b>이징</b>이고 절반은 <a href=\"duration.html\">길이</a>입니다. 곡선 토큰 세 개를 정해 두고 그것만 쓰게 하면, 화면마다 다르게 움직이는 문제가 거의 사라집니다. 처음에 정하는 데 한 시간, 나중에 고치는 데 한 주입니다.",
  siblings=siblings("easing"),
  related='''        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>
        <li><a href="spring.html"><b>스프링</b><em>9부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>''',
)
