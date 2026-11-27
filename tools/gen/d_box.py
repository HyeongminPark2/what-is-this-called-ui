# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(w=86, p=10, b=3, m=8, label="내용", mb="color-mix(in srgb,var(--warn) 22%,transparent)"):
    return ('              <div style="display:inline-block;background:%s;padding:%dpx">'
            '<div style="width:%dpx;box-sizing:border-box;border:%dpx solid color-mix(in srgb,var(--accent) 55%%,transparent);'
            'padding:%dpx;background:color-mix(in srgb,#1f8a4c 16%%,transparent)">'
            '<div style="background:var(--surface);border:1px dashed var(--line-strong);font-size:10.5px;'
            'text-align:center;padding:5px 0">%s</div></div></div>') % (mb, m, w, b, p, label)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px;justify-items:start">
                  <div class="pin-out" data-pin="1" style="display:inline-block;background:color-mix(in srgb,var(--warn) 22%,transparent);padding:12px">
                    <div class="pin-out" data-pin="2" style="width:150px;box-sizing:border-box;border:4px solid color-mix(in srgb,var(--accent) 55%,transparent)">
                      <div class="pin-out" data-pin="3" style="padding:12px;background:color-mix(in srgb,#1f8a4c 16%,transparent)">
                        <div class="pin-out" data-pin="4" style="background:var(--surface);border:1px dashed var(--line-strong);font-size:11px;text-align:center;padding:7px 0">내용</div>
                      </div>
                    </div>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">box-sizing: border-box</div>
                </div>
              </div>'''

D = dict(
  slug="box", ko="박스 모델", en="Box model",
  desc="상자 하나를 이루는 네 겹(내용·패딩·테두리·마진)과 box-sizing 의 차이를 실물과 해부도로 보여주는 항목.",
  lede="화면의 모든 것은 <b>네 겹짜리 상자</b>입니다 — 내용 · 안쪽 여백 · 테두리 · 바깥 여백. 레이아웃이 어긋나는 거의 모든 일이 여기서 시작합니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 움직이며 네 겹이 어떻게 자라는지 보세요. 아래 줄에 <b>적은 값</b>과
          <b>실제로 차지하는 자리</b>가 같이 나옵니다.<br>
          <code>box-sizing</code>을 꺼 보면 <b><code>width: 200px</code>이라고 적었는데 상자가 240px</b>이 됩니다 —
          기본값에서 width 는 '내용만'의 너비이기 때문입니다. 거의 모든 프로젝트가
          맨 위에 <code>* { box-sizing: border-box }</code> 한 줄을 까는 이유입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "박스 모델, 상자 모델"),
    ("영어", "box model, content box, border box"),
    ("같이 쓰는 말",
     "안쪽 여백은 <b>패딩</b>(padding), 바깥 여백은 <b>마진</b>(margin), "
     "테두리는 <b>보더</b>(border), 글과 그림이 들어가는 칸은 <b>콘텐츠 박스</b>(content box)입니다. "
     "width 가 어디까지를 뜻하는지 정하는 속성이 <b><code>box-sizing</code></b>이고, "
     "위아래 마진이 하나로 합쳐지는 현상을 <b>마진 겹침</b>(margin collapsing)이라 합니다."),
    ("자주 잘못 부름",
     "<b>패딩과 마진</b> — 둘 다 '여백'이라 섞어 부르기 쉽지만, <b>테두리 안인지 밖인지</b>가 다릅니다. "
     "배경색이 칠해지면 패딩, 안 칠해지면 마진입니다.<br>"
     "<b>width</b> — 적은 값이 곧 상자 너비라고 생각하기 쉬운데, <code>box-sizing</code>에 따라 달라집니다.<br>"
     "<b>여백</b> — 디자인에서 말하는 여백(white space)은 더 넓은 뜻입니다."),
  ]),
  axes=ax("박스 모델"),
  oneline="박스 모델은 <b>'적은 값이 무엇의 크기인가'</b>를 묻는 것입니다. 그 답이 <code>box-sizing</code> 한 줄로 바뀝니다.",
  s4_title="겹", s4_hint="네 겹이 각각 다르게 자란다",
  states=states([
    (box(86, 0, 0, 0, "내용", "transparent"), "내용만", "글과 그림이 들어가는 칸"),
    (box(86, 10, 0, 0, "내용", "transparent"), "+ 패딩", "<b>테두리 안쪽</b> 여백. 배경색이 여기까지 칠해진다"),
    (box(86, 10, 3, 0, "내용", "transparent"), "+ 테두리", "선. <b>두께가 자리를 먹는다</b>"),
    (box(86, 10, 3, 8), "+ 마진", "<b>테두리 바깥</b> 여백. 배경색이 안 칠해진다"),
    ('''              <div style="display:grid;gap:6px;justify-items:center">
                <div style="display:inline-block;background:color-mix(in srgb,var(--warn) 22%,transparent);padding:0 8px">
                  <div style="width:86px;box-sizing:content-box;border:3px solid color-mix(in srgb,var(--accent) 55%,transparent);padding:10px;background:color-mix(in srgb,#1f8a4c 16%,transparent)">
                    <div style="background:var(--surface);border:1px dashed var(--line-strong);font-size:10.5px;text-align:center;padding:5px 0">86px?</div></div></div>
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--danger)">실제 112px</span>
              </div>''',
     "content-box", "기본값. width 는 <b>내용만</b>이라 패딩·테두리가 밖으로 더 붙는다"),
    ('''              <div style="display:grid;gap:6px;justify-items:center">
                <div style="display:inline-block;background:color-mix(in srgb,var(--warn) 22%,transparent);padding:0 8px">
                  <div style="width:86px;box-sizing:border-box;border:3px solid color-mix(in srgb,var(--accent) 55%,transparent);padding:10px;background:color-mix(in srgb,#1f8a4c 16%,transparent)">
                    <div style="background:var(--surface);border:1px dashed var(--line-strong);font-size:10.5px;text-align:center;padding:5px 0">86px</div></div></div>
                <span style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c">실제 86px</span>
              </div>''',
     "border-box", "<b>테두리까지</b>가 width. 거의 모든 프로젝트가 이것으로 깔아 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("마진", "margin", "<b>테두리 바깥</b>. 배경색이 안 칠해지고, 상자 크기에도 안 들어간다"),
    ("테두리", "border", "선. 투명해도 <b>두께만큼 자리를 먹는다</b>"),
    ("패딩", "padding", "<b>테두리 안쪽</b>. 배경색이 여기까지 칠해져서 누를 수 있는 범위도 여기까지다"),
    ("내용", "content", "글·그림이 들어가는 칸. <code>width</code>가 기본으로 가리키는 것이 바로 이것"),
    ("box-sizing", "box-sizing", "<code>width</code>가 <b>내용까지냐 테두리까지냐</b>를 정한다. 한 줄로 모든 계산이 바뀐다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>마진 겹침</b>이라는 함정이 하나 더 있습니다. 위아래로 맞닿은 두 상자의 마진은
          더해지지 않고 <b>큰 쪽 하나로 합쳐집니다</b>(24 + 16 = 24). 가로에서는 안 일어나고,
          플렉스·그리드 안에서도 안 일어납니다. '왜 간격이 생각보다 좁지'의 절반이 이것이고,
          그래서 요즘은 마진 대신 <b><code>gap</code></b>을 먼저 씁니다 — gap 은 겹치지 않습니다.</p>''',
  do=ul([
    "<b>모든 화면</b> — 피할 수 없습니다. 이것부터 알아야 나머지가 설명됩니다",
    "간격이 생각과 다를 때 <b>제일 먼저 의심할 곳</b>",
    "누를 수 있는 범위를 키우고 싶을 때 — 마진이 아니라 <b>패딩</b>을 키웁니다",
  ]),
  dont=ul([
    "<b>마진으로 간격을 만드는 것</b> — 겹침이 생깁니다. <code>gap</code>을 먼저 씁니다",
    "<code>width</code>와 <code>padding</code>을 둘 다 못 박는 것 — 계산이 어긋나기 시작합니다",
    "<code>box-sizing</code>을 요소마다 다르게 쓰는 것 — 한 번 깔고 끝냅니다",
  ]),
  instead='간격 값 자체는 <a href="../items/spacing.html">간격 체계</a>가 정하고, 넘친 내용은 <a href="overflow.html">넘침</a>이 맡습니다.',
  cases=cases([
    ('''              <div style="display:inline-block;background:var(--accent);color:#fff;border-radius:7px;padding:10px 18px;font-size:12px;font-weight:700">버튼</div>
              <div style="font-size:10.5px;color:var(--fg-muted);margin-top:7px;font-family:var(--mono)">padding: 10px 18px</div>''',
     "버튼 크기", "버튼은 <b>높이를 못 박지 않습니다.</b> 패딩이 크기를 만듭니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:8px;padding:11px;background:var(--surface);box-sizing:border-box">
                <span style="font-size:11.5px;font-weight:700;display:block">카드</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">width: 100% 가 테두리까지</span>
              </div>''',
     "100% 와 패딩", "border-box 라야 <code>width:100%</code>에 패딩을 더해도 안 터진다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:5px">
                <div style="background:var(--accent-soft);height:22px;border-radius:5px"></div>
                <div style="background:var(--accent-soft);height:22px;border-radius:5px"></div>
                <span style="font-size:10px;color:var(--fg-muted);font-family:var(--mono)">gap: 5px — 겹치지 않는다</span>
              </div>''',
     "gap 으로 바꾸기", "마진 겹침을 아예 안 만나는 방법"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 상자의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="프로젝트 맨 위의 <b>세 줄</b>이 거의 모든 계산을 정상으로 만듭니다.",
  code='''<span class="c">/* 거의 모든 프로젝트의 첫 줄 */</span>
<span class="t">*</span>, <span class="t">*</span>::<span class="t">before</span>, <span class="t">*</span>::<span class="t">after</span> { <span class="a">box-sizing</span>: border-box; }

<span class="t">.card</span> {
  <span class="a">width</span>: <span class="a">100%</span>;        <span class="c">/* border-box 라 패딩을 더해도 안 터진다 */</span>
  <span class="a">padding</span>: <span class="a">16px</span>;
  <span class="a">border</span>: <span class="a">1px</span> solid <span class="t">var</span>(<span class="a">--line</span>);
}

<span class="c">/* 마진 대신 gap — 겹침이 아예 안 생긴다 */</span>
<span class="t">.list</span> { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">16px</span>; }

<span class="c">/* 누를 자리를 키울 때는 마진이 아니라 패딩 */</span>
<span class="t">.icon-btn</span> { <span class="a">padding</span>: <span class="a">10px</span>; }   <span class="c">/* 아이콘 20px + 패딩 = 40px 터치 영역 */</span>''',
  keys=kbd([
    ("<code>border-box</code>를 깐다", "맨 위에 한 번. <b>요소마다 다르게 두지 않는다</b>"),
    ("마진 대신 <code>gap</code>", "마진은 위아래가 <b>합쳐진다</b>(겹침). gap 은 안 합쳐진다"),
    ("누를 자리는 패딩으로", "마진으로 떼면 <b>안 눌리는 빈 공간</b>이 생긴다"),
    ("테두리는 투명해도 자리를 먹는다", "호버에만 테두리를 주면 <b>1px 씩 덜컥거린다</b>. 미리 투명 테두리를 둔다"),
    ("<code>width</code>와 <code>padding</code>을 같이 못 박지 않는다", "둘 중 하나는 자동으로 두는 편이 안전하다"),
  ]),
  backend=rows([
    ("박스 모델 = 데이터의 포장", "값 자체(내용)와 포장(패딩·테두리)을 나눠 생각하는 것과 같습니다. API 응답의 <code>data</code>와 <code>meta</code>를 나누는 것처럼, <b>어디까지가 내용인지</b>를 정하는 일입니다."),
    ("글 길이가 크기를 정한다", "상자 높이는 보통 <b>내용이 정합니다.</b> 그래서 데이터가 길어지면 레이아웃이 바뀝니다 — <b>가장 긴 값</b>으로 한 번 그려 보는 것이 테스트입니다."),
    ("이미지 크기를 미리 알려 준다", "<code>width</code>·<code>height</code> 속성이 없으면 사진이 올 때 상자가 갑자기 커져 <b>화면이 덜컥거립니다</b>. 서버가 크기를 같이 내려주면 미리 자리를 잡을 수 있습니다."),
    ("메일 HTML", "메일 클라이언트는 <code>box-sizing</code>을 무시하는 곳이 많습니다. 그래서 메일 템플릿은 여전히 <code>&lt;table&gt;</code>로 짭니다."),
  ]),
  plat_lede="박스 모델은 웹의 개념이고, 두 OS 는 비슷하지만 다른 말을 씁니다.",
  plats=plats([
    ("웹", "CSS box model",
     box(70, 8, 3, 6),
     "<b>네 겹</b>이 또렷하게 나뉘고 <code>box-sizing</code>으로 width 의 뜻이 바뀝니다."),
    ("iOS", "Apple HIG · SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.padding(16)<br>.frame(width:)<br>.border( )</div>''',
     "<code>.padding()</code>이 패딩, <code>.frame()</code>이 크기입니다. <b>마진이라는 개념이 없고</b> 바깥 여백도 패딩이나 간격으로 줍니다."),
    ("안드로이드", "Compose · View",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Modifier<br>&nbsp;.padding(16.dp)<br>&nbsp;.size(200.dp)</div>''',
     "예전 View 에는 padding 과 margin 이 다 있었지만, Compose 는 <b>순서가 있는 <code>Modifier</code></b>로 바뀌었습니다 — 패딩을 테두리 앞에 쓰냐 뒤에 쓰냐로 결과가 달라집니다."),
  ]),
  plat_note="iOS·Compose 에는 <b>마진이 없습니다.</b> 그래서 \"마진 16 주세요\"가 앱 쪽에서는 '부모의 패딩'이나 '간격(spacing)'으로 번역돼야 합니다. 시안의 바깥 여백이 <b>누구의 것인지</b>(이 상자의 바깥인지, 부모의 안쪽인지)를 분명히 해 두면 그대로 옮겨집니다.",
  siblings=siblings("box"),
  related='''        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
