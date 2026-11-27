# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">간격을 1 · 2 · 4 · 8초로 두 배씩 늘림</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">흔들기(jitter)로 요청이 몰리지 않게 함</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">다섯 번쯤 실패하면 자동 재시도를 멈춤</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">다시 보내도 되는 요청인지 먼저 확인함</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">몇 번째 시도인지, 언제 다시 보내는지 보여 줌</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">끝내 실패하면 다시 시도 버튼을 줌</div>
                </div>
              </div>'''

def track(bars, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = ''.join('<span style="display:block;width:5px;height:' + str(h) + 'px;border-radius:1px;background:'
                  + ('var(--accent)' if kind == 'ok' else 'color-mix(in srgb, var(--danger) 45%, transparent)')
                  + '"></span>' for h, kind in bars)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:3px;align-items:flex-end;height:30px;border-bottom:1px solid var(--line);'
            'border:1px solid ' + c + ';border-radius:6px;background:var(--surface);padding:4px 6px">' + out + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

D = dict(
  slug="retry", ko="재시도", en="Retry · backoff",
  desc="실패한 요청을 다시 보내는 방법을 다룹니다. 지수 백오프와 다시 보내도 되는 요청, 재시도를 사용자에게 보여 주는 방법을 보여 주는 항목입니다.",
  lede="재시도는 실패한 요청을 다시 보내는 것입니다. 멈춘 서버에 요청을 <b>쉬지 않고 계속 보내면</b> 부하가 쌓여 서버가 복구되기 더 어려워지므로, 다시 보내는 간격을 <b>두 배씩</b> 늘리는 것이 기본입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>서버가 잠깐 멈췄다가 돌아오는 상황이라고 가정해 보겠습니다. 실패하자마자 <b>바로바로</b> 다시 보내면
          짧은 시간에 요청이 수십 번 나가는데, 데모는 <b>보낸 횟수</b>와
          <b>마지막 간격</b>을 재서 적습니다.<br>
          <b>지수 백오프</b>는 간격을 1 · 2 · 4 · 8초로 늘립니다. 그러면 같은 시간 동안 보내는 횟수가 크게 줄면서도,
          서버가 돌아오면 금세 성공합니다. 재시도하는 동안에는
          언제 다시 시도하는지, 지금 몇 번째 시도인지를 <b>사용자에게도 보여 줘야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "재시도, 다시 시도, 백오프"),
    ("영어", "retry, exponential backoff, jitter"),
    ("같이 쓰는 말",
     "재시도 간격을 두 배씩 늘리는 것은 <b>지수 백오프</b>, 그 간격에 무작위 값을 섞어 "
     "여러 기기가 같은 순간에 몰리지 않게 하는 것은 <b>지터</b>(jitter)라고 합니다. "
     "같은 요청을 두 번 받아도 한 번만 처리되는 성질은 <b>멱등</b>(idempotent)이라고 하고, "
     "실패가 계속될 때 요청 자체를 끊는 장치는 <b>서킷 브레이커</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>새로 고침</b> — 새로 고침은 <b>사용자가 직접</b> 화면 전체를 다시 불러오는 것이고, 재시도는 실패한 요청 하나를 다시 보내는 것입니다.<br>"
     "<b>폴링</b> — 폴링은 <b>실패와 상관없이</b> 일정한 주기로 서버에 묻는 것입니다.<br>"
     "<b>오프라인 큐</b> — <a href=\"offline.html\">오프라인</a> 큐는 <b>연결이 없을 때</b> 요청을 쌓아 두는 것이고, 재시도는 연결된 상태에서 실패한 요청을 다시 보내는 것입니다."),
  ]),
  s4_title="상태", s4_hint="간격에 따라 달라지는 결과",
  states=states([
    (track([(8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f')],
           "바로바로", "짧은 시간에 수십 번 보냄", False),
     "쉬지 않고 다시 보낼 때", "<b>서버 부하를 더 키웁니다</b>"),
    (track([(10, 'f'), (10, 'f'), (10, 'f'), (10, 'f'), (10, 'ok')], "같은 간격", "1초마다 보냄", None),
     "같은 간격으로 보낼 때", "연결이 잠깐씩 짧게 끊길 때만 씁니다"),
    (track([(6, 'f'), (11, 'f'), (18, 'f'), (26, 'ok')], "지수 백오프", "1 · 2 · 4초 뒤 성공", True),
     "간격을 두 배씩 늘릴 때", "<b>대부분의 경우</b>에 씁니다"),
    (one(txt('<span style="display:block;font-size:8.5px">3번째 시도 중…</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">4초 뒤 다시 시도합니다</span>'),
         "사용자에게 보여 줌", True, "몇 번째인지, 언제 다시 보내는지", "152px"),
     "재시도 중임을 보여 줄 때", "재시도를 <b>사용자 모르게</b> 돌리지 않습니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--danger)">보내지 못했습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">다시 시도 ›</span>'),
         "끝내 실패", True, "사용자에게 버튼을 넘김", "152px"),
     "자동 재시도를 멈출 때", "자동 재시도를 멈추고 사용자에게 다시 시도 <b>버튼</b>을 줍니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">결제를 세 번 보냄</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">멱등 키가 없으면 세 번 결제됨</span>'),
         "위험", False, "", "152px"),
     "멱등하지 않은 요청을 다시 보낼 때", "멱등 키 없이 <b>다시 보내면 안 됩니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("간격", "두 배씩 늘림", "1 · 2 · 4 · 8초로 간격을 늘립니다"),
    ("흔들기", "무작위 섞기", "간격에 무작위 값을 섞어 여러 기기의 요청이 <b>한꺼번에 몰리지</b> 않게 합니다"),
    ("최대 횟수", "다섯 번쯤", "다섯 번쯤 실패하면 자동 재시도를 멈추고 사용자에게 넘깁니다"),
    ("다시 보내도 되는지 확인", "보내기 전에 확인", "다시 보내도 되는 요청인지 먼저 확인합니다. <b>결제는 멱등 키 없이 다시 보내면 안 됩니다</b>"),
    ("진행 상황 표시", "몇 번째 시도인지와 다음 시각", "몇 번째 시도인지, 언제 다시 보내는지 보여 줍니다"),
    ("자동 재시도 중단", "다시 시도 버튼", "다시 시도할지는 <b>사용자가</b> 정하게 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          다시 보내기 전에 <b>이 요청을 두 번 보내도 되는지</b> 꼭 확인해야 합니다.
          조회(GET)는 두 번 보내도 괜찮지만, <b>결제나 전송은 두 번 처리되면 사고</b>로 이어집니다.
          그래서 결제나 전송 요청에는 <b>멱등 키</b>를 붙여,
          서버가 같은 키를 두 번 받으면 한 번만 처리하게 해 둡니다.<br>
          <b>흔들기</b>가 없는 백오프도 문제를 일으킵니다.
          수천 대의 기기가 동시에 끊겼다면 모두 정확히 1초 뒤에 다시 보내게 되고,
          그 순간 몰린 요청 때문에 서버가 또 멈춥니다. 간격에 <b>무작위 값을 조금 섞으면</b>
          요청이 보내지는 시점이 흩어집니다.</p>''',
  do=ul([
    "재시도를 구현할 때. <b>지수 백오프에 흔들기</b>를 더한 방식을 기본으로 씁니다",
    "요청을 다시 보내기 전. 다시 보내도 되는 요청인지 <b>먼저</b> 확인합니다",
    "재시도하는 동안. 지금 <b>몇 번째 시도인지</b> 보여 줍니다",
  ]),
  dont=ul([
    "쉬지 않고 다시 보낼 때. <b>서버 부하를 더 키웁니다</b>",
    "결제나 전송 요청을 <b>멱등 키 없이</b> 다시 보낼 때",
    "끝없이 다시 보낼 때. <b>다섯 번쯤</b>에서 멈춥니다",
    "사용자에게 알리지 않고 재시도할 때. 사용자는 화면이 <b>멈춘 줄</b> 압니다",
  ]),
  instead='연결이 아예 없을 때의 처리는 <a href="offline.html">오프라인</a> 항목에서, 실패 화면은 <a href="error.html">에러 상태</a> 항목에서 다룹니다. 기다리는 동안 보여 줄 표시는 <a href="spinner.html">스피너</a>에, 실패를 알리는 문구는 <a href="errortext.html">오류 문구</a>에 정리되어 있습니다.',
  do_title="재시도를 구현할 때 지킬 것", dont_title="재시도에서 피할 것", instead_title="함께 보면 좋은 항목",
  cases=cases([
    (track([(6, 'f'), (11, 'f'), (18, 'ok')], "목록 받기", "", True), "목록을 뒤에서 다시 받아 오기", "사용자에게 따로 묻지 않고 뒤에서 다시 받아 옵니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--danger)">보내지 못했습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">다시 시도 ›</span>'),
         "폼 보내기", True, "", "150px"),
     "폼을 다시 보낼지 사용자에게 맡기기", "다시 보낼지는 <b>사용자에게</b> 맡깁니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">Idempotency-Key: 9fa3…</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">두 번 와도 한 번만 처리</span>'),
         "결제", True, "", "150px"),
     "결제 요청에 멱등 키 붙이기", "다시 보낼 때는 반드시 <b>멱등 키</b>를 붙입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="간격을 두 배씩 늘리고 무작위 값을 조금 섞습니다. 최대 횟수는 다섯 번이면 충분합니다.",
  code='''<span class="t">async function</span> withRetry(fn, { max = <span class="a">5</span> } = {}) {
  <span class="t">for</span> (<span class="t">let</span> n = <span class="a">0</span>; ; n++) {
    <span class="t">try</span> { <span class="t">return</span> <span class="t">await</span> fn(); }
    <span class="t">catch</span> (e) {
      <span class="t">if</span> (n &gt;= max || !canRetry(e)) <span class="t">throw</span> e;
      <span class="t">const</span> base = Math.min(<span class="a">8000</span>, <span class="a">1000</span> * <span class="a">2</span> ** n);
      <span class="t">const</span> jitter = base * (<span class="a">0.5</span> + Math.random() * <span class="a">0.5</span>);  <span class="c">// 흔들기</span>
      show(<span class="s">`${n + 2}번째 시도 — ${Math.round(jitter / 1000)}초 뒤`</span>);
      <span class="t">await</span> sleep(jitter);
    }
  }
}

<span class="c">// 두 번 보내면 안 되는 요청에는 열쇠를 붙인다</span>
fetch(<span class="s">'/pay'</span>, { headers: { <span class="s">'Idempotency-Key'</span>: orderKey } });''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "'3번째 시도 중'을 <b>스크린 리더로도</b> 알립니다"),
    ("다시 시도 버튼을 둘 때", "자동 재시도를 멈춘 뒤에는 <b>초점을 받을 수 있는</b> 다시 시도 버튼을 둡니다"),
    ("<code>aria-busy</code>", "다시 받아 오는 동안 그 자리에 붙입니다"),
    ("428 · 429 · 503", "<b>다시 보내도 되는</b> 응답 코드입니다"),
    ("400 · 401 · 404", "다시 보내도 <b>똑같이 실패</b>하므로 재시도하지 않습니다"),
    ("확인하는 방법", "네트워크를 끊었다 다시 켠 뒤 요청을 <b>몇 번 보냈는지</b> 셉니다"),
  ]),
  backend=rows([
    ("<code>Retry-After</code> 헤더로 간격 알려 주기", "서버가 이 헤더로 <b>언제 다시 보내라</b>고 알려 주면 화면에서 간격을 짐작할 필요가 없습니다."),
    ("멱등 키로 중복 처리 막기", "서버는 같은 키가 붙은 요청을 두 번 받으면 다시 처리하지 않고 <b>처음 결과</b>를 그대로 돌려줍니다."),
    ("오류 종류에 따라 다르게 대응하기", "<code>429</code>(요청이 너무 잦음)는 기다렸다가 다시 보내면 되지만 <code>400</code>(잘못된 요청)은 다시 보내도 실패하므로, 두 오류는 <b>전혀 다르게 대응</b>해야 합니다."),
    ("서킷 브레이커로 요청 잠시 끊기", "실패가 연달아 쌓이면 <b>잠시 요청 자체를 끊어서</b> 서버가 복구될 시간을 줍니다."),
  ]),
  plat_lede="재시도의 <b>원리는 플랫폼마다 같고</b>, 쓰는 라이브러리만 다릅니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     track([(6, 'f'), (11, 'f'), (18, 'ok')], "", "", True, "110px"),
     "<code>fetch</code> 자체에는 재시도 기능이 없지만, 데이터를 불러오는 쿼리 라이브러리들은 재시도를 <b>기본으로</b> 넣어 둡니다."),
    ("iOS", "URLSession · 직접",
     '''              <div class="phone" role="img" aria-label="iOS 재시도 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:7px;border-radius:2px;background:color-mix(in srgb, var(--danger) 35%, transparent)"></div></div></div>''',
     "<code>waitsForConnectivity</code>를 켜면 요청이 <b>연결될 때까지</b> 기다렸다가 나가게 할 수 있습니다."),
    ("안드로이드", "WorkManager",
     '''              <div class="phone" role="img" aria-label="안드로이드 재시도 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:7px;border-radius:2px;background:color-mix(in srgb, var(--danger) 35%, transparent)"></div></div></div>''',
     "<b>백오프까지 OS가</b> 맡아서, 앱이 꺼져 있어도 나중에 다시 보냅니다."),
  ]),
  plat_note="안드로이드의 <b>WorkManager</b>는 앱이 꺼진 뒤에도 재시도를 이어 가는 장치로, 웹에는 이런 장치가 없습니다. 웹에서 가장 비슷한 기능은 <b>서비스 워커의 백그라운드 동기화</b>인데, 아직 브라우저마다 지원 여부가 다릅니다. 그래서 웹에서는 <b>탭이 열려 있는 동안에만</b> 재시도가 돈다고 보는 편이 안전합니다. 중요한 요청은 <a href=\"offline.html\">오프라인</a> 항목처럼 <b>쌓아 두었다가 다음에 앱을 열었을 때</b> 보내도록 설계합니다.",
  siblings=siblings("retry"),
  related='''        <li><a href="offline.html"><b>오프라인</b><em>8부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="spinner.html"><b>스피너</b><em>8부</em></a></li>''',
)
