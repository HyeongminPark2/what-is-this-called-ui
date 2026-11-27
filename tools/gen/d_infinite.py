# -*- coding: utf-8 -*-
from parts import *
from ax7 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div class="pin-out" data-pin="2" style="font-size:11px;color:var(--fg-muted);margin-bottom:18px">… 앞서 불러온 48건</div>
                  <div class="pin-out" data-pin="3" style="border-top:1px dashed var(--line-strong);height:1px;margin-bottom:32px"></div>
                  <div style="display:flex;align-items:center;gap:40px;margin-bottom:18px">
                    <span class="pin-out" data-pin="4" style="width:16px;height:16px;border:2px solid var(--line);border-top-color:var(--accent);border-radius:50%;flex:none"></span>
                    <span class="pin-out" data-pin="5" style="font-size:11px;color:var(--fg-muted)">더 불러오는 중…</span>
                  </div>
                  <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-faint);border-top:1px solid var(--line);padding-top:16px">여기까지입니다</div>
                </div>
              </div>'''

D = dict(
  slug="infinite", ko="무한 스크롤", en="Infinite scroll",
  desc="무한 스크롤이 무엇이고 페이지네이션·더 보기와 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="목록 끝에 닿으면 <b>저절로</b> 다음 묶음을 이어 붙이는 방식. 읽기만 하는 피드에는 편하지만, 돌아올 자리와 끝이 사라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>끝까지 스크롤하면 저절로 더 불러옵니다. 대신 <b>푸터에 닿을 수 없고</b> 전부 몇 건인지도 알 수 없습니다 —
          아래 숫자가 계속 늘어날 뿐입니다.<br>
          위의 체크를 켜면 <b>더 보기</b> 버튼으로 바뀝니다. 멈출 자리를 사용자가 정할 수 있어
          푸터에 닿고 키보드로도 쓸 수 있습니다. <b>대부분의 경우 이쪽이 더 안전합니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "무한 스크롤, 끝없는 스크롤, 자동 불러오기"),
    ("영어", "infinite scroll, endless scroll, infinite loading"),
    ("같이 쓰는 말", "끝을 감시하는 보이지 않는 표식을 <b>센티널</b>(sentinel), 사용자가 눌러 불러오는 꼴을 <b>더 보기</b>(load more), 끝에 닿았다는 표시를 <b>끝 표시</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>페이지네이션</b> — 쪽 번호가 있는 쪽입니다. 지금 어디인지와 전체를 알 수 있습니다.<br>"
     "<b>가상 스크롤</b> — 가상 스크롤은 <b>그리는 양</b>을 줄이는 기법이고, 무한 스크롤은 <b>불러오는 방식</b>입니다. 같이 쓰기도 합니다.<br>"
     "<b>지연 로딩</b> — 지연 로딩은 이미지처럼 <b>개별 자원</b>을 늦게 받는 것입니다."),
  ]),
  axes=ax("무한 스크롤"),
  oneline="무한 스크롤은 <b>끝과 위치를 버리고</b> 흐름을 얻습니다. 찾아서 돌아와야 하는 목록에는 맞지 않습니다.",
  states=states([
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="첫 묶음"), "첫 묶음", "한 번에 다 받지 않는다. 보통 10~30건"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", label="더 불러오는 중"), "불러오는 중", "끝 가까이 가면 미리 부른다. <b>닿기 전에</b> 부르면 끊김이 없다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:6px;padding:2px 6px">더 보기</span></div>', bars="", label="더 보기 버튼"), "더 보기", "사용자가 멈출 자리를 정한다. <b>푸터에 닿을 수 있다</b>"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center;font-size:5.5px;color:var(--fg-muted);border-top:1px solid var(--line);padding-top:4px">여기까지입니다</div>', bars="", label="끝에 닿음"), "끝", "<b>끝 표시를 꼭 둔다.</b> 없으면 영영 기다리게 된다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center;font-size:5.5px;color:var(--danger);font-weight:700">불러오지 못했습니다 · 다시</div>', bars="", label="불러오기 실패"), "실패", "그 자리에서 다시 시도. 목록 전체를 날리지 않는다"),
    (mini('<div class="mini__bg" style="opacity:.45"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--danger);font-weight:700">푸터에 못 닿음</div>', bars="", label="푸터에 닿지 못하는 문제"), "푸터 문제", "스크롤할 때마다 아래가 늘어나 <b>푸터를 영영 못 만진다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("목록", "list", "묶음이 계속 뒤에 붙는다. 앞의 것은 그대로 남는다"),
    ("앞서 불러온 것", "loaded items", "길어질수록 메모리와 그리는 양이 늘어난다 — <b>가상 스크롤</b>과 묶어 쓰는 이유"),
    ("센티널", "sentinel", "보이지 않는 표식. 이게 화면에 들어오면 다음 묶음을 부른다"),
    ("불러오는 표시", "loading indicator", "목록 끝에만 둔다. 화면 전체를 덮지 않는다"),
    ("안내 문구", "status", "라이브 리전으로 '12건 더 불러왔습니다'를 알린다"),
    ("끝 표시", "end marker", "<b>반드시 둔다.</b> 끝났다는 말이 없으면 계속 기다린다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          센티널을 목록 <b>끝에서 조금 위</b>에 두면(<code>rootMargin</code>) 사용자가 닿기 전에 미리 불러와
          끊김이 없습니다. 너무 위에 두면 안 볼 것까지 받아 데이터만 축냅니다.</p>''',
  do=ul([
    "<b>둘러보는</b> 피드 — 소셜, 사진, 추천",
    "순서가 시간순이고 <b>돌아올 일이 적은</b> 목록",
    "폰에서 손가락으로 계속 넘기는 화면",
  ]),
  dont=ul([
    "찾아서 <b>돌아와야</b> 하는 목록 → 페이지네이션. 뒤로가면 자리가 사라집니다",
    "푸터에 중요한 것이 있을 때 — <b>영영 못 닿습니다</b>",
    "전체가 몇 건인지 알아야 할 때",
    "표나 관리 도구 — 비교하고 건너뛰어야 하는 화면",
  ]),
  instead='돌아와야 하면 <a href="pagination.html">페이지네이션</a>, 멈출 자리를 주려면 <b>더 보기</b> 버튼, 그리는 양이 문제면 가상 스크롤(10부), 결과가 없으면 <a href="empty.html">빈 상태</a>.',
  cases=cases([
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", tall=False, label="피드 무한 스크롤 재현"),
     "피드", "둘러보는 화면. 이 방식이 가장 잘 맞는 자리"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:6px;padding:2px 6px">더 보기</span></div>', bars="", tall=False, label="더 보기 재현"),
     "더 보기", "<b>타협안.</b> 끊김은 조금 있지만 푸터와 키보드를 지킨다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:5.5px;padding:2px 5px">더 보기</span><div style="font-size:5px;color:var(--fg-muted);margin-top:2px">48 / 1,284</div></div>', bars="", tall=False, label="진행 표시가 붙은 재현"),
     "개수 표시", "불러온 수와 전체를 같이. 무한 스크롤의 약점을 메운다"),
  ]),
  code_lede="<code>IntersectionObserver</code>로 센티널을 지켜봅니다. 스크롤 이벤트를 세는 것보다 가볍고 정확합니다.",
  code='''&lt;<span class="t">ul</span> <span class="a">id</span>=<span class="s">"list"</span>&gt;…&lt;/<span class="t">ul</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"sentinel"</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;12건 더 불러왔습니다&lt;/<span class="t">p</span>&gt;

<span class="c">// 닿기 전에 미리 부른다 (rootMargin)</span>
<span class="a">new</span> IntersectionObserver(es =&gt; <span class="a">{</span>
  <span class="a">if</span> (es[<span class="a">0</span>].isIntersecting) loadMore();
<span class="a">}</span>, <span class="a">{</span> rootMargin: <span class="s">'200px'</span> <span class="a">}</span>).observe(sentinel);

<span class="c">// 두 번 부르지 않게 잠근다 — 가장 흔한 버그</span>
<span class="a">if</span> (busy || done) <span class="a">return</span>;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "자동 로드는 <b>키보드 사용자에게 불리하다</b>. 끝에 닿을 방법이 없다 — 더 보기 버튼이면 해결된다"),
    ("<code>aria-live</code>", "'12건 더 불러왔습니다'를 알린다. 안 알리면 화면이 바뀐 줄 모른다"),
    ("더 보기 버튼", "눌린 뒤 <b>새로 들어온 첫 항목으로</b> 포커스를 옮기면 이어서 읽을 수 있다"),
    ("끝", "'여기까지입니다'를 글로 알린다"),
    ("<code>prefers-reduced-motion</code>", "새 묶음이 나타나는 애니메이션을 끈다"),
  ]),
  backend=rows([
    ("커서가 거의 필수", "오프셋으로 이어 붙이면 그 사이 새 항목이 들어올 때 <b>같은 항목이 두 번</b> 보입니다. 커서(마지막 ID·시각)를 쓰면 그 문제가 없습니다."),
    ("중복 요청 잠금", "스크롤이 빠르면 센티널이 여러 번 걸립니다. <code>busy</code> 플래그가 없으면 같은 묶음을 서너 번 부릅니다 — <b>가장 흔한 버그</b>입니다."),
    ("끝을 어떻게 아나", "응답에 <code>hasMore</code>를 담습니다. '받은 수 &lt; 요청 수'로 추측하면 경계에서 틀립니다."),
    ("쌓이는 비용", "1,000건을 이어 붙이면 DOM 도 메모리도 그만큼 커집니다. <b>가상 스크롤</b>로 보이는 만큼만 그리거나, 앞쪽을 버리는 창 방식을 씁니다."),
    ("돌아올 자리", "뒤로 왔을 때 보던 자리를 되살리려면 <b>받아 둔 묶음과 스크롤 위치</b>를 함께 저장해야 합니다. 페이지네이션이 주소 한 줄로 푸는 일을 여기서는 직접 해야 합니다."),
  ]),
  plat_lede="모바일 앱에서는 사실상 기본 방식이고, 웹에서는 쓰임에 따라 갈립니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", label="웹 무한 스크롤 재현"),
     "<code>IntersectionObserver</code>로 직접 만듭니다. 푸터와 뒤로가기 문제 때문에 <b>더 보기</b>로 타협하는 제품이 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:5px"><div style="height:8px;border-radius:3px;background:var(--line)"></div><div style="height:8px;border-radius:3px;background:var(--line)"></div></div><div style="position:absolute;left:0;right:0;bottom:24px;text-align:center"><span style="font-size:7px;color:var(--fg-muted)">불러오는 중…</span></div>', "iOS 이어서 불러오기 재현"),
     "목록이 끝에 가까워지면 <b>더 가져오는 것이 기본</b>입니다. 위에서 당겨 새로 고치는 <b>당겨 새로고침</b>과 짝으로 씁니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:5px"><div style="height:8px;border-radius:3px;background:var(--line)"></div><div style="height:8px;border-radius:3px;background:var(--line)"></div></div><div style="position:absolute;left:0;right:0;bottom:24px;text-align:center"><span class="spn spn--sm" style="width:10px;height:10px;border-width:1.5px"></span></div>', "안드로이드 Paging 재현"),
     "<b>Paging 라이브러리</b>가 표준입니다. 커서 기반 이어 붙이기와 재시도·끝 처리가 틀로 제공됩니다."),
  ]),
  plat_note="\"무한 스크롤로 해 주세요\"는 앱에서는 그냥 기본값이지만, <b>웹에서는 뒤로가기와 푸터를 포기한다</b>는 뜻입니다. 결제·주문처럼 돌아올 일이 있는 목록이면 그 포기가 비쌉니다 — 쓰임을 먼저 가려야 합니다.",
  siblings=siblings("infinite"),
  related='''        <li><span class="na"><b>가상 스크롤</b><em>10부</em></span></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>당겨 새로고침</b><em>9부</em></span></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
