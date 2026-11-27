# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

OFF = table(
  ["쓴 것이 남나", "읽기는 되나", "언제 나가나", "사용자가 아나"],
  [["쌓아 두기", "<b>남는다</b>", "받아 둔 것은 된다", "연결되면 저절로", "띠로 알린다"],
   ["못 누르게 막기", "해당 없음", "된다", "다시 눌러야", "<b>단추가 꺼져 있다</b>"],
   ["그때마다 실패", "<b>사라진다</b>", "된다", "다시 써야", "오류만 뜬다"],
   ["아무 대비 없음", "사라진다", "<b>안 된다</b>", "—", "화면이 빈다"]],
  me="오프라인")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">끊김 띠 — 화면 꼭대기에 한 줄</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">쓴 것은 쌓아 둔다 — 사라지지 않게</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">쌓인 것이 몇 건인지 보인다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">읽기는 되게 — 받아 둔 것은 보여 준다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">연결되면 저절로 나가고 알린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">그때마다 실패하면 쓴 글이 사라진다</div>
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
  desc="연결이 끊겼을 때의 화면. 쌓아 두기, 읽기는 되게 두기, 다시 연결됐을 때.",
  lede="끊긴 동안 <b>쓴 것이 사라지면</b> 그게 가장 큰 사고입니다. 쌓아 뒀다가 연결되면 보냅니다.",
  axes_lede="연결이 끊겼을 때 다루는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'연결됨'을 꺼 보세요. 끊긴 동안 저장을 누르면 셋 중 하나가 일어납니다 —
          <b>쌓아 두거나</b>, <b>못 누르게 막거나</b>, <b>그때마다 실패하거나</b>.
          데모가 <b>쌓인 작업 수</b>와 <b>헛되이 실패한 횟수</b>를 세서 적습니다.<br>
          다시 연결하면 쌓아 둔 것이 <b>저절로 나갑니다</b>.
          '그때마다 실패'는 가장 흔하면서 가장 나쁜 쪽입니다 — 쓴 글이 사라지니까요.
          <b>읽기는 끊겨도 되게</b> 두는 편이 낫습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오프라인, 연결 끊김, 오프라인 지원"),
    ("영어", "offline, offline-first, outbox, background sync"),
    ("같이 쓰는 말",
     "보내지 못한 작업을 모아 두는 곳을 <b>아웃박스</b>(outbox)나 <b>큐</b>라 하고, "
     "연결되면 저절로 보내는 것을 <b>백그라운드 동기화</b>라 합니다. "
     "끊겨도 쓸 수 있게 만드는 설계를 <b>오프라인 퍼스트</b>(offline-first)라 부르고, "
     "웹에서 그걸 맡는 장치가 <b>서비스 워커</b>입니다."),
    ("자주 잘못 부름",
     "<b>재시도</b> — <a href=\"retry.html\">재시도</a>는 <b>연결은 있는데</b> 실패했을 때입니다.<br>"
     "<b>캐시</b> — 캐시는 <b>빠르게 하려고</b> 두는 것이고, 오프라인은 <b>없을 때를 대비</b>하는 것입니다.<br>"
     "<b>에러 상태</b> — <a href=\"error.html\">에러 상태</a>는 더 넓은 말입니다."),
  ]),
  axes=OFF,
  oneline="<b>쓴 것은 절대로 잃지 마세요.</b> 보내는 것은 나중에 해도 됩니다.",
  s4_title="상태", s4_hint="쓴 것이 남는지가 갈린다",
  states=states([
    (scr("● 연결됨", "on", '<span style="display:block;font-size:8px;color:var(--fg-muted)">바로 보낸다</span>',
         "", "평소", True),
     "연결됨", "평소대로"),
    (scr("● 연결이 끊겼습니다 — 쌓아 뒀다가 보냅니다", "off", q(["메모 1", "메모 2"]), "", "2건이 기다린다", True),
     "끊김 · 쌓아 둠", "<b>안 사라진다</b>"),
    (scr("● 연결됨 — 쌓인 2건을 보내는 중", "on",
         '<span style="display:block;font-size:8px;color:var(--fg-muted)">저절로 나간다</span>', "", "복구", True),
     "다시 연결", "<b>저절로</b> 나간다"),
    (scr("● 연결이 끊겼습니다", "off",
         '<span style="display:block;border:1px solid var(--line);border-radius:4px;padding:2px 6px;'
         'font-size:7.5px;color:var(--fg-faint);text-align:center">메모 저장 (꺼짐)</span>', "", "아예 못 누른다", None),
     "막기", "<b>헛수고는 없지만</b> 못 쓴다"),
    (scr("● 보내지 못했습니다", "err",
         '<span style="display:block;font-size:8px;color:var(--danger)">쓴 글이 사라졌다</span>', "", "가장 나쁜 쪽", False),
     "그때마다 실패", "<b>쓴 것을 잃는다</b>"),
    (scr("● 연결이 끊겼습니다", "off",
         '<span style="display:block;font-size:8px">받아 둔 목록은 볼 수 있다</span>', "", "읽기는 된다", True),
     "읽기", "<b>끊겨도</b> 보인다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("끊김 띠", "꼭대기 한 줄", "<b>왜 안 되는지</b>를 알린다"),
    ("쌓아 두기", "쓴 것", "<b>사라지지 않게</b>"),
    ("몇 건인지", "보이기", "기다리는 것이 있다는 신호"),
    ("읽기", "되게 두기", "받아 둔 것은 보여 준다"),
    ("다시 연결", "저절로", "나갔다고 <b>알린다</b>"),
    ("그때마다 실패", "가장 나쁨", "<b>쓴 글이 사라진다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>연결이 있다 없다</b>는 생각보다 흐릿합니다 —
          <code>navigator.onLine</code> 은 '랜선이 꽂혀 있다' 정도만 알려 주고,
          <b>인터넷이 실제로 되는지</b>는 모릅니다.
          지하철에서 안테나는 떠 있는데 아무것도 안 되는 상태가 그것입니다.
          그래서 <b>요청이 실패한 것</b>을 신호로 삼는 편이 더 정확합니다.<br>
          쌓아 둔 것을 보낼 때는 <b>차례</b>가 중요합니다 —
          '만들기' 뒤에 '고치기'가 있었다면 그 순서대로 나가야 하고,
          중간에 하나가 실패하면 <b>뒤엣것을 보내면 안 됩니다</b>.</p>''',
  do=ul([
    "쓴 것을 <b>쌓아 두고</b> 연결되면 보내기",
    "<b>읽기는 되게</b> 두기 — 받아 둔 것은 보여 준다",
    "쌓인 것이 <b>몇 건인지</b> 보여 주기",
  ]),
  dont=ul([
    "끊긴 동안 쓴 글을 <b>버리기</b>",
    "<code>navigator.onLine</code> 만 믿기 — <b>떠 있어도 안 될</b> 수 있다",
    "끊겼다고 <b>읽기까지</b> 막기",
    "쌓인 것을 <b>차례 없이</b> 한꺼번에 보내기",
  ]),
  instead='연결은 되는데 실패하면 <a href="retry.html">재시도</a>, 실패 화면은 <a href="error.html">에러 상태</a>, 기다리는 표시는 <a href="spinner.html">스피너</a>, 문구는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (scr("● 연결이 끊겼습니다", "off", q(["메모 1"]), "", "", True), "메모 앱", "<b>쌓아 둔다</b>"),
    (scr("", "on", '<span style="display:block;font-size:8px">받아 둔 목록 12건</span>', "", "", True),
     "목록 보기", "<b>끊겨도</b> 읽힌다"),
    (scr("● 연결이 끊겨 결제를 시작할 수 없습니다", "off",
         '<span style="display:block;font-size:7.5px;color:var(--fg-muted)">연결되면 다시 눌러 주세요</span>', "", "", None),
     "결제", "<b>쌓아 두면 안 되는</b> 일"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 대비의 계약서",
  code_lede="실패를 신호로 삼아 쌓아 두고, 연결되면 <b>차례대로</b> 보냅니다.",
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
    ("<code>role=\"status\"</code>", "끊김과 복구를 <b>소리로도</b> 알린다"),
    ("단추 잠금", "막을 거라면 <b>왜 꺼졌는지</b>를 같이 적는다"),
    ("<code>online</code>·<code>offline</code>", "브라우저가 주는 신호. <b>정확하지는 않다</b>"),
    ("<code>navigator.onLine</code>", "'랜선이 꽂혔다'만 안다 — <b>인터넷은 모른다</b>"),
    ("서비스 워커", "탭이 닫혀도 <b>나중에</b> 보낼 수 있는 길"),
    ("확인하는 법", "개발자 도구에서 <b>Offline</b> 으로 바꾸고 써 본다"),
  ]),
  backend=rows([
    ("멱등 키", "쌓아 둔 것을 보낼 때 <b>두 번 가는 일</b>이 생깁니다 — 키가 있으면 한 번만 처리됩니다."),
    ("차례", "<code>created_at</code> 이나 순번이 있어야 <b>만든 뒤 고친</b> 차례가 지켜집니다."),
    ("충돌", "끊긴 동안 남이 같은 것을 고쳤으면 <b>어느 쪽을 남길지</b>를 정해야 합니다."),
    ("읽기 캐시", "목록에 <code>ETag</code> 가 있으면 <b>바뀐 것만</b> 받아 옵니다."),
  ]),
  plat_lede="<b>앱 쪽이 훨씬 잘 되어</b> 있습니다.",
  plats=plats([
    ("웹", "서비스 워커",
     scr("● 연결이 끊겼습니다", "off", q(["메모 1"]), "", "", True, "110px"),
     "탭이 열려 있어야 하는 것이 한계입니다. 백그라운드 동기화는 <b>브라우저마다</b> 다릅니다."),
    ("iOS", "로컬 저장 + 동기화",
     '''              <div class="phone" role="img" aria-label="iOS 오프라인 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;height:7px;border-radius:2px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱이 <b>자기 저장소</b>를 가져 끊겨도 그대로 씁니다. 동기화는 직접 만듭니다."),
    ("안드로이드", "Room + WorkManager",
     '''              <div class="phone" role="img" aria-label="안드로이드 오프라인 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:22px;height:7px;border-radius:2px;background:color-mix(in srgb,#9a6700 25%,transparent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>앱이 꺼져 있어도</b> 연결되면 OS 가 대신 보냅니다 — 웹에는 없는 장치입니다."),
  ]),
  plat_note="앱은 <b>자기 저장소를 들고</b> 시작하니 '끊기면 못 쓴다'는 말 자체가 드뭅니다. 웹은 반대로 <b>연결이 기본</b>이라, 끊김 대비를 하려면 품이 많이 듭니다. 그래서 웹에서는 <b>쓴 것만은 잃지 않게</b> 하는 선까지를 현실적인 목표로 잡는 편이 낫습니다 — 그것만 해도 사용자가 겪는 가장 큰 고통이 사라집니다.",
  siblings=siblings("offline"),
  related='''        <li><a href="retry.html"><b>재시도</b><em>8부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="stale.html"><b>오래된 데이터</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>''',
)
