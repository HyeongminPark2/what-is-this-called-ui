# -*- coding: utf-8 -*-
from ax2 import ax
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
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">1px<span style="color:var(--fg-faint)"> ← 거의 늘 이 굵기다</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">맞닿으면 1 + 1 = <b>2px</b> 이음선</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">border-box<span style="color:var(--fg-faint)"> ← 선이 폭 안에 들어간다</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">outline<span style="color:var(--fg-faint)"> ← 자리를 안 차지한다</span></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">바탕색 차이<span style="color:var(--fg-faint)"> ← 선 없이 가르는 법</span></div>
                </div>
              </div>'''

D = dict(
  slug="border", ko="테두리와 구분선", en="Border · divider",
  desc="칸을 가르는 선을 어떻게 쓰는가. 테두리와 구분선의 차이, 2px 이음선, box-sizing 사고.",
  lede="선은 <b>칸을 가르는 가장 센 수단</b>입니다. 그래서 적게 쓸수록 화면이 조용해집니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>가르는 법 넷을 바꿔 보세요. <b>줄마다 테두리</b>를 두르면 맞닿은 자리에서 선이
          두 겹이 되어 <b>2px 이음선</b>이 생깁니다 — 데모가 두 테두리를 더해 잽니다.<br>
          줄은 <code>width: 100%</code> 입니다. <code>box-sizing</code>을 끄면 그 100%에
          테두리가 <b>더 붙어</b> 2px 넘칩니다. 격자가 어긋나는 흔한 원인이라
          넘친 줄에 빨간 테를 둘러 표시합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "테두리, 구분선, 선, 괘선"),
    ("영어", "border, divider, separator, rule, hairline"),
    ("같이 쓰는 말",
     "상자를 <b>둘러싸는</b> 선이 테두리, 둘 <b>사이를 가르는</b> 선이 구분선입니다. "
     "아주 얇은 선은 <b>헤어라인</b>(hairline)이라 부릅니다. "
     "HTML 의 <code>&lt;hr&gt;</code>은 <b>내용이 바뀐다</b>는 뜻을 가진 태그라, "
     "그냥 선을 긋고 싶을 때는 <code>border-top</code>이 맞습니다."),
    ("자주 잘못 부름",
     "<b>아웃라인</b> — <code>outline</code>은 <b>자리를 안 차지</b>해 포커스 테에 씁니다. 꾸미는 선이 아닙니다.<br>"
     "<b>그림자</b> — <a href=\"elevation.html\">고도</a>는 <b>높이</b>를, 선은 <b>경계</b>를 말합니다.<br>"
     "<b>모서리</b> — <a href=\"radius.html\">모서리</a>는 모양이고 이건 선입니다."),
  ]),
  axes=ax("테두리와 구분선"),
  oneline="<b>선을 긋기 전에 여백으로 되는지</b> 보세요. 선은 여백으로 안 될 때만 씁니다.",
  s4_title="가르는 법", s4_hint="센 것부터 약한 것까지",
  states=states([
    (rowbox("border:1px solid var(--line);margin-bottom:-1px", "줄마다 테두리", "이음선 2px", False),
     "테두리", "<b>가장 세다</b>. 선이 두 겹이 된다"),
    (rowbox("border-top:1px solid var(--line)", "구분선만", "선 하나", True),
     "구분선", "목록의 <b>기본값</b>으로 삼기 좋다"),
    (rowbox("", "바탕색 차이", "선이 없다", True, 3, zebra=True),
     "바탕색", "줄이 많을 때 <b>가장 조용하다</b>"),
    (rowbox("", "여백만", "선도 색도 없다", None, 3, gap="margin-bottom:7px;"),
     "여백", "덩어리가 <b>저절로</b> 갈린다"),
    (one(txt('<span style="display:block;border:1px solid var(--line);border-radius:5px;padding:5px 7px;font-size:9px">모란상회</span>'
             '<span style="display:block;height:7px"></span>'
             '<span style="display:block;border:1px solid var(--line);border-radius:5px;padding:5px 7px;font-size:9px">새벽상사</span>'),
         "떼어 놓기", True, "사이를 벌리면 이음선이 안 생긴다", "116px"),
     "카드로", "테두리를 쓰되 <b>붙이지 않는다</b>"),
    (rowbox("border:1px solid var(--line);box-sizing:content-box;width:100%", "content-box", "폭을 넘는다", False, 2),
     "<code>content-box</code>", "<b>선이 폭에 더해진다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("색", "한 가지", "<code>--line</code> 하나면 거의 충분하다"),
    ("굵기", "1px", "2px 은 <b>선택됨</b> 같은 뜻이 된다"),
    ("이음선", "1 + 1 = 2px", "맞닿은 테두리는 <b>두 겹</b>이 된다"),
    ("<code>border-box</code>", "폭 안에", "선을 켜도 <b>치수가 안 변한다</b>"),
    ("<code>outline</code>", "자리 없음", "<b>포커스 테</b> 전용"),
    ("바탕색", "선 없이", "줄이 많을 때 가장 조용하다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          선을 쓰는 순서가 있습니다 — <b>여백 → 바탕색 → 구분선 → 테두리</b> 순으로 세집니다.
          화면이 어수선하다는 말을 들으면 대개 <b>한 단계 센 것</b>을 쓰고 있습니다.
          카드마다 테두리를 두르는 대신 바탕색만 바꿔도 구역은 충분히 나뉩니다.<br>
          색은 <b>한 가지면 됩니다</b>. 진한 선과 흐린 선을 섞으면
          '왜 여기만 진하지'라는 질문이 생기고, 그 질문에 답이 없으면 실수입니다.</p>''',
  do=ul([
    "선 색을 <b><code>--line</code> 하나</b>로 두기",
    "목록은 <b>구분선</b>, 떨어진 덩어리는 <b>테두리</b>",
    "<code>box-sizing: border-box</code>를 <b>전역</b>으로 깔기",
  ]),
  dont=ul([
    "맞닿은 줄마다 테두리 두르기 — <b>2px 이음선</b>이 생긴다",
    "선 굵기를 2px 로 올리기 — <b>선택됨</b>이라는 뜻이 생겨 버린다",
    "<code>&lt;hr&gt;</code>로 그냥 선 긋기 — <b>내용이 바뀐다</b>는 뜻이 읽힌다",
    "<code>outline</code>을 꾸미는 데 쓰기 — <b>포커스 테</b>와 헷갈린다",
  ]),
  instead='모양은 <a href="radius.html">모서리</a>, 높이는 <a href="elevation.html">고도</a>, 포커스 테는 <a href="focus.html">초점</a>, 선 대신 쓰는 여백은 <a href="spacing.html">간격 체계</a>.',
  cases=cases([
    (rowbox("border-top:1px solid var(--line)", "목록", "", True), "목록", "구분선 하나"),
    (rowbox("", "표", "", True, 3, zebra=True),
     "표", "<b>줄무늬</b>가 선보다 조용하다"),
    (code(['input {', '  border: 1px solid', '    var(--line);', '}'], "116px", "입력칸은 테두리가 있어야 칸으로 읽힌다", True),
     "입력칸", "여기서는 <b>테두리가 필요</b>하다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 선의 계약서",
  code_lede="전역에 <code>border-box</code>를 깔고, 선은 색 하나로 통일합니다.",
  code='''<span class="c">/* 이 한 줄이 치수 사고를 통째로 없앤다 */</span>
*, *::before, *::after { <span class="a">box-sizing</span>: border-box; }

:root { --line: <span class="a">#e4e6eb</span>; }

<span class="c">/* 목록 — 구분선 하나. 첫 줄 위에는 안 붙는다 */</span>
.row + .row { <span class="a">border-top</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); }

<span class="c">/* 떨어진 덩어리 — 테두리를 쓰되 서로 붙이지 않는다 */</span>
.card { <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); <span class="a">border-radius</span>: <span class="a">var</span>(--radius-3); }

<span class="c">/* ✕ 맞닿은 테두리 — 이음선이 2px 이 된다 */</span>
.row { <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--line); }''',
  keys=kbd([
    ("<code>* + *</code>", "첫 줄 위에는 선이 안 붙는다 — <b>구분선의 기본 꼴</b>"),
    ("<code>border-collapse</code>", "표에서는 이 값으로 <b>이음선을 한 겹</b>으로 만든다"),
    ("<code>outline-offset</code>", "포커스 테를 바깥으로 띄운다. <b>테두리와 겹치지 않게</b>"),
    ("0.5px", "레티나에서만 그려진다. 안 되는 기기에서는 <b>0px 로 사라진다</b>"),
    ("<code>border-box</code>", "폭·높이에 선과 안쪽 여백이 <b>포함</b>된다"),
    ("확인하는 법", "줄을 두 개 겹쳐 두고 <b>이음선 자리를 확대</b>해 본다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "선은 전부 화면의 일입니다. 다만 <b>줄 수</b>에 따라 알맞은 가르기가 달라집니다."),
    ("줄이 많을 때", "수십 줄이 오면 테두리보다 <b>줄무늬</b>가 읽기 편합니다 — 어느 쪽이 올지 미리 물어보면 좋습니다."),
    ("빈 목록", "줄이 없으면 구분선만 남아 <b>이상한 금</b>이 보입니다. <a href=\"empty.html\">빈 상태</a>로 갈아 끼웁니다."),
  ]),
  plat_lede="<b>얇은 선</b>을 그리는 방식이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "1px solid",
     rowbox("border-top:1px solid var(--line)", "CSS px", "", None, 2),
     "<b>CSS 픽셀</b> 1px 입니다. 화면 밀도가 높으면 실제로는 2~3 화소로 그려집니다."),
    ("iOS", "separator",
     '''              <div class="phone" role="img" aria-label="iOS 구분선 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:0;top:34px;height:1px;background:var(--line)"></div>
                <div style="position:absolute;left:8px;right:0;top:48px;height:1px;background:var(--line)"></div></div></div>''',
     "구분선이 <b>왼쪽에서 들여쓰여</b> 시작합니다. 글머리와 선이 맞아 떨어져 보입니다."),
    ("안드로이드", "Divider",
     '''              <div class="phone" role="img" aria-label="안드로이드 구분선 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:34px;height:1px;background:var(--line)"></div>
                <div style="position:absolute;left:0;right:0;top:48px;height:1px;background:var(--line)"></div></div></div>''',
     "Material 3 은 선을 <b>줄이는 쪽</b>입니다. 목록에서는 아예 안 쓰고 여백으로 가르기를 권합니다."),
  ]),
  plat_note="iOS 의 <b>들여쓴 구분선</b>은 웹에서도 그대로 쓸 만합니다 — 아이콘이나 아바타가 있는 목록에서 선을 글머리에 맞추면 줄이 <b>한 덩어리</b>로 읽힙니다. 반대로 안드로이드가 선을 줄이는 쪽으로 간 것도 참고할 만합니다. 선을 지우고 여백만 늘려 보면, 생각보다 많은 경우 선이 없어도 됩니다.",
  siblings=siblings("border"),
  related='''        <li><a href="radius.html"><b>모서리</b><em>2부</em></a></li>
        <li><a href="spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
