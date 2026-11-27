# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">태그는 분류를 보여 주기만 하고 눌리지 않음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">칩은 눌러서 거르고 aria-pressed를 씀</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">입력 태그는 지울 수 있고 ✕에 이름을 붙임</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">배지는 혼자 놓이지 않고 무언가에 붙음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">줄이 넘치면 +N으로 접음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">색만으로 뜻을 전하지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="tag", ko="태그", en="Tag",
  desc="분류를 보여 주는 작은 알약 모양의 태그를 배지·칩과 가르는 세 가지 질문, 그리고 입력 태그를 지우는 법을 보여 주는 항목입니다.",
  lede="태그는 배지, 칩과 생김새가 거의 같아서 특히 많이 섞여 쓰입니다. 셋을 가르려면 <b>누를 수 있나, 지울 수 있나, 다른 요소에 붙지 않고 혼자 놓이나</b>를 물어보면 됩니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>무엇을 만들지 골라 보세요. 데모가 고른 부품이 세 가지 질문에 어떻게 답하는지 표로 적습니다.<br>
          <b>태그</b>는 분류를 보여 주기만 합니다. <b>칩</b>은 눌러서 목록을 거르고,
          <b>입력 태그</b>는 지울 수 있습니다. <b>배지</b>는 혼자 놓이지 않고
          <b>다른 요소에 붙어서</b> 숫자를 알리며, 누를 수 있는 것은 배지가 아니라 배지가 붙은 요소입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "태그, 라벨, 꼬리표, 분류"),
    ("영어", "tag, label, pill, token"),
    ("같이 쓰는 말",
     "입력칸 안에서 값 하나하나가 알약 모양으로 바뀌는 것은 <b>토큰</b>(token)이나 <b>태그 인풋</b>이라고 부릅니다.  "
     "깃허브나 지라에서 쓰는 색깔 있는 꼬리표는 <b>라벨</b>(label)이라고 부르는데,  "
     "HTML의 <code>&lt;label&gt;</code>과는 전혀 다른 것입니다."),
    ("자주 잘못 부르는 이름",
     "<b>칩</b> — <a href=\"chip.html\">칩</a>은 <b>눌러서 목록을 거르고</b>, 태그는 눌리지 않습니다.<br>"
     "<b>배지</b> — <a href=\"badge.html\">배지</a>는 늘 다른 요소에 붙어서 쓰고 <b>혼자 놓이지 않습니다</b>.<br>"
     "<b>버튼</b> — 알약처럼 생겼다고 해서 버튼은 아닙니다. 누르면 <b>동작이 일어나야</b> 버튼입니다."),
  ]),
  axes=ax("태그"),
  oneline="<b>누를 수 있나, 지울 수 있나, 혼자 놓이나.</b> 이 세 가지만 물으면 배지와 칩과 태그를 가를 수 있습니다.",
  s4_title="비슷한 부품과 상태", s4_hint="태그와 닮은 부품, 그리고 태그가 많거나 길 때의 모습",
  states=states([
    (tags([("정산", ""), ("카드", ""), ("지연", "")], "태그", "분류만 보여 주고 눌리지 않음", True),
     "분류만 보여 주는 태그", "분류를 <b>보여 주기만</b> 합니다"),
    (tags([("정산", ""), ("카드", "on"), ("지연", "")], "칩", "눌러서 목록을 거름", True),
     "눌러서 거르는 칩", "<b>눌러서</b> 켜고 끕니다"),
    (tags([("정산", "x"), ("카드", "x")], "입력 태그", "내가 넣은 값이라 지울 수 있음", True),
     "지울 수 있는 입력 태그", "사용자가 넣은 값이라 <b>지울 수 있습니다</b>"),
    (tags([("알림", ""), ("3", "cnt")], "배지", "혼자 놓이지 않고 무언가에 붙음", None),
     "다른 요소에 붙는 배지", "다른 요소에 붙어서만 쓰고 <b>혼자 놓이지 않습니다</b>"),
    (tags([("정산", ""), ("카드", ""), ("지연", ""), ("+4", "")], "접힘", "줄이 넘치면 +N으로 접음", True),
     "너무 많을 때", "넘치는 태그는 <b>+N</b>으로 접습니다"),
    (tags([("긴 분류 이름이 아주 긴 경…", "")], "긴 이름", "말줄임하거나 줄을 넘김", None),
     "이름이 길 때", "긴 이름은 <b>말줄임</b>합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("태그", "눌리지 않음", "분류를 <b>보여 주기만</b> 합니다"),
    ("칩", "눌러서 켜고 끔", "<code>aria-pressed</code>로 켜짐 상태를 알립니다"),
    ("입력 태그", "지울 수 있음", "✕에 <b>이름을 붙입니다</b>"),
    ("배지", "혼자 놓이지 않음", "배지가 아니라 배지가 <b>붙은</b> 요소가 눌립니다"),
    ("많을 때", "<code>+N</code>", "태그 줄이 세 줄을 넘기 전에 접습니다"),
    ("색", "색만으로 쓰지 않기", "뜻은 색이 아니라 <b>글자</b>로 전합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          태그와 칩과 입력 태그를 섞어 쓰면 <b>누를 수 있는지</b>를 눈으로 가릴 수 없게 됩니다.
          생김새가 같은 알약인데 어떤 것은 눌리고 어떤 것은 눌리지 않으면
          사용자는 <b>하나하나 눌러 보게</b> 됩니다.
          그래서 한 화면 안에서는 <b>한 가지만</b> 쓰거나, 함께 쓰더라도
          눌리는 것과 눌리지 않는 것의 <b>생김새를 다르게</b> 두어야 합니다.<br>
          색으로 분류를 알리는 경우도 흔한데, 색만 쓰면
          <a href="statecolor.html">상태 색</a>에서 본 문제가 그대로 생깁니다.
          뜻은 <b>글자로 전하고</b>, 색은 글자를 돕는 데만 써야 합니다.</p>''',
  do_title="태그를 만들 때 지킬 것", dont_title="태그를 만들 때 피할 것",
  do=ul([
    "한 화면에서는 <b>한 가지만</b> 쓰기",
    "눌리는 것은 <b><code>&lt;button&gt;</code></b>, 눌리지 않는 것은 <code>&lt;span&gt;</code>으로 만들기",
    "지우기 ✕에 <b>'○○ 지우기'</b> 같은 이름 붙이기",
  ]),
  dont=ul([
    "눌리지 않는 태그를 <b>버튼</b>으로 만들기. 사용자가 누를 수 있는 것으로 여깁니다",
    "눌리는 칩을 <b><code>&lt;span&gt;</code></b>으로 두기. 키보드로 누를 수 없습니다",
    "<b>색으로만</b> 분류 알리기",
    "태그 줄이 다섯 줄이 되도록 <b>모두 늘어놓기</b>. 넘치는 태그는 <code>+N</code>으로 접습니다",
  ]),
  instead='눌러서 목록을 걸러야 하면 <a href="chip.html">칩</a>을, 다른 요소에 숫자를 붙여 알리려면 <a href="badge.html">배지</a>를 씁니다. 값을 골라 넣는 칸이라면 <a href="combobox.html">콤보박스</a>가 맞고, 거르기 화면 전체를 설계하는 방법은 <a href="filter.html">필터와 패싯</a>에서 다룹니다.',
  cases=cases([
    (tags([("정산", ""), ("카드", "")], "글의 분류", "", True), "글의 분류 보여 주기", "글이 어떤 분류인지 보여 주기만 합니다"),
    (tags([("정산", "x"), ("카드", "x")], "입력칸 안", "", True), "입력칸에 넣은 값 지우기", "넣은 값을 <b>지울 수 있게</b> 합니다"),
    (tags([("승인됨", "")], "상태", "", True), "처리 상태 알리기", "<a href=\"statecolor.html\">상태 색</a>과 함께 씁니다"),
  ]),
  keys_heads="<th>키와 마크업</th><th>지켜야 할 점</th>",
  code_lede="마크업은 <b>누를 수 있느냐</b>로 갈립니다. 누를 수 있으면 button으로, 그렇지 않으면 span이나 목록 태그로 만듭니다.",
  code='''<span class="c">&lt;!-- 태그: 보여 주기만 한다 --&gt;</span>
&lt;<span class="t">ul</span> <span class="a">class</span>=<span class="s">"tags"</span>&gt;
  &lt;<span class="t">li</span>&gt;정산&lt;/<span class="t">li</span>&gt;&lt;<span class="t">li</span>&gt;카드&lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ul</span>&gt;

<span class="c">&lt;!-- 칩: 눌러서 켜고 끈다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"true"</span>&gt;카드&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 입력 태그: 값 하나하나를 지울 수 있다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"token"</span>&gt;정산
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 지우기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">span</span>&gt;''',
  keys=kbd([
    ("칩에 <code>aria-pressed</code> 달기", "칩이 켜졌는지 알립니다. <b>색만 바꾸면</b> 스크린 리더로는 알 수 없습니다"),
    ("Backspace", "입력 태그에서 <b>마지막 값</b>을 지우는 관습이 있습니다"),
    ("✕ 버튼에 <code>aria-label</code> 붙이기", "✕에는 <b>무엇을 지우는지</b>까지 적습니다"),
    ("태그 묶음은 <code>&lt;ul&gt;</code>로 만들기", "태그 묶음은 목록으로 만듭니다. 그래야 스크린 리더가 태그가 <b>몇 개인지</b> 알려 줍니다"),
    ("Tab", "눌리지 않는 태그에는 포커스가 <b>멈추지 않습니다</b>"),
    ("확인하는 방법", "Tab으로 지나가며 <b>눌리는 것에만</b> 포커스가 멈추는지 봅니다"),
  ]),
  backend=rows([
    ("태그의 이름과 열쇠를 함께 보내기", "<code>{id: \"card\", name: \"카드\"}</code> 처럼 이름과 열쇠를 함께 보내면, <b>목록을 거를 때</b> 바뀔 수 있는 이름 대신 열쇠를 쓸 수 있습니다."),
    ("넣을 수 있는 태그 개수 정하기", "입력 태그를 몇 개까지 넣을 수 있는지는 서버가 정하고, 화면은 그 제한을 <b>미리</b> 적어 둡니다."),
    ("자주 쓰는 순서 함께 보내기", "많이 쓰인 순서를 함께 보내면 화면에서 <b>고르기 목록의 차례</b>를 정할 수 있습니다."),
  ]),
  plat_lede="태그는 부르는 이름이 특히 어지럽게 섞인 부품입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     tags([("정산", ""), ("카드", "on")], "", "", True, "110px"),
     "정해진 부품이 없어서 <b>이름도 제각각</b>이므로, 팀 안에서 이름을 먼저 정해 두는 편이 낫습니다."),
    ("iOS", "정식 부품 없음 · Capsule",
     '''              <div class="phone" role="img" aria-label="iOS 알약 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:18px;height:7px;border-radius:999px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:26px;top:28px;width:14px;height:7px;border-radius:999px;background:var(--accent-soft)"></div></div></div>''',
     "정식 부품이 없어서 <code>Capsule</code> 모양으로 직접 만들고, 목록 거르기에는 <b>세그먼티드 컨트롤</b>을 더 많이 씁니다."),
    ("안드로이드", "Chip",
     '''              <div class="phone" role="img" aria-label="안드로이드 칩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:19px;height:8px;border-radius:999px;border:1px solid var(--accent)"></div>
                <div style="position:absolute;left:27px;top:28px;width:15px;height:8px;border-radius:999px;background:var(--accent-soft)"></div></div></div>''',
     "Material에는 <b>Chip이 assist, filter, input, suggestion 네 종류</b>로 정리되어 있습니다."),
  ]),
  plat_note="Material이 <b>칩을 네 종류로 나눠</b> 이름을 붙여 둔 것이 특히 쓸모 있는 정리입니다. 목록을 거르는 칩(filter), 값을 넣는 칩(input), 추천하는 칩(suggestion), 동작을 일으키는 칩(assist)으로 나뉩니다. 우리가 '태그'라고 부르는 것은 대개 <b>필터 칩이거나 단순한 분류 표시</b>입니다. 그래서 이름을 정할 때 이 네 종류에 견주어 보면 <b>무엇을 만들고 있는지</b>가 분명해집니다.",
  siblings=siblings("tag"),
  related='''        <li><a href="chip.html"><b>칩</b><em>5부</em></a></li>
        <li><a href="badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="combobox.html"><b>콤보박스</b><em>4부</em></a></li>''',
)
