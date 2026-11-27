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
  desc="페이지네이션이 무엇이고 무한 스크롤과 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="긴 목록을 <b>쪽으로 끊어</b> 보여 주는 줄. 지금 몇 쪽인지, 전부 몇 쪽인지, 어디로 갈 수 있는지를 함께 알려 줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>쪽을 옮기면 <b>주소에도 남습니다</b>(<code>?page=2</code>). 그래서 그 쪽을 그대로 공유할 수 있고
          뒤로가기로 돌아와도 보던 자리가 남습니다 — 무한 스크롤에는 없는 두 가지입니다.<br>
          쪽이 많아지면 가운데를 <b>…</b>로 줄입니다. 처음·끝·지금 주변만 남기는 것이 관례입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "페이지네이션, 쪽 넘김, 페이징"),
    ("영어", "pagination, pager"),
    ("같이 쓰는 말", "가운데를 줄이는 것을 <b>생략</b>(ellipsis·truncation), 쪽당 줄 수를 <b>페이지 크기</b>, 한 쪽씩만 오가는 단순한 꼴을 <b>이전/다음</b>(prev-next)이라 합니다."),
    ("자주 잘못 부름",
     "<b>무한 스크롤</b> — 끝없이 이어 붙이는 쪽입니다. 쪽 번호가 없고 전체도 모릅니다.<br>"
     "<b>스테퍼</b> — 스테퍼는 <b>순서가 있는 단계</b>이고 페이지네이션은 <b>같은 층의 다른 쪽</b>입니다.<br>"
     "<b>캐러셀</b> — 캐러셀은 내용을 가로로 넘깁니다."),
  ]),
  axes=ax("페이지네이션"),
  oneline="페이지네이션은 <b>지금 어디이고 전부 얼마인지</b>를 알려 줍니다. 그 두 가지가 필요 없으면 무한 스크롤이 더 편합니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line);border-radius:2px;padding:0 3px;font-size:5px;color:var(--fg-faint)">‹</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="첫 쪽"), "첫 쪽", "이전이 <b>막혀 있다</b>. 숨기지 말고 비활성으로 둔다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="가운데 쪽"), "가운데", "지금 쪽이 또렷하게. <b>색만으로는 약하다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="font-size:5px;color:var(--fg-muted)">…</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">9</span><span style="font-size:5px;color:var(--fg-muted)">…</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">18</span></div>', bars="", label="접힌 페이지네이션"), "접힘", "처음·끝·지금 주변만. 쪽이 많을 때의 기본"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;justify-content:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">‹ 이전</span><span style="font-size:5px;color:var(--fg-muted)">2 / 18</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">다음 ›</span></div>', bars="", label="이전 다음만 있는 꼴"), "이전 · 다음", "좁은 화면이나 커서 방식. <b>쪽으로 건너뛰지는 못한다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center;opacity:.6"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span class="spn spn--sm" style="width:7px;height:7px;border-width:1.5px"></span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">›</span></div>', bars="", label="쪽을 불러오는 중"), "불러오는 중", "<b>목록만</b> 바꾼다. 쪽 줄까지 사라지면 돌아갈 길이 사라진다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;font-size:5px;color:var(--fg-muted)"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px">쪽당 20 ▾</span><span style="margin-left:auto">1–20 / 137</span></div>', bars="", label="쪽당 줄 수"), "쪽당 줄 수", "바꿀 수 있게 두면 좋다. 바꾸면 <b>1쪽으로 돌아간다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("페이지네이션", "pagination", "<code>&lt;nav aria-label=\"쪽 이동\"&gt;</code>로 감싼다"),
    ("이전 · 다음", "prev · next", "양 끝에서는 <b>비활성</b>. 숨기면 자리가 흔들린다"),
    ("현재 쪽", "current page", "<code>aria-current=\"page\"</code>. 배경까지 바꿔 또렷하게"),
    ("다른 쪽", "page link", "과녁 38px 이상. 숫자만 작게 두면 손가락이 못 맞춘다"),
    ("생략", "ellipsis", "가운데를 줄인 표시. 누를 수 없게 두는 쪽이 흔하다"),
    ("전체 표시", "range · total", "<b>9–16 / 137</b>. 무한 스크롤이 못 주는 정보다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에 없지만 가장 중요한 것이 <b>주소</b>입니다. 쪽 번호가 주소에 남아야
          공유·뒤로가기·새로고침이 전부 제대로 됩니다 — 그게 이 부품의 진짜 값어치입니다.</p>''',
  do=ul([
    "<b>찾아서 돌아와야</b> 하는 목록 — 거래 내역, 주문 목록, 검색 결과",
    "전체가 몇 건인지 알아야 할 때",
    "특정 쪽을 <b>공유하거나 다시 찾아올</b> 일이 있을 때",
  ]),
  dont=ul([
    "끝없이 흘러가는 피드 → 무한 스크롤이나 더 보기",
    "쪽이 두세 쪽뿐일 때 — 그냥 다 보여 주는 편이 낫습니다",
    "쪽 번호를 주소에 안 남기기 — 뒤로가면 1쪽으로 돌아갑니다",
    "숫자를 작게 촘촘히 늘어놓기 — 손가락으로는 못 누릅니다",
  ]),
  instead='흘러가는 피드면 <a href="infinite.html">무한 스크롤</a>, 결과가 없으면 <a href="empty.html">빈 상태</a>, 쪽을 바꾸는 동안은 <a href="skeleton.html">스켈레톤</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">1</span><span style="font-size:5px">…</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">9</span><span style="font-size:5px">…</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">18</span></div>', bars="", tall=False, label="숫자형 재현"),
     "숫자형", "가장 흔한 꼴. 건너뛸 수 있다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;justify-content:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">‹ 이전</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 4px;font-size:5px">다음 ›</span></div>', bars="", tall=False, label="이전 다음만 재현"),
     "이전 · 다음", "커서 방식에서. <b>전체 쪽 수를 모를 때</b>도 쓸 수 있다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px;align-items:center;font-size:5px;color:var(--fg-muted)"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px">쪽당 20 ▾</span><span style="margin-left:auto">1–20 / 137</span></div>', bars="", tall=False, label="표 아래 재현"),
     "표 아래", "쪽당 줄 수와 전체 건수를 함께. 관리 도구의 표준"),
  ]),
  code_lede="쪽 번호를 <b>주소에 담는 것</b>이 절반입니다. 나머지는 가운데를 줄이는 규칙입니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"쪽 이동"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"?page=1"</span>&gt;1&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"?page=9"</span> <span class="a">aria-current</span>=<span class="s">"page"</span>&gt;9&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

<span class="c">// 처음·끝·지금 주변만 남기고 나머지는 … 으로</span>
<span class="a">const</span> near = [<span class="a">1</span>, last, at - <span class="a">1</span>, at, at + <span class="a">1</span>];

<span class="c">// 쪽을 바꾸면 주소에도 남긴다 — 공유와 뒤로가기가 공짜가 된다</span>
history.pushState(<span class="a">null</span>, <span class="s">''</span>, <span class="s">'?page='</span> + at);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "쪽마다 한 번씩. 그래서 <b>접기</b>가 접근성에도 도움이 된다"),
    ("<code>aria-current</code>", "지금 쪽에 <code>\"page\"</code>. 색만으로는 안 전해진다"),
    ("<code>aria-label</code>", "<b>‹</b> 같은 기호에는 '이전 쪽'처럼 이름을 붙인다"),
    ("비활성", "양 끝에서는 <code>disabled</code>. 사라지게 두면 자리가 흔들린다"),
    ("쪽을 바꾼 뒤", "목록 맨 위로 <b>포커스를 옮기거나</b> 스크롤을 올린다. 안 그러면 어디가 바뀐지 모른다"),
  ]),
  backend=rows([
    ("오프셋 vs 커서", "<code>?page=9</code>는 <b>오프셋</b>입니다. 쉽지만 뒤쪽 쪽일수록 느려지고, 그 사이 새 항목이 들어오면 <b>같은 항목을 두 번</b> 보게 됩니다. <b>커서</b>는 그 문제가 없는 대신 쪽으로 건너뛸 수 없어 '이전/다음'만 됩니다."),
    ("전체 건수의 값", "<code>COUNT(*)</code>는 큰 표에서 비쌉니다. '약 1,200건'처럼 근사치를 주거나, 전체를 안 보여 주고 <b>이전/다음</b>만 두는 선택이 있습니다."),
    ("쪽당 줄 수 = 상한", "사용자가 정하게 두되 <b>서버에서 상한</b>을 겁니다. <code>?per=100000</code>을 그대로 받으면 그게 곧 공격입니다."),
    ("주소가 곧 상태", "쪽·정렬·필터가 모두 주소에 있으면 화면은 상태를 따로 안 들고 있어도 됩니다. 공유·뒤로가기·새로고침이 전부 공짜가 됩니다."),
  ]),
  plat_lede="웹의 부품입니다. 모바일 앱에서는 거의 쓰지 않습니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:2px;align-items:center"><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">‹</span><span style="background:var(--accent);color:#fff;border-radius:2px;padding:0 3px;font-size:5px">2</span><span style="border:1px solid var(--line-strong);border-radius:2px;padding:0 3px;font-size:5px">3</span></div>', bars="", label="웹 페이지네이션 재현"),
     "<b>페이지네이션</b> · 검색·목록 화면의 기본입니다. 주소에 쪽을 담는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center"><span style="font-size:10px;letter-spacing:3px;color:var(--fg-faint)">••<b style="color:var(--fg)">•</b>••</span></div>', "iOS 페이지 컨트롤 재현"),
     "<b>페이지 컨트롤</b>(Page control)은 <b>점</b>입니다 — 캐러셀의 몇 번째인지를 뜻하지 목록의 쪽이 아닙니다. 목록은 <b>이어서 불러오기</b>로 풉니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center"><span style="border:1px solid var(--line-strong);border-radius:99px;padding:3px 10px;font-size:7.5px">더 보기</span></div>', "안드로이드 더 보기 재현"),
     "표준 페이지네이션이 없습니다. <b>Paging 라이브러리</b>로 이어서 불러오는 것이 기본이고, 화면에는 더 보기나 자동 로드만 보입니다."),
  ]),
  plat_note="모바일 앱에서 \"페이지네이션\"이라고 하면 보통 <b>캐러셀의 점</b>이나 <b>내부 페이징 구현</b>을 뜻합니다. 쪽 번호 줄은 거의 안 씁니다 — 숫자가 작아 손가락으로 못 누르기 때문입니다. 같은 목록도 웹은 쪽, 앱은 이어 붙이기로 갈리는 일이 흔합니다.",
  siblings=siblings("pagination"),
  related='''        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>데이터 테이블</b><em>10부</em></span></li>
        <li><span class="na"><b>가상 스크롤</b><em>10부</em></span></li>''',
)
