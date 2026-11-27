# -*- coding: utf-8 -*-
from ax9 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def stage(inner, w="152px", h="76px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="height:' + h + ';position:relative;border:1px solid ' + col + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def th(x, y, w, h):
    return ('<span style="position:absolute;left:' + x + ';top:' + y + ';width:' + w + ';height:' + h +
            ';border-radius:4px;background:var(--accent)"></span>')

ROWS = ''.join('<span style="position:absolute;left:28px;right:6px;top:' + str(6 + i * 14) +
               'px;height:8px;border-radius:2px;background:var(--ink-100)"></span>' for i in range(3))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">두 화면에 같은 것이 있다 — 그걸 코드가 알아야 한다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">출발 자리와 도착 자리를 잰다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">그 사이를 이어서 움직인다 — 240~320ms</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">나머지는 투명도로 바꿔치기</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">돌아갈 때도 같은 길 — 왔던 자리로</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자리를 못 찾으면 그냥 페이드로 떨어뜨린다</div>
                </div>
              </div>'''

D = dict(
  slug="sharedelement", ko="공유 요소 전환", en="Shared element transition",
  desc="두 화면에 있는 같은 것을 이어서 움직이는 전환. 관계를 눈으로 알려 주지만 비싸다.",
  lede="두 화면에 있는 <b>같은 것</b>을 이어서 움직입니다. 관계를 말이 아니라 <b>눈으로</b> 알려 줍니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목록의 그림이 상세의 큰 그림으로 <b>이어서</b> 자랍니다.<br>
          <b>이어서 움직이기</b>를 끄면 목록이 사라지고 상세가 따로 나타납니다 — 같은 자료인데
          <b>관계가 안 보여</b> 어디서 왔는지 잠깐 헷갈립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "공유 요소 전환, 이어지는 전환, 확대 전환"),
    ("영어", "shared element transition, shared axis, hero animation, container transform"),
    ("같이 쓰는 말",
     "안드로이드에서는 <b>셰어드 엘리먼트</b>, Material 3 에서는 <b>컨테이너 트랜스폼</b>이라 부릅니다. "
     "플러터 쪽에서는 <b>히어로 애니메이션</b>입니다. "
     "웹에는 <b>뷰 트랜지션</b>(View Transitions API)이 생겨 "
     "<code>view-transition-name</code>으로 같은 것임을 알려 줍니다."),
    ("자주 잘못 부름",
     "<b>페이지 전환</b> — 화면이 통째로 바뀌는 것이고, 이쪽은 <b>한 조각이 이어지는</b> 것입니다.<br>"
     "<b>확대 애니메이션</b> — 그냥 커지는 것과 <b>두 화면을 잇는</b> 것은 다릅니다.<br>"
     "<b>모프</b> — 모양이 변형되는 연출을 가리키기도 해 자주 섞입니다."),
  ]),
  axes=ax("공유 요소 전환"),
  oneline="<b>같은 것이라는 사실을 코드가 알아야</b> 되는 연출입니다. 그 값을 치를 만한 자리인지 먼저 따져 보세요.",
  s4_title="이어지는 네 토막", s4_hint="같은 것이 자란다",
  states=states([
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "152px", "76px", "목록 — 작은 그림"),
     "출발", "목록의 <b>작은 그림</b>"),
    (stage(ROWS + th('6px', '6px', '46px', '34px'), "152px", "76px", "이어서 자라는 중"),
     "가는 중", "<b>240~320ms</b>. 그 사이 목록은 흐려진다"),
    (stage(th('6px', '6px', 'calc(100% - 12px)', '40px') +
           '<span style="position:absolute;left:6px;right:6px;top:52px;height:8px;border-radius:2px;background:var(--ink-100)"></span>',
           "152px", "76px", "상세 — 큰 그림"),
     "도착", "같은 것이 <b>커진 것</b>으로 읽힌다"),
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "152px", "76px", "돌아갈 때도 같은 길"),
     "돌아오기", "<b>왔던 자리로</b> 줄어든다"),
    (stage('<span style="position:absolute;inset:6px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></span>',
           "152px", "76px", "그냥 나타났다", False),
     "안 이을 때", "<b>관계가 안 보인다</b>"),
    (stage('<span style="position:absolute;inset:6px;border-radius:5px;background:var(--surface);border:1px dashed var(--line-strong);display:grid;place-items:center;font-size:8px;color:var(--fg-muted)">페이드</span>',
           "152px", "76px", "자리를 못 찾으면"),
     "떨어뜨리기", "<b>그냥 페이드</b>로 물러난다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("같은 것", "이름을 붙인다", "<b>코드가 알아야</b> 이을 수 있다"),
    ("자리 재기", "출발과 도착", "두 자리를 재서 <b>그 사이</b>를 움직인다"),
    ("길이", "240~320ms", "짧으면 안 보이고 길면 기다린다 — <a href=\"duration.html\">지속 시간</a>"),
    ("나머지", "투명도", "이어지는 것 말고는 <b>바꿔치기</b>한다"),
    ("돌아오기", "같은 길", "<b>왔던 자리로.</b> 안 그러면 더 헷갈린다"),
    ("못 찾으면", "페이드로", "<b>떨어뜨릴 길</b>을 반드시 둔다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>떨어뜨릴 길이 가장 중요합니다.</b>
          목록에서 한참 굴려 내려간 뒤 들어갔다 나오면
          출발 자리가 <b>화면 밖</b>일 수 있고,
          필터가 바뀌어 그 줄이 아예 사라졌을 수도 있습니다.
          그럴 때 억지로 이으면 <b>화면 밖에서 날아오는</b> 이상한 연출이 됩니다.
          <b>자리를 못 찾으면 그냥 페이드</b>로 물러나게 해 두면,
          되는 때만 예쁘고 안 되는 때도 멀쩡합니다.</p>''',
  do=ul([
    "목록 → 상세처럼 <b>같은 것</b>이 양쪽에 있을 때",
    "사진·카드처럼 <b>눈에 띄는 한 조각</b>이 이어질 때",
    "<b>돌아올 때도</b> 같은 길을 둘 수 있을 때",
  ]),
  dont=ul([
    "이어지는 것이 <b>작고 안 눈에 띌</b> 때 — 값을 못 한다",
    "출발 자리가 <b>화면 밖</b>인데 억지로 잇기",
    "글자처럼 <b>크기가 많이 다른</b> 것을 억지로 모프하기",
    "떨어뜨릴 길 없이 — <b>안 되는 때</b>가 반드시 온다",
  ]),
  instead='그냥 들고 나는 것은 <a href="enterexit.html">진입과 퇴장</a>, 곡선은 <a href="easing.html">이징</a>, 줄이 차례로면 <a href="stagger.html">차례로 들어오기</a>.',
  cases=cases([
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "150px", "72px", "목록 → 상세"), "사진 목록", "<b>가장 잘 맞는 자리</b>"),
    (stage('<span style="position:absolute;left:6px;right:6px;top:20px;height:28px;border-radius:5px;background:var(--accent)"></span>',
           "150px", "72px", "카드 → 전체 화면"), "카드 펼치기", "카드가 <b>그대로 자란다</b>"),
    (stage('<span style="position:absolute;left:6px;top:28px;width:20px;height:20px;border-radius:50%;background:var(--accent)"></span>',
           "150px", "72px", "아바타 → 프로필"), "작은 조각", "<b>너무 작으면</b> 값을 못 한다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 전환의 계약서",
  code_lede="같은 것에 <b>같은 이름</b>을 붙이면 브라우저가 이어 줍니다.",
  code='''<span class="c">/* 두 화면의 같은 것에 같은 이름을 붙인다 */</span>
.list .thumb[data-id="42"] { <span class="a">view-transition-name</span>: store-42; }
.detail .hero                { <span class="a">view-transition-name</span>: store-42; }

<span class="c">// 화면을 바꾸는 일을 감싸면 그 사이를 이어 준다</span>
<span class="k">if</span> (!document.startViewTransition) { render(); }   <span class="c">// 안 되면 그냥 바꾼다</span>
<span class="k">else</span> document.startViewTransition(() =&gt; render());

<span class="c">/* 모션 줄이기에서는 잇지 않는다 */</span>
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) { <span class="a">animation-duration</span>: <span class="a">1ms</span>; }
}''',
  keys=kbd([
    ("이름은 <b>한 화면에 하나</b>", "같은 <code>view-transition-name</code>이 둘이면 <b>전환이 통째로 멎는다</b>"),
    ("안 되는 브라우저", "<code>startViewTransition</code>이 없으면 <b>그냥 바꾼다.</b> 기능은 그대로여야 한다"),
    ("초점은 기다리지 않는다", "연출 중에도 초점은 <b>바로</b> 옮긴다 — <a href=\"enterexit.html\">진입과 퇴장</a>"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>", "큰 거리를 지나가는 연출이라 <b>줄이기에서 끈다</b>"),
    ("읽는 순서", "연출은 눈에만 있다. <b>DOM 순서</b>는 그대로여야 한다"),
    ("긴 목록", "<a href=\"virtual.html\">가상 스크롤</a>이면 출발 요소가 <b>아예 없을 수</b> 있다"),
  ]),
  backend=rows([
    ("자료가 양쪽에 있어야", "상세를 새로 받아야 한다면 <b>그 사이에 빈 화면</b>이 생깁니다. 목록이 가진 값으로 먼저 그려 두면 매끄럽습니다."),
    ("그림을 미리 받아 둔다", "큰 그림이 늦게 오면 <b>자라다 멈춘 자리</b>가 비어 보입니다."),
    ("주소가 바뀌는 전환", "뒤로가기로 돌아올 때도 같은 길을 쓰려면 <b>어디서 왔는지</b>를 알아야 합니다 — <a href=\"systemback.html\">시스템 백</a>."),
  ]),
  plat_lede="<b>앱에서 먼저 흔해졌고</b> 웹은 최근에 따라왔습니다.",
  plats=plats([
    ("웹", "View Transitions",
     stage(ROWS + th('6px', '6px', '18px', '18px'), "110px", "60px"),
     "<code>view-transition-name</code>으로 같은 것임을 알립니다. <b>최근 브라우저</b>에서만 됩니다."),
    ("iOS", "matchedGeometryEffect",
     '''              <div class="phone" role="img" aria-label="iOS 공유 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:18px;border-radius:4px;background:var(--accent)"></div></div></div>''',
     "SwiftUI 에서 <code>matchedGeometryEffect</code>로 잇습니다. <b>같은 id</b>를 주면 됩니다."),
    ("안드로이드", "Container transform",
     '''              <div class="phone" role="img" aria-label="Material 컨테이너 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:18px;border-radius:4px;background:var(--accent)"></div></div></div>''',
     "Material 3 의 <b>컨테이너 트랜스폼</b>이 규격입니다. 네 가지 전환 가운데 하나로 정리돼 있습니다."),
  ]),
  plat_note="시안에서 가장 멋있어 보이는 연출이지만, <b>되는 경우와 안 되는 경우</b>를 함께 정해야 합니다 — 목록을 한참 굴려 내려간 뒤, 필터가 바뀐 뒤, 검색으로 바로 들어온 뒤. 받을 때 <b>\"자리를 못 찾으면 어떻게 합니까\"</b>를 한 번 물어보면 떨어뜨릴 길이 함께 정해집니다.",
  siblings=siblings("sharedelement"),
  related='''        <li><a href="enterexit.html"><b>진입과 퇴장</b><em>9부</em></a></li>
        <li><a href="easing.html"><b>이징 곡선</b><em>9부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
