# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 '누르면 어디론가 간다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
  desc="갈래가 많은 사이트의 큰 드롭다운. 대각선 문제와 지연으로 푸는 법, 키보드 처리.",
  lede="갈래가 <b>수십 개</b>인 사이트에서 한 번에 펼쳐 보여 주는 큰 메뉴입니다. 손이 지나가는 <b>길</b>이 설계의 절반입니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>메가 메뉴의 고질병은 <b>대각선</b>입니다 — 머리글자에서 패널 오른쪽 아래 항목으로
          곧장 가면 손이 <b>옆 머리글자 위를 스쳐</b> 메뉴가 바뀌고, 가려던 항목이 사라집니다.
          데모가 그 경로를 흉내 내 <b>가는 길에 몇 번 끊겼는지</b> 셉니다.<br>
          <b>열기를 100ms 늦추고 닫기를 300ms 늦추면</b> 스쳐 지나가는 손은 메뉴를 못 바꾸고,
          잠깐 빈틈을 지나도 열린 채로 버팁니다. <b>눌러야 열림</b>으로 두면
          지나가는 손과 아예 상관이 없고 키보드·터치에서도 같게 동작합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "메가 메뉴, 대형 드롭다운, 전체 분류 메뉴"),
    ("영어", "mega menu, mega dropdown, flyout menu"),
    ("같이 쓰는 말",
     "손이 지나갈 만한 세모 모양을 미리 열어 두는 기법을 <b>의도 삼각형</b>(intent triangle), "
     "열고 닫기를 늦추는 것을 <b>호버 인텐트</b>(hover intent)라 부릅니다. "
     "작고 한 줄짜리는 그냥 <b>드롭다운</b>, 옆으로 펼쳐지는 것은 <b>플라이아웃</b>입니다."),
    ("자주 잘못 부름",
     "<b>팝오버</b> — <a href=\"popover.html\">팝오버</a>는 <b>어딘가에 붙어</b> 뜨는 작은 판입니다.<br>"
     "<b>셀렉트</b> — <a href=\"select.html\">셀렉트</a>는 <b>값을 고르는</b> 것이지 길 안내가 아닙니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 늘 보이는 <b>자리</b>입니다."),
  ]),
  axes=ax("메가 메뉴"),
  oneline="<b>지연 두 개로 거의 다 고쳐집니다</b> — 열기 100ms, 닫기 300ms. 안 되면 눌러야 열리게 하세요.",
  states=states([
    (menu(-1, None, "152px", "닫혀 있다", True), "닫힘", "머리글자만 보인다"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠", "셔츠"]), ("하의", ["청바지"])], "152px", "한 갈래가 펼쳐졌다", True),
     "열림", "<b>여러 단을 한 번에</b>"),
    (menu(1, [("주방", ["냄비"]), ("욕실", ["수건"]), ("청소", ["세제"])], "152px", "옆으로 스쳐 바뀌었다", False),
     "대각선 사고", "<b>가려던 항목이 사라진다</b>"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "152px", "지연 덕에 안 바뀐다", True),
     "지연 켬", "스쳐도 <b>버틴다</b>"),
    (menu(0, [("아우터", ["패딩", "코트"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "152px", "눌러서 열었다 — 터치에서도 같다", True),
     "눌러야 열림", "<b>가장 안전하다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">☰ 전체 분류</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">폰에서는 드로어로 바꾼다</span>'),
         "폰", True, "", "152px"),
     "폰", "메가 메뉴가 <b>설 자리가 없다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("머리글자", "대여섯 개", "더 늘면 <b>머리줄이 먼저</b> 무너진다"),
    ("패널", "여러 단", "갈래 안을 <b>한 번에</b> 보인다"),
    ("지연", "100 / 300ms", "<b>가장 싼 수리</b>"),
    ("대각선", "스치면 바뀜", "손의 <b>직선 경로</b>가 원인"),
    ("<code>aria-expanded</code>", "열렸는지", "소리로도 알린다"),
    ("Esc", "닫고 돌아오기", "초점이 <b>머리글자</b>로"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          호버로 여는 메뉴에는 공짜가 없습니다 —
          <b>터치에는 호버가 없고</b>, 키보드에도 없습니다.
          그래서 호버로 열더라도 <b>누르면 열리는 길</b>을 반드시 같이 둬야 하고,
          그 길이 있으면 사실 호버는 덤입니다.<br>
          <a href="hover.html">호버가 없는 세계</a>에서는 첫 탭이 '열기'가 되고
          두 번째 탭이 '들어가기'가 되는데, 그러면 <b>머리글자 자체로 가는 길</b>이 막힙니다.
          패널 안에 <b>'의류 전체 보기'</b> 같은 줄을 하나 두면 그 길이 살아납니다.</p>''',
  do=ul([
    "<b>열기 100ms · 닫기 300ms</b> 늦추기",
    "패널 안에 <b>'○○ 전체 보기'</b> 줄 두기",
    "폰에서는 <a href=\"drawer.html\">드로어</a>나 <b>한 단씩 들어가는</b> 화면으로 바꾸기",
  ]),
  dont=ul([
    "닿자마자 열고 떠나자마자 닫기 — <b>대각선에서 끊긴다</b>",
    "호버로만 열기 — <b>터치·키보드</b>에서 못 쓴다",
    "머리글자를 <b>여덟 개</b> 넘게 두기",
    "패널을 <b>화면 밖까지</b> 늘리기 — 오른쪽 끝 갈래가 잘린다",
  ]),
  instead='작게 뜨면 <a href="popover.html">팝오버</a>, 늘 보이면 <a href="sidebar.html">사이드바</a>, 폰에서는 <a href="drawer.html">드로어</a>, 찾기가 목적이면 <a href="search.html">검색</a>.',
  cases=cases([
    (menu(0, [("아우터", ["패딩"]), ("상의", ["티셔츠"]), ("하의", ["청바지"])], "150px", "", True),
     "쇼핑몰", "갈래가 많은 <b>대표 자리</b>"),
    (menu(0, [("제품", ["요금제"]), ("문서", ["시작하기"]), ("회사", ["채용"])], "150px", "", True),
     "기업 사이트", "갈래가 적어도 <b>깊이</b>가 있으면"),
    (one(txt('<span style="display:block;font-size:8.5px">☰ 전체 분류</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">의류 ›</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted)">생활용품 ›</span>'),
         "폰", True, "드로어로 바꾼다", "150px"),
     "폰", "<b>드로어</b>가 대신한다"),
  ]),
  code_lede="호버로 열더라도 <b>누르면 열리는 길</b>을 같이 둡니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"전체 분류"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"m-wear"</span>&gt;의류&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"m-wear"</span> <span class="a">hidden</span>&gt;
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/wear"</span>&gt;의류 전체 보기&lt;/<span class="t">a</span>&gt;
    …
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">// 스쳐 가는 손은 열지 않고, 잠깐 벗어나도 안 닫는다</span>
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
    ("Tab", "머리글자를 하나씩 지나간다. <b>열려 있으면</b> 패널 안으로 들어간다"),
    ("Enter · Space", "눌러서 연다 — <b>호버 없이도</b> 되는 길"),
    ("← →", "머리글자 사이를 옮긴다 (<code>role=\"menubar\"</code> 를 쓸 때)"),
    ("Esc", "닫고 초점을 <b>머리글자로</b> 되돌린다"),
    ("<code>aria-expanded</code>", "열렸는지. <b>머리글자 쪽에</b> 붙인다"),
    ("확인하는 법", "마우스를 안 쓰고 <b>Tab 만으로</b> 셋째 갈래의 넷째 항목까지 가 본다"),
  ]),
  backend=rows([
    ("분류는 한 번에", "메뉴에 쓰는 분류는 거의 안 바뀌니 <b>한 번 받아 캐시</b>합니다. 머리글자마다 요청하면 지연이 커집니다."),
    ("깊이를 미리 줄여", "메가 메뉴는 보통 <b>두 단</b>까지만 폅니다 — 서버가 세 단을 주면 화면이 접어야 합니다."),
    ("인기 갈래", "클릭 수가 있으면 <b>맨 앞 칸</b>에 올릴 수 있습니다 — 없으면 정해 둔 차례대로입니다."),
  ]),
  plat_lede="<b>데스크톱 웹의 부품</b>입니다. 모바일 지침에는 자리가 없습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     menu(0, [("아우터", ["패딩"]), ("상의", ["티셔츠"])], "110px", "", True),
     "정해진 부품이 없습니다. 지연과 키보드를 <b>전부 손으로</b> 붙입니다."),
    ("iOS", "없다 — 드릴다운",
     '''              <div class="phone" role="img" aria-label="iOS 한 단씩 들어가는 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:41px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:30px;font-size:5px;color:var(--fg-muted)">›</div></div></div>''',
     "한 단씩 <b>화면을 갈아 가며</b> 들어갑니다. 돌아오는 길은 ‹ 입니다."),
    ("안드로이드", "없다 — 드로어",
     '''              <div class="phone" role="img" aria-label="안드로이드 드로어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;top:20px;bottom:0;width:30px;background:var(--surface);border-right:1px solid var(--line)"></div>
                <div style="position:absolute;left:3px;top:28px;width:24px;height:6px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:3px;top:38px;width:24px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>내비게이션 드로어</b>가 같은 자리입니다. 하위 갈래는 접었다 펴는 꼴로 둡니다."),
  ]),
  plat_note="메가 메뉴가 폰에 없는 것은 <b>호버가 없고 화면이 좁아서</b>입니다. 둘 다 없는 조건에서 같은 정보를 보이려면 <b>한 단씩 들어가는</b> 수밖에 없고, 그래서 iOS·안드로이드 모두 그 길을 씁니다. 웹에서도 폰 폭에서는 메가 메뉴를 통째로 접고 <a href=\"drawer.html\">드로어</a>로 바꾸는 것이 맞습니다 — 작게 줄여 넣으려 하면 <b>둘 다 못 쓰게</b> 됩니다.",
  siblings=siblings("megamenu"),
  related='''        <li><a href="popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><a href="hover.html"><b>호버가 없는 세계</b><em>11부</em></a></li>
        <li><a href="appbar.html"><b>앱바</b><em>7부</em></a></li>''',
)
