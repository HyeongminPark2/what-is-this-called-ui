# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">오른쪽 누르기 · 길게 누르기로만 열린다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">그래서 있는 줄 모르는 기능이 된다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">⋯ 단추를 같이 두어 보이는 길을 만든다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">누른 자리에 뜬다 — 가장자리에서 비켜난다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">브라우저 기본 메뉴를 막는 것은 빼앗는 일</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">키보드에도 길이 있어야 한다 — Shift+F10</div>
                </div>
              </div>'''

D = dict(
  slug="contextmenu", ko="컨텍스트 메뉴", en="Context menu",
  desc="오른쪽 누르기·길게 누르기로 여는 메뉴. 숨은 길의 함정과 브라우저 기본 메뉴.",
  lede="<b>누른 자리</b>에 뜹니다. 그 방법으로만 열리기 때문에 <b>있는 줄 모르는</b> 기능이 되기 쉽습니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>줄에 <b>마우스 오른쪽</b>을 눌러 보세요(폰에서는 길게 누르기).
          데모가 <b>같은 일에 이르는 길이 몇 개인지</b> 세서 적습니다.<br>
          ⋯ 단추를 같이 두면 길이 둘이 되고, 끄면 하나뿐입니다 —
          <b>숨은 길만 두지 않는 것</b>이 규칙입니다.<br>
          브라우저 기본 메뉴를 막는 것은 <b>빼앗는 일</b>입니다. 복사·새 탭으로 열기를 못 쓰게 되니,
          정말 필요할 때만 막고 <b>그 안에 그 기능들을 다시 넣어</b> 줘야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "컨텍스트 메뉴, 오른쪽 메뉴, 마우스 우클릭 메뉴"),
    ("영어", "context menu, right-click menu, long-press menu"),
    ("같이 쓰는 말",
     "폰에서는 <b>길게 누르기</b>(long press)로 같은 것을 엽니다. "
     "iOS 에서는 미리보기까지 같이 띄우는 <b>콘텍스트 메뉴</b>가 정식 부품이고, "
     "안드로이드에는 여러 개를 고르는 <b>컨텍스추얼 액션 바</b>가 따로 있습니다."),
    ("자주 잘못 부름",
     "<b>드롭다운 메뉴</b> — <a href=\"menu.html\">드롭다운 메뉴</a>는 <b>단추에 붙어</b> 열립니다.<br>"
     "<b>액션 시트</b> — <a href=\"actionsheet.html\">액션 시트</a>는 <b>아래에서</b> 올라옵니다.<br>"
     "<b>팝오버</b> — <a href=\"popover.html\">팝오버</a>는 <b>아무 내용</b>이나 담습니다."),
  ]),
  axes=axis_table("컨텍스트 메뉴"),
  oneline="<b>숨은 길만 두지 마세요.</b> 오른쪽 누르기를 모르는 사람에게는 없는 기능입니다.",
  states=states([
    (cm("", "줄마다 ⋯ 가 있다", True, "152px", True, False), "닫힘", "<b>보이는 길</b>이 있다"),
    (cm("", "누른 자리에 떴다", True), "열림", "<b>누른 자리</b>에"),
    (cm("", "가장자리에서는 안쪽으로 비켜난다", True, "152px", True, True, (70, 10)),
     "가장자리", "<b>잘리지 않게</b> 비킨다"),
    (cm("", "⋯ 가 없다 — 길이 하나뿐", False, "152px", False, False), "숨은 길만", "<b>모르면 없는</b> 기능"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">브라우저 기본 메뉴를 막았다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">복사 · 새 탭으로 열기를 못 쓴다</span>'),
         "기본 메뉴 막음", False, "", "152px"),
     "기본 메뉴를 막음", "<b>빼앗는 일</b>이다"),
    (one(txt('<span style="display:block;font-size:8px">Shift + F10</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">키보드로도 열린다</span>'),
         "키보드", True, "", "152px"),
     "키보드", "<b>길이 하나 더</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("여는 법", "오른쪽 · 길게", "<b>그 방법으로만</b>"),
    ("숨은 길", "모르면 없음", "가장 큰 약점"),
    ("⋯ 단추", "보이는 길", "<b>같이</b> 둔다"),
    ("자리", "누른 곳", "가장자리에서 <b>비켜난다</b>"),
    ("기본 메뉴", "막으면 빼앗음", "복사·새 탭이 사라진다"),
    ("키보드", "Shift + F10", "길이 <b>하나 더</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          브라우저 기본 메뉴를 막을지는 <b>신중하게</b> 정해야 합니다.
          거기에는 복사·붙여넣기·새 탭으로 열기·이미지 저장처럼
          <b>사용자가 당연히 기대하는</b> 것들이 들어 있고,
          막는 순간 그것들이 전부 사라집니다.
          꼭 막아야 한다면 <b>우리 메뉴 안에 그 기능들을 다시 넣어</b> 줘야 합니다.<br>
          키보드에는 <b>Shift + F10</b>(또는 메뉴 키)이라는 길이 있습니다 —
          대부분 안 붙이지만, 붙이면 마우스 없이도 같은 일을 할 수 있습니다.
          물론 그보다 쉬운 답은 <b>⋯ 단추를 두는 것</b>입니다.</p>''',
  do=ul([
    "<b>⋯ 단추</b>를 같이 두어 보이는 길 만들기",
    "가장자리에서 <b>안쪽으로 비키기</b>",
    "기본 메뉴를 막는다면 <b>그 기능들을 다시</b> 넣기",
  ]),
  dont=ul([
    "컨텍스트 메뉴에만 있는 기능 두기 — <b>모르면 없는</b> 기능",
    "<b>아무 데서나</b> 기본 메뉴 막기",
    "폰에서 길게 누르기를 <b>드래그와 겹치게</b> 두기",
    "메뉴를 <b>화면 밖으로</b> 넘기기",
  ]),
  instead='단추에 붙으면 <a href="menu.html">드롭다운 메뉴</a>, 아래에서 올라오면 <a href="actionsheet.html">액션 시트</a>, 아무 내용이나 담으면 <a href="popover.html">팝오버</a>, 여러 줄을 고르면 <a href="bulk.html">일괄 선택</a>.',
  cases=cases([
    (cm("", "", True, "150px", True, False), "파일 목록", "<b>⋯ 와 함께</b>"),
    (cm("", "", True, "150px", False, True), "편집기", "<b>오른쪽 누르기</b>가 익숙한 자리"),
    (one(txt('<span style="display:block;font-size:8px">길게 눌렀다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">폰에서는 시트로 올라온다</span>'),
         "폰", True, "", "150px"),
     "폰", "<a href=\"actionsheet.html\">액션 시트</a>로 바꾼다"),
  ]),
  code_lede="<code>contextmenu</code> 이벤트를 받되, <b>막을지는 신중하게</b> 정합니다.",
  code='''&lt;<span class="t">li</span>&gt;
  영수증_2411_01.jpg
  &lt;<span class="t">button</span> <span class="a">aria-haspopup</span>=<span class="s">"menu"</span>
          <span class="a">aria-label</span>=<span class="s">"영수증_2411_01.jpg 메뉴 열기"</span>&gt;⋯&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">li</span>&gt;

row.addEventListener(<span class="s">'contextmenu'</span>, e =&gt; {
  e.preventDefault();          <span class="c">// 기본 메뉴를 빼앗는다 — 꼭 필요할 때만</span>
  openMenu(e.clientX, e.clientY);
});

<span class="c">// 키보드에도 길을 둔다</span>
row.addEventListener(<span class="s">'keydown'</span>, e =&gt; {
  <span class="t">if</span> (e.key === <span class="s">'ContextMenu'</span> || (e.shiftKey &amp;&amp; e.key === <span class="s">'F10'</span>)) {
    e.preventDefault();
    <span class="t">const</span> r = row.getBoundingClientRect();
    openMenu(r.left, r.bottom);
  }
});''',
  keys=kbd([
    ("Shift + F10 · 메뉴 키", "키보드로 여는 <b>표준 방법</b>"),
    ("↑ ↓", "항목 사이를 옮긴다"),
    ("Esc", "닫고 초점을 <b>그 줄로</b>"),
    ("<code>aria-haspopup</code>", "⋯ 단추에 붙인다"),
    ("길게 누르기", "폰에서는 <b>드래그와 안 겹치게</b> 시간을 둔다"),
    ("확인하는 법", "마우스를 안 쓰고 <b>같은 일을 할 수 있는지</b> 본다"),
  ]),
  backend=rows([
    ("할 수 있는 일", "줄마다 권한이 다르면 <b>항목을 지웁니다</b> — <a href=\"menu.html\">드롭다운 메뉴</a>와 같습니다."),
    ("여러 줄", "여러 줄을 고른 상태에서 열면 <b>묶음 동작</b>이 떠야 합니다 — <a href=\"bulk.html\">일괄 선택</a>과 이어집니다."),
  ]),
  plat_lede="<b>여는 몸짓</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "contextmenu 이벤트",
     cm("", "", True, "110px", True, True, (34, 18)),
     "브라우저 기본 메뉴를 <b>막을지</b>가 늘 고민거리입니다."),
    ("iOS", "Context Menu (길게 누르기)",
     '''              <div class="phone" role="img" aria-label="iOS 컨텍스트 메뉴 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 30%, transparent)"></div>
                <div style="position:absolute;left:6px;right:6px;top:22px;height:16px;border-radius:4px;background:var(--surface)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:18px;border-radius:4px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "길게 누르면 <b>미리보기와 메뉴</b>가 같이 뜹니다 — 정식 부품입니다."),
    ("안드로이드", "길게 누르기 + 액션 바",
     '''              <div class="phone" role="img" aria-label="안드로이드 선택 모드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:18px;height:11px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "길게 누르면 <b>선택 모드</b>로 들어가 앱바가 동작 모음으로 바뀝니다."),
  ]),
  plat_note="안드로이드가 길게 누르기를 <b>선택 모드</b>로 쓰는 것은 다른 두 플랫폼과 크게 다릅니다 — 한 줄을 고르면 앱바가 '지우기·공유' 같은 동작 모음으로 바뀌고, 더 고를 수도 있습니다. 웹에서 폰 폭을 만들 때 <b>길게 누르기를 메뉴로 쓸지 선택으로 쓸지</b>를 정해 두지 않으면 둘이 부딪힙니다. 대부분은 <b>⋯ 단추 + 액션 시트</b> 쪽이 덜 헷갈립니다.",
  siblings=siblings("contextmenu"),
  related='''        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><a href="actionsheet.html"><b>액션 시트</b><em>6부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="gesture.html"><b>제스처</b><em>9부</em></a></li>''',
)
