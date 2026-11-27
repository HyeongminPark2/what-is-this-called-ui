# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

RT = table(
  ["누가 다시 보내나", "간격", "서버에 주는 부담", "언제 쓰나"],
  [["바로바로", "기계", "<b>거의 없음</b>", "<b>가장 크다</b>", "쓰지 않는다"],
   ["같은 간격", "기계", "1초 · 1초 · 1초", "중간", "짧게 끊길 때"],
   ["지수 백오프", "기계", "<b>1 · 2 · 4 · 8초</b>", "<b>작다</b>", "거의 늘 이쪽"],
   ["사람이 누르기", "<b>사람</b>", "사람 마음", "가장 작다", "자동이 실패한 뒤"]],
  me="지수 백오프")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">간격을 두 배씩 — 1 · 2 · 4 · 8초</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">흔들기(jitter) — 다 같이 몰리지 않게</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">최대 횟수 — 다섯 번쯤에서 멈춘다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">다시 보내도 되는 요청인지 먼저 본다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">사람에게 보여 준다 — 몇 번째, 언제 다시</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">끝내 실패하면 다시 시도 단추를 준다</div>
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
  desc="실패한 요청을 다시 보내는 방법. 지수 백오프, 다시 보내도 되는 요청, 사람에게 보여 주기.",
  lede="죽은 서버에 <b>쉬지 않고 몰아치면</b> 더 못 일어납니다. 간격을 <b>두 배씩</b> 늘리는 것이 기본입니다.",
  axes_lede="다시 보내는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>서버가 잠깐 죽었다 돌아온다고 칩시다. <b>바로바로</b> 다시 보내면
          짧은 시간에 요청이 수십 번 나갑니다 — 데모가 <b>보낸 횟수</b>와
          <b>마지막 간격</b>을 재서 적습니다.<br>
          <b>지수 백오프</b>는 1 · 2 · 4 · 8초로 간격을 늘립니다. 같은 시간에 보내는 횟수가 확 줄고,
          서버가 돌아오면 금세 성공합니다. 그리고 재시도가 도는 동안
          <b>사람에게도 보여 줘야</b> 합니다 — 언제 다시 시도하는지, 지금 몇 번째인지.</p>
        </div>''',
  names=rows([
    ("한국어", "재시도, 다시 시도, 백오프"),
    ("영어", "retry, exponential backoff, jitter"),
    ("같이 쓰는 말",
     "간격을 두 배씩 늘리는 것이 <b>지수 백오프</b>, 거기에 무작위를 섞어 "
     "여러 기기가 같은 순간에 몰리지 않게 하는 것이 <b>지터</b>(jitter)입니다. "
     "같은 요청을 두 번 받아도 한 번만 처리되게 하는 성질을 <b>멱등</b>(idempotent)이라 하고, "
     "계속 실패할 때 아예 요청을 끊는 장치를 <b>서킷 브레이커</b>라 부릅니다."),
    ("자주 잘못 부름",
     "<b>새로 고침</b> — 새로 고침은 <b>사람이</b> 화면 전체를 다시 부르는 것입니다.<br>"
     "<b>폴링</b> — 폴링은 <b>실패와 상관없이</b> 주기적으로 묻는 것입니다.<br>"
     "<b>오프라인 큐</b> — <a href=\"offline.html\">오프라인</a>은 <b>연결이 없을 때</b> 쌓아 두는 쪽입니다."),
  ]),
  axes=RT,
  oneline="<b>간격을 두 배씩 늘리고, 다섯 번쯤에서 멈추고, 사람에게 단추를 주세요.</b>",
  s4_title="상태", s4_hint="간격이 전부를 가른다",
  states=states([
    (track([(8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f'), (8, 'f')],
           "바로바로", "짧은 시간에 수십 번", False),
     "쉬지 않음", "<b>서버를 더 눕힌다</b>"),
    (track([(10, 'f'), (10, 'f'), (10, 'f'), (10, 'f'), (10, 'ok')], "같은 간격", "1초마다", None),
     "같은 간격", "짧게 끊길 때만"),
    (track([(6, 'f'), (11, 'f'), (18, 'f'), (26, 'ok')], "지수 백오프", "1 · 2 · 4초 뒤 성공", True),
     "지수 백오프", "<b>거의 늘 이쪽</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">3번째 시도 중…</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">4초 뒤 다시 시도합니다</span>'),
         "사람에게", True, "몇 번째인지, 언제 다시인지", "152px"),
     "보여 주기", "<b>말없이</b> 돌리지 않는다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--danger)">보내지 못했습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">다시 시도 ›</span>'),
         "끝내 실패", True, "사람에게 단추를 넘긴다", "152px"),
     "포기", "<b>단추</b>를 준다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">결제를 세 번 보냈다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">멱등 키가 없으면 세 번 결제된다</span>'),
         "위험", False, "", "152px"),
     "멱등하지 않은 요청", "<b>다시 보내면 안 된다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("간격", "두 배씩", "1 · 2 · 4 · 8초"),
    ("흔들기", "무작위 섞기", "여러 기기가 <b>같이 몰리지</b> 않게"),
    ("최대 횟수", "다섯 번쯤", "그 뒤엔 사람에게"),
    ("다시 보내도 되나", "먼저 확인", "<b>결제는 안 된다</b>"),
    ("보여 주기", "몇 번째 · 언제", "말없이 돌리지 않는다"),
    ("포기", "단추", "<b>사람이</b> 정하게"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          다시 보내기 전에 꼭 물어볼 것이 있습니다 —
          <b>이 요청을 두 번 보내도 되나</b>입니다.
          조회(GET)는 괜찮지만 <b>결제나 전송은 두 번 가면 사고</b>입니다.
          그래서 그런 요청에는 <b>멱등 키</b>를 붙여,
          서버가 같은 키를 두 번 받으면 한 번만 처리하게 해 둡니다.<br>
          <b>흔들기</b>가 없는 백오프도 문제가 됩니다 —
          수천 대가 동시에 끊겼다면 모두 정확히 1초 뒤에 다시 보내고,
          그 순간 서버가 또 넘어집니다. 간격에 <b>무작위를 조금 섞으면</b>
          그 몰림이 흩어집니다.</p>''',
  do=ul([
    "<b>지수 백오프 + 흔들기</b>를 기본으로",
    "다시 보내도 되는 요청인지 <b>먼저</b> 보기",
    "도는 동안 <b>몇 번째인지</b> 보여 주기",
  ]),
  dont=ul([
    "쉬지 않고 다시 보내기 — <b>서버를 더 눕힌다</b>",
    "결제·전송을 <b>멱등 키 없이</b> 다시 보내기",
    "끝없이 다시 보내기 — <b>다섯 번쯤</b>에서 멈춘다",
    "말없이 돌리기 — 사용자는 <b>멈춘 줄</b> 안다",
  ]),
  instead='연결이 아예 없으면 <a href="offline.html">오프라인</a>, 실패 화면은 <a href="error.html">에러 상태</a>, 기다림 표시는 <a href="spinner.html">스피너</a>, 문구는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (track([(6, 'f'), (11, 'f'), (18, 'ok')], "목록 받기", "", True), "목록 받기", "조용히 다시 받는다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--danger)">보내지 못했습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:3px">다시 시도 ›</span>'),
         "폼 보내기", True, "", "150px"),
     "폼 보내기", "<b>사람에게</b> 맡긴다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">Idempotency-Key: 9fa3…</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">두 번 와도 한 번만 처리</span>'),
         "결제", True, "", "150px"),
     "결제", "<b>멱등 키</b>와 함께"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 재시도의 계약서",
  code_lede="간격을 두 배씩 늘리고 무작위를 조금 섞습니다. 다섯 번이면 충분합니다.",
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
    ("<code>role=\"status\"</code>", "'3번째 시도 중'을 <b>소리로도</b> 알린다"),
    ("다시 시도 단추", "포기한 뒤에는 <b>초점을 받을 수 있는</b> 단추를 둔다"),
    ("<code>aria-busy</code>", "다시 받는 동안 그 자리에 붙인다"),
    ("428 · 429 · 503", "<b>다시 보내도 되는</b> 응답 코드"),
    ("400 · 401 · 404", "다시 보내도 <b>똑같이 실패</b>한다 — 재시도하지 않는다"),
    ("확인하는 법", "네트워크를 끊었다 켜고 <b>몇 번 보냈는지</b> 센다"),
  ]),
  backend=rows([
    ("<code>Retry-After</code>", "서버가 <b>언제 다시 오라</b>고 알려 주면 화면이 추측할 필요가 없습니다."),
    ("멱등 키", "같은 키의 요청을 두 번 받으면 <b>처음 결과</b>를 그대로 돌려줍니다."),
    ("어떤 오류인지", "<code>429</code>(너무 잦음)와 <code>400</code>(잘못된 요청)은 <b>전혀 다른 대응</b>이 필요합니다."),
    ("서킷 브레이커", "연속 실패가 쌓이면 <b>잠시 요청 자체를 끊어</b> 서버가 일어날 틈을 줍니다."),
  ]),
  plat_lede="<b>생각은 같고</b> 라이브러리가 다릅니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     track([(6, 'f'), (11, 'f'), (18, 'ok')], "", "", True, "110px"),
     "<code>fetch</code> 자체에는 재시도가 없습니다. 쿼리 라이브러리들이 <b>기본으로</b> 붙여 둡니다."),
    ("iOS", "URLSession · 직접",
     '''              <div class="phone" role="img" aria-label="iOS 재시도 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:7px;border-radius:2px;background:color-mix(in srgb, var(--danger) 35%, transparent)"></div></div></div>''',
     "<code>waitsForConnectivity</code> 로 <b>연결될 때까지</b> 기다리게 할 수 있습니다."),
    ("안드로이드", "WorkManager",
     '''              <div class="phone" role="img" aria-label="안드로이드 재시도 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:42px;height:7px;border-radius:2px;background:color-mix(in srgb, var(--danger) 35%, transparent)"></div></div></div>''',
     "<b>백오프까지 OS 가</b> 맡습니다 — 앱이 꺼져 있어도 나중에 다시 보냅니다."),
  ]),
  plat_note="안드로이드의 <b>WorkManager</b> 는 앱이 꺼진 뒤에도 재시도를 이어 가는, 웹에는 없는 장치입니다. 웹에서 가장 가까운 것은 <b>서비스 워커의 백그라운드 동기화</b>인데 아직 브라우저마다 다릅니다. 그래서 웹에서는 <b>탭이 살아 있는 동안만</b> 재시도가 돈다고 보는 편이 안전하고, 중요한 것은 <a href=\"offline.html\">오프라인</a>처럼 <b>쌓아 뒀다가 다음에 열렸을 때</b> 보내는 쪽으로 설계합니다.",
  siblings=siblings("retry"),
  related='''        <li><a href="offline.html"><b>오프라인</b><em>8부</em></a></li>
        <li><a href="error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="spinner.html"><b>스피너</b><em>8부</em></a></li>''',
)
