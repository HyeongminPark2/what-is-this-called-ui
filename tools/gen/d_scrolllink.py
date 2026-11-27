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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">읽은 만큼 막대 — 내가 어디쯤인가</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">붙박이 머리말 — position: sticky</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">시차 배경 — 배경이 다른 속도로</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">스크롤 가로채기 — 굴린 만큼 안 간다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-timeline · IntersectionObserver</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">모션 줄이기에서 연출만 끄고 막대는 남긴다</div>
                </div>
              </div>'''

D = dict(
  slug="scrolllink", ko="스크롤 연동", en="Scroll-linked animation",
  desc="굴림에 맞춰 움직이는 것들. 쓸모 있는 둘과 조심할 둘, 그리고 가로채기를 쓰지 않는 이유.",
  lede="굴림에 <b>맞춰</b> 움직이는 것들. 쓸모 있는 것과 멀미를 부르는 것이 한 이름 아래 섞여 있습니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>굴려 보세요. <b>읽은 만큼 막대</b>와 <b>붙박이 머리말</b>은 '내가 어디쯤인지'를 알려 줘
          쓸모가 분명합니다.<br>
          <b>스크롤 가로채기</b>를 골라 굴려 보면 굴린 만큼 안 갑니다 — <b>기기가 고장 난 느낌</b>이
          어떤 것인지 바로 알 수 있습니다. <b>모션 줄이기</b>를 켜면 연출 쪽만 멎습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스크롤 연동, 시차 스크롤, 스크롤 애니메이션, 스크롤 가로채기"),
    ("영어", "scroll-linked animation, parallax, scroll-driven animation, scrolljacking"),
    ("같이 쓰는 말",
     "배경이 다른 속도로 움직이는 것이 <b>패럴랙스</b>(parallax), "
     "굴림에 맞춰 재생되는 애니메이션이 <b>스크롤 드리븐</b>입니다. "
     "굴린 양과 다르게 움직이게 가로채는 것을 <b>스크롤재킹</b>이라 하고 "
     "거의 늘 나쁜 뜻으로 씁니다. "
     "요소가 화면에 들어온 것을 아는 장치가 <code>IntersectionObserver</code>입니다."),
    ("자주 잘못 부름",
     "<b>스티키</b> — <a href=\"../items/sticky.html\">스티키</a>는 <b>붙어 있는</b> 것이지 움직이는 것이 아닙니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 <b>더 받아오는</b> 일입니다.<br>"
     "<b>애니메이션</b> — 시간에 따라 도는 것과 <b>굴림에 매인</b> 것은 다릅니다."),
  ]),
  axes=ax("스크롤 연동"),
  oneline="<b>굴림은 사용자의 것입니다.</b> 거기에 매달 수는 있어도 <b>빼앗으면</b> 안 됩니다.",
  s4_title="네 가지", s4_hint="쓸모 있는 것과 아닌 것",
  states=states([
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:62%;height:4px;background:var(--accent)"></span>' + LINES,
         "152px", "72px", "읽은 비율을 그대로", True),
     "읽은 만큼 막대 ✓", "<b>자리 이동이 거의 없다.</b> 줄이기에서도 남긴다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:14px;background:var(--bg);border-bottom:1px solid var(--line);font-size:7px;color:var(--fg-muted);display:grid;place-items:center">11월 정산</span>' + LINES,
         "152px", "72px", "position: sticky", True),
     "붙박이 머리말 ✓", "움직임이 아니라 <b>고정</b>이다"),
    (box('<span style="position:absolute;left:0;right:0;top:-8px;height:34px;background:var(--accent);opacity:.8"></span>'
         '<span style="position:absolute;left:6px;right:6px;top:30px;height:5px;border-radius:2px;background:var(--ink-100)"></span>',
         "152px", "72px", "배경이 다른 속도로"),
     "시차 배경 △", "크게 쓰면 <b>멀미를 부른다</b>"),
    (box(LINES + '<span style="position:absolute;right:4px;top:4px;font-size:7px;color:var(--danger)">↓ 한 장씩</span>',
         "152px", "72px", "굴린 만큼 안 간다", False),
     "가로채기 ✕", "<b>기기가 고장 난 느낌</b>을 준다"),
    (box('<span style="position:absolute;left:6px;top:14px;width:22px;height:22px;border-radius:4px;background:var(--accent);opacity:.35"></span>'
         '<span style="position:absolute;left:34px;top:14px;width:22px;height:22px;border-radius:4px;background:var(--accent)"></span>' ,
         "152px", "72px", "화면에 들어오면 나타난다"),
     "들어올 때 나타나기", "<b>한 번만.</b> 다시 굴릴 때마다면 방해다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:62%;height:4px;background:var(--accent)"></span>' + LINES,
         "152px", "72px", "줄이기 — 막대는 남는다", True),
     "모션 줄이기에서", "연출은 끄고 <b>알려 주는 것은 남긴다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("읽은 만큼 막대", "진행 비율", "<b>자리 이동이 없다.</b> 가장 안전하다"),
    ("붙박이", "position: sticky", "지금 어느 묶음인지 — <a href=\"../items/sticky.html\">스티키</a>"),
    ("시차", "다른 속도", "크게 쓰면 <b>멀미</b>. 줄이기에서 끈다"),
    ("가로채기", "굴린 만큼 안 감", "<b>쓰지 않는다.</b> 손맛을 빼앗는다"),
    ("재는 법", "scroll-timeline", "CSS 로도 되고 <code>IntersectionObserver</code>로도 된다"),
    ("줄이기", "연출만 끈다", "막대·붙박이는 <b>남긴다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>굴림은 사용자가 쥔 몇 안 되는 손잡이입니다.</b>
          화면이 어떻게 생겼든 굴리면 그만큼 내려간다는 것이
          모두가 믿고 있는 약속이라,
          그걸 깨면 <b>기기가 고장 난 것처럼</b> 느껴집니다.
          가로채기가 유독 미움받는 이유가 이것입니다 —
          예뻐 보이는 연출 하나를 위해 <b>가장 기본적인 약속</b>을 깨기 때문입니다.
          굴림에 <b>매다는</b> 것은 괜찮고, <b>빼앗는</b> 것은 안 됩니다.</p>''',
  do=ul([
    "긴 글에 <b>읽은 만큼 막대</b>",
    "묶음이 있는 목록에 <b>붙박이 머리말</b>",
    "화면에 들어올 때 <b>한 번</b> 나타나게",
  ]),
  dont=ul([
    "<b>스크롤 가로채기</b> — 거의 늘 미움받는다",
    "크게 움직이는 시차 — <b>멀미를 부른다</b>",
    "굴릴 때마다 다시 나타나기 — <b>두 번째부터는 방해</b>다",
    "굴림에 매단 것을 <b>읽는 데 꼭 필요한</b> 정보로 두기",
  ]),
  instead='붙어 있기만 하면 <a href="../items/sticky.html">스티키</a>, 더 받아오면 <a href="../items/infinite.html">무한 스크롤</a>, 진행을 알리면 <a href="../items/progress.html">프로그레스 바</a>.',
  cases=cases([
    (box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:40%;height:4px;background:var(--accent)"></span>' + LINES, "150px", "68px"),
     "긴 글", "<b>얼마나 남았나</b>를 알려 준다"),
    (box('<span style="position:absolute;left:0;right:0;top:0;height:14px;background:var(--bg);border-bottom:1px solid var(--line);font-size:7px;color:var(--fg-muted);display:grid;place-items:center">11월</span>' + LINES, "150px", "68px"),
     "날짜별 목록", "지금 <b>어느 달</b>인지"),
    (box('<span style="position:absolute;inset:6px;border:1px dashed var(--danger);border-radius:5px;display:grid;place-items:center;font-size:8px;color:var(--danger)">가로채기</span>', "150px", "68px"),
     "안 쓰는 것", "<b>굴림을 빼앗지 않는다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 연출의 계약서",
  code_lede="CSS 로 굴림에 매달고, <b>줄이기에서는 끕니다</b>.",
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
  keys=kbd([
    ("굴림을 가로채지 않는다", "<code>preventDefault</code>로 막으면 <b>키보드 굴림까지</b> 막힌다"),
    ("<code>animation-timeline: scroll()</code>", "CSS 로 매단다. <b>자바스크립트보다 매끄럽다</b>"),
    ("<code>IntersectionObserver</code>", "<code>scroll</code> 이벤트를 매번 듣는 것보다 가볍다"),
    ("한 번만", "<code>unobserve</code>로 끊는다. 굴릴 때마다면 <b>읽기를 방해</b>한다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>", "시차는 끄고 <b>막대·붙박이는 남긴다</b>"),
    ("읽는 데 필요한 것은 매달지 않는다", "굴려야 나타나는 글은 <b>스크린 리더에서도</b> 안 나타날 수 있다"),
  ]),
  backend=rows([
    ("굴림으로 더 받을 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 섞이면 <b>높이가 계속 변해</b> 막대가 튑니다."),
    ("들어올 때 받기", "화면에 들어온 것만 받으면 가볍지만, <b>빨리 굴리면</b> 요청이 몰립니다. 디바운스를 겁니다."),
    ("검색 엔진", "굴려야 나타나는 내용은 <b>안 보일 수</b> 있습니다. 중요한 글은 처음부터 둡니다."),
  ]),
  plat_lede="<b>웹에서 가장 흔하고 가장 자주 과합니다</b>.",
  plats=plats([
    ("웹", "scroll-timeline · IO",
     box('<span style="position:absolute;left:0;right:0;top:0;height:4px;background:var(--line)"></span>'
         '<span style="position:absolute;left:0;top:0;width:50%;height:4px;background:var(--accent)"></span>', "110px", "56px"),
     "CSS 로 굴림에 매달 수 있게 됐습니다. <b>홍보 사이트</b>에서 가장 많이 쓰고 가장 자주 과합니다."),
    ("iOS", "스크롤에 매단 효과",
     '''              <div class="phone" role="img" aria-label="iOS 큰 제목 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;font-size:8px;font-weight:700">정산</div></div></div>''',
     "큰 제목이 굴리면 작아져 앱바에 붙는 것이 <b>OS 기본</b>입니다. 가로채기는 거의 안 씁니다."),
    ("안드로이드", "CollapsingToolbar",
     '''              <div class="phone" role="img" aria-label="안드로이드 접히는 툴바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px;height:14px;background:var(--accent)"></div></div></div>''',
     "<b>접히는 툴바</b>가 규격으로 있습니다. 굴림에 매달되 <b>굴림을 빼앗지는 않습니다</b>."),
  ]),
  plat_note="\"스크롤하면 뭔가 움직이게\"라는 요청은 대개 <b>홍보 사이트의 기억</b>에서 옵니다. 제품 화면에서는 <b>읽은 만큼 막대</b>와 <b>붙박이 머리말</b> 둘이 거의 전부이고, 나머지는 멀미와 성능을 사면서 얻는 것이 적습니다. 요청을 받으면 <b>\"무엇을 알려 주려는 건가요\"</b>를 한 번 물어보는 편이 좋습니다.",
  siblings=siblings("scrolllink"),
  related='''        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="cheap.html"><b>무엇을 움직이나</b><em>9부</em></a></li>''',
)
