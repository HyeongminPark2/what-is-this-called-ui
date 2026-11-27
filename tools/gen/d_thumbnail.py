# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 모두 보여 주기만 합니다. 아래 네 가지로 서로 가릅니다."

def box(inner, label, note="", ok=None, w="152px", h="56px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:center">'
            '<span style="display:block;width:76px;height:' + h + ';border:1px solid ' + c + ';'
            'border-radius:5px;overflow:hidden;background:var(--bg);position:relative">' + inner + '</span>'
            '<span style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:9px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

def pic(w, h, left=0, top=0, sx=1, sy=1):
    # 동그라미가 사진 속 얼굴 구실을 한다 — 잘리면 테두리가 끊기고, 늘어나면 타원이 된다
    return ('<span style="position:absolute;left:' + str(left) + 'px;top:' + str(top) + 'px;'
            'width:' + str(w) + 'px;height:' + str(h) + 'px;background:var(--accent-soft);'
            'border:2px dashed var(--accent);box-sizing:border-box;display:grid;place-items:center">'
            '<span style="display:block;width:' + str(round(14 * sx)) + 'px;height:' + str(round(14 * sy)) +
            'px;border-radius:999px;background:var(--accent)"></span></span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">칸의 비율은 aspect-ratio로 고정</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">object-fit: cover로 잘라 채움(기본으로 삼음)</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">object-position으로 남길 곳을 정함</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">fill은 잘리지 않지만 찌그러짐</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">width·height를 적어 두면 자리가 밀리지 않음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">alt는 그림에 뜻이 있을 때 적음</div>
                </div>
              </div>'''

D = dict(
  slug="thumbnail", ko="썸네일", en="Thumbnail",
  desc="비율이 정해진 칸에 비율이 제각각인 사진을 넣는 법을 잘라 채우기, 여백 두기, 찌그러짐, 자리 예약으로 나눠 보여 주는 항목입니다.",
  lede="썸네일은 사진을 작게 줄여 보여 주는 그림입니다. 썸네일 칸은 <b>가로세로 비율이 정해져</b> 있는데 사진의 비율은 제각각이라서, 사진의 일부를 잘라 낼지, 여백을 둘지, 비율을 포기할지 가운데 <b>무엇을 포기할지</b> 늘 골라야 합니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모는 <b>원본에서 잘려 나간 넓이</b>와 <b>가로세로 비가 얼마나 어긋났는지</b>를 재서 적습니다.
          <code>cover</code>는 사진을 잘라 칸을 채우고, <code>contain</code>은 여백을 남깁니다.
          <code>fill</code>은 한 픽셀도 잘리지 않는 대신 사진이 <b>찌그러지기</b> 때문에 거의 쓰지 않습니다.<br>
          <code>cover</code>를 쓰면 사진의 어느 부분을 남길지 정해야 하는데, 기본값은 가운데입니다.
          인물 사진은 <code>object-position: top</code>으로 위쪽을 남겨야 머리가 잘리지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "썸네일, 미리보기 그림, 작은 그림"),
    ("영어", "thumbnail, thumb, preview image"),
    ("같이 쓰는 말",
     "칸을 꽉 채우려고 사진을 자르는 것은 <b>크롭</b>(crop), 비율을 지키며 여백을 두는 것은 <b>레터박스</b>라고 부릅니다.  "
     "사진을 자를 때 남길 중심을 미리 정해 둔 점은 <b>포컬 포인트</b>(focal point)라고 하고,  "
     "흐릿한 그림을 먼저 보여 주는 기법은 <b>LQIP</b>(저품질 미리보기)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>아바타</b> — <a href=\"avatar.html\">아바타</a>는 <b>사람이나 조직</b>을 가리키는 동그란 그림이고, 썸네일은 내용을 줄여 보여 주는 그림입니다.<br>"
     "<b>아이콘</b> — <a href=\"icon.html\">아이콘</a>은 뜻을 나타내는 <b>기호</b>이고, 썸네일은 <b>그 물건을 찍은 사진</b>입니다.<br>"
     "<b>커버</b> — 커버는 화면 맨 위에 넓게 까는 <b>띠 모양 그림</b>입니다."),
  ]),
  axes=ax("썸네일"),
  oneline="<b>썸네일은 <code>cover</code>를 기본으로 두세요.</b> 대개 여백을 남기는 것보다 잘라 채우는 쪽이 낫고, 사진이 찌그러지는 것은 둘 다보다 나쁩니다.",
  s4_title="채우는 방식과 상태", s4_hint="채우는 방식과 상태마다 달라지는 썸네일",
  states=states([
    (box(pic(100, 56, -12, 0), "cover", "칸을 꽉 채우고 양옆이 잘림", True),
     "<code>cover</code>로 잘라 채울 때", "썸네일의 <b>기본</b>으로 삼습니다"),
    (box(pic(76, 42, 0, 7), "contain", "비율을 지키고 위아래에 여백을 둠", None),
     "<code>contain</code>으로 여백을 둘 때", "사진 전체가 <b>다 보여야</b> 할 때만 씁니다"),
    (box(pic(76, 56, 0, 0, 1.8, 0.8), "fill", "잘리지 않지만 찌그러짐", False),
     "<code>fill</code>로 늘려 맞출 때", "사진이 찌그러지므로 <b>거의 쓰지 않습니다</b>"),
    (box(pic(76, 78, 0, -22), "object-position: top", "아래쪽이 잘리고 머리가 남음", True),
     "사진 위쪽을 남길 때", "머리가 잘리지 않도록 <b>인물 사진</b>에 씁니다"),
    (box('<span style="position:absolute;inset:0;background:linear-gradient(90deg,var(--bg) 0%,var(--line) 50%,var(--bg) 100%)"></span>',
         "자리 예약", "크기를 적어 두어 자리가 밀리지 않음", True),
     "사진을 불러오는 중", "사진이 오기 전에 <b>칸을 미리</b> 잡아 둡니다"),
    (box('<span style="position:absolute;inset:0;display:grid;place-items:center;font-size:8.5px;color:var(--fg-muted)">사진 없음</span>',
         "빈 자리", "회색 네모 대신 말로 알림", None),
     "사진이 없을 때", "사진이 없으면 <b>대체 그림</b>을 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("칸의 비", "고정된 가로세로 비율", "<code>aspect-ratio</code>로 비율을 고정합니다"),
    ("<code>cover</code>", "잘라서 채우는 방식", "썸네일의 <b>기본</b>으로 삼습니다"),
    ("<code>object-position</code>", "남길 곳을 정하는 속성", "인물 사진은 <code>top</code>으로 둡니다"),
    ("<code>fill</code>", "늘려서 맞추는 방식", "사진이 찌그러지므로 <b>쓰지 않습니다</b>"),
    ("<code>width·height</code>", "자리를 예약하는 값", "사진이 늦게 와도 글이 <b>밀리지 않습니다</b>"),
    ("<code>alt</code>", "그림에 뜻이 있을 때 적는 글", "장식용이면 <b>빈 문자열</b>로 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          썸네일에서 특히 흔한 문제는 <b>레이아웃이 갑자기 밀리는 것</b>입니다.
          사진이 늦게 들어오면 사진 높이만큼 아래 글이 밀려 내려가서,
          읽던 사람이 누르려던 곳이 아닌 <b>엉뚱한 곳을 누르게</b> 됩니다.
          <code>width</code>·<code>height</code>를 적어 두거나
          <code>aspect-ratio</code>를 걸어 두면 브라우저가 사진이 오기 전에
          <b>미리 자리를 잡아</b> 두므로, 코드 한 줄로 고칠 수 있습니다.<br>
          두 번째 문제는 <b>너무 큰 원본</b>입니다. 76px 칸에 2000px 사진을 넣으면
          화면에 보이는 모습은 같은데 데이터는 수십 배를 씁니다.
          그래서 <code>srcset</code>으로 <b>칸에 맞는 크기</b>의 사진을 받습니다.</p>''',
  do_title="썸네일을 만들 때 지킬 것", dont_title="썸네일을 만들 때 피할 것",
  instead_title="썸네일 대신 쓸 부품과 함께 볼 항목",
  do=ul([
    "칸에 <b><code>aspect-ratio</code></b>를 걸고 <code>cover</code>로 채우기",
    "<code>width</code>·<code>height</code>를 적어 <b>자리를 예약</b>하기",
    "<code>srcset</code>으로 <b>칸에 맞는 크기</b> 받기",
  ]),
  dont=ul([
    "<code>fill</code>로 늘려 맞추기. 사진 속 <b>얼굴이 찌그러집니다</b>",
    "크기를 적어 두지 않기. 사진이 들어올 때 <b>레이아웃이 밀립니다</b>",
    "원본을 그대로 쓰기. 76px 칸에 2000px 사진을 받게 됩니다",
    "빈 자리를 <b>회색 네모</b>로만 두기. 사진이 왜 없는지 한 줄 적어 줍니다",
  ]),
  instead='사람이나 조직을 가리키는 그림이면 <a href="avatar.html">아바타</a>를, 뜻을 나타내는 기호면 <a href="icon.html">아이콘</a>을 씁니다. 가로세로 비율을 정하는 방법은 <a href="aspectratio.html">종횡비</a>에서, 사진을 불러오는 동안 보여 줄 뼈대는 <a href="skeleton.html">스켈레톤</a>에서 다룹니다.',
  cases=cases([
    (box(pic(100, 56, -12, 0), "상품 목록", "", True), "상품 사진을 같은 비율로 맞추기", "모든 사진을 <b>같은 비율</b>로 가지런히 맞춥니다"),
    (box(pic(76, 78, 0, -22), "사람 목록", "", True), "인물 사진에서 머리 남기기", "머리가 잘리지 않게 사진 <b>위쪽</b>을 남깁니다"),
    (box(pic(76, 42, 0, 7), "작품 · 도면", "", None), "원본을 자르면 안 되는 그림 보여 주기", "사진이 잘리면 안 되므로 <b>여백</b>이 생기는 것을 감수합니다"),
  ]),
  s8_title="최소 마크업과 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="칸의 비율을 고정하고 <code>cover</code>로 채웁니다. 이미지에 크기를 적어 두면 브라우저가 그 크기만큼 자리를 예약합니다.",
  code='''&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"/p/2411.jpg"</span> <span class="a">width</span>=<span class="s">"320"</span> <span class="a">height</span>=<span class="s">"240"</span>
     <span class="a">srcset</span>=<span class="s">"/p/2411@1x.jpg 320w, /p/2411@2x.jpg 640w"</span>
     <span class="a">sizes</span>=<span class="s">"(max-width: 600px) 45vw, 160px"</span>
     <span class="a">alt</span>=<span class="s">"한빛아웃도어 등산화"</span> <span class="a">loading</span>=<span class="s">"lazy"</span>&gt;

.thumb {
  <span class="a">aspect-ratio</span>: <span class="a">4</span> / <span class="a">3</span>;      <span class="c">/* 칸의 비율을 고정한다 */</span>
  <span class="a">object-fit</span>: cover;       <span class="c">/* 넘치는 쪽을 자른다 */</span>
  <span class="a">object-position</span>: center; <span class="c">/* 인물이면 top */</span>
  <span class="a">width</span>: <span class="a">100%</span>; <span class="a">background</span>: <span class="a">var</span>(--bg);
}''',
  keys=kbd([
    ("<code>alt</code>에 사진의 뜻 적기", "사진에 전할 뜻이 있으면 적고, 장식용이면 <b>빈 문자열</b>로 둡니다"),
    ("링크 안에 든 썸네일의 <code>alt</code>", "같은 링크 안에 글이 있으면 그림의 <code>alt</code>는 <b>비웁니다</b>. 채우면 같은 내용이 두 번 읽힙니다"),
    ("<code>loading=\"lazy\"</code>로 나중에 받기", "화면 밖에 있는 그림은 화면에 가까워졌을 때 <b>나중에</b> 받습니다"),
    ("<code>decoding=\"async\"</code>로 기다리지 않기", "그림 디코딩이 끝나기를 기다리지 않고 화면을 그립니다"),
    ("<code>aspect-ratio</code>로 자리 잡기", "크기를 적을 수 없을 때 <b>자리를 잡는</b> 다른 방법입니다"),
    ("확인하는 방법", "네트워크 속도를 느리게 설정하고 사진이 들어올 때 <b>글이 밀리는지</b> 봅니다"),
  ]),
  backend=rows([
    ("사진을 여러 크기로 내려 주기", "원본 하나만 보내면 화면이 <b>큰 그림을 받아 줄여</b> 써야 합니다. 그래서 썸네일 크기의 사진을 서버에서 미리 만들어 두는 편이 낫습니다."),
    ("사진 크기를 응답에 함께 담기", "<code>width</code>·<code>height</code>가 응답에 들어 있으면 화면이 사진을 받기 전에 <b>자리를 예약</b>할 수 있습니다."),
    ("자를 때 남길 포컬 포인트 보내기", "<code>focal: {x: 0.5, y: 0.3}</code> 같은 값을 함께 보내면 사진을 자를 때 <b>어디를 남길지</b>를 사진마다 다르게 정할 수 있습니다."),
  ]),
  plat_lede="사진을 <b>칸에 맞춰 자른다</b>는 방식은 세 플랫폼이 모두 같습니다.",
  plats=plats([
    ("웹", "object-fit",
     box(pic(100, 56, -12, 0), "cover", "", True, "110px"),
     "<code>object-fit</code>과 <code>aspect-ratio</code> 두 줄이면 됩니다."),
    ("iOS", "contentMode",
     '''              <div class="phone" role="img" aria-label="iOS 썸네일 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>.scaledToFill()</code>이 cover, <code>.scaledToFit()</code>이 contain에 해당합니다."),
    ("안드로이드", "scaleType",
     '''              <div class="phone" role="img" aria-label="안드로이드 썸네일 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>centerCrop</code>이 cover, <code>fitCenter</code>가 contain에 해당하고, 이름만 다릅니다."),
  ]),
  plat_note="세 플랫폼에서 부르는 이름은 다르지만 <b>하는 일은 같아서</b>, 모두 cover와 contain 두 가지로 나뉩니다. 앱에서는 이미지 불러오기 라이브러리가 <b>크기별 캐시</b>까지 맡아 주는 반면, 웹에서는 <code>srcset</code>으로 크기별 사진을 직접 적어 줘야 합니다. 대신 웹에는 <code>aspect-ratio</code>로 <b>자리를 미리 잡는</b> 간단한 방법이 있어서, 레이아웃이 밀리는 문제만큼은 한 줄로 막을 수 있습니다.",
  siblings=siblings("thumbnail"),
  related='''        <li><a href="aspectratio.html"><b>종횡비</b><em>1부</em></a></li>
        <li><a href="avatar.html"><b>아바타</b><em>5부</em></a></li>
        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="alttext.html"><b>대체 텍스트</b><em>12부</em></a></li>''',
)
