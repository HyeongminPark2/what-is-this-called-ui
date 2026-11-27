# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def mini_list(head="붙박이 머리말", head_style="", w="150px", rows_n=3, sec=None):
    body = ""
    if sec:
        body += ('<div style="background:var(--bg);padding:3px 7px;font-size:9px;font-weight:700;color:var(--fg-muted)">' + sec + '</div>')
    for i in range(rows_n):
        body += ('<div style="padding:5px 7px;font-size:9.5px;border-bottom:1px solid var(--line)">#482' + str(1 - i if i < 2 else 9) + ' · ₩' + ['1,245,480', '953,025', '412,000'][i] + '</div>')
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<div style="background:var(--surface);border-bottom:1px solid var(--line);padding:5px 7px;'
            'font-size:10px;font-weight:700;' + head_style + '">' + head + '</div>' + body + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:240px"><div style="height:94px;overflow:auto;border:1px solid var(--line);border-radius:7px;background:var(--surface)">
                    <div style="position:sticky;top:0;background:var(--surface);border-bottom:1px solid var(--line);padding:6px 9px;font-size:11px;font-weight:700;z-index:2">정산 목록</div>
                    <div style="position:sticky;top:29px;background:var(--bg);padding:3px 9px;font-size:9.5px;font-weight:700;color:var(--fg-muted);z-index:1">11월 1주</div>
                    <div style="padding:6px 9px;font-size:10.5px;border-bottom:1px solid var(--line)">#4821 · ₩1,245,480</div>
                    <div style="padding:6px 9px;font-size:10.5px;border-bottom:1px solid var(--line)">#4820 · ₩953,025</div>
                    <div style="padding:6px 9px;font-size:10.5px;border-bottom:1px solid var(--line)">#4819 · ₩412,000</div>
                    <div style="padding:6px 9px;font-size:10.5px">#4818 · ₩820,500</div>
                  </div></div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">position: sticky</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">top: 0   없으면 붙지 않음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">스크롤되는 조상 안에서만 붙음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">top: 29px   머리말 아래에 쌓음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">z-index   지나가는 줄보다 위에 둠</div>
                </div>
              </div>'''

D = dict(
  slug="sticky", ko="스티키", en="Sticky positioning",
  desc="position: sticky가 어떻게 동작하는지, 그리고 왜 작동하지 않는지(세 가지 원인)를 실물과 해부도로 보여 주는 항목입니다.",
  lede="스티키는 평소에는 문서 흐름을 따라 움직이다가, 스크롤되어 <b>정해진 선에 닿으면 그 자리에 붙어 있는</b> 요소입니다. 붙박이 머리말과 묶음 머리글은 모두 스티키로 만듭니다.",
  axes_lede="뼈대를 다루는 항목들은 눈에 보이지 않으면서 요소의 자리를 정한다는 점이 같아서 생김새로는 구별하기 어렵습니다. 대신 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목록을 스크롤해 보세요. 머리말은 맨 위에 계속 붙어 있지만, <b>'11월 1주' 같은 묶음 머리글은 하나씩 번갈아</b> 붙습니다.
          스티키는 <b>자기 부모 안에서만</b> 붙어 있기 때문입니다.<br>
          <b>스티키가 작동하지 않게 만들어 보기</b>를 켜면 머리말이 붙지 않고 그냥 올라갑니다. 실무에서 '스티키가 안 먹어요'라는 문제는
          거의 항상 <code>top</code>을 적지 않았거나, 조상에 <code>overflow</code>가 걸렸거나,
          부모 높이가 내용과 같은 경우 셋 가운데 하나입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스티키, 붙박이, 고정 머리말"),
    ("영어", "sticky, sticky header, stuck state"),
    ("같이 쓰는 말",
     "붙은 상태는 <b>스턱</b>(stuck), 붙는 기준선은 <b>오프셋</b>(<code>top</code>·<code>bottom</code>)이라고 부릅니다. "
     "화면에 아예 고정하는 것은 <b><code>fixed</code></b>이고, 묶음마다 머리글이 번갈아 붙는 것은 "
     "<b>스티키 섹션 헤더</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>fixed</code></b> — fixed는 <b>화면</b>에 붙어서 스크롤해도 움직이지 않지만, sticky는 <b>부모가 화면을 벗어나면 함께 사라집니다</b>.<br>"
     "<b>float</b> — 스티키와는 전혀 다른 속성으로, 요소 옆으로 글이 흐르게 하는 옛 방식입니다.<br>"
     "<b>스크롤 스파이</b> — 지금 보고 있는 구역을 메뉴에 표시하는 기능으로, 스티키와는 다른 것입니다."),
  ]),
  axes=ax("스티키"),
  oneline="스티키는 <b>부모 안에서만 붙는 fixed</b>라고 보면 됩니다. fixed와 다른 점은 부모가 화면 밖으로 지나가면 함께 사라진다는 것 하나입니다.",
  s4_title="상태", s4_hint="붙기 전과 붙은 뒤에 달라지는 모습",
  states=states([
    (mini_list("붙박이 머리말"), "아직 붙기 전", "맨 위에 있을 때는 <b>평범한 요소</b>와 똑같이 보입니다"),
    (mini_list("붙박이 머리말", "box-shadow:0 2px 6px rgba(20,22,26,.12)"), "위에 붙었을 때(stuck)",
     "붙은 뒤에는 <b>그림자나 선</b>을 넣어 내용 위에 떠 있다는 것을 알립니다"),
    (mini_list("11월 1주", "background:var(--bg);color:var(--fg-muted);font-size:9.5px", sec=None),
     "묶음 머리글이 번갈아 붙을 때", "묶음마다 부모가 달라서 머리글이 하나씩 <b>번갈아</b> 붙습니다"),
    (mini_list("안 붙는 머리말", "opacity:.5"), "스티키가 작동하지 않을 때",
     "<code>top</code>이 없거나, 조상에 <code>overflow</code>가 있거나, 부모 높이가 내용과 같은 경우입니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="background:var(--surface);border-bottom:1px solid var(--line);padding:5px 7px;font-size:10px;font-weight:700">머리말</div>
                <div style="background:var(--bg);padding:3px 7px;font-size:9px;font-weight:700;color:var(--fg-muted)">11월 1주</div>
                <div style="padding:5px 7px;font-size:9.5px">#4821</div>
              </div>''',
     "두 겹으로 쌓아 붙일 때", "<code>top: 0</code>과 <code>top: 29px</code>로 묶음 머리글을 <b>머리말 아래에</b> 붙입니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:5px 7px;font-size:9.5px;border-bottom:1px solid var(--line)">#4821</div>
                <div style="padding:5px 7px;font-size:9.5px;border-bottom:1px solid var(--line)">#4820</div>
                <div style="background:var(--surface);border-top:1px solid var(--line);padding:6px 7px;font-size:10px;font-weight:700;box-shadow:0 -2px 6px rgba(20,22,26,.1)">합계 ₩2,198,505</div>
              </div>''',
     "아래쪽에 붙일 때", "<code>bottom: 0</code>으로 아래에 붙입니다. 표의 합계 줄이나 폼의 저장 버튼에 씁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크롤 상자", "scroll container", "스티키가 붙는 <b>기준</b>입니다. 화면일 수도 있고, 안쪽 상자일 수도 있습니다"),
    ("<code>position: sticky</code>", "sticky", "이 줄만으로는 <b>아무 일도 일어나지 않습니다</b>"),
    ("오프셋", "top · bottom", "<b>어디에 붙을지</b> 정합니다. 이 줄을 빠뜨리는 것이 '안 먹어요'의 가장 흔한 원인입니다"),
    ("조상의 overflow", "overflow", "스크롤되는 조상에 <code>hidden</code>·<code>auto</code>가 있으면 스티키가 <b>그 상자를 기준</b>으로 붙습니다"),
    ("쌓아 붙이기", "top: 29px", "머리말 높이만큼 내려 적으면 <b>두 겹</b>으로 붙습니다"),
    ("z-index", "z-index", "주지 않으면 스크롤되는 <b>목록 줄이 머리말 위로</b> 지나갑니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '스티키가 안 먹어요'의 세 가지 원인 가운데 <b>가장 찾기 어려운 것은 조상의 <code>overflow</code></b>입니다.
          대여섯 단계 위의 래퍼에 <code>overflow: hidden</code> 한 줄이 있으면 스티키는
          <b>그 상자를 기준으로</b> 붙으려 하는데, 그 상자는 스크롤되지 않으므로 아무 일도 일어나지 않습니다.
          이럴 때는 개발자 도구에서 부모를 거슬러 올라가며 <code>overflow</code>를 찾는 것이 가장 빠릅니다.</p>''',
  do=ul([
    "<b>긴 목록의 머리말</b>을 붙여 둘 때. 스크롤해도 무슨 열인지 알 수 있습니다",
    "지금 보는 항목이 몇 월 것인지 알려 주는 묶음 머리글을 둘 때",
    "표의 <b>합계 줄</b>이나 폼의 저장 버튼을 아래에 붙일 때. <code>bottom: 0</code>을 씁니다",
    "긴 글의 목차를 붙여 둘 때",
  ]),
  dont=ul([
    "<b>화면을 반쯤 덮을</b> 만큼 큰 요소를 붙일 때. 내용을 볼 자리가 없어집니다",
    "폰에서 머리말과 꼬리말을 둘 다 붙일 때. 가운데 내용 영역이 너무 좁아집니다",
    "스크롤할 때마다 모양이 <b>크게 바뀌는</b> 머리말을 만들 때. 화면이 덜컥거려 보입니다",
    "<code>fixed</code>로 해도 되는 것을 굳이 sticky로 만들 때. 부모를 벗어나면 함께 사라집니다",
  ]),
  instead='부모와 상관없이 화면에 완전히 고정하려면 <code>position: fixed</code>를 씁니다. 화면 맨 위 머리말을 어떻게 꾸밀지는 <a href="../items/appbar.html">앱바</a>에서, 상자 안쪽만 스크롤하게 만드는 방법은 <a href="overflow.html">넘침</a>에서 다룹니다.',
  cases=cases([
    (mini_list("정산 목록", "box-shadow:0 2px 6px rgba(20,22,26,.1)", "190px"),
     "목록 머리말 붙여 두기", "스티키를 가장 흔하게 쓰는 자리입니다. 붙은 뒤에는 <b>그림자</b>로 붙었다는 것을 알립니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="display:flex;background:var(--bg);border-bottom:1px solid var(--line);padding:5px 8px;font-size:9.5px;font-weight:700;color:var(--fg-muted)"><span style="flex:1">번호</span><span>금액</span></div>
                <div style="display:flex;padding:5px 8px;font-size:10px;border-bottom:1px solid var(--line)"><span style="flex:1">#4821</span><span>₩1,245,480</span></div>
                <div style="display:flex;padding:5px 8px;font-size:10px"><span style="flex:1">#4820</span><span>₩953,025</span></div>
              </div>''',
     "표의 열 이름 붙여 두기", "<code>thead th</code>에 sticky를 걸면 긴 표를 내려가도 <b>무슨 열인지</b> 알 수 있습니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:6px 8px;font-size:10px;border-bottom:1px solid var(--line)">계좌번호 입력…</div>
                <div style="padding:6px 8px;font-size:10px;border-bottom:1px solid var(--line)">예금주 입력…</div>
                <div style="padding:7px 8px;background:var(--surface);border-top:1px solid var(--line);box-shadow:0 -2px 6px rgba(20,22,26,.1);text-align:right">
                  <span style="background:var(--accent);color:#fff;border-radius:5px;padding:4px 10px;font-size:10px;font-weight:700">저장</span></div>
              </div>''',
     "긴 폼 아래에 저장 바 붙이기", "<code>bottom: 0</code>으로 붙여 두면 긴 폼에서 <b>끝까지 내려가지 않아도</b> 저장할 수 있습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="스티키가 작동하지 않을 때 확인할 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="스티키는 <b>두 줄</b>이면 됩니다. 그런데도 작동하지 않는다면 그 두 줄이 아니라 <b>조상</b> 요소를 살펴봐야 합니다.",
  code='''<span class="t">.table-head</span> {
  <span class="a">position</span>: sticky;
  <span class="a">top</span>: <span class="a">0</span>;          <span class="c">/* 이 줄이 없으면 아무 일도 안 일어난다 */</span>
  <span class="a">z-index</span>: <span class="a">2</span>;       <span class="c">/* 없으면 목록 줄이 머리말 위로 지나간다 */</span>
  <span class="a">background</span>: <span class="t">var</span>(<span class="a">--surface</span>); <span class="c">/* 없으면 뒤가 비쳐 보인다 */</span>
}

<span class="c">/* 머리말 아래에 한 겹 더 쌓기 */</span>
<span class="t">.section-head</span> { <span class="a">position</span>: sticky; <span class="a">top</span>: <span class="a">36px</span>; <span class="a">z-index</span>: <span class="a">1</span>; }

<span class="c">/* 붙었을 때만 그림자 — 브라우저가 알려 준다 */</span>
<span class="t">.table-head</span> { <span class="a">top</span>: -<span class="a">1px</span>; }
<span class="t">.table-head</span>:is(.is-stuck) { <span class="a">box-shadow</span>: <span class="a">0 2px 6px</span> rgba(<span class="a">20,22,26,.1</span>); }''',
  keys=kbd([
    ("<code>top</code>(또는 <code>bottom</code>) 적기", "적지 않으면 <b>아무 일도 일어나지 않습니다</b>. 작동하지 않는 원인 가운데 가장 흔합니다"),
    ("조상의 <code>overflow</code> 확인하기", "스크롤되는 조상에 걸려 있으면 <b>그 상자를 기준</b>으로 붙습니다. 세 원인 가운데 가장 찾기 어렵습니다"),
    ("부모 높이 확인하기", "부모 높이가 내용과 같으면 <b>붙어 있을 구간이 없습니다</b>"),
    ("<code>z-index</code>와 배경 함께 주기", "둘 다 없으면 목록 줄이 머리말 위로 지나가고, 머리말 뒤가 비쳐 보입니다"),
    ("키보드 포커스가 가려지지 않게 하기", "붙박이 머리말이 <code>Tab</code>으로 옮겨 간 요소를 <b>가릴 수 있으므로</b>, <code>scroll-margin-top</code>으로 그만큼 띄웁니다"),
    ("머리말 높이 고정하기", "머리말 높이가 바뀌면 아래 겹의 <code>top</code> 값도 어긋나기 때문입니다"),
  ]),
  backend=rows([
    ("JS 없이 CSS만으로 동작함", "예전에는 스크롤 이벤트로 스티키를 흉내 냈지만, 지금은 <b>JS가 전혀 필요 없어서</b> 스크롤이 훨씬 부드럽습니다."),
    ("붙은 상태를 알아야 할 때", "붙었을 때만 그림자를 넣으려면 <code>IntersectionObserver</code>로 붙었는지 감시합니다. 스크롤 이벤트마다 위치를 재면 화면이 느려지기 때문입니다."),
    ("가상 스크롤과 함께 쓸 때", "화면 밖으로 나간 줄을 지웠다가 다시 그리는 목록에서는 <b>머리말이 그 안에 들어가면</b> 줄과 함께 사라집니다. 그래서 머리말은 가상 스크롤 영역 <b>밖</b>에 둡니다."),
    ("표 열 이름에 걸 때", "sticky는 <code>&lt;thead&gt;</code> 자체가 아니라 <code>&lt;th&gt;</code>에 걸어야 합니다. 브라우저마다 다르게 동작하던 예전 사정 때문입니다."),
  ]),
  plat_lede="iOS와 안드로이드는 목록 부품에 스티키 기능이 <b>처음부터 들어</b> 있습니다.",
  plats=plats([
    ("웹", "position: sticky",
     mini_list("머리말", "box-shadow:0 2px 5px rgba(20,22,26,.1)", "120px", 2),
     "CSS 두 줄로 만들 수 있지만, <b>조상의 overflow</b> 때문에 작동하지 않는 함정이 있습니다."),
    ("iOS", "UITableView · SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Section(header:)<br>List { }</div>''',
     "<b>섹션 헤더가 기본으로 붙기</b> 때문에 따로 적을 것이 없고, 오히려 <b>붙지 않게 하려면</b> 설정을 바꿔야 합니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyColumn {<br>&nbsp;stickyHeader { }<br>}</div>''',
     "<code>stickyHeader</code> 블록이 따로 있고, 웹과 거의 같게 동작합니다."),
  ]),
  plat_note="iOS는 <b>섹션 헤더가 기본으로 붙어서</b>, 디자이너가 \"머리글 붙여 주세요\"라고 하면 앱 개발자는 \"원래 붙는데요\"라고 답하게 됩니다. 반대로 웹에서는 <b>붙지 않는 것이 기본</b>이라서 같은 화면을 만들어도 드는 품이 다릅니다.",
  siblings=siblings("sticky"),
  related='''        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>''',
)
