# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def gr(tpl, n=6, w="180px", gap="5px", labels=None, extra=""):
    cells = ""
    for i in range(n):
        t = labels[i] if labels and i < len(labels) else str(i + 1)
        cells += ('<span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);'
                  'border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;'
                  'font-size:10.5px;font-weight:700;padding:7px 4px;min-width:0;overflow:hidden">' + t + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;grid-template-columns:' + tpl +
            ';gap:' + gap + ';background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;'
            + extra + '">' + cells + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:7px;padding:9px">
                    <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:9px 0">1</span>
                    <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:9px 0">2</span>
                    <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:9px 0">3</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">grid-template-columns: 1fr 1fr 1fr</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">gap: 8px  (거터)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">repeat(auto-fit, minmax(150px, 1fr))</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">minmax(0, 1fr)  — 1fr 의 함정을 푸는 값</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">grid-column: span 2  (한 칸이 두 칸을 먹기)</div>
                </div>
              </div>'''

D = dict(
  slug="grid", ko="그리드", en="CSS Grid · grid layout",
  desc="그리드의 트랙과 거터, 1fr과 auto-fit minmax, 그리고 minmax(0,1fr)로 푸는 1fr의 함정을 실물과 해부도로 보여 주는 항목입니다.",
  lede="그리드는 <b>판을 먼저 칸으로 나누고 그 칸에 자식을 넣는</b> 방법입니다. 플렉스가 자식을 한 줄로 늘어놓는 방법이라면, 그리드는 가로와 세로로 칸을 나누는 방법입니다.",
  axes_lede="뼈대를 다루는 항목들은 눈에 보이지 않으면서 요소의 자리를 정한다는 점이 같아서 생김새로는 구별하기 어렵습니다. 대신 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>짜는 법을 <b>칸이 알아서 접히기</b>로 두고 위의 폭 토글로 화면 폭을 바꿔 보세요.
          <code>auto-fit</code>과 <code>minmax</code>를 함께 쓰면 <b>미디어 쿼리 없이도</b> 폭에 맞춰 열 수가 줄어들기 때문에,
          요즘 카드 그리드는 대부분 이 방식으로 만듭니다.<br>
          <b>긴 글 넣기</b>를 켜면 너비가 고르던 칸들이 어긋납니다. <code>1fr</code>은 사실
          <code>minmax(<b>auto</b>, 1fr)</code>이라서 긴 글이 든 칸이 글보다 좁아지지 못하기 때문입니다.
          <code>minmax(0, 1fr)</code>로 고쳐야 그 칸도 다른 칸과 같은 너비로 줄어듭니다.</p>
        </div>''',
  names=rows([
    ("한국어", "그리드, 격자, 레이아웃 그리드"),
    ("영어", "CSS Grid, grid layout, track, gutter"),
    ("같이 쓰는 말",
     "열과 행 하나하나는 <b>트랙</b>(track), 칸 사이의 빈 줄은 <b>거터</b>(gutter · <code>gap</code>)라고 부릅니다. "
     "<code>fr</code>은 <b>남은 자리의 몫</b>(fraction)을 나타내는 단위이고, <code>auto-fit</code>/<code>auto-fill</code>은 "
     "<b>열 수를 브라우저가 정하게</b> 하는 키워드입니다. 칸마다 이름을 붙여 짠 배치는 <b>그리드 템플릿 영역</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>간격 그리드</b> — 여백 단위로 쓰는 8px 격자와는 다른 것입니다. CSS 그리드는 <b>열을 나누는</b> 배치 방법입니다.<br>"
     "<b>테이블</b> — 표는 <b>데이터</b>를 담는 것이고 그리드는 <b>배치</b>를 정하는 것입니다. 배치에 표를 쓰면 스크린 리더가 그 영역을 '표'라고 읽습니다.<br>"
     "<b>플렉스</b> — 플렉스는 한 방향, 그리드는 두 방향으로 배치합니다. 위아래 줄의 칸이 서로 맞아야 하면 그리드를 씁니다."),
  ]),
  axes=ax("그리드"),
  oneline="그리드는 <b>판을 먼저 정해 두는</b> 방법입니다. 자식이 몇 개가 들어와도 판은 그대로이기 때문에 줄과 열이 서로 맞습니다.",
  s4_title="짜는 법", s4_hint="같은 자식, 다른 판",
  states=states([
    (gr("1fr 1fr 1fr"), "열 수 못 박기", "<code>repeat(3, 1fr)</code>로 적으면 화면 폭과 상관없이 <b>항상 3열</b>입니다"),
    (gr("repeat(auto-fit, minmax(38px, 1fr))"), "알아서 접기", "<code>auto-fit minmax</code>로 적으면 폭에 따라 열 수가 바뀌어서 <b>미디어 쿼리가 필요 없습니다</b>"),
    (gr("70px 1fr", 2, labels=["사이드바", "본문"]), "고정 + 유동", "한쪽 폭만 고정하고 나머지는 <code>1fr</code>로 채웁니다"),
    (gr("1fr 1fr 1fr", 6, extra="row-gap:14px"), "거터", "<code>gap</code>으로 열 사이와 행 사이 간격을 따로 줄 수 있습니다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:7px">
                <span style="grid-column:span 2;display:grid;place-items:center;background:var(--warn-soft);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">span 2</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">3</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">4</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">5</span>
              </div>''',
     "칸 합치기", "<code>grid-column: span 2</code>로 두 칸을 합칩니다. 플렉스로는 할 수 없는 일입니다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;overflow:hidden">
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px">1</span>
                <span style="display:grid;place-items:center;background:var(--warn-soft);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px;white-space:nowrap">긴칸이옆칸을빼앗음</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px">3</span>
              </div>''',
     "1fr 의 함정", "긴 글이 든 칸이 <b>옆 칸의 자리를 빼앗습니다</b>. <code>minmax(0,1fr)</code>로 고칩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그리드 컨테이너", "grid container", "<code>display: grid</code>를 준 부모입니다. 자식은 <b>마크업 순서대로 칸에 들어갑니다</b>"),
    ("트랙", "track · template", "열(과 행)의 크기를 정의합니다. <code>1fr</code>은 <b>남은 자리를 한 몫</b> 나눠 받습니다"),
    ("거터", "gap · gutter", "칸 사이의 빈 줄입니다. <code>column-gap</code>·<code>row-gap</code>으로 따로 줄 수 있습니다"),
    ("알아서 접기", "auto-fit + minmax", "칸이 최소 150px보다 좁아지면 열 수를 줄이라는 뜻입니다. <b>미디어 쿼리 없이</b> 화면 폭에 맞춰집니다"),
    ("minmax(0, 1fr)", "minmax", "<code>1fr</code>에 숨은 최소값(auto)을 0으로 바꿔서 <b>칸이 글보다 좁아질 수 있게</b> 합니다"),
    ("칸 합치기", "grid-column: span", "자식 하나가 여러 칸을 차지합니다. <b>플렉스로는 할 수 없는 일</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>1fr</code>은 남은 자리를 한 몫 나눠 받는다는 뜻이지만, 실제로는
          <code>minmax(<b>auto</b>, 1fr)</code>로 계산되고 <b>auto는 '내용만큼'</b>을 뜻합니다. 그래서 긴 글이 든 칸은
          내용보다 좁아지지 않고 <b>옆 칸의 자리를 빼앗습니다.</b> 글이 더 길면 판 전체가 부모보다 넓어져
          가로 스크롤이 생깁니다. <code>minmax(0, 1fr)</code>로 적으면 숨은 최소값이 0으로 바뀌어 이 문제가 사라집니다.</p>''',
  do=ul([
    "카드 그리드나 표 같은 배치처럼 <b>줄과 열이 서로 맞아야</b> 할 때",
    "사이드바, 본문, 꼬리말로 화면 전체를 짤 때",
    "<b>미디어 쿼리 없이</b> 열 수가 줄어들게 하고 싶을 때. <code>auto-fit minmax</code>를 씁니다",
    "자식 하나가 여러 칸을 차지해야 할 때",
  ]),
  dont=ul([
    "한 줄에 늘어놓기만 하면 될 때. <a href=\"flex.html\">플렉스</a>로 적는 편이 짧습니다",
    "<b>데이터 표</b>를 만들 때. 그리드로 만들면 스크린 리더가 행과 열을 읽지 못하니 <code>&lt;table&gt;</code>을 씁니다",
    "자식 개수가 매번 달라서 열 수를 못 박은 판이 무너질 때. <code>auto-fit</code>으로 바꿉니다",
  ]),
  instead='한 방향이면 <a href="flex.html">플렉스</a>, 데이터면 데이터 테이블(10부), 가운데만 놓으면 <a href="center.html">가운데 맞추기</a>.',
  cases=cases([
    (gr("repeat(auto-fit, minmax(55px, 1fr))", 6, "190px"),
     "카드 그리드", "폭이 줄면 <b>저절로</b> 3열에서 2열, 1열로 바뀝니다"),
    (gr("70px 1fr", 2, "190px", labels=["사이드바", "본문"]),
     "화면 짜임", "고정 폭 사이드바와 유동 폭 본문을 <b>코드 한 줄로</b> 짭니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;grid-template-columns:auto 1fr auto;gap:7px;align-items:center;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:8px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft)"></span>
                <span style="font-size:10.5px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">제목이 길어도 가운데만 줄어듭니다</span>
                <span style="font-size:10px;color:var(--fg-muted)">›</span>
              </div>''',
     "auto 1fr auto", "앞뒤 칸은 내용만큼, 가운데 칸만 남은 폭을 차지합니다. <b>리스트 한 줄</b>에 많이 씁니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="그리드를 쓸 때 지킬 것",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="외워 둘 것은 카드 그리드 한 줄과 화면 짜임 한 줄, 이렇게 <b>두 줄</b>입니다.",
  code='''<span class="c">/* 카드 그리드. 미디어 쿼리 없이 열 수가 줄어든다 */</span>
<span class="t">.cards</span> {
  <span class="a">display</span>: grid;
  <span class="a">grid-template-columns</span>: <span class="t">repeat</span>(auto-fit, <span class="t">minmax</span>(<span class="a">220px</span>, <span class="a">1fr</span>));
  <span class="a">gap</span>: <span class="a">16px</span>;
}

<span class="c">/* 사이드바와 본문으로 짠 화면 */</span>
<span class="t">.app</span> {
  <span class="a">display</span>: grid;
  <span class="a">grid-template-columns</span>: <span class="a">240px</span> <span class="t">minmax</span>(<span class="a">0</span>, <span class="a">1fr</span>);
}                       <span class="c">/* ↑ 0이어야 긴 글이 들어와도 본문이 넘치지 않는다 */</span>

<span class="c">/* 자식 하나가 두 칸을 차지하게 하기 */</span>
<span class="t">.cards</span> &gt; <span class="t">.featured</span> { <span class="a">grid-column</span>: span <span class="a">2</span>; }''',
  keys=kbd([
    ("<code>minmax(0, 1fr)</code>", "본문처럼 <b>긴 글이 들어올</b> 칸에는 거의 항상 필요합니다"),
    ("<code>auto-fit</code> vs <code>auto-fill</code>", "auto-fit은 빈 트랙을 접고 auto-fill은 <b>빈 칸을 남깁니다</b>. 보통은 auto-fit을 씁니다"),
    ("<code>gap</code>만 쓴다", "자식에 마진을 줘서 간격을 만들면 판의 <b>가장자리에도</b> 여백이 생깁니다"),
    ("<code>auto</code> 트랙", "<code>auto 1fr auto</code>는 앞뒤 칸을 내용만큼, 가운데 칸만 유동 폭으로 둡니다. 리스트 한 줄을 짤 때 흔히 씁니다"),
    ("배치에 <code>&lt;table&gt;</code>을 쓰지 않는다", "배치에 표를 쓰면 스크린 리더가 '표, 3열 5행'이라고 읽습니다"),
    ("자식 순서 = 읽는 순서", "<code>grid-area</code>로 눈에 보이는 자리를 바꿔도 <b>키보드 순서는 바뀌지 않습니다</b>"),
  ]),
  backend=rows([
    ("그리드 = 판이 먼저", "자식이 몇 개 오든 판은 그대로이기 때문에, <b>응답 개수가 들쭉날쭉해도</b> 레이아웃이 무너지지 않습니다. 이 점이 플렉스와 가장 크게 다릅니다."),
    ("빈 칸 처리", "마지막 줄이 덜 찼을 때 어떻게 보일지 정해 둬야 합니다. <code>auto-fit</code>이면 남은 칸이 늘어나고, <code>auto-fill</code>이면 빈 자리가 남습니다."),
    ("페이지 크기", "한 번에 12개를 주면 3열·4열·6열 어디서도 줄이 딱 맞습니다. <b>12의 약수</b>로 페이지 크기를 잡는 관례가 여기서 나왔습니다."),
    ("이미지 비율", "칸 너비가 바뀌어도 카드 높이가 들쭉날쭉하지 않게 하려면 이미지에 <code>aspect-ratio</code>를 정해 둬야 합니다. 서버가 원본 비율을 함께 내려 주면 더 정확하게 맞출 수 있습니다."),
  ]),
  plat_lede="두 방향 배치는 세 플랫폼 모두 나중에 들어온 기능이고, 부르는 이름이 저마다 다릅니다.",
  plats=plats([
    ("웹", "CSS Grid",
     gr("1fr 1fr", 4, "120px", "4px"),
     "<code>display: grid</code>로 켭니다. <b>auto-fit minmax</b>로 미디어 쿼리 없이 열 수를 줄일 수 있다는 것이 큰 장점입니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyVGrid<br>GridItem(.adaptive<br>&nbsp;(minimum: 150))</div>''',
     "<b>LazyVGrid</b>와 <code>GridItem(.adaptive)</code>가 <code>auto-fit minmax</code>와 같은 일을 합니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyVerticalGrid<br>GridCells.Adaptive<br>&nbsp;(minSize = 150.dp)</div>''',
     "<b>LazyVerticalGrid</b>와 <code>GridCells.Adaptive</code>를 씁니다. 여기서도 칸의 최소 크기를 주면 열 수를 알아서 정합니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>칸의 최소 너비만 주면 열 수는 알아서 정하는</b> 방식을 지원합니다. 그래서 시안에 \"3열\"이라고만 적지 말고 <b>\"칸 최소 220px\"</b>처럼 적어 주면, 세 플랫폼 모두 그대로 구현할 수 있고 화면 크기마다 열 수가 알맞게 바뀝니다.",
  siblings=siblings("grid"),
  related='''        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
