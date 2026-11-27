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
  desc="상자 하나를 이루는 네 겹(내용·패딩·테두리·마진)과 box-sizing에 따른 차이를 실물과 해부도로 보여 주는 항목입니다.",
  lede="화면에 놓이는 요소는 모두 내용, 안쪽 여백, 테두리, 바깥 여백으로 이루어진 <b>네 겹짜리 상자</b>입니다. 레이아웃이 어긋나는 일은 대부분 이 네 겹을 잘못 셈하는 데서 시작합니다.",
  axes_lede="뼈대를 다루는 항목들은 눈에 보이지 않으면서 요소의 자리를 정한다는 점이 같아서 생김새로는 구별하기 어렵습니다. 대신 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 움직여 네 겹의 크기가 어떻게 바뀌는지 보세요. 아래 줄에는 CSS에 <b>적은 값</b>과
          상자가 <b>실제로 차지하는 자리</b>가 함께 나옵니다.<br>
          <code>box-sizing</code>을 끄면 <b><code>width: 200px</code>이라고 적었는데도 상자가 240px</b>로 커집니다.
          기본값에서 width는 내용 칸만의 너비라서 패딩과 테두리가 그 바깥에 더해지기 때문입니다. 대부분의 프로젝트가
          스타일시트 맨 위에 <code>* { box-sizing: border-box }</code> 한 줄을 넣어 두는 것도 이 계산을 피하려는 것입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "박스 모델, 상자 모델"),
    ("영어", "box model, content box, border box"),
    ("같이 쓰는 말",
     "안쪽 여백은 <b>패딩</b>(padding), 바깥 여백은 <b>마진</b>(margin), "
     "테두리는 <b>보더</b>(border), 글과 그림이 들어가는 칸은 <b>콘텐츠 박스</b>(content box)입니다. "
     "width가 어디까지의 너비를 뜻하는지 정하는 속성은 <b><code>box-sizing</code></b>이고, "
     "위아래 마진이 하나로 합쳐지는 현상은 <b>마진 겹침</b>(margin collapsing)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>패딩과 마진</b> — 둘 다 '여백'이라서 섞어 부르기 쉽지만, 패딩은 <b>테두리 안쪽</b>, 마진은 <b>테두리 바깥쪽</b> 여백입니다. "
     "배경색이 칠해지는 여백이면 패딩이고, 칠해지지 않으면 마진입니다.<br>"
     "<b>width</b> — width에 적은 값이 곧 상자 너비라고 생각하기 쉽지만, 실제 너비는 <code>box-sizing</code> 값에 따라 달라집니다.<br>"
     "<b>여백</b> — 디자인에서 말하는 여백(white space)은 패딩·마진보다 넓은 뜻으로 씁니다."),
  ]),
  axes=ax("박스 모델"),
  oneline="박스 모델에서 따질 것은 <b>CSS에 적은 값이 어느 겹까지의 크기인가</b>입니다. 그 답은 <code>box-sizing</code> 한 줄에 따라 달라집니다.",
  s4_title="상자를 이루는 네 겹", s4_hint="겹을 하나씩 더할 때마다 커지는 크기",
  do_title="박스 모델을 따져 봐야 하는 경우",
  dont_title="박스 모델을 다룰 때 피할 것",
  instead_title="박스 모델과 함께 보면 좋은 항목",
  states=states([
    (box(86, 0, 0, 0, "내용", "transparent"), "내용 칸만 있을 때", "글과 그림이 들어가는 칸입니다"),
    (box(86, 10, 0, 0, "내용", "transparent"), "패딩을 더했을 때", "<b>테두리 안쪽</b> 여백이라서 배경색이 여기까지 칠해집니다"),
    (box(86, 10, 3, 0, "내용", "transparent"), "테두리를 더했을 때", "상자를 두르는 선이며, <b>선 두께만큼 자리를 차지합니다</b>"),
    (box(86, 10, 3, 8), "마진까지 더했을 때", "<b>테두리 바깥</b> 여백이라서 배경색이 칠해지지 않습니다"),
    ('''              <div style="display:grid;gap:6px;justify-items:center">
                <div style="display:inline-block;background:color-mix(in srgb,var(--warn) 22%,transparent);padding:0 8px">
                  <div style="width:86px;box-sizing:content-box;border:3px solid color-mix(in srgb,var(--accent) 55%,transparent);padding:10px;background:color-mix(in srgb,#1f8a4c 16%,transparent)">
                    <div style="background:var(--surface);border:1px dashed var(--line-strong);font-size:10.5px;text-align:center;padding:5px 0">86px?</div></div></div>
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--danger)">실제 112px</span>
              </div>''',
     "<code>content-box</code>일 때", "기본값입니다. width가 <b>내용 칸만</b>의 너비라서 패딩과 테두리가 그 바깥에 더해집니다"),
    ('''              <div style="display:grid;gap:6px;justify-items:center">
                <div style="display:inline-block;background:color-mix(in srgb,var(--warn) 22%,transparent);padding:0 8px">
                  <div style="width:86px;box-sizing:border-box;border:3px solid color-mix(in srgb,var(--accent) 55%,transparent);padding:10px;background:color-mix(in srgb,#1f8a4c 16%,transparent)">
                    <div style="background:var(--surface);border:1px dashed var(--line-strong);font-size:10.5px;text-align:center;padding:5px 0">86px</div></div></div>
                <span style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c">실제 86px</span>
              </div>''',
     "<code>border-box</code>일 때", "width가 <b>테두리까지</b>의 너비입니다. 대부분의 프로젝트가 이 값을 기본으로 깔아 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("마진", "margin", "<b>테두리 바깥</b> 여백입니다. 배경색이 칠해지지 않고, 상자 크기에도 들어가지 않습니다"),
    ("테두리", "border", "상자를 두르는 선입니다. 투명하게 칠해도 <b>두께만큼 자리를 차지합니다</b>"),
    ("패딩", "padding", "<b>테두리 안쪽</b> 여백입니다. 배경색이 여기까지 칠해지고, 누를 수 있는 범위도 여기까지입니다"),
    ("내용", "content", "글과 그림이 들어가는 칸입니다. 기본값에서는 <code>width</code>가 이 칸의 너비를 가리킵니다"),
    ("box-sizing", "box-sizing", "<code>width</code>가 <b>내용 칸까지의 너비인지, 테두리까지의 너비인지</b>를 정합니다. 이 값에 따라 상자 크기 계산이 모두 달라집니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          박스 모델에는 <b>마진 겹침</b>이라는 현상도 있습니다. 위아래로 맞닿은 두 상자의 마진은 서로
          더해지지 않고 <b>큰 쪽 하나로 합쳐지기</b> 때문에, 24px과 16px이 맞닿으면 간격은 40px이 아니라 24px이 됩니다.
          이 현상은 가로 방향에서는 일어나지 않고, 플렉스나 그리드 안에서도 일어나지 않습니다. 간격이 생각보다 좁게 나올 때
          원인이 마진 겹침인 경우가 많아서, 요즘은 마진 대신 겹치지 않는 <b><code>gap</code></b>을 먼저 씁니다.</p>''',
  do=ul([
    "<b>모든 화면</b>을 만들 때. 어떤 요소든 박스 모델을 따르기 때문에, 이것부터 알아야 나머지 레이아웃이 설명됩니다",
    "간격이 생각과 다를 때. 박스 모델은 <b>가장 먼저 확인할 곳</b>입니다",
    "누를 수 있는 범위를 키우고 싶을 때. 마진이 아니라 <b>패딩</b>을 키워야 누르는 범위가 넓어집니다",
  ]),
  dont=ul([
    "<b>마진으로 요소 사이 간격을 만들 때</b>. 마진 겹침이 생길 수 있으니 <code>gap</code>을 먼저 씁니다",
    "<code>width</code>와 <code>padding</code>을 둘 다 고정값으로 정할 때. 크기 계산이 어긋나기 쉽습니다",
    "<code>box-sizing</code>을 요소마다 다르게 줄 때. 맨 위에서 한 번 정하고 모든 요소에 같은 값을 씁니다",
  ]),
  instead='간격 값 자체는 <a href="../items/spacing.html">간격 체계</a>가 정하고, 넘친 내용을 어떻게 처리할지는 <a href="overflow.html">넘침</a>에서 다룹니다.',
  cases=cases([
    ('''              <div style="display:inline-block;background:var(--accent);color:#fff;border-radius:7px;padding:10px 18px;font-size:12px;font-weight:700">버튼</div>
              <div style="font-size:10.5px;color:var(--fg-muted);margin-top:7px;font-family:var(--mono)">padding: 10px 18px</div>''',
     "패딩으로 버튼 크기 만들기", "버튼은 <b>높이를 고정하지 않고</b> 글자 둘레에 패딩을 주어 크기를 만듭니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:8px;padding:11px;background:var(--surface);box-sizing:border-box">
                <span style="font-size:11.5px;font-weight:700;display:block">카드</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">width: 100%가 테두리까지 포함</span>
              </div>''',
     "<code>width: 100%</code>에 패딩 더하기", "border-box여야 <code>width:100%</code>에 패딩을 더해도 상자가 부모 밖으로 넘치지 않습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:5px">
                <div style="background:var(--accent-soft);height:22px;border-radius:5px"></div>
                <div style="background:var(--accent-soft);height:22px;border-radius:5px"></div>
                <span style="font-size:10px;color:var(--fg-muted);font-family:var(--mono)">gap: 5px라 겹치지 않음</span>
              </div>''',
     "마진 대신 gap으로 간격 주기", "요소 사이 간격을 gap으로 주면 마진 겹침이 아예 생기지 않습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="상자를 다룰 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="프로젝트 맨 위에 아래 <b>세 줄</b>을 넣어 두면 크기 계산이 대부분 예상대로 맞습니다.",
  code='''<span class="c">/* 대부분의 프로젝트가 맨 위에 두는 줄 */</span>
<span class="t">*</span>, <span class="t">*</span>::<span class="t">before</span>, <span class="t">*</span>::<span class="t">after</span> { <span class="a">box-sizing</span>: border-box; }

<span class="t">.card</span> {
  <span class="a">width</span>: <span class="a">100%</span>;        <span class="c">/* border-box라서 패딩을 더해도 넘치지 않는다 */</span>
  <span class="a">padding</span>: <span class="a">16px</span>;
  <span class="a">border</span>: <span class="a">1px</span> solid <span class="t">var</span>(<span class="a">--line</span>);
}

<span class="c">/* 마진 대신 gap을 쓰면 겹침이 아예 안 생긴다 */</span>
<span class="t">.list</span> { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">16px</span>; }

<span class="c">/* 누를 자리를 키울 때는 마진이 아니라 패딩 */</span>
<span class="t">.icon-btn</span> { <span class="a">padding</span>: <span class="a">10px</span>; }   <span class="c">/* 아이콘 20px + 패딩 = 40px 터치 영역 */</span>''',
  keys=kbd([
    ("<code>border-box</code>를 기본값으로 정하기", "스타일시트 맨 위에서 한 번만 정하고, <b>요소마다 다르게 두지 않습니다</b>"),
    ("마진 대신 <code>gap</code>으로 간격 주기", "위아래 마진은 맞닿으면 <b>합쳐지지만</b>(마진 겹침), gap은 합쳐지지 않습니다"),
    ("누를 자리는 패딩으로 넓히기", "마진으로 간격을 벌리면 그 자리는 <b>눌리지 않는 빈 공간</b>이 됩니다"),
    ("투명한 테두리로 자리를 미리 잡아 두기", "호버할 때만 테두리를 주면 그 두께만큼 상자가 커져서 <b>레이아웃이 1px씩 밀립니다</b>. 처음부터 투명한 테두리를 둬서 자리를 잡아 둡니다"),
    ("<code>width</code>와 <code>padding</code>을 함께 고정하지 않기", "둘 중 하나는 자동으로 두는 편이 안전합니다"),
  ]),
  backend=rows([
    ("API 응답에서 내용과 포장을 나누는 일과 비슷함", "내용과 그 둘레의 패딩·테두리를 나눠 생각하는 것은 API 응답에서 <code>data</code>와 <code>meta</code>를 나누는 일과 비슷합니다. 두 경우 모두 <b>어디까지가 내용인지</b>를 정하는 일입니다."),
    ("글 길이에 따라 달라지는 상자 크기", "상자 높이는 보통 <b>내용의 양에 따라 정해지기</b> 때문에 데이터가 길어지면 레이아웃도 바뀝니다. 그래서 들어올 수 있는 <b>가장 긴 값</b>을 넣고 화면을 한 번 그려 보는 것이 좋은 테스트가 됩니다."),
    ("이미지 크기를 미리 알려 주기", "이미지에 <code>width</code>·<code>height</code> 속성이 없으면 사진을 다 받은 순간 상자가 갑자기 커지면서 <b>아래 내용이 밀려납니다</b>. 서버가 이미지 크기를 함께 내려 주면 사진을 받기 전에 자리를 미리 잡아 둘 수 있습니다."),
    ("메일 HTML을 만들 때", "메일 클라이언트 가운데에는 <code>box-sizing</code>을 무시하는 곳이 많기 때문에, 메일 템플릿은 지금도 <code>&lt;table&gt;</code>로 레이아웃을 짭니다."),
  ]),
  plat_lede="박스 모델은 웹에서 쓰는 개념이고, iOS와 안드로이드는 비슷한 개념을 다른 이름으로 부릅니다.",
  plats=plats([
    ("웹", "CSS box model",
     box(70, 8, 3, 6),
     "<b>네 겹</b>이 분명하게 나뉘고, <code>box-sizing</code> 값에 따라 width가 가리키는 범위가 바뀝니다."),
    ("iOS", "Apple HIG · SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.padding(16)<br>.frame(width:)<br>.border( )</div>''',
     "<code>.padding()</code>으로 패딩을, <code>.frame()</code>으로 크기를 정합니다. <b>마진이라는 개념이 없어서</b> 바깥 여백도 패딩이나 간격으로 줍니다."),
    ("안드로이드", "Compose · View",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Modifier<br>&nbsp;.padding(16.dp)<br>&nbsp;.size(200.dp)</div>''',
     "예전 View에는 padding과 margin이 모두 있었지만, Compose에서는 <b>적은 순서대로 적용되는 <code>Modifier</code></b>로 바뀌었습니다. 그래서 패딩을 테두리보다 앞에 쓰는지 뒤에 쓰는지에 따라 결과가 달라집니다."),
  ]),
  plat_note="iOS와 Compose에는 <b>마진이 없기</b> 때문에, \"마진 16 주세요\"라는 요청은 앱에서 '부모의 패딩'이나 '간격(spacing)'으로 바꿔 구현해야 합니다. 시안의 바깥 여백이 <b>어느 상자에 속하는지</b>(이 상자의 바깥인지, 부모의 안쪽인지)를 분명히 적어 두면 앱에서도 같은 간격으로 옮길 수 있습니다.",
  siblings=siblings("box"),
  related='''        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>''',
)
