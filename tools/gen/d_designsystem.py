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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">토큰 — --accent: #2f6df6. 이름 붙인 값</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">부품 — 토큰을 쓰는 버튼 · 칩 · 입력칸</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">패턴 — 부품을 모은 카드 · 폼 · 표</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">문서 — 언제 쓰고 언제 안 쓰나</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">시안과 코드가 같은 토큰을 본다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">색을 부품마다 박으면 연결이 끊긴다</div>
                </div>
              </div>'''

D = dict(
  slug="designsystem", ko="디자인 시스템", en="Design system",
  desc="토큰·부품·패턴·문서의 네 겹. 스타일 가이드·컴포넌트 라이브러리와 무엇이 다른가.",
  lede="<b>토큰 · 부품 · 패턴 · 문서</b> 네 겹입니다. 넷 중 하나라도 빠지면 다른 이름으로 불러야 합니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꿔 보세요 — <b>토큰 하나</b>를 고치면 부품도 패턴도 따라옵니다.
          이게 디자인 시스템이 하는 일의 거의 전부입니다.<br>
          <b>색을 부품마다 박아 두기</b>를 켜면 연결이 끊깁니다. 색을 바꿔도 몇 개는 안 따라오고,
          어느 것이 안 따라왔는지는 <b>눈으로 찾아야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "디자인 시스템, 디자인 언어, 컴포넌트 라이브러리, 스타일 가이드"),
    ("영어", "design system, design language, component library, style guide"),
    ("같이 쓰는 말",
     "값에 이름을 붙인 것이 <b>디자인 토큰</b>, 그 값을 쓰는 조각이 <b>컴포넌트</b>, "
     "조각을 모은 화면 단위가 <b>패턴</b>입니다. "
     "색·글꼴 규칙만 적은 문서는 <b>스타일 가이드</b>, 쓸 수 있는 코드 묶음은 <b>컴포넌트 라이브러리</b>입니다. "
     "넷이 다 있고 <b>지켜지는</b> 것을 디자인 시스템이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>스타일 가이드</b> — 규칙만 적은 문서입니다. <b>쓸 수 있는 부품</b>이 없으면 지켜지지 않습니다.<br>"
     "<b>컴포넌트 라이브러리</b> — 부품은 있는데 <b>언제 쓰는지</b>가 없으면 아무거나 쓰게 됩니다.<br>"
     "<b>UI 킷</b> — 시안 파일만 가리키는 일이 많습니다. <b>코드가 따라오지 않으면</b> 반쪽입니다."),
  ]),
  axes=ax("디자인 시스템"),
  oneline="<b>시안과 코드가 같은 토큰을 보고 있나</b>가 전부입니다. 아니면 그림과 화면이 조금씩 멀어집니다.",
  s4_title="네 겹", s4_hint="무엇이 빠지면 무엇이 안 되나",
  states=states([
    (layer('① 토큰', SW + ' <span style="font-family:var(--mono);font-size:8.5px">--accent: #2f6df6</span>', "152px", "이름 붙인 값", True),
     "토큰", "색·간격·글자 크기. <b>값이 아니라 이름</b>을 쓴다"),
    (layer('② 부품', btn('저장') + ' ' + btn('취소', False), "152px", "토큰을 쓰는 조각", True),
     "부품", "버튼·칩·입력칸. <b>토큰을 참조</b>한다"),
    (layer('③ 패턴', '<span style="font-size:8.5px;font-weight:700">모란상회</span>'
           '<div style="display:flex;gap:4px">' + btn('정산 보기') + btn('내역', False) + '</div>', "152px", "부품을 모은 화면 조각", True),
     "패턴", "카드·폼·표. <b>부품을 조립</b>한 것"),
    (layer('④ 문서', '<span style="font-size:8.5px">주 동작에만 쓴다</span>'
           '<span style="font-size:8px;color:var(--fg-muted)">한 화면에 하나. 취소는 약하게</span>', "152px", "언제 쓰고 언제 안 쓰나", True),
     "문서", "<b>이게 빠지면</b> 아무거나 쓰게 된다"),
    (layer('규칙만', '<span style="font-size:8.5px;color:var(--fg-muted)">주 색은 #2f6df6<br>본문은 15px</span>', "152px", "쓸 수 있는 부품이 없다", False),
     "스타일 가이드", "<b>지켜지지 않는다</b> — 매번 손으로 만든다"),
    (layer('부품만', btn('저장') + ' ' + btn('삭제') + ' ' + btn('확인'), "152px", "언제 쓰는지가 없다", False),
     "컴포넌트 라이브러리", "<b>아무거나 쓰게</b> 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("토큰", "이름 붙인 값", "<code>--accent</code>·<code>--space-3</code>. <b>값을 직접 안 쓴다</b>"),
    ("부품", "토큰을 쓰는 조각", "버튼·칩·입력칸"),
    ("패턴", "부품을 모은 것", "카드·폼·표"),
    ("문서", "언제 쓰나", "<b>이게 시스템과 라이브러리를 가른다</b>"),
    ("한 뿌리", "시안 = 코드", "둘이 <b>같은 토큰</b>을 봐야 안 멀어진다"),
    ("박아 두기", "연결 끊김", "고칠 때 <b>어느 것이 안 따라왔는지</b> 모른다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          디자인 시스템이 실패하는 가장 흔한 이유는 <b>만들지 않아서</b>가 아니라
          <b>지켜지지 않아서</b>입니다.
          부품을 아무리 잘 만들어도 '이럴 때는 어떤 걸 쓰나'가 없으면
          급한 사람은 새로 만듭니다 —
          그래서 <b>문서가 네 번째가 아니라 사실은 첫 번째</b>입니다.
          그리고 문서는 길 필요가 없습니다.
          부품마다 <b>'언제 쓴다 / 언제 안 쓴다' 두 줄</b>이면 대부분 해결됩니다.</p>''',
  do=ul([
    "같은 부품이 <b>여러 화면</b>에 나올 때",
    "사람이 늘어 <b>손으로 맞추기</b> 어려워질 때",
    "브랜드·테마를 <b>통째로 바꿀</b> 일이 있을 때",
  ]),
  dont=ul([
    "화면이 다섯 장인데 시스템부터 만들기 — <b>과하다</b>",
    "값을 부품마다 박아 두기 — <b>토큰을 쓸 이유가 없어진다</b>",
    "문서 없이 부품만 — <b>아무거나 쓰게</b> 된다",
    "쓰는 사람 없이 혼자 만들기 — <b>안 쓰이면 없는 것</b>이다",
  ]),
  instead='값 하나하나는 <a href="../items/color.html">색 토큰</a>·<a href="../items/spacing.html">간격 체계</a>, 부품의 변형은 <a href="variant.html">배리언트</a>, 넘기는 일은 <a href="handoff.html">핸드오프</a>.',
  cases=cases([
    (code(['--accent: #2f6df6;', '--space-3: 12px;', '--radius-1: 6px;'], "150px", "이름이 곧 계약이다", True),
     "토큰", "<b>값이 아니라 이름</b>을 쓴다"),
    (layer('버튼', btn('저장') + ' ' + btn('취소', False) + ' ' + btn('삭제'), "150px", "변형은 정해 둔다"),
     "부품", "<a href=\"variant.html\">배리언트</a>로 묶는다"),
    (layer('쓰는 법', '<span style="font-size:8.5px">주 동작에만 · 한 화면에 하나</span>'
           '<span style="font-size:8px;color:var(--danger)">취소에는 쓰지 않는다</span>', "150px", "두 줄이면 충분하다"),
     "문서", "<b>언제 쓰고 언제 안 쓰나</b>"),
  ]),
  s8_title="최소 구조와 규칙", s8_hint="이 시스템의 계약서",
  code_lede="토큰은 <b>한 곳</b>에 두고, 부품은 값이 아니라 이름을 씁니다.",
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
  keys=kbd([
    ("토큰은 <b>한 곳</b>에", "흩어지면 '진짜 값'이 어디인지 아무도 모른다"),
    ("이름은 <b>쓰임</b>으로", "<code>--blue-500</code>보다 <code>--accent</code>. 다크 모드에서 파랑이 아닐 수 있다"),
    ("접근성은 <b>부품에</b>", "<code>role</code>·키보드를 부품에 넣어 두면 <b>쓰는 사람이 공짜로</b> 얻는다"),
    ("<a href=\"../items/dark.html\">다크 모드</a>", "토큰이 있으면 <b>값만 바꾸면</b> 된다 — 없으면 전수 조사다"),
    ("<a href=\"../items/contrast.html\">대비비</a>", "토큰 단계에서 한 번 재 두면 <b>부품마다 안 재도</b> 된다"),
    ("버전", "부품을 고치면 쓰는 쪽이 전부 바뀐다. <b>무엇이 바뀌는지</b> 적어 둔다"),
  ]),
  backend=rows([
    ("토큰을 한 벌로 뽑는다", "시안 도구의 변수를 <b>CSS 변수·JSON 으로 내보내</b> 쓰면 손으로 옮기다 틀릴 일이 없습니다."),
    ("부품을 패키지로", "여러 저장소가 쓰면 <b>버전</b>이 필요합니다. 고칠 때마다 쓰는 쪽이 다 바뀝니다."),
    ("쓰이는지 센다", "어느 부품이 어디서 몇 번 쓰이는지를 세어 보면 <b>버릴 것</b>이 보입니다."),
    ("손으로 만든 것 찾기", "<code>#2f6df6</code> 같은 값을 코드에서 검색하면 <b>끊긴 연결</b>이 바로 나옵니다."),
  ]),
  plat_lede="<b>토큰 한 벌을 여러 곳이 본다</b>는 꼴은 같습니다.",
  plats=plats([
    ("웹", "CSS 변수",
     code(['--accent: #2f6df6'], "110px", "", True),
     "<code>:root</code>에 두고 어디서나 참조합니다. <b>다크 모드</b>도 값만 바꾸면 됩니다."),
    ("iOS", "Asset Catalog",
     '''              <div class="phone" role="img" aria-label="iOS 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Color/Accent<br>Color/Surface</div></div></div>''',
     "색을 <b>이름으로</b> 등록하고 라이트·다크 값을 함께 넣습니다. OS 가 골라 줍니다."),
    ("안드로이드", "Material Theme",
     '''              <div class="phone" role="img" aria-label="안드로이드 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">colorPrimary<br>colorSurface</div></div></div>''',
     "<b>역할 이름</b>이 규격에 정해져 있습니다. 쓰는 쪽은 역할만 부릅니다."),
  ]),
  plat_note="\"디자인 시스템 만들어 주세요\"는 <b>얼마나 크게</b>인지에 따라 하루짜리도 되고 반년짜리도 됩니다. 가장 값싼 시작은 <b>토큰 열 개와 부품 다섯 개</b>이고, 거기에 <b>'언제 쓴다' 두 줄씩</b>만 붙여도 대부분의 어긋남이 사라집니다. 처음부터 크게 잡으면 완성 전에 아무도 안 씁니다.",
  siblings=siblings("designsystem"),
  related='''        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="variant.html"><b>배리언트와 프롭</b><em>15부</em></a></li>
        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>''',
)
