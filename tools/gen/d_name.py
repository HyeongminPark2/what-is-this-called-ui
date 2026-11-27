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
  desc="접근 이름이 무엇이고 어떤 순서로 정해지는지, 자리글이 왜 이름이 아닌지를 보여주는 항목.",
  lede="화면을 못 보는 사람에게 버튼은 <b>이름 하나로만</b> 존재합니다. 이름이 없으면 그냥 '버튼'입니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>각 줄의 오른쪽이 <b>스크린 리더가 읽는 말</b>입니다. 빨간 줄은 이름이 아예 없는 것입니다.<br>
          <b>아이콘만 있는 버튼</b>과 <b>label 없는 입력칸</b>이 가장 흔한 사고입니다 —
          눈으로는 쓰레기통 그림과 자리글이 보이지만, <b>소리로는 아무것도 아닙니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "이름, 접근 이름, 레이블"),
    ("영어", "accessible name, label, labelling"),
    ("같이 쓰는 말",
     "계산된 이름을 <b>접근 이름</b>(accessible name), 덧붙는 설명을 "
     "<b>접근 설명</b>(accessible description · <code>aria-describedby</code>)이라 합니다. "
     "이름을 정하는 규칙은 <b>이름 계산</b>(accname) 이라는 표준으로 정해져 있습니다."),
    ("자주 잘못 부름",
     "<b>자리글</b>(placeholder) — <b>이름이 아닙니다.</b> 입력을 시작하면 사라지고, 기기마다 읽는 방식이 다릅니다.<br>"
     "<b><code>title</code></b> — 마지막 수단입니다. 마우스를 올려야 보이고 터치에서는 안 보입니다.<br>"
     "<b><code>alt</code></b> — 그림 전용입니다. 버튼의 이름은 <code>aria-label</code>로 줍니다."),
  ]),
  axes=ax("이름 붙이기"),
  oneline="이름은 <b>순서대로</b> 정해집니다 — <code>aria-labelledby</code> → <code>aria-label</code> → <code>&lt;label&gt;</code> → 안의 글자 → <code>title</code>.",
  s4_title="갈래", s4_hint="무엇이 이름이 되나",
  states=states([
    (nm('<span style="display:inline-block;padding:7px 13px;border-radius:6px;border:1px solid var(--line-strong);background:var(--surface);font-size:12px">저장</span>', '"저장, 버튼"'),
     "안의 글자", "가장 좋다. <b>보이는 글이 곧 이름</b>"),
    (nm(ICON, '"버튼" — 이름 없음', False), "아이콘만", "<b>이름이 없다.</b> 가장 흔한 사고"),
    (nm(ICON, '"정산 #4821 지우기, 버튼"'), "+ aria-label", "<b>무엇을</b> 지우는지까지 넣는다"),
    (nm('<span style="display:inline-block;border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">계좌번호</span>', '"편집" — 이름 없음', False),
     "자리글만", "<b>자리글은 이름이 아니다.</b> 입력하면 사라진다"),
    (nm('<span style="display:grid;gap:3px"><span style="font-size:10px;color:var(--fg-muted)">계좌번호</span>'
        '<span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">- 없이</span></span>',
        '"계좌번호, 편집"'), "+ label", "<b>label 이 이름</b>이 된다. 눌러서 포커스도 간다"),
    (nm('<span style="font-size:12px;color:var(--accent);text-decoration:underline">더 보기</span>', '"더 보기, 링크" ×10', False),
     "같은 이름 여럿", "링크 목록이 <b>'더 보기' 열 개</b>가 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이름이 필요한 것", "button · link · input", "<b>누를 수 있는 모든 것</b>과 입력칸"),
    ("직접 적기", "aria-label", "보이는 글이 없을 때. <b>무엇을</b>까지 넣는다"),
    ("입력칸의 이름", "&lt;label for&gt;", "<b>눌러서 포커스도 간다</b> — aria-label 보다 낫다"),
    ("이미 있는 글 가리키기", "aria-labelledby", "제목이 이미 있으면 그걸 가리킨다. <b>가장 우선</b>한다"),
    ("자리글", "placeholder", "<b>이름이 아니다.</b> 입력하면 사라진다"),
    ("아이콘 숨기기", "aria-hidden=\"true\"", "장식 아이콘은 이름 계산에서 뺀다 — 안 빼면 '쓰레기통 버튼'이 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이름은 <b>위에서부터 하나만</b> 쓰입니다. <code>aria-label</code>을 주면 안의 글자는
          <b>통째로 무시됩니다</b> — 그래서 <code>&lt;button aria-label="삭제"&gt;저장&lt;/button&gt;</code> 같은 실수가
          눈에 안 띄게 숨습니다. 보이는 글과 읽히는 이름이 다르면
          <b>음성으로 조작하는 사람</b>이 "저장 눌러"라고 말해도 안 눌립니다.</p>''',
  do=ul([
    "<b>아이콘만 있는 버튼</b> — 거의 늘 빠뜨리는 자리",
    "같은 글자가 여럿인 링크 — '더 보기'에 <b>무엇을</b> 더 보는지 붙입니다",
    "모든 입력칸에 <code>&lt;label&gt;</code>",
    "묶음에 이름 붙이기 — <code>role=\"group\"</code> + <code>aria-label</code>",
  ]),
  dont=ul([
    "<b>자리글로 label 을 대신</b>하는 것",
    "보이는 글과 <b>다른 이름</b>을 붙이는 것 — 음성 조작이 안 됩니다",
    "<code>title</code>에만 의지하는 것 — 터치에서는 안 보입니다",
    "<b>'버튼'·'링크'를 이름에 넣는 것</b> — 역할은 따로 읽히므로 '저장 버튼 버튼'이 됩니다",
  ]),
  instead='역할·상태까지 보려면 <a href="screenreader.html">스크린 리더가 읽는 것</a>, 태그 고르기는 <a href="semantics.html">시맨틱 태그</a>, 저절로 바뀐 것은 <a href="live.html">라이브 리전</a>.',
  cases=cases([
    (nm(ICON, '"정산 #4821 지우기, 버튼"', True, "190px"), "아이콘 버튼", "<b>무엇을</b> 지우는지까지. 목록에서는 특히 중요하다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:3px">
                <span style="font-size:10.5px;color:var(--fg-muted)">계좌번호</span>
                <span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px;color:var(--fg-faint)">- 없이 입력</span>
                <span style="font-size:9.5px;color:var(--fg-faint)">숫자만 입력하세요</span>
              </div>''',
     "입력칸", "<b>label 은 이름</b>, 도움말은 <code>aria-describedby</code> 로 따로"),
    ('''              <div style="width:100%;max-width:190px;display:flex;gap:5px;flex-wrap:wrap">
                <span style="border:1px solid var(--line-strong);border-radius:99px;padding:3px 9px;font-size:10.5px">전체</span>
                <span style="background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent);border-radius:99px;padding:3px 9px;font-size:10.5px;font-weight:700">검토 중</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);margin-top:6px;text-align:center">role="group" aria-label="상태로 거르기"</div>''',
     "묶음", "칩 하나하나뿐 아니라 <b>묶음에도</b> 이름이 필요하다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이름이 정해지는 순서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="순서를 알면 디버깅이 쉬워집니다 — <b>위의 것이 있으면 아래는 무시</b>됩니다.",
  code='''<span class="c">&lt;!-- 1. aria-labelledby — 이미 있는 글을 가리킨다 --&gt;</span>
&lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;정산 요청 #4821&lt;/<span class="t">h2</span>&gt;
&lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;…&lt;/<span class="t">section</span>&gt;

<span class="c">&lt;!-- 2. aria-label — 보이는 글이 없을 때 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 #4821 지우기"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 3. label — 입력칸은 이게 가장 좋다 --&gt;</span>
&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"acc"</span>&gt;계좌번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"acc"</span> <span class="a">aria-describedby</span>=<span class="s">"hint"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"hint"</span>&gt;숫자만 입력하세요&lt;/<span class="t">p</span>&gt;   <span class="c">&lt;!-- 설명은 따로 --&gt;</span>''',
  keys=kbd([
    ("순서를 안다", "labelledby → label(aria) → <code>&lt;label&gt;</code> → 안의 글자 → title"),
    ("입력칸은 <code>&lt;label&gt;</code>", "눌러서 포커스가 가는 이점까지 있다"),
    ("아이콘은 숨긴다", "<code>aria-hidden=\"true\"</code>. 안 숨기면 그림 이름이 섞인다"),
    ("보이는 글과 맞춘다", "다르면 <b>음성 조작이 안 된다</b>"),
    ("역할은 안 적는다", "'저장 버튼'이라고 쓰면 '저장 버튼 버튼'으로 읽힌다"),
    ("설명은 <code>describedby</code>", "이름은 짧게, 긴 도움말은 설명으로 따로"),
  ]),
  backend=rows([
    ("이름에 데이터를 넣는다", "'지우기'보다 <b>'정산 #4821 지우기'</b>가 낫습니다. 목록에서 같은 버튼이 열 개일 때 구별이 됩니다 — 서버가 주는 ID 를 이름에 끼워 넣습니다."),
    ("다국어", "<code>aria-label</code>도 <b>번역 대상</b>입니다. 코드에 한국어를 박아 두면 번역에서 빠집니다."),
    ("자동 검사", "<code>axe-core</code> 같은 도구가 '이름 없는 버튼'을 바로 잡아 줍니다. <b>CI 에 넣기 가장 쉬운 접근성 검사</b>입니다."),
    ("접근성 트리", "개발자 도구의 Accessibility 패널에서 <b>계산된 이름</b>을 볼 수 있습니다. 추측하지 말고 보면 됩니다."),
  ]),
  plat_lede="이름을 붙이는 일은 세 플랫폼이 거의 같습니다.",
  plats=plats([
    ("웹", "aria-label · label",
     nm(ICON, '"지우기, 버튼"', True, "120px"),
     "속성으로 붙입니다. <b>순서</b>가 정해져 있어 위의 것이 아래를 덮습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.accessibilityLabel( )<br>.accessibilityHint( )</div>''',
     "<b>Label</b> 과 <b>Hint</b> 로 나뉩니다. 웹의 이름·설명과 거의 1대1입니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">contentDescription<br>semantics { }</div>''',
     "<b>contentDescription</b> 하나로 붙입니다. 장식은 <code>null</code> 로 두어 뺍니다."),
  ]),
  plat_note="세 쪽 다 <b>이름·설명 두 층</b>이 있고 쓰임이 같습니다. 그래서 \"아이콘 버튼에 이름 붙여 주세요\"가 그대로 통합니다 — 접근성 항목 중 소통이 가장 쉬운 축입니다.",
  siblings=siblings("name"),
  related='''        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/avatar.html"><b>아바타</b><em>5부</em></a></li>''',
)
