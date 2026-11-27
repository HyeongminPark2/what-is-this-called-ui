# -*- coding: utf-8 -*-
from parts import *
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:4px">
                <div data-pin="1" style="display:flex;flex-direction:column;gap:7px">
                  <div style="opacity:.3;background:var(--ink-900);border-radius:6px;padding:8px 12px;font-size:10.5px;color:#fff">먼저 띄운 토스트</div>
                  <div data-pin="2" style="position:relative;background:var(--ink-900);border-radius:6px;padding:12px 14px 16px;box-shadow:var(--e2)">
                    <div style="display:flex;align-items:center;gap:26px;margin-bottom:12px">
                      <span style="width:17px;height:17px;border-radius:50%;background:#2d6a44;color:#8ff0b5;font-size:9px;display:grid;place-items:center;flex:none">✓</span>
                      <span class="pin-out" data-pin="3" style="color:#fff;font-size:11.5px">“회고 문서 초안 쓰기”를 지웠습니다</span>
                    </div>
                    <div style="display:flex;align-items:center;justify-content:flex-end;gap:28px">
                      <span class="pin-out" data-pin="4" style="color:#8fc3ff;font-size:11.5px;font-weight:800">되돌리기</span>
                      <span data-pin="5" style="color:rgba(255,255,255,.6);font-size:13px;line-height:1">&times;</span>
                    </div>
                    <span class="pin-tr" data-pin="6" style="position:absolute;left:0;right:0;bottom:0;height:4px;background:rgba(255,255,255,.2);border-radius:0 0 6px 6px"><i style="display:block;width:62%;height:100%;background:#8fc3ff;border-radius:0 0 0 6px"></i></span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="toast", ko="토스트 · 스낵바", en="Toast · Snackbar",
  desc="토스트가 무엇인지, 모달·배너·인라인 얼럿과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="토스트는 화면 구석에 잠깐 떴다가 <b>저절로 사라지는</b> 알림입니다. 사용자가 하던 일을 막지 않는 대신 금방 사라지기 때문에, 사용자가 못 읽고 지나가도 문제가 없는 내용만 담아야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>항목 여러 개를 빠르게 지워 보세요.</b> 지울 때마다 토스트가 하나씩 떠서 위로 <b>쌓입니다</b>(스택). 토스트에 마우스를 올리면 타이머가 멈추고,
          <b>되돌리기</b>를 누르면 지운 항목이 원래 자리로 돌아옵니다.
          이렇게 되돌릴 수 있으면 지우기 전에 "정말 지울까요?"라고 묻는 확인 모달을 띄우지 않아도 됩니다.</p>
        </div>
        <div class="note note--warn touch-only" style="margin-bottom:0">
          <p><b>지금 보는 기기는 호버를 지원하지 않습니다.</b> 마우스를 올려 타이머를 멈출 수 없으므로, 터치 화면에서는
          토스트를 더 오래 띄우거나 되돌리기 버튼을 토스트 밖의 다른 자리에도 남겨 둬야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "토스트, 토스트 메시지, 스낵바"),
    ("영어", "toast, snackbar"),
    ("같이 쓰는 말", "되돌리기 같은 액션이 붙은 것을 <b>스낵바</b>, 글만 있는 것을 <b>토스트</b>로 나눠 부르기도 합니다. 이 구분은 Material 기준이고, 웹에서는 두 이름을 섞어 씁니다."),
    ("자주 잘못 부르는 이름",
     "<b>팝업</b> — 토스트는 뒤 화면을 막지 않고 저절로 사라지기 때문에 팝업과는 전혀 다른 부품입니다.<br>"
     "<b>알림</b> — 이렇게 부르면 운영체제가 띄우는 푸시 알림(notification)과 헷갈립니다. 토스트는 앱 화면 안에서만 뜹니다.<br>"
     "<b>얼럿</b> — 얼럿은 사용자의 답을 받으려고 화면을 막는 것이고, 토스트는 알리기만 합니다."),
  ]),
  axes=axis_table("토스트"),
  oneline="토스트인지 아닌지는 <b>저절로 사라지느냐</b>로 가릅니다. 사용자가 닫지 않아도 없어지기 때문에 <b>못 읽고 지나가도 되는 말만</b> 담을 수 있습니다.",
  states=states([
    (mini(trigger(), bars="486", label="토스트가 없는 목록 화면"), "토스트가 없을 때", "트리거만 보입니다"),
    (mini(toast("지웠습니다", "", "transform:translateY(8px);opacity:.45"), bars="486", label="토스트가 올라오는 중"), "아래에서 떠오르는 중", "0.2초 동안 아래에서 떠오릅니다"),
    (mini(toast("“회고 초안”을 지웠습니다"), bars="486", label="토스트가 표시된 모습"), "화면에 떠 있을 때", "메시지와 되돌리기 버튼 하나를 보여 줍니다"),
    (mini('<div class="mini__toast" style="bottom:22px;left:30px;opacity:.5">앞서 지운 것</div>' + toast("또 지웠습니다"), bars="486", label="토스트 두 개가 쌓인 모습"), "여러 개가 쌓였을 때", "여러 건을 큐로 다루고, 보통 3개까지만 쌓습니다"),
    (mini(toast("“회고 초안”을 지웠습니다") + '<div style="position:absolute;right:8px;bottom:30px;font-size:8px;color:var(--accent);font-weight:800">⏸ 멈춤</div>', bars="486", label="마우스를 올려 타이머가 멈춘 모습"), "마우스를 올려 타이머를 멈췄을 때", "마우스를 올려 두는 동안에는 사라지지 않아서 읽을 시간이 생깁니다"),
    (mini(toast("지웠습니다", "되돌리기", "opacity:.35;transform:translateY(5px)"), bars="486", label="토스트가 사라지는 중"), "사라지는 중", "토스트가 사라진 뒤에도 작업 결과는 화면에 남아 있어야 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스택", "stack · container", "토스트가 쌓이는 자리입니다. 여기에 <code>aria-live</code>를 걸어 둡니다"),
    ("토스트 몸통", "toast · snackbar", "알림 한 건을 담는 상자입니다. 보통 화면 폭의 절반을 넘기지 않습니다"),
    ("메시지", "message", "무엇이 끝났는지만 한 줄로 적습니다. 앞의 아이콘은 <b>상태 아이콘</b>인데, 색만으로 상태를 알리지 않으려고 모양을 함께 씁니다"),
    ("액션", "action", "하나만 둡니다. 되돌리기를 가장 많이 씁니다"),
    ("닫기", "dismiss", "토스트가 저절로 사라지더라도 사용자가 먼저 치울 수 있게 둡니다"),
    ("타이머 바", "timer · progress", "사라지기까지 얼마나 남았는지 보여 주고, 마우스를 올려 두면 멈춥니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않는 부분이 하나 더 있는데, <b>라이브 리전</b>(<code>aria-live</code>)입니다. 화면에는 나타나지 않지만
          스크린 리더에게 글이 새로 생겼다는 사실을 알려 주는 표시입니다.
          <a href="../index.html#toc">12부 접근성</a>에서 따로 다룹니다.</p>''',
  do=ul([
    "'저장했습니다', '보냈습니다', '지웠습니다'처럼 이미 끝난 일을 알릴 때",
    "되돌릴 수 있는 일을 알릴 때. <b>되돌리기를 붙이면 확인 모달을 띄우지 않아도 됩니다</b>",
    "못 읽고 지나가도 괜찮은 짧은 소식을 전할 때",
  ]),
  dont=ul([
    "사용자가 꼭 읽어야 하는 에러를 알릴 때. 인라인 얼럿이나 배너를 씁니다",
    "사용자의 답을 받아야 할 때. 토스트에는 선택지를 넣지 않고 모달을 씁니다",
    "긴 글이나 링크 여러 개를 담을 때. 다 읽기 전에 사라집니다",
    "중요한 정보를 토스트<b>에만</b> 담을 때. 토스트가 사라지면 다시 볼 방법이 없습니다",
  ]),
  instead='사용자가 꼭 읽어야 하는 내용이면 <a href="inlinealert.html">인라인 얼럿</a>이나 <a href="banner.html">배너</a>를 쓰고, 사용자의 답을 받아야 하면 <a href="modal.html">모달</a>을 씁니다. 누른 요소 바로 옆에 붙어 떠야 하면 <a href="popover.html">팝오버</a>가 맞습니다.',
  cases=cases([
    (mini(toast("“회고 초안”을 지웠습니다"), bars="684", tall=False, label="되돌리기 토스트 재현"),
     "지운 뒤 되돌리기 버튼 주기", "토스트를 가장 쓸모 있게 쓰는 형태입니다. 되돌릴 수 있으니 확인 모달을 띄우지 않아도 됩니다"),
    (mini('<div class="mini__toast" style="bottom:22px;left:30px;opacity:.55">2건 지웠습니다</div>' + toast("3건 지웠습니다"), bars="684", tall=False, label="쌓인 토스트 재현"),
     "빠르게 여러 번 지워 쌓일 때", "같은 작업을 빠르게 여러 번 하면 토스트가 포개지므로 쌓이는 개수에 상한을 둡니다"),
    (mini('<div class="mini__toast" style="background:#7a211c;left:18px"><span style="color:#ffb3ae">✕</span> 보내지 못했습니다<b style="color:#ffd2ce">다시 시도</b></div>', bars="684", tall=False, label="에러 토스트 재현"),
     "보내기 실패 알리기", "실패를 알리는 토스트는 저절로 사라지지 않게 두는 편이 안전합니다"),
  ]),
  code_lede="토스트는 포커스를 가져가지 않습니다. 포커스가 옮겨 가면 사용자가 하던 입력이 끊기기 때문입니다. 그 대신 스크린 리더에게는 <b>라이브 리전</b>으로 새 토스트를 알립니다.",
  code='''<span class="c">&lt;!-- 토스트가 쌓이는 자리는 페이지에 하나만 둔다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"toasts"</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;&lt;/<span class="t">div</span>&gt;

<span class="c">// 한 건을 넣되 포커스는 건드리지 않는다</span>
toasts.append(el);

<span class="c">// 마우스를 올리거나 포커스가 들어오면 타이머를 멈춰 읽을 시간을 준다</span>
el.addEventListener(<span class="s">'mouseenter'</span>, pause);
el.addEventListener(<span class="s">'focusin'</span>, pause);

<span class="c">// 되돌리기를 누를 때는 아직 실제로 지우지 않은 상태여야 한다 (아래 ⑨칸)</span>
undoBtn.addEventListener(<span class="s">'click'</span>, () =&gt; cancelPendingDelete(id));''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "토스트가 떠도 포커스가 토스트로 <b>곧바로 옮겨 가지 않습니다</b>. 포커스를 가져가면 하던 입력이 끊기기 때문입니다"),
    ("<kbd>Esc</kbd>", "포커스가 토스트 안에 있을 때 토스트를 닫습니다"),
    ("마우스를 올렸을 때", "타이머가 멈추고, 마우스를 치우면 남은 시간부터 다시 줄어듭니다"),
    ("스크린 리더로 읽을 때", "<code>aria-live=\"polite\"</code>로 두면 읽던 말을 끊지 않고 이어서 읽습니다. <code>assertive</code>는 읽던 말을 끊기 때문에 에러에만 씁니다"),
    ("화면에 띄워 두는 시간", "글자 수가 많을수록 길게 띄웁니다. 액션이 붙으면 최소 5초, 짧은 글도 4초 아래로는 내리지 않습니다"),
  ]),
  backend=rows([
    ("보내고 잊는 fire-and-forget 이벤트와 같음", "토스트는 보내고 나면 잊는 이벤트처럼 사용자가 받았는지 확인하지 않습니다. 그래서 <b>꼭 전달돼야 하는 내용은 토스트에 담으면 안 됩니다.</b>"),
    ("되돌리기는 커밋을 미루는 방식", "화면에는 '지웠습니다'라고 띄우지만 <b>실제 삭제는 5초 미룹니다.</b> soft delete와 보류 큐를 함께 쓰는 방식으로, 되돌리기를 누르면 큐에서 빼고 누르지 않으면 5초 뒤에 커밋합니다."),
    ("쌓이는 토스트는 큐로 관리", "짧은 시간에 여러 건이 들어오면 토스트가 포개지기 때문에 상한(보통 3개)과 오래된 것을 밀어내는 정책이 필요합니다. 로그에 레이트 리밋을 거는 것과 같은 문제입니다."),
    ("최대 한 번만 전달하는 at-most-once", "토스트는 '최대 한 번' 전달하는 방식이라서 사용자가 못 읽어도 다시 띄우지 않습니다. 반드시 읽혀야 하는 내용이라면 배너나 목록처럼 화면에 남는 통로를 따로 둡니다."),
  ]),
  plat_lede="토스트는 플랫폼마다 부르는 이름이 특히 많이 엇갈리는 부품입니다. 안드로이드에서는 '토스트'가 아예 다른 것을 가리킵니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini(toast("저장했습니다"), bars="684", label="웹 토스트 재현"),
     "<b>토스트</b> · 띄우는 자리는 제품마다 다른데, 오른쪽 아래가 가장 흔하고 가운데 위도 씁니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:14px;background:rgba(255,255,255,.92);border-radius:9px;padding:6px 8px;font-size:8.5px;color:#11131a;box-shadow:0 4px 12px rgba(0,0,0,.25)">저장했습니다</div>', "iOS 배너 재현"),
     "<b>표준 토스트가 없습니다.</b> 위에서 내려오는 <b>배너</b>나 화면 가운데 잠깐 뜨는 <b>HUD</b>로 비슷하게 만듭니다. 애플은 저절로 사라지는 알림을 권하지 않습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:6px;right:6px;bottom:10px;background:#2e3238;border-radius:5px;padding:6px 8px;font-size:8.5px;color:#fff;display:flex;gap:6px"><span style="flex:1">지웠습니다</span><b style="color:#9ecaff">실행 취소</b></div>', "안드로이드 스낵바 재현"),
     "<b>스낵바</b>(Snackbar) · 왼쪽 아래에 뜨고 액션을 하나 붙입니다. 이 부품을 <b>처음 내놓은 곳</b>이 Material입니다."),
  ]),
  plat_note="안드로이드에는 <b>Toast라는 다른 API</b>가 따로 있는데, 액션을 붙일 수 없고 포커스도 받지 못하는 더 단순한 시스템 알림입니다. 그래서 안드로이드 개발자에게 \"토스트에 되돌리기 붙여 주세요\"라고 하면 \"그건 스낵바\"라는 답이 돌아옵니다.",
  siblings=siblings("toast"),
  related='''        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>
        <li><a href="undo.html"><b>되돌리기</b><em>8부</em></a></li>
        <li><span class="na"><b>확인 요청의 수준</b><em>8부</em></span></li>
        <li><span class="na"><b>에러 4단</b><em>8부</em></span></li>''',
)
