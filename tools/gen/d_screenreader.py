# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sr(visual, said, ok=True, w="168px"):
    color = "#1f8a4c" if ok else "var(--danger)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:7px;justify-items:center">'
            + visual +
            '<span style="font-family:var(--mono);font-size:10px;color:' + color + ';font-weight:700;text-align:center">' + said + '</span></div>')

def sw(on=False):
    bg = "var(--accent)" if on else "var(--line-strong)"
    x = "16px" if on else "2px"
    return ('<span style="display:inline-flex;align-items:center;gap:6px;font-size:11px">'
            '<span style="position:relative;width:34px;height:20px;border-radius:99px;background:' + bg + ';display:inline-block">'
            '<span style="position:absolute;left:' + x + ';top:2px;width:16px;height:16px;border-radius:99px;background:#fff"></span>'
            '</span>이메일 알림</span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:inline-flex;align-items:center;gap:7px;font-size:12px;justify-self:start">
                    <span style="position:relative;width:38px;height:22px;border-radius:99px;background:var(--accent);display:inline-block">
                      <span style="position:absolute;left:18px;top:2px;width:18px;height:18px;border-radius:99px;background:#fff"></span>
                    </span>이메일 알림
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">role="switch"   — 이게 무엇인가</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이름 "이메일 알림"   — 뭐라고 부르나</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">aria-checked="true"   — 지금 어떤가</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-expanded · disabled · aria-selected</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">색·위치로만 표현한 것은 안 읽힌다</div>
                </div>
              </div>'''

D = dict(
  slug="screenreader", ko="스크린 리더가 읽는 것", en="What screen readers announce",
  desc="스크린 리더가 역할, 이름, 상태 세 가지로 화면을 읽는다는 것과, 화면의 상태를 말로 옮겨 주는 aria 속성을 보여 주는 항목입니다.",
  lede="스크린 리더는 화면의 요소마다 <b>세 가지</b>를 읽습니다. 그 요소가 무엇인지 알려 주는 <b>역할</b>, 무엇이라고 부르는지 알려 주는 <b>이름</b>, 지금 어떤 상태인지 알려 주는 <b>상태</b>입니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>스위치를 켜고 '자세히'를 펼쳐 보세요. 아래 접근성 트리에서 <b>상태가 바로 바뀝니다</b>.<br>
          <b>role·state 를 빼고 보기</b>를 켜면 트리에 이름만 남기 때문에, '이메일 알림'이
          <b>스위치인지 버튼인지, 켜져 있는지 꺼져 있는지</b> 알 수 없게 됩니다.
          눈으로 보면 모두 알 수 있는 정보인데도 스크린 리더로는 전달되지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스크린 리더, 화면 낭독기, 접근성 트리"),
    ("영어", "screen reader, accessibility tree, role · name · state"),
    ("같이 쓰는 말",
     "브라우저가 스크린 리더에 넘겨주려고 만드는 구조를 <b>접근성 트리</b>(accessibility tree)라고 합니다. "
     "대표적인 스크린 리더로는 <b>NVDA·JAWS</b>(윈도), <b>VoiceOver</b>(맥·아이폰), "
     "<b>TalkBack</b>(안드로이드)이 있습니다. 역할은 <code>role</code> 속성에, "
     "상태는 <code>aria-*</code> 속성에 적습니다."),
    ("자주 잘못 부르는 이름",
     "<b>ARIA</b> — <code>aria-*</code>는 <b>알맞은 태그가 없을 때 빈 곳을 채우는 수단</b>이고, 기본 수단이 아닙니다. "
     "알맞은 태그가 있으면 그 태그를 씁니다.<br>"
     "<b><code>role</code>을 붙이면 동작이 생긴다</b> — 동작은 <b>생기지 않습니다.</b> 스크린 리더가 읽는 역할만 바뀌고, 키 처리는 직접 짜야 합니다.<br>"
     "<b>읽기 전용</b> — <code>aria-hidden</code>은 스크린 리더가 <b>읽지 않게</b> 하는 속성이고, 화면에서 숨기지는 않습니다."),
  ]),
  axes=ax("스크린 리더가 읽는 것"),
  oneline="화면에서 <b>색과 위치로만</b> 표현한 정보는 스크린 리더가 소리로 전달하지 못합니다. 그래서 요소의 상태는 <b>속성으로 따로 적어</b> 둬야 합니다.",
  s4_title="갈래", s4_hint="무엇이 읽히고 무엇이 안 읽히나",
  states=states([
    (sr(sw(False), '"이메일 알림, 스위치, 꺼짐"'), "역할+이름+상태", "세 가지가 모두 있습니다. <b>모든 요소가 갖춰야 하는 기본</b>입니다"),
    (sr(sw(True), '"이메일 알림, 스위치, 켜짐"'), "상태가 바뀜", "<code>aria-checked</code> 값을 바꿔야 <b>스크린 리더가 읽는 말도 바뀝니다</b>"),
    (sr(sw(True), '"이메일 알림" — 역할·상태 없음', False), "속성이 없으면", "스크린 리더로는 <b>켜졌는지 알 수 없습니다</b>. 눈으로만 확인할 수 있습니다"),
    (sr('<span style="display:inline-block;border:1px solid var(--line-strong);border-radius:6px;padding:6px 11px;font-size:11px">자세히</span>',
        '"자세히, 버튼, 접힘"'), "펼침 상태", "<code>aria-expanded</code>는 <b>버튼을 누르면 무엇이 펼쳐지거나 접히는지</b> 알려 줍니다"),
    (sr('<span style="display:inline-block;border:1px solid var(--line-strong);border-radius:6px;padding:6px 11px;font-size:11px;opacity:.45">확정</span>',
        '"확정, 버튼, 흐림"'), "비활성", "<code>disabled</code>를 달면 버튼이 왜 눌리지 않는지 알려 줍니다"),
    (sr('<span style="display:inline-grid;place-items:center;width:30px;height:30px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700">길동</span>',
        '(안 읽힘) — aria-hidden'), "일부러 안 읽히기", "옆에 같은 이름이 글자로 또 있으면 <b>그림은 읽지 않게 뺍니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("부품 하나", "element", "눈에는 스위치 하나로 보이지만, 스크린 리더는 <b>세 가지 정보</b>로 읽습니다"),
    ("역할", "role", "버튼, 스위치, 탭, 목록처럼 요소가 무엇인지 나타냅니다. <b>태그에 역할이 들어 있으면 따로 적지 않아도 됩니다</b>"),
    ("이름", "accessible name", "요소를 무엇이라고 부르는지 나타냅니다. 이름을 정하는 규칙은 <a href=\"name.html\">이름 붙이기</a>에서 다룹니다"),
    ("상태", "aria-checked 등", "요소가 지금 어떤 상태인지 나타냅니다. 상태가 <b>바뀔 때마다 속성 값도 같이 바꿔야</b> 합니다"),
    ("상태 속성들", "expanded · selected · disabled", "펼침, 골라짐, 비활성처럼 화면에 모양으로 표현한 상태를 <b>스크린 리더가 읽을 수 있는 말로 옮깁니다</b>"),
    ("안 읽히는 것", "색 · 위치 · 굵기", "색, 위치, 굵기는 <b>소리로 전달되지 않기</b> 때문에 속성으로 따로 적어야 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>role</code>을 붙여도 <b>동작은 생기지 않습니다.</b>
          <code>role="button"</code>은 스크린 리더에게 이 요소를 버튼이라고 읽으라고 알려 줄 뿐이고, Enter와 Space 처리는
          여전히 직접 짜야 합니다. 그래서 <b>ARIA 사용 규칙의 첫 번째가 "ARIA를 쓰지 않는 것"</b>입니다.
          <code>&lt;button&gt;</code>을 쓰면 역할과 동작이 <b>함께</b> 들어오기 때문입니다.</p>''',
  do=ul([
    "켜짐, 펼침, 골라짐, 비활성처럼 <b>상태가 바뀌는 요소</b>를 만들 때",
    "탭, 콤보박스, 스위치를 직접 만들 때. <code>role</code>과 상태 속성이 필요합니다",
    "장식용 아이콘을 넣을 때. <code>aria-hidden=\"true\"</code>로 읽지 않게 합니다",
  ]),
  dont=ul([
    "<b>알맞은 태그가 있는데도</b> <code>role</code>로 흉내 낼 때",
    "상태 속성을 <b>처음 한 번만</b> 적고 바꾸지 않을 때. 화면과 다른 상태를 읽게 됩니다",
    "<code>aria-hidden</code>을 <b>포커스를 받는 요소</b>에 걸 때. 포커스는 가는데 스크린 리더가 아무것도 읽지 않습니다",
    "색이나 위치로만 상태를 표현할 때",
  ]),
  instead='이름만 다루려면 <a href="name.html">이름 붙이기</a>, 태그 고르기는 <a href="semantics.html">시맨틱 태그</a>, 저절로 바뀌는 것은 <a href="live.html">라이브 리전</a>.',
  cases=cases([
    (sr(sw(True), '"이메일 알림, 스위치, 켜짐"', True, "190px"), "스위치", "<code>role=\"switch\"</code>와 <code>aria-checked</code>로 역할과 켜짐 상태를 알립니다"),
    ('''              <div style="width:100%;max-width:190px;display:flex;gap:10px;border-bottom:1px solid var(--line);padding-bottom:4px">
                <span style="font-size:11px;color:var(--accent);font-weight:700;border-bottom:2px solid var(--accent);padding-bottom:4px;margin-bottom:-5px">개요</span>
                <span style="font-size:11px;color:var(--fg-muted)">거래</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);margin-top:7px;text-align:center">"개요, 탭, 1/2, 선택됨"</div>''',
     "탭", "탭이 <b>몇 개 중 몇 번째</b>인지까지 읽힙니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="border:1px solid var(--danger);border-radius:5px;padding:6px 9px;font-size:11px">1234</span>
                <span style="font-size:10px;color:var(--danger)">계좌번호는 10자리입니다</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);margin-top:6px;text-align:center">"계좌번호, 편집, 잘못됨"</div>''',
     "에러 상태", "<code>aria-invalid</code>로 잘못된 값임을 알리고 <code>aria-describedby</code>로 에러 문구를 연결합니다. <b>빨간 테두리만으로는 스크린 리더에 전달되지 않습니다</b>"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="역할·이름·상태 세 줄",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="역할과 상태는 <b>태그로 줄 수 있으면 태그로</b> 주고, 태그로 줄 수 없을 때만 <code>role</code>과 <code>aria-*</code>로 채웁니다.",
  code='''<span class="c">&lt;!-- 태그가 역할을 주는 방법이 가장 좋다 --&gt;</span>
&lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">id</span>=<span class="s">"n"</span>&gt;&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"n"</span>&gt;알림&lt;/<span class="t">label</span>&gt;

<span class="c">&lt;!-- 알맞은 태그가 없을 때만 role로 채운다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"switch"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>
      <span class="a">aria-checked</span>=<span class="s">"false"</span>&gt;이메일 알림&lt;/<span class="t">span</span>&gt;

<span class="c">// 상태가 바뀌면 속성도 같이 바꾼다. 안 바꾸면 화면과 다른 상태를 읽는다</span>
el.setAttribute(<span class="s">'aria-checked'</span>, String(on));

<span class="c">&lt;!-- 장식은 아예 빼 둔다 --&gt;</span>
&lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;''',
  keys=kbd([
    ("태그를 먼저", "<code>&lt;button&gt;</code>이나 <code>&lt;input&gt;</code>을 쓰면 역할과 동작이 함께 들어옵니다"),
    ("<code>role</code>은 보조 수단", "역할만 바뀌고 <b>키 처리는 따라오지 않습니다</b>"),
    ("상태를 같이 바꾼다", "화면에 보이는 상태가 바뀔 때마다 <code>aria-*</code> 값도 바꿉니다"),
    ("장식은 숨긴다", "<code>aria-hidden=\"true\"</code>로 숨기되, <b>포커스를 받는 요소에는 걸지 않습니다</b>"),
    ("에러는 말로", "빨간 테두리에 더해 <code>aria-invalid</code>와 <code>aria-describedby</code>로 에러를 말로 알립니다"),
    ("트리를 본다", "개발자 도구의 Accessibility 패널에서 <b>실제로 무엇이라고 읽힐지</b> 확인합니다"),
  ]),
  backend=rows([
    ("상태는 서버가 아는 것과 다르다", "서버의 <code>status</code>는 데이터이고, <code>aria-expanded</code>는 <b>지금 화면에 보이는 모습</b>입니다. 둘을 혼동하면 화면에서는 접혀 있는 패널을 스크린 리더가 '펼침'으로 읽습니다."),
    ("목록 개수", "<code>&lt;ul&gt;</code>을 쓰면 스크린 리더가 '목록, 항목 12개'처럼 항목 수를 자동으로 읽습니다. <b>무한 스크롤</b>로 항목이 계속 늘어날 때는 <code>aria-setsize</code>로 전체 개수를 알려 주기도 합니다."),
    ("실제로 들어 본다", "맥에서는 <kbd>Cmd</kbd>+<kbd>F5</kbd>를 누르면 VoiceOver가 켜집니다. VoiceOver로 화면을 <b>10분만 써 봐도</b> 코드만 읽어서는 알 수 없던 문제를 많이 발견합니다."),
    ("자동 검사의 한계", "검사 도구는 이름이 없는 요소는 찾아내지만, <b>이름이 틀린 요소</b>는 찾지 못합니다. 그래서 사람이 한 번은 직접 들어 봐야 합니다."),
  ]),
  plat_lede="웹, iOS, 안드로이드 모두 <b>역할, 이름, 상태</b>로 읽는 구조가 같습니다.",
  plats=plats([
    ("웹", "role + aria-*",
     sr(sw(True), '"스위치, 켜짐"', True, "120px"),
     "태그가 역할을 주고, 태그로 부족한 부분은 <code>role</code>과 <code>aria-*</code>로 채웁니다."),
    ("iOS", "VoiceOver",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.accessibilityTraits<br>.accessibilityValue</div>''',
     "역할은 <b>trait</b>, 상태는 <b>value</b>라고 부릅니다. 표준 부품에는 둘 다 기본으로 들어 있습니다."),
    ("안드로이드", "TalkBack",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">semantics {<br>&nbsp;role = Role.Switch<br>}</div>''',
     "<code>semantics</code> 블록에 역할과 상태를 적는데, 구조가 웹과 거의 같습니다."),
  ]),
  plat_note="세 플랫폼의 구조가 같아서 <b>\"이 스위치가 켜졌다고 읽히나요\"</b>라는 질문이 어디서나 같은 뜻으로 통합니다. 다만 <b>읽는 순서와 말투</b>는 스크린 리더마다 다르기 때문에, 한 기기에서 자연스럽게 들리는 문장이 다른 기기에서는 어색할 수 있습니다. 그래서 이름은 <b>짧게, 사실만</b> 적는 편이 안전합니다.",
  siblings=siblings("screenreader"),
  related='''        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="../items/switch.html"><b>스위치</b><em>4부</em></a></li>
        <li><a href="../items/tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>''',
)
