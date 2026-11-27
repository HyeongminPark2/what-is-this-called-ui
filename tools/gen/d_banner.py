# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">화면 꼭대기 — 자리를 차지한다(안 뜬다)</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">사라지지 않는다 — 읽고 치울 때까지</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">할 일 하나 — '갱신하기'</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">닫을 수 있어야 한다 · 닫은 것은 기억한다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">쌓이면 내용보다 알림이 커진다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">화면 전체에 걸린 사정만 — 칸 하나는 인라인 얼럿</div>
                </div>
              </div>'''

D = dict(
  slug="banner", ko="배너", en="Banner",
  desc="화면 꼭대기에 자리를 차지하고 남는 알림. 토스트와의 차이, 쌓임과 닫기.",
  lede="<b>사라지지 않습니다</b> — 토스트와 가장 크게 다른 점입니다. 그래서 읽고 <b>치울 수</b> 있어야 합니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>배너는 쌓이면 화면을 먹습니다. 수를 늘려 보세요 —
          데모가 <b>배너가 화면의 몇 %를 먹는지</b>를 재서 적습니다.<br>
          <b>닫을 수 있게</b>를 끄면 영영 남습니다. 그리고 닫은 것을 <b>기억하지 않으면</b>
          새로 고칠 때마다 다시 뜹니다 — 데모가 그때 다시 뜬 개수를 셉니다.<br>
          배너는 <b>화면 전체에 걸린 사정</b>을 알립니다 — 칸 하나의 오류는
          <a href="inlinealert.html">인라인 얼럿</a>의 몫입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배너, 상단 알림, 공지 띠"),
    ("영어", "banner, message bar, notification banner"),
    ("같이 쓰는 말",
     "앱 전체에 걸리는 것은 <b>앱 배너</b>, 한 화면에만 걸리는 것은 <b>페이지 배너</b>라 가릅니다. "
     "브라우저가 띄우는 쿠키·알림 요청 띠도 배너라 부릅니다. "
     "Material 에는 <b>Banner</b> 라는 이름의 부품이 있었고(M2), "
     "M3 에서는 <b>대신 다른 방법을 쓰라</b>고 권합니다."),
    ("자주 잘못 부름",
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 <b>저절로 사라집니다</b>. 배너는 안 사라집니다.<br>"
     "<b>인라인 얼럿</b> — <a href=\"inlinealert.html\">인라인 얼럿</a>은 <b>그 자리</b>의 사정을 말합니다.<br>"
     "<b>광고 배너</b> — 같은 낱말이지만 <b>전혀 다른 것</b>입니다."),
  ]),
  axes=axis_table("배너"),
  oneline="<b>한 번에 하나만.</b> 둘이 쌓이는 순간 사람은 둘 다 안 읽습니다.",
  states=states([
    (bn([("11월 15일 02:00~04:00 점검", "warn", True)], "", "하나 — 알맞다", True),
     "하나", "<b>읽힌다</b>"),
    (bn([("점검 안내", "warn", True), ("새 정산 방식 안내", "info", True),
         ("사업자 정보 갱신", "warn", True), ("새 버전 안내", "info", True)], "", "내용보다 알림이 크다", False),
     "쌓임", "<b>둘 다 안 읽는다</b>"),
    (bn([("사업자 정보가 만료됐습니다 — 갱신하기", "warn", True)], "", "할 일이 붙어 있다", True),
     "할 일과 함께", "<b>무엇을 하라</b>고 적는다"),
    (bn([("점검 안내", "warn", False)], "", "닫을 수 없다", False),
     "닫기 없음", "<b>영영 남는다</b>"),
    (bn([("결제가 실패해 서비스가 멈췄습니다", "err", False)], "", "닫으면 안 되는 것도 있다", None),
     "막는 사정", "<b>닫기를 안 준다</b>"),
    (bn([], "", "다 읽고 치웠다", True),
     "다 치움", "<b>내용만</b> 남는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자리", "꼭대기", "<b>안 뜬다</b> — 자리를 차지한다"),
    ("안 사라짐", "치울 때까지", "토스트와 <b>반대</b>"),
    ("할 일", "하나", "'갱신하기'"),
    ("닫기", "있어야 함", "닫은 것은 <b>기억</b>한다"),
    ("쌓임", "위험", "둘이면 <b>둘 다</b> 안 읽는다"),
    ("범위", "화면 전체", "칸 하나는 <b>인라인 얼럿</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          배너가 늘어나는 과정은 늘 비슷합니다 —
          누군가 중요한 공지를 하나 올리고,
          다음 달에 또 하나가 붙고,
          반 년 뒤에는 <b>내용보다 띠가 큰 화면</b>이 됩니다.
          그래서 배너에는 <b>언제 사라지는지</b>를 처음부터 정해 두는 것이 좋습니다 —
          점검 안내라면 점검이 끝나는 시각에 저절로 내려가야 합니다.<br>
          닫은 것을 <b>기억하지 않으면</b> 사용자는 같은 띠를 매번 닫게 되고,
          그러면 닫기는 '읽었다'가 아니라 <b>'또 떴네'</b>라는 뜻이 됩니다.</p>''',
  do=ul([
    "한 번에 <b>하나만</b> 띄우기",
    "<b>닫을 수 있게</b> 하고 닫은 것은 기억하기",
    "<b>언제 사라지는지</b>를 처음부터 정해 두기",
  ]),
  dont=ul([
    "배너를 <b>쌓기</b> — 둘이면 둘 다 안 읽는다",
    "닫기를 <b>안 주기</b>(서비스가 멈춘 경우는 예외)",
    "칸 하나의 오류를 배너로 올리기 — <b>그 칸 옆</b>이 맞다",
    "성공을 배너로 알리기 — <b>토스트</b>나 그 자리가 맞다",
  ]),
  instead='저절로 사라지면 <a href="toast.html">토스트</a>, 그 자리의 사정이면 <a href="inlinealert.html">인라인 얼럿</a>, 막아야 하면 <a href="modal.html">모달</a>, 나중에 보는 것은 <a href="notifications.html">알림 센터</a>.',
  cases=cases([
    (bn([("11월 15일 02:00~04:00 점검", "warn", True)], "", "", True, "150px", False), "점검 안내", "<b>기간</b>이 있는 사정"),
    (bn([("사업자 정보 갱신이 필요합니다", "warn", True)], "", "", True, "150px", False), "할 일 알림", "<b>안 하면 막힌다</b>"),
    (bn([("새 버전이 나왔습니다 — 새로 고침", "info", True)], "", "", True, "150px", False), "버전 안내", "<b>조용한 색</b>으로"),
  ]),
  code_lede="<code>role=\"status\"</code> 로 알리고 닫기를 답니다. 자리를 차지하니 <b>뜨지 않습니다</b>.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"banner banner--warn"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;!&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">p</span>&gt;사업자 정보가 만료되어 갱신이 필요합니다.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settings/business"</span>&gt;갱신하기&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"이 알림 닫기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 닫은 것은 기억한다 — 안 그러면 매번 다시 뜬다</span>
