# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ctr(inner_style="", box_style="display:grid;place-items:center", w="150px", h="76px", label="가운데"):
    return ('              <div style="width:100%;max-width:' + w + ';height:' + h + ';background:var(--surface);'
            'border:1px dashed var(--line-strong);border-radius:6px;position:relative;' + box_style + '">'
            '<span style="display:grid;place-items:center;width:52px;height:28px;border-radius:5px;'
            'background:var(--accent);color:#fff;font-size:10.5px;font-weight:700;' + inner_style + '">' + label + '</span></div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="height:78px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:7px;display:grid;place-items:center;max-width:240px">
                    <span style="display:grid;place-items:center;width:62px;height:30px;border-radius:5px;background:var(--accent);color:#fff;font-size:11px;font-weight:700">가운데</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">display: grid; place-items: center</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">display: flex; align-items + justify-content</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">margin-inline: auto   — 가로만</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">position: absolute + translate(-50%, -50%)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">text-align: center   — 글에만. 세로는 못 맞춘다</div>
                </div>
              </div>'''

D = dict(
  slug="center", ko="가운데 맞추기", en="Centering",
  desc="가운데 놓는 다섯 가지 방법과 되는 범위의 차이를 실물과 해부도로 보여주는 항목.",
  lede="'가운데에 놓기'는 방법이 다섯 가지나 되는데 <b>되는 범위가 다 다릅니다.</b> 그래서 유독 자주 틀립니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>다섯 칸 아래에 <b>가로·세로가 실제로 맞았는지</b> 재서 표시해 뒀습니다.
          처음엔 다섯 다 맞아 보이는데, <b>글을 두 줄로 늘려 보세요</b> —
          <code>margin: auto</code>와 <code>text-align</code>은 세로가 따라오지 않습니다.
          위에서 일정한 거리만큼 떨어뜨려 놓은 것뿐이라 그렇습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "가운데 맞추기, 가운데 정렬, 센터링"),
    ("영어", "centering, center alignment"),
    ("같이 쓰는 말",
     "가로 가운데는 <b>수평 정렬</b>, 세로 가운데는 <b>수직 정렬</b>(vertical centering)이라 합니다. "
     "<code>place-items</code>는 <code>align-items</code>와 <code>justify-items</code>를 한 번에 적은 것이고, "
     "<code>place-content</code>는 <b>내용 덩어리 전체</b>를 옮깁니다."),
    ("자주 잘못 부름",
     "<b><code>vertical-align</code></b> — 이름 때문에 세로 가운데에 쓸 것 같지만, "
     "<b>글줄 안에서 글자끼리</b> 맞추는 속성입니다. 블록을 가운데로 못 옮깁니다.<br>"
     "<b><code>text-align: center</code></b> — <b>글만</b> 가운데로 갑니다. 상자 자체는 안 움직입니다.<br>"
     "<b><code>align-content</code></b> — items 와 content 는 다릅니다. content 는 <b>줄 덩어리 전체</b>를 옮깁니다."),
  ]),
  axes=ax("가운데 맞추기"),
  oneline="외울 것은 하나입니다 — <b>부모에 <code>display: grid; place-items: center</code></b>. 가로·세로가 한 줄로 끝납니다.",
  s4_title="방법", s4_hint="되는 범위가 다 다르다",
  states=states([
    (ctr(), "place-items", "<b>그리드 한 줄.</b> 가로·세로가 동시에, 자식이 몇 개든"),
    (ctr(box_style="display:flex;align-items:center;justify-content:center"), "flex ×2", "두 줄이지만 가장 많이 쓰인다"),
    (ctr(inner_style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)", box_style=""),
     "absolute", "<b>흐름에서 빠진다.</b> 부모 크기에 영향을 못 준다"),
    (ctr(inner_style="margin:24px auto", box_style="display:flow-root"), "margin: auto", "<b>가로만.</b> 세로는 못 맞춘다"),
    (ctr(inner_style="display:inline-grid", box_style="text-align:center;padding-top:24px"), "text-align", "<b>글만.</b> 블록은 안 움직인다"),
    ('''              <div style="width:100%;max-width:150px;height:76px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;display:grid;place-items:center;gap:4px">
                <span style="display:grid;place-items:center;width:52px;height:22px;border-radius:5px;background:var(--accent);color:#fff;font-size:10px;font-weight:700">하나</span>
                <span style="display:grid;place-items:center;width:52px;height:22px;border-radius:5px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700">둘</span>
              </div>''',
     "자식 여럿", "<code>place-items</code>는 자식이 <b>몇 개든</b> 가운데로 모은다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("가운데에 놓인 것", "centered item", "자식 하나 또는 여럿. <b>자식이 아니라 부모가 정한다</b>"),
    ("그리드 방법", "place-items: center", "<b>한 줄로 가로·세로.</b> 외울 것은 이것 하나면 된다"),
    ("플렉스 방법", "align-items + justify-content", "두 줄. 주축·교차축 개념이 필요해 한 번 더 생각하게 된다"),
    ("가로만", "margin-inline: auto", "블록의 <b>가로</b> 가운데. 세로는 못 맞춘다 — 가장 흔한 착각"),
    ("흐름에서 빼기", "absolute + translate", "부모 크기에 영향을 못 준다. <b>겹쳐 놓을 때만</b> 쓴다"),
    ("글만", "text-align: center", "글줄만 가운데로. 상자 자체는 제자리에 있다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '세로 가운데가 안 된다'는 고민의 거의 전부가 <b><code>margin: auto</code>와 <code>text-align</code>을
          세로에도 쓸 수 있다고 생각해서</b> 생깁니다. 둘 다 가로 전용입니다.
          세로를 맞추려면 <b>부모가 플렉스나 그리드여야</b> 합니다 — 세로 가운데는
          자식 혼자서는 정할 수 없는 일입니다.</p>''',
  do=ul([
    "<b>부모 안에 하나만</b> 놓을 때 — 빈 상태, 로딩 스피너, 아이콘 버튼",
    "자식이 여럿이라도 다 가운데로 모아야 할 때",
    "<b>세로</b> 가운데가 필요할 때 — 방법이 둘뿐입니다(그리드·플렉스)",
  ]),
  dont=ul([
    "읽는 <b>긴 글</b>을 가운데 정렬하는 것 — 줄 시작이 들쭉날쭉해 읽기 힘듭니다",
    "<code>position: absolute</code>로 가운데 놓고 부모 높이를 기대하는 것 — <b>흐름에서 빠져</b> 부모가 0이 됩니다",
    "<code>vertical-align</code>으로 블록을 옮기려는 것 — 안 됩니다",
  ]),
  instead='여럿을 줄 세우며 가운데면 <a href="flex.html">플렉스</a>, 판을 짜면 <a href="grid.html">그리드</a>, 화면 가운데 띄우면 <a href="../items/modal.html">모달</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:170px;height:92px;background:var(--surface);border:1px solid var(--line);border-radius:8px;display:grid;place-items:center;gap:5px;text-align:center">
                <span style="width:26px;height:26px;border-radius:99px;background:var(--bg)"></span>
                <span style="font-size:11px;font-weight:700">아직 정산이 없습니다</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">첫 정산을 올려 보세요</span>
              </div>''',
     "빈 상태", "<code>place-items: center</code> 한 줄. <b>자식이 셋이어도 그대로</b>"),
    ('''              <div style="width:100%;max-width:170px;height:92px;background:var(--surface);border:1px solid var(--line);border-radius:8px;display:grid;place-items:center">
                <span class="spn" style="width:22px;height:22px"></span>
              </div>''',
     "로딩", "가장 짧게 쓰이는 자리"),
    ('''              <div style="width:100%;max-width:170px;display:inline-flex;align-items:center;justify-content:center;gap:5px;background:var(--accent);color:#fff;border-radius:7px;padding:9px 14px;font-size:11.5px;font-weight:700">
                <span style="width:12px;height:12px;border-radius:3px;background:rgba(255,255,255,.7)"></span> 저장하기
              </div>''',
     "아이콘 + 글자", "버튼 안에서도 같은 문제. <b>플렉스로 가운데</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="외울 것은 한 줄",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="다섯 가지를 다 외울 필요는 없습니다. <b>한 줄</b>만 외우고 나머지는 '그런 것도 있다'로 둡니다.",
  code='''<span class="c">/* 이것 하나면 거의 끝난다 — 가로·세로 동시에 */</span>
<span class="t">.center</span> { <span class="a">display</span>: grid; <span class="a">place-items</span>: center; }

<span class="c">/* 많이 쓰이는 플렉스 방식 — 두 줄 */</span>
<span class="t">.center</span> { <span class="a">display</span>: flex; <span class="a">align-items</span>: center; <span class="a">justify-content</span>: center; }

<span class="c">/* 가로만 — 블록 하나를 가운데로 */</span>
<span class="t">.container</span> { <span class="a">max-width</span>: <span class="a">65ch</span>; <span class="a">margin-inline</span>: auto; }

<span class="c">/* 겹쳐 놓을 때만 — 흐름에서 빠진다 */</span>
<span class="t">.overlay</span> { <span class="a">position</span>: absolute; <span class="a">left</span>: <span class="a">50%</span>; <span class="a">top</span>: <span class="a">50%</span>;
            <span class="a">transform</span>: <span class="t">translate</span>(-<span class="a">50%</span>, -<span class="a">50%</span>); }''',
  keys=kbd([
    ("부모가 정한다", "가운데 놓기는 <b>자식이 아니라 부모</b>의 일이다. 자식만 고치면 세로는 안 된다"),
    ("<code>place-items: center</code>", "한 줄로 끝난다. 자식이 몇 개든 상관없다"),
    ("<code>margin: auto</code>는 가로만", "세로 가운데에는 쓸 수 없다. <b>가장 흔한 착각</b>"),
    ("<code>text-align</code>은 글만", "상자 자체는 안 움직인다"),
    ("읽는 글은 가운데 정렬하지 않는다", "줄 시작이 들쭉날쭉해져 눈이 다음 줄을 못 찾는다"),
    ("<code>absolute</code>는 마지막 수단", "부모 높이에 영향을 못 줘서 <b>부모가 0</b>이 되는 일이 생긴다"),
  ]),
  backend=rows([
    ("가운데 놓기 = 부모의 책임", "자식에게 아무 값도 안 줘도 됩니다. <b>부모 설정 하나로 모든 자식</b>이 따라오는 구조라, 공통 레이아웃 컴포넌트로 빼기 좋습니다."),
    ("빈 상태와 로딩", "<a href=\"../items/empty.html\">빈 상태</a>와 <a href=\"../items/spinner.html\">스피너</a>는 거의 늘 가운데입니다. <b>같은 래퍼</b>를 돌려쓰면 화면마다 다르게 보이는 일이 없어집니다."),
    ("높이가 없으면 가운데도 없다", "부모 높이가 내용과 똑같으면 '가운데'가 제자리입니다. <code>min-height</code>를 주는 것이 먼저입니다."),
  ]),
  plat_lede="세 플랫폼 모두 '부모가 정한다'는 점이 같습니다.",
  plats=plats([
    ("웹", "CSS",
     ctr(w="120px", h="62px"),
     "<code>place-items: center</code> 또는 flex 두 줄. <b>세로 가운데는 부모가 flex·grid 여야</b> 합니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">ZStack { }<br>.frame(maxWidth:<br>&nbsp;.infinity)</div>''',
     "<b>ZStack</b> 의 기본 정렬이 가운데입니다. 또는 <code>Spacer()</code> 를 위아래에 둡니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Box(contentAlignment<br>&nbsp;= Alignment.Center)</div>''',
     "<b>Box</b> 에 <code>contentAlignment</code> 하나로 끝납니다. 웹의 <code>place-items</code> 와 가장 닮았습니다."),
  ]),
  plat_note="세 쪽 다 짧게 끝나는 일이라 소통 문제가 거의 없습니다. 다만 <b>'가운데'가 무엇의 가운데인지</b>는 확인하세요 — 화면 가운데인지, 카드 안 가운데인지, 글줄 가운데인지에 따라 전혀 다른 코드가 됩니다.",
  siblings=siblings("center"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>''',
)
