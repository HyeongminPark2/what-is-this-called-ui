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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">line-height: 1.8   — 배수로 적는다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">line-height: 28px   — 못 박으면 글자가 커졌을 때 겹친다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">줄 높이 − 글자 크기 = 실제 틈</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">제목 1.2~1.3 · 본문 1.6~1.8</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한글은 영문 기준보다 한 단계 넓게</div>
                </div>
              </div>'''

D = dict(
  slug="lineheight", ko="행간", en="Line height · leading",
  desc="행간을 배수로 적는 이유와 제목·본문의 범위, 한글이 더 넓어야 하는 까닭을 실물과 해부도로 보여주는 항목.",
  lede="글줄과 글줄 사이의 거리. <b>글이 읽히느냐 마느냐</b>를 글꼴보다 더 많이 좌우합니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>글자 크기를 키워 보세요. <b>배수로 적었기 때문에 줄 높이도 따라 커집니다</b> —
          <code>28px</code>처럼 못 박았다면 글자만 커져 줄이 겹쳤을 것입니다.<br>
          아래에 <b>줄 높이와 실제 틈</b>을 재서 알려 주고, 지금 값이 제목용인지 본문용인지도 판정합니다.
          <b>줄 격자 보기</b>를 켜면 줄이 어디에 앉는지 보입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "행간, 줄 간격, 줄 높이"),
    ("영어", "line-height, leading, line spacing"),
    ("같이 쓰는 말",
     "인쇄에서는 <b>레딩</b>(leading)이라 불렀습니다 — 납 활자 사이에 끼우던 납 조각에서 온 말입니다. "
     "글자 위아래로 생기는 빈 공간을 <b>하프 레딩</b>(half-leading), "
     "줄들이 일정한 간격에 맞춰 앉는 것을 <b>베이스라인 그리드</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>자간</b> — 자간은 <b>글자 사이</b>, 행간은 <b>줄 사이</b>입니다. 답답해 보이는 이유는 대개 행간입니다.<br>"
     "<b>문단 간격</b> — 문단과 문단 사이는 <code>margin</code>이지 행간이 아닙니다.<br>"
     "<b><code>line-height: 1.5em</code></b> — 단위를 붙이면 <b>자식이 물려받을 때</b> 계산이 굳어 버립니다."),
  ]),
  axes=ax("행간"),
  oneline="행간은 <b>단위 없이 배수로</b> 적습니다. 그래야 글자 크기가 바뀌어도 비율이 따라옵니다.",
  s4_title="값", s4_hint="같은 글, 다른 행간",
  states=states([
    (lh(1.0, "1.0", "줄이 엉긴다"), "1.0", "윗줄과 아랫줄이 <b>거의 닿는다.</b> 읽을 수 없다"),
    (lh(1.3, "1.3", "제목용"), "1.3", "<b>큰 글자</b>에 맞다. 본문에 쓰면 빽빽하다"),
    (lh(1.7, "1.7", "본문용"), "1.7", "<b>한글 본문의 기본.</b> 영문 기준보다 한 단계 넓다"),
    (lh(2.4, "2.4", "흩어진다"), "2.4", "줄들이 따로 놀아 <b>한 문단으로 안 읽힌다</b>"),
    (lh(1.7, "1.7 · 10px", "작은 글자", 9.5), "작은 글자", "작을수록 <b>더 넓게</b>. 같은 배수라도 틈이 좁다"),
    (lh(1.3, "1.3 · 20px", "큰 글자", 18), "큰 글자", "클수록 <b>좁게</b>. 넓으면 제목이 흩어진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("문단", "paragraph", "행간이 걸리는 단위. 줄 격자를 겹쳐 보면 줄이 어디 앉는지 보인다"),
    ("배수로 적기", "line-height: 1.8", "<b>단위 없이.</b> 글자 크기가 바뀌면 줄 높이도 따라온다"),
    ("못 박기", "line-height: 28px", "글자만 커지면 <b>줄이 겹친다.</b> 쓰지 않는다"),
    ("실제 틈", "line-height − font-size", "눈에 보이는 빈 공간. 같은 배수라도 <b>글자가 작으면 틈도 좁다</b>"),
    ("범위", "1.2~1.8", "제목 1.2~1.3, 본문 1.6~1.8. <b>크면 좁게, 작으면 넓게</b>"),
    ("한글 보정", "+0.1~0.2", "받침 때문에 글자가 아래로 길다. 영문 기준에 <b>한 단계 더</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          단위를 붙인 <code>1.5em</code>이 위험한 이유가 있습니다. <b>계산된 값이 자식에게 그대로 내려가기</b> 때문입니다 —
          부모가 16px 이면 24px 이 되고, 자식 글자가 30px 이어도 <b>줄 높이는 24px 그대로</b>라 겹칩니다.
          단위 없는 <code>1.5</code>는 <b>비율이 내려가서</b> 자식이 자기 크기로 다시 계산합니다.</p>''',
  do=ul([
    "<b>모든 글</b> — 안 정하면 브라우저 기본값(약 1.2)이 쓰여 한글에는 좁습니다",
    "긴 글을 읽히는 화면 — 1.7 안팎",
    "글자 크기가 바뀌는 자리 — <b>배수</b>라야 따라옵니다",
  ]),
  dont=ul([
    "<code>px</code>이나 <code>em</code>으로 못 박는 것 — <b>자식에서 겹칩니다</b>",
    "제목에 본문 행간을 그대로 쓰는 것 — 큰 글자가 <b>흩어져</b> 보입니다",
    "행간으로 문단을 나누는 것 — 문단 사이는 <code>margin</code>입니다",
    "버튼·한 줄 라벨에 1.8 — <b>상자만 커집니다</b>",
  ]),
  instead='글자 크기 단과 함께 묶으려면 <a href="../items/typescale.html">타입 스케일</a>, 줄바꿈은 <a href="hangul.html">한글 조판</a>, 문단 사이는 <a href="../items/spacing.html">간격 체계</a>.',
  cases=cases([
    (lh(1.75, "본문 1.75", "", 11.5, "180px"), "읽는 글", "가장 많이 쓰는 값. <b>한글은 1.7~1.8</b>"),
    (lh(1.3, "제목 1.3", "", 16, "180px"), "제목", "큰 글자는 좁게. <b>덩어리로 보이게</b>"),
    ('''              <div style="width:100%;max-width:180px;display:inline-flex;align-items:center;justify-content:center;background:var(--accent);color:#fff;border-radius:7px;padding:9px 14px;font-size:12px;font-weight:700;line-height:1.2">
                저장하기
              </div>
              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);margin-top:6px;text-align:center">line-height: 1.2</div>''',
     "버튼", "한 줄짜리는 <b>좁게</b>. 안 그러면 상자만 커진다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 문단의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="단위 없는 숫자 하나입니다. 그 한 가지만 지키면 나머지는 범위 문제입니다.",
  code='''<span class="t">body</span> { <span class="a">line-height</span>: <span class="a">1.7</span>; }   <span class="c">/* 단위 없이 — 비율이 내려간다 */</span>

<span class="t">h1</span>, <span class="t">h2</span>, <span class="t">h3</span> { <span class="a">line-height</span>: <span class="a">1.3</span>; }   <span class="c">/* 큰 글자는 좁게 */</span>
<span class="t">.btn</span>, <span class="t">.chip</span> { <span class="a">line-height</span>: <span class="a">1.2</span>; }   <span class="c">/* 한 줄짜리는 더 좁게 */</span>

<span class="c">/* 크기와 행간을 한 묶음으로 토큰에 둔다 */</span>
<span class="t">:root</span> {
  <span class="a">--text-base</span>: <span class="a">16px</span>;  <span class="a">--lh-base</span>: <span class="a">1.7</span>;
  <span class="a">--text-xl</span>: <span class="a">25px</span>;    <span class="a">--lh-xl</span>: <span class="a">1.3</span>;
}

<span class="c">/* 이렇게 쓰지 않는다 — 자식에서 겹친다 */</span>
<span class="t">body</span> { <span class="a">line-height</span>: <span class="a">1.5em</span>; }''',
  keys=kbd([
    ("단위 없이 적는다", "<code>1.7</code>. <code>em</code>·<code>px</code>은 <b>자식에서 겹친다</b>"),
    ("크면 좁게, 작으면 넓게", "제목 1.2~1.3, 본문 1.6~1.8, 아주 작은 글은 더 넓게"),
    ("한글은 한 단계 더", "영문 1.5 가 편하면 한글은 1.7. <b>받침만큼 더</b>"),
    ("크기와 묶어 둔다", "토큰에 <code>--text-lg</code>와 <code>--lh-lg</code>를 짝으로"),
    ("한 줄짜리는 1.2", "버튼·칩·배지. 넓으면 <b>상자만 커진다</b>"),
    ("문단 사이는 margin", "행간을 늘려 문단을 나누려 하면 <b>둘 다 망가진다</b>"),
  ]),
  backend=rows([
    ("행간은 높이를 바꾼다", "같은 글이라도 행간이 0.2 커지면 목록 한 줄의 높이가 달라집니다. <b>가상 스크롤의 줄 높이</b>를 계산해 뒀다면 같이 고쳐야 합니다."),
    ("줄 수 예측", "'세 줄까지만 보여 주기'를 서버에서 글자 수로 자르면 틀립니다. 줄 수는 <b>폭·글꼴·행간</b>이 함께 정합니다 — 화면에서 <a href=\"truncate.html\">말줄임</a>으로 처리합니다."),
    ("메일 HTML", "메일 클라이언트는 행간을 멋대로 덮습니다. <b>인라인 스타일</b>로 적고, 값이 무시될 수 있다고 보고 만듭니다."),
    ("PDF·인쇄", "화면용 1.7 은 인쇄에서 성기게 보입니다. 인쇄용 스타일에서는 <b>조금 좁혀</b> 둡니다."),
  ]),
  plat_lede="두 OS 는 <b>줄 간격을 더하는 방식</b>이라 계산이 다릅니다.",
  plats=plats([
    ("웹", "line-height",
     lh(1.7, "1.7", "", 10, "120px"),
     "<b>배수</b>로 적고, 글자 위아래에 절반씩 나눠 붙습니다(하프 레딩)."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineSpacing(8)<br>.font(.body)</div>''',
     "<b>줄 사이에 더할 값</b>(lineSpacing)을 적습니다. 웹의 배수와 달라서 <b>그대로 옮기면 안 됩니다</b>."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">lineHeight = 24.sp<br>includeFontPadding</div>''',
     "<b>절대값</b>(sp)으로 적습니다. 예전 <code>includeFontPadding</code> 때문에 위아래 여백이 더 생기던 문제가 유명합니다."),
  ]),
  plat_note="<b>웹은 배수, 앱은 더할 값이나 절대값</b>입니다. 시안에 \"행간 1.7\"이라고만 적으면 앱 쪽에서 옮길 수가 없습니다. <b>\"16px 글자에 줄 높이 27px\"</b>처럼 계산된 값을 같이 적어 주면 세 쪽이 같은 화면을 만듭니다.",
  siblings=siblings("lineheight"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>''',
)
