# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(tag, ok_focus, ok_key, note, w="168px"):
    mark = lambda v: ('<span style="color:#1f8a4c;font-weight:700">○</span>' if v
                      else '<span style="color:var(--danger);font-weight:700">✕</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:6px;justify-items:center">'
            '<span style="display:inline-block;background:var(--accent);color:#fff;border-radius:6px;'
            'padding:6px 12px;font-size:11.5px;font-weight:700">저장하기</span>'
            '<span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted)">' + tag + '</span>'
            '<span style="font-size:10.5px">Tab ' + mark(ok_focus) + ' &nbsp; Enter ' + mark(ok_key) + '</span>'
            '<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:inline-block;background:var(--accent);color:#fff;border-radius:6px;padding:8px 14px;font-size:12.5px;font-weight:700;justify-self:start">저장하기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">&lt;button&gt;   — 포커스·Enter·Space 가 공짜</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">&lt;div onclick&gt;   — 키보드로 아예 못 간다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">tabindex="0" + role="button"   — 갈 수는 있다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">keydown: Enter · Space   — 직접 짜야 한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">화살표 · Esc · Home/End   — 부품마다 약속이 있다</div>
                </div>
              </div>'''

D = dict(
  slug="keyboard", ko="키보드 조작", en="Keyboard operability",
  desc="마우스 없이 전부 되는지, div 로 만든 버튼이 왜 안 되는지를 실물로 보여주는 항목.",
  lede="<b>마우스 없이도 전부 되어야</b> 한다는 것. 손을 못 쓰는 사람뿐 아니라 마우스가 고장 난 사람에게도 해당합니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 가지가 똑같아 보이는데 <b>키보드로는 전혀 다릅니다.</b>
          마우스를 쓰지 말고 <kbd>Tab</kbd>·<kbd>Enter</kbd>·<kbd>Space</kbd>로만 해 보세요.<br>
          <code>&lt;div&gt;</code>는 <b>Tab 이 아예 지나가고</b>, <code>tabindex</code>를 더하면 갈 수는 있는데
          <b>Enter·Space 가 안 먹습니다</b>. 기록에 '아무 일도 안 일어남'이 찍히는 것이 그 순간입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "키보드 조작, 키보드 접근성, 키보드만으로"),
    ("영어", "keyboard operability, keyboard accessibility, keyboard trap"),
    ("같이 쓰는 말",
     "빠져나올 수 없게 갇히는 것을 <b>키보드 트랩</b>(keyboard trap)이라 하고 — "
     "<a href=\"focustrap.html\">포커스 트랩</a>과 달리 <b>나쁜 뜻</b>입니다. "
     "부품마다 정해진 키 약속을 <b>키보드 인터랙션 패턴</b>(ARIA Authoring Practices)이라 합니다."),
    ("자주 잘못 부름",
     "<b>단축키</b> — 단축키는 <b>빠르게</b> 하는 것이고, 키보드 조작은 <b>되기는 하는가</b>입니다.<br>"
     "<b>포커스</b> — 포커스는 '어디 있는가', 키보드 조작은 '<b>거기서 뭘 할 수 있는가</b>'입니다.<br>"
     "<b>키보드 트랩</b> — 못 빠져나오는 사고입니다. 모달의 포커스 트랩과 헷갈리면 안 됩니다."),
  ]),
  axes=ax("키보드 조작"),
  oneline="규칙은 하나입니다 — <b>누를 것은 <code>&lt;button&gt;</code>, 이동은 <code>&lt;a href&gt;</code></b>. div 로 만들면 다섯 가지를 직접 짜야 합니다.",
  s4_title="갈래", s4_hint="같은 모양, 다른 속",
  states=states([
    (row("&lt;button&gt;", True, True, "공짜로 다 된다"), "진짜 버튼", "<b>포커스·Enter·Space·비활성</b>이 다 따라온다"),
    (row("&lt;div onclick&gt;", False, False, "키보드로 못 간다"), "div + onclick", "<b>Tab 이 지나간다.</b> 마우스로만 쓸 수 있다"),
    (row("div + tabindex", True, False, "갈 수는 있다"), "+ tabindex", "<b>Enter·Space 가 안 먹는다.</b> 직접 짜야 한다"),
    (row("+ keydown", True, True, "겨우 비슷해졌다"), "+ 키 처리", "여기까지 와야 버튼 흉내가 난다 — <b>그냥 button 을 쓰면 된다</b>"),
    (row("&lt;a&gt; (href 없음)", False, False, "링크가 아니다"), "href 없는 a", "<code>href</code> 없는 <code>&lt;a&gt;</code>는 <b>포커스를 못 받는다</b>"),
    (row("&lt;button disabled&gt;", False, False, "일부러 뺀 것"), "비활성", "포커스를 <b>일부러</b> 안 받는다 — 이건 맞는 동작"),
  ]),
  anat=ANAT,
  pins=pins([
    ("누를 것", "button", "<b>원래 태그를 쓰면</b> 아래 다섯 줄이 전부 공짜다"),
    ("태그가 주는 것", "&lt;button&gt;", "포커스 순서 · Enter · Space · 역할 · 비활성 처리"),
    ("div 로 만들면", "&lt;div onclick&gt;", "<b>Tab 이 아예 안 간다.</b> 마우스 전용이 된다"),
    ("순서에 넣기", "tabindex=\"0\" + role", "갈 수는 있게 된다. <b>아직 눌리지는 않는다</b>"),
    ("키 처리", "keydown", "Enter 와 Space 를 <b>직접</b> 받아 click 을 만들어야 한다"),
    ("부품별 약속", "화살표 · Esc · Home/End", "탭·라디오·메뉴마다 <b>정해진 키</b>가 있다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>&lt;div&gt;</code>로 버튼을 만들면 챙길 것이 <b>다섯 가지</b>입니다 —
          <code>tabindex</code> · <code>role</code> · Enter · Space · 비활성 처리.
          거기에 <b>Space 는 기본으로 화면을 스크롤</b>하므로 <code>preventDefault()</code>도 필요합니다.
          전부 맞춰도 <code>&lt;button&gt;</code> 한 글자보다 나은 점이 없습니다 —
          그래서 이 항목의 결론은 언제나 <b>"원래 태그를 쓰세요"</b>입니다.</p>''',
  do=ul([
    "<b>모든 화면</b> — 마우스를 치우고 한 번 끝까지 해 봅니다",
    "부품을 새로 만들 때 — <b>원래 태그</b>가 있는지 먼저 찾습니다",
    "탭·메뉴·라디오처럼 <b>화살표로 도는</b> 부품을 만들 때",
  ]),
  dont=ul([
    "<code>&lt;div&gt;</code>·<code>&lt;span&gt;</code>에 <code>onclick</code>만 거는 것",
    "<b>빠져나올 수 없게</b> 만드는 것(키보드 트랩) — 가장 심각한 사고입니다",
    "마우스 전용 동작만 두는 것 — 호버로만 열리는 메뉴, 드래그로만 되는 정렬",
    "<code>tabindex</code>에 1 이상을 주는 것",
  ]),
  instead='어디 있는지 보이게 하려면 <a href="focus.html">포커스</a>, 모달 안에 가두려면 <a href="focustrap.html">포커스 트랩</a>, 태그 고르기는 <a href="semantics.html">시맨틱 태그</a>.',
  cases=cases([
    (row("&lt;button&gt;", True, True, "", "190px"), "버튼", "<b>이것 하나면 끝난다</b>"),
    ('''              <div style="width:100%;max-width:190px;display:flex;gap:10px;border-bottom:1px solid var(--line);padding-bottom:4px">
                <span style="font-size:11px;color:var(--accent);font-weight:700;border-bottom:2px solid var(--accent);padding-bottom:4px;margin-bottom:-5px">개요</span>
                <span style="font-size:11px;color:var(--fg-muted)">거래</span>
                <span style="font-size:11px;color:var(--fg-muted)">정산</span>
              </div>
              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);margin-top:7px;text-align:center">Tab 한 번 + ← → 로 이동</div>''',
     "탭", "<b>로빙 탭인덱스</b> — 줄 전체가 Tab 한 번이고 안에서는 화살표"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:5px">
                <span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px">서울특별시</span>
                <span style="font-size:10px;color:var(--fg-muted);font-family:var(--mono)">↑↓ 이동 · Enter 고르기 · Esc 닫기</span>
              </div>''',
     "콤보박스", "부품마다 <b>정해진 키 약속</b>이 있다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="원래 태그를 쓰면 공짜",
  code_lede="가장 짧은 답은 <b>태그를 바꾸는 것</b>입니다. 굳이 div 로 만들 때 필요한 줄들을 아래에 적어 뒀습니다.",
  code='''<span class="c">&lt;!-- 이 한 줄이면 끝난다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span>&gt;저장하기&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 굳이 div 로 만든다면 이만큼이 필요하다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"button"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>
     <span class="a">aria-disabled</span>=<span class="s">"false"</span>&gt;저장하기&lt;/<span class="t">div</span>&gt;

el.addEventListener(<span class="s">'keydown'</span>, (e) =&gt; {
  <span class="t">if</span> (e.key === <span class="s">'Enter'</span> || e.key === <span class="s">' '</span>) {
    e.preventDefault();      <span class="c">// Space 는 기본이 '화면 스크롤'이다</span>
    el.click();
  }
});''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "다음 누를 것으로. <b>보이는 순서와 같아야</b> 한다"),
    ("<kbd>Enter</kbd>", "버튼·링크를 누른다"),
    ("<kbd>Space</kbd>", "버튼·체크박스를 누른다. <b>기본은 화면 스크롤</b>이라 막아야 한다"),
    ("<kbd>Esc</kbd>", "모달·메뉴·콤보박스를 닫는다"),
    ("<kbd>←</kbd><kbd>→</kbd><kbd>↑</kbd><kbd>↓</kbd>", "탭·라디오·메뉴 <b>안에서</b> 움직인다"),
    ("<kbd>Home</kbd><kbd>End</kbd>", "목록의 처음·끝으로"),
  ]),
  backend=rows([
    ("테스트가 가장 쉽다", "접근성 항목 중 <b>직접 해 보기가 가장 쉽습니다</b> — 마우스를 치우고 화면을 끝까지 써 보면 됩니다. 도구도 지식도 필요 없습니다."),
    ("자동 검사", "Playwright 로 <kbd>Tab</kbd>을 눌러 가며 <code>activeElement</code>를 기록하면 '누를 수 있는데 Tab 이 안 가는 것'을 <b>CI 에서</b> 잡을 수 있습니다."),
    ("컴포넌트 라이브러리", "직접 만들기 전에 <b>키 약속이 구현된 라이브러리</b>를 찾는 편이 거의 늘 낫습니다. 콤보박스 하나에만 키 처리가 열 줄 넘게 들어갑니다."),
    ("드래그로만 되는 것", "순서 바꾸기를 드래그로만 만들면 <b>키보드로는 아예 못 합니다.</b> '위로/아래로' 버튼을 함께 둡니다."),
  ]),
  plat_lede="두 OS 는 <b>키보드 말고도</b> 다른 조작 수단이 있어 범위가 더 넓습니다.",
  plats=plats([
    ("웹", "기본 태그",
     row("&lt;button&gt;", True, True, "", "120px"),
     "<code>&lt;button&gt;</code>·<code>&lt;a href&gt;</code>가 전부 해 줍니다. <b>div 로 만들 때만</b> 문제가 생깁니다."),
    ("iOS", "VoiceOver · 스위치 제어",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Button { }<br>.accessibilityAction</div>''',
     "키보드보다 <b>VoiceOver 제스처</b>와 <b>스위치 제어</b>가 주된 수단입니다. 표준 부품을 쓰면 따라옵니다."),
    ("안드로이드", "TalkBack · 스위치",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Modifier.clickable<br>onClickLabel</div>''',
     "<code>clickable</code> 을 쓰면 TalkBack 동작이 따라옵니다. <b>직접 그린 터치 영역</b>은 안 됩니다."),
  ]),
  plat_note="앱에서는 '키보드'보다 <b>스크린 리더 제스처와 스위치 제어</b>가 주인공입니다. 그래서 같은 요구가 웹에서는 \"Tab 으로 되나요\", 앱에서는 \"VoiceOver 로 되나요\"로 나옵니다 — <b>뜻은 같습니다</b>.",
  siblings=siblings("keyboard"),
  related='''        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/semantics.html"><b>시맨틱 태그</b><em>12부</em></a></li>
        <li><a href="../items/combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>''',
)
