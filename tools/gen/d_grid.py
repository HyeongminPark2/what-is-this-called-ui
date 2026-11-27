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
  desc="그리드의 트랙과 거터, 1fr 과 auto-fit minmax, minmax(0,1fr) 함정을 실물과 해부도로 보여주는 항목.",
  lede="<b>판을 먼저 그리고 거기에 넣는</b> 방법. 플렉스가 '줄 세우기'라면 그리드는 '칸 나누기'입니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>칸이 알아서 접히기</b>로 두고 브라우저 폭을 바꿔 보세요(위의 폭 토글).
          <code>auto-fit</code> + <code>minmax</code>는 <b>미디어 쿼리 없이</b> 열 수를 줄입니다 —
          요즘 카드 그리드가 거의 다 이것입니다.<br>
          <b>긴 글 넣기</b>를 켜면 고르던 칸이 어긋납니다. <code>1fr</code>이 사실
          <code>minmax(<b>auto</b>, 1fr)</code>이라 그 칸이 글보다 작아지지 못하기 때문입니다.
          <code>minmax(0, 1fr)</code>로 고치면 그제서야 줄어듭니다.</p>
        </div>''',
  names=rows([
    ("한국어", "그리드, 격자, 레이아웃 그리드"),
    ("영어", "CSS Grid, grid layout, track, gutter"),
    ("같이 쓰는 말",
     "열과 행 하나하나를 <b>트랙</b>(track), 칸 사이의 홈을 <b>거터</b>(gutter · <code>gap</code>)라 합니다. "
     "<code>fr</code>은 <b>남은 자리의 몫</b>(fraction), <code>auto-fit</code>/<code>auto-fill</code>은 "
     "<b>열 수를 브라우저가 정하게</b> 하는 말입니다. 이름을 붙인 칸 짜임은 <b>그리드 템플릿 영역</b>입니다."),
    ("자주 잘못 부름",
     "<b>간격 그리드</b> — 여백 단위(8px 격자)와는 다른 것입니다. 이쪽은 <b>열 나누기</b>입니다.<br>"
     "<b>테이블</b> — 표는 <b>데이터</b>이고 그리드는 <b>배치</b>입니다. 표를 배치에 쓰면 스크린 리더가 '표'라고 읽습니다.<br>"
     "<b>플렉스</b> — 플렉스는 한 방향, 그리드는 두 방향. 줄끼리 맞아야 하면 그리드입니다."),
  ]),
  axes=ax("그리드"),
  oneline="그리드는 <b>판을 먼저 정하는 것</b>입니다. 자식이 몇 개든 판은 그대로라, 줄과 열이 서로 맞습니다.",
  s4_title="짜는 법", s4_hint="같은 자식, 다른 판",
  states=states([
    (gr("1fr 1fr 1fr"), "열 수 못 박기", "<code>repeat(3, 1fr)</code>. <b>항상 3열</b>"),
    (gr("repeat(auto-fit, minmax(38px, 1fr))"), "알아서 접기", "<code>auto-fit minmax</code>. <b>미디어 쿼리가 필요 없다</b>"),
    (gr("70px 1fr", 2, labels=["사이드바", "본문"]), "고정 + 유동", "한쪽만 못 박고 나머지는 <code>1fr</code>"),
    (gr("1fr 1fr 1fr", 6, extra="row-gap:14px"), "거터", "<code>gap</code>으로 열·행 사이를 따로 줄 수 있다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:7px">
                <span style="grid-column:span 2;display:grid;place-items:center;background:var(--warn-soft);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">span 2</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">3</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">4</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10.5px;font-weight:700;padding:7px 0">5</span>
              </div>''',
     "칸 합치기", "<code>grid-column: span 2</code>. 플렉스로는 못 하는 일"),
    ('''              <div style="width:100%;max-width:180px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;overflow:hidden">
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px">1</span>
                <span style="display:grid;place-items:center;background:var(--warn-soft);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px;white-space:nowrap">긴칸이옆칸을빼앗음</span>
                <span style="display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);border-radius:5px;font-size:10px;font-weight:700;padding:7px 2px">3</span>
              </div>''',
     "1fr 의 함정", "긴 칸이 <b>옆 칸 자리를 빼앗는다</b>. <code>minmax(0,1fr)</code>로 푼다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그리드 컨테이너", "grid container", "<code>display: grid</code>를 준 부모. 자식은 <b>순서대로 칸에 들어간다</b>"),
    ("트랙", "track · template", "열(과 행)의 정의. <code>1fr</code>은 <b>남은 자리를 한 몫</b>"),
    ("거터", "gap · gutter", "칸 사이의 홈. <code>column-gap</code>·<code>row-gap</code>을 따로 줄 수 있다"),
    ("알아서 접기", "auto-fit + minmax", "'최소 150px, 안 되면 열 수를 줄여라'. <b>미디어 쿼리 없이</b> 반응한다"),
    ("minmax(0, 1fr)", "minmax", "<code>1fr</code>의 숨은 최소값(auto)을 0 으로 바꾼다. <b>칸이 글보다 작아질 수 있게</b>"),
    ("칸 합치기", "grid-column: span", "한 자식이 여러 칸을 먹는다. <b>플렉스로는 못 하는 일</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>1fr</code>은 '남은 자리를 한 몫'이지만 숨은 조건이 하나 있습니다 — 사실은
          <code>minmax(<b>auto</b>, 1fr)</code>이고, <b>auto 는 '내용만큼'</b>입니다. 그래서 긴 글이 든 칸은
          줄어들기를 거부하고 <b>옆 칸의 자리를 빼앗습니다.</b> 글이 더 길면 판이 통째로 터지고
          가로 스크롤이 생깁니다. <code>minmax(0, 1fr)</code>이 그 숨은 최소값을 0 으로 바꿔 줍니다.</p>''',
  do=ul([
    "<b>줄과 열이 서로 맞아야</b> 할 때 — 카드 그리드, 표 같은 배치",
    "화면 전체의 짜임 — 사이드바 + 본문 + 꼬리말",
    "<b>미디어 쿼리 없이</b> 접히게 하고 싶을 때 — <code>auto-fit minmax</code>",
    "한 칸이 여러 칸을 먹어야 할 때",
  ]),
  dont=ul([
    "한 줄에 늘어놓기만 하면 될 때 → <a href=\"flex.html\">플렉스</a>가 짧습니다",
    "<b>데이터 표</b> → <code>&lt;table&gt;</code>을 씁니다. 그리드로 만들면 행·열이 안 읽힙니다",
    "자식 개수가 매번 달라 판이 무너질 때 — <code>auto-fit</code>으로 바꿉니다",
  ]),
  instead='한 방향이면 <a href="flex.html">플렉스</a>, 데이터면 데이터 테이블(10부), 가운데만 놓으면 <a href="center.html">가운데 맞추기</a>.',
  cases=cases([
    (gr("repeat(auto-fit, minmax(55px, 1fr))", 6, "190px"),
     "카드 그리드", "폭이 줄면 <b>저절로</b> 3열 → 2열 → 1열"),
    (gr("70px 1fr", 2, "190px", labels=["사이드바", "본문"]),
     "화면 짜임", "고정 사이드바 + 유동 본문. <b>한 줄로 끝난다</b>"),
    ('''              <div style="width:100%;max-width:190px;display:grid;grid-template-columns:auto 1fr auto;gap:7px;align-items:center;background:var(--surface);border:1px dashed var(--line-strong);border-radius:6px;padding:8px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft)"></span>
                <span style="font-size:10.5px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">제목이 길어도 가운데만 줄어듭니다</span>
                <span style="font-size:10px;color:var(--fg-muted)">›</span>
              </div>''',
     "auto 1fr auto", "앞뒤는 내용만큼, 가운데만 유동. <b>리스트 한 줄</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 판의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="외울 것은 사실상 <b>두 줄</b>입니다 — 카드 그리드 한 줄과 화면 짜임 한 줄.",
  code='''<span class="c">/* 카드 그리드 — 미디어 쿼리 없이 접힌다 */</span>
<span class="t">.cards</span> {
  <span class="a">display</span>: grid;
  <span class="a">grid-template-columns</span>: <span class="t">repeat</span>(auto-fit, <span class="t">minmax</span>(<span class="a">220px</span>, <span class="a">1fr</span>));
  <span class="a">gap</span>: <span class="a">16px</span>;
}

<span class="c">/* 화면 짜임 — 사이드바 + 본문 */</span>
<span class="t">.app</span> {
  <span class="a">display</span>: grid;
  <span class="a">grid-template-columns</span>: <span class="a">240px</span> <span class="t">minmax</span>(<span class="a">0</span>, <span class="a">1fr</span>);
}                       <span class="c">/* ↑ 0 이라야 긴 글에 본문이 터지지 않는다 */</span>

<span class="c">/* 한 칸이 두 칸을 먹기 */</span>
<span class="t">.cards</span> &gt; <span class="t">.featured</span> { <span class="a">grid-column</span>: span <span class="a">2</span>; }''',
  keys=kbd([
    ("<code>minmax(0, 1fr)</code>", "본문처럼 <b>긴 글이 들어올</b> 칸에는 거의 늘 필요하다"),
    ("<code>auto-fit</code> vs <code>auto-fill</code>", "auto-fit 은 빈 트랙을 접고, auto-fill 은 <b>빈 칸을 남긴다</b>. 보통 auto-fit"),
    ("<code>gap</code>만 쓴다", "자식 마진으로 간격을 만들면 <b>가장자리에도</b> 생긴다"),
    ("<code>auto</code> 트랙", "<code>auto 1fr auto</code>는 '앞뒤는 내용만큼, 가운데만 유동'. 리스트 한 줄의 정석"),
    ("배치에 <code>&lt;table&gt;</code>을 쓰지 않는다", "스크린 리더가 '표, 3열 5행'이라고 읽는다"),
    ("자식 순서 = 읽는 순서", "<code>grid-area</code>로 눈에 보이는 자리를 바꿔도 <b>키보드 순서는 안 바뀐다</b>"),
  ]),
  backend=rows([
    ("그리드 = 판이 먼저", "자식이 몇 개 오든 판은 그대로입니다. 그래서 <b>응답 개수가 들쭉날쭉해도</b> 레이아웃이 안 무너집니다 — 플렉스와 가장 큰 차이입니다."),
    ("빈 칸 처리", "마지막 줄이 덜 찼을 때 어떻게 보일지 정해 둬야 합니다. <code>auto-fit</code>이면 남은 칸이 늘어나고, <code>auto-fill</code>이면 빈 자리가 남습니다."),
    ("페이지 크기", "한 번에 12개를 주면 3열·4열·6열 어디서도 줄이 딱 맞습니다. <b>12의 약수</b>로 페이지 크기를 잡는 관례가 여기서 나왔습니다."),
    ("이미지 비율", "칸 크기가 바뀌어도 카드 높이가 흔들리지 않으려면 <code>aspect-ratio</code>를 못 박아야 합니다. 서버가 원본 비율을 내려주면 더 정확해집니다."),
  ]),
  plat_lede="두 방향 배치는 세 플랫폼 모두 늦게 들어왔고, 이름이 다 다릅니다.",
  plats=plats([
    ("웹", "CSS Grid",
     gr("1fr 1fr", 4, "120px", "4px"),
     "<code>display: grid</code>. <b>auto-fit minmax</b> 로 미디어 쿼리 없이 접히는 것이 큰 장점입니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyVGrid<br>GridItem(.adaptive<br>&nbsp;(minimum: 150))</div>''',
     "<b>LazyVGrid</b> 와 <code>GridItem(.adaptive)</code> 가 <code>auto-fit minmax</code> 와 같은 일을 합니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">LazyVerticalGrid<br>GridCells.Adaptive<br>&nbsp;(minSize = 150.dp)</div>''',
     "<b>LazyVerticalGrid</b> 와 <code>GridCells.Adaptive</code>. 역시 최소 크기를 주면 열 수를 알아서 정합니다."),
  ]),
  plat_note="세 쪽 다 <b>'최소 칸 너비를 주면 열 수는 알아서'</b>라는 같은 패턴을 갖고 있습니다. 그래서 시안에 \"3열\"이라고만 적지 말고 <b>\"칸 최소 220px\"</b>로 적어 주면 세 플랫폼이 그대로 구현하고 화면 크기마다 알아서 맞습니다.",
  siblings=siblings("grid"),
  related='''        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
