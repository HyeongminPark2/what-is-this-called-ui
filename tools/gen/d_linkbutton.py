# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def r(items, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = ''.join('<span style="display:flex;gap:5px;align-items:center;border:1px solid '
                  + ('var(--danger)' if bad else 'var(--line)') + ';border-radius:4px;'
                  'background:var(--surface);padding:3px 6px;font-size:8px">'
                  '<span style="' + ('color:var(--accent);text-decoration:underline;' if tag == 'a' else '') + '">'
                  + name + '</span>'
                  '<span style="margin-left:auto;font-family:var(--mono);font-size:7px;color:'
                  + ('var(--danger)' if bad else 'var(--fg-muted)') + '">' + tag + '</span></span>'
                  for name, tag, bad in items)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:3px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);padding:5px">' + out + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">주소가 바뀌면 &lt;a href&gt; — 이동</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">그 자리에서 일이 일어나면 &lt;button&gt; — 동작</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">링크는 새 탭 · 복사 · 공유가 된다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">버튼은 Space 로도 눌린다 — 링크는 Enter 만</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">div + onclick — Tab 이 안 멈추고 Enter 가 안 먹는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">생김새는 자유다 — 뜻만 지킨다</div>
                </div>
              </div>'''

D = dict(
  slug="linkbutton", ko="링크와 버튼", en="Link vs button",
  desc="이동인가 동작인가로 태그를 가르는 규칙. div+onclick의 대가와 서로 바꿔 썼을 때의 증상.",
  lede="가르는 질문은 하나입니다 — <b>이동인가, 동작인가</b>. 생김새는 자유지만 <b>태그는 뜻을 따라야</b> 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>주소가 바뀌면 링크(<code>&lt;a href&gt;</code>), 그 자리에서 일이 일어나면 버튼(<code>&lt;button&gt;</code>)입니다.<br>
          <b>div 에 onclick</b> 으로 만들면 보기에는 같지만 <b>Tab 이 멈추지 않고</b> Enter 로도 안 눌립니다 —
          '<b>Tab 으로 훑어보기</b>'를 누르면 초점이 몇 군데 멈추는지 세 줍니다.<br>
          <b>서로 바꿔서</b> 만들면 더 조용히 나쁩니다 — 링크로 만든 '저장'은 <b>새 탭으로 열리고</b>,
          버튼으로 만든 '상세 보기'는 <b>가운데 버튼·복사·공유</b>가 안 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "링크와 버튼, 앵커와 버튼"),
    ("영어", "link vs button, anchor vs button"),
    ("같이 쓰는 말",
     "링크처럼 보이는 버튼을 <b>링크 버튼</b>·<b>텍스트 버튼</b>, "
     "버튼처럼 보이는 링크를 <b>버튼 링크</b>라 부르는데 둘 다 <b>생김새 이야기</b>입니다. "
     "태그 이름으로는 <code>&lt;a&gt;</code>가 <b>앵커</b>, <code>&lt;button&gt;</code>이 버튼입니다."),
    ("자주 잘못 부름",
     "<b>버튼 위계</b> — <a href=\"buttonlevel.html\">버튼 위계</a>는 <b>세기</b>이고 이건 <b>뜻</b>입니다.<br>"
     "<b>CTA</b> — CTA 는 역할 이름이지 태그가 아닙니다.<br>"
     "<b>링크 색</b> — 파란 밑줄은 <b>관습</b>이지 규칙이 아닙니다."),
  ]),
  axes=ax("링크와 버튼"),
  oneline="<b>주소가 바뀌면 링크, 아니면 버튼.</b> 이 한 줄이 전부입니다.",
  states=states([
    (r([("주문 상세 보기", "a", False), ("저장", "button", False)], "", "뜻에 맞다", True),
     "맞게 씀", "<b>뜻대로</b> 썼다"),
    (r([("주문 상세 보기", "button", True), ("저장", "a", True)], "", "서로 바꿔 썼다", False),
     "바꿔 씀", "<b>조용히</b> 나쁘다"),
    (r([("주문 상세 보기", "div", True), ("저장", "div", True)], "", "Tab 이 안 멈춘다", False),
     "<code>div</code> 로", "<b>키보드로 못 쓴다</b>"),
    (one(txt('<span style="display:block;font-size:8px">⌘ + 클릭 · 가운데 버튼</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">링크만 새 탭으로 열린다</span>'),
         "새 탭", True, "", "152px"),
     "새 탭", "<b>링크만</b> 된다"),
    (one(txt('<span style="display:block;font-size:8px">Space 로 눌림</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">버튼만 된다 — 링크는 Enter 만</span>'),
         "키보드", True, "", "152px"),
     "키보드", "<b>키가 다르다</b>"),
    (r([("도움말 보기", "a", False), ("도움말 보기", "button", False)], "", "둘 다 밑줄이어도 된다", None),
     "생김새", "<b>자유</b>다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이동", "<code>&lt;a href&gt;</code>", "주소가 바뀐다"),
    ("동작", "<code>&lt;button&gt;</code>", "그 자리에서 일이"),
    ("링크만", "새 탭 · 복사", "오른쪽 메뉴가 다르다"),
    ("버튼만", "Space", "링크는 <b>Enter 만</b>"),
    ("<code>div</code>", "둘 다 안 됨", "Tab 도 Enter 도"),
    ("생김새", "자유", "<b>뜻만</b> 지킨다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          서로 바꿔 쓰는 것이 <code>div</code> 보다 더 흔하고, 더 조용히 나쁩니다 —
          <b>링크로 만든 '저장'</b>은 가운데 버튼으로 누르면 새 탭에서 열리고,
          거기서 또 저장이 일어납니다.
          <b>버튼으로 만든 '상세 보기'</b>는 링크 주소 복사도, 새 탭으로 열기도 안 됩니다.
          둘 다 평소에는 안 드러나서 <b>오래 남습니다</b>.<br>
          판단이 애매하면 <b>주소창을 보세요</b> — 누른 뒤 주소가 바뀐다면 링크입니다.
          '모달을 연다'는 주소를 바꾸기도 하는데, 그때는 <a href="lightbox.html">라이트박스</a>처럼
          <b>링크로 두는 편</b>이 공유도 되고 뒤로가기도 됩니다.</p>''',
  do=ul([
    "주소가 바뀌면 <b>링크</b>, 아니면 <b>버튼</b>",
    "폼 안의 버튼에는 <b><code>type=\"button\"</code></b> 적기",
    "<code>div</code> 에 <code>onclick</code> 을 달지 않기",
  ]),
  dont=ul([
    "<b>저장</b>을 링크로 만들기 — 새 탭에서 또 저장된다",
    "<b>상세 보기</b>를 버튼으로 만들기 — 복사·새 탭이 안 된다",
    "<code>&lt;a href=\"#\"&gt;</code> 에 <code>onclick</code> — 주소가 더러워진다",
    "<code>role=\"button\"</code> 만 붙이고 <b>키보드를 안 붙이기</b>",
  ]),
  instead='세기는 <a href="buttonlevel.html">버튼 위계</a>, 갈래가 붙으면 <a href="splitbutton.html">분할 버튼</a>, 문구는 <a href="buttontext.html">버튼 문구</a>, 차례는 <a href="order.html">보이는 순서와 읽는 순서</a>.',
  cases=cases([
    (r([("주문 상세 보기", "a", False)], "", "", True, "150px"), "목록의 줄", "<b>링크</b>"),
    (r([("저장", "button", False)], "", "", True, "150px"), "폼의 제출", "<b>버튼</b>"),
    (r([("영수증 내려받기", "a", False)], "", "", True, "150px"), "파일 받기", "주소가 있으니 <b>링크</b>"),
  ]),
  code_lede="생김새는 클래스로, 뜻은 태그로 가릅니다 — 둘은 <b>따로</b>입니다.",
  code='''<span class="c">&lt;!-- 이동 — 버튼처럼 보여도 링크다 --&gt;</span>
&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"btn btn--primary"</span> <span class="a">href</span>=<span class="s">"/orders/2411"</span>&gt;주문 상세 보기&lt;/<span class="t">a</span>&gt;

<span class="c">&lt;!-- 동작 — 링크처럼 보여도 버튼이다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"btn btn--text"</span> <span class="a">type</span>=<span class="s">"button"</span>&gt;도움말 보기&lt;/<span class="t">button</span>&gt;

<span class="c">/* 둘을 같은 모양으로 — 생김새는 클래스가 맡는다 */</span>
.btn { <span class="a">display</span>: inline-flex; <span class="a">align-items</span>: center; <span class="a">justify-content</span>: center;
  <span class="a">min-height</span>: <span class="a">44px</span>; <span class="a">text-decoration</span>: none; <span class="a">font</span>: inherit; <span class="a">cursor</span>: pointer; }

<span class="c">/* ✕ 이건 둘 다 아니다 */</span>
&lt;<span class="t">div</span> <span class="a">onclick</span>=<span class="s">"save()"</span>&gt;저장&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("Enter", "링크와 버튼 <b>둘 다</b> 눌린다"),
    ("Space", "<b>버튼만</b> 눌린다 — 링크에서는 스크롤이 내려간다"),
    ("⌘ · Ctrl + 클릭", "<b>링크만</b> 새 탭으로 열린다"),
    ("<code>type=\"button\"</code>", "폼 안에서 안 적으면 <b>제출</b>이 된다"),
    ("<code>role=\"button\"</code>", "붙였으면 <b>Enter·Space</b>도 손으로 붙여야 한다"),
    ("확인하는 법", "Tab 으로 훑어 <b>멈추지 않는 자리</b>가 있는지 본다"),
  ]),
  backend=rows([
    ("이동이면 주소를", "응답에 <code>url</code> 이 있으면 화면이 <b>링크로</b> 만들 수 있습니다 — id 만 주면 화면이 주소를 지어야 합니다."),
    ("동작이면 결과를", "버튼이 부르는 API 는 <b>무엇이 바뀌었는지</b>를 돌려줘야 <a href=\"partialload.html\">부분 로딩</a>이 됩니다."),
  ]),
  plat_lede="<b>웹에만 있는 구분</b>입니다 — 앱에는 주소가 없습니다.",
  plats=plats([
    ("웹", "&lt;a&gt; vs &lt;button&gt;",
     r([("상세 보기", "a", False), ("저장", "button", False)], "", "", True, "110px"),
     "주소가 있다는 것이 웹의 힘입니다 — <b>공유·새 탭·뒤로가기</b>가 공짜로 됩니다."),
    ("iOS", "NavigationLink vs Button",
     '''              <div class="phone" role="img" aria-label="iOS 이동과 동작 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:28px;font-size:5px;color:var(--fg-muted)">›</div>
                <div style="position:absolute;left:5px;right:5px;bottom:8px;height:10px;border-radius:4px;background:var(--accent)"></div></div></div>''',
     "<code>NavigationLink</code> 가 이동, <code>Button</code> 이 동작입니다 — <b>같은 구분</b>이 있습니다."),
    ("안드로이드", "Navigation vs Button",
     '''              <div class="phone" role="img" aria-label="안드로이드 이동과 동작 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:5px;bottom:8px;width:30px;height:10px;border-radius:999px;background:var(--accent)"></div></div></div>''',
     "화면 이동은 <b>내비게이션</b>, 동작은 <b>버튼</b>으로 코드에서 갈립니다."),
  ]),
  plat_note="앱에도 <b>이동과 동작</b>이라는 구분은 똑같이 있지만, 웹만큼 티가 안 납니다 — 주소가 없어 '새 탭으로 열기'나 '링크 복사'가 애초에 없기 때문입니다. 웹에서 이 구분을 지키면 <b>공짜로 얻는 것</b>이 많습니다: 공유 가능한 주소, 뒤로가기, 가운데 버튼, 검색 엔진. 앱 쪽에서 온 분들이 가장 자주 놓치는 자리이기도 합니다.",
  siblings=siblings("linkbutton"),
  related='''        <li><a href="buttonlevel.html"><b>버튼 위계</b><em>4부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="semantics.html"><b>시맨틱 태그</b><em>12부</em></a></li>
        <li><a href="backnav.html"><b>뒤로가기</b><em>7부</em></a></li>''',
)
