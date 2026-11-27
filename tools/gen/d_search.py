# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(inner, w="170px", extra=""):
    return ('              <div style="width:100%;max-width:' + w + ';' + extra + '">' + inner + '</div>')

def field(txt, ph=False, icon="🔍"):
    return ('<div style="display:flex;align-items:center;gap:5px;border:1px solid var(--line);border-radius:999px;'
            'background:var(--surface);padding:4px 10px"><span aria-hidden="true" style="font-size:9px">' + icon + '</span>'
            '<span style="flex:1;min-width:0;font-size:10.5px;' + ('color:var(--fg-muted)' if ph else '') + '">' + txt + '</span></div>')

def res(items):
    return ('<div style="margin-top:4px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">'
            + ''.join('<div style="padding:4px 8px;font-size:10px;border-top:1px solid var(--line)">' + i + '</div>' for i in items)
            + '</div>')

MARK = '<b style="background:var(--warn-soft);border-radius:2px;padding:0 1px">모란</b>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:220px">''' + field('모란').strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">입력이 멈추고 300ms 뒤에야 보냄</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">늦게 온 '모'의 답이 '모란'의 답을 덮어씀</div>
                  <div class="pin-out" data-pin="4" style="max-width:220px">''' + res(['<b style="background:var(--warn-soft)">모란</b>상회', '<b style="background:var(--warn-soft)">모란</b>동 지점']).strip() + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">role="status"로 "3건 찾음" 알림</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">?q=%EB%AA%A8%EB%9E%80</div>
                </div>
              </div>'''

