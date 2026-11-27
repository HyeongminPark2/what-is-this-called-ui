# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def rowbox(style, label, note="", ok=None, n=3, zebra=False, gap=""):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--fg-muted)")
    names = ["모란상회", "한빛아웃도어", "새벽상사"][:n]
    inner = ''
    for i, x in enumerate(names):
        bg = 'background:var(--bg);' if (zebra and i % 2 == 1) else ''
        inner += ('<span style="display:block;padding:5px 7px;font-size:9px;' + bg + gap + style + '">'
                  + x + '</span>')
    return ('              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">'
            '<span style="display:block;width:116px;background:var(--surface)">' + inner + '</span>'
            '<span style="font-family:var(--mono);font-size:10px;color:' + col + '">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--line: 테두리와 구분선의 <b>한 가지 색</b></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">1px<span style="color:var(--fg-faint)"> ← 거의 늘 이 굵기</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">맞닿으면 1 + 1 = <b>2px</b> 이음선</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">border-box<span style="color:var(--fg-faint)"> ← 선이 폭 안에 들어감</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">outline<span style="color:var(--fg-faint)"> ← 자리를 차지하지 않음</span></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">바탕색 차이<span style="color:var(--fg-faint)"> ← 선 없이 가르는 방법</span></div>
                </div>
              </div>'''

D = dict(
  slug="border", ko="테두리와 구분선", en="Border · divider",
  desc="칸을 가르는 선을 쓰는 법과 함께, 테두리와 구분선의 차이, 맞닿은 테두리가 만드는 2px 이음선, box-sizing 때문에 생기는 치수 문제를 보여 주는 항목입니다.",
  lede="선은 칸을 가르는 방법 가운데 <b>눈에 가장 강하게 띄는 방법</b>입니다. 그래서 선을 적게 쓸수록 화면이 덜 어수선해집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>가르는 법 네 가지를 바꿔 보세요. <b>줄마다 테두리</b>를 두르면 맞닿은 자리에서 선이
          두 겹이 되어 <b>2px 이음선</b>이 생기는데, 데모는 맞닿은 두 테두리의 두께를 실제로 더해 보여 줍니다.<br>
          각 줄의 폭은 <code>width: 100%</code>입니다. <code>box-sizing</code>을 끄면 그 100%에
          테두리 두께가 <b>더해져</b> 줄이 2px 넘칩니다. 격자가 어긋나는 흔한 원인이라서
          넘친 줄에는 빨간 테를 둘러 표시합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "테두리, 구분선, 선, 괘선"),
    ("영어", "border, divider, separator, rule, hairline"),
    ("같이 쓰는 말",
     "상자를 <b>둘러싸는</b> 선은 테두리, 두 요소 <b>사이를 가르는</b> 선은 구분선입니다. "
     "아주 얇은 선은 <b>헤어라인</b>(hairline)이라고 부릅니다. "
     "HTML의 <code>&lt;hr&gt;</code>은 <b>내용이 바뀐다</b>는 뜻을 담은 태그라서, "
     "모양으로만 선을 긋고 싶을 때는 <code>border-top</code>을 쓰는 것이 맞습니다."),
    ("자주 잘못 부르는 이름",
     "<b>아웃라인</b> — <code>outline</code>은 <b>자리를 차지하지 않기</b> 때문에 포커스 테에 씁니다. 꾸미려고 긋는 선이 아닙니다.<br>"
     "<b>그림자</b> — 그림자로 나타내는 <a href=\"elevation.html\">고도</a>는 <b>높이</b>를 보여 주고, 선은 <b>경계</b>를 보여 줍니다.<br>"
     "<b>모서리</b> — <a href=\"radius.html\">모서리</a>는 상자의 모양이고, 테두리와 구분선은 선입니다."),
  ]),
  s4_title="칸을 가르는 방법", s4_hint="눈에 강하게 띄는 것부터 약한 것까지",
  states=states([
    (rowbox("border:1px solid var(--line);margin-bottom:-1px", "줄마다 테두리", "이음선 2px", False),
     "줄마다 테두리 두르기", "<b>가장 강하게</b> 나뉩니다. 맞닿은 자리에서 선이 두 겹이 됩니다"),
    (rowbox("border-top:1px solid var(--line)", "구분선만", "선 하나", True),
     "구분선만 긋기", "목록의 <b>기본값</b>으로 삼기 좋습니다"),
    (rowbox("", "바탕색 차이", "선 없음", True, 3, zebra=True),
     "바탕색을 번갈아 칠하기", "줄이 많을 때 <b>가장 깔끔해 보입니다</b>"),
    (rowbox("", "여백만", "선도 색도 없음", None, 3, gap="margin-bottom:7px;"),
     "여백만으로 나누기", "선이나 색 없이도 덩어리가 <b>저절로</b> 나뉘어 보입니다"),
    (one(txt('<span style="display:block;border:1px solid var(--line);border-radius:5px;padding:5px 7px;font-size:9px">모란상회</span>'
             '<span style="display:block;height:7px"></span>'
             '<span style="display:block;border:1px solid var(--line);border-radius:5px;padding:5px 7px;font-size:9px">새벽상사</span>'),
         "떼어 놓기", True, "사이를 벌려 이음선이 안 생김", "116px"),
     "카드로 떼어 놓기", "테두리를 쓰되 카드끼리 <b>붙이지 않습니다</b>"),
    (rowbox("border:1px solid var(--line);box-sizing:content-box;width:100%", "content-box", "폭을 넘음", False, 2),
     "<code>content-box</code>로 둘 때", "테두리 두께가 <b>폭에 더해집니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("색", "한 가지", "<code>--line</code> 하나면 거의 충분합니다"),
    ("굵기", "1px", "2px로 올리면 <b>선택됨</b> 같은 다른 뜻으로 읽힙니다"),
    ("이음선", "1 + 1 = 2px", "맞닿은 두 테두리가 <b>두 겹</b>으로 겹쳐 2px이 됩니다"),
    ("<code>border-box</code>", "폭 안에", "테두리를 넣어도 <b>치수가 변하지 않습니다</b>"),
    ("<code>outline</code>", "자리 없음", "<b>포커스 테</b>에만 씁니다"),
    ("바탕색", "선 없이", "줄이 많을 때 가장 깔끔해 보입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          칸을 가르는 방법에는 순서가 있습니다. <b>여백, 바탕색, 구분선, 테두리</b> 순으로 갈수록 눈에 강하게 띕니다.
          화면이 어수선하다는 말을 들었다면 대개 필요한 것보다 <b>한 단계 강한 방법</b>을 쓰고 있는 것입니다.
          예를 들어 카드마다 테두리를 두르는 대신 바탕색만 바꿔도 구역은 충분히 나뉩니다.<br>
          선 색은 <b>한 가지면 됩니다</b>. 진한 선과 흐린 선을 섞으면 보는 사람에게
          '왜 여기만 진하지' 하는 의문이 생기는데, 그 차이에 정해 둔 이유가 없다면 실수로 들어간 것입니다.</p>''',
  do_title="테두리와 구분선을 쓸 때 지킬 것",
  dont_title="테두리와 구분선을 쓸 때 피할 것",
  do=ul([
    "선 색을 <b><code>--line</code> 하나</b>로 두기",
    "목록은 <b>구분선</b>으로, 떨어진 덩어리는 <b>테두리</b>로 나누기",
    "<code>box-sizing: border-box</code>를 <b>전역</b>에 적용하기",
  ]),
  dont=ul([
    "맞닿은 줄마다 테두리 두르기. 맞닿은 자리에 <b>2px 이음선</b>이 생깁니다",
    "선 굵기를 2px로 올리기. <b>선택됨</b>이라는 뜻으로 읽힐 수 있습니다",
    "모양만 내려고 <code>&lt;hr&gt;</code>로 선 긋기. <b>내용이 바뀐다</b>는 뜻이 함께 전달됩니다",
    "<code>outline</code>을 꾸미는 데 쓰기. <b>포커스 테</b>와 헷갈립니다",
  ]),
  instead_title="함께 보면 좋은 항목",
  instead='상자의 모양은 <a href="radius.html">모서리</a> 항목에서, 높이는 <a href="elevation.html">고도</a> 항목에서 다룹니다. 포커스 테는 <a href="focus.html">초점</a> 항목에서, 선 대신 여백으로 나누는 방법은 <a href="spacing.html">간격 체계</a> 항목에서 설명합니다.',
  cases=cases([
    (rowbox("border-top:1px solid var(--line)", "목록", "", True), "목록 줄 사이에 구분선 긋기", "줄 사이에 구분선 하나만 둡니다"),
    (rowbox("", "표", "", True, 3, zebra=True),
     "표에 줄무늬 쓰기", "<b>줄무늬</b>가 선보다 덜 어수선합니다"),
    (code(['input {', '  border: 1px solid', '    var(--line);', '}'], "116px", "입력칸은 테두리가 있어야 칸으로 읽힘", True),
     "입력칸에 테두리 두르기", "입력칸에는 <b>테두리가 필요</b>합니다. 테두리가 있어야 입력하는 칸으로 읽히기 때문입니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="선을 코드로 옮기는 방법",
  keys_heads="<th>값과 속성</th><th>쓰면 일어나는 일</th>",
  code_lede="전역에 <code>border-box</code>를 적용하고, 선 색은 하나로 통일합니다.",
  code='''<span class="c">/* 이 한 줄로 테두리 때문에 치수가 넘치는 문제를 막는다 */</span>
*, *::before, *::after { <span class="a">box-sizing</span>: border-box; }

:root { --line: <span class="a">#e4e6eb</span>; }

<span class="c">/* 목록은 구분선 하나. 첫 줄 위에는 붙지 않는다 */</span>
.row + .row { <span class="a">border-top</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); }

<span class="c">/* 떨어진 덩어리는 테두리를 쓰되 서로 붙이지 않는다 */</span>
.card { <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); <span class="a">border-radius</span>: <span class="a">var</span>(--radius-3); }

<span class="c">/* ✕ 맞닿은 테두리는 이음선이 2px이 된다 */</span>
.row { <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); }''',
  keys=kbd([
    ("<code>* + *</code>", "첫 줄 위에는 선이 붙지 않습니다. <b>구분선을 넣는 기본 방식</b>입니다"),
    ("<code>border-collapse</code>", "표에서는 이 값으로 <b>이음선을 한 겹</b>으로 만듭니다"),
    ("<code>outline-offset</code>", "포커스 테를 바깥으로 띄워 <b>테두리와 겹치지 않게</b> 합니다"),
    ("0.5px", "레티나 화면에서만 그려지고, 지원하지 않는 기기에서는 <b>0px로 처리되어 사라집니다</b>"),
    ("<code>border-box</code>", "폭과 높이에 테두리와 안쪽 여백이 <b>포함</b>됩니다"),
    ("확인하는 방법", "줄 두 개를 맞붙여 두고 <b>이음선 자리를 확대</b>해 봅니다"),
  ]),
  backend=rows([
    ("서버와 관계없는 화면 쪽 값", "선은 전부 화면 쪽에서 정합니다. 다만 데이터의 <b>줄 수</b>에 따라 알맞은 가르는 법이 달라집니다."),
    ("줄이 많을 때 가르는 방법", "수십 줄이 오면 테두리보다 <b>줄무늬</b>가 읽기 편합니다. 그래서 데이터가 몇 줄쯤 올지 미리 물어 두면 좋습니다."),
    ("목록이 비었을 때 남는 선", "줄이 하나도 없으면 구분선만 남아 <b>이상한 금</b>이 보입니다. 이때는 목록 대신 <a href=\"empty.html\">빈 상태</a> 화면을 보여 줍니다."),
  ]),
  plat_lede="<b>얇은 선</b>을 그리는 방식이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "1px solid",
     rowbox("border-top:1px solid var(--line)", "CSS px", "", None, 2),
     "<b>CSS 픽셀</b>로 1px입니다. 화면 밀도가 높으면 실제로는 2~3 화소 두께로 그려집니다."),
    ("iOS", "separator",
     '''              <div class="phone" role="img" aria-label="iOS 구분선 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:0;top:34px;height:1px;background:var(--line)"></div>
                <div style="position:absolute;left:8px;right:0;top:48px;height:1px;background:var(--line)"></div></div></div>''',
     "구분선이 <b>왼쪽에서 들여쓴 자리</b>부터 시작해서, 줄의 글머리와 선의 시작점이 맞춰져 보입니다."),
    ("안드로이드", "Divider",
     '''              <div class="phone" role="img" aria-label="안드로이드 구분선 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:34px;height:1px;background:var(--line)"></div>
                <div style="position:absolute;left:0;right:0;top:48px;height:1px;background:var(--line)"></div></div></div>''',
     "Material 3는 선을 <b>줄이는 쪽</b>을 택했습니다. 목록에서는 선을 아예 쓰지 않고 여백으로 가르기를 권합니다."),
  ]),
  plat_note="iOS의 <b>들여쓴 구분선</b>은 웹에서도 그대로 쓸 만합니다. 아이콘이나 아바타가 있는 목록에서 선의 시작점을 글머리에 맞추면 줄 하나가 <b>한 덩어리</b>로 읽힙니다. 안드로이드가 선을 줄이는 쪽을 택한 것도 참고할 만합니다. 선을 지우고 여백만 늘려 보면, 생각보다 많은 경우에 선 없이도 구역이 나뉩니다.",
  siblings=siblings("border"),
  related='''        <li><a href="radius.html"><b>모서리</b><em>2부</em></a></li>
        <li><a href="spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
