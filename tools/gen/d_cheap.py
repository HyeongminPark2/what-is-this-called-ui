# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def band(label, stages, cost, warn=False, w="152px"):
    col = ("var(--warn)" if warn == 2 else "var(--danger)") if warn else "var(--accent)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<div style="font-family:var(--mono);font-size:10px;color:' + col + '">' + label + '</div>'
            '<div style="display:flex;gap:3px">' + stages + '</div>'
            '<span style="font-size:9px;color:var(--fg-muted)">' + cost + '</span></div>')

def step(name, on):
    return ('<span style="flex:1;text-align:center;font-size:8.5px;padding:3px 0;border-radius:3px;'
            + ('background:var(--accent);color:#fff' if on == 1 else
               'background:var(--danger);color:#fff' if on == 2 else
               'background:var(--warn);color:#fff' if on == 3 else
               'background:var(--bg);color:var(--fg-faint);border:1px solid var(--line)')
            + '">' + name + '</span>')

PIPE = lambda a, b, c, d: step('스타일', a) + step('배치', b) + step('칠하기', c) + step('합치기', d)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:230px;display:flex;gap:3px">''' + PIPE(1, 0, 0, 1) + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">transform · opacity — 배치도 칠하기도 건너뛴다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">color · box-shadow — 다시 칠한다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">left · width · margin — 배치부터 다시</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한 프레임에 쓸 수 있는 시간 = 16.7ms</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">쓰고 바로 읽으면 그 자리에서 배치가 돈다</div>
                </div>
              </div>'''

D = dict(
  slug="cheap", ko="무엇을 움직이나", en="Cheap vs expensive properties",
  desc="transform·opacity는 배치를 다시 하지 않고, left·width는 한다. 버벅임의 거의 모든 원인.",
  lede="같은 움직임도 <b>어떤 속성을 바꾸느냐</b>에 따라 값이 다릅니다. 버벅임의 거의 전부가 여기서 납니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 가지 방법으로 같은 거리를 움직이고 <b>한 프레임을 만드는 데 걸린 시간</b>을 잽니다.<br>
          상자 수를 올리면 차이가 벌어집니다 — <code>transform</code>·<code>opacity</code>는
          거의 그대로인데 <code>left</code>·<code>width</code>는 함께 올라갑니다.
          그 차이가 그대로 <b>버벅임</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "리플로우, 리페인트, 합성, 레이어"),
    ("영어", "reflow / layout, repaint, compositing, GPU acceleration"),
    ("같이 쓰는 말",
     "배치를 다시 재는 것이 <b>리플로우</b>(reflow)·<b>레이아웃</b>, "
     "다시 칠하는 것이 <b>리페인트</b>(repaint)·<b>페인트</b>, "
     "이미 그린 조각을 옮겨 겹치는 것이 <b>컴포지팅</b>(compositing)입니다. "
     "읽기와 쓰기가 번갈아 일어나 배치가 되풀이되는 것을 <b>레이아웃 스래싱</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>GPU 가속</b> — <code>transform</code>이 빠른 것은 가속 때문만이 아니라 <b>배치를 건너뛰기</b> 때문입니다.<br>"
     "<b>FPS</b> — 초당 프레임 수는 결과이고, 원인은 <b>프레임 하나에 든 시간</b>입니다.<br>"
     "<b>최적화</b> — 이건 최적화가 아니라 <b>처음부터 맞게 쓰는</b> 문제입니다."),
  ]),
  axes=ax("무엇을 움직이나"),
  oneline="<b>움직일 때는 <code>transform</code>, 사라질 때는 <code>opacity</code>.</b> 이 둘로 안 되는 움직임은 대개 설계를 다시 보는 게 빠릅니다.",
  s4_title="속성별 비용", s4_hint="어느 단계부터 다시 하나",
  states=states([
    (band("transform", PIPE(1, 0, 0, 1), "배치 · 칠하기 건너뜀 — 가장 싸다"), "자리 옮기기", "<code>translate</code>·<code>scale</code>·<code>rotate</code>"),
    (band("opacity", PIPE(1, 0, 0, 1), "같은 길. 투명도만 바꾼다"), "사라지기", "<b>페이드</b>에 쓰는 바로 그것"),
    (band("color · background", PIPE(1, 0, 3, 1), "다시 칠한다 — 중간", 2), "색 바뀜", "자리는 그대로지만 칠은 다시 한다"),
    (band("box-shadow · filter", PIPE(1, 0, 3, 1), "넓은 영역을 다시 칠한다", 2), "그림자 · 흐림", "면적이 넓어 생각보다 비싸다"),
    (band("left · top · margin", PIPE(1, 2, 2, 1), "배치부터 전부 다시 — 가장 비싸다", True), "자리 바꾸기", "<b>같은 결과를 transform 으로</b> 낼 수 있다"),
    (band("width · height · font-size", PIPE(1, 2, 2, 1), "형제들 자리까지 흔든다", True), "크기 바꾸기", "<b>scale</b>로 대신할 수 있는지 먼저 본다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("네 단계", "스타일 → 배치 → 칠하기 → 합치기", "뒤로 갈수록 싸다. <b>어디서 끼어드느냐</b>가 비용이다"),
    ("가장 싼 둘", "transform · opacity", "스타일만 바꾸고 <b>합치기로 건너뛴다</b>"),
    ("중간", "색 · 그림자", "자리는 그대로지만 <b>다시 칠해야</b> 한다"),
    ("가장 비싼 것", "left · width · margin", "그 줄 전체, 때로는 문서 전체를 <b>다시 잰다</b>"),
    ("예산", "16.7ms", "60fps 기준 한 프레임. 여기서 <b>브라우저 몫도</b> 빼야 한다"),
    ("쓰고 바로 읽기", "layout thrashing", "<code>el.style.width=…; el.offsetWidth</code> — 그 줄에서 배치가 <b>즉시</b> 돈다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>읽기와 쓰기를 섞지 않는 것</b>이 두 번째 규칙입니다.
          반복문 안에서 <code>style.left</code>를 쓰고 바로 <code>offsetLeft</code>를 읽으면,
          브라우저는 정확한 값을 주려고 <b>그 자리에서 배치를 다시</b> 합니다 —
          100개면 배치가 100번 돕니다.
          <b>읽을 것을 먼저 다 읽고, 쓸 것을 나중에 다 쓰면</b> 한 번으로 끝납니다.</p>''',
  do=ul([
    "자리 옮김은 <code>transform: translate()</code>",
    "크기 변화는 <code>scale()</code>로 대신할 수 있는지 먼저 보기",
    "나타남·사라짐은 <code>opacity</code>",
    "읽기를 먼저 몰아 하고 <b>쓰기를 나중에</b>",
  ]),
  dont=ul([
    "<code>left</code>·<code>top</code>으로 애니메이션 — 같은 결과를 더 비싸게 낸다",
    "<code>width</code>를 매 프레임 — 형제들 자리까지 흔든다",
    "반복문 안에서 <b>쓰고 바로 읽기</b>",
    "<code>will-change</code>를 아무 데나 — 레이어가 늘면 <b>메모리를 먹는다</b>",
  ]),
  instead='긴 목록이 무거우면 <a href="virtual.html">가상 스크롤</a>, 그림이 무거우면 크기를 줄이기, 애니메이션이 많으면 <a href="reducedmotion.html">모션 줄이기</a>부터 챙기기.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--danger)">left: 0 → 200px</span>
                <span style="color:var(--accent)">transform: translateX(200px)</span>
                <span style="color:var(--fg-muted)">같은 결과, 다른 값</span>
              </div>''',
     "자리 옮김", "결과가 같으면 <b>싼 쪽</b>을 고른다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--danger)">height: 0 → auto <span style="color:var(--fg-muted)">(안 된다)</span></span>
                <span style="color:var(--accent)">grid-template-rows: 0fr → 1fr</span>
              </div>''',
     "펼치기", "<code>auto</code>로는 전환이 안 돼 오래 꼼수를 썼다. 요즘은 <b>격자 비율</b>로 한다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--fg-muted)">// 읽기를 먼저</span>
                <span>const ws = els.map(e =&gt; e.offsetWidth);</span>
                <span style="color:var(--fg-muted)">// 쓰기를 나중에</span>
                <span>els.forEach((e,i) =&gt; e.style.transform = …);</span>
              </div>''',
     "읽기와 쓰기 가르기", "배치가 <b>100번에서 한 번</b>이 된다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 성능의 계약서",
  code_lede="움직임은 <code>transform</code>·<code>opacity</code>로 적고, 읽기와 쓰기를 가릅니다.",
  code='''<span class="c">/* 싼 쪽 */</span>
