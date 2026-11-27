# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ls(v, label, note="", size=14, txt="정산이 확정되었습니다", w="150px", extra=""):
    return ('              <div style="display:grid;gap:6px;width:100%;max-width:' + w + '">'
            '<div style="border:1px dashed var(--line-strong);border-radius:5px;padding:8px;background:var(--surface)">'
            '<p style="margin:0;font-size:' + str(size) + 'px;letter-spacing:' + v + ';line-height:1.6;max-width:none;' + extra + '">' + txt + '</p></div>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted);text-align:center">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="font-size:22px;font-weight:800;letter-spacing:-0.02em;line-height:1.3">정산이 확정되었습니다</div>
                  <div class="pin-out" data-pin="2" style="font-size:13px;letter-spacing:0;line-height:1.8;color:var(--fg-muted);max-width:250px">본문은 손대지 않습니다. 글꼴 디자이너가 이미 맞춰 둔 값입니다.</div>
                  <div class="pin-out" data-pin="3" style="font-size:11px;font-weight:700;letter-spacing:0.06em;color:var(--fg-muted)">THIS WEEK REVENUE</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">em   — 글자 크기에 딸려 가는 단위</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">px   — 크기가 바뀌면 비율이 깨진다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한글은 0 — 조금만 벌려도 흩어진다</div>
                </div>
              </div>'''

D = dict(
  slug="letterspacing", ko="자간", en="Letter spacing · tracking",
  desc="자간을 언제 조정하고 언제 그대로 두는지, 한글에서 특히 조심해야 하는 이유를 실물과 해부도로 보여 주는 항목입니다.",
  lede="자간은 글자와 글자 사이의 거리입니다. 글꼴에 이미 알맞은 값이 들어 있어서, <b>본문에서는 거의 건드리지 않는 것</b>이 맞습니다.",
  axes_lede="글자를 다루는 항목들은 값 하나를 바꾸면 글 전체가 함께 바뀐다는 점이 같습니다. 서로 구별하려면 아래 네 가지를 물어보면 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 양 끝으로 밀어 보세요. 음수로 가면 <b>글자가 서로 닿고</b>, 양수로 가면 글자 사이가 벌어져 <b>낱글자로 흩어져</b> 보입니다.
          지금 값이 어느 범위에 드는지는 아래에 알려 줍니다.<br>
          자간을 조정하는 자리는 두 군데뿐입니다. <b>아주 큰 제목</b>은 조금 좁히고(<code>-0.02em</code>),
          <b>작은 대문자 라벨</b>은 조금 벌립니다(<code>0.05em</code>). 그 밖의 본문은 <b>0</b>으로 둡니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자간, 글자 간격"),
    ("영어", "letter-spacing, tracking"),
    ("같이 쓰는 말",
     "글 전체의 글자 사이를 고르게 벌리거나 좁히는 것을 <b>트래킹</b>(tracking), 특정 두 글자 사이만 "
     "다듬는 것을 <b>커닝</b>(kerning)이라고 합니다. 커닝 값은 글꼴 안에 표로 들어 있어서 "
     "브라우저가 자동으로 적용합니다(<code>font-kerning</code>)."),
    ("자주 잘못 부르는 이름",
     "<b>커닝</b> — 커닝은 <b>글자 쌍마다 값이 다른</b> 보정이고, 자간은 모든 글자 사이를 똑같이 벌립니다.<br>"
     "<b>행간</b> — 글이 답답해 보이는 이유는 대개 자간이 아니라 <b>행간</b>이기 때문에, 자간부터 고쳐서는 나아지지 않습니다.<br>"
     "<b>단어 간격</b> — 띄어쓰기 폭은 자간과 별개로 <code>word-spacing</code>으로 정합니다."),
  ]),
  axes=ax("자간"),
  oneline="자간은 <b>기본값을 그대로 두는 것이 맞는</b> 드문 속성입니다. 값을 바꾸는 곳은 아주 큰 제목과 작은 대문자 라벨, 두 군데뿐입니다.",
  s4_title="값", s4_hint="같은 글, 다른 자간",
  states=states([
    (ls("-0.05em", "-0.05em", "글자가 닿는다"), "너무 좁게", "획이 서로 붙어서 <b>글자를 구별할 수 없습니다</b>"),
    (ls("-0.02em", "-0.02em", "큰 제목에만", 18), "제목 보정", "아주 큰 글자에만 씁니다. 조금 좁혀서 제목이 <b>한 덩어리로 보이게</b> 합니다"),
    (ls("0", "0", "기본값 · 본문"), "0", "<b>본문은 이대로 둡니다.</b> 글꼴을 만들 때 이미 맞춰 둔 값입니다"),
    (ls("0.06em", "0.06em", "작은 대문자 라벨", 10, "THIS WEEK REVENUE"), "라벨 보정",
     "작은 대문자는 조금 벌립니다. <b>벌리지 않으면 글자끼리 붙어 보입니다</b>"),
    (ls("0.12em", "0.12em", "낱글자로 흩어진다"), "너무 넓게", "한 낱말이 <b>따로 떨어진 글자 여럿</b>으로 보입니다"),
    (ls("0.12em", "0.12em · 한글", "한글은 더 빨리 무너진다", 14, "정산이 확정되었습니다"),
     "한글에서", "한글은 네모 칸을 채우는 글자라서 <b>조금만 벌려도</b> 낱말이 한 덩어리로 보이지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("큰 제목", "-0.02em", "글자가 아주 크면 글자 사이가 벌어져 보이므로, <b>조금 좁혀</b> 한 덩어리로 보이게 합니다"),
    ("본문", "0", "<b>건드리지 않습니다.</b> 글꼴 디자이너가 이미 맞춰 둔 값입니다"),
    ("작은 대문자 라벨", "0.05~0.06em", "대문자는 폭이 고르게 커서 글자끼리 붙어 보이므로 <b>조금 벌립니다</b>"),
    ("em 단위", "em", "글자 크기에 비례하는 단위라서 <b>글자 크기가 바뀌어도 비율이 유지됩니다</b>"),
    ("px 단위", "px (쓰지 않는다)", "같은 px 값이 큰 글자에서는 티도 나지 않고, 작은 글자에서는 <b>너무 벌어집니다</b>"),
    ("한글", "0", "한글은 네모 칸을 꽉 채우는 글자라서 <b>벌리면 바로 흩어져 보입니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          한글은 영문과 사정이 다릅니다. 영문은 글자마다 폭이 달라서 <b>사이를 조금 벌려도 글자 간격이 고르게 보이지만</b>,
          한글은 모든 글자가 같은 크기의 네모 칸에 들어 있어서 조금만 벌려도 <b>칸 사이의 빈틈이 그대로 드러납니다.</b>
          '시원하게 보이려고' 자간을 벌린 한국어 화면이 유독 읽기 힘든 것도 이 때문입니다.
          글이 답답해 보일 때 고칠 것은 자간이 아니라 <a href="lineheight.html">행간</a>입니다.</p>''',
  do=ul([
    "<b>아주 큰 제목</b>(28px 이상)을 조금 좁힐 때",
    "영문 <b>작은 대문자 라벨</b>을 조금 벌릴 때. 한글 라벨에는 쓰지 않습니다",
    "로고나 표지처럼 <b>글자 자체가 그림</b>일 때",
  ]),
  dont=ul([
    "<b>본문에 자간을 줄 때</b>. 특히 한글은 조금만 벌려도 글자가 흩어져 보입니다",
    "글이 답답해 보인다고 자간부터 벌릴 때. 원인은 대개 <b>행간</b>입니다",
    "자간을 <code>px</code>로 적을 때. 글자 크기가 바뀌면 글자 크기와 자간의 비율이 달라집니다",
    "대문자 라벨을 벌리는 영문 관례를 한글 라벨에 그대로 쓸 때",
  ]),
  instead='글이 답답하면 <a href="lineheight.html">행간</a>, 줄이 너무 길면 <a href="../items/container.html">최대 폭</a>, 위계가 안 보이면 <a href="hierarchy.html">글자 위계</a>.',
  cases=cases([
    (ls("-0.02em", "큰 제목", "", 20, "정산이 확정되었습니다", "180px"),
     "큰 제목", "<b>-0.02em</b>만 줍니다. 눈에 띄게 좁히려는 것이 아니라 글자가 커지면서 <b>벌어져 보이는 만큼만 되돌리는</b> 값입니다"),
    (ls("0.06em", "작은 라벨", "", 10, "THIS WEEK REVENUE", "180px"),
     "영문 라벨", "작은 대문자는 조금 벌려야 잘 읽힙니다. <b>한글 라벨에는 쓰지 않습니다</b>"),
    (ls("0", "본문", "", 12, "정산 요청이 승인되면 영업일 기준 2일 안에 입금됩니다.", "180px"),
     "본문", "<b>0</b>으로 둡니다. 이 항목에서 가장 중요한 규칙입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="값을 바꾸는 곳은 두 군데",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="기본값을 그대로 쓰기 때문에, 코드에 적는 것은 <b>예외 두 줄</b>뿐입니다.",
  code='''<span class="c">/* 본문에는 아무것도 적지 않는다 */</span>

<span class="c">/* 예외 1. 아주 큰 제목만 살짝 좁게 */</span>
<span class="t">h1</span> { <span class="a">font-size</span>: <span class="a">32px</span>; <span class="a">letter-spacing</span>: -<span class="a">0.02em</span>; }

<span class="c">/* 예외 2. 작은 영문 대문자 라벨만 살짝 넓게 */</span>
<span class="t">.label</span> {
  <span class="a">font-size</span>: <span class="a">11px</span>;
  <span class="a">text-transform</span>: uppercase;
  <span class="a">letter-spacing</span>: <span class="a">0.06em</span>;
}

<span class="c">/* 한글 라벨에는 쓰지 않는다 */</span>
<span class="t">.label</span>:lang(ko) { <span class="a">letter-spacing</span>: <span class="a">0</span>; <span class="a">text-transform</span>: none; }''',
  keys=kbd([
    ("본문은 0", "본문에는 자간을 <b>아무것도 적지 않는 것</b>이 기본입니다"),
    ("<code>em</code>으로 적는다", "자간은 글자 크기에 비례해야 합니다. <code>px</code>로 적으면 글자 크기가 바뀔 때 비율이 맞지 않습니다"),
    ("큰 제목만 -0.02em", "눈에 띄게 좁히는 것이 아니라 글자가 <b>커지면서 벌어져 보이는 만큼만 되돌리는</b> 정도로 줍니다"),
    ("작은 대문자만 +0.05em", "영문에만 쓰고, <b>한글 라벨에는 쓰지 않습니다</b>"),
    ("답답하면 행간을 본다", "글이 답답할 때 자간을 벌려 해결하려 하면 <b>오히려 더 읽기 어려워집니다</b>"),
    ("<code>text-transform</code>과 짝", "글자를 대문자로 바꿀 때만 자간을 함께 조정합니다. 한국어에는 둘 다 쓰지 않습니다"),
  ]),
  backend=rows([
    ("자간은 길이를 바꾼다", "자간을 주면 같은 글자 수라도 <b>글줄이 길어집니다.</b> 그러면 한 줄에 들어가는 글자 수가 줄어서 말줄임이 더 자주 걸립니다."),
    ("다국어", "영문에 맞춘 자간을 한국어나 일본어에 그대로 쓰면 글자가 흩어져 보입니다. 자간을 <b>언어별로 다르게</b> 두려면 <code>:lang()</code>을 씁니다."),
    ("검색과 복사", "자간은 화면에 보이는 모양만 바꾸고 <b>글자 자체는 그대로</b> 둡니다. 그래서 글을 복사하면 자간 없이 붙어 나오는데, 당연한 일이지만 가끔 오해를 삽니다."),
  ]),
  plat_lede="세 플랫폼 모두 자간을 다루는 방식은 비슷하고, 단위만 다릅니다.",
  plats=plats([
    ("웹", "letter-spacing",
     ls("0", "0 · 본문", "", 11, "정산이 확정", "120px"),
     "<code>em</code>으로 적습니다. 대부분의 경우 기본값을 그대로 두는 것이 맞습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.tracking(-0.5)<br>.kerning( )</div>''',
     "<b>트래킹</b>이라고 부르고 <b>포인트 단위</b>로 적습니다. 시스템 글꼴에는 글자 크기별 자간 보정이 이미 들어 있습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">letterSpacing =<br>&nbsp;0.5.sp</div>''',
     "<code>sp</code> 단위로 적습니다. Material 타입 스케일에는 단마다 권장 자간이 정해져 있습니다."),
  ]),
  plat_note="iOS의 시스템 글꼴은 <b>글자 크기에 따라 자간이 자동으로 달라집니다</b>(옵티컬 사이즈). 그래서 디자이너가 iOS 화면에서 재어 온 자간 값을 웹에 그대로 옮기면 어긋납니다. 처음부터 <b>\"본문은 기본값\"</b>으로 합의해 두면 자간 값을 옮길 일이 없어서 이런 어긋남도 생기지 않습니다.",
  siblings=siblings("letterspacing"),
  related='''        <li><a href="../items/lineheight.html"><b>행간</b><em>3부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/hierarchy.html"><b>글자 위계</b><em>3부</em></a></li>''',
)
