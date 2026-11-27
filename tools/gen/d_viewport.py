# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def phone(bar, panel_h, note, warn=False, w="112px"):
    """bar: 주소창 높이(px), panel_h: 패널 높이(px) — 상자는 120px 높이"""
    H = 120
    top = bar
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:center">'
            '<div style="width:72px;height:' + str(H) + 'px;border:2px solid var(--line-strong);border-radius:10px;'
            'background:var(--surface);position:relative;overflow:hidden">'
            + ('<div style="position:absolute;left:0;right:0;top:0;height:' + str(bar) + 'px;background:var(--bg);'
               'border-bottom:1px solid var(--line);font-size:6px;color:var(--fg-muted);display:grid;place-items:center">example.com</div>' if bar else '')
            + '<div style="position:absolute;left:0;right:0;top:' + str(top) + 'px;bottom:0;overflow:hidden">'
              '<div style="position:absolute;left:3px;right:3px;top:3px;height:' + str(panel_h - 6) + 'px;'
              'background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px">'
              '<span style="position:absolute;left:2px;right:2px;bottom:2px;height:11px;border-radius:3px;background:var(--accent)"></span></div>'
            '</div></div>'
            '<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + ';text-align:center">' + note + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100lvh — 큰 쪽. 주소창이 숨었을 때</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100svh — 작은 쪽. 주소창이 보일 때</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">100dvh — 지금 보이는 만큼. 굴리면 바뀐다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">100vh = 100lvh — 주소창이 보이면 삐져나간다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100vw 는 세로 막대 폭을 안 뺀다 — 가로로 넘친다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">meta viewport 가 없으면 전부 헛돈다</div>
                </div>
              </div>'''

D = dict(
  slug="viewport", ko="뷰포트 단위", en="Viewport units",
  desc="100vh가 가리키는 높이는 하나가 아니다. svh·lvh·dvh의 차이와 바닥 버튼이 잘리는 이유.",
  lede="<b>100vh 가 가리키는 높이는 하나가 아닙니다.</b> 폰 주소창이 숨었다 나타나기 때문입니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 폰이 같은 화면을 <code>100vh</code>·<code>100svh</code>·<code>100dvh</code>로 그린 것입니다.
          <b>주소창 보이기</b>를 켜 보세요 — <code>100vh</code> 짜리만 바닥의 '다음' 버튼이 잘립니다.<br>
          아래 표는 <b>이 브라우저</b>에서 네 단위가 실제로 몇 px 인지 잰 것입니다.
          PC 에서는 숨는 주소창이 없어 넷이 같습니다 — 차이는 <b>폰에서만</b> 드러납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "뷰포트 단위, 화면 높이 단위"),
    ("영어", "viewport units, vh / svh / lvh / dvh"),
    ("같이 쓰는 말",
     "<b>v</b>는 viewport, <b>h</b>는 height 입니다. 앞에 붙는 글자가 "
     "<b>s</b>mall(작은 쪽) · <b>l</b>arge(큰 쪽) · <b>d</b>ynamic(지금) 입니다. "
     "가로는 <code>vw</code>, 짧은 쪽·긴 쪽이 <code>vmin</code>·<code>vmax</code>입니다. "
     "브라우저 창 안쪽에서 실제로 보이는 영역을 <b>비주얼 뷰포트</b>라 하고 "
     "<code>window.visualViewport</code>로 읽습니다."),
    ("자주 잘못 부름",
     "<b>화면 높이</b> — 기기 화면이 아니라 <b>브라우저 창 안쪽</b>입니다.<br>"
     "<b>100%</b> — <code>100%</code>는 <b>부모</b>의 높이이고 <code>100vh</code>는 창의 높이입니다. 전혀 다릅니다.<br>"
     "<b>풀스크린</b> — 전체 화면 API 와는 상관없습니다."),
  ]),
  axes=ax("뷰포트 단위"),
  oneline="<b>바닥에 뭔가 붙는 화면이면 <code>100dvh</code></b>입니다. <code>100vh</code>는 PC 에서만 맞습니다.",
  s4_title="주소창에 따라", s4_hint="같은 100%가 네 가지",
  states=states([
    (phone(0, 120, "주소창 없음 — 셋이 같다"), "굴려서 숨었을 때", "이때의 높이가 <b>lvh</b>이자 <b>vh</b>"),
    (phone(16, 120, "100vh — 아래가 잘린다", True), "주소창이 보일 때", "<b>vh 는 큰 쪽으로 고정</b>이라 삐져나간다"),
    (phone(16, 104, "100svh — 늘 안전하다"), "svh", "작은 쪽. 주소창이 숨으면 <b>아래가 남는다</b>"),
    (phone(16, 104, "100dvh — 지금 보이는 만큼"), "dvh", "굴리면 따라 바뀐다. <b>바닥에 딱 붙는다</b>"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:72px;height:120px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:0;right:0;top:0;bottom:52px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px;margin:3px"></div>
                  <div style="position:absolute;left:0;right:0;bottom:0;height:52px;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted);text-align:center">키보드가 올라오면 또 줄어든다</span>
              </div>''',
     "키보드까지 더하면", "<a href=\"softkeyboard.html\">폰 키보드</a>는 <code>dvh</code>로도 안 잡힌다"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:72px;height:120px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:3px;top:3px;width:84px;height:40px;background:var(--accent-soft);border:1px solid var(--danger);border-radius:4px"></div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--danger);text-align:center">100vw — 세로 막대 폭을 안 뺀다</span>
              </div>''',
     "가로도 함정이 있다", "<code>100vw</code>는 <b>스크롤 막대</b>를 포함한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("큰 쪽", "lvh", "주소창이 숨었을 때의 높이. <code>vh</code>와 같다"),
    ("작은 쪽", "svh", "주소창이 보일 때. <b>늘 안전</b>하지만 아래가 남는다"),
    ("지금", "dvh", "보이는 만큼. <b>굴리면 따라 바뀐다</b>"),
    ("vh 의 정체", "= lvh", "큰 쪽 고정. <b>주소창이 보이면 삐져나간다</b>"),
    ("가로의 함정", "100vw", "세로 스크롤 막대 폭을 <b>안 뺀다.</b> PC 에서 가로로 넘친다"),
    ("전제", "meta viewport", "없으면 폰이 <b>980px 창</b>인 척한다. 전부 헛돈다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>100dvh</code>가 늘 정답인 것도 아닙니다.
          굴릴 때마다 값이 바뀌므로, 그 높이를 쓰는 상자가 <b>따라 움직이며 흔들립니다</b>.
          배경처럼 <b>가만히 있어야 하는 것</b>에는 <code>100lvh</code>가 낫고,
          <b>바닥에 버튼이 붙는 화면</b>에는 <code>100dvh</code>가 맞습니다.
          둘 다 피하고 싶으면 <code>100svh</code>를 쓰고 <b>아래가 조금 남는 것</b>을 받아들입니다.</p>''',
  do=ul([
    "바닥에 버튼이 붙는 <b>한 화면짜리</b> 폼 → <code>100dvh</code>",
    "화면을 꽉 채우는 <a href=\"../items/modal.html\">모달</a>·시트",
    "히어로 영역 — 다만 <b>흔들림</b>을 보고 lvh 와 고른다",
  ]),
  dont=ul([
    "<code>100vh</code>를 폰에서 그대로 — <b>바닥이 잘린다</b>",
    "<code>100vw</code>로 전체 폭 — PC 에서 <b>가로 스크롤</b>이 생긴다",
    "<code>&lt;meta name=\"viewport\"&gt;</code> 빠뜨리기",
    "키보드까지 <code>dvh</code>로 해결될 거라 믿기 → <a href=\"softkeyboard.html\">폰 키보드</a>",
  ]),
  instead='부모 높이를 꽉 채우려면 <code>100%</code>, 바닥에 붙이려면 <a href="../items/sticky.html">스티키</a>나 <code>position:fixed</code>, 글줄 길이를 묶으려면 <a href="../items/container.html">컨테이너</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.screen {</span>
                <span>&nbsp;&nbsp;min-height: 100vh;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">min-height: 100dvh;</span></span>
                <span>}</span>
              </div>''',
     "두 줄로 적는다", "옛 브라우저는 앞줄, 새 브라우저는 <b>뒷줄</b>을 쓴다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--danger)">width: 100vw;</span>
                <span style="color:var(--accent)">width: 100%;</span>
                <span style="font-size:8.5px">세로 막대가 있으면 vw 가 더 넓다</span>
              </div>''',
     "가로는 100%", "전체 폭이 필요해도 <code>100vw</code>는 피한다"),
    (phone(16, 104, "100dvh — 바닥에 딱", False, "150px"), "한 화면짜리 폼", "<b>다음 버튼이 늘 보인다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 단위의 계약서",
  code_lede="<code>meta viewport</code>를 적고, 높이는 두 줄로 겹쳐 적습니다.",
  code='''&lt;<span class="t">meta</span> <span class="a">name</span>=<span class="s">"viewport"</span> <span class="a">content</span>=<span class="s">"width=device-width, initial-scale=1"</span>&gt;

.screen {
  <span class="a">min-height</span>: <span class="a">100vh</span>;     <span class="c">/* 옛 브라우저 */</span>
  <span class="a">min-height</span>: <span class="a">100dvh</span>;    <span class="c">/* 아는 브라우저는 이 줄을 쓴다 */</span>
  <span class="a">display</span>: flex; <span class="a">flex-direction</span>: column;
}
.screen .cta { <span class="a">margin-top</span>: auto; }   <span class="c">/* 바닥에 붙인다 */</span>

<span class="c">/* 가로는 vw 대신 % */</span>
.full { <span class="a">width</span>: <span class="a">100%</span>; }

<span class="c">/* 키보드까지 따라가려면 직접 재야 한다 */</span>
visualViewport.addEventListener(<span class="s">'resize'</span>, () =&gt; {
  document.documentElement.style.setProperty(<span class="s">'--vvh'</span>, visualViewport.height + <span class="s">'px'</span>);
});''',
  keys=kbd([
    ("<code>meta viewport</code>", "없으면 폰이 <b>980px 창</b>인 척한다. 이 한 줄이 반응형의 전제다"),
    ("<code>user-scalable=no</code>를 쓰지 않는다", "확대를 막으면 <b>저시력 사용자가 못 읽는다</b>. 접근성 위반이다"),
    ("<code>maximum-scale</code>도 마찬가지", "5배까지는 열어 둔다"),
    ("두 줄로 겹쳐 적기", "모르는 단위가 나오는 줄은 <b>통째로 무시</b>되므로, 옛 줄을 먼저 적으면 저절로 대비가 된다"),
    ("<code>svh</code>·<code>dvh</code> 지원", "2022년 이후 브라우저. 그 전 것에는 <code>vh</code>가 떨어진다"),
    ("<code>100vw</code> 대신 <code>100%</code>", "세로 스크롤 막대가 있는 PC 에서 <b>가로 스크롤</b>이 생기는 흔한 원인"),
  ]),
  backend=rows([
    ("서버는 높이를 모른다", "창 높이는 <b>요청에 담겨 오지 않습니다.</b> 서버에서 미리 그려 보낼 때는 CSS 로만 처리합니다."),
    ("첫 그림이 흔들린다", "자바스크립트로 높이를 재서 넣는 방식은 <b>한 번 그린 뒤</b> 바뀌어 덜컥거립니다. CSS 단위로 되면 CSS 로 합니다."),
  ]),
  plat_lede="<b>웹에만 있는 문제</b>입니다. 앱에는 주소창이 없습니다.",
  plats=plats([
    ("웹", "vh · svh · lvh · dvh",
     phone(16, 104, "dvh", False, "105px"),
     "브라우저 UI 가 숨었다 나타나기 때문에 생긴 단위들입니다. 2022년에야 정리됐습니다."),
    ("iOS", "safe area · 전체 높이",
     '''              <div class="phone" role="img" aria-label="iOS 세이프 에어리어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;bottom:10px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px"></div></div></div>''',
     "앱에는 주소창이 없어 높이가 하나입니다. 대신 <a href=\"../items/safearea.html\">세이프 에어리어</a>를 빼야 합니다."),
    ("안드로이드", "insets",
     '''              <div class="phone" role="img" aria-label="안드로이드 인셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;bottom:10px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px"></div></div></div>''',
     "상태 표시줄·내비 바를 <b>인셋</b>으로 빼 줍니다. 역시 높이가 흔들리지는 않습니다."),
  ]),
  plat_note="\"폰에서 아래 버튼이 안 눌려요\"의 절반이 이것이고(<code>100vh</code>), 나머지 절반이 <a href=\"softkeyboard.html\">폰 키보드</a>입니다. PC 브라우저에서는 둘 다 재현되지 않아 <b>고쳤는지 확인할 길이 폰뿐</b>입니다 — 이 항목만큼은 실제 기기에서 한 번 열어 보는 일정을 넣어 두는 편이 낫습니다.",
  siblings=siblings("viewport"),
  related='''        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>''',
)
