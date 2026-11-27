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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">CSS 1px — 길이 단위다. 화소가 아니다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">devicePixelRatio = 3 — 기기 화소 3개가 CSS 1px</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">그림은 CSS 크기 × 배율 만큼의 화소가 필요하다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">srcset · 2x · 3x — 그 배율에 맞는 것을 받는다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">SVG · 글자는 배율과 상관없다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">머리카락 선 = 1 ÷ 배율 px</div>
                </div>
              </div>'''

D = dict(
  slug="dpr", ko="화면 밀도", en="Device pixel ratio",
  desc="CSS 1px은 길이이지 화소가 아니다. 배율에 따라 그림을 몇 배로 받아야 하는지, 머리카락 선은 어떻게 긋는지.",
  lede="<b>CSS 의 1px 은 길이 단위이지 화소가 아닙니다.</b> 배율 3배 화면에서는 화소 세 개로 그려집니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>배율을 바꾸면 캔버스의 <b>실제 화소 수</b>가 함께 바뀝니다.<br>
          <b>1배짜리 그림</b>은 3배 화면에서 세 배로 늘어나 뭉개지고, <b>배율만큼 받은 그림</b>과
          <b>SVG</b>는 그대로입니다. 아래 두 줄은 <code>1px</code> 선과 <b>화소 하나짜리</b> 선의 차이입니다 —
          배율이 높을수록 화소 하나는 가늘어집니다. 위에 이 화면의 실제 배율도 나옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "화면 밀도, 픽셀 배율, 고해상도 화면"),
    ("영어", "device pixel ratio (DPR), pixel density, Retina / HiDPI"),
    ("같이 쓰는 말",
     "브라우저가 알려 주는 값이 <code>window.devicePixelRatio</code>이고, "
     "애플은 <b>레티나</b>, 일반적으로는 <b>HiDPI</b>라 부릅니다. "
     "그림을 배율별로 주는 것이 <code>srcset</code>의 <b>1x · 2x · 3x</b>이고, "
     "화소 하나 굵기의 선을 <b>헤어라인</b>(hairline)이라 합니다. "
     "안드로이드의 길이 단위 <b>dp</b>, 애플의 <b>pt</b>가 CSS 의 px 과 같은 자리입니다."),
    ("자주 잘못 부름",
     "<b>해상도</b> — '1920×1080'은 화소 수이고, 밀도는 <b>그 화소가 얼마나 빽빽한가</b>입니다.<br>"
     "<b>화면 크기</b> — <a href=\"breakpoint.html\">브레이크포인트</a>가 보는 폭은 <b>CSS px</b>이라 밀도와 무관합니다.<br>"
     "<b>DPI</b> — 인쇄의 단위입니다. 화면에서는 배율로 다룹니다."),
  ]),
  axes=ax("화면 밀도"),
  oneline="<b>선은 저절로 맞고, 그림은 저절로 안 맞습니다.</b> 밀도 때문에 할 일은 거의 전부 <b>그림</b>에 관한 것입니다.",
  s4_title="배율에 따라", s4_hint="무엇이 바뀌고 무엇이 안 바뀌나",
  states=states([
    (grid(9, "150px", "1배 — 화소와 CSS px 이 같다"), "1배", "옛날 모니터. 지금은 드물다"),
    (grid(9, "150px", "2배 — 같은 자리에 화소 네 배"), "2배", "노트북 대부분. <b>보기엔 같다</b>"),
    (grid(9, "150px", "3배 — 화소 아홉 배"), "3배", "요즘 폰. 그림은 <b>세 배로 받아야</b> 한다"),
    (grid(9, "150px", "1배 그림을 3배 화면에 — 뭉갠다", True, True), "안 맞췄을 때", "흐릿해진다. <b>가장 흔한 사고</b>"),
    (lines("1px", "CSS 1px — 어느 배율에서나 같은 굵기"), "선 — 1px", "브라우저가 <b>알아서 화소를 맞춘다</b>"),
    (lines("0.5px", "화소 하나 — 배율이 높을수록 가늘다"), "선 — 머리카락", "<b>1 ÷ 배율</b> px. iOS 의 구분선이 이것이다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("CSS px", "길이 단위", "어느 화면에서나 <b>눈에 같은 크기</b>로 보이게 정한 단위"),
    ("배율", "devicePixelRatio", "CSS 1px 을 기기 화소 <b>몇 개</b>로 그리는가"),
    ("그림에 필요한 화소", "CSS 크기 × 배율", "100px 자리에 3배면 <b>300화소</b>짜리가 필요하다"),
    ("배율별로 주기", "srcset 1x 2x 3x", "브라우저가 <b>자기 배율에 맞는 것</b>만 받는다"),
    ("배율과 무관한 것", "SVG · 글자", "그릴 때마다 다시 계산한다. <b>늘 선명하다</b>"),
    ("머리카락 선", "1 ÷ 배율 px", "3배에서 <code>0.33px</code>이면 정확히 화소 하나"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>반대 방향의 실수</b>도 흔합니다 —
          어디서나 선명하라고 모든 그림을 3배짜리로만 주는 것입니다.
          그러면 1배 모니터에서도 <b>아홉 배 큰 파일</b>을 받게 되고,
          화면에 뿌릴 때 줄이느라 오히려 느려집니다.
          <code>srcset</code>을 적어 두면 브라우저가 <b>자기 배율과 통신 사정</b>을 보고
          알아서 고릅니다 — 골라 주는 일을 브라우저에 넘기는 것이 요점입니다.</p>''',
  do=ul([
    "사진·비트맵 아이콘에 <code>srcset</code> 적기",
    "아이콘은 되도록 <b>SVG</b>나 글꼴로",
    "캔버스로 그릴 때 <b>배율만큼 크게</b> 잡고 축소해 쓰기",
  ]),
  dont=ul([
    "모든 그림을 3배짜리로만 주기 — <b>1배 기기가 손해</b>를 본다",
    "<code>devicePixelRatio</code>로 <b>기기를 짐작</b>하기 — 같은 값이 여럿이다",
    "선 굵기를 배율로 계산하기 — <b>1px 은 이미 맞는다</b>",
    "글자 크기를 배율로 바꾸기 — 바꿀 필요가 없다",
  ]),
  instead='폭에 따른 배치는 <a href="breakpoint.html">브레이크포인트</a>, 그림이 무거우면 포맷(WebP·AVIF)을 바꾸기, 아이콘이면 SVG 로.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>&lt;img</span>
                <span>&nbsp;&nbsp;src="logo.png"</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">srcset="logo@2x.png 2x,</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">&nbsp;&nbsp;logo@3x.png 3x"&gt;</span></span>
              </div>''',
     "배율별로", "브라우저가 <b>하나만</b> 받는다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>cv.width = w * <span style="color:var(--accent)">dpr</span>;</span>
                <span>cv.style.width = w + 'px';</span>
                <span>ctx.scale(<span style="color:var(--accent)">dpr, dpr</span>);</span>
              </div>''',
     "캔버스", "안 하면 <b>캔버스만 흐릿</b>하다"),
    (lines("0.5px", "border-width: 0.5px — 3배에선 화소 하나", "150px"),
     "구분선", "iOS 느낌의 <b>가는 선</b>. 1배 화면에서는 흐려질 수 있다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 밀도의 계약서",
  code_lede="그림은 배율별로 주고, 캔버스는 직접 맞춥니다.",
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
    ("<code>width</code>·<code>height</code>를 적는다", "밀도와 별개로 <b>자리를 미리 잡아</b> 글이 덜컥거리지 않게 한다"),
    ("<code>srcset</code>의 <code>2x</code>와 <code>800w</code>", "배율만 다르면 <code>x</code>, <b>폭도 다르면</b> <code>w</code> + <code>sizes</code>"),
    ("<code>alt</code>", "밀도와 무관하지만 <b>같이 빠지기 쉽다</b>. <a href=\"../items/name.html\">이름 붙이기</a>"),
    ("<code>image-rendering: pixelated</code>", "일부러 도트를 살릴 때만. <b>사진에 쓰면 더 나빠진다</b>"),
    ("<code>0.5px</code> 테두리", "1배 화면에서는 반올림돼 <b>사라지거나 흐려질 수</b> 있다. 질의로 가린다"),
    ("배율로 기기를 짐작하지 않는다", "같은 값이 폰에도 노트북에도 있다. 입력 방식은 <a href=\"hover.html\">포인터 질의</a>로 묻는다"),
  ]),
  backend=rows([
    ("이미지 변환은 서버에서", "원본 하나를 올려 두고 <b>필요한 크기로 잘라</b> 내려주는 쪽이 파일을 따로 관리하는 것보다 쌉니다."),
    ("캐시가 갈라진다", "같은 주소가 기기마다 다른 그림을 주면 CDN 캐시가 어긋납니다. <b>주소를 크기마다 따로</b> 두는 편이 안전합니다."),
    ("포맷이 더 큰 몫", "같은 그림이라도 WebP·AVIF 로 바꾸면 절반 아래로 떨어집니다. <b>배율보다 먼저</b> 볼 일입니다."),
    ("업로드한 사진", "요즘 폰 사진은 4000px 이 넘습니다. 받자마자 <b>쓸 크기로 줄여</b> 저장해 두지 않으면 목록 화면이 통째로 느려집니다."),
  ]),
  plat_lede="세 곳 모두 <b>길이와 화소를 갈라</b> 둡니다. 이름만 다릅니다.",
  plats=plats([
    ("웹", "CSS px · DPR",
     grid(7, "105px", "CSS px"),
     "<code>px</code>이 길이이고 <code>devicePixelRatio</code>가 배율입니다. 그림은 <code>srcset</code>으로 갈라 줍니다."),
    ("iOS", "pt · @2x @3x",
     '''              <div class="phone" role="img" aria-label="iOS 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;font-size:6px;color:var(--fg-muted)">icon@2x<br>icon@3x</div></div></div>''',
     "길이는 <b>pt</b>이고 파일 이름에 <code>@2x</code>·<code>@3x</code>를 붙여 둡니다. 구분선은 <b>화소 하나</b>가 관례입니다."),
    ("안드로이드", "dp · mdpi~xxxhdpi",
     '''              <div class="phone" role="img" aria-label="안드로이드 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;font-size:6px;color:var(--fg-muted)">drawable-xhdpi<br>drawable-xxhdpi</div></div></div>''',
     "길이는 <b>dp</b>이고 폴더 이름으로 배율을 가릅니다. 벡터 드로어블을 쓰면 한 벌로 끝납니다."),
  ]),
  plat_note="\"로고가 흐릿해요\"는 거의 늘 이것입니다. 그리고 디자이너의 화면과 개발자의 화면이 <b>둘 다 2배</b>라서 못 보고 지나가는 일이 잦습니다. 시안을 받을 때 <b>2배·3배 파일을 함께</b> 달라고 하거나, 아예 SVG 로 받아 두면 이 왕복이 사라집니다.",
  siblings=siblings("dpr"),
  related='''        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>''',
)
