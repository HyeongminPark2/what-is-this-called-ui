# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(inner, w="152px", h="74px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="height:' + h + ';position:relative;border:1px solid ' + col + ';border-radius:6px;'
            'background:var(--surface);overflow:hidden">' + inner + '</div>'
            + ('<span style="font-family:var(--mono);font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

PAGES = ''.join('<div style="height:36px;border-bottom:1px solid var(--line);display:grid;place-items:center;font-size:11px;color:var(--fg-muted)">' + str(i) + '</div>' for i in range(1, 5))
CARDS = ''.join('<span style="flex:none;width:48px;height:34px;border-radius:4px;background:var(--accent-soft);border:1px solid var(--accent)"></span>' for _ in range(4))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">scroll-snap-type   칸 단위로 멈추게 함</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-snap-align   멈출 기준 (start·center)</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">overscroll-behavior: contain   바깥이 밀리지 않음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-behavior: smooth   이동할 때 부드럽게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-margin   붙박이 머리말에 가리지 않게 띄움</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">스크롤 양은 두고 멈출 자리만 정함</div>
                </div>
              </div>'''

D = dict(
  slug="scrollbehavior", ko="스크롤 동작", en="Scroll behavior",
  desc="스냅, 체이닝, 부드러운 스크롤, scroll-margin처럼 스크롤 자체를 다루는 CSS 네 가지를 보여 주는 항목입니다.",
  lede="스크롤 동작은 스크롤 자체를 다루는 CSS 값들입니다. 스크롤이 <b>칸 단위로 멈추게</b> 하거나 <b>바깥 페이지까지 밀리지 않게</b> 하는 일을 CSS 한 줄로 할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>스냅</b>을 켜면 세로 상자와 가로 줄 모두에서 스크롤이 칸 단위로 멈춥니다.<br>
          <b>바깥 페이지도 밀리게 하기</b>를 끄면 안쪽을 끝까지 스크롤해도 <b>바깥 페이지가 따라 움직이지 않는데</b>,
          이 설정은 <a href="../items/modal.html">모달</a> 안에서 특히 쓸모가 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스크롤 동작, 스냅, 스크롤 체이닝, 부드러운 굴림"),
    ("영어", "scroll snap, overscroll behavior, scroll chaining, smooth scroll"),
    ("같이 쓰는 말",
     "스크롤이 칸 단위로 멈추게 하는 것은 <b>스크롤 스냅</b>, "
     "안쪽을 끝까지 스크롤했을 때 바깥이 따라 움직이는 것은 <b>스크롤 체이닝</b>이라고 부릅니다. "
     "끝에서 더 당기면 튕기는 효과는 <b>바운스</b>·<b>러버밴딩</b>이라고 하며 "
     "<code>overscroll-behavior: none</code>으로 막습니다. "
     "앵커 링크로 이동할 때 목표가 붙박이 머리말에 가리지 않게 띄우는 값은 <code>scroll-margin</code>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>스크롤 연동</b> — <a href=\"scrolllink.html\">스크롤 연동</a>은 스크롤 위치에 따라 <b>다른 무언가를 움직이는</b> 일이고, 스크롤 동작은 <b>스크롤 자체</b>를 다룹니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 목록 끝에 닿으면 데이터를 더 받아오는 일입니다.<br>"
     "<b>스크롤 가로채기</b> — 사용자가 스크롤한 양과 다르게 화면을 움직이는 것으로, <b>이 항목에서 다루는 값들과는 다릅니다</b>."),
  ]),
  s4_title="스크롤을 다루는 값", s4_hint="값마다 달라지는 스크롤의 움직임",
  do_title="스크롤 동작을 따로 정하는 경우",
  dont_title="스크롤 동작을 다룰 때 피할 것",
  states=states([
    (box(PAGES, "152px", "74px", "scroll-snap-type: none"), "스냅을 걸지 않았을 때", "<b>아무 위치에서나</b> 멈춥니다"),
    (box(PAGES, "152px", "74px", "y mandatory로 칸 단위 멈춤", True), "세로로 스냅을 걸었을 때", "<b>한 장씩</b> 멈춥니다"),
    (box('<div style="display:flex;gap:5px;padding:18px 6px;overflow:hidden">' + CARDS + '</div>', "152px", "74px", "x mandatory로 가로 캐러셀", True),
     "가로로 스냅을 걸었을 때", "사진첩이나 <b>캐러셀</b>에 씁니다"),
    (box('<div style="position:absolute;inset:6px;border:1px solid var(--accent);border-radius:4px;display:grid;place-items:center;font-size:9px;color:var(--accent)">contain</div>',
         "152px", "74px", "바깥이 밀리지 않음", True),
     "바깥으로 이어지는 스크롤을 막을 때", "<a href=\"../items/modal.html\">모달</a> 안에서 씁니다"),
    (box('<div style="position:absolute;left:0;right:0;top:0;height:16px;background:var(--bg);border-bottom:1px solid var(--line);font-size:8px;color:var(--fg-muted);display:grid;place-items:center">붙박이 머리말</div>'
         '<div style="position:absolute;left:6px;right:6px;top:22px;height:12px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div>',
         "152px", "74px", "scroll-margin-top으로 띄움", True),
     "<code>scroll-margin</code>으로 띄울 때", "앵커로 이동했을 때 목표가 머리말에 <b>가리지 않게</b> 합니다"),
    (box('<div style="position:absolute;inset:6px;border:1px dashed var(--danger);border-radius:4px;display:grid;place-items:center;font-size:8.5px;color:var(--danger)">스크롤을 가로챔</div>',
         "152px", "74px", "스크롤한 만큼 움직이지 않음", False),
     "스크롤을 가로챌 때", "<b>쓰지 않습니다</b>. 자세한 내용은 <a href=\"scrolllink.html\">스크롤 연동</a>에서 다룹니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스냅", "scroll-snap-type", "스크롤이 <b>칸 단위</b>로 멈춥니다. 축과 세기를 함께 적습니다"),
    ("맞춤", "scroll-snap-align", "칸의 <b>어디에</b> 맞춰 멈출지 start · center 같은 값으로 정합니다"),
    ("체이닝", "overscroll-behavior", "<code>contain</code>으로 두면 <b>바깥이 밀리지 않습니다</b>"),
    ("부드러운 이동", "scroll-behavior", "앵커나 버튼으로 이동할 때만 적용되고, <b>사용자가 직접 스크롤할 때는 영향을 주지 않습니다</b>"),
    ("scroll-margin", "가리지 않게 띄우기", "<a href=\"../items/sticky.html\">붙박이 머리말</a> 높이만큼 띄웁니다"),
    ("가로채기", "쓰지 않음", "사용자가 스크롤한 <b>양</b>을 바꾸면 화면이 고장 난 것처럼 느껴집니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>scroll-margin</code>은 작은 값이지만 <b>자주 빠뜨립니다</b>.
          붙박이 머리말이 있는 화면에서 앵커 링크로 이동하면
          목표 요소가 <b>머리말 뒤에 가려져서</b>,
          링크를 눌렀는데 아무 일도 일어나지 않은 것처럼 보입니다.
          목표 요소에 <code>scroll-margin-top</code>을 머리말 높이만큼 주면 해결됩니다.
          이 설정은 <b>키보드로 건너뛰기</b>를 쓰는 사람에게도 똑같이 필요한데,
          <a href="../items/focus.html">포커스</a>가 머리말에 가려지면 지금 어디에 있는지 알 수 없기 때문입니다.</p>''',
  do=ul([
    "<b>캐러셀이나 사진첩</b>에 스냅을 걸 때",
    "<a href=\"../items/modal.html\">모달</a>·<a href=\"../items/drawer.html\">드로어</a> 안의 스크롤이 바깥으로 이어지지 않게 할 때. <code>overscroll-behavior: contain</code>을 씁니다",
    "붙박이 머리말이 있는 화면에서 앵커 링크를 쓸 때. <code>scroll-margin-top</code>을 줍니다",
  ]),
  dont=ul([
    "긴 글에 스냅을 걸 때. 읽는 도중에 <b>스크롤이 칸 단위로 멈춰서 답답합니다</b>",
    "스크롤되는 <b>양</b>을 바꿀 때. 화면이 고장 난 것처럼 느껴집니다",
    "<code>scroll-behavior: smooth</code>를 전역으로 걸 때. <a href=\"reducedmotion.html\">모션 줄이기</a> 설정에서는 꺼야 합니다",
    "<code>overscroll-behavior: none</code>을 본문에 걸 때. <b>당겨서 새로고침</b>이 막힙니다",
  ]),
  instead='스크롤 위치에 따라 다른 요소를 움직이려면 <a href="scrolllink.html">스크롤 연동</a>을, 머리말을 위에 붙여 두려면 <a href="../items/sticky.html">스티키</a>를 봅니다. 목록 끝에 닿았을 때 데이터를 더 받아오는 일은 <a href="../items/infinite.html">무한 스크롤</a>에서 다룹니다.',
  cases=cases([
    (box('<div style="display:flex;gap:5px;padding:18px 6px;overflow:hidden">' + CARDS + '</div>', "150px", "70px", "x mandatory + center"),
     "가로 캐러셀을 칸 단위로 멈추기", "스냅이 <b>가장 잘 맞는</b> 자리입니다"),
    (box('<div style="position:absolute;inset:6px;background:var(--surface);border:1px solid var(--line);border-radius:4px"></div>', "150px", "70px", "모달 안 contain"),
     "모달 안 목록의 스크롤 가두기", "목록을 끝까지 스크롤해도 바깥 페이지가 <b>밀리지 않습니다</b>"),
    (code(['h2 { scroll-margin-top: 64px }'], "150px", "머리말 높이만큼", True), "앵커로 이동한 목표가 가리지 않게 하기", "목표가 머리말에 <b>가리지 않습니다</b>"),
  ]),
  s8_title="최소 코드와 키보드", s8_hint="스크롤 동작을 다룰 때 지킬 것",
  keys_heads="<th>키와 설정</th><th>그때 일어나야 하는 일</th>",
  code_lede="스냅은 두 줄, 체이닝 막기는 한 줄이면 됩니다.",
  code='''<span class="c">/* 가로 캐러셀 */</span>
.carousel { <span class="a">display</span>: flex; <span class="a">overflow-x</span>: auto; <span class="a">scroll-snap-type</span>: x mandatory; }
.carousel &gt; * { <span class="a">flex</span>: none; <span class="a">scroll-snap-align</span>: center; }

<span class="c">/* 모달 안에서 바깥이 밀리지 않게 */</span>
.modal__body { <span class="a">overflow</span>: auto; <span class="a">overscroll-behavior</span>: contain; }

<span class="c">/* 붙박이 머리말에 가리지 않게 */</span>
<span class="t">h2</span> { <span class="a">scroll-margin-top</span>: <span class="a">64px</span>; }

<span class="c">/* 앵커로 이동할 때만 부드럽게. 모션 줄이기에서는 끈다 */</span>
<span class="t">html</span> { <span class="a">scroll-behavior</span>: smooth; }
@media (prefers-reduced-motion: reduce) { <span class="t">html</span> { <span class="a">scroll-behavior</span>: auto; } }''',
  keys=kbd([
    ("<kbd>PageDown</kbd>·<kbd>Home</kbd>", "스냅을 걸어도 <b>키보드로 하는 스크롤은 그대로</b> 동작해야 합니다"),
    ("가로 캐러셀에서 <kbd>Tab</kbd>을 누를 때", "칸 안에 누를 것이 있으면 <b>초점이 옮겨 갈 때 저절로 스크롤됩니다</b>"),
    ("<code>scroll-margin</code>을 주었을 때", "<a href=\"../items/focus.html\">초점</a>이 머리말에 가리는 것도 함께 막습니다"),
    ("<code>scroll-behavior: smooth</code>를 쓸 때", "<a href=\"reducedmotion.html\">모션 줄이기</a> 설정에서는 <code>auto</code>로 되돌립니다"),
    ("<code>overscroll-behavior: none</code>을 쓸 때", "<b>당겨서 새로고침</b>까지 막기 때문에 본문에는 쓰지 않습니다"),
    ("<code>mandatory</code>와 <code>proximity</code> 중에 고를 때", "<code>mandatory</code>는 항상 칸에 맞춰 멈추기 때문에, 칸이 화면보다 크면 <b>지나갈 수 없는</b> 자리가 생길 수 있습니다"),
  ]),
  backend=rows([
    ("스냅과 무한 스크롤을 함께 쓸 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 함께 쓰면 <b>칸이 늘어날 때마다</b> 멈추는 자리가 바뀝니다."),
    ("돌아왔을 때 스크롤 위치 되살리기", "화면에 돌아왔을 때 스크롤 위치를 되살리려면 목록을 <b>다 그린 뒤에</b> 해야 합니다(<a href=\"searchresults.html\">검색 결과 화면</a> 참고)."),
  ]),
  plat_lede="<b>스냅은 웹보다 앱에서 먼저</b> 흔하게 쓰였습니다.",
  plats=plats([
    ("웹", "CSS 스크롤 스냅",
     box('<div style="display:flex;gap:4px;padding:12px 5px;overflow:hidden">' + CARDS + '</div>', "110px", "56px"),
     "자바스크립트 없이 CSS만으로 만들 수 있습니다. 예전에는 캐러셀을 <b>모두 직접 코드로</b> 짰습니다."),
    ("iOS", "isPagingEnabled",
     '''              <div class="phone" role="img" aria-label="iOS 페이징 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:20px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "한 줄로 페이지 단위 스크롤을 만들 수 있고, <b>바운스</b>도 OS가 기본으로 넣어 줍니다."),
    ("안드로이드", "SnapHelper · Pager",
     '''              <div class="phone" role="img" aria-label="안드로이드 페이저 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:20px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<code>PagerSnapHelper</code>·Compose의 <code>HorizontalPager</code>가 같은 일을 합니다."),
  ]),
  plat_note="예전에는 \"캐러셀 만들어 주세요\"라는 요청을 받으면 라이브러리를 들여야 했지만, 지금은 <b>CSS 세 줄</b>이면 됩니다. 그래서 라이브러리를 고르기 전에 스냅으로 되는지 먼저 보는 편이 좋습니다. 키보드와 스크린 리더 대응도 <b>브라우저 기본 스크롤</b> 쪽이 훨씬 낫습니다.",
  siblings=siblings("scrollbehavior"),
  related='''        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="scrolllink.html"><b>스크롤 연동</b><em>9부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>''',
)