closeBtn.onclick = () =&gt; {
  localStorage.setItem(<span class="s">'banner:biz-expiry'</span>, <span class="s">'dismissed'</span>);
  banner.remove();
};''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "뜰 때 <b>하던 말이 끝난 뒤</b> 읽어 준다"),
    ("Tab", "배너의 링크와 닫기로 <b>갈 수 있어야</b> 한다"),
    ("<code>aria-label</code>", "✕ 에 <b>무엇을 닫는지</b> 적는다"),
    ("초점", "배너로 <b>초점을 뺏지 않는다</b> — 하던 일이 끊긴다"),
    ("차례", "마크업에서 <b>본문보다 먼저</b> 둬야 소리로도 먼저 들린다"),
    ("확인하는 법", "닫고 <b>새로 고쳐</b> 다시 뜨는지 본다"),
  ]),
  backend=rows([
    ("언제까지", "<code>expires_at</code> 이 있으면 <b>저절로 내려갑니다</b> — 사람이 지우는 것을 잊지 않아도 됩니다."),
    ("누구에게", "'사업자 정보 만료'는 해당되는 사람에게만 — <b>모두에게</b> 띄우면 대부분에게 쓸모없는 띠입니다."),
    ("닫음 기록", "계정별로 저장하면 <b>다른 기기에서도</b> 안 뜹니다."),
  ]),
  plat_lede="<b>웹에서 가장 흔하고</b>, 앱 쪽은 줄이는 추세입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     bn([("점검 안내", "warn", True)], "", "", True, "110px", False),
     "쿠키 띠·공지 띠로 익숙합니다. <b>쌓이기 쉬운</b> 것도 웹의 특징입니다."),
    ("iOS", "없다",
     '''              <div class="phone" role="img" aria-label="iOS 상단 알림 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:20px;height:9px;border-radius:3px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:6px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "정식 부품이 없습니다. 중요한 사정은 <b>화면 안에</b> 섞어 넣는 쪽을 권합니다."),
    ("안드로이드", "M2 Banner (M3 에서 뺌)",
     '''              <div class="phone" role="img" aria-label="안드로이드 배너 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:20px;height:12px;background:color-mix(in srgb,#9a6700 20%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "M2 에 있던 Banner 가 <b>M3 에서는 빠졌습니다</b> — 남용되기 쉬워서입니다."),
  ]),
  plat_note="Material 이 <b>배너를 지침에서 뺀 것</b>은 눈여겨볼 만합니다 — 쓰기 쉬워서 자꾸 늘어나고, 늘어나면 아무도 안 읽기 때문입니다. 그 자리에 권하는 것은 <b>화면 안에 섞어 넣기</b>입니다. 웹에서도 '띠를 하나 더 올릴까'라는 생각이 들 때 <b>그 사정을 본문 어디에 쓸 수 있는지</b>를 먼저 보면, 배너가 늘어나는 것을 막을 수 있습니다.",
  siblings=siblings("banner"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="inlinealert.html"><b>인라인 얼럿</b><em>6부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="statecolor.html"><b>상태 색</b><em>2부</em></a></li>''',
)
