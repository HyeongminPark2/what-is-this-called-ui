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
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">margin-inline: auto   가로만 맞춤</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">position: absolute + translate(-50%, -50%)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">text-align: center   글만 옮기고 세로는 못 맞춤</div>
                </div>
              </div>'''

D = dict(
  slug="center", ko="가운데 맞추기", en="Centering",
  desc="가운데에 놓는 다섯 가지 방법과 방법마다 맞출 수 있는 범위의 차이를 실물과 해부도로 보여 주는 항목입니다.",
  lede="요소를 가운데에 놓는 방법은 다섯 가지나 되지만, 방법마다 <b>가운데로 맞춰지는 범위가 다릅니다.</b> 그래서 다른 레이아웃보다 유독 자주 틀립니다.",
  axes_lede="뼈대 항목은 눈에 보이지 않고 자리만 정해서 생김새로는 가를 수 없습니다. 아래 네 가지로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>다섯 칸 아래에는 <b>가로·세로가 실제로 맞았는지</b> 재서 표시해 두었습니다.
          처음에는 다섯 칸 모두 맞아 보이지만, <b>글을 두 줄로 늘려 보면</b>
          <code>margin: auto</code>와 <code>text-align</code>은 세로 가운데가 어긋납니다.
          두 방법은 상자를 위에서 일정한 거리만큼 떨어뜨려 놓았을 뿐이라서, 상자 높이가 바뀌면 세로 위치가 따라오지 않기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "가운데 맞추기, 가운데 정렬, 센터링"),
    ("영어", "centering, center alignment"),
    ("같이 쓰는 말",
     "가로 가운데는 <b>수평 정렬</b>, 세로 가운데는 <b>수직 정렬</b>(vertical centering)이라고 부릅니다. "
     "<code>place-items</code>는 <code>align-items</code>와 <code>justify-items</code>를 한 번에 적는 단축 속성이고, "
     "<code>place-content</code>는 <b>내용 덩어리 전체</b>의 위치를 옮깁니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>vertical-align</code></b> — 이름 때문에 세로 가운데에 쓸 것 같지만, "
     "<b>글줄 안에서 글자끼리</b> 높이를 맞추는 속성이라서 블록을 가운데로 옮기지는 못합니다.<br>"
     "<b><code>text-align: center</code></b> — <b>글만</b> 가운데로 옮기고, 상자 자체는 움직이지 않습니다.<br>"
     "<b><code>align-content</code></b> — items와 content는 옮기는 대상이 다릅니다. items는 자식 하나하나를, content는 <b>줄 덩어리 전체</b>를 옮깁니다."),
  ]),
  axes=ax("가운데 맞추기"),
  oneline="외울 것은 <b>부모에 <code>display: grid; place-items: center</code></b>를 주는 방법 하나입니다. 이 한 줄로 가로와 세로를 함께 맞출 수 있습니다.",
  s4_title="가운데에 놓는 방법", s4_hint="방법마다 맞출 수 있는 범위",
  states=states([
    (ctr(), "그리드의 <code>place-items</code>로 맞출 때", "<b>그리드 한 줄</b>로 가로·세로를 함께 맞추며, 자식이 몇 개든 상관없습니다"),
    (ctr(box_style="display:flex;align-items:center;justify-content:center"), "플렉스 정렬 두 줄로 맞출 때", "두 줄이 필요하지만 가장 많이 쓰는 방법입니다"),
    (ctr(inner_style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)", box_style=""),
     "<code>absolute</code>로 띄워서 맞출 때", "<b>흐름에서 빠지기</b> 때문에 부모 크기에 영향을 주지 못합니다"),
    (ctr(inner_style="margin:24px auto", box_style="display:flow-root"), "<code>margin: auto</code>로 맞출 때", "<b>가로만</b> 맞추고 세로는 맞추지 못합니다"),
    (ctr(inner_style="display:inline-grid", box_style="text-align:center;padding-top:24px"), "<code>text-align</code>으로 맞출 때", "<b>글만</b> 가운데로 옮기고 블록은 움직이지 않습니다"),
    ('''              <div style="width:100%;max-width:150px;height:76px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;display:grid;place-items:center;gap:4px">
                <span style="display:grid;place-items:center;width:52px;height:22px;border-radius:5px;background:var(--accent);color:#fff;font-size:10px;font-weight:700">하나</span>
                <span style="display:grid;place-items:center;width:52px;height:22px;border-radius:5px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700">둘</span>
              </div>''',
     "자식이 여럿일 때", "<code>place-items</code>는 자식이 <b>몇 개든</b> 가운데로 모읍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("가운데에 놓인 것", "centered item", "자식 하나일 수도, 여럿일 수도 있습니다. 가운데 위치는 <b>자식이 아니라 부모가 정합니다</b>"),
    ("그리드 방법", "place-items: center", "<b>한 줄로 가로·세로를</b> 함께 맞춥니다. 외울 것은 이것 하나면 됩니다"),
    ("플렉스 방법", "align-items + justify-content", "두 줄을 적어야 하고, 주축·교차축 개념을 알아야 해서 한 번 더 생각하게 됩니다"),
    ("마진 방법", "margin-inline: auto", "블록의 <b>가로</b> 가운데만 맞춥니다. 세로도 맞출 수 있다고 생각하는 것이 가장 흔한 착각입니다"),
    ("절대 위치 방법", "absolute + translate", "부모 크기에 영향을 주지 못하기 때문에 <b>겹쳐 놓을 때만</b> 씁니다"),
    ("글 정렬 방법", "text-align: center", "글줄만 가운데로 옮기고, 상자 자체는 제자리에 있습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '세로 가운데가 안 맞는다'는 문제는 대부분 <b><code>margin: auto</code>와 <code>text-align</code>을
          세로에도 쓸 수 있다고 생각해서</b> 생기지만, 두 속성은 가로에만 작동합니다.
          세로 가운데는 자식 혼자서는 정할 수 없기 때문에, 세로를 맞추려면
          <b>부모를 플렉스나 그리드로</b> 만들어야 합니다.</p>''',
  do=ul([
    "빈 상태, 로딩 스피너, 아이콘 버튼처럼 <b>부모 안에 하나만</b> 놓을 때",
    "자식이 여럿이라도 다 가운데로 모아야 할 때",
    "<b>세로</b> 가운데가 필요할 때. 세로를 맞추는 방법은 그리드와 플렉스 두 가지뿐입니다",
  ]),
  dont=ul([
    "읽어야 하는 <b>긴 글</b>을 가운데 정렬할 때. 줄 시작 위치가 들쭉날쭉해서 읽기 힘듭니다",
    "<code>position: absolute</code>로 가운데에 놓으면서 부모가 자식 높이만큼 커지길 기대할 때. 자식이 <b>흐름에서 빠지므로</b> 부모 높이가 0이 됩니다",
    "<code>vertical-align</code>으로 블록을 옮기려 할 때. 이 속성으로는 블록이 움직이지 않습니다",
  ]),
  instead='여러 요소를 한 줄로 세우면서 가운데에 모으려면 <a href="flex.html">플렉스</a>를, 판 전체를 칸으로 나눠야 하면 <a href="grid.html">그리드</a>를 씁니다. 화면 한가운데에 창을 띄우는 일이라면 <a href="../items/modal.html">모달</a>을 봅니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:170px;height:92px;background:var(--surface);border:1px solid var(--line);border-radius:8px;display:grid;place-items:center;gap:5px;text-align:center">
                <span style="width:26px;height:26px;border-radius:99px;background:var(--bg)"></span>
                <span style="font-size:11px;font-weight:700">아직 정산이 없습니다</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">첫 정산을 올려 보세요</span>
              </div>''',
     "빈 상태 안내를 가운데에 놓기", "<code>place-items: center</code> 한 줄로 맞추며, <b>자식이 셋이어도 그대로</b> 가운데에 모입니다"),
    ('''              <div style="width:100%;max-width:170px;height:92px;background:var(--surface);border:1px solid var(--line);border-radius:8px;display:grid;place-items:center">
                <span class="spn" style="width:22px;height:22px"></span>
              </div>''',
     "로딩 스피너를 가운데에 놓기", "가운데 맞추기를 가장 간단하게 쓰는 자리입니다"),
    ('''              <div style="width:100%;max-width:170px;display:inline-flex;align-items:center;justify-content:center;gap:5px;background:var(--accent);color:#fff;border-radius:7px;padding:9px 14px;font-size:11.5px;font-weight:700">
                <span style="width:12px;height:12px;border-radius:3px;background:rgba(255,255,255,.7)"></span> 저장하기
              </div>''',
     "버튼 안 아이콘과 글자 맞추기", "버튼 안에서도 아이콘과 글자를 가운데에 맞춰야 하는데, 이때는 <b>플렉스로 가운데</b>를 맞춥니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="외워 둘 한 줄과 지킬 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="다섯 가지를 다 외울 필요는 없습니다. <b>한 줄</b>만 외우고 나머지는 이런 방법도 있다는 정도로 알아 두면 됩니다.",
  code='''<span class="c">/* 대부분 이것 하나로 된다. 가로·세로를 함께 맞춘다 */</span>
