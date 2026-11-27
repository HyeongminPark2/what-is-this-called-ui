# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

def mn(items, label, note="", ok=None, w="152px", up=False, trigger="더 보기 ▾"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    lis = ''.join(('<span style="display:block;border-top:1px solid var(--line);margin:2px 0"></span>' if t == 'SEP'
                   else '<span style="display:flex;gap:5px;align-items:center;padding:2px 5px;border-radius:3px;'
                        'font-size:7.5px;' + ('background:var(--accent-soft);color:var(--accent);' if on else
                                              ('color:var(--danger);' if d else '')) + '">' + t
                        + ('<small style="margin-left:auto;font-family:var(--mono);font-size:6.5px;color:var(--fg-muted)">'
                           + s + '</small>' if s else '') + '</span>')
                  for t, s, on, d in items)
    box = ('<span style="position:absolute;left:6px;' + ('bottom:26px;' if up else 'top:26px;') +
           'border-radius:5px;background:var(--surface);border:1px solid var(--line);padding:3px;'
           'min-width:92px;box-shadow:0 6px 16px rgba(20,22,26,.14)">' + lis + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden">'
            '<span style="position:absolute;left:6px;' + ('bottom:6px;' if up else 'top:6px;') +
            'border:1px solid var(--line);border-radius:4px;background:var(--surface);'
            'padding:2px 6px;font-size:7.5px">' + trigger + '</span>' + box + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">단추 — aria-haspopup · aria-expanded</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">동작 목록이면 menu / menuitem</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">값 고르기면 listbox / option</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단축키는 오른쪽에 적는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">자리가 없으면 위로 뒤집는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">닫으면 초점이 단추로 돌아온다</div>
                </div>
              </div>'''

D = dict(
  slug="menu", ko="드롭다운 메뉴", en="Dropdown menu",
  desc="단추에 붙어 열리는 동작 목록. 값 고르기(셀렉트)와의 차이, 뒤집기, 키보드.",
  lede="누르면 <b>무슨 일이 일어나는</b> 목록입니다. 누르면 <b>값이 정해질 뿐</b>인 셀렉트와 생김새가 같아 가장 많이 섞입니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>동작 목록</b>과 <b>값 고르기</b>는 생김새가 같아 가장 많이 섞입니다 —
          데모가 둘의 역할·키보드·표시를 나눠서 적습니다.<br>
          단추를 아래로 내려 보세요. 자리가 모자라면 메뉴가 <b>위로 뒤집혀야</b> 합니다 —
          데모가 <b>화면 밖으로 삐져나간 px</b>을 재서 적습니다. 뒤집기를 끄면 잘립니다.<br>
          ↑↓ 로 옮기고 Esc 로 닫으며, 닫으면 초점이 <b>단추로 돌아와야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "드롭다운 메뉴, 메뉴, 더 보기 메뉴, 케밥 메뉴"),
    ("영어", "dropdown menu, menu, overflow menu, kebab menu"),
    ("같이 쓰는 말",
     "점 세 개로 여는 것을 <b>오버플로 메뉴</b>·<b>케밥 메뉴</b>라 부릅니다. "
     "주 동작 옆에 화살표가 붙은 것은 <b>스플릿 버튼</b>(split button), "
     "메뉴 안에서 또 열리는 것은 <b>서브메뉴</b>입니다. "
     "값을 고르는 쪽은 <b>셀렉트</b>이고 역할 이름도 다릅니다."),
    ("자주 잘못 부름",
     "<b>셀렉트</b> — <a href=\"select.html\">셀렉트</a>는 <b>값</b>을 고릅니다. 아무 일도 안 일어납니다.<br>"
     "<b>팝오버</b> — <a href=\"popover.html\">팝오버</a>는 <b>아무 내용</b>이나 담습니다.<br>"
     "<b>컨텍스트 메뉴</b> — <a href=\"contextmenu.html\">컨텍스트 메뉴</a>는 <b>오른쪽 눌러</b> 엽니다."),
  ]),
  axes=axis_table("드롭다운 메뉴"),
  oneline="<b>누르면 일이 일어나면 메뉴, 값만 정해지면 셀렉트입니다.</b> 역할 이름부터 다릅니다.",
  states=states([
    (mn([("이름 바꾸기", "", True, False), ("복사본 만들기", "⌘D", False, False),
         ("SEP", "", False, False), ("지우기", "⌫", False, True)], "", "동작 목록", True),
     "메뉴", "<b>누르면 일이</b> 일어난다"),
    (mn([("매주 수요일", "", True, False), ("매달 1일", "", False, False), ("매달 15일", "", False, False)],
        "", "값 고르기", True, "152px", False, "매주 수요일 ▾"),
     "셀렉트", "<b>값이 정해질</b> 뿐"),
    (mn([("이름 바꾸기", "", True, False), ("지우기", "", False, True)], "", "자리가 없어 위로 뒤집었다", True, "152px", True),
     "위로 뒤집음", "<b>안 잘린다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">아래로만 열었다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">화면 밖으로 32px 삐져나감</span>'),
         "안 뒤집음", False, "", "152px"),
     "안 뒤집음", "<b>잘린다</b>"),
    (mn([("이름 바꾸기", "F2", True, False), ("복사", "⌘C", False, False)], "", "단축키를 가르친다", True),
     "단축키 표시", "<b>다음엔 안 열어도</b> 되게"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">Esc 로 닫았다</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">초점이 <b>단추</b>로 돌아왔다</span>'),
         "닫기", True, "", "152px"),
     "닫은 뒤", "<b>단추로</b> 돌아간다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단추", "<code>aria-haspopup</code>", "무엇이 열리는지"),
    ("동작 목록", "<code>menu/menuitem</code>", "누르면 <b>일이</b> 일어난다"),
    ("값 고르기", "<code>listbox/option</code>", "누르면 <b>값이</b> 정해진다"),
    ("단축키", "오른쪽", "<b>가르치는</b> 자리"),
    ("뒤집기", "자리가 없으면", "<b>잘리지 않게</b>"),
    ("닫은 뒤", "단추로", "초점을 <b>돌려준다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          둘을 가르는 질문은 하나입니다 — <b>누르면 무슨 일이 일어나나</b>.
          '지우기'는 일이 일어나니 메뉴고, '매주 수요일'은 값만 정해지니 셀렉트입니다.
          역할 이름이 다르면 <b>소리로 듣는 사람이 듣는 말</b>도 달라집니다 —
          메뉴는 '메뉴 항목', 셀렉트는 '목록 상자 · 선택됨'이라고 읽힙니다.<br>
          섞어 쓰면 <b>키보드도 어긋납니다</b>.
          메뉴는 Enter 로 실행하고 닫히지만,
          셀렉트는 고른 값이 <b>표시로 남아야</b> 합니다 —
          어느 쪽인지 모르면 어느 쪽 동작도 제대로 못 만듭니다.</p>''',
  do=ul([
    "<b>누르면 일이 일어나면</b> 메뉴, 아니면 셀렉트",
    "자리가 없으면 <b>위로 뒤집기</b>",
    "닫으면 <b>초점을 단추로</b> 돌려주기",
  ]),
  dont=ul([
    "셀렉트를 <code>role=\"menu\"</code> 로 만들기 — <b>고른 값</b>이 안 들린다",
    "메뉴를 <b>아래로만</b> 열기 — 화면 끝에서 잘린다",
    "메뉴에 <b>입력칸</b> 넣기 — 그건 <a href=\"popover.html\">팝오버</a>다",
    "항목을 <b>열다섯 개</b> 넘게 두기 — 묶거나 <a href=\"commandpalette.html\">팔레트</a>로",
  ]),
  instead='값을 고르면 <a href="select.html">셀렉트</a>, 아무 내용이나 담으면 <a href="popover.html">팝오버</a>, 오른쪽 눌러 열면 <a href="contextmenu.html">컨텍스트 메뉴</a>, 아래에서 올라오면 <a href="actionsheet.html">액션 시트</a>.',
  cases=cases([
    (mn([("이름 바꾸기", "", True, False), ("지우기", "", False, True)], "", "", True, "150px", False, "⋯"),
     "줄의 더 보기", "<b>케밥 메뉴</b>"),
    (mn([("CSV 로", "", True, False), ("엑셀로", "", False, False)], "", "", True, "150px", False, "내보내기 ▾"),
     "스플릿 버튼", "주 동작 + <b>갈래</b>"),
    (mn([("매주 수요일", "", True, False), ("매달 1일", "", False, False)], "", "", True, "150px", False, "매주 수요일 ▾"),
     "값 고르기", "이건 <b>셀렉트</b>다"),
  ]),
  code_lede="동작 목록이면 <code>menu</code>, 값 고르기면 <code>listbox</code> — 여기서부터 갈립니다.",
  code='''<span class="c">&lt;!-- 동작 목록 — 누르면 일이 일어난다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-haspopup</span>=<span class="s">"menu"</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span>
        <span class="a">aria-controls</span>=<span class="s">"m1"</span>&gt;더 보기&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"m1"</span> <span class="a">role</span>=<span class="s">"menu"</span> <span class="a">hidden</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"menuitem"</span>&gt;이름 바꾸기&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"menuitem"</span> <span class="a">class</span>=<span class="s">"danger"</span>&gt;지우기&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 자리가 없으면 위로 — CSS 만으로도 된다 */</span>
[popover] { <span class="a">position-try-fallbacks</span>: flip-block; }

<span class="c">// 닫으면 초점을 단추로 돌려준다</span>
menu.addEventListener(<span class="s">'close'</span>, () =&gt; trigger.focus());''',
  keys=kbd([
    ("Enter · Space · ↓", "단추에서 <b>메뉴를 연다</b>"),
    ("↑ ↓", "항목 사이를 옮긴다 — <b>Tab 이 아니다</b>"),
    ("Home · End", "<b>처음 · 마지막</b> 항목으로"),
    ("Esc", "닫고 초점을 <b>단추로</b>"),
    ("글자 키", "그 글자로 시작하는 항목으로 — <b>긴 메뉴</b>에서 쓸모가 크다"),
    ("확인하는 법", "Tab 을 눌러 <b>메뉴 밖으로 안 나가는지</b> 본다"),
  ]),
  backend=rows([
    ("할 수 있는 일", "권한에 따라 <b>항목을 지웁니다</b> — 흐리게 두면 '왜 안 되나'를 묻게 됩니다."),
    ("동작의 결과", "메뉴 항목을 누르면 보통 요청이 나갑니다 — <a href=\"undo.html\">되돌리기</a>를 붙일지 미리 정합니다."),
  ]),
  plat_lede="<b>이름과 역할</b>이 플랫폼마다 또렷하게 나뉘어 있습니다.",
  plats=plats([
    ("웹", "role=\"menu\" 또는 &lt;select&gt;",
     mn([("이름 바꾸기", "", True, False)], "", "", True, "110px"),
     "<code>popover</code> 속성이 생겨 <b>위치 잡기와 닫기</b>가 쉬워졌습니다."),
    ("iOS", "UIMenu",
     '''              <div class="phone" role="img" aria-label="iOS 메뉴 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:22px;width:14px;height:5px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;left:6px;top:32px;width:26px;height:20px;border-radius:4px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "길게 누르거나 단추로 엽니다. <b>destructive</b> 역할이 따로 있어 빨갛게 나옵니다."),
    ("안드로이드", "DropdownMenu",
     '''              <div class="phone" role="img" aria-label="안드로이드 메뉴 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:6px;top:22px;width:4px;height:9px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;right:6px;top:34px;width:26px;height:20px;border-radius:4px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "앱바 오른쪽의 <b>점 세 개</b>가 표준 자리입니다 — 오버플로 메뉴라 부릅니다."),
  ]),
  plat_note="앱 쪽은 <b>점 세 개의 자리</b>가 정해져 있어(iOS 는 오른쪽 위, 안드로이드는 앱바 오른쪽) 사용자가 찾을 줄 압니다. 웹에는 그런 약속이 없어 <b>어디에 두는지를 팀이 정해</b> 두어야 하고, 한 화면에서 자리가 바뀌면 바로 '못 찾겠다'가 됩니다. 줄마다 쓰는 메뉴는 <b>줄 끝</b>에 고정하는 것이 가장 무난합니다.",
  siblings=siblings("menu"),
  related='''        <li><a href="select.html"><b>셀렉트</b><em>4부</em></a></li>
        <li><a href="popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="contextmenu.html"><b>컨텍스트 메뉴</b><em>6부</em></a></li>
        <li><a href="tablerow.html"><b>테이블 행</b><em>5부</em></a></li>''',
)
