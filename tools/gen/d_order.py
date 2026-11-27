# -*- coding: utf-8 -*-
from ax1 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def chips(names, nums=None, col=None, w="152px", note="", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for i, n in enumerate(names):
        num = ('<small style="display:block;font-size:7px;color:' + c + '">' + str(nums[i]) + '</small>') if nums else ''
        out.append('<span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);'
                   'padding:3px 5px;font-size:8.5px;text-align:center">' + n + num + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:4px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);padding:5px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def twoline(eye, tab, w="152px", ok=None):
    c = "var(--accent)" if ok else "var(--danger)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:3px;'
            'font-family:var(--mono);font-size:8.5px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);padding:6px 7px">'
            '<span style="color:var(--fg-muted)">눈 &nbsp;' + eye + '</span>'
            '<span style="color:' + c + '">Tab ' + tab + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">마크업 순서   Tab과 읽어 주는 차례의 <b>유일한</b> 근거</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">order·row-reverse   <b>보이는 자리만</b> 바꿈</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">position으로 옮겨도 보이는 자리만 바뀜</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">tabindex="0"   원래 못 받는 요소에 초점을 줌</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">tabindex="3" 같은 양수   차례를 뒤엎음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">두 차례를 맞추려면 마크업을 고침</div>
                </div>
              </div>'''

D = dict(
  slug="order", ko="보이는 순서와 읽는 순서", en="Visual order vs DOM order",
  desc="눈에 보이는 차례와 Tab·스크린 리더가 따라가는 차례를 비교하고, CSS로 자리를 바꾸면 왜 두 차례가 어긋나는지 보여 주는 항목입니다.",
  lede="CSS로는 <b>보이는 자리</b>만 바꿀 수 있습니다. <b>Tab으로 옮겨 가는 차례와 스크린 리더가 읽어 주는 차례</b>는 CSS와 상관없이 마크업 순서를 따릅니다.",
  axes_lede="뼈대는 눈에 보이지 않지만 <b>모든 화면의 배치</b>를 정합니다. 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>보이는 차례를 바꾸는 방법을 고른 뒤 <b>Tab으로 차례대로 옮겨 보기</b>를 누르면 초점이 옮겨 간 차례가 적힙니다.<br>
          <code>row-reverse</code>나 <code>order</code>로 뒤집으면 눈에는 <b>취소</b>가 먼저 보이지만
          Tab은 <b>저장</b>부터 갑니다. 마우스를 쓰는 사람은 이 차이를 알아챌 일이 없지만,
          키보드를 쓰는 사람은 <b>보이는 차례와 다르게 움직이는 초점</b>을 따라가야 합니다.<br>
          마크업 순서를 바꾸면 두 차례가 같아지며, 이것이 유일하게 맞는 방법입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "보이는 순서와 읽는 순서, 시각 순서와 DOM 순서, 초점 순서"),
    ("영어", "visual order, DOM order, focus order, reading order"),
    ("같이 쓰는 말",
     "Tab이 따라가는 차례는 <b>초점 순서</b>(focus order), "
     "스크린 리더가 읽어 가는 차례는 <b>읽는 순서</b>(reading order)라고 합니다. "
     "두 순서는 거의 항상 같고, 모두 <b>마크업 순서</b>를 따릅니다. "
     "눈에 보이는 차례는 따로 <b>시각 순서</b>(visual order)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>z-index</b> — <a href=\"../items/zindex.html\">겹침 순서</a>는 요소가 <b>위아래로 쌓이는</b> 순서이고, 이 항목은 <b>앞뒤로 이어지는</b> 차례를 다룹니다.<br>"
     "<b>order 속성</b> — <code>order</code>는 이 문제를 <b>일으키는 속성</b>이지 해결하는 속성이 아닙니다.<br>"
     "<b>tabindex</b> — 요소가 <a href=\"focus.html\">초점</a>을 받게 할 뿐이고, 차례를 고치는 도구는 아닙니다."),
  ]),
  axes=ax("보이는 순서와 읽는 순서"),
  oneline="<b>자리를 바꾸고 싶으면 마크업을 바꾸세요.</b> <code>order</code>와 <code>row-reverse</code>는 보이는 자리만 바꾸고 Tab 차례는 그대로 둡니다.",
  s4_title="두 차례가 어긋나는 경우", s4_hint="보이는 차례와 Tab 차례가 같은지 비교",
  do_title="두 차례를 맞추기 위해 할 일",
  dont_title="두 차례를 어긋나게 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  states=states([
    (chips(["저장", "취소", "삭제"], ["1", "2", "3"], None, "152px", "기본값이라 둘이 같음", True),
     "아무것도 바꾸지 않았을 때", "보이는 차례와 Tab 차례가 같습니다"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px">
                <div style="display:flex;flex-direction:row-reverse;gap:4px;border:1px solid var(--danger);border-radius:6px;background:var(--bg);padding:5px">
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">저장<small style="display:block;font-size:7px;color:var(--danger)">Tab 1</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">취소<small style="display:block;font-size:7px;color:var(--danger)">Tab 2</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">삭제<small style="display:block;font-size:7px;color:var(--danger)">Tab 3</small></span>
                </div>
                <span style="font-size:8.5px;color:var(--fg-muted)">눈은 삭제부터, Tab은 저장부터</span>
              </div>''',
     "<code>row-reverse</code>로 뒤집었을 때", "보이는 차례와 Tab 차례가 <b>어긋납니다</b>"),
    (twoline("취소 → 저장 → 삭제", "저장 → 취소 → 삭제", "152px", False),
     "<code>order</code>로 한 칸 옮겼을 때", "한 칸만 옮겨도 <b>어긋납니다</b>"),
    (twoline("요약 → 본문", "본문 → 요약", "152px", False),
     "넓은 화면에서 둘째 단을 위로 올렸을 때", "넓은 화면에서만 <b>어긋납니다</b>"),
    (chips(["취소", "저장", "삭제"], ["1", "2", "3"], None, "152px", "마크업을 바꿈", True),
     "마크업 순서를 고쳤을 때", "보이는 차례와 Tab 차례가 <b>다시 같아집니다</b>"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px">
                <div style="display:flex;gap:4px;border:1px solid var(--danger);border-radius:6px;background:var(--bg);padding:5px">
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">저장<small style="display:block;font-size:7px;color:var(--danger)">Tab 3</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">취소<small style="display:block;font-size:7px;color:var(--danger)">Tab 1</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">삭제<small style="display:block;font-size:7px;color:var(--danger)">Tab 2</small></span>
                </div>
                <span style="font-size:8.5px;color:var(--fg-muted)">양수 tabindex는 페이지 전체 차례를 뒤엎음</span>
              </div>''',
     "양수 <code>tabindex</code>를 주었을 때", "페이지 전체 차례를 뒤엎어서 <b>더 나쁩니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("마크업 순서", "유일한 근거", "Tab과 <b>스크린 리더가 읽어 주는 차례</b>는 마크업 순서만 따릅니다"),
    ("<code>order</code>·<code>row-reverse</code>", "보이는 자리만 바꿈", "<b>보이는 자리만</b> 바뀝니다"),
    ("<code>position</code>", "보이는 자리만 바꿈", "자리를 옮겨도 차례는 <b>그대로</b>입니다"),
    ("<code>tabindex=\"0\"</code>", "초점을 줌", "초점을 받는 차례는 마크업의 <b>제자리</b>에서 정해집니다"),
    ("양수 <code>tabindex</code>", "쓰지 않음", "페이지 <b>전체</b>의 차례를 뒤엎습니다"),
    ("두 차례를 맞추는 방법", "마크업 수정", "차례를 맞추는 <b>하나뿐인</b> 방법입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          두 차례가 어긋나도 <b>마우스로 쓸 때는 전혀 드러나지 않기</b> 때문에,
          몇 달이 지나서야 '키보드로 쓰면 버튼 차례가 이상하다'는 제보로 발견되곤 합니다.
          확인하는 방법은 간단합니다. <b>Tab을 눌러 초점이 가는 차례와 눈에 보이는 차례가 같은지</b> 보면 됩니다.
          특히 <b>반응형 화면에서 단 순서를 뒤집은 자리</b>를 의심하세요.
          좁은 화면에서는 맞는데 넓은 화면에서만 어긋나는 일이 흔합니다.</p>''',
  do=ul([
    "요소의 자리를 바꿀 때. CSS가 아니라 <b>마크업을 바꿉니다</b>",
    "화면을 다 만든 뒤. <b>Tab만 눌러 한 바퀴</b> 돌려 봅니다",
    "반응형에서 단 순서를 바꿨을 때. <b>좁은 폭과 넓은 폭 모두</b> 확인합니다",
  ]),
  dont=ul([
    "<code>order</code>로 버튼 자리를 바꿀 때. <b>Tab 차례는 원래대로 남습니다</b>",
    "<code>row-reverse</code>로 오른쪽 정렬을 흉내 낼 때. <code>margin-left:auto</code>로 충분합니다",
    "양수 <code>tabindex</code>로 차례를 고칠 때. <b>페이지 전체</b>의 차례가 망가집니다",
    "<code>position:absolute</code>로 요소를 멀리 옮겨 놓고 마크업은 그대로 둘 때",
  ]),
  instead='초점이 무엇인지는 <a href="focus.html">초점</a>에서, 창 안에 초점을 가두는 방법은 <a href="focustrap.html">초점 갇힘</a>에서, 키보드로 조작하는 방법은 <a href="keyboard.html">키보드 조작</a>에서 다룹니다. 요소가 위아래로 쌓이는 순서는 <a href="../items/zindex.html">겹침 순서</a>에서 봅니다.',
  cases=cases([
    (twoline("취소 → 저장", "취소 → 저장", "150px", True),
     "버튼 줄을 보이는 차례대로 적기", "마크업을 보이는 차례대로 <b>취소 → 저장</b>으로 적습니다"),
    (code(['&lt;main&gt;본문&lt;/main&gt;', '&lt;aside&gt;요약&lt;/aside&gt;'], "150px", "요약을 위에 보이고 싶어도 마크업은 본문 먼저", True),
     "본문과 요약의 차례 정하기", "보이는 위치보다 읽는 차례를 <b>먼저</b> 정합니다"),
    (code(['.btn { margin-left: auto; }'], "150px", "오른쪽으로 붙여도 차례는 그대로", True),
     "차례를 건드리지 않고 오른쪽 정렬하기", "<code>row-reverse</code> 대신 <code>margin-left: auto</code>로 붙입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="순서를 다룰 때 지킬 것",
  keys_heads="<th>키와 속성</th><th>초점이 움직이는 방식</th>",
  code_lede="보이는 차례와 마크업 차례를 <b>같게</b> 두면 지킬 규칙이 하나로 줄어듭니다.",
  code='''<span class="c">&lt;!-- 마크업 순서가 Tab 순서다. 보이고 싶은 차례대로 적는다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"row"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"ghost"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 오른쪽으로 붙인다. 차례는 바뀌지 않는다 */</span>
.row { <span class="a">display</span>: flex; <span class="a">gap</span>: <span class="a">8px</span>; }
.row .ghost { <span class="a">margin-right</span>: auto; }

<span class="c">/* ✕ 보이는 자리만 뒤집혀서 Tab은 저장부터 간다 */</span>
.row { <span class="a">flex-direction</span>: row-reverse; }
.save { <span class="a">order</span>: <span class="a">-1</span>; }

<span class="c">/* ✕ 페이지 전체 차례를 뒤엎는다 */</span>
&lt;<span class="t">button</span> <span class="a">tabindex</span>=<span class="s">"3"</span>&gt;''',
  keys=kbd([
    ("Tab", "마크업 순서로만 이동하고, CSS는 <b>영향을 주지 않습니다</b>"),
    ("Shift + Tab", "마크업의 역순으로 이동하며, 눈에 보이는 역순과 <b>다를 수 있습니다</b>"),
    ("<code>tabindex=\"0\"</code>", "마크업 자리에서 초점을 받습니다. <b>권장하는</b> 값입니다"),
    ("<code>tabindex=\"-1\"</code>", "Tab으로는 갈 수 없고 <code>focus()</code>로만 초점을 옮길 수 있습니다"),
    ("양수 <code>tabindex</code>", "0인 요소들보다 <b>먼저</b> 모두 돌기 때문에 쓰지 않습니다"),
    ("확인하는 방법", "주소창에서 Tab을 계속 누르며 <b>초점 테두리</b>를 눈으로 따라갑니다"),
  ]),
  backend=rows([
    ("정렬된 배열로 보내 주기", "목록 API가 정렬된 배열을 주면 그대로 그려도 차례가 맞습니다. 반면 <b>객체(dict)로 주면</b> 순서가 보장되지 않아 어긋날 수 있습니다."),
    ("정렬 기준도 함께 보내기", "<code>?sort=amount.desc</code>처럼 <b>무엇으로 정렬했는지</b>를 응답에도 담아 주면 화면에서 임의로 다시 정렬하는 일이 없습니다."),
    ("실시간으로 줄이 추가될 때", "실시간으로 새 줄이 끼어들면 <b>초점이 엉뚱한 줄</b>로 옮겨지기 때문에, 줄을 끼워 넣기 전에 초점 위치를 기억해 둡니다."),
  ]),
  plat_lede="보이는 자리와 초점 차례가 따로 정해진다는 것은 <b>어느 플랫폼에서나 같은 규칙</b>입니다.",
  plats=plats([
    ("웹", "DOM order",
     chips(["저장", "취소"], ["1", "2"], None, "110px", "", True),
     "<code>order</code>·<code>row-reverse</code>·<code>position</code>은 모두 <b>보이는 자리만</b> 바꿉니다."),
    ("iOS", "accessibilityElements",
     '''              <div class="phone" role="img" aria-label="iOS 초점 차례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px">
                  <span style="flex:1;height:11px;border-radius:3px;background:var(--accent-soft)"></span>
                  <span style="flex:1;height:11px;border-radius:3px;background:var(--accent)"></span></div></div></div>''',
     "뷰 계층이 차례를 정합니다. 필요하면 <code>accessibilityElements</code>로 <b>따로 지정</b>합니다."),
    ("안드로이드", "traversalBefore",
     '''              <div class="phone" role="img" aria-label="안드로이드 초점 차례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;gap:3px">
                  <span style="flex:1;height:11px;border-radius:3px;background:var(--accent)"></span>
                  <span style="flex:1;height:11px;border-radius:3px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>traversalBefore</code>·<code>traversalAfter</code>로 두 뷰 사이 차례를 <b>국소적으로</b> 바꿉니다."),
  ]),
  plat_note="앱에는 차례를 <b>따로 지정하는 방법</b>이 있지만 웹에는 사실상 없습니다. 양수 <code>tabindex</code>는 페이지 전체 차례를 바꿔 버려서 쓰지 않기 때문입니다. 그래서 웹에서는 <b>마크업을 올바른 차례로 적는 것</b>이 유일한 방법이고, 달리 보면 지킬 규칙이 하나뿐이라 간단합니다.",
  siblings=siblings("order"),
  related='''        <li><a href="focus.html"><b>초점</b><em>12부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>겹침 순서</b><em>2부</em></a></li>''',
)
