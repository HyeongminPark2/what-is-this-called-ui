# -*- coding: utf-8 -*-
from ax1 import ax
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">scroll-snap-type — 칸 단위로 멎게 한다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-snap-align — 어디에 맞춰 멎나 (start · center)</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">overscroll-behavior: contain — 바깥까지 안 밀린다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-behavior: smooth — 뛸 때 부드럽게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">scroll-margin — 붙박이 머리말에 가리지 않게</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">굴림을 가로채지 않는다 — 매달기만 한다</div>
                </div>
              </div>'''

D = dict(
  slug="scrollbehavior", ko="스크롤 동작", en="Scroll behavior",
  desc="굴림을 다루는 CSS 넷 — 스냅·체이닝·부드러운 굴림·scroll-margin.",
  lede="굴림 자체를 다루는 값들. <b>칸 단위로 멎게</b> 하거나 <b>바깥까지 안 밀리게</b> 하는 일이 CSS 한 줄로 됩니다.",
  axes_lede="뼈대는 눈에 안 보이지만 <b>모든 화면이 그 위에</b> 섭니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>스냅</b>을 켜면 굴림이 칸 단위로 멎습니다 — 세로 상자와 가로 줄 둘 다에서요.<br>
          <b>끝에서 바깥까지 밀리기</b>를 끄면 안쪽을 끝까지 굴려도 <b>바깥이 안 따라 움직입니다</b> —
          <a href="../items/modal.html">모달</a> 안에서 특히 쓸모 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스크롤 동작, 스냅, 스크롤 체이닝, 부드러운 굴림"),
    ("영어", "scroll snap, overscroll behavior, scroll chaining, smooth scroll"),
    ("같이 쓰는 말",
     "칸 단위로 멎게 하는 것이 <b>스크롤 스냅</b>, "
     "안쪽을 끝까지 굴렸을 때 바깥이 따라 움직이는 것이 <b>스크롤 체이닝</b>입니다. "
     "끝에서 더 당기면 튕기는 효과가 <b>바운스</b>·<b>러버밴딩</b>이고 "
     "<code>overscroll-behavior: none</code>으로 막습니다. "
     "앵커로 뛸 때 붙박이 머리말에 가리지 않게 띄우는 값이 <code>scroll-margin</code>입니다."),
    ("자주 잘못 부름",
     "<b>스크롤 연동</b> — <a href=\"scrolllink.html\">스크롤 연동</a>은 굴림에 <b>무언가를 매다는</b> 일입니다. 이쪽은 <b>굴림 자체</b>입니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 더 받아오는 일입니다.<br>"
     "<b>스크롤 가로채기</b> — 굴린 양과 다르게 움직이게 하는 것으로, <b>여기 있는 것들과 다릅니다</b>."),
  ]),
  axes=ax("스크롤 동작"),
  oneline="<b>굴림은 사용자 것</b>입니다. 멎는 자리를 정하거나 새지 않게 막을 수는 있어도, <b>양을 바꾸면</b> 안 됩니다.",
  s4_title="네 가지 값", s4_hint="무엇을 다루나",
  states=states([
    (box(PAGES, "152px", "74px", "scroll-snap-type: none"), "스냅 없음", "<b>아무 데서나</b> 멎는다"),
    (box(PAGES, "152px", "74px", "y mandatory — 칸 단위로", True), "세로 스냅", "<b>한 장씩</b> 멎는다"),
    (box('<div style="display:flex;gap:5px;padding:18px 6px;overflow:hidden">' + CARDS + '</div>', "152px", "74px", "x mandatory — 가로 캐러셀", True),
     "가로 스냅", "사진첩·<b>캐러셀</b>에"),
    (box('<div style="position:absolute;inset:6px;border:1px solid var(--accent);border-radius:4px;display:grid;place-items:center;font-size:9px;color:var(--accent)">contain</div>',
         "152px", "74px", "바깥이 안 밀린다", True),
     "체이닝 막기", "<a href=\"../items/modal.html\">모달</a> 안에서 쓴다"),
    (box('<div style="position:absolute;left:0;right:0;top:0;height:16px;background:var(--bg);border-bottom:1px solid var(--line);font-size:8px;color:var(--fg-muted);display:grid;place-items:center">붙박이 머리말</div>'
         '<div style="position:absolute;left:6px;right:6px;top:22px;height:12px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div>',
         "152px", "74px", "scroll-margin-top 으로 띄운다", True),
     "scroll-margin", "뛰었을 때 <b>안 가리게</b>"),
    (box('<div style="position:absolute;inset:6px;border:1px dashed var(--danger);border-radius:4px;display:grid;place-items:center;font-size:8.5px;color:var(--danger)">굴림을 가로챔</div>',
         "152px", "74px", "굴린 만큼 안 간다", False),
     "가로채기", "<b>쓰지 않는다</b> — <a href=\"scrolllink.html\">스크롤 연동</a>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스냅", "scroll-snap-type", "<b>칸 단위</b>로 멎는다. 축과 세기를 적는다"),
    ("맞춤", "scroll-snap-align", "<b>어디에</b> 맞춰 멎나 — start · center"),
    ("체이닝", "overscroll-behavior", "<code>contain</code>이면 <b>바깥이 안 밀린다</b>"),
    ("부드럽게", "scroll-behavior", "뛸 때만 쓴다. <b>굴릴 때는 안 건드린다</b>"),
    ("scroll-margin", "가리지 않게", "<a href=\"../items/sticky.html\">붙박이 머리말</a>만큼 띄운다"),
    ("가로채기", "하지 않는다", "굴린 <b>양</b>을 바꾸면 고장 난 느낌이 난다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>scroll-margin</code>은 작지만 <b>자주 빠지는</b> 값입니다.
          붙박이 머리말이 있는 화면에서 앵커 링크로 뛰면
          목표가 <b>머리말 뒤에 숨어</b> 버립니다 —
          눌렀는데 아무 일도 안 일어난 것처럼 보이죠.
          목표 요소에 <code>scroll-margin-top</code>을 머리말 높이만큼 주면 끝나고,
          이건 <b>키보드로 건너뛰기</b>를 쓰는 사람에게도 똑같이 적용됩니다 —
          <a href="../items/focus.html">포커스</a>가 가려지면 어디에 있는지 알 수 없습니다.</p>''',
  do=ul([
    "<b>캐러셀·사진첩</b>에 스냅",
    "<a href=\"../items/modal.html\">모달</a>·<a href=\"../items/drawer.html\">드로어</a> 안에 <code>overscroll-behavior: contain</code>",
    "붙박이 머리말이 있으면 <code>scroll-margin-top</code>",
  ]),
  dont=ul([
    "긴 글에 스냅 — <b>읽다 멎어 답답하다</b>",
    "굴림 <b>양</b>을 바꾸기 — 고장 난 느낌이 난다",
    "<code>scroll-behavior: smooth</code>를 전역으로 — <a href=\"reducedmotion.html\">줄이기</a>에서 꺼야 한다",
    "<code>overscroll-behavior: none</code>을 본문에 — <b>당겨서 새로고침</b>이 막힌다",
  ]),
  instead='굴림에 무언가를 매다는 것은 <a href="scrolllink.html">스크롤 연동</a>, 붙는 머리말은 <a href="../items/sticky.html">스티키</a>, 더 받아오면 <a href="../items/infinite.html">무한 스크롤</a>.',
  cases=cases([
    (box('<div style="display:flex;gap:5px;padding:18px 6px;overflow:hidden">' + CARDS + '</div>', "150px", "70px", "x mandatory + center"),
     "가로 캐러셀", "<b>가장 잘 맞는</b> 자리"),
    (box('<div style="position:absolute;inset:6px;background:var(--surface);border:1px solid var(--line);border-radius:4px"></div>', "150px", "70px", "모달 안 contain"),
     "모달 안 목록", "바깥 페이지가 <b>안 밀린다</b>"),
    (code(['h2 { scroll-margin-top: 64px }'], "150px", "머리말 높이만큼", True), "앵커로 뛸 때", "<b>안 가린다</b>"),
  ]),
  s8_title="최소 코드와 키보드", s8_hint="이 굴림의 계약서",
  code_lede="스냅은 두 줄, 체이닝은 한 줄입니다.",
  code='''<span class="c">/* 가로 캐러셀 */</span>
.carousel { <span class="a">display</span>: flex; <span class="a">overflow-x</span>: auto; <span class="a">scroll-snap-type</span>: x mandatory; }
.carousel &gt; * { <span class="a">flex</span>: none; <span class="a">scroll-snap-align</span>: center; }

<span class="c">/* 모달 안에서 바깥이 밀리지 않게 */</span>
.modal__body { <span class="a">overflow</span>: auto; <span class="a">overscroll-behavior</span>: contain; }

<span class="c">/* 붙박이 머리말에 가리지 않게 */</span>
<span class="t">h2</span> { <span class="a">scroll-margin-top</span>: <span class="a">64px</span>; }

<span class="c">/* 뛸 때만 부드럽게 — 줄이기에서는 끈다 */</span>
<span class="t">html</span> { <span class="a">scroll-behavior</span>: smooth; }
@media (prefers-reduced-motion: reduce) { <span class="t">html</span> { <span class="a">scroll-behavior</span>: auto; } }''',
  keys=kbd([
    ("<kbd>PageDown</kbd>·<kbd>Home</kbd>", "스냅을 걸어도 <b>키보드 굴림은 그대로</b> 돌아야 한다"),
    ("가로 캐러셀의 <kbd>Tab</kbd>", "칸 안에 누를 것이 있으면 <b>초점이 가며 저절로 굴러간다</b>"),
    ("<code>scroll-margin</code>", "<a href=\"../items/focus.html\">초점</a>이 머리말에 가리는 것도 함께 막는다"),
    ("<code>scroll-behavior: smooth</code>", "<a href=\"reducedmotion.html\">모션 줄이기</a>에서 <code>auto</code>로 되돌린다"),
    ("<code>overscroll-behavior: none</code>", "<b>당겨서 새로고침</b>까지 막는다. 본문에는 쓰지 않는다"),
    ("<code>mandatory</code>와 <code>proximity</code>", "<code>mandatory</code>는 늘 붙는다. 칸이 화면보다 크면 <b>못 지나가는</b> 자리가 생길 수 있다"),
  ]),
  backend=rows([
    ("스냅과 더 받아오기", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 같이 쓰면 <b>칸이 늘 때마다</b> 멎는 자리가 바뀝니다."),
    ("굴린 자리 복원", "돌아왔을 때 자리를 되살리려면 <b>그린 뒤에</b> 해야 합니다 — <a href=\"searchresults.html\">검색 결과 화면</a>."),
  ]),
  plat_lede="<b>스냅은 앱에서 먼저</b> 흔했습니다.",
  plats=plats([
    ("웹", "CSS 로",
     box('<div style="display:flex;gap:4px;padding:12px 5px;overflow:hidden">' + CARDS + '</div>', "110px", "56px"),
     "자바스크립트 없이 CSS 로 됩니다. 예전에는 캐러셀을 <b>전부 손으로</b> 짰습니다."),
    ("iOS", "isPagingEnabled",
     '''              <div class="phone" role="img" aria-label="iOS 페이징 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:20px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "한 줄로 페이지 단위 굴림이 됩니다. <b>바운스</b>도 OS 기본입니다."),
    ("안드로이드", "SnapHelper · Pager",
     '''              <div class="phone" role="img" aria-label="안드로이드 페이저 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:20px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<code>PagerSnapHelper</code>·Compose 의 <code>HorizontalPager</code>가 같은 일을 합니다."),
  ]),
  plat_note="\"캐러셀 만들어 주세요\"가 예전에는 라이브러리를 들이는 일이었는데, 지금은 <b>CSS 세 줄</b>이면 됩니다. 라이브러리를 고르기 전에 스냅으로 되는지 먼저 보는 편이 좋습니다 — 키보드·스크린 리더 대응도 <b>브라우저 기본 굴림</b>이 훨씬 낫습니다.",
  siblings=siblings("scrollbehavior"),
  related='''        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="scrolllink.html"><b>스크롤 연동</b><em>9부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>''',
)