<span class="t">.center</span> { <span class="a">display</span>: grid; <span class="a">place-items</span>: center; }

<span class="c">/* 많이 쓰는 플렉스 방식(두 줄) */</span>
<span class="t">.center</span> { <span class="a">display</span>: flex; <span class="a">align-items</span>: center; <span class="a">justify-content</span>: center; }

<span class="c">/* 블록 하나를 가로로만 가운데에 놓는다 */</span>
<span class="t">.container</span> { <span class="a">max-width</span>: <span class="a">65ch</span>; <span class="a">margin-inline</span>: auto; }

<span class="c">/* 흐름에서 빠지므로 겹쳐 놓을 때만 쓴다 */</span>
<span class="t">.overlay</span> { <span class="a">position</span>: absolute; <span class="a">left</span>: <span class="a">50%</span>; <span class="a">top</span>: <span class="a">50%</span>;
            <span class="a">transform</span>: <span class="t">translate</span>(-<span class="a">50%</span>, -<span class="a">50%</span>); }''',
  keys=kbd([
    ("가운데 위치는 부모에서 정하기", "가운데 놓기는 <b>자식이 아니라 부모</b>에 설정합니다. 자식만 고쳐서는 세로 가운데를 맞출 수 없습니다"),
    ("<code>place-items: center</code> 한 줄 외워 두기", "한 줄로 가로·세로를 맞추며, 자식이 몇 개든 상관없습니다"),
    ("<code>margin: auto</code>는 가로만 맞춘다는 점 기억하기", "세로 가운데에는 쓸 수 없는데, 쓸 수 있다고 생각하는 것이 <b>가장 흔한 착각</b>입니다"),
    ("<code>text-align</code>은 글만 옮긴다는 점 기억하기", "글만 옮기고 상자 자체는 움직이지 않습니다"),
    ("읽는 글은 가운데 정렬하지 않기", "줄 시작 위치가 들쭉날쭉해져서 다음 줄의 시작을 찾기 어렵습니다"),
    ("<code>absolute</code>는 다른 방법이 안 될 때만 쓰기", "부모 높이에 영향을 주지 못해서 <b>부모 높이가 0</b>이 되는 일이 생깁니다"),
  ]),
  backend=rows([
    ("가운데 위치를 부모가 맡는 구조", "자식에게는 아무 값도 주지 않아도 됩니다. <b>부모 설정 하나로 모든 자식</b>이 가운데로 모이기 때문에, 공통 레이아웃 컴포넌트로 빼 두기 좋습니다."),
    ("빈 상태와 로딩에 같은 래퍼 쓰기", "<a href=\"../items/empty.html\">빈 상태</a>와 <a href=\"../items/spinner.html\">스피너</a>는 거의 항상 가운데에 놓입니다. <b>같은 래퍼</b> 컴포넌트를 돌려쓰면 화면마다 위치가 다르게 보이는 일이 없어집니다."),
    ("부모 높이를 먼저 정해 두기", "부모 높이가 내용 높이와 같으면 가운데에 놓아도 제자리와 구별되지 않습니다. 그래서 부모에 <code>min-height</code>를 먼저 줘야 합니다."),
  ]),
  plat_lede="세 플랫폼 모두 가운데 위치를 부모가 정한다는 점이 같습니다.",
  plats=plats([
    ("웹", "CSS",
     ctr(w="120px", h="62px"),
     "<code>place-items: center</code> 한 줄이나 flex 두 줄로 맞춥니다. <b>세로 가운데를 맞추려면 부모가 flex나 grid여야</b> 합니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">ZStack { }<br>.frame(maxWidth:<br>&nbsp;.infinity)</div>''',
     "<b>ZStack</b>은 기본 정렬이 가운데입니다. <code>Spacer()</code>를 위아래에 두는 방법도 씁니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Box(contentAlignment<br>&nbsp;= Alignment.Center)</div>''',
     "<b>Box</b>에 <code>contentAlignment</code> 하나만 주면 됩니다. 웹의 <code>place-items</code>와 가장 비슷합니다."),
  ]),
  plat_note="세 플랫폼 모두 코드가 짧아서 소통 문제는 거의 생기지 않습니다. 다만 <b>'가운데'가 무엇의 가운데인지</b>는 확인하세요. 화면 가운데인지, 카드 안 가운데인지, 글줄 가운데인지에 따라 코드가 완전히 달라집니다.",
  siblings=siblings("center"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>''',
)
