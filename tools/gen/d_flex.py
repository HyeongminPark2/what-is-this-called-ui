# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(style="", items=("앞", "가운데", "뒤"), mid_style="", w="180px"):
    cells = ""
    for i, t in enumerate(items):
        st = ("background:var(--warn-soft);color:var(--warn);"
              "border-color:color-mix(in srgb,var(--warn) 35%,transparent);" + mid_style) if (i == 1 and mid_style) else ""
        cells += ('<span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);'
                  'border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;'
                  'font-size:10.5px;font-weight:700;padding:6px 8px;' + st + '">' + t + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:flex;background:var(--surface);'
            'border:1px dashed var(--line-strong);border-radius:6px;padding:7px;min-height:54px;' + style + '">'
            + cells + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:flex;align-items:center;gap:8px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:7px;padding:9px">
                    <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 9px">앞</span>
                    <span style="flex:1;min-width:0;display:grid;place-items:center;background:var(--warn-soft);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 9px">가운데</span>
                    <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 9px">뒤</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">flex-direction: row  ←→</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">justify-content  ←→  (주축)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">align-items  ↑↓  (교차축)</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">flex: 1   — 남은 자리를 먹는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">min-width: 0   — 이게 없으면 안 줄어든다</div>
                </div>
              </div>'''

D = dict(
  slug="flex", ko="플렉스", en="Flexbox · flex layout",
  desc="플렉스의 주축·교차축과 flex:1, min-width:0 함정을 실물과 해부도로 보여주는 항목.",
  lede="<b>한 줄(또는 한 열)에 늘어놓는</b> 방법. 화면의 가로 배치 거의 전부가 이것입니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>방향을 <code>column</code>으로 바꿔 보세요. <b><code>justify-content</code>와 <code>align-items</code>의 역할이 통째로 뒤집힙니다</b> —
          둘은 가로·세로가 아니라 <b>주축·교차축</b>을 가리키기 때문입니다.<br>
          <b><code>flex: 1</code></b>을 켜면 가운데 칸이 남은 자리를 다 먹습니다. 거기에 <b>긴 글</b>까지 켜 보세요 —
          <code>min-width: 0</code>이 없으면 칸이 글에 밀려 '뒤'를 쫓아냅니다. 아래 코드에 그 줄이 같이 붙습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "플렉스, 플렉스박스, 플렉스 레이아웃"),
    ("영어", "flexbox, flex layout, flex container / flex item"),
    ("같이 쓰는 말",
     "늘어놓는 방향을 <b>주축</b>(main axis), 가로지르는 방향을 <b>교차축</b>(cross axis)이라 합니다. "
     "부모가 <b>플렉스 컨테이너</b>, 자식이 <b>플렉스 아이템</b>입니다. "
     "<code>flex</code>는 <b>grow·shrink·basis</b> 세 값을 한 번에 적은 것이고, "
     "줄을 넘기는 것은 <b>랩</b>(wrap)입니다."),
    ("자주 잘못 부름",
     "<b>그리드</b> — 플렉스는 <b>한 방향</b>, 그리드는 <b>두 방향</b>입니다. 줄바꿈이 되는 것과 판을 짜는 것은 다릅니다.<br>"
     "<b>가로 정렬</b> — <code>justify-content</code>는 방향에 따라 세로가 되기도 합니다. <b>주축</b>이라고 불러야 안 헷갈립니다.<br>"
     "<b>flex: 1</b> — '너비 100%'가 아니라 <b>'남은 자리를 한 몫'</b>입니다."),
  ]),
  axes=ax("플렉스"),
  oneline="플렉스는 <b>한 줄에 늘어놓는 것</b>입니다. 줄과 열이 서로 맞아야 하면 그건 <a href=\"grid.html\">그리드</a>의 일입니다.",
  s4_title="갈래", s4_hint="같은 속성이 방향 따라 다르게 먹는다",
  states=states([
    (row(), "기본", "자식이 <b>내용만큼</b> 차지하고 왼쪽부터 붙는다"),
    (row("justify-content:space-between"), "space-between", "양 끝에 붙이고 <b>사이를 똑같이</b>"),
    (row("justify-content:center;gap:6px"), "center + gap", "가운데로 모으고 사이를 띄운다"),
    (row("", mid_style="flex:1;min-width:0"), "flex: 1", "가운데만 <b>남은 자리를 다 먹는다</b>"),
    (row("flex-direction:column;gap:5px;align-items:flex-start"), "column", "방향을 바꾸면 <b>justify 가 세로</b>가 된다"),
    (row("flex-wrap:wrap;gap:5px", ("앞", "가운데", "뒤", "넷", "다섯", "여섯")), "wrap", "넘치면 줄을 넘긴다. <b>안 켜면 다 찌그러진다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("플렉스 컨테이너", "flex container", "<code>display: flex</code>를 준 <b>부모</b>. 자식들이 자동으로 아이템이 된다"),
    ("주축", "main axis", "<code>flex-direction</code>이 정한다. <b>늘어놓는 방향</b>"),
    ("주축 정렬", "justify-content", "주축에서 어디로 모을지. <b>방향을 바꾸면 세로가 된다</b>"),
    ("교차축 정렬", "align-items", "가로지르는 방향. 기본값 <code>stretch</code>라 자식 높이가 저절로 같아진다"),
    ("늘어나기", "flex: 1", "<b>남은 자리를 한 몫씩</b>. '앞·가운데·뒤' 짜임의 핵심"),
    ("줄어들기", "min-width: 0", "플렉스 자식의 최소 너비는 <b>내용만큼</b>이다. 이 줄이 없으면 영영 안 줄어든다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>min-width: 0</code>은 이 도감에서 <b>가장 자주 나오는 한 줄</b>입니다.
          플렉스·그리드 자식의 자동 최소 크기가 <b>'내용만큼'</b>이라, 긴 글이 들어오면 칸이 줄어들기를
          거부하고 옆 칸을 밀어냅니다. 말줄임이 안 걸리는 것도, 가로 스크롤이 생기는 것도,
          판이 터지는 것도 대개 이 한 줄이 빠져서입니다.</p>''',
  do=ul([
    "<b>한 줄에 늘어놓을</b> 때 — 상단 바, 리스트 아이템, 버튼 줄",
    "'앞·가운데·뒤' 짜임 — 가운데만 늘어나야 할 때",
    "개수가 정해지지 않은 것들을 나란히 둘 때",
    "세로 가운데 맞추기 — <code>align-items: center</code> 한 줄",
  ]),
  dont=ul([
    "<b>줄과 열이 서로 맞아야</b> 할 때 → <a href=\"grid.html\">그리드</a>. 플렉스는 줄끼리 모릅니다",
    "판 전체의 짜임(사이드바 + 본문 + 꼬리말) → 그리드가 더 또렷합니다",
    "한 칸만 가운데 놓으면 될 때 — <code>place-items: center</code> 한 줄이 더 짧습니다",
  ]),
  instead='두 방향이면 <a href="grid.html">그리드</a>, 가운데만 놓으면 <a href="center.html">가운데 맞추기</a>, 넘친 뒤 처리는 <a href="overflow.html">넘침</a>.',
  cases=cases([
    (row("align-items:center;gap:7px", ("☰", "모란상회", "설정"), "flex:1;min-width:0", "200px"),
     "상단 바", "<b>앞 · 가운데(늘어남) · 뒤</b>. 가장 흔한 짜임"),
    (row("align-items:center;gap:7px", ("아바타", "제목과 보조 글", "₩48,000"), "flex:1;min-width:0", "200px"),
     "리스트 아이템", "같은 짜임이 목록의 한 줄이 된다"),
    (row("justify-content:flex-end;gap:6px", ("취소", "저장"), "", "200px"),
     "버튼 줄", "오른쪽에 모은다. <b>주 동작이 바깥쪽</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 부품의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="플렉스는 <b>부모에 한 줄, 자식에 한 줄</b>이면 거의 끝납니다.",
  code='''<span class="t">.bar</span> {
  <span class="a">display</span>: flex;
  <span class="a">align-items</span>: center;   <span class="c">/* 교차축 — 세로 가운데 */</span>
  <span class="a">gap</span>: <span class="a">12px</span>;
}

<span class="t">.bar__title</span> {
  <span class="a">flex</span>: <span class="a">1</span>;          <span class="c">/* 남은 자리를 먹는다 */</span>
  <span class="a">min-width</span>: <span class="a">0</span>;     <span class="c">/* 이게 없으면 긴 글에 밀려 안 줄어든다 */</span>
  <span class="a">overflow</span>: hidden;
  <span class="a">text-overflow</span>: ellipsis;
  <span class="a">white-space</span>: nowrap;
}

<span class="c">/* 오른쪽 끝으로 밀기 — 빈 칸 대신 이 한 줄 */</span>
<span class="t">.bar__end</span> { <span class="a">margin-left</span>: auto; }''',
  keys=kbd([
    ("<code>gap</code>을 쓴다", "자식에 마진을 주면 <b>첫 칸·끝 칸</b>을 따로 챙겨야 한다. gap 은 사이에만 들어간다"),
    ("<code>min-width: 0</code>", "줄어들어야 하는 칸에는 거의 늘 필요하다. <b>이 도감에서 가장 자주 나오는 한 줄</b>"),
    ("<code>margin-left: auto</code>", "한 칸만 오른쪽 끝으로 밀 때. 빈 <code>&lt;div&gt;</code>를 넣지 않는다"),
    ("<code>flex-wrap</code>을 생각한다", "기본값은 <code>nowrap</code>이라 좁아지면 <b>다 찌그러진다</b>"),
    ("순서를 바꾸지 않는다", "<code>order</code>나 <code>row-reverse</code>는 <b>보이는 순서와 탭 순서를 어긋나게</b> 한다"),
    ("<code>align-items: stretch</code>가 기본", "자식 높이가 저절로 같아진다. 아이콘이 늘어나 보이면 이것 때문이다"),
  ]),
  backend=rows([
    ("플렉스 = 남은 자리 나누기", "<code>flex: 1</code>은 '남은 폭을 비율대로 나눠라'입니다. 고정 칸을 먼저 빼고 나머지를 분배하는 것이라, <b>합이 정해진 자원 배분</b>과 같은 계산입니다."),
    ("내용 길이가 배치를 바꾼다", "이름이 길면 칸이 밀립니다. <b>가장 긴 값</b>과 <b>빈 값</b> 둘로 한 번씩 그려 보는 것이 최소 테스트입니다."),
    ("개수가 바뀌는 경우", "서버가 버튼을 3개 줄지 7개 줄지 모르면 <code>flex-wrap: wrap</code>을 켜 둡니다. 안 켜면 좁은 화면에서 전부 찌그러집니다."),
    ("순서와 접근성", "<code>order</code>로 눈에 보이는 순서를 바꿔도 <b>키보드 순서는 안 바뀝니다.</b> 서버가 내려주는 순서를 그대로 쓰는 편이 안전합니다."),
  ]),
  plat_lede="세 플랫폼 모두 거의 같은 생각이고, 이름만 다릅니다.",
  plats=plats([
    ("웹", "CSS Flexbox",
     row("gap:5px", ("앞", "가운데", "뒤"), "flex:1;min-width:0", "130px"),
     "<code>display: flex</code>. <b>자동 최소 크기</b>라는 함정이 웹에만 있습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">HStack { }<br>VStack { }<br>Spacer( )</div>''',
     "<b>HStack · VStack</b> 이 플렉스와 같습니다. <code>flex: 1</code> 자리에 <b><code>Spacer()</code></b>나 <code>.frame(maxWidth: .infinity)</code>를 씁니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Row { }<br>Column { }<br>Modifier.weight(1f)</div>''',
     "<b>Row · Column</b> 이고, <code>flex: 1</code> 은 <b><code>Modifier.weight(1f)</code></b> 입니다. 개념이 거의 1대1로 옮겨집니다."),
  ]),
  plat_note="세 쪽이 생각은 같아서 \"가운데만 늘어나게\"가 그대로 통합니다. 다만 <b><code>min-width: 0</code> 문제는 웹에만</b> 있습니다. 앱 개발자에게 \"글이 길어도 안 줄어들어요\"는 낯선 증상이니, <b>'칸이 내용보다 작아지지 못한다'</b>로 풀어 말하는 편이 빠릅니다.",
  siblings=siblings("flex"),
  related='''        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>''',
)
