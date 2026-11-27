# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT = table(
  ["끝나는 때를 아나", "들어올 자리를 잡나", "사용자가 기다리나", "화면이 덜컥거리나"],
  [["스피너", "모른다", "안 잡는다", "기다린다", "덜컥거린다"],
   ["스켈레톤", "모른다", "잡는다", "기다린다", "안 덜컥거린다"],
   ["프로그레스 바", "안다", "잡기도 한다", "기다린다", "안 덜컥거린다"],
   ["낙관적 UI", "해당 없음", "잡는다", "안 기다린다", "안 덜컥거린다"]],
  me="낙관적")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:10px">
                <div style="display:grid;gap:14px">
                  <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:11px 26px;display:flex;align-items:center;gap:26px">
                    <span style="flex:1;font-size:11px;color:var(--fg-muted)">누른 직후</span>
                    <span class="pin-out" data-pin="1" style="color:#f0a500;font-size:16px;line-height:1">★</span>
                    <span class="pin-tr" data-pin="2" style="font-size:9.5px;color:var(--fg-faint)">보냄</span>
                  </div>
                  <div style="background:var(--surface);border:1px solid color-mix(in srgb,var(--danger) 40%,transparent);border-radius:8px;padding:11px 26px;display:flex;align-items:center;gap:26px">
                    <span style="flex:1;font-size:11px;color:var(--fg-muted)">서버가 거절</span>
                    <span class="pin-out" data-pin="3" style="color:var(--fg-faint);font-size:16px;line-height:1">★</span>
                    <span class="pin-tr" data-pin="4" style="font-size:9.5px;color:var(--danger);font-weight:700">되돌림</span>
                  </div>
                  <div data-pin="5" style="background:var(--ink-900);color:#fff;border-radius:6px;padding:9px 26px;display:flex;align-items:center;gap:26px;font-size:11px">
                    <span style="flex:1">권한이 없어 되돌렸습니다</span>
                    <span style="color:#8fc3ff;font-weight:800">다시 시도</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="optimistic", ko="낙관적 UI", en="Optimistic UI",
  desc="낙관적 UI가 무엇인지, 스피너·프로그레스 바와는 어떻게 다른지를 되돌림까지 포함해 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="낙관적 UI는 서버 응답을 <b>기다리지 않고 화면부터 먼저 바꾸는</b> 방식입니다. 거의 항상 성공하는 일에 쓰고, 서버가 거절하면 바꾼 화면을 <b>되돌립니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>'서버를 느리게'를 켜고 별을 눌러 보세요.</b> 서버가 느려져도 누를 때의 느낌은 똑같습니다. 화면이 서버 응답을 기다리지 않기 때문에 사용자는 기다림을 겪지 않습니다.
          <b>세 번째 줄(권한 없음)</b>은 서버가 거절하므로 별이 원래대로 <b>되돌아가고</b>, 되돌린 이유를 알려 줍니다.
          낙관적 UI는 이렇게 되돌려도 문제가 없는 일에만 쓸 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "낙관적 UI, 낙관적 업데이트, 선반영"),
    ("영어", "optimistic UI, optimistic update"),
    ("같이 쓰는 말", "응답을 기다리지 않고 먼저 바꾼 화면은 <b>낙관적 상태</b>, 서버가 거절해서 원래대로 되돌리는 것은 <b>롤백</b>이라고 부릅니다. 반대로 응답을 받은 뒤에 화면을 바꾸는 방식은 <b>비관적</b>(pessimistic) 방식이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>캐싱</b> — 캐시는 <b>읽기</b>를 빠르게 하고, 낙관적 UI는 <b>쓰기</b>가 빨라 보이게 합니다.<br>"
     "<b>즉시 반영</b> — 말은 통하지만, 실패했을 때 <b>되돌리는 처리가 핵심</b>이라는 점이 빠집니다.<br>"
     "<b>로컬 상태</b> — 화면 상태만 바꾸고 끝나는 로컬 상태와 달리, 낙관적 UI는 변경을 <b>서버에 보낸 뒤 응답에 맞춰 화면을 확정하거나 되돌려야</b> 합니다."),
  ]),
  axes=WAIT,
  oneline="스피너나 프로그레스 바가 기다림을 보여 주는 방법이라면, 낙관적 UI는 기다림을 <b>없애는</b> 방법입니다. 그래서 기다리는 동안 무엇을 보여 줄지보다 <b>실패하면 어떻게 되돌릴지</b>를 설계하는 데 대부분의 노력이 들어갑니다.",
  states=states([
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:var(--fg-faint)">★</div>', bars="68", label="누르기 전"), "누르기 전", "별이 꺼져 있습니다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:15px;color:#f0a500">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--accent);font-weight:800">0ms — 벌써 바뀜</div>', bars="68", label="누른 직후 바로 바뀐 모습"), "누른 직후", "누르자마자(<b>0ms</b>) 바뀌고 스피너가 뜨지 않습니다. 낙관적 UI를 쓰는 목적이 이 즉시 반응입니다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500;opacity:.7">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--fg-muted)">서버에 보내는 중</div>', bars="68", label="보류 중인 모습"), "보류 중", "서버에 보내는 중이라는 표시는 아주 옅게만 합니다. <b>표시가 눈에 띄면 사용자가 결국 기다리게 됩니다</b>"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:#1f8a4c;font-weight:700">확정</div>', bars="68", label="서버가 받아들인 모습"), "확정", "서버가 받아들여도 <b>화면에는 아무 변화가 없습니다.</b> 이미 맞는 화면을 보여 주고 있기 때문입니다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:var(--fg-faint)">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--danger);font-weight:700">되돌림</div>' + toast("권한이 없어 되돌렸습니다", "다시 시도"), bars="68", label="거절당해 되돌아간 모습"), "되돌림", "원래대로 돌아가면서 <b>되돌린 이유를 알려 줍니다</b>. 아무 알림 없이 되돌리면 안 됩니다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500;opacity:.55">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--warn);font-weight:700">연결 끊김 · 보류</div>', bars="68", label="오프라인에서 보류된 모습"), "오프라인", "보내지 못한 변경을 쌓아 두었다가 연결이 돌아오면 보냅니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("먼저 바뀐 화면", "optimistic state", "서버는 아직 변경을 받지 못했고, 사용자만 바뀐 결과를 보고 있습니다"),
    ("보류 표시", "pending", "아주 약하게 표시합니다. 눈에 띄면 사용자가 결국 응답을 기다리게 되어 낙관적 UI를 쓴 의미가 없어집니다"),
    ("되돌아간 값", "rollback", "<b>누르기 전 값을 기억해 두었다가</b> 그 값으로 되돌립니다"),
    ("되돌림 신호", "rollback cue", "아무 신호 없이 되돌리면 사용자는 자기가 잘못 본 줄 압니다. 짧게 흔들거나 색을 바꿔서 되돌렸다는 것을 알립니다"),
    ("이유 알림", "reason", "왜 실패했는지와 <b>다시 시도하는 방법</b>을 함께 알려 줍니다. 보통 토스트로 띄웁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않지만 낙관적 UI에서 특히 중요한 요소가 <b>기억해 둔 원래 값</b>입니다. 원래 값을 기억해 두지 않으면 서버가 거절했을 때 화면을 되돌릴 수 없고,
          되돌릴 수 없다면 낙관적 UI를 쓸 수 없습니다.</p>''',
  do=ul([
    "좋아요, 즐겨찾기, 체크, 순서 바꾸기처럼 거의 항상 성공하는 일을 처리할 때",
    "값 하나만 되돌리면 될 만큼 되돌리기 쉬운 일을 처리할 때",
    "자주 반복하는 일을 처리할 때. 누를 때마다 기다려야 하면 사용자가 금세 지칩니다",
  ]),
  dont=ul([
    "실패가 잦은 일을 처리할 때. 되돌림이 자주 보이면 사용자가 화면을 믿지 않게 됩니다",
    "결제나 이체처럼 돈이 오가는 일을 처리할 때. 결과는 <b>서버가 확정한 뒤</b> 보여 줍니다",
    "메일 발송이나 파일 삭제처럼 앱 바깥에 영향이 남아 되돌리기 어려운 일을 처리할 때",
    "결과가 다른 화면에도 반영되는 일을 처리할 때. 되돌릴 곳이 여러 군데면 상태가 금세 엉킵니다",
  ]),
  instead='확정을 기다려야 하면 <a href="spinner.html">스피너</a>나 <a href="progress.html">프로그레스 바</a>, 되돌릴 틈을 주려면 <a href="toast.html">되돌리기 토스트</a>, 실패를 알릴 때는 <a href="error.html">에러 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:14px;color:#f0a500">★</div>', bars="68", tall=False, label="즐겨찾기 재현"),
     "좋아요 · 즐겨찾기", "낙관적 UI를 가장 흔하게 쓰는 자리입니다. 실패해도 값 하나만 되돌리면 되기 때문입니다"),
    (mini('<div style="margin-top:8px;display:grid;gap:4px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60" style="background:var(--accent-soft)"></div><div class="mini__bar mini__bar--w40"></div></div><div style="position:absolute;right:6px;top:22px;font-size:7px;color:var(--accent);font-weight:800">↕ 옮기는 중</div>', bars="", tall=False, label="순서 바꾸기 재현"),
     "순서 바꾸기", "끌어다 놓은 자리에 항목을 바로 둡니다. 서버가 거절하면 항목이 원래 자리로 돌아갑니다"),
    (mini('<div style="margin-top:8px;display:grid;gap:5px"><div class="mini__bar mini__bar--w80"></div><div style="background:var(--accent-soft);border-radius:3px;padding:3px 5px;font-size:7px;color:var(--accent);opacity:.75">보내는 중…</div></div>', bars="", tall=False, label="메시지 선반영 재현"),
     "메시지 보내기", "말풍선을 먼저 띄워 옅게 두고, 전송에 실패하면 느낌표를 붙입니다"),
  ]),
  code_lede="구현할 때는 순서가 중요합니다. <b>화면을 먼저 바꾸고, 서버에 보내고, 거절당하면 되돌립니다.</b> 그리고 그보다 앞서, 되돌릴 때 쓸 원래 값을 챙겨 두는 일이 코드의 첫 줄에 옵니다.",
  code='''<span class="a">const</span> before = state.starred;       <span class="c">// 1) 되돌릴 값을 챙긴다</span>
setStarred(!before);                  <span class="c">// 2) 화면을 먼저 바꾼다</span>

<span class="a">try</span> <span class="a">{</span>
  <span class="a">await</span> api.star(id, !before);       <span class="c">// 3) 서버에 보낸다</span>
<span class="a">}</span> <span class="a">catch</span> (e) <span class="a">{</span>
  setStarred(before);                 <span class="c">// 4) 거절당하면 되돌린다</span>
  toast(<span class="s">'권한이 없어 되돌렸습니다'</span>, <span class="a">{</span> retry <span class="a">}</span>);   <span class="c">// 5) 이유를 알린다</span>
<span class="a">}</span>

<span class="c">// 빠르게 여러 번 누르면 응답이 뒤섞이므로 마지막 것만 반영한다</span>
<span class="a">const</span> seq = ++latest;
<span class="a">if</span> (seq !== latest) <span class="a">return</span>;''',
  keys=kbd([
    ("누름", "<b>바로</b> 바뀝니다. 포커스는 누른 자리에 그대로 둡니다"),
    ("스크린 리더", "바뀐 상태를 <code>aria-pressed</code>로 알립니다. 되돌릴 때는 라이브 리전으로 이유를 읽어 줍니다"),
    ("되돌릴 때", "<b>알림 없이 되돌리지 않습니다.</b> 화면에서 눈을 떼고 있던 사용자는 값이 되돌아간 줄도 모릅니다"),
    ("빠른 연타", "마지막으로 누른 것만 반영합니다. 응답 순서가 뒤섞이면 화면과 서버의 값이 어긋나기 때문입니다"),
    ("오프라인", "보내지 못한 변경은 보류함에 쌓아 두었다가 연결되면 보냅니다. 보류함에 쌓인 변경이 있다는 표시를 화면에 남깁니다"),
  ]),
  backend=rows([
    ("낙관적 UI = 낙관적 잠금과 같은 생각", "일단 진행하고 충돌이 나면 되돌린다는 점에서 DB의 optimistic locking과 이름도 발상도 같습니다. <b>충돌이 드물 때만 이득</b>이라는 조건도 같습니다."),
    ("되돌림 = 보상 트랜잭션", "되돌림은 이미 보여 준 결과를 취소하는 일이라서 사가(saga) 패턴의 보상 단계와 같습니다. 그래서 사가와 마찬가지로 <b>보상할 수 없는 일에는 쓸 수 없습니다.</b>"),
    ("연타 = 순서 뒤섞임", "빠르게 두 번 누르면 두 요청의 응답이 보낸 순서와 거꾸로 도착할 수 있습니다. 그래서 요청에 일련번호를 붙여 <b>마지막 것만</b> 반영합니다. 분산 시스템의 last-write-wins와 같은 문제입니다."),
    ("멱등성", "같은 요청이 두 번 가도 결과가 같아야 안심하고 재시도할 수 있습니다. 요청에 멱등 키를 붙여 두면 되돌리는 처리도 단순해집니다."),
    ("오프라인 = 아웃박스", "오프라인 보류함은 보내지 못한 변경을 쌓아 두는 큐입니다. 큐가 길어질수록 실패했을 때 되돌리기가 어려워지므로 쌓을 수 있는 양에 상한을 둡니다."),
  ]),
  plat_lede="낙관적 UI는 화면 부품이 아니라 <b>구현 방식</b>이라서 플랫폼 지침에 부품으로 실려 있지 않습니다.",
  plats=plats([
    ("웹", "부품이 아니라 방식",
     mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:14px;color:#f0a500">★</div>', bars="68", label="웹 낙관적 반영 재현"),
     "React Query나 SWR 같은 라이브러리가 <b>낙관적 업데이트와 롤백</b> 기능을 제공합니다. 이름도 낙관적 업데이트라고 그대로 씁니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:6px"><span style="flex:1;font-size:8px">즐겨찾기</span><span style="color:#f0a500;font-size:12px">★</span></div>', "iOS 즉시 반영 재현"),
     "지침에는 '<b>사용자를 기다리게 하지 말라</b>'는 말만 있고 따로 정한 부품 이름은 없습니다. 되돌릴 때 <b>햅틱</b>으로 알리는 관례가 있습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:6px"><span style="flex:1;font-size:8px">즐겨찾기</span><span style="color:#f0a500;font-size:12px">★</span></div><div style="position:absolute;left:6px;right:6px;bottom:10px;background:#2e3238;border-radius:5px;padding:5px 7px;font-size:7.5px;color:#fff;display:flex;gap:5px"><span style="flex:1">되돌렸습니다</span><b style="color:#9ecaff">다시</b></div>', "안드로이드 되돌림 알림 재현"),
     "안드로이드에서도 따로 정한 부품은 없습니다. 되돌림을 알릴 때는 <b>스낵바</b>를 쓰는 것이 자리 잡은 관례입니다."),
  ]),
  plat_note="낙관적 UI는 <b>디자인 부품이 아니라 구현 방식</b>이라서 디자인 시안에 잘 그려지지 않습니다. 그래서 시안을 본 사람에게서 \"왜 로딩이 없죠?\"라는 질문이 나오기 쉽습니다. 시안에 <b>되돌림 상태</b>를 함께 그려 두면 이런 오해가 줄고, 개발할 때 실패 처리를 빠뜨리는 일도 줄어듭니다.",
  siblings=siblings("optimistic"),
  related='''        <li><a href="toast.html"><b>되돌리기 토스트</b><em>6부</em></a></li>
        <li><span class="na"><b>비활성 · 읽기 전용</b><em>8부</em></span></li>
        <li><span class="na"><b>스위치</b><em>4부</em></span></li>
        <li><span class="na"><b>제스처</b><em>9부</em></span></li>''',
)
