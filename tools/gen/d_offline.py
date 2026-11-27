# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">끊김 띠는 화면 맨 위에 한 줄로</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">쓴 내용은 사라지지 않게 쌓아 둠</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">쌓인 작업이 몇 건인지 보여 줌</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">받아 둔 내용은 계속 읽을 수 있게 둠</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">연결되면 저절로 보내고 알림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">그때마다 실패하면 쓴 글이 사라짐</div>
                </div>
              </div>'''

def scr(banner, kind, body, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if kind == 'on':
        bst = 'background:color-mix(in srgb, #1a7f37 12%, var(--surface));color:#1a7f37;border:1px solid color-mix(in srgb, #1a7f37 35%, transparent);'
    elif kind == 'off':
        bst = 'background:color-mix(in srgb, #9a6700 14%, var(--surface));color:#9a6700;border:1px solid color-mix(in srgb, #9a6700 35%, transparent);'
    else:
        bst = 'background:color-mix(in srgb, var(--danger) 10%, var(--surface));color:var(--danger);border:1px solid color-mix(in srgb, var(--danger) 35%, transparent);'
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:4px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">'
            + ('<span style="display:block;border-radius:4px;padding:3px 6px;font-size:7.5px;' + bst + '">' + banner + '</span>' if banner else '')
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def q(items):
    return ''.join('<span style="display:block;border:1px dashed var(--line);border-radius:3px;'
                   'padding:2px 5px;font-size:7.5px;color:var(--fg-muted)">⏳ ' + x + '</span>' for x in items)

D = dict(
  slug="offline", ko="오프라인", en="Offline handling",
  desc="연결이 끊겼을 때의 화면을 다룹니다. 쓴 것을 쌓아 두는 법과 읽기는 되게 두는 법, 다시 연결됐을 때의 처리를 보여 주는 항목입니다.",
  lede="오프라인 처리는 네트워크 연결이 끊긴 동안 화면이 어떻게 동작할지 정하는 일입니다. 끊긴 동안 사용자가 <b>쓴 내용이 사라지는 것</b>이 가장 큰 사고이므로, 쓴 내용은 쌓아 두었다가 연결되면 보냅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'연결됨'을 꺼 보세요. 끊긴 동안 저장을 누르면 방식에 따라 <b>쌓아 두거나</b>, <b>버튼을 못 누르게 막거나</b>,
          <b>누를 때마다 실패하는</b> 세 가지 가운데 하나가 일어납니다.
          데모는 <b>쌓인 작업 수</b>와 <b>헛되이 실패한 횟수</b>를 세서 적습니다.<br>
          다시 연결하면 쌓아 둔 작업이 <b>저절로 나갑니다</b>.
          '그때마다 실패'는 가장 흔하면서도 가장 나쁜 방식인데, 사용자가 쓴 글이 사라지기 때문입니다.
          그리고 연결이 <b>끊겨도 읽기는 되게</b> 두는 편이 낫습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오프라인, 연결 끊김, 오프라인 지원"),
    ("영어", "offline, offline-first, outbox, background sync"),
    ("같이 쓰는 말",
     "보내지 못한 작업을 모아 두는 곳은 <b>아웃박스</b>(outbox)나 <b>큐</b>라고 하고, "
     "연결되면 쌓인 작업을 저절로 보내는 것은 <b>백그라운드 동기화</b>라고 합니다. "
     "연결이 끊겨도 쓸 수 있게 만드는 설계는 <b>오프라인 퍼스트</b>(offline-first)라고 부르며, "
     "웹에서 이 일을 맡는 장치가 <b>서비스 워커</b>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>재시도</b> — <a href=\"retry.html\">재시도</a>는 <b>연결은 되어 있는데</b> 요청이 실패했을 때 다시 보내는 것입니다.<br>"
     "<b>캐시</b> — 캐시는 <b>빠르게 읽으려고</b> 데이터를 두는 것이고, 오프라인 처리는 <b>연결이 없을 때를 대비</b>하는 것입니다.<br>"
     "<b>에러 상태</b> — <a href=\"error.html\">에러 상태</a>는 연결 끊김을 포함해 여러 실패를 아우르는 더 넓은 말입니다."),
  ]),
  s4_title="상태", s4_hint="방식에 따라 쓴 내용이 남는지 사라지는지",
  states=states([
    (scr("● 연결됨", "on", '<span style="display:block;font-size:8px;color:var(--fg-muted)">바로 보냄</span>',
         "", "평소", True),
     "연결되어 있을 때", "평소처럼 바로 보냅니다"),
    (scr("● 연결이 끊겼습니다 — 쌓아 뒀다가 보냅니다", "off", q(["메모 1", "메모 2"]), "", "2건이 기다리는 중", True),
     "끊긴 동안 쌓아 둘 때", "쓴 내용을 쌓아 두므로 <b>사라지지 않습니다</b>"),
    (scr("● 연결됨 — 쌓인 2건을 보내는 중", "on",
         '<span style="display:block;font-size:8px;color:var(--fg-muted)">저절로 보냄</span>', "", "복구됨", True),
     "다시 연결됐을 때", "쌓아 둔 작업이 <b>저절로</b> 나갑니다"),
    (scr("● 연결이 끊겼습니다", "off",
         '<span style="display:block;border:1px solid var(--line);border-radius:4px;padding:2px 6px;'
         'font-size:7.5px;color:var(--fg-faint);text-align:center">메모 저장 (꺼짐)</span>', "", "아예 누를 수 없음", None),
     "버튼을 막아 둘 때", "<b>헛수고는 없지만</b> 끊긴 동안에는 쓸 수 없습니다"),
    (scr("● 보내지 못했습니다", "err",
         '<span style="display:block;font-size:8px;color:var(--danger)">쓴 글이 사라짐</span>', "", "가장 나쁜 방식", False),
     "누를 때마다 실패할 때", "사용자가 <b>쓴 내용을 잃습니다</b>"),
    (scr("● 연결이 끊겼습니다", "off",
         '<span style="display:block;font-size:8px">받아 둔 목록은 볼 수 있음</span>', "", "읽기는 됨", True),
     "끊긴 동안 읽을 때", "연결이 <b>끊겨도</b> 받아 둔 목록은 보입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("끊김 띠", "맨 위 한 줄", "보내기가 <b>왜 안 되는지</b> 알립니다"),
    ("쌓아 두기", "쓴 내용", "쓴 내용이 <b>사라지지 않게</b> 쌓아 둡니다"),
    ("쌓인 건수", "건수 표시", "보내기를 기다리는 작업이 있다는 것을 알립니다"),
    ("읽기", "끊겨도 허용", "이미 받아 둔 내용은 보여 줍니다"),
    ("다시 연결", "저절로 보냄", "쌓인 작업을 보낸 뒤 보냈다고 <b>알립니다</b>"),
    ("그때마다 실패", "쓴 글이 사라짐", "누를 때마다 실패하면 <b>쓴 글이 사라집니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>연결이 있는지 없는지</b>는 생각보다 판단하기 어렵습니다.
          <code>navigator.onLine</code>은 '랜선이 꽂혀 있다' 정도만 알려 줄 뿐
          <b>인터넷이 실제로 되는지</b>는 알지 못합니다.
          예를 들어 지하철에서 안테나는 떠 있는데 아무것도 열리지 않는 상태가 있습니다.
          그래서 <b>요청이 실패했다는 사실</b>을 끊김의 신호로 삼는 편이 더 정확합니다.<br>
          쌓아 둔 작업을 보낼 때는 <b>순서</b>가 중요합니다.
          '만들기' 뒤에 '고치기'가 있었다면 그 순서대로 보내야 하고,
          중간에 하나가 실패하면 <b>그 뒤의 작업은 보내면 안 됩니다</b>.</p>''',
  do=ul([
    "끊긴 동안 쓴 내용을 <b>쌓아 두었다가</b> 연결되면 보낼 때",
    "끊긴 동안에도 <b>읽기는 되게</b> 둘 때. 이미 받아 둔 내용은 보여 줍니다",
    "쌓인 작업이 <b>몇 건인지</b> 보여 줄 때",
  ]),
  dont=ul([
    "끊긴 동안 쓴 글을 <b>버릴 때</b>",
    "<code>navigator.onLine</code>만 믿을 때. 연결된 것으로 <b>나와도 실제로는 안 될</b> 수 있습니다",
    "연결이 끊겼다고 <b>읽기까지</b> 막을 때",
    "쌓인 작업을 <b>순서 없이</b> 한꺼번에 보낼 때",
  ]),
  instead='연결은 되어 있는데 요청이 실패하는 경우는 <a href="retry.html">재시도</a> 항목에서, 실패 화면은 <a href="error.html">에러 상태</a> 항목에서 다룹니다. 기다리는 동안 보여 줄 표시는 <a href="spinner.html">스피너</a>에, 실패를 알리는 문구는 <a href="errortext.html">오류 문구</a>에 정리되어 있습니다.',
  do_title="연결이 끊겼을 때 지킬 것", dont_title="연결이 끊겼을 때 피할 것", instead_title="함께 보면 좋은 항목",
  cases=cases([
    (scr("● 연결이 끊겼습니다", "off", q(["메모 1"]), "", "", True), "끊긴 동안 쓴 메모 쌓아 두기", "끊긴 동안 쓴 메모를 <b>쌓아 둡니다</b>"),
    (scr("", "on", '<span style="display:block;font-size:8px">받아 둔 목록 12건</span>', "", "", True),
     "끊긴 동안 받아 둔 목록 읽기", "연결이 <b>끊겨도</b> 받아 둔 목록을 읽을 수 있습니다"),
    (scr("● 연결이 끊겨 결제를 시작할 수 없습니다", "off",
         '<span style="display:block;font-size:7.5px;color:var(--fg-muted)">연결되면 다시 눌러 주세요</span>', "", "", None),
     "결제는 쌓아 두지 않고 막기", "결제는 <b>쌓아 두었다가 나중에 보내면 안 되는</b> 일입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="요청이 실패하면 그것을 신호로 삼아 작업을 쌓아 두고, 연결되면 <b>순서대로</b> 보냅니다.",
  code='''<span class="c">&lt;!-- 끊김 띠는 화면 꼭대기에 한 줄 --&gt;</span>
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">class</span>=<span class="s">"offline-bar"</span>&gt;
  연결이 끊겼습니다 — 쓴 것은 쌓아 뒀다가 보냅니다 (2건)
&lt;/<span class="t">p</span>&gt;

<span class="t">async function</span> send(job) {
  <span class="t">try</span> { <span class="t">await</span> api.post(job); }
  <span class="t">catch</span> (e) {
    outbox.push(job);              <span class="c">// 실패를 신호로 삼는다</span>
    render();
  }
}

<span class="t">window</span>.addEventListener(<span class="s">'online'</span>, <span class="t">async</span> () =&gt; {
  <span class="t">while</span> (outbox.length) {
    <span class="t">await</span> api.post(outbox[<span class="a">0</span>]);   <span class="c">// 차례대로</span>
    outbox.shift();
  }
  announce(<span class="s">'쌓아 둔 2건을 보냈습니다'</span>);
});''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "연결 끊김과 복구를 <b>스크린 리더로도</b> 알립니다"),
    ("버튼을 막을 때", "버튼을 막는다면 <b>왜 꺼졌는지</b>도 함께 적습니다"),
    ("<code>online</code>·<code>offline</code>", "브라우저가 보내 주는 신호지만 <b>정확하지는 않습니다</b>"),
    ("<code>navigator.onLine</code>", "'랜선이 꽂혔다'는 것만 알 뿐 <b>인터넷이 실제로 되는지는 모릅니다</b>"),
    ("서비스 워커를 쓸 때", "탭이 닫혀도 쌓인 작업을 <b>나중에</b> 보낼 수 있게 해 줍니다"),
    ("확인하는 방법", "개발자 도구에서 네트워크를 <b>Offline</b>으로 바꾸고 직접 써 봅니다"),
  ]),
  backend=rows([
    ("멱등 키로 중복 전송 막기", "쌓아 둔 작업을 보내다 보면 같은 요청이 <b>두 번 가는 일</b>이 생기는데, 멱등 키가 있으면 서버가 한 번만 처리합니다."),
    ("쌓인 작업의 순서 지키기", "작업에 <code>created_at</code>이나 순번이 있어야 <b>만든 뒤 고친</b> 순서가 지켜집니다."),
    ("끊긴 동안 생긴 충돌 정리하기", "끊긴 동안 다른 사람이 같은 항목을 고쳤다면 <b>어느 쪽 변경을 남길지</b> 정해야 합니다."),
    ("읽기 캐시를 바뀐 것만 갱신하기", "목록 응답에 <code>ETag</code>가 있으면 <b>바뀐 것만</b> 받아 올 수 있습니다."),
  ]),
  plat_lede="오프라인 대비는 웹보다 <b>네이티브 앱 쪽이 훨씬 잘 갖춰져</b> 있습니다.",
  plats=plats([
    ("웹", "서비스 워커",
     scr("● 연결이 끊겼습니다", "off", q(["메모 1"]), "", "", True, "110px"),
     "탭이 열려 있어야 동작한다는 한계가 있고, 백그라운드 동기화 지원은 <b>브라우저마다</b> 다릅니다."),
    ("iOS", "로컬 저장 + 동기화",
     '''              <div class="phone" role="img" aria-label="iOS 오프라인 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;height:7px;border-radius:2px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱에 <b>자체 저장소</b>가 있어서 연결이 끊겨도 그대로 쓸 수 있습니다. 서버와의 동기화는 직접 만듭니다."),
    ("안드로이드", "Room + WorkManager",
     '''              <div class="phone" role="img" aria-label="안드로이드 오프라인 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;height:7px;border-radius:2px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>앱이 꺼져 있어도</b> 연결되면 OS가 대신 보내 주는데, 웹에는 이런 장치가 없습니다."),
  ]),
  plat_note="네이티브 앱은 처음부터 <b>자체 저장소를 갖추고</b> 시작하기 때문에 '끊기면 못 쓴다'는 일이 드뭅니다. 반대로 웹은 <b>연결되어 있는 것이 기본</b>이라서 끊김에 대비하려면 품이 많이 듭니다. 그래서 웹에서는 <b>쓴 내용만은 잃지 않게</b> 하는 데까지를 현실적인 목표로 잡는 편이 낫습니다. 그것만 해도 연결이 끊겼을 때 사용자가 겪는 가장 큰 문제인, 쓴 내용을 잃는 일은 막을 수 있습니다.",
  siblings=siblings("offline"),
  related='''        <li><a href="retry.html"><b>재시도</b><em>8부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="stale.html"><b>오래된 데이터</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>''',
)
