# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def chip(t, on=False):
    return ('<span style="display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:999px;font-size:9.5px;'
            + ('background:var(--accent);color:#fff' if on else 'background:var(--bg);border:1px solid var(--line);color:var(--fg-muted)')
            + '">' + t + '</span>')

def facet(items, w="150px"):
    body = ''.join(
      '<label style="display:flex;align-items:center;gap:5px;font-size:10px;padding:2px 0">'
      '<span style="width:9px;height:9px;border:1px solid var(--line);border-radius:2px;'
      + ('background:var(--accent);border-color:var(--accent)' if on else '') + '"></span>'
      '<span style="flex:1;min-width:0">' + n + '</span>'
      '<span style="color:var(--fg-muted);font-variant-numeric:tabular-nums">' + c + '</span></label>'
      for n, c, on in items)
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);padding:7px 8px;display:grid;gap:1px">'
            '<span style="font-size:9px;font-weight:700;color:var(--fg-muted);margin-bottom:2px">상태</span>' + body + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="display:flex;gap:5px;flex-wrap:wrap">''' + chip('승인됨 ✕', True) + chip('11월 ✕', True) + '''<span style="font-size:9.5px;color:var(--accent);align-self:center">모두 지우기</span></div>
                  <div class="pin-out" data-pin="2" style="max-width:190px">''' + facet([("승인됨", "128", True), ("대기", "14", False), ("반려", "0", False)], "190px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">같은 묶음 안은 OR로, 승인됨 <b>또는</b> 대기</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">묶음끼리는 AND로, 상태 <b>그리고</b> 기간</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">반려는 0건이라 눌러도 결과가 없음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">?status=approved&amp;month=11</div>
                </div>
              </div>'''

