# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def scr(inner, w="152px", head="검색 결과"):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<div style="padding:5px 8px;border-bottom:1px solid var(--line);background:var(--bg);font-size:9px;font-weight:700">' + head + '</div>'
            '<div style="padding:7px 8px;display:grid;gap:5px">' + inner + '</div></div>')

def qbox(q):
    return ('<div style="display:flex;align-items:center;gap:4px;border:1px solid var(--line);border-radius:999px;'
            'padding:3px 8px;font-size:9.5px"><span aria-hidden="true" style="font-size:8px">🔍</span><span>' + q + '</span></div>')

def res(items):
    return ''.join('<div style="font-size:9.5px;border-top:1px solid var(--line);padding:4px 0">' + i +
                   '<span style="display:block;font-size:8px;color:var(--fg-muted)">1,284,000원 · 승인됨</span></div>' for i in items)

MARK = '<b style="background:var(--warn-soft);border-radius:2px;padding:0 1px">모란</b>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:220px">''' + qbox('모란').strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">‘모란’ · 승인됨 · 6건처럼 찾은 조건을 다시 적음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">?q=모란&amp;f=승인됨&amp;page=2처럼 주소에 담음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">굴린 자리를 기억했다가 돌아올 때 되살림</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">0건이면 조건 지우기와 다른 질의를 제안함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">돌아왔을 때 빈 화면이 가장 흔한 민원</div>
                </div>
              </div>'''

D = dict(
  slug="searchresults", ko="검색 결과 화면", en="Search results page",
  desc="찾은 것 가운데 하나를 고르는 화면입니다. 질의를 다시 보여 주는 법, 상태를 주소에 담는 법, 돌아왔을 때 되살리는 법을 다룹니다.",
  lede="검색은 <b>찾는 일</b>이고 결과 화면은 그 가운데서 <b>고르는 일</b>을 합니다. 사용자는 결과 하나에 들어갔다가 다시 <b>돌아오기</b>를 되풀이하므로, 이 왕복이 매끄럽게 되도록 만드는 것이 설계의 핵심입니다.",
  axes_lede="화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>결과에서 한 건을 눌러 들어갔다가 <b>← 뒤로</b>를 눌러 보세요.<br>
          두 설정을 모두 켜 두면 <b>질의 · 필터 · 굴린 자리</b>가 그대로 되살아납니다. 반대로 끄면 빈 검색 화면으로
          돌아가서 <b>처음부터 다시</b> 찾아야 하는데, 목록 화면에서 가장 자주 나오는 민원이 바로 이 경우입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "검색 결과, 결과 목록, 목록 화면"),
    ("영어", "search results page, SERP, results listing"),
    ("같이 쓰는 말",
     "검색 엔진 쪽에서는 <b>SERP</b>(search engine results page)라고 부릅니다. "
     "결과에서 하나를 눌러 들어갔다 돌아오는 것을 <b>왕복</b>(pogo-sticking)이라 하고, "
     "돌아왔을 때 이전 상태를 되살리는 것을 <b>상태 복원</b>(scroll restoration·state restoration)이라고 합니다. "
     "검색어와 맞은 글자를 굵게 보여 주는 것은 <b>하이라이팅</b>·<b>스니펫</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>검색</b> — <a href=\"search.html\">검색</a>은 입력칸과 응답 처리를 다루고, 이 항목은 <b>결과 화면 전체</b>를 다룹니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터</a>는 결과 화면을 이루는 한 부분입니다.<br>"
     "<b>목록</b> — 일반 목록에는 질의가 없지만, 결과 화면은 <b>무엇으로 찾았는지</b>를 늘 함께 들고 있습니다."),
  ]),
  axes=ax("검색 결과 화면"),
  oneline="<b>검색 상태를 주소에 담으세요.</b> 주소에 담으면 공유·새로고침·뒤로가기가 한꺼번에 해결되지만, 담지 않으면 세 가지 모두 제대로 동작하지 않습니다.",
  do_title="검색 결과 화면으로 만들면 좋은 경우",
  dont_title="검색 결과 화면을 잘못 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  s4_title="결과 화면의 상태", s4_hint="들어갔다 돌아오는 왕복이 매끄러운가",
  states=states([
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">‘모란’ · <b>6건</b></span>' + res([MARK + '상회 신길역점', MARK + '김밥 가산점'])),
     "결과가 있을 때", "<b>무엇으로 찾았는지</b>와 건수를 다시 적어 줍니다"),
    (scr(qbox('모란') + '<div style="display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:1px 6px;font-size:8px">승인됨 ✕</span></div>'
         '<span style="font-size:8.5px;color:var(--fg-muted)">‘모란’ · 승인됨 · <b>3건</b></span>' + res([MARK + '상회 신길역점'])),
     "필터 조건을 걸었을 때", "걸어 둔 <a href=\"filter.html\">필터</a>가 <b>칩</b>으로 보입니다"),
    (scr(qbox('모란닭강정') + '<div style="border:1px dashed var(--line);border-radius:5px;padding:8px;text-align:center;font-size:8.5px;color:var(--fg-muted)">맞는 것이 없습니다<br><span style="color:var(--accent)">‘모란’으로 넓혀 보기</span></div>'),
     "결과가 0건일 때", "<b>입력한 글자를 그대로 적고</b> 검색 범위를 넓힐 방법을 알려 줍니다"),
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">불러오는 중…</span>'
         '<div style="display:grid;gap:4px"><span class="skl" style="height:9px"></span><span class="skl" style="height:9px;width:70%"></span></div>'),
     "새 결과를 불러오는 중", "새 결과가 올 때까지 <b>이전 결과를 지우지 않습니다</b>"),
    (scr('<span style="font-size:9.5px;font-weight:700">모란상회 신길역점</span>'
         '<span style="font-size:8.5px;color:var(--fg-muted)">1,284,000원 · 승인됨</span>'
         '<span style="font-size:9px;color:var(--accent)">← 결과로 돌아가기</span>', "152px", "상세"),
     "결과 하나에 들어갔을 때", "결과로 <b>돌아가는 링크</b>가 화면 안에도 있어야 합니다"),
    (scr(qbox('') + '<span style="font-size:8.5px;color:var(--danger)">질의를 잃어 처음부터 다시 찾음</span>', "152px"),
     "돌아왔는데 빈 화면이 뜰 때", "검색 상태를 <b>주소에 담지 않았을 때</b> 생기는 일입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("질의 상자", "입력한 글자 그대로", "입력한 글자가 결과 화면에도 <b>남아 있어야</b> 고쳐서 다시 찾을 수 있습니다"),
    ("요약 줄", "‘모란’ · 승인됨 · 6건", "<b>무엇으로 찾아 몇 건</b>이 나왔는지 적습니다. 0건일 때 특히 중요합니다"),
    ("주소", "?q=&f=&page=", "상태를 주소에 담으면 <b>공유 · 새로고침 · 뒤로가기</b>가 한꺼번에 해결됩니다"),
    ("굴린 자리", "복원", "돌아왔을 때 <b>보던 줄</b>부터 이어서 볼 수 있게 합니다"),
    ("0건일 때 안내", "넓히기 · 지우기", "결과가 없을 때도 다음에 할 일을 보여 줘서 사용자가 멈추지 않게 합니다"),
    ("상태를 잃은 화면", "빈 화면", "사용자가 <b>처음부터 다시</b> 찾아야 해서 가장 흔한 민원이 됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>굴린 자리를 복원하는 일은 생각보다 까다롭습니다.</b>
          돌아왔을 때 목록 데이터를 아직 받지 못했다면 복원할 자리가 없고,
          그 상태에서 억지로 스크롤 위치를 맞춰 두면 데이터가 들어오면서 위치가 다시 바뀝니다.
          그래서 데이터를 <b>받아서 그린 다음</b>에 복원해야 하고,
          <a href="../items/infinite.html">무한 스크롤</a>이라면 <b>몇 쪽까지 받았는지</b>도 함께 기억해야 합니다.
          무한 스크롤보다 <a href="../items/pagination.html">페이지네이션</a>이
          복원하기 편한 이유가 여기에 있는데, 쪽 번호 하나만 있으면 돌아갈 자리가 정해지기 때문입니다.</p>''',
  do=ul([
    "목록·상품·문서처럼 찾은 뒤 <b>하나를 골라 들어가는</b> 화면일 때",
    "조건이 여럿 붙는 목록일 때. 조건을 <b>주소에 담아</b> 공유할 수 있게 합니다",
    "건수가 많아 <b>쪽을 넘겨야 하는</b> 화면일 때",
  ]),
  dont=ul([
    "질의를 <b>주소에 담지 않을 때</b>. 공유도 새로고침도 되지 않습니다",
    "0건일 때 다음에 할 일을 보여 주지 않아 <b>막다른 길</b>을 만들 때",
    "돌아온 사용자를 <b>맨 위로</b> 보낼 때",
    "입력한 글자를 결과 화면에서 지울 때. 검색어를 고쳐서 다시 찾을 수 없게 됩니다",
  ]),
  instead='검색 입력칸과 응답 처리는 <a href="search.html">검색</a>에서, 조건을 고르는 부품은 <a href="filter.html">필터와 패싯</a>에서 다룹니다. 결과 줄이 아주 많으면 <a href="virtual.html">가상 스크롤</a>도 함께 봅니다.',
  cases=cases([
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">6건 · 관련도순</span>' + res([MARK + '상회 신길역점']), "150px"),
     "건수와 정렬 기준 알려 주기", "결과를 <b>무엇을 기준으로</b> 정렬했는지 적어 둡니다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--accent);word-break:break-all">
                /search?q=모란&amp;f=승인됨&amp;page=2
              </div>''',
     "검색 상태를 주소에 담기", "주소 한 줄에 상태를 담으면 <b>공유·새로고침·뒤로가기</b>가 모두 해결됩니다"),
    (scr(qbox('모란닭강정') + '<span style="font-size:8.5px;color:var(--fg-muted)">이렇게 찾아보세요</span>'
         '<span style="font-size:9px;color:var(--accent)">모란 · 닭강정 · 모란상회</span>', "150px"),
     "0건일 때 다른 검색어 제안하기", "범위를 넓힌 질의를 <b>눌러서</b> 바로 검색할 수 있게 합니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="검색 상태를 주소에 담고, 돌아왔을 때는 목록을 <b>그린 뒤에</b> 스크롤 위치를 되살립니다.",
  code='''&lt;<span class="t">form</span> <span class="a">role</span>=<span class="s">"search"</span> <span class="a">action</span>=<span class="s">"/search"</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"q"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;가맹점 검색&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"q"</span> <span class="a">name</span>=<span class="s">"q"</span> <span class="a">type</span>=<span class="s">"search"</span> <span class="a">value</span>=<span class="s">"모란"</span>&gt;
&lt;/<span class="t">form</span>&gt;

&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;‘모란’ 검색 결과 6건&lt;/<span class="t">p</span>&gt;
&lt;<span class="t">ol</span>&gt;…&lt;/<span class="t">ol</span>&gt;

<span class="c">// 조건이 바뀌면 방문 기록을 쌓지 말고 갈아끼운다</span>
history.replaceState(<span class="k">null</span>, <span class="s">''</span>, <span class="s">`?q=${</span>q<span class="s">}&amp;f=${</span>f<span class="s">}`</span>);

<span class="c">// 상세로 갈 때 굴린 자리를 적어 둔다</span>
sessionStorage.setItem(<span class="s">'pos'</span>, String(list.scrollTop));

<span class="c">// 돌아와서는 "그린 뒤에" 되살린다</span>
<span class="k">await</span> renderResults();
list.scrollTop = +sessionStorage.getItem(<span class="s">'pos'</span>) || <span class="a">0</span>;''',
  keys=kbd([
    ("<code>role=\"search\"</code>", "검색 영역을 하나의 구역으로 알립니다. 스크린 리더 사용자가 그 구역으로 바로 건너뛸 수 있습니다"),
    ("<code>role=\"status\"</code>", "'6건'처럼 건수를 알립니다. 소리 없이 <b>결과만 바뀌면</b> 화면을 눈으로 보지 않는 사람은 바뀐 줄 모릅니다"),
    ("결과를 <code>&lt;ol&gt;</code>로 적기", "결과는 순서에 뜻이 있으므로 순서 있는 목록으로 적습니다. 스크린 리더가 '6개 중 2번째'처럼 읽어 줍니다"),
    ("<code>replaceState</code>와 <code>pushState</code>", "조건만 바뀌었을 때는 방문 기록을 쌓지 않고 <b>갈아끼웁니다</b>(<a href=\"systemback.html\">시스템 백</a>)"),
    ("<code>scrollRestoration</code>", "브라우저 기본 복원과 직접 만든 복원이 함께 돌면 <b>서로 위치를 덮어쓸 수</b> 있으므로 하나만 씁니다"),
    ("초점을 되돌릴 자리", "상세 화면에서 돌아오면 <b>눌렀던 줄</b>로 초점을 되돌립니다. 되돌리지 않으면 Tab을 처음부터 다시 눌러야 합니다"),
  ]),
  backend=rows([
    ("검색 조건을 주소에서 읽기", "서버가 <code>?q=</code>·<code>?page=</code>를 그대로 받아 화면을 그리면, <b>공유한 링크를 연 사람도 같은 화면</b>을 봅니다."),
    ("정렬·필터 값은 허용 목록으로 거르기", "<code>sort</code>·<code>f</code> 값을 그대로 질의에 넣지 않고, 허용한 값인지 확인한 뒤에 씁니다. <a href=\"table.html\">데이터 테이블</a>과 같은 주입 문제가 생기기 때문입니다."),
    ("정렬 값이 같은 줄의 순서 고정하기", "정렬 값이 같은 줄들의 순서가 요청마다 달라지면 <b>쪽을 넘길 때 같은 줄이 두 번</b> 나옵니다. 그래서 ID를 2차 정렬 기준으로 붙입니다."),
    ("건수를 세는 비용이 큼", "큰 표에서는 <code>COUNT(*)</code>가 느립니다. 그래서 건수를 <b>'100+ 건'</b>으로 적거나 커서 방식으로 바꿉니다."),
    ("검색어 없이 요청이 왔을 때", "<code>?q=</code>가 비었을 때 전체를 돌려줄지, 아무것도 돌려주지 않을지 <b>미리 정해 둡니다</b>. 정해 두지 않으면 빈 질의가 들어올 때마다 전체 조회가 돌아 서버에 큰 부하가 걸립니다."),
  ]),
  plat_lede="결과 화면으로 <b>돌아오는 방식</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "주소 + 뒤로가기",
     scr(qbox('모란') + res([MARK + '상회']), "112px"),
     "상태를 주소에 담으면 공유·새로고침·뒤로가기가 한꺼번에 됩니다. 이 점이 <b>웹의 가장 큰 장점</b>입니다."),
    ("iOS", "화면 스택",
     '''              <div class="phone" role="img" aria-label="iOS 결과 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px;color:var(--accent)">‹ 검색</span>
                <div style="position:absolute;left:4px;right:4px;top:28px;display:grid;gap:3px"><span style="height:7px;background:var(--line);border-radius:2px"></span><span style="height:7px;background:var(--line);border-radius:2px"></span></div></div></div>''',
     "앞 화면이 스택에 <b>그대로 남아 있어서</b> 따로 복원할 필요가 없습니다. 대신 공유할 주소가 없으므로 딥링크를 따로 만듭니다."),
    ("안드로이드", "백 스택",
     '''              <div class="phone" role="img" aria-label="안드로이드 결과 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px">← 모란</span>
                <div style="position:absolute;left:4px;right:4px;top:28px;display:grid;gap:3px"><span style="height:7px;background:var(--line);border-radius:2px"></span><span style="height:7px;background:var(--line);border-radius:2px"></span></div></div></div>''',
     "iOS와 같은 방식이지만, 시스템이 앱 <b>프로세스를 종료했다가 다시 띄울 수</b> 있어서 상태를 따로 저장해 두는 코드가 필요합니다."),
  ]),
  plat_note="\"목록에서 들어갔다 나오면 맨 위로 가요\"는 기획서에 적혀 있지 않지만 <b>반드시 나오는</b> 민원입니다. 단일 페이지 앱(SPA)으로 만들면 브라우저가 해 주던 스크롤 복원이 사라지기 때문입니다. 목록 화면을 설계할 때 <b>'돌아왔을 때'</b> 어떻게 되는지 한 줄 적어 두면, 나중에 급하게 붙이는 것보다 훨씬 적은 품으로 끝납니다.",
  siblings=siblings("searchresults"),
  related='''        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