.card { <span class="a">transition</span>: transform <span class="a">220ms</span> <span class="a">var</span>(--ease-out), opacity <span class="a">160ms</span> linear; }
.card.out { <span class="a">transform</span>: translateY(<span class="a">8px</span>); <span class="a">opacity</span>: <span class="a">0</span>; }

<span class="c">/* 펼치기 — height: auto 는 전환이 안 된다 */</span>
.acc { <span class="a">display</span>: grid; <span class="a">grid-template-rows</span>: <span class="a">0fr</span>; <span class="a">transition</span>: grid-template-rows <span class="a">220ms</span>; }
.acc[open] { <span class="a">grid-template-rows</span>: <span class="a">1fr</span>; }
.acc &gt; div { <span class="a">overflow</span>: hidden; }

<span class="c">// 읽기를 먼저, 쓰기를 나중에</span>
<span class="k">const</span> tops = items.map(el =&gt; el.getBoundingClientRect().top);   <span class="c">// 읽기</span>
items.forEach((el, i) =&gt; { el.style.transform = <span class="s">`translateY(${</span>tops[i]<span class="s">}px)`</span>; });  <span class="c">// 쓰기</span>''',
  keys=kbd([
    ("<code>will-change</code>는 <b>미리</b>, 그리고 <b>치운다</b>", "움직이기 직전에 켜고 끝나면 지운다. 늘 켜 두면 레이어가 쌓인다"),
    ("<code>transform</code>은 <b>새 기준</b>을 만든다", "자식의 <code>position:fixed</code>가 화면이 아니라 <b>이 상자</b>를 따르게 된다"),
    ("<code>opacity</code>도 쌓임 맥락을 만든다", "<a href=\"../items/zindex.html\">z-index</a>가 안 먹는 흔한 이유다"),
    ("<code>content-visibility: auto</code>", "화면 밖 덩어리를 안 그린다. 긴 문서에 효과가 크다"),
    ("<code>@media (prefers-reduced-motion)</code>", "비싼 애니메이션일수록 <b>줄이기에서 먼저</b> 끈다"),
    ("재는 법", "개발자 도구의 성능 탭에서 <b>보라색(배치)·초록색(칠하기)</b> 띠를 본다"),
  ]),
  backend=rows([
    ("느린 쪽이 어디인지", "'화면이 버벅인다'의 원인은 서버일 수도 그리기일 수도 있습니다. <b>응답 시간과 프레임 시간</b>을 따로 재야 갈립니다."),
    ("한 번에 밀어 넣는 양", "서버가 2,000건을 한 번에 주면 그리는 쪽이 멎습니다. <b>쪽을 나누거나</b> <a href=\"virtual.html\">가상 스크롤</a>로 받습니다."),
    ("이미지 크기", "원본 2000px 이미지를 100px 자리에 넣으면 칠하기가 비쌉니다. <b>서버에서 줄여</b> 보냅니다."),
    ("실사용자 측정", "개발 기기는 빠릅니다. <b>INP</b> 같은 실사용자 지표를 모아 보면 느린 기기의 사정이 드러납니다."),
  ]),
  plat_lede="<b>어디서나 같은 규칙</b>입니다 — 자리를 다시 재게 하지 마라.",
  plats=plats([
    ("웹", "transform · opacity",
     band("transform", PIPE(1, 0, 0, 1), "", False, "105px"),
     "브라우저가 네 단계를 돕니다. 개발자 도구에서 <b>어느 단계가 걸렸는지</b> 색으로 볼 수 있습니다."),
    ("iOS", "Core Animation",
     '''              <div class="phone" role="img" aria-label="iOS 레이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:30px;width:26px;height:26px;border-radius:5px;background:var(--accent)"></div></div></div>''',
     "레이어를 옮기는 일은 <b>GPU 몫</b>입니다. 반면 <code>cornerRadius</code>·그림자는 오프스크린 칠하기를 부릅니다."),
    ("안드로이드", "View · Compose",
     '''              <div class="phone" role="img" aria-label="안드로이드 레이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:30px;width:26px;height:26px;border-radius:5px;background:var(--accent)"></div></div></div>''',
     "<code>translationX</code>는 싸고 <code>layout()</code>을 부르는 변경은 비쌉니다. Compose 도 같은 갈래입니다."),
  ]),
  plat_note="\"애니메이션이 끊겨요\"를 받으면 <b>무엇을 바꾸고 있는지</b>부터 봅니다. <code>left</code>나 <code>width</code>를 매 프레임 바꾸고 있다면 기기를 탓할 일이 아니고, <code>transform</code>으로 바꾸는 것만으로 해결되는 경우가 많습니다. 라이브러리를 바꾸는 것보다 <b>속성 두 개를 바꾸는 쪽</b>이 거의 늘 빠릅니다.",
  siblings=siblings("cheap"),
  related='''        <li><a href="virtual.html"><b>가상 스크롤</b><em>10부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
