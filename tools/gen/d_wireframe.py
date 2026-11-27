# -*- coding: utf-8 -*-
from _t15 import code, card, btn, blocks
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">와이어프레임은 회색 상자로 구조만 물음</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">목업은 자리와 크기까지 정함, 아직 안 눌림</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">시안은 색 · 글꼴 · 그림까지 입힌 완성 그림</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">프로토타입은 화면끼리 이어 둔 눌리는 시안</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">진짜 같을수록 보는 사람이 다른 것을 봄</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">구조를 물었는데 색 이야기가 돌아옴</div>
                </div>
              </div>'''

D = dict(
  slug="wireframe", ko="와이어프레임과 목업과 시안", en="Wireframe / Mockup / Visual",
  desc="같은 화면을 실제 화면에 얼마나 가깝게 그렸는지(충실도)에 따라 네 단계로 나누고, 단계마다 물을 수 있는 질문이 어떻게 달라지는지 보여 주는 항목입니다.",
  lede="와이어프레임과 목업, 시안은 같은 화면을 <b>얼마나 실제 화면에 가깝게</b> 그렸는지에 따라 나눈 단계입니다. 그림이 어느 단계에 있느냐에 따라 그 그림을 보며 <b>물을 수 있는 질문</b>도 달라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 단계를 차례로 눌러 보세요. 오른쪽에 <b>이 단계에서 할 질문</b>과
          <b>아직 하면 안 되는 질문</b>이 나뉘어 있습니다.<br>
          그림이 실제 화면에 가까울수록 보는 사람의 눈은 <b>다른 곳으로</b> 갑니다.
          구조를 정하려는 자리에서 색 이야기가 나온다면 리뷰어 탓이 아니라 <b>그림에 색이 칠해져 있기 때문</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "와이어프레임, 목업, 시안, 프로토타입, 선화"),
    ("영어", "wireframe, mockup, visual design / comp, prototype"),
    ("같이 쓰는 말",
     "그림이 실제 화면에 얼마나 가까운지를 <b>충실도</b>(fidelity)라고 하며, "
     "충실도가 낮은 그림을 <b>로파이</b>(lo-fi), 높은 그림을 <b>하이파이</b>(hi-fi)라고 부릅니다. "
     "손으로 그린 밑그림은 <b>스케치</b>, 완성 그림은 <b>컴프</b>(comp)라고도 합니다. "
     "한국에서는 완성 그림을 통틀어 <b>시안</b>이라고 부르는 일이 많습니다."),
    ("자주 잘못 부르는 이름",
     "<b>목업</b> — 한국에서는 '실물 사진에 합성한 그림'이라는 뜻으로도 쓰여서, 같은 말을 두고 <b>서로 다른 것을 떠올리는 일</b>이 잦습니다.<br>"
     "<b>시안</b> — '초안'이라는 뜻으로도, '완성 그림'이라는 뜻으로도 쓰이기 때문에 받은 시안이 <b>어느 쪽인지</b> 물어보는 편이 낫습니다.<br>"
     "<b>프로토타입</b> — 개발 쪽에서는 <b>실제로 돌아가는 코드</b>를 뜻하기도 하지만, 디자인 쪽에서는 <b>눌러 볼 수 있는 그림</b>을 뜻합니다."),
  ]),
  s4_title="충실도의 네 단계", s4_hint="단계마다 물을 수 있는 것",
  states=states([
    (blocks(False, "152px", "회색 상자와 선만 있음"), "와이어프레임", "<b>구조</b>를 묻습니다. 화면에 무엇이 있고 무엇이 중요한지 봅니다"),
    (blocks(False, "152px", "자리와 크기를 정함"), "목업", "<b>배치</b>를 묻습니다. 글이 길어지거나 화면이 좁아지면 어떻게 되는지 봅니다"),
    (blocks(True, "152px", "색 · 글꼴 · 그림까지 입힘"), "시안", "<b>마감</b>을 묻습니다. 색 대비와 브랜드 표현, 아이콘을 봅니다"),
    (card(blocks(True, "100%").strip() + '<span style="font-size:8.5px;color:var(--accent)">→ 누르면 상세 화면으로 넘어감</span>', "152px", "눌리는 시안"),
     "프로토타입", "<b>흐름</b>을 묻습니다. 화면을 넘겨 가다 막히는 곳이 있는지 봅니다"),
    (card('<span style="font-size:9px">구조를 묻고 싶은데</span>'
          '<span style="font-size:8.5px;color:var(--danger)">“이 파란색이 좀…”</span>', "152px", "시안으로 구조 회의를 하면", False),
     "단계를 섞어 보여 주면", "묻고 싶은 것과 상관없는 <b>엉뚱한 리뷰</b>가 돌아옵니다"),
    (card('<span style="font-size:9px;font-weight:700">“거의 다 된 거죠?”</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">프로토타입을 본 사람의 첫마디</span>', "152px", "눌려도 아직 만든 것은 아님", False),
     "프로토타입을 완성품으로 오해할 때", "그림이 <b>진짜 같을수록</b> 거의 다 만들었다는 오해가 커집니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("와이어프레임", "회색 상자", "색과 글꼴을 <b>일부러 쓰지 않습니다</b>"),
    ("목업", "자리와 크기", "자리와 크기는 정했지만 아직 <b>눌러 볼 수 없습니다</b>"),
    ("시안", "완성 그림", "색과 글꼴, 그림까지 모두 입힌 그림입니다"),
    ("프로토타입", "눌리는 시안", "시안의 화면끼리 <b>이어 두어</b> 눌러서 넘어갈 수 있게 한 것입니다"),
    ("충실도", "fidelity", "충실도가 높을수록 보는 사람이 <b>다른 질문</b>을 합니다"),
    ("단계 섞기", "질문과 어긋난 리뷰", "구조를 물었는데 색 이야기가 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          물을 질문에 맞춰 <b>충실도를 일부러 낮추는 것</b>이 요령입니다.
          구조를 정하는 회의에 색이 칠해진 그림을 가져가면 사람들은 색 이야기를 먼저 꺼내는데,
          색이 가장 눈에 띄고 의견을 내기도 쉽기 때문입니다.
          따라서 회색 상자로만 그린 그림은 <b>덜 만든 그림</b>이 아니라
          <b>구조를 묻는 데 맞춰 만든 그림</b>입니다.
          반대로 색을 확정해야 하는 자리에 와이어프레임을 가져가면
          판단할 재료가 없어서 아무것도 정하지 못하고 끝납니다.</p>''',
  do_title="단계에 맞춰 그림을 고르는 방법",
  dont_title="그림을 주고받을 때 피할 것",
  do=ul([
    "구조를 정할 때는 <b>와이어프레임</b>을 가져갑니다",
    "화면 폭과 글 길이를 볼 때는 <b>목업</b>을 가져갑니다",
    "흐름을 시험할 때는 <b>프로토타입</b>을 씁니다",
  ]),
  dont=ul([
    "구조 회의에 <b>시안</b>을 가져갈 때. 사람들이 구조 대신 색 이야기를 합니다",
    "색을 정하는 자리에 <b>회색 상자</b>를 가져갈 때",
    "프로토타입을 <b>다 만든 것</b>처럼 보고할 때",
    "단계를 밝히지 않고 그림만 넘길 때",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='눌러 볼 수 있게 만든 그림은 <a href="prototype.html">프로토타입</a>에서, 그림을 개발 쪽에 넘기는 일은 <a href="handoff.html">핸드오프</a>에서, 부품 규칙은 <a href="designsystem.html">디자인 시스템</a>에서 다룹니다.',
  cases=cases([
    (blocks(False, "150px", "구조만 그림"), "기획 회의에서 구조 정하기", "화면에 <b>무엇이 있고 무엇이 중요한지</b> 정합니다"),
    (blocks(True, "150px", "완성 그림"), "색과 글꼴 확정하기", "<b>색과 글꼴, 아이콘</b>을 정합니다"),
    (card('<span style="font-size:9px">1 → 2 → 3</span>'
          '<span style="font-size:8.5px;color:var(--accent)">눌러서 넘어감</span>', "150px", "흐름 시험"),
     "사용자 시험으로 막히는 곳 찾기", "사용자가 화면을 넘기다 <b>막히는 곳</b>을 찾습니다"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="그림과 함께 적을 것",
  code_lede="그림을 넘길 때는 그 그림의 <b>단계</b>와 받는 사람에게 묻고 싶은 <b>질문</b>을 함께 적어 보냅니다.",
  code='''<span class="c"># 그림을 넘길 때 함께 적는 것</span>

단계   : 와이어프레임
묻는 것: 이 화면에 들어갈 정보와 그 순서
안 묻는 것: 색 · 글꼴 · 아이콘 (아직 안 정했습니다)
다음   : 구조가 정해지면 목업으로 갑니다

<span class="c"># 프로토타입을 넘길 때는 한 줄 더</span>

이 프로토타입은 <span class="s">세 화면만</span> 이어 뒀습니다.
나머지는 눌러도 아무 일이 없습니다. <span class="s">아직 코드가 아닙니다.</span>''',
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("단계를 <b>파일 이름에</b> 적기", "<code>정산목록_와이어_v2</code>처럼 적어 두면 파일을 열어 보기 전에 단계를 알 수 있습니다"),
    ("묻고 싶은 질문을 함께 적기", "'무엇을 봐 주세요'라는 요청이 없으면 보는 사람은 그림에서 <b>눈에 보이는 것</b>을 말하게 됩니다"),
    ("와이어프레임은 회색으로만 그리기", "와이어프레임에 브랜드 색을 한 군데만 써도 보는 사람의 <b>눈이 그곳으로 먼저 갑니다</b>"),
    ("진짜 글을 넣을지 정하기", "Lorem ipsum 같은 가짜 글로는 실제 글이 얼마나 길어질지 <b>감</b>을 잡을 수 없습니다. 진짜 글을 넣더라도 색은 아직 정하지 않아도 됩니다"),
    ("프로토타입에 꼬리표 붙이기", "'아직 코드가 아닙니다'라는 문구를 <b>화면 안에</b> 적어 두면 다 만든 것으로 오해하는 일이 줄어듭니다"),
    ("버전 이름 짓기", "<code>v2</code>·<code>v3</code> 같은 번호보다 <b>날짜와 바뀐 내용</b>을 적어 두는 편이 쓸모 있습니다"),
  ]),
  backend=rows([
    ("와이어프레임 단계에서 필요한 데이터 확인하기", "화면에 어떤 필드가 필요한지는 <b>구조를 정하는 단계에서</b> 이미 드러납니다. 그래서 와이어프레임을 볼 때 필요한 데이터를 함께 확인해야 하고, 시안이 나올 때까지 기다리면 API 설계가 그만큼 늦어집니다."),
    ("시안에 그려지지 않은 상태 묻기", "빈 화면과 로딩, 오류 상태는 시안에 거의 그려져 있지 않으므로 시안을 받는 <b>이 단계에서 물어봐야</b> 합니다. 무엇을 물을지는 <a href=\"handoff.html\">핸드오프</a> 항목에 정리해 두었습니다."),
    ("프로토타입으로는 알 수 없는 성능", "프로토타입에서 누르자마자 다음 화면이 뜨는 것은 미리 그려 둔 <b>그림을 바꿔 보여 주기 때문</b>입니다. 실제 서비스에서는 그 사이에 서버와 요청이 오가므로 기다리는 시간이 생깁니다."),
  ]),
  plat_lede="플랫폼마다 쓰는 도구는 달라도 <b>그림을 그려 나가는 단계는 같습니다</b>.",
  plats=plats([
    ("웹", "HTML로 바로 짜기",
     blocks(False, "110px"),
     "웹에서는 HTML 코드로 와이어프레임을 짜기도 하는데, <b>실제 글 길이와 반응형 배치</b>를 바로 확인할 수 있다는 장점이 있습니다."),
    ("iOS", "단계는 웹과 같음",
     '''              <div class="phone" role="img" aria-label="iOS 와이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:7px;background:var(--ink-100);border-radius:2px"></span><span style="height:7px;background:var(--ink-100);border-radius:2px;width:70%"></span></div></div></div>''',
     "OS가 제공하는 부품이 정해져 있어서 <b>와이어프레임 단계가 짧게</b> 끝나는 편입니다."),
    ("안드로이드", "단계는 웹과 같음",
     '''              <div class="phone" role="img" aria-label="안드로이드 와이어 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:7px;background:var(--ink-100);border-radius:2px"></span><span style="height:7px;background:var(--ink-100);border-radius:2px;width:70%"></span></div></div></div>''',
     "단계는 iOS와 같지만, <b>기기마다 화면 폭이 다양</b>해서 목업 단계가 길어집니다."),
  ]),
  plat_note="\"시안 나왔어요\"라는 말을 들으면 그 시안이 <b>어느 단계인지</b>부터 물어보는 편이 좋습니다. 완성 그림인 줄 알고 그대로 만들었는데 디자이너는 <b>아직 구조를 보는 중</b>이었던 경우가 흔하고, 반대로 제안 단계인 줄 알고 의견을 냈는데 <b>이미 확정</b>된 그림이었던 경우도 있습니다. 파일 이름에 단계를 적어 두면 단계를 확인하려고 묻고 답하는 일이 없어집니다.",
  siblings=siblings("wireframe"),
  related='''        <li><a href="prototype.html"><b>프로토타입</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>''',
)