D = dict(
  slug="search", ko="검색", en="Search",
  desc="검색 입력칸과 결과 화면을 디바운스, 늦게 온 응답 버리기, 일치 글자 강조, 빈 결과 문구까지 다루는 항목입니다.",
  lede="검색은 사용자가 <b>글자를 자유롭게 입력해</b> 원하는 것을 찾는 장치입니다. 입력칸을 만드는 일보다 <b>요청을 언제 보내고 어떤 응답을 버릴지</b> 정하는 일이 더 까다롭습니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>글자를 빠르게 쳐 보세요. <b>디바운스</b>를 끄면 글자를 칠 때마다 요청이 나갑니다.
          <b>늦은 응답 버리기</b>를 끄면 먼저 보낸 요청의 응답이 늦게 도착해 <b>지금 입력한 글자와 다른 결과</b>가 남는데,
          입력칸에는 '모란'이 적혀 있는데 목록은 '모'로 찾은 결과인 상태입니다. 실제 서비스에서 가장 자주 생기는 검색 버그입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "검색, 검색창, 찾기, 자동완성"),
    ("영어", "search, search field, typeahead, autocomplete"),
    ("같이 쓰는 말",
     "글자를 치는 대로 입력칸 아래에 후보가 뜨는 것은 <b>타입어헤드</b>(typeahead)·<b>자동완성</b>이라고 하고, "
     "결과 페이지로 넘어가는 것은 그냥 <b>검색</b>이라고 합니다. "
     "입력이 멈출 때까지 기다렸다가 요청을 보내는 것은 <b>디바운스</b>(debounce), "
     "일정한 간격으로만 요청을 보내는 것은 <b>스로틀</b>(throttle)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>필터</b> — <a href=\"filter.html\">필터</a>는 정해진 값 가운데서 고르는 방식이고, 검색은 <b>글자를 직접 입력하는</b> 방식입니다.<br>"
     "<b>콤보박스</b> — <a href=\"../items/select.html\">셀렉트</a>에 글자 입력이 붙은 콤보박스는 값 <b>하나를 고르는</b> 입력이고, 검색은 입력한 글자에 따라 목록을 바꿉니다.<br>"
     "<b>명령 팔레트</b> — <kbd>Ctrl</kbd>+<kbd>K</kbd>로 여는 창은 데이터 검색이 아니라 <b>기능을 찾는</b> 도구입니다."),
  ]),
  axes=ax("검색"),
  oneline="검색에서 가장 중요한 일은 <b>지금 입력한 글자와 지금 보이는 결과를 서로 맞게 유지하는 것</b>입니다. 둘이 어긋나면 사용자는 화면의 결과가 어떤 글자로 찾은 것인지 알 수 없어서 결과를 믿지 못하게 됩니다.",
  s4_title="상태", s4_hint="여섯 가지 상태를 모두 만들어야 합니다",
  states=states([
    (box(field('가맹점 이름이나 번호', True)), "입력칸이 비었을 때", "<b>무엇으로 찾을 수 있는지</b> 알려 줍니다"),
    (box(field('모') + res(['<span class="skl" style="height:8px;width:60%;display:block"></span>', '<span class="skl" style="height:8px;width:45%;display:block"></span>'])),
     "결과를 찾는 중", "<b>이전 결과를 지우지 않습니다.</b> 지웠다가 새 결과를 그리면 화면이 깜빡입니다"),
    (box(field('모란') + res([MARK + '상회', MARK + '동 지점'])),
     "결과가 있을 때", "<b>일치한 글자를 강조</b>해서 각 결과가 왜 검색되었는지 보여 줍니다"),
    (box(field('모란닭강정') + '<div style="margin-top:4px;border:1px dashed var(--line);border-radius:6px;padding:10px 8px;text-align:center;font-size:9.5px;color:var(--fg-muted)">\'모란닭강정\'에 맞는 것이 없습니다<br><span style="color:var(--accent)">\'모란\'으로 다시 찾기</span></div>'),
     "맞는 결과가 없을 때", "<b>입력한 글자를 그대로 적고</b>, 다르게 찾아볼 방법을 제안합니다"),
    (box(field('모란') + '<div style="margin-top:4px;border:1px solid var(--danger);border-radius:6px;padding:8px;font-size:9.5px;color:var(--danger)">잠시 문제가 있었습니다 · <span style="text-decoration:underline">다시 시도</span></div>'),
     "요청이 실패했을 때", "요청이 실패했을 때는 빈 결과와 <b>다르게</b> 보여야 합니다"),
    (box(field('모란 ✕') + res(['최근: 모란상회', '최근: 한빛아웃도어'])),
     "최근 검색어를 보여 줄 때", "입력을 지우는 버튼(<b>✕</b>)과 <b>최근 검색어</b>를 함께 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("입력칸", "type=\"search\"", "돋보기와 ✕ 버튼을 함께 둡니다. <b>레이블</b>은 화면에서 숨기더라도 마크업에는 있어야 합니다"),
    ("디바운스", "300ms", "입력이 멈춘 뒤에 요청을 보냅니다. 글자마다 보내면 열 글자를 칠 때 요청이 열 번 나갑니다"),
    ("늦은 응답 버리기", "순번 비교", "<b>지금 입력한 글자에 대한 응답이 아니면 버립니다.</b> 버리지 않으면 이전 글자의 결과가 섞여 보입니다"),
    ("결과", "listbox / list", "일치한 글자를 <b>굵게</b> 표시해서 왜 검색되었는지 보여 줍니다"),
    ("건수 알림", "role=status", "화면을 보지 않고 스크린 리더로 듣는 사람에게 <b>결과가 바뀐 것</b>을 알립니다"),
    ("주소", "?q=", "결과 화면이면 검색어를 주소에 담고, 자동완성이면 담지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          검색을 구현할 때 손이 많이 가는 부분이 <b>늦게 온 응답을 버리는 일</b>입니다.
          '모'와 '모란'을 연달아 보내면 네트워크 사정에 따라 <b>'모'의 응답이 나중에</b> 도착할 수 있고,
          그러면 입력칸에는 '모란'이 적혀 있는데 목록은 '모'로 찾은 결과가 됩니다.
          이를 막으려면 요청마다 번호를 붙여 <b>마지막 번호의 응답만</b> 반영하거나,
          <code>AbortController</code>로 이전 요청을 취소해야 합니다.</p>''',
  do=ul([
    "이름, 번호, 메모처럼 찾을 값이 <b>정해져 있지 않을</b> 때",
    "목록이 길어서 <b>눈으로 훑어서는 찾기 어려울</b> 때",
    "찾는 대상이 무엇인지 <b>사용자가 이미 알고</b> 있을 때",
  ]),
  dont=ul([
    "고를 값이 <b>정해져 있을</b> 때. <a href=\"filter.html\">필터</a>가 낫습니다",
    "항목이 열 개 남짓일 때. 검색칸을 두지 말고 <b>전부 보여 줍니다</b>",
    "글자를 칠 때마다 요청을 보낼 때. <b>디바운스</b>를 겁니다",
    "찾는 동안 이전 결과를 지울 때. 화면만 깜빡이고 얻는 것이 없습니다",
  ]),
  instead='고를 값이 미리 정해져 있으면 <a href="filter.html">필터</a>를 쓰고, 값 하나를 골라 넣는 입력이면 <a href="../items/select.html">셀렉트</a>가 맞습니다. 데이터가 아니라 기능을 찾게 하려면 명령 팔레트를 둡니다.',
  cases=cases([
    (box(field('모란') + res([MARK + '상회', MARK + '동 지점']), "150px"),
     "자동완성으로 후보 하나 고르기", "글자를 치는 대로 후보가 뜨고, <b>후보를 하나 고르면 끝납니다</b>"),
    (box(field('모란') + '<div style="margin-top:4px;font-size:9.5px;color:var(--fg-muted)">3건 · 관련도순</div>' + res([MARK + '상회 · 승인됨']), "150px"),
     "결과 목록 화면 보여 주기", "<b>결과 건수와 정렬 순서</b>를 적고, 검색어를 주소에 담습니다"),
    (box('<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:6px"><div style="font-size:9px;color:var(--fg-muted);margin-bottom:3px">⌘K</div><div style="font-size:10px">정산 내보내기</div><div style="font-size:10px;color:var(--fg-muted)">가맹점 추가</div></div>', "150px"),
     "명령 팔레트로 기능 찾기", "데이터가 아니라 <b>기능</b>을 찾는 도구라서 데이터 검색과는 성격이 다릅니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="검색을 만들 때 꼭 갖출 것",
  code_lede="입력칸에는 레이블을, 결과 개수에는 <code>role=\"status\"</code>를 답니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"q"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;가맹점 검색&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"q"</span> <span class="a">type</span>=<span class="s">"search"</span> <span class="a">placeholder</span>=<span class="s">"가맹점 이름이나 번호"</span>&gt;

&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;3건 찾음&lt;/<span class="t">p</span>&gt;
&lt;<span class="t">ul</span>&gt;&lt;<span class="t">li</span>&gt;&lt;<span class="t">mark</span>&gt;모란&lt;/<span class="t">mark</span>&gt;상회&lt;/<span class="t">li</span>&gt;&lt;/<span class="t">ul</span>&gt;

<span class="c">// 늦게 온 답을 버린다</span>
<span class="k">let</span> seq = <span class="a">0</span>;
<span class="k">async function</span> run(q) {
  <span class="k">const</span> my = ++seq;
  <span class="k">const</span> r = <span class="k">await</span> fetch(<span class="s">`/api/search?q=${</span>encodeURIComponent(q)<span class="s">}`</span>);
  <span class="k">if</span> (my !== seq) <span class="k">return</span>;   <span class="c">// 더 나중에 보낸 요청이 있으면 버린다</span>
  render(<span class="k">await</span> r.json());
}''',
  keys=kbd([
    ("<code>type=\"search\"</code>", "폰 키보드의 입력 키가 '검색'으로 바뀌고, 브라우저가 ✕ 버튼을 붙여 줍니다"),
    ("입력칸에 레이블 붙이기", "<b>플레이스홀더는 레이블을 대신하지 못합니다.</b> 글자를 치면 사라지기 때문에 무엇을 입력하는 칸인지 잊게 됩니다"),
    ("<kbd>Esc</kbd>", "후보 목록을 닫거나 입력한 글자를 지웁니다. 두 번 누르면 칸을 비웁니다"),
    ("<kbd>↑</kbd><kbd>↓</kbd>", "후보가 떠 있으면 후보 사이를 오르내립니다. <code>aria-activedescendant</code>를 써서 <b>포커스는 입력칸에 둔 채</b> 움직입니다"),
    ("<code>role=\"status\"</code>", "'3건 찾음'처럼 결과 개수를 알립니다. 목록만 바뀌면 화면을 보지 않는 사람은 결과가 바뀐 것을 알 수 없습니다"),
    ("<code>&lt;mark&gt;</code>", "일치한 글자를 표시합니다. 색만으로 구분하지 않습니다"),
  ]),
  backend=rows([
    ("<code>LIKE '%모란%'</code>가 색인을 못 쓰는 문제", "검색어 앞에 <code>%</code>가 붙으면 색인을 쓰지 못해 테이블 전체를 훑습니다. 그래서 건수가 늘어나는 만큼 검색도 느려집니다."),
    ("한국어 검색어를 쪼개 색인하는 방법", "'모란상회'를 '모란'으로 찾으려면 글자를 <b>형태소</b>나 <b>n-gram</b> 단위로 쪼개 색인해야 합니다. 띄어쓰기를 기준으로 쪼개면 '모란상회'가 한 덩어리로 색인되어 '모란'으로는 찾을 수 없습니다."),
    ("너무 짧은 검색어 막기", "검색어가 한두 자이면 거의 모든 데이터가 결과로 나옵니다. 그래서 <b>두 자 이상</b>일 때부터 요청을 보내거나, 서버에서 짧은 검색어를 거릅니다."),
    ("같은 검색 요청이 몰릴 때", "디바운스를 걸지 않으면 한 사람이 10자를 칠 때 요청이 10번 옵니다. 같은 검색어 요청이 몰릴 때를 대비해 <b>서버에도</b> 짧은 캐시를 둡니다."),
    ("관련도순으로 순위 매기기", "'관련도순'으로 정렬하려면 따로 할 일이 많습니다. 검색어가 어느 필드의 어디에서 일치했는지 따져 점수를 매겨야 하는데, 이 단계부터는 데이터베이스만으로 버거워 검색 엔진이 필요해집니다."),
  ]),
  plat_lede="세 플랫폼 모두 검색칸을 <b>둥근 입력칸에 돋보기를 붙인 모양</b>으로 만듭니다.",
  plats=plats([
    ("웹", "input[type=search]",
     box(field('모란'), "120px"),
     "검색 전용 입력 타입이 있고, 브라우저가 ✕ 버튼을 그려 줍니다. 검색어를 <b>주소에 담아</b> 공유할 수 있는 것은 웹의 강점입니다."),
    ("iOS", "UISearchBar",
     '''              <div class="phone" role="img" aria-label="iOS 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:28px;background:var(--bg);border-radius:999px;padding:3px 6px;font-size:6px;color:var(--fg-muted)">🔍 검색</div></div></div>''',
     "검색칸을 목록 맨 위에 숨겨 두고 <b>목록을 끌어내리면 나타나게</b> 하는 것이 관례입니다. 검색칸 오른쪽에는 취소 버튼이 붙습니다."),
    ("안드로이드", "SearchBar / M3",
     '''              <div class="phone" role="img" aria-label="Material 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:28px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:3px 6px;font-size:6px;color:var(--fg-muted)">🔍 검색</div></div></div>''',
     "M3는 검색창을 누르면 <b>검색창이 그대로 펼쳐져 전체 화면</b>이 되는 전환을 표준으로 둡니다."),
  ]),
  plat_note="\"검색 넣어 주세요\"라는 요청을 받으면 <b>자동완성</b>을 말하는지 <b>결과 화면</b>을 말하는지부터 가려야 합니다. 자동완성은 후보를 고르면 끝나므로 검색어를 주소에 담지 않고, 결과 화면은 공유와 뒤로가기가 되어야 하므로 주소에 담습니다. 두 방식을 섞어 만들면 뒤로가기를 눌렀을 때 돌아갈 화면이 없어집니다.",
  siblings=siblings("search"),
  related='''        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
