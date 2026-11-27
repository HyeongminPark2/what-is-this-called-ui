# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">transform과 opacity는 배치와 칠하기를 건너뜀</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">color와 box-shadow는 다시 칠함</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">left·width·margin은 배치부터 다시 함</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한 프레임에 쓸 수 있는 시간은 16.7ms</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">쓰고 바로 읽으면 그 자리에서 배치를 계산함</div>
                </div>
              </div>'''

D = dict(
  slug="cheap", ko="무엇을 움직이나", en="Cheap vs expensive properties",
  desc="transform과 opacity는 배치를 다시 계산하지 않지만 left와 width는 다시 계산합니다. 화면이 버벅이는 원인 대부분이 이 차이에서 나온다는 것을 보여 주는 항목입니다.",
  lede="같은 움직임이라도 <b>어떤 속성을 바꾸느냐</b>에 따라 브라우저가 치르는 비용이 다릅니다. 움직임이 버벅이는 원인은 대부분 여기에 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 가지 방법으로 같은 거리를 움직이면서 <b>한 프레임을 만드는 데 걸린 시간</b>을 잽니다.<br>
          상자 수를 늘리면 차이가 벌어지는데, <code>transform</code>과 <code>opacity</code>는
          시간이 거의 그대로인 반면 <code>left</code>와 <code>width</code>는 상자 수와 함께 늘어납니다.
          이렇게 늘어난 시간이 화면에서는 <b>버벅임</b>으로 나타납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "리플로우, 리페인트, 합성, 레이어"),
    ("영어", "reflow / layout, repaint, compositing, GPU acceleration"),
    ("같이 쓰는 말",
     "요소의 자리와 크기를 다시 계산하는 것을 <b>리플로우</b>(reflow) 또는 <b>레이아웃</b>, "
     "픽셀을 다시 칠하는 것을 <b>리페인트</b>(repaint) 또는 <b>페인트</b>, "
     "이미 그린 조각을 옮겨 겹치는 것을 <b>컴포지팅</b>(compositing)이라고 합니다. "
     "값을 읽고 쓰는 일이 번갈아 일어나 배치 계산이 되풀이되는 현상은 <b>레이아웃 스래싱</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>GPU 가속</b> — <code>transform</code>이 빠른 것은 GPU 가속 때문만이 아니라 <b>배치 계산을 건너뛰기</b> 때문입니다.<br>"
     "<b>FPS</b> — 초당 프레임 수는 결과로 나타나는 숫자이고, 그 원인은 <b>프레임 하나를 만드는 데 든 시간</b>입니다.<br>"
     "<b>최적화</b> — 속성을 고르는 일은 나중에 하는 최적화가 아니라 <b>처음부터 맞게 써야</b> 하는 기본입니다."),
  ]),
  s4_title="속성마다 다른 비용", s4_hint="속성을 바꿨을 때 어느 단계부터 다시 하는지",
  states=states([
    (band("transform", PIPE(1, 0, 0, 1), "배치와 칠하기를 건너뛰어 가장 쌈"), "transform으로 자리 옮기기", "<code>translate</code>·<code>scale</code>·<code>rotate</code>로 자리와 크기, 각도를 바꿉니다"),
    (band("opacity", PIPE(1, 0, 0, 1), "투명도만 바꿔 같은 단계를 거침"), "opacity로 사라지게 하기", "<b>페이드</b> 효과에 쓰는 속성입니다"),
    (band("color · background", PIPE(1, 0, 3, 1), "다시 칠해서 비용은 중간", 2), "색을 바꿀 때", "자리는 그대로지만 픽셀은 다시 칠합니다"),
    (band("box-shadow · filter", PIPE(1, 0, 3, 1), "넓은 영역을 다시 칠함", 2), "그림자나 흐림을 바꿀 때", "다시 칠하는 면적이 넓어서 생각보다 비용이 큽니다"),
    (band("left · top · margin", PIPE(1, 2, 2, 1), "배치부터 다시 해서 가장 비쌈", True), "left·top으로 자리 바꾸기", "<b>같은 결과를 transform으로</b> 낼 수 있습니다"),
    (band("width · height · font-size", PIPE(1, 2, 2, 1), "옆 요소 자리까지 다시 계산함", True), "width·height로 크기 바꾸기", "<b>scale</b>로 대신할 수 있는지 먼저 따져 봅니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("네 단계", "스타일 → 배치 → 칠하기 → 합치기", "뒤 단계일수록 비용이 적습니다. 속성을 바꿨을 때 <b>어느 단계부터 다시 하느냐</b>가 비용을 정합니다"),
    ("비용이 가장 적은 두 속성", "transform · opacity", "스타일만 바꾸고 배치와 칠하기를 건너뛰어 <b>바로 합치기</b>로 갑니다"),
    ("비용이 중간인 속성", "색 · 그림자", "자리는 그대로지만 <b>다시 칠해야</b> 합니다"),
    ("비용이 가장 큰 속성", "left · width · margin", "그 줄 전체, 때로는 문서 전체의 자리를 <b>다시 계산합니다</b>"),
    ("한 프레임 예산", "16.7ms", "60fps 기준으로 한 프레임에 쓸 수 있는 시간입니다. 여기서 <b>브라우저가 쓰는 시간도</b> 빼야 합니다"),
    ("쓰고 바로 읽기", "layout thrashing", "<code>el.style.width=…; el.offsetWidth</code>처럼 쓰고 바로 읽으면 그 줄에서 배치 계산이 <b>즉시</b> 일어납니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          두 번째 규칙은 <b>읽기와 쓰기를 섞지 않는 것</b>입니다.
          반복문 안에서 <code>style.left</code>를 쓰고 바로 <code>offsetLeft</code>를 읽으면,
          브라우저는 정확한 값을 돌려주려고 <b>그 자리에서 배치를 다시</b> 계산합니다.
          그래서 요소가 100개면 배치 계산도 100번 일어납니다.
          반면 <b>읽을 값을 먼저 다 읽고 쓸 값을 나중에 다 쓰면</b> 배치 계산은 한 번으로 끝납니다.</p>''',
  do_title="비용이 적은 속성으로 움직이는 방법",
  dont_title="움직임을 만들 때 피할 속성과 습관",
  instead_title="속성을 바꿔도 화면이 무거울 때 살펴볼 것",
  do=ul([
    "자리를 옮길 때. <code>transform: translate()</code>를 씁니다",
    "크기를 바꿀 때. <code>scale()</code>로 대신할 수 있는지 먼저 봅니다",
    "나타나거나 사라질 때. <code>opacity</code>를 씁니다",
    "값을 여러 개 읽고 쓸 때. 읽기를 먼저 몰아서 하고 <b>쓰기는 나중에</b> 합니다",
  ]),
  dont=ul([
    "<code>left</code>·<code>top</code>으로 애니메이션할 때. <code>transform</code>과 같은 결과를 더 큰 비용으로 냅니다",
    "<code>width</code>를 매 프레임 바꿀 때. 옆에 있는 요소들의 자리까지 다시 계산됩니다",
    "반복문 안에서 값을 <b>쓰고 바로 읽을</b> 때",
    "<code>will-change</code>를 아무 데나 걸 때. 레이어가 늘어나면 그만큼 <b>메모리를 씁니다</b>",
  ]),
  instead='긴 목록 때문에 무거우면 <a href="virtual.html">가상 스크롤</a>을 쓰고, 그림이 무거우면 그림 크기를 줄입니다. 애니메이션이 많아서 무겁다면 <a href="reducedmotion.html">모션 줄이기</a>부터 살펴봅니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--danger)">left: 0 → 200px</span>
                <span style="color:var(--accent)">transform: translateX(200px)</span>
                <span style="color:var(--fg-muted)">결과는 같고 비용만 다름</span>
              </div>''',
     "자리를 옮길 때 속성 고르기", "결과가 같으면 <b>비용이 적은 쪽</b>을 고릅니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--danger)">height: 0 → auto <span style="color:var(--fg-muted)">(전환 안 됨)</span></span>
                <span style="color:var(--accent)">grid-template-rows: 0fr → 1fr</span>
              </div>''',
     "높이를 펼치는 방법", "높이를 <code>auto</code>로 두면 전환이 되지 않아서 오랫동안 우회하는 방법을 썼습니다. 요즘은 <b>격자 비율</b>을 바꿔서 펼칩니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;display:grid;gap:3px">
                <span style="color:var(--fg-muted)">// 읽기를 먼저</span>
                <span>const ws = els.map(e =&gt; e.offsetWidth);</span>
                <span style="color:var(--fg-muted)">// 쓰기를 나중에</span>
                <span>els.forEach((e,i) =&gt; e.style.transform = …);</span>
              </div>''',
     "읽기와 쓰기를 나눠 하기", "배치 계산이 <b>100번에서 한 번</b>으로 줄어듭니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="움직임은 <code>transform</code>과 <code>opacity</code>로 적고, 값을 읽는 코드와 쓰는 코드를 나눕니다.",
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
  keys_heads="<th>알아 둘 규칙</th><th>자세한 내용</th>",
  keys=kbd([
    ("<code>will-change</code>는 <b>미리</b> 켜고 <b>끝나면</b> 지우기", "움직이기 직전에 켜고 움직임이 끝나면 지웁니다. 늘 켜 두면 레이어가 계속 쌓입니다"),
    ("<code>transform</code>이 만드는 <b>새 기준</b>", "자식 요소의 <code>position:fixed</code>가 화면이 아니라 <b>이 상자</b>를 기준으로 자리를 잡습니다"),
    ("<code>opacity</code>가 만드는 쌓임 맥락", "<a href=\"../items/zindex.html\">z-index</a>가 듣지 않을 때 흔히 이것이 원인입니다"),
    ("<code>content-visibility: auto</code>", "화면 밖에 있는 덩어리는 그리지 않습니다. 긴 문서에서 효과가 큽니다"),
    ("<code>@media (prefers-reduced-motion)</code>", "비용이 큰 애니메이션일수록 <b>모션 줄이기 설정에서 먼저</b> 끕니다"),
    ("비용을 재는 방법", "개발자 도구의 성능 탭에서 <b>보라색(배치)·초록색(칠하기)</b> 띠가 얼마나 긴지 봅니다"),
  ]),
  backend=rows([
    ("느린 쪽이 서버인지 화면인지 가리기", "화면이 버벅일 때 원인은 서버일 수도 있고 화면을 그리는 쪽일 수도 있습니다. <b>응답 시간과 프레임 시간</b>을 따로 재야 어느 쪽인지 가릴 수 있습니다."),
    ("한 번에 보내는 데이터 양", "서버가 2,000건을 한 번에 보내면 화면을 그리는 동안 브라우저가 멈춥니다. 그래서 <b>페이지를 나눠 받거나</b> <a href=\"virtual.html\">가상 스크롤</a>을 씁니다."),
    ("이미지를 서버에서 줄여 보내기", "원본 2000px 이미지를 100px 자리에 넣으면 칠하는 비용이 커집니다. 이미지는 <b>서버에서 줄여</b> 보냅니다."),
    ("실제 사용자 기기에서 재기", "개발자가 쓰는 기기는 대개 빠릅니다. <b>INP</b> 같은 실사용자 지표를 모아 보면 느린 기기에서 실제로 얼마나 걸리는지 알 수 있습니다."),
  ]),
  plat_lede="플랫폼이 달라도 <b>자리를 다시 계산하게 하지 않는다</b>는 규칙은 같습니다.",
  plats=plats([
    ("웹", "transform · opacity",
     band("transform", PIPE(1, 0, 0, 1), "", False, "105px"),
     "브라우저가 네 단계를 거쳐 화면을 그립니다. 개발자 도구에서 <b>어느 단계에 시간이 걸렸는지</b> 색으로 볼 수 있습니다."),
    ("iOS", "Core Animation",
     '''              <div class="phone" role="img" aria-label="iOS 레이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:30px;width:26px;height:26px;border-radius:5px;background:var(--accent)"></div></div></div>''',
     "레이어를 옮기는 일은 <b>GPU가 맡습니다</b>. 반면 <code>cornerRadius</code>와 그림자는 화면 밖에서 따로 칠하는 오프스크린 렌더링을 일으킵니다."),
    ("안드로이드", "View · Compose",
     '''              <div class="phone" role="img" aria-label="안드로이드 레이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:30px;width:26px;height:26px;border-radius:5px;background:var(--accent)"></div></div></div>''',
     "<code>translationX</code>는 비용이 적고 <code>layout()</code>을 부르는 변경은 비용이 큽니다. Compose도 마찬가지입니다."),
  ]),
  plat_note="\"애니메이션이 끊겨요\"라는 신고를 받으면 애니메이션이 <b>어떤 속성을 바꾸고 있는지</b>부터 봅니다. <code>left</code>나 <code>width</code>를 매 프레임 바꾸고 있다면 기기 성능 문제가 아니고, <code>transform</code>으로 바꾸는 것만으로 해결되는 경우가 많습니다. 애니메이션 라이브러리를 바꾸는 것보다 <b>속성 두 개를 바꾸는 편</b>이 대부분 더 빨리 해결됩니다.",
  siblings=siblings("cheap"),
  related='''        <li><a href="virtual.html"><b>가상 스크롤</b><em>10부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
