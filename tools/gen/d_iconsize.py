# -*- coding: utf-8 -*-
from ax2 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ICO = ('<svg width="%s" height="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:block">'
       '<path d="M12 3v12M7 11l5 5 5-5M4 20h16"/></svg>')

def ic(size, label, note="", ok=None, sw="1.5"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">'
            '<span style="display:grid;place-items:center;width:52px;height:52px;border:1px solid ' + col + ';'
            'border-radius:6px;background:var(--surface);color:var(--fg)">' + (ICO % (size, size, sw)) + '</span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">viewBox="0 0 24 24"<span style="color:var(--fg-faint)"> ← 그린 좌표계</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">width · height<span style="color:var(--fg-faint)"> ← 화면에서의 크기</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">stroke-width 는 <b>같이 줄어든다</b></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">stroke="currentColor"<span style="color:var(--fg-faint)"> ← 글자색을 따라간다</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">인라인 SVG 는 <b>베이스라인</b>에 앉는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">누르는 자리는 44px<span style="color:var(--fg-faint)"> ← 그림 크기와 별개</span></div>
                </div>
              </div>'''

D = dict(
  slug="iconsize", ko="아이콘 크기", en="Icon size scale",
  desc="아이콘 크기를 단으로 정해 두는 방법과 함께, 아이콘을 줄이면 선 굵기도 함께 줄어드는 문제와 아이콘을 글자와 가운데로 맞추는 법을 보여 주는 항목입니다.",
  lede="아이콘 크기는 <b>글자 크기가 아니라 줄 높이</b>에 맞춥니다. 또 아이콘의 <b>그림 크기와 누르는 자리의 크기</b>는 따로 정하는 값입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 값을 어떻게 쓸지 <b>정해 둔 규칙</b>입니다. 그래서 생김새 대신 아래 네 가지를 물어보면 토큰끼리 무엇이 다른지 가려집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이 아이콘은 <code>viewBox 24</code>에 <b>선 굵기 1.5</b>로 그렸습니다.
          그대로 줄이면 선도 함께 얇아져서 <b>12px에서는 0.75px</b>이 되는데,
          작은 아이콘이 화면에서 흐려 보이는 이유가 이것입니다. '선 굵기를 고정'을 켜면 선이 다시 1.5px로 그려집니다.<br>
          인라인 SVG는 <b>글자처럼 베이스라인 위에 놓여</b> 글자의 세로 가운데보다 몇 px 위로 뜹니다.
          눈으로는 잘 보이지 않지만, 아이콘과 글자를 나란히 두는 자리마다 이 어긋남이 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "아이콘 크기, 아이콘 단"),
    ("영어", "icon size, icon scale, optical size"),
    ("같이 쓰는 말",
     "선으로 그린 아이콘은 <b>라인 아이콘</b>(outline · stroke), 면을 채운 아이콘은 <b>솔리드</b>(filled)라고 합니다. "
     "크기마다 <b>따로 다시 그린</b> 그림을 쓰는 방식은 <b>광학 크기</b>(optical size)라고 하는데, "
     "Material Symbols는 이것을 <code>opsz</code> 축으로 넣어 두었습니다."),
    ("자주 잘못 부르는 이름",
     "<b>터치 타깃</b> — <a href=\"touchtarget.html\">터치 타깃</a>은 <b>누르는 넓이</b>이고, 아이콘 크기는 <b>그림의 크기</b>입니다.<br>"
     "<b>아이콘 글꼴</b> — <a href=\"iconfont.html\">아이콘 글꼴</a>은 크기가 아니라 그림을 <b>글자로</b> 다루는 방식을 가리킵니다.<br>"
     "<b>파비콘</b> — 파비콘은 브라우저 탭에 쓰는 아이콘이라 화면 안 아이콘의 크기 단과는 별개입니다."),
  ]),
  axes=ax("아이콘 크기"),
  oneline="아이콘 크기는 16 · 20 · 24, <b>세 단이면 충분합니다</b>. 그리고 누르는 자리는 그림 크기와 상관없이 언제나 44px입니다.",
  s4_title="단", s4_hint="자리마다 쓰는 크기",
  states=states([
    (ic(12, "12px", "거의 안 쓴다", False, "1.5"), "너무 작다", "선 굵기가 <b>1px 아래</b>로 줄어 흐려 보입니다"),
    (ic(16, "16px", "본문 속 · 칩"), "1단", "본문 글 안에 섞어 씁니다"),
    (ic(20, "20px", "목록 · 버튼"), "2단", "<b>가장 많이</b> 씁니다"),
    (ic(24, "24px", "앱바 · 바텀탭"), "3단", "글자 없이 아이콘만 놓이는 자리에 씁니다"),
    (ic(32, "32px", "빈 상태 · 안내"), "큰 단", "아이콘이라기보다 그림에 가깝게 씁니다"),
    (ic(12, "12px", "굵기를 되돌림", True, "3"), "굵기 고정", "크기가 작아도 선이 <b>1.5px로</b> 그려집니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>viewBox</code>", "그린 좌표계", "보통 24로 통일합니다"),
    ("<code>width·height</code>", "화면 크기", "크기를 바꿀 때는 이 값만 바꿉니다"),
    ("<code>stroke-width</code>", "같이 줄어듦", "아이콘을 작게 쓰면 선이 얇아져 <b>흐려 보입니다</b>"),
    ("<code>currentColor</code>", "글자색 따라감", "글자색을 따라가므로 아이콘 색을 따로 적지 않아도 됩니다"),
    ("베이스라인", "위로 뜸", "<code>display: block</code>을 주면 위로 뜨지 않습니다"),
    ("누르는 자리", "44px", "그림 크기와 <b>따로</b> 정합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          가장 흔한 실수는 <b>24로 그린 아이콘을 16으로 줄여 쓰는 것</b>입니다.
          모양은 같아 보여도 선이 1.5에서 1.0으로 얇아져서 다른 아이콘처럼 보입니다.
          그래서 같은 줄에 24px짜리와 16px짜리를 나란히 두면 <b>굵기가 달라</b> 금방 티가 납니다.<br>
          해결 방법은 두 가지로, 크기마다 <b>선 굵기를 원래대로 되돌리거나</b>
          아예 <b>크기별로 다시 그린</b> 그림을 쓰는 것입니다.
          뒤의 방법이 광학 크기인데, 작은 아이콘일수록 획을 덜어 내서 더 또렷하게 보이도록 그립니다.</p>''',
  do=ul([
    "크기를 <b>16 · 20 · 24</b> 세 단으로 두기",
    "SVG에 <code>display: block</code>을 주어 <b>베이스라인 어긋남</b> 막기",
    "<code>stroke=\"currentColor\"</code>로 <b>글자색을 따라가게</b> 하기",
  ]),
  dont=ul([
    "24px 그림을 12px로 줄여 쓰기. 선이 얇아져 <b>흐려 보입니다</b>",
    "아이콘 크기를 그대로 <b>누르는 자리</b>로 쓰기. 누르는 자리가 44px보다 작아집니다",
    "같은 줄에 <b>굵기가 다른</b> 아이콘 섞기",
    "아이콘만 두고 <b>이름을 붙이지 않기</b>. 스크린 리더로는 이 버튼이 무엇인지 알 수 없습니다",
  ]),
  instead='누르는 넓이는 <a href="touchtarget.html">터치 타깃</a>, 글자로 다루는 법은 <a href="iconfont.html">아이콘 글꼴</a>, 이름 붙이기는 <a href="name.html">이름 붙이기</a>.',
  cases=cases([
    (ic(20, "목록 20px", "", True), "목록", "목록 줄 높이에 맞춥니다"),
    (ic(24, "앱바 24px", "", True), "앱바", "글자 없이 아이콘만 놓이므로 <b>크게</b> 씁니다"),
    (ic(16, "버튼 속 16px", "", True), "버튼 속", "버튼 글자보다 <b>살짝 작게</b> 씁니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="아이콘 크기를 코드로 옮기는 법",
  code_lede="크기는 정해 둔 단에서 고르고, 선 굵기는 크기에 맞춰 원래대로 되돌립니다.",
  code='''<span class="c">/* 세 단이면 거의 모든 자리에 충분하다 */</span>
:root { --icon-1: <span class="a">16px</span>; --icon-2: <span class="a">20px</span>; --icon-3: <span class="a">24px</span>; }

<span class="c">/* 베이스라인에 놓이지 않게 해서 세로 가운데 어긋남을 없앤다 */</span>
svg { <span class="a">display</span>: block; }

<span class="c">/* 누르는 자리는 그림 크기와 따로 둔다 */</span>
.icon-btn { <span class="a">display</span>: grid; <span class="a">place-items</span>: center;
  <span class="a">min-width</span>: <span class="a">44px</span>; <span class="a">min-height</span>: <span class="a">44px</span>; }

&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"icon-btn"</span> <span class="a">aria-label</span>=<span class="s">"영수증 내려받기"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">width</span>=<span class="s">"20"</span> <span class="a">height</span>=<span class="s">"20"</span> <span class="a">viewBox</span>=<span class="s">"0 0 24 24"</span>
       <span class="a">stroke</span>=<span class="s">"currentColor"</span> <span class="a">stroke-width</span>=<span class="s">"1.8"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;''',
  keys=kbd([
    ("<code>aria-hidden=\"true\"</code>", "스크린 리더가 그림은 읽지 않게 하고, 이름은 <b>버튼 쪽에</b> 붙입니다"),
    ("<code>aria-label</code>", "아이콘만 있는 버튼에는 <b>반드시</b> 필요합니다"),
    ("<code>currentColor</code>", "호버나 비활성 상태에서 글자색이 바뀌면 아이콘 <b>색도 저절로</b> 바뀝니다"),
    ("<code>vector-effect</code>", "<code>non-scaling-stroke</code>를 주면 크기를 바꿔도 선 굵기가 그대로 유지됩니다"),
    ("1em", "아이콘이 글자 크기를 따라가게 하는 방법입니다. 다만 <b>줄 높이</b>와는 다른 값이니 주의합니다"),
    ("확인하는 법", "크기가 다른 두 아이콘을 <b>나란히 놓고</b> 선 굵기가 같아 보이는지 봅니다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "아이콘 파일은 화면 쪽에 두는 자산입니다. 다만 어떤 아이콘을 보여 줄지 가르는 <b>상태 이름</b>은 서버가 정합니다."),
    ("상태 이름", "서버가 <code>status: \"pending\"</code>처럼 상태 <b>이름</b>을 보내면 화면이 거기에 맞는 아이콘을 고릅니다. 아이콘 파일명을 직접 주고받지는 않습니다."),
  ]),
  plat_lede="<b>기본 단</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "16 · 20 · 24",
     ic(20, "20px", ""),
     "정해진 규격이 없어서, 보통 쓰고 있는 아이콘 묶음(Lucide · Heroicons)의 <b>viewBox 24</b>를 따릅니다."),
    ("iOS", "SF Symbols",
     '''              <div class="phone" role="img" aria-label="iOS 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:30px;width:13px;height:13px;border:1.2px solid var(--accent);border-radius:3px"></div>
                <div style="position:absolute;left:26px;right:6px;top:34px;height:6px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "아이콘을 글자와 <b>같은 방식</b>으로 다룹니다. 그래서 아이콘의 굵기와 크기가 본문 글꼴에 맞춰 저절로 정해집니다."),
    ("안드로이드", "24dp 기본",
     '''              <div class="phone" role="img" aria-label="안드로이드 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:28px;width:16px;height:16px;border:1.4px solid var(--accent);border-radius:3px"></div>
                <div style="position:absolute;left:30px;right:6px;top:34px;height:6px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "<b>24dp</b>가 기본 크기이고, 그 안에 20dp 그림이 들어가서 바깥쪽 2dp가 여백이 됩니다."),
  ]),
  plat_note="iOS의 <b>SF Symbols</b>는 아이콘을 글자처럼 다루기 때문에, 글자 크기를 키우면 아이콘도 함께 커지고 굵기도 글자에 맞춰집니다. 웹에는 그런 장치가 없어서 <b>단을 직접 정해</b> 두어야 합니다. 안드로이드의 <b>24dp 안에 20dp 그림</b>이라는 규칙은 웹에서도 쓸 만합니다. 아이콘 둘레에 여백을 넣어 두면 어느 자리에 놓아도 아이콘끼리 <b>같은 크기</b>로 보입니다.",
  siblings=siblings("iconsize"),
  related='''        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="iconfont.html"><b>아이콘 글꼴</b><em>3부</em></a></li>
        <li><a href="name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="typescale.html"><b>타입 스케일</b><em>2부</em></a></li>''',
)
