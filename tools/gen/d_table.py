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
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-sort="descending"   정렬 기준을 알림</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">숫자는 오른쪽 정렬과 tabular-nums</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">첫 열을 고정해 누구 줄인지 보이게</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">?sort=amount&dir=desc&page=2</div>
                </div>
              </div>'''

D = dict(
  slug="table", ko="데이터 테이블", en="Data table",
  desc="관리 도구의 중심 화면인 데이터 테이블을 정렬과 고정 열, 숫자 정렬부터 상태를 주소에 담는 일까지 다루는 항목입니다.",
  lede="데이터 테이블은 같은 모양의 건을 줄지어 놓고 여러 값을 <b>세로로 견주어 보도록</b> 만든 화면입니다. 관리 도구 화면의 절반 정도가 이런 표입니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>열 이름을 눌러 정렬해 보세요. <b>어느 열을 기준으로 어느 방향으로</b> 정렬했는지가 화살표와
          <code>aria-sort</code>로 함께 표시되고, 아래 오른쪽에는 정렬 상태가 <b>주소에 담긴 모습</b>이 나옵니다.<br>
          <b>줄바꿈 허용</b>을 켜면 줄마다 높이가 달라져서 값을 세로로 훑어보기가 어려워집니다.
          <b>첫 열 고정</b>을 끄고 표를 가로로 밀면 이름 열이 화면 밖으로 나가서 <b>어느 가맹점의 줄인지</b> 알 수 없게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "데이터 테이블, 표, 그리드, 목록 화면"),
    ("영어", "data table, data grid, table view"),
    ("같이 쓰는 말",
     "열 이름이 적힌 줄은 <b>헤더</b>(thead), 값이 적힌 줄은 <b>행</b>(row)이라고 부릅니다. "
     "정렬과 필터, 쪽 넘김 기능까지 붙은 표는 <b>데이터 그리드</b>라고 부르기도 합니다. "
     "열을 제자리에 고정하는 기능은 <b>프리즈</b>(freeze · pinned column), "
     "열 너비를 끌어서 바꾸는 기능은 <b>리사이즈</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>그리드</b> — CSS의 <a href=\"../items/grid.html\">레이아웃 그리드</a>는 화면 배치를 나누는 틀이고, 데이터 그리드는 <b>데이터</b>를 보여 주는 표라서 서로 다릅니다.<br>"
     "<b>리스트</b> — 리스트 아이템은 앞·가운데·뒤 세 자리에 내용을 자유롭게 놓지만, 표는 <b>열이 정해져</b> 있어서 모든 줄이 같은 칸을 씁니다.<br>"
     "<b>엑셀</b> — 표라고 해서 모두 엑셀처럼 칸을 고칠 수 있는 시트는 아닙니다. 만들기 전에 <b>읽기용인지 편집용인지</b>부터 정합니다."),
  ]),
  axes=ax("데이터 테이블"),
  oneline="표는 값을 <b>세로로 견주어 보도록</b> 만든 화면입니다. 그래서 줄 높이가 제각각이거나 숫자 자릿수가 어긋나 있으면 값을 견주기 어려워져 표를 쓴 의미가 줄어듭니다.",
  s4_title="상태", s4_hint="건수와 화면 폭에 따라 달라지는 모습",
  states=states([
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000'))),
     "평소 상태", "열 이름 줄 아래에 행이 이어집니다. <b>숫자는 오른쪽</b>으로 붙여 자릿수를 맞춥니다"),
    (tb('<span style="flex:1">가맹점</span><span style="width:62px;text-align:right;color:var(--accent)">매출 ▼</span>',
        row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000'))),
     "열을 눌러 정렬했을 때", "<b>어느 열을 기준으로 어느 방향으로</b> 정렬했는지 보여야 합니다"),
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500'), True) + row(cells('모란상회', '1,284,000'))),
     "줄을 골랐을 때", "고른 줄은 바탕색이 바뀝니다. 여러 줄을 골라 한꺼번에 처리하는 <a href=\"bulk.html\">일괄 선택</a>으로 이어집니다"),
    (tb(HEAD, '<div style="padding:7px 8px;border-top:1px solid var(--line);display:grid;gap:4px">'
        '<span class="skl" style="height:8px;width:70%"></span><span class="skl" style="height:8px;width:55%"></span></div>'),
     "데이터를 불러오는 중", "실제 줄과 <b>같은 높이</b>로 뼈대를 그립니다. 높이가 다르면 데이터가 들어오는 순간 줄 위치가 밀립니다"),
    (tb(HEAD, '<div style="padding:16px 8px;border-top:1px solid var(--line);text-align:center;font-size:10px;color:var(--fg-muted)">조건에 맞는 것이 없습니다</div>'),
     "조건에 맞는 결과가 없을 때", "결과가 없다는 안내와 함께 <b>조건을 지우는 방법</b>을 보여 줍니다"),
    (tb('<span style="flex:1">가맹점</span><span style="width:62px;text-align:right">매출</span><span style="width:48px;text-align:right">수수료</span><span style="width:40px">상태</span>',
        row(cells('한빛', '9,827,500') + '<span style="width:48px;text-align:right">294,825</span><span style="width:40px">승인</span>'),
        "180px", "overflow:hidden"),
     "열이 많을 때", "표를 가로로 밀어서 봅니다. <b>첫 열을 고정</b>해 두면 밀어도 어느 가맹점의 줄인지 알 수 있습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("표", "table", "<code>&lt;table&gt;</code>로 만들어야 스크린 리더가 '표, 5열 20행'으로 읽습니다. div로 만들면 표로 읽지 못합니다"),
    ("붙박이 열 이름", "sticky thead", "표를 아래로 스크롤해도 <b>무슨 열인지</b> 알 수 있도록 열 이름 줄을 위에 붙여 둡니다. <code>&lt;th&gt;</code>에 겁니다"),
    ("정렬 표시", "aria-sort", "화살표와 함께 씁니다. 열 이름을 <b>눌렀는데 표시가 없으면</b> 무엇을 기준으로 정렬했는지 알 수 없습니다"),
    ("숫자 열", "오른쪽 + tabular-nums", "자릿수가 세로로 맞아야 <b>값의 크기를 눈으로</b> 견줄 수 있습니다"),
    ("고정 열", "sticky left", "열이 많을 때 씁니다. 이름 열을 왼쪽에 붙여 두어 가로로 밀어도 보이게 합니다"),
    ("주소에 담기", "?sort=&dir=&page=", "정렬 기준과 쪽 번호를 주소에 담아야 <b>새로고침·공유·뒤로가기</b>를 해도 같은 화면이 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          표를 <code>&lt;div&gt;</code>로 만들면 <b>스크린 리더가 표로 읽지 못합니다.</b>
          '3열 5행' 같은 안내도, '매출 열, 1,284,000'처럼 열 이름을 붙여 읽는 일도 없이 칸의 글자만 차례로 읽습니다.
          그래서 CSS 그리드로 모양을 내더라도 <b>마크업은 <code>&lt;table&gt;</code></b>로 두는 편이
          거의 언제나 맞습니다. <code>&lt;table&gt;</code>에 <code>display: grid</code>를 거는 방법도 있습니다.</p>''',
  do=ul([
    "<b>같은 모양의 건</b>이 여럿이고 <b>여러 값을 견줘야</b> 할 때",
    "정렬·필터·쪽 넘김이 필요할 때",
    "숫자가 많아서 세로로 맞춰 봐야 하는 화면일 때",
  ]),
  dont=ul([
    "<b>건마다 보여 줄 내용이 다를</b> 때. <a href=\"../items/card.html\">카드</a>나 <a href=\"../items/listitem.html\">리스트</a>가 맞습니다",
    "폰에서 열 다섯 개를 그대로 보여 줄 때. <b>가로 스크롤</b>을 두거나 카드로 바꿔야 합니다",
    "화면 배치를 잡으려고 <code>&lt;table&gt;</code>을 쓸 때",
    "모든 열에 정렬을 걸 때. 정렬은 <b>정렬해서 볼 뜻이 있는 열</b>에만 겁니다",
  ]),
  instead='건마다 보여 줄 내용이 다르면 <a href="../items/card.html">카드</a>를 쓰고, 한 건이 한 줄로 끝나면 <a href="../items/listitem.html">리스트 아이템</a>으로 충분합니다. 건수가 아주 많아 목록이 길어지면 <a href="virtual.html">가상 스크롤</a>을 함께 씁니다.',
  cases=cases([
    (tb(HEAD, row(cells('한빛아웃도어', '9,827,500')) + row(cells('모란상회', '1,284,000')) + row(cells('새벽상사', '11,100')), "190px"),
     "정산 목록 보여 주기", "관리 도구에서 가장 흔한 표 화면입니다"),
    (tb('<span style="width:20px"></span><span style="flex:1">가맹점</span><span style="width:52px;text-align:right">매출</span>',
        row('<span style="width:20px">☑</span>' + '<span style="flex:1">한빛아웃도어</span><span style="width:52px;text-align:right;font-variant-numeric:tabular-nums">9,827,500</span>', True) +
        row('<span style="width:20px">☐</span>' + '<span style="flex:1">모란상회</span><span style="width:52px;text-align:right;font-variant-numeric:tabular-nums">1,284,000</span>'), "190px"),
     "여러 줄을 골라 한꺼번에 처리하기", "줄 맨 앞에 체크박스를 두고, 고른 줄을 <a href=\"bulk.html\">일괄 선택</a>으로 한꺼번에 처리합니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:8px;display:grid;gap:5px">
                <span style="font-size:10.5px;font-weight:700">한빛아웃도어</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">매출 9,827,500 · 수수료 294,825</span>
                <span style="font-size:9.5px;color:var(--fg-muted)">11월 1일 ~ 7일 · 승인됨</span>
              </div>''',
     "폰에서 한 건을 카드 한 장으로 보여 주기", "폰에서는 열 다섯 개를 가로로 밀어 보게 하기보다 <b>한 건을 카드 한 장으로</b> 바꾸는 편이 읽기 쉽습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="표를 만들 때 꼭 갖출 것",
  code_lede="마크업은 <code>&lt;table&gt;</code>로 쓰고, 정렬 상태는 <code>aria-sort</code>와 주소 양쪽에 함께 적습니다.",
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
    ("<kbd>Tab</kbd>", "정렬 버튼과 줄 안의 누를 수 있는 것들로 옮겨 갑니다. <b>셀마다 멈추지는 않습니다</b>"),
    ("<code>scope</code> 속성 적기", "<code>col</code>·<code>row</code>를 적어 두면 스크린 리더가 '매출 열, 1,284,000'처럼 열 이름을 붙여 읽습니다"),
    ("<code>aria-sort</code>", "정렬 기준인 열 <b>하나</b>에만 달고, 화살표와 함께 씁니다"),
    ("<code>&lt;caption&gt;</code>", "표가 무엇인지 한 줄로 적습니다. 화면에는 보이지 않게 둬도 됩니다"),
    ("정렬 단추는 <code>&lt;button&gt;</code>으로 만들기", "<code>&lt;th&gt;</code>에 onclick을 걸면 키보드로 누를 수 없습니다"),
    ("모든 줄의 높이를 똑같이 맞추기", "긴 글자는 말줄임으로 잘라 한 줄로 고정합니다. 줄 높이가 같은 것은 <a href=\"virtual.html\">가상 스크롤</a>의 전제 조건이기도 합니다"),
  ]),
  backend=rows([
    ("정렬은 서버에서 하기", "화면에 받아 둔 20건만 정렬하면 <b>쪽을 넘길 때마다 순서가 이어지지 않습니다.</b> 서버가 전체 데이터를 기준으로 정렬한 뒤 해당 쪽만 잘라 보내야 합니다."),
    ("정렬 기준은 정해 둔 열 이름만 받기", "<code>?sort=</code> 값을 그대로 SQL에 넣으면 SQL 주입 공격을 당할 수 있습니다. 정렬할 수 있는 열 이름을 <b>허용 목록</b>으로 정해 두고 그 안의 값만 받습니다."),
    ("값이 같은 줄의 순서 고정하기", "매출이 같은 두 건의 순서가 요청마다 바뀌면 <b>쪽을 넘길 때 같은 줄이 두 번</b> 나옵니다. 그래서 ID를 2차 정렬 기준으로 붙여 순서를 고정합니다."),
    ("전체 건수를 세는 비용", "'20건 중 1~5'처럼 전체 건수를 보여 주려면 <code>COUNT(*)</code>를 따로 돌려야 하는데, 행이 많은 표에서는 이 쿼리가 오래 걸립니다. 그래서 큰 표에서는 <b>'100+ 건'</b>처럼 대략 적거나 커서 방식으로 바꿉니다."),
    ("열이 많은 표의 응답 크기", "열이 늘수록 응답 크기도 커집니다. 화면에 <b>보이는 열만</b> 요청하는 방식(필드 선택)을 두면 목록 응답이 가벼워집니다."),
  ]),
  plat_lede="표는 <b>PC 화면을 전제로 한 부품</b>이라서, iOS와 안드로이드에서는 대개 다른 모양으로 바꿔 보여 줍니다.",
  plats=plats([
    ("웹", "&lt;table&gt;",
     tb(HEAD, row(cells('모란상회', '1,284,000')), "120px"),
     "표준 태그가 있어서 스크린 리더가 표로 읽습니다. 열이 많으면 <b>가로 스크롤</b>을 그대로 두는 것도 웹에서 흔히 쓰는 방식입니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">모란상회 · 1,284,000</div>
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">한빛 · 9,827,500</div>
                </div></div></div>''',
     "표라는 부품이 따로 없어서 보통 <b>리스트</b>로 바꾸고, 화면이 넓은 아이패드에서만 표와 비슷하게 만듭니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">모란상회</div>
                  <div style="padding:5px 8px;font-size:7px;border-bottom:1px solid var(--line)">한빛아웃도어</div>
                </div></div></div>''',
     "M3에 데이터 테이블이 있지만 <b>큰 화면 전용</b>이라서, 폰에서는 리스트로 바꾸라고 권합니다."),
  ]),
  plat_note="\"표로 보여 주세요\"라는 요청은 폰에서는 거의 언제나 <b>리스트나 카드로 바뀝니다.</b> 열이 셋을 넘으면 폰 화면 폭에 들어가지 않기 때문입니다. 그래서 같은 데이터를 <b>PC에서는 표, 폰에서는 카드</b>로 두 벌 만드는 것이 보통인데, 어느 쪽을 어떻게 보여 줄지 먼저 정해 두어야 두 화면에 담기는 내용이 서로 어긋나지 않습니다.",
  siblings=siblings("table"),
  related='''        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
