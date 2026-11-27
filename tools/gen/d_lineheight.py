# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def lh(v, label, note="", size=11, w="150px"):
    return ('              <div style="display:grid;gap:6px;width:100%;max-width:' + w + '">'
            '<div style="border:1px dashed var(--line-strong);border-radius:5px;padding:7px;background:var(--surface)">'
            '<p style="margin:0;font-size:' + str(size) + 'px;line-height:' + str(v) + ';max-width:none">'
            '행간은 글줄 사이의 거리입니다. 한글은 받침이 있어 더 넓게 봅니다.</p></div>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted);text-align:center">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:240px;border:1px dashed var(--line-strong);border-radius:6px;padding:9px;background:var(--surface);background-image:repeating-linear-gradient(to bottom,color-mix(in srgb,var(--accent) 16%,transparent) 0 1px,transparent 1px 24px);background-position:0 9px">
                    <p style="margin:0;font-size:13px;line-height:24px;max-width:none">행간은 글줄 사이의 거리입니다. 한글은 받침이 있어 글자가 아래로 길기 때문에 영문과 같은 값을 쓰면 답답해 보입니다.</p>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">line-height: 1.8   배수로 적은 값</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">line-height: 28px   고정값이라 글자가 커지면 줄이 겹침</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">줄 높이 − 글자 크기 = 실제 틈</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">제목 1.2~1.3 · 본문 1.6~1.8</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한글은 영문 기준보다 한 단계 넓게</div>
                </div>
              </div>'''

D = dict(
  slug="lineheight", ko="행간", en="Line height · leading",
  desc="행간을 배수로 적는 이유와 제목·본문에 맞는 범위, 한글에서 행간을 더 넓혀야 하는 까닭을 실물과 해부도로 보여 주는 항목입니다.",
  lede="행간은 글줄과 글줄 사이의 거리입니다. 글이 <b>얼마나 잘 읽히는지</b>는 어떤 글꼴을 고르느냐보다 행간을 어떻게 잡느냐에 더 크게 좌우됩니다.",
  axes_lede="글자를 다루는 항목들은 값 하나를 바꾸면 글 전체가 함께 바뀐다는 점이 같습니다. 서로 구별하려면 아래 네 가지를 물어보면 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>글자 크기를 키워 보세요. 행간을 <b>배수로 적었기 때문에 줄 높이도 따라 커집니다</b>.
          <code>28px</code>처럼 고정값으로 적었다면 글자만 커지고 줄 높이는 그대로라서 줄이 겹쳤을 것입니다.<br>
          아래에는 <b>줄 높이와 실제 틈</b>을 재서 보여 주고, 지금 값이 제목에 맞는지 본문에 맞는지도 알려 줍니다.
          <b>줄 격자 보기</b>를 켜면 각 줄이 어느 높이에 놓이는지 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "행간, 줄 간격, 줄 높이"),
    ("영어", "line-height, leading, line spacing"),
    ("같이 쓰는 말",
     "인쇄에서는 <b>레딩</b>(leading)이라고 불렀는데, 납 활자 줄 사이에 끼우던 납 조각에서 온 말입니다. "
     "글자 위아래로 생기는 빈 공간은 <b>하프 레딩</b>(half-leading), "
     "모든 줄을 일정한 간격의 가로줄에 맞춰 놓는 방식은 <b>베이스라인 그리드</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>자간</b> — 자간은 <b>글자 사이</b>, 행간은 <b>줄 사이</b>의 거리입니다. 글이 답답해 보일 때 원인은 대개 자간이 아니라 행간입니다.<br>"
     "<b>문단 간격</b> — 문단과 문단 사이의 거리는 행간이 아니라 <code>margin</code>으로 정합니다.<br>"
     "<b><code>line-height: 1.5em</code></b> — 단위를 붙이면 부모에서 계산한 픽셀 값이 그대로 <b>자식에게 물려지기</b> 때문에, 자식 글자 크기가 달라도 줄 높이가 바뀌지 않습니다."),
  ]),
  axes=ax("행간"),
  oneline="행간은 <b>단위 없이 배수로</b> 적습니다. 그래야 글자 크기가 바뀌어도 줄 높이가 같은 비율로 따라 바뀝니다.",
  s4_title="행간 값에 따른 차이", s4_hint="같은 글을 행간만 바꿔 본 모습",
  states=states([
    (lh(1.0, "1.0", "줄이 거의 닿음"), "1.0으로 너무 좁을 때", "윗줄과 아랫줄이 <b>거의 닿아서</b> 읽기 어렵습니다"),
    (lh(1.3, "1.3", "제목용"), "1.3으로 제목에 맞출 때", "<b>큰 글자</b>에 맞는 값입니다. 본문에 쓰면 줄이 빽빽해 보입니다"),
    (lh(1.7, "1.7", "본문용"), "1.7로 본문에 맞출 때", "<b>한글 본문의 기본값</b>으로, 영문 기준보다 한 단계 넓습니다"),
    (lh(2.4, "2.4", "줄이 흩어져 보임"), "2.4로 너무 넓을 때", "줄 사이가 너무 벌어져 <b>한 문단으로 읽히지 않습니다</b>"),
    (lh(1.7, "1.7 · 10px", "작은 글자", 9.5), "글자가 작을 때", "글자가 작을수록 <b>더 넓게</b> 잡습니다. 같은 배수라도 글자가 작으면 실제 틈이 좁기 때문입니다"),
    (lh(1.3, "1.3 · 20px", "큰 글자", 18), "글자가 클 때", "글자가 클수록 <b>좁게</b> 잡습니다. 넓게 두면 제목 줄 사이가 벌어져 한 덩어리로 보이지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("문단", "paragraph", "행간을 적용하는 단위입니다. 줄 격자를 겹쳐 보면 각 줄이 어느 높이에 놓이는지 보입니다"),
    ("배수로 적기", "line-height: 1.8", "<b>단위 없이</b> 적습니다. 그러면 글자 크기가 바뀔 때 줄 높이도 따라 바뀝니다"),
    ("고정값으로 적기", "line-height: 28px", "글자만 커지고 줄 높이는 그대로라 <b>줄이 겹칩니다.</b> 그래서 쓰지 않습니다"),
    ("실제 틈", "line-height − font-size", "눈에 보이는 줄 사이 빈 공간입니다. 같은 배수라도 <b>글자가 작으면 틈도 좁습니다</b>"),
    ("범위", "1.2~1.8", "제목은 1.2~1.3, 본문은 1.6~1.8을 씁니다. <b>글자가 크면 좁게, 작으면 넓게</b> 잡습니다"),
    ("한글 보정", "+0.1~0.2", "한글은 받침 때문에 글자가 아래로 길어서, 영문 기준보다 <b>한 단계 더</b> 넓힙니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          단위를 붙인 <code>1.5em</code>을 피하는 이유는 <b>계산이 끝난 픽셀 값이 자식에게 그대로 내려가기</b> 때문입니다.
          예를 들어 부모 글자가 16px이면 줄 높이는 24px로 계산되고, 자식 글자가 30px이어도 <b>줄 높이는 24px 그대로</b>라서 줄이 겹칩니다.
          반면 단위 없는 <code>1.5</code>는 <b>비율이 그대로 내려가므로</b> 자식이 자기 글자 크기로 줄 높이를 다시 계산합니다.</p>''',
  do=ul([
    "<b>모든 글</b>에 행간을 정해 둘 때. 정하지 않으면 브라우저 기본값(약 1.2)이 쓰이는데, 한글에는 좁습니다",
    "긴 글을 읽는 화면을 만들 때. 1.7 안팎을 씁니다",
    "글자 크기가 바뀌는 자리에 쓸 때. <b>배수</b>로 적어야 줄 높이가 따라 바뀝니다",
  ]),
  dont=ul([
    "<code>px</code>이나 <code>em</code>으로 고정할 때. 글자가 더 큰 자식 요소에서 <b>줄이 겹칩니다</b>",
    "제목에 본문 행간을 그대로 쓸 때. 큰 글자의 줄 사이가 벌어져 <b>흩어져</b> 보입니다",
    "행간을 늘려 문단을 나눌 때. 문단 사이는 <code>margin</code>으로 띄웁니다",
    "버튼이나 한 줄짜리 라벨에 1.8을 줄 때. 글은 한 줄인데 <b>상자만 커집니다</b>",
  ]),
  instead_title="행간과 이어지는 주제를 다루는 항목",
  instead='글자 크기 단계와 행간을 한 묶음으로 정하려면 <a href="../items/typescale.html">타입 스케일</a>을 봅니다. 줄을 어디서 바꾸는지는 <a href="hangul.html">한글 조판</a>에서, 문단 사이를 띄우는 값은 <a href="../items/spacing.html">간격 체계</a>에서 다룹니다.',
  cases=cases([
    (lh(1.75, "본문 1.75", "", 11.5, "180px"), "긴 글을 읽는 본문", "가장 많이 쓰는 값으로, <b>한글은 1.7~1.8</b>을 씁니다"),
    (lh(1.3, "제목 1.3", "", 16, "180px"), "여러 줄 제목을 한 덩어리로 보이기", "큰 글자는 행간을 좁게 잡아서 여러 줄이 <b>한 덩어리로 보이게</b> 합니다"),
    ('''              <div style="width:100%;max-width:180px;display:inline-flex;align-items:center;justify-content:center;background:var(--accent);color:#fff;border-radius:7px;padding:9px 14px;font-size:12px;font-weight:700;line-height:1.2">
                저장하기
              </div>
              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);margin-top:6px;text-align:center">line-height: 1.2</div>''',
     "한 줄짜리 버튼 글자", "한 줄짜리 글은 행간을 <b>좁게</b> 잡습니다. 넓히면 버튼 상자만 커집니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="행간을 적는 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="행간은 단위 없는 숫자 하나로 적습니다. 이것만 지키면 나머지는 자리마다 알맞은 범위를 고르는 일입니다.",
  code='''<span class="t">body</span> { <span class="a">line-height</span>: <span class="a">1.7</span>; }   <span class="c">/* 단위 없이 적으면 비율이 내려간다 */</span>

<span class="t">h1</span>, <span class="t">h2</span>, <span class="t">h3</span> { <span class="a">line-height</span>: <span class="a">1.3</span>; }   <span class="c">/* 큰 글자는 좁게 */</span>
<span class="t">.btn</span>, <span class="t">.chip</span> { <span class="a">line-height</span>: <span class="a">1.2</span>; }   <span class="c">/* 한 줄짜리는 더 좁게 */</span>

<span class="c">/* 크기와 행간을 한 묶음으로 토큰에 둔다 */</span>
<span class="t">:root</span> {
  <span class="a">--text-base</span>: <span class="a">16px</span>;  <span class="a">--lh-base</span>: <span class="a">1.7</span>;
  <span class="a">--text-xl</span>: <span class="a">25px</span>;    <span class="a">--lh-xl</span>: <span class="a">1.3</span>;
}

<span class="c">/* 이렇게 쓰지 않는다. 자식에서 줄이 겹친다 */</span>
<span class="t">body</span> { <span class="a">line-height</span>: <span class="a">1.5em</span>; }''',
  keys=kbd([
    ("단위 없이 배수로 적기", "<code>1.7</code>처럼 적습니다. <code>em</code>이나 <code>px</code>을 붙이면 <b>자식에서 줄이 겹칩니다</b>"),
    ("글자가 크면 좁게, 작으면 넓게 잡기", "제목은 1.2~1.3, 본문은 1.6~1.8로 두고, 아주 작은 글은 더 넓게 잡습니다"),
    ("한글은 한 단계 더 넓히기", "영문이 1.5에서 편하게 읽히면 한글은 1.7을 씁니다. <b>받침만큼 더</b> 넓히는 것입니다"),
    ("글자 크기와 짝지어 두기", "토큰에 <code>--text-lg</code>와 <code>--lh-lg</code>를 짝으로 둡니다"),
    ("한 줄짜리 글은 1.2로", "버튼, 칩, 배지에 씁니다. 넓히면 <b>상자만 커집니다</b>"),
    ("문단 사이는 margin으로 띄우기", "행간을 늘려 문단을 나누려 하면 문단 안의 줄 간격까지 벌어져 <b>행간과 문단 간격이 둘 다 어긋납니다</b>"),
  ]),
  backend=rows([
    ("행간에 따라 바뀌는 목록 줄 높이", "같은 글이라도 행간이 0.2 커지면 목록 한 줄의 높이가 달라집니다. 그래서 <b>가상 스크롤의 줄 높이</b>를 미리 계산해 두었다면 행간을 바꿀 때 그 값도 같이 고쳐야 합니다."),
    ("서버에서 줄 수를 맞추기 어려운 이유", "'세 줄까지만 보여 주기'를 서버에서 글자 수로 자르면 줄 수가 맞지 않습니다. 줄 수는 <b>폭·글꼴·행간</b>이 함께 정하기 때문에, 화면에서 <a href=\"truncate.html\">말줄임</a>으로 처리합니다."),
    ("메일 HTML에서 행간 적기", "메일 클라이언트는 적어 둔 행간을 자기 기본값으로 덮어쓰기도 합니다. 그래서 행간을 <b>인라인 스타일</b>로 적고, 그래도 값이 무시될 수 있다고 보고 만듭니다."),
    ("PDF와 인쇄에 쓰는 행간", "화면용 1.7은 인쇄하면 줄 사이가 성기게 보이기 때문에, 인쇄용 스타일에서는 행간을 <b>조금 좁혀</b> 둡니다."),
  ]),
  plat_lede="두 OS는 웹과 달리 <b>줄 간격을 더하는 방식</b>을 쓰기 때문에 계산이 다릅니다.",
  plats=plats([
    ("웹", "line-height",
     lh(1.7, "1.7", "", 10, "120px"),
     "<b>배수</b>로 적으며, 줄 높이에서 글자 크기를 뺀 나머지가 글자 위아래에 절반씩 나뉘어 붙습니다(하프 레딩)."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineSpacing(8)<br>.font(.body)</div>''',
     "<b>줄 사이에 더할 값</b>(lineSpacing)을 적습니다. 웹의 배수와 뜻이 달라서 웹 값을 <b>그대로 옮기면 안 됩니다</b>."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">lineHeight = 24.sp<br>includeFontPadding</div>''',
     "줄 높이를 <b>절대값</b>(sp)으로 적습니다. 예전에는 <code>includeFontPadding</code> 설정 때문에 글자 위아래에 여백이 더 생기는 문제가 잘 알려져 있었습니다."),
  ]),
  plat_note="행간을 <b>웹은 배수로, 앱은 더할 값이나 절대값으로</b> 적습니다. 그래서 시안에 \"행간 1.7\"이라고만 적으면 앱 개발자는 그 값을 옮길 수 없습니다. <b>\"16px 글자에 줄 높이 27px\"</b>처럼 계산된 값을 함께 적어 주면 웹과 두 앱이 같은 화면을 만들 수 있습니다.",
  siblings=siblings("lineheight"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>''',
)
