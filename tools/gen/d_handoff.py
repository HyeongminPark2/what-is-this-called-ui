# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def chk(items, w="152px", note=""):
    body = ''.join('<div style="display:flex;gap:5px;align-items:flex-start;font-size:9px">'
                   '<span style="color:' + ('var(--accent)' if ok else 'var(--danger)') + ';font-weight:700">' + ('✓' if ok else '✕') + '</span>'
                   '<span style="flex:1">' + t + '</span></div>' for t, ok in items)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">'
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">그림에서 잴 수 있는 것 — 간격 · 색 · 크기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">토큰 이름 — accent 인가 brand 인가</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">상태 — 호버 · 누름 · 비활성 · 로딩</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글이 길어지면 · 폰에서는 · 비어 있으면</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">문구 — 버튼 글자와 오류 문장</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">그림만 받으면 여덟 가지를 물어보게 된다</div>
                </div>
              </div>'''

D = dict(
  slug="handoff", ko="핸드오프", en="Handoff",
  desc="시안을 개발로 넘기는 일. 그림에서 잴 수 있는 것과 물어봐야 아는 것을 가른다.",
  lede="그림을 넘기는 일이 아니라 <b>만들 수 있을 만큼의 정보</b>를 넘기는 일입니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>체크를 끄면 <b>그림만</b> 받은 상태입니다. ✕ 가 붙은 것들이 개발 중에
          <b>하나씩 물어보게 되는</b> 것들이고, 그 왕복이 일정의 상당 부분을 먹습니다.<br>
          그림에서 <b>재서 알 수 있는 것</b>은 둘뿐이고, 나머지 여덟은 <b>말로 넘겨야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "핸드오프, 전달, 개발 전달, 스펙"),
    ("영어", "handoff, design handoff, spec, redline"),
    ("같이 쓰는 말",
     "치수를 적어 넣은 그림을 <b>레드라인</b>(redline)·<b>스펙</b>이라 하고, "
     "시안 도구가 자동으로 보여 주는 값이 <b>인스펙트</b>(inspect) 화면입니다. "
     "그림과 코드 부품을 짝지어 두는 것을 <b>코드 커넥트</b>라 부르기도 합니다. "
     "넘기고 끝나는 게 아니라 계속 오간다는 뜻으로 <b>지속적 핸드오프</b>라는 말도 씁니다."),
    ("자주 잘못 부름",
     "<b>스펙</b> — 기능 명세서를 뜻하기도 합니다. 여기서는 <b>화면의 치수와 규칙</b>입니다.<br>"
     "<b>QA</b> — 만든 뒤 확인하는 일입니다. 핸드오프는 <b>만들기 전</b>입니다.<br>"
     "<b>리뷰</b> — 의견을 주고받는 일이고, 핸드오프는 <b>넘기는</b> 일입니다."),
  ]),
  axes=ax("핸드오프"),
  oneline="<b>그림에서 잴 수 있는 것은 둘뿐입니다.</b> 나머지 여덟은 적어 주지 않으면 물어보게 됩니다.",
  s4_title="무엇이 넘어오나", s4_hint="재는 것과 묻는 것",
  states=states([
    (chk([('간격과 크기', True), ('색과 글꼴', True)], "152px", "그림에서 잴 수 있다"),
     "그림에 있는 것", "도구가 <b>자동으로</b> 보여 준다"),
    (chk([('토큰 이름', False), ('accent 인가 brand 인가', False)], "152px", "값은 보이지만 이름은 안 보인다"),
     "토큰 이름", "<b>#2f6df6 이 무엇인지</b> 모른다"),
    (chk([('호버 · 누름', False), ('비활성 · 로딩', False)], "152px", "시안에는 기본 상태 하나뿐"),
     "상태", "<b>가장 자주 빠진다</b>"),
    (chk([('글이 길어지면', False), ('폰에서는 몇 단', False)], "152px", "시안은 한 폭, 짧은 글"),
     "경계", "말줄임인가 두 줄인가"),
    (chk([('빈 화면', False), ('로딩 · 오류', False)], "152px", "시안에는 데이터가 가득하다"),
     "없는 화면", "<a href=\"emptytext.html\">빈 상태</a>·<a href=\"errortext.html\">오류</a>가 통째로 빠진다"),
    (chk([('간격과 크기', True), ('토큰 이름', True), ('상태', True), ('빈 화면 · 오류', True), ('문구 · 에셋', True)],
         "152px", "스펙까지 함께 받은 상태"),
     "스펙이 있으면", "<b>물어볼 것이 없다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잴 수 있는 것", "간격 · 색 · 크기", "도구가 자동으로 보여 준다"),
    ("토큰 이름", "값이 아니라 이름", "<b>#2f6df6 이 무엇인지</b>를 적는다"),
    ("상태", "호버 · 누름 · 비활성", "시안에는 <b>기본 하나</b>뿐이다"),
    ("경계", "길어지면 · 좁아지면", "말줄임인가 두 줄인가"),
    ("없는 화면", "빈 · 로딩 · 오류", "데이터가 가득한 시안에는 <b>안 보인다</b>"),
    ("문구 · 에셋", "글자와 파일", "버튼 글자, 아이콘 파일 꼴"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>스펙은 긴 문서가 아니어도 됩니다.</b>
          시안 옆에 적은 메모 열 줄이면 대개 충분합니다 —
          '이 파랑은 <code>--accent</code>', '글이 길면 두 줄까지',
          '560px 아래에서 한 단', '목록이 비면 가맹점 등록 버튼'.
          중요한 것은 분량이 아니라 <b>그림에서 알 수 없는 것만 골라 적는</b> 것입니다.
          그리고 이 목록은 거의 매번 같기 때문에,
          <b>한 번 만들어 둔 점검표</b>를 돌려 쓰면 됩니다.</p>''',
  do=ul([
    "<b>그림에서 알 수 없는 것</b>만 골라 적기",
    "같은 점검표를 <b>매번</b> 돌려 쓰기",
    "토큰 <b>이름</b>으로 적기 — 값이 아니라",
  ]),
  dont=ul([
    "그림만 넘기고 '보면 알죠' — <b>여덟 번 물어보게</b> 된다",
    "값을 박아 적기 — <code>#2f6df6</code> 대신 <b>이름</b>을",
    "상태·빈 화면을 안 그리기 — <b>개발 중에 즉흥</b>으로 정해진다",
    "넘기고 끝내기 — <b>계속 오간다</b>",
  ]),
  instead='그림 단계는 <a href="wireframe.html">와이어프레임과 목업과 시안</a>, 부품 규칙은 <a href="designsystem.html">디자인 시스템</a>, 파일은 <a href="assets.html">에셋 내보내기</a>.',
  cases=cases([
    (code(['배경: --accent', '간격: --space-3', '모서리: --radius-1'], "150px", "값이 아니라 이름으로", True),
     "토큰으로 적기", "<b>다크 모드</b>까지 한 번에 해결된다"),
    (chk([('기본', True), ('호버', True), ('누름', True), ('비활성', True)], "150px", "네 상태를 다 그렸다"),
     "상태를 그려 주기", "<b>가장 값이 큰 한 장</b>"),
    (chk([('목록이 비면', True), ('불러오는 중', True), ('실패했을 때', True)], "150px", "세 화면을 더 그렸다"),
     "없는 화면", "<a href=\"emptytext.html\">빈 상태</a>·<a href=\"errortext.html\">오류</a>를 미리 정한다"),
  ]),
  s8_title="점검표", s8_hint="이 전달의 계약서",
  code_lede="매번 같은 열 줄을 적습니다.",
  code='''<span class="c"># 핸드오프 점검표 — 그림에서 알 수 없는 것만</span>

1. 토큰 이름  : 이 파랑은 --accent, 간격은 --space-3
2. 상태       : 기본 / 호버 / 누름 / 비활성 / 로딩
3. 글이 길면  : 두 줄까지, 넘으면 말줄임
4. 좁아지면   : 560px 아래에서 한 단, 메뉴는 접기
5. 비어 있으면: "아직 등록한 가맹점이 없어요" + [가맹점 등록]
6. 불러오는 중: 스켈레톤 세 줄
7. 실패하면   : "불러오지 못했습니다" + [다시 시도]
8. 문구       : 버튼은 "내보내기" (확인 아님)
9. 움직임     : 240ms ease-out, 모션 줄이기에서는 0
10. 에셋      : 아이콘 SVG, 사진 WebP 2x''',
  keys=kbd([
    ("상태에 <b>초점</b>도 넣는다", "호버만 그리면 <a href=\"../items/focus.html\">키보드 초점</a>이 빠진다"),
    ("<a href=\"../items/contrast.html\">대비비</a>를 적는다", "흐린 회색 글씨는 <b>시안에서 예뻐 보이고</b> 기준에 걸린다"),
    ("<a href=\"../items/name.html\">아이콘의 이름</a>", "아이콘만 있는 버튼은 <b>뭐라고 읽힐지</b>를 적어 준다"),
    ("<a href=\"touchtarget.html\">눌리는 넓이</a>", "보이는 크기와 따로다. <b>시안에서는 안 보인다</b>"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>", "움직임을 적을 때 <b>줄이기에서 어떻게 되는지</b>도 함께"),
    ("읽는 순서", "눈에 보이는 차례와 <b>Tab 순서</b>가 다르면 적어 둔다"),
  ]),
  backend=rows([
    ("데이터 모양을 함께", "화면에 필요한 값이 정해지면 <b>API 설계</b>가 앞당겨집니다."),
    ("없는 화면이 일정을 늘린다", "빈·로딩·오류는 <b>화면 수가 세 배</b>가 되는 일입니다. 핸드오프에서 드러나야 일정에 들어갑니다."),
    ("문구를 한곳에", "버튼 글자·오류 문장을 <b>표로</b> 받으면 그대로 문구 파일이 됩니다 — <a href=\"voice.html\">말투와 높임</a>."),
    ("토큰을 코드로 내보내기", "시안 도구의 변수를 <b>CSS 변수로 뽑아</b> 쓰면 옮겨 적다 틀릴 일이 없습니다."),
  ]),
  plat_lede="도구가 거드는 범위가 다릅니다 — <b>잴 수 있는 것까지</b>입니다.",
  plats=plats([
    ("웹", "인스펙트 + 메모",
     code(['padding: 12px', 'color: --accent'], "110px", "", True),
     "도구가 CSS 를 보여 줍니다. 다만 <b>이름·상태·경계</b>는 사람이 적어야 합니다."),
    ("iOS", "같은 문제",
     '''              <div class="phone" role="img" aria-label="iOS 스펙 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">spacing: 12pt<br>color: Accent</div></div></div>''',
     "pt 로 보여 줍니다. <b>다이내믹 타입</b>에서 어떻게 되는지는 따로 물어야 합니다."),
    ("안드로이드", "같은 문제",
     '''              <div class="phone" role="img" aria-label="안드로이드 스펙 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">padding: 12dp<br>color: colorPrimary</div></div></div>''',
     "dp 로 보여 줍니다. <b>기기 폭이 다양해</b> 경계 질문이 더 많습니다."),
  ]),
  plat_note="\"시안 다 나왔으니 개발만 하면 됩니다\"가 자주 틀리는 이유가 이것입니다. 시안에 있는 것은 <b>기본 상태 한 장</b>이고, 만들어야 하는 것은 <b>상태 다섯에 경계 셋</b>입니다. 핸드오프 점검표를 한 번 만들어 두면 이 차이가 일정 잡을 때 드러나고, 개발 중 왕복이 크게 줄어듭니다.",
  siblings=siblings("handoff"),
  related='''        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>
        <li><a href="emptytext.html"><b>빈 상태 문구</b><em>14부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>''',
)
