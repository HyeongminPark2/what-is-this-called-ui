# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">두 화면의 같은 요소를 코드가 알아야 함</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">출발 자리와 도착 자리를 잼</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">그 사이를 240~320ms 동안 이어서 움직임</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">나머지는 투명도로 바꿔치기</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">돌아갈 때도 같은 길로 왔던 자리에</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자리를 못 찾으면 그냥 페이드로 바꿈</div>
                </div>
              </div>'''

D = dict(
  slug="sharedelement", ko="공유 요소 전환", en="Shared element transition",
  desc="두 화면에 있는 같은 요소를 이어서 움직이는 전환입니다. 두 화면의 관계를 눈으로 보여 주지만 구현 비용이 크다는 점을 다루는 항목입니다.",
  lede="공유 요소 전환은 두 화면에 있는 <b>같은 요소</b>를 이어서 움직이는 전환입니다. 두 화면이 어떤 관계인지 설명하는 글 없이 <b>움직임으로</b> 보여 줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목록의 작은 그림이 상세 화면의 큰 그림으로 <b>이어서</b> 커집니다.<br>
          <b>이어서 움직이기</b>를 끄면 목록이 사라진 뒤 상세 화면이 따로 나타나는데, 같은 자료인데도
          두 화면의 <b>관계가 보이지 않아서</b> 상세 화면이 어디서 왔는지 잠깐 헷갈립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "공유 요소 전환, 이어지는 전환, 확대 전환"),
    ("영어", "shared element transition, shared axis, hero animation, container transform"),
    ("같이 쓰는 말",
     "안드로이드에서는 <b>셰어드 엘리먼트</b>, Material 3에서는 <b>컨테이너 트랜스폼</b>이라고 부르고, "
     "플러터에서는 <b>히어로 애니메이션</b>이라고 부릅니다. "
     "웹에는 <b>뷰 트랜지션</b>(View Transitions API)이 생겨서 "
     "<code>view-transition-name</code>으로 두 요소가 같은 것임을 브라우저에 알려 줍니다."),
    ("자주 잘못 부르는 이름",
     "<b>페이지 전환</b> — 페이지 전환은 화면이 통째로 바뀌는 것이고, 공유 요소 전환은 그 가운데 <b>한 요소가 두 화면을 이어 움직이는</b> 것입니다.<br>"
     "<b>확대 애니메이션</b> — 요소가 그냥 커지는 것과 <b>두 화면을 이어 주는</b> 것은 다릅니다.<br>"
     "<b>모프</b> — 모프는 모양이 변형되는 연출을 가리키기도 해서 공유 요소 전환과 자주 섞어 부릅니다."),
  ]),
  s4_title="이어지는 전환의 단계", s4_hint="같은 그림이 목록에서 상세 화면으로 커지는 과정",
  states=states([
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "152px", "76px", "목록의 작은 그림"),
     "목록에서 출발할 때", "목록에 <b>작은 그림</b>이 있습니다"),
    (stage(ROWS + th('6px', '6px', '46px', '34px'), "152px", "76px", "이어서 커지는 중"),
     "이어서 움직이는 중", "<b>240~320ms</b> 동안 그림이 커지고, 그 사이 목록은 흐려집니다"),
    (stage(th('6px', '6px', 'calc(100% - 12px)', '40px') +
           '<span style="position:absolute;left:6px;right:6px;top:52px;height:8px;border-radius:2px;background:var(--ink-100)"></span>',
           "152px", "76px", "상세 화면의 큰 그림"),
     "상세 화면에 도착했을 때", "목록의 그림이 <b>커진 것</b>으로 보입니다"),
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "152px", "76px", "돌아갈 때도 같은 길로"),
     "목록으로 돌아올 때", "<b>왔던 자리로</b> 줄어들며 돌아갑니다"),
    (stage('<span style="position:absolute;inset:6px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></span>',
           "152px", "76px", "그냥 나타남", False),
     "이어서 움직이지 않을 때", "두 화면의 <b>관계가 보이지 않습니다</b>"),
    (stage('<span style="position:absolute;inset:6px;border-radius:5px;background:var(--surface);border:1px dashed var(--line-strong);display:grid;place-items:center;font-size:8px;color:var(--fg-muted)">페이드</span>',
           "152px", "76px", "자리를 못 찾으면"),
     "이을 수 없어 페이드로 바꿀 때", "이을 수 없을 때는 <b>그냥 페이드</b>로 바꿔 보여 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("같은 요소", "이름 붙이기", "두 요소가 같다는 것을 <b>코드가 알아야</b> 이을 수 있습니다"),
    ("자리 재기", "출발과 도착", "출발 자리와 도착 자리를 재서 <b>그 사이</b>를 움직입니다"),
    ("길이", "240~320ms", "짧으면 움직임이 보이지 않고 길면 기다리게 됩니다. 자세한 내용은 <a href=\"duration.html\">지속 시간</a>에 있습니다"),
    ("나머지", "투명도", "이어지는 요소를 뺀 나머지는 투명도로 <b>바꿔치기</b>합니다"),
    ("돌아오기", "같은 길", "돌아갈 때도 <b>왔던 자리로</b> 움직입니다. 다른 자리로 가면 더 헷갈립니다"),
    ("자리를 못 찾을 때", "페이드로", "이을 수 없을 때 <b>대신할 방법(폴백)</b>을 반드시 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          공유 요소 전환에서 특히 중요한 것은 <b>이을 수 없을 때 대신할 방법</b>입니다.
          목록을 한참 스크롤해 내려간 뒤 상세에 들어갔다 나오면
          출발 자리가 <b>화면 밖</b>에 있을 수 있고,
          필터가 바뀌어서 그 줄이 아예 사라졌을 수도 있습니다.
          이럴 때 억지로 이으면 요소가 <b>화면 밖에서 날아 들어오는</b> 이상한 연출이 됩니다.
          그래서 <b>자리를 못 찾으면 그냥 페이드</b>로 바꿔 보여 주도록 해 두면,
          이을 수 있을 때는 이어서 움직이고 이을 수 없을 때도 화면이 어색해지지 않습니다.</p>''',
  instead_title="공유 요소 전환 대신 쓰거나 함께 볼 것",
  do=ul([
    "목록과 상세 화면처럼 <b>같은 요소</b>가 양쪽 화면에 있을 때",
    "사진이나 카드처럼 <b>눈에 띄는 요소 하나</b>가 이어질 때",
    "<b>돌아올 때도</b> 같은 경로로 움직이게 할 수 있을 때",
  ]),
  dont=ul([
    "이어지는 요소가 <b>작아서 눈에 잘 띄지 않을</b> 때. 들인 비용만큼 효과가 없습니다",
    "출발 자리가 <b>화면 밖</b>에 있는데 억지로 이을 때",
    "글자처럼 두 화면에서 <b>크기가 많이 다른</b> 것을 억지로 모프할 때",
    "이을 수 없을 때 대신할 방법을 두지 않을 때. <b>이을 수 없는 경우</b>는 반드시 생깁니다",
  ]),
  instead='요소가 다른 화면과 이어지지 않고 그냥 들어오고 나가기만 하면 <a href="enterexit.html">진입과 퇴장</a>으로 충분합니다. 곡선은 <a href="easing.html">이징</a>에서, 여러 줄이 차례로 들어오게 하는 방법은 <a href="stagger.html">차례로 들어오기</a>에서 다룹니다.',
  cases=cases([
    (stage(ROWS + th('6px', '6px', '18px', '18px'), "150px", "72px", "목록에서 상세로"), "사진 목록에서 상세로 넘어가기", "공유 요소 전환이 <b>가장 잘 맞는 자리</b>입니다"),
    (stage('<span style="position:absolute;left:6px;right:6px;top:20px;height:28px;border-radius:5px;background:var(--accent)"></span>',
           "150px", "72px", "카드에서 전체 화면으로"), "카드를 전체 화면으로 펼치기", "카드가 <b>그대로 커져서</b> 전체 화면이 됩니다"),
    (stage('<span style="position:absolute;left:6px;top:28px;width:20px;height:20px;border-radius:50%;background:var(--accent)"></span>',
           "150px", "72px", "아바타에서 프로필로"), "아바타처럼 작은 요소 잇기", "이어지는 요소가 <b>너무 작으면</b> 들인 비용만큼 효과가 없습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="두 화면의 같은 요소에 <b>같은 이름</b>을 붙이면 브라우저가 둘 사이를 이어 줍니다.",
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
  keys_heads="<th>알아 둘 규칙</th><th>자세한 내용</th>",
  keys=kbd([
    ("한 화면에 같은 이름은 <b>하나만</b> 쓰기", "같은 <code>view-transition-name</code>이 한 화면에 둘 있으면 <b>전환 전체가 동작하지 않습니다</b>"),
    ("지원하지 않는 브라우저에서", "<code>startViewTransition</code>이 없으면 연출 없이 <b>그냥 화면을 바꿉니다.</b> 기능은 그대로 동작해야 합니다"),
    ("초점은 연출을 기다리지 않고 옮기기", "연출 중에도 초점은 <b>바로</b> 옮깁니다. 자세한 내용은 <a href=\"enterexit.html\">진입과 퇴장</a>에 있습니다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>를 켰을 때", "큰 거리를 지나가는 연출이라서 <b>모션 줄이기에서는 끕니다</b>"),
    ("읽는 순서 그대로 두기", "연출은 화면에서만 일어나는 일이므로 <b>DOM 순서</b>는 그대로 둬야 합니다"),
    ("긴 목록에서 출발 요소가 없을 때", "<a href=\"virtual.html\">가상 스크롤</a>을 쓰면 출발 요소가 DOM에 <b>아예 없을 수</b> 있습니다"),
  ]),
  backend=rows([
    ("목록이 가진 값으로 상세 화면 먼저 그리기", "상세 자료를 새로 받아야 한다면 <b>받는 동안 빈 화면</b>이 생깁니다. 목록이 이미 가진 값으로 먼저 그려 두면 전환이 매끄럽습니다."),
    ("큰 그림을 미리 받아 두기", "큰 그림이 늦게 오면 <b>커지는 연출이 끝난 자리</b>가 비어 보입니다. 그래서 큰 그림은 미리 받아 둡니다."),
    ("주소가 바뀌는 전환", "뒤로가기로 돌아올 때도 같은 경로로 움직이려면 상세 화면이 <b>어느 줄에서 왔는지</b> 알아야 합니다. 자세한 내용은 <a href=\"systemback.html\">시스템 백</a>에 있습니다."),
  ]),
  plat_lede="공유 요소 전환은 <b>앱에서 먼저 흔해졌고</b>, 웹에서는 최근에야 쓸 수 있게 되었습니다.",
  plats=plats([
    ("웹", "View Transitions",
     stage(ROWS + th('6px', '6px', '18px', '18px'), "110px", "60px"),
     "<code>view-transition-name</code>으로 두 요소가 같은 것임을 알립니다. <b>최근 브라우저</b>에서만 동작합니다."),
    ("iOS", "matchedGeometryEffect",
     '''              <div class="phone" role="img" aria-label="iOS 공유 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:18px;border-radius:4px;background:var(--accent)"></div></div></div>''',
     "SwiftUI에서는 <code>matchedGeometryEffect</code>로 두 요소를 잇고, 두 요소에 <b>같은 id</b>를 주면 됩니다."),
    ("안드로이드", "Container transform",
     '''              <div class="phone" role="img" aria-label="Material 컨테이너 전환 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:18px;border-radius:4px;background:var(--accent)"></div></div></div>''',
     "Material 3에는 <b>컨테이너 트랜스폼</b>이라는 규격이 있고, 네 가지 전환 패턴 가운데 하나로 정리되어 있습니다."),
  ]),
  plat_note="공유 요소 전환은 시안에서 가장 멋있어 보이는 연출이지만, <b>이을 수 있는 경우와 없는 경우</b>를 함께 정해야 합니다. 목록을 한참 스크롤해 내려간 뒤, 필터가 바뀐 뒤, 검색으로 상세 화면에 바로 들어온 뒤가 이을 수 없는 대표적인 경우입니다. 시안을 받을 때 <b>\"출발 자리를 못 찾으면 어떻게 하나요?\"</b>라고 한 번 물어보면 대신할 방법도 함께 정해집니다.",
  siblings=siblings("sharedelement"),
  related='''        <li><a href="enterexit.html"><b>진입과 퇴장</b><em>9부</em></a></li>
        <li><a href="easing.html"><b>이징 곡선</b><em>9부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
