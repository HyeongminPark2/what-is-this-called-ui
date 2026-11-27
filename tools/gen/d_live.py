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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">role="status"   — aria-live="polite"와 같음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">role="alert"   — aria-live="assertive"와 같음(말을 끊음)</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">리전은 빈 채로 미리 두어야 함</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">통째로 새로 만들면 읽지 않으니 내용만 바꿈</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-busy   — 다 바뀐 뒤에 한 번만 읽히게 함</div>
                </div>
              </div>'''

D = dict(
  slug="live", ko="라이브 리전", en="Live region",
  desc="사용자가 보고 있지 않은 사이에 바뀐 화면 내용을 소리로 알리는 방법과, 리전을 미리 만들어 두어야 하는 이유를 보여 주는 항목입니다.",
  lede="라이브 리전은 화면 내용이 <b>저절로 바뀌었을 때</b> 스크린 리더가 그 내용을 소리로 읽어 주게 하는 영역입니다. 화면에 새로 뜬 내용은 눈으로는 바로 보이지만, 라이브 리전이 없으면 스크린 리더는 아무것도 읽지 않습니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 버튼을 눌러 보세요. <b>조용히 바꾸기</b>를 누르면 화면의 숫자만 바뀌고
          아래 기록에는 아무것도 남지 않습니다. 화면을 보지 못하는 사람은 <b>무엇이 바뀌었는지 전혀 알 수 없습니다</b>.<br>
          <code>status</code>는 스크린 리더가 <b>읽던 말을 마친 뒤</b> 알리고, <code>alert</code>는 <b>읽던 말을 끊고</b> 바로 알립니다.
          기록에 찍히는 '[기다렸다가]'와 '[말을 끊고]'가 이 차이를 보여 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "라이브 리전, 실시간 알림 영역"),
    ("영어", "live region, aria-live, polite, assertive"),
    ("같이 쓰는 말",
     "읽던 말을 마칠 때까지 기다렸다가 읽는 방식은 <b>polite</b>, 읽던 말을 끊고 바로 읽는 방식은 <b>assertive</b>라고 합니다. "
     "<code>role=\"status\"</code>는 polite 리전을, <code>role=\"alert\"</code>는 assertive 리전을 "
     "짧게 쓰는 방법입니다. 내용이 바뀔 때 무엇을 읽을지는 <b><code>aria-atomic</code></b>과 "
     "<b><code>aria-relevant</code></b>로 정합니다."),
    ("자주 잘못 부르는 이름",
     "<b>토스트</b> — 토스트는 화면에 뜨는 <b>부품</b>이고, 라이브 리전은 그 내용을 <b>스크린 리더가 읽게 하는 장치</b>입니다. "
     "그래서 토스트를 띄워도 라이브 리전이 없으면 스크린 리더는 읽지 않습니다.<br>"
     "<b>알림</b>(notification) — 브라우저가 띄우는 알림은 라이브 리전과 다른 기능입니다.<br>"
     "<b><code>alert()</code></b> — <code>role=\"alert\"</code>는 자바스크립트의 <code>alert()</code> 함수와 아무 상관이 없습니다."),
  ]),
  axes=ax("라이브 리전"),
  oneline="라이브 리전은 <b>처음부터 빈 채로 화면에 두어야</b> 합니다. 알릴 때가 되어서야 리전을 새로 만들면 스크린 리더가 읽지 않는데, 이것이 가장 흔한 실수입니다.",
  s4_title="알리는 방식", s4_hint="바뀐 내용을 언제 어떻게 알리는지",
  states=states([
    (lv(toast(), '리전이 없어 읽지 않음', "no"), "라이브 리전이 없을 때", "화면에는 토스트가 떴지만 <b>스크린 리더는 아무것도 읽지 않습니다</b>"),
    (lv(toast(), '[기다렸다가] "저장했습니다"'), "status로 기다렸다가 알릴 때", "<b>읽던 말을 마친 뒤</b> 알립니다. 대부분 이 방식을 씁니다"),
    (lv(toast("연결이 끊겼습니다"), '[말을 끊고] "연결이 끊겼습니다"', "warn"), "alert로 말을 끊고 알릴 때",
     "<b>읽던 말을 끊고</b> 알립니다. 정말 급한 내용에만 씁니다"),
    (lv('<span style="display:inline-block;border:1px solid var(--line);border-radius:6px;padding:6px 11px;font-size:11px;background:var(--surface)">검색 결과 12건</span>',
        '[기다렸다가] "검색 결과 12건"'), "검색 결과 개수를 알릴 때", "입력할 때마다 바뀌는 숫자이므로 <b>polite로 알리는 것이 맞습니다</b>"),
    (lv('<span style="display:inline-block;border:1px solid var(--danger);border-radius:6px;padding:6px 11px;font-size:11px;color:var(--danger)">계좌번호는 10자리입니다</span>',
        '[말을 끊고] "계좌번호는 10자리입니다"', "warn"), "제출을 막은 폼 오류를 알릴 때", "제출을 막은 오류는 <b>바로 알려야</b> 합니다"),
    (lv('<span style="display:inline-block;border:1px solid var(--line);border-radius:6px;padding:6px 11px;font-size:11px;background:var(--surface);color:var(--fg-muted)">1초마다 바뀌는 숫자</span>',
        '(쉬지 않고 읽어 시끄러움)', "no"), "내용이 너무 자주 바뀔 때", "내용이 <b>너무 자주 바뀌는 리전</b>은 스크린 리더가 쉬지 않고 읽어서, 리전을 두지 않은 것보다 더 불편합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("알릴 말", "message", "저절로 바뀐 내용입니다. 사용자가 누른 버튼의 결과일 수도 있고, 서버가 보낸 소식일 수도 있습니다"),
    ("기다렸다 알리기", "role=\"status\"", "읽던 말을 마친 뒤에 읽습니다. <b>대부분은 이 방식으로 충분합니다</b>"),
    ("끊고 알리기", "role=\"alert\"", "읽던 말을 끊고 바로 읽습니다. <b>오류나 연결 끊김</b>처럼 급한 내용에만 씁니다"),
    ("리전을 미리 두기", "빈 리전", "<b>알릴 때 리전을 만들면 읽지 않으므로</b>, 처음부터 빈 리전을 두어야 합니다"),
    ("내용만 바꾸기", "textContent", "리전을 지웠다가 다시 만들면 스크린 리더가 <b>새 리전</b>으로 보고 읽지 않습니다"),
    ("다 바뀐 뒤에 읽히기", "aria-busy", "여러 줄을 한꺼번에 고칠 때 <code>true</code>로 두었다가, 다 고친 뒤 <code>false</code>로 바꿉니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>알릴 때가 되어서 리전을 만들면 스크린 리더가 읽지 않습니다.</b> 스크린 리더는 이미 있던 리전의 내용이 바뀌는 것만
          지켜보기 때문입니다. 그래서 토스트를 띄울 때마다 <code>&lt;div role="status"&gt;</code>를
          새로 붙이면 아무 소리도 나지 않습니다. <b>빈 리전을 화면 어딘가에 미리 두고
          그 안의 글만 바꾸는</b> 것이 표준적인 방법입니다.</p>''',
  do=ul([
    "저장됨, 삭제됨, N건 추가됨처럼 <b>사용자가 버튼을 누른 뒤 저절로</b> 바뀌는 내용을 알릴 때",
    "검색 결과 개수처럼 <b>입력에 따라</b> 바뀌는 숫자를 알릴 때",
    "폼 오류를 알릴 때. 오류 때문에 제출을 막았다면 <code>alert</code>로 알립니다",
    "연결이 끊기거나 세션이 만료되었을 때",
  ]),
  dont=ul([
    "<b>1초마다 바뀌는 내용</b>에 걸 때. 스크린 리더가 쉬지 않고 읽어서 시끄럽습니다",
    "<b>모든 알림</b>에 <code>alert</code>를 쓸 때. 읽던 말이 자꾸 끊기면 사용자가 불편합니다",
    "리전을 <b>알릴 때 새로 만들</b> 때. 스크린 리더가 읽지 않습니다",
    "화면에는 보이지 않고 소리로만 알릴 때. 화면 표시와 소리 <b>둘 다</b> 있어야 합니다",
  ]),
  dont_title="라이브 리전을 쓰지 않거나 잘못 쓰는 경우",
  instead_title="라이브 리전과 이어지는 주제는 다른 항목에서 다룹니다",
  instead='화면에 뜨는 부품 자체는 <a href="../items/toast.html">토스트</a>와 <a href="../items/error.html">에러 상태</a> 항목에서, 요소의 상태를 알리는 속성은 <a href="screenreader.html">스크린 리더가 읽는 것</a>에서 다룹니다.',
  cases=cases([
    (lv(toast("정산을 확정했습니다"), '[기다렸다가] 읽음', "ok", "190px"),
     "토스트 내용 알리기", "<b>리전은 토스트와 따로</b> 둡니다. 토스트를 띄울 때 토스트 자체를 리전으로 만들면 스크린 리더가 읽지 않습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="border:1px solid var(--line-strong);border-radius:5px;padding:6px 9px;font-size:11px">모란</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">검색 결과 12건</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:#1f8a4c;margin-top:6px;text-align:center;font-weight:700">role="status"</div>''',
     "검색 결과 개수 알리기", "글자를 칠 때마다 바뀌기 때문에 <b>polite</b>로 알려야 시끄럽지 않습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span style="border:1px solid var(--danger);border-radius:5px;padding:6px 9px;font-size:11px">1234</span>
                <span style="font-size:10px;color:var(--danger)">계좌번호는 10자리입니다</span>
              </div>
              <div style="font-family:var(--mono);font-size:9.5px;color:var(--danger);margin-top:6px;text-align:center;font-weight:700">role="alert"</div>''',
     "제출을 막은 폼 오류 바로 알리기", "오류 때문에 제출을 막았다면 <b>바로</b> 알립니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="리전을 미리 두고 내용만 바꾸는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="빈 리전을 <b>미리</b> 만들어 두고, 알릴 때는 <b>리전 안의 글만</b> 바꿉니다.",
  code='''<span class="c">&lt;!-- 화면 어딘가에 빈 채로 미리 둔다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"status"</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"errors"</span> <span class="a">role</span>=<span class="s">"alert"</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;&lt;/<span class="t">div</span>&gt;

<span class="c">// 알릴 때는 '내용만' 바꾼다</span>
status.textContent = <span class="s">'정산을 확정했습니다'</span>;

<span class="c">// 같은 말을 또 알려야 하면 한 번 비웠다 넣는다</span>
status.textContent = <span class="s">''</span>;
requestAnimationFrame(() =&gt; status.textContent = msg);

<span class="c">/* 보이지 않게 두는 표준 방법. display:none 으로 숨기면 읽히지 않는다 */</span>
<span class="t">.sr-only</span> { <span class="a">position</span>: absolute; <span class="a">width</span>: <span class="a">1px</span>; <span class="a">height</span>: <span class="a">1px</span>;
           <span class="a">overflow</span>: hidden; <span class="a">clip</span>: <span class="t">rect</span>(<span class="a">0 0 0 0</span>); }''',
  keys=kbd([
    ("리전을 미리 두기", "빈 채로 미리 둡니다. <b>알릴 때 만들면 읽히지 않습니다</b>"),
    ("리전의 내용만 바꾸기", "리전 요소를 새 요소로 바꾸지 않고 안의 글만 바꿉니다"),
    ("<code>status</code>를 기본으로 쓰기", "<code>alert</code>는 읽던 말을 끊기 때문에 <b>정말 급한 내용</b>에만 씁니다"),
    ("<code>display:none</code>으로 숨기지 않기", "<code>display:none</code>으로 숨기면 읽히지 않으므로 <code>.sr-only</code> 방식으로 숨깁니다"),
    ("같은 말을 또 알릴 때", "리전을 한 번 비웠다가 다시 넣어야 스크린 리더가 <b>내용이 바뀐 것</b>으로 봅니다"),
    ("자주 바뀌는 내용은 묶어서 알리기", "<code>aria-busy</code>로 묶어 두었다가 바뀌는 일이 <b>끝난 뒤 한 번만</b> 읽히게 합니다"),
  ]),
  backend=rows([
    ("무엇을 알릴지 정하기", "서버 응답이 올 때마다 모두 알리면 시끄럽기 때문에, <b>사용자가 한 행동의 결과</b>만 알리는 것을 기준으로 삼습니다."),
    ("실시간으로 받은 변경 알리기", "웹소켓으로 받은 다른 사람의 변경까지 모두 알리면 <b>스크린 리더가 쉬지 않고 읽습니다.</b> 그래서 내가 한 행동의 결과와 다른 사람이 바꾼 내용을 나눠서 다룹니다."),
    ("알리는 문구를 짧게 쓰기", "라이브 리전의 문구는 소리로 듣는 글이므로 짧을수록 좋습니다. '정산 요청 #4821이(가) 정상적으로 처리 완료되었습니다' 보다 <b>'정산을 확정했습니다'</b>가 낫습니다."),
    ("실제로 읽히는지 검사하기", "자동 검사 도구는 리전이 <b>있는지</b>는 확인하지만 <b>실제로 읽히는지</b>는 확인하지 못합니다. 그래서 VoiceOver를 켜고 직접 한 번 들어 봐야 합니다."),
  ]),
  plat_lede="iOS와 안드로이드에서는 <b>알림을 보내는 함수</b>를 불러 같은 일을 합니다.",
  plats=plats([
    ("웹", "aria-live",
     lv(toast(), 'role="status"', "ok", "120px"),
     "<b>미리 둔 리전</b>의 내용을 바꿔서 알립니다. 알릴 때 리전을 만들면 읽히지 않는 문제는 웹에만 있습니다."),
    ("iOS", "VoiceOver",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">UIAccessibility<br>&nbsp;.post(notification:<br>&nbsp;.announcement)</div>''',
     "<b>함수를 불러</b> 알립니다. 리전을 미리 둘 필요가 없어서 웹보다 단순합니다."),
    ("안드로이드", "TalkBack",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">announceForAccessibility<br>liveRegion = Polite</div>''',
     "함수로 알리는 방법과 <b>liveRegion</b> 속성을 다는 방법이 둘 다 있는데, liveRegion은 웹의 라이브 리전과 거의 같은 개념입니다."),
  ]),
  plat_note="앱에서는 읽을 문장을 넘겨 함수를 한 번 부르면 되지만, 웹에서는 <b>미리 둔 리전의 내용을 바꾸는</b> 간접적인 방식을 씁니다. 그래서 웹에서는 \"알림이 안 읽혀요\"라는 문제의 원인이 '리전을 새로 만들어서'인 경우가 많습니다.",
  siblings=siblings("live"),
  related='''        <li><a href="../items/toast.html"><b>토스트 · 스낵바</b><em>6부</em></a></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>''',
)
