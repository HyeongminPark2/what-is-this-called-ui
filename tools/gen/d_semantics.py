# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def land(tag, text, bad=False, w="160px"):
    color = "var(--danger)" if bad else "var(--accent)"
    return ('              <div style="width:100%;max-width:' + w + ';border:1px dashed var(--line-strong);'
            'border-radius:5px;padding:7px 9px">'
            '<span style="font-family:var(--mono);font-size:9.5px;color:' + color + ';display:block;margin-bottom:2px">&lt;' + tag + '&gt;</span>'
            '<span style="font-size:11px">' + text + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:13px">
                  <div class="pin-out" data-pin="1" style="max-width:230px;border:1px dashed var(--line-strong);border-radius:6px;padding:7px 9px"><span style="font-family:var(--mono);font-size:10px;color:var(--accent);display:block">&lt;header&gt;</span><span style="font-size:11px">로고와 검색</span></div>
                  <div class="pin-out" data-pin="2" style="max-width:230px;border:1px dashed var(--line-strong);border-radius:6px;padding:7px 9px"><span style="font-family:var(--mono);font-size:10px;color:var(--accent);display:block">&lt;nav&gt;</span><span style="font-size:11px">홈 · 정산 · 설정</span></div>
                  <div class="pin-out" data-pin="3" style="max-width:230px;border:1px dashed var(--line-strong);border-radius:6px;padding:7px 9px"><span style="font-family:var(--mono);font-size:10px;color:var(--accent);display:block">&lt;main&gt;</span><span style="font-size:11px">정산 목록 — 화면에 하나만</span></div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">h1 → h2 → h3   — 건너뛰지 않는다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">ul · ol   — "항목 12개" 가 읽힌다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">div 로만 쌓으면 구역 목록이 빈다</div>
                </div>
              </div>'''

D = dict(
  slug="semantics", ko="시맨틱 태그", en="Semantic HTML · landmarks",
  desc="시맨틱 태그를 쓰면 생기는 구역 목록과 역할, 키보드 동작을 보여 주고, div로만 쌓았을 때 무엇이 사라지는지 보여 주는 항목입니다.",
  lede="시맨틱 태그는 태그 이름만 보고도 <b>그 자리가 무슨 내용인지</b> 알 수 있는 태그입니다. 알맞은 태그를 쓰면 역할과 키보드 동작, 문서 구조가 <b>따로 코드를 쓰지 않아도</b> 함께 들어옵니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>아래에 <b>스크린 리더의 구역 목록</b>이 나옵니다. 스크린 리더 사용자는 이 목록을 띄워 놓고
          '내비게이션'이나 '메인' 같은 구역으로 바로 건너뜁니다.<br>
          <b>전부 div 로 바꾸기</b>를 켜 보세요. 화면은 똑같은데 <b>구역 목록이 모두 비어 버려서</b>,
          페이지를 처음부터 끝까지 순서대로 읽는 방법밖에 남지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시맨틱 태그, 의미 있는 마크업, 구역"),
    ("영어", "semantic HTML, landmarks, document structure"),
    ("같이 쓰는 말",
     "<code>&lt;header&gt;</code>·<code>&lt;nav&gt;</code>·<code>&lt;main&gt;</code>처럼 화면을 크게 나누는 구역은 "
     "<b>랜드마크</b>(landmark)라고 하고, <code>h1~h6</code>이 만드는 목차는 "
     "<b>제목 구조</b>(heading structure)라고 합니다. 태그에 기본으로 들어 있는 역할은 "
     "<b>암시적 역할</b>(implicit role)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>SEO 용</b> — 시맨틱 태그는 검색에도 도움이 되지만, <b>본래 목적은 문서 구조를 알리는</b> 것입니다.<br>"
     "<b><code>role</code>을 붙이면 같다</b> — <code>role</code>을 붙이면 역할만 같아지고 <b>키보드 동작은 따라오지 않습니다</b>.<br>"
     "<b><code>&lt;section&gt;</code></b> — <code>&lt;section&gt;</code>은 <b>이름이 있어야</b> 구역으로 인정되고, 이름 없이 쓰면 div와 같습니다."),
  ]),
  axes=ax("시맨틱 태그"),
  oneline="<b>ARIA 사용 규칙의 첫 번째는 \"ARIA를 쓰지 않는 것\"</b>입니다. 알맞은 태그가 있으면 ARIA 속성을 붙이지 말고 그 태그를 씁니다.",
  s4_title="갈래", s4_hint="태그 하나가 주는 것",
  states=states([
    (land("header", "로고와 검색"), "header", "구역 목록에 <b>'배너'</b>로 올라갑니다"),
    (land("nav", "홈 · 정산 · 설정"), "nav", "구역 목록에 <b>'내비게이션'</b>으로 올라갑니다. 여러 개라면 각각 이름을 붙입니다"),
    (land("main", "정산 목록"), "main", "<b>화면에 하나만</b> 둡니다. 건너뛰기 링크를 누르면 이 구역으로 옵니다"),
    (land("div", "아무 뜻 없음", True), "div", "<b>구역 목록에 올라가지 않으므로</b> 처음부터 순서대로 읽는 수밖에 없습니다"),
    ('''              <div style="width:100%;max-width:160px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;ul&gt;</span>
                <span style="font-size:11px">· 정산 #4821</span>
                <span style="font-size:11px">· 정산 #4820</span>
                <span style="font-size:9.5px;color:var(--fg-muted);font-family:var(--mono)">"목록, 항목 2개"</span>
              </div>''',
     "ul · ol", "목록이 <b>몇 건인지</b> 저절로 읽힙니다"),
    ('''              <div style="width:100%;max-width:160px;display:grid;gap:3px">
                <span style="font-size:13px;font-weight:800">h1 정산</span>
                <span style="font-size:11.5px;font-weight:700;padding-left:8px">h2 이번 주</span>
                <span style="font-size:11px;padding-left:16px">h3 모란상회</span>
              </div>''',
     "h1 ~ h6", "스크린 리더 사용자는 제목만 골라 훑으면서 <b>목차처럼</b> 씁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("배너", "&lt;header&gt;", "화면 맨 위 구역으로, 로고와 검색, 계정 메뉴가 들어갑니다"),
    ("내비게이션", "&lt;nav&gt;", "다른 페이지로 가는 링크를 모은 구역입니다. <b>여러 개라면 각각 이름을 붙입니다</b>"),
    ("메인", "&lt;main&gt;", "그 화면의 본문입니다. <b>하나만</b> 두고, 건너뛰기 링크를 누르면 이곳으로 옵니다"),
    ("제목 구조", "h1 ~ h6", "제목 단계는 <b>건너뛰지 않습니다.</b> 화면에 보이는 크기는 CSS로 따로 정합니다"),
    ("목록", "&lt;ul&gt; · &lt;ol&gt;", "'항목 12개'처럼 개수가 저절로 읽힙니다. <code>&lt;div&gt;</code>로 쌓으면 몇 건인지 알 수 없습니다"),
    ("div 만 쌓기", "&lt;div&gt;", "<b>구역 목록이 비어 버려서</b> 처음부터 끝까지 순서대로 읽는 수밖에 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          알맞은 태그 하나를 쓰면 요소가 무엇인지 알려 주는 역할, 키보드로 누를 수 있는 동작,
          목록과 목차에 들어가는 구조까지 <b>세 가지가 한꺼번에</b> 들어옵니다.
          반면 <code>role</code>로 흉내 내면 <b>역할 하나만</b> 생기고, 나머지 둘은 직접 짜야 합니다.
          그래서 <b>접근성 작업의 대부분은 알맞은 태그를 고르는 일</b>이라는 말이 나옵니다.</p>''',
  do=ul([
    "<b>모든 화면</b>의 틀을 잡을 때. 레이아웃보다 태그를 먼저 고릅니다",
    "누르는 요소와 이동하는 요소를 만들 때. 누르는 것은 <code>&lt;button&gt;</code>, 이동하는 것은 <code>&lt;a href&gt;</code>로 만듭니다",
    "같은 모양이 반복되는 항목을 만들 때. <code>&lt;ul&gt;</code>이나 <code>&lt;ol&gt;</code>로 감쌉니다",
    "<code>&lt;nav&gt;</code>가 여러 개일 때. 각각 <code>aria-label</code>로 이름을 붙입니다",
  ]),
  dont=ul([
    "화면을 <b>전부 <code>&lt;div&gt;</code></b>로 쌓을 때",
    "한 화면에 <code>&lt;main&gt;</code>을 여러 개 둘 때",
    "<code>h1</code> 다음에 바로 <code>h4</code>를 쓸 때. 제목 구조로 만든 목차의 단계가 어긋납니다",
    "표가 아닌 내용을 <b>배치하려고</b> <code>&lt;table&gt;</code>을 쓸 때. 스크린 리더가 '표, 3열 5행'으로 읽습니다",
  ]),
  instead='키보드로 되는지는 <a href="keyboard.html">키보드 조작</a>, 역할·상태는 <a href="screenreader.html">스크린 리더가 읽는 것</a>, 보이는 위계는 <a href="../items/hierarchy.html">글자 위계</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                ''' + land("header", "로고 · 검색", False, "100%").replace('              ','') +
       land("nav", "홈 · 정산 · 설정", False, "100%").replace('              ','') +
       land("main", "정산 목록", False, "100%").replace('              ','') + '''
              </div>''',
     "화면 뼈대", "header, nav, main 세 가지만 있어도 <b>구역 목록이 생깁니다</b>"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;nav aria-label="주 메뉴"&gt;</span>
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;nav aria-label="빵부스러기"&gt;</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">둘 다 '내비게이션'이면 구별이 안 된다</span>
              </div>''',
     "nav 가 여럿", "구역 목록에서 구별할 수 있도록 <b>각각 이름</b>을 붙입니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--danger)">&lt;div onclick&gt;저장&lt;/div&gt;</span>
                <span style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c">&lt;button&gt;저장&lt;/button&gt;</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">아래 한 줄이 다섯 가지를 대신한다</span>
              </div>''',
     "버튼", "<b>button 태그 하나로</b> 역할, 포커스, Enter, Space, 비활성 처리가 모두 들어옵니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="태그부터 고른다",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="화면의 틀을 잡을 때는 <b>태그부터</b> 고르고, CSS는 그다음에 씁니다.",
  code='''&lt;<span class="t">body</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#main"</span> <span class="a">class</span>=<span class="s">"skip"</span>&gt;본문으로 건너뛰기&lt;/<span class="t">a</span>&gt;

  &lt;<span class="t">header</span>&gt;…&lt;/<span class="t">header</span>&gt;
  &lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"주 메뉴"</span>&gt;…&lt;/<span class="t">nav</span>&gt;

  &lt;<span class="t">main</span> <span class="a">id</span>=<span class="s">"main"</span>&gt;          <span class="c">&lt;!-- 화면에 하나만 --&gt;</span>
    &lt;<span class="t">h1</span>&gt;정산&lt;/<span class="t">h1</span>&gt;
    &lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"w"</span>&gt;
      &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"w"</span>&gt;이번 주&lt;/<span class="t">h2</span>&gt;
      &lt;<span class="t">ul</span>&gt;&lt;<span class="t">li</span>&gt;…&lt;/<span class="t">li</span>&gt;&lt;/<span class="t">ul</span>&gt;     <span class="c">&lt;!-- "항목 12개" --&gt;</span>
    &lt;/<span class="t">section</span>&gt;
  &lt;/<span class="t">main</span>&gt;

  &lt;<span class="t">footer</span>&gt;…&lt;/<span class="t">footer</span>&gt;
&lt;/<span class="t">body</span>&gt;''',
  keys=kbd([
    ("태그부터 고른다", "알맞은 태그를 쓰면 <b>역할, 동작, 구조</b>가 한꺼번에 들어옵니다"),
    ("<code>&lt;main&gt;</code>은 하나", "건너뛰기 링크를 누르면 도착하는 곳이므로 하나만 둡니다"),
    ("제목을 건너뛰지 않는다", "h1, h2, h3 순서로 내려갑니다. 화면에 보이는 크기는 CSS로 따로 정합니다"),
    ("<code>&lt;nav&gt;</code>가 여럿이면 이름", "<code>aria-label</code>로 이름을 붙여 서로 구별합니다"),
    ("<code>&lt;section&gt;</code>에는 이름", "이름이 없는 section은 <b>div와 같습니다</b>"),
    ("배치에 <code>&lt;table&gt;</code>을 안 쓴다", "배치용 표도 스크린 리더는 '표, 3열 5행'으로 읽습니다"),
  ]),
  backend=rows([
    ("템플릿에서 한 번", "레이아웃 컴포넌트에 <code>&lt;header&gt;</code>와 <code>&lt;main&gt;</code>을 넣어 두면 그 레이아웃을 쓰는 <b>모든 화면에 구역이 저절로</b> 생깁니다."),
    ("제목 단계는 화면이 정한다", "같은 컴포넌트라도 어떤 화면에서는 <code>h2</code>, 어떤 화면에서는 <code>h3</code>이 되어야 합니다. 그래서 <b>제목 단계를 props로</b> 받도록 설계하는 경우가 많습니다."),
    ("SEO 와 겹친다", "문서 구조가 또렷하면 검색 엔진도 페이지를 잘 읽기 때문에, <b>한 번의 작업으로 접근성과 검색 노출을 함께</b> 챙길 수 있습니다."),
    ("자동 검사", "랜드마크가 있는지, <code>h1</code>이 몇 개인지, 제목 단계를 건너뛰었는지는 <b>모두 자동 검사로</b> 찾을 수 있어서 CI에 넣기 쉽습니다."),
  ]),
  plat_lede="앱에는 HTML 태그가 없는 대신 <b>표준 부품마다 역할</b>이 정해져 있습니다.",
  plats=plats([
    ("웹", "HTML 태그",
     land("main", "정산 목록", False, "120px"),
     "태그 이름이 그대로 역할이 됩니다. 화면을 <b>div로만 쌓는 것</b>은 웹에서만 생기는 사고입니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Button { }<br>List { }<br>.accessibilityHeading</div>''',
     "<b>표준 부품을 쓰면</b> 역할이 기본으로 들어 있고, 직접 그린 뷰에만 역할을 적어 줍니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Button { }<br>LazyColumn { }<br>semantics { heading( ) }</div>''',
     "iOS와 마찬가지로 <b>표준 부품에는 역할이 들어</b> 있습니다. <code>Box</code>로만 화면을 만들면 웹에서 div로만 쌓을 때와 같은 문제가 생깁니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>표준 부품을 쓰면 역할이 기본으로 들어오고, 직접 그리면 역할을 직접 짜야 한다</b>는 점이 같습니다. 그래서 \"이거 div로 만들었어요\"와 \"Box로 그렸어요\"는 같은 상황을 말하고, 그 뒤에 해야 할 일도 같습니다.",
  siblings=siblings("semantics"),
  related='''        <li><a href="../items/keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/hierarchy.html"><b>글자 위계</b><em>3부</em></a></li>''',
)
