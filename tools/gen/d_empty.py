# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

KINDS = table(
  ["왜 비었나", "해야 할 말", "버튼", "그림"],
  [["처음", "아직 아무것도 안 만들었다", "<b>첫 걸음</b>을 알려 준다", "만들기 · 가져오기", "밝게, 기대감"],
   ["검색 결과 없음", "조건이 너무 좁다", "<b>조건을 푸는 길</b>", "조건 지우기 · 다시 찾기", "조용하게"],
   ["다 지움", "<b>잘 끝냈다</b>", "수고했다고 말한다", "처리한 것 보기 (선택)", "성공 색"],
   ["권한 없음", "볼 자격이 없다", "<b>누구에게 요청</b>할지", "관리자에게 요청", "잠금 느낌"]])

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;text-align:center;padding:22px 26px 24px">
                  <div data-pin="2" style="width:50px;height:50px;margin:0 auto 14px;border-radius:12px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:20px">＋</div>
                  <div class="pin-out" data-pin="3" style="font-size:13px;font-weight:750;margin-bottom:7px">아직 프로젝트가 없습니다</div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted);line-height:1.7;margin-bottom:14px">첫 프로젝트를 만들면 팀원을 부르고<br>지표를 모을 수 있습니다.</div>
                  <div style="display:flex;gap:26px;justify-content:center">
                    <span data-pin="5" style="background:var(--accent);color:#fff;border-radius:6px;padding:7px 14px;font-size:11px;font-weight:700">프로젝트 만들기</span>
                    <span data-pin="6" style="border:1px solid var(--line-strong);border-radius:6px;padding:7px 14px;font-size:11px;font-weight:700">가져오기</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="empty", ko="빈 상태", en="Empty state",
  desc="빈 상태가 무엇인지, 처음·검색 결과 없음·다 지움이 서로 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="빈 상태는 목록이나 화면에 <b>보여 줄 것이 하나도 없을 때 띄우는 화면</b>입니다. 비어 있는 이유가 경우마다 다르기 때문에 사용자에게 해야 할 말도 경우마다 다릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>세 가지를 번갈아 눌러 보세요.</b> 셋 다 "아무것도 없는 화면"이지만 사용자에게 하는 말은 전혀 다릅니다.
          처음 쓰는 사람에게는 <b>첫 걸음</b>을, 검색 결과가 없을 때는 <b>조건을 푸는 방법</b>을 알려 주고, 할 일을 다 지운 뒤에는 <b>잘 끝냈다</b>고 말합니다.
          세 경우를 모두 "데이터가 없습니다" 한 줄로 처리하면 어느 경우에도 사용자에게 도움이 되지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "빈 상태, 빈 화면, 공백 상태"),
    ("영어", "empty state, blank state, zero state"),
    ("같이 쓰는 말", "처음 쓰는 사람에게 보이는 빈 상태는 <b>제로 스테이트</b>나 <b>온보딩 빈 상태</b>라고 따로 부르기도 합니다. 가짜 데이터를 흐리게 깔아 두는 기법은 <b>고스트 콘텐츠</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>404</b> — 404는 <b>주소 자체가 없다</b>는 뜻입니다. 반면 빈 상태는 주소는 맞는데 그 안에 든 것이 없는 상태입니다.<br>"
     "<b>에러</b> — 비어 있다고 해서 무언가 잘못된 것은 아니므로 에러처럼 빨갛게 칠하면 안 됩니다.<br>"
     "<b>로딩</b> — 데이터가 아직 도착하지 않은 것과 <b>원래 없는 것</b>은 다릅니다. 불러오는 중에 빈 상태를 띄우면 사용자에게 사실과 다른 정보를 주게 됩니다."),
  ]),
  axes=KINDS,
  oneline="빈 상태에서 알려 줘야 할 것은 화면이 비었다는 사실보다 <b>왜 비었고 이제 무엇을 하면 되는지</b>입니다. 이 안내가 없으면 사용자는 그 화면에서 더 할 수 있는 일이 없습니다.",
  states=states([
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:9px">＋</span><span style="font-size:7.5px;font-weight:700">아직 없습니다</span><span class="mini__btn" style="font-size:7px;padding:2px 6px">만들기</span></div>', bars="", label="처음 빈 상태"), "처음", "첫 걸음을 알려 줍니다. 빈 상태 가운데 가장 공들일 가치가 있는 화면입니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:var(--bg);color:var(--fg-faint);display:grid;place-items:center;font-size:9px">⌕</span><span style="font-size:7.5px;font-weight:700">맞는 것이 없습니다</span><span style="font-size:6.5px;color:var(--fg-muted)">조건 두 개를 풀어 보세요</span></div>', bars="", label="검색 결과 없음"), "검색 결과 없음", "<b>무엇으로 찾았는지</b>를 다시 보여 주고, 조건을 푸는 방법을 알려 줍니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:#e4f4ea;color:#1f8a4c;display:grid;place-items:center;font-size:9px">✓</span><span style="font-size:7.5px;font-weight:700;color:#1f8a4c">다 처리했습니다</span><span style="font-size:6.5px;color:var(--fg-muted)">12건을 끝냈습니다</span></div>', bars="", label="다 지운 뒤"), "다 지움", "할 일을 모두 끝낸 결과이므로 빈 자리로 다루지 말고 <b>잘 끝냈다고 알려 줍니다</b>"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:var(--bg);color:var(--fg-faint);display:grid;place-items:center;font-size:9px">🔒</span><span style="font-size:7.5px;font-weight:700">볼 권한이 없습니다</span><span style="font-size:6.5px;color:var(--fg-muted)">관리자에게 요청</span></div>', bars="", label="권한 없음"), "권한 없음", "비어 보이지만 <b>비어 있는 원인이 다릅니다.</b> 누구에게 권한을 요청하면 되는지 알려 줍니다"),
    (mini('<div style="margin-top:8px;display:grid;gap:5px;opacity:.4"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:0;right:0;top:34px;text-align:center"><span class="mini__btn" style="font-size:7px;padding:2px 6px">첫 항목 만들기</span></div>', bars="", label="고스트 콘텐츠"), "고스트 콘텐츠", "가짜 데이터를 흐리게 깔아서 <b>내용이 채워지면 어떤 모습이 되는지</b> 보여 줍니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;font-size:7.5px;color:var(--fg-faint)">데이터가 없습니다</div>', bars="", label="할 말이 없는 빈 상태"), "하면 안 되는 것", "“데이터가 없습니다” 한 줄만 두면 사용자가 <b>다음에 할 일을 찾을 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자리", "container", "목록이 들어올 자리에 그대로 둡니다. 사용자를 다른 화면으로 보내지 않습니다"),
    ("그림", "illustration · icon", "화면의 분위기를 정합니다. 처음 쓰는 사람에게는 밝게, 검색 결과가 없을 때는 차분하게 그립니다"),
    ("제목", "title", "<b>왜 비었는지</b> 한 줄로 적습니다. '없습니다'로 끝내지 않습니다"),
    ("설명", "description", "다음에 무엇을 하면 되는지 적습니다. 두 줄을 넘기지 않습니다"),
    ("주 행동", "primary action", "<b>하나만</b> 둡니다. 이 화면에서 사용자가 가장 자연스럽게 이어 할 일을 고릅니다"),
    ("보조 행동", "secondary action", "주 행동 말고 다른 선택지입니다. 없어도 되고, 둔다면 하나까지만 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림은 <b>없어도 됩니다.</b> 관리 도구처럼 자주 보는 화면에서는 큰 그림이 볼 때마다 자리를 차지해 오히려 성가십니다.
          반대로 처음 쓰는 사람이 보는 화면이라면 그림에 공들일 만한 가치가 큽니다.</p>''',
  do=ul([
    "처음 쓰는 사람에게 <b>첫 걸음</b>을 알려 줄 때. 처음 빈 상태는 사용자가 제품을 처음 접하는 화면입니다",
    "검색이나 필터 결과가 없을 때 <b>무엇으로 찾았는지</b>와 조건을 푸는 방법을 보여 줄 때",
    "할 일을 다 끝내서 목록이 비었을 때. 비어 있다는 것이 곧 <b>일을 다 끝냈다</b>는 뜻입니다",
  ]),
  dont=ul([
    "세 경우를 같은 문구로 처리할 때. \"데이터가 없습니다\"는 어느 경우에도 도움이 되지 않습니다",
    "에러처럼 빨갛게 칠할 때. 비어 있다고 해서 잘못된 것은 아닙니다",
    "아직 불러오는 중일 때. 불러오는 동안에는 <b>스켈레톤</b>이나 스피너를 띄웁니다",
    "큰 그림만 두고 <b>다음에 할 일을 알려 주지 않을 때</b>. 보기에는 좋아도 사용자가 그 화면에서 할 수 있는 일이 없습니다",
  ]),
  instead='아직 불러오는 중이면 <a href="skeleton.html">스켈레톤</a>, 불러오다 실패했으면 <a href="error.html">에러 상태</a>, 방금 비운 것을 되돌릴 수 있으면 <a href="toast.html">되돌리기 토스트</a>.',
  cases=cases([
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:9px">＋</span><span style="font-size:7.5px;font-weight:700">아직 프로젝트가 없습니다</span><span class="mini__btn" style="font-size:7px;padding:2px 6px">만들기</span></div>', bars="", tall=False, label="처음 빈 상태 재현"),
     "처음", "버튼 하나만 둡니다. 고를 것이 많으면 사용자가 무엇부터 할지 몰라 첫 걸음을 떼기 어렵습니다"),
    (mini('<div style="margin-top:6px;padding:0 6px"><div style="border:1px solid var(--line-strong);border-radius:3px;padding:3px 5px;font-size:7px;color:var(--fg-muted)">“환불 대기”</div></div><div style="position:absolute;left:0;right:0;top:34px;text-align:center;padding:0 8px"><div style="font-size:7.5px;font-weight:700">맞는 것이 없습니다</div><div style="font-size:6.5px;color:var(--fg-muted);margin-top:3px">조건 두 개를 풀어 보세요</div></div>', bars="", tall=False, label="검색 결과 없음 재현"),
     "검색 결과 없음", "<b>검색한 말을 그대로 다시 보여 줍니다.</b> 그래야 사용자가 오타를 알아챕니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;padding:8px;text-align:center"><span style="width:18px;height:18px;border-radius:5px;background:#e4f4ea;color:#1f8a4c;display:grid;place-items:center;font-size:9px">✓</span><span style="font-size:7.5px;font-weight:700;color:#1f8a4c">다 처리했습니다</span></div>', bars="", tall=False, label="다 지운 뒤 재현"),
     "다 지움", "받은편지함을 모두 비웠을 때 보이는 화면입니다. 이 화면의 그림에 공들이는 제품이 많습니다"),
  ]),
  code_lede="마크업은 간단하고, 손이 가는 부분은 <b>세 가지(또는 네 가지) 경우를 가려내는 일</b>입니다. 불러오는 중인 상태와 비어 있는 상태를 같은 분기로 처리하면 불러오는 동안 빈 상태가 잘못 뜹니다.",
  code='''<span class="c">// 상태를 하나로 뭉치지 않고 경우마다 따로 분기한다</span>
<span class="a">if</span> (loading) <span class="a">return</span> &lt;Skeleton /&gt;;
<span class="a">if</span> (error)   <span class="a">return</span> &lt;ErrorState … /&gt;;
<span class="a">if</span> (!items.length) <span class="a">return</span> hasFilters
  ? &lt;Empty kind=<span class="s">"noResult"</span> query=<span class="a">{</span>q<span class="a">}</span> onClear=<span class="a">{</span>clear<span class="a">}</span> /&gt;
  : &lt;Empty kind=<span class="s">"first"</span> onCreate=<span class="a">{</span>create<span class="a">}</span> /&gt;;
<span class="a">return</span> &lt;List items=<span class="a">{</span>items<span class="a">}</span> /&gt;;

<span class="c">&lt;!-- 비어 있는 것은 에러가 아니다. role="alert" 를 붙이지 않는다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"empty"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">alt</span>=<span class="s">""</span>&gt;  <span class="c">&lt;!-- 장식 그림은 alt 를 비운다 --&gt;</span>
  &lt;<span class="t">h3</span>&gt;아직 프로젝트가 없습니다&lt;/<span class="t">h3</span>&gt;
&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "주 행동 버튼에 바로 닿아야 합니다. 빈 화면에서 누를 수 있는 것은 사실상 그 버튼뿐입니다"),
    ("스크린 리더", "제목을 <code>h2</code>나 <code>h3</code>로 두면 스크린 리더의 제목 목록에 나타나 바로 건너갈 수 있습니다"),
    ("장식 그림", "<code>alt=\"\"</code>로 비웁니다. 뜻을 담은 그림이라면 설명을 적습니다"),
    ("<code>role</code>", "빈 상태는 <b>경고가 아니므로</b> <code>role=\"alert\"</code>나 <code>status</code>를 붙이지 않습니다"),
    ("검색 결과 없음", "\"'환불 대기'에 맞는 것이 없습니다\"처럼 검색한 말을 제목에 넣어 함께 읽히게 합니다"),
  ]),
  backend=rows([
    ("빈 응답 ≠ 에러", "<code>200</code>과 빈 배열을 돌려주는 것이 정상입니다. 빈 목록을 <code>404</code>로 돌려주면 화면이 <b>빈 상태 대신 에러 화면을 띄웁니다.</b> 자주 하는 실수입니다."),
    ("왜 비었는지도 응답에", "필터 때문에 비었는지 원래 없는지는 <b>서버가 더 잘 압니다.</b> 응답에 <code>total</code>과 <code>filteredTotal</code>을 함께 주면 화면에서 두 경우를 가려낼 수 있습니다."),
    ("권한으로 빈 것", "<code>403</code>을 빈 목록으로 바꿔 돌려주면 사용자는 이유도 모른 채 빈 화면을 봅니다. <b>비어 있는 이유를 구분해서 응답에 담아 줍니다.</b>"),
    ("첫 사용자 지표", "처음 빈 상태는 가입 직후 거의 모든 사용자가 보는 화면입니다. 그래서 이 화면에서 떠나는 사용자의 비율이 제품 전체 이탈률에 바로 반영됩니다."),
  ]),
  plat_lede="빈 상태는 부품이라기보다 <b>화면 한 장</b>에 가깝기 때문에, 플랫폼 지침들도 모양보다 '무슨 말을 할지'를 주로 다룹니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;text-align:center;padding:8px"><span style="width:16px;height:16px;border-radius:4px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:8px">＋</span><span style="font-size:7px;font-weight:700">아직 없습니다</span></div>', bars="", label="웹 빈 상태 재현"),
     "<b>빈 상태</b> · 그림을 크게 넣는 제품이 많지만, 관리 도구에서는 글자만 두는 편이 보기 편합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;text-align:center;padding:10px"><span style="font-size:8.5px;font-weight:700">항목 없음</span><span style="font-size:7px;color:var(--fg-muted)">새로 추가해 보세요</span></div>', "iOS 빈 상태 재현"),
     "<b>글자 위주</b>로 구성합니다. 큰 그림보다 <b>짧은 제목과 한 줄 설명</b>을 권합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px;text-align:center;padding:10px"><span style="width:20px;height:20px;border-radius:6px;background:var(--accent-soft)"></span><span style="font-size:8px;font-weight:700">아직 없습니다</span><span style="background:var(--accent);color:#fff;border-radius:99px;padding:3px 9px;font-size:7.5px;font-weight:700">만들기</span></div>', "안드로이드 빈 상태 재현"),
     "<b>빈 상태</b>(Empty state) · 아이콘과 제목, 설명, 버튼으로 이루어진 구성을 지침에서 직접 보여 줍니다."),
  ]),
  plat_note="\"빈 화면 하나 만들어 주세요\"라는 요청에는 보통 <b>네 가지 경우가 한데 섞여</b> 있습니다. 처음·검색 결과 없음·다 지움·권한 없음 가운데 <b>어느 경우인지</b>를 먼저 가려야 문구와 버튼을 정할 수 있습니다. 경우를 가리지 않으면 \"데이터가 없습니다\" 한 줄로 끝나기 쉽습니다.",
  siblings=siblings("empty"),
  related='''        <li><span class="na"><b>빈 상태 문구</b><em>14부</em></span></li>
        <li><span class="na"><b>온보딩</b><em>13부</em></span></li>
        <li><span class="na"><b>검색과 결과</b><em>13부</em></span></li>
        <li><span class="na"><b>필터와 패싯</b><em>10부</em></span></li>''',
)
