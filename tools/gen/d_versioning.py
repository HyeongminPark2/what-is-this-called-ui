# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def files(names, w="152px", note="", ok=None, cur=-1):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    body = ''.join('<div style="font-size:9px;padding:3px 5px;border-radius:3px;'
                   + ('background:var(--accent-soft);color:var(--accent);font-weight:700' if i == cur else '')
                   + '">' + n + ('  · 지금 것' if i == cur else '') + '</div>'
                   for i, n in enumerate(names))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:6px;display:grid;gap:1px">'
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">날짜와 무엇이 바뀌었는지 적기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">누가 고쳤는지</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">지금 것이 하나로 분명해야 함</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">파일을 복제하지 말고 버전 기록을 씀</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">v1 · v2로는 차이를 모름</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">final · 진짜final로는 지금 것을 모름</div>
                </div>
              </div>'''

D = dict(
  slug="versioning", ko="버전 관리", en="Versioning",
  desc="시안 파일이 바뀌어 온 기록을 다루는 항목입니다. 어느 것이 지금 쓰는 파일인지, 무엇이 왜 바뀌었는지를 남기는 방법을 보여 줍니다.",
  lede="시안도 고칠 때마다 바뀐 기록이 쌓입니다. 이 기록에서 꼭 남겨야 할 것은 <b>어느 것이 지금 것인가</b>와 <b>무엇이 왜 바뀌었나</b>, 두 가지입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이름 짓는 법을 바꿔 보세요. <code>v3</code>나 <code>final</code> 같은 이름으로는
          <b>두 질문 어느 쪽에도 답할 수 없습니다</b>.<br>
          <b>날짜와 무엇이 바뀌었는지</b>를 적으면 고친 이유가 남기 때문에, 코드의 커밋 메시지와
          같은 역할을 합니다. <b>고친 것 하나 더</b>를 눌러 보면 두 방식의 차이가 더 벌어집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버전 관리, 이력, 변경 기록, 되돌리기"),
    ("영어", "versioning, version history, branching, change log"),
    ("같이 쓰는 말",
     "시안 도구가 자동으로 쌓아 두는 기록을 <b>버전 기록</b>(version history)이라고 하고, "
     "그 가운데 따로 이름을 붙여 둔 지점을 <b>마일스톤</b> 또는 <b>명명된 버전</b>이라고 합니다. "
     "코드 쪽에서는 <b>커밋</b>과 <b>브랜치</b>가 같은 역할을 하고, "
     "무엇이 바뀌었는지 적은 글을 <b>커밋 메시지</b> 또는 <b>체인지로그</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>백업</b> — 파일을 잃지 않으려고 만드는 사본이고, 버전은 파일이 바뀌어 온 <b>기록</b>입니다.<br>"
     "<b>릴리스 버전</b> — 제품의 1.2.0 같은 번호는 사용자에게 <b>밖으로 알리는</b> 이름이라서 시안의 버전 기록과는 다릅니다.<br>"
     "<b>브랜치</b> — 원본에서 갈라져 나와 따로 작업하는 것을 말하며, 시안 도구에도 비슷한 기능이 있습니다."),
  ]),
  s4_title="버전 이름 짓는 방식", s4_hint="지금 것과 바뀐 내용을 알 수 있는지",
  states=states([
    (files(['11-07 첫 구조 — 목록과 상세', '11-10 상태를 칩으로', '11-14 빈 화면 추가'], "152px", "무엇이 바뀌었는지 남음", True, 2),
     "날짜와 바뀐 내용을 적은 이름 ✓", "나중에 보아도 <b>왜 바꿨는지</b> 알 수 있습니다"),
    (files(['정산목록_v1', '정산목록_v2', '정산목록_v3'], "152px", "v2와 v3의 차이를 알 수 없음", False, 2),
     "v1 · v2 · v3 번호만 붙인 이름", "무엇이 다른지는 파일을 <b>열어 봐야</b> 압니다"),
    (files(['정산목록', '정산목록_final', '정산목록_진짜final', '정산목록_진짜final_수정'], "152px", "어느 것이 지금 것인지 알 수 없음", False),
     "final을 이어 붙인 이름(final 사슬)", "<b>가장 흔하면서 가장 나쁜</b> 방식입니다. 어느 것이 지금 것인지 알 수 없습니다"),
    (files(['정산목록 (버전 기록 안에)'], "152px", "파일 하나에 기록이 쌓임", True, 0),
     "도구의 버전 기록 쓰기", "파일이 하나뿐이라 <b>지금 것이 늘 하나</b>로 분명합니다"),
    (files(['정산목록', '정산목록_김철수수정본', '정산목록_복사본'], "152px", "복제본이 갈라짐", False),
     "파일을 복제해 갈라진 경우", "각자 고친 내용을 <b>하나로 합칠 수 없습니다</b>"),
    (files(['11-14 승인 전 (마일스톤)'], "152px", "돌아올 지점에 이름을 붙여 둠", True, 0),
     "마일스톤 붙여 두기", "나중에 <b>돌아올 지점</b>에 이름을 붙여 표시해 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("날짜", "11-14", "<b>언제</b> 바뀌었는지 적습니다"),
    ("바뀐 것", "빈 화면 추가", "<b>무엇이</b> 바뀌었는지 적습니다. 이름에서 가장 중요한 부분입니다"),
    ("지금 것", "하나로 분명하게", "지금 것이 둘 이상이면 <b>이미 관리가 어긋난</b> 상태입니다"),
    ("버전 기록", "도구가 쌓음", "도구가 기록을 쌓으니 파일을 <b>복제하지 않습니다</b>"),
    ("마일스톤", "돌아올 지점", "'승인 전'처럼 <b>이름을 붙여</b> 둡니다"),
    ("번호·final", "알 수 있는 것이 없음", "번호나 final로는 지금 것도, 바뀐 내용도 <b>알 수 없습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>시안 파일을 복제하면 그 뒤로는 두 파일을 합칠 수 없습니다.</b>
          코드는 갈라져도 다시 합칠 수 있지만, 복제한 시안 파일은
          두 사람이 각자 고친 내용을 <b>자동으로 합칠 방법이 없습니다</b>.
          그래서 복제본이 생기면 결국 누군가 한쪽의 수정 내용을 <b>손으로 옮겨 붙여야</b> 하고,
          그 과정에서 무언가 빠지기 쉽습니다.
          도구의 버전 기록을 쓰면 <b>파일은 늘 하나</b>로 남고
          바뀐 기록은 그 파일 안에 쌓입니다. 파일을 복제하고 싶어질 때도
          따져 보면 대개 <b>따로 작업할 이유가 없는 경우</b>가 많습니다.</p>''',
  do_title="버전을 관리할 때 지킬 것",
  dont_title="버전을 관리할 때 피할 것",
  do=ul([
    "시안 도구의 <b>버전 기록</b>을 씁니다",
    "버전 이름에는 <b>무엇이 바뀌었는지</b> 적습니다",
    "돌아올 지점에는 <b>마일스톤</b> 이름을 붙여 둡니다",
  ]),
  dont=ul([
    "<code>v1</code>·<code>v2</code>처럼 번호만 붙일 때. 버전끼리 <b>무엇이 다른지</b> 알 수 없습니다",
    "<code>final</code>·<code>진짜final</code>처럼 이름을 붙일 때. 어느 것이 <b>지금 것인지</b> 알 수 없습니다",
    "파일을 복제해서 따로 작업할 때. 나중에 <b>합칠 수 없습니다</b>",
    "고친 이유를 적지 않을 때. 몇 달 뒤에는 <b>왜 바꿨는지 아는 사람이 없습니다</b>",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='시안을 두고 의견을 주고받는 일은 <a href="review.html">디자인 리뷰</a>에서, 시안을 개발 쪽에 넘기는 일은 <a href="handoff.html">핸드오프</a>에서, 부품이 바뀌어 온 기록은 <a href="designsystem.html">디자인 시스템</a>에서 다룹니다.',
  cases=cases([
    (files(['11-14 빈 화면과 오류 추가'], "150px", "커밋 메시지와 같은 역할", True, 0),
     "바뀐 내용을 적은 이름", "이름만 보고도 <b>무엇이 바뀌었는지</b> 알 수 있습니다"),
    (files(['11-14 승인 전 (마일스톤)'], "150px", "돌아올 자리", True, 0),
     "승인 전 지점에 마일스톤 붙이기", "승인이나 배포 직전에 붙여 둡니다"),
    (files(['정산목록_진짜final_수정_v2'], "150px", "실제로 자주 보이는 이름", False),
     "final과 번호가 뒤섞인 이름", "<b>이름만 보고는</b> 지금 것인지도, 무엇이 바뀌었는지도 알 수 없습니다"),
  ]),
  s8_title="버전 이름 적는 법", s8_hint="날짜와 바뀐 내용 적기",
  code_lede="버전 이름에는 커밋 메시지처럼 <b>무엇이 바뀌었는지</b>를 적습니다.",
  code='''<span class="c"># 버전 이름 — 날짜 + 무엇이 바뀌었는지</span>
11-07  첫 구조 — 목록과 상세
11-10  정산 상태를 칩으로 바꿈 (리뷰 반영)
11-12  폰에서 두 단 → 한 단
11-14  빈 화면 · 오류 화면 추가       ← 지금 것
11-14  승인 전 (마일스톤)

<span class="c"># 안 되는 이름</span>
정산목록_v3          <span class="c"># v2 와 뭐가 다른가</span>
정산목록_final       <span class="c"># final 다음에 또 온다</span>
정산목록_김철수수정본 <span class="c"># 합칠 수 없는 복제본</span>

<span class="c"># 코드 쪽도 같은 일을 한다</span>
git commit -m <span class="s">"정산 목록에 빈 화면과 오류 화면을 더한다"</span>''',
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("무엇이 바뀌었는지 적기", "번호 대신 바뀐 <b>내용</b>을 적습니다"),
    ("파일 복제하지 않기", "복제한 시안 파일은 나중에 <b>합칠 수 없습니다</b>"),
    ("마일스톤 붙이기", "승인이나 배포 직전에 그 지점에 <b>이름을 붙여</b> 둡니다"),
    ("누가 고쳤는지 남기기", "두 사람 이상이 같은 파일을 고치면 <b>누가 고쳤는지</b>도 남겨야 합니다"),
    ("부품을 쓰는 쪽에 미리 알리기", "부품을 고치면 그 부품을 <b>쓰는 화면이 모두</b> 바뀌므로 미리 알립니다(<a href=\"designsystem.html\">디자인 시스템</a> 참고)"),
    ("파일 대신 링크 공유하기", "파일을 보내면 <b>보낸 시점에서 더 바뀌지 않는 사본</b>이 여기저기 돌아다니게 됩니다"),
  ]),
  backend=rows([
    ("티켓에 시안 링크 붙이기", "티켓에는 파일 대신 시안 <b>링크</b>를 답니다. 링크는 늘 최신 시안을 가리키므로 시안을 고쳐도 다시 달 필요가 없습니다."),
    ("부품을 고칠 때 버전 붙이기", "디자인 시스템 부품을 고치면 그 부품을 <b>쓰는 곳이 모두</b> 바뀌므로, 무엇이 바뀌는지 적어서 함께 배포합니다."),
    ("토큰을 바꾼 이유도 남기기", "토큰의 색을 바꿀 때 그 이유를 적어 둬야 나중에 <b>되돌릴지 말지</b> 판단할 수 있습니다."),
  ]),
  plat_lede="버전 기록은 <b>도구가 쌓아 주지만, 버전 이름은 사람이</b> 지어야 합니다.",
  plats=plats([
    ("웹", "git 커밋과 같은 원리",
     files(['11-14 빈 화면 추가'], "110px", "", True, 0),
     "버전 이름은 git의 커밋 메시지와 <b>같은 역할</b>을 하므로, 커밋 메시지처럼 무엇이 바뀌었는지를 적습니다."),
    ("iOS", "웹과 같은 문제",
     '''              <div class="phone" role="img" aria-label="버전 기록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">버전 기록</div></div></div>''',
     "에셋과 시안 모두 웹과 같습니다. <b>복제본</b>이 생기면 그때부터 파일끼리 내용이 어긋나기 시작합니다."),
    ("안드로이드", "웹과 같은 문제",
     '''              <div class="phone" role="img" aria-label="버전 기록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">버전 기록</div></div></div>''',
     "방식은 같지만, 기기 폭이 다양해서 <b>시안 수가 늘어나는</b> 만큼 더 자주 어긋납니다."),
  ]),
  plat_note="<b>final 사슬</b>은 농담처럼 이야기되지만 실제로 비용이 드는 문제입니다. 개발자가 옛 시안을 보고 만들면 그 작업을 그대로 다시 해야 하는데, 이런 일은 버전 이름 한 줄로 막을 수 있습니다. 도구의 버전 기록을 쓰고 <b>무엇이 바뀌었는지</b>를 적는 습관만 들여도 이런 일은 대부분 사라집니다.",
  siblings=siblings("versioning"),
  related='''        <li><a href="review.html"><b>디자인 리뷰</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>''',
)
