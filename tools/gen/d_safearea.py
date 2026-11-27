# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ph(inner, label="", h="140px", w="86px"):
    return ('              <div style="position:relative;width:' + w + ';height:' + h + ';border-radius:14px;'
            'background:var(--ink-900);padding:4px;margin:0 auto" role="img" aria-label="' + label + '">'
            '<div style="position:relative;height:100%;border-radius:11px;background:var(--surface);overflow:hidden">'
            + inner +
            '<span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:34px;height:9px;'
            'background:var(--ink-900);border-radius:0 0 6px 6px;z-index:5"></span>'
            '<span style="position:absolute;left:50%;bottom:3px;transform:translateX(-50%);width:34px;height:2px;'
            'border-radius:99px;background:var(--ink-900);opacity:.35;z-index:5"></span>'
            '</div></div>')

BAND_T = ('<span style="position:absolute;left:0;right:0;top:0;height:12px;'
          'background:color-mix(in srgb,var(--danger) 18%,transparent);z-index:1"></span>')
BAND_B = ('<span style="position:absolute;left:0;right:0;bottom:0;height:9px;'
          'background:color-mix(in srgb,var(--danger) 18%,transparent);z-index:1"></span>')

def bar(text, top=True, pad=""):
    side = 'top:0' if top else 'bottom:0'
    return ('<span style="position:absolute;left:0;right:0;' + side + ';background:var(--accent);color:#fff;'
            'font-size:7px;font-weight:700;padding:4px 6px;z-index:3;' + pad + '">' + text + '</span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="position:relative;width:110px;height:170px;border-radius:18px;background:var(--ink-900);padding:5px">
                    <div style="position:relative;height:100%;border-radius:14px;background:var(--surface);overflow:hidden">
                      <span style="position:absolute;left:0;right:0;top:0;background:var(--accent);color:#fff;font-size:8px;font-weight:700;padding:5px 7px;padding-top:19px;z-index:3">모란상회</span>
                      <span style="position:absolute;left:0;right:0;bottom:0;background:var(--accent);color:#fff;font-size:8px;font-weight:700;padding:5px 7px;padding-bottom:15px;z-index:3;display:flex;justify-content:space-around"><span>홈</span><span>정산</span></span>
                      <span style="position:absolute;left:0;right:0;top:0;height:16px;background:color-mix(in srgb,var(--danger) 45%,transparent);z-index:4"></span>
                      <span style="position:absolute;left:0;right:0;bottom:0;height:12px;background:color-mix(in srgb,var(--danger) 45%,transparent);z-index:4"></span>
                      <span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:44px;height:11px;background:var(--ink-900);border-radius:0 0 7px 7px;z-index:5"></span>
                      <span style="position:absolute;left:50%;bottom:4px;transform:translateX(-50%);width:42px;height:2px;border-radius:99px;background:var(--ink-900);opacity:.35;z-index:5"></span>
                    </div>
                  </div>
                  <div class="pin-out" data-pin="2" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span style="display:block;width:44px;height:13px;border-radius:3px;background:color-mix(in srgb,var(--danger) 45%,transparent);flex:none"></span>
                    <span>위 — 노치가 가져가는 두께</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span style="display:block;width:44px;height:10px;border-radius:3px;background:color-mix(in srgb,var(--danger) 45%,transparent);flex:none"></span>
                    <span>아래 — 홈 막대가 가져가는 두께</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">env(safe-area-inset-top)</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">env(safe-area-inset-bottom)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">viewport-fit=cover   — 없으면 값이 늘 0</div>
                </div>
              </div>'''

D = dict(
  slug="safearea", ko="세이프 에어리어", en="Safe area · safe area insets",
  desc="노치와 홈 인디케이터가 차지하는 영역과 env(safe-area-inset-*), viewport-fit=cover 함정을 보여주는 항목.",
  lede="화면에서 <b>무엇을 놓아도 안전한 영역</b>. 그 바깥은 노치와 홈 막대가 가져가서, 글자나 버튼을 두면 가려지거나 안 눌립니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>빨간 띠가 <b>못 쓰는 자리</b>입니다. 체크를 켜 보세요 — 상단 바 글자가 노치 아래로 내려오고
          탭바가 홈 인디케이터 위로 올라옵니다.<br>
          웹에서는 <code>env(safe-area-inset-top)</code> 같은 값으로 읽는데,
          <b><code>viewport-fit=cover</code>를 안 적으면 이 값이 늘 0</b>입니다 —
          "env 가 안 먹어요"의 대부분이 이것입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "세이프 에어리어, 안전 영역"),
    ("영어", "safe area, safe area insets, notch, display cutout"),
    ("같이 쓰는 말",
     "위쪽 카메라 자리는 <b>노치</b>(notch) 또는 <b>다이내믹 아일랜드</b>, 구멍 모양은 "
     "<b>펀치홀</b>(punch hole · display cutout), 아래 막대는 <b>홈 인디케이터</b>(home indicator)입니다. "
     "안전 영역의 두께를 <b>인셋</b>(inset)이라 하고, 화면 끝까지 그리는 것을 "
     "<b>엣지 투 엣지</b>(edge-to-edge)라 합니다."),
    ("자주 잘못 부름",
     "<b>상태 바</b> — 시계·배터리가 있는 띠는 <b>상태 바</b>이고, 세이프 에어리어는 "
     "그것까지 포함한 <b>'쓰면 안 되는 범위'</b>입니다.<br>"
     "<b>패딩</b> — 그냥 <code>padding-top: 44px</code>로 못 박으면 기기마다 틀립니다. <b>값을 물어봐야</b> 합니다.<br>"
     "<b>뷰포트</b> — 화면 크기와 안전 영역은 다릅니다. 화면은 넓고 안전 영역은 그 안쪽입니다."),
  ]),
  axes=ax("세이프 에어리어"),
  oneline="세이프 에어리어는 <b>내가 정하는 값이 아니라 OS 에게 물어보는 값</b>입니다. 숫자를 못 박는 순간 어느 기기에선가 깨집니다.",
  s4_title="갈래", s4_hint="기기와 방향마다 다르다",
  states=states([
    (ph(BAND_T + BAND_B + bar("모란상회") + bar("홈 · 정산 · 설정", False), "안 챙긴 화면"),
     "안 챙김", "글자가 <b>노치와 홈 막대에 겹친다</b>"),
    (ph(BAND_T + BAND_B + bar("모란상회", True, "padding-top:14px") + bar("홈 · 정산 · 설정", False, "padding-bottom:11px"), "챙긴 화면"),
     "챙김", "바 자체는 끝까지, <b>내용만</b> 안쪽으로 민다"),
    (ph(BAND_T + bar("모란상회", True, "padding-top:14px"), "위만 있는 화면", "140px"),
     "위만", "꼬리말이 없으면 위만 챙기면 된다"),
    ('''              <div style="position:relative;width:140px;height:80px;border-radius:12px;background:var(--ink-900);padding:4px;margin:0 auto">
                <div style="position:relative;height:100%;border-radius:9px;background:var(--surface);overflow:hidden">
                  <span style="position:absolute;top:0;bottom:0;left:0;width:11px;background:color-mix(in srgb,var(--danger) 18%,transparent)"></span>
                  <span style="position:absolute;top:0;bottom:0;right:0;width:11px;background:color-mix(in srgb,var(--danger) 18%,transparent)"></span>
                  <span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:0;height:0"></span>
                  <span style="position:absolute;left:0;top:50%;transform:translateY(-50%);width:9px;height:30px;background:var(--ink-900);border-radius:0 6px 6px 0"></span>
                  <span style="position:absolute;left:14px;top:9px;font-size:7.5px;color:var(--fg-muted)">가로로 돌리면 좌우에도 생긴다</span>
                </div>
              </div>''',
     "가로 화면", "<b>좌우에도</b> 생긴다. 위아래만 챙기면 여기서 깨진다"),
    (ph(BAND_B + bar("저장하기", False, "padding-bottom:11px"), "키보드가 올라온 화면", "140px"),
     "붙박이 버튼", "화면 아래 버튼은 <b>홈 막대와 가장 자주 부딪힌다</b>"),
    ('''              <div style="position:relative;width:86px;height:140px;border-radius:14px;background:var(--ink-900);padding:4px;margin:0 auto">
                <div style="position:relative;height:100%;border-radius:11px;background:var(--surface);overflow:hidden">
                  <span style="position:absolute;left:0;right:0;top:0;height:28px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 5px,var(--ink-050) 5px 10px)"></span>
                  <span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:34px;height:9px;background:var(--ink-900);border-radius:0 0 6px 6px;z-index:5"></span>
                  <span style="position:absolute;left:4px;top:32px;font-size:7px;color:var(--fg-muted)">사진은 끝까지</span>
                </div>
              </div>''',
     "배경은 끝까지", "사진·배경색은 <b>노치 뒤까지</b> 보내고 글자만 안으로"),
  ]),
  anat=ANAT,
  pins=pins([
    ("화면 전체", "viewport", "기기의 물리적 화면. <b>여기까지 그릴 수는 있다</b>"),
    ("위 인셋", "safe-area-inset-top", "노치·상태 바가 차지하는 두께. 기기마다 다르다"),
    ("아래 인셋", "safe-area-inset-bottom", "홈 인디케이터 자리. <b>버튼을 두면 안 눌린다</b>"),
    ("위 값 읽기", "env(safe-area-inset-top)", "숫자를 못 박지 않고 <b>OS 에게 물어본다</b>"),
    ("아래 값 읽기", "env(safe-area-inset-bottom)", "홈 막대가 없는 기기에서는 0 이 온다 — 그래서 <code>max()</code>와 함께 쓴다"),
    ("viewport-fit=cover", "meta viewport", "<b>이게 없으면 env 값이 늘 0</b>이다. 'env 가 안 먹어요'의 정답"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          인셋 값은 <b>0 일 수도 있습니다</b> — 노치 없는 기기, 데스크톱 브라우저가 그렇습니다.
          그래서 <code>padding-bottom: env(safe-area-inset-bottom)</code>만 적으면 그런 기기에서
          패딩이 아예 사라집니다. <b><code>max(16px, env(…))</code></b>처럼 적어서
          '최소한 이만큼은'을 함께 정해 두는 것이 정석입니다.</p>''',
  do=ul([
    "<b>화면 끝까지</b> 그리는 앱·웹앱(엣지 투 엣지)",
    "화면 아래 <b>붙박이 버튼</b>이나 탭바가 있을 때",
    "노치 쪽까지 사진·배경을 보낼 때 — 배경은 끝까지, 글자는 안쪽으로",
    "가로 화면을 지원할 때 — <b>좌우 인셋</b>도 챙깁니다",
  ]),
  dont=ul([
    "<b>숫자를 못 박는 것</b> — <code>padding-top: 44px</code>은 다음 기기에서 틀립니다",
    "<code>env()</code>만 쓰고 <b>최소값을 안 주는</b> 것 — 노치 없는 기기에서 여백이 0이 됩니다",
    "바의 <b>배경까지</b> 안쪽으로 미는 것 — 가장자리에 흰 띠가 남습니다",
    "<code>viewport-fit=cover</code> 없이 <code>env()</code>를 기대하는 것",
  ]),
  instead='아래 붙박이 줄 자체는 <a href="../items/bottomnav.html">바텀 탭바</a>, 위는 <a href="../items/appbar.html">앱바</a>, 굴릴 때 붙이는 일은 <a href="sticky.html">스티키</a>.',
  cases=cases([
    (ph(BAND_B + bar("홈 · 정산 · 설정", False, "padding-bottom:11px"), "탭바 재현", "140px"),
     "바텀 탭바", "가장 자주 부딪히는 자리. <b>아이콘이 홈 막대에 닿으면 안 눌린다</b>"),
    (ph(BAND_B + bar("저장하기", False, "padding-bottom:11px"), "저장 바 재현", "140px"),
     "붙박이 저장 바", "긴 폼의 아래 버튼. 같은 문제를 똑같이 겪는다"),
    (ph(BAND_T + bar("← 상세", True, "padding-top:14px"), "상단 바 재현", "140px"),
     "상단 바", "뒤로가기 버튼이 <b>노치에 가려 안 눌리는</b> 일이 흔하다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="두 줄이면 끝난다",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="<code>&lt;meta&gt;</code> 한 줄과 <code>padding</code> 한 줄입니다. <b>메타가 먼저</b>입니다.",
  code='''<span class="c">&lt;!-- 이게 없으면 env( ) 가 늘 0 이다 --&gt;</span>
&lt;<span class="t">meta</span> <span class="a">name</span>=<span class="s">"viewport"</span>
      <span class="a">content</span>=<span class="s">"width=device-width, initial-scale=1, viewport-fit=cover"</span>&gt;

<span class="c">/* 바 배경은 끝까지, 내용만 안쪽으로 */</span>
<span class="t">.bottom-nav</span> {
  <span class="a">padding-bottom</span>: <span class="t">max</span>(<span class="a">12px</span>, <span class="t">env</span>(safe-area-inset-bottom));
}                   <span class="c">/* ↑ 노치 없는 기기에서도 최소 12px */</span>

<span class="t">.app-bar</span> {
  <span class="a">padding-top</span>: <span class="t">max</span>(<span class="a">12px</span>, <span class="t">env</span>(safe-area-inset-top));
}

<span class="c">/* 가로 화면 — 좌우도 잊지 않는다 */</span>
<span class="t">.page</span> {
  <span class="a">padding-inline</span>: <span class="t">max</span>(<span class="a">16px</span>, <span class="t">env</span>(safe-area-inset-left));
}''',
  keys=kbd([
    ("<code>viewport-fit=cover</code> 먼저", "이 한 줄이 없으면 <code>env()</code>가 <b>전부 0</b>이다. 1번 원인"),
    ("<code>max()</code>와 함께 쓴다", "노치 없는 기기에서 0 이 와도 <b>최소 여백</b>이 남게"),
    ("배경은 끝까지", "바의 <b>배경은 화면 끝까지</b>, 안의 내용만 민다. 안 그러면 가장자리에 띠가 생긴다"),
    ("좌우도 챙긴다", "가로로 돌리면 <code>left</code>·<code>right</code>에 값이 생긴다"),
    ("숫자를 못 박지 않는다", "44px·34px 같은 값은 <b>그 기기에서만</b> 맞다"),
    ("터치 자리로 확인한다", "눈에 안 가려 보여도 <b>안 눌리는</b> 경우가 있다. 실기기로 눌러 본다"),
  ]),
  backend=rows([
    ("서버가 할 일은 없다", "순수하게 화면의 일입니다. 다만 <b>웹앱을 홈 화면에 설치</b>해 쓰는 경우라면 매니페스트의 <code>display: standalone</code>과 함께 생각해야 합니다."),
    ("기기 목록으로 테스트", "노치 있는 기기 · 없는 기기 · 가로 화면 <b>세 가지</b>가 최소 조합입니다. 브라우저 개발자 도구의 기기 흉내로도 상당 부분 잡힙니다."),
    ("키보드가 올라올 때", "입력칸에 포커스가 가면 화면이 줄어듭니다. 아래 붙박이 버튼은 <b>키보드 위로 올라오게</b> 따로 다뤄야 합니다."),
    ("스크린샷 자동 검사", "글자 상자가 인셋 영역과 겹치는지는 좌표로 잴 수 있습니다. 실기기 없이도 <b>회귀를 막을</b> 수 있습니다."),
  ]),
  plat_lede="OS 가 값을 알려 주는 것은 같고, 이름과 기본값이 다릅니다.",
  plats=plats([
    ("웹", "env( ) + viewport-fit",
     ph(BAND_B + bar("탭바", False, "padding-bottom:11px"), "웹 재현", "120px", "74px"),
     "<code>env(safe-area-inset-*)</code>. <b><code>viewport-fit=cover</code></b> 가 없으면 값이 0 이라는 함정이 웹에만 있습니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.safeAreaInset( )<br>safeAreaLayoutGuide<br>.ignoresSafeArea( )</div>''',
     "<b>기본이 안전 영역 안</b>입니다. 끝까지 그리려면 오히려 <code>.ignoresSafeArea()</code>로 <b>빠져나와야</b> 합니다."),
    ("안드로이드", "WindowInsets",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">WindowInsets<br>&nbsp;.safeDrawing<br>enableEdgeToEdge( )</div>''',
     "<b>WindowInsets</b> 로 읽습니다. 최신 안드로이드는 <b>엣지 투 엣지가 기본</b>이라 안 챙기면 바로 겹칩니다."),
  ]),
  plat_note="<b>기본값이 정반대입니다.</b> iOS 는 안전 영역 '안'이 기본이라 안 챙기면 안전하고, 웹과 최신 안드로이드는 '끝까지'가 기본이라 <b>안 챙기면 겹칩니다.</b> 같은 시안을 세 쪽에 넘길 때 \"끝까지 그릴지\"를 먼저 정해 두면 서로 다른 버그를 안 만듭니다.",
  siblings=siblings("safearea"),
  related='''        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
