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
  desc="모서리 둥글기를 단으로 두는 방법과, 겹친 상자의 안쪽 모서리를 구하는 공식.",
  lede="둥글기를 <b>단으로 정해 두고</b> 그 단만 씁니다. 아무 데나 <code>8px</code>을 적기 시작하면 화면이 조금씩 어긋납니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>겹친 상자의 <b>안쪽 모서리</b>는 바깥보다 여백만큼 작아야 두 곡선이 나란히 돕니다 —
          <code>안쪽 = 바깥 − 여백</code>입니다. 공식을 끄면 사이가 벌어져
          <b>안쪽이 네모져</b> 보입니다.<br>
          둥근 카드 안에 그림을 꽉 채우면 <code>overflow: hidden</code>이 있어야 모양대로 잘립니다.
          끄면 네모난 그림이 모서리를 덮는데, 데모는 그 자리를 실제로 찍어서 확인합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "모서리, 모서리 둥글기, 라운드, 코너 반경"),
    ("영어", "border radius, corner radius, rounding"),
    ("같이 쓰는 말",
     "완전히 둥근 양 끝은 <b>알약</b>(pill), 정사각형을 동그랗게 만든 것은 <b>원형</b>입니다. "
     "애플이 쓰는 매끈한 곡선은 <b>연속 곡률</b>(continuous · squircle)이라 부르고, "
     "CSS 의 <code>border-radius</code>는 <b>원호</b>(circular)라 미세하게 다릅니다."),
    ("자주 잘못 부름",
     "<b>테두리</b> — <a href=\"border.html\">테두리</a>는 선이고 모서리는 모양입니다. 이름만 같이 붙어 있습니다.<br>"
     "<b>그림자</b> — <a href=\"elevation.html\">고도</a>와 함께 다니지만 따로 정하는 값입니다.<br>"
     "<b>50%</b> — 정사각형에만 동그라미가 되고, 직사각형에서는 <b>타원</b>이 됩니다."),
  ]),
  axes=ax("모서리"),
  oneline="<b>단을 넘지 마세요.</b> 네댓 단이면 화면 전체가 덮이고, 그 밖의 값은 거의 다 실수입니다.",
  s4_title="단", s4_hint="단마다 맡은 부품이 있다",
  states=states([
    (box("0", "0", "표 · 전폭 띠"), "0단", "<b>각지게</b>. 화면 끝에 붙는 것"),
    (box("4px", "4px", "칩 · 배지"), "1단", "모서리만 살짝 눅인다"),
    (box("8px", "8px", "버튼 · 입력칸"), "2단", "손에 가장 많이 잡히는 값"),
    (box("12px", "12px", "카드"), "3단", "덩어리가 <b>한 장</b>으로 읽힌다"),
    (box("16px", "16px", "시트 · 모달"), "4단", "위쪽 두 모서리만 주기도 한다"),
    (box("999px", "999px", "알약 · 아바타", None, "110px", "30px"), "끝단", "<b>높이의 절반</b>보다 크면 더 안 둥글어진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("1단 4px", "칩 · 배지", "작은 것은 <b>작게</b>"),
    ("2단 8px", "버튼 · 입력칸", "가장 자주 쓴다"),
    ("3단 12px", "카드", "덩어리를 <b>한 장</b>으로 묶는다"),
    ("4단 16px", "시트 · 모달", "큰 면일수록 크게"),
    ("999px", "알약 · 원", "<b>50%</b> 는 직사각형에서 타원이 된다"),
    ("공식", "안쪽 = 바깥 − 여백", "겹친 상자의 <b>유일한</b> 규칙"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>큰 면일수록 크게, 작은 면일수록 작게</b>가 원칙입니다.
          16px 짜리 배지에 12px 모서리를 주면 거의 알약이 되고,
          반대로 큰 시트에 4px 을 주면 둥근 줄도 모릅니다.
          알약을 만들 때 <code>50%</code> 대신 <b><code>999px</code></b>을 쓰는 이유도 같습니다 —
          50% 는 가로세로 비를 따라 <b>타원</b>이 되지만,
          999px 은 짧은 변의 절반에서 멈춰 어떤 비에서도 알약이 됩니다.</p>''',
  do=ul([
    "둥글기를 <b>토큰 네댓 개</b>로 두고 그것만 쓰기",
    "겹친 상자는 <b>안쪽 = 바깥 − 여백</b>으로 계산하기",
    "알약은 <code>999px</code>, 동그라미는 <b>정사각형 + 50%</b>",
  ]),
  dont=ul([
    "자리마다 <code>6px</code>·<code>7px</code>을 직접 적기 — <b>조금씩 다른 화면</b>이 된다",
    "둥근 카드 안에 그림을 넣고 <code>overflow</code>를 안 걸기",
    "직사각형에 <code>50%</code> 주기 — <b>타원</b>이 된다",
    "안팎에 <b>같은 값</b> 주기 — 사이가 벌어져 안쪽이 네모져 보인다",
  ]),
  instead='선 자체는 <a href="border.html">테두리와 구분선</a>, 떠 있는 느낌은 <a href="elevation.html">고도</a>, 값 이름은 <a href="tokenname.html">토큰 이름 짓기</a>.',
  cases=cases([
    (box("12px", "카드 12px", "", True, "104px", "40px"), "카드", "3단 하나로 통일"),
    (box("999px", "칩 999px", "", True, "104px", "26px"), "칩 · 필터", "알약으로 <b>눌리는 것</b>임을 알린다"),
    (box("16px 16px 0 0", "시트 위만", "", True, "104px", "40px"), "바텀시트", "<b>위쪽 둘만</b> 둥글린다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 단의 계약서",
  code_lede="단을 토큰으로 두고, 겹칠 때만 공식을 씁니다.",
  code='''<span class="c">/* 네댓 단이면 화면 전체가 덮인다 */</span>
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
    ("<code>999px</code>", "짧은 변의 절반에서 멈춘다 — 어떤 비에서도 <b>알약</b>"),
    ("<code>50%</code>", "가로세로 비를 따라간다 — 정사각형에서만 <b>원</b>"),
    ("<code>overflow: hidden</code>", "자식을 모양대로 자른다. 대신 <b>그림자·툴팁도</b> 잘린다"),
    ("네 값 따로", "<code>16px 16px 0 0</code> — 위 둘만 둥글린다"),
    ("<code>calc()</code>", "안쪽 값은 <b>손으로 적지 말고</b> 바깥에서 빼서 쓴다"),
    ("확인하는 법", "개발자 도구에서 두 모서리를 <b>같이 확대</b>해 곡선이 나란한지 본다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "전부 CSS 값입니다. 다만 <b>이미지 자체를 둥글게</b> 잘라 보내 달라는 요청이 가끔 오는데, 모양은 화면에서 정하는 편이 낫습니다."),
    ("아바타", "서버는 <b>정사각형</b>으로 잘라 주고 화면이 동그랗게 만듭니다 — 자리마다 다른 모양을 쓸 수 있습니다."),
  ]),
  plat_lede="<b>곡선의 모양</b>이 플랫폼마다 조금씩 다릅니다.",
  plats=plats([
    ("웹", "border-radius",
     box("12px", "원호", "", None, "72px", "30px"),
     "<b>원호</b>입니다. 모서리와 직선이 만나는 곳에서 곡률이 한 번에 꺾입니다."),
    ("iOS", "continuous",
     '''              <div class="phone" role="img" aria-label="iOS 모서리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;height:22px;border-radius:9px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<b>연속 곡률</b>을 씁니다. 같은 값이라도 <b>더 부드럽게</b> 보여, 웹에서 흉내 내면 살짝 각져 보입니다."),
    ("안드로이드", "Shape",
     '''              <div class="phone" role="img" aria-label="안드로이드 모서리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;height:22px;border-radius:12px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "Material 3 이 모서리를 <b>크게</b> 씁니다(12~28dp). 버튼은 아예 알약이 기본입니다."),
  ]),
  plat_note="같은 <b>12px</b>이라도 iOS 쪽이 더 둥글어 보입니다 — 곡선을 그리는 방식이 다르기 때문입니다. 디자인 도구에서 'continuous' 로 그린 시안을 웹에 옮기면 <b>각져 보인다</b>는 말을 듣는데, 값이 틀린 게 아니라 곡선이 다른 것입니다. 맞추려면 값을 1~2px 키우거나, 그대로 두고 <b>플랫폼의 기본</b>을 따르는 편이 낫습니다.",
  siblings=siblings("radius"),
  related='''        <li><a href="border.html"><b>테두리와 구분선</b><em>2부</em></a></li>
        <li><a href="elevation.html"><b>고도</b><em>2부</em></a></li>
        <li><a href="card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="chip.html"><b>칩</b><em>5부</em></a></li>''',
)
