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
  desc="무한 스크롤이 무엇인지, 페이지네이션·더 보기와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="무한 스크롤은 목록 끝에 닿으면 <b>저절로</b> 다음 묶음을 불러와 이어 붙이는 방식입니다. 읽기만 하는 피드에서는 편하지만, 보던 자리로 돌아오기 어렵고 목록이 어디서 끝나는지도 알 수 없습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>끝까지 스크롤하면 저절로 더 불러옵니다. 대신 <b>푸터까지 내려갈 수 없고</b> 전부 몇 건인지도 알 수 없어서,
          아래에 보이는 숫자는 불러온 만큼 계속 늘어나기만 합니다.<br>
          위의 체크를 켜면 <b>더 보기</b> 버튼 방식으로 바뀝니다. 언제 더 불러올지를 사용자가 정하기 때문에
          푸터까지 내려갈 수 있고 키보드로도 쓸 수 있습니다. <b>대부분의 경우 더 보기 버튼이 더 안전합니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "무한 스크롤, 끝없는 스크롤, 자동 불러오기"),
    ("영어", "infinite scroll, endless scroll, infinite loading"),
    ("같이 쓰는 말", "목록 끝에 두어 스크롤이 닿았는지 감지하는 보이지 않는 요소는 <b>센티널</b>(sentinel), 사용자가 버튼을 눌러 불러오는 형태는 <b>더 보기</b>(load more), 목록이 끝났다는 표시는 <b>끝 표시</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>페이지네이션</b> — 페이지네이션은 쪽 번호가 있어서 지금 몇 쪽인지와 전체가 얼마인지를 알 수 있습니다.<br>"
     "<b>가상 스크롤</b> — 가상 스크롤은 화면에 <b>그리는 양</b>을 줄이는 기법이고, 무한 스크롤은 데이터를 <b>불러오는 방식</b>입니다. 둘을 함께 쓰기도 합니다.<br>"
     "<b>지연 로딩</b> — 지연 로딩은 이미지처럼 <b>개별 자원</b>을 필요할 때 늦게 받는 기법이고, 목록의 다음 묶음을 불러오는 무한 스크롤과는 다릅니다."),
  ]),
  axes=ax("무한 스크롤"),
  oneline="무한 스크롤을 쓰면 멈추지 않고 계속 내려 볼 수 있는 대신, <b>목록의 끝과 지금 위치를 알 수 없게 됩니다</b>. 그래서 항목을 찾아서 다시 돌아와야 하는 목록에는 맞지 않습니다.",
  states=states([
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div></div>', bars="", label="첫 묶음"), "첫 묶음", "목록 전체를 한 번에 받지 않고 보통 10~30건씩 받습니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", label="더 불러오는 중"), "불러오는 중", "끝에 가까워지면 다음 묶음을 미리 요청합니다. <b>끝에 닿기 전에</b> 요청하면 스크롤이 멈추지 않고 이어집니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:6px;padding:2px 6px">더 보기</span></div>', bars="", label="더 보기 버튼"), "더 보기", "언제 더 불러올지를 사용자가 정합니다. 그래서 <b>푸터까지 내려갈 수 있습니다</b>"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center;font-size:5.5px;color:var(--fg-muted);border-top:1px solid var(--line);padding-top:4px">여기까지입니다</div>', bars="", label="끝에 닿음"), "끝", "<b>끝 표시를 꼭 둡니다.</b> 끝 표시가 없으면 사용자는 더 불러올 것이 남았는지 몰라 계속 기다립니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center;font-size:5.5px;color:var(--danger);font-weight:700">불러오지 못했습니다 · 다시</div>', bars="", label="불러오기 실패"), "실패", "실패한 자리에서 다시 시도할 수 있게 합니다. 이미 불러온 목록은 그대로 둡니다"),
    (mini('<div class="mini__bg" style="opacity:.45"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--danger);font-weight:700">푸터에 못 닿음</div>', bars="", label="푸터에 닿지 못하는 문제"), "푸터 문제", "끝에 닿을 때마다 아래에 항목이 더 붙기 때문에 <b>푸터까지 내려갈 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("목록", "list", "새 묶음이 계속 뒤에 붙고, 앞에 불러온 항목은 그대로 남습니다"),
    ("앞서 불러온 것", "loaded items", "목록이 길어질수록 메모리와 화면에 그리는 양이 늘어납니다. 그래서 <b>가상 스크롤</b>과 함께 쓰는 경우가 많습니다"),
    ("센티널", "sentinel", "목록 끝에 둔 보이지 않는 요소입니다. 센티널이 화면에 들어오면 다음 묶음을 요청합니다"),
    ("불러오는 표시", "loading indicator", "목록 끝에만 두고, 화면 전체를 덮지 않습니다"),
    ("안내 문구", "status", "라이브 리전으로 '12건 더 불러왔습니다'처럼 알립니다"),
    ("끝 표시", "end marker", "<b>반드시 둡니다.</b> 끝났다는 표시가 없으면 사용자는 더 나올 것을 계속 기다립니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          센티널을 목록 <b>끝보다 조금 위</b>에서 감지하게 하면(<code>rootMargin</code>) 사용자가 끝에 닿기 전에 다음 묶음을 미리 받아 두므로
          스크롤이 멈추지 않고 이어집니다. 다만 너무 위에서 감지하게 하면 사용자가 보지도 않을 항목까지 받아서 데이터를 낭비합니다.</p>''',
  do=ul([
    "소셜, 사진, 추천처럼 <b>훑어보는</b> 피드일 때",
    "시간순으로 늘어놓았고 <b>다시 돌아올 일이 적은</b> 목록일 때",
    "폰에서 손가락으로 계속 넘겨 보는 화면일 때",
  ]),
  dont=ul([
    "항목을 찾아서 <b>다시 돌아와야</b> 하는 목록일 때. 뒤로가기로 돌아오면 보던 자리를 잃으므로 페이지네이션을 씁니다",
    "푸터에 중요한 내용이 있을 때. 사용자가 <b>푸터까지 내려갈 수 없습니다</b>",
    "전체가 몇 건인지 알아야 할 때",
    "항목을 비교하거나 원하는 위치로 건너뛰어야 하는 표나 관리 도구일 때",
  ]),
  instead='돌아와야 하면 <a href="pagination.html">페이지네이션</a>, 멈출 자리를 주려면 <b>더 보기</b> 버튼, 그리는 양이 문제면 가상 스크롤(10부), 결과가 없으면 <a href="empty.html">빈 상태</a>.',
  cases=cases([
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", tall=False, label="피드 무한 스크롤 재현"),
     "피드", "훑어보는 화면이라서 무한 스크롤이 가장 잘 맞습니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:6px;padding:2px 6px">더 보기</span></div>', bars="", tall=False, label="더 보기 재현"),
     "더 보기", "<b>무한 스크롤과 페이지네이션의 중간</b>입니다. 버튼을 눌러야 해서 흐름이 조금 끊기지만 푸터에 닿을 수 있고 키보드로도 쓸 수 있습니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:7px;text-align:center"><span class="mini__btn mini__btn--ghost" style="font-size:5.5px;padding:2px 5px">더 보기</span><div style="font-size:5px;color:var(--fg-muted);margin-top:2px">48 / 1,284</div></div>', bars="", tall=False, label="진행 표시가 붙은 재현"),
     "개수 표시", "불러온 건수와 전체 건수를 함께 보여 줘서, 전체 규모를 알 수 없다는 무한 스크롤의 약점을 보완합니다"),
  ]),
  code_lede="<code>IntersectionObserver</code>로 센티널이 화면에 들어오는지 감지합니다. 스크롤 이벤트마다 위치를 계산하는 방식보다 가볍고 정확합니다.",
  code='''&lt;<span class="t">ul</span> <span class="a">id</span>=<span class="s">"list"</span>&gt;…&lt;/<span class="t">ul</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"sentinel"</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;12건 더 불러왔습니다&lt;/<span class="t">p</span>&gt;

<span class="c">// 끝에 닿기 전에 미리 부른다 (rootMargin)</span>
<span class="a">new</span> IntersectionObserver(es =&gt; <span class="a">{</span>
  <span class="a">if</span> (es[<span class="a">0</span>].isIntersecting) loadMore();
<span class="a">}</span>, <span class="a">{</span> rootMargin: <span class="s">'200px'</span> <span class="a">}</span>).observe(sentinel);

<span class="c">// 두 번 부르지 않게 잠근다. 이걸 빠뜨리는 버그가 가장 흔하다</span>
<span class="a">if</span> (busy || done) <span class="a">return</span>;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "자동 로드는 <b>키보드 사용자에게 불리합니다</b>. 목록 끝을 지나 그 아래로 갈 방법이 없는데, 더 보기 버튼을 두면 이 문제가 해결됩니다"),
    ("<code>aria-live</code>", "'12건 더 불러왔습니다'처럼 알립니다. 알리지 않으면 스크린 리더 사용자는 목록이 늘어난 것을 모릅니다"),
    ("더 보기 버튼", "버튼을 누른 뒤 <b>새로 들어온 첫 항목으로</b> 포커스를 옮기면 이어서 읽을 수 있습니다"),
    ("끝", "'여기까지입니다'처럼 글로 끝을 알립니다"),
    ("<code>prefers-reduced-motion</code>", "이 설정이 켜져 있으면 새 묶음이 나타나는 애니메이션을 끕니다"),
  ]),
  backend=rows([
    ("커서가 거의 필수", "오프셋으로 이어 붙이면 묶음을 받는 사이에 새 항목이 들어왔을 때 <b>같은 항목이 두 번</b> 보입니다. 마지막으로 받은 항목의 ID나 시각을 커서로 넘기면 이 문제가 생기지 않습니다."),
    ("중복 요청 잠금", "스크롤이 빠르면 센티널이 짧은 사이에 여러 번 감지됩니다. 요청 중임을 나타내는 <code>busy</code> 플래그가 없으면 같은 묶음을 서너 번 요청하게 되는데, 무한 스크롤에서 <b>가장 흔한 버그</b>입니다."),
    ("끝을 어떻게 아나", "응답에 <code>hasMore</code>를 담아 더 있는지 알려 줍니다. '받은 수 &lt; 요청 수'로 끝을 추측하면 남은 항목 수가 묶음 크기와 정확히 맞아떨어질 때 틀립니다."),
    ("쌓이는 비용", "1,000건을 이어 붙이면 DOM과 메모리도 그만큼 커집니다. 그래서 <b>가상 스크롤</b>로 화면에 보이는 만큼만 그리거나, 앞쪽 항목을 버리고 일정 개수만 유지하는 창(window) 방식을 씁니다."),
    ("돌아올 자리", "뒤로가기로 돌아왔을 때 보던 자리를 되살리려면 <b>받아 둔 묶음과 스크롤 위치</b>를 함께 저장해야 합니다. 페이지네이션은 주소에 쪽 번호만 담으면 되지만, 무한 스크롤에서는 이 일을 직접 구현해야 합니다."),
  ]),
  plat_lede="모바일 앱에서는 무한 스크롤이 사실상 기본 방식이고, 웹에서는 목록의 쓰임에 따라 쓸지 말지가 갈립니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div class="mini__bg"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;bottom:8px;display:grid;place-items:center"><span class="spn spn--sm" style="width:9px;height:9px;border-width:1.5px"></span></div>', bars="", label="웹 무한 스크롤 재현"),
     "<code>IntersectionObserver</code>로 직접 만듭니다. 푸터와 뒤로가기 문제 때문에 자동 로드 대신 <b>더 보기</b> 버튼을 쓰는 제품이 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:5px"><div style="height:8px;border-radius:3px;background:var(--line)"></div><div style="height:8px;border-radius:3px;background:var(--line)"></div></div><div style="position:absolute;left:0;right:0;bottom:24px;text-align:center"><span style="font-size:7px;color:var(--fg-muted)">불러오는 중…</span></div>', "iOS 이어서 불러오기 재현"),
     "목록이 끝에 가까워지면 <b>다음 묶음을 더 가져오는 것이 기본</b>입니다. 목록 맨 위에서 아래로 당겨 새 항목을 받는 <b>당겨 새로고침</b>과 함께 씁니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:5px"><div style="height:8px;border-radius:3px;background:var(--line)"></div><div style="height:8px;border-radius:3px;background:var(--line)"></div></div><div style="position:absolute;left:0;right:0;bottom:24px;text-align:center"><span class="spn spn--sm" style="width:10px;height:10px;border-width:1.5px"></span></div>', "안드로이드 Paging 재현"),
     "<b>Paging 라이브러리</b>가 표준입니다. 커서 기반으로 이어 붙이는 기능과 재시도, 끝 처리가 라이브러리에 들어 있습니다."),
  ]),
  plat_note="\"무한 스크롤로 해 주세요\"라는 요청은 앱에서는 기본값을 쓰자는 말이지만, <b>웹에서는 뒤로가기로 보던 자리에 돌아오는 것과 푸터를 포기한다</b>는 뜻이 됩니다. 결제나 주문처럼 다시 찾아올 일이 있는 목록에서는 이 손해가 크므로, 목록의 쓰임부터 따져 보고 정해야 합니다.",
  siblings=siblings("infinite"),
  related='''        <li><span class="na"><b>가상 스크롤</b><em>10부</em></span></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>당겨 새로고침</b><em>9부</em></span></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
