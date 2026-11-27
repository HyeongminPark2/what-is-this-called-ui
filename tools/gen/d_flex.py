# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">flex: 1   남은 자리를 차지함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">min-width: 0   없으면 줄어들지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="flex", ko="플렉스", en="Flexbox · flex layout",
  desc="플렉스의 주축과 교차축, flex:1, 그리고 min-width:0을 빠뜨려서 생기는 문제를 실물과 해부도로 보여 주는 항목입니다.",
  lede="플렉스는 자식 요소들을 <b>한 줄(또는 한 열)에 늘어놓는</b> 방법입니다. 화면에서 요소를 가로로 늘어놓는 배치는 대부분 플렉스로 만듭니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>방향을 <code>column</code>으로 바꿔 보세요. <b><code>justify-content</code>와 <code>align-items</code>가 맡는 방향이 서로 뒤바뀝니다</b>.
          두 속성은 가로·세로가 아니라 <b>주축·교차축</b>을 기준으로 하기 때문입니다.<br>
          <b><code>flex: 1</code></b>을 켜면 가운데 칸이 남은 자리를 모두 차지합니다. 여기에 <b>긴 글</b>까지 켜 보세요.
          <code>min-width: 0</code>이 없으면 가운데 칸이 글 길이만큼 넓어지면서 '뒤' 칸을 밀어내는데, 이때 아래 코드에 <code>min-width: 0</code> 줄이 함께 붙습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "플렉스, 플렉스박스, 플렉스 레이아웃"),
    ("영어", "flexbox, flex layout, flex container / flex item"),
    ("같이 쓰는 말",
     "자식을 늘어놓는 방향은 <b>주축</b>(main axis), 주축을 가로지르는 방향은 <b>교차축</b>(cross axis)이라고 부릅니다. "
     "<code>display: flex</code>를 준 부모는 <b>플렉스 컨테이너</b>, 그 자식은 <b>플렉스 아이템</b>입니다. "
     "<code>flex</code>는 <b>grow·shrink·basis</b> 세 값을 한 번에 적는 단축 속성이고, "
     "자리가 모자랄 때 다음 줄로 넘기는 것은 <b>랩</b>(wrap)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>그리드</b> — 플렉스는 <b>한 방향</b>으로 늘어놓고, 그리드는 <b>두 방향</b>으로 칸을 나눕니다. 플렉스도 줄을 넘길 수는 있지만, 줄을 넘기는 것과 판을 짜는 것은 다릅니다.<br>"
     "<b>가로 정렬</b> — <code>justify-content</code>는 방향에 따라 세로 정렬이 되기도 하므로, <b>주축</b> 정렬이라고 불러야 헷갈리지 않습니다.<br>"
     "<b>flex: 1</b> — '너비 100%'가 아니라 <b>남은 자리를 한 몫 나눠 받으라</b>는 뜻입니다."),
  ]),
  s4_title="자주 쓰는 여섯 가지 배치", s4_hint="속성 값에 따라 달라지는 자식의 자리",
  states=states([
    (row(), "아무 값도 주지 않았을 때", "자식이 <b>내용만큼</b> 자리를 차지하고 왼쪽부터 붙습니다"),
    (row("justify-content:space-between"), "<code>space-between</code>으로 나눌 때", "양 끝에 붙이고 <b>사이 간격을 똑같이</b> 나눕니다"),
    (row("justify-content:center;gap:6px"), "<code>center</code>와 <code>gap</code>을 함께 줄 때", "가운데로 모으고 사이를 띄웁니다"),
    (row("", mid_style="flex:1;min-width:0"), "가운데 칸에 <code>flex: 1</code>을 줄 때", "가운데 칸만 <b>남은 자리를 모두 차지합니다</b>"),
    (row("flex-direction:column;gap:5px;align-items:flex-start"), "방향을 <code>column</code>으로 바꿀 때", "방향을 바꾸면 <b>justify-content가 세로 정렬</b>을 맡습니다"),
    (row("flex-wrap:wrap;gap:5px", ("앞", "가운데", "뒤", "넷", "다섯", "여섯")), "<code>wrap</code>으로 줄을 넘길 때", "자리가 모자라면 다음 줄로 넘깁니다. <b>켜지 않으면 모든 칸이 좁게 찌그러집니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("플렉스 컨테이너", "flex container", "<code>display: flex</code>를 준 <b>부모</b>입니다. 그 자식들은 자동으로 플렉스 아이템이 됩니다"),
    ("주축", "main axis", "자식을 <b>늘어놓는 방향</b>이며, <code>flex-direction</code>으로 정합니다"),
    ("주축 정렬", "justify-content", "주축에서 자식을 어느 쪽으로 모을지 정합니다. <b>방향을 바꾸면 세로 정렬이 됩니다</b>"),
    ("교차축 정렬", "align-items", "주축을 가로지르는 방향의 정렬입니다. 기본값이 <code>stretch</code>라서 자식 높이가 저절로 같아집니다"),
    ("늘어나기", "flex: 1", "<b>남은 자리를 한 몫씩</b> 나눠 받습니다. '앞·가운데·뒤' 짜임에서 가운데 칸을 늘리는 데 씁니다"),
    ("줄어들기", "min-width: 0", "플렉스 자식의 최소 너비는 기본값이 <b>내용만큼</b>이라서, 이 줄이 없으면 내용보다 좁게 줄어들지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>min-width: 0</code>은 이 도감에서 <b>가장 자주 나오는 코드 한 줄</b>입니다.
          플렉스·그리드 자식의 자동 최소 크기는 <b>'내용만큼'</b>이라서, 긴 글이 들어오면 칸이 내용보다 좁아지지 않고
          옆 칸을 밀어냅니다. 말줄임이 걸리지 않거나, 가로 스크롤이 생기거나,
          레이아웃이 판 밖으로 넘치는 문제는 대개 이 한 줄이 빠져서 생깁니다.</p>''',
  do=ul([
    "상단 바, 리스트 아이템, 버튼 줄처럼 요소를 <b>한 줄에 늘어놓을</b> 때",
    "'앞·가운데·뒤' 짜임에서 가운데 칸만 늘어나야 할 때",
    "개수가 정해지지 않은 것들을 나란히 둘 때",
    "한 줄 안에서 세로 가운데를 맞출 때. <code>align-items: center</code> 한 줄이면 됩니다",
  ]),
  dont=ul([
    "<b>줄과 열이 서로 맞아야</b> 할 때. 플렉스는 줄마다 따로 배치해서 위아래 줄의 칸을 맞추지 못하므로 <a href=\"grid.html\">그리드</a>를 씁니다",
    "사이드바, 본문, 꼬리말로 판 전체를 짤 때. 그리드로 짜는 편이 구조가 더 분명합니다",
    "한 칸만 가운데 놓으면 될 때. 그리드의 <code>place-items: center</code> 한 줄이 더 짧습니다",
  ]),
  instead='가로와 세로 두 방향을 함께 맞춰야 하면 <a href="grid.html">그리드</a>를 쓰고, 요소 하나를 가운데에 놓기만 하면 되는 경우는 <a href="center.html">가운데 맞추기</a>에서 다룹니다. 내용이 넘친 뒤 어떻게 처리할지는 <a href="overflow.html">넘침</a>에서 봅니다.',
  cases=cases([
    (row("align-items:center;gap:7px", ("☰", "모란상회", "설정"), "flex:1;min-width:0", "200px"),
     "상단 바를 앞·가운데·뒤로 나누기", "<b>앞 · 가운데(늘어남) · 뒤</b>로 나눈, 가장 흔한 짜임입니다"),
    (row("align-items:center;gap:7px", ("아바타", "제목과 보조 글", "₩48,000"), "flex:1;min-width:0", "200px"),
     "리스트 아이템 한 줄 만들기", "상단 바와 같은 짜임으로 목록의 한 줄을 만듭니다"),
    (row("justify-content:flex-end;gap:6px", ("취소", "저장"), "", "200px"),
     "버튼 줄을 오른쪽에 모으기", "버튼을 오른쪽에 모으고, <b>주 동작 버튼을 바깥쪽</b>에 둡니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="플렉스를 쓸 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="플렉스는 대개 <b>부모에 한 줄, 자식에 한 줄</b>만 적으면 원하는 배치가 나옵니다.",
  code='''<span class="t">.bar</span> {
  <span class="a">display</span>: flex;
  <span class="a">align-items</span>: center;   <span class="c">/* 교차축(세로) 가운데 */</span>
  <span class="a">gap</span>: <span class="a">12px</span>;
}

<span class="t">.bar__title</span> {
  <span class="a">flex</span>: <span class="a">1</span>;          <span class="c">/* 남은 자리를 차지한다 */</span>
  <span class="a">min-width</span>: <span class="a">0</span>;     <span class="c">/* 이게 없으면 긴 글에 밀려 안 줄어든다 */</span>
  <span class="a">overflow</span>: hidden;
  <span class="a">text-overflow</span>: ellipsis;
  <span class="a">white-space</span>: nowrap;
}

<span class="c">/* 빈 칸을 넣지 않고 이 한 줄로 오른쪽 끝에 붙인다 */</span>
<span class="t">.bar__end</span> { <span class="a">margin-left</span>: auto; }''',
  keys=kbd([
    ("간격은 <code>gap</code>으로 주기", "자식에 마진을 주면 <b>첫 칸과 끝 칸</b>의 바깥 여백을 따로 처리해야 하지만, gap은 칸 사이에만 들어갑니다"),
    ("줄어들 칸에 <code>min-width: 0</code> 주기", "줄어들어야 하는 칸에는 거의 항상 필요합니다. <b>이 도감에서 가장 자주 나오는 한 줄</b>입니다"),
    ("끝으로 밀 때는 <code>margin-left: auto</code> 쓰기", "한 칸만 오른쪽 끝으로 밀 때 씁니다. 자리를 채우려고 빈 <code>&lt;div&gt;</code>를 넣지 않습니다"),
    ("<code>flex-wrap</code>이 필요한지 따져 보기", "기본값이 <code>nowrap</code>이라서 화면이 좁아지면 <b>모든 칸이 찌그러집니다</b>"),
    ("CSS로 순서를 바꾸지 않기", "<code>order</code>나 <code>row-reverse</code>를 쓰면 <b>보이는 순서와 탭 순서가 어긋납니다</b>"),
    ("<code>align-items</code>의 기본값이 <code>stretch</code>라는 점 기억하기", "자식 높이가 저절로 같아지기 때문에, 아이콘이 세로로 늘어나 보이면 대개 이 기본값이 원인입니다"),
  ]),
  backend=rows([
    ("남은 자리를 비율대로 나누는 계산", "<code>flex: 1</code>은 남은 폭을 비율대로 나누라는 뜻입니다. 고정 칸의 폭을 먼저 빼고 나머지를 나눠 주기 때문에, <b>총량이 정해진 자원을 배분</b>하는 계산과 같습니다."),
    ("내용 길이에 따라 달라지는 배치", "이름이 길면 옆 칸이 밀려납니다. 그래서 <b>가장 긴 값</b>과 <b>빈 값</b>을 하나씩 넣고 화면을 그려 보는 것이 최소한의 테스트입니다."),
    ("버튼 개수가 바뀌는 경우", "서버가 버튼을 3개 보낼지 7개 보낼지 미리 알 수 없다면 <code>flex-wrap: wrap</code>을 켜 둡니다. 켜지 않으면 좁은 화면에서 버튼이 모두 찌그러집니다."),
    ("보이는 순서와 키보드 순서", "<code>order</code>로 눈에 보이는 순서를 바꿔도 <b>키보드 순서는 바뀌지 않습니다.</b> 그래서 화면에서 순서를 바꾸기보다 서버가 내려 주는 순서를 그대로 쓰는 편이 안전합니다."),
  ]),
  plat_lede="세 플랫폼 모두 같은 방식으로 늘어놓고, 부르는 이름만 다릅니다.",
  plats=plats([
    ("웹", "CSS Flexbox",
     row("gap:5px", ("앞", "가운데", "뒤"), "flex:1;min-width:0", "130px"),
     "<code>display: flex</code>로 켭니다. 자식이 내용보다 좁아지지 않는 <b>자동 최소 크기</b> 문제는 웹에만 있습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">HStack { }<br>VStack { }<br>Spacer( )</div>''',
     "<b>HStack · VStack</b>이 플렉스에 해당합니다. <code>flex: 1</code> 대신 <b><code>Spacer()</code></b>나 <code>.frame(maxWidth: .infinity)</code>를 씁니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Row { }<br>Column { }<br>Modifier.weight(1f)</div>''',
     "플렉스에 해당하는 것은 <b>Row · Column</b>이고, <code>flex: 1</code>은 <b><code>Modifier.weight(1f)</code></b>로 씁니다. 개념이 거의 일대일로 대응합니다."),
  ]),
  plat_note="세 플랫폼의 방식이 같아서 \"가운데만 늘어나게 해 주세요\"라는 요청은 어디서나 그대로 통합니다. 다만 <b><code>min-width: 0</code> 문제는 웹에만</b> 있어서, 앱 개발자는 \"글이 길어도 안 줄어들어요\"라는 증상을 낯설어합니다. 이때는 <b>'칸이 내용보다 작아지지 못한다'</b>고 풀어 말하는 편이 빨리 통합니다.",
  siblings=siblings("flex"),
  related='''        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>''',
)
