# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn, blocks
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">와이어프레임 — 회색 상자. 구조만 묻는다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">목업 — 자리와 크기까지. 아직 안 눌린다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">시안 — 색 · 글꼴 · 그림까지 입힌 완성 그림</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">프로토타입 — 눌리는 시안. 화면끼리 이어 둔 것</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">진짜 같을수록 보는 사람이 다른 것을 본다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">구조를 묻고 싶은데 색 이야기가 돌아온다</div>
                </div>
              </div>'''

D = dict(
  slug="wireframe", ko="와이어프레임과 목업과 시안", en="Wireframe / Mockup / Visual",
  desc="같은 화면의 네 단계. 얼마나 진짜 같은가(충실도)에 따라 할 수 있는 질문이 달라진다.",
  lede="같은 화면을 <b>얼마나 진짜 같이</b> 그렸느냐의 단계입니다. 단계마다 <b>할 수 있는 질문</b>이 다릅니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 단계를 눌러 가며 봐 보세요. 오른쪽에 <b>이 단계에서 할 질문</b>과
          <b>아직 하면 안 되는 질문</b>이 갈려 있습니다.<br>
          그림이 진짜에 가까울수록 보는 사람은 <b>다른 것을 보게</b> 됩니다 —
          구조를 정하고 싶은데 색 이야기가 나오면, 리뷰어 탓이 아니라 <b>그림이 그렇게 생겨서</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "와이어프레임, 목업, 시안, 프로토타입, 선화"),
    ("영어", "wireframe, mockup, visual design / comp, prototype"),
    ("같이 쓰는 말",
     "얼마나 진짜 같은지를 <b>충실도</b>(fidelity)라 하고, "
     "낮은 것이 <b>로파이</b>(lo-fi), 높은 것이 <b>하이파이</b>(hi-fi)입니다. "
     "손으로 그린 밑그림은 <b>스케치</b>, 완성 그림은 <b>컴프</b>(comp)라고도 합니다. "
     "한국에서는 완성 그림을 통틀어 <b>시안</b>이라 부르는 일이 많습니다."),
    ("자주 잘못 부름",
     "<b>목업</b> — 한국에서는 '실물 사진에 합성한 그림'을 뜻하기도 해서 <b>말이 자주 엇갈립니다</b>.<br>"
     "<b>시안</b> — '초안'이라는 뜻으로도, '완성 그림'이라는 뜻으로도 쓰입니다. <b>어느 쪽인지</b> 물어보는 편이 낫습니다.<br>"
     "<b>프로토타입</b> — 개발 쪽에서는 <b>돌아가는 코드</b>를 뜻하기도 합니다. 디자인 쪽은 <b>눌리는 그림</b>입니다."),
  ]),
  axes=ax("와이어프레임과 목업과 시안"),
  oneline="<b>받은 그림이 어느 단계인지 먼저 물어보세요.</b> 그래야 무엇을 물어도 되는지가 정해집니다.",
  s4_title="네 단계", s4_hint="무엇을 묻는 자리인가",
  states=states([
    (blocks(False, "152px", "회색 상자와 선뿐이다"), "와이어프레임", "<b>구조</b>를 묻는다 — 무엇이 있고 무엇이 중요한가"),
    (blocks(False, "152px", "자리와 크기가 정해졌다"), "목업", "<b>배치</b>를 묻는다 — 길어지면, 좁아지면"),
    (blocks(True, "152px", "색 · 글꼴 · 그림까지"), "시안", "<b>마감</b>을 묻는다 — 대비·브랜드·아이콘"),
    (card(blocks(True, "100%").strip() + '<span style="font-size:8.5px;color:var(--accent)">→ 누르면 상세로 이어 뒀다</span>', "152px", "눌리는 시안"),
     "프로토타입", "<b>흐름</b>을 묻는다 — 막히는 데가 있나"),
    (card('<span style="font-size:9px">구조를 묻고 싶은데</span>'
          '<span style="font-size:8.5px;color:var(--danger)">“이 파란색이 좀…”</span>', "152px", "시안으로 구조 회의를 하면", False),
     "단계를 섞으면", "<b>엉뚱한 리뷰</b>가 돌아온다"),
    (card('<span style="font-size:9px;font-weight:700">“거의 다 된 거죠?”</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">프로토타입을 본 사람의 첫마디</span>', "152px", "눌린다고 만들어진 게 아니다", False),
     "프로토타입의 함정", "<b>진짜 같을수록</b> 오해가 커진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("와이어프레임", "회색 상자", "색·글꼴을 <b>일부러 안 쓴다</b>"),
    ("목업", "자리와 크기", "아직 <b>안 눌린다</b>"),
    ("시안", "완성 그림", "색·글꼴·그림까지 다 입힌 것"),
    ("프로토타입", "눌리는 시안", "화면끼리 <b>이어 둔</b> 것"),
    ("충실도", "진짜 같은 정도", "높을수록 <b>다른 질문</b>이 돌아온다"),
    ("단계 섞기", "엉뚱한 리뷰", "구조를 묻는데 색 이야기가 나온다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>충실도를 일부러 낮추는 것</b>이 요령입니다.
          구조를 정하는 회의에 색이 칠해진 그림을 가져가면,
          사람들은 색을 말합니다 — 그게 가장 눈에 띄고 말하기 쉽기 때문입니다.
          그래서 회색 상자로만 그린 그림이 <b>덜 만든 것</b>이 아니라
          <b>그 질문에 맞게 만든 것</b>입니다.
          반대로 색을 확정해야 하는 자리에 와이어프레임을 가져가면
          아무것도 못 정하고 끝납니다.</p>''',
  do=ul([
    "구조를 정할 때는 <b>와이어프레임</b>으로",
    "폭·글 길이를 볼 때는 <b>목업</b>으로",
    "흐름을 시험할 때는 <b>프로토타입</b>으로",
  ]),
  dont=ul([
    "구조 회의에 <b>시안</b> 가져가기 — 색 이야기가 나온다",
    "색을 정하는 자리에 <b>회색 상자</b> 가져가기",
    "프로토타입을 <b>다 된 것</b>으로 보고하기",
    "단계를 안 밝히고 그림만 넘기기",
  ]),
  instead='눌리는 그림은 <a href="prototype.html">프로토타입</a>, 넘기는 일은 <a href="handoff.html">핸드오프</a>, 부품 규칙은 <a href="designsystem.html">디자인 시스템</a>.',
  cases=cases([
    (blocks(False, "150px", "구조만"), "기획 회의", "<b>무엇이 있고 무엇이 중요한가</b>"),
    (blocks(True, "150px", "완성 그림"), "디자인 확정", "<b>색·글꼴·아이콘</b>을 정한다"),
    (card('<span style="font-size:9px">1 → 2 → 3</span>'
          '<span style="font-size:8.5px;color:var(--accent)">눌러서 넘어간다</span>', "150px", "흐름 시험"),
     "사용자 시험", "<b>막히는 데</b>를 찾는다"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="이 그림의 계약서",
  code_lede="그림을 넘길 때 <b>단계와 질문</b>을 함께 적습니다.",
  code='''<span class="c"># 그림을 넘길 때 함께 적는 것</span>

단계   : 와이어프레임
묻는 것: 이 화면에 들어갈 정보와 그 순서
안 묻는 것: 색 · 글꼴 · 아이콘 (아직 안 정했습니다)
다음   : 구조가 정해지면 목업으로 갑니다

<span class="c"># 프로토타입을 넘길 때는 한 줄 더</span>

이 프로토타입은 <span class="s">세 화면만</span> 이어 뒀습니다.
나머지는 눌러도 아무 일이 없습니다 — <span class="s">아직 코드가 아닙니다.</span>''',
  keys=kbd([
    ("단계를 <b>파일 이름에</b>", "<code>정산목록_와이어_v2</code>. 열어 보기 전에 알 수 있다"),
    ("질문을 함께 적는다", "'무엇을 봐 주세요'가 없으면 <b>보이는 것</b>을 말하게 된다"),
    ("회색은 회색으로", "와이어프레임에 브랜드 색을 한 군데만 써도 <b>거기로 눈이 간다</b>"),
    ("진짜 글을 넣을지", "Lorem ipsum 은 <b>길이 감</b>을 못 준다. 대신 색은 안 정해도 된다"),
    ("프로토타입에는 꼬리표", "'아직 코드가 아닙니다'를 <b>화면 안에</b> 적어 두면 오해가 줄어든다"),
    ("버전", "<code>v2</code>·<code>v3</code>보다 <b>날짜와 무엇이 바뀌었는지</b>가 쓸모 있다"),
  ]),
  backend=rows([
    ("와이어프레임에서 데이터를 본다", "어떤 필드가 필요한지는 <b>구조 단계에서</b> 드러납니다. 시안까지 기다리면 API 설계가 늦습니다."),
    ("시안에 없는 상태", "빈 화면·로딩·오류는 시안에 거의 없습니다. <b>이 단계에서 물어봐야</b> 합니다 — <a href=\"handoff.html\">핸드오프</a>."),
    ("프로토타입은 성능을 안 보여 준다", "눌러서 바로 넘어가는 것은 <b>그림이라서</b>입니다. 실제로는 요청이 오갑니다."),
  ]),
  plat_lede="도구는 달라도 <b>단계는 같습니다</b>.",
  plats=plats([
    ("웹", "HTML 로 바로",
     blocks(False, "110px"),
     "코드로 와이어프레임을 짜기도 합니다. <b>진짜 글 길이·반응형</b>을 바로 볼 수 있는 것이 장점입니다."),
    ("iOS", "같은 단계",
     '''              <div class="phone" role="img" aria-label="iOS 와이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:7px;background:var(--ink-100);border-radius:2px"></span><span style="height:7px;background:var(--ink-100);border-radius:2px;width:70%"></span></div></div></div>''',
     "OS 부품이 정해져 있어 <b>와이어프레임이 짧게</b> 끝나는 편입니다."),
    ("안드로이드", "같은 단계",
     '''              <div class="phone" role="img" aria-label="안드로이드 와이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:7px;background:var(--ink-100);border-radius:2px"></span><span style="height:7px;background:var(--ink-100);border-radius:2px;width:70%"></span></div></div></div>''',
     "역시 같습니다. 다만 <b>기기 폭이 다양</b>해 목업 단계가 길어집니다."),
  ]),
  plat_note="\"시안 나왔어요\"를 받으면 <b>어느 단계인지</b>부터 물어보는 편이 좋습니다. 완성 그림인 줄 알고 그대로 만들었는데 <b>아직 구조를 보는 중</b>이었던 경우가 흔하고, 반대로 아직 제안인 줄 알고 질문했는데 <b>이미 확정</b>인 경우도 있습니다. 파일 이름에 단계를 적어 두면 이 왕복이 사라집니다.",
  siblings=siblings("wireframe"),
  related='''        <li><a href="prototype.html"><b>프로토타입</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>''',
)
