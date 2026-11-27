# -*- coding: utf-8 -*-
from ax1 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def pair(gap_px, label, w="152px", note="", ok=None, wrap=""):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    bx = ('<span style="display:block;background:var(--accent-soft);border:1px solid var(--accent);'
          'border-radius:4px;padding:4px 6px;font-size:8.5px">')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);' + wrap + '">'
            + bx + '위 상자</span>'
            '<span style="display:block;height:' + str(gap_px) + 'px;background:repeating-linear-gradient(45deg,'
            'color-mix(in srgb, var(--accent) 18%, transparent) 0 4px, transparent 4px 8px);'
            'font-family:var(--mono);font-size:7.5px;color:var(--accent);display:grid;place-items:center">' + label + '</span>'
            + bx + '아래 상자</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">위 24와 아래 16이 만나면 40이 아닌 24</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">세로만 겹치고 가로는 더해짐</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">flex·grid 안에서는 겹치지 않음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">부모에 padding·테두리가 생기면 멈춤</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">첫 자식의 margin이 부모 밖으로 빠지기도 함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">gap을 쓰면 적은 값이 그대로 나옴</div>
                </div>
              </div>'''

D = dict(
  slug="margincollapse", ko="여백 붕괴", en="Margin collapse",
  desc="맞닿은 세로 여백이 겹쳐 큰 쪽만 남는 규칙을 다루는 항목입니다. 두 여백을 더한 값이 왜 나오지 않는지, gap이 왜 더 나은지 보여 줍니다.",
  lede="맞닿은 세로 여백은 <b>더해지지 않고 겹칩니다</b>. 그래서 24px과 16px이 맞닿으면 간격은 40px이 아니라 큰 쪽인 <b>24px</b>이 됩니다.",
  axes_lede="뼈대는 눈에 보이지 않지만 <b>모든 배치</b>를 정합니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>여백을 주는 방법을 바꿔 가며 <b>실제 간격을 잰 값</b>을 보세요. 두 값을 더하면 40px이지만
          <code>margin</code>으로 붙이면 <b>24px</b>로 나옵니다.<br>
          <b>flex</b> 안에서는 여백이 겹치지 않아 40px이 그대로 나오고, 부모에 <b>padding</b>이 생겨도
          붕괴가 멈춥니다. 코드를 건드리지 않은 것 같은데 간격이 바뀌는 일은 흔히 이 때문에 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "여백 붕괴, 마진 겹침, 마진 상쇄"),
    ("영어", "margin collapsing, collapsing margins"),
    ("같이 쓰는 말",
     "맞닿은 두 형제 사이에서 여백이 겹치는 것은 <b>인접 형제 붕괴</b>, "
     "첫 자식의 <code>margin-top</code>이 부모 밖으로 빠져나가는 것은 <b>부모-자식 붕괴</b>라고 부릅니다. "
     "붕괴가 멈추는 상태는 <b>새 블록 서식 문맥</b>(BFC)이 생겼다고 말하는데, "
     "<code>overflow: hidden</code>이나 <code>display: flow-root</code>를 주면 새 블록 서식 문맥이 생깁니다."),
    ("자주 잘못 부르는 이름",
     "<b>간격 체계</b> — <a href=\"../items/spacing.html\">간격 체계</a>는 간격을 <b>얼마로 할지</b> 정하는 규칙이고, 여백 붕괴는 여백이 <b>어떻게 계산되는지</b>에 관한 규칙입니다.<br>"
     "<b>패딩</b> — <a href=\"../items/box.html\">패딩</a>은 안쪽 여백이라서 <b>겹치지 않습니다</b>.<br>"
     "<b>gap</b> — <code>gap</code>은 마진과 다른 방식으로 간격을 만들기 때문에 겹치지 않습니다."),
  ]),
  axes=ax("여백 붕괴"),
  oneline="<b>간격은 <code>gap</code>으로 주세요.</b> 그러면 적은 값이 그대로 나오고, 첫 요소와 마지막 요소를 따로 처리할 필요도 없습니다.",
  s4_title="여백이 겹치는 경우와 겹치지 않는 경우", s4_hint="적은 값이 그대로 나오는지 비교",
  do_title="여백 붕괴를 피해 간격을 주는 방법",
  dont_title="여백을 줄 때 피할 것",
  instead_title="여백 붕괴와 함께 보면 좋은 항목",
  states=states([
    (pair(24, "24px", "152px", "24와 16을 더한 40이 아님", False), "margin끼리 맞닿을 때", "두 여백 가운데 <b>큰 쪽만</b> 남습니다"),
    (pair(40, "40px", "152px", "적은 값이 그대로 나옴", True, "display:flex;flex-direction:column;"),
     "flex 안에 있을 때", "flex 안에서는 여백이 <b>겹치지 않습니다</b>"),
    (pair(40, "40px", "152px", "grid 안에서도 겹치지 않음", True, "display:grid;"),
     "grid 안에 있을 때", "flex와 마찬가지로 겹치지 않습니다"),
    (pair(40, "40px", "152px", "부모에 padding이 생기면 멈춤", None, "padding:1px;"),
     "부모에 padding이 생겼을 때", "부모에 padding이 생기면 붕괴가 멈춰서 <b>예고 없이</b> 간격이 바뀝니다"),
    (pair(16, "16px", "152px", "gap: 16px가 그대로 나옴", True, "display:flex;flex-direction:column;gap:16px;"),
     "gap으로 간격을 줄 때", "gap으로 간격을 주면 <b>겹칠 일이 없습니다</b>"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px">
                <div style="border:1px solid var(--danger);border-radius:6px;background:var(--surface);margin-top:14px;position:relative">
                  <span style="position:absolute;left:0;right:0;top:-14px;height:14px;background:repeating-linear-gradient(45deg,color-mix(in srgb, var(--danger) 18%, transparent) 0 4px,transparent 4px 8px)"></span>
                  <span style="display:block;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px;padding:4px 6px;font-size:8.5px">첫 자식</span>
                </div>
                <span style="font-size:8.5px;color:var(--fg-muted)">자식의 margin이 부모 밖으로 빠짐</span>
              </div>''',
     "첫 자식의 여백이 부모 밖으로 빠질 때", "첫 자식의 여백이 부모 밖으로 빠져나가 <b>부모 전체를</b> 밀어냅니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("형제끼리", "큰 쪽만 남음", "24px과 16px이 맞닿으면 <b>24px</b>만 남습니다"),
    ("세로 방향", "가로는 더해짐", "좌우 여백은 <b>겹치지 않습니다</b>"),
    ("flex · grid", "겹치지 않음", "여백이 겹치지 않기 때문에 <code>gap</code>으로 준 간격은 <b>예측할 수 있습니다</b>"),
    ("멈추는 조건", "padding · 테두리", "padding이나 테두리가 생기면 붕괴가 <b>그 자리에서</b> 멈춥니다"),
    ("부모-자식", "밖으로 빠짐", "첫 자식의 여백이 <b>부모를 밀어냅니다</b>"),
    ("해결 방법", "gap", "적은 값이 <b>그대로</b> 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          여백 붕괴는 <b>'건드리지도 않았는데 간격이 바뀌었다'</b>는 문제의 흔한 원인입니다.
          부모에 <code>padding</code>이나 테두리를 <b>1px</b>만 더해도
          붕괴가 멈춰서 간격이 갑자기 늘어납니다.
          반대로 패딩을 지우면 자식 여백이 <b>부모 밖으로 빠져나가면서</b>
          엉뚱한 자리가 벌어집니다.
          원인과 결과가 멀리 떨어져 있어 찾기 어렵지만,
          <b>간격을 <code>gap</code>으로 주는 습관</b>을 들이면 이런 문제가 아예 생기지 않습니다.</p>''',
  do=ul([
    "요소 사이 간격을 줄 때. <b><code>gap</code>으로</b> 줍니다",
    "꼭 margin을 써야 할 때. <b>한 방향만</b>(아래쪽만) 씁니다",
    "붕괴를 막고 싶을 때. <code>display: flow-root</code>를 씁니다",
  ]),
  dont=ul([
    "위아래 margin을 <b>둘 다</b> 줄 때. 여백이 겹쳐서 계산이 어긋납니다",
    "간격을 맞추려고 <code>padding</code>을 1px 더할 때. 붕괴가 멈춰서 <b>옆 간격까지</b> 바뀝니다",
    "<code>overflow: hidden</code>으로 붕괴를 막을 때. <b>그림자와 툴팁이 잘립니다</b>",
    "margin과 gap을 섞어 간격을 줄 때. 섞으면 간격을 추적하기 어려우니, margin은 <b>가운데 맞추기</b>에만 쓰고 나머지는 gap으로 줍니다",
  ]),
  instead='간격을 얼마로 할지는 <a href="../items/spacing.html">간격 체계</a>에서, 안쪽 여백인 패딩은 <a href="../items/box.html">박스 모델</a>에서 다룹니다. 요소를 한 줄로 세우면서 gap으로 띄우는 방법은 <a href="../items/flex.html">플렉스</a>에서 봅니다.',
  cases=cases([
    (pair(16, "gap: 16px", "150px", "목록 사이", True, "display:flex;flex-direction:column;gap:16px;"),
     "목록 항목 사이를 gap으로 띄우기", "첫 항목과 마지막 항목을 <b>따로 처리할 필요가 없습니다</b>"),
    (pair(24, "margin-bottom만", "150px", "한 방향만 써서 덜 헷갈림"),
     "글 사이 여백은 아래쪽만 주기", "글 사이 여백은 <b>아래쪽만</b> 줍니다"),
    (code(['.box {', '  display: flow-root;', '}'], "150px", "붕괴만 막고 잘리지 않음", True),
     "flow-root로 붕괴만 막기", "붕괴만 막고 내용을 자르지 않아서 <code>overflow:hidden</code>보다 낫습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="여백을 줄 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="<code>gap</code>을 기본으로 두고, 꼭 필요할 때만 <code>flow-root</code>로 막습니다.",
  code='''<span class="c">/* 대부분 이쪽. 겹칠 일이 없다 */</span>
.stack { <span class="a">display</span>: flex; <span class="a">flex-direction</span>: column; <span class="a">gap</span>: <span class="a">var</span>(--space-4); }

<span class="c">/* margin을 쓴다면 한 방향만 */</span>
.prose &gt; * + * { <span class="a">margin-top</span>: <span class="a">var</span>(--space-4); }

<span class="c">/* 붕괴만 막는다. overflow:hidden과 달리 잘리지 않는다 */</span>
.card { <span class="a">display</span>: flow-root; }

<span class="c">/* ✕ 이렇게 하면 계산이 어긋난다 */</span>
.a { <span class="a">margin-bottom</span>: <span class="a">24px</span>; }
.b { <span class="a">margin-top</span>: <span class="a">16px</span>; }    <span class="c">/* 합 40 이 아니라 24 */</span>''',
  keys=kbd([
    ("세로 여백만 겹친다는 점 기억하기", "좌우 여백은 <b>그대로 더해집니다</b>"),
    ("붕괴는 <code>display: flow-root</code>로 막기", "붕괴만 막습니다. 반면 <code>overflow:hidden</code>은 <b>그림자와 툴팁까지</b> 자릅니다"),
    ("<code>gap</code>은 flex·grid 안에서만 쓰기", "일반 블록 흐름에는 아직 적용되지 않습니다"),
    ("<code>* + *</code>로 한 방향 여백 주기", "첫 요소만 빼고 여백을 붙입니다. <b>한 방향 규칙</b>을 적용하는 흔한 방법입니다"),
    ("빈 요소의 여백도 겹친다는 점 기억하기", "내용이 없는 상자는 <b>자기 위아래 여백끼리</b>도 겹칩니다"),
    ("개발자 도구로 실제 여백 확인하기", "개발자 도구에서 요소를 선택하면 <b>실제 여백</b>이 주황색으로 표시됩니다"),
  ]),
  backend=rows([
    ("CSS 안에서만 계산되는 규칙", "여백 붕괴는 모두 CSS 안에서 계산됩니다. 다만 데이터가 없어 <b>내용이 비었을 때</b> 간격이 달라져서 화면이 어색해지는 일이 있습니다."),
    ("목록이 비었을 때", "목록에 줄이 하나도 없으면 여백만 남아 <b>이상한 빈칸</b>이 생기므로 <a href=\"emptytext.html\">빈 상태 문구</a>를 둡니다."),
  ]),
  plat_lede="여백 붕괴는 <b>웹에만 있는 규칙</b>입니다.",
  plats=plats([
    ("웹", "margin collapsing",
     pair(24, "24px", "110px", "", False),
     "CSS 초기부터 있던 규칙입니다. <b>글 문서</b>를 위해 만든 규칙이라서 UI에서는 자주 방해가 됩니다."),
    ("iOS", "여백 붕괴 없음",
     '''              <div class="phone" role="img" aria-label="iOS 간격 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:10px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<code>VStack(spacing:)</code>으로 <b>사이 간격</b>을 직접 주기 때문에 겹칠 일이 없습니다."),
    ("안드로이드", "여백 붕괴 없음",
     '''              <div class="phone" role="img" aria-label="안드로이드 간격 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:10px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:10px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<code>Arrangement.spacedBy()</code>로 같은 일을 하며, 여기서도 <b>여백이 겹치지 않습니다</b>."),
  ]),
  plat_note="앱을 만들다 웹으로 온 사람들이 가장 먼저 당황하는 규칙입니다. CSS에 <b>적은 값이 그대로 나오지 않기</b> 때문입니다. 다행히 요즘은 <code>gap</code>이 널리 쓰여서 이 규칙과 마주칠 일이 줄었습니다. <b>간격은 gap으로 준다</b>는 것을 팀 규칙으로 적어 두면 여백 붕괴는 알고만 있으면 되는 지식이 됩니다.",
  siblings=siblings("margincollapse"),
  related='''        <li><a href="../items/box.html"><b>박스 모델</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="autolayout.html"><b>오토 레이아웃</b><em>15부</em></a></li>''',
)
