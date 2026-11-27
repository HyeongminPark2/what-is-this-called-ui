# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def pair(light, dark, cap, sub):
    return ('              <div style="display:grid;gap:7px;width:100%%;max-width:150px">'
            '<span style="display:block;height:34px;border-radius:8px;background:%s;border:1px solid var(--line)"></span>'
            '<span style="display:block;height:34px;border-radius:8px;background:%s;border:1px solid #2a2f38"></span>'
            '<span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center">%s</span>'
            '<span style="font-size:10.5px;color:var(--fg-faint);text-align:center">%s</span></div>'
            ) % (light, dark, cap, sub)

ANAT = '''              <div style="background:#0d0f13;border-radius:var(--r2);padding:14px 10px 14px 0">
                <div style="padding-left:26px">
                  <div class="pin-out" data-pin="1" style="background:#15181e;border:1px solid #272c35;border-radius:10px;padding:13px 13px 14px">
                    <div style="padding-left:26px;display:grid;gap:11px">
                      <div class="pin-out" data-pin="2" style="font-size:13px;font-weight:700;color:#e8ebf0">정산 요약</div>
                      <div class="pin-out" data-pin="3" style="font-size:11.5px;color:#9aa3b2">이번 주 ₩1,284,000</div>
                      <div class="pin-out" data-pin="4" style="background:#1c2029;border:1px solid #2b313b;border-radius:8px;padding:8px 10px;font-size:11px;color:#c7cedb">떠 있는 면은 <b style="color:#fff">더 밝게</b></div>
                      <div class="pin-out" data-pin="5" style="display:inline-block;background:#6f9bff;color:#10131a;border-radius:7px;padding:6px 12px;font-size:11.5px;font-weight:700;justify-self:start">확정하기</div>
                      <div class="pin-out" data-pin="6" style="font-size:11px;color:#9aa3b2;border-top:1px solid #272c35;padding-top:9px">사진은 <b style="color:#c7cedb">살짝 어둡게</b></div>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="dark", ko="다크 모드", en="Dark mode · dark theme",
  desc="다크 모드가 색을 뒤집는 일이 아니라 두 벌의 값을 따로 정하는 일이라는 것을 실물과 해부도로 보여주는 항목.",
  lede="같은 화면을 위한 <b>두 벌의 값</b>. 밝은 색을 뒤집는 것이 아니라, 어두운 바탕에 맞춰 <b>따로 고른</b> 색입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위 카드는 토큰만 쓰고, 아래 카드는 <code>#ffffff</code>를 <b>직접 박아</b> 뒀습니다.
          <b>어둡게 켜기</b>를 눌러 보세요 — 아래 카드만 혼자 하얗게 남습니다.
          다크 모드가 깨졌다는 제보의 대부분이 이것입니다. 대비비도 같이 다시 잽니다.</p>
        </div>''',
  names=rows([
    ("한국어", "다크 모드, 어두운 테마, 야간 모드"),
    ("영어", "dark mode, dark theme, night mode"),
    ("같이 쓰는 말",
     "밝은 쪽을 <b>라이트 모드</b>라 부릅니다. OS 설정을 따라가는 것은 <b>시스템 따름</b>(system · auto), "
     "대비를 더 높인 것은 <b>고대비</b>(high contrast)입니다. "
     "검정을 완전한 <code>#000</code>으로 쓰는 것은 OLED 전용인 <b>블랙 모드</b>(AMOLED · true black)로 따로 부릅니다."),
    ("자주 잘못 부름",
     "<b>색 반전</b> — OS 의 색 반전은 사진까지 뒤집는 <b>접근성 기능</b>이고 다크 모드가 아닙니다.<br>"
     "<b>테마</b> — 테마는 더 넓은 말입니다. 다크 모드는 테마 <b>한 쌍</b>을 가리킵니다.<br>"
     "<b>야간 모드</b> — 화면을 노랗게 만드는 <b>나이트 시프트</b>(색온도)와는 다른 것입니다."),
  ]),
  axes=ax("다크 모드"),
  oneline="다크 모드는 <b>색을 뒤집는 일이 아니라 값을 한 벌 더 만드는 일</b>입니다. 뒤집어서 되는 화면은 처음부터 토큰을 쓴 화면뿐입니다.",
  s4_title="모드", s4_hint="두 벌로 끝나지 않는다",
  states=states([
    (pair("#ffffff", "#15181e", "--bg", "바탕"), "바탕", "순검정(<code>#000</code>)은 눈이 아프다. <b>#121~#18</b> 언저리를 쓴다"),
    (pair("#f6f8fb", "#1c2029", "--surface", "떠 있는 면"), "면", "밝은 쪽은 더 희게, <b>어두운 쪽은 더 밝게</b> — 방향이 뒤집힌다"),
    (pair("#14161a", "#e8ebf0", "--fg", "본문 글"), "글", "어두운 쪽 글은 순백(<code>#fff</code>)보다 살짝 낮춘다"),
    (pair("#2f6df6", "#6f9bff", "--accent", "강조"), "강조", "같은 파랑을 쓰면 어두운 바탕에서 <b>대비가 모자란다</b>"),
    (pair("#e4e8ee", "#272c35", "--line", "선"), "선", "어두운 쪽에서는 선보다 <b>면의 밝기 차</b>가 더 잘 보인다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:150px">
                <span style="display:block;height:34px;border-radius:8px;background:#ffffff;border:1px solid var(--line);box-shadow:0 6px 14px rgba(20,22,26,.16)"></span>
                <span style="display:block;height:34px;border-radius:8px;background:#1c2029;border:1px solid #2b313b"></span>
                <span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center">--e2</span>
                <span style="font-size:10.5px;color:var(--fg-faint);text-align:center">그림자</span></div>''',
     "그림자", "어두운 바탕에서는 그림자가 <b>안 보인다</b>. 대신 면을 밝혀 높이를 낸다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바탕", "background", "가장 아래. <b>순검정이 아니다</b> — 흰 글과의 대비가 너무 세서 글자가 번져 보인다"),
    ("제목 글", "fg", "흰색을 그대로 쓰지 않고 한 단계 낮춘다(<code>#e8ebf0</code>)"),
    ("보조 글", "fg-muted", "밝은 모드의 회색을 그대로 가져오면 대비가 모자란다. <b>다시 재야</b> 한다"),
    ("떠 있는 면", "surface · elevated", "어두운 쪽에서는 <b>위로 올라갈수록 밝아진다</b>. 그림자 대신 밝기가 높이를 말한다"),
    ("강조색", "accent", "채도를 낮추고 밝기를 올린다. 밝은 모드의 원색은 어두운 바탕에서 눈을 찌른다"),
    ("사진 · 일러스트", "media", "흰 바탕이 든 그림은 밝기를 살짝(<code>brightness(.9)</code>) 낮춘다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          방향이 <b>뒤집히는 규칙</b>이 하나 있습니다. 밝은 모드에서는 위로 올라갈수록 <b>그림자가 짙어지고</b>,
          어두운 모드에서는 위로 올라갈수록 <b>면이 밝아집니다.</b> 그림자 토큰만 복사해 오면
          어두운 화면에서는 아무 일도 일어나지 않습니다.</p>''',
  do=ul([
    "오래 보는 화면 — 읽기 앱, 코드 편집기, 영상",
    "어두운 데서 쓰는 화면 — 밤에 보는 폰",
    "토큰을 <b>이미 쓰고 있을</b> 때. 그때만 비용이 싸집니다",
    "OS 설정을 따라갈 수 있을 때(<code>prefers-color-scheme</code>)",
  ]),
  dont=ul([
    "색이 화면 곳곳에 <b>직접 박혀</b> 있을 때 — 먼저 토큰으로 바꾸는 것이 순서입니다",
    "사진과 색이 주인공인 화면 — 쇼핑몰 상품 사진은 흰 바탕에서 더 잘 보입니다",
    "인쇄용 화면 · 문서",
    "'요즘 다 하니까' — 두 벌을 <b>끝까지 관리할</b> 사람이 없으면 한쪽이 반드시 썩습니다",
  ]),
  instead='색을 쓰임으로 먼저 정리하는 것이 <a href="color.html">색 토큰</a>이고, 어두운 쪽의 높이 표현은 <a href="elevation.html">고도</a>에서 이어집니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:8px;width:100%;max-width:220px;font-size:12px">
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled checked style="accent-color:var(--accent)"> 시스템 설정 따름</label>
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled> 밝게</label>
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled> 어둡게</label>
              </div>''',
     "세 갈래 설정", "<b>따름 / 밝게 / 어둡게</b>. 켬·끔 두 개만 두면 OS 를 따라갈 길이 없다"),
    ('''              <div style="display:grid;gap:0;width:100%;max-width:220px;border-radius:10px;overflow:hidden;border:1px solid var(--line)">
                <div style="background:#fff;color:#14161a;padding:10px;font-size:12px">밝은 쪽 — 위로 갈수록 <b>그림자</b>가 짙어진다</div>
                <div style="background:#15181e;color:#e8ebf0;padding:10px;font-size:12px">어두운 쪽 — 위로 갈수록 <b>면이 밝아진다</b></div>
              </div>''',
     "높이의 방향", "같은 '위'를 두 모드가 다른 방법으로 말한다"),
    ('''              <div style="display:grid;gap:6px;width:100%;max-width:220px">
                <div style="background:#15181e;border-radius:8px;padding:9px;display:grid;gap:6px">
                  <span style="display:block;height:22px;border-radius:5px;background:#1c2029"></span>
                  <span style="display:block;height:22px;border-radius:5px;background:#ffffff"></span>
                </div>
                <span style="font-size:11px;color:var(--danger)">아래 칸만 색이 박혀 있다</span>
              </div>''',
     "안 따라오는 한 칸", "다크 모드 제보의 대부분. <b>토큰을 안 쓴 자리</b>가 그대로 드러난다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="두 벌을 어떻게 갈아 끼우나",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="OS 설정을 기본으로 따르고, 사용자가 고른 값이 있으면 그것을 우선합니다. <b>깜빡임</b>을 막는 것이 마지막 한 수입니다.",
  code='''<span class="c">/* 1) OS 설정을 기본으로 따른다 */</span>
<span class="t">:root</span> { <span class="a">color-scheme</span>: light dark; <span class="a">--bg</span>: <span class="s">#fff</span>; <span class="a">--fg</span>: <span class="s">#14161a</span>; }
<span class="t">@media</span> (<span class="a">prefers-color-scheme</span>: dark) {
  <span class="t">:root</span> { <span class="a">--bg</span>: <span class="s">#15181e</span>; <span class="a">--fg</span>: <span class="s">#e8ebf0</span>; }
}

<span class="c">/* 2) 사용자가 고른 값이 있으면 그것이 이긴다 */</span>
<span class="t">:root[data-theme="dark"]</span> { <span class="a">--bg</span>: <span class="s">#15181e</span>; <span class="a">--fg</span>: <span class="s">#e8ebf0</span>; }
<span class="t">:root[data-theme="light"]</span> { <span class="a">--bg</span>: <span class="s">#fff</span>; <span class="a">--fg</span>: <span class="s">#14161a</span>; }

<span class="c">// 3) &lt;head&gt; 안에서 먼저 칠한다 — 안 그러면 흰 화면이 한 번 번쩍인다</span>
<span class="t">document</span>.documentElement.dataset.theme =
  localStorage.getItem(<span class="s">'theme'</span>) ?? <span class="s">''</span>;''',
  keys=kbd([
    ("<code>color-scheme</code>를 적는다", "스크롤바·입력창 같은 <b>브라우저가 그리는 부품</b>까지 따라오게 한다. 이거 하나로 해결되는 제보가 많다"),
    ("OS 를 기본으로", "<code>prefers-color-scheme</code>이 먼저고, 사용자가 고른 값은 그 위에 덮는다"),
    ("첫 칠을 먼저", "저장된 설정을 <code>&lt;head&gt;</code>에서 읽어 적용한다. 나중에 하면 <b>흰 화면이 번쩍</b>인다"),
    ("대비를 다시 잰다", "밝은 쪽에서 통과한 회색이 어두운 쪽에서도 통과하지는 않는다. <b>두 벌 모두</b> 잰다"),
    ("사진과 아이콘", "흰 바탕이 든 그림·로고는 어두운 쪽 전용을 따로 준비하거나 밝기를 낮춘다"),
  ]),
  backend=rows([
    ("설정은 어디에 두나", "기기마다 다를 수 있어 <b>로컬에 두는 것이 기본</b>입니다. 계정에 저장하면 기기를 옮겨도 따라오지만, 밤에만 어둡게 쓰는 사람에게는 거슬립니다."),
    ("서버 렌더링", "서버는 사용자의 OS 설정을 모릅니다. 그래서 첫 HTML 은 늘 한쪽으로 칠해져 나오고, <b>브라우저에서 한 번 고쳐</b> 그립니다 — 이 틈이 번쩍임입니다."),
    ("메일 · PDF 처럼 밖으로 나가는 것", "메일 클라이언트는 다크 모드에서 색을 <b>제멋대로 바꿉니다.</b> 중요한 글자는 색에만 기대지 않게 만듭니다."),
    ("이미지 두 벌", "로고처럼 모드마다 달라야 하는 그림은 <code>&lt;picture&gt;</code>로 두 벌을 보내거나 SVG 안에서 <code>currentColor</code>를 씁니다."),
  ]),
  plat_lede="두 OS 는 다크 모드를 <b>시스템 기능</b>으로 갖고 있습니다. 앱이 할 일은 거스르지 않는 것입니다.",
  plats=plats([
    ("웹", "prefers-color-scheme",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">@media (prefers-<br>&nbsp;&nbsp;color-scheme: dark)</div>''',
     "미디어 쿼리로 OS 설정을 읽습니다. <code>color-scheme</code> 속성을 함께 적어야 <b>스크롤바와 입력창</b>까지 따라옵니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">UITraitCollection<br>.userInterfaceStyle</div>''',
     "<b>Dark Mode</b> · 시맨틱 색을 쓰면 거의 저절로 됩니다. 어두운 쪽에서 면이 밝아지는 규칙도 OS 가 갖고 있습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">isSystemInDarkTheme()<br>darkColorScheme()</div>''',
     "<b>Dark theme</b> · 색 역할마다 밝은·어두운 값이 짝으로 정의돼 있습니다. 순검정은 권하지 않습니다."),
  ]),
  plat_note="\"다크 모드 해 주세요\"가 세 플랫폼에서 비용이 아주 다릅니다. iOS·안드로이드는 <b>시맨틱 색만 썼다면 거의 공짜</b>지만, 웹에서 색을 직접 박아 뒀다면 화면 전부를 다시 훑어야 합니다. 일정 이야기를 할 때 이 차이를 먼저 확인하는 편이 좋습니다.",
  siblings=siblings("dark"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>
        <li><span class="na"><b>모션 줄이기</b><em>9부</em></span></li>
        <li><span class="na"><b>설정 화면</b><em>13부</em></span></li>''',
)
