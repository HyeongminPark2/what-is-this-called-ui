# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 누르면 다른 곳으로 옮겨 간다는 점이 같습니다. 그래서 아래 네 가지를 물어보면 서로 구별할 수 있습니다."

def menu(open_i, cols, w="152px", note="", ok=None, heads=("의류", "생활용품", "식품")):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    hs = []
    for i, h in enumerate(heads):
        st = ('color:var(--accent);box-shadow:inset 0 -2px 0 var(--accent);' if i == open_i else 'color:var(--fg-muted);')
        hs.append('<span style="padding:4px 7px;font-size:8.5px;' + st + '">' + h + '</span>')
    panel = ''
    if cols:
        cs = []
        for title, items in cols:
            cs.append('<span style="display:grid;gap:2px;align-content:start">'
                      '<span style="font-size:7px;color:var(--fg-muted)">' + title + '</span>'
                      + ''.join('<span style="font-size:8px">' + x + '</span>' for x in items) + '</span>')
        panel = ('<span style="display:grid;grid-template-columns:repeat(' + str(len(cols)) +
                 ',1fr);gap:6px;padding:6px 7px;border-top:1px solid var(--line)">' + ''.join(cs) + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            '<span style="display:flex;gap:1px;border-bottom:1px solid var(--line)">' + ''.join(hs) + '</span>'
            + panel + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">머리글자 — 갈래 대여섯 개</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">패널 — 여러 단을 한 번에 펼친다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">열기 100ms · 닫기 300ms 늦추기</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">대각선 — 옆 머리글자를 스치면 바뀐다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">aria-expanded — 열렸는지 알린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">Esc 로 닫고 머리글자로 초점이 돌아온다</div>
                </div>
              </div>'''

D = dict(
  slug="megamenu", ko="메가 메뉴", en="Mega menu",
  desc="분류가 많은 사이트에서 쓰는 큰 드롭다운인 메가 메뉴를, 대각선 문제와 지연으로 해결하는 방법, 키보드 처리까지 함께 다루는 항목입니다.",
  lede="메가 메뉴는 분류가 <b>수십 개</b>인 사이트에서 여러 단의 항목을 한 번에 펼쳐 보여 주는 큰 메뉴입니다. 설계할 때는 항목 배치만큼 마우스가 지나가는 <b>경로</b>를 신경 써야 합니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>메가 메뉴에서 가장 자주 생기는 문제는 <b>대각선</b> 이동입니다. 머리글자에서 패널 오른쪽 아래 항목으로
          마우스를 곧장 옮기면 마우스가 <b>옆 머리글자 위를 지나가면서</b> 메뉴가 바뀌고, 가려던 항목이 사라집니다.
          데모는 이 경로를 따라 마우스를 움직여 보고 <b>가는 동안 메뉴가 몇 번 바뀌거나 닫혔는지</b> 셉니다.<br>
          <b>열기를 100ms, 닫기를 300ms 늦추면</b> 머리글자 위를 잠깐 지나가는 마우스로는 메뉴가 바뀌지 않고,
          머리글자와 패널 사이 빈틈을 잠깐 지나도 메뉴가 열린 채로 유지됩니다. <b>눌러야 열림</b>으로 두면
          마우스 이동과는 아예 상관이 없어지고, 키보드와 터치에서도 똑같이 동작합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "메가 메뉴, 대형 드롭다운, 전체 분류 메뉴"),
    ("영어", "mega menu, mega dropdown, flyout menu"),
    ("같이 쓰는 말",
     "마우스가 지나갈 만한 삼각형 영역을 미리 열어 두는 기법은 <b>의도 삼각형</b>(intent triangle), "
     "열고 닫기를 잠깐 늦추는 기법은 <b>호버 인텐트</b>(hover intent)라고 부릅니다. "
     "작고 항목이 한 줄로 늘어선 메뉴는 그냥 <b>드롭다운</b>, 옆으로 펼쳐지는 메뉴는 <b>플라이아웃</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>팝오버</b> — <a href=\"popover.html\">팝오버</a>는 특정 요소 <b>옆에 붙어</b> 뜨는 작은 판이고, 메가 메뉴는 화면 폭에 가깝게 펼쳐지는 큰 판입니다.<br>"
     "<b>셀렉트</b> — <a href=\"select.html\">셀렉트</a>는 <b>값을 고르는</b> 입력 부품이고, 다른 화면으로 가는 길 안내 부품이 아닙니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 화면 옆에 <b>늘 보이는</b> 메뉴이고, 메가 메뉴는 필요할 때만 펼쳐집니다."),
  ]),
  axes=ax("메가 메뉴"),
  oneline="대각선 문제는 열기 100ms, 닫기 300ms <b>두 가지 지연만으로 대부분 해결됩니다</b>. 그래도 해결되지 않으면 눌러야 열리게 하세요.",
  states=states([
    (menu(-1, None, "152px", "닫혀 있다", True), "닫힘", "머리글자만 보입니다"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠", "셔츠"]), ("하의", ["청바지"])], "152px", "한 갈래가 펼쳐졌다", True),
     "열림", "한 분류 안의 <b>여러 단을 한 번에</b> 보여 줍니다"),
    (menu(1, [("주방", ["냄비"]), ("욕실", ["수건"]), ("청소", ["세제"])], "152px", "옆으로 스쳐 바뀌었다", False),
     "대각선 사고", "옆 머리글자를 지나가면서 메뉴가 바뀌어 <b>가려던 항목이 사라집니다</b>"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "152px", "지연 덕에 안 바뀐다", True),
     "지연 켬", "옆 머리글자를 잠깐 지나가도 <b>메뉴가 바뀌지 않습니다</b>"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "152px", "눌러서 열었다 — 터치에서도 같다", True),
     "눌러야 열림", "마우스 이동과 상관없이 열리므로 <b>가장 안전합니다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">☰ 전체 분류</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">폰에서는 드로어로 바꾼다</span>'),
         "폰", True, "", "152px"),
     "폰", "폰 화면에는 메가 메뉴를 펼칠 <b>자리가 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("머리글자", "대여섯 개", "이보다 많으면 <b>머리글자 줄부터</b> 한 줄에 다 들어가지 않습니다"),
    ("패널", "여러 단", "한 분류 안의 항목을 <b>한 번에</b> 보여 줍니다"),
    ("지연", "100 / 300ms", "대각선 문제를 <b>가장 적은 품으로</b> 고치는 방법입니다"),
    ("대각선", "스치면 바뀜", "마우스가 목표 항목까지 <b>직선으로 움직이는 것</b>이 원인입니다"),
    ("<code>aria-expanded</code>", "열렸는지", "메뉴가 열렸는지를 스크린 리더에도 알립니다"),
    ("Esc", "닫고 돌아오기", "메뉴를 닫고 포커스를 <b>머리글자</b>로 되돌립니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          호버로 여는 메뉴는 따로 챙겨야 할 것이 생깁니다.
          <b>터치 화면과 키보드에는 호버가 없기</b> 때문입니다.
          그래서 호버로 열더라도 <b>누르면 열리는 방법</b>을 반드시 함께 둬야 하는데,
          누르면 열리는 방법이 있으면 호버는 사실상 보조 수단이 됩니다.<br>
          <a href="hover.html">호버가 없는 환경</a>에서는 머리글자를 처음 탭하면 메뉴가 열리고
          두 번째 탭에서야 그 분류 화면으로 들어가는데, 이렇게 하면 <b>머리글자가 가리키는 분류 화면으로 바로 갈 방법</b>이 없어집니다.
          패널 안에 <b>'의류 전체 보기'</b> 같은 줄을 하나 두면 그 화면으로 갈 수 있습니다.</p>''',
  do=ul([
    "<b>열기는 100ms, 닫기는 300ms</b> 늦출 때",
    "패널 안에 <b>'○○ 전체 보기'</b> 줄을 둘 때",
    "폰에서는 <a href=\"drawer.html\">드로어</a>나 <b>한 단씩 들어가는</b> 화면으로 바꿀 때",
  ]),
  dont=ul([
    "마우스가 닿자마자 열고 벗어나자마자 닫을 때. <b>대각선으로 움직이면 메뉴가 바뀌거나 닫힙니다</b>",
    "호버로만 열 때. <b>터치 화면과 키보드</b>에서는 메뉴를 열 수 없습니다",
    "머리글자를 <b>여덟 개</b> 넘게 둘 때",
    "패널이 <b>화면 밖까지</b> 넘어갈 때. 오른쪽 끝 분류가 잘립니다",
  ]),
  instead='작게 뜨면 <a href="popover.html">팝오버</a>, 늘 보이면 <a href="sidebar.html">사이드바</a>, 폰에서는 <a href="drawer.html">드로어</a>, 찾기가 목적이면 <a href="search.html">검색</a>.',
  cases=cases([
    (menu(0, [("아우터", ["패딩"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "150px", "", True),
     "쇼핑몰", "분류가 많아서 메가 메뉴를 <b>가장 많이 쓰는 곳</b>입니다"),
    (menu(0, [("제품", ["요금제"]), ("문서", ["시작하기"]), ("회사", ["채용"])], "150px", "", True),
     "기업 사이트", "분류 수가 적어도 <b>깊이</b>가 있으면 씁니다"),
    (one(txt('<span style="display:block;font-size:8.5px">☰ 전체 분류</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">의류 ›</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted)">생활용품 ›</span>'),
         "폰", True, "드로어로 바꾼다", "150px"),
     "폰", "폰에서는 <b>드로어</b>가 메가 메뉴를 대신합니다"),
  ]),
  code_lede="호버로 열더라도 <b>누르면 열리는 방법</b>을 함께 둡니다. 그래서 머리글자는 <code>&lt;button&gt;</code>으로 만듭니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"전체 분류"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"m-wear"</span>&gt;의류&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"m-wear"</span> <span class="a">hidden</span>&gt;
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wear"</span>&gt;의류 전체 보기&lt;/<span class="t">a</span>&gt;
    …
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">// 잠깐 지나가는 마우스로는 열지 않고, 잠깐 벗어나도 닫지 않는다</span>
<span class="t">let</span> openT, closeT;
bar.addEventListener(<span class="s">'pointerover'</span>, e =&gt; {
  clearTimeout(closeT);
  clearTimeout(openT);                       <span class="c">// 머리글자를 벗어나면 예약 취소</span>
  <span class="t">const</span> b = e.target.closest(<span class="s">'button'</span>);
  <span class="t">if</span> (b) openT = setTimeout(() =&gt; open(b), <span class="a">100</span>);
});
nav.addEventListener(<span class="s">'pointerleave'</span>, () =&gt; {
  closeT = setTimeout(closeAll, <span class="a">300</span>);
});''',
  keys=kbd([
    ("Tab", "머리글자를 하나씩 지나가고, 메뉴가 <b>열려 있으면</b> 패널 안으로 들어갑니다"),
    ("Enter · Space", "눌러서 메뉴를 엽니다. <b>호버 없이도</b> 메뉴를 여는 방법입니다"),
    ("← →", "머리글자 사이를 옮겨 다닙니다(<code>role=\"menubar\"</code>를 쓸 때)"),
    ("Esc", "메뉴를 닫고 포커스를 <b>머리글자로</b> 되돌립니다"),
    ("<code>aria-expanded</code>", "메뉴가 열렸는지 알리며, <b>머리글자 쪽에</b> 붙입니다"),
    ("확인하는 법", "마우스를 쓰지 않고 <b><kbd>Tab</kbd>만으로</b> 셋째 분류의 넷째 항목까지 가 봅니다"),
  ]),
  backend=rows([
    ("분류는 한 번에", "메뉴에 쓰는 분류는 거의 바뀌지 않으므로 <b>한 번 받아서 캐시</b>해 둡니다. 머리글자에 마우스를 올릴 때마다 요청하면 메뉴가 늦게 열립니다."),
    ("깊이를 미리 줄여", "메가 메뉴는 보통 <b>두 단</b>까지만 펼칩니다. 서버가 세 단까지 내려 주면 화면에서 셋째 단을 따로 접어야 하므로, 서버에서 미리 두 단으로 줄여 보냅니다."),
    ("인기 갈래", "분류별 클릭 수 데이터가 있으면 많이 찾는 분류를 <b>맨 앞 칸</b>에 올릴 수 있습니다. 데이터가 없으면 미리 정해 둔 순서대로 보여 줍니다."),
  ]),
  plat_lede="메가 메뉴는 <b>데스크톱 웹에서 쓰는 부품</b>이라서 모바일 지침에서는 다루지 않습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     menu(0, [("아우터", ["패딩"]), ("상의", ["티셔츠"])], "110px", "", True),
     "정해진 부품이 없어서 지연과 키보드 동작을 <b>모두 직접</b> 구현합니다."),
    ("iOS", "없다 — 드릴다운",
     '''              <div class="phone" role="img" aria-label="iOS 한 단씩 들어가는 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:41px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:30px;font-size:5px;color:var(--fg-muted)">›</div></div></div>''',
     "한 단씩 <b>새 화면으로 넘어가며</b> 들어갑니다. 앞 화면으로는 ‹ 버튼으로 돌아옵니다."),
    ("안드로이드", "없다 — 드로어",
     '''              <div class="phone" role="img" aria-label="안드로이드 드로어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;top:20px;bottom:0;width:30px;background:var(--surface);border-right:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;top:28px;width:24px;height:6px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:3px;top:38px;width:24px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>내비게이션 드로어</b>가 같은 역할을 합니다. 하위 분류는 접었다 펼 수 있게 둡니다."),
  ]),
  plat_note="폰에서 메가 메뉴를 쓰지 않는 것은 <b>호버가 없고 화면이 좁기</b> 때문입니다. 이런 조건에서 같은 정보를 보여 주려면 <b>한 단씩 들어가는</b> 방법밖에 없어서 iOS와 안드로이드 모두 이 방식을 씁니다. 웹에서도 폰 폭에서는 메가 메뉴 전체를 접고 <a href=\"drawer.html\">드로어</a>로 바꾸는 것이 맞습니다. 메가 메뉴를 작게 줄여 폰 화면에 넣으려 하면 <b>메가 메뉴로도 드로어로도 제대로 쓸 수 없게</b> 됩니다.",
  siblings=siblings("megamenu"),
  related='''        <li><a href="popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><a href="hover.html"><b>호버가 없는 세계</b><em>11부</em></a></li>
        <li><a href="appbar.html"><b>앱바</b><em>7부</em></a></li>''',
)
