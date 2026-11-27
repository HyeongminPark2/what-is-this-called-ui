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
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">top: 0   — 없으면 아무 일도 안 일어난다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">스크롤되는 조상 — 여기 안에서만 붙는다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">top: 29px   — 머리말 아래에 쌓기</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">z-index   — 지나가는 줄보다 위로</div>
                </div>
              </div>'''

D = dict(
  slug="sticky", ko="스티키", en="Sticky positioning",
  desc="position: sticky 가 어떻게 동작하고 왜 안 먹는지(세 가지 원인)를 실물과 해부도로 보여주는 항목.",
  lede="평소엔 흐름에 있다가 <b>정해진 선에 닿으면 거기 붙는</b> 것. 붙박이 머리말과 묶음 머리글이 다 이것입니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목록을 굴려 보세요. 머리말은 맨 위에 붙어 있고, <b>'11월 1주' 같은 묶음 머리글은 하나씩 교대</b>합니다 —
          스티키는 <b>자기 부모 안에서만</b> 붙어 있기 때문입니다.<br>
          <b>안 먹게 만들어 보기</b>를 켜면 그냥 올라가 버립니다. 실무에서 '스티키가 안 먹어요'는
          거의 늘 아래 셋 중 하나입니다 — <code>top</code>을 안 적었거나, 조상에 <code>overflow</code>가 걸렸거나,
          부모 높이가 내용과 같거나.</p>
        </div>''',
  names=rows([
    ("한국어", "스티키, 붙박이, 고정 머리말"),
    ("영어", "sticky, sticky header, stuck state"),
    ("같이 쓰는 말",
     "붙은 상태를 <b>스턱</b>(stuck), 붙는 기준선을 <b>오프셋</b>(<code>top</code>·<code>bottom</code>)이라 합니다. "
     "화면에 아예 못 박는 것은 <b><code>fixed</code></b>, 묶음마다 머리글이 교대하는 것은 "
     "<b>스티키 섹션 헤더</b>입니다."),
    ("자주 잘못 부름",
     "<b><code>fixed</code></b> — fixed 는 <b>화면</b>에 붙어 끝까지 안 움직입니다. sticky 는 <b>부모를 벗어나면 같이 사라집니다</b>.<br>"
     "<b>float</b> — 전혀 다른 것입니다. float 는 글이 옆으로 흐르게 하는 옛 방식입니다.<br>"
     "<b>스크롤 스파이</b> — 지금 보는 구역을 메뉴에 표시하는 것은 다른 기능입니다."),
  ]),
  axes=ax("스티키"),
  oneline="스티키는 <b>'부모 안에서만 붙는 fixed'</b>입니다. 부모가 지나가면 같이 사라지는 것이 fixed 와의 모든 차이입니다.",
  s4_title="상태", s4_hint="붙기 전과 붙은 뒤가 다르다",
  states=states([
    (mini_list("붙박이 머리말"), "안 붙음", "맨 위에 있을 때는 <b>평범한 요소</b>와 똑같다"),
    (mini_list("붙박이 머리말", "box-shadow:0 2px 6px rgba(20,22,26,.12)"), "붙음(stuck)",
     "붙은 뒤에 <b>그림자나 선</b>을 넣어 '떠 있다'를 알린다"),
    (mini_list("11월 1주", "background:var(--bg);color:var(--fg-muted);font-size:9.5px", sec=None),
     "묶음 머리글", "묶음마다 하나씩 <b>교대</b>한다 — 부모가 다르기 때문"),
    (mini_list("안 붙는 머리말", "opacity:.5"), "안 먹음",
     "<code>top</code>이 없거나, 조상에 <code>overflow</code>가 있거나, 부모 높이가 같거나"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="background:var(--surface);border-bottom:1px solid var(--line);padding:5px 7px;font-size:10px;font-weight:700">머리말</div>
                <div style="background:var(--bg);padding:3px 7px;font-size:9px;font-weight:700;color:var(--fg-muted)">11월 1주</div>
                <div style="padding:5px 7px;font-size:9.5px">#4821</div>
              </div>''',
     "두 겹 쌓기", "<code>top: 0</code>과 <code>top: 29px</code>로 <b>머리말 아래에</b> 붙인다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:5px 7px;font-size:9.5px;border-bottom:1px solid var(--line)">#4821</div>
                <div style="padding:5px 7px;font-size:9.5px;border-bottom:1px solid var(--line)">#4820</div>
                <div style="background:var(--surface);border-top:1px solid var(--line);padding:6px 7px;font-size:10px;font-weight:700;box-shadow:0 -2px 6px rgba(20,22,26,.1)">합계 ₩2,198,505</div>
              </div>''',
     "아래에 붙기", "<code>bottom: 0</code>. 표의 합계 줄이나 폼의 저장 버튼"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크롤 상자", "scroll container", "스티키가 붙는 <b>기준</b>. 화면일 수도, 안쪽 상자일 수도 있다"),
    ("<code>position: sticky</code>", "sticky", "이것만으로는 <b>아무 일도 안 일어난다</b>"),
    ("오프셋", "top · bottom", "<b>어디에 붙을지.</b> 이 줄이 빠진 것이 '안 먹어요'의 1번 원인"),
    ("조상의 overflow", "overflow", "스크롤되는 조상에 <code>hidden</code>·<code>auto</code>가 있으면 <b>그 상자 기준</b>이 된다"),
    ("쌓아 붙이기", "top: 29px", "머리말 높이만큼 내려 적으면 <b>두 겹</b>으로 붙는다"),
    ("z-index", "z-index", "안 주면 <b>지나가는 줄이 머리말 위로</b> 지나간다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '스티키가 안 먹어요'의 원인 셋 중 <b>가장 찾기 어려운 것이 조상의 <code>overflow</code></b>입니다.
          대여섯 단계 위의 래퍼에 <code>overflow: hidden</code> 한 줄이 있으면, 스티키는
          <b>그 상자를 기준으로</b> 붙으려 하고 그 상자는 안 굴러가므로 아무 일도 안 일어납니다.
          개발자 도구에서 부모를 거슬러 올라가며 <code>overflow</code>를 찾는 것이 가장 빠릅니다.</p>''',
  do=ul([
    "<b>긴 목록의 머리말</b> — 무슨 열인지 잊지 않게",
    "묶음 머리글 — '지금 보는 게 몇 월 것인지'",
    "표의 <b>합계 줄</b>이나 폼의 저장 버튼 — <code>bottom: 0</code>",
    "긴 글의 목차",
  ]),
  dont=ul([
    "<b>화면을 반쯤 덮을</b> 만큼 큰 것 — 볼 자리가 없어집니다",
    "폰에서 머리말·꼬리말을 둘 다 붙이는 것 — 가운데가 너무 좁아집니다",
    "스크롤 때마다 모양이 <b>크게 바뀌는</b> 머리말 — 덜컥거려 보입니다",
    "<code>fixed</code>로 해도 되는 것을 굳이 sticky 로 — 부모를 벗어나면 사라집니다",
  ]),
  instead='화면에 완전히 못 박으려면 <code>position: fixed</code>, 머리말 자체는 <a href="../items/appbar.html">앱바</a>, 안쪽만 굴리려면 <a href="overflow.html">넘침</a>.',
  cases=cases([
    (mini_list("정산 목록", "box-shadow:0 2px 6px rgba(20,22,26,.1)", "190px"),
     "목록 머리말", "가장 흔한 자리. 붙은 뒤에 <b>그림자</b>로 알린다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="display:flex;background:var(--bg);border-bottom:1px solid var(--line);padding:5px 8px;font-size:9.5px;font-weight:700;color:var(--fg-muted)"><span style="flex:1">번호</span><span>금액</span></div>
                <div style="display:flex;padding:5px 8px;font-size:10px;border-bottom:1px solid var(--line)"><span style="flex:1">#4821</span><span>₩1,245,480</span></div>
                <div style="display:flex;padding:5px 8px;font-size:10px"><span style="flex:1">#4820</span><span>₩953,025</span></div>
              </div>''',
     "표의 열 이름", "<code>thead th</code>에 sticky. 긴 표에서 <b>무슨 열인지</b> 안 잊는다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:6px 8px;font-size:10px;border-bottom:1px solid var(--line)">계좌번호 입력…</div>
                <div style="padding:6px 8px;font-size:10px;border-bottom:1px solid var(--line)">예금주 입력…</div>
                <div style="padding:7px 8px;background:var(--surface);border-top:1px solid var(--line);box-shadow:0 -2px 6px rgba(20,22,26,.1);text-align:right">
                  <span style="background:var(--accent);color:#fff;border-radius:5px;padding:4px 10px;font-size:10px;font-weight:700">저장</span></div>
              </div>''',
     "저장 바", "<code>bottom: 0</code>. 긴 폼에서 <b>끝까지 안 내려가도</b> 저장할 수 있다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="안 먹을 때 볼 목록",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="<b>두 줄</b>이면 됩니다. 안 먹는다면 그 두 줄이 아니라 <b>조상</b>을 봐야 합니다.",
  code='''<span class="t">.table-head</span> {
  <span class="a">position</span>: sticky;
  <span class="a">top</span>: <span class="a">0</span>;          <span class="c">/* 이 줄이 없으면 아무 일도 안 일어난다 */</span>
  <span class="a">z-index</span>: <span class="a">2</span>;       <span class="c">/* 없으면 지나가는 줄이 위로 지나간다 */</span>
  <span class="a">background</span>: <span class="t">var</span>(<span class="a">--surface</span>); <span class="c">/* 없으면 뒤가 비쳐 보인다 */</span>
}

<span class="c">/* 머리말 아래에 한 겹 더 쌓기 */</span>
<span class="t">.section-head</span> { <span class="a">position</span>: sticky; <span class="a">top</span>: <span class="a">36px</span>; <span class="a">z-index</span>: <span class="a">1</span>; }

<span class="c">/* 붙었을 때만 그림자 — 브라우저가 알려 준다 */</span>
<span class="t">.table-head</span> { <span class="a">top</span>: -<span class="a">1px</span>; }
<span class="t">.table-head</span>:is(.is-stuck) { <span class="a">box-shadow</span>: <span class="a">0 2px 6px</span> rgba(<span class="a">20,22,26,.1</span>); }''',
  keys=kbd([
    ("<code>top</code>(또는 <code>bottom</code>)을 적는다", "없으면 <b>아무 일도 안 일어난다</b>. 원인 1위"),
    ("조상의 <code>overflow</code>를 의심한다", "스크롤되는 조상에 걸려 있으면 <b>그 상자 기준</b>이 된다. 가장 찾기 어렵다"),
    ("부모 높이를 본다", "부모 높이가 내용과 같으면 <b>붙어 있을 구간이 없다</b>"),
    ("<code>z-index</code>와 배경", "둘 다 없으면 지나가는 줄이 위로 지나가고 뒤가 비친다"),
    ("키보드도 생각한다", "붙박이 머리말이 <code>Tab</code>으로 간 요소를 <b>가릴 수 있다</b>. <code>scroll-margin-top</code>으로 띄운다"),
    ("높이를 못 박는다", "머리말 높이가 바뀌면 아래 겹의 <code>top</code> 값도 어긋난다"),
  ]),
  backend=rows([
    ("스티키는 순수 CSS 다", "예전에는 스크롤 이벤트로 흉내 냈습니다. 지금은 <b>JS 가 전혀 필요 없고</b>, 그래서 스크롤이 훨씬 부드럽습니다."),
    ("붙은 상태를 알아야 할 때", "그림자를 붙었을 때만 넣으려면 <code>IntersectionObserver</code>로 감시합니다 — 스크롤 이벤트로 매번 재면 느려집니다."),
    ("가상 스크롤과 함께", "줄을 지웠다 그렸다 하는 목록에서는 <b>머리말이 그 안에 들어가면</b> 같이 사라집니다. 머리말은 가상 영역 <b>밖</b>에 둡니다."),
    ("표 열 이름", "<code>&lt;thead&gt;</code> 자체가 아니라 <code>&lt;th&gt;</code>에 걸어야 합니다. 브라우저마다 다르게 동작하던 오래된 사정입니다."),
  ]),
  plat_lede="두 OS 는 목록 부품에 <b>처음부터 들어</b> 있습니다.",
  plats=plats([
    ("웹", "position: sticky",
     mini_list("머리말", "box-shadow:0 2px 5px rgba(20,22,26,.1)", "120px", 2),
     "CSS 두 줄. 대신 <b>조상의 overflow</b>라는 함정이 있습니다."),
    ("iOS", "UITableView · SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Section(header:)<br>List { }</div>''',
     "<b>섹션 헤더가 기본으로 붙습니다.</b> 따로 적을 것이 없고, 오히려 <b>안 붙이려면</b> 설정을 바꿔야 합니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyColumn {<br>&nbsp;stickyHeader { }<br>}</div>''',
     "<code>stickyHeader</code> 블록이 따로 있습니다. 웹과 거의 같은 동작입니다."),
  ]),
  plat_note="iOS 는 <b>섹션 헤더가 기본으로 붙어서</b>, 디자이너가 \"머리글 붙여 주세요\"라고 하면 앱 쪽은 \"원래 붙는데요\"가 됩니다. 반대로 웹에서는 <b>안 붙는 게 기본</b>이라 같은 화면을 만들어도 드는 품이 다릅니다.",
  siblings=siblings("sticky"),
  related='''        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>''',
)
