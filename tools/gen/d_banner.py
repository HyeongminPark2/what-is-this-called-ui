# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def bn(items, label, note="", ok=None, w="152px", body=True):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for text, kind, x in items:
        if kind == 'warn':
            st = 'background:color-mix(in srgb, #9a6700 14%, var(--surface));color:#9a6700;'
        elif kind == 'err':
            st = 'background:color-mix(in srgb, var(--danger) 10%, var(--surface));color:var(--danger);'
        else:
            st = 'background:color-mix(in srgb, #0969da 10%, var(--surface));color:#0969da;'
        out.append('<span style="display:flex;gap:4px;align-items:center;padding:3px 6px;font-size:7.5px;'
                   + st + 'border-bottom:1px solid var(--line)">'
                   '<span style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + text + '</span>'
                   + ('<span style="margin-left:auto;opacity:.7">✕</span>' if x else '') + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            + ''.join(out)
            + ('<span style="display:grid;gap:3px;padding:5px 6px">'
               '<span style="display:block;height:5px;border-radius:2px;background:var(--bg)"></span>'
               '<span style="display:block;height:5px;width:70%;border-radius:2px;background:var(--bg)"></span>'
               '<span style="display:block;height:5px;width:85%;border-radius:2px;background:var(--bg)"></span></span>' if body else '')
            + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">화면 꼭대기에 떠 있지 않고 자리를 차지함</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">읽고 치울 때까지 사라지지 않음</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">'갱신하기' 같은 할 일 하나를 붙임</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">닫을 수 있고, 닫은 배너는 기억해 둠</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">쌓이면 내용보다 알림이 더 커짐</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">화면 전체의 사정만, 칸 하나는 인라인 얼럿으로</div>
                </div>
              </div>'''

D = dict(
  slug="banner", ko="배너", en="Banner",
  desc="화면 꼭대기에 자리를 차지하고 계속 남아 있는 알림입니다. 토스트와 어떻게 다른지, 여러 개가 쌓일 때와 닫을 때 무엇을 챙기는지 다룹니다.",
  lede="배너는 화면 꼭대기에 뜨는 알림으로, 토스트와 달리 저절로 <b>사라지지 않습니다</b>. 사용자가 닫을 때까지 남아 있기 때문에 다 읽은 뒤에는 <b>치울 수</b> 있어야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>배너가 여러 개 쌓이면 그만큼 화면 자리를 차지합니다. 배너 수를 늘려 보면
          데모가 <b>배너가 화면의 몇 %를 차지하는지</b> 재서 적어 줍니다.<br>
          <b>배너를 닫을 수 있게 하기</b>를 끄면 배너를 치울 방법이 없어 계속 남습니다. 또 닫은 배너를 <b>기억하지 않으면</b>
          새로 고칠 때마다 다시 뜨는데, 데모가 그렇게 다시 뜬 개수를 세어 보여 줍니다.<br>
          배너는 <b>화면 전체에 해당하는 사정</b>을 알리는 데 씁니다. 입력 칸 하나의 오류는
          <a href="inlinealert.html">인라인 얼럿</a>으로 알립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배너, 상단 알림, 공지 띠"),
    ("영어", "banner, message bar, notification banner"),
    ("같이 쓰는 말",
     "앱 전체에 해당하는 것은 <b>앱 배너</b>, 한 화면에만 해당하는 것은 <b>페이지 배너</b>라고 나눠 부릅니다. "
     "브라우저 화면에 뜨는 쿠키 동의 띠나 알림 허용 요청 띠도 배너라고 부릅니다. "
     "Material에는 M2 때 <b>Banner</b>라는 이름의 부품이 있었지만, "
     "M3에서는 <b>다른 방법을 쓰라</b>고 권합니다."),
    ("자주 잘못 부르는 이름",
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 <b>저절로 사라지지만</b>, 배너는 사용자가 닫을 때까지 남습니다.<br>"
     "<b>인라인 얼럿</b> — <a href=\"inlinealert.html\">인라인 얼럿</a>은 화면 전체가 아니라 <b>그 자리</b>에 해당하는 사정을 알립니다.<br>"
     "<b>광고 배너</b> — 같은 낱말을 쓰지만 알림 배너와는 <b>전혀 다른 것</b>입니다."),
  ]),
  states=states([
    (bn([("11월 15일 02:00~04:00 점검", "warn", True)], "", "하나면 알맞음", True),
     "배너가 하나일 때", "사용자가 <b>읽습니다</b>"),
    (bn([("점검 안내", "warn", True), ("새 정산 방식 안내", "info", True),
         ("사업자 정보 갱신", "warn", True), ("새 버전 안내", "info", True)], "", "내용보다 알림이 큼", False),
     "여러 개가 쌓였을 때", "여러 개가 쌓이면 <b>어느 것도 읽지 않습니다</b>"),
    (bn([("사업자 정보가 만료됐습니다 — 갱신하기", "warn", True)], "", "할 일이 붙어 있음", True),
     "할 일을 함께 붙였을 때", "사용자가 <b>무엇을 해야 하는지</b> 적습니다"),
    (bn([("점검 안내", "warn", False)], "", "닫을 수 없음", False),
     "닫기 버튼이 없을 때", "치울 수 없어서 <b>계속 남습니다</b>"),
    (bn([("결제가 실패해 서비스가 멈췄습니다", "err", False)], "", "닫으면 안 되는 배너도 있음", None),
     "서비스가 멈춘 사정을 알릴 때", "서비스가 멈춘 상황처럼 닫으면 안 되는 배너에는 <b>닫기를 두지 않습니다</b>"),
    (bn([], "", "다 읽고 치움", True),
     "배너를 다 치웠을 때", "배너를 다 닫으면 화면에 <b>내용만</b> 남습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자리", "화면 꼭대기", "화면 위에 <b>떠 있지 않고</b> 본문 위쪽 자리를 차지합니다"),
    ("남아 있는 시간", "치울 때까지", "저절로 사라지는 토스트와 <b>반대</b>입니다"),
    ("할 일", "하나만 붙임", "'갱신하기'처럼 할 일 하나를 붙입니다"),
    ("닫기", "꼭 둠", "사용자가 닫은 배너는 <b>기억</b>해 둡니다"),
    ("쌓임", "읽지 않게 됨", "두 개가 쌓이면 <b>둘 다</b> 읽지 않습니다"),
    ("범위", "화면 전체", "입력 칸 하나의 사정은 <b>인라인 얼럿</b>으로 알립니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          배너는 대개 비슷한 과정을 거쳐 늘어납니다.
          누군가 중요한 공지를 하나 올리고, 다음 달에 또 하나가 붙다 보면,
          반 년 뒤에는 <b>본문보다 배너 띠가 더 큰 화면</b>이 됩니다.
          그래서 배너를 만들 때 <b>언제 내릴지</b>를 처음부터 정해 두는 것이 좋습니다.
          예를 들어 점검 안내라면 점검이 끝나는 시각에 저절로 내려가게 합니다.<br>
          닫은 배너를 <b>기억하지 않으면</b> 사용자는 같은 배너를 들어올 때마다 닫아야 합니다.
          그러면 사용자에게 닫기 버튼은 '읽었다'는 표시가 아니라 <b>'또 떴네'</b> 하며 치우는 버튼이 됩니다.</p>''',
  do_title="배너를 알맞게 쓰는 경우",
  dont_title="배너를 잘못 쓰는 경우",
  do=ul([
    "한 번에 <b>하나만</b> 띄울 때",
    "<b>닫을 수 있게</b> 하고, 닫은 배너를 기억해 둘 때",
    "<b>언제 내릴지</b>를 처음부터 정해 둘 때",
  ]),
  dont=ul([
    "배너를 여러 개 <b>쌓을</b> 때. 두 개가 쌓이면 사용자는 둘 다 읽지 않습니다",
    "닫기 버튼을 <b>두지 않을</b> 때(서비스가 멈춘 경우는 예외)",
    "입력 칸 하나의 오류를 배너로 알릴 때. 오류는 <b>그 칸 옆</b>에 적습니다",
    "성공을 배너로 알릴 때. 성공은 <b>토스트</b>나 작업한 자리에서 알립니다",
  ]),
  instead='저절로 사라져도 되는 알림이면 <a href="toast.html">토스트</a>, 특정 자리에 해당하는 사정이면 <a href="inlinealert.html">인라인 얼럿</a>, 하던 일을 막아야 하면 <a href="modal.html">모달</a>, 나중에 모아 보는 알림이면 <a href="notifications.html">알림 센터</a>를 씁니다.',
  cases=cases([
    (bn([("11월 15일 02:00~04:00 점검", "warn", True)], "", "", True, "150px", False), "정해진 기간의 점검 알리기", "정해진 <b>기간</b> 동안만 해당하는 사정을 알립니다"),
    (bn([("사업자 정보 갱신이 필요합니다", "warn", True)], "", "", True, "150px", False), "사용자가 처리할 일 알리기", "사용자가 처리하지 않으면 <b>서비스를 쓸 수 없게 되는</b> 일을 알립니다"),
    (bn([("새 버전이 나왔습니다 — 새로 고침", "info", True)], "", "", True, "150px", False), "새 버전 소식 알리기", "급하지 않은 소식이라 <b>눈에 덜 띄는 색</b>으로 띄웁니다"),
  ]),
  code_lede="<code>role=\"status\"</code>로 스크린 리더에 알리고 닫기 버튼을 답니다. 배너는 본문 위쪽 자리를 차지하므로 화면 위에 <b>떠 있게 만들지 않습니다</b>.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"banner banner--warn"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;!&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">p</span>&gt;사업자 정보가 만료되어 갱신이 필요합니다.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settings/business"</span>&gt;갱신하기&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"이 알림 닫기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 닫은 배너는 기억해 둔다. 기억하지 않으면 매번 다시 뜬다</span>
closeBtn.onclick = () =&gt; {
  localStorage.setItem(<span class="s">'banner:biz-expiry'</span>, <span class="s">'dismissed'</span>);
  banner.remove();
};''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "배너가 뜨면 스크린 리더가 <b>읽던 말을 마친 뒤</b> 배너를 읽어 줍니다"),
    ("Tab", "배너 안의 링크와 닫기 버튼으로 <b>포커스를 옮길 수 있어야</b> 합니다"),
    ("<code>aria-label</code>", "✕ 버튼에 <b>무엇을 닫는지</b> 적습니다"),
    ("배너가 뜰 때의 초점", "배너가 떠도 <b>초점을 옮기지 않습니다</b>. 초점이 옮겨 가면 하던 일이 끊깁니다"),
    ("마크업 안에서의 차례", "마크업에서 <b>본문보다 먼저</b> 둬야 스크린 리더도 배너를 먼저 읽습니다"),
    ("확인하는 방법", "배너를 닫고 <b>새로 고침</b>한 뒤 다시 뜨는지 봅니다"),
  ]),
  backend=rows([
    ("언제까지 띄울지 정하기", "<code>expires_at</code> 값을 두면 그 시각에 배너가 <b>저절로 내려가기</b> 때문에, 누군가 잊지 않고 직접 지울 필요가 없습니다."),
    ("누구에게 띄울지 정하기", "'사업자 정보 만료' 같은 배너는 해당하는 사용자에게만 띄웁니다. <b>모두에게</b> 띄우면 대부분의 사용자에게는 쓸모없는 띠가 됩니다."),
    ("닫은 기록을 계정별로 저장하기", "닫은 기록을 계정별로 저장하면 <b>다른 기기에서도</b> 그 배너가 다시 뜨지 않습니다."),
  ]),
  plat_lede="배너는 <b>웹에서 가장 흔하게</b> 쓰고, 앱 쪽 지침은 배너를 줄이는 추세입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     bn([("점검 안내", "warn", True)], "", "", True, "110px", False),
     "쿠키 동의 띠와 공지 띠로 익숙한 부품입니다. 웹에서는 배너가 <b>쉽게 쌓이는</b> 편입니다."),
    ("iOS", "정식 부품 없음",
     '''              <div class="phone" role="img" aria-label="iOS 상단 알림 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:20px;height:9px;border-radius:3px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:6px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "정식 부품이 없습니다. 중요한 사정은 <b>화면 내용 안에</b> 섞어 넣는 방식을 권합니다."),
    ("안드로이드", "M2 Banner (M3에서 뺌)",
     '''              <div class="phone" role="img" aria-label="안드로이드 배너 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:20px;height:12px;background:color-mix(in srgb,#9a6700 20%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "M2에 있던 Banner가 <b>M3에서는 빠졌습니다</b>. 남용되기 쉬운 부품이기 때문입니다."),
  ]),
  plat_note="Material이 <b>배너를 지침에서 뺀 이유</b>를 볼 만합니다. 배너는 만들기 쉬워서 자꾸 늘어나는데, 늘어날수록 사용자가 읽지 않게 되기 때문입니다. Material은 배너 대신 <b>알릴 내용을 화면 안에 섞어 넣는 방식</b>을 권합니다. 웹에서도 배너를 하나 더 올리고 싶을 때 <b>그 내용을 본문 어디에 적을 수 있는지</b> 먼저 찾아보면 배너가 늘어나는 것을 막을 수 있습니다.",
  siblings=siblings("banner"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="inlinealert.html"><b>인라인 얼럿</b><em>6부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="statecolor.html"><b>상태 색</b><em>2부</em></a></li>''',
)
