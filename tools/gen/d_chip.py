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
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted)">켜진 칩은 바탕과 테두리가 함께 바뀐다 — <b style="color:var(--fg)">색만</b> 바꾸면 못 알아본다</div>
                  <div class="pin-out" data-pin="5" style="display:flex;flex-wrap:wrap;gap:6px">
                    ''' + chip("전체") + chip("검토 중", on=True) + chip("승인됨") + chip("거절됨") + '''
                  </div>
                </div>
              </div>'''

D = dict(
  slug="chip", ko="칩", en="Chip · tag · pill",
  desc="필터 칩·입력 칩·표시 칩 세 갈래와 배지와의 차이, 지울 때 포커스 처리를 실물과 해부도로 보여주는 항목.",
  lede="한 낱말짜리 작은 덩어리. 생김새는 하나인데 <b>셋이 서로 다른 일</b>을 해서 가장 많이 헷갈립니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위는 <b>필터 칩</b>(눌러서 거른다), 가운데는 <b>입력 칩</b>(내가 넣은 값이라 뗄 수 있다),
          아래는 <b>표시 칩</b>(그냥 라벨이라 안 눌린다)입니다.<br>
          칩을 <kbd>×</kbd>로 지워 보세요. <b>포커스가 사라지지 않고</b> 다음 칩으로 넘어갑니다 —
          지운 자리에 포커스를 두면 키보드 사용자는 화면 맨 위로 튕깁니다. 삭제 칩의 1번 사고입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "칩, 태그, 필터 칩, 알약"),
    ("영어", "chip, tag, pill, token, filter chip"),
    ("같이 쓰는 말",
     "Material 은 네 갈래로 나눕니다 — <b>어시스트</b>(assist) · <b>필터</b>(filter) · "
     "<b>인풋</b>(input) · <b>서제스천</b>(suggestion). "
     "입력칸 안에 들어간 칩은 <b>토큰</b>(token)이라고도 하고, 떼는 ×는 <b>딜리트 아이콘</b>입니다."),
    ("자주 잘못 부름",
     "<b>배지</b> — 가장 잦은 혼동입니다. <b>배지는 붙어서 알리기만</b> 하고 칩은 눌리거나 떼어집니다.<br>"
     "<b>버튼</b> — 칩도 눌리지만 <b>값을 켜고 끄는</b> 것이지 동작을 일으키지 않습니다.<br>"
     "<b>세그먼티드 컨트롤</b> — 세그먼티드는 <b>하나만</b> 고르고 칸이 붙어 있습니다. 필터 칩은 여럿 고를 수 있습니다."),
  ]),
  axes=ax("칩"),
  oneline="칩은 <b>눌리거나 떼어집니다.</b> 둘 다 아니면 그건 <a href=\"badge.html\">배지</a>이거나 그냥 글자입니다.",
  s4_title="갈래", s4_hint="같은 모양이 세 가지 일을 한다",
  states=states([
    (box(chip("검토 중")), "필터 — 꺼짐", "눌러서 켤 수 있다. 테두리가 있고 바탕은 비어 있다"),
    (box(chip("검토 중", on=True)), "필터 — 켜짐", "<b>바탕과 테두리가 함께</b> 바뀐다. <code>aria-pressed=\"true\"</code>"),
    (box(chip("홍길동", x=True)), "입력", "내가 넣은 값. <b>×로 뗄 수 있다</b>"),
    (box(chip("#정산", static=True)), "표시", "그냥 라벨. <b>테두리와 호버를 빼</b> 눌러 보지 않게 한다"),
    (box(chip("거절됨", style="opacity:.45")), "비활성", "지금은 고를 수 없는 것. <b>왜인지</b>를 옆에 적어 준다"),
    (box(chip("전체") + chip("검토 중", on=True) + chip("승인됨") + chip("거절됨")),
     "무리", "여럿이 모여 한 줄을 이룬다. 넘치면 <b>줄을 넘기거나 가로로 민다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("칩", "chip", "알약 모양 한 덩어리. <b>높이가 32px 안팎</b>이라 버튼보다 작다"),
    ("라벨", "label", "한 낱말. 길어지면 칩이 늘어나니 <b>글자 수 상한</b>을 정해 둔다"),
    ("지우기", "delete icon", "입력 칩에만 붙는다. <b>칩 본체와 다른 누를 것</b>이라 따로 이름이 필요하다"),
    ("켜짐 표시", "selected", "바탕·테두리·글자색이 함께 바뀐다. 체크 아이콘을 넣기도 한다"),
    ("무리", "chip group", "칩들이 모인 줄. <code>role=\"group\"</code>으로 묶고 이름을 붙인다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          입력 칩은 <b>누를 것이 둘</b>입니다 — 칩 본체와 ×. 그래서 키보드로는 칩마다 두 번 멈추고,
          스크린 리더에는 '홍길동', '홍길동 빼기'로 두 번 읽힙니다. ×의 이름을 그냥 '삭제'로 두면
          칩이 열 개일 때 <b>'삭제'가 열 번</b> 읽혀 무엇을 지우는지 알 수 없습니다.</p>''',
  do=ul([
    "목록을 <b>빠르게 거를</b> 때 — 상태·기간·분류",
    "내가 넣은 값을 <b>여러 개 쌓아</b> 보여 줄 때 — 받는 사람, 태그",
    "고를 것이 <b>미리 정해져</b> 있고 개수가 적을 때",
  ]),
  dont=ul([
    "동작을 일으킬 때 → 버튼입니다. 칩은 <b>값</b>을 다룹니다",
    "선택지가 열 개를 넘을 때 → <a href=\"../items/combobox.html\">콤보박스</a>나 필터 패널",
    "하나만 골라야 하고 선택지가 2~4개일 때 → <a href=\"../items/segmented.html\">세그먼티드 컨트롤</a>",
    "누를 수 없는 칩에 <b>테두리와 호버</b>를 주는 것 — 눌러 보게 됩니다",
  ]),
  instead='붙어서 알리기만 하면 <a href="badge.html">배지</a>, 하나만 고르면 <a href="../items/segmented.html">세그먼티드</a>, 많으면 <a href="../items/combobox.html">콤보박스</a>.',
  cases=cases([
    (box(chip("전체") + chip("미처리", on=True) + chip("이번 주") + chip("₩10만 이상")),
     "필터 줄", "목록 바로 위. <b>지금 무엇으로 걸렀는지</b>가 다 보인다"),
    ('''              <div style="width:100%;max-width:200px;border:1px solid var(--line-strong);border-radius:7px;padding:5px;display:flex;flex-wrap:wrap;gap:5px;align-items:center">
                ''' + chip("홍길동", x=True) + chip("김철수", x=True) + '''
                <span style="font-size:11px;color:var(--fg-faint);padding:2px 4px">이름을 쓰고 Enter</span>
              </div>''',
     "입력칸 속 칩", "메일 받는 사람. <b>칩이 입력칸 안에서 쌓인다</b>"),
    (box(chip("#정산", static=True) + chip("#11월", static=True) + chip("#모란상회", static=True)),
     "태그 줄", "분류를 보여 주기만 한다. <b>누르면 그 태그로 걸러지게</b> 만들기도 한다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 부품의 계약서",
  code_lede="필터 칩은 <b>켜고 끄는 버튼</b>이라 <code>aria-pressed</code>를 씁니다. 입력 칩의 ×는 <b>무엇을 지우는지</b>까지 이름에 적습니다.",
  code='''<span class="c">&lt;!-- 필터 칩: 켜고 끄는 버튼 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"group"</span> <span class="a">aria-label</span>=<span class="s">"상태로 거르기"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"true"</span>&gt;검토 중&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"chip"</span> <span class="a">aria-pressed</span>=<span class="s">"false"</span>&gt;승인됨&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">&lt;!-- 입력 칩: 본체와 × 가 각각 누를 것 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"chip"</span>&gt;홍길동
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"홍길동 빼기"</span>&gt;×&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">// 지운 뒤 포커스를 옮긴다 — 안 옮기면 화면 맨 위로 튕긴다</span>
chips.splice(i, <span class="a">1</span>); render();
(next ?? input).focus();''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "칩마다 한 번. <b>입력 칩은 두 번</b>(본체 + ×)"),
    ("<kbd>Enter</kbd> · <kbd>Space</kbd>", "필터 칩을 켜고 끈다"),
    ("<kbd>Backspace</kbd>", "입력칸이 비어 있을 때 누르면 <b>마지막 칩</b>을 뺀다 — 메일 앱의 관례"),
    ("지운 뒤 포커스", "<b>다음 칩, 없으면 입력칸</b>으로. 지운 자리에 두면 포커스가 사라진다"),
    ("× 의 이름", "<code>aria-label=\"홍길동 빼기\"</code> — 그냥 '삭제'면 열 개가 다 같은 말이 된다"),
    ("무리에 이름", "<code>role=\"group\"</code> + <code>aria-label</code>로 '무엇으로 거르는 칩인지' 알린다"),
  ]),
  backend=rows([
    ("필터 칩 = 질의 조건", "켜진 칩이 곧 <code>WHERE</code> 조건입니다. 여럿 켜질 수 있으니 <b>AND 인지 OR 인지</b>를 먼저 정해야 합니다 — 같은 갈래끼리는 보통 OR, 갈래가 다르면 AND 입니다."),
    ("주소에 담기", "<code>?status=wait,ok&period=week</code>처럼 담아 두면 <b>공유와 뒤로가기</b>가 됩니다. 안 담으면 새로고침 때 필터가 날아갑니다."),
    ("개수 보여 주기", "칩에 '검토 중 7' 처럼 수를 붙이려면 <b>거르기 전 전체에서</b> 세야 합니다. 거른 결과에서 세면 늘 자기 수만 나옵니다."),
    ("입력 칩의 값", "화면에 보이는 것은 이름이지만 서버로 가는 것은 <b>ID</b> 입니다. 칩마다 ID 를 함께 들고 있어야 동명이인이 섞이지 않습니다."),
  ]),
  plat_lede="칩은 안드로이드에서 가장 또렷한 부품이고, iOS 에는 같은 이름의 부품이 없습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     box(chip("검토 중", on=True) + chip("승인됨")),
     "<code>&lt;button&gt;</code>에 알약 모양을 준 것입니다. 이름은 팀마다 칩·태그·필터로 갈립니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 토큰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:4px;flex-wrap:wrap">
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:2px 6px">홍길동</span>
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:2px 6px">김철수</span></div>
              </div></div>''',
     "'칩'이라는 부품이 없습니다. 입력칸 속 칩은 <b>토큰</b>이라 부르고, 거르기는 보통 <b>세그먼티드 컨트롤</b>이나 메뉴로 합니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 칩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:4px;flex-wrap:wrap">
                  <span style="font-size:6.5px;border:1px solid var(--line-strong);border-radius:99px;padding:2px 6px">전체</span>
                  <span style="font-size:6.5px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent);border-radius:99px;padding:2px 6px">✓ 검토 중</span></div>
              </div></div>''',
     "<b>Chip</b> 이 정식 부품이고 네 갈래가 규격에 있습니다. 골라진 필터 칩에는 <b>체크 아이콘</b>이 들어갑니다."),
  ]),
  plat_note="\"칩으로 해 주세요\"가 안드로이드에서는 <b>네 갈래 중 어느 것인지</b>까지 정해야 하는 말이고, iOS 쪽에는 <b>그런 부품이 없어서</b> 세그먼티드나 메뉴로 다시 설계해야 합니다. 세 쪽이 같은 화면을 만든다면 '거르기'인지 '내가 넣은 값'인지부터 합의하세요.",
  siblings=siblings("chip"),
  related='''        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/segmented.html"><b>세그먼티드 컨트롤</b><em>4부</em></a></li>
        <li><a href="../items/combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><span class="na"><b>필터와 패싯</b><em>10부</em></span></li>''',
)
