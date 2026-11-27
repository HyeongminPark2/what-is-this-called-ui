# -*- coding: utf-8 -*-
from ax15 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def say(s, why, ok=None, w="152px"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    mark = '○' if ok else ('✕' if ok is False else '·')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">'
            '<span style="font-size:9.5px"><b style="color:' + col + '">' + mark + '</b> “' + s + '”</span></div>'
            '<span style="font-size:8.5px;color:var(--fg-muted)">' + why + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">단계를 먼저 밝힌다 — 무엇을 봐 주세요</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">구조는 와이어프레임에서 · 색은 시안에서</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">왜 이렇게 했나요 — 설명을 끌어낸다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">이건 아닌 것 같아요 — 방어를 끌어낸다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇이 걱정인지를 적으면 고칠 거리가 된다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">정한 것을 적어 둔다 — 두 번 논의하지 않게</div>
                </div>
              </div>'''

D = dict(
  slug="review", ko="디자인 리뷰", en="Design review",
  desc="시안에 의견을 주고받는 일. 단계에 맞는 질문과 고칠 거리가 되는 말투.",
  lede="의견을 주고받는 자리. <b>단계에 맞는 질문</b>과 <b>고칠 거리가 되는 말투</b>가 전부입니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 바꿔 가며 보세요 — 같은 말이 어느 단계에서는 쓸모 있고 어느 단계에서는
          <b>너무 이르거나 너무 늦습니다</b>.<br>
          <b>“이건 아닌 것 같아요”</b>처럼 어느 단계에서도 못 고치는 말도 있습니다.
          무엇이 걱정인지가 없기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "디자인 리뷰, 시안 리뷰, 크리틱, 피드백"),
    ("영어", "design review, design critique, feedback round"),
    ("같이 쓰는 말",
     "여럿이 모여 보는 자리를 <b>크리틱</b>(critique)이라 하고, "
     "고쳐야 할 것을 적어 돌려주는 것이 <b>피드백</b>입니다. "
     "꼭 고쳐야 하는 것과 의견을 가려 <b>블로커</b>·<b>논블로커</b>로 나누기도 합니다. "
     "정한 것을 적어 두는 글은 <b>결정 기록</b>(decision log)입니다."),
    ("자주 잘못 부름",
     "<b>승인</b> — 통과시키는 절차이고, 리뷰는 <b>고칠 거리를 찾는</b> 자리입니다.<br>"
     "<b>QA</b> — 만든 뒤 <b>된다/안 된다</b>를 보는 일입니다.<br>"
     "<b>보고</b> — 보여 주는 자리와 <b>물어보는</b> 자리는 준비가 다릅니다."),
  ]),
  axes=ax("디자인 리뷰"),
  oneline="<b>“왜 이렇게 했나요”는 설명을 끌어내고, “이건 아닌 것 같아요”는 방어를 끌어냅니다.</b>",
  s4_title="어느 단계의 말인가", s4_hint="같은 말, 다른 쓸모",
  states=states([
    (say('이 정보를 빼죠', '구조 이야기 — 와이어프레임 단계에서', True), "와이어프레임", "<b>구조</b>를 묻는 자리"),
    (say('이 파랑이 좀 칙칙한데요', '와이어프레임에는 색이 없다', False), "너무 이른 말", "<b>아직 안 정한 것</b>을 말한다"),
    (say('대비가 모자라 보입니다', '시안에서 재면 고치기 싸다', True), "시안", "<b>마감</b>을 묻는 자리"),
    (say('이 화면 구조를 바꾸자', '시안에서 하면 처음부터 다시 그린다', False), "너무 늦은 말", "<b>단계를 거슬러</b> 간다"),
    (say('폰에서 눌러 봤는데 안 눌려요', '실제 기기 — 만든 뒤에만 안다', True), "만든 뒤", "<b>실제로 되는가</b>를 묻는다"),
    (say('이건 아닌 것 같아요', '무엇이 걱정인지가 없다', False), "어느 단계에서도", "<b>고칠 거리가 안 된다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계를 밝힌다", "무엇을 봐 주세요", "안 밝히면 <b>보이는 것</b>을 말하게 된다"),
    ("단계에 맞는 질문", "구조 / 마감 / 동작", "이르거나 늦으면 <b>버려진다</b>"),
    ("왜 이렇게 했나요", "설명을 끌어낸다", "대개 <b>이유가 있다</b>"),
    ("이건 아닌 것 같아요", "방어를 끌어낸다", "<b>무엇이 걱정인지</b>가 없다"),
    ("걱정을 적는다", "고칠 거리", "'글이 길어지면 깨질 것 같다'처럼"),
    ("정한 것을 적어 둔다", "결정 기록", "<b>두 번 논의하지 않게</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          리뷰에서 가장 쓸모 있는 말은 <b>'무엇이 걱정인지'</b>입니다.
          '이 버튼이 눈에 안 띄어요'보다
          '이게 주 동작인데 취소와 같은 무게라 헷갈릴 것 같아요'가
          <b>고칠 거리</b>가 됩니다 — 앞의 말은 취향으로도 읽히지만
          뒤의 말은 <b>해결해야 할 문제</b>로 읽힙니다.
          이것은 코드 리뷰에서 '이 코드 이상해요'보다
          '여기서 null 이 오면 터질 것 같아요'가 나은 것과 <b>정확히 같은 이야기</b>입니다.</p>''',
  do=ul([
    "<b>단계와 질문</b>을 먼저 밝히기",
    "걱정을 <b>구체적으로</b> 적기",
    "정한 것을 <b>그 자리에서</b> 적어 두기",
  ]),
  dont=ul([
    "단계를 안 밝히고 그림만 올리기",
    "취향으로 말하기 — <b>무엇을 해치는지</b>를 적는다",
    "한 번에 <b>스무 가지</b> 지적하기 — 아무것도 안 고쳐진다",
    "정한 것을 안 적어 두기 — <b>다음 회의에 또 나온다</b>",
  ]),
  instead='단계 구분은 <a href="wireframe.html">와이어프레임과 목업과 시안</a>, 넘기는 일은 <a href="handoff.html">핸드오프</a>, 파일 역사는 <a href="versioning.html">버전 관리</a>.',
  cases=cases([
    (say('글이 길어지면 두 줄로 접히나요', '경계 질문 — 늘 쓸모 있다', True), "경계", "<b>어느 단계에서나</b> 맞다"),
    (say('주 동작인데 취소와 무게가 같아 보여요', '무엇이 걱정인지가 있다', True), "좋은 지적", "<b>고칠 거리</b>가 된다"),
    (say('제 취향은 아니지만요', '취향은 기준이 아니다', False), "안 되는 말", "<b>무엇을 해치는지</b>를 적는다"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="이 자리의 계약서",
  code_lede="리뷰를 요청할 때와 돌려줄 때 <b>적을 것</b>이 정해져 있습니다.",
  code='''<span class="c"># 리뷰를 요청할 때</span>
단계   : 시안
봐 주실 것: 주 동작이 눈에 띄는지 · 대비가 충분한지
이미 정한 것: 구조와 정보 순서 (지난주 확정)
기한   : 11월 16일까지

<span class="c"># 의견을 줄 때 — 무엇이 걱정인지를 적는다</span>
○ 주 동작인데 취소와 무게가 같아 보입니다. 잘못 누를 것 같아요.
○ 회색 글씨가 3.1:1 로 보입니다. 4.5:1 을 못 넘깁니다.
✕ 이건 좀 아닌 것 같아요.
✕ 제 취향은 아닌데요.

<span class="c"># 정한 것은 그 자리에서 적는다</span>
11-14 주 동작은 칠한 버튼, 취소는 테두리만. (홍길동·김철수 합의)''',
  keys=kbd([
    ("단계와 질문을 먼저", "'무엇을 봐 주세요'가 없으면 <b>보이는 것</b>을 말하게 된다"),
    ("이미 정한 것을 적는다", "<b>다시 논의되는 것</b>을 막는다"),
    ("걱정을 구체적으로", "'눈에 안 띈다'보다 <b>'잘못 누를 것 같다'</b>"),
    ("<a href=\"../items/contrast.html\">대비비</a>처럼 <b>잴 수 있는 것</b>", "숫자로 말하면 취향 논쟁이 안 된다"),
    ("개수를 줄인다", "스무 가지를 주면 <b>아무것도 안 고쳐진다</b>. 중요한 셋을 고른다"),
    ("정한 것을 적어 둔다", "<b>결정 기록</b>이 없으면 같은 회의를 두 번 한다"),
  ]),
  backend=rows([
    ("개발 쪽 질문을 일찍", "'이 값은 서버에 있나요'는 <b>와이어프레임 단계</b>에서 물을수록 쌉니다."),
    ("없는 화면을 지적한다", "빈·로딩·오류는 시안에 거의 없습니다 — <a href=\"handoff.html\">핸드오프</a>에서 다시 걸립니다."),
    ("만들 수 있는지", "'이 애니메이션은 매 프레임 배치를 다시 합니다' 같은 지적이 <b>시안 단계에서</b> 나오면 값이 큽니다 — <a href=\"cheap.html\">무엇을 움직이나</a>."),
  ]),
  plat_lede="<b>어느 쪽 일이든 같습니다</b> — 코드 리뷰와 뿌리가 같습니다.",
  plats=plats([
    ("웹", "코드 리뷰와 같다",
     say('여기서 null 이 오면 터질 것 같아요', '같은 말투', True, "110px"),
     "'무엇이 걱정인지'를 적는 것이 <b>코드 리뷰의 요령</b>과 정확히 같습니다."),
    ("iOS", "같은 규칙",
     '''              <div class="phone" role="img" aria-label="리뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">단계 · 질문 · 기한</div></div></div>''',
     "OS 관례를 지적할 때는 <b>HIG 의 어느 대목</b>인지 함께 적으면 논쟁이 짧아집니다."),
    ("안드로이드", "같은 규칙",
     '''              <div class="phone" role="img" aria-label="리뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">단계 · 질문 · 기한</div></div></div>''',
     "Material 규격도 마찬가지입니다 — <b>근거를 적으면</b> 취향 논쟁이 안 됩니다."),
  ]),
  plat_note="리뷰가 길어지는 이유는 대개 <b>단계가 안 밝혀져서</b>입니다. 구조를 묻는 자리에 색 이야기가 나오고, 색을 정하는 자리에 구조 이야기가 나옵니다. 요청할 때 <b>\"이번에는 이것만 봐 주세요\"</b> 한 줄을 적는 것으로 회의 시간이 눈에 띄게 줄어듭니다.",
  siblings=siblings("review"),
  related='''        <li><a href="wireframe.html"><b>와이어프레임과 목업과 시안</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="versioning.html"><b>버전 관리</b><em>15부</em></a></li>
        <li><a href="../items/contrast.html"><b>대비비</b><em>12부</em></a></li>''',
)
