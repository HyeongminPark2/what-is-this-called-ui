# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px;display:flex;align-items:center;gap:40px;flex-wrap:wrap">
                  <span data-pin="2" style="border:1px solid var(--line-strong);border-radius:4px;padding:4px 9px;font-size:11px;color:var(--fg-faint)">‹</span>
                  <span data-pin="3" style="background:var(--accent);color:#fff;border-radius:4px;padding:4px 10px;font-size:11px;font-weight:700">2</span>
                  <span data-pin="4" style="border:1px solid var(--line-strong);border-radius:4px;padding:4px 10px;font-size:11px">3</span>
                  <span data-pin="5" style="font-size:11px;color:var(--fg-muted)">…</span>
                  <span class="pin-tr" data-pin="6" style="font-size:10.5px;color:var(--fg-muted)">9–16 / 전체 137건</span>
                </div>
              </div>'''

D = dict(
  slug="pagination", ko="페이지네이션", en="Pagination",
  desc="페이지네이션이 무엇인지, 무한 스크롤과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="페이지네이션은 긴 목록을 <b>쪽 단위로 나눠</b> 보여 줄 때 목록 아래에 두는 쪽 번호 줄입니다. 지금 몇 쪽인지, 전부 몇 쪽인지, 어느 쪽으로 갈 수 있는지를 함께 알려 줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>쪽을 옮기면 쪽 번호가 <b>주소에도 남습니다</b>(<code>?page=2</code>). 그래서 그 쪽을 링크로 그대로 공유할 수 있고,
          다른 화면에 갔다가 뒤로가기로 돌아와도 보던 쪽이 그대로 나옵니다. 무한 스크롤로는 이 두 가지를 할 수 없습니다.<br>
          쪽이 많아지면 가운데 쪽 번호를 <b>…</b>로 줄입니다. 첫 쪽과 끝 쪽, 지금 쪽 주변만 남기는 것이 관례입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "페이지네이션, 쪽 넘김, 페이징"),
    ("영어", "pagination, pager"),
    ("같이 쓰는 말", "가운데 쪽 번호를 줄이는 것은 <b>생략</b>(ellipsis·truncation), 한 쪽에 보여 주는 줄 수는 <b>페이지 크기</b>, 한 쪽씩만 오가는 단순한 형태는 <b>이전/다음</b>(prev-next)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>무한 스크롤</b> — 무한 스크롤은 목록 끝에 다음 묶음을 계속 이어 붙이는 방식이라서 쪽 번호가 없고 전체가 얼마인지도 알 수 없습니다.<br>"
     "<b>스테퍼</b> — 스테퍼는 <b>순서가 있는 단계</b>를 거쳐 가는 부품이고, 페이지네이션은 <b>같은 목록의 다른 쪽</b>으로 옮겨 가는 부품입니다.<br>"
     "<b>캐러셀</b> — 캐러셀은 목록의 쪽이 아니라 카드나 사진 같은 내용을 가로로 넘겨 보는 부품입니다."),
  ]),
  axes=ax("페이지네이션"),
  oneline="페이지네이션은 <b>지금 몇 쪽이고 전부 얼마인지</b>를 알려 줍니다. 사용자에게 이 두 가지 정보가 필요 없다면 무한 스크롤이 더 편합니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line);border-radius:2px;padding:0 3px;font-size:5px;color:var(--fg-faint)">‹</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="첫 쪽"), "첫 쪽", "이전 버튼은 <b>누를 수 없게</b> 막습니다. 버튼을 숨기지 말고 비활성 상태로 둡니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="가운데 쪽"), "가운데", "지금 쪽이 분명히 드러나야 합니다. <b>색만 바꾸면 구별하기 어렵습니다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="font-size:5px;color:var(--fg-muted)">…</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">9</span><span style="font-size:5px;color:var(--fg-muted)">…</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">18</span></div>', bars="", label="접힌 페이지네이션"), "접힘", "첫 쪽과 끝 쪽, 지금 쪽 주변만 보여 줍니다. 쪽이 많을 때 기본으로 쓰는 형태입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;justify-content:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">‹ 이전</span><span style="font-size:5px;color:var(--fg-muted)">2 / 18</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">다음 ›</span></div>', bars="", label="이전 다음만 있는 꼴"), "이전 · 다음", "좁은 화면이나 커서 방식에서 씁니다. <b>원하는 쪽으로 건너뛸 수는 없습니다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center;opacity:.6"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span class="spn spn--sm" style="width:7px;height:7px;border-width:1.5px"></span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">›</span></div>', bars="", label="쪽을 불러오는 중"), "불러오는 중", "<b>목록 부분만</b> 로딩 상태로 바꿉니다. 쪽 번호 줄까지 사라지면 다른 쪽으로 옮길 방법이 없어집니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;font-size:5px;color:var(--fg-muted)"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px">쪽당 20 ▾</span><span style="margin-left:auto">1–20 / 137</span></div>', bars="", label="쪽당 줄 수"), "쪽당 줄 수", "사용자가 바꿀 수 있게 두면 좋습니다. 줄 수를 바꾸면 <b>1쪽으로 돌아갑니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("페이지네이션", "pagination", "<code>&lt;nav aria-label=\"쪽 이동\"&gt;</code>로 감쌉니다"),
    ("이전 · 다음", "prev · next", "첫 쪽과 끝 쪽에서는 <b>비활성</b>으로 둡니다. 버튼을 숨기면 쪽 번호들의 위치가 옆으로 밀립니다"),
    ("현재 쪽", "current page", "<code>aria-current=\"page\"</code>를 달고, 배경색까지 바꿔 분명히 드러냅니다"),
    ("다른 쪽", "page link", "누르는 영역을 38px 이상으로 잡습니다. 숫자 크기만큼만 작게 두면 손가락으로 정확히 누르기 어렵습니다"),
    ("생략", "ellipsis", "가운데 쪽 번호를 줄였다는 표시입니다. 누를 수 없게 두는 경우가 흔합니다"),
    ("전체 표시", "range · total", "<b>9–16 / 137</b>처럼 지금 보는 범위와 전체 건수를 보여 줍니다. 무한 스크롤로는 줄 수 없는 정보입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 없지만 페이지네이션에서 특히 중요한 것이 <b>주소</b>입니다. 쪽 번호가 주소에 남아 있어야
          링크로 공유하거나 뒤로가기로 돌아오거나 새로고침했을 때 같은 쪽이 다시 나옵니다. 무한 스크롤 대신 페이지네이션을 쓰는 주된 이유가 이 동작입니다.</p>''',
  do=ul([
    "거래 내역, 주문 목록, 검색 결과처럼 항목을 <b>찾아서 다시 돌아와야</b> 하는 목록일 때",
    "전체가 몇 건인지 알아야 할 때",
    "특정 쪽을 <b>공유하거나 다시 찾아올</b> 일이 있을 때",
  ]),
  dont=ul([
    "새 글이 계속 올라오는 피드일 때. 무한 스크롤이나 더 보기 버튼을 씁니다",
    "두세 쪽뿐일 때. 쪽을 나누지 않고 전부 보여 주는 편이 낫습니다",
    "쪽 번호를 주소에 남기지 않을 때. 뒤로가기로 돌아오면 1쪽으로 돌아갑니다",
    "숫자를 작게 촘촘히 늘어놓을 때. 손가락으로는 원하는 쪽을 정확히 누를 수 없습니다",
  ]),
  instead='흘러가는 피드면 <a href="infinite.html">무한 스크롤</a>, 결과가 없으면 <a href="empty.html">빈 상태</a>, 쪽을 바꾸는 동안은 <a href="skeleton.html">스켈레톤</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="font-size:5px">…</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">9</span><span style="font-size:5px">…</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">18</span></div>', bars="", tall=False, label="숫자형 재현"),
     "숫자형", "가장 흔한 형태로, 원하는 쪽으로 바로 건너뛸 수 있습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;justify-content:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">‹ 이전</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">다음 ›</span></div>', bars="", tall=False, label="이전 다음만 재현"),
     "이전 · 다음", "커서 방식에서 씁니다. <b>전체 쪽 수를 모를 때</b>도 쓸 수 있습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;font-size:5px;color:var(--fg-muted)"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px">쪽당 20 ▾</span><span style="margin-left:auto">1–20 / 137</span></div>', bars="", tall=False, label="표 아래 재현"),
     "표 아래", "쪽당 줄 수와 전체 건수를 함께 보여 줍니다. 관리 도구에서 표준처럼 쓰는 형태입니다"),
  ]),
  code_lede="구현에서 가장 중요한 일은 쪽 번호를 <b>주소에 담는 것</b>이고, 그다음은 쪽이 많을 때 가운데 번호를 줄이는 규칙을 정하는 것입니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"쪽 이동"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"?page=1"</span>&gt;1&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"?page=9"</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;9&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">// 첫 쪽·끝 쪽·지금 쪽 주변만 남기고 나머지는 … 으로 줄인다</span>
