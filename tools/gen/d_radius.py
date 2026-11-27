# -*- coding: utf-8 -*-
from ax2 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(r, label, note="", ok=None, w="110px", h="44px"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">'
            '<span style="display:block;width:' + w + ';height:' + h + ';background:var(--accent-soft);'
            'border:1px solid ' + col + ';border-radius:' + r + '"></span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:10.5px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--radius-1: 4px<span style="color:var(--fg-faint)"> ← 칩 · 배지</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">--radius-2: 8px<span style="color:var(--fg-faint)"> ← 버튼 · 입력칸</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">--radius-3: 12px<span style="color:var(--fg-faint)"> ← 카드</span></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">--radius-4: 16px<span style="color:var(--fg-faint)"> ← 시트 · 모달</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">--radius-full: 999px<span style="color:var(--fg-faint)"> ← 알약 · 동그라미</span></div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">안쪽 = 바깥 − 여백<span style="color:var(--fg-faint)"> ← 겹칠 때의 공식</span></div>
                </div>
              </div>'''

D = dict(
  slug="radius", ko="모서리", en="Border radius · corner scale",
  desc="모서리 둥글기를 단으로 정해 두는 방법과, 겹친 상자의 안쪽 모서리 값을 구하는 공식을 보여 주는 항목입니다.",
  lede="모서리 둥글기는 몇 가지 <b>단으로 정해 두고</b> 그 단만 씁니다. 자리마다 <code>8px</code> 같은 값을 직접 적기 시작하면 화면마다 둥글기가 조금씩 어긋납니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 값을 어떻게 쓸지 <b>정해 둔 규칙</b>입니다. 그래서 생김새 대신 아래 네 가지를 물어보면 토큰끼리 무엇이 다른지 가려집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>겹친 상자의 <b>안쪽 모서리</b>는 바깥 모서리보다 여백만큼 작아야 두 곡선이 나란히 이어집니다.
          식으로 쓰면 <code>안쪽 = 바깥 − 여백</code>입니다. 공식을 끄면 모서리에서 두 곡선 사이가 벌어져
          <b>안쪽이 네모져</b> 보입니다.<br>
          둥근 카드 안에 그림을 꽉 채울 때는 <code>overflow: hidden</code>이 있어야 그림이 카드 모양대로 잘립니다.
          이 설정을 끄면 네모난 그림이 둥근 모서리를 덮는데, 데모는 그 자리를 실제로 찍어서 그림이 튀어나왔는지 확인합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "모서리, 모서리 둥글기, 라운드, 코너 반경"),
    ("영어", "border radius, corner radius, rounding"),
    ("같이 쓰는 말",
     "양 끝을 완전히 둥글린 모양은 <b>알약</b>(pill), 정사각형을 동그랗게 만든 것은 <b>원형</b>이라고 합니다. "
     "애플이 쓰는 매끈한 곡선은 <b>연속 곡률</b>(continuous · squircle)이라고 부르는데, "
     "CSS의 <code>border-radius</code>는 <b>원호</b>(circular)로 그리기 때문에 모양이 미세하게 다릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>테두리</b> — <a href=\"border.html\">테두리</a>는 선이고 모서리는 모양입니다. CSS 속성 이름에 둘 다 border가 들어갈 뿐 서로 다른 값입니다.<br>"
     "<b>그림자</b> — 모서리는 <a href=\"elevation.html\">고도</a>와 함께 쓰이는 일이 많지만, 둘은 따로 정하는 값입니다.<br>"
     "<b>50%</b> — <code>50%</code>를 주면 정사각형에서만 동그라미가 되고, 직사각형에서는 <b>타원</b>이 됩니다."),
  ]),
  axes=ax("모서리"),
  oneline="모서리 값은 <b>정해 둔 단 안에서만</b> 고르세요. 네댓 단이면 화면 전체에 필요한 둥글기를 모두 나타낼 수 있어서, 단에 없는 값은 대부분 실수로 들어간 것입니다.",
  s4_title="단", s4_hint="단마다 쓰는 부품",
  states=states([
    (box("0", "0", "표 · 전폭 띠"), "0단", "화면 끝에 붙는 것은 <b>각지게</b> 둡니다"),
    (box("4px", "4px", "칩 · 배지"), "1단", "모서리만 살짝 둥글립니다"),
    (box("8px", "8px", "버튼 · 입력칸"), "2단", "가장 자주 쓰는 값입니다"),
    (box("12px", "12px", "카드"), "3단", "내용 덩어리가 <b>한 장</b>의 카드로 읽힙니다"),
    (box("16px", "16px", "시트 · 모달"), "4단", "위쪽 두 모서리에만 주기도 합니다"),
    (box("999px", "999px", "알약 · 아바타", None, "110px", "30px"), "끝단", "값이 <b>높이의 절반</b>을 넘으면 더 둥글어지지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("1단 4px", "칩 · 배지", "작은 부품에는 <b>작은</b> 값을 줍니다"),
    ("2단 8px", "버튼 · 입력칸", "가장 자주 씁니다"),
    ("3단 12px", "카드", "내용 덩어리를 <b>한 장</b>으로 묶어 보이게 합니다"),
    ("4단 16px", "시트 · 모달", "큰 면일수록 크게 줍니다"),
    ("999px", "알약 · 원", "<b>50%</b>를 주면 직사각형에서 타원이 되므로 999px을 씁니다"),
    ("공식", "안쪽 = 바깥 − 여백", "겹친 상자에서 지켜야 할 <b>유일한</b> 규칙입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          모서리 값은 <b>큰 면일수록 크게, 작은 면일수록 작게</b> 주는 것이 원칙입니다.
          16px짜리 배지에 12px 모서리를 주면 거의 알약 모양이 되고,
          반대로 큰 시트에 4px을 주면 둥근지 알아보기 어렵습니다.
          알약을 만들 때 <code>50%</code> 대신 <b><code>999px</code></b>을 쓰는 데에도 이유가 있습니다.
          50%는 가로세로 비율을 따라가서 <b>타원</b>이 되지만,
          999px은 짧은 변의 절반에서 더 커지지 않으므로 비율과 상관없이 알약 모양이 됩니다.</p>''',
  do=ul([
    "둥글기를 <b>토큰 네댓 개</b>로 정해 두고 그 토큰만 쓰기",
    "겹친 상자는 <b>안쪽 = 바깥 − 여백</b>으로 계산하기",
    "알약은 <code>999px</code>로, 동그라미는 <b>정사각형에 50%</b>로 만들기",
  ]),
  dont=ul([
    "자리마다 <code>6px</code>·<code>7px</code>을 직접 적기. 화면마다 둥글기가 <b>조금씩 달라집니다</b>",
    "둥근 카드 안에 그림을 넣고 <code>overflow</code>를 걸지 않기. 그림이 모서리 밖으로 튀어나옵니다",
    "직사각형에 <code>50%</code> 주기. 알약이 아니라 <b>타원</b>이 됩니다",
    "겹친 상자 안팎에 <b>같은 값</b> 주기. 모서리에서 두 곡선 사이가 벌어져 안쪽이 네모져 보입니다",
  ]),
  instead='선 자체는 <a href="border.html">테두리와 구분선</a>, 떠 있는 느낌은 <a href="elevation.html">고도</a>, 값 이름은 <a href="tokenname.html">토큰 이름 짓기</a>.',
  cases=cases([
    (box("12px", "카드 12px", "", True, "104px", "40px"), "카드", "카드는 3단 하나로 통일합니다"),
    (box("999px", "칩 999px", "", True, "104px", "26px"), "칩 · 필터", "알약 모양으로 <b>누를 수 있는 것</b>임을 알립니다"),
    (box("16px 16px 0 0", "시트 위만", "", True, "104px", "40px"), "바텀시트", "<b>위쪽 두 모서리만</b> 둥글립니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="모서리를 코드로 옮기는 법",
  code_lede="단은 토큰으로 정해 두고, 상자가 겹칠 때만 공식으로 안쪽 값을 구합니다.",
  code='''<span class="c">/* 네댓 단이면 화면 전체에 충분하다 */</span>
:root {
  --radius-1: <span class="a">4px</span>;    <span class="c">/* 칩 · 배지 */</span>
  --radius-2: <span class="a">8px</span>;    <span class="c">/* 버튼 · 입력칸 */</span>
  --radius-3: <span class="a">12px</span>;   <span class="c">/* 카드 */</span>
  --radius-4: <span class="a">16px</span>;   <span class="c">/* 시트 · 모달 */</span>
  --radius-full: <span class="a">999px</span>;
}

<span class="c">/* 겹치면 안쪽은 여백만큼 작게 */</span>
.card { <span class="a">border-radius</span>: <span class="a">var</span>(--radius-3); <span class="a">padding</span>: <span class="a">8px</span>; <span class="a">overflow</span>: hidden; }
.card &gt; .thumb { <span class="a">border-radius</span>: <span class="a">calc</span>(<span class="a">var</span>(--radius-3) - <span class="a">8px</span>); }

<span class="c">/* ✕ 직사각형에서는 타원이 된다 */</span>
.pill { <span class="a">border-radius</span>: <span class="a">50%</span>; }''',
  keys=kbd([
    ("<code>999px</code>", "짧은 변의 절반에서 더 커지지 않으므로, 가로세로 비율과 상관없이 <b>알약</b> 모양이 됩니다"),
    ("<code>50%</code>", "가로세로 비율을 따라가므로 정사각형에서만 <b>원</b>이 됩니다"),
    ("<code>overflow: hidden</code>", "자식을 카드 모양대로 자릅니다. 대신 카드 밖으로 나가는 <b>그림자와 툴팁도</b> 함께 잘립니다"),
    ("네 값 따로", "<code>16px 16px 0 0</code>처럼 네 값을 따로 주면 위쪽 두 모서리만 둥글립니다"),
    ("<code>calc()</code>", "안쪽 값은 <b>손으로 적지 말고</b> 바깥 값에서 여백을 빼서 구합니다"),
    ("확인하는 법", "개발자 도구에서 두 모서리를 <b>함께 확대</b>해 곡선이 나란한지 봅니다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "모서리는 전부 CSS 값입니다. 다만 <b>이미지 자체를 둥글게</b> 잘라 보내 달라는 요청이 가끔 오는데, 모양은 화면 쪽에서 정하는 편이 낫습니다."),
    ("아바타", "서버는 이미지를 <b>정사각형</b>으로 잘라 주고, 화면에서 동그랗게 만듭니다. 그래야 같은 이미지를 자리마다 다른 모양으로 쓸 수 있습니다."),
  ]),
  plat_lede="<b>곡선의 모양</b>이 플랫폼마다 조금씩 다릅니다.",
  plats=plats([
    ("웹", "border-radius",
     box("12px", "원호", "", None, "72px", "30px"),
     "모서리를 <b>원호</b>로 그립니다. 그래서 곡선과 직선이 만나는 곳에서 곡률이 한 번에 바뀝니다."),
    ("iOS", "continuous",
     '''              <div class="phone" role="img" aria-label="iOS 모서리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;height:22px;border-radius:9px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<b>연속 곡률</b>을 씁니다. 같은 값이라도 <b>더 부드럽게</b> 보이기 때문에, 같은 값을 웹에 옮기면 살짝 각져 보입니다."),
    ("안드로이드", "Shape",
     '''              <div class="phone" role="img" aria-label="안드로이드 모서리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;height:22px;border-radius:12px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "Material 3는 모서리 값을 <b>크게</b>(12~28dp) 쓰고, 버튼은 알약 모양이 기본입니다."),
  ]),
  plat_note="곡선을 그리는 방식이 다르기 때문에 같은 <b>12px</b>이라도 iOS 쪽이 더 둥글어 보입니다. 그래서 디자인 도구에서 'continuous'로 그린 시안을 웹에 옮기면 <b>각져 보인다</b>는 말을 듣는데, 값이 틀린 것이 아니라 곡선을 그리는 방식이 다른 것입니다. 모양을 맞추려면 웹 쪽 값을 1~2px 키우거나, 값은 그대로 두고 <b>플랫폼마다 기본 곡선</b>을 따르는 편이 낫습니다.",
  siblings=siblings("radius"),
  related='''        <li><a href="border.html"><b>테두리와 구분선</b><em>2부</em></a></li>
        <li><a href="elevation.html"><b>고도</b><em>2부</em></a></li>
        <li><a href="card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="chip.html"><b>칩</b><em>5부</em></a></li>''',
)
