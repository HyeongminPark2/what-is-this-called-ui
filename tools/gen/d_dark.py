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
  desc="다크 모드는 색을 뒤집는 일이 아니라 값을 한 벌 더 따로 정하는 일이라는 것을 실물과 해부도로 보여 주는 항목입니다.",
  lede="다크 모드는 같은 화면에 쓸 색 값을 <b>두 벌</b> 정해 두고 바꿔 쓰는 방식입니다. 어두운 쪽 색은 밝은 색을 뒤집어 얻는 것이 아니라, 어두운 바탕에 맞춰 <b>따로 고른</b> 색입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 값을 어떻게 쓸지 <b>정해 둔 규칙</b>입니다. 그래서 생김새 대신 아래 네 가지를 물어보면 토큰끼리 무엇이 다른지 가려집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위 카드는 토큰만 쓰고, 아래 카드는 <code>#ffffff</code>를 코드에 <b>직접 적어</b> 두었습니다.
          <b>어두운 모드로 바꾸기</b>를 눌러 보면 아래 카드만 하얗게 남는데, 다크 모드가 깨졌다는 제보는 대부분 이렇게 색을 직접 적어 둔 자리에서 나옵니다.
          모드를 바꿀 때마다 글자의 대비비도 다시 재서 보여 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "다크 모드, 어두운 테마, 야간 모드"),
    ("영어", "dark mode, dark theme, night mode"),
    ("같이 쓰는 말",
     "밝은 쪽은 <b>라이트 모드</b>라고 부릅니다. OS 설정을 따라 바뀌는 것은 <b>시스템 따름</b>(system · auto), "
     "대비를 더 높인 것은 <b>고대비</b>(high contrast)입니다. "
     "바탕을 완전한 검정인 <code>#000</code>으로 칠하는 방식은 OLED 화면용으로 따로 <b>블랙 모드</b>(AMOLED · true black)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>색 반전</b> — OS의 색 반전은 사진 색까지 모두 뒤집는 <b>접근성 기능</b>이지 다크 모드가 아닙니다.<br>"
     "<b>테마</b> — 테마는 더 넓은 뜻의 말이고, 다크 모드는 밝은 테마와 어두운 테마 <b>한 쌍</b>을 가리킵니다.<br>"
     "<b>야간 모드</b> — 이렇게 부르면 색온도를 낮춰 화면을 노랗게 만드는 <b>나이트 시프트</b>와 헷갈리기 쉬운데, 둘은 서로 다른 기능입니다."),
  ]),
  axes=ax("다크 모드"),
  oneline="다크 모드는 <b>색을 뒤집는 일이 아니라 값을 한 벌 더 만드는 일</b>입니다. 그래서 값만 바꿔 끼워 어두운 화면으로 바꿀 수 있는 것은 처음부터 토큰을 쓴 화면뿐입니다.",
  s4_title="쓰임별로 정한 두 모드의 값", s4_hint="쓰임마다 밝은 쪽과 어두운 쪽 값을 고르는 규칙",
  states=states([
    (pair("#ffffff", "#15181e", "--bg", "바탕"), "페이지 바탕", "순검정(<code>#000</code>)은 눈이 쉽게 피로해지므로 <b>#121~#18</b> 언저리의 색을 씁니다"),
    (pair("#f6f8fb", "#1c2029", "--surface", "떠 있는 면"), "떠 있는 면", "밝은 쪽에서는 더 희게, <b>어두운 쪽에서는 더 밝게</b> 칠해서 방향이 뒤집힙니다"),
    (pair("#14161a", "#e8ebf0", "--fg", "본문 글"), "본문 글자", "어두운 쪽 글자는 순백(<code>#fff</code>)보다 밝기를 살짝 낮춥니다"),
    (pair("#2f6df6", "#6f9bff", "--accent", "강조"), "강조색", "밝은 쪽과 같은 파랑을 쓰면 어두운 바탕에서 <b>대비가 모자랍니다</b>"),
    (pair("#e4e8ee", "#272c35", "--line", "선"), "구분선", "어두운 쪽에서는 선을 긋는 것보다 <b>면의 밝기 차</b>로 나누는 편이 더 잘 보입니다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:150px">
                <span style="display:block;height:34px;border-radius:8px;background:#ffffff;border:1px solid var(--line);box-shadow:0 6px 14px rgba(20,22,26,.16)"></span>
                <span style="display:block;height:34px;border-radius:8px;background:#1c2029;border:1px solid #2b313b"></span>
                <span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center">--e2</span>
                <span style="font-size:10.5px;color:var(--fg-faint);text-align:center">그림자</span></div>''',
     "그림자로 높이를 나타낼 때", "어두운 바탕에서는 그림자가 <b>잘 보이지 않습니다</b>. 그래서 그림자 대신 면을 밝게 칠해 높이를 나타냅니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바탕", "background", "가장 아래에 깔리는 색입니다. 순검정을 쓰면 흰 글자와의 대비가 너무 커서 글자가 번져 보이기 때문에 <b>순검정은 쓰지 않습니다</b>"),
    ("제목 글", "fg", "흰색을 그대로 쓰지 않고 한 단계 낮춘 색(<code>#e8ebf0</code>)을 씁니다"),
    ("보조 글", "fg-muted", "밝은 모드의 회색을 그대로 가져오면 대비가 모자라므로, 어두운 바탕에서 대비비를 <b>다시 재야</b> 합니다"),
    ("떠 있는 면", "surface · elevated", "어두운 쪽에서는 <b>위에 놓인 면일수록 밝게</b> 칠합니다. 그림자 대신 밝기 차이로 높이를 나타내는 방식입니다"),
    ("강조색", "accent", "채도를 낮추고 밝기를 올립니다. 밝은 모드의 원색을 그대로 쓰면 어두운 바탕에서 지나치게 튀어 눈이 피로합니다"),
    ("사진 · 일러스트", "media", "흰 바탕이 들어 있는 그림은 밝기를 살짝(<code>brightness(.9)</code>) 낮춥니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          두 모드 사이에서 방법이 <b>뒤바뀌는 규칙</b>이 하나 있습니다. 밝은 모드에서는 위에 놓인 면일수록 <b>그림자가 짙어지고</b>,
          어두운 모드에서는 위에 놓인 면일수록 <b>면 자체가 밝아집니다.</b> 그래서 밝은 모드의 그림자 토큰만 복사해 오면
          어두운 화면에서는 그림자가 거의 보이지 않아 높이 차이가 드러나지 않습니다.</p>''',
  do=ul([
    "읽기 앱이나 코드 편집기, 영상처럼 오래 보는 화면일 때",
    "밤에 보는 폰처럼 어두운 곳에서 쓰는 화면일 때",
    "색 토큰을 <b>이미 쓰고 있을</b> 때. 토큰이 있으면 값만 한 벌 더 만들면 되므로 비용이 적게 듭니다",
    "OS 설정을 따라갈 수 있을 때(<code>prefers-color-scheme</code>)",
  ]),
  dont=ul([
    "색 값이 화면 곳곳에 <b>직접 적혀</b> 있을 때. 이때는 다크 모드보다 토큰으로 바꾸는 일을 먼저 합니다",
    "사진과 색을 보여 주는 것이 목적인 화면일 때. 예를 들어 쇼핑몰 상품 사진은 흰 바탕에서 더 잘 보입니다",
    "인쇄용 화면이나 문서일 때",
    "'요즘 다들 하니까'라는 이유뿐일 때. 두 벌을 <b>계속 관리할</b> 사람이 없으면 한쪽 값이 고쳐지지 않은 채 남아 화면이 어긋납니다",
  ]),
  instead_title="다크 모드와 함께 보면 좋은 항목",
  instead='다크 모드를 만들기 전에 색을 쓰임별로 정리하는 방법은 <a href="color.html">색 토큰</a> 항목에서 다루고, 어두운 화면에서 높이를 나타내는 방법은 <a href="elevation.html">고도</a> 항목에서 이어서 설명합니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:8px;width:100%;max-width:220px;font-size:12px">
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled checked style="accent-color:var(--accent)"> 시스템 설정 따름</label>
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled> 밝게</label>
                <label style="display:flex;align-items:center;gap:8px"><input type="radio" disabled> 어둡게</label>
              </div>''',
     "모드 설정을 세 가지로 두기", "설정을 <b>따름 / 밝게 / 어둡게</b> 세 가지로 둡니다. 켬과 끔 두 가지만 두면 OS 설정을 따르게 할 방법이 없습니다"),
    ('''              <div style="display:grid;gap:0;width:100%;max-width:220px;border-radius:10px;overflow:hidden;border:1px solid var(--line)">
                <div style="background:#fff;color:#14161a;padding:10px;font-size:12px">밝은 쪽은 위로 갈수록 <b>그림자</b>가 짙어짐</div>
                <div style="background:#15181e;color:#e8ebf0;padding:10px;font-size:12px">어두운 쪽은 위로 갈수록 <b>면이 밝아짐</b></div>
              </div>''',
     "두 모드에서 높이를 나타내는 방법", "같은 높이를 두 모드가 서로 다른 방법으로 나타냅니다"),
    ('''              <div style="display:grid;gap:6px;width:100%;max-width:220px">
                <div style="background:#15181e;border-radius:8px;padding:9px;display:grid;gap:6px">
                  <span style="display:block;height:22px;border-radius:5px;background:#1c2029"></span>
                  <span style="display:block;height:22px;border-radius:5px;background:#ffffff"></span>
                </div>
                <span style="font-size:11px;color:var(--danger)">아래 칸만 색을 직접 적어 둠</span>
              </div>''',
     "모드를 따라 바뀌지 않는 칸", "다크 모드 오류 제보는 대부분 이런 경우입니다. <b>토큰을 쓰지 않은 자리</b>만 밝은 색으로 남습니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="두 벌의 값을 바꿔 끼우는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
  code_lede="기본으로는 OS 설정을 따르고, 사용자가 직접 고른 값이 있으면 그 값을 우선합니다. 마지막으로 페이지를 처음 그릴 때 흰 화면이 잠깐 보이는 <b>깜빡임</b>을 막아야 합니다.",
  code='''<span class="c">/* 1) OS 설정을 기본으로 따른다 */</span>
<span class="t">:root</span> { <span class="a">color-scheme</span>: light dark; <span class="a">--bg</span>: <span class="s">#fff</span>; <span class="a">--fg</span>: <span class="s">#14161a</span>; }
<span class="t">@media</span> (<span class="a">prefers-color-scheme</span>: dark) {
  <span class="t">:root</span> { <span class="a">--bg</span>: <span class="s">#15181e</span>; <span class="a">--fg</span>: <span class="s">#e8ebf0</span>; }
}

<span class="c">/* 2) 사용자가 고른 값이 있으면 그 값을 우선한다 */</span>
<span class="t">:root[data-theme="dark"]</span> { <span class="a">--bg</span>: <span class="s">#15181e</span>; <span class="a">--fg</span>: <span class="s">#e8ebf0</span>; }
<span class="t">:root[data-theme="light"]</span> { <span class="a">--bg</span>: <span class="s">#fff</span>; <span class="a">--fg</span>: <span class="s">#14161a</span>; }

<span class="c">// 3) &lt;head&gt; 안에서 먼저 적용한다. 늦으면 흰 화면이 한 번 번쩍인다</span>
<span class="t">document</span>.documentElement.dataset.theme =
  localStorage.getItem(<span class="s">'theme'</span>) ?? <span class="s">''</span>;''',
  keys=kbd([
    ("<code>color-scheme</code> 속성 적기", "스크롤바나 입력창처럼 <b>브라우저가 그리는 부품</b>까지 어두운 색으로 바뀌게 합니다. 이 속성 하나만 적어도 해결되는 제보가 많습니다"),
    ("OS 설정을 기본으로 따르기", "<code>prefers-color-scheme</code>을 기본으로 따르고, 사용자가 고른 값이 있으면 그 위에 덮어씁니다"),
    ("본문을 그리기 전에 모드 적용하기", "저장된 설정을 <code>&lt;head&gt;</code>에서 읽어 바로 적용합니다. 본문을 그린 뒤에 적용하면 <b>흰 화면이 한 번 번쩍</b>입니다"),
    ("두 모드에서 대비비를 따로 재기", "밝은 쪽에서 대비비 기준을 통과한 회색이 어두운 쪽에서도 통과한다는 보장은 없으므로 <b>두 벌 모두</b> 잽니다"),
    ("사진과 아이콘을 어두운 쪽에 맞추기", "흰 바탕이 들어 있는 그림이나 로고는 어두운 쪽 전용 그림을 따로 준비하거나 밝기를 낮춥니다"),
  ]),
  backend=rows([
    ("모드 설정을 저장하는 곳", "모드 설정은 기기마다 다를 수 있어서 <b>기기에 저장하는 것이 기본</b>입니다. 계정에 저장하면 기기를 바꿔도 설정이 따라오지만, 밤에만 어둡게 쓰는 사람에게는 오히려 불편할 수 있습니다."),
    ("서버 렌더링에서 생기는 번쩍임", "서버는 사용자의 OS 설정을 알 수 없기 때문에 첫 HTML은 늘 한쪽 모드의 색으로 만들어집니다. 브라우저는 이 HTML을 받은 뒤 <b>설정에 맞게 한 번 고쳐</b> 그리는데, 고쳐 그리기 전 잠깐 보이는 화면이 번쩍임입니다."),
    ("메일과 PDF처럼 밖으로 보내는 문서", "메일 클라이언트는 다크 모드에서 보낸 쪽이 정한 색을 <b>자기 규칙대로 바꿉니다.</b> 그래서 중요한 내용은 색에만 기대지 않도록 만듭니다."),
    ("모드마다 이미지를 따로 보내기", "로고처럼 모드마다 달라야 하는 그림은 <code>&lt;picture&gt;</code>로 두 벌을 보내거나 SVG 안에서 <code>currentColor</code>를 씁니다."),
  ]),
  plat_lede="iOS와 안드로이드에는 다크 모드가 <b>시스템 기능</b>으로 들어 있습니다. 그래서 앱은 시스템 설정을 거스르지 않고 따르기만 하면 됩니다.",
  plats=plats([
    ("웹", "prefers-color-scheme",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">@media (prefers-<br>&nbsp;&nbsp;color-scheme: dark)</div>''',
     "미디어 쿼리로 OS 설정을 읽습니다. <code>color-scheme</code> 속성을 함께 적어야 <b>스크롤바와 입력창</b>까지 어두운 색으로 바뀝니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">UITraitCollection<br>.userInterfaceStyle</div>''',
     "<b>Dark Mode</b> · 시맨틱 색을 쓰면 대부분 저절로 바뀝니다. 어두운 쪽에서 위에 놓인 면을 밝게 칠하는 규칙도 OS에 들어 있습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">isSystemInDarkTheme()<br>darkColorScheme()</div>''',
     "<b>Dark theme</b> · 색 역할마다 밝은 값과 어두운 값이 짝으로 정의돼 있고, 바탕에 순검정을 쓰는 것은 권하지 않습니다."),
  ]),
  plat_note="\"다크 모드 해 주세요\"라는 요청은 플랫폼마다 드는 비용이 크게 다릅니다. iOS와 안드로이드에서는 <b>시맨틱 색만 썼다면 추가 작업이 거의 없지만</b>, 웹에서 색 값을 직접 적어 두었다면 화면 전부를 다시 살펴봐야 합니다. 그래서 일정을 이야기할 때 이 차이부터 확인하는 편이 좋습니다.",
  siblings=siblings("dark"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="settings.html"><b>설정 화면</b><em>13부</em></a></li>''',
)
