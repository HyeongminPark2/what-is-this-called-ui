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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100lvh는 주소창이 숨었을 때의 큰 높이</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100svh는 주소창이 보일 때의 작은 높이</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">100dvh는 지금 보이는 높이라 굴리면 바뀜</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">100vh는 100lvh와 같아 주소창이 보이면 넘침</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">100vw는 세로 막대 폭을 빼지 않아 가로로 넘침</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">meta viewport가 없으면 모두 다르게 계산됨</div>
                </div>
              </div>'''

D = dict(
  slug="viewport", ko="뷰포트 단위", en="Viewport units",
  desc="폰에서 100vh가 가리키는 높이가 주소창에 따라 달라지는 까닭과 svh·lvh·dvh의 차이, 바닥 버튼이 잘리는 이유를 보여 주는 항목입니다.",
  lede="폰 브라우저에서는 주소창이 숨었다 나타나기 때문에, <b>100vh 같은 뷰포트 단위가 가리키는 높이도 그때그때 달라집니다.</b>",
  axes_lede="PC와 폰의 차이는 기계 자체보다 화면을 쓰는 <b>전제</b>에 있습니다. 아래 네 가지를 물어보면 두 환경이 어디서 갈리는지 알 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 폰은 같은 화면을 각각 <code>100vh</code>·<code>100svh</code>·<code>100dvh</code>로 그린 것입니다.
          <b>주소창 보이기</b>를 켜 보면 <code>100vh</code>로 그린 폰에서만 바닥의 '다음' 버튼이 잘립니다.<br>
          아래 표는 <b>지금 보는 브라우저</b>에서 네 단위가 실제로 몇 px인지 잰 결과입니다.
          PC에는 숨었다 나타나는 주소창이 없어서 네 값이 같고, 차이는 <b>폰에서만</b> 드러납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "뷰포트 단위, 화면 높이 단위"),
    ("영어", "viewport units, vh / svh / lvh / dvh"),
    ("같이 쓰는 말",
     "<b>v</b>는 viewport, <b>h</b>는 height의 머리글자이고, 앞에 붙는 글자는 "
     "<b>s</b>mall(작은 쪽), <b>l</b>arge(큰 쪽), <b>d</b>ynamic(지금 보이는 만큼)을 뜻합니다. "
     "가로 폭은 <code>vw</code>로 적고, 짧은 쪽과 긴 쪽은 각각 <code>vmin</code>과 <code>vmax</code>로 적습니다. "
     "브라우저 창 안쪽에서 실제로 보이는 영역은 <b>비주얼 뷰포트</b>라고 하며 "
     "<code>window.visualViewport</code>로 크기를 읽습니다."),
    ("자주 잘못 부르는 이름",
     "<b>화면 높이</b> — 뷰포트 단위가 재는 것은 기기 화면이 아니라 <b>브라우저 창 안쪽</b>의 높이입니다.<br>"
     "<b>100%</b> — <code>100%</code>는 <b>부모 요소</b>의 높이를 기준으로 하고, <code>100vh</code>는 창의 높이를 기준으로 하므로 서로 다른 값입니다.<br>"
     "<b>풀스크린</b> — 화면 전체를 쓰게 하는 전체 화면 API와는 상관이 없습니다."),
  ]),
  axes=ax("뷰포트 단위"),
  oneline="<b>바닥에 버튼 같은 것이 붙는 화면이라면 <code>100dvh</code></b>를 씁니다. <code>100vh</code>는 주소창이 숨지 않는 PC에서만 화면 높이와 맞습니다.",
  s4_title="주소창에 따라 달라지는 높이", s4_hint="같은 100이 가리키는 네 가지 높이",
  dont_title="뷰포트 단위를 잘못 쓰는 경우",
  states=states([
    (phone(0, 120, "주소창이 없으면 셋이 같음"), "굴려서 주소창이 숨었을 때", "이때의 높이가 <b>lvh</b>이고, <b>vh</b>도 이 높이입니다"),
    (phone(16, 120, "100vh는 아래가 잘림", True), "주소창이 보일 때 vh로 그리면", "<b>vh는 큰 쪽 높이로 고정</b>되어 있어서 화면 아래로 넘칩니다"),
    (phone(16, 104, "100svh는 넘치지 않음"), "svh로 그렸을 때", "작은 쪽 높이입니다. 주소창이 숨으면 <b>아래에 빈 공간이 남습니다</b>"),
    (phone(16, 104, "100dvh는 보이는 만큼"), "dvh로 그렸을 때", "화면을 굴리면 높이가 따라 바뀌어서 <b>바닥에 딱 맞게 붙습니다</b>"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:72px;height:120px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:0;right:0;top:0;bottom:52px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px;margin:3px"></div>
                  <div style="position:absolute;left:0;right:0;bottom:0;height:52px;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted);text-align:center">키보드가 올라오면 또 줄어듦</span>
              </div>''',
     "키보드까지 올라왔을 때", "<a href=\"softkeyboard.html\">폰 키보드</a>가 차지하는 높이는 <code>dvh</code>에도 반영되지 않습니다"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:72px;height:120px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:3px;top:3px;width:84px;height:40px;background:var(--accent-soft);border:1px solid var(--danger);border-radius:4px"></div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--danger);text-align:center">100vw는 세로 막대 폭을 빼지 않음</span>
              </div>''',
     "가로 폭을 100vw로 잡았을 때", "<code>100vw</code>는 <b>스크롤 막대</b> 폭까지 포함합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("큰 쪽 높이", "lvh", "주소창이 숨었을 때의 높이로, <code>vh</code>와 같습니다"),
    ("작은 쪽 높이", "svh", "주소창이 보일 때의 높이입니다. 화면 밖으로 넘치지 않아 <b>늘 안전</b>하지만, 주소창이 숨으면 아래가 남습니다"),
    ("지금 보이는 높이", "dvh", "지금 보이는 만큼의 높이라서 <b>화면을 굴리면 따라 바뀝니다</b>"),
    ("vh가 가리키는 높이", "lvh와 같음", "큰 쪽 높이로 고정되어 있어서 <b>주소창이 보이면 화면 아래로 넘칩니다</b>"),
    ("가로 폭 단위", "100vw", "세로 스크롤 막대 폭을 <b>빼지 않기</b> 때문에 PC에서 가로로 넘칩니다"),
    ("먼저 넣을 태그", "meta viewport", "이 태그가 없으면 폰 브라우저가 화면을 <b>폭 980px짜리 창</b>으로 여기고 그려서, 뷰포트 단위와 미디어 쿼리가 모두 의도와 다르게 계산됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>100dvh</code>에도 단점이 있습니다.
          화면을 굴릴 때마다 값이 바뀌기 때문에, 그 높이를 쓰는 상자가 <b>크기를 따라 바꾸며 흔들립니다</b>.
          그래서 배경처럼 <b>가만히 있어야 하는 것</b>에는 <code>100lvh</code>가 낫고,
          <b>바닥에 버튼이 붙는 화면</b>에는 <code>100dvh</code>가 맞습니다.
          흔들림과 잘림을 둘 다 피하고 싶다면 <code>100svh</code>를 쓰고, 주소창이 숨었을 때 <b>아래가 조금 비는 것</b>은 감수합니다.</p>''',
  do=ul([
    "바닥에 버튼이 붙는 <b>한 화면짜리</b> 폼을 만들 때. <code>100dvh</code>를 씁니다",
    "화면을 꽉 채우는 <a href=\"../items/modal.html\">모달</a>이나 시트를 만들 때",
    "첫 화면을 채우는 히어로 영역을 만들 때. 다만 <b>흔들림</b>이 거슬리면 lvh를 고릅니다",
  ]),
  dont=ul([
    "<code>100vh</code>를 폰에서 그대로 쓸 때. 주소창이 보이면 <b>바닥이 잘립니다</b>",
    "<code>100vw</code>로 전체 폭을 잡을 때. PC에서 <b>가로 스크롤</b>이 생깁니다",
    "<code>&lt;meta name=\"viewport\"&gt;</code>를 빠뜨렸을 때",
    "키보드가 올라오는 문제까지 <code>dvh</code>로 해결될 거라고 여길 때. <a href=\"softkeyboard.html\">폰 키보드</a> 항목을 봅니다",
  ]),
  instead='부모 요소의 높이를 꽉 채우려면 <code>100%</code>를 쓰고, 바닥에 붙이려면 <a href="../items/sticky.html">스티키</a>나 <code>position:fixed</code>를 씁니다. 글줄 길이를 묶을 때는 <a href="../items/container.html">컨테이너</a>가 맞습니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.screen {</span>
                <span>&nbsp;&nbsp;min-height: 100vh;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">min-height: 100dvh;</span></span>
                <span>}</span>
              </div>''',
     "옛 단위와 새 단위를 두 줄로 적기", "옛 브라우저는 앞줄을, dvh를 아는 브라우저는 <b>뒷줄</b>을 씁니다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--danger)">width: 100vw;</span>
                <span style="color:var(--accent)">width: 100%;</span>
                <span style="font-size:8.5px">세로 막대가 있으면 vw가 더 넓음</span>
              </div>''',
     "가로 폭은 100%로 잡기", "전체 폭이 필요해도 <code>100vw</code> 대신 <code>100%</code>를 씁니다"),
    (phone(16, 104, "100dvh로 바닥에 맞춤", False, "150px"), "한 화면짜리 폼의 바닥 버튼", "주소창이 보이든 숨든 <b>다음 버튼이 늘 보입니다</b>"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="먼저 <code>meta viewport</code>를 적고, 높이는 옛 단위와 새 단위를 두 줄로 겹쳐 적습니다.",
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
    ("<code>meta viewport</code> 넣기", "이 태그가 없으면 폰 브라우저가 화면을 <b>폭 980px짜리 창</b>으로 여기고 그립니다. 반응형 화면은 이 한 줄이 있어야 작동합니다"),
    ("<code>user-scalable=no</code>를 쓰지 않기", "확대를 막으면 <b>저시력 사용자가 글을 읽을 수 없어서</b> 접근성 기준에 어긋납니다"),
    ("<code>maximum-scale</code>로 확대를 막지 않기", "확대 배율은 5배까지 허용해 둡니다"),
    ("두 줄로 겹쳐 적기", "브라우저는 모르는 단위가 나오는 줄을 <b>통째로 무시</b>하므로, 옛 단위 줄을 먼저 적어 두면 옛 브라우저에서도 그 줄이 적용됩니다"),
    ("<code>svh</code>·<code>dvh</code>를 지원하는 브라우저", "2022년 이후에 나온 브라우저가 지원합니다. 그 전 브라우저에서는 <code>vh</code> 줄이 적용됩니다"),
    ("<code>100vw</code> 대신 <code>100%</code> 쓰기", "세로 스크롤 막대가 있는 PC에서 <b>가로 스크롤</b>이 생기는 흔한 원인이 <code>100vw</code>입니다"),
  ]),
  backend=rows([
    ("서버가 알 수 없는 창 높이", "창 높이는 <b>요청에 담겨 오지 않습니다.</b> 그래서 서버에서 HTML을 미리 그려 보낼 때는 높이 처리를 CSS에 맡깁니다."),
    ("자바스크립트로 높이를 잴 때 생기는 흔들림", "자바스크립트로 높이를 재서 넣으면 화면을 <b>한 번 그린 뒤에</b> 높이가 바뀌어 화면이 덜컥거립니다. CSS 단위로 해결할 수 있으면 CSS로 처리합니다."),
  ]),
  plat_lede="앱에는 주소창이 없기 때문에, 높이가 흔들리는 것은 <b>웹에만 있는 문제</b>입니다.",
  plats=plats([
    ("웹", "vh · svh · lvh · dvh",
     phone(16, 104, "dvh", False, "105px"),
     "svh·lvh·dvh는 브라우저 UI가 숨었다 나타나는 문제 때문에 생긴 단위이고, 2022년에야 표준으로 정리되었습니다."),
    ("iOS", "safe area · 전체 높이",
     '''              <div class="phone" role="img" aria-label="iOS 세이프 에어리어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;bottom:10px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px"></div></div></div>''',
     "앱에는 주소창이 없어서 화면 높이가 하나로 정해집니다. 대신 노치와 홈 표시줄이 차지하는 <a href=\"../items/safearea.html\">세이프 에어리어</a>를 빼고 배치해야 합니다."),
    ("안드로이드", "insets",
     '''              <div class="phone" role="img" aria-label="안드로이드 인셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:24px;bottom:10px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:4px"></div></div></div>''',
     "상태 표시줄과 내비게이션 바가 차지하는 높이를 <b>인셋</b>(insets)으로 알려 줍니다. 안드로이드 앱도 주소창이 없어서 높이가 흔들리지는 않습니다."),
  ]),
  plat_note="\"폰에서 아래 버튼이 안 눌려요\"라는 문의는 대개 <code>100vh</code> 때문이거나 <a href=\"softkeyboard.html\">폰 키보드</a> 때문입니다. 두 문제 모두 PC 브라우저에서는 재현되지 않아서 <b>고쳤는지 확인하려면 폰에서 열어 봐야</b> 합니다. 그러니 이 부분은 일정에 실제 기기에서 한 번 열어 보는 단계를 넣어 두는 편이 낫습니다.",
  siblings=siblings("viewport"),
  related='''        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>''',
)
