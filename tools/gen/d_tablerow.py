# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">고르기 — 줄마다 다른 이름을 준다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">주 열 — 이 줄이 무엇인지 말한다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">숫자 열 — 오른쪽 맞춤 · tabular-nums</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">동작 — 줄 끝에 둔다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">행 전체를 링크로 두면 안쪽 단추가 행을 뚫는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">밀도 — 한 화면에 몇 줄이 들어가나</div>
                </div>
              </div>'''

D = dict(
  slug="tablerow", ko="테이블 행", en="Table row",
  desc="표의 줄 하나. 고르기·주 열·값·동작의 자리, 밀도, 행 전체를 눌리게 할 때의 함정.",
  lede="줄 하나에 보통 넷이 들어갑니다 — <b>고르기 · 주 열 · 값 · 동작</b>. 자리를 섞으면 눈이 줄마다 헤맵니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>밀도를 바꾸면 한 화면에 들어가는 줄 수가 달라집니다 — 데모가
          <b>480px 높이에 몇 줄이 들어가는지</b> 재서 적습니다.<br>
          <b>행 전체를 눌리게</b> 하면 편한 대신, 안에 있는 단추를 눌러도
          <b>행 이동이 같이 일어납니다</b>. 데모가 그 횟수를 셉니다 —
          막으려면 안쪽 단추에서 <code>stopPropagation()</code> 을 해야 합니다.<br>
          고르기 체크박스에는 <b>줄마다 다른 이름</b>이 필요합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "테이블 행, 표 줄, 레코드 행"),
    ("영어", "table row, record row, data row"),
    ("같이 쓰는 말",
     "그 줄이 무엇인지 말해 주는 열을 <b>주 열</b>(primary column), "
     "줄 간격의 빽빽함을 <b>밀도</b>(density), 한 줄 건너 바탕을 바꾸는 것을 <b>줄무늬</b>(zebra striping)라 합니다. "
     "마우스를 올려야 나타나는 단추는 <b>호버 액션</b>인데, 터치에서는 안 보입니다."),
    ("자주 잘못 부름",
     "<b>데이터 테이블</b> — <a href=\"table.html\">데이터 테이블</a>은 <b>표 전체</b>의 설계입니다.<br>"
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>열이 없는</b> 한 건입니다.<br>"
     "<b>카드</b> — <a href=\"card.html\">카드</a>는 <b>덩어리</b>로 서고 행은 <b>줄</b>로 섭니다."),
  ]),
  axes=ax("테이블 행"),
  oneline="<b>행 전체를 누르게 하려면 안쪽 단추를 먼저 막으세요.</b> 안 막으면 둘이 같이 일어납니다.",
  states=states([
    (row([cell("모란상회", "1,284,000")], "기본", "넷이 제자리에 있다", True),
     "기본", "고르기 · 주 열 · 값 · 동작"),
    (row([cell("모란상회", "1,284,000")], "고름", "", True, "152px", "5px 6px", True),
     "고른 줄", "<b>바탕이 바뀐다</b>"),
    (row([cell("모란상회", "1,284,000"), cell("한빛아웃도어 영등…", "842,500")], "빽빽하게", "한 화면에 더 들어간다", True, "152px", "2px 6px"),
     "빽빽하게", "<b>훑어보기</b>에 좋다"),
    (row([cell("모란상회", "1,284,000")], "넉넉하게", "읽기 편한 대신 줄이 적다", None, "152px", "9px 6px"),
     "넉넉하게", "<b>한 줄씩 읽을</b> 때"),
    (row([cell("한빛아웃도어 영등포타…", "842,500")], "긴 이름", "말줄임으로 줄 높이를 지킨다", True),
     "내용이 길면", "<b>말줄임</b>한다"),
    (row([cell("모란상회", "1,284,000")], "행 전체 링크", "단추를 눌러도 행 이동이 따라온다", False),
     "행 전체 누름", "<b>안쪽 단추와 부딪힌다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("고르기", "줄마다 이름", "전부 '선택'이면 <b>구별이 안 된다</b>"),
    ("주 열", "무엇인지", "<b>왼쪽 첫 자리</b>에 둔다"),
    ("숫자 열", "오른쪽 맞춤", "<code>tabular-nums</code> 로 자릿수 맞춤"),
    ("동작", "줄 끝", "늘 <b>같은 자리</b>에"),
    ("행 전체 링크", "부딪힘", "안쪽 단추를 <b>먼저 막는다</b>"),
    ("밀도", "줄 수", "빽빽할수록 <b>많이 보인다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>마우스를 올려야 단추가 보이게</b> 하는 꼴이 흔한데,
          터치에서는 호버가 없어 <b>단추가 영영 안 보입니다</b>.
          늘 보이게 두거나, 적어도 좁은 화면에서는 보이게 바꿔야 합니다.<br>
          행 전체를 링크로 만들 때는 <b>안쪽에 뭐가 있는지</b> 먼저 세어 보세요 —
          체크박스 하나와 단추 하나만 있어도
          둘 다 <code>stopPropagation()</code> 이 필요합니다.
          그게 번거로우면 <b>주 열만 링크</b>로 두는 쪽이 사고가 적습니다.</p>''',
  do=ul([
    "고르기 체크박스에 <b>줄마다 다른 이름</b> 주기",
    "숫자는 <b>오른쪽 맞춤 + <code>tabular-nums</code></b>",
    "행 전체를 누르게 하려면 <b>안쪽 단추를 먼저</b> 막기",
  ]),
  dont=ul([
    "단추를 <b>호버에만</b> 보이게 하기 — 터치에서는 안 보인다",
    "줄마다 동작 단추의 <b>자리를 다르게</b> 두기",
    "긴 이름을 <b>줄바꿈</b>으로 흘리기 — 줄 높이가 들쭉날쭉해진다",
    "고르기 이름을 전부 <b>'선택'</b>으로 두기",
  ]),
  instead='표 전체 설계는 <a href="table.html">데이터 테이블</a>, 열 없는 한 건은 <a href="listitem.html">리스트 아이템</a>, 여러 줄 고르기는 <a href="bulk.html">일괄 선택</a>, 덩어리로 서면 <a href="card.html">카드</a>.',
  cases=cases([
    (row([cell("모란상회", "1,284,000")], "정산 목록", "", True), "정산 목록", "<b>가장 흔한</b> 꼴"),
    (row([cell("영수증_01.jpg", "1.2MB", True, False)], "파일 목록", "", True), "파일 목록", "동작은 <b>줄 끝</b>에"),
    (row([cell("홍길동", "관리자", False, False)], "사람 목록", "", True), "사람 목록", "고르기가 <b>없을 수도</b> 있다"),
  ]),
  code_lede="표의 줄은 <code>&lt;tr&gt;</code> 입니다. 행 전체를 링크로 만들지 않고 <b>주 열만</b> 링크로 두는 쪽이 안전합니다.",
  code='''&lt;<span class="t">tr</span>&gt;
  &lt;<span class="t">td</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">aria-label</span>=<span class="s">"모란상회 고르기"</span>&gt;&lt;/<span class="t">td</span>&gt;
  &lt;<span class="t">th</span> <span class="a">scope</span>=<span class="s">"row"</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/s/2411"</span>&gt;모란상회&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">th</span>&gt;
  &lt;<span class="t">td</span> <span class="a">class</span>=<span class="s">"num"</span>&gt;1,284,000원&lt;/<span class="t">td</span>&gt;
  &lt;<span class="t">td</span>&gt;&lt;<span class="t">button</span>&gt;영수증&lt;/<span class="t">button</span>&gt;&lt;/<span class="t">td</span>&gt;
&lt;/<span class="t">tr</span>&gt;

.num { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }

<span class="c">// 행 전체를 눌리게 했다면 안쪽은 먼저 막는다</span>
row.querySelectorAll(<span class="s">'button, input, a'</span>).forEach(el =&gt;
  el.addEventListener(<span class="s">'click'</span>, e =&gt; e.stopPropagation()));''',
  keys=kbd([
    ("<code>&lt;th scope=\"row\"&gt;</code>", "주 열을 <b>줄의 제목</b>으로 삼는다 — 소리로 읽을 때 기준이 된다"),
    ("Tab", "줄마다 <b>체크박스 → 링크 → 단추</b> 차례로 지나간다"),
    ("<code>aria-label</code>", "체크박스에 <b>그 줄의 이름</b>을 넣는다"),
    ("<code>aria-selected</code>", "고른 줄을 알린다 — 바탕색만으로는 안 들린다"),
    ("행 전체 링크", "링크 안에 단추를 넣는 것은 <b>잘못된 마크업</b>이다"),
    ("확인하는 법", "Tab 으로 한 줄을 지나며 <b>몇 번 멈추는지</b> 센다"),
  ]),
  backend=rows([
    ("줄의 열쇠", "<code>id</code> 가 있어야 고르기와 동작을 줄에 묶을 수 있습니다 — 순서 번호로 하면 정렬이 바뀔 때 어긋납니다."),
    ("말줄임은 화면에서", "서버가 미리 잘라 보내면 <b>검색도 복사도</b> 안 됩니다 — 온전한 값을 주고 화면이 줄입니다."),
    ("권한", "줄마다 할 수 있는 일이 다르면 <code>can_edit</code> 같은 값을 같이 줘야 <b>단추를 그릴지</b> 정할 수 있습니다."),
  ]),
  plat_lede="<b>표는 PC 쪽</b>이고 폰에서는 줄이 카드로 바뀝니다.",
  plats=plats([
    ("웹", "&lt;tr&gt;",
     row([cell("모란상회", "1,284,000")], "표의 줄", "", True, "110px"),
     "진짜 표 태그를 쓰면 <b>소리로 읽을 때</b> 열 이름이 같이 읽힙니다."),
    ("iOS", "Table row · List",
     '''              <div class="phone" role="img" aria-label="iOS 목록 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:41px;height:9px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:30px;font-size:5px;color:var(--fg-muted)">›</div></div></div>''',
     "좁아서 열을 못 세웁니다 — <b>한 줄에 두세 값</b>만 넣고 나머지는 상세로 넘깁니다."),
    ("안드로이드", "RecyclerView 항목",
     '''              <div class="phone" role="img" aria-label="안드로이드 목록 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;height:11px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:43px;height:11px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "역시 표가 아니라 <b>목록 항목</b>입니다. 값이 많으면 접어서 보입니다."),
  ]),
  plat_note="폰에 표가 없는 데는 이유가 있습니다 — 열 넷을 390px 에 세우면 <b>어느 열도 못 읽습니다</b>. 웹에서도 폰 폭에서는 줄을 <b>카드 꼴</b>로 바꾸는 것이 보통인데, 그때 <b>어떤 값을 남기고 어떤 값을 상세로 미룰지</b>를 정해야 합니다. 그 판단이 곧 '이 줄에서 무엇이 주 열인가'에 대한 답이라, 표를 만들 때 미리 해 두면 좋습니다.",
  siblings=siblings("tablerow"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="hover.html"><b>호버가 없는 세계</b><em>11부</em></a></li>''',
)
