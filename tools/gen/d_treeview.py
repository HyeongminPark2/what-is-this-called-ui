# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 '누르면 어디론가 간다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">role="tree" — 목록이 아니라 트리다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">treeitem + aria-level — 몇 단인지</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-expanded — 폈나 접었나</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">꺾쇠(▸ ▾) — 자식이 있다는 신호</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">들여쓰기 — 깊어질수록 <b>이름 자리를 먹는다</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">tabindex 는 하나만 0 — 나머지는 -1</div>
                </div>
              </div>'''

D = dict(
  slug="treeview", ko="트리뷰", en="Tree view",
  desc="계층을 펴고 접으며 다니는 길 안내. 깊이 제한, 화살표 키, 들여쓰기가 먹는 폭.",
  lede="<b>부모와 자식</b>이 있는 것들을 펴고 접으며 다닙니다. 깊이가 <b>세 단</b>을 넘으면 다른 길을 찾는 편이 낫습니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>트리는 깊어질수록 <b>들여쓰기가 폭을 먹습니다</b> — 데모가 가장 깊은 줄에 남은
          이름 자리를 재서 적습니다. 들여쓰기를 키우거나 가지를 더 펼치면 이름이 먼저 잘립니다.<br>
          트리는 <b>목록이 아니라 트리로 읽혀야</b> 합니다 — <code>role="tree"</code> ·
          <code>treeitem</code> · <code>aria-expanded</code> 를 쓰고 화살표 키로 폅니다.
          '키보드로 훑어보기'를 누르면 ↓ 로 내려가며 간 차례가 적힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "트리뷰, 트리, 폴더 트리, 계층 목록"),
    ("영어", "tree view, tree, file tree, hierarchy navigation"),
    ("같이 쓰는 말",
     "가지를 펴고 접는 꺾쇠를 <b>디스클로저</b>(disclosure triangle), "
     "자식이 없는 끝 가지를 <b>잎</b>(leaf)이라 부릅니다. "
     "여러 개를 고를 수 있게 체크박스를 붙인 것이 <b>체크박스 트리</b>이고, "
     "한 번에 한 가지만 펴지는 것을 <b>아코디언 트리</b>라 하기도 합니다."),
    ("자주 잘못 부름",
     "<b>아코디언</b> — 아코디언은 <b>내용을 펴는</b> 것이고 트리는 <b>길을 펴는</b> 것입니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 <b>자리</b>이고, 그 안에 트리가 들어가기도 합니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 <b>한 줄기만</b> 보여 줍니다."),
  ]),
  axes=ax("트리뷰"),
  oneline="<b>깊이 세 단, 가지 스무 개</b>가 넘어가면 트리로는 감당이 안 됩니다 — 검색을 붙이세요.",
  states=states([
    (tree([(0, "▸", "의류", False), (0, "▸", "생활용품", False), (0, "▸", "식품", False)], "152px", "다 접힘", True),
     "접힘", "<b>한눈에</b> 전체가 보인다"),
    (tree([(0, "▾", "의류", False), (1, "▸", "아우터", True), (1, "▸", "상의", False), (0, "▸", "생활용품", False)], "152px", "한 가지만 폄", True),
     "폄", "지금 가지만 열어 둔다"),
    (tree([(0, "▾", "의류", False), (1, "▾", "상의", False), (2, "▾", "티셔츠", False), (3, "", "반팔 티…", False)], "152px", "이름이 잘렸다", False),
     "너무 깊음", "<b>들여쓰기가</b> 이름을 먹는다"),
    (tree([(0, "▾", "의류", False), (1, "▸", "아우터", False), (1, "▸", "상의", True), (1, "▸", "하의", False)], "152px", "고른 줄이 밝다", True),
     "고름", "<code>aria-selected</code>"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">⌨ ↓ ↑ 로 오르내리고</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted)">→ 로 펴고 ← 로 접는다</span>'),
         "키보드", True, "Tab 은 트리 전체에 한 번만 멈춘다", "152px"),
     "키보드", "<b>화살표</b>가 주인공이다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">가지 184개</span>'
             '<span style="display:block;font-size:8.5px;color:var(--danger);margin-top:2px">굴려도 못 찾는다</span>'),
         "너무 많음", False, "검색이 필요하다", "152px"),
     "가지가 많음", "트리만으로는 <b>못 찾는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>role=\"tree\"</code>", "목록이 아니다", "소리로 <b>트리</b>라고 전해진다"),
    ("<code>treeitem</code>", "+ <code>aria-level</code>", "<b>몇 단</b>인지 알린다"),
    ("<code>aria-expanded</code>", "폈나 접었나", "꺾쇠의 <b>소리 버전</b>"),
    ("꺾쇠", "▸ ▾", "자식이 있다는 신호"),
    ("들여쓰기", "폭을 먹는다", "깊이 × 들여쓰기만큼 <b>이름 자리가 준다</b>"),
    ("<code>tabindex</code>", "하나만 0", "Tab 은 트리에 <b>한 번만</b> 멈춘다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          트리는 <b>만들기는 쉽고 쓰기는 어려운</b> 부품입니다.
          가지가 백 개를 넘으면 펴고 접는 수고가 쌓여, 결국 찾던 것을 못 찾습니다.
          그래서 실제로 쓸 만한 트리에는 거의 늘 <b>검색 칸</b>이 붙어 있고,
          검색 결과를 고르면 <b>그 가지까지 저절로 펴지게</b> 해 둡니다.<br>
          키보드도 보통 부품과 다릅니다 — Tab 은 트리 전체에 <b>한 번만</b> 멈추고,
          그 안은 <b>화살표</b>로 다닙니다. 가지 백 개를 Tab 으로 넘기게 두면 못 씁니다.</p>''',
  do=ul([
    "깊이를 <b>세 단</b> 안으로 두기",
    "트리 위에 <b>검색 칸</b> 두기 — 찾으면 그 가지까지 펴 주기",
    "<b>화살표 키</b>로 펴고 접게 하기",
  ]),
  dont=ul([
    "가지마다 Tab 이 멈추게 두기 — <b>백 번 눌러야</b> 지나간다",
    "꺾쇠 없이 들여쓰기만으로 계층 알리기",
    "트리를 <b>폰에</b> 그대로 올리기 — 들여쓰기가 화면을 다 먹는다",
    "펴고 접은 상태를 <b>안 기억하기</b> — 돌아오면 다시 처음부터다",
  ]),
  instead='자리로서의 옆 띠는 <a href="sidebar.html">사이드바</a>, 한 줄기만이면 <a href="breadcrumb.html">브레드크럼</a>, 찾기가 주 목적이면 <a href="search.html">검색</a>, 좁은 화면에서는 <a href="drawer.html">드로어</a>.',
  cases=cases([
    (tree([(0, "▾", "src", False), (1, "", "app.js", True), (1, "▸", "lib", False)], "150px", "", True),
     "파일 트리", "가장 익은 자리"),
    (tree([(0, "▾", "의류", False), (1, "", "아우터", False), (1, "", "상의", False)], "150px", "", True),
     "분류 고르기", "깊이 <b>둘</b>이면 충분하다"),
    (one(txt('<span style="display:block;font-size:8.5px">🔍 반팔</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">의류 › 상의 › 티셔츠 ›</span>'
             '<span style="display:block;font-size:8.5px;color:var(--accent)">반팔 티셔츠</span>'),
         "검색과 함께", True, "찾으면 그 가지까지 펴 준다", "150px"),
     "검색과 함께", "가지가 많으면 <b>이게 본체</b>다"),
  ]),
  code_lede="목록 태그에 역할을 얹습니다. 중첩 <code>&lt;ul&gt;</code>이 계층 그대로입니다.",
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
    ("↓ ↑", "보이는 줄을 하나씩 오르내린다 — <b>접힌 자식은 건너뛴다</b>"),
    ("→", "접혀 있으면 편다. 이미 폈으면 <b>첫 자식</b>으로"),
    ("←", "펴져 있으면 접는다. 이미 접혔으면 <b>부모</b>로"),
    ("Home · End", "트리의 <b>처음 · 마지막</b> 줄로"),
    ("Tab", "트리 전체에 <b>한 번만</b> 멈춘다"),
    ("글자 키", "그 글자로 시작하는 <b>다음 줄</b>로 — 긴 트리에서 쓸모가 크다"),
  ]),
  backend=rows([
    ("한 번에 다 주지 않는다", "가지가 수천 개면 처음부터 다 보내지 않습니다. <b>펼 때마다</b> 그 가지의 자식만 받아 옵니다(lazy)."),
    ("자식이 있는지", "<code>has_children: true</code> 를 같이 주면 <b>꺾쇠를 그릴지</b> 바로 정할 수 있습니다 — 안 주면 펴 보고서야 압니다."),
    ("경로", "<code>path: [\"의류\",\"상의\"]</code> 처럼 주면 <b>그 가지까지 펴 둔 채</b> 화면을 열 수 있습니다."),
  ]),
  plat_lede="<b>PC 쪽 부품</b>입니다. 폰에는 거의 안 씁니다.",
  plats=plats([
    ("웹", "role=\"tree\"",
     tree([(0, "▾", "의류", False), (1, "", "상의", True)], "110px", "", True),
     "정해진 태그가 없어 <b>역할로</b> 만듭니다. 화살표 키도 직접 붙입니다."),
    ("iOS", "OutlineGroup",
     '''              <div class="phone" role="img" aria-label="iOS 트리 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:12px;right:5px;top:40px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "SwiftUI 의 <code>OutlineGroup</code>. 폰에서는 거의 안 쓰고 <b>아이패드·맥</b>에서 씁니다."),
    ("안드로이드", "없다",
     '''              <div class="phone" role="img" aria-label="안드로이드 계층 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "Material 에 트리가 없습니다. <b>화면을 갈아 가며</b> 한 단씩 들어가는 쪽을 씁니다."),
  ]),
  plat_note="폰에 트리가 없는 데는 이유가 있습니다 — 깊이마다 들여쓰기가 들어가면 <b>390px 가 금세 동납니다</b>. 안드로이드가 쓰는 <b>한 단씩 들어가는 화면</b>(분류 → 하위 분류 → 목록)이 좁은 화면에서는 훨씬 낫고, 그때 지금 자리를 알려 주는 것이 <a href=\"breadcrumb.html\">브레드크럼</a>입니다. 웹에서도 폰 폭에서는 트리를 접고 그 꼴로 바꾸는 편이 안전합니다.",
  siblings=siblings("treeview"),
  related='''        <li><a href="sidebar.html"><b>사이드바</b><em>7부</em></a></li>
        <li><a href="breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>''',
)
