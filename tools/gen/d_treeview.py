# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 누르면 다른 곳으로 옮겨 갑니다. 아래 네 가지로 서로 가릅니다."

def tree(items, w="152px", note="", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for depth, tw, name, sel in items:
        bg = 'background:var(--accent-soft);' if sel else ''
        clr = 'color:var(--danger);' if name.endswith('…') else ''
        out.append('<span style="display:flex;align-items:center;gap:4px;padding:2px 4px;border-radius:3px;'
                   + bg + 'margin-left:' + str(depth * 12) + 'px">'
                   '<span style="width:8px;font-size:7px;color:var(--fg-muted)">' + tw + '</span>'
                   '<span style="font-size:8.5px;' + clr + 'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'
                   + name + '</span></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:1px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">role="tree"로 트리임을 알림</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">treeitem과 aria-level로 몇 단인지 알림</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-expanded로 펼침 여부를 알림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">꺾쇠(▸ ▾)는 자식이 있다는 표시</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">들여쓰기가 깊어질수록 <b>이름 자리가 줄어듦</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">tabindex는 하나만 0, 나머지는 -1</div>
                </div>
              </div>'''

D = dict(
  slug="treeview", ko="트리뷰", en="Tree view",
  desc="계층을 펴고 접으며 옮겨 다니는 트리뷰를, 깊이 제한과 화살표 키 조작, 들여쓰기가 차지하는 폭까지 함께 다루는 항목입니다.",
  lede="트리뷰는 폴더와 파일처럼 <b>부모와 자식</b> 관계가 있는 항목들을 가지 단위로 펴고 접으며 찾아가는 부품입니다. 깊이가 <b>세 단</b>을 넘으면 다른 길 안내 방식을 쓰는 편이 낫습니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>트리는 깊어질수록 <b>들여쓰기가 가로 폭을 많이 차지합니다</b>. 데모는 가장 깊은 줄에서
          이름을 적을 자리가 얼마나 남았는지 재서 보여 줍니다. 들여쓰기를 키우거나 가지를 더 펼치면 이름부터 잘립니다.<br>
          스크린 리더에서도 트리는 <b>목록이 아니라 트리로 읽혀야</b> 하므로 <code>role="tree"</code>,
          <code>treeitem</code>, <code>aria-expanded</code>를 쓰고 화살표 키로 가지를 펴게 합니다.
          '키보드로 훑어보기'를 누르면 ↓ 키로 내려가면서 지나간 줄이 차례대로 적힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "트리뷰, 트리, 폴더 트리, 계층 목록"),
    ("영어", "tree view, tree, file tree, hierarchy navigation"),
    ("같이 쓰는 말",
     "가지를 펴고 접는 꺾쇠는 <b>디스클로저</b>(disclosure triangle), "
     "자식이 없는 끝 가지는 <b>잎</b>(leaf)이라고 부릅니다. "
     "여러 항목을 고를 수 있게 체크박스를 붙인 것은 <b>체크박스 트리</b>이고, "
     "한 번에 한 가지만 펼쳐지는 것은 <b>아코디언 트리</b>라고 부르기도 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>아코디언</b> — 아코디언은 펼치면 <b>내용</b>이 나오고, 트리는 펼치면 그 아래 <b>하위 항목</b>이 나옵니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 화면 옆이라는 <b>자리</b>를 가리키는 이름이고, 그 안에 트리가 들어가기도 합니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 지금 위치까지 이어진 <b>한 줄기만</b> 보여 주고, 트리는 여러 가지를 함께 보여 줍니다."),
  ]),
  axes=ax("트리뷰"),
  oneline="<b>깊이가 세 단, 가지가 스무 개</b>를 넘으면 트리만으로는 원하는 항목을 찾기 어려우므로 검색을 함께 붙입니다.",
  states=states([
    (tree([(0, "▸", "의류", False), (0, "▸", "생활용품", False), (0, "▸", "식품", False)], "152px", "모두 접힘", True),
     "모두 접혀 있을 때", "최상위 가지만 보여서 <b>한눈에</b> 전체 구성이 보입니다"),
    (tree([(0, "▾", "의류", False), (1, "▸", "아우터", True), (1, "▸", "상의", False), (0, "▸", "생활용품", False)], "152px", "한 가지만 폄", True),
     "한 가지만 펼쳤을 때", "지금 보고 있는 가지만 펼쳐 둡니다"),
    (tree([(0, "▾", "의류", False), (1, "▾", "상의", False), (2, "▾", "티셔츠", False), (3, "", "반팔 티…", False)], "152px", "이름이 잘림", False),
     "너무 깊이 펼쳤을 때", "<b>들여쓰기가</b> 폭을 차지해서 이름이 잘립니다"),
    (tree([(0, "▾", "의류", False), (1, "▸", "아우터", False), (1, "▸", "상의", True), (1, "▸", "하의", False)], "152px", "고른 줄이 밝음", True),
     "한 줄을 골랐을 때", "고른 줄은 배경을 밝히고 <code>aria-selected</code>로 알립니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">⌨ ↓ ↑ 로 오르내리고</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted)">→로 펴고 ←로 접음</span>'),
         "키보드", True, "Tab은 트리 전체에서 한 번만 멈춤", "152px"),
     "키보드로 움직일 때", "트리 안에서는 <b>화살표 키</b>로 움직입니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">가지 184개</span>'
             '<span style="display:block;font-size:8.5px;color:var(--danger);margin-top:2px">스크롤해도 찾기 어려움</span>'),
         "너무 많음", False, "검색이 필요함", "152px"),
     "가지가 너무 많을 때", "가지가 많으면 트리만으로는 원하는 항목을 <b>찾기 어렵습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>role=\"tree\"</code>", "트리 역할", "스크린 리더가 <b>트리</b>라고 읽어 줍니다"),
    ("<code>treeitem</code>", "+ <code>aria-level</code>", "항목이 <b>몇 단</b>에 있는지 알립니다"),
    ("<code>aria-expanded</code>", "펼침 상태", "꺾쇠 모양이 보여 주는 펼침 상태를 <b>스크린 리더에도</b> 알립니다"),
    ("꺾쇠", "▸ ▾", "자식 항목이 있다는 표시입니다"),
    ("들여쓰기", "폭을 차지함", "깊이 × 들여쓰기 폭만큼 <b>이름을 적을 자리가 줄어듭니다</b>"),
    ("<code>tabindex</code>", "하나만 0", "<kbd>Tab</kbd>을 누르면 트리 안에서는 <b>한 번만</b> 멈춥니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          트리는 <b>만들기는 쉽지만 사용자가 쓰기는 어려운</b> 부품입니다.
          가지가 백 개를 넘으면 가지를 하나하나 펴고 접어 봐야 해서, 결국 찾던 항목을 찾지 못하는 일이 생깁니다.
          그래서 실제 제품의 트리에는 거의 늘 <b>검색 칸</b>이 붙어 있고,
          검색 결과를 고르면 <b>그 항목이 있는 가지까지 저절로 펼쳐지게</b> 해 둡니다.<br>
          키보드 조작도 다른 부품과 다릅니다. <kbd>Tab</kbd>은 트리 전체에서 <b>한 번만</b> 멈추고,
          트리 안에서는 <b>화살표 키</b>로 움직입니다. 가지가 백 개인 트리에서 <kbd>Tab</kbd>이 줄마다 멈추면 키보드로는 트리를 지나갈 수 없습니다.</p>''',
  do=ul([
    "깊이를 <b>세 단</b> 안으로 둘 때",
    "트리 위에 <b>검색 칸</b>을 두고, 찾은 항목이 있는 가지까지 펼쳐 줄 때",
    "<b>화살표 키</b>로 가지를 펴고 접게 할 때",
  ]),
  dont=ul([
    "가지마다 <kbd>Tab</kbd>이 멈추게 둘 때. 가지가 백 개면 <b>백 번 눌러야</b> 트리를 지나갑니다",
    "꺾쇠 없이 들여쓰기만으로 계층을 알릴 때",
    "트리를 <b>폰 화면에</b> 그대로 올릴 때. 들여쓰기가 좁은 화면 폭을 대부분 차지합니다",
    "펴고 접은 상태를 <b>기억하지 않을</b> 때. 다른 화면에 갔다 돌아오면 가지를 처음부터 다시 펼쳐야 합니다",
  ]),
  instead='화면 옆에 늘 붙어 있는 메뉴 띠가 필요하면 <a href="sidebar.html">사이드바</a>를 쓰고, 지금 위치까지 이어진 한 줄기만 보여 주면 되는 경우에는 <a href="breadcrumb.html">브레드크럼</a>이 맞습니다. 항목을 찾는 것이 주된 목적이면 <a href="search.html">검색</a>을 쓰고, 좁은 화면에서는 <a href="drawer.html">드로어</a>를 씁니다.',
  cases=cases([
    (tree([(0, "▾", "src", False), (1, "", "app.js", True), (1, "▸", "lib", False)], "150px", "", True),
     "파일과 폴더 보여 주기", "사용자에게 가장 익숙한 트리입니다"),
    (tree([(0, "▾", "의류", False), (1, "", "아우터", False), (1, "", "상의", False)], "150px", "", True),
     "상품 분류 고르기", "깊이는 <b>두 단</b>이면 충분합니다"),
    (one(txt('<span style="display:block;font-size:8.5px">🔍 반팔</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">의류 › 상의 › 티셔츠 ›</span>'
             '<span style="display:block;font-size:8.5px;color:var(--accent)">반팔 티셔츠</span>'),
         "검색과 함께", True, "찾으면 그 가지까지 펼쳐 줌", "150px"),
     "검색으로 찾고 가지 펼치기", "가지가 많으면 트리보다 <b>검색이 주된 찾기 수단</b>이 됩니다"),
  ]),
  code_lede="목록 태그에 ARIA 역할을 붙여 만듭니다. <code>&lt;ul&gt;</code>을 중첩한 구조가 그대로 트리의 계층이 됩니다.",
  code='''&lt;<span class="t">ul</span> <span class="a">role</span>=<span class="s">"tree"</span> <span class="a">aria-label</span>=<span class="s">"분류"</span>&gt;
  &lt;<span class="t">li</span> <span class="a">role</span>=<span class="s">"none"</span>&gt;
    &lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"treeitem"</span> <span class="a">aria-expanded</span>=<span class="s">"true"</span>
         <span class="a">aria-level</span>=<span class="s">"1"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>&gt;의류&lt;/<span class="t">div</span>&gt;
    &lt;<span class="t">ul</span> <span class="a">role</span>=<span class="s">"group"</span>&gt;
      &lt;<span class="t">li</span> <span class="a">role</span>=<span class="s">"none"</span>&gt;
        &lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"treeitem"</span> <span class="a">aria-level</span>=<span class="s">"2"</span>
             <span class="a">aria-selected</span>=<span class="s">"true"</span> <span class="a">tabindex</span>=<span class="s">"-1"</span>&gt;아우터&lt;/<span class="t">div</span>&gt;
      &lt;/<span class="t">li</span>&gt;
    &lt;/<span class="t">ul</span>&gt;
  &lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ul</span>&gt;''',
  keys=kbd([
    ("↓ ↑", "화면에 보이는 줄을 하나씩 오르내리며, <b>접힌 가지의 자식은 건너뜁니다</b>"),
    ("→", "접혀 있으면 펼치고, 이미 펼쳐져 있으면 <b>첫 자식</b>으로 갑니다"),
    ("←", "펼쳐져 있으면 접고, 이미 접혀 있으면 <b>부모</b>로 갑니다"),
    ("Home · End", "트리의 <b>첫 줄이나 마지막 줄</b>로 갑니다"),
    ("Tab", "트리 전체에서 <b>한 번만</b> 멈춥니다"),
    ("글자 키를 누르면", "누른 글자로 시작하는 <b>다음 줄</b>로 갑니다. 긴 트리에서 특히 쓸모가 있습니다"),
  ]),
  backend=rows([
    ("펼칠 때마다 자식만 받아 오기", "가지가 수천 개면 처음부터 전부 보내지 않고, 사용자가 가지를 <b>펼 때마다</b> 그 가지의 자식만 받아 옵니다(lazy)."),
    ("자식이 있는지 함께 알려 주기", "응답에 <code>has_children: true</code>를 함께 담아 주면 화면이 <b>꺾쇠를 그릴지</b> 바로 정할 수 있습니다. 이 값이 없으면 가지를 펼쳐 본 뒤에야 자식이 있는지 알 수 있습니다."),
    ("경로를 담아 가지를 펼친 채 열기", "<code>path: [\"의류\",\"상의\"]</code>처럼 경로를 담아 주면 <b>그 가지까지 펼친 상태로</b> 화면을 열 수 있습니다."),
  ]),
  plat_lede="트리뷰는 <b>PC 화면에서 쓰는 부품</b>이라서 폰에서는 거의 쓰지 않습니다.",
  plats=plats([
    ("웹", "role=\"tree\"",
     tree([(0, "▾", "의류", False), (1, "", "상의", True)], "110px", "", True),
     "트리용 태그가 따로 없어서 목록 태그에 <b>ARIA 역할</b>을 붙여 만들고, 화살표 키 동작도 직접 구현합니다."),
    ("iOS", "OutlineGroup",
     '''              <div class="phone" role="img" aria-label="iOS 트리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:12px;right:5px;top:40px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "SwiftUI의 <code>OutlineGroup</code>으로 만듭니다. 아이폰에서는 거의 쓰지 않고 <b>아이패드와 맥</b>에서 씁니다."),
    ("안드로이드", "정해진 부품 없음",
     '''              <div class="phone" role="img" aria-label="안드로이드 계층 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "Material에는 트리 부품이 없습니다. 대신 단계마다 <b>새 화면으로 넘어가며</b> 한 단씩 들어가는 방식을 씁니다."),
  ]),
  plat_note="폰에서 트리를 쓰지 않는 이유는 깊이마다 들여쓰기가 더해지면 <b>390px 폭이 금세 모자라기</b> 때문입니다. 좁은 화면에서는 안드로이드처럼 분류, 하위 분류, 목록 순으로 <b>한 단씩 새 화면으로 들어가는 방식</b>이 훨씬 낫고, 이때 지금 위치를 알려 주는 부품이 <a href=\"breadcrumb.html\">브레드크럼</a>입니다. 웹에서도 폰 폭에서는 트리를 접고 이 방식으로 바꾸는 편이 안전합니다.",
  siblings=siblings("treeview"),
  related='''        <li><a href="sidebar.html"><b>사이드바</b><em>7부</em></a></li>
        <li><a href="breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>''',
)
