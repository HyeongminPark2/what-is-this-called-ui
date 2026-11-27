# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

def tags(items, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for t, kind in items:
        if kind == 'on':
            st = 'border:1px solid var(--accent);background:var(--accent-soft);color:var(--accent);'
        elif kind == 'cnt':
            st = 'border:1px solid var(--accent);background:var(--accent);color:#fff;'
        else:
            st = 'border:1px solid var(--line);background:var(--surface);color:var(--fg-muted);'
        extra = ' <span style="opacity:.6">✕</span>' if kind == 'x' else ''
        out.append('<span style="' + st + 'border-radius:999px;padding:1px 7px;font-size:8px">'
                   + t + extra + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:4px;flex-wrap:wrap;align-items:center;border:1px solid ' + c + ';'
            'border-radius:6px;background:var(--surface);padding:6px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">태그 — 분류를 보여 준다 · 안 눌린다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">칩 — 눌러서 걸러낸다 · aria-pressed</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">입력 태그 — 지울 수 있다 · ✕ 에 이름을 준다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">배지 — 혼자 서지 못한다 · 무언가에 붙는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">줄이 넘치면 +N 으로 접는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">색으로만 뜻을 싣지 않는다</div>
                </div>
              </div>'''

D = dict(
  slug="tag", ko="태그", en="Tag",
  desc="분류를 보여 주는 작은 알약. 배지·칩과 가르는 세 질문과 입력 태그의 지우기.",
  lede="생김새가 거의 같아 가장 많이 섞여 쓰입니다. 가르는 질문은 셋입니다 — <b>눌리나 · 지울 수 있나 · 혼자 서나</b>.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>무엇을 만들지 골라 보세요 — 데모가 그 셋에 어떻게 답하는지 표로 적습니다.<br>
          <b>태그</b>는 분류를 보여 주기만 합니다. <b>칩</b>은 눌러서 거르고,
          <b>입력 태그</b>는 지울 수 있습니다. <b>배지</b>는 혼자 서지 못하고
          <b>무언가에 붙어</b> 숫자를 알립니다 — 눌리는 것은 배지가 붙은 쪽입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "태그, 라벨, 꼬리표, 분류"),
    ("영어", "tag, label, pill, token"),
    ("같이 쓰는 말",
     "입력칸 안에서 값 하나하나가 알약이 되는 것을 <b>토큰</b>(token)이나 <b>태그 인풋</b>이라 합니다. "
     "깃허브·지라에서 쓰는 색 있는 꼬리표는 <b>라벨</b>(label)이라 부르는데, "
     "HTML 의 <code>&lt;label&gt;</code> 과는 전혀 다른 말입니다."),
    ("자주 잘못 부름",
     "<b>칩</b> — <a href=\"chip.html\">칩</a>은 <b>눌러서 거릅니다</b>. 태그는 안 눌립니다.<br>"
     "<b>배지</b> — <a href=\"badge.html\">배지</a>는 <b>혼자 서지 못합니다</b>.<br>"
     "<b>버튼</b> — 알약처럼 생겼다고 버튼은 아닙니다. <b>동작이 있어야</b> 버튼입니다."),
  ]),
  axes=ax("태그"),
  oneline="<b>눌리나 · 지울 수 있나 · 혼자 서나.</b> 이 셋만 물으면 배지·칩·태그가 갈립니다.",
  states=states([
    (tags([("정산", ""), ("카드", ""), ("지연", "")], "태그", "분류를 보여 준다 — 안 눌린다", True),
     "태그", "<b>보여 주기만</b> 한다"),
    (tags([("정산", ""), ("카드", "on"), ("지연", "")], "칩", "눌러서 걸러낸다", True),
     "칩", "<b>눌린다</b> · 켜고 끈다"),
    (tags([("정산", "x"), ("카드", "x")], "입력 태그", "내가 넣은 값 — 지울 수 있다", True),
     "입력 태그", "<b>지울 수 있다</b>"),
    (tags([("알림", ""), ("3", "cnt")], "배지", "무언가에 붙는다 — 혼자 못 선다", None),
     "배지", "<b>혼자 안 선다</b>"),
    (tags([("정산", ""), ("카드", ""), ("지연", ""), ("+4", "")], "접힘", "줄이 넘치면 +N 으로", True),
     "너무 많을 때", "<b>+N</b> 으로 접는다"),
    (tags([("긴 분류 이름이 아주 긴 경…", "")], "긴 이름", "말줄임하거나 줄을 넘긴다", None),
     "이름이 길 때", "<b>말줄임</b>한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("태그", "안 눌림", "분류를 <b>보여 주기만</b>"),
    ("칩", "눌림", "<code>aria-pressed</code> 로 상태"),
    ("입력 태그", "지움", "✕ 에 <b>이름을 준다</b>"),
    ("배지", "혼자 못 섬", "<b>붙는</b> 쪽이 눌린다"),
    ("많을 때", "<code>+N</code>", "줄이 세 줄 넘기 전에 접는다"),
    ("색", "혼자 쓰지 않기", "<b>글자</b>가 뜻을 진다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          셋을 섞어 쓰면 <b>누를 수 있는지</b>를 눈으로 가릴 수 없게 됩니다 —
          같은 알약인데 어떤 것은 눌리고 어떤 것은 안 눌리면
          사용자는 <b>전부 눌러 보게</b> 됩니다.
          한 화면 안에서는 <b>한 가지만</b> 쓰거나, 쓰더라도
          눌리는 것과 안 눌리는 것의 <b>생김새를 다르게</b> 둬야 합니다.<br>
          색으로 분류를 알리는 것도 흔한데, 색만으로는
          <a href="statecolor.html">상태 색</a>에서 본 문제가 그대로 생깁니다 —
          <b>글자가 뜻을 지고</b> 색은 거드는 역할이어야 합니다.</p>''',
  do=ul([
    "한 화면에서는 <b>한 가지만</b> 쓰기",
    "눌리는 것은 <b><code>&lt;button&gt;</code></b>, 아닌 것은 <code>&lt;span&gt;</code>",
    "지우기 ✕ 에 <b>'○○ 지우기'</b> 이름 붙이기",
  ]),
  dont=ul([
    "안 눌리는 태그를 <b>버튼</b>으로 만들기 — 누를 줄 알게 된다",
    "눌리는 칩을 <b><code>&lt;span&gt;</code></b> 으로 두기 — 키보드로 못 쓴다",
    "<b>색으로만</b> 분류 알리기",
    "줄이 다섯 줄 되도록 <b>다 늘어놓기</b> — <code>+N</code> 으로 접는다",
  ]),
  instead='눌러서 거르면 <a href="chip.html">칩</a>, 숫자를 붙이면 <a href="badge.html">배지</a>, 값을 고르는 칸이면 <a href="combobox.html">콤보박스</a>, 거르기 화면 전체는 <a href="filter.html">필터와 패싯</a>.',
  cases=cases([
    (tags([("정산", ""), ("카드", "")], "글의 분류", "", True), "글의 분류", "읽기만 한다"),
    (tags([("정산", "x"), ("카드", "x")], "입력칸 안", "", True), "입력칸 안", "<b>지울 수 있게</b>"),
    (tags([("승인됨", "")], "상태", "", True), "상태 표시", "<a href=\"statecolor.html\">상태 색</a>과 함께"),
  ]),
  code_lede="<b>눌리느냐</b>가 태그를 가릅니다 — 눌리면 버튼, 아니면 span 입니다.",
  code='''<span class="c">&lt;!-- 태그 — 보여 주기만 한다 --&gt;</span>
&lt;<span class="t">ul</span> <span class="a">class</span>=<span class="s">"tags"</span>&gt;
  &lt;<span class="t">li</span>&gt;정산&lt;/<span class="t">li</span>&gt;&lt;<span class="t">li</span>&gt;카드&lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ul</span>&gt;

<span class="c">&lt;!-- 칩 — 눌러서 켜고 끈다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"true"</span>&gt;카드&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 입력 태그 — 값 하나하나를 지울 수 있다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"token"</span>&gt;정산
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 지우기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">span</span>&gt;''',
  keys=kbd([
    ("<code>aria-pressed</code>", "칩이 켜졌는지. <b>색만으로는</b> 안 들린다"),
    ("Backspace", "입력 태그에서 <b>마지막 값</b>을 지우는 관습이 있다"),
    ("<code>aria-label</code>", "✕ 에는 <b>무엇을 지우는지</b>까지 적는다"),
    ("<code>&lt;ul&gt;</code>", "태그 묶음은 목록이다 — <b>몇 개인지</b>가 소리로 전해진다"),
    ("Tab", "안 눌리는 태그는 <b>멈추지 않는다</b>"),
    ("확인하는 법", "Tab 으로 지나며 <b>눌리는 것만</b> 멈추는지 본다"),
  ]),
  backend=rows([
    ("태그는 이름과 열쇠를 같이", "<code>{id: \"card\", name: \"카드\"}</code> 처럼 주면 <b>걸러낼 때</b> 이름이 아니라 열쇠를 씁니다."),
    ("개수 제한", "입력 태그에 몇 개까지 넣을 수 있는지는 서버가 정합니다 — <b>화면에 미리</b> 적어 둡니다."),
    ("자주 쓰는 태그", "많이 쓰인 순서를 주면 <b>고르기 목록의 차례</b>를 정할 수 있습니다."),
  ]),
  plat_lede="이름이 가장 어지러운 부품입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     tags([("정산", ""), ("카드", "on")], "", "", True, "110px"),
     "정해진 부품이 없어 <b>이름도 제각각</b>입니다 — 팀 안에서 먼저 정해 두는 편이 낫습니다."),
    ("iOS", "없다 — Capsule",
     '''              <div class="phone" role="img" aria-label="iOS 알약 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:18px;height:7px;border-radius:999px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:26px;top:28px;width:14px;height:7px;border-radius:999px;background:var(--accent-soft)"></div></div></div>''',
     "정식 부품이 없습니다. <code>Capsule</code> 모양으로 직접 만들고, 거르기에는 <b>세그먼티드</b>를 더 씁니다."),
    ("안드로이드", "Chip",
     '''              <div class="phone" role="img" aria-label="안드로이드 칩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:19px;height:8px;border-radius:999px;border:1px solid var(--accent)"></div>
                <div style="position:absolute;left:27px;top:28px;width:15px;height:8px;border-radius:999px;background:var(--accent-soft)"></div></div></div>''',
     "Material 에 <b>Chip 이 네 종류</b>로 정리돼 있습니다 — assist · filter · input · suggestion."),
  ]),
  plat_note="Material 이 <b>칩을 네 종류로 나눠</b> 이름을 붙여 둔 것이 가장 쓸모 있는 정리입니다 — 거르는 칩(filter), 값을 넣는 칩(input), 권하는 칩(suggestion), 동작하는 칩(assist). 우리말로 '태그'라 부르는 것은 대개 <b>필터 칩이거나 그냥 분류 표시</b>입니다. 이름을 정할 때 이 네 갈래에 대 보면 <b>무엇을 만들고 있는지</b>가 분명해집니다.",
  siblings=siblings("tag"),
  related='''        <li><a href="chip.html"><b>칩</b><em>5부</em></a></li>
        <li><a href="badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="combobox.html"><b>콤보박스</b><em>4부</em></a></li>''',
)
