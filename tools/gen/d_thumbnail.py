# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">칸의 비는 고정 — aspect-ratio</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">object-fit: cover — 잘라 채운다(기본으로 삼는다)</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">object-position — 어디를 남길지</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">fill — 안 잘리지만 찌그러진다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">width·height 를 적어 둔다 — 자리가 안 튄다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">alt — 그림이 뜻을 가지면 적는다</div>
                </div>
              </div>'''

D = dict(
  slug="thumbnail", ko="썸네일", en="Thumbnail",
  desc="정해진 칸에 제각각인 사진을 넣는 법. 잘라 채우기와 여백, 찌그러짐, 자리 예약.",
  lede="칸은 <b>비율이 정해져</b> 있고 사진은 제각각입니다. 그래서 늘 <b>무엇을 버릴지</b>를 고르게 됩니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모가 <b>원본에서 잘려 나간 넓이</b>와 <b>가로세로 비가 얼마나 어긋났는지</b>를 재서 적습니다.
          <code>cover</code> 는 잘라 채우고, <code>contain</code> 은 여백을 남기고,
          <code>fill</code> 은 한 픽셀도 안 잘리는 대신 <b>찌그러집니다</b> — 그래서 거의 안 씁니다.<br>
          <code>cover</code> 를 쓰면 어디를 남길지가 문제인데 기본은 가운데입니다.
          인물 사진은 <code>object-position: top</code> 쪽이 머리가 안 잘립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "썸네일, 미리보기 그림, 작은 그림"),
    ("영어", "thumbnail, thumb, preview image"),
    ("같이 쓰는 말",
     "칸을 꽉 채우려 자르는 것이 <b>크롭</b>(crop), 비율을 지키며 여백을 두는 것이 <b>레터박스</b>입니다. "
     "사진에서 남길 가운데를 미리 정해 둔 점을 <b>포컬 포인트</b>(focal point)라 하고, "
     "흐릿한 그림을 먼저 보여 주는 기법은 <b>LQIP</b>(저품질 미리보기)입니다."),
    ("자주 잘못 부름",
     "<b>아바타</b> — <a href=\"avatar.html\">아바타</a>는 <b>사람·조직</b>을 가리키는 동그란 그림입니다.<br>"
     "<b>아이콘</b> — <a href=\"icon.html\">아이콘</a>은 <b>뜻의 기호</b>이고 썸네일은 <b>그 물건의 사진</b>입니다.<br>"
     "<b>커버</b> — 커버는 맨 위의 <b>넓은 띠 그림</b>입니다."),
  ]),
  axes=ax("썸네일"),
  oneline="<b><code>cover</code> 를 기본으로 두세요.</b> 여백보다 잘림이 낫고, 찌그러짐은 둘보다 나쁩니다.",
  states=states([
    (box(pic(100, 56, -12, 0), "cover", "칸을 꽉 채운다 — 양옆이 잘렸다", True),
     "<code>cover</code>", "<b>기본으로</b> 삼는다"),
    (box(pic(76, 42, 0, 7), "contain", "비를 지키고 위아래에 여백", None),
     "<code>contain</code>", "<b>다 보여야</b> 할 때만"),
    (box(pic(76, 56, 0, 0, 1.8, 0.8), "fill", "안 잘리지만 찌그러졌다", False),
     "<code>fill</code>", "<b>거의 안 쓴다</b>"),
    (box(pic(76, 78, 0, -22), "object-position: top", "아래쪽이 잘리고 머리가 남는다", True),
     "위쪽 남기기", "<b>인물 사진</b>에 쓴다"),
    (box('<span style="position:absolute;inset:0;background:linear-gradient(90deg,var(--bg) 0%,var(--line) 50%,var(--bg) 100%)"></span>',
         "자리 예약", "크기를 적어 둬 자리가 안 튄다", True),
     "불러오는 중", "<b>칸을 미리</b> 잡아 둔다"),
    (box('<span style="position:absolute;inset:0;display:grid;place-items:center;font-size:8.5px;color:var(--fg-muted)">사진 없음</span>',
         "빈 자리", "회색 네모가 아니라 말로", None),
     "그림 없음", "<b>대체 그림</b>을 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("칸의 비", "고정", "<code>aspect-ratio</code> 로 못 박는다"),
    ("<code>cover</code>", "잘라 채움", "<b>기본</b>으로 삼는다"),
    ("<code>object-position</code>", "어디를 남길지", "인물은 <code>top</code>"),
    ("<code>fill</code>", "찌그러짐", "<b>쓰지 않는다</b>"),
    ("<code>width·height</code>", "자리 예약", "글이 <b>안 튄다</b>"),
    ("<code>alt</code>", "뜻이 있으면", "장식이면 <b>빈 문자열</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          썸네일에서 가장 흔한 사고는 <b>자리가 튀는 것</b>입니다 —
          사진이 늦게 오면 그만큼 아래 글이 밀려 내려가고,
          읽던 사람은 <b>엉뚱한 곳을 누르게</b> 됩니다.
          <code>width</code>·<code>height</code> 를 적어 두거나
          <code>aspect-ratio</code> 를 걸어 두면 브라우저가
          <b>미리 자리를 잡아</b> 둡니다 — 한 줄로 끝나는 수리입니다.<br>
          두 번째는 <b>너무 큰 원본</b>입니다. 76px 칸에 2000px 사진을 넣으면
          보이기는 같은데 데이터는 수십 배를 씁니다 —
          <code>srcset</code> 으로 <b>칸에 맞는 크기</b>를 받습니다.</p>''',
  do=ul([
    "칸에 <b><code>aspect-ratio</code></b> 를 걸고 <code>cover</code> 로 채우기",
    "<code>width</code>·<code>height</code> 를 적어 <b>자리를 예약</b>하기",
    "<code>srcset</code> 으로 <b>칸에 맞는 크기</b> 받기",
  ]),
  dont=ul([
    "<code>fill</code> 로 늘려 맞추기 — <b>얼굴이 찌그러진다</b>",
    "크기를 안 적어 두기 — <b>자리가 튄다</b>",
    "원본을 그대로 쓰기 — 76px 칸에 2000px 사진",
    "빈 자리를 <b>회색 네모</b>로만 두기 — 왜 없는지 한 줄 적는다",
  ]),
  instead='사람·조직이면 <a href="avatar.html">아바타</a>, 뜻의 기호면 <a href="icon.html">아이콘</a>, 비율 자체는 <a href="aspectratio.html">종횡비</a>, 불러오는 중은 <a href="skeleton.html">스켈레톤</a>.',
  cases=cases([
    (box(pic(100, 56, -12, 0), "상품 목록", "", True), "상품 목록", "<b>같은 비</b>로 가지런히"),
    (box(pic(76, 78, 0, -22), "사람 목록", "", True), "사람 목록", "<b>위쪽</b>을 남긴다"),
    (box(pic(76, 42, 0, 7), "작품 · 도면", "", None), "원본이 중요할 때", "<b>여백</b>을 받아들인다"),
  ]),
  code_lede="칸의 비를 못 박고 <code>cover</code> 로 채웁니다. 크기를 적어 두는 것이 자리 예약입니다.",
  code='''&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"/p/2411.jpg"</span> <span class="a">width</span>=<span class="s">"320"</span> <span class="a">height</span>=<span class="s">"240"</span>
     <span class="a">srcset</span>=<span class="s">"/p/2411@1x.jpg 320w, /p/2411@2x.jpg 640w"</span>
     <span class="a">sizes</span>=<span class="s">"(max-width: 600px) 45vw, 160px"</span>
     <span class="a">alt</span>=<span class="s">"한빛아웃도어 등산화"</span> <span class="a">loading</span>=<span class="s">"lazy"</span>&gt;

.thumb {
  <span class="a">aspect-ratio</span>: <span class="a">4</span> / <span class="a">3</span>;      <span class="c">/* 칸의 비를 못 박는다 */</span>
  <span class="a">object-fit</span>: cover;       <span class="c">/* 넘치는 쪽을 자른다 */</span>
  <span class="a">object-position</span>: center; <span class="c">/* 인물이면 top */</span>
  <span class="a">width</span>: <span class="a">100%</span>; <span class="a">background</span>: <span class="a">var</span>(--bg);
}''',
  keys=kbd([
    ("<code>alt</code>", "뜻이 있으면 적고, 장식이면 <b>빈 문자열</b>로 둔다"),
    ("링크 속 썸네일", "같은 링크에 글이 있으면 그림 <code>alt</code> 는 <b>비운다</b> — 두 번 읽힌다"),
    ("<code>loading=\"lazy\"</code>", "화면 밖 그림은 <b>나중에</b> 받는다"),
    ("<code>decoding=\"async\"</code>", "그림 풀기를 기다리지 않는다"),
    ("<code>aspect-ratio</code>", "크기를 못 적을 때 <b>자리를 잡는</b> 다른 길"),
    ("확인하는 법", "네트워크를 느리게 걸고 <b>글이 튀는지</b> 본다"),
  ]),
  backend=rows([
    ("여러 크기로 내려 준다", "원본 하나만 주면 화면이 <b>큰 그림을 줄여</b> 쓰게 됩니다 — 썸네일 크기를 미리 만들어 두는 편이 낫습니다."),
    ("크기를 같이", "<code>width</code>·<code>height</code> 가 응답에 있으면 화면이 <b>자리를 예약</b>할 수 있습니다."),
    ("포컬 포인트", "<code>focal: {x: 0.5, y: 0.3}</code> 같은 값이 있으면 <b>어디를 남길지</b>를 사진마다 다르게 둘 수 있습니다."),
  ]),
  plat_lede="<b>칸에 맞춰 자른다</b>는 생각은 어디서나 같습니다.",
  plats=plats([
    ("웹", "object-fit",
     box(pic(100, 56, -12, 0), "cover", "", True, "110px"),
     "<code>object-fit</code> 과 <code>aspect-ratio</code> 두 줄이면 끝납니다."),
    ("iOS", "contentMode",
     '''              <div class="phone" role="img" aria-label="iOS 썸네일 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>.scaledToFill()</code> 이 cover, <code>.scaledToFit()</code> 이 contain 입니다."),
    ("안드로이드", "scaleType",
     '''              <div class="phone" role="img" aria-label="안드로이드 썸네일 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="aspect-ratio:1;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>centerCrop</code> 이 cover, <code>fitCenter</code> 가 contain 입니다. 이름만 다릅니다."),
  ]),
  plat_note="이름은 셋 다 다른데 <b>하는 일은 같습니다</b> — cover / contain 두 갈래입니다. 앱 쪽은 이미지 불러오기 라이브러리가 <b>크기별 캐시</b>까지 맡아 주는 반면, 웹은 <code>srcset</code> 으로 직접 적어 줘야 합니다. 그 대신 웹에는 <code>aspect-ratio</code> 로 <b>자리를 미리 잡는</b> 간단한 길이 있어, 자리 튐만은 한 줄로 막을 수 있습니다.",
  siblings=siblings("thumbnail"),
  related='''        <li><a href="aspectratio.html"><b>종횡비</b><em>1부</em></a></li>
        <li><a href="avatar.html"><b>아바타</b><em>5부</em></a></li>
        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="alttext.html"><b>대체 텍스트</b><em>12부</em></a></li>''',
)
