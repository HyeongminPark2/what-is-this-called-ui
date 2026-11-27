# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn, blocks
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">핫스팟은 눌리는 자리로, 여기만 이어 둠</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">나머지는 그림이라 눌러도 아무 일이 없음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이어 두는 화면은 세 장이나 다섯 장 정도</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">데이터가 고정되어 치거나 고를 수 없음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇을 시험하려는 흐름인지 먼저 정함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">진짜 같을수록 “다 된 거죠?”라는 말이 나옴</div>
                </div>
              </div>'''

D = dict(
  slug="prototype", ko="프로토타입", en="Prototype",
  desc="프로토타입이 시안의 화면끼리 이어 두어 눌러 볼 수 있게 만든 그림이고, 아직 코드가 아니라는 것을 보여 주는 항목입니다.",
  lede="프로토타입은 <b>눌러 볼 수 있게 만든 시안</b>입니다. 화면 몇 장을 서로 이어 둔 그림일 뿐 실제로 <b>만들어진 제품이 아닙니다</b>.",
  axes_lede="현장 용어는 부품이 아니라 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>이어 둔 자리 보이기</b>를 끄고 아무 데나 눌러 보세요. 대부분은 눌러도 아무 일도 일어나지 않습니다.<br>
          <b>진짜 데이터처럼 보이기</b>를 켜면 화면이 더 그럴듯해지는데, 그럴수록 보는 사람에게서
          <b>“거의 다 된 거죠?”</b>라는 말이 돌아옵니다. 하지만 눌린다고 해서 만들어진 것은 아닙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "프로토타입, 시제품, 눌리는 시안, 인터랙션 시안"),
    ("영어", "prototype, clickable prototype, interactive mockup"),
    ("같이 쓰는 말",
     "눌리는 자리를 <b>핫스팟</b>(hotspot), 화면끼리 이어 둔 선을 <b>연결</b>(connection) 또는 <b>플로우</b>라고 합니다. "
     "그림이 실제 화면에 얼마나 가까운지는 <b>충실도</b>라고 하며, "
     "종이에 그려 손으로 넘겨 보는 것도 <b>페이퍼 프로토타입</b>이라고 부릅니다. "
     "사람을 앉혀 놓고 프로토타입을 직접 써 보게 하는 것을 <b>사용자 시험</b>(usability test)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>MVP</b> — 기능을 최소한으로 줄였지만 <b>실제로 돌아가는</b> 제품입니다. 프로토타입은 돌아가지 않으므로 MVP가 아닙니다.<br>"
     "<b>데모</b> — 보여 주려고 만드는 것이고, 프로토타입은 사용자에게 <b>물어보려고</b> 만드는 것입니다.<br>"
     "<b>프로토타입(개발)</b> — 개발 쪽에서는 <b>시험해 보고 버릴 생각으로 짠 코드</b>를 뜻하기도 합니다. 같은 말이 디자인 쪽과 다른 것을 가리킵니다."),
  ]),
  axes=ax("프로토타입"),
  oneline="프로토타입으로 <b>무엇을 물어보려는지</b>를 먼저 정하세요. 물을 것이 정해지면 이어 둘 화면도 몇 장으로 줄어듭니다.",
  s4_title="프로토타입으로 할 수 있는 것과 없는 것", s4_hint="그림과 실제 제품의 차이",
  states=states([
    (card('<span style="font-size:9px">목록 → 상세 → 내보내기</span>'
          '<span style="font-size:8.5px;color:var(--accent)">세 장을 이어 둠</span>', "152px", "흐름을 시험할 수 있음", True),
     "화면 흐름 시험하기", "화면을 넘겨 가다 <b>막히는 곳</b>을 찾을 수 있습니다"),
    (card('<span style="font-size:9px">버튼을 누르면 다음 화면</span>'
          '<span style="font-size:8.5px;color:var(--accent)">연결해 둔 자리만</span>', "152px", "이어 둔 자리만 눌림", True),
     "누르는 자리 알아보기", "사용자가 <b>어디를 누르는지</b> 알 수 있습니다"),
    (card('<span style="font-size:9px">검색칸에 글자 치기</span>'
          '<span style="font-size:8.5px;color:var(--danger)">그림이라 칠 수 없음</span>', "152px", "입력은 대부분 안 됨", False),
     "글자 입력은 할 수 없음", "<b>데이터가 고정</b>되어 있어서 글자를 치거나 값을 고를 수 없습니다"),
    (card('<span style="font-size:9px">목록이 128건일 때</span>'
          '<span style="font-size:8.5px;color:var(--danger)">세 줄만 그려 둠</span>', "152px", "진짜 데이터가 아님", False),
     "데이터 양은 볼 수 없음", "그려 둔 몇 줄만 있으니 데이터가 <b>많아지면 어떻게 되는지</b> 알 수 없습니다"),
    (card('<span style="font-size:9px">응답이 2초 걸릴 때</span>'
          '<span style="font-size:8.5px;color:var(--danger)">바로 넘어감</span>', "152px", "기다리는 시간이 없음", False),
     "속도는 알 수 없음", "누르면 바로 넘어가므로 <b>로딩이나 실패</b> 화면이 보이지 않습니다"),
    (card('<span style="font-size:9px;font-weight:700">“거의 다 된 거죠?”</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">가장 자주 돌아오는 말</span>', "152px", "진짜 같을수록 오해가 커짐", False),
     "완성품으로 오해받기 쉬움", "다 만든 것으로 오해하지 않도록 <b>그림이라는 표시를 붙여</b> 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("핫스팟", "눌리는 자리", "이어 둔 곳만 눌렀을 때 다음 화면으로 넘어갑니다"),
    ("나머지", "그림", "핫스팟 밖은 그림이라 눌러도 <b>아무 일이 일어나지 않습니다</b>"),
    ("이어 둔 화면", "세 장 · 다섯 장", "물어볼 흐름에 필요한 화면만 잇고, 전부 이을 필요는 없습니다"),
    ("데이터", "고정", "값이 고정되어 있어서 글자를 치거나 항목을 고를 수 없습니다"),
    ("목적", "무엇을 물을지", "<b>무엇을 물을지 정해야</b> 화면을 몇 장 만들지가 정해집니다"),
    ("오해", "완성품으로 오해", "그림이라는 <b>표시</b>를 화면에 붙여 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>프로토타입은 무언가를 물어보려고 만드는 그림입니다.</b>
          '이 흐름에서 사람들이 어디서 멈추나' 같은 질문을 확인하려고 만들기 때문에,
          질문이 정해지면 <b>이어 둘 화면은 보통 서너 장</b>으로 끝납니다.
          반대로 '전부 눌리게' 만들려고 하면 만드는 데만 몇 주가 걸리고,
          그렇게 공들인 뒤에는 <b>고치기가 아까워서</b> 시험 결과를 반영하지 못하게 됩니다.
          그래서 시험이 끝나면 <b>버려도 아깝지 않을 만큼만 만드는 것</b>이 요령입니다.</p>''',
  dont_title="프로토타입을 만들거나 보여 줄 때 피할 것",
  do=ul([
    "사용자가 어디서 막히는지 <b>흐름</b>을 시험할 때",
    "사람을 앉혀 놓고 <b>써 보게</b> 할 때",
    "말로 설명이 안 되는 <b>움직임</b>을 보여 줄 때",
  ]),
  dont=ul([
    "<b>전부 눌리게</b> 만들 때. 만드는 데만 몇 주가 걸립니다",
    "입력이나 검색이 되는 것처럼 보이게 둘 때",
    "완성물처럼 보고할 때. 그림이라는 <b>표시</b>를 붙여 둡니다",
    "프로토타입을 보고 <b>성능</b>을 이야기할 때",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='그림의 단계 구분은 <a href="wireframe.html">와이어프레임과 목업과 시안</a>에서, 시안을 개발 쪽에 넘기는 일은 <a href="handoff.html">핸드오프</a>에서 다룹니다. 실제 화면의 움직임은 <a href="easing.html">이징</a>과 <a href="duration.html">지속 시간</a> 항목을 보세요.',
  cases=cases([
    (card('<span style="font-size:9px">가입 → 인증 → 첫 화면</span>'
          '<span style="font-size:8.5px;color:var(--accent)">어디서 멈추는지</span>', "150px"),
     "가입 흐름에서 막히는 곳 찾기", "<a href=\"onboarding.html\">온보딩</a> 흐름을 시험할 때 가장 쓸모가 큽니다"),
    (card('<span style="font-size:9px">시트가 올라오는 모습</span>'
          '<span style="font-size:8.5px;color:var(--accent)">말로는 설명하기 어려움</span>', "150px"),
     "움직임 보여 주기", "<a href=\"enterexit.html\">진입과 퇴장</a> 움직임을 디자이너와 개발자가 합의할 때 씁니다"),
    (card('<span style="font-size:9px;color:var(--danger)">전 화면 전부 연결</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">만드는 데만 몇 주 걸림</span>', "150px"),
     "모든 화면을 이어 버린 경우", "<b>버려도 아깝지 않을 만큼</b>만 만듭니다"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="되는 것과 안 되는 것 적기",
  code_lede="프로토타입을 넘길 때는 그 안에서 <b>무엇이 되고 무엇이 안 되는지</b>를 함께 적어 보냅니다.",
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
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("꼬리표는 <b>화면 안에</b> 붙이기", "말로만 전하면 그 말을 듣지 못한 다음 사람은 모릅니다"),
    ("안 되는 것을 <b>목록으로</b> 적기", "'대충 눌러 보세요'라고 넘기는 것보다 오해가 훨씬 적습니다"),
    ("키보드로는 거의 쓸 수 없음", "핫스팟은 <b>마우스로 누르는 자리</b>라서 Tab으로 옮겨 다닐 수 없으므로 접근성 시험에는 쓸 수 없습니다"),
    ("스크린 리더로도 읽을 수 없음", "그림이라서 스크린 리더가 <b>읽을 것이 없습니다</b>. 접근성은 코드 단계에서 확인합니다"),
    ("진짜 글 넣기", "Lorem ipsum 같은 가짜 글로는 글이 길어질 때 생기는 <b>길이 문제</b>가 드러나지 않습니다"),
    ("시험 기록 남기기", "시험한 날짜와 그때 <b>무엇을 물었는지</b>를 함께 남깁니다"),
  ]),
  backend=rows([
    ("프로토타입으로는 알 수 없는 성능", "프로토타입에서 누르자마자 다음 화면이 뜨는 것은 미리 그려 둔 <b>그림을 바꿔 보여 주기 때문</b>입니다. 실제 서비스에서는 그 사이에 서버와 요청이 오가므로 기다리는 시간이 생깁니다."),
    ("빠진 화면 찾아내기", "화면을 흐름대로 이어 보면 <b>로딩, 빈 화면, 실패</b> 화면이 빠져 있다는 것이 드러납니다. 빈 화면에 넣을 글은 <a href=\"emptytext.html\">빈 상태 문구</a> 항목을 참고하세요."),
    ("필요한 데이터 미리 정리하기", "화면마다 어떤 값이 필요한지가 흐름을 따라가며 드러나기 때문에, 프로토타입 단계에서 <b>API 설계</b>를 미리 시작할 수 있습니다."),
  ]),
  plat_lede="플랫폼마다 만드는 도구는 달라도, 프로토타입이 화면을 <b>이어 둔 그림</b>이라는 점은 같습니다.",
  plats=plats([
    ("웹", "HTML로 만들기도 함",
     card('<span style="font-size:8.5px">세 화면을 링크로 이음</span>', "110px"),
     "HTML 코드로 만들면 <b>실제 입력과 반응형 배치</b>까지 확인할 수 있지만, 들인 품이 큰 만큼 버리기도 아까워집니다."),
    ("iOS", "웹과 같은 방식",
     '''              <div class="phone" role="img" aria-label="iOS 프로토타입 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:10px;border:1px dashed var(--accent);border-radius:3px"></div></div></div>''',
     "실제 기기에 올려 보면 버튼의 <b>터치 크기</b>가 충분한지 드러납니다(<a href=\"touchtarget.html\">터치 타깃</a> 참고)."),
    ("안드로이드", "웹과 같은 방식",
     '''              <div class="phone" role="img" aria-label="안드로이드 프로토타입 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:10px;border:1px dashed var(--accent);border-radius:3px"></div></div></div>''',
     "기기마다 화면 폭이 달라서 <b>한 가지 폭으로만</b> 만든 프로토타입은 다른 기기에서 금방 어긋납니다."),
  ]),
  plat_note="프로토타입을 <b>경영진에게 보여 줄 때</b> 오해가 가장 크게 생깁니다. 화면이 눌리기 때문에 '거의 다 됐다'로 받아들여지고, 그 인상 때문에 개발 일정을 짧게 잡으라는 요구가 돌아옵니다. 보여 주기 전에 <b>'이건 그림이고, 여기부터가 만드는 일입니다'</b>라는 내용을 한 장으로 정리해 두면 이런 오해가 크게 줄어듭니다.",
  siblings=siblings("prototype"),
  related='''        <li><a href="wireframe.html"><b>와이어프레임과 목업과 시안</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="enterexit.html"><b>진입과 퇴장</b><em>9부</em></a></li>''',
)
