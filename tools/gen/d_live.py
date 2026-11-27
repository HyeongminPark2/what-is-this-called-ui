# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def lv(visual, said, kind="ok", w="168px"):
    color = {"ok": "#1f8a4c", "no": "var(--danger)", "warn": "var(--warn)"}[kind]
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:7px;justify-items:center">'
            + visual +
            '<span style="font-family:var(--mono);font-size:10px;color:' + color + ';font-weight:700;text-align:center">' + said + '</span></div>')

def toast(txt="저장했습니다"):
    return ('<span style="display:inline-block;background:var(--ink-900);color:#fff;border-radius:6px;'
            'padding:6px 11px;font-size:11px">' + txt + '</span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="display:inline-block;background:var(--ink-900);color:#fff;border-radius:7px;padding:8px 13px;font-size:12px;justify-self:start">정산이 3건 추가되었습니다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">role="status"   = aria-live="polite"</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">role="alert"   = aria-live="assertive" (말을 끊는다)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">리전은 미리 비워 둔 채로 있어야 한다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">내용만 바꾼다 — 통째로 새로 만들면 안 읽는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-busy   — 다 바뀐 뒤에 한 번만 읽히게</div>
                </div>
              </div>'''

D = dict(
  slug="live", ko="라이브 리전", en="Live region",
  desc="저절로 바뀐 화면을 소리로 알리는 방법과, 리전을 미리 두어야 하는 이유를 보여주는 항목.",
  lede="화면이 <b>저절로 바뀐 것</b>을 소리로 알리는 자리. 눈으로는 보이지만 소리로는 안 들리는 틈을 메웁니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 버튼을 눌러 보세요. <b>조용히 바꾸기</b>는 화면 숫자만 바뀌고
          아래 기록은 그대로입니다 — 화면을 못 보는 사람에게는 <b>아무 일도 없던 것</b>입니다.<br>
          <code>status</code>는 <b>하던 말이 끝난 뒤</b>, <code>alert</code>는 <b>말을 끊고</b> 알립니다.
          기록의 '[기다렸다가]'와 '[말을 끊고]'가 그 차이입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "라이브 리전, 실시간 알림 영역"),
    ("영어", "live region, aria-live, polite, assertive"),
    ("같이 쓰는 말",
     "기다렸다 읽는 것을 <b>polite</b>, 말을 끊고 읽는 것을 <b>assertive</b>라 합니다. "
     "<code>role=\"status\"</code>는 polite 의, <code>role=\"alert\"</code>는 assertive 의 "
     "짧은 이름입니다. 여러 번 바뀔 때 다 읽을지 정하는 것은 <b><code>aria-atomic</code></b>·"
     "<b><code>aria-relevant</code></b> 입니다."),
    ("자주 잘못 부름",
     "<b>토스트</b> — 토스트는 <b>부품</b>이고 라이브 리전은 <b>읽히게 하는 장치</b>입니다. "
     "토스트를 띄워도 리전이 없으면 안 읽힙니다.<br>"
     "<b>알림</b>(notification) — 브라우저 알림은 다른 기능입니다.<br>"
     "<b><code>alert()</code></b> — 자바스크립트의 그 함수와는 아무 상관이 없습니다."),
  ]),
  axes=ax("라이브 리전"),
  oneline="라이브 리전은 <b>미리 비워 둔 채로 있어야</b> 합니다. 알릴 때 통째로 만들면 읽지 않습니다 — 가장 흔한 실수입니다.",
  s4_title="갈래", s4_hint="언제 어떻게 알리나",
  states=states([
    (lv(toast(), '(안 읽힘) — 리전이 없다', "no"), "리전 없음", "화면에는 떴는데 <b>소리로는 아무 일도 없다</b>"),
    (lv(toast(), '[기다렸다가] "저장했습니다"'), "status", "<b>하던 말이 끝난 뒤</b> 알린다. 대부분 이것"),
    (lv(toast("연결이 끊겼습니다"), '[말을 끊고] "연결이 끊겼습니다"', "warn"), "alert",
     "<b>말을 끊는다.</b> 정말 급한 것에만"),
    (lv('<span style="display:inline-block;border:1px solid var(--line);border-radius:6px;padding:6px 11px;font-size:11px;background:var(--surface)">검색 결과 12건</span>',
        '[기다렸다가] "검색 결과 12건"'), "결과 개수", "입력할 때마다 바뀌는 숫자 — <b>polite 가 맞다</b>"),
    (lv('<span style="display:inline-block;border:1px solid var(--danger);border-radius:6px;padding:6px 11px;font-size:11px;color:var(--danger)">계좌번호는 10자리입니다</span>',
        '[말을 끊고] "계좌번호는 10자리입니다"', "warn"), "폼 오류", "제출을 막은 오류는 <b>바로 알려야</b> 한다"),
    (lv('<span style="display:inline-block;border:1px solid var(--line);border-radius:6px;padding:6px 11px;font-size:11px;background:var(--surface);color:var(--fg-muted)">1초마다 바뀌는 숫자</span>',
        '(계속 읽어 시끄럽다)', "no"), "너무 자주", "<b>수다스러운 리전</b>은 안 쓰느니만 못하다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("알릴 말", "message", "저절로 바뀐 것. 사용자가 누른 결과거나 서버가 보낸 것"),
    ("기다렸다 알리기", "role=\"status\"", "하던 말을 마치고 읽는다. <b>대부분 이것으로 충분</b>"),
    ("끊고 알리기", "role=\"alert\"", "말을 끊는다. <b>오류·연결 끊김</b>처럼 급한 것에만"),
    ("미리 두기", "빈 리전", "<b>알릴 때 만들면 안 읽는다.</b> 처음부터 비워 둔 채로 있어야 한다"),
    ("내용만 바꾸기", "textContent", "리전을 지웠다 다시 만들면 <b>새 리전</b>이라 안 읽힌다"),
    ("다 바뀐 뒤에", "aria-busy", "여러 줄을 고칠 때 <code>true</code>로 묶었다가 끝나면 <code>false</code>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>리전을 알릴 때 만들면 안 읽힙니다.</b> 스크린 리더는 '이미 있던 리전의 내용이 바뀐 것'을
          감시하기 때문입니다. 그래서 토스트를 띄울 때마다 <code>&lt;div role="status"&gt;</code>를
          새로 붙이면 아무 소리도 안 납니다 — <b>빈 리전을 화면 어딘가에 미리 두고
          그 안의 글만 바꾸는</b> 것이 정석입니다.</p>''',
  do=ul([
    "<b>사용자가 누른 뒤 저절로</b> 바뀌는 것 — 저장됨, 삭제됨, N건 추가됨",
    "검색 결과 개수처럼 <b>입력에 따라</b> 바뀌는 숫자",
    "폼 오류 — 제출을 막았으면 <code>alert</code>",
    "연결 끊김·세션 만료",
  ]),
  dont=ul([
    "<b>1초마다 바뀌는 것</b>에 거는 것 — 계속 읽어 시끄럽습니다",
    "<b>모든 것</b>에 <code>alert</code>를 쓰는 것 — 끊는 것은 거슬립니다",
    "리전을 <b>알릴 때 만드는</b> 것 — 안 읽힙니다",
    "화면에 안 보이는데 소리로만 알리는 것 — <b>둘 다</b> 있어야 합니다",
  ]),
  instead='부품 자체는 <a href="../items/toast.html">토스트</a>·<a href="../items/error.html">에러 상태</a>, 상태 속성은 <a href="screenreader.html">스크린 리더가 읽는 것</a>.',
  cases=cases([
    (lv(toast("정산을 확정했습니다"), '[기다렸다가] 읽는다', "ok", "190px"),
     "토스트", "<b>리전은 따로</b> 둔다. 토스트 자체를 리전으로 만들면 안 읽힌다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px">모란</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">검색 결과 12건</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c;margin-top:6px;text-align:center;font-weight:700">role="status"</div>''',
     "검색 결과", "타이핑할 때마다 바뀐다. <b>polite</b> 라야 안 시끄럽다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="border:1px solid var(--danger);border-radius:5px;padding:6px 9px;font-size:11px">1234</span>
                <span style="font-size:10px;color:var(--danger)">계좌번호는 10자리입니다</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--danger);margin-top:6px;text-align:center;font-weight:700">role="alert"</div>''',
     "폼 오류", "제출을 막았으면 <b>바로</b> 알린다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="미리 두고 내용만 바꾼다",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="빈 리전을 <b>미리</b> 두고, 알릴 때는 <b>그 안의 글만</b> 바꿉니다.",
  code='''<span class="c">&lt;!-- 화면 어딘가에 미리 — 비어 있는 채로 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"status"</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"errors"</span> <span class="a">role</span>=<span class="s">"alert"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;&lt;/<span class="t">div</span>&gt;

<span class="c">// 알릴 때는 '내용만' 바꾼다</span>
status.textContent = <span class="s">'정산을 확정했습니다'</span>;

<span class="c">// 같은 말을 또 알려야 하면 한 번 비웠다 넣는다</span>
status.textContent = <span class="s">''</span>;
requestAnimationFrame(() =&gt; status.textContent = msg);

<span class="c">/* 보이지 않게 두는 표준 방법 — display:none 은 안 읽힌다 */</span>
<span class="t">.sr-only</span> { <span class="a">position</span>: absolute; <span class="a">width</span>: <span class="a">1px</span>; <span class="a">height</span>: <span class="a">1px</span>;
           <span class="a">overflow</span>: hidden; <span class="a">clip</span>: <span class="t">rect</span>(<span class="a">0 0 0 0</span>); }''',
  keys=kbd([
    ("리전을 미리 둔다", "비어 있는 채로. <b>알릴 때 만들면 안 읽힌다</b>"),
    ("내용만 바꾼다", "요소를 갈아 끼우지 않는다"),
    ("<code>status</code>를 기본으로", "<code>alert</code>는 말을 끊으니 <b>정말 급한 것</b>에만"),
    ("<code>display:none</code>으로 숨기지 않는다", "안 읽힌다. <code>.sr-only</code> 방식으로 숨긴다"),
    ("같은 말을 또 알릴 때", "한 번 비웠다가 다시 넣어야 <b>바뀐 것</b>으로 친다"),
    ("자주 바뀌면 묶는다", "<code>aria-busy</code>로 묶었다가 <b>끝나고 한 번</b>만 읽히게"),
  ]),
  backend=rows([
    ("무엇을 알릴지 정한다", "서버 응답이 올 때마다 다 알리면 시끄럽습니다. <b>사용자가 한 행동의 결과</b>만 알리는 것이 기준입니다."),
    ("실시간 밀어 주기", "웹소켓으로 남이 바꾼 것까지 알리면 <b>끝없이 말합니다.</b> 내 행동과 남의 행동을 나눠 다룹니다."),
    ("문구는 짧게", "소리로 듣는 글입니다. '정산 요청 #4821이(가) 정상적으로 처리 완료되었습니다' 보다 <b>'정산을 확정했습니다'</b>가 낫습니다."),
    ("검사", "자동 도구는 리전이 <b>있는지</b>는 보지만 <b>실제로 읽히는지</b>는 못 봅니다. VoiceOver 를 켜고 한 번 해 보는 수밖에 없습니다."),
  ]),
  plat_lede="두 OS 는 <b>알림을 보내는 함수</b>로 같은 일을 합니다.",
  plats=plats([
    ("웹", "aria-live",
     lv(toast(), 'role="status"', "ok", "120px"),
     "<b>미리 둔 리전</b>의 내용을 바꿉니다. '알릴 때 만들면 안 읽힌다'는 함정이 웹 특유입니다."),
    ("iOS", "VoiceOver",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">UIAccessibility<br>&nbsp;.post(notification:<br>&nbsp;.announcement)</div>''',
     "<b>함수를 불러</b> 알립니다. 리전을 미리 둘 필요가 없어 더 단순합니다."),
    ("안드로이드", "TalkBack",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">announceForAccessibility<br>liveRegion = Polite</div>''',
     "함수와 <b>liveRegion</b> 속성 둘 다 있습니다. 웹과 거의 같은 개념입니다."),
  ]),
  plat_note="앱은 <b>\"이 말을 지금 해 줘\"</b>라고 함수를 부르면 끝나지만, 웹은 <b>미리 둔 리전의 내용을 바꾸는</b> 간접적인 방식입니다. 그래서 \"알림이 안 읽혀요\"의 원인이 웹에서만 '리전을 새로 만들어서'인 경우가 많습니다.",
  siblings=siblings("live"),
  related='''        <li><a href="../items/toast.html"><b>토스트 · 스낵바</b><em>6부</em></a></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>''',
)
