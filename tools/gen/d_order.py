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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">마크업 순서 — Tab · 읽어 주는 차례의 <b>유일한</b> 근거</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">order · row-reverse — <b>보이기만</b> 바꾼다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">position 으로 자리 옮기기 — 역시 보이기만</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">tabindex="0" — 원래 못 받는 것에 초점을 준다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">tabindex="3" 같은 양수 — 차례를 뒤엎는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">둘을 맞추는 법 — 마크업을 고친다</div>
                </div>
              </div>'''

D = dict(
  slug="order", ko="보이는 순서와 읽는 순서", en="Visual order vs DOM order",
  desc="눈에 보이는 차례와 Tab·스크린 리더가 따라가는 차례. 왜 CSS로 자리를 바꾸면 어긋나는가.",
  lede="CSS 는 <b>보이는 자리</b>만 바꿉니다. <b>Tab 과 읽어 주는 차례</b>는 끝까지 마크업 순서를 따라갑니다.",
  axes_lede="뼈대는 눈에 안 보이지만 <b>모든 화면이 그 위에</b> 섭니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>뒤집는 법을 골라 보고 <b>Tab 으로 훑어보기</b>를 누르세요 — 초점이 간 차례가 적힙니다.<br>
          <code>row-reverse</code>나 <code>order</code>로 뒤집으면 눈에는 <b>취소</b>가 먼저인데
          Tab 은 <b>저장</b>부터 갑니다. 마우스로 쓰는 사람은 영영 모르고,
          키보드로 쓰는 사람에게는 <b>화면이 거짓말</b>을 합니다.<br>
          마크업 순서를 바꾸면 둘이 같아집니다 — 유일하게 맞는 방법입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "보이는 순서와 읽는 순서, 시각 순서와 DOM 순서, 초점 순서"),
    ("영어", "visual order, DOM order, focus order, reading order"),
    ("같이 쓰는 말",
     "Tab 이 따라가는 차례가 <b>초점 순서</b>(focus order), "
     "스크린 리더가 읽어 가는 차례가 <b>읽는 순서</b>(reading order)입니다. "
     "둘은 거의 늘 같고, 둘 다 <b>마크업 순서</b>를 따릅니다. "
     "눈에 보이는 차례만 <b>시각 순서</b>(visual order)라고 따로 부릅니다."),
    ("자주 잘못 부름",
     "<b>z-index</b> — <a href=\"../items/zindex.html\">겹침 순서</a>는 <b>위아래</b>이고, 이건 <b>앞뒤</b>입니다.<br>"
     "<b>order 속성</b> — <code>order</code>는 이 문제를 <b>만드는 쪽</b>이지 해결하는 쪽이 아닙니다.<br>"
     "<b>tabindex</b> — <a href=\"focus.html\">초점</a>을 받게 할 뿐, 차례를 고치는 도구가 아닙니다."),
  ]),
  axes=ax("보이는 순서와 읽는 순서"),
  oneline="<b>자리를 바꾸고 싶으면 마크업을 바꾸세요.</b> <code>order</code>와 <code>row-reverse</code>는 눈만 속입니다.",
  s4_title="어긋나는 꼴", s4_hint="눈과 Tab 이 같은가",
  states=states([
    (chips(["저장", "취소", "삭제"], ["1", "2", "3"], None, "152px", "기본 — 둘이 같다", True),
     "그대로", "눈 = Tab"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px">
                <div style="display:flex;flex-direction:row-reverse;gap:4px;border:1px solid var(--danger);border-radius:6px;background:var(--bg);padding:5px">
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">저장<small style="display:block;font-size:7px;color:var(--danger)">Tab 1</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">취소<small style="display:block;font-size:7px;color:var(--danger)">Tab 2</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">삭제<small style="display:block;font-size:7px;color:var(--danger)">Tab 3</small></span>
                </div>
                <span style="font-size:8.5px;color:var(--fg-muted)">눈은 삭제부터, Tab 은 저장부터</span>
              </div>''',
     "<code>row-reverse</code>", "<b>어긋난다</b>"),
    (twoline("취소 → 저장 → 삭제", "저장 → 취소 → 삭제", "152px", False),
     "<code>order</code>", "한 칸만 옮겨도 <b>어긋난다</b>"),
    (twoline("요약 → 본문", "본문 → 요약", "152px", False),
     "둘째 단을 위로", "넓은 화면에서만 <b>어긋난다</b>"),
    (chips(["취소", "저장", "삭제"], ["1", "2", "3"], None, "152px", "마크업을 바꿨다", True),
     "마크업 수정", "<b>다시 같아진다</b>"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px">
                <div style="display:flex;gap:4px;border:1px solid var(--danger);border-radius:6px;background:var(--bg);padding:5px">
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">저장<small style="display:block;font-size:7px;color:var(--danger)">Tab 3</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">취소<small style="display:block;font-size:7px;color:var(--danger)">Tab 1</small></span>
                  <span style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:3px 5px;font-size:8.5px;text-align:center">삭제<small style="display:block;font-size:7px;color:var(--danger)">Tab 2</small></span>
                </div>
                <span style="font-size:8.5px;color:var(--fg-muted)">양수 tabindex — 페이지 전체 차례를 뒤엎는다</span>
              </div>''',
     "<code>tabindex=\"3\"</code>", "<b>더 나쁘다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("마크업 순서", "유일한 근거", "Tab 과 <b>읽어 주는 차례</b>가 이것만 본다"),
    ("<code>order</code>·<code>row-reverse</code>", "보이기만", "<b>눈만</b> 바뀐다"),
    ("<code>position</code>", "보이기만", "자리를 옮겨도 차례는 <b>그대로</b>"),
    ("<code>tabindex=\"0\"</code>", "초점을 준다", "차례는 <b>제자리</b>에서 생긴다"),
    ("양수 <code>tabindex</code>", "쓰지 않는다", "페이지 <b>전체</b> 차례를 뒤엎는다"),
    ("맞추는 법", "마크업 수정", "<b>하나뿐인</b> 방법"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          어긋나도 <b>마우스로는 전혀 드러나지 않습니다</b>.
          그래서 몇 달 지나 '키보드로 쓰면 버튼 차례가 이상하다'는 제보로 발견됩니다.
          확인은 간단합니다 — <b>Tab 을 눌러 보고 적힌 차례와 눈에 보이는 차례가 같은지</b> 보면 됩니다.
          특히 <b>반응형에서 단 순서를 뒤집은 자리</b>를 의심하세요.
          좁은 화면에서는 맞는데 넓은 화면에서만 어긋나는 일이 흔합니다.</p>''',
  do=ul([
    "자리를 바꾸려면 <b>마크업을 바꾸기</b>",
    "다 만든 뒤 <b>Tab 만 눌러 한 바퀴</b> 돌려 보기",
    "단 순서를 바꾼 자리는 <b>두 폭 모두</b> 확인하기",
  ]),
  dont=ul([
    "<code>order</code>로 버튼 자리 바꾸기 — <b>Tab 차례가 남는다</b>",
    "<code>row-reverse</code>로 '오른쪽 정렬' 흉내 내기 — <code>margin-left:auto</code>면 된다",
    "양수 <code>tabindex</code>로 차례 고치기 — <b>페이지 전체</b>가 망가진다",
    "<code>position:absolute</code>로 멀리 옮겨 놓고 마크업은 그대로 두기",
  ]),
  instead='초점 자체는 <a href="focus.html">초점</a>, 갇힘은 <a href="focustrap.html">초점 갇힘</a>, 키보드 조작은 <a href="keyboard.html">키보드 조작</a>, 겹침 순서는 <a href="../items/zindex.html">겹침 순서</a>.',
  cases=cases([
    (twoline("취소 → 저장", "취소 → 저장", "150px", True),
     "버튼 줄", "마크업을 <b>취소 → 저장</b>으로 적는다"),
    (code(['&lt;main&gt;본문&lt;/main&gt;', '&lt;aside&gt;요약&lt;/aside&gt;'], "150px", "요약을 위에 보이고 싶어도 마크업은 본문 먼저", True),
     "본문과 요약", "읽는 차례를 <b>먼저</b> 정한다"),
    (code(['.btn { margin-left: auto; }'], "150px", "오른쪽으로 붙이기 — 차례는 안 건드린다", True),
     "오른쪽 정렬", "<code>row-reverse</code>를 안 쓴다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 순서의 계약서",
  code_lede="보이기와 차례를 <b>같이</b> 두면 규칙이 하나로 줄어듭니다.",
  code='''<span class="c">&lt;!-- 마크업 순서가 Tab 순서다. 보이고 싶은 차례대로 적는다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"row"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"ghost"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 오른쪽으로 붙이기 — 차례를 안 건드린다 */</span>
.row { <span class="a">display</span>: flex; <span class="a">gap</span>: <span class="a">8px</span>; }
.row .ghost { <span class="a">margin-right</span>: auto; }

<span class="c">/* ✕ 눈만 뒤집힌다 — Tab 은 저장부터 간다 */</span>
.row { <span class="a">flex-direction</span>: row-reverse; }
.save { <span class="a">order</span>: <span class="a">-1</span>; }

<span class="c">/* ✕ 페이지 전체 차례를 뒤엎는다 */</span>
&lt;<span class="t">button</span> <span class="a">tabindex</span>=<span class="s">"3"</span>&gt;''',
  keys=kbd([
    ("Tab", "마크업 순서로만 간다. CSS 는 <b>영향이 없다</b>"),
    ("Shift + Tab", "그 역순. 눈으로 보는 역순과 <b>다를 수 있다</b>"),
    ("<code>tabindex=\"0\"</code>", "제자리에서 초점을 받는다 — <b>권장</b>"),
    ("<code>tabindex=\"-1\"</code>", "Tab 으로는 못 가고 <code>focus()</code>로만 간다"),
    ("양수 <code>tabindex</code>", "0 인 것들보다 <b>먼저</b> 전부 돈다 — 쓰지 않는다"),
    ("확인하는 법", "주소창에서 Tab 을 계속 누르며 <b>초점 테두리</b>를 눈으로 따라간다"),
  ]),
  backend=rows([
    ("순서대로 보내 준다", "목록 API 가 정렬된 배열을 주면 그대로 그려도 차례가 맞습니다. <b>객체(dict)로 주면</b> 순서 보장이 없어 어긋날 수 있습니다."),
    ("sort 기준을 같이", "<code>?sort=amount.desc</code>처럼 <b>무엇으로 정렬했는지</b>를 응답에도 담으면 화면이 임의로 다시 섞지 않습니다."),
    ("추가되는 줄", "실시간으로 줄이 끼어들면 <b>초점이 엉뚱한 줄</b>로 옮겨집니다 — 끼워 넣기 전에 초점 위치를 기억해 둡니다."),
  ]),
  plat_lede="<b>어디서나 같은 규칙</b>입니다 — 보이기와 차례는 따로 간다.",
  plats=plats([
    ("웹", "DOM order",
     chips(["저장", "취소"], ["1", "2"], None, "110px", "", True),
     "<code>order</code>·<code>row-reverse</code>·<code>position</code>이 전부 <b>보이기만</b> 바꿉니다."),
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
  plat_note="앱 쪽에는 차례를 <b>고쳐 지정하는 길</b>이 있고 웹에는 사실상 없습니다 — 양수 <code>tabindex</code>는 너무 거칠어서 쓰지 않습니다. 그래서 웹에서는 <b>마크업을 옳게 적는 것</b>이 유일한 방법이 되고, 거꾸로 보면 지켜야 할 규칙이 하나뿐이라 간단합니다.",
  siblings=siblings("order"),
  related='''        <li><a href="focus.html"><b>초점</b><em>12부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>겹침 순서</b><em>2부</em></a></li>''',
)
