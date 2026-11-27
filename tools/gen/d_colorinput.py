# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sw(hexv, note="", ok=None, label="흰 글자", w="150px", preset=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    pre = ''
    if preset:
        pre = ('<span style="display:flex;gap:3px;margin-top:3px">'
               + ''.join('<span style="width:13px;height:13px;border-radius:3px;background:' + h
                         + ';border:1px solid rgba(0,0,0,.14)"></span>'
                         for h in ['#1f6feb', '#1a7f37', '#9a6700', '#cf222e', '#8250df', '#0e7490'])
               + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:flex;gap:5px;align-items:center;border:1px solid ' + c + ';'
            'border-radius:4px;background:var(--surface);padding:4px 6px">'
            '<span style="width:15px;height:15px;border-radius:3px;background:' + hexv + ';'
            'border:1px solid rgba(0,0,0,.14);flex:0 0 auto"></span>'
            '<span style="font-family:var(--mono);font-size:8px;color:var(--fg-muted)">' + hexv + '</span></span>'
            + pre +
            '<span style="display:block;border-radius:3px;background:' + hexv + ';color:#fff;'
            'font-size:7.5px;padding:3px 5px;text-align:center">' + label + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">견본 — 고른 색을 그대로 보여 준다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">색 코드 칸 — 디자이너가 주는 값을 받는다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">정해 둔 색 — 가짓수를 줄여 사고를 막는다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">아무 색 — 대비비가 모자란 색이 들어온다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">미리보기 — 글자를 올려 봐야 안다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">색 이름 — 색맹에게는 이름이 전부다</div>
                </div>
              </div>'''

D = dict(
  slug="colorinput", ko="색 고르기", en="Color input",
  desc="색을 고르는 칸에서 아무 색이나 고르게 두면 글자를 읽을 수 없는 색이 들어오는 문제를 다루는 항목입니다.",
  lede="견본만 보고 고른 색은 <b>고른 사람 눈에는</b> 괜찮아 보여도, 그 위에 글자를 올려 보기 전에는 실제로 쓸 수 있는 색인지 알 수 없습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모에서 <b>노랑</b>이나 <b>연두</b>를 골라 보세요.
          데모가 그 색 위에 올린 흰 글자의 <b>대비비</b>를 재서, 4.5:1보다 낮으면 고르지 못하게 막습니다.
          '아무 색이나 고르기'로 바꾸면 고를 수 있는 색이 <b>천육백만 가지</b>로 늘어나는데,
          그중 대부분은 흰 글자를 올리면 읽기 어려운 색입니다.<br>
          <b>정해 둔 색</b>만 보이게 하면 가짓수가 <b>여섯</b>으로 줄고,
          모두 대비비를 미리 재 둔 색이라서 읽을 수 없는 색이 들어올 일이 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "색 고르기, 색상 선택기, 컬러 피커"),
    ("영어", "color input, color picker, swatch picker"),
    ("같이 쓰는 말",
     "색 하나를 보여 주는 작은 네모는 <b>스와치</b>(swatch), 미리 정해 둔 색 묶음은 <b>팔레트</b>라고 합니다. "
     "여러 색이 번진 사각형 안을 끌어 고르는 꼴은 <b>색 공간 선택기</b>, "
     "<code>#1f6feb</code> 같은 값은 <b>헥스 코드</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>테마</b> — 테마는 색 하나가 아니라 <a href=\"dark.html\">다크 모드</a>처럼 색의 묶음을 고르는 것입니다.<br>"
     "<b>색 토큰</b> — <a href=\"tokenname.html\">토큰 이름</a>은 색을 고르는 일이 아니라 색에 <b>이름을 붙이는</b> 일입니다.<br>"
     "<b>상태 색</b> — <a href=\"statecolor.html\">상태 색</a>은 사용자가 고르는 색이 아니라 뜻이 정해진 색입니다."),
  ]),
  axes=ax("색 고르기"),
  oneline="<b>정해 둔 색에서 고르게 하세요.</b> 아무 색이나 고를 수 있게 열어 두면 글자를 읽을 수 없는 색이 들어옵니다.",
  states=states([
    (sw("#1f6feb", "대비비 4.7:1 — 쓸 수 있다", True), "괜찮은 색", "흰 글자를 올려도 <b>잘 읽힙니다</b>"),
    (sw("#f2d024", "대비비 1.6:1 — 못 읽는다", False), "밝은 색", "흰 글자를 읽을 수 없으므로 <b>막아야</b> 합니다"),
    (sw("#1f6feb", "여섯 가지만", True, "흰 글자", "150px", True), "정해 둔 색", "대비비를 미리 재 둔 색만 있어서 <b>읽을 수 없는 색이 들어오지 않습니다</b>"),
    (sw("#8250df", "코드로 쳐서 넣었다", True), "코드 입력", "디자이너가 <b>건네는 색 코드</b>를 그대로 넣습니다"),
    (sw("#cf222e", "뜻이 정해진 색이다", None), "상태 색", "뜻이 정해진 색이라 <b>바꾸면 안 됩니다</b>"),
    (sw("#0e7490", "색 이름이 없다", None, "이름 없음"), "이름 없음", "색 이름이 없으면 스크린 리더로 무슨 색인지 <b>들을 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("견본", "고른 색", "고른 색을 눈으로 <b>확인</b>합니다"),
    ("코드 칸", "#1f6feb", "색 코드를 <b>쳐서</b>도 넣을 수 있습니다"),
    ("정해 둔 색", "여섯 가지", "대비비를 <b>미리 재 둔</b> 색입니다"),
    ("아무 색", "천육백만", "고를 수 있는 색 가운데 대부분은 글자 배경으로 <b>쓸 수 없습니다</b>"),
    ("미리보기", "글자를 얹어", "글자를 <b>올려 보기 전에는</b> 쓸 수 있는 색인지 알 수 없습니다"),
    ("색 이름", "소리로", "색맹인 사람은 <b>이름</b>으로만 색을 구별할 수 있습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          색을 고르게 하는 화면을 만들 때는 먼저 <b>이 색 위에 글자가 올라가는지</b> 따져 봐야 합니다.
          글자가 올라간다면 대비비를 재서 읽기 어려운 색을 막아야 하고,
          막대 그래프의 색처럼 글자가 올라가지 않는다면 훨씬 자유롭게 고르게 해도 됩니다.<br>
          색을 고르는 자리에 <b>색 이름</b>을 같이 두면
          색맹인 사람도 무엇을 골랐는지 알 수 있습니다.
          견본 옆에 '파랑' 같은 이름을 적어 두기만 하면 됩니다.</p>''',
  do=ul([
    "<b>정해 둔 색</b>에서 고르게 하기",
    "고른 색 위에 <b>글자를 올려</b> 보여 주기",
    "<b>색 코드</b>를 쳐서도 넣을 수 있게 하기",
    "색마다 <b>이름</b> 적어 두기",
  ]),
  dont=ul([
    "아무 색이나 고를 수 있게 열어 두기. 글자를 <b>읽을 수 없는 색</b>이 들어옵니다",
    "고른 색의 <b>대비비를 재지 않기</b>",
    "견본만 두고 색 <b>이름을 적지 않기</b>",
    "<a href=\"statecolor.html\">상태 색</a>까지 고치게 하기. 빨강 같은 색이 원래 가진 <b>뜻이 흐려집니다</b>",
  ]),
  instead='색에 이름을 붙이는 일은 <a href="tokenname.html">토큰 이름</a>, 뜻이 정해진 색은 <a href="statecolor.html">상태 색</a>, 밝은 화면과 어두운 화면의 색 짝은 <a href="dark.html">다크 모드</a>, 글자가 읽히는지 따지는 일은 <a href="contrast.html">명도 대비</a>.',
  cases=cases([
    (sw("#1f6feb", "", True, "흰 글자", "148px", True), "브랜드 색", "<b>정해 둔 색</b>에서 고르게 합니다"),
    (sw("#8250df", "", True, "라벨", "148px"), "꼬리표 색", "색 위에 <b>글자가 올라가므로</b> 대비비를 따져야 합니다"),
    (sw("#0e7490", "", None, "그래프", "148px"), "그래프 색", "색 위에 글자가 <b>올라가지 않아서</b> 비교적 자유롭게 골라도 됩니다"),
  ]),
  code_lede="<code>&lt;input type=\"color\"&gt;</code>는 아무 색이나 고를 수 있게 열어 둡니다. 그래서 정해 둔 색에서 고르게 할 때는 라디오 그룹으로 만듭니다.",
  code='''<span class="c">&lt;!-- 정해 둔 색은 라디오 그룹으로 만든다 --&gt;</span>
&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;브랜드 색&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"brand"</span> <span class="a">value</span>=<span class="s">"#1f6feb"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"sw"</span> <span class="a">style</span>=<span class="s">"background:#1f6feb"</span>&gt;&lt;/<span class="t">span</span>&gt; 파랑&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

<span class="c">&lt;!-- 아무 색이나 고르게 할 때는 코드 칸을 같이 둔다 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"color"</span> <span class="a">aria-label</span>=<span class="s">"색 고르기"</span>&gt;
&lt;<span class="t">input</span> <span class="a">aria-label</span>=<span class="s">"색 코드"</span> <span class="a">placeholder</span>=<span class="s">"#1f6feb"</span>&gt;
&lt;<span class="t">p</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;흰 글자 대비비 4.7:1&lt;/<span class="t">p</span>&gt;''',
  keys=kbd([
    ("정해 둔 색", "<b>라디오 그룹</b>이라서 ↑↓←→로 옮깁니다"),
    ("<code>type=color</code>", "브라우저가 자체 창을 띄우는데, 그 창의 <b>키보드 동작은 브라우저마다 다릅니다</b>"),
    ("색 이름", "견본 옆에 <b>글자로</b> 적습니다. 스크린 리더는 색 자체를 읽어 주지 못합니다"),
    ("<code>aria-live</code>", "대비비가 바뀌면 바뀐 값을 <b>읽어</b> 줍니다"),
    ("확인하는 법", "화면을 <b>흑백</b>으로 바꾸고 무엇을 골랐는지 알 수 있는지 확인합니다"),
  ]),
  backend=rows([
    ("저장은 코드로", "색은 <code>\"#1f6feb\"</code>처럼 <b>헥스 코드</b>로 저장하고, '파랑' 같은 이름은 화면에서 붙입니다."),
    ("정해 둔 색이면", "정해 둔 색에서 고르게 했다면 <code>\"brand.blue\"</code> 같은 <b>키</b>로 저장해 두어야 나중에 색 값을 바꿀 수 있습니다."),
    ("검사", "서버에서도 값이 <b>헥스 코드 형식인지</b> 확인합니다. <code>javascript:</code> 같은 값이 그대로 CSS에 들어가면 안 되기 때문입니다."),
  ]),
  plat_lede="플랫폼이 기본으로 주는 부품은 모두 <b>아무 색이나</b> 고르게 하는 쪽입니다.",
  plats=plats([
    ("웹", "type=color",
     sw("#1f6feb", "", True, "흰 글자", "108px"),
     "색을 고르는 <b>창 모양이 브라우저마다 다르므로</b>, 코드 칸을 같이 두는 편이 낫습니다."),
    ("iOS", "UIColorPickerVC",
     '''              <div class="phone" role="img" aria-label="iOS 색 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:22px;height:26px;border-radius:5px;background:linear-gradient(90deg,#cf222e,#9a6700,#1a7f37,#1f6feb,#8250df)"></div>
                <div style="position:absolute;left:6px;top:54px;width:14px;height:14px;border-radius:4px;background:#1f6feb;border:1.5px solid var(--surface)"></div></div></div>''',
     "<b>UIColorPickerViewController</b>가 화면 전체를 덮는 창으로 뜹니다."),
    ("안드로이드", "없다 — 직접",
     '''              <div class="phone" role="img" aria-label="안드로이드 색 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;display:flex;gap:4px;flex-wrap:wrap">
                  <span style="width:13px;height:13px;border-radius:4px;background:#1f6feb"></span>
                  <span style="width:13px;height:13px;border-radius:4px;background:#1a7f37"></span>
                  <span style="width:13px;height:13px;border-radius:4px;background:#9a6700"></span>
                  <span style="width:13px;height:13px;border-radius:4px;background:#cf222e"></span></div></div></div>''',
     "Material에는 색 고르기 부품이 <b>없어서</b>, 대부분 <b>정해 둔 색</b>을 격자로 늘어놓습니다."),
  ]),
  plat_note="안드로이드에 색 고르기 기본 부품이 없는 것은 그만큼 <b>아무 색이나 골라야 하는 자리가 드물기</b> 때문입니다. 색을 고르는 칸을 만들기 전에 <b>사용자가 정말 색을 직접 골라야 하는지</b>부터 따져 보세요. 대개는 <b>미리 골라 둔 여섯 색</b>으로 충분하고, 그렇게 하면 대비비가 모자란 색이 들어오는 문제도 함께 없어집니다.",
  siblings=siblings("colorinput"),
  related='''        <li><a href="contrast.html"><b>명도 대비</b><em>12부</em></a></li>
        <li><a href="statecolor.html"><b>상태 색</b><em>12부</em></a></li>
        <li><a href="tokenname.html"><b>토큰 이름</b><em>12부</em></a></li>
        <li><a href="radio.html"><b>라디오 그룹</b><em>4부</em></a></li>''',
)
