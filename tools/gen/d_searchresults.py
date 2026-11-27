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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">‘모란’ · 승인됨 · 6건 — 무엇으로 찾았는지 다시 적는다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">?q=모란&amp;f=승인됨&amp;page=2 — 주소에 담는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">굴린 자리를 기억했다 돌아올 때 되살린다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">0건이면 조건을 지울 길과 다른 질의를 준다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">돌아왔더니 빈 화면 — 가장 흔한 민원</div>
                </div>
              </div>'''

D = dict(
  slug="searchresults", ko="검색 결과 화면", en="Search results page",
  desc="찾은 것을 고르는 화면. 질의를 다시 보여 주기, 주소에 담기, 돌아왔을 때 되살리기.",
  lede="검색은 <b>찾는 일</b>이고 결과 화면은 <b>고르는 일</b>입니다. 들어갔다 <b>돌아오는</b> 왕복이 설계의 전부입니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>결과에서 한 건을 눌러 들어갔다가 <b>← 뒤로</b>를 눌러 보세요.<br>
          둘 다 켜 두면 <b>질의 · 필터 · 굴린 자리</b>가 그대로 살아납니다. 끄면 빈 검색 화면으로
          돌아가고 <b>처음부터 다시</b> 찾아야 합니다 — 목록 화면에서 가장 자주 나오는 민원입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "검색 결과, 결과 목록, 목록 화면"),
    ("영어", "search results page, SERP, results listing"),
    ("같이 쓰는 말",
     "검색 엔진 쪽에서는 <b>SERP</b>(search engine results page)라 부릅니다. "
     "결과에서 하나를 눌러 들어갔다 돌아오는 것을 <b>왕복</b>(pogo-sticking), "
     "돌아왔을 때 상태를 되살리는 것을 <b>상태 복원</b>(scroll restoration·state restoration)이라 합니다. "
     "맞은 글자를 굵게 보여 주는 것은 <b>하이라이팅</b>·<b>스니펫</b>입니다."),
    ("자주 잘못 부름",
     "<b>검색</b> — <a href=\"search.html\">검색</a>은 입력칸과 응답 처리, 이쪽은 <b>결과 화면 전체</b>입니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터</a>는 이 화면의 한 부분입니다.<br>"
     "<b>목록</b> — 그냥 목록은 질의가 없습니다. 결과 화면은 <b>무엇으로 찾았는지</b>를 늘 지고 있습니다."),
  ]),
  axes=ax("검색 결과 화면"),
  oneline="<b>상태를 주소에 담으세요.</b> 그러면 공유·새로고침·뒤로가기가 한꺼번에 해결되고, 안 담으면 셋 다 깨집니다.",
  s4_title="상태", s4_hint="왕복이 되는가",
  states=states([
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">‘모란’ · <b>6건</b></span>' + res([MARK + '상회 신길역점', MARK + '김밥 가산점'])),
     "결과 있음", "<b>무엇으로 찾았는지</b>와 건수를 다시 적는다"),
    (scr(qbox('모란') + '<div style="display:flex;gap:3px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:1px 6px;font-size:8px">승인됨 ✕</span></div>'
         '<span style="font-size:8.5px;color:var(--fg-muted)">‘모란’ · 승인됨 · <b>3건</b></span>' + res([MARK + '상회 신길역점'])),
     "조건이 걸림", "<a href=\"filter.html\">필터</a>가 <b>칩</b>으로 보인다"),
    (scr(qbox('모란닭강정') + '<div style="border:1px dashed var(--line);border-radius:5px;padding:8px;text-align:center;font-size:8.5px;color:var(--fg-muted)">맞는 것이 없습니다<br><span style="color:var(--accent)">‘모란’으로 넓혀 보기</span></div>'),
     "0건", "<b>친 글자를 그대로 적고</b> 넓힐 길을 준다"),
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">불러오는 중…</span>'
         '<div style="display:grid;gap:4px"><span class="skl" style="height:9px"></span><span class="skl" style="height:9px;width:70%"></span></div>'),
     "불러오는 중", "<b>이전 결과를 지우지 않는다</b>"),
    (scr('<span style="font-size:9.5px;font-weight:700">모란상회 신길역점</span>'
         '<span style="font-size:8.5px;color:var(--fg-muted)">1,284,000원 · 승인됨</span>'
         '<span style="font-size:9px;color:var(--accent)">← 결과로 돌아가기</span>', "152px", "상세"),
     "들어갔을 때", "<b>돌아갈 길</b>이 화면 안에도 있어야 한다"),
    (scr(qbox('') + '<span style="font-size:8.5px;color:var(--danger)">질의를 잃었다 — 처음부터 다시</span>', "152px"),
     "돌아왔는데 빈 화면", "<b>주소에 안 담았을 때</b> 생기는 일"),
  ]),
  anat=ANAT,
  pins=pins([
    ("질의 상자", "친 글자 그대로", "결과 화면에도 <b>남아 있어야</b> 고쳐 찾는다"),
    ("요약 줄", "‘모란’ · 승인됨 · 6건", "<b>무엇으로 몇 건</b>인지. 0건일 때 특히 중요하다"),
    ("주소", "?q=&f=&page=", "<b>공유 · 새로고침 · 뒤로가기</b>가 한꺼번에 해결된다"),
    ("굴린 자리", "복원", "돌아왔을 때 <b>보던 줄</b>에서 이어 본다"),
    ("0건의 길", "넓히기 · 지우기", "막다른 길을 만들지 않는다"),
    ("안 담았을 때", "빈 화면", "<b>처음부터 다시</b>. 가장 흔한 민원"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>굴린 자리 복원은 생각보다 까다롭습니다.</b>
          돌아왔을 때 목록이 아직 안 받아졌으면 복원할 자리가 없고,
          그때 억지로 굴려 놓으면 데이터가 들어오면서 다시 튑니다.
          그래서 <b>받고 그린 다음</b>에 복원해야 하고,
          <a href="../items/infinite.html">무한 스크롤</a>이면 <b>몇 쪽까지 받았는지</b>도 함께 기억해야 합니다.
          이것이 무한 스크롤보다 <a href="../items/pagination.html">페이지네이션</a>이
          편한 이유 가운데 하나입니다 — 쪽 번호 하나면 자리가 정해집니다.</p>''',
  do=ul([
    "찾은 뒤 <b>골라 들어가는</b> 화면 — 목록·상품·문서",
    "조건이 여럿 붙는 목록 — <b>주소에 담아</b> 공유되게",
    "건수가 많아 <b>쪽을 넘기는</b> 화면",
  ]),
  dont=ul([
    "질의를 <b>주소에 안 담기</b> — 공유도 새로고침도 안 된다",
    "0건에서 <b>막다른 길</b> 만들기",
    "돌아왔을 때 <b>맨 위로</b> 보내기",
    "친 글자를 결과 화면에서 지우기 — 고쳐 찾을 수가 없다",
  ]),
  instead='입력칸과 응답 처리는 <a href="search.html">검색</a>, 조건 고르기는 <a href="filter.html">필터와 패싯</a>, 줄이 아주 많으면 <a href="virtual.html">가상 스크롤</a>.',
  cases=cases([
    (scr(qbox('모란') + '<span style="font-size:8.5px;color:var(--fg-muted)">6건 · 관련도순</span>' + res([MARK + '상회 신길역점']), "150px"),
     "건수와 순서", "<b>무엇을 기준으로</b> 줄 세웠는지 적는다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--accent);word-break:break-all">
                /search?q=모란&amp;f=승인됨&amp;page=2
              </div>''',
     "주소에 담기", "이 한 줄이 <b>공유·새로고침·뒤로가기</b>를 다 해결한다"),
    (scr(qbox('모란닭강정') + '<span style="font-size:8.5px;color:var(--fg-muted)">이렇게 찾아보세요</span>'
         '<span style="font-size:9px;color:var(--accent)">모란 · 닭강정 · 모란상회</span>', "150px"),
     "0건의 다음 수", "넓힌 질의를 <b>눌러서</b> 갈 수 있게"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="상태를 주소에 담고, 돌아올 때 <b>그린 뒤에</b> 자리를 되살립니다.",
  code='''&lt;<span class="t">form</span> <span class="a">role</span>=<span class="s">"search"</span> <span class="a">action</span>=<span class="s">"/search"</span>&gt;
  &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"q"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;가맹점 검색&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"q"</span> <span class="a">name</span>=<span class="s">"q"</span> <span class="a">type</span>=<span class="s">"search"</span> <span class="a">value</span>=<span class="s">"모란"</span>&gt;
&lt;/<span class="t">form</span>&gt;

&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;‘모란’ 검색 결과 6건&lt;/<span class="t">p</span>&gt;
&lt;<span class="t">ol</span>&gt;…&lt;/<span class="t">ol</span>&gt;

<span class="c">// 조건이 바뀌면 쌓지 말고 갈아끼운다</span>
history.replaceState(<span class="k">null</span>, <span class="s">''</span>, <span class="s">`?q=${</span>q<span class="s">}&amp;f=${</span>f<span class="s">}`</span>);

<span class="c">// 상세로 갈 때 굴린 자리를 적어 둔다</span>
sessionStorage.setItem(<span class="s">'pos'</span>, String(list.scrollTop));

<span class="c">// 돌아와서는 "그린 뒤에" 되살린다</span>
<span class="k">await</span> renderResults();
list.scrollTop = +sessionStorage.getItem(<span class="s">'pos'</span>) || <span class="a">0</span>;''',
  keys=kbd([
    ("<code>role=\"search\"</code>", "검색 영역을 구역으로 알린다. 스크린 리더가 바로 건너뛴다"),
    ("<code>role=\"status\"</code>", "'6건'. <b>결과만 바뀌면</b> 눈으로 안 보는 사람은 모른다"),
    ("<code>&lt;ol&gt;</code>로 적는다", "순서가 뜻을 지닌다. '6개 중 2번째'로 읽힌다"),
    ("<code>replaceState</code>와 <code>pushState</code>", "조건이 바뀔 뿐이면 <b>갈아끼운다</b> — <a href=\"systemback.html\">시스템 백</a>"),
    ("<code>scrollRestoration</code>", "브라우저 기본 복원과 직접 복원이 <b>싸울 수</b> 있다. 하나만 쓴다"),
    ("초점", "상세에서 돌아오면 <b>눌렀던 줄</b>로 초점을 되돌린다. 안 그러면 처음부터 Tab 한다"),
  ]),
  backend=rows([
    ("조건을 주소에서 읽는다", "서버가 <code>?q=</code>·<code>?page=</code>를 그대로 받아 그리면 <b>공유한 링크가 같은 화면</b>이 됩니다."),
    ("허용 목록으로", "<code>sort</code>·<code>f</code> 값을 그대로 질의에 넣지 않습니다 — <a href=\"table.html\">데이터 테이블</a>과 같은 주입 문제입니다."),
    ("같은 값의 순서", "순서가 요청마다 흔들리면 <b>쪽을 넘길 때 같은 줄이 두 번</b> 나옵니다. ID 를 2차 정렬로 붙입니다."),
    ("건수는 비싸다", "<code>COUNT(*)</code>가 큰 표에서는 느립니다. <b>'100+ 건'</b>으로 적거나 커서 방식으로 바꿉니다."),
    ("빈 질의", "<code>?q=</code>가 비었을 때 전체를 돌려줄지 아무것도 안 줄지 <b>정해 둡니다</b>. 안 정하면 전체 조회가 터집니다."),
  ]),
  plat_lede="<b>돌아오는 길</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "주소 + 뒤로가기",
     scr(qbox('모란') + res([MARK + '상회']), "112px"),
     "주소에 담으면 공유·새로고침·뒤로가기가 한꺼번에 됩니다. <b>웹의 가장 큰 장점</b>입니다."),
    ("iOS", "화면 스택",
     '''              <div class="phone" role="img" aria-label="iOS 결과 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px;color:var(--accent)">‹ 검색</span>
                <div style="position:absolute;left:4px;right:4px;top:28px;display:grid;gap:3px"><span style="height:7px;background:var(--line);border-radius:2px"></span><span style="height:7px;background:var(--line);border-radius:2px"></span></div></div></div>''',
     "앞 화면이 <b>통째로 살아 있어</b> 복원이 공짜입니다. 대신 공유할 주소가 없어 딥링크를 따로 만듭니다."),
    ("안드로이드", "백 스택",
     '''              <div class="phone" role="img" aria-label="안드로이드 결과 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px">← 모란</span>
                <div style="position:absolute;left:4px;right:4px;top:28px;display:grid;gap:3px"><span style="height:7px;background:var(--line);border-radius:2px"></span><span style="height:7px;background:var(--line);border-radius:2px"></span></div></div></div>''',
     "같은 방식이지만 <b>프로세스가 죽었다 살아날 수</b> 있어, 상태를 따로 저장해 두는 코드가 필요합니다."),
  ]),
  plat_note="\"목록에서 들어갔다 나오면 맨 위로 가요\"는 기획서에 안 적혀 있지만 <b>반드시 나오는</b> 민원입니다. 단일 페이지 앱(SPA)으로 만들면 브라우저가 해 주던 복원이 사라지기 때문입니다. 목록 화면을 잡을 때 <b>'돌아왔을 때'</b>를 한 줄 적어 두면, 나중에 급하게 붙이는 것보다 훨씬 싸게 끝납니다.",
  siblings=siblings("searchresults"),
  related='''        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
