# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">무엇을 봐 달라는지 단계부터 밝힘</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">구조는 와이어프레임에서 · 색은 시안에서</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">“왜 이렇게 했나요”는 설명을 끌어냄</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">“이건 아닌 것 같아요”는 방어를 끌어냄</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇이 걱정인지를 적으면 고칠 거리가 됨</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">두 번 논의하지 않게 정한 것을 적어 둠</div>
                </div>
              </div>'''

D = dict(
  slug="review", ko="디자인 리뷰", en="Design review",
  desc="시안을 두고 의견을 주고받는 디자인 리뷰에서, 단계에 맞는 질문과 고칠 거리가 되는 말투를 보여 주는 항목입니다.",
  lede="디자인 리뷰는 시안을 두고 의견을 주고받는 자리입니다. 리뷰가 쓸모 있으려면 시안의 <b>단계에 맞는 질문</b>을 하고, 듣는 사람이 <b>바로 고칠 수 있는 말투</b>로 의견을 줘야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 바꿔 가며 보세요. 같은 말이라도 어떤 단계에서는 쓸모 있지만, 다른 단계에서는
          <b>너무 이르거나 너무 늦습니다</b>.<br>
          <b>“이건 아닌 것 같아요”</b>처럼 어느 단계에서 들어도 고칠 수 없는 말도 있는데,
          무엇이 걱정인지가 빠져 있기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "디자인 리뷰, 시안 리뷰, 크리틱, 피드백"),
    ("영어", "design review, design critique, feedback round"),
    ("같이 쓰는 말",
     "여럿이 모여 시안을 함께 보는 자리를 <b>크리틱</b>(critique)이라고 하고, "
     "고쳐야 할 것을 적어 돌려주는 것을 <b>피드백</b>이라고 합니다. "
     "꼭 고쳐야 하는 것과 참고할 의견을 가려 <b>블로커</b>와 <b>논블로커</b>로 나누기도 합니다. "
     "리뷰에서 정한 것을 적어 두는 글은 <b>결정 기록</b>(decision log)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>승인</b> — 시안을 통과시키는 절차이고, 리뷰는 <b>고칠 거리를 찾는</b> 자리입니다.<br>"
     "<b>QA</b> — 다 만든 뒤에 기능이 <b>되는지 안 되는지</b>를 확인하는 일이라서 시안을 두고 하는 리뷰와 다릅니다.<br>"
     "<b>보고</b> — 결과를 보여 주는 자리와 의견을 <b>물어보는</b> 자리는 준비할 것이 다릅니다."),
  ]),
  s4_title="말이 맞는 리뷰 단계", s4_hint="단계에 따라 달라지는 말의 쓸모",
  states=states([
    (say('이 정보를 빼죠', '구조 이야기라 와이어프레임 단계에서 할 말', True), "와이어프레임 단계에 맞는 말", "<b>구조</b>를 묻는 단계라서 정보를 빼자는 말이 쓸모 있습니다"),
    (say('이 파랑이 좀 칙칙한데요', '와이어프레임에는 색이 없음', False), "너무 이른 말", "와이어프레임에는 색이 없으니 <b>아직 정하지 않은 것</b>을 말하는 셈입니다"),
    (say('대비가 모자라 보입니다', '시안에서 재면 적은 품으로 고침', True), "시안 단계에 맞는 말", "<b>마감</b>을 묻는 단계라서 대비를 지적하기에 알맞습니다"),
    (say('이 화면 구조를 바꾸자', '시안에서 하면 처음부터 다시 그려야 함', False), "너무 늦은 말", "시안 단계에서 구조를 바꾸자고 하면 <b>앞 단계로 되돌아가</b> 처음부터 다시 그려야 합니다"),
    (say('폰에서 눌러 봤는데 안 눌려요', '실제 기기에서 만든 뒤에만 알 수 있음', True), "만든 뒤에 할 말", "실제 기기에서 <b>정말 되는지</b>를 묻습니다"),
    (say('이건 아닌 것 같아요', '무엇이 걱정인지가 없음', False), "어느 단계에서도 쓸모없는 말", "무엇이 걱정인지가 없어서 <b>고칠 거리가 되지 않습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계 밝히기", "무엇을 봐 주세요", "단계를 밝히지 않으면 보는 사람은 그림에서 <b>눈에 보이는 것</b>을 말하게 됩니다"),
    ("단계에 맞는 질문", "구조 / 마감 / 동작", "단계보다 이르거나 늦은 의견은 반영되지 못하고 <b>버려집니다</b>"),
    ("왜 이렇게 했나요", "설명을 끌어냄", "디자인에는 대개 <b>이유가 있으니</b> 먼저 그 이유를 묻습니다"),
    ("이건 아닌 것 같아요", "방어를 끌어냄", "이 말에는 <b>무엇이 걱정인지</b>가 빠져 있습니다"),
    ("걱정 적기", "고칠 거리", "'글이 길어지면 깨질 것 같다'처럼 걱정을 적으면 고칠 거리가 됩니다"),
    ("정한 것 적어 두기", "결정 기록", "정한 것을 적어 두어야 같은 문제를 <b>두 번 논의하지 않습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          리뷰에서 가장 쓸모 있는 말은 <b>'무엇이 걱정인지'</b>를 밝힌 말입니다.
          예를 들어 '이 버튼이 눈에 안 띄어요'보다
          '이게 주 동작인데 취소와 같은 무게라 헷갈릴 것 같아요'라고 해야
          <b>고칠 거리</b>가 됩니다. 앞의 말은 개인 취향으로도 들리지만,
          뒤의 말은 <b>해결해야 할 문제</b>를 짚기 때문입니다.
          코드 리뷰에서 '이 코드 이상해요'보다
          '여기서 null이 오면 터질 것 같아요'가 나은 것도 <b>같은 이유</b>입니다.</p>''',
  do_title="디자인 리뷰에서 지킬 것",
  dont_title="디자인 리뷰에서 피할 것",
  do=ul([
    "리뷰를 요청할 때 <b>단계와 질문</b>을 먼저 밝힙니다",
    "걱정을 <b>구체적으로</b> 적습니다",
    "정한 것을 <b>그 자리에서</b> 적어 둡니다",
  ]),
  dont=ul([
    "단계를 밝히지 않고 그림만 올릴 때",
    "취향으로 말할 때. 대신 그 디자인이 <b>무엇을 해치는지</b>를 적습니다",
    "한 번에 <b>스무 가지</b>를 지적할 때. 너무 많으면 결국 아무것도 고쳐지지 않습니다",
    "정한 것을 적어 두지 않을 때. 같은 이야기가 <b>다음 회의에 또 나옵니다</b>",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='그림의 단계 구분은 <a href="wireframe.html">와이어프레임과 목업과 시안</a>에서, 시안을 개발 쪽에 넘기는 일은 <a href="handoff.html">핸드오프</a>에서, 시안 파일이 바뀌어 온 기록은 <a href="versioning.html">버전 관리</a>에서 다룹니다.',
  cases=cases([
    (say('글이 길어지면 두 줄로 접히나요', '경계 질문이라 늘 쓸모 있음', True), "글 길이와 화면 폭 묻기", "글이 길어지거나 화면이 좁아질 때를 묻는 질문은 <b>어느 단계에서나</b> 쓸모 있습니다"),
    (say('주 동작인데 취소와 무게가 같아 보여요', '무엇이 걱정인지 담겨 있음', True), "걱정을 담아 지적하기", "무엇이 걱정인지 담겨 있어서 <b>고칠 거리</b>가 됩니다"),
    (say('제 취향은 아니지만요', '취향은 기준이 될 수 없음', False), "취향으로 말하는 경우", "취향은 기준이 될 수 없으니, 대신 <b>무엇을 해치는지</b>를 적습니다"),
  ]),
  s8_title="주고받을 때의 규칙", s8_hint="요청할 때와 돌려줄 때 적을 것",
  code_lede="리뷰를 요청할 때와 의견을 돌려줄 때 각각 <b>적어야 할 것</b>이 정해져 있습니다.",
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
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("단계와 질문 먼저 밝히기", "'무엇을 봐 주세요'라는 요청이 없으면 보는 사람은 그림에서 <b>눈에 보이는 것</b>을 말하게 됩니다"),
    ("이미 정한 것 적기", "이미 정한 것을 적어 두면 그 내용이 <b>다시 논의되지 않습니다</b>"),
    ("걱정을 구체적으로 적기", "'눈에 안 띈다'보다 <b>'잘못 누를 것 같다'</b>처럼 생길 문제를 적습니다"),
    ("<a href=\"../items/contrast.html\">대비비</a>처럼 <b>잴 수 있는 것</b>으로 말하기", "대비비처럼 숫자로 말하면 취향을 두고 다툴 일이 없습니다"),
    ("지적 개수 줄이기", "스무 가지를 한꺼번에 주면 <b>아무것도 고쳐지지 않으니</b> 중요한 세 가지만 고릅니다"),
    ("결정 기록 남기기", "<b>결정 기록</b>이 없으면 같은 안건으로 회의를 두 번 하게 됩니다"),
  ]),
  backend=rows([
    ("개발 쪽 질문은 일찍 하기", "'이 값은 서버에 있나요' 같은 질문은 <b>와이어프레임 단계</b>에서 일찍 물을수록 고치는 비용이 적게 듭니다."),
    ("빠진 화면 지적하기", "빈 화면과 로딩, 오류 화면은 시안에 거의 없습니다. 리뷰에서 지적하지 않으면 <a href=\"handoff.html\">핸드오프</a> 때 다시 문제가 됩니다."),
    ("만들 수 있는지 미리 따지기", "'이 애니메이션은 매 프레임 배치를 다시 합니다' 같은 지적이 <b>시안 단계에서</b> 나오면, 만들고 나서 고치는 것보다 훨씬 적은 품으로 해결할 수 있습니다(<a href=\"cheap.html\">무엇을 움직이나</a> 참고)."),
  ]),
  plat_lede="디자인 리뷰의 요령은 <b>플랫폼과 상관없이 같고</b>, 코드 리뷰의 요령과도 같습니다.",
  plats=plats([
    ("웹", "코드 리뷰와 같은 요령",
     say('여기서 null 이 오면 터질 것 같아요', '같은 말투', True, "110px"),
     "'무엇이 걱정인지'를 적는다는 점에서 <b>코드 리뷰의 요령</b>과 같습니다."),
    ("iOS", "웹과 같은 규칙",
     '''              <div class="phone" role="img" aria-label="리뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">단계 · 질문 · 기한</div></div></div>''',
     "OS 관례를 지적할 때 <b>HIG의 어느 대목</b>에 근거하는지 함께 적으면 논쟁이 짧아집니다."),
    ("안드로이드", "웹과 같은 규칙",
     '''              <div class="phone" role="img" aria-label="리뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">단계 · 질문 · 기한</div></div></div>''',
     "Material 규격도 마찬가지로, 규격의 어느 대목인지 <b>근거를 적으면</b> 취향을 두고 다투지 않게 됩니다."),
  ]),
  plat_note="리뷰가 길어지는 이유는 대개 <b>단계를 밝히지 않아서</b>입니다. 단계를 모르니 구조를 묻는 자리에서 색 이야기가 나오고, 색을 정하는 자리에서 구조 이야기가 나옵니다. 리뷰를 요청할 때 <b>\"이번에는 이것만 봐 주세요\"</b>라는 한 줄만 적어도 회의 시간이 눈에 띄게 줄어듭니다.",
  siblings=siblings("review"),
  related='''        <li><a href="wireframe.html"><b>와이어프레임과 목업과 시안</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="versioning.html"><b>버전 관리</b><em>15부</em></a></li>
        <li><a href="../items/contrast.html"><b>대비비</b><em>12부</em></a></li>''',
)