D = dict(
  slug="filter", ko="필터와 패싯", en="Filter / Facet",
  desc="조건으로 목록을 거르는 화면을 묶음 안의 OR와 묶음 사이의 AND, 조건별 개수, 주소에 담기까지 다루는 항목입니다.",
  lede="필터는 목록을 <b>조건으로 걸러</b> 원하는 건만 남기는 장치입니다. 지금 고른 조건이 화면에 보이고 그 조건을 <b>바로 지울 수 있어야</b> 필터로서 제 역할을 합니다.",
  axes_lede="데이터를 다루는 화면을 설계할 때는 '건수가 늘면 어떻게 되나'부터 따져야 합니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>조건을 여럿 골라 보세요. <b>같은 묶음 안은 OR</b>, <b>묶음끼리는 AND</b>로 걸립니다.
          이 규칙을 어기고 같은 묶음 안을 AND로 걸면 '승인됨과 대기를 둘 다 골랐는데 0건'이 나옵니다.<br>
          <b>개수 보이기</b>를 끄면 어떤 조건이 0건인지 미리 알 수 없어서 눌러 본 뒤에야 알게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "필터, 거름, 조건 검색, 패싯 검색"),
    ("영어", "filter, facet, faceted search, refinement"),
    ("같이 쓰는 말",
     "상태·기간·지역처럼 성격이 다른 조건 묶음 하나하나를 <b>패싯</b>(facet)이라고 부릅니다. "
     "고른 조건을 둥근 알약 모양으로 보여 주는 것은 <b>칩</b>(chip)·<b>토큰</b>·<b>필터 태그</b>라고 하고, "
     "조건마다 붙는 결과 개수는 <b>패싯 카운트</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>검색</b> — <a href=\"search.html\">검색</a>은 사용자가 글자를 자유롭게 입력하는 방식이고, 필터는 <b>정해진 값 가운데서 고르는</b> 방식입니다.<br>"
     "<b>정렬</b> — 정렬은 순서만 바꾸기 때문에 <b>건수가 줄지 않지만</b>, 필터는 조건에 맞지 않는 건을 빼서 건수가 줄어듭니다.<br>"
     "<b>탭</b> — <a href=\"../items/tabs.html\">탭</a>도 목록을 거르는 것처럼 보이지만 <b>하나만</b> 고를 수 있고, 탭끼리 보여 주는 내용이 보통 겹치지 않습니다."),
  ]),
  axes=ax("필터와 패싯"),
  oneline="필터에서 가장 중요한 일은 <b>지금 어떤 조건이 걸려 있는지 보여 주는 것</b>입니다. 결과만 바뀌고 조건이 보이지 않으면 사용자는 목록이 왜 줄었는지, 어떻게 되돌리는지 알 수 없습니다.",
  s4_title="상태", s4_hint="고른 조건이 보여야 합니다",
  states=states([
    (facet([("승인됨", "128", False), ("대기", "14", False), ("반려", "3", False)]),
     "아무것도 안 골랐을 때", "전체 목록이 보입니다. 조건 옆 개수는 <b>지금 결과를 기준으로</b> 셉니다"),
    (facet([("승인됨", "128", True), ("대기", "14", False), ("반려", "3", False)]),
     "조건을 하나 골랐을 때", "결과가 줄어들고, 고른 조건이 <b>칩</b>으로 나타납니다"),
    (facet([("승인됨", "128", True), ("대기", "14", True), ("반려", "3", False)]),
     "같은 묶음에서 둘을 골랐을 때", "<b>OR</b>로 걸려서 두 조건의 결과가 모두 보입니다. AND로 걸면 0건이 됩니다"),
    (facet([("승인됨", "128", False), ("대기", "0", False), ("반려", "0", False)]),
     "결과가 0건인 조건", "<b>흐리게</b> 표시하거나 숨깁니다. 눌렀을 때 빈 화면이 나오는 조건을 눌러 보게 두지 않습니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="display:flex;gap:4px;flex-wrap:wrap">''' + chip('승인됨 ✕', True) + chip('11월 ✕', True) + '''</div>
                <span style="font-size:9.5px;color:var(--accent)">모두 지우기</span>
              </div>''',
     "고른 조건을 칩으로 모아 보일 때", "조건 목록이 접혀 있어도 <b>어떤 조건이 걸렸는지</b> 보입니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px dashed var(--line);border-radius:6px;padding:12px 8px;text-align:center">
                <span style="font-size:10px;color:var(--fg-muted);display:block">조건에 맞는 것이 없습니다</span>
                <span style="font-size:9.5px;color:var(--accent)">조건 지우기</span>
              </div>''',
     "거른 결과가 0건일 때", "결과가 없다고만 하지 말고 <b>어느 조건을 풀면 결과가 나오는지</b>까지 알려 주면 더 좋습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("고른 조건 칩", "chip", "지금 어떤 조건이 걸렸는지 보여 줍니다. <b>✕를 눌러 하나씩</b> 풀 수 있어야 합니다"),
    ("패싯 묶음", "fieldset", "성격이 같은 조건들을 한데 묶고, <code>&lt;legend&gt;</code>로 묶음 이름을 붙입니다"),
    ("묶음 안은 OR", "같은 축", "둘을 고르면 <b>둘 다</b> 보입니다. 사용자도 대개 이렇게 동작하리라고 기대합니다"),
    ("묶음끼리는 AND", "다른 축", "상태 <b>그리고</b> 기간처럼 걸리므로 조건을 더할수록 결과가 줄어듭니다"),
    ("0건 조건", "disabled", "결과가 0건인 조건은 비활성으로 두어 눌러서 빈 화면을 보는 일이 없게 합니다"),
    ("주소", "query string", "조건을 <b>주소에 담아</b> 두어야 공유하거나 뒤로 가도 같은 결과가 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>OR/AND 규칙은 따로 설명하지 않아도 사용자가 예상한 대로 동작해야 합니다.</b>
          같은 묶음 안을 AND로 걸면 '승인됨과 대기를 둘 다 골랐는데 0건'이 나오는데,
          사용자는 이것을 버그로 여깁니다. 그래서 거의 모든 쇼핑몰이
          <b>묶음 안은 OR, 묶음 사이는 AND</b>로 통일했고, 사용자가 이미 익힌 이 규칙을 따르는 편이 낫습니다.</p>''',
  do=ul([
    "상태, 분류, 기간처럼 고를 값이 <b>정해져 있을</b> 때",
    "조건을 <b>여럿 겹쳐</b> 걸어야 할 때",
    "건수가 많아 <b>좁혀 들어가야</b> 할 때",
  ]),
  dont=ul([
    "사용자가 값을 자유롭게 입력해야 할 때. <a href=\"search.html\">검색</a>이 맞습니다",
    "조건이 <b>하나뿐</b>일 때. <a href=\"../items/tabs.html\">탭</a>이나 <a href=\"../items/select.html\">셀렉트</a>로 충분합니다",
    "고른 조건을 <b>보여 주지 않을</b> 때. 필터에서 가장 흔하게 생기는 문제입니다",
    "조건을 누를 때마다 서버에 요청을 보낼 때. 여러 번 누른 것을 <b>묶어서</b> 보내거나 '적용' 버튼을 둡니다",
  ]),
  instead='사용자가 글자를 자유롭게 입력해야 하면 <a href="search.html">검색</a>을 쓰고, 값을 하나만 고르면 되는 경우에는 <a href="../items/tabs.html">탭</a>이 맞습니다. 조건이 많고 복잡하면 <a href="../items/drawer.html">드로어</a>에 담아 필요할 때 엽니다.',
  cases=cases([
    (facet([("승인됨", "128", True), ("대기", "14", False), ("반려", "3", False)]),
     "왼쪽에 조건 목록을 펼쳐 두기", "PC에서 가장 흔한 배치로, 조건 목록이 늘 펼쳐져 있습니다"),
    ('''              <div style="width:100%;max-width:170px;display:flex;gap:4px;flex-wrap:wrap">''' + chip('상태 ▾') + chip('기간 ▾') + chip('지역 ▾') + '''</div>''',
     "조건을 가로 드롭다운으로 늘어놓기", "조건이 적을 때 씁니다. 드롭다운을 <b>열어 조건을 고르면 닫힙니다</b>"),
    ('''              <div class="phone" role="img" aria-label="폰 필터 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:28px;display:flex;gap:3px"><span style="font-size:6px;background:var(--accent);color:#fff;padding:2px 5px;border-radius:999px">승인됨</span><span style="font-size:6px;border:1px solid var(--line);padding:2px 5px;border-radius:999px">기간</span></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-top:1px solid var(--line);border-radius:8px 8px 0 0;padding:6px"><div style="width:22px;height:2px;background:var(--line);border-radius:2px;margin:0 auto 5px"></div><div style="font-size:6px">상태 · 기간 · 지역</div></div>
              </div></div>''',
     "폰에서 시트를 열어 조건 고르기", "<a href=\"../items/drawer.html\">바텀 시트</a>를 열어 조건을 고른 뒤 <b>'적용'</b>을 눌러 닫습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="필터를 만들 때 꼭 갖출 것",
  code_lede="조건 묶음은 <code>&lt;fieldset&gt;</code>으로 묶고, 결과 개수는 <code>aria-live</code>로 알립니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;상태&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">name</span>=<span class="s">"status"</span> <span class="a">value</span>=<span class="s">"approved"</span>&gt;
    승인됨 &lt;<span class="t">span</span>&gt;128&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">name</span>=<span class="s">"status"</span> <span class="a">value</span>=<span class="s">"rejected"</span> <span class="a">disabled</span>&gt;
    반려 &lt;<span class="t">span</span>&gt;0&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;128건&lt;/<span class="t">p</span>&gt;   <span class="c">&lt;!-- 결과가 바뀌면 읽어 준다 --&gt;</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "조건 하나하나로 옮겨 갑니다. 체크박스는 <kbd>Space</kbd>로 켭니다"),
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "스크린 리더가 '상태 묶음, 승인됨 체크박스'처럼 읽습니다. 묶음 이름이 없으면 무엇에 대한 조건인지 알 수 없습니다"),
    ("<code>role=\"status\"</code>", "'128건'처럼 결과 개수가 바뀐 것을 <b>하던 일을 끊지 않고</b> 알립니다. <code>alert</code>는 읽던 내용을 끊고 바로 읽어서 이 용도에는 지나칩니다"),
    ("0건인 조건은 <code>disabled</code>로 두기", "눌러도 결과가 없는 조건은 탭 순서에서 빠지는 편이 낫습니다"),
    ("칩의 ✕ 버튼에 이름 붙이기", "<code>&lt;button aria-label=\"승인됨 조건 지우기\"&gt;</code>처럼 이름을 붙입니다. ✕만 있으면 무엇을 지우는 버튼인지 알 수 없습니다"),
    ("조건이 바뀔 때 주소를 고치는 방법", "<code>history.replaceState</code>로 바꿉니다. 조건을 바꿀 때마다 방문 기록을 쌓으면 뒤로가기를 조건 수만큼 눌러야 필터 화면을 벗어날 수 있습니다"),
  ]),
  backend=rows([
    ("조건별 개수는 한 번에 받기", "조건마다 <code>COUNT</code>를 따로 보내면 조건이 열 개일 때 요청도 열 번 갑니다. 그래서 한 번의 <b>집계 질의</b>(facet aggregation)로 모든 개수를 함께 받아 옵니다."),
    ("개수를 세는 기준", "'승인됨 128'은 <b>다른 조건을 적용한 뒤</b>에 센 숫자여야 합니다. 전체 데이터를 기준으로 세면 그 조건을 눌렀을 때 나오는 건수와 숫자가 맞지 않습니다."),
    ("같은 묶음의 조건은 빼고 세기", "상태 묶음의 개수를 셀 때는 <b>상태 조건만 빼고</b> 나머지 조건을 적용해 셉니다. 상태 조건까지 넣고 세면 이미 고른 값 말고는 모두 0건으로 나옵니다."),
    ("조건 값은 허용 목록으로 받기", "<code>?status=</code> 값을 그대로 질의에 넘기면 주입 공격을 당할 수 있습니다. 미리 정해 둔 값만 받습니다."),
    ("자주 거르는 열의 색인", "자주 거르는 열에 색인이 없으면 조건을 더할수록 질의가 느려집니다. 패싯이 많다면 데이터베이스 대신 <b>검색 엔진</b>(Elasticsearch 등)으로 옮기는 편이 낫습니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>폰에서는 화면을 덮는 시트를 띄워</b> 조건을 고르게 합니다.",
  plats=plats([
    ("웹", "체크박스 묶음",
     facet([("승인됨", "128", True), ("대기", "14", False)], "120px"),
     "화면 왼쪽에 조건 목록을 늘 펼쳐 두는 것이 기본입니다. 조건을 <b>주소에 담을</b> 수 있는 것도 웹만의 특징입니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 필터 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:50%;background:var(--surface);border-top:1px solid var(--line);border-radius:8px 8px 0 0;padding:6px"><div style="font-size:6px">필터</div></div></div></div>''',
     "필터용 부품이 따로 없어서 <b>시트</b>를 띄우고 그 안에 리스트를 둡니다. 고른 조건은 오른쪽 위 '완료'를 눌러 적용합니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 칩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:30px;display:flex;gap:3px"><span style="font-size:6px;background:var(--accent);color:#fff;padding:2px 5px;border-radius:999px">승인</span><span style="font-size:6px;border:1px solid var(--line);padding:2px 5px;border-radius:999px">대기</span></div></div></div>''',
     "<b>필터 칩</b>(filter chip)이라는 정식 부품이 있습니다. 칩을 켜면 바탕색이 채워지고 ✓ 표시가 붙습니다."),
  ]),
  plat_note="\"필터를 넣어 주세요\"라는 요청에는 보통 <b>패싯 카운트까지</b> 들어 있습니다. 숫자 없이 조건만 늘어놓으면 사용자가 0건인 조건을 눌러 빈 화면을 여러 번 보게 되기 때문입니다. 그런데 이 숫자를 만들려면 서버가 <b>집계 질의</b>를 한 번 더 해야 해서, 일정을 잡을 때 이 작업을 빼먹기 쉽습니다.",
  siblings=siblings("filter"),
  related='''        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>
        <li><a href="../items/chip.html"><b>칩</b><em>5부</em></a></li>
        <li><a href="../items/checkbox.html"><b>체크박스</b><em>4부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
