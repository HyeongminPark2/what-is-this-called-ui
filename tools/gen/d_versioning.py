# -*- coding: utf-8 -*-
from ax15 import ax
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">날짜 + 무엇이 바뀌었는지</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">누가 고쳤는지</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">지금 것이 하나로 분명할 것</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">파일을 복제하지 말고 버전 기록을 쓴다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">v1 · v2 — 차이를 모른다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">final · 진짜final — 어느 것이 지금 것인지 모른다</div>
                </div>
              </div>'''

D = dict(
  slug="versioning", ko="버전 관리", en="Versioning",
  desc="시안 파일의 역사. 어느 것이 지금 것인지와 무엇이 왜 바뀌었는지를 남기는 법.",
  lede="시안에도 역사가 쌓입니다. 남겨야 할 것은 둘입니다 — <b>어느 것이 지금 것인가</b>와 <b>무엇이 왜 바뀌었나</b>.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>이름 짓는 법을 바꿔 보세요. <code>v3</code>·<code>final</code>은 둘 다
          <b>두 질문에 답하지 않습니다</b>.<br>
          <b>날짜 + 무엇이 바뀌었는지</b>를 적으면 고친 이유가 남고, 코드의 커밋 메시지와
          같은 일을 하게 됩니다. <b>고친 것 하나 더</b>를 눌러 보면 차이가 더 벌어집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버전 관리, 이력, 변경 기록, 되돌리기"),
    ("영어", "versioning, version history, branching, change log"),
    ("같이 쓰는 말",
     "시안 도구가 자동으로 쌓아 두는 것이 <b>버전 기록</b>(version history)이고, "
     "따로 이름을 붙여 둔 지점이 <b>마일스톤</b>·<b>명명된 버전</b>입니다. "
     "코드 쪽에서는 <b>커밋</b>과 <b>브랜치</b>가 같은 자리이고, "
     "무엇이 바뀌었는지 적은 글이 <b>커밋 메시지</b>·<b>체인지로그</b>입니다."),
    ("자주 잘못 부름",
     "<b>백업</b> — 잃지 않으려고 만드는 사본입니다. 버전은 <b>역사</b>입니다.<br>"
     "<b>릴리스 버전</b> — 제품의 1.2.0 같은 번호는 <b>밖에 알리는</b> 이름입니다.<br>"
     "<b>브랜치</b> — 갈라져 따로 가는 것입니다. 시안 도구에도 비슷한 기능이 있습니다."),
  ]),
  axes=ax("버전 관리"),
  oneline="<b>파일 이름으로 버전을 적지 마세요.</b> 도구의 버전 기록을 쓰고, 이름에는 <b>무엇이 바뀌었는지</b>를 적으세요.",
  s4_title="이름 짓는 법", s4_hint="두 질문에 답하나",
  states=states([
    (files(['11-07 첫 구조 — 목록과 상세', '11-10 상태를 칩으로', '11-14 빈 화면 추가'], "152px", "무엇이 바뀌었는지 남는다", True, 2),
     "날짜 + 바뀐 것 ✓", "<b>왜 그랬는지</b>를 나중에 알 수 있다"),
    (files(['정산목록_v1', '정산목록_v2', '정산목록_v3'], "152px", "v2 와 v3 의 차이를 모른다", False, 2),
     "v1 · v2 · v3", "<b>열어 봐야</b> 안다"),
    (files(['정산목록', '정산목록_final', '정산목록_진짜final', '정산목록_진짜final_수정'], "152px", "어느 것이 지금 것인지 모른다", False),
     "final 사슬", "<b>가장 흔하고 가장 나쁜</b> 꼴"),
    (files(['정산목록 (버전 기록 안에)'], "152px", "파일은 하나, 역사는 안에", True, 0),
     "도구의 버전 기록", "<b>지금 것이 늘 하나</b>다"),
    (files(['정산목록', '정산목록_김철수수정본', '정산목록_복사본'], "152px", "복제본이 갈라졌다", False),
     "복제로 갈라짐", "누가 무엇을 고쳤는지 <b>합칠 수 없다</b>"),
    (files(['11-14 승인 전 (마일스톤)'], "152px", "돌아올 지점을 이름으로 박아 둔다", True, 0),
     "마일스톤", "<b>돌아올 자리</b>를 표시해 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("날짜", "11-14", "<b>언제</b> 바뀌었나"),
    ("바뀐 것", "빈 화면 추가", "<b>무엇이</b> 바뀌었나 — 가장 중요하다"),
    ("지금 것", "하나로 분명하게", "둘 이상이면 <b>이미 틀렸다</b>"),
    ("버전 기록", "도구가 쌓는다", "파일을 <b>복제하지 않는다</b>"),
    ("마일스톤", "돌아올 지점", "'승인 전'처럼 <b>이름을 박아</b> 둔다"),
    ("번호·final", "답을 안 준다", "<b>둘 다 아무것도</b> 알려 주지 않는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>파일을 복제하는 순간 합칠 수 없게 됩니다.</b>
          코드는 갈라져도 합칠 수 있지만, 시안 파일은
          두 사람이 각자 고친 것을 <b>자동으로 합칠 길이 없습니다</b>.
          그래서 복제본이 생기면 결국 누군가 <b>손으로 옮겨 붙이고</b>,
          그 과정에서 반드시 뭔가 빠집니다.
          도구의 버전 기록을 쓰면 <b>파일은 늘 하나</b>이고,
          역사는 그 안에 쌓입니다 — 복제하고 싶어지는 순간이
          대개 <b>따로 갈 이유가 없는 순간</b>입니다.</p>''',
  do=ul([
    "도구의 <b>버전 기록</b>을 쓰기",
    "이름에 <b>무엇이 바뀌었는지</b> 적기",
    "돌아올 지점에 <b>마일스톤</b> 이름 박아 두기",
  ]),
  dont=ul([
    "<code>v1</code>·<code>v2</code> — <b>차이를 모른다</b>",
    "<code>final</code>·<code>진짜final</code> — <b>지금 것을 모른다</b>",
    "파일 복제로 갈라지기 — <b>합칠 수 없다</b>",
    "고친 이유를 안 적기 — 몇 달 뒤 <b>아무도 모른다</b>",
  ]),
  instead='의견을 주고받는 일은 <a href="review.html">디자인 리뷰</a>, 넘기는 일은 <a href="handoff.html">핸드오프</a>, 부품의 역사는 <a href="designsystem.html">디자인 시스템</a>.',
  cases=cases([
    (files(['11-14 빈 화면과 오류 추가'], "150px", "커밋 메시지와 같은 일", True, 0),
     "좋은 이름", "<b>무엇이 바뀌었는지</b>"),
    (files(['11-14 승인 전 (마일스톤)'], "150px", "돌아올 자리", True, 0),
     "마일스톤", "승인·배포 직전에 박는다"),
    (files(['정산목록_진짜final_수정_v2'], "150px", "실제로 자주 본다", False),
     "흔한 사고", "<b>이름만으로는</b> 아무것도 모른다"),
  ]),
  s8_title="적어 두는 법", s8_hint="이 역사의 계약서",
  code_lede="이름에 <b>무엇이 바뀌었는지</b>를 적습니다 — 커밋 메시지와 같습니다.",
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
  keys=kbd([
    ("무엇이 바뀌었는지", "번호가 아니라 <b>내용</b>을 적는다"),
    ("복제하지 않는다", "시안 파일은 <b>합칠 수 없다</b>"),
    ("마일스톤", "승인·배포 직전에 <b>이름을 박아</b> 둔다"),
    ("누가", "두 사람 이상이 만지면 <b>누가 고쳤는지</b>가 필요하다"),
    ("쓰는 쪽에 알린다", "부품을 고치면 <b>쓰는 화면이 전부</b> 바뀐다 — <a href=\"designsystem.html\">디자인 시스템</a>"),
    ("링크를 공유한다", "파일을 보내면 <b>그 순간에 멈춘 사본</b>이 돌아다닌다"),
  ]),
  backend=rows([
    ("시안 링크를 티켓에 붙인다", "파일을 보내지 말고 <b>링크</b>를 답니다. 고치면 링크가 따라 바뀝니다."),
    ("부품 버전", "디자인 시스템 부품을 고치면 <b>쓰는 쪽이 전부</b> 바뀝니다. 무엇이 바뀌는지 적어 배포합니다."),
    ("토큰도 역사가 있다", "색을 바꾸면 그 이유를 적어 둬야 <b>나중에 되돌릴지</b> 판단할 수 있습니다."),
  ]),
  plat_lede="<b>도구가 거들지만 이름은 사람이</b> 짓습니다.",
  plats=plats([
    ("웹", "git 과 같은 생각",
     files(['11-14 빈 화면 추가'], "110px", "", True, 0),
     "커밋 메시지와 <b>정확히 같은 일</b>입니다. 무엇이 바뀌었는지를 적습니다."),
    ("iOS", "같은 문제",
     '''              <div class="phone" role="img" aria-label="버전 기록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">버전 기록</div></div></div>''',
     "에셋·시안 모두 같습니다. <b>복제본</b>이 생기는 순간 어긋나기 시작합니다."),
    ("안드로이드", "같은 문제",
     '''              <div class="phone" role="img" aria-label="버전 기록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">버전 기록</div></div></div>''',
     "역시 같습니다. 기기 폭이 많아 <b>시안 수가 늘어나</b> 더 잘 어긋납니다."),
  ]),
  plat_note="<b>final 사슬</b>은 농담처럼 쓰이지만 실제로 돈이 드는 문제입니다 — 개발자가 옛 시안을 보고 만들면 그대로 다시 작업이고, 그 왕복은 이름 한 줄로 막을 수 있었던 것입니다. 도구의 버전 기록을 쓰고 <b>무엇이 바뀌었는지</b>를 적는 습관 하나면 대부분 사라집니다.",
  siblings=siblings("versioning"),
  related='''        <li><a href="review.html"><b>디자인 리뷰</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="component.html"><b>컴포넌트와 인스턴스</b><em>15부</em></a></li>''',
)
