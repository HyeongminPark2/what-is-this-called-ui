# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def nm(visual, said, ok=True, w="168px"):
    color = "#1f8a4c" if ok else "var(--danger)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:7px;justify-items:center">'
            + visual +
            '<span style="font-family:var(--mono);font-size:10px;color:' + color + ';font-weight:700;text-align:center">' + said + '</span></div>')

ICON = ('<span style="display:grid;place-items:center;width:34px;height:34px;border-radius:6px;'
        'border:1px solid var(--line-strong);background:var(--surface);font-size:14px">🗑</span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:inline-grid;place-items:center;width:38px;height:38px;border-radius:7px;border:1px solid var(--line-strong);background:var(--surface);font-size:16px;justify-self:start">🗑</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">aria-label="정산 #4821 지우기"</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;label for&gt;   — 입력칸의 이름</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-labelledby   — 이미 있는 글을 가리킨다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">placeholder   — 이름이 아니다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-hidden="true"   — 아이콘은 이름에서 뺀다</div>
                </div>
              </div>'''

D = dict(
  slug="name", ko="이름 붙이기", en="Accessible name",
  desc="접근 이름이 무엇이고 어떤 순서로 정해지는지, 자리글은 왜 이름이 될 수 없는지 보여 주는 항목입니다.",
  lede="화면을 보지 못하는 사람은 버튼을 <b>이름으로만</b> 구별합니다. 버튼에 이름이 없으면 스크린 리더는 그냥 '버튼'이라고만 읽습니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>각 줄의 오른쪽에 적힌 것이 <b>스크린 리더가 읽는 말</b>입니다. 빨간 줄은 이름이 아예 없는 요소입니다.<br>
          그중 <b>아이콘만 있는 버튼</b>과 <b>label 없는 입력칸</b>이 가장 흔한 사고입니다.
          눈으로 보면 쓰레기통 그림과 자리글이 있지만, 스크린 리더는 <b>그 요소가 무엇인지 읽어 주지 못합니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "이름, 접근 이름, 레이블"),
    ("영어", "accessible name, label, labelling"),
    ("같이 쓰는 말",
     "브라우저가 계산해 낸 요소의 이름은 <b>접근 이름</b>(accessible name), 이름 뒤에 덧붙는 설명은 "
     "<b>접근 설명</b>(accessible description · <code>aria-describedby</code>)이라고 합니다. "
     "이름을 정하는 규칙은 <b>이름 계산</b>(accname)이라는 표준에 정해져 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>자리글</b>(placeholder) — 자리글은 <b>이름이 아닙니다.</b> 입력을 시작하면 사라지고, 스크린 리더마다 읽는 방식도 다릅니다.<br>"
     "<b><code>title</code></b> — 다른 방법이 없을 때 마지막으로 쓰는 수단입니다. 마우스를 올려야 보이고 터치 화면에서는 보이지 않습니다.<br>"
     "<b><code>alt</code></b> — 그림에만 쓰는 속성입니다. 버튼의 이름은 <code>aria-label</code>로 줍니다."),
  ]),
  axes=ax("이름 붙이기"),
  oneline="이름은 정해진 <b>순서대로</b> 찾습니다. <code>aria-labelledby</code>를 먼저 보고, 없으면 <code>aria-label</code>, <code>&lt;label&gt;</code>, 요소 안의 글자, <code>title</code> 순서로 내려가며 처음 찾은 것을 이름으로 씁니다.",
  s4_title="갈래", s4_hint="무엇이 이름이 되나",
  states=states([
    (nm('<span style="display:inline-block;padding:7px 13px;border-radius:6px;border:1px solid var(--line-strong);background:var(--surface);font-size:12px">저장</span>', '"저장, 버튼"'),
     "안의 글자", "가장 좋은 방법입니다. <b>화면에 보이는 글이 그대로 이름</b>이 됩니다"),
    (nm(ICON, '"버튼" — 이름 없음', False), "아이콘만", "<b>이름이 없습니다.</b> 가장 흔한 사고입니다"),
    (nm(ICON, '"정산 #4821 지우기, 버튼"'), "+ aria-label", "이름에 <b>무엇을</b> 지우는지까지 넣습니다"),
    (nm('<span style="display:inline-block;border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">계좌번호</span>', '"편집" — 이름 없음', False),
     "자리글만", "<b>자리글은 이름이 될 수 없습니다.</b> 입력을 시작하면 사라지기 때문입니다"),
    (nm('<span style="display:grid;gap:3px"><span style="font-size:10px;color:var(--fg-muted)">계좌번호</span>'
        '<span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">- 없이</span></span>',
        '"계좌번호, 편집"'), "+ label", "<b>label이 이름</b>이 됩니다. label을 누르면 입력칸으로 포커스도 옮겨 갑니다"),
    (nm('<span style="font-size:12px;color:var(--accent);text-decoration:underline">더 보기</span>', '"더 보기, 링크" ×10', False),
     "같은 이름 여럿", "스크린 리더의 링크 목록에 <b>'더 보기'가 열 개</b> 나열되어 서로 구별할 수 없습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이름이 필요한 것", "button · link · input", "<b>누를 수 있는 모든 요소</b>와 입력칸에는 이름이 있어야 합니다"),
    ("직접 적기", "aria-label", "화면에 보이는 글이 없을 때 씁니다. 이름에 <b>무엇을</b> 하는지까지 넣습니다"),
    ("입력칸의 이름", "&lt;label for&gt;", "<b>label을 누르면 입력칸으로 포커스도 옮겨 가기</b> 때문에 aria-label보다 낫습니다"),
    ("이미 있는 글 가리키기", "aria-labelledby", "화면에 제목이 이미 있으면 그 제목을 가리켜 이름으로 씁니다. 이름을 정할 때 <b>가장 먼저</b> 봅니다"),
    ("자리글", "placeholder", "자리글은 <b>이름이 아닙니다.</b> 입력을 시작하면 사라집니다"),
    ("아이콘 숨기기", "aria-hidden=\"true\"", "장식용 아이콘은 이름 계산에서 뺍니다. 빼지 않으면 아이콘 이름이 섞여 '쓰레기통 버튼'처럼 읽힙니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이름은 위의 순서에서 <b>처음 찾은 하나만</b> 쓰입니다. 예를 들어 <code>aria-label</code>을 주면 버튼 안의 글자는
          <b>전부 무시됩니다</b>. 그래서 <code>&lt;button aria-label="삭제"&gt;저장&lt;/button&gt;</code> 같은 실수는
          화면만 봐서는 눈에 띄지 않습니다. 이렇게 보이는 글과 읽히는 이름이 다르면
          <b>음성으로 화면을 조작하는 사람</b>이 "저장 눌러"라고 말해도 버튼이 눌리지 않습니다.</p>''',
  do=ul([
    "<b>아이콘만 있는 버튼</b>을 만들 때. 이름을 가장 자주 빠뜨리는 자리입니다",
    "같은 글자의 링크가 여러 개일 때. '더 보기'에 <b>무엇을</b> 더 보는지 붙입니다",
    "입력칸을 만들 때. 모든 입력칸에 <code>&lt;label&gt;</code>을 붙입니다",
    "요소 여러 개를 한 묶음으로 보여 줄 때. <code>role=\"group\"</code>과 <code>aria-label</code>로 묶음에도 이름을 붙입니다",
  ]),
  dont=ul([
    "<b>label 대신 자리글</b>만 둘 때",
    "화면에 보이는 글과 <b>다른 이름</b>을 붙일 때. 음성으로 조작할 수 없게 됩니다",
    "이름을 <code>title</code>에만 맡길 때. 터치 화면에서는 보이지 않습니다",
    "<b>'버튼'이나 '링크'라는 말을 이름에 넣을</b> 때. 역할은 스크린 리더가 따로 읽기 때문에 '저장 버튼 버튼'처럼 겹쳐 읽힙니다",
  ]),
  instead='역할·상태까지 보려면 <a href="screenreader.html">스크린 리더가 읽는 것</a>, 태그 고르기는 <a href="semantics.html">시맨틱 태그</a>, 저절로 바뀐 것은 <a href="live.html">라이브 리전</a>.',
  cases=cases([
    (nm(ICON, '"정산 #4821 지우기, 버튼"', True, "190px"), "아이콘 버튼", "이름에 <b>무엇을</b> 지우는지까지 넣습니다. 같은 버튼이 줄마다 있는 목록에서는 특히 중요합니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:3px">
                <span style="font-size:10.5px;color:var(--fg-muted)">계좌번호</span>
                <span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">- 없이 입력</span>
                <span style="font-size:9.5px;color:var(--fg-faint)">숫자만 입력하세요</span>
              </div>''',
     "입력칸", "<b>label은 이름</b>이 되고, 도움말은 <code>aria-describedby</code>로 따로 연결해 설명이 되게 합니다"),
    ('''              <div style="width:100%;max-width:190px;display:flex;gap:5px;flex-wrap:wrap">
                <span style="border:1px solid var(--line-strong);border-radius:99px;padding:3px 9px;font-size:10.5px">전체</span>
                <span style="background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent);border-radius:99px;padding:3px 9px;font-size:10.5px;font-weight:700">검토 중</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);margin-top:6px;text-align:center">role="group" aria-label="상태로 거르기"</div>''',
     "묶음", "칩 하나하나뿐 아니라 칩을 모은 <b>묶음에도</b> 이름이 필요합니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이름이 정해지는 순서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="이름이 정해지는 순서를 알면 디버깅이 쉬워집니다. <b>순서상 위의 것이 있으면 아래의 것은 무시</b>되기 때문입니다.",
  code='''<span class="c">&lt;!-- 1. aria-labelledby는 이미 있는 글을 가리킨다 --&gt;</span>
&lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;정산 요청 #4821&lt;/<span class="t">h2</span>&gt;
&lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;…&lt;/<span class="t">section</span>&gt;

<span class="c">&lt;!-- 2. aria-label은 보이는 글이 없을 때 쓴다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 #4821 지우기"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 3. 입력칸에는 label이 가장 좋다 --&gt;</span>
&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"acc"</span>&gt;계좌번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"acc"</span> <span class="a">aria-describedby</span>=<span class="s">"hint"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"hint"</span>&gt;숫자만 입력하세요&lt;/<span class="t">p</span>&gt;   <span class="c">&lt;!-- 설명은 따로 --&gt;</span>''',
  keys=kbd([
    ("순서를 안다", "labelledby, label(aria), <code>&lt;label&gt;</code>, 안의 글자, title 순서로 찾습니다"),
    ("입력칸은 <code>&lt;label&gt;</code>", "label을 누르면 입력칸으로 포커스가 옮겨 가는 이점까지 있습니다"),
    ("아이콘은 숨긴다", "<code>aria-hidden=\"true\"</code>로 숨깁니다. 숨기지 않으면 아이콘 그림의 이름이 버튼 이름에 섞입니다"),
    ("보이는 글과 맞춘다", "보이는 글과 이름이 다르면 <b>음성으로 조작할 수 없습니다</b>"),
    ("역할은 안 적는다", "이름을 '저장 버튼'이라고 쓰면 '저장 버튼 버튼'으로 읽힙니다"),
    ("설명은 <code>describedby</code>", "이름은 짧게 두고, 긴 도움말은 설명으로 따로 연결합니다"),
  ]),
  backend=rows([
    ("이름에 데이터를 넣는다", "'지우기'보다 <b>'정산 #4821 지우기'</b>가 낫습니다. 목록에 같은 버튼이 열 개 있어도 서로 구별할 수 있기 때문입니다. 이름에는 서버가 내려주는 ID를 끼워 넣습니다."),
    ("다국어", "<code>aria-label</code>도 <b>번역 대상</b>입니다. 코드에 한국어 문구를 직접 적어 두면 번역할 때 빠지기 쉽습니다."),
    ("자동 검사", "<code>axe-core</code> 같은 도구를 돌리면 '이름 없는 버튼'을 바로 찾아 줍니다. 접근성 검사 가운데 <b>CI에 넣기 가장 쉬운 검사</b>입니다."),
    ("접근성 트리", "개발자 도구의 Accessibility 패널을 열면 브라우저가 <b>계산한 이름</b>을 직접 볼 수 있으니, 이름이 무엇으로 정해졌는지 추측할 필요가 없습니다."),
  ]),
  plat_lede="이름을 붙이는 방식은 웹, iOS, 안드로이드가 거의 같습니다.",
  plats=plats([
    ("웹", "aria-label · label",
     nm(ICON, '"지우기, 버튼"', True, "120px"),
     "속성으로 이름을 붙입니다. 이름을 찾는 <b>순서</b>가 정해져 있어서, 순서상 위의 것이 있으면 아래의 것은 쓰이지 않습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.accessibilityLabel( )<br>.accessibilityHint( )</div>''',
     "<b>Label</b>과 <b>Hint</b>로 나뉘는데, 웹의 이름과 설명에 거의 1대1로 대응합니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">contentDescription<br>semantics { }</div>''',
     "<b>contentDescription</b> 하나로 이름을 붙입니다. 장식용 그림은 <code>null</code>로 두어 이름에서 뺍니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>이름과 설명</b>을 따로 두고 같은 용도로 씁니다. 그래서 \"아이콘 버튼에 이름 붙여 주세요\"라는 요청이 웹 개발자와 앱 개발자에게 같은 뜻으로 전달되고, 접근성 항목 가운데 소통하기가 가장 쉽습니다.",
  siblings=siblings("name"),
  related='''        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/avatar.html"><b>아바타</b><em>5부</em></a></li>''',
)
