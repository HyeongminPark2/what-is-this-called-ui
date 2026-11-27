# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def grid(px, w="150px", note="", warn=False, blur=False):
    cells = ''
    n = 6
    for y in range(3):
        for x in range(n):
            on = (x + y) % 2 == 0
            cells += ('<span style="background:' + ('var(--accent)' if on else 'transparent') + '"></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;grid-template-columns:repeat(' + str(n) + ',1fr);grid-auto-rows:' + str(px) + 'px;'
            'border:1px solid var(--line);border-radius:5px;overflow:hidden;background:var(--bg);'
            + ('filter:blur(1.1px);' if blur else '') + '">' + cells + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

def lines(thick, note, w="150px", warn=False):
    bars = ''.join('<span style="display:block;height:' + thick + ';background:var(--fg);margin:7px 0"></span>' for _ in range(3))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:5px;background:var(--bg);padding:5px 8px">' + bars + '</div>'
            '<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">CSS 1px은 화소가 아닌 길이 단위</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">devicePixelRatio가 3이면 기기 화소 3개가 CSS 1px</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">그림에는 CSS 크기 × 배율만큼의 화소가 필요함</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">srcset의 2x·3x로 배율에 맞는 그림을 받음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">SVG와 글자는 배율과 상관없음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">머리카락 선의 굵기는 1 ÷ 배율 px</div>
                </div>
              </div>'''

D = dict(
  slug="dpr", ko="화면 밀도", en="Device pixel ratio",
  desc="CSS의 1px이 화소가 아니라 길이 단위라는 점과, 화면 배율에 따라 그림을 몇 배 크기로 받아야 하는지, 머리카락처럼 가는 선은 어떻게 긋는지를 보여 주는 항목입니다.",
  lede="<b>CSS의 1px은 화소가 아니라 길이 단위입니다.</b> 그래서 배율이 3배인 화면에서는 CSS 1px 길이를 기기 화소 세 개로 그립니다.",
  axes_lede="PC와 폰은 기계보다 <b>쓰는 전제</b>가 다릅니다. 아래 네 가지로 두 환경을 견줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>배율을 바꾸면 캔버스의 <b>실제 화소 수</b>가 함께 바뀝니다.<br>
          <b>1배짜리 그림</b>은 3배 화면에서 세 배로 늘어나 뭉개지지만, <b>배율만큼 크게 받은 그림</b>과
          <b>SVG</b>는 선명하게 그대로 보입니다. 아래 두 줄은 <code>1px</code> 선과 <b>화소 하나짜리</b> 선을 비교한 것으로,
          배율이 높을수록 화소 하나짜리 선이 가늘어집니다. 위쪽에는 지금 보는 화면의 실제 배율도 나옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "화면 밀도, 픽셀 배율, 고해상도 화면"),
    ("영어", "device pixel ratio (DPR), pixel density, Retina / HiDPI"),
    ("같이 쓰는 말",
     "브라우저는 배율을 <code>window.devicePixelRatio</code> 값으로 알려 줍니다. "
     "배율이 높은 화면을 애플은 <b>레티나</b>라고 부르고, 일반적으로는 <b>HiDPI</b>라고 부릅니다. "
     "그림을 배율별로 나눠 줄 때는 <code>srcset</code>에 <b>1x · 2x · 3x</b>를 적고, "
     "화소 하나 굵기로 그은 선은 <b>헤어라인</b>(hairline)이라고 합니다. "
     "안드로이드의 길이 단위 <b>dp</b>와 애플의 <b>pt</b>는 CSS의 px과 같은 역할을 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>해상도</b> — '1920×1080'은 화면 전체의 화소 수이고, 밀도는 <b>화소가 얼마나 빽빽하게 들어 있는가</b>를 가리킵니다.<br>"
     "<b>화면 크기</b> — <a href=\"breakpoint.html\">브레이크포인트</a>가 기준으로 삼는 폭은 <b>CSS px</b>로 재기 때문에 밀도와 상관이 없습니다.<br>"
     "<b>DPI</b> — 인쇄에서 쓰는 단위이고, 화면에서는 밀도를 배율로 다룹니다."),
  ]),
  axes=ax("화면 밀도"),
  oneline="<b>선과 글자는 브라우저가 배율에 맞춰 그려 주지만, 비트맵 그림은 그렇지 않습니다.</b> 그래서 화면 밀도 때문에 챙길 일은 거의 전부 <b>그림</b>에 관한 것입니다.",
  s4_title="배율에 따라 달라지는 것", s4_hint="배율에 따라 바뀌는 것과 바뀌지 않는 것",
  do_title="화면 밀도를 챙겨야 하는 경우",
  dont_title="화면 밀도를 잘못 다루는 경우",
  instead_title="함께 살펴볼 것",
  states=states([
    (grid(9, "150px", "1배는 화소와 CSS px이 같음"), "배율이 1배일 때", "예전 모니터의 배율입니다. 지금은 드뭅니다"),
    (grid(9, "150px", "2배는 같은 자리에 화소가 네 배"), "배율이 2배일 때", "대부분의 노트북이 2배입니다. 화소는 네 배지만 <b>눈에 보이는 크기는 같습니다</b>"),
    (grid(9, "150px", "3배는 화소가 아홉 배"), "배율이 3배일 때", "요즘 폰의 배율입니다. 그림을 가로세로 <b>세 배 크기로 받아야</b> 선명합니다"),
    (grid(9, "150px", "1배 그림을 3배 화면에 넣으면 뭉개짐", True, True), "그림을 배율에 맞추지 않았을 때", "그림이 흐릿해집니다. <b>가장 흔하게 일어나는 실수</b>입니다"),
    (lines("1px", "CSS 1px은 어느 배율에서나 같은 굵기"), "1px로 그은 선", "브라우저가 <b>배율에 맞게 화소 수를 맞춰</b> 그립니다"),
    (lines("0.5px", "화소 하나 굵기라 배율이 높을수록 가늘어짐"), "머리카락처럼 가는 선", "굵기를 <b>1 ÷ 배율</b> px로 잡은 선입니다. iOS의 구분선이 이 굵기입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("CSS px", "길이 단위", "어느 화면에서나 <b>눈에 같은 크기</b>로 보이도록 정한 길이 단위입니다"),
    ("배율", "devicePixelRatio", "CSS 1px을 기기 화소 <b>몇 개</b>로 그리는지 나타내는 값입니다"),
    ("그림에 필요한 화소", "CSS 크기 × 배율", "폭 100px 자리에 배율 3배라면 폭 <b>300화소</b>짜리 그림이 필요합니다"),
    ("배율별로 주기", "srcset 1x 2x 3x", "브라우저가 <b>화면 배율에 맞는 그림</b> 하나만 골라 받습니다"),
    ("배율과 무관한 것", "SVG · 글자", "그릴 때마다 배율에 맞춰 다시 계산하기 때문에 <b>늘 선명합니다</b>"),
    ("머리카락 선", "1 ÷ 배율 px", "배율 3배 화면에서는 <code>0.33px</code>이 정확히 화소 하나입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          어디서나 선명하게 보이도록 모든 그림을 3배짜리로만 주는 <b>반대 방향의 실수</b>도 흔합니다.
          그러면 1배 모니터에서도 <b>화소 수가 아홉 배인 그림</b>을 받게 되고,
          화면에 그릴 때 크기를 줄이는 작업까지 더해져 오히려 느려집니다.
          <code>srcset</code>에 여러 크기를 적어 두면 브라우저가 <b>화면 배율과 통신 사정</b>을 보고
          알맞은 것을 고르므로, 어떤 그림을 받을지는 브라우저에 맡기는 편이 낫습니다.</p>''',
  do=ul([
    "사진이나 비트맵 아이콘을 넣을 때. <code>srcset</code>을 적습니다",
    "아이콘을 넣을 때. 되도록 <b>SVG</b>나 아이콘 글꼴을 씁니다",
    "캔버스로 그릴 때. 캔버스를 <b>배율만큼 크게</b> 잡고 줄여서 보여 줍니다",
  ]),
  dont=ul([
    "모든 그림을 3배짜리로만 줄 때. <b>1배 기기</b>가 필요 없이 큰 파일을 받습니다",
    "<code>devicePixelRatio</code>로 <b>기기를 짐작</b>할 때. 서로 다른 기기가 같은 값을 냅니다",
    "선 굵기를 배율로 계산할 때. <b>1px 선은 브라우저가 이미 맞춰</b> 그립니다",
    "글자 크기를 배율에 따라 바꿀 때. 글자는 배율과 상관없이 선명하므로 바꿀 필요가 없습니다",
  ]),
  instead='화면 폭에 따라 배치를 바꾸는 일은 <a href="breakpoint.html">브레이크포인트</a>에서 다룹니다. 그림이 무거우면 배율보다 먼저 포맷(WebP·AVIF)을 바꿔 보고, 아이콘은 처음부터 SVG로 만듭니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>&lt;img</span>
                <span>&nbsp;&nbsp;src="logo.png"</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">srcset="logo@2x.png 2x,</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">&nbsp;&nbsp;logo@3x.png 3x"&gt;</span></span>
              </div>''',
     "배율별로 그림 나눠 주기", "브라우저가 화면 배율에 맞는 그림 <b>하나만</b> 받습니다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>cv.width = w * <span style="color:var(--accent)">dpr</span>;</span>
                <span>cv.style.width = w + 'px';</span>
                <span>ctx.scale(<span style="color:var(--accent)">dpr, dpr</span>);</span>
              </div>''',
     "캔버스를 배율에 맞추기", "이렇게 맞추지 않으면 화면에서 <b>캔버스만 흐릿하게</b> 보입니다"),
    (lines("0.5px", "border-width: 0.5px는 3배에서 화소 하나", "150px"),
     "가는 구분선 긋기", "iOS 구분선 같은 <b>가는 선</b>을 긋습니다. 1배 화면에서는 흐려질 수 있습니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="그림은 <code>srcset</code>으로 배율별 파일을 주고, 캔버스는 배율을 읽어 화소 수를 직접 맞춥니다.",
  code='''&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"logo.png"</span>
     <span class="a">srcset</span>=<span class="s">"logo@2x.png 2x, logo@3x.png 3x"</span>
     <span class="a">width</span>=<span class="s">"120"</span> <span class="a">height</span>=<span class="s">"40"</span> <span class="a">alt</span>=<span class="s">"이름표"</span>&gt;

<span class="c">/* 폭까지 다를 때는 sizes 와 w 서술자로 */</span>
&lt;<span class="t">img</span> <span class="a">srcset</span>=<span class="s">"c-400.jpg 400w, c-800.jpg 800w, c-1200.jpg 1200w"</span>
     <span class="a">sizes</span>=<span class="s">"(min-width: 900px) 33vw, 100vw"</span> <span class="a">src</span>=<span class="s">"c-800.jpg"</span>&gt;

<span class="c">// 캔버스는 직접 맞춘다</span>
<span class="k">const</span> dpr = window.devicePixelRatio || <span class="a">1</span>;
cv.width = w * dpr; cv.height = h * dpr;      <span class="c">// 그리는 화소 수</span>
cv.style.width = w + <span class="s">'px'</span>;                  <span class="c">// 보이는 크기</span>
ctx.scale(dpr, dpr);''',
  keys=kbd([
    ("<code>width</code>·<code>height</code> 적기", "밀도와는 별개로, 그림이 들어갈 <b>자리를 미리 잡아</b> 그림이 늦게 뜰 때 글이 밀려 움직이지 않게 합니다"),
    ("<code>srcset</code>의 <code>2x</code>와 <code>800w</code> 구분하기", "배율만 다르면 <code>x</code>를 쓰고, <b>표시 폭도 달라지면</b> <code>w</code>와 <code>sizes</code>를 함께 씁니다"),
    ("<code>alt</code> 함께 적기", "밀도와는 상관없지만 그림을 넣을 때 <b>함께 빠뜨리기 쉽습니다</b>. <a href=\"../items/name.html\">이름 붙이기</a>를 참고합니다"),
    ("<code>image-rendering: pixelated</code>", "도트 그림처럼 화소를 일부러 살릴 때만 씁니다. <b>사진에 쓰면 오히려 거칠어집니다</b>"),
    ("<code>0.5px</code> 테두리", "1배 화면에서는 굵기가 반올림되어 <b>사라지거나 흐려질 수</b> 있으므로, 배율을 묻는 미디어 쿼리로 배율이 높은 화면에만 적용합니다"),
    ("배율로 기기를 짐작하지 않기", "같은 배율 값이 폰에도 노트북에도 있습니다. 입력 방식이 궁금하면 <a href=\"hover.html\">포인터 질의</a>로 묻습니다"),
  ]),
  backend=rows([
    ("그림 크기 변환은 서버에서 하기", "원본 하나만 올려 두고 서버가 <b>필요한 크기로 줄여</b> 내려주게 하면, 크기별 파일을 따로 관리하는 것보다 비용이 적게 듭니다."),
    ("기기별 그림과 CDN 캐시", "같은 주소에서 기기마다 다른 그림을 내려주면 CDN 캐시가 엉뚱한 그림을 돌려줄 수 있습니다. 그래서 <b>크기마다 주소를 따로</b> 두는 편이 안전합니다."),
    ("배율보다 먼저 살펴볼 그림 포맷", "같은 그림이라도 WebP나 AVIF로 바꾸면 파일 크기가 절반 아래로 줄어듭니다. 그래서 그림이 무거우면 <b>배율보다 포맷을 먼저</b> 살펴봅니다."),
    ("업로드한 사진은 줄여서 저장하기", "요즘 폰으로 찍은 사진은 폭이 4000px을 넘습니다. 업로드를 받자마자 <b>화면에 쓸 크기로 줄여</b> 저장해 두지 않으면, 사진이 여러 장 뜨는 목록 화면 전체가 느려집니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>길이 단위와 기기 화소를 나눠</b> 다루고, 부르는 이름만 다릅니다.",
  plats=plats([
    ("웹", "CSS px · DPR",
     grid(7, "105px", "CSS px"),
     "<code>px</code>이 길이 단위이고 <code>devicePixelRatio</code>가 배율입니다. 그림은 <code>srcset</code>으로 배율별로 나눠 줍니다."),
    ("iOS", "pt · @2x @3x",
     '''              <div class="phone" role="img" aria-label="iOS 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;font-size:6px;color:var(--fg-muted)">icon@2x<br>icon@3x</div></div></div>''',
     "길이 단위는 <b>pt</b>이고, 배율별 그림은 파일 이름에 <code>@2x</code>·<code>@3x</code>를 붙여 구분합니다. 구분선은 <b>화소 하나</b> 굵기로 긋는 것이 관례입니다."),
    ("안드로이드", "dp · mdpi~xxxhdpi",
     '''              <div class="phone" role="img" aria-label="안드로이드 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;font-size:6px;color:var(--fg-muted)">drawable-xhdpi<br>drawable-xxhdpi</div></div></div>''',
     "길이 단위는 <b>dp</b>이고, 배율별 그림은 폴더 이름으로 구분합니다. 벡터 드로어블을 쓰면 그림 한 벌로 모든 배율을 처리할 수 있습니다."),
  ]),
  plat_note="\"로고가 흐릿해요\"라는 문의는 거의 늘 배율에 맞는 그림을 주지 않아서 생깁니다. 게다가 디자이너와 개발자의 화면이 <b>둘 다 2배</b>인 경우가 많아서, 만드는 동안에는 문제를 못 보고 지나가기 쉽습니다. 시안을 받을 때 <b>2배·3배 파일을 함께</b> 달라고 하거나 처음부터 SVG로 받아 두면, 나중에 파일을 다시 주고받을 일이 없어집니다.",
  siblings=siblings("dpr"),
  related='''        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>''',
)
