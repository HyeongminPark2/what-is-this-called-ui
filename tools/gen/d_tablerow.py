# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(cells, label, note="", ok=None, w="152px", pad="5px 6px", sel=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    bg = 'background:var(--accent-soft);' if sel else 'background:var(--surface);'
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;overflow:hidden">'
            + ''.join('<span style="display:grid;grid-template-columns:auto 1fr auto auto;gap:5px;align-items:center;'
                      'padding:' + pad + ';font-size:8px;border-top:1px solid var(--line);' + (bg if i == 0 and sel else 'background:var(--surface);') + '">'
                      + x + '</span>' for i, x in enumerate(cells))
            + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def cell(name, amt, box=True, btn=True):
    return (('<span style="width:8px;height:8px;border:1px solid var(--line);border-radius:2px"></span>' if box else '<span></span>')
            + '<span style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + name + '</span>'
            + '<span style="font-family:var(--mono)">' + amt + '</span>'
            + ('<span style="border:1px solid var(--line);border-radius:3px;padding:0 4px;font-size:7px">영수증</span>' if btn else '<span></span>'))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">고르기 칸에는 줄마다 다른 이름을 붙임</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">주 열은 이 줄이 무엇인지 알려 줌</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">숫자 열은 오른쪽 맞춤과 tabular-nums</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">동작 단추는 줄 끝에 둠</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">행 전체가 링크면 안쪽 단추를 눌러도 행이 눌림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">밀도는 한 화면에 들어가는 줄 수를 정함</div>
                </div>
              </div>'''

D = dict(
  slug="tablerow", ko="테이블 행", en="Table row",
  desc="표의 줄 하나에 들어가는 고르기·주 열·값·동작의 자리와 밀도, 그리고 행 전체를 누를 수 있게 만들 때 생기는 문제를 보여 주는 항목입니다.",
  lede="테이블 행은 표의 줄 하나로, 보통 <b>고르기 · 주 열 · 값 · 동작</b> 네 가지가 들어갑니다. 줄마다 이 네 가지의 자리가 다르면 사용자가 줄을 바꿀 때마다 원하는 값을 다시 찾아야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>밀도를 바꾸면 한 화면에 들어가는 줄 수가 달라지는데, 데모는
          <b>480px 높이에 몇 줄이 들어가는지</b> 재서 적습니다.<br>
          <b>행 전체를 누를 수 있게</b> 하면 누르기는 편하지만, 행 안에 있는 단추를 눌러도
          <b>행 이동이 같이 일어납니다</b>. 데모는 그렇게 함께 일어난 이동 횟수를 셉니다.
          이를 막으려면 안쪽 단추에서 <code>stopPropagation()</code>을 호출해야 합니다.<br>
          고르기 체크박스에는 <b>줄마다 다른 이름</b>을 붙여야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "테이블 행, 표 줄, 레코드 행"),
    ("영어", "table row, record row, data row"),
    ("같이 쓰는 말",
     "그 줄이 무엇에 대한 것인지 알려 주는 열은 <b>주 열</b>(primary column),  "
     "줄 간격이 얼마나 빽빽한지는 <b>밀도</b>(density), 한 줄씩 건너 바탕색을 바꾸는 것은 <b>줄무늬</b>(zebra striping)라고 부릅니다.  "
     "마우스를 올려야 나타나는 단추는 <b>호버 액션</b>이라고 하는데, 터치 화면에서는 보이지 않습니다."),
    ("자주 잘못 부르는 이름",
     "<b>데이터 테이블</b> — <a href=\"table.html\">데이터 테이블</a>은 줄 하나가 아니라 <b>표 전체</b>의 설계를 다룹니다.<br>"
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>열 구분이 없는</b> 한 건입니다.<br>"
     "<b>카드</b> — <a href=\"card.html\">카드</a>는 내용을 <b>상자 하나로</b> 묶고, 테이블 행은 값을 열에 맞춰 <b>한 줄로</b> 늘어놓습니다."),
  ]),
  s4_title="상태와 밀도", s4_hint="상태와 밀도에 따라 달라지는 줄 모습",
  states=states([
    (row([cell("모란상회", "1,284,000")], "기본", "네 자리가 제자리에 있음", True),
     "기본 구성", "고르기, 주 열, 값, 동작이 제자리에 있습니다"),
    (row([cell("모란상회", "1,284,000")], "고른 줄", "", True, "152px", "5px 6px", True),
     "줄을 골랐을 때", "고른 줄은 <b>바탕색이 바뀝니다</b>"),
    (row([cell("모란상회", "1,284,000"), cell("한빛아웃도어 영등…", "842,500")], "빽빽하게", "한 화면에 더 많이 들어감", True, "152px", "2px 6px"),
     "줄을 빽빽하게 둘 때", "한 화면에 많은 줄이 들어가서 <b>훑어보기</b>에 좋습니다"),
    (row([cell("모란상회", "1,284,000")], "넉넉하게", "읽기 편한 대신 줄이 적음", None, "152px", "9px 6px"),
     "줄을 넉넉하게 둘 때", "줄 수는 적지만 <b>한 줄씩 읽을</b> 때 편합니다"),
    (row([cell("한빛아웃도어 영등포타…", "842,500")], "긴 이름", "말줄임으로 줄 높이를 지킴", True),
     "내용이 길 때", "줄 높이를 지키도록 <b>말줄임</b>합니다"),
    (row([cell("모란상회", "1,284,000")], "행 전체 링크", "단추를 눌러도 행 이동이 함께 일어남", False),
     "행 전체를 누를 수 있게 했을 때", "<b>안쪽 단추의 눌림과 겹칩니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("고르기", "줄마다 다른 이름을 붙이는 칸", "이름이 모두 '선택'이면 스크린 리더로 들을 때 <b>줄을 구별할 수 없습니다</b>"),
    ("주 열", "줄이 무엇인지 알려 주는 열", "<b>왼쪽 첫 자리</b>에 둡니다"),
    ("숫자 열", "오른쪽에 맞추는 열", "<code>tabular-nums</code>로 자릿수를 맞춥니다"),
    ("동작", "줄 끝에 두는 단추", "줄마다 늘 <b>같은 자리</b>에 둡니다"),
    ("행 전체 링크", "안쪽 단추와 부딪히는 링크", "안쪽 단추의 눌림을 <b>먼저 막습니다</b>"),
    ("밀도", "한 화면에 들어가는 줄 수", "빽빽할수록 한 화면에 <b>많은 줄이 보입니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>마우스를 올려야 단추가 보이게</b> 만드는 경우가 흔한데,
          터치 화면에는 호버가 없어서 이렇게 만든 <b>단추는 끝내 보이지 않습니다</b>.
          단추를 늘 보이게 두거나, 적어도 좁은 화면에서는 보이게 바꿔야 합니다.<br>
          행 전체를 링크로 만들 때는 행 <b>안에 누를 것이 몇 개 있는지</b> 먼저 세어 보세요.
          체크박스 하나와 단추 하나만 있어도
          둘 다 <code>stopPropagation()</code>을 호출해야 합니다.
          그렇게 하기가 번거로우면 <b>주 열만 링크</b>로 두는 쪽이 오류가 적습니다.</p>''',
  do_title="테이블 행을 만들 때 지킬 것", dont_title="테이블 행을 만들 때 피할 것",
  instead_title="테이블 행 대신 쓸 부품과 함께 볼 항목",
  do=ul([
    "고르기 체크박스에 <b>줄마다 다른 이름</b> 주기",
    "숫자는 <b>오른쪽 맞춤과 <code>tabular-nums</code></b>로 맞추기",
    "행 전체를 누르게 하려면 <b>안쪽 단추를 먼저</b> 막기",
  ]),
  dont=ul([
    "단추를 <b>호버할 때만</b> 보이게 하기. 터치 화면에서는 보이지 않습니다",
    "줄마다 동작 단추의 <b>자리를 다르게</b> 두기",
    "긴 이름을 <b>줄바꿈</b>해서 여러 줄로 늘어뜨리기. 줄 높이가 들쭉날쭉해집니다",
    "고르기 이름을 전부 <b>'선택'</b>으로 두기",
  ]),
  instead='표 전체를 어떻게 설계할지는 <a href="table.html">데이터 테이블</a>에서, 여러 줄을 한꺼번에 고르는 방법은 <a href="bulk.html">일괄 선택</a>에서 다룹니다. 열 구분이 없는 한 건이면 <a href="listitem.html">리스트 아이템</a>을 쓰고, 내용을 상자 하나로 묶어 따로 세우려면 <a href="card.html">카드</a>를 씁니다.',
  cases=cases([
    (row([cell("모란상회", "1,284,000")], "정산 목록", "", True), "정산 내역을 줄로 늘어놓기", "테이블 행을 <b>가장 흔히</b> 보는 모습입니다"),
    (row([cell("영수증_01.jpg", "1.2MB", True, False)], "파일 목록", "", True), "파일마다 동작 단추 두기", "동작 단추는 <b>줄 끝</b>에 둡니다"),
    (row([cell("홍길동", "관리자", False, False)], "사람 목록", "", True), "고르기 칸이 없는 사람 목록", "여러 줄을 고를 일이 없으면 고르기가 <b>없을 수도</b> 있습니다"),
  ]),
  keys_heads="<th>키와 마크업</th><th>지켜야 할 점</th>",
  code_lede="표의 줄은 <code>&lt;tr&gt;</code>로 만듭니다. 행 전체를 링크로 만들지 말고 <b>주 열만</b> 링크로 두는 쪽이 안전합니다.",
  code='''&lt;<span class="t">tr</span>&gt;
  &lt;<span class="t">td</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">aria-label</span>=<span class="s">"모란상회 고르기"</span>&gt;&lt;/<span class="t">td</span>&gt;
  &lt;<span class="t">th</span> <span class="a">scope</span>=<span class="s">"row"</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/s/2411"</span>&gt;모란상회&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">th</span>&gt;
  &lt;<span class="t">td</span> <span class="a">class</span>=<span class="s">"num"</span>&gt;1,284,000원&lt;/<span class="t">td</span>&gt;
  &lt;<span class="t">td</span>&gt;&lt;<span class="t">button</span>&gt;영수증&lt;/<span class="t">button</span>&gt;&lt;/<span class="t">td</span>&gt;
&lt;/<span class="t">tr</span>&gt;

.num { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">// 행 전체를 누를 수 있게 했다면 안쪽 요소의 눌림을 먼저 막는다</span>
row.querySelectorAll(<span class="s">'button, input, a'</span>).forEach(el =&gt;
  el.addEventListener(<span class="s">'click'</span>, e =&gt; e.stopPropagation()));''',
  keys=kbd([
    ("주 열에 <code>&lt;th scope=\"row\"&gt;</code> 쓰기", "주 열을 <b>줄의 제목</b>으로 삼습니다. 스크린 리더가 값을 읽을 때 이 제목을 기준으로 읽습니다"),
    ("Tab", "포커스가 줄마다 <b>체크박스, 링크, 단추</b> 차례로 지나갑니다"),
    ("체크박스에 <code>aria-label</code> 붙이기", "체크박스에 <b>그 줄의 이름</b>을 넣습니다"),
    ("고른 줄에 <code>aria-selected</code> 달기", "고른 줄을 알립니다. 바탕색만 바꾸면 스크린 리더로는 알 수 없습니다"),
    ("행 전체를 링크로 감쌀 때", "링크 안에 단추를 넣는 것은 <b>잘못된 마크업</b>입니다"),
    ("확인하는 방법", "Tab으로 한 줄을 지나가며 포커스가 <b>몇 번 멈추는지</b> 셉니다"),
  ]),
  backend=rows([
    ("줄을 데이터에 묶는 <code>id</code>", "<code>id</code>가 있어야 고르기와 동작을 그 줄의 데이터에 묶을 수 있습니다. 줄의 순서 번호로 묶으면 정렬이 바뀔 때 다른 데이터를 가리키게 됩니다."),
    ("말줄임은 화면에서 하기", "서버가 값을 미리 잘라 보내면 잘린 부분은 <b>검색도 복사도</b> 할 수 없습니다. 서버는 온전한 값을 보내고, 화면에서 말줄임으로 줄입니다."),
    ("줄마다 다른 권한 알려 주기", "줄마다 할 수 있는 일이 다르면 <code>can_edit</code> 같은 값을 함께 보내야 화면에서 줄마다 <b>단추를 그릴지</b> 정할 수 있습니다."),
  ]),
  plat_lede="<b>표는 주로 PC 화면</b>에서 쓰고, 폰에서는 표의 줄이 카드 모양으로 바뀝니다.",
  plats=plats([
    ("웹", "&lt;tr&gt;",
     row([cell("모란상회", "1,284,000")], "표의 줄", "", True, "110px"),
     "실제 표 태그를 쓰면 스크린 리더가 <b>값을 읽을 때</b> 열 이름도 함께 읽어 줍니다."),
    ("iOS", "Table row · List",
     '''              <div class="phone" role="img" aria-label="iOS 목록 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:41px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:30px;font-size:5px;color:var(--fg-muted)">›</div></div></div>''',
     "화면이 좁아서 여러 열을 세울 수 없으므로, <b>한 줄에 값을 두세 개</b>만 넣고 나머지는 상세 화면으로 넘깁니다."),
    ("안드로이드", "RecyclerView 항목",
     '''              <div class="phone" role="img" aria-label="안드로이드 목록 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:11px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:43px;height:11px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "안드로이드도 표가 아니라 <b>목록 항목</b>으로 보여 주고, 값이 많으면 접어 두었다가 펼쳐 보게 합니다."),
  ]),
  plat_note="폰 화면에서 표를 쓰지 않는 것은, 열 네 개를 390px 폭에 세우면 <b>어느 열도 읽을 수 없기</b> 때문입니다. 웹에서도 폰 폭에서는 표의 줄을 <b>카드 모양</b>으로 바꾸는 것이 보통인데, 이때 <b>어떤 값을 남기고 어떤 값을 상세 화면으로 미룰지</b> 정해야 합니다. 이 판단은 그 줄에서 무엇이 주 열인지를 정하는 일과 같으므로, 표를 처음 설계할 때 미리 정해 두면 좋습니다.",
  siblings=siblings("tablerow"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="hover.html"><b>호버가 없는 세계</b><em>11부</em></a></li>''',
)
