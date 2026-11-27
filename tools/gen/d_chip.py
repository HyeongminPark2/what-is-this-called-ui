# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def chip(txt, on=False, x=False, static=False, style=""):
    base = ('display:inline-flex;align-items:center;gap:5px;min-height:26px;padding:3px 10px;'
            'border-radius:99px;font-size:11.5px;')
    if on:
        base += 'background:var(--accent-soft);border:1px solid var(--accent);color:var(--accent);font-weight:700;'
    elif static:
        base += 'background:var(--bg);border:1px solid transparent;color:var(--fg-muted);'
    else:
        base += 'background:var(--surface);border:1px solid var(--line-strong);color:var(--fg);'
    xb = ('<span style="display:grid;place-items:center;width:14px;height:14px;margin-right:-3px;'
          'border-radius:99px;background:rgba(0,0,0,.08);font-size:9px;line-height:1">×</span>') if x else ''
    return '<span style="%s%s">%s%s</span>' % (base, style, txt, xb)

def box(inner):
    return '              <div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center">%s</div>' % inner

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:inline-flex;align-items:center;gap:6px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:99px;padding:5px 12px;justify-self:start">
                    <span class="pin-out" data-pin="2" style="font-size:11.5px;color:var(--accent);font-weight:700;margin-left:26px">검토 중</span>
                    <span class="pin-tr" data-pin="3" style="display:grid;place-items:center;width:15px;height:15px;border-radius:99px;background:rgba(47,109,246,.18);color:var(--accent);font-size:9px;line-height:1">×</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted)">켜진 칩은 바탕과 테두리가 함께 바뀜. <b style="color:var(--fg)">색만</b> 바꾸면 알아보기 어려움</div>
                  <div class="pin-out" data-pin="5" style="display:flex;flex-wrap:wrap;gap:6px">
                    ''' + chip("전체") + chip("검토 중", on=True) + chip("승인됨") + chip("거절됨") + '''
                  </div>
                </div>
              </div>'''

D = dict(
  slug="chip", ko="칩", en="Chip · tag · pill",
  desc="필터 칩·입력 칩·표시 칩 세 갈래와 배지와의 차이, 칩을 지울 때 포커스를 어디로 옮기는지를 실물과 해부도로 보여 주는 항목입니다.",
  lede="칩은 한 낱말을 담은 작은 알약 모양의 부품입니다. 생김새는 하나인데 필터 칩, 입력 칩, 표시 칩 <b>세 가지가 서로 다른 일</b>을 하기 때문에 특히 많이 헷갈립니다.",
  axes_lede="표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위는 눌러서 목록을 거르는 <b>필터 칩</b>, 가운데는 사용자가 넣은 값이라 뗄 수 있는 <b>입력 칩</b>,
          아래는 라벨일 뿐이라 눌리지 않는 <b>표시 칩</b>입니다.<br>
          칩을 <kbd>×</kbd>로 지워 보세요. <b>포커스가 사라지지 않고</b> 다음 칩으로 넘어갑니다.
          지운 칩에 있던 포커스를 그대로 두면 포커스가 갈 곳을 잃고 화면 맨 위로 돌아가 버리는데, 지울 수 있는 칩에서 특히 흔한 오류입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "칩, 태그, 필터 칩, 알약"),
    ("영어", "chip, tag, pill, token, filter chip"),
    ("같이 쓰는 말",
     "Material은 칩을 <b>어시스트</b>(assist) · <b>필터</b>(filter) ·  "
     "<b>인풋</b>(input) · <b>서제스천</b>(suggestion) 네 가지로 나눕니다.  "
     "입력칸 안에 들어간 칩은 <b>토큰</b>(token)이라고도 하고, 칩을 떼는 ×는 <b>딜리트 아이콘</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>배지</b> — 칩과 가장 자주 헷갈리는 부품입니다. <b>배지는 다른 요소에 붙어서 알리기만</b> 하고, 칩은 누르거나 뗄 수 있습니다.<br>"
     "<b>버튼</b> — 칩도 누를 수 있지만, 칩을 누르면 <b>값이 켜지거나 꺼질</b> 뿐 저장이나 전송 같은 동작이 일어나지는 않습니다.<br>"
     "<b>세그먼티드 컨트롤</b> — 세그먼티드 컨트롤은 칸이 서로 붙어 있고 <b>하나만</b> 고를 수 있는 반면, 필터 칩은 여럿을 함께 고를 수 있습니다."),
  ]),
  axes=ax("칩"),
  oneline="칩은 <b>누르거나 뗄 수 있습니다.</b> 누를 수도 뗄 수도 없다면 그건 칩이 아니라 <a href=\"badge.html\">배지</a>이거나 그냥 글자입니다.",
  s4_title="칩의 종류와 상태", s4_hint="종류와 상태마다 달라지는 칩 모습",
  states=states([
    (box(chip("검토 중")), "꺼져 있는 필터 칩", "눌러서 켤 수 있습니다. 테두리만 있고 바탕은 비어 있습니다"),
    (box(chip("검토 중", on=True)), "켜져 있는 필터 칩", "<b>바탕과 테두리가 함께</b> 바뀌고, 코드에는 <code>aria-pressed=\"true\"</code>를 답니다"),
    (box(chip("홍길동", x=True)), "사용자가 넣은 입력 칩", "사용자가 넣은 값입니다. <b>×로 뗄 수 있습니다</b>"),
    (box(chip("#정산", static=True)), "보여 주기만 하는 표시 칩", "라벨일 뿐인 칩입니다. <b>테두리와 호버 효과를 빼서</b> 사용자가 눌러 보지 않게 합니다"),
    (box(chip("거절됨", style="opacity:.45")), "지금은 고를 수 없을 때", "지금은 고를 수 없는 칩입니다. <b>왜 고를 수 없는지</b>를 옆에 적어 줍니다"),
    (box(chip("전체") + chip("검토 중", on=True) + chip("승인됨") + chip("거절됨")),
     "여러 칩이 한 줄로 모였을 때", "여러 칩이 모여 한 줄을 이룹니다. 줄이 넘치면 <b>다음 줄로 넘기거나 가로로 밀어 보게</b> 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("칩", "chip", "알약 모양의 한 덩어리입니다. <b>높이가 32px 안팎</b>이라서 버튼보다 작습니다"),
    ("라벨", "label", "한 낱말을 담습니다. 글이 길어지면 칩도 길어지므로 <b>글자 수 상한</b>을 정해 둡니다"),
    ("지우기", "delete icon", "입력 칩에만 붙습니다. <b>칩 본체와는 별도로 누르는 곳</b>이라서 스크린 리더가 읽을 이름을 따로 붙여야 합니다"),
    ("켜짐 표시", "selected", "칩이 켜지면 바탕, 테두리, 글자색이 함께 바뀝니다. 체크 아이콘을 넣기도 합니다"),
    ("무리", "chip group", "칩들이 모인 줄입니다. <code>role=\"group\"</code>으로 묶고 이름을 붙입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          입력 칩에는 칩 본체와 × 두 가지, 즉 <b>누를 것이 둘</b> 있습니다. 그래서 키보드 포커스는 칩마다 두 번 멈추고,
          스크린 리더는 '홍길동', '홍길동 빼기'처럼 두 번 읽습니다. 이때 ×의 이름을 그냥 '삭제'로 두면
          칩이 열 개일 때 <b>'삭제'를 열 번</b> 읽어서 무엇을 지우는지 알 수 없습니다.</p>''',
  do=ul([
    "상태, 기간, 분류로 목록을 <b>빠르게 거를</b> 때",
    "받는 사람이나 태그처럼 사용자가 넣은 값을 <b>여러 개 쌓아</b> 보여 줄 때",
    "고를 것이 <b>미리 정해져</b> 있고 개수가 적을 때",
  ]),
  dont=ul([
    "누르면 동작이 일어나야 할 때. 동작은 버튼으로 만들고, 칩은 <b>값</b>을 다룰 때만 씁니다",
    "선택지가 열 개를 넘을 때. <a href=\"../items/combobox.html\">콤보박스</a>나 필터 패널을 씁니다",
    "하나만 골라야 하고 선택지가 2~4개일 때. <a href=\"../items/segmented.html\">세그먼티드 컨트롤</a>을 씁니다",
    "누를 수 없는 칩에 <b>테두리와 호버 효과</b>를 줄 때. 사용자가 누를 수 있는 줄 알고 눌러 봅니다",
  ]),
  instead='다른 요소에 붙어서 알리기만 하면 <a href="badge.html">배지</a>를 쓰고, 몇 안 되는 선택지 가운데 하나만 골라야 하면 <a href="../items/segmented.html">세그먼티드 컨트롤</a>을 씁니다. 선택지가 많다면 <a href="../items/combobox.html">콤보박스</a>가 맞습니다.',
  cases=cases([
    (box(chip("전체") + chip("미처리", on=True) + chip("이번 주") + chip("₩10만 이상")),
     "목록 위에서 조건으로 거르기", "목록 바로 위에 놓여서 <b>지금 무엇으로 걸렀는지</b>가 한눈에 보입니다"),
    ('''              <div style="width:100%;max-width:200px;border:1px solid var(--line-strong);border-radius:7px;padding:5px;display:flex;flex-wrap:wrap;gap:5px;align-items:center">
                ''' + chip("홍길동", x=True) + chip("김철수", x=True) + '''
                <span style="font-size:11px;color:var(--fg-faint);padding:2px 4px">이름을 쓰고 Enter</span>
              </div>''',
     "입력칸 안에 받는 사람 쌓기", "메일 받는 사람 칸에서 흔히 봅니다. <b>칩이 입력칸 안에 차례로 쌓입니다</b>"),
    (box(chip("#정산", static=True) + chip("#11월", static=True) + chip("#모란상회", static=True)),
     "글의 분류를 태그로 보여 주기", "분류를 보여 주기만 합니다. 다만 <b>누르면 그 태그로 목록이 걸러지게</b> 만들기도 합니다"),
  ]),
  s8_title="최소 마크업과 키보드",
  code_lede="필터 칩은 <b>켜고 끄는 버튼</b>이므로 <code>aria-pressed</code>로 상태를 알립니다. 입력 칩의 ×에는 <b>무엇을 지우는지</b>까지 이름에 적습니다.",
  code='''<span class="c">&lt;!-- 필터 칩: 켜고 끄는 버튼 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"group"</span> <span class="a">aria-label</span>=<span class="s">"상태로 거르기"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"true"</span>&gt;검토 중&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"false"</span>&gt;승인됨&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">&lt;!-- 입력 칩: 본체와 × 를 따로 누른다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"chip"</span>&gt;홍길동
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"홍길동 빼기"</span>&gt;×&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">// 지운 뒤 포커스를 옮긴다. 안 옮기면 포커스가 화면 맨 위로 돌아간다</span>
chips.splice(i, <span class="a">1</span>); render();
(next ?? input).focus();''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "포커스가 칩마다 한 번 멈춥니다. <b>입력 칩에서는 두 번</b>(본체와 ×) 멈춥니다"),
    ("<kbd>Enter</kbd> · <kbd>Space</kbd>", "필터 칩을 켜고 끕니다"),
    ("<kbd>Backspace</kbd>", "입력칸이 비어 있을 때 누르면 <b>마지막 칩</b>을 뺍니다. 메일 앱에서 굳어진 관례입니다"),
    ("칩을 지운 뒤의 포커스", "포커스를 <b>다음 칩으로, 다음 칩이 없으면 입력칸으로</b> 옮깁니다. 지운 칩에 두면 포커스가 사라집니다"),
    ("× 버튼의 이름", "<code>aria-label=\"홍길동 빼기\"</code> 처럼 이름을 붙입니다. 그냥 '삭제'라고 하면 칩 열 개의 ×가 모두 같은 이름이 됩니다"),
    ("칩 무리의 이름", "<code>role=\"group\"</code> + <code>aria-label</code>로 무엇을 기준으로 거르는 칩인지 알립니다"),
  ]),
  backend=rows([
    ("필터 칩은 질의 조건", "켜진 칩은 질의의 <code>WHERE</code> 조건이 됩니다. 칩이 여럿 켜질 수 있으므로 조건을 <b>AND로 묶을지 OR로 묶을지</b> 먼저 정해야 하는데, 보통 같은 갈래의 칩끼리는 OR, 갈래가 다른 칩끼리는 AND로 묶습니다."),
    ("필터를 주소에 담기", "<code>?status=wait,ok&period=week</code>처럼 필터를 주소에 담아 두면 <b>주소 공유와 뒤로가기</b>로도 같은 필터가 유지됩니다. 주소에 담지 않으면 새로고침할 때 필터가 풀립니다."),
    ("칩에 건수를 붙일 때", "칩에 '검토 중 7'처럼 건수를 붙이려면 <b>거르기 전의 전체 목록에서</b> 세어야 합니다. 이미 거른 결과에서 세면 지금 켜진 칩에 해당하는 건수만 나옵니다."),
    ("입력 칩이 서버로 보내는 값", "화면에는 이름이 보이지만 서버로 보내는 값은 <b>ID</b>입니다. 칩마다 ID를 함께 들고 있어야 이름이 같은 사람끼리 섞이지 않습니다."),
  ]),
  plat_lede="칩은 안드로이드에서는 규격이 또렷하게 정해진 부품이지만, iOS에는 같은 이름의 부품이 없습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     box(chip("검토 중", on=True) + chip("승인됨")),
     "<code>&lt;button&gt;</code>을 알약 모양으로 꾸며 만듭니다. 팀마다 칩, 태그, 필터 등 부르는 이름이 다릅니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:4px;flex-wrap:wrap">
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:2px 6px">홍길동</span>
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:2px 6px">김철수</span></div>
              </div></div>''',
     "'칩'이라는 부품이 없습니다. 입력칸 속 칩은 <b>토큰</b>이라고 부르고, 목록 거르기는 보통 <b>세그먼티드 컨트롤</b>이나 메뉴로 만듭니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 칩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:4px;flex-wrap:wrap">
                  <span style="font-size:6.5px;border:1px solid var(--line-strong);border-radius:99px;padding:2px 6px">전체</span>
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent);border-radius:99px;padding:2px 6px">✓ 검토 중</span></div>
              </div></div>''',
     "<b>Chip</b>이 정식 부품으로 있고, 규격에 네 가지 종류가 정해져 있습니다. 골라진 필터 칩에는 <b>체크 아이콘</b>이 들어갑니다."),
  ]),
  plat_note="\"칩으로 해 주세요\"라는 요청을 받으면 안드로이드에서는 <b>네 가지 종류 가운데 어느 것인지</b>까지 정해야 하고, iOS에는 <b>그런 부품이 없어서</b> 세그먼티드 컨트롤이나 메뉴로 다시 설계해야 합니다. 웹, iOS, 안드로이드가 같은 화면을 만든다면, 그 칩이 목록을 거르는 칩인지 사용자가 넣은 값을 보여 주는 칩인지부터 합의하세요.",
  siblings=siblings("chip"),
  related='''        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/segmented.html"><b>세그먼티드 컨트롤</b><em>4부</em></a></li>
        <li><a href="../items/combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>''',
)
