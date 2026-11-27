# -*- coding: utf-8 -*-
from ax9 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(inner, w="152px", h="72px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="height:' + h + ';position:relative;border:1px solid ' + col + ';border-radius:6px;'
            'background:var(--surface);overflow:hidden">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

LINES = ''.join('<span style="position:absolute;left:6px;right:6px;top:' + str(t) +
                'px;height:5px;border-radius:2px;background:var(--ink-100)"></span>'
                for t in (22, 32, 42, 52, 62))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">읽은 만큼 막대로 위치를 알려 줌</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">붙박이 머리말은 position: sticky</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">시차 배경은 배경이 다른 속도로 움직임</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">스크롤 가로채기는 굴린 만큼 안 내려감</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-timeline · IntersectionObserver</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">모션 줄이기에서는 연출만 끄고 막대는 남김</div>
                </div>
              </div>'''

D = dict(
  slug="scrolllink", ko="스크롤 연동", en="Scroll-linked animation",
  desc="스크롤에 맞춰 움직이는 것들을 다루는 항목입니다. 쓸모 있는 두 가지와 조심해야 할 두 가지, 그리고 스크롤 가로채기를 쓰지 않는 이유를 보여 줍니다.",
  lede="스크롤 연동은 사용자가 스크롤하는 만큼에 <b>맞춰</b> 요소를 움직이는 것입니다. 같은 이름 아래에 쓸모 있는 것과 멀미를 일으키는 것이 섞여 있습니다.",
  axes_lede="움직임은 화면에서 무엇이 바뀌었는지 사용자에게 <b>알려 주는</b> 역할을 합니다. 아래 네 가지를 따져 보면 움직임을 다루는 항목들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>스크롤해 보세요. <b>읽은 만큼 막대</b>와 <b>붙박이 머리말</b>은 사용자가 글의 어디쯤에 있는지 알려 주기 때문에
          쓸모가 분명합니다.<br>
          <b>스크롤 가로채기</b>를 고르고 스크롤해 보면 스크롤한 만큼 내려가지 않아서, <b>기기가 고장 난 것 같은 느낌</b>이
          어떤 것인지 바로 알 수 있습니다. <b>모션 줄이기</b>를 켜면 연출만 멈춥니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스크롤 연동, 시차 스크롤, 스크롤 애니메이션, 스크롤 가로채기"),
    ("영어", "scroll-linked animation, parallax, scroll-driven animation, scrolljacking"),
    ("같이 쓰는 말",
     "배경이 앞의 내용과 다른 속도로 움직이는 것을 <b>패럴랙스</b>(parallax), "
     "스크롤 위치에 맞춰 재생되는 애니메이션을 <b>스크롤 드리븐</b>이라고 합니다. "
     "스크롤 입력을 가로채서 사용자가 스크롤한 양과 다르게 움직이게 하는 것은 <b>스크롤재킹</b>이라고 하는데, "
     "대부분 나쁜 뜻으로 씁니다. "
     "요소가 화면에 들어왔는지 알려 주는 API는 <code>IntersectionObserver</code>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>스티키</b> — <a href=\"../items/sticky.html\">스티키</a>는 화면에 <b>붙어 있는</b> 것이지 움직이는 것이 아닙니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 스크롤이 끝에 닿으면 자료를 <b>더 받아오는</b> 기능입니다.<br>"
     "<b>애니메이션</b> — 시간에 따라 재생되는 애니메이션과 <b>스크롤 위치에 따라</b> 움직이는 것은 다릅니다."),
  ]),
  axes=ax("스크롤 연동"),
  oneline="<b>스크롤은 사용자가 직접 하는 조작입니다.</b> 스크롤 위치에 맞춰 무언가를 움직이는 것은 괜찮지만, 스크롤한 만큼 화면이 움직이지 않도록 <b>가로채면</b> 안 됩니다.",
  s4_title="스크롤에 맞춰 움직이는 것들", s4_hint="쓸모 있는 것과 조심하거나 피할 것",
  states=states([
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:62%;height:4px;background:var(--accent)"></span>' + LINES,
         "152px", "72px", "읽은 비율을 그대로 보여 줌", True),
     "읽은 만큼 막대 ✓", "<b>자리 이동이 거의 없어서</b> 모션 줄이기에서도 남깁니다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:14px;background:var(--bg);border-bottom:1px solid var(--line);font-size:7px;color:var(--fg-muted);display:grid;place-items:center">11월 정산</span>' + LINES,
         "152px", "72px", "position: sticky", True),
     "붙박이 머리말 ✓", "움직이는 것이 아니라 제자리에 <b>고정</b>된 것입니다"),
    (box('<span style="position:absolute;left:0;right:0;top:-8px;height:34px;background:var(--accent);opacity:.8"></span>'
         '<span style="position:absolute;left:6px;right:6px;top:30px;height:5px;border-radius:2px;background:var(--ink-100)"></span>',
         "152px", "72px", "배경이 다른 속도로 움직임"),
     "시차 배경 △", "크게 움직이면 <b>멀미를 일으킵니다</b>"),
    (box(LINES + '<span style="position:absolute;right:4px;top:4px;font-size:7px;color:var(--danger)">↓ 한 장씩</span>',
         "152px", "72px", "굴린 만큼 안 내려감", False),
     "스크롤 가로채기 ✕", "스크롤한 만큼 내려가지 않아서 <b>기기가 고장 난 것처럼</b> 느껴집니다"),
    (box('<span style="position:absolute;left:6px;top:14px;width:22px;height:22px;border-radius:4px;background:var(--accent);opacity:.35"></span>'
         '<span style="position:absolute;left:34px;top:14px;width:22px;height:22px;border-radius:4px;background:var(--accent)"></span>' ,
         "152px", "72px", "화면에 들어오면 나타남"),
     "화면에 들어올 때 나타나기", "<b>한 번만</b> 나타나게 합니다. 다시 스크롤할 때마다 나타나면 방해가 됩니다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:62%;height:4px;background:var(--accent)"></span>' + LINES,
         "152px", "72px", "모션 줄이기에서도 막대는 남음", True),
     "모션 줄이기를 켰을 때", "연출은 끄고 <b>위치를 알려 주는 것은 남깁니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("읽은 만큼 막대", "진행 비율", "<b>자리 이동이 없어서</b> 가장 안전합니다"),
    ("붙박이 머리말", "position: sticky", "지금 어느 묶음을 보고 있는지 알려 줍니다. 자세한 내용은 <a href=\"../items/sticky.html\">스티키</a>에 있습니다"),
    ("시차 배경", "다른 속도", "크게 움직이면 <b>멀미</b>를 일으키므로 모션 줄이기에서 끕니다"),
    ("스크롤 가로채기", "굴린 만큼 안 내려감", "<b>쓰지 않습니다.</b> 사용자가 스크롤한 만큼 화면이 움직이지 않기 때문입니다"),
    ("만드는 방법", "scroll-timeline", "CSS로도 만들 수 있고 <code>IntersectionObserver</code>로도 만들 수 있습니다"),
    ("모션 줄이기", "연출만 끔", "막대와 붙박이 머리말은 <b>남깁니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>스크롤은 사용자가 화면을 직접 다루는 몇 안 되는 조작입니다.</b>
          사용자는 화면이 어떻게 생겼든 스크롤한 만큼 내려간다고 기대하기 때문에,
          스크롤한 만큼 움직이지 않으면 <b>기기가 고장 난 것처럼</b> 느낍니다.
          스크롤 가로채기를 사용자들이 특히 싫어하는 이유도 여기에 있습니다.
          보기 좋은 연출 하나를 위해 <b>스크롤한 만큼 움직인다는 기본 동작</b>을 바꾸기 때문입니다.
          스크롤 위치에 <b>맞춰</b> 무언가를 움직이는 것은 괜찮지만, 스크롤 자체를 <b>가로채는</b> 것은 안 됩니다.</p>''',
  do=ul([
    "긴 글에 <b>읽은 만큼 막대</b>를 달 때",
    "묶음이 있는 목록에 <b>붙박이 머리말</b>을 둘 때",
    "요소가 화면에 들어올 때 <b>한 번</b> 나타나게 할 때",
  ]),
  dont=ul([
    "<b>스크롤 가로채기</b>를 쓸 때. 사용자 대부분이 불편해합니다",
    "시차를 크게 줄 때. <b>멀미를 일으킵니다</b>",
    "스크롤할 때마다 다시 나타나게 할 때. <b>두 번째부터는 방해</b>가 됩니다",
    "스크롤해야 나타나는 요소에 <b>읽는 데 꼭 필요한</b> 정보를 담을 때",
  ]),
  instead='화면에 붙어 있기만 하면 되는 것은 <a href="../items/sticky.html">스티키</a>로 충분합니다. 스크롤이 끝에 닿을 때 자료를 더 받아오는 것은 <a href="../items/infinite.html">무한 스크롤</a>이고, 작업이 얼마나 진행됐는지 알리려면 <a href="../items/progress.html">프로그레스 바</a>를 씁니다.',
  cases=cases([
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:40%;height:4px;background:var(--accent)"></span>' + LINES, "150px", "68px"),
     "긴 글에 읽은 만큼 막대 달기", "글이 <b>얼마나 남았는지</b> 알려 줍니다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:14px;background:var(--bg);border-bottom:1px solid var(--line);font-size:7px;color:var(--fg-muted);display:grid;place-items:center">11월</span>' + LINES, "150px", "68px"),
     "날짜별 목록에 붙박이 머리말 두기", "지금 <b>어느 달</b>을 보고 있는지 알려 줍니다"),
    (box('<span style="position:absolute;inset:6px;border:1px dashed var(--danger);border-radius:5px;display:grid;place-items:center;font-size:8px;color:var(--danger)">가로채기</span>', "150px", "68px"),
     "스크롤 가로채기는 쓰지 않기", "<b>스크롤을 가로채지 않습니다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="CSS로 애니메이션을 스크롤 위치에 연결하고, 연출은 <b>모션 줄이기에서 끕니다</b>.",
  code='''<span class="c">/* 읽은 만큼 막대 — CSS 만으로 */</span>
@keyframes grow { from { <span class="a">transform</span>: scaleX(<span class="a">0</span>); } to { <span class="a">transform</span>: scaleX(<span class="a">1</span>); } }
.progress {
  <span class="a">transform-origin</span>: left;
  <span class="a">animation</span>: grow linear;
  <span class="a">animation-timeline</span>: scroll();   <span class="c">/* 시간이 아니라 굴림에 매단다 */</span>
}

<span class="c">/* 화면에 들어올 때 한 번 */</span>
<span class="k">const</span> io = <span class="k">new</span> IntersectionObserver(es =&gt; es.forEach(e =&gt; {
  <span class="k">if</span> (e.isIntersecting) { e.target.classList.add(<span class="s">'in'</span>); io.unobserve(e.target); }
}), { threshold: <span class="a">.2</span> });

<span class="c">/* 줄이기에서는 연출만 끈다 — 막대는 남긴다 */</span>
@media (prefers-reduced-motion: reduce) {
  .parallax { <span class="a">transform</span>: none !important; }
  .reveal   { <span class="a">opacity</span>: <span class="a">1</span>; <span class="a">transform</span>: none; }
}''',
  keys_heads="<th>알아 둘 규칙</th><th>자세한 내용</th>",
  keys=kbd([
    ("스크롤을 가로채지 않기", "<code>preventDefault</code>로 스크롤을 막으면 <b>키보드로 하는 스크롤까지</b> 막힙니다"),
    ("<code>animation-timeline: scroll()</code>", "CSS만으로 애니메이션을 스크롤 위치에 연결합니다. <b>자바스크립트로 만들 때보다 매끄럽습니다</b>"),
    ("<code>IntersectionObserver</code>", "<code>scroll</code> 이벤트를 매번 받아 처리하는 것보다 가볍습니다"),
    ("한 번만 나타나게 하기", "한 번 나타난 뒤에는 <code>unobserve</code>로 관찰을 끊습니다. 스크롤할 때마다 나타나면 <b>읽기를 방해</b>합니다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>를 켰을 때", "시차는 끄고 <b>막대와 붙박이 머리말은 남깁니다</b>"),
    ("읽는 데 필요한 글은 스크롤에 매달지 않기", "스크롤해야 나타나는 글은 <b>스크린 리더에서도</b> 나타나지 않을 수 있습니다"),
  ]),
  backend=rows([
    ("스크롤하며 자료를 더 받을 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 함께 쓰면 문서 <b>높이가 계속 바뀌어서</b> 읽은 만큼 막대가 갑자기 줄어듭니다."),
    ("화면에 들어온 것만 받을 때", "화면에 들어온 것만 받으면 가볍지만, <b>빠르게 스크롤하면</b> 요청이 한꺼번에 몰립니다. 그래서 디바운스를 겁니다."),
    ("검색 엔진에 보이지 않는 내용", "스크롤해야 나타나는 내용은 검색 엔진에 <b>보이지 않을 수</b> 있습니다. 중요한 글은 처음부터 화면에 둡니다."),
  ]),
  plat_lede="스크롤 연동은 <b>웹에서 가장 흔하고, 웹에서 가장 자주 지나치게 쓰입니다</b>.",
  plats=plats([
    ("웹", "scroll-timeline · IO",
     box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:50%;height:4px;background:var(--accent)"></span>', "110px", "56px"),
     "이제 CSS만으로 애니메이션을 스크롤 위치에 연결할 수 있습니다. <b>홍보 사이트</b>에서 가장 많이 쓰고, 지나치게 쓰는 경우도 가장 많습니다."),
    ("iOS", "스크롤에 매단 효과",
     '''              <div class="phone" role="img" aria-label="iOS 큰 제목 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;font-size:8px;font-weight:700">정산</div></div></div>''',
     "스크롤하면 큰 제목이 작아지며 앱바에 붙는 것이 <b>OS 기본 동작</b>입니다. 스크롤 가로채기는 거의 쓰지 않습니다."),
    ("안드로이드", "CollapsingToolbar",
     '''              <div class="phone" role="img" aria-label="안드로이드 접히는 툴바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px;height:14px;background:var(--accent)"></div></div></div>''',
     "<b>접히는 툴바</b>가 규격으로 있습니다. 툴바가 스크롤에 맞춰 접히지만 <b>스크롤 자체를 가로채지는 않습니다</b>."),
  ]),
  plat_note="\"스크롤하면 뭔가 움직이게 해 주세요\"라는 요청은 대개 <b>예전에 본 홍보 사이트</b>를 떠올리며 하는 말입니다. 제품 화면에서 쓸모 있는 것은 <b>읽은 만큼 막대</b>와 <b>붙박이 머리말</b> 두 가지가 거의 전부이고, 나머지는 멀미와 성능 저하를 감수하는 것에 비해 얻는 것이 적습니다. 이런 요청을 받으면 <b>\"이 움직임으로 무엇을 알려 주려는 건가요?\"</b>라고 한 번 물어보는 편이 좋습니다.",
  siblings=siblings("scrolllink"),
  related='''        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="cheap.html"><b>무엇을 움직이나</b><em>9부</em></a></li>''',
)
