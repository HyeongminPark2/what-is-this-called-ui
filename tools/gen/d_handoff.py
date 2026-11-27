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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">그림에서 잴 수 있는 것은 간격 · 색 · 크기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">토큰 이름이 accent인지 brand인지</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">상태는 호버 · 누름 · 비활성 · 로딩</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글이 길거나 폰이거나 비어 있을 때</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">문구는 버튼 글자와 오류 문장</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">그림만 받으면 여덟 가지를 물어보게 됨</div>
                </div>
              </div>'''

D = dict(
  slug="handoff", ko="핸드오프", en="Handoff",
  desc="시안을 개발 쪽으로 넘기는 핸드오프에서, 그림에서 재서 알 수 있는 것과 물어봐야 알 수 있는 것을 가르는 항목입니다.",
  lede="핸드오프는 시안을 개발 쪽에 넘기는 일입니다. 이때 넘겨야 하는 것은 그림 파일만이 아니라, 개발자가 화면을 <b>실제로 만들 수 있을 만큼의 정보</b>입니다.",
  axes_lede="15부에서 다루는 현장 용어는 화면 부품의 이름 대신 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지를 물어보면 이 용어들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>체크를 끄면 <b>그림만</b> 받은 상태가 됩니다. ✕가 붙은 항목은 개발하는 동안
          <b>하나씩 물어보게 되는</b> 것들이고, 이렇게 묻고 답하는 데 일정의 상당 부분이 들어갑니다.<br>
          그림에서 <b>재서 알 수 있는 것</b>은 두 가지뿐이고, 나머지 여덟 가지는 <b>글로 적어 넘겨야</b> 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "핸드오프, 전달, 개발 전달, 스펙"),
    ("영어", "handoff, design handoff, spec, redline"),
    ("같이 쓰는 말",
     "치수를 적어 넣은 그림을 <b>레드라인</b>(redline) 또는 <b>스펙</b>이라고 하고, "
     "시안 도구가 값을 자동으로 보여 주는 화면을 <b>인스펙트</b>(inspect) 화면이라고 합니다. "
     "그림 속 부품과 코드 부품을 짝지어 두는 것을 <b>코드 커넥트</b>라고 부르기도 합니다. "
     "한 번 넘기고 끝나지 않고 디자인과 개발 사이를 계속 오간다는 뜻으로 <b>지속적 핸드오프</b>라는 말도 씁니다."),
    ("자주 잘못 부르는 이름",
     "<b>스펙</b> — 기능 명세서를 뜻하기도 하지만, 핸드오프에서 말하는 스펙은 <b>화면의 치수와 규칙</b>입니다.<br>"
     "<b>QA</b> — 다 만든 뒤에 확인하는 일이고, 핸드오프는 <b>만들기 전</b>에 하는 일입니다.<br>"
     "<b>리뷰</b> — 의견을 주고받는 일이고, 핸드오프는 만들 정보를 <b>넘기는</b> 일입니다."),
  ]),
  axes=ax("핸드오프"),
  oneline="<b>그림에서 재서 알 수 있는 것은 간격·크기와 색·글꼴 두 가지뿐입니다.</b> 나머지 여덟 가지는 적어 주지 않으면 개발자가 하나씩 물어보게 됩니다.",
  s4_title="그림과 함께 넘어오는 정보", s4_hint="그림에서 재는 것과 물어야 하는 것",
  states=states([
    (chk([('간격과 크기', True), ('색과 글꼴', True)], "152px", "그림에서 잴 수 있음"),
     "그림에서 잴 수 있는 것", "시안 도구가 <b>자동으로</b> 보여 줍니다"),
    (chk([('토큰 이름', False), ('accent인지 brand인지', False)], "152px", "값은 보이지만 이름은 안 보임"),
     "값에 붙은 토큰 이름", "값은 보이지만 <b>#2f6df6이 어떤 토큰인지</b>는 알 수 없습니다"),
    (chk([('호버 · 누름', False), ('비활성 · 로딩', False)], "152px", "시안에는 기본 상태 하나뿐"),
     "호버·누름 같은 상태", "시안에는 기본 상태만 그려져 있어서 <b>가장 자주 빠집니다</b>"),
    (chk([('글이 길어지면', False), ('폰에서 몇 단인지', False)], "152px", "시안은 한 폭에 짧은 글뿐"),
     "글 길이와 화면 폭의 경계", "글이 길어지면 말줄임으로 자를지 두 줄로 보일지 정해야 합니다"),
    (chk([('빈 화면', False), ('로딩 · 오류', False)], "152px", "시안에는 데이터가 가득함"),
     "시안에 없는 화면", "<a href=\"emptytext.html\">빈 상태</a>와 <a href=\"errortext.html\">오류</a> 화면이 아예 빠져 있습니다"),
    (chk([('간격과 크기', True), ('토큰 이름', True), ('상태', True), ('빈 화면 · 오류', True), ('문구 · 에셋', True)],
         "152px", "스펙까지 함께 받은 상태"),
     "스펙까지 받았을 때", "필요한 정보가 다 있으니 <b>물어볼 것이 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잴 수 있는 것", "간격 · 색 · 크기", "시안 도구가 자동으로 보여 줍니다"),
    ("토큰 이름", "값이 아니라 이름", "<b>#2f6df6이 어떤 토큰인지</b>를 적어 줍니다"),
    ("상태", "호버 · 누름 · 비활성", "시안에는 <b>기본 상태 하나</b>만 그려져 있습니다"),
    ("경계", "길어질 때 · 좁아질 때", "글이 길어지거나 화면이 좁아질 때 어떻게 보일지 정합니다"),
    ("없는 화면", "빈 · 로딩 · 오류", "데이터가 가득 찬 시안에는 빈 화면, 로딩, 오류 화면이 <b>보이지 않습니다</b>"),
    ("문구 · 에셋", "글자와 파일", "버튼에 들어갈 글자와 아이콘 파일 형식을 정합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>스펙은 짧아도 됩니다.</b>
          예를 들어 '이 파랑은 <code>--accent</code>', '글이 길면 두 줄까지',
          '560px 아래에서 한 단', '목록이 비면 가맹점 등록 버튼'처럼
          시안 옆에 메모 열 줄 정도만 적어 두어도 대개 충분합니다.
          분량보다 중요한 것은 <b>그림에서 알 수 없는 것만 골라 적는</b> 것입니다.
          적어야 할 항목은 화면이 달라도 거의 매번 같기 때문에,
          <b>한 번 만들어 둔 점검표</b>를 화면마다 다시 쓰면 됩니다.</p>''',
  do_title="핸드오프할 때 지킬 것",
  dont_title="핸드오프할 때 피할 것",
  do=ul([
    "<b>그림에서 알 수 없는 것</b>만 골라 적습니다",
    "같은 점검표를 <b>매번</b> 다시 씁니다",
    "색과 간격은 값 대신 토큰 <b>이름</b>으로 적습니다",
  ]),
  dont=ul([
    "그림만 넘기고 '보면 알죠'라고 할 때. 개발자가 <b>여덟 번 물어보게</b> 됩니다",
    "값을 그대로 적을 때. <code>#2f6df6</code> 대신 토큰 <b>이름</b>을 적어야 합니다",
    "상태와 빈 화면을 그리지 않을 때. 그 화면들이 <b>개발하는 도중에 즉흥</b>으로 정해집니다",
    "한 번 넘기고 끝났다고 여길 때. 개발하는 동안에도 질문과 수정이 <b>계속 오갑니다</b>",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='그림의 단계 구분은 <a href="wireframe.html">와이어프레임과 목업과 시안</a>에서, 부품 규칙은 <a href="designsystem.html">디자인 시스템</a>에서, 그림 파일을 넘기는 방법은 <a href="assets.html">에셋 내보내기</a>에서 다룹니다.',
  cases=cases([
    (code(['배경: --accent', '간격: --space-3', '모서리: --radius-1'], "150px", "값 대신 이름으로 적음", True),
     "값을 토큰 이름으로 적기", "토큰 이름으로 적어 두면 <b>다크 모드</b>까지 한 번에 해결됩니다"),
    (chk([('기본', True), ('호버', True), ('누름', True), ('비활성', True)], "150px", "네 상태를 다 그림"),
     "버튼 상태 네 가지 그려 주기", "핸드오프에서 더 그려 줄 화면 가운데 <b>가장 쓸모가 큰 한 장</b>입니다"),
    (chk([('목록이 비면', True), ('불러오는 중', True), ('실패했을 때', True)], "150px", "세 화면을 더 그림"),
     "빈 화면·로딩·실패 화면 더 그리기", "<a href=\"emptytext.html\">빈 상태</a>와 <a href=\"errortext.html\">오류</a> 화면을 미리 정해 둡니다"),
  ]),
  s8_title="핸드오프 점검표", s8_hint="그림에서 알 수 없는 열 가지",
  code_lede="화면이 달라도 매번 같은 열 가지 항목을 채워 넘깁니다.",
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
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("상태에 <b>초점</b>도 넣기", "호버만 그려 두면 <a href=\"../items/focus.html\">키보드 초점</a> 상태가 빠지기 쉽습니다"),
    ("<a href=\"../items/contrast.html\">대비비</a> 적기", "흐린 회색 글씨는 <b>시안에서는 보기 좋아도</b> 대비비 기준을 통과하지 못하는 경우가 많습니다"),
    ("<a href=\"../items/name.html\">아이콘의 이름</a> 적기", "아이콘만 있는 버튼은 스크린 리더가 <b>뭐라고 읽을지</b>를 적어 줍니다"),
    ("<a href=\"touchtarget.html\">눌리는 넓이</a> 적기", "눌리는 넓이는 보이는 크기와 따로 정하는 값이라 <b>시안에는 드러나지 않습니다</b>"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>에서의 동작 적기", "움직임을 적을 때 모션 줄이기 설정에서 <b>어떻게 되는지</b>도 함께 적습니다"),
    ("읽는 순서 적기", "눈에 보이는 차례와 <b>Tab 순서</b>가 달라야 하면 적어 둡니다"),
  ]),
  backend=rows([
    ("필요한 데이터 함께 정하기", "핸드오프 때 화면에 필요한 값을 함께 정해 두면 <b>API 설계</b>를 그만큼 일찍 시작할 수 있습니다."),
    ("빠진 화면 때문에 늘어나는 일정", "화면마다 빈 화면, 로딩, 오류를 더하면 <b>만들 화면 수가 세 배</b>가 됩니다. 이 화면들이 핸드오프 때 드러나야 일정에 반영할 수 있습니다."),
    ("문구를 표 하나로 받기", "버튼 글자와 오류 문장을 <b>표로</b> 받으면 그 표를 그대로 문구 파일로 쓸 수 있습니다. 문구를 정하는 기준은 <a href=\"voice.html\">말투와 높임</a> 항목에 있습니다."),
    ("토큰을 코드로 내보내기", "시안 도구에 정의한 변수를 <b>CSS 변수로 뽑아</b> 그대로 쓰면, 값을 손으로 옮겨 적다가 틀리는 일이 없습니다."),
  ]),
  plat_lede="플랫폼마다 시안 도구가 보여 주는 단위는 다르지만, 도구가 도와주는 범위는 모두 그림에서 <b>잴 수 있는 것까지</b>입니다.",
  plats=plats([
    ("웹", "인스펙트 화면과 메모",
     code(['padding: 12px', 'color: --accent'], "110px", "", True),
     "시안 도구가 CSS 값을 보여 주지만, 토큰 <b>이름과 상태, 경계</b>는 사람이 적어야 합니다."),
    ("iOS", "웹과 같은 문제",
     '''              <div class="phone" role="img" aria-label="iOS 스펙 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">spacing: 12pt<br>color: Accent</div></div></div>''',
     "값을 pt 단위로 보여 줍니다. 사용자가 글자 크기를 키우는 <b>다이내믹 타입</b>에서 화면이 어떻게 되는지는 따로 물어야 합니다."),
    ("안드로이드", "웹과 같은 문제",
     '''              <div class="phone" role="img" aria-label="안드로이드 스펙 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">padding: 12dp<br>color: colorPrimary</div></div></div>''',
     "값을 dp 단위로 보여 줍니다. <b>기기마다 화면 폭이 다양해서</b> 경계에 관한 질문이 더 많이 생깁니다."),
  ]),
  plat_note="\"시안 다 나왔으니 개발만 하면 됩니다\"라는 말이 자주 틀리는 것도 그림에 없는 정보 때문입니다. 시안에 그려진 것은 <b>기본 상태 한 장</b>이지만, 실제로 만들어야 하는 것은 <b>상태 다섯 가지와 경계 세 가지</b>입니다. 핸드오프 점검표를 한 번 만들어 두면 일정을 잡을 때 이 차이가 드러나고, 개발하면서 묻고 답하는 일도 크게 줄어듭니다.",
  siblings=siblings("handoff"),
  related='''        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>
        <li><a href="emptytext.html"><b>빈 상태 문구</b><em>14부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>''',
)
