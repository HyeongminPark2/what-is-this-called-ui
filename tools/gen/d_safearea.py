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
                    <span>위는 노치가 차지하는 두께</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span style="display:block;width:44px;height:10px;border-radius:3px;background:color-mix(in srgb,var(--danger) 45%,transparent);flex:none"></span>
                    <span>아래는 홈 막대가 차지하는 두께</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">env(safe-area-inset-top)</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">env(safe-area-inset-bottom)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">viewport-fit=cover   없으면 값이 늘 0</div>
                </div>
              </div>'''

D = dict(
  slug="safearea", ko="세이프 에어리어", en="Safe area · safe area insets",
  desc="노치와 홈 인디케이터가 차지하는 영역, env(safe-area-inset-*), 그리고 viewport-fit=cover를 빠뜨려서 생기는 문제를 보여 주는 항목입니다.",
  lede="세이프 에어리어는 화면에서 <b>무엇을 놓아도 안전한 영역</b>입니다. 그 바깥은 노치와 홈 막대가 차지하고 있어서, 글자나 버튼을 두면 가려지거나 눌리지 않습니다.",
  axes_lede="뼈대 항목은 눈에 보이지 않고 자리만 정해서 생김새로는 가를 수 없습니다. 아래 네 가지로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>빨간 띠는 내용을 <b>놓으면 안 되는 자리</b>입니다. 체크를 켜면 상단 바 글자가 노치 아래로 내려오고,
          탭바가 홈 인디케이터 위로 올라옵니다.<br>
          웹에서는 <code>env(safe-area-inset-top)</code> 같은 값으로 인셋을 읽는데,
          <b><code>viewport-fit=cover</code>를 적지 않으면 이 값이 항상 0</b>입니다.
          "env가 안 먹어요"라는 문제는 대부분 이 때문에 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "세이프 에어리어, 안전 영역"),
    ("영어", "safe area, safe area insets, notch, display cutout"),
    ("같이 쓰는 말",
     "위쪽 카메라 자리는 <b>노치</b>(notch) 또는 <b>다이내믹 아일랜드</b>, 구멍 모양은 "
     "<b>펀치홀</b>(punch hole · display cutout), 아래 막대는 <b>홈 인디케이터</b>(home indicator)입니다. "
     "안전 영역의 두께는 <b>인셋</b>(inset)이라고 하고, 화면 끝까지 그리는 것은 "
     "<b>엣지 투 엣지</b>(edge-to-edge)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>상태 바</b> — 시계와 배터리가 있는 띠는 <b>상태 바</b>이고, 세이프 에어리어는 "
     "상태 바까지 포함한 <b>'쓰면 안 되는 범위'</b>입니다.<br>"
     "<b>패딩</b> — <code>padding-top: 44px</code>처럼 숫자로 고정하면 기기마다 어긋나기 때문에 OS에 <b>값을 물어봐야</b> 합니다.<br>"
     "<b>뷰포트</b> — 화면 크기와 안전 영역은 다릅니다. 안전 영역은 화면 전체보다 안쪽에 있습니다."),
  ]),
  axes=ax("세이프 에어리어"),
  oneline="세이프 에어리어는 <b>개발자가 정하는 값이 아니라 OS에 물어보는 값</b>입니다. 숫자로 고정해 두면 그 값과 맞지 않는 기기에서 화면이 깨집니다.",
  s4_title="화면 모양에 따라 챙길 자리", s4_hint="기기와 화면 방향마다 달라지는 인셋",
  do_title="세이프 에어리어를 챙겨야 하는 경우",
  dont_title="세이프 에어리어를 다룰 때 피할 것",
  instead_title="세이프 에어리어와 함께 보면 좋은 항목",
  states=states([
    (ph(BAND_T + BAND_B + bar("모란상회") + bar("홈 · 정산 · 설정", False), "안 챙긴 화면"),
     "인셋을 챙기지 않았을 때", "글자가 <b>노치와 홈 막대에 겹칩니다</b>"),
    (ph(BAND_T + BAND_B + bar("모란상회", True, "padding-top:14px") + bar("홈 · 정산 · 설정", False, "padding-bottom:11px"), "챙긴 화면"),
     "인셋을 챙겼을 때", "바 자체는 화면 끝까지 두고, <b>내용만</b> 안쪽으로 밉니다"),
    (ph(BAND_T + bar("모란상회", True, "padding-top:14px"), "위만 있는 화면", "140px"),
     "위쪽만 챙기면 될 때", "꼬리말이 없으면 위쪽만 챙기면 됩니다"),
    ('''              <div style="position:relative;width:140px;height:80px;border-radius:12px;background:var(--ink-900);padding:4px;margin:0 auto">
                <div style="position:relative;height:100%;border-radius:9px;background:var(--surface);overflow:hidden">
                  <span style="position:absolute;top:0;bottom:0;left:0;width:11px;background:color-mix(in srgb,var(--danger) 18%,transparent)"></span>
                  <span style="position:absolute;top:0;bottom:0;right:0;width:11px;background:color-mix(in srgb,var(--danger) 18%,transparent)"></span>
                  <span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:0;height:0"></span>
                  <span style="position:absolute;left:0;top:50%;transform:translateY(-50%);width:9px;height:30px;background:var(--ink-900);border-radius:0 6px 6px 0"></span>
                  <span style="position:absolute;left:14px;top:9px;font-size:7.5px;color:var(--fg-muted)">가로로 돌리면 좌우에도 생김</span>
                </div>
              </div>''',
     "가로로 돌렸을 때", "인셋이 <b>좌우에도</b> 생겨서, 위아래만 챙기면 가로 화면에서 깨집니다"),
    (ph(BAND_B + bar("저장하기", False, "padding-bottom:11px"), "키보드가 올라온 화면", "140px"),
     "아래에 버튼을 붙였을 때", "화면 아래 버튼은 <b>홈 막대와 가장 자주 겹칩니다</b>"),
    ('''              <div style="position:relative;width:86px;height:140px;border-radius:14px;background:var(--ink-900);padding:4px;margin:0 auto">
                <div style="position:relative;height:100%;border-radius:11px;background:var(--surface);overflow:hidden">
                  <span style="position:absolute;left:0;right:0;top:0;height:28px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 5px,var(--ink-050) 5px 10px)"></span>
                  <span style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:34px;height:9px;background:var(--ink-900);border-radius:0 0 6px 6px;z-index:5"></span>
                  <span style="position:absolute;left:4px;top:32px;font-size:7px;color:var(--fg-muted)">사진은 끝까지 채움</span>
                </div>
              </div>''',
     "배경을 끝까지 채울 때", "사진과 배경색은 <b>노치 뒤까지</b> 채우고 글자만 안쪽에 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("화면 전체", "viewport", "기기의 물리적 화면입니다. <b>여기까지 그릴 수는 있습니다</b>"),
    ("위 인셋", "safe-area-inset-top", "노치와 상태 바가 차지하는 두께로, 기기마다 다릅니다"),
    ("아래 인셋", "safe-area-inset-bottom", "홈 인디케이터 자리입니다. <b>여기에 버튼을 두면 눌리지 않습니다</b>"),
    ("위 값 읽기", "env(safe-area-inset-top)", "숫자를 고정하지 않고 <b>OS에 값을 물어봅니다</b>"),
    ("아래 값 읽기", "env(safe-area-inset-bottom)", "홈 막대가 없는 기기에서는 0이 오기 때문에 <code>max()</code>와 함께 씁니다"),
    ("viewport-fit=cover", "meta viewport", "<b>이 설정이 없으면 env 값이 항상 0</b>입니다. 'env가 안 먹어요'라는 문제는 대개 이것이 원인입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          노치가 없는 기기나 데스크톱 브라우저에서는 인셋 값이 <b>0일 수도 있습니다</b>.
          그래서 <code>padding-bottom: env(safe-area-inset-bottom)</code>만 적으면 그런 기기에서
          패딩이 아예 사라집니다. <b><code>max(16px, env(…))</code></b>처럼 적어서
          최소 여백을 함께 정해 두는 것이 정석입니다.</p>''',
  do=ul([
    "<b>화면 끝까지</b> 그리는 앱이나 웹앱(엣지 투 엣지)을 만들 때",
    "화면 아래 <b>붙박이 버튼</b>이나 탭바가 있을 때",
    "노치 쪽까지 사진이나 배경을 채울 때. 배경은 끝까지 채우고 글자는 안쪽에 둡니다",
    "가로 화면을 지원할 때. <b>좌우 인셋</b>도 챙깁니다",
  ]),
  dont=ul([
    "<b>인셋을 숫자로 고정할</b> 때. <code>padding-top: 44px</code>은 다른 기기에서 맞지 않습니다",
    "<code>env()</code>만 쓰고 <b>최소값을 주지 않을</b> 때. 노치 없는 기기에서 여백이 0이 됩니다",
    "바의 <b>배경까지</b> 안쪽으로 밀 때. 화면 가장자리에 흰 띠가 남습니다",
    "<code>viewport-fit=cover</code> 없이 <code>env()</code> 값을 쓰려 할 때",
  ]),
  instead='화면 아래에 붙는 탭바 자체는 <a href="../items/bottomnav.html">바텀 탭바</a>에서, 위쪽 바는 <a href="../items/appbar.html">앱바</a>에서 다룹니다. 스크롤하는 동안 요소를 한자리에 붙여 두는 방법은 <a href="sticky.html">스티키</a>에서 봅니다.',
  cases=cases([
    (ph(BAND_B + bar("홈 · 정산 · 설정", False, "padding-bottom:11px"), "탭바 재현", "140px"),
     "바텀 탭바를 홈 막대 위로 올리기", "홈 막대와 가장 자주 겹치는 자리입니다. <b>아이콘이 홈 막대에 닿으면 눌리지 않습니다</b>"),
    (ph(BAND_B + bar("저장하기", False, "padding-bottom:11px"), "저장 바 재현", "140px"),
     "폼 아래 저장 바를 홈 막대 위로 올리기", "긴 폼 아래에 붙인 버튼도 탭바와 같은 문제를 겪습니다"),
    (ph(BAND_T + bar("← 상세", True, "padding-top:14px"), "상단 바 재현", "140px"),
     "상단 바를 노치 아래로 내리기", "뒤로가기 버튼이 <b>노치에 가려 눌리지 않는</b> 일이 흔합니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="메타 태그 한 줄과 패딩 한 줄",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="<code>&lt;meta&gt;</code> 한 줄과 <code>padding</code> 한 줄이면 되는데, <b>메타 태그를 먼저</b> 적어야 합니다.",
  code='''<span class="c">&lt;!-- 이 줄이 없으면 env( )가 항상 0이다 --&gt;</span>
&lt;<span class="t">meta</span> <span class="a">name</span>=<span class="s">"viewport"</span>
      <span class="a">content</span>=<span class="s">"width=device-width, initial-scale=1, viewport-fit=cover"</span>&gt;

<span class="c">/* 바 배경은 끝까지, 내용만 안쪽으로 */</span>
<span class="t">.bottom-nav</span> {
  <span class="a">padding-bottom</span>: <span class="t">max</span>(<span class="a">12px</span>, <span class="t">env</span>(safe-area-inset-bottom));
}                   <span class="c">/* ↑ 노치 없는 기기에서도 최소 12px */</span>

<span class="t">.app-bar</span> {
  <span class="a">padding-top</span>: <span class="t">max</span>(<span class="a">12px</span>, <span class="t">env</span>(safe-area-inset-top));
}

<span class="c">/* 가로 화면에서는 좌우도 챙긴다 */</span>
<span class="t">.page</span> {
  <span class="a">padding-inline</span>: <span class="t">max</span>(<span class="a">16px</span>, <span class="t">env</span>(safe-area-inset-left));
}''',
  keys=kbd([
    ("<code>viewport-fit=cover</code>부터 적기", "이 한 줄이 없으면 <code>env()</code>가 <b>모두 0</b>이 됩니다. env가 작동하지 않는 가장 흔한 원인입니다"),
    ("<code>max()</code>로 최소 여백 함께 주기", "노치 없는 기기에서 0이 와도 <b>최소 여백</b>이 남게 합니다"),
    ("바 배경은 화면 끝까지 두기", "바의 <b>배경은 화면 끝까지</b> 두고 안의 내용만 밉니다. 배경까지 밀면 가장자리에 띠가 생깁니다"),
    ("가로 화면의 좌우 인셋도 챙기기", "가로로 돌리면 <code>left</code>·<code>right</code>에 값이 생깁니다"),
    ("인셋을 숫자로 고정하지 않기", "44px·34px 같은 값은 <b>특정 기기에서만</b> 맞습니다"),
    ("실기기에서 눌러 보며 확인하기", "눈으로는 가려지지 않은 것 같아도 <b>눌리지 않는</b> 경우가 있으므로 실기기로 눌러 봅니다"),
  ]),
  backend=rows([
    ("화면에서만 처리하는 일", "세이프 에어리어는 화면에서만 처리하는 일입니다. 다만 <b>웹앱을 홈 화면에 설치</b>해 쓰는 경우라면 매니페스트의 <code>display: standalone</code>과 함께 생각해야 합니다."),
    ("테스트할 기기 조합", "노치 있는 기기, 노치 없는 기기, 가로 화면 <b>세 가지</b>가 최소한의 테스트 조합입니다. 브라우저 개발자 도구의 기기 에뮬레이션으로도 문제를 상당 부분 잡을 수 있습니다."),
    ("키보드가 올라올 때", "입력칸에 포커스가 가면 키보드가 올라와 화면이 줄어듭니다. 그래서 아래 붙박이 버튼은 <b>키보드 위로 올라오게</b> 따로 처리해야 합니다."),
    ("스크린샷으로 자동 검사하기", "글자 상자가 인셋 영역과 겹치는지는 좌표로 잴 수 있기 때문에, 실기기 없이도 <b>회귀를 막을</b> 수 있습니다."),
  ]),
  plat_lede="OS가 인셋 값을 알려 준다는 점은 같고, 이름과 기본값이 다릅니다.",
  plats=plats([
    ("웹", "env( ) + viewport-fit",
     ph(BAND_B + bar("탭바", False, "padding-bottom:11px"), "웹 재현", "120px", "74px"),
     "<code>env(safe-area-inset-*)</code>로 읽습니다. <b><code>viewport-fit=cover</code></b>가 없으면 값이 0이 되는 함정은 웹에만 있습니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.safeAreaInset( )<br>safeAreaLayoutGuide<br>.ignoresSafeArea( )</div>''',
     "<b>기본으로 안전 영역 안에</b> 그립니다. 화면 끝까지 그리려면 오히려 <code>.ignoresSafeArea()</code>로 <b>안전 영역을 벗어나야</b> 합니다."),
    ("안드로이드", "WindowInsets",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">WindowInsets<br>&nbsp;.safeDrawing<br>enableEdgeToEdge( )</div>''',
     "<b>WindowInsets</b>로 읽습니다. 최신 안드로이드는 <b>엣지 투 엣지가 기본</b>이라서 인셋을 챙기지 않으면 바로 겹칩니다."),
  ]),
  plat_note="플랫폼마다 <b>기본값이 정반대입니다.</b> iOS는 안전 영역 안쪽에 그리는 것이 기본이라서 따로 챙기지 않아도 안전하지만, 웹과 최신 안드로이드는 화면 끝까지 그리는 것이 기본이라서 <b>챙기지 않으면 겹칩니다.</b> 같은 시안을 세 플랫폼에 넘길 때 \"화면 끝까지 그릴지\"를 먼저 정해 두면 플랫폼마다 다른 버그가 생기는 일을 막을 수 있습니다.",
  siblings=siblings("safearea"),
  related='''        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>''',
)
