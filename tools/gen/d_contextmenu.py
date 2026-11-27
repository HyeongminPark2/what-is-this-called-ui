# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def cm(label, note="", ok=None, w="152px", dots=True, menu=True, at=(40, 22)):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    rows_ = ''.join('<span style="display:flex;gap:5px;align-items:center;border:1px solid var(--line);'
                    'border-radius:3px;background:var(--surface);padding:2px 5px;font-size:7.5px">'
                    '<span>' + n + '</span>'
                    + ('<span style="margin-left:auto;color:var(--fg-muted)">⋯</span>' if dots else '')
                    + '</span>' for n in ['영수증_01.jpg', '영수증_02.jpg', '정산내역.pdf'])
    mbox = ('<span style="position:absolute;left:' + str(at[0]) + 'px;top:' + str(at[1]) + 'px;'
            'border-radius:5px;background:var(--surface);border:1px solid var(--line);padding:3px;'
            'min-width:72px;box-shadow:0 6px 16px rgba(20,22,26,.16);z-index:3">'
            '<span style="display:block;padding:2px 5px;font-size:7px;border-radius:2px;'
            'background:var(--accent-soft);color:var(--accent)">열기</span>'
            '<span style="display:block;padding:2px 5px;font-size:7px">이름 바꾸기</span>'
            '<span style="display:block;border-top:1px solid var(--line);margin:2px 0"></span>'
            '<span style="display:block;padding:2px 5px;font-size:7px;color:var(--danger)">지우기</span>'
            '</span>') if menu else ''
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden;padding:5px">'
            '<span style="display:grid;gap:3px">' + rows_ + '</span>' + mbox + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">오른쪽 누르기 · 길게 누르기로만 열림</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">그래서 있는 줄 모르고 지나치기 쉬움</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">⋯ 단추를 같이 두어 보이는 길을 만듦</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">누른 자리에 뜨고 가장자리에서는 비켜남</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">브라우저 기본 메뉴를 막으면 그 기능을 못 씀</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">Shift+F10으로 키보드에서도 열 수 있어야 함</div>
                </div>
              </div>'''

D = dict(
  slug="contextmenu", ko="컨텍스트 메뉴", en="Context menu",
  desc="마우스 오른쪽 버튼이나 길게 누르기로 여는 메뉴입니다. 여는 길이 화면에 보이지 않아 생기는 문제와 브라우저 기본 메뉴를 막을 때 생기는 일을 다룹니다.",
  lede="컨텍스트 메뉴는 마우스 오른쪽 버튼으로 누르거나 손가락으로 길게 누른 <b>그 자리</b>에 뜨는 메뉴입니다. 화면에 여는 단추가 보이지 않고 그 동작으로만 열리기 때문에, 사용자가 <b>메뉴가 있는 줄도 모르고</b> 지나치기 쉽습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목록의 줄 위에서 <b>마우스 오른쪽 버튼</b>을 눌러 보세요(폰에서는 길게 누릅니다).
          같은 메뉴를 여는 <b>길이 몇 개인지</b> 데모가 세어 적습니다.<br>
          ⋯ 단추를 함께 두면 메뉴를 여는 길이 둘이 되고, ⋯ 단추를 끄면 눈에 보이지 않는 오른쪽 버튼 하나만 남습니다.
          그래서 <b>숨은 길만 두지 않는 것</b>이 규칙입니다.<br>
          브라우저 기본 메뉴를 막으면 사용자는 그 메뉴에 있던 복사나 새 탭으로 열기를 <b>쓸 수 없게</b> 됩니다.
          그러니 정말 필요할 때만 막고, 막았다면 <b>우리 메뉴 안에 그 기능들을 다시 넣어</b> 줘야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "컨텍스트 메뉴, 오른쪽 메뉴, 마우스 우클릭 메뉴"),
    ("영어", "context menu, right-click menu, long-press menu"),
    ("같이 쓰는 말",
     "폰에서는 <b>길게 누르기</b>(long press)로 같은 메뉴를 엽니다. "
     "iOS에서는 미리보기를 함께 띄우는 <b>콘텍스트 메뉴</b>가 정식 부품이고, "
     "안드로이드에는 여러 항목을 고를 때 쓰는 <b>컨텍스추얼 액션 바</b>가 따로 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>드롭다운 메뉴</b> — 단추를 눌렀을 때 그 <b>단추에 붙어</b> 열리면 컨텍스트 메뉴가 아니라 <a href=\"menu.html\">드롭다운 메뉴</a>입니다.<br>"
     "<b>액션 시트</b> — 화면 <b>아래에서</b> 올라오는 동작 목록은 <a href=\"actionsheet.html\">액션 시트</a>입니다.<br>"
     "<b>팝오버</b> — 메뉴 항목만이 아니라 <b>아무 내용</b>이나 담을 수 있는 상자는 <a href=\"popover.html\">팝오버</a>입니다."),
  ]),
  states=states([
    (cm("", "줄마다 ⋯ 단추가 있음", True, "152px", True, False), "닫혀 있을 때", "줄마다 ⋯ 단추가 있어 메뉴를 여는 <b>보이는 길</b>이 있습니다"),
    (cm("", "누른 자리에 뜸", True), "누른 자리에 열렸을 때", "메뉴가 <b>누른 자리</b>에 뜹니다"),
    (cm("", "가장자리에서는 안쪽으로 비켜남", True, "152px", True, True, (70, 10)),
     "화면 가장자리에서 열 때", "화면 가장자리에서는 메뉴가 <b>잘리지 않도록</b> 안쪽으로 비켜 뜹니다"),
    (cm("", "⋯ 단추가 없어 여는 길이 하나뿐", False, "152px", False, False), "숨은 길만 있을 때", "⋯ 단추가 없어서 오른쪽 버튼을 <b>모르는 사람은</b> 메뉴를 열 수 없습니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">브라우저 기본 메뉴를 막음</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">복사 · 새 탭으로 열기를 못 씀</span>'),
         "기본 메뉴 막음", False, "", "152px"),
     "기본 메뉴를 막았을 때", "브라우저 메뉴에 있던 복사와 새 탭으로 열기를 <b>쓸 수 없게</b> 됩니다"),
    (one(txt('<span style="display:block;font-size:8px">Shift + F10</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">키보드로도 열림</span>'),
         "키보드", True, "", "152px"),
     "키보드로 열 때", "키보드로 여는 <b>길이 하나 더</b> 생깁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("여는 방법", "오른쪽 버튼 · 길게 누르기", "마우스 오른쪽 버튼을 누르거나 길게 누르는 <b>동작으로만</b> 열립니다"),
    ("숨은 길", "모르면 못 씀", "컨텍스트 메뉴의 가장 큰 약점으로, 여는 길이 화면에 보이지 않아 모르는 사람은 메뉴가 있는 줄도 모릅니다"),
    ("⋯ 단추", "보이는 길", "눈에 보이는 여는 길로 ⋯ 단추를 <b>함께</b> 둡니다"),
    ("자리", "누른 곳", "누른 자리에 뜨되, 화면 가장자리에서는 잘리지 않게 안쪽으로 <b>비켜납니다</b>"),
    ("기본 메뉴", "막으면 기능을 잃음", "막으면 브라우저 메뉴에 있던 복사와 새 탭으로 열기를 쓸 수 없게 됩니다"),
    ("키보드", "Shift + F10", "마우스 없이 메뉴를 여는 길이 <b>하나 더</b> 생깁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          브라우저 기본 메뉴를 막을지는 <b>신중하게</b> 정해야 합니다.
          기본 메뉴에는 복사, 붙여넣기, 새 탭으로 열기, 이미지 저장처럼
          <b>사용자가 당연히 있으리라 기대하는</b> 기능이 들어 있는데,
          기본 메뉴를 막으면 이 기능들을 모두 쓸 수 없게 됩니다.
          그래서 꼭 막아야 한다면 <b>우리 메뉴 안에 그 기능들을 다시 넣어</b> 줘야 합니다.<br>
          키보드로는 <b>Shift + F10</b>(또는 메뉴 키)을 눌러 컨텍스트 메뉴를 엽니다.
          이 키까지 처리해 두는 경우는 드물지만, 처리해 두면 마우스 없이도 같은 일을 할 수 있습니다.
          다만 키 처리보다 더 쉬운 방법은 <b>⋯ 단추를 두는 것</b>입니다.</p>''',
  do_title="컨텍스트 메뉴를 만들 때 지킬 것",
  dont_title="컨텍스트 메뉴를 만들 때 피할 것",
  do=ul([
    "<b>⋯ 단추</b>를 함께 두어 메뉴를 여는 보이는 길 만들기",
    "화면 가장자리에서는 메뉴를 <b>안쪽으로 비켜</b> 띄우기",
    "기본 메뉴를 막는다면 <b>그 기능들을</b> 우리 메뉴에 <b>다시</b> 넣기",
  ]),
  dont=ul([
    "컨텍스트 메뉴에만 기능을 두기. 오른쪽 버튼을 <b>모르는 사람은</b> 그 기능을 쓸 수 없습니다",
    "<b>아무 데서나</b> 기본 메뉴 막기",
    "폰에서 길게 누르기를 <b>드래그와 겹치게</b> 두기",
    "메뉴가 <b>화면 밖으로</b> 넘쳐 잘리게 두기",
  ]),
  instead='눈에 보이는 단추에 붙여 열려면 <a href="menu.html">드롭다운 메뉴</a>를 쓰고, 화면 아래에서 올라오게 하려면 <a href="actionsheet.html">액션 시트</a>가 맞습니다. 동작 목록이 아닌 다른 내용까지 담으려면 <a href="popover.html">팝오버</a>를 쓰고, 여러 줄을 골라 한꺼번에 처리하는 방법은 <a href="bulk.html">일괄 선택</a>에서 다룹니다.',
  cases=cases([
    (cm("", "", True, "150px", True, False), "파일 목록에서 쓰기", "오른쪽 버튼 메뉴를 <b>⋯ 단추와 함께</b> 둡니다"),
    (cm("", "", True, "150px", False, True), "편집기에서 쓰기", "사용자가 <b>오른쪽 버튼 메뉴</b>에 익숙해서 먼저 찾아보는 자리입니다"),
    (one(txt('<span style="display:block;font-size:8px">길게 누름</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">폰에서는 시트로 올라옴</span>'),
         "폰", True, "", "150px"),
     "폰에서 길게 누를 때", "폰에서는 메뉴 대신 <a href=\"actionsheet.html\">액션 시트</a>로 바꿔 띄웁니다"),
  ]),
  code_lede="<code>contextmenu</code> 이벤트를 받아 우리 메뉴를 띄우되, 브라우저 기본 메뉴를 <b>막을지는 신중하게</b> 정합니다.",
  code='''&lt;<span class="t">li</span>&gt;
  영수증_2411_01.jpg
  &lt;<span class="t">button</span> <span class="a">aria-haspopup</span>=<span class="s">"menu"</span>
          <span class="a">aria-label</span>=<span class="s">"영수증_2411_01.jpg 메뉴 열기"</span>&gt;⋯&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">li</span>&gt;

row.addEventListener(<span class="s">'contextmenu'</span>, e =&gt; {
  e.preventDefault();          <span class="c">// 브라우저 기본 메뉴를 막는다. 꼭 필요할 때만</span>
  openMenu(e.clientX, e.clientY);
});

<span class="c">// 키보드로도 열 수 있게 한다</span>
row.addEventListener(<span class="s">'keydown'</span>, e =&gt; {
  <span class="t">if</span> (e.key === <span class="s">'ContextMenu'</span> || (e.shiftKey &amp;&amp; e.key === <span class="s">'F10'</span>)) {
    e.preventDefault();
    <span class="t">const</span> r = row.getBoundingClientRect();
    openMenu(r.left, r.bottom);
  }
});''',
  keys=kbd([
    ("Shift + F10 · 메뉴 키", "키보드로 컨텍스트 메뉴를 여는 <b>표준 방법</b>입니다"),
    ("↑ ↓", "메뉴 항목 사이로 초점을 옮깁니다"),
    ("Esc", "메뉴를 닫고 초점을 메뉴를 열었던 <b>그 줄로</b> 돌려놓습니다"),
    ("<code>aria-haspopup</code>", "⋯ 단추에 붙여, 누르면 메뉴가 열리는 단추라고 알립니다"),
    ("폰에서 길게 누를 때", "폰에서는 <b>드래그와 겹치지 않도록</b> 누르고 있어야 하는 시간을 둡니다"),
    ("확인하는 방법", "마우스를 쓰지 않고도 <b>같은 일을 할 수 있는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("권한에 따라 지우는 항목", "줄마다 사용자 권한이 다르면 할 수 없는 동작은 메뉴에서 <b>항목을 지웁니다</b>. <a href=\"menu.html\">드롭다운 메뉴</a>와 같은 방식입니다."),
    ("여러 줄을 고른 뒤 열 때", "여러 줄을 고른 상태에서 메뉴를 열면 고른 줄 전체에 적용하는 <b>묶음 동작</b>이 떠야 합니다. 이 부분은 <a href=\"bulk.html\">일괄 선택</a>과 이어집니다."),
  ]),
  plat_lede="컨텍스트 메뉴를 <b>여는 동작</b>은 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "contextmenu 이벤트",
     cm("", "", True, "110px", True, True, (34, 18)),
     "브라우저 기본 메뉴를 <b>막을지 말지</b>를 늘 따져 봐야 합니다."),
    ("iOS", "Context Menu (길게 누르기)",
     '''              <div class="phone" role="img" aria-label="iOS 컨텍스트 메뉴 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 30%, transparent)"></div>
                <div style="position:absolute;left:6px;right:6px;top:22px;height:16px;border-radius:4px;background:var(--surface)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:18px;border-radius:4px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "길게 누르면 <b>미리보기와 메뉴</b>가 함께 뜨는 정식 부품이 있습니다."),
    ("안드로이드", "길게 누르기 + 액션 바",
     '''              <div class="phone" role="img" aria-label="안드로이드 선택 모드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:18px;height:11px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "길게 누르면 <b>선택 모드</b>로 들어가 앱바가 동작 모음으로 바뀝니다."),
  ]),
  plat_note="안드로이드는 길게 누르기를 <b>선택 모드</b>에 쓴다는 점에서 다른 두 플랫폼과 크게 다릅니다. 한 줄을 길게 누르면 그 줄이 선택되면서 앱바가 '지우기·공유' 같은 동작 모음으로 바뀌고, 다른 줄을 더 고를 수도 있습니다. 그래서 웹에서 폰 폭 화면을 만들 때 <b>길게 누르기를 메뉴로 쓸지 선택으로 쓸지</b> 정해 두지 않으면, 메뉴와 선택이 같은 동작을 두고 부딪힙니다. 대부분은 <b>⋯ 단추를 누르면 액션 시트가 올라오는</b> 방식이 덜 헷갈립니다.",
  siblings=siblings("contextmenu"),
  related='''        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><a href="actionsheet.html"><b>액션 시트</b><em>6부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="gesture.html"><b>제스처</b><em>9부</em></a></li>''',
)
