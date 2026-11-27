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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">rem · em — 사용자 설정을 따라간다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">px 로 박으면 설정을 켜도 안 커진다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">높이까지 px 로 박으면 글이 잘린다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">200%까지 키워도 내용과 기능을 잃지 않을 것</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">user-scalable=no 를 쓰지 않는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자만 키우는 설정과 화면 전체 확대는 다르다</div>
                </div>
              </div>'''

D = dict(
  slug="textzoom", ko="확대와 글자 크기", en="Zoom & text resize",
  desc="사용자가 글자를 키웠을 때도 쓰이는가. px로 박으면 안 커지고, 높이까지 박으면 잘린다.",
  lede="사용자는 <b>글자를 키울 수 있습니다</b>. 저시력인 사람에게는 이게 유일한 길입니다.",
  axes_lede="접근성은 따로 붙이는 것이 아니라 <b>빠뜨리지 않는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 글자를 키워 보세요. OS·브라우저 설정으로 <b>사용자가 직접</b> 키울 수 있습니다.<br>
          <b>px 로 박아 두기</b>를 켜면 안 커지고, 상자 높이까지 박으면 <b>글이 잘립니다</b> —
          설정을 켠 사람만 겪는 사고라 <b>우리 화면에서는 안 보입니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "확대, 글자 크기 조절, 글자 키우기, 텍스트 리사이즈"),
    ("영어", "zoom, text resize, text spacing, dynamic type"),
    ("같이 쓰는 말",
     "화면 전체를 키우는 것이 <b>브라우저 확대</b>(zoom), 글자만 키우는 것이 <b>글자 크기 설정</b>입니다. "
     "iOS 는 <b>다이내믹 타입</b>, 안드로이드는 <b>글꼴 크기</b>라 부릅니다. "
     "WCAG 에는 <b>200%까지 확대</b>(1.4.4)와 "
     "<b>글자 간격을 늘려도 안 깨질 것</b>(1.4.12)이 따로 적혀 있습니다."),
    ("자주 잘못 부름",
     "<b>반응형</b> — 폭이 달라지는 것과 <b>글자가 커지는</b> 것은 다릅니다. 다만 결과가 비슷해 섞입니다.<br>"
     "<b>핀치 줌</b> — 손가락으로 벌리는 것도 확대지만, <b>막아 두는 코드</b>가 흔해 따로 짚어야 합니다.<br>"
     "<b>화면 밀도</b> — <a href=\"dpr.html\">화면 밀도</a>는 기기의 성질이고, 이쪽은 <b>사용자의 선택</b>입니다."),
  ]),
  axes=ax("확대와 글자 크기"),
  oneline="<b>크기는 rem 으로, 높이는 박지 마세요.</b> 그러면 설정을 켠 사람에게도 그대로 쓰입니다.",
  s4_title="키웠을 때", s4_hint="무엇이 깨지나",
  states=states([
    (card("10px", note="기본 — 100%"), "기본", "우리가 보는 모습"),
    (card("13px", note="150% — rem 으로 두면 따라온다", ok=True), "150%", "<b>상자가 글에 맞춰</b> 늘어난다"),
    (card("17px", note="200% — 여기까지는 지켜야 한다", ok=True), "200%", "WCAG 가 요구하는 <b>상한</b>"),
    (card("10px", note="px 로 박음 — 설정을 켜도 안 커진다", ok=False), "px 로 박으면", "<b>설정이 아무 일도 안 한다</b>"),
    (card("17px", h="22px", clip=True, note="높이까지 박음 — 글이 잘렸다", ok=False), "높이까지 박으면", "<b>내용을 잃는다</b>"),
    (one(mono('user-scalable=no', 'var(--danger)'), "확대 막기", False, "폰에서 아예 못 키운다"),
     "확대를 막으면", "<b>접근성 위반</b>이다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>rem</code>", "설정을 따라간다", "뿌리 글자 크기의 배수다"),
    ("<code>px</code>", "안 커진다", "<b>설정이 아무 일도 안 한다</b>"),
    ("높이", "박지 않는다", "내용이 밀고 늘어나게 둔다"),
    ("200%", "지켜야 하는 선", "여기까지 <b>내용과 기능</b>을 잃지 않아야 한다"),
    ("<code>user-scalable=no</code>", "쓰지 않는다", "핀치 줌을 막는 것은 <b>위반</b>이다"),
    ("두 가지 설정", "글자만 / 화면 전체", "따로 켜지므로 <b>둘 다</b> 봐야 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>깨지는 자리는 글자 크기가 아니라 '박아 둔 높이'입니다.</b>
          <code>font-size</code>를 <code>rem</code>으로 두어도
          상자에 <code>height: 40px</code>이 박혀 있으면 글이 잘립니다.
          버튼·칩·표 줄처럼 <b>높이를 맞춰 예쁘게 만든 곳</b>이 특히 그렇습니다.
          <code>min-height</code>로 바꾸고 <code>overflow</code>를 열어 두면
          대부분 해결되고, 그러면 <b>번역해서 글이 길어질 때</b>도 같이 버팁니다.</p>''',
  do=ul([
    "글자 크기를 <b>rem</b>으로 두기",
    "높이는 <code>min-height</code>로, <b>박지 않기</b>",
    "<b>200%로 키워 한 번</b> 열어 보기",
  ]),
  dont=ul([
    "<code>user-scalable=no</code>·<code>maximum-scale=1</code> — <b>위반</b>이다",
    "<code>font-size</code>를 px 로 박기",
    "상자 높이를 px 로 박고 <code>overflow:hidden</code>",
    "키우면 <b>기능이 사라지게</b> 두기 — 버튼이 밖으로 밀려나는 식",
  ]),
  instead='기기의 배율은 <a href="dpr.html">화면 밀도</a>, 폭에 따른 배치는 <a href="breakpoint.html">브레이크포인트</a>, 글줄 길이는 <a href="../items/container.html">컨테이너</a>.',
  cases=cases([
    (code(['html { font-size: 100% }', '.card { font-size: 0.95rem }'], "150px", "설정을 그대로 따라간다", True),
     "크기", "<b>rem</b>으로 둔다"),
    (code(['.btn { min-height: 44px }', '/* height 가 아니다 */'], "150px", "글이 커지면 같이 늘어난다", True),
     "높이", "<code>min-height</code>로"),
    (one(mono('width=device-width, initial-scale=1', 'var(--accent)'), "메타 태그", True, "확대를 막는 말을 넣지 않는다"),
     "뷰포트", "<a href=\"viewport.html\">뷰포트 단위</a>와 같은 줄"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 크기의 계약서",
  code_lede="<code>rem</code>으로 두고 높이를 열어 둡니다.",
  code='''&lt;<span class="t">meta</span> <span class="a">name</span>=<span class="s">"viewport"</span>
      <span class="a">content</span>=<span class="s">"width=device-width, initial-scale=1"</span>&gt;
<span class="c">&lt;!-- user-scalable=no · maximum-scale=1 을 넣지 않는다 --&gt;</span>

<span class="t">html</span> { <span class="a">font-size</span>: <span class="a">100%</span>; }        <span class="c">/* 브라우저·OS 설정을 그대로 받는다 */</span>
<span class="t">body</span> { <span class="a">font-size</span>: <span class="a">1rem</span>; }

.btn  { <span class="a">min-height</span>: <span class="a">44px</span>; }   <span class="c">/* height 가 아니다 */</span>
.card { <span class="a">min-height</span>: <span class="a">0</span>; <span class="a">overflow</span>: visible; }

<span class="c">/* 큰 글자에서 한 줄에 다 안 들어가면 접히게 */</span>
.row { <span class="a">display</span>: flex; <span class="a">flex-wrap</span>: wrap; <span class="a">gap</span>: <span class="a">var</span>(--s2); }''',
  keys=kbd([
    ("<code>rem</code>으로", "뿌리 크기의 배수라 <b>설정을 그대로</b> 따라간다"),
    ("<code>html</code>에 px 을 박지 않는다", "<code>font-size: 16px</code>을 뿌리에 적으면 <b>설정이 무시</b>된다"),
    ("<code>min-height</code>", "<a href=\"touchtarget.html\">터치 타깃</a>을 지키면서 글이 커지면 같이 늘어난다"),
    ("<code>flex-wrap: wrap</code>", "큰 글자에서 한 줄에 안 들어가면 <b>접히게</b> 둔다"),
    ("<code>user-scalable=no</code>", "쓰지 않는다. <b>WCAG 1.4.4 위반</b>이다"),
    ("확인하는 법", "브라우저를 <b>200%</b>로, 폰은 <b>글자 크기 최대</b>로 두고 열어 본다"),
  ]),
  backend=rows([
    ("서버는 설정을 모른다", "글자 크기 설정은 <b>요청에 안 담겨 옵니다.</b> 화면에서 CSS 로만 다룹니다."),
    ("글이 길어지는 것과 같은 문제", "번역해서 길어질 때 깨지는 자리와 <b>거의 같습니다</b>. 한 번 고치면 둘 다 해결됩니다."),
  ]),
  plat_lede="세 곳 모두 <b>사용자가 켜는 설정</b>입니다.",
  plats=plats([
    ("웹", "rem · 브라우저 확대",
     card("12px", w="110px"),
     "브라우저 확대와 글자 크기 설정이 <b>따로</b> 있습니다. 둘 다 봐야 합니다."),
    ("iOS", "Dynamic Type",
     '''              <div class="phone" role="img" aria-label="iOS 글자 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;font-size:8px;font-weight:700">모란상회</div></div></div>''',
     "시스템 글자 스타일을 쓰면 <b>자동으로</b> 따라갑니다. 접근성 설정에서 아주 크게도 됩니다."),
    ("안드로이드", "sp 단위",
     '''              <div class="phone" role="img" aria-label="안드로이드 글자 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;font-size:8px;font-weight:700">모란상회</div></div></div>''',
     "글자는 <b>sp</b>, 나머지는 <b>dp</b>. sp 로 적어야 설정을 따라갑니다."),
  ]),
  plat_note="이 항목은 <b>우리 화면에서는 영영 안 보이는</b> 종류입니다 — 설정을 안 켰으니까요. 그래서 점검법이 하나뿐입니다. <b>브라우저를 200%로 두고, 폰은 글자 크기를 최대로 두고 한 번 열어 보는 것</b>. 그 한 번에 박아 둔 높이가 거의 다 드러납니다.",
  siblings=siblings("textzoom"),
  related='''        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="../items/truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