<span class="a">const</span> near = [<span class="a">1</span>, last, at - <span class="a">1</span>, at, at + <span class="a">1</span>];

<span class="c">// 쪽을 바꾸면 주소에도 남긴다. 그러면 공유와 뒤로가기를 따로 구현하지 않아도 된다</span>
history.pushState(<span class="a">null</span>, <span class="s">''</span>, <span class="s">'?page='</span> + at);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "쪽 번호마다 포커스가 한 번씩 거쳐 갑니다. 그래서 가운데 번호를 <b>접어</b> 두면 키보드 사용자도 덜 누르게 됩니다"),
    ("<code>aria-current</code>", "지금 쪽에 <code>\"page\"</code> 값을 답니다. 색만으로는 스크린 리더에 전해지지 않습니다"),
    ("<code>aria-label</code>", "<b>‹</b> 같은 기호 버튼에는 '이전 쪽'처럼 이름을 붙입니다"),
    ("비활성", "첫 쪽과 끝 쪽에서는 <code>disabled</code>로 둡니다. 버튼을 없애면 쪽 번호들의 위치가 밀립니다"),
    ("쪽을 바꾼 뒤", "목록 맨 위로 <b>포커스를 옮기거나</b> 스크롤을 올립니다. 그러지 않으면 사용자는 화면의 어디가 바뀌었는지 알 수 없습니다"),
  ]),
  backend=rows([
    ("오프셋 vs 커서", "<code>?page=9</code>는 앞에서 몇 건을 건너뛸지 정하는 <b>오프셋</b> 방식입니다. 구현은 쉽지만 뒤쪽 쪽일수록 질의가 느려지고, 쪽을 넘기는 사이에 새 항목이 들어오면 <b>같은 항목을 두 번</b> 보게 됩니다. 마지막으로 본 항목을 기준으로 다음 묶음을 가져오는 <b>커서</b> 방식은 이런 문제가 없지만, 특정 쪽으로 건너뛸 수 없어서 '이전/다음'만 쓸 수 있습니다."),
    ("전체 건수의 값", "큰 표에서 <code>COUNT(*)</code>는 비용이 큽니다. 그래서 '약 1,200건'처럼 근사치를 보여 주거나, 전체 건수를 아예 보여 주지 않고 <b>이전/다음</b>만 두는 방법도 있습니다."),
    ("쪽당 줄 수 = 상한", "쪽당 줄 수는 사용자가 정하게 두되 <b>서버에서 상한</b>을 겁니다. <code>?per=100000</code> 같은 요청을 그대로 받으면 서버에 큰 부하를 주는 공격 수단이 됩니다."),
    ("주소가 곧 상태", "쪽 번호와 정렬, 필터가 모두 주소에 들어 있으면 화면이 이 상태를 따로 저장하지 않아도 됩니다. 공유와 뒤로가기, 새로고침도 따로 구현할 필요 없이 제대로 동작합니다."),
  ]),
  plat_lede="페이지네이션은 웹에서 쓰는 부품이고, 모바일 앱에서는 거의 쓰지 않습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="웹 페이지네이션 재현"),
     "<b>페이지네이션</b> · 검색 결과와 목록 화면에서 기본으로 씁니다. 쪽 번호를 주소에 담는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center"><span style="font-size:10px;letter-spacing:3px;color:var(--fg-faint)">••<b style="color:var(--fg)">•</b>••</span></div>', "iOS 페이지 컨트롤 재현"),
     "<b>페이지 컨트롤</b>(Page control)은 <b>점</b> 모양이고, 목록의 쪽이 아니라 캐러셀에서 지금 몇 번째 내용을 보는지를 나타냅니다. 긴 목록은 <b>이어서 불러오기</b>로 보여 줍니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center"><span style="border:1px solid var(--line-strong);border-radius:99px;padding:3px 10px;font-size:7.5px">더 보기</span></div>', "안드로이드 더 보기 재현"),
     "표준 페이지네이션 부품이 없습니다. <b>Paging 라이브러리</b>로 데이터를 이어서 불러오는 것이 기본이라서, 화면에는 더 보기 버튼이나 자동 로드만 보입니다."),
  ]),
  plat_note="모바일 앱에서 \"페이지네이션\"이라고 하면 보통 <b>캐러셀의 점</b>이나 데이터를 나눠 받는 <b>내부 페이징 구현</b>을 뜻합니다. 쪽 번호 줄은 숫자가 작아 손가락으로 누르기 어렵기 때문에 거의 쓰지 않습니다. 그래서 같은 목록이라도 웹에서는 쪽으로 나누고 앱에서는 이어 붙이는 경우가 흔합니다.",
  siblings=siblings("pagination"),
  related='''        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>데이터 테이블</b><em>10부</em></span></li>
        <li><span class="na"><b>가상 스크롤</b><em>10부</em></span></li>''',
)
