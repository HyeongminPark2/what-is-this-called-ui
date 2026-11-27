# -*- coding: utf-8 -*-
from ax12 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def card(size, h="", clip=False, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    inner = ('<span style="font-weight:700;font-size:' + size + '">모란상회</span>'
             '<span style="color:var(--fg-muted);font-size:' + size + ';display:block'
             + (';height:' + h + ';overflow:hidden' if h else '') + '">11월 1일 ~ 7일 정산이 승인되었습니다. 수수료를 뺀 금액이 들어갑니다.</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">'
            + inner + '</div>'
            + ('<span style="font-size:8.5px;color:' + ('var(--danger)' if clip else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">rem · em   — 사용자 설정을 따라감</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">px로 고정하면 설정을 켜도 커지지 않음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">높이까지 px로 고정하면 글이 잘림</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">200%까지 키워도 내용과 기능을 잃지 않을 것</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">user-scalable=no는 쓰지 않음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자 크기 설정과 화면 전체 확대는 서로 다른 설정</div>
                </div>
              </div>'''

D = dict(
  slug="textzoom", ko="확대와 글자 크기", en="Zoom & text resize",
  desc="사용자가 글자를 키웠을 때도 화면을 쓸 수 있는지 다루는 항목입니다. 글자 크기를 px로 고정하면 글자가 커지지 않고, 상자 높이까지 고정하면 글이 잘립니다.",
  lede="사용자는 브라우저나 OS 설정으로 <b>글자를 키울 수 있습니다</b>. 저시력인 사람은 이 설정으로 글자를 키워야 화면을 읽을 수 있습니다.",
  axes_lede="접근성은 다 만든 뒤에 덧붙이기보다 만드는 동안 <b>빠뜨리지 않고 챙기는 일</b>입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 글자를 키워 보세요. 실제로는 사용자가 OS나 브라우저 설정으로 <b>직접</b> 글자를 키웁니다.<br>
          <b>글자 크기를 px로 고정하기</b>를 켜면 막대를 끌어도 글자가 커지지 않고, 상자 높이까지 px로 고정하면 <b>글이 잘립니다</b>.
          이 사고는 글자 크기 설정을 켠 사람만 겪기 때문에 <b>개발하는 사람의 화면에서는 드러나지 않습니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "확대, 글자 크기 조절, 글자 키우기, 텍스트 리사이즈"),
    ("영어", "zoom, text resize, text spacing, dynamic type"),
    ("같이 쓰는 말",
     "화면 전체를 키우는 것은 <b>브라우저 확대</b>(zoom), 글자만 키우는 것은 <b>글자 크기 설정</b>이라고 합니다. "
     "글자 크기 설정을 iOS에서는 <b>다이내믹 타입</b>, 안드로이드에서는 <b>글꼴 크기</b>라고 부릅니다. "
     "WCAG에는 <b>200%까지 확대해도 쓸 수 있어야 한다</b>는 기준(1.4.4)과 "
     "<b>글자 간격을 늘려도 화면이 깨지지 않아야 한다</b>는 기준(1.4.12)이 따로 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>반응형</b> — 반응형은 화면 폭이 달라질 때를 다루고, 이 항목은 <b>글자가 커질 때</b>를 다룹니다. 다만 화면이 바뀌는 결과가 비슷해서 자주 섞어 부릅니다.<br>"
     "<b>핀치 줌</b> — 두 손가락을 벌려 키우는 것도 확대에 속하지만, 핀치 줌을 <b>막아 두는 코드</b>가 흔해서 따로 짚어야 합니다.<br>"
     "<b>화면 밀도</b> — <a href=\"dpr.html\">화면 밀도</a>는 기기가 원래 가진 성질이고, 글자 크기는 <b>사용자가 고르는 설정</b>입니다."),
  ]),
  axes=ax("확대와 글자 크기"),
  oneline="<b>글자 크기는 rem으로 정하고, 상자 높이는 고정하지 않습니다.</b> 그러면 글자 크기 설정을 켠 사람도 화면을 그대로 쓸 수 있습니다.",
  s4_title="글자를 키웠을 때의 모습", s4_hint="배율과 단위에 따라 무엇이 깨지는지",
  states=states([
    (card("10px", note="기본 크기 100%"), "기본 크기일 때", "개발하는 사람이 보통 보는 모습입니다"),
    (card("13px", note="150%, rem이면 같이 커짐", ok=True), "150%로 키웠을 때", "<b>상자가 글자 크기에 맞춰</b> 늘어납니다"),
    (card("17px", note="200%, 여기까지는 지켜야 함", ok=True), "200%로 키웠을 때", "WCAG가 이 배율까지 쓸 수 있어야 한다고 정한 <b>상한</b>입니다"),
    (card("10px", note="px로 고정해 설정을 켜도 그대로", ok=False), "글자 크기를 px로 고정했을 때", "글자 크기를 px로 고정하면 <b>설정을 바꿔도 글자가 커지지 않습니다</b>"),
    (card("17px", h="22px", clip=True, note="높이까지 고정해 글이 잘림", ok=False), "상자 높이까지 고정했을 때", "커진 글이 상자 밖으로 넘쳐 잘리므로 <b>내용을 잃습니다</b>"),
    (one(mono('user-scalable=no', 'var(--danger)'), "확대 막기", False, "폰에서 아예 키울 수 없음"),
     "확대를 막아 두었을 때", "<b>접근성 기준 위반</b>입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>rem</code>", "설정을 따라감", "뿌리 요소(html)의 글자 크기에 곱하는 배수입니다"),
    ("<code>px</code>", "커지지 않음", "px로 고정하면 <b>글자 크기 설정을 바꿔도 반영되지 않습니다</b>"),
    ("상자 높이", "고정하지 않음", "높이를 고정하지 않고, 내용이 커지는 만큼 상자도 늘어나게 둡니다"),
    ("200%", "지켜야 하는 선", "200%까지 키워도 <b>내용과 기능</b>을 잃지 않아야 합니다"),
    ("<code>user-scalable=no</code>", "쓰지 않음", "핀치 줌을 막는 것은 <b>접근성 기준 위반</b>입니다"),
    ("두 가지 설정", "글자만 / 화면 전체", "두 설정은 따로 켜지므로 <b>둘 다</b> 확인해야 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>글자를 키웠을 때 화면이 깨지는 원인은 대개 px로 고정해 둔 상자 높이입니다.</b>
          <code>font-size</code>를 <code>rem</code>으로 두어도
          상자에 <code>height: 40px</code>이 고정되어 있으면 커진 글이 잘립니다.
          버튼, 칩, 표의 줄처럼 <b>높이를 딱 맞춰 정돈한 곳</b>에서 특히 이런 일이 생깁니다.
          <code>height</code>를 <code>min-height</code>로 바꾸고 <code>overflow</code>를 열어 두면
          대부분 해결되고, 그렇게 고쳐 두면 <b>번역해서 글이 길어질 때</b>도 화면이 깨지지 않습니다.</p>''',
  do=ul([
    "글자 크기를 정할 때. <b>rem</b> 단위로 정합니다",
    "상자 높이를 정할 때. 높이를 <b>고정하지 말고</b> <code>min-height</code>로 정합니다",
    "화면을 다 만든 뒤 점검할 때. 글자를 <b>200%로 키워서 한 번</b> 열어 봅니다",
  ]),
  dont=ul([
    "<code>user-scalable=no</code>나 <code>maximum-scale=1</code>로 확대를 막을 때. <b>접근성 기준 위반</b>입니다",
    "<code>font-size</code>를 px로 고정할 때",
    "상자 높이를 px로 고정하고 <code>overflow:hidden</code>을 걸 때",
    "글자를 키우면 버튼이 화면 밖으로 밀려나는 식으로 <b>기능이 사라질</b> 때",
  ]),
  do_title="글자 크기 설정에 대비해야 하는 경우",
  dont_title="글자를 키울 수 없게 만드는 실수",
  instead_title="글자 크기와 이어지는 주제는 다른 항목에서 다룹니다",
  instead='기기가 원래 가진 배율은 <a href="dpr.html">화면 밀도</a>에서, 화면 폭에 따라 배치를 바꾸는 방법은 <a href="breakpoint.html">브레이크포인트</a>에서 다룹니다. 한 줄에 들어가는 글의 길이는 <a href="../items/container.html">컨테이너</a>를 보세요.',
  cases=cases([
    (code(['html { font-size: 100% }', '.card { font-size: 0.95rem }'], "150px", "설정을 그대로 따라감", True),
     "글자 크기를 rem으로 정하기", "글자 크기는 <b>rem</b>으로 정합니다"),
    (code(['.btn { min-height: 44px }', '/* height 가 아니다 */'], "150px", "글이 커지면 같이 늘어남", True),
     "상자 높이를 min-height로 정하기", "높이는 <code>min-height</code>로 정합니다"),
    (one(mono('width=device-width, initial-scale=1', 'var(--accent)'), "메타 태그", True, "확대를 막는 값을 넣지 않음"),
     "뷰포트 메타 태그로 확대 허용하기", "<a href=\"viewport.html\">뷰포트 단위</a>에서 다루는 것과 같은 뷰포트 메타 태그입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="글자 크기는 <code>rem</code>으로 정하고, 상자 높이는 고정하지 않고 열어 둡니다.",
  code='''&lt;<span class="t">meta</span> <span class="a">name</span>=<span class="s">"viewport"</span>
      <span class="a">content</span>=<span class="s">"width=device-width, initial-scale=1"</span>&gt;
<span class="c">&lt;!-- user-scalable=no · maximum-scale=1 을 넣지 않는다 --&gt;</span>

<span class="t">html</span> { <span class="a">font-size</span>: <span class="a">100%</span>; }        <span class="c">/* 브라우저·OS 설정을 그대로 받는다 */</span>
<span class="t">body</span> { <span class="a">font-size</span>: <span class="a">1rem</span>; }

.btn  { <span class="a">min-height</span>: <span class="a">44px</span>; }   <span class="c">/* height 가 아니다 */</span>
.card { <span class="a">min-height</span>: <span class="a">0</span>; <span class="a">overflow</span>: visible; }

<span class="c">/* 글자가 커져 한 줄에 다 들어가지 않으면 다음 줄로 넘긴다 */</span>
.row { <span class="a">display</span>: flex; <span class="a">flex-wrap</span>: wrap; <span class="a">gap</span>: <span class="a">var</span>(--s2); }''',
  keys=kbd([
    ("글자 크기는 <code>rem</code>으로", "뿌리 요소의 글자 크기에 곱하는 배수라서 <b>사용자 설정을 그대로</b> 따라갑니다"),
    ("<code>html</code>에 px을 고정하지 않기", "뿌리 요소에 <code>font-size: 16px</code>을 적으면 <b>사용자의 글자 크기 설정이 무시</b>됩니다"),
    ("높이는 <code>min-height</code>로", "<a href=\"touchtarget.html\">터치 타깃</a> 최소 크기를 지키면서도, 글이 커지면 상자가 같이 늘어납니다"),
    ("<code>flex-wrap: wrap</code>으로 줄 넘기기", "글자가 커져 한 줄에 들어가지 않으면 <b>다음 줄로 넘어가게</b> 둡니다"),
    ("<code>user-scalable=no</code> 쓰지 않기", "확대를 막으면 <b>WCAG 1.4.4 위반</b>입니다"),
    ("확인하는 방법", "브라우저는 <b>200%</b>로 확대하고, 폰은 <b>글자 크기를 최대</b>로 두고 화면을 열어 봅니다"),
  ]),
  backend=rows([
    ("서버로 전달되지 않는 설정", "사용자의 글자 크기 설정은 <b>서버로 오는 요청에 담기지 않으므로</b>, 화면 쪽에서 CSS로만 다룹니다."),
    ("번역으로 글이 길어질 때와 같은 문제", "글자를 키웠을 때 깨지는 자리는 번역해서 글이 길어질 때 깨지는 자리와 <b>거의 같아서</b>, 한 번 고치면 두 문제가 함께 해결됩니다."),
  ]),
  plat_lede="웹, iOS, 안드로이드 모두 글자 크기는 <b>사용자가 직접 켜는 설정</b>입니다.",
  plats=plats([
    ("웹", "rem · 브라우저 확대",
     card("12px", w="110px"),
     "브라우저 확대와 글자 크기 설정이 <b>따로</b> 있어서 둘 다 확인해야 합니다."),
    ("iOS", "Dynamic Type",
     '''              <div class="phone" role="img" aria-label="iOS 글자 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;font-size:8px;font-weight:700">모란상회</div></div></div>''',
     "시스템 글자 스타일을 쓰면 사용자 설정을 <b>자동으로</b> 따라갑니다. 접근성 설정에서는 글자를 훨씬 더 크게 키울 수도 있습니다."),
    ("안드로이드", "sp 단위",
     '''              <div class="phone" role="img" aria-label="안드로이드 글자 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;font-size:8px;font-weight:700">모란상회</div></div></div>''',
     "글자 크기는 <b>sp</b>, 나머지 크기는 <b>dp</b>로 적습니다. 글자를 sp로 적어야 사용자 설정을 따라갑니다."),
  ]),
  plat_note="이 항목의 문제는 개발하는 사람이 글자 크기 설정을 켜 두지 않는 한 <b>개발 화면에서는 드러나지 않습니다</b>. 그래서 일부러 <b>브라우저는 200%로 확대하고, 폰은 글자 크기를 최대로 둔 채 화면을 한 번 열어 봐야</b> 합니다. 그렇게 한 번만 열어 봐도 높이를 고정해 둔 자리가 대부분 드러납니다.",
  siblings=siblings("textzoom"),
  related='''        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="../items/truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
