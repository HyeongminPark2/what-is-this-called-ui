# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def tb(head, body, w="180px", extra=""):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);'
            'border-radius:6px;overflow:hidden;background:var(--surface);' + extra + '">'
            '<div style="display:flex;background:var(--bg);padding:5px 8px;font-size:9.5px;font-weight:700;color:var(--fg-muted)">'
            + head + '</div>' + body + '</div>')

def row(cells, sel=False):
    return ('<div style="display:flex;padding:5px 8px;font-size:10.5px;border-top:1px solid var(--line);'
            + ('background:var(--accent-soft);' if sel else '') + '">' + cells + '</div>')

HEAD = '<span style="flex:1">가맹점</span><span style="width:62px;text-align:right">매출</span>'
def cells(n, a):
    return '<span style="flex:1;min-width:0">' + n + '</span><span style="width:62px;text-align:right;font-variant-numeric:tabular-nums">' + a + '</span>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:240px">
                   <div style="border:1px solid var(--line);border-radius:7px;overflow:hidden;background:var(--surface)">
                    <div style="display:flex;background:var(--bg);padding:6px 9px;font-size:10px;font-weight:700;color:var(--fg-muted)"><span style="flex:1">가맹점</span><span style="width:70px;text-align:right">매출 ▼</span></div>
                    <div style="display:flex;padding:6px 9px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">한빛아웃도어</span><span style="width:70px;text-align:right;font-variant-numeric:tabular-nums">9,827,500</span></div>
                    <div style="display:flex;padding:6px 9px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">모란상회</span><span style="width:70px;text-align:right;font-variant-numeric:tabular-nums">1,284,000</span></div>
                   </div>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">thead th { position: sticky; top: 0 }</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-sort="descending"   — 무엇으로 정렬했나</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">숫자는 오른쪽 + tabular-nums</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">첫 열 고정 — 누구 줄인지 안 잊게</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">?sort=amount&dir=desc&page=2</div>
                </div>
              </div>'''

D = dict(
  slug="table", ko="데이터 테이블", en="Data table",
  desc="표의 정렬·고정 열·숫자 정렬과 상태를 주소에 담는 일까지, 관리 도구의 중심 화면을 다루는 항목.",
  lede="여러 값을 <b>세로로 견주라고</b> 만든 화면. 관리 도구의 절반은 이것입니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>열 이름을 눌러 정렬해 보세요. <b>무엇으로 어느 방향인지</b>가 화살표와
          <code>aria-sort</code>로 같이 표시되고, 아래 오른쪽에 <b>주소에 담긴 모습</b>이 나옵니다.<br>
          <b>줄바꿈 허용</b>을 켜면 줄 높이가 제각각이 되어 세로로 훑기가 어려워집니다.
          <b>첫 열 고정</b>을 끄고 가로로 밀면 <b>누구 줄인지</b>를 잃어버립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "데이터 테이블, 표, 그리드, 목록 화면"),
    ("영어", "data table, data grid, table view"),
    ("같이 쓰는 말",
     "열 이름 줄이 <b>헤더</b>(thead), 값 줄이 <b>행</b>(row)입니다. "
     "정렬·필터·쪽 넘김이 붙은 것을 <b>데이터 그리드</b>라 부르기도 합니다. "
     "열을 고정하는 것은 <b>프리즈</b>(freeze · pinned column), "
     "열 너비를 끌어 바꾸는 것은 <b>리사이즈</b>입니다."),
    ("자주 잘못 부름",
     "<b>그리드</b> — CSS 의 <a href=\"../items/grid.html\">레이아웃 그리드</a>와 다릅니다. 이쪽은 <b>데이터</b>입니다.<br>"
     "<b>리스트</b> — 리스트는 자유로운 세 자리, 표는 <b>열이 정해져</b> 있습니다.<br>"
     "<b>엑셀</b> — 표가 곧 편집 가능한 시트는 아닙니다. <b>읽기용인지 편집용인지</b>부터 정합니다."),
  ]),
  axes=ax("데이터 테이블"),
  oneline="표의 일은 <b>세로로 견주는 것</b>입니다. 줄 높이가 제각각이거나 숫자가 어긋나면 이미 표의 일을 못 하고 있습니다.",
  s4_title="상태", s4_hint="건수와 폭에 따라 달라진다",
  states=states([
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000'))),
     "기본", "열 이름 + 행. <b>숫자는 오른쪽</b>에 자릿수를 맞춘다"),
    (tb('<span style="flex:1">가맹점</span><span style="width:62px;text-align:right;color:var(--accent)">매출 ▼</span>',
        row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000'))),
     "정렬됨", "<b>무엇으로 어느 방향인지</b>가 보여야 한다"),
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500'), True) + row(cells('모란상회', '1,284,000'))),
     "줄 선택", "고른 줄은 바탕이 바뀐다. <a href=\"bulk.html\">일괄 선택</a>으로 이어진다"),
    (tb(HEAD, '<div style="padding:7px 8px;border-top:1px solid var(--line);display:grid;gap:4px">'
        '<span class="skl" style="height:8px;width:70%"></span><span class="skl" style="height:8px;width:55%"></span></div>'),
     "로딩", "<b>같은 줄 높이</b>의 뼈대. 다르면 들어올 때 덜컥거린다"),
    (tb(HEAD, '<div style="padding:16px 8px;border-top:1px solid var(--line);text-align:center;font-size:10px;color:var(--fg-muted)">조건에 맞는 것이 없습니다</div>'),
     "빈 결과", "<b>조건을 지울 길</b>을 함께 준다"),
    (tb('<span style="flex:1">가맹점</span><span style="width:62px;text-align:right">매출</span><span style="width:48px;text-align:right">수수료</span><span style="width:40px">상태</span>',
        row(cells('한빛', '9,827,500') + '<span style="width:48px;text-align:right">294,825</span><span style="width:40px">승인</span>'),
        "180px", "overflow:hidden"),
     "열이 많을 때", "가로로 민다. <b>첫 열은 고정</b>해 누구 줄인지 안 잊게"),
  ]),
  anat=ANAT,
  pins=pins([
    ("표", "table", "<code>&lt;table&gt;</code>이라야 '표, 5열 20행'으로 읽힌다. div 로 만들면 안 읽힌다"),
    ("붙박이 열 이름", "sticky thead", "굴려도 <b>무슨 열인지</b> 안 잊게. <code>&lt;th&gt;</code>에 건다"),
    ("정렬 표시", "aria-sort", "화살표와 함께. <b>눌렀는데 표시가 없으면</b> 뭘 눌렀는지 모른다"),
    ("숫자 열", "오른쪽 + tabular-nums", "자릿수가 세로로 맞아야 <b>크기를 눈으로</b> 견줄 수 있다"),
    ("고정 열", "sticky left", "열이 많을 때. 이름 열을 왼쪽에 붙여 둔다"),
    ("주소에 담기", "?sort=&dir=&page=", "<b>새로고침·공유·뒤로가기</b>가 되려면 필요하다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          표를 <code>&lt;div&gt;</code>로 만들면 <b>스크린 리더가 표로 읽지 못합니다.</b>
          '3열 5행'도, '매출 열, 1,284,000'도 안 나오고 글자만 줄줄 읽힙니다.
          CSS 그리드로 모양을 내더라도 <b>마크업은 <code>&lt;table&gt;</code></b>로 두는 것이
          거의 늘 맞습니다 — <code>display: grid</code>를 <code>&lt;table&gt;</code>에 걸 수도 있습니다.</p>''',
  do=ul([
    "<b>같은 모양의 건</b>이 여럿이고 <b>여러 값을 견줘야</b> 할 때",
    "정렬·필터·쪽 넘김이 필요할 때",
    "숫자가 많은 화면 — 세로로 맞춰 봐야 할 때",
  ]),
  dont=ul([
    "<b>건마다 보여 줄 것이 다를</b> 때 → <a href=\"../items/card.html\">카드</a>나 <a href=\"../items/listitem.html\">리스트</a>",
    "폰에서 열 다섯 개를 그대로 — <b>가로 스크롤</b>이거나 카드로 바뀌어야 합니다",
    "배치하려고 <code>&lt;table&gt;</code>을 쓰는 것",
    "모든 열에 정렬을 거는 것 — <b>정렬이 뜻 있는 열</b>에만",
  ]),
  instead='건마다 내용이 다르면 <a href="../items/card.html">카드</a>, 한 줄이면 <a href="../items/listitem.html">리스트 아이템</a>, 아주 길면 <a href="virtual.html">가상 스크롤</a>.',
  cases=cases([
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000')) + row(cells('새벽상사', '11,100')), "190px"),
     "정산 목록", "관리 도구의 기본 화면"),
    (tb('<span style="width:20px"></span><span style="flex:1">가맹점</span><span style="width:52px;text-align:right">매출</span>',
        row('<span style="width:20px">☑</span>' + '<span style="flex:1">한빛아웃도어</span><span style="width:52px;text-align:right;font-variant-numeric:tabular-nums">9,827,500</span>', True) +
        row('<span style="width:20px">☐</span>' + '<span style="flex:1">모란상회</span><span style="width:52px;text-align:right;font-variant-numeric:tabular-nums">1,284,000</span>'), "190px"),
     "선택이 붙은 표", "맨 앞에 체크박스. <a href=\"bulk.html\">일괄 선택</a>으로 이어진다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:8px;display:grid;gap:5px">
                <span style="font-size:10.5px;font-weight:700">한빛아웃도어</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">매출 9,827,500 · 수수료 294,825</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">11월 1일 ~ 7일 · 승인됨</span>
              </div>''',
     "폰에서는 카드로", "열 다섯 개를 그대로 밀기보다 <b>한 건을 카드로</b> 바꾸는 쪽이 낫다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 표의 계약서",
  code_lede="<code>&lt;table&gt;</code>을 쓰고, 정렬 상태를 <code>aria-sort</code>와 주소에 함께 적습니다.",
  code='''&lt;<span class="t">table</span>&gt;
  &lt;<span class="t">caption</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;정산 목록, 20건 중 1~5&lt;/<span class="t">caption</span>&gt;
  &lt;<span class="t">thead</span>&gt;&lt;<span class="t">tr</span>&gt;
    &lt;<span class="t">th</span> <span class="a">scope</span>=<span class="s">"col"</span>&gt;가맹점&lt;/<span class="t">th</span>&gt;
    &lt;<span class="t">th</span> <span class="a">scope</span>=<span class="s">"col"</span> <span class="a">aria-sort</span>=<span class="s">"descending"</span>&gt;
      &lt;<span class="t">button</span>&gt;매출 ▼&lt;/<span class="t">button</span>&gt;
    &lt;/<span class="t">th</span>&gt;
  &lt;/<span class="t">tr</span>&gt;&lt;/<span class="t">thead</span>&gt;
  &lt;<span class="t">tbody</span>&gt;
    &lt;<span class="t">tr</span>&gt;&lt;<span class="t">th</span> <span class="a">scope</span>=<span class="s">"row"</span>&gt;모란상회&lt;/<span class="t">th</span>&gt;&lt;<span class="t">td</span>&gt;1,284,000&lt;/<span class="t">td</span>&gt;&lt;/<span class="t">tr</span>&gt;
  &lt;/<span class="t">tbody</span>&gt;
&lt;/<span class="t">table</span>&gt;

<span class="t">thead</span> <span class="t">th</span> { <span class="a">position</span>: sticky; <span class="a">top</span>: <span class="a">0</span>; <span class="a">z-index</span>: <span class="a">2</span>; }
<span class="t">td</span>.num { <span class="a">text-align</span>: right; <span class="a">font-variant-numeric</span>: tabular-nums; }''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "정렬 버튼과 줄 안의 누를 것들로. <b>셀마다 멈추지는 않는다</b>"),
    ("<code>scope</code>를 적는다", "<code>col</code>·<code>row</code>. 스크린 리더가 '매출 열, 1,284,000'으로 읽는다"),
    ("<code>aria-sort</code>", "정렬한 열 <b>하나</b>에만. 화살표와 함께 쓴다"),
    ("<code>&lt;caption&gt;</code>", "표가 무엇인지 한 줄. 보이지 않게 둬도 된다"),
    ("정렬은 <code>&lt;button&gt;</code>으로", "<code>&lt;th&gt;</code>에 onclick 을 걸면 키보드로 못 누른다"),
    ("줄 높이를 맞춘다", "말줄임으로 한 줄 고정. <a href=\"virtual.html\">가상 스크롤</a>의 전제이기도 하다"),
  ]),
  backend=rows([
    ("정렬은 서버에서", "화면에 있는 20건만 정렬하면 <b>쪽을 넘길 때마다 순서가 깨집니다.</b> 전체를 기준으로 정렬해 그 쪽을 잘라 보내야 합니다."),
    ("정렬 기준을 열어 두지 않는다", "<code>?sort=</code>를 그대로 SQL 에 넣으면 주입이 됩니다. <b>허용 목록</b>으로 받습니다."),
    ("같은 값의 순서", "매출이 같은 두 건의 순서가 요청마다 바뀌면 <b>쪽을 넘길 때 같은 줄이 두 번</b> 나옵니다. ID 를 2차 정렬로 붙입니다."),
    ("전체 건수", "'20건 중 1~5'를 보여 주려면 <code>COUNT(*)</code>가 필요한데 비쌉니다. 큰 표에서는 <b>'100+ 건'</b>으로 적거나 커서 방식으로 바꿉니다."),
    ("열 많은 표", "열이 늘수록 응답도 커집니다. <b>보이는 열만</b> 요청하는 방식(필드 선택)을 두면 목록이 가벼워집니다."),
  ]),
  plat_lede="표는 <b>PC 의 화면</b>입니다. 두 OS 는 대개 다른 모양으로 바꿉니다.",
  plats=plats([
    ("웹", "&lt;table&gt;",
     tb(HEAD, row(cells('모란상회', '1,284,000')), "120px"),
     "표준 태그가 있고 스크린 리더가 표로 읽습니다. <b>가로 스크롤</b>을 그대로 쓰는 것도 웹의 방식입니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">모란상회 · 1,284,000</div>
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">한빛 · 9,827,500</div>
                </div></div></div>''',
     "표라는 부품이 없습니다. 보통 <b>리스트</b>로 바꾸고, 아이패드에서만 표 비슷하게 만듭니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">모란상회</div>
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">한빛아웃도어</div>
                </div></div></div>''',
     "M3 에 데이터 테이블이 있지만 <b>큰 화면 전용</b>입니다. 폰에서는 리스트로 바꾸라고 권합니다."),
  ]),
  plat_note="\"표로 보여 주세요\"가 폰에서는 거의 늘 <b>리스트나 카드로 바뀝니다.</b> 열이 셋을 넘으면 폰 화면에 안 들어가기 때문입니다. 같은 데이터를 <b>PC 는 표, 폰은 카드</b>로 두 벌 만드는 것이 보통이고, 그 결정을 먼저 해 두면 서로 다른 것을 만들지 않습니다.",
  siblings=siblings("table"),
  related='''        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
