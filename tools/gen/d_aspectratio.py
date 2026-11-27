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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">aspect-ratio: 16 / 9   폭에 맞춰 높이가 정해짐</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">폭이 바뀌어도 비가 유지됨</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">그림이 오기 전에 자리를 잡아 글이 밀리지 않음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">object-fit: cover   넘치는 부분을 잘라 채움</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">img에는 width·height 속성도 함께 적음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">높이를 따로 정하면 비가 무시됨</div>
                </div>
              </div>'''

D = dict(
  slug="aspectratio", ko="종횡비", en="Aspect ratio",
  desc="폭이 정해지면 높이가 따라오게 하는 종횡비를 다루는 항목입니다. 비를 유지하는 쓸모보다 자리를 미리 잡는 쓸모가 더 큽니다.",
  lede="종횡비는 폭이 정해지면 그 비에 맞춰 <b>높이가 따라오게</b> 하는 값입니다. 실무에서는 비를 지키는 것보다 그림이 오기 전에 <b>자리를 미리 잡는</b> 데 더 쓸모가 있습니다.",
  axes_lede="뼈대는 눈에 보이지 않지만 <b>모든 배치</b>를 정합니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>폭이 서로 다른 세 상자가 <b>같은 비</b>를 유지하는지, 아래에 실제로 잰 값이 나옵니다.<br>
          <b>비를 정하지 않고 높이만 주기</b>를 켜면 폭마다 비가 달라집니다. 화면 폭에 따라 칸 폭이 바뀌는 반응형 화면에서 바로 드러나는 차이입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "종횡비, 가로세로비, 비율"),
    ("영어", "aspect ratio, intrinsic ratio"),
    ("같이 쓰는 말",
     "CSS 속성 이름도 그대로 <code>aspect-ratio</code>입니다. "
     "이 속성이 없던 시절에는 <code>padding-top: 56.25%</code>로 비를 흉내 냈는데, 이 방법을 <b>패딩 트릭</b>이라고 불렀습니다. "
     "상자 안을 어떻게 채울지는 <code>object-fit</code>으로 정하며, <b>cover</b>는 넘치는 부분을 잘라 내며 채우고 <b>contain</b>은 그림 전체가 보이게 넣습니다. "
     "그림이 늦게 도착해 글이 밀리는 현상은 <b>레이아웃 시프트</b>(CLS)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>해상도</b> — 화소 수와 <b>비</b>는 다릅니다. 예를 들어 1920×1080과 1280×720은 화소 수가 다르지만 비는 똑같이 16:9입니다.<br>"
     "<b>크롭</b> — 그림을 잘라 내는 것은 <code>object-fit</code>이 하는 일이고, 비는 <b>상자의 모양</b>을 정합니다.<br>"
     "<b>스케일</b> — 크기를 키우는 것과 <b>비를 유지하는</b> 것은 다른 일입니다."),
  ]),
  axes=ax("종횡비"),
  oneline="<b>그림이 들어갈 자리에는 거의 항상 비를 적어 두세요.</b> 그러면 그림이 늦게 도착해도 글이 밀리지 않습니다.",
  s4_title="자주 쓰는 비와 자리 잡기", s4_hint="폭이 같아도 비에 따라 달라지는 높이",
  do_title="종횡비를 정해 두는 경우",
  dont_title="종횡비를 다룰 때 피할 것",
  instead_title="종횡비와 함께 보면 좋은 항목",
  states=states([
    (ar("16/9", "16 / 9", "110px", "영상·히어로"), "16 : 9", "<b>가장 흔한</b> 가로형 비입니다"),
    (ar("4/3", "4 / 3", "110px", "옛 사진"), "4 : 3", "사진과 썸네일에 씁니다"),
    (ar("1/1", "1 / 1", "110px", "아바타·상품"), "1 : 1", "<b>정사각형</b>이라서 목록에서 줄이 가지런히 맞습니다"),
    (ar("3/4", "3 / 4", "110px", "세로 사진"), "3 : 4", "폰에서 세로로 찍은 사진의 비입니다"),
    (ar("16/9", "자리만 잡아 둠", "110px", "그림이 오기 전", True, "var(--ink-050)"),
     "그림이 오기 전", "그림이 오기 전에 <b>자리를 미리</b> 잡아 둡니다"),
    (ar("16/9", "높이를 따로 정함", "110px", "비가 무시됨", False, "color-mix(in srgb, var(--danger) 10%, transparent)"),
     "높이를 따로 정했을 때", "높이가 따로 정해져 있으면 <b>비가 적용되지 않습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("비", "16 / 9", "폭이 정해지면 <b>높이가 따라옵니다</b>"),
    ("반응형", "비 유지", "칸 폭이 바뀌어도 <b>모양이 같습니다</b>"),
    ("자리 잡기", "그림이 오기 전", "그림이 늦게 와도 <b>글이 밀리지 않습니다</b>"),
    ("채우기", "object-fit: cover", "넘치는 부분을 <b>잘라서</b> 채웁니다. contain은 그림 전체가 보이게 넣습니다"),
    ("<code>&lt;img&gt;</code>", "width · height 속성", "속성만 적어도 <b>비가 정해집니다</b>"),
    ("비가 무시되는 경우", "높이를 따로 정함", "<code>height</code>가 따로 있으면 <b>비가 무시됩니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>그림에 <code>width</code>·<code>height</code> 속성을 적기만 해도</b>
          브라우저가 비를 계산해 자리를 미리 잡아 주고,
          CSS로 <code>width: 100%</code>를 주어도 그 비는 그대로 쓰입니다.
          예전에는 'HTML에 크기를 적지 마라'고 조언했지만 지금은 정반대가 되었기 때문에,
          옛 습관대로 속성을 지워 두면 <b>그림이 뜰 때마다 글이 밀립니다</b>.
          사진마다 비가 다르다면 서버가 <b>가로·세로 크기를 함께</b> 내려 주는 것이
          가장 적은 비용으로 이 문제를 푸는 방법입니다.</p>''',
  do=ul([
    "그림이나 영상이 들어갈 자리를 만들 때. <b>거의 항상</b> 비를 적어 둡니다",
    "목록 썸네일을 넣을 때. 썸네일 <b>모양이 같아야</b> 줄이 가지런합니다",
    "<code>&lt;img&gt;</code>를 쓸 때. <b>width·height 속성</b>도 함께 적습니다",
  ]),
  dont=ul([
    "비와 <code>height</code>를 <b>함께</b> 줄 때. height가 우선해서 비가 무시됩니다",
    "글이 든 상자에 비를 고정할 때. 글이 길어지면 <b>상자 밖으로 넘칩니다</b>",
    "패딩 트릭을 새로 쓸 때. <b>이제는 aspect-ratio 속성이 있습니다</b>",
    "<code>object-fit</code> 없이 그림을 넣을 때. 그림이 <b>찌그러집니다</b>",
  ]),
  instead='상자 크기 자체를 정하는 방법은 <a href="sizing.html">크기 정하기</a>에서, 넘친 내용을 처리하는 방법은 <a href="../items/overflow.html">넘침</a>에서 다룹니다. 그림이 오기 전에 그 자리를 어떻게 표시할지는 <a href="../items/skeleton.html">스켈레톤</a>에서 봅니다.',
  cases=cases([
    (ar("1/1", "아바타", "150px", "목록에서 줄이 맞음"), "정사각 썸네일로 목록 줄 맞추기", "<a href=\"../items/listitem.html\">리스트</a>에서 정사각 썸네일로 줄을 맞춥니다"),
    (ar("16/9", "영상", "150px", "가장 흔한 비"), "영상 자리 미리 잡기", "영상을 불러오기 전에 <b>자리를 미리</b> 잡습니다"),
    (code(['&lt;img src="s.jpg"', '  width="800" height="450"', '  style="width:100%;height:auto"&gt;'], "150px", "속성만으로도 비가 정해짐", True),
     "img 속성으로 비 정하기", "속성 두 개만 적는 <b>가장 간단한 방법</b>입니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="종횡비를 쓸 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="상자에는 <code>aspect-ratio</code>, 그림에는 <b>크기 속성</b>을 적습니다.",
  code='''<span class="c">/* 상자. 폭이 정해지면 높이가 따라온다 */</span>
.thumb {
  <span class="a">aspect-ratio</span>: <span class="a">16</span> / <span class="a">9</span>;
  <span class="a">width</span>: <span class="a">100%</span>;
  <span class="a">overflow</span>: hidden;
  <span class="a">border-radius</span>: <span class="a">var</span>(--radius-1);
}
.thumb <span class="t">img</span> { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">height</span>: <span class="a">100%</span>; <span class="a">object-fit</span>: cover; }

<span class="c">&lt;!-- 그림 자체. 속성만 적어도 비가 생긴다 --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"store.jpg"</span> <span class="a">width</span>=<span class="s">"800"</span> <span class="a">height</span>=<span class="s">"450"</span>
     <span class="a">style</span>=<span class="s">"width:100%;height:auto"</span> <span class="a">alt</span>=<span class="s">"모란상회 매장"</span>&gt;''',
  keys=kbd([
    ("<code>width</code>·<code>height</code> 속성 남겨 두기", "<b>지우지 않습니다.</b> 브라우저가 이 속성으로 비를 계산해 자리를 잡습니다"),
    ("CSS에서는 <code>height: auto</code>로 두기", "CSS로 폭만 주면 <b>속성에서 계산한 비</b>가 쓰입니다"),
    ("그림에 <code>object-fit: cover</code> 주기", "없으면 그림이 <b>찌그러집니다</b>"),
    ("<code>alt</code>는 따로 적기", "비는 자리만 잡아 줄 뿐이고, 그림의 뜻은 <a href=\"alttext.html\">대체 텍스트</a>로 따로 적습니다"),
    ("글이 든 상자에는 비를 고정하지 않기", "비를 고정하면 <b>글이 넘치므로</b>, 글이 든 상자에는 <code>min-height</code>를 씁니다"),
    ("SVG는 <code>viewBox</code>의 비 따르기", "<code>viewBox</code>에 이미 비가 들어 있습니다. <code>preserveAspectRatio</code>를 <code>none</code>으로 두면 <b>찌그러집니다</b>"),
  ]),
  backend=rows([
    ("가로·세로 크기를 함께 보내기", "응답에 <code>{\"w\":800,\"h\":450}</code>처럼 크기가 있으면 화면이 그림을 받기 전에 <b>자리를 미리</b> 잡을 수 있습니다."),
    ("사진마다 비가 다를 때", "사용자가 올린 사진은 비가 제각각이라서, 저장할 때 <b>한 비로 잘라</b> 두거나 응답에 비를 함께 보냅니다."),
    ("썸네일을 미리 만들어 두기", "큰 원본을 화면에서 줄여 쓰면 느리기 때문에 썸네일을 따로 만들어 둡니다(<a href=\"dpr.html\">화면 밀도</a>·<a href=\"assets.html\">에셋 내보내기</a> 참고)."),
  ]),
  plat_lede="<b>비로 자리를 잡는다</b>는 생각은 세 플랫폼 모두 같습니다.",
  plats=plats([
    ("웹", "aspect-ratio",
     ar("16/9", "16/9", "100px"),
     "2021년부터는 속성 하나로 비를 정할 수 있고, 그전에는 <b>패딩 트릭</b>을 썼습니다."),
    ("iOS", "aspectRatio",
     '''              <div class="phone" role="img" aria-label="iOS 비 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;aspect-ratio:16/9;background:var(--accent-soft);border:1px solid var(--accent);border-radius:3px"></div></div></div>''',
     "<code>.aspectRatio(16/9, contentMode:)</code>로 정하고, <code>fill</code>이 웹의 cover에 해당합니다."),
    ("안드로이드", "aspectRatio",
     '''              <div class="phone" role="img" aria-label="안드로이드 비 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;aspect-ratio:16/9;background:var(--accent-soft);border:1px solid var(--accent);border-radius:3px"></div></div></div>''',
     "Compose의 <code>Modifier.aspectRatio()</code>로 정하고, <code>ContentScale.Crop</code>이 웹의 cover에 해당합니다."),
  ]),
  plat_note="\"그림이 뜨면 글이 밀려요\"라는 문제는 비를 적지 않아서 생깁니다. <code>&lt;img&gt;</code> 속성 두 개만 적으면 고칠 수 있고 효과도 바로 보이기 때문에, <b>목록 화면을 만들 때 가장 먼저 챙기면 좋은 한 줄</b>입니다.",
  siblings=siblings("aspectratio"),
  related='''        <li><a href="sizing.html"><b>크기 정하기</b><em>1부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="dpr.html"><b>화면 밀도</b><em>11부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
