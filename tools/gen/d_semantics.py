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
  desc="시맨틱 태그가 주는 구역 목록·역할·키보드 동작과, div 로만 쌓았을 때 무엇이 사라지는지 보여주는 항목.",
  lede="태그 이름이 <b>그 자리의 뜻</b>을 말해 주는 것. 역할·키보드 동작·구조를 <b>공짜로</b> 줍니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>아래에 <b>스크린 리더의 구역 목록</b>이 나옵니다. 사용자는 이 목록을 띄워
          '내비게이션으로', '메인으로' 하고 건너뜁니다.<br>
          <b>전부 div 로 바꾸기</b>를 켜 보세요. 화면은 똑같은데 <b>구역 목록이 통째로 비어</b>
          처음부터 끝까지 순서대로 읽는 수밖에 없게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시맨틱 태그, 의미 있는 마크업, 구역"),
    ("영어", "semantic HTML, landmarks, document structure"),
    ("같이 쓰는 말",
     "<code>&lt;header&gt;</code>·<code>&lt;nav&gt;</code>·<code>&lt;main&gt;</code> 같은 큰 구역을 "
     "<b>랜드마크</b>(landmark)라 하고, <code>h1~h6</code>이 만드는 목차를 "
     "<b>제목 구조</b>(heading structure)라 합니다. 태그가 기본으로 갖는 역할은 "
     "<b>암시적 역할</b>(implicit role)입니다."),
    ("자주 잘못 부름",
     "<b>SEO 용</b> — 검색에도 도움이 되지만 <b>본래는 구조를 알리는</b> 것입니다.<br>"
     "<b><code>role</code>을 붙이면 같다</b> — 역할만 같아지고 <b>키보드 동작은 안 따라옵니다</b>.<br>"
     "<b><code>&lt;section&gt;</code></b> — <b>이름이 있어야</b> 구역으로 쳐 줍니다. 그냥 쓰면 div 와 같습니다."),
  ]),
  axes=ax("시맨틱 태그"),
  oneline="<b>ARIA 의 첫 규칙은 \"ARIA 를 쓰지 않는 것\"</b>입니다 — 맞는 태그가 있으면 그걸 씁니다.",
  s4_title="갈래", s4_hint="태그 하나가 주는 것",
  states=states([
    (land("header", "로고와 검색"), "header", "구역 목록에 <b>'배너'</b>로 올라간다"),
    (land("nav", "홈 · 정산 · 설정"), "nav", "<b>'내비게이션'</b>. 여럿이면 각각 이름을 붙인다"),
    (land("main", "정산 목록"), "main", "<b>화면에 하나만.</b> 건너뛰기 링크가 여기로 온다"),
    (land("div", "아무 뜻 없음", True), "div", "<b>구역 목록에 안 올라간다.</b> 순서대로 읽는 수밖에"),
    ('''              <div style="width:100%;max-width:160px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;ul&gt;</span>
                <span style="font-size:11px">· 정산 #4821</span>
                <span style="font-size:11px">· 정산 #4820</span>
                <span style="font-size:9.5px;color:var(--fg-muted);font-family:var(--mono)">"목록, 항목 2개"</span>
              </div>''',
     "ul · ol", "<b>몇 건인지</b>가 저절로 읽힌다"),
    ('''              <div style="width:100%;max-width:160px;display:grid;gap:3px">
                <span style="font-size:13px;font-weight:800">h1 정산</span>
                <span style="font-size:11.5px;font-weight:700;padding-left:8px">h2 이번 주</span>
                <span style="font-size:11px;padding-left:16px">h3 모란상회</span>
              </div>''',
     "h1 ~ h6", "제목만 따라 훑어 <b>목차처럼</b> 쓴다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("배너", "&lt;header&gt;", "화면 맨 위. 로고·검색·계정"),
    ("내비게이션", "&lt;nav&gt;", "길 안내 묶음. <b>여럿이면 이름을 붙인다</b>"),
    ("메인", "&lt;main&gt;", "그 화면의 본문. <b>하나만</b> 두고, 건너뛰기 링크가 여기로 온다"),
    ("제목 구조", "h1 ~ h6", "<b>건너뛰지 않는다.</b> 보이는 크기는 CSS 가 따로 정한다"),
    ("목록", "&lt;ul&gt; · &lt;ol&gt;", "'항목 12개'가 저절로 읽힌다. <code>&lt;div&gt;</code>로 쌓으면 몇 건인지 모른다"),
    ("div 만 쌓기", "&lt;div&gt;", "<b>구역 목록이 빈다.</b> 처음부터 끝까지 읽는 수밖에 없다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          태그 하나가 <b>세 가지를 한꺼번에</b> 줍니다 — 역할(이게 무엇인가) ·
          동작(키보드로 눌리는가) · 구조(목록·목차에 들어가는가).
          <code>role</code>로 흉내 내면 <b>역할 하나만</b> 따라오고 나머지 둘은 직접 짜야 합니다.
          그래서 <b>태그를 고르는 일이 접근성의 8할</b>이라는 말이 나옵니다.</p>''',
  do=ul([
    "<b>모든 화면</b> — 틀을 잡을 때 태그부터 고릅니다",
    "누를 것은 <code>&lt;button&gt;</code>, 이동은 <code>&lt;a href&gt;</code>",
    "반복되는 것은 <code>&lt;ul&gt;</code>·<code>&lt;ol&gt;</code>",
    "<code>&lt;nav&gt;</code>가 여럿이면 각각 <code>aria-label</code>",
  ]),
  dont=ul([
    "<b>전부 <code>&lt;div&gt;</code></b>로 쌓는 것",
    "<code>&lt;main&gt;</code>을 여러 개 두는 것",
    "<code>h1</code> 다음에 <code>h4</code>로 뛰는 것 — 목차가 엉킵니다",
    "<b>배치 때문에</b> <code>&lt;table&gt;</code>을 쓰는 것 — '표, 3열 5행'으로 읽힙니다",
  ]),
  instead='키보드로 되는지는 <a href="keyboard.html">키보드 조작</a>, 역할·상태는 <a href="screenreader.html">스크린 리더가 읽는 것</a>, 보이는 위계는 <a href="../items/hierarchy.html">글자 위계</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                ''' + land("header", "로고 · 검색", False, "100%").replace('              ','') +
       land("nav", "홈 · 정산 · 설정", False, "100%").replace('              ','') +
       land("main", "정산 목록", False, "100%").replace('              ','') + '''
              </div>''',
     "화면 뼈대", "이 셋만 있어도 <b>구역 목록이 생긴다</b>"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;nav aria-label="주 메뉴"&gt;</span>
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--accent)">&lt;nav aria-label="빵부스러기"&gt;</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">둘 다 '내비게이션'이면 구별이 안 된다</span>
              </div>''',
     "nav 가 여럿", "<b>각각 이름</b>을 붙인다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="font-family:var(--mono);font-size:9.5px;color:var(--danger)">&lt;div onclick&gt;저장&lt;/div&gt;</span>
                <span style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c">&lt;button&gt;저장&lt;/button&gt;</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">아래 한 줄이 다섯 가지를 대신한다</span>
              </div>''',
     "버튼", "<b>태그 하나로</b> 역할·포커스·Enter·Space·비활성이 온다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="태그부터 고른다",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="틀을 잡을 때 <b>태그부터</b> 고릅니다. CSS 는 그다음입니다.",
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
    ("태그부터 고른다", "<b>역할·동작·구조</b>가 한꺼번에 온다"),
    ("<code>&lt;main&gt;</code>은 하나", "건너뛰기 링크의 목적지"),
    ("제목을 건너뛰지 않는다", "h1 → h2 → h3. 보이는 크기는 CSS 로 따로"),
    ("<code>&lt;nav&gt;</code>가 여럿이면 이름", "<code>aria-label</code>로 구별한다"),
    ("<code>&lt;section&gt;</code>에는 이름", "이름 없는 section 은 <b>div 와 같다</b>"),
    ("배치에 <code>&lt;table&gt;</code>을 안 쓴다", "'표, 3열 5행'으로 읽힌다"),
  ]),
  backend=rows([
    ("템플릿에서 한 번", "레이아웃 컴포넌트에 <code>&lt;header&gt;</code>·<code>&lt;main&gt;</code>을 박아 두면 <b>모든 화면이 공짜로</b> 따라옵니다."),
    ("제목 단계는 화면이 정한다", "같은 컴포넌트가 어떤 화면에서는 <code>h2</code>, 어떤 화면에서는 <code>h3</code>입니다. <b>단계를 props 로</b> 받는 설계가 흔합니다."),
    ("SEO 와 겹친다", "구조가 또렷하면 검색 엔진도 잘 읽습니다 — <b>같은 작업으로 두 가지</b>가 해결됩니다."),
    ("자동 검사", "랜드마크 유무, <code>h1</code> 개수, 제목 단계 건너뜀은 <b>전부 자동으로</b> 잡힙니다. CI 에 넣기 쉬운 쪽입니다."),
  ]),
  plat_lede="앱에는 '태그'가 없고 <b>부품 자체가 역할</b>을 갖습니다.",
  plats=plats([
    ("웹", "HTML 태그",
     land("main", "정산 목록", False, "120px"),
     "태그 이름이 곧 역할입니다. <b>div 로만 쌓는 것</b>이 웹 특유의 사고입니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Button { }<br>List { }<br>.accessibilityHeading</div>''',
     "<b>표준 부품을 쓰면</b> 역할이 따라옵니다. 직접 그린 뷰에만 역할을 적어 줍니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Button { }<br>LazyColumn { }<br>semantics { heading( ) }</div>''',
     "역시 <b>표준 부품에 역할이 들어</b> 있습니다. <code>Box</code>로만 만들면 웹의 div 와 같은 문제가 생깁니다."),
  ]),
  plat_note="세 쪽 다 <b>\"표준 부품을 쓰면 공짜, 직접 그리면 직접 짜야 한다\"</b>가 같습니다. 그래서 \"이거 div 로 만들었어요\"와 \"Box 로 그렸어요\"는 같은 말이고, 뒤따르는 할 일도 같습니다.",
  siblings=siblings("semantics"),
  related='''        <li><a href="../items/keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/hierarchy.html"><b>글자 위계</b><em>3부</em></a></li>''',
)
