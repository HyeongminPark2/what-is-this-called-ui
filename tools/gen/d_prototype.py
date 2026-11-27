# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn, blocks
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">핫스팟 — 눌리는 자리. 이것만 이어 둔다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">나머지는 그림 — 눌러도 아무 일이 없다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이어 둔 화면 수 — 세 장 · 다섯 장</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">데이터는 고정 — 치거나 고를 수 없다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇을 시험하려는 흐름인가</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">진짜 같을수록 “다 된 거죠?”가 돌아온다</div>
                </div>
              </div>'''

D = dict(
  slug="prototype", ko="프로토타입", en="Prototype",
  desc="눌리는 시안. 화면끼리 이어 둔 것이고, 아직 코드가 아니다.",
  lede="<b>눌리는 시안</b>입니다. 화면 몇 장을 이어 둔 것이지 <b>만들어진 것이 아닙니다</b>.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>이어 둔 자리 보이기</b>를 끄고 아무 데나 눌러 보세요 — 대부분 아무 일도 안 일어납니다.<br>
          <b>진짜 데이터처럼 보이기</b>를 켜면 더 그럴듯해지는데, 그럴수록
          <b>“거의 다 된 거죠?”</b>라는 말이 돌아옵니다. 눌린다고 만들어진 것이 아닙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "프로토타입, 시제품, 눌리는 시안, 인터랙션 시안"),
    ("영어", "prototype, clickable prototype, interactive mockup"),
    ("같이 쓰는 말",
     "눌리는 자리를 <b>핫스팟</b>(hotspot), 화면끼리 이어 둔 선을 <b>연결</b>(connection)·<b>플로우</b>라 합니다. "
     "얼마나 진짜 같은지를 <b>충실도</b>라 하고, "
     "종이에 그려 손으로 넘기는 것도 <b>페이퍼 프로토타입</b>이라 부릅니다. "
     "사람을 앉혀 놓고 써 보게 하는 것이 <b>사용자 시험</b>(usability test)입니다."),
    ("자주 잘못 부름",
     "<b>MVP</b> — <b>진짜 돌아가는</b> 최소 제품입니다. 프로토타입은 돌아가지 않습니다.<br>"
     "<b>데모</b> — 보여 주려고 만든 것이고, 프로토타입은 <b>물어보려고</b> 만든 것입니다.<br>"
     "<b>프로토타입(개발)</b> — 개발 쪽에서는 <b>버릴 작정으로 짠 코드</b>를 뜻하기도 합니다. 같은 말, 다른 것."),
  ]),
  axes=ax("프로토타입"),
  oneline="<b>무엇을 물어보려는 것인지</b>를 먼저 정하세요. 그게 정해지면 이어 둘 화면도 몇 장으로 끝납니다.",
  s4_title="무엇이 되고 무엇이 안 되나", s4_hint="그림과 만들어진 것 사이",
  states=states([
    (card('<span style="font-size:9px">목록 → 상세 → 내보내기</span>'
          '<span style="font-size:8.5px;color:var(--accent)">세 장을 이어 뒀다</span>', "152px", "흐름을 시험할 수 있다", True),
     "되는 것 — 흐름", "<b>막히는 데</b>를 찾을 수 있다"),
    (card('<span style="font-size:9px">버튼을 누르면 다음 화면</span>'
          '<span style="font-size:8.5px;color:var(--accent)">연결해 둔 자리만</span>', "152px", "이어 둔 자리만 눌린다", True),
     "되는 것 — 자리", "<b>어디를 누를지</b> 알 수 있다"),
    (card('<span style="font-size:9px">검색칸에 글자 치기</span>'
          '<span style="font-size:8.5px;color:var(--danger)">칠 수 없다 — 그림이다</span>', "152px", "입력은 대부분 안 된다", False),
     "안 되는 것 — 입력", "<b>데이터가 고정</b>돼 있다"),
    (card('<span style="font-size:9px">목록이 128건일 때</span>'
          '<span style="font-size:8.5px;color:var(--danger)">세 줄만 그려 뒀다</span>', "152px", "진짜 데이터가 아니다", False),
     "안 되는 것 — 양", "<b>많아지면 어떻게 되는지</b> 모른다"),
    (card('<span style="font-size:9px">응답이 2초 걸릴 때</span>'
          '<span style="font-size:8.5px;color:var(--danger)">바로 넘어간다</span>', "152px", "기다림이 없다", False),
     "안 되는 것 — 속도", "<b>로딩·실패</b>가 안 보인다"),
    (card('<span style="font-size:9px;font-weight:700">“거의 다 된 거죠?”</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">가장 자주 돌아오는 말</span>', "152px", "진짜 같을수록 심해진다", False),
     "오해", "<b>꼬리표를 붙여</b> 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("핫스팟", "눌리는 자리", "이어 둔 곳만 움직인다"),
    ("나머지", "그림", "눌러도 <b>아무 일이 없다</b>"),
    ("이어 둔 화면", "세 장 · 다섯 장", "전부 이을 필요가 없다"),
    ("데이터", "고정", "치거나 고를 수 없다"),
    ("목적", "무엇을 묻나", "<b>이게 정해져야</b> 몇 장 만들지가 정해진다"),
    ("오해", "다 된 줄 안다", "<b>꼬리표</b>를 붙여 둔다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>프로토타입은 답이 아니라 질문입니다.</b>
          '이 흐름에서 사람들이 어디서 멈추나'를 물어보려고 만드는 것이라,
          물음이 정해지면 <b>이어 둘 화면은 보통 서넛</b>으로 끝납니다.
          반대로 '전부 눌리게' 만들려고 하면 만드는 데만 몇 주가 걸리고,
          그러고 나면 <b>고치기 아까워서</b> 시험 결과를 반영하지 못합니다.
          <b>버릴 수 있을 만큼만 만드는 것</b>이 요점입니다.</p>''',
  do=ul([
    "<b>흐름</b>을 시험할 때 — 어디서 막히나",
    "사람을 앉혀 놓고 <b>써 보게</b> 할 때",
    "말로 설명이 안 되는 <b>움직임</b>을 보여 줄 때",
  ]),
  dont=ul([
    "<b>전부 눌리게</b> 만들기 — 만드는 데 몇 주가 든다",
    "입력·검색이 되는 것처럼 보이게 두기",
    "완성물로 보고하기 — <b>꼬리표</b>를 붙인다",
    "프로토타입으로 <b>성능</b>을 말하기",
  ]),
  instead='그림 단계는 <a href="wireframe.html">와이어프레임과 목업과 시안</a>, 넘기는 일은 <a href="handoff.html">핸드오프</a>, 진짜 움직임은 <a href="easing.html">이징</a>·<a href="duration.html">지속 시간</a>.',
  cases=cases([
    (card('<span style="font-size:9px">가입 → 인증 → 첫 화면</span>'
          '<span style="font-size:8.5px;color:var(--accent)">어디서 멈추나</span>', "150px"),
     "흐름 시험", "<a href=\"onboarding.html\">온보딩</a>에서 가장 값이 크다"),
    (card('<span style="font-size:9px">시트가 올라오는 모습</span>'
          '<span style="font-size:8.5px;color:var(--accent)">말로는 설명이 안 된다</span>', "150px"),
     "움직임 보여 주기", "<a href=\"enterexit.html\">진입과 퇴장</a>을 합의할 때"),
    (card('<span style="font-size:9px;color:var(--danger)">전 화면 전부 연결</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">만드는 데 몇 주</span>', "150px"),
     "과한 경우", "<b>버릴 수 있을 만큼</b>만"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="이 그림의 계약서",
  code_lede="프로토타입을 넘길 때 <b>무엇이 되고 무엇이 안 되는지</b>를 적습니다.",
  code='''<span class="c"># 프로토타입을 넘길 때 함께 적는 것</span>

묻는 것 : 가입에서 첫 화면까지, 어디서 멈추는가
이어 둔 것: 가입 → 인증 → 첫 화면 (<span class="s">세 화면</span>)
안 되는 것:
  - 입력칸에 글자를 칠 수 없습니다 (값이 고정)
  - 목록은 세 줄만 있습니다 (실제는 128건)
  - 로딩 · 실패 화면은 없습니다
  - <span class="s">아직 코드가 아닙니다</span>

<span class="c"># 화면 안에도 한 줄 적어 두면 오해가 준다</span>
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"proto-stamp"</span>&gt;이 화면은 그림입니다&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("꼬리표를 <b>화면 안에</b>", "말로만 하면 다음 사람에게 안 전해진다"),
    ("안 되는 것을 <b>목록으로</b>", "'대충 눌러 보세요'보다 훨씬 오해가 적다"),
    ("키보드는 거의 안 된다", "핫스팟은 <b>마우스 자리</b>라 Tab 으로 못 다닌다 — 접근성 시험에는 못 쓴다"),
    ("스크린 리더로도 못 본다", "그림이라 <b>읽을 것이 없다</b>. 접근성은 코드 단계에서 본다"),
    ("진짜 글을 넣는다", "Lorem ipsum 으로는 <b>길이 문제</b>가 안 드러난다"),
    ("버전", "시험한 날짜와 <b>무엇을 물었는지</b>를 함께 남긴다"),
  ]),
  backend=rows([
    ("프로토타입은 성능을 안 보여 준다", "눌러서 바로 넘어가는 것은 <b>그림이라서</b>입니다. 실제로는 요청이 오갑니다."),
    ("없는 화면이 드러난다", "흐름을 이어 보면 <b>로딩·빈 화면·실패</b>가 빠져 있다는 게 보입니다 — <a href=\"emptytext.html\">빈 상태 문구</a>."),
    ("데이터 모양을 미리 본다", "어떤 값이 화면에 필요한지가 흐름에서 드러나, <b>API 설계</b>를 앞당길 수 있습니다."),
  ]),
  plat_lede="도구는 달라도 <b>이어 둔 그림</b>이라는 점은 같습니다.",
  plats=plats([
    ("웹", "HTML 로도 만든다",
     card('<span style="font-size:8.5px">세 화면을 링크로</span>', "110px"),
     "코드로 만들면 <b>진짜 입력·반응형</b>까지 볼 수 있지만, 그만큼 버리기 아까워집니다."),
    ("iOS", "같은 방식",
     '''              <div class="phone" role="img" aria-label="iOS 프로토타입 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:10px;border:1px dashed var(--accent);border-radius:3px"></div></div></div>''',
     "실제 기기에 올려 보면 <b>터치 크기</b>가 드러납니다 — <a href=\"touchtarget.html\">터치 타깃</a>."),
    ("안드로이드", "같은 방식",
     '''              <div class="phone" role="img" aria-label="안드로이드 프로토타입 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:10px;border:1px dashed var(--accent);border-radius:3px"></div></div></div>''',
     "기기 폭이 다양해 <b>한 폭으로만</b> 만든 프로토타입은 금방 어긋납니다."),
  ]),
  plat_note="프로토타입을 <b>경영진에게 보여 줄 때</b>가 가장 위험합니다. 눌리기 때문에 '거의 다 됐다'로 읽히고, 그 인상이 일정으로 돌아옵니다. 보여 주기 전에 <b>'이건 그림이고, 여기부터가 만드는 일입니다'</b>를 한 장으로 적어 두면 그 오해가 크게 줄어듭니다.",
  siblings=siblings("prototype"),
  related='''        <li><a href="wireframe.html"><b>와이어프레임과 목업과 시안</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="enterexit.html"><b>진입과 퇴장</b><em>9부</em></a></li>''',
)
