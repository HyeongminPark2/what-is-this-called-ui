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
  desc="낙관적 UI가 무엇이고 스피너·프로그레스와 어떻게 다른지, 되돌림까지 실물과 상태와 해부도로 보여주는 항목.",
  lede="서버 응답을 <b>기다리지 않고 먼저 화면을 바꾸는</b> 방식. 거의 성공할 일에 쓰고, 실패하면 <b>되돌립니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>'서버를 느리게'를 켜고 별을 눌러 보세요.</b> 느낌이 똑같습니다 — 기다림이 사용자 쪽에서 사라졌기 때문입니다.
          <b>세 번째 줄(권한 없음)</b>은 서버가 거절해서 별이 원래대로 <b>되돌아가고</b> 이유를 알려 줍니다.
          이 되돌림을 감당할 수 있는 일에만 쓸 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "낙관적 UI, 낙관적 업데이트, 선반영"),
    ("영어", "optimistic UI, optimistic update"),
    ("같이 쓰는 말", "먼저 바꾼 화면을 <b>낙관적 상태</b>, 서버가 거절해 되돌리는 것을 <b>롤백</b>이라 합니다. 반대말은 <b>비관적</b>(pessimistic) — 응답을 받고 나서 바꾸는 쪽입니다."),
    ("자주 잘못 부름",
     "<b>캐싱</b> — 캐시는 <b>읽기</b>를 빠르게 하고, 낙관적 UI는 <b>쓰기</b>를 빠르게 보이게 합니다.<br>"
     "<b>즉시 반영</b> — 통하기는 하지만 <b>되돌림이 핵심</b>이라는 점이 빠집니다.<br>"
     "<b>로컬 상태</b> — 그냥 화면 상태를 바꾸는 것과 달리, 낙관적 UI는 <b>서버에 보낸 뒤 결과를 맞춰야</b> 합니다."),
  ]),
  axes=WAIT,
  oneline="낙관적 UI는 기다림을 <b>없애는</b> 쪽입니다. 그래서 '어떻게 보여 줄까'가 아니라 <b>'실패하면 어떻게 되돌릴까'</b>가 설계의 전부입니다.",
  states=states([
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:var(--fg-faint)">★</div>', bars="68", label="누르기 전"), "누르기 전", "꺼진 상태"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:15px;color:#f0a500">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--accent);font-weight:800">0ms — 벌써 바뀜</div>', bars="68", label="누른 직후 바로 바뀐 모습"), "누른 직후", "<b>0ms.</b> 스피너가 없다. 이게 이 방식의 전부다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500;opacity:.7">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--fg-muted)">서버에 보내는 중</div>', bars="68", label="보류 중인 모습"), "보류 중", "아주 옅게만 표시한다. <b>눈에 띄면 기다리게 된다</b>"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:#1f8a4c;font-weight:700">확정</div>', bars="68", label="서버가 받아들인 모습"), "확정", "<b>아무 일도 안 일어난다.</b> 이미 맞는 화면이라서"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:var(--fg-faint)">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--danger);font-weight:700">되돌림</div>' + toast("권한이 없어 되돌렸습니다", "다시 시도"), bars="68", label="거절당해 되돌아간 모습"), "되돌림", "원래대로 돌아가고 <b>이유를 알려 준다</b>. 소리 없이 되돌리면 안 된다"),
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:13px;color:#f0a500;opacity:.55">★</div><div style="position:absolute;left:6px;top:30px;font-size:7px;color:var(--warn);font-weight:700">연결 끊김 · 보류</div>', bars="68", label="오프라인에서 보류된 모습"), "오프라인", "보내지 못한 채 쌓아 둔다. 연결되면 보낸다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("먼저 바뀐 화면", "optimistic state", "서버는 아직 모른다. 사용자만 결과를 보고 있다"),
    ("보류 표시", "pending", "아주 약하게. 눈에 띄면 결국 기다리게 되어 쓰는 뜻이 없어진다"),
    ("되돌아간 값", "rollback", "<b>누르기 전 값을 기억해 뒀다가</b> 그대로 되돌린다"),
    ("되돌림 신호", "rollback cue", "조용히 바꾸면 사용자는 자기가 잘못 본 줄 안다. 짧게 흔들거나 색으로 알린다"),
    ("이유 알림", "reason", "왜 안 됐는지와 <b>다시 할 길</b>을 같이 준다. 보통 토스트로"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에 안 보이는 가장 중요한 것이 <b>기억해 둔 원래 값</b>입니다. 이게 없으면 되돌릴 수 없고,
          되돌릴 수 없으면 낙관적 UI를 쓸 수 없습니다.</p>''',
  do=ul([
    "거의 항상 성공하는 일 — 좋아요, 즐겨찾기, 체크, 순서 바꾸기",
    "되돌리는 비용이 싼 일 — 값 하나만 되돌리면 되는 것",
    "자주 반복하는 일 — 누를 때마다 기다리면 금세 지칩니다",
  ]),
  dont=ul([
    "실패가 잦은 일 — 되돌림이 자주 보이면 화면을 못 믿게 됩니다",
    "돈이 오가는 일 — 결제·이체는 <b>서버가 확정한 뒤</b> 보여 줍니다",
    "되돌리기 어려운 일 — 메일 발송, 파일 삭제처럼 바깥에 영향이 남는 것",
    "결과가 다른 화면에도 퍼지는 일 — 되돌릴 곳이 여러 군데면 금세 엉킵니다",
  ]),
  instead='확정을 기다려야 하면 <a href="spinner.html">스피너</a>나 <a href="progress.html">프로그레스 바</a>, 되돌릴 틈을 주려면 <a href="toast.html">되돌리기 토스트</a>, 실패를 알릴 때는 <a href="error.html">에러 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:14px;color:#f0a500">★</div>', bars="68", tall=False, label="즐겨찾기 재현"),
     "좋아요 · 즐겨찾기", "가장 떳떳한 자리. 틀려도 값 하나만 되돌리면 된다"),
    (mini('<div style="margin-top:8px;display:grid;gap:4px"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60" style="background:var(--accent-soft)"></div><div class="mini__bar mini__bar--w40"></div></div><div style="position:absolute;right:6px;top:22px;font-size:7px;color:var(--accent);font-weight:800">↕ 옮기는 중</div>', bars="", tall=False, label="순서 바꾸기 재현"),
     "순서 바꾸기", "끌어 놓은 자리에 바로 둔다. 거절당하면 제자리로 돌아간다"),
    (mini('<div style="margin-top:8px;display:grid;gap:5px"><div class="mini__bar mini__bar--w80"></div><div style="background:var(--accent-soft);border-radius:3px;padding:3px 5px;font-size:7px;color:var(--accent);opacity:.75">보내는 중…</div></div>', bars="", tall=False, label="메시지 선반영 재현"),
     "메시지 보내기", "말풍선을 먼저 띄우고 옅게 둔다. 실패하면 느낌표가 붙는다"),
  ]),
  code_lede="순서가 전부입니다 — <b>먼저 바꾸고, 보내고, 거절당하면 되돌린다.</b> 되돌릴 값을 먼저 챙기는 것이 첫 줄입니다.",
  code='''<span class="a">const</span> before = state.starred;       <span class="c">// 1) 되돌릴 값을 챙긴다</span>
setStarred(!before);                  <span class="c">// 2) 화면을 먼저 바꾼다</span>

<span class="a">try</span> <span class="a">{</span>
  <span class="a">await</span> api.star(id, !before);       <span class="c">// 3) 서버에 보낸다</span>
<span class="a">}</span> <span class="a">catch</span> (e) <span class="a">{</span>
  setStarred(before);                 <span class="c">// 4) 거절당하면 되돌린다</span>
  toast(<span class="s">'권한이 없어 되돌렸습니다'</span>, <span class="a">{</span> retry <span class="a">}</span>);   <span class="c">// 5) 이유를 알린다</span>
<span class="a">}</span>

<span class="c">// 빠르게 여러 번 누르면 응답이 뒤섞인다 — 마지막 것만 반영한다</span>
<span class="a">const</span> seq = ++latest;
<span class="a">if</span> (seq !== latest) <span class="a">return</span>;''',
  keys=kbd([
    ("누름", "<b>바로</b> 바뀐다. 포커스는 누른 자리에 그대로 둔다"),
    ("스크린 리더", "바뀐 상태를 <code>aria-pressed</code>로 알린다. 되돌릴 때는 라이브 리전으로 이유를 읽어 준다"),
    ("되돌릴 때", "<b>소리 없이 되돌리지 않는다.</b> 눈을 떼고 있던 사용자는 바뀐 줄도 모른다"),
    ("빠른 연타", "마지막 눌림만 반영한다. 응답이 뒤섞이면 화면과 서버가 어긋난다"),
    ("오프라인", "보류함에 쌓아 두고, 연결되면 보낸다. 쌓인 것이 있다는 표시를 남긴다"),
  ]),
  backend=rows([
    ("낙관적 UI = 낙관적 잠금과 같은 생각", "먼저 진행하고 충돌하면 되돌립니다. DB 의 optimistic locking 과 이름도 생각도 같습니다. <b>충돌이 드물 때만 이득</b>이라는 조건도 같습니다."),
    ("되돌림 = 보상 트랜잭션", "이미 보여 준 것을 물리는 일입니다. 사가(saga) 패턴의 보상 단계와 같아서, <b>보상할 수 없는 일에는 쓸 수 없습니다.</b>"),
    ("연타 = 순서 뒤섞임", "요청 두 개의 응답이 거꾸로 올 수 있습니다. 일련번호를 붙여 <b>마지막 것만</b> 반영합니다. 분산 시스템의 last-write-wins 와 같은 문제입니다."),
    ("멱등성", "같은 요청이 두 번 가도 결과가 같아야 재시도를 마음 놓고 합니다. 멱등 키를 붙이면 되돌림도 단순해집니다."),
    ("오프라인 = 아웃박스", "보내지 못한 변경을 쌓아 두는 큐입니다. 큐가 길어질수록 되돌림이 어려워지니 상한을 둡니다."),
  ]),
  plat_lede="낙관적 UI 는 모양이 아니라 <b>방식</b>이라서, 플랫폼 지침에 부품으로 실려 있지 않습니다.",
  plats=plats([
    ("웹", "부품이 아니라 방식",
     mini('<div style="margin-top:12px;text-align:right;padding-right:6px;font-size:14px;color:#f0a500">★</div>', bars="68", label="웹 낙관적 반영 재현"),
     "React Query·SWR 같은 도구가 <b>낙관적 업데이트와 롤백</b>을 거들어 줍니다. 이름은 그대로 씁니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:6px"><span style="flex:1;font-size:8px">즐겨찾기</span><span style="color:#f0a500;font-size:12px">★</span></div>', "iOS 즉시 반영 재현"),
     "지침은 '<b>기다리게 하지 말라</b>'고만 말합니다. 부품 이름은 없고, 되돌릴 때 <b>햅틱</b>으로 알리는 관례가 있습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:6px"><span style="flex:1;font-size:8px">즐겨찾기</span><span style="color:#f0a500;font-size:12px">★</span></div><div style="position:absolute;left:6px;right:6px;bottom:10px;background:#2e3238;border-radius:5px;padding:5px 7px;font-size:7.5px;color:#fff;display:flex;gap:5px"><span style="flex:1">되돌렸습니다</span><b style="color:#9ecaff">다시</b></div>', "안드로이드 되돌림 알림 재현"),
     "역시 부품이 아닙니다. 되돌림을 알릴 때 <b>스낵바</b>를 쓰는 것이 굳은 관례입니다."),
  ]),
  plat_note="이건 <b>디자인 부품이 아니라 구현 방식</b>이라 디자인 시안에는 잘 안 그려집니다. 그래서 \"왜 로딩이 없죠?\"라는 말이 나오기 쉽습니다. 시안에 <b>되돌림 상태</b>를 같이 그려 두면 그 오해가 줄고, 실패 처리를 빠뜨리는 일도 줄어듭니다.",
  siblings=siblings("optimistic"),
  related='''        <li><a href="toast.html"><b>되돌리기 토스트</b><em>6부</em></a></li>
        <li><span class="na"><b>비활성 · 읽기 전용</b><em>8부</em></span></li>
        <li><span class="na"><b>스위치</b><em>4부</em></span></li>
        <li><span class="na"><b>제스처</b><em>9부</em></span></li>''',
)
