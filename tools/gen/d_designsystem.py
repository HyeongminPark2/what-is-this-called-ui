# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def layer(title, inner, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:5px">'
            '<span style="font-size:8.5px;font-weight:700;color:var(--fg-muted)">' + title + '</span>' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

SW = '<span style="width:16px;height:16px;border-radius:4px;background:var(--accent);display:inline-block;vertical-align:-3px"></span>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">토큰은 --accent: #2f6df6처럼 이름 붙인 값</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">부품은 토큰을 쓰는 버튼 · 칩 · 입력칸</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">패턴은 부품을 모은 카드 · 폼 · 표</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">문서에는 언제 쓰고 언제 안 쓰는지 적음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">시안과 코드가 같은 토큰을 참조함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">색을 부품마다 박으면 연결이 끊김</div>
                </div>
              </div>'''

D = dict(
  slug="designsystem", ko="디자인 시스템", en="Design system",
  desc="디자인 시스템을 이루는 토큰과 부품, 패턴, 문서의 네 겹을 보여 주고, 스타일 가이드나 컴포넌트 라이브러리와 무엇이 다른지 가르는 항목입니다.",
  lede="디자인 시스템은 <b>토큰과 부품, 패턴, 문서</b>가 네 겹으로 쌓인 묶음입니다. 넷 중 하나라도 빠지면 스타일 가이드나 컴포넌트 라이브러리처럼 다른 이름으로 불러야 합니다.",
  axes_lede="현장 용어는 부품이 아니라 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꿔 보세요. <b>토큰 하나</b>를 고치면 그 토큰을 참조하는 부품과 패턴의 색이 함께 바뀌는데,
          디자인 시스템이 하는 일은 대부분 이것입니다.<br>
          <b>색을 부품마다 박아 두기</b>를 켜면 부품이 토큰 대신 색 값을 직접 쓰게 되어 연결이 끊깁니다. 그러면 색을 바꿔도 몇 개는 바뀌지 않고,
          어느 것이 바뀌지 않았는지는 <b>눈으로 하나씩 찾아야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "디자인 시스템, 디자인 언어, 컴포넌트 라이브러리, 스타일 가이드"),
    ("영어", "design system, design language, component library, style guide"),
    ("같이 쓰는 말",
     "색이나 간격 같은 값에 이름을 붙인 것을 <b>디자인 토큰</b>, 그 토큰을 가져다 쓰는 화면 조각을 <b>컴포넌트</b>, "
     "조각 여러 개를 모은 화면 단위를 <b>패턴</b>이라고 합니다. "
     "색과 글꼴 규칙만 적은 문서는 <b>스타일 가이드</b>, 가져다 쓸 수 있는 코드 묶음은 <b>컴포넌트 라이브러리</b>입니다. "
     "토큰과 부품, 패턴, 문서가 모두 갖춰져 있고 실제로 <b>지켜지는</b> 것을 디자인 시스템이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>스타일 가이드</b> — 규칙만 적은 문서입니다. 규칙대로 만든 <b>가져다 쓸 수 있는 부품</b>이 함께 없으면 매번 손으로 만들어야 해서 규칙이 잘 지켜지지 않습니다.<br>"
     "<b>컴포넌트 라이브러리</b> — 부품은 있어도 각 부품을 <b>언제 쓰는지</b> 적은 문서가 없으면 사람마다 아무 부품이나 골라 쓰게 됩니다.<br>"
     "<b>UI 킷</b> — 대개 시안 파일만 가리킵니다. 같은 부품이 <b>코드로 함께 있지 않으면</b> 디자인 쪽에서만 쓸 수 있는 묶음에 그칩니다."),
  ]),
  axes=ax("디자인 시스템"),
  oneline="디자인 시스템에서 가장 먼저 확인할 것은 <b>시안과 코드가 같은 토큰을 참조하고 있는지</b>입니다. 서로 다른 값을 쓰고 있으면 고칠 때마다 시안과 실제 화면이 조금씩 달라집니다.",
  s4_title="디자인 시스템의 네 겹", s4_hint="한 겹이 빠지면 생기는 문제",
  states=states([
    (layer('① 토큰', SW + ' <span style="font-family:var(--mono);font-size:8.5px">--accent: #2f6df6</span>', "152px", "이름 붙인 값", True),
     "토큰", "색과 간격, 글자 크기 같은 값에 이름을 붙입니다. 부품은 <b>값이 아니라 이름</b>을 씁니다"),
    (layer('② 부품', btn('저장') + ' ' + btn('취소', False), "152px", "토큰을 쓰는 조각", True),
     "부품", "버튼과 칩, 입력칸 같은 조각입니다. 색과 간격은 <b>토큰을 참조</b>합니다"),
    (layer('③ 패턴', '<span style="font-size:8.5px;font-weight:700">모란상회</span>'
           '<div style="display:flex;gap:4px">' + btn('정산 보기') + btn('내역', False) + '</div>', "152px", "부품을 모은 화면 조각", True),
     "패턴", "카드와 폼, 표처럼 <b>부품을 조립</b>해 만든 화면 단위입니다"),
    (layer('④ 문서', '<span style="font-size:8.5px">주 동작에만 씀</span>'
           '<span style="font-size:8px;color:var(--fg-muted)">한 화면에 하나. 취소는 약하게</span>', "152px", "언제 쓰고 언제 안 쓰는지", True),
     "문서", "부품을 언제 쓰는지 적습니다. <b>문서가 빠지면</b> 사람마다 아무 부품이나 골라 씁니다"),
    (layer('규칙만', '<span style="font-size:8.5px;color:var(--fg-muted)">주 색은 #2f6df6<br>본문은 15px</span>', "152px", "가져다 쓸 부품이 없음", False),
     "규칙만 있는 스타일 가이드", "가져다 쓸 부품이 없어서 매번 손으로 만들게 되고, 그래서 규칙이 <b>지켜지지 않습니다</b>"),
    (layer('부품만', btn('저장') + ' ' + btn('삭제') + ' ' + btn('확인'), "152px", "언제 쓰는지 적혀 있지 않음", False),
     "부품만 있는 컴포넌트 라이브러리", "언제 쓰는지가 적혀 있지 않아서 <b>아무 부품이나 골라 쓰게</b> 됩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("토큰", "이름 붙인 값", "<code>--accent</code>·<code>--space-3</code>처럼 이름을 붙여 두고, 부품에는 <b>값을 직접 쓰지 않습니다</b>"),
    ("부품", "토큰을 쓰는 조각", "버튼, 칩, 입력칸 같은 조각입니다"),
    ("패턴", "부품을 모은 것", "카드, 폼, 표 같은 화면 단위입니다"),
    ("문서", "언제 쓰는지", "문서가 있느냐 없느냐로 <b>디자인 시스템과 컴포넌트 라이브러리가 갈립니다</b>"),
    ("같은 토큰 참조", "시안과 코드", "시안과 코드가 <b>같은 토큰</b>을 참조해야 둘이 서로 달라지지 않습니다"),
    ("값 박아 두기", "hard-coding", "값을 고친 뒤 <b>어느 부품이 바뀌지 않았는지</b> 알 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          디자인 시스템이 실패하는 가장 흔한 이유는 만들어 둔 규칙과 부품이
          <b>지켜지지 않아서</b>입니다.
          부품을 잘 만들어 두어도 '이럴 때는 어떤 부품을 쓰나'가 적혀 있지 않으면
          급한 사람은 부품을 새로 만들어 버립니다.
          그래서 문서는 그림에서 네 번째 칸에 있지만 <b>가장 먼저 챙겨야 할 겹</b>입니다.
          문서가 길 필요는 없고,
          부품마다 <b>'언제 쓴다 / 언제 안 쓴다' 두 줄</b>만 적어 두어도 대부분의 문제가 해결됩니다.</p>''',
  do_title="디자인 시스템이 필요한 경우",
  dont_title="디자인 시스템을 만들 때 피할 것",
  do=ul([
    "같은 부품이 <b>여러 화면</b>에 나올 때",
    "사람이 늘어 <b>손으로 맞추기</b> 어려워질 때",
    "브랜드·테마를 <b>통째로 바꿀</b> 일이 있을 때",
  ]),
  dont=ul([
    "화면이 다섯 장뿐인데 시스템부터 만들 때. 화면 수에 비해 <b>일이 과합니다</b>",
    "값을 부품마다 박아 둘 때. 토큰을 고쳐도 부품이 바뀌지 않으니 <b>토큰을 둔 의미가 없어집니다</b>",
    "문서 없이 부품만 만들 때. 사람마다 <b>아무 부품이나 골라 쓰게</b> 됩니다",
    "쓸 사람과 상의하지 않고 혼자 만들 때. 아무도 쓰지 않으면 <b>만든 효과가 없습니다</b>",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='값 하나하나를 정하는 방법은 <a href="../items/color.html">색 토큰</a>과 <a href="../items/spacing.html">간격 체계</a>에서, 부품의 변형은 <a href="variant.html">배리언트</a>에서, 시안을 개발 쪽에 넘기는 일은 <a href="handoff.html">핸드오프</a>에서 다룹니다.',
  cases=cases([
    (code(['--accent: #2f6df6;', '--space-3: 12px;', '--radius-1: 6px;'], "150px", "부품은 이름으로 값을 씀", True),
     "값에 이름 붙여 쓰기", "부품에서는 <b>값이 아니라 이름</b>을 씁니다"),
    (layer('버튼', btn('저장') + ' ' + btn('취소', False) + ' ' + btn('삭제'), "150px", "변형을 미리 정해 둠"),
     "부품의 변형 정해 두기", "정해 둔 변형을 <a href=\"variant.html\">배리언트</a>로 묶어 둡니다"),
    (layer('쓰는 법', '<span style="font-size:8.5px">주 동작에만 · 한 화면에 하나</span>'
           '<span style="font-size:8px;color:var(--danger)">취소에는 쓰지 않음</span>', "150px", "두 줄이면 충분함"),
     "부품 쓰는 법 적어 두기", "부품을 <b>언제 쓰고 언제 안 쓰는지</b> 적습니다"),
  ]),
  s8_title="최소 구조와 규칙", s8_hint="토큰과 부품을 나눠 두는 법",
  code_lede="토큰은 <b>한 곳</b>에 모아 두고, 부품에서는 값 대신 토큰 이름을 씁니다.",
  code=''':root {
  <span class="c">/* ① 토큰 — 값에 이름을 붙인다 */</span>
  <span class="a">--accent</span>: <span class="a">#2f6df6</span>;
  <span class="a">--space-3</span>: <span class="a">12px</span>;
  <span class="a">--radius-1</span>: <span class="a">6px</span>;
}

<span class="c">/* ② 부품 — 값이 아니라 이름을 쓴다 */</span>
.btn {
  <span class="a">background</span>: <span class="a">var</span>(--accent);      <span class="c">/* ○ */</span>
  <span class="a">padding</span>: <span class="a">var</span>(--space-3);
  <span class="a">border-radius</span>: <span class="a">var</span>(--radius-1);
}
.btn--bad { <span class="a">background</span>: <span class="a">#2f6df6</span>; }   <span class="c">/* ✕ 박아 두면 끊긴다 */</span>

<span class="c">/* ③ 패턴 — 부품을 모은다 */</span>
.store-card { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">var</span>(--space-3); }''',
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("토큰은 <b>한 곳</b>에 모으기", "토큰이 여러 파일에 흩어지면 어느 쪽이 '진짜 값'인지 알 수 없게 됩니다"),
    ("이름은 <b>쓰임</b>에 따라 짓기", "<code>--blue-500</code>보다 <code>--accent</code>처럼 쓰임을 이름으로 붙입니다. 다크 모드에서는 강조색이 파랑이 아닐 수도 있기 때문입니다"),
    ("접근성은 <b>부품에</b> 넣어 두기", "<code>role</code>과 키보드 동작을 부품에 넣어 두면 그 부품을 쓰는 사람은 <b>따로 손대지 않아도</b> 접근성을 갖추게 됩니다"),
    ("<a href=\"../items/dark.html\">다크 모드</a> 대응", "토큰이 있으면 토큰의 <b>값만 바꾸면</b> 되지만, 없으면 색을 쓴 곳을 모두 찾아 고쳐야 합니다"),
    ("<a href=\"../items/contrast.html\">대비비</a> 확인", "토큰 단계에서 색 조합의 대비비를 한 번 재 두면 <b>부품마다 따로 재지 않아도</b> 됩니다"),
    ("부품 버전 기록", "부품을 고치면 그 부품을 쓰는 화면이 모두 바뀌므로 <b>무엇이 바뀌는지</b> 적어 둡니다"),
  ]),
  backend=rows([
    ("토큰을 코드로 한 벌 내보내기", "시안 도구에 정의한 변수를 <b>CSS 변수나 JSON으로 내보내</b> 코드에서 그대로 쓰면, 값을 손으로 옮겨 적다가 틀리는 일이 없습니다."),
    ("부품을 패키지로 묶어 버전 붙이기", "여러 저장소가 같은 부품 패키지를 쓰면 <b>버전</b>을 붙여 관리해야 합니다. 버전 없이 부품을 고치면 그 패키지를 쓰는 저장소가 모두 한꺼번에 바뀌기 때문입니다."),
    ("부품이 쓰인 횟수 세기", "어느 부품이 어디서 몇 번 쓰이는지 세어 보면 거의 쓰이지 않아 <b>정리해도 되는 부품</b>을 찾을 수 있습니다."),
    ("토큰 대신 값을 직접 쓴 곳 찾기", "<code>#2f6df6</code> 같은 색 값을 코드에서 검색하면 토큰 대신 값을 직접 써서 <b>연결이 끊긴 곳</b>을 바로 찾을 수 있습니다."),
  ]),
  plat_lede="플랫폼마다 도구는 달라도 <b>토큰 한 벌을 여러 곳에서 참조하는</b> 구조는 같습니다.",
  plats=plats([
    ("웹", "CSS 변수",
     code(['--accent: #2f6df6'], "110px", "", True),
     "토큰을 <code>:root</code>에 두고 어디서나 참조합니다. <b>다크 모드</b>를 만들 때도 변수의 값만 바꾸면 됩니다."),
    ("iOS", "Asset Catalog",
     '''              <div class="phone" role="img" aria-label="iOS 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Color/Accent<br>Color/Surface</div></div></div>''',
     "색을 <b>이름으로</b> 등록하면서 라이트 모드와 다크 모드 값을 함께 넣어 두면, OS가 현재 모드에 맞는 값을 골라 씁니다."),
    ("안드로이드", "Material Theme",
     '''              <div class="phone" role="img" aria-label="안드로이드 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">colorPrimary<br>colorSurface</div></div></div>''',
     "색의 <b>역할 이름</b>이 규격에 정해져 있어서, 앱 코드에서는 색 값 대신 역할 이름만 씁니다."),
  ]),
  plat_note="\"디자인 시스템 만들어 주세요\"라는 요청은 <b>범위를 얼마나 크게 잡느냐</b>에 따라 하루면 끝나는 일도, 반년이 걸리는 일도 됩니다. 가장 적은 품으로 시작하는 방법은 <b>토큰 열 개와 부품 다섯 개</b>를 먼저 만드는 것이고, 부품마다 <b>'언제 쓴다' 두 줄씩</b>만 붙여도 시안과 화면이 어긋나는 일이 대부분 사라집니다. 처음부터 범위를 크게 잡으면 완성되기 전까지는 아무도 그 시스템을 쓰지 않습니다.",
  siblings=siblings("designsystem"),
  related='''        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="variant.html"><b>배리언트와 프롭</b><em>15부</em></a></li>
        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>''',
)
