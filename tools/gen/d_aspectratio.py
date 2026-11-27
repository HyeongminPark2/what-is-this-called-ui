# -*- coding: utf-8 -*-
from ax1 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ar(ratio, label, w="110px", note="", ok=None, fill="var(--accent-soft)"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--accent)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="width:100%;aspect-ratio:' + ratio + ';border:1px solid ' + col + ';border-radius:5px;'
            'background:' + fill + ';display:grid;place-items:center;font-family:var(--mono);font-size:9.5px;color:' + col + '">'
            + label + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">aspect-ratio: 16 / 9 — 폭이 정해지면 높이가 따라온다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">폭이 바뀌어도 비가 유지된다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">그림이 오기 전에 자리를 잡는다 — 글이 안 덜컥거린다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">object-fit: cover — 잘라서 채운다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">img 에는 width · height 속성도 함께 적는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">높이가 따로 정해지면 비가 무시된다</div>
                </div>
              </div>'''

D = dict(
  slug="aspectratio", ko="종횡비", en="Aspect ratio",
  desc="폭이 정해지면 높이가 따라오게 하는 값. 비를 유지하는 쓸모보다 자리를 미리 잡는 쓸모가 크다.",
  lede="폭이 정해지면 <b>높이가 따라오게</b> 하는 값. 비를 지키는 것보다 <b>자리를 미리 잡는</b> 쓸모가 큽니다.",
  axes_lede="뼈대는 눈에 안 보이지만 <b>모든 화면이 그 위에</b> 섭니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>폭이 서로 다른 세 상자가 <b>같은 비</b>를 지킵니다 — 아래에 실제로 잰 값이 나옵니다.<br>
          <b>비를 안 정하고 높이만 주기</b>를 켜면 폭마다 비가 달라집니다. 반응형에서 바로 드러나는 차이입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "종횡비, 가로세로비, 비율"),
    ("영어", "aspect ratio, intrinsic ratio"),
    ("같이 쓰는 말",
     "CSS 속성 이름이 그대로 <code>aspect-ratio</code>입니다. "
     "이 속성이 없던 시절 <code>padding-top: 56.25%</code>로 흉내 내던 것을 <b>패딩 트릭</b>이라 불렀습니다. "
     "안을 어떻게 채울지는 <code>object-fit</code>이고, <b>cover</b>는 잘라 채우고 <b>contain</b>은 다 보이게 넣습니다. "
     "그림이 늦게 와 글이 밀리는 것을 <b>레이아웃 시프트</b>(CLS)라 합니다."),
    ("자주 잘못 부름",
     "<b>해상도</b> — 화소 수와 <b>비</b>는 다릅니다. 1920×1080 과 1280×720 은 같은 16:9 입니다.<br>"
     "<b>크롭</b> — 잘라내는 것은 <code>object-fit</code>의 일입니다. 비는 <b>상자의 모양</b>입니다.<br>"
     "<b>스케일</b> — 키우는 것과 <b>비를 유지하는</b> 것은 다릅니다."),
  ]),
  axes=ax("종횡비"),
  oneline="<b>그림 자리에는 거의 늘 비를 적어 두세요.</b> 그림이 늦게 와도 글이 밀리지 않습니다.",
  s4_title="비별로", s4_hint="같은 폭, 다른 높이",
  states=states([
    (ar("16/9", "16 / 9", "110px", "영상·히어로"), "16 : 9", "<b>가장 흔한</b> 가로형"),
    (ar("4/3", "4 / 3", "110px", "옛 사진"), "4 : 3", "사진·썸네일"),
    (ar("1/1", "1 / 1", "110px", "아바타·상품"), "1 : 1", "<b>정사각.</b> 목록에서 잘 선다"),
    (ar("3/4", "3 / 4", "110px", "세로 사진"), "3 : 4", "폰에서 찍은 사진"),
    (ar("16/9", "자리만 잡아 둠", "110px", "그림이 오기 전", True, "var(--ink-050)"),
     "오기 전", "<b>자리를 미리</b> 잡아 둔다"),
    (ar("16/9", "높이가 따로 박힘", "110px", "비가 무시된다", False, "color-mix(in srgb, var(--danger) 10%, transparent)"),
     "높이가 박히면", "<b>비가 안 먹는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("비", "16 / 9", "폭이 정해지면 <b>높이가 따라온다</b>"),
    ("반응형", "비가 유지된다", "칸 폭이 바뀌어도 <b>모양이 같다</b>"),
    ("자리 잡기", "오기 전에", "그림이 늦게 와도 <b>글이 안 밀린다</b>"),
    ("채우기", "object-fit: cover", "<b>잘라서</b> 채운다. contain 은 다 보이게"),
    ("<code>&lt;img&gt;</code>", "width · height 속성", "속성만 적어도 <b>비가 생긴다</b>"),
    ("안 먹을 때", "높이가 따로 박힘", "<code>height</code>가 있으면 <b>비가 진다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>그림에 <code>width</code>·<code>height</code> 속성을 적는 것만으로</b>
          브라우저가 비를 계산해 자리를 미리 잡아 줍니다 —
          CSS 로 <code>width: 100%</code>를 주어도 그 비는 그대로 쓰입니다.
          오래된 조언('HTML 에 크기를 적지 마라')이 지금은 정반대가 된 자리라,
          옛 습관대로 속성을 지워 두면 <b>그림이 뜰 때마다 글이 밀립니다</b>.
          비가 저마다 다른 사진이라면 서버가 <b>가로·세로를 함께</b> 내려주는 것이
          이 문제를 가장 싸게 해결합니다.</p>''',
  do=ul([
    "그림·영상 자리에 <b>거의 늘</b>",
    "목록 썸네일 — <b>모양이 같아야</b> 줄이 선다",
    "<code>&lt;img&gt;</code>에는 <b>width·height 속성</b>도 함께",
  ]),
  dont=ul([
    "비와 <code>height</code>를 <b>같이</b> 주기 — 비가 진다",
    "글이 든 상자에 비를 박기 — <b>글이 넘친다</b>",
    "패딩 트릭을 새로 쓰기 — <b>이제 속성이 있다</b>",
    "<code>object-fit</code> 없이 그림 넣기 — <b>찌그러진다</b>",
  ]),
  instead='크기 자체는 <a href="sizing.html">크기 정하기</a>, 넘치는 처리는 <a href="../items/overflow.html">넘침</a>, 오기 전 자리는 <a href="../items/skeleton.html">스켈레톤</a>.',
  cases=cases([
    (ar("1/1", "아바타", "150px", "목록에서 줄이 선다"), "정사각 썸네일", "<a href=\"../items/listitem.html\">리스트</a>에서"),
    (ar("16/9", "영상", "150px", "가장 흔한 비"), "영상", "<b>자리를 미리</b> 잡는다"),
    (code(['&lt;img src="s.jpg"', '  width="800" height="450"', '  style="width:100%;height:auto"&gt;'], "150px", "속성만으로도 비가 생긴다", True),
     "속성으로", "<b>가장 간단한 길</b>"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 비의 계약서",
  code_lede="상자에는 <code>aspect-ratio</code>, 그림에는 <b>크기 속성</b>을 적습니다.",
  code='''<span class="c">/* 상자 — 폭이 정해지면 높이가 따라온다 */</span>
.thumb {
  <span class="a">aspect-ratio</span>: <span class="a">16</span> / <span class="a">9</span>;
  <span class="a">width</span>: <span class="a">100%</span>;
  <span class="a">overflow</span>: hidden;
  <span class="a">border-radius</span>: <span class="a">var</span>(--radius-1);
}
.thumb <span class="t">img</span> { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">height</span>: <span class="a">100%</span>; <span class="a">object-fit</span>: cover; }

<span class="c">&lt;!-- 그림 자체 — 속성만 적어도 비가 생긴다 --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"store.jpg"</span> <span class="a">width</span>=<span class="s">"800"</span> <span class="a">height</span>=<span class="s">"450"</span>
     <span class="a">style</span>=<span class="s">"width:100%;height:auto"</span> <span class="a">alt</span>=<span class="s">"모란상회 매장"</span>&gt;''',
  keys=kbd([
    ("<code>width</code>·<code>height</code> 속성", "<b>지우지 않는다.</b> 브라우저가 비를 계산해 자리를 잡는다"),
    ("<code>height: auto</code>", "CSS 로 폭만 주면 <b>속성의 비</b>가 쓰인다"),
    ("<code>object-fit: cover</code>", "없으면 <b>찌그러진다</b>"),
    ("<code>alt</code>", "자리만 잡고 뜻은 따로다 — <a href=\"alttext.html\">대체 텍스트</a>"),
    ("글이 든 상자", "비를 박으면 <b>글이 넘친다</b>. 글에는 <code>min-height</code>를 쓴다"),
    ("SVG", "<code>viewBox</code>가 이미 비를 가진다. <code>preserveAspectRatio</code>를 <code>none</code>으로 두면 <b>찌그러진다</b>"),
  ]),
  backend=rows([
    ("가로·세로를 함께 보낸다", "<code>{\"w\":800,\"h\":450}</code>가 있으면 화면이 <b>자리를 미리</b> 잡습니다."),
    ("사진마다 비가 다르다", "사용자가 올린 사진은 제각각입니다. <b>한 비로 잘라</b> 저장하거나 비를 함께 보냅니다."),
    ("썸네일을 만들어 둔다", "원본을 줄여 쓰면 느립니다 — <a href=\"dpr.html\">화면 밀도</a>·<a href=\"assets.html\">에셋 내보내기</a>."),
  ]),
  plat_lede="<b>비로 자리를 잡는다</b>는 생각은 같습니다.",
  plats=plats([
    ("웹", "aspect-ratio",
     ar("16/9", "16/9", "100px"),
     "2021년부터 속성 하나로 됩니다. 전에는 <b>패딩 트릭</b>을 썼습니다."),
    ("iOS", "aspectRatio",
     '''              <div class="phone" role="img" aria-label="iOS 비 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;aspect-ratio:16/9;background:var(--accent-soft);border:1px solid var(--accent);border-radius:3px"></div></div></div>''',
     "<code>.aspectRatio(16/9, contentMode:)</code>. <code>fill</code>이 cover 자리입니다."),
    ("안드로이드", "aspectRatio",
     '''              <div class="phone" role="img" aria-label="안드로이드 비 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;aspect-ratio:16/9;background:var(--accent-soft);border:1px solid var(--accent);border-radius:3px"></div></div></div>''',
     "Compose 의 <code>Modifier.aspectRatio()</code>. <code>ContentScale.Crop</code>이 cover 입니다."),
  ]),
  plat_note="\"그림이 뜨면 글이 밀려요\"는 비를 안 적어서 생깁니다. 고치는 값이 아주 싸고(<code>&lt;img&gt;</code> 속성 두 개) 효과는 바로 보여서, <b>목록 화면을 만들 때 가장 먼저 챙기면 좋은 한 줄</b>입니다.",
  siblings=siblings("aspectratio"),
  related='''        <li><a href="sizing.html"><b>크기 정하기</b><em>1부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="dpr.html"><b>화면 밀도</b><em>11부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
