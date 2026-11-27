# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 '누르면 어디론가 간다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

def steps(marks, w="152px", note="", ok=None, col=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    cells = []
    for n, state in marks:
        if state == 'done':
            dot = ('<span style="display:grid;place-items:center;width:17px;height:17px;border-radius:999px;'
                   'background:var(--accent);color:#fff;font-size:8px">✓</span>')
            col_t = 'var(--accent)'
        elif state == 'now':
            dot = ('<span style="display:grid;place-items:center;width:17px;height:17px;border-radius:999px;'
                   'border:2px solid var(--accent);color:var(--accent);font-size:8px;font-weight:700">●</span>')
            col_t = 'var(--accent)'
        else:
            dot = ('<span style="display:grid;place-items:center;width:17px;height:17px;border-radius:999px;'
                   'border:1px solid var(--line);color:var(--fg-muted);font-size:8px">·</span>')
            col_t = 'var(--fg-muted)'
        if col:
            cells.append('<span style="display:flex;align-items:center;gap:5px">' + dot +
                         '<span style="font-size:8.5px;color:' + col_t + '">' + n + '</span></span>')
        else:
            cells.append('<span style="display:grid;gap:3px;justify-items:center;min-width:0;flex:1 1 0">' + dot +
                         '<span style="font-size:7.5px;color:' + col_t + ';white-space:nowrap;overflow:hidden;'
                         'text-overflow:ellipsis;max-width:100%">' + n + '</span></span>')
    lay = ('display:grid;gap:5px' if col else 'display:flex;gap:4px;align-items:flex-start')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="' + lay + ';border:1px solid ' + c + ';border-radius:6px;background:var(--surface);padding:6px">'
            + ''.join(cells) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">번호 또는 ✓ — 끝났는지 한눈에</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">지금 단계 — 색 + aria-current="step"</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">단계 이름 — <b>잘리면 안 된다</b></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">적은 값 요약 — '모란상회'</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">끝낸 단계는 <b>눌러서 되돌아간다</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">좁으면 가로가 먼저 무너진다 — 세로로</div>
                </div>
              </div>'''

D = dict(
  slug="stepper", ko="스테퍼", en="Stepper · wizard",
  desc="여러 단계로 나뉜 흐름에서 어디까지 왔는지 보여 주는 길 안내. 되돌아가기와 좁은 화면 처리.",
  lede="긴 입력을 <b>몇 토막으로 나누고</b>, 지금 어디인지와 <b>얼마나 남았는지</b>를 같이 보여 줍니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계 이름은 <b>잘리면 안 됩니다</b> — 데모가 칸마다 담긴 폭과 보이는 폭을 견줘
          잘린 개수를 셉니다. 가로로 둔 채 폭을 줄이면 이름이 먼저 무너지고,
          '좁으면 세로로'를 켜면 같은 폭에서도 온전합니다.<br>
          <b>끝낸 단계는 눌러서 되돌아갈 수 있어야</b> 합니다. 끄면 눌러도 안 갑니다 —
          '배송지를 잘못 적었는데 처음부터 다시'가 벌어지는 자리입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스테퍼, 단계 표시, 진행 단계, 위저드"),
    ("영어", "stepper, wizard, progress steps, multi-step form"),
    ("같이 쓰는 말",
     "앞 단계를 끝내야만 다음으로 가는 것이 <b>선형</b>(linear), "
     "아무 단계나 오갈 수 있는 것이 <b>비선형</b>(non-linear)입니다. "
     "한 화면에 한 단계씩 보여 주는 긴 흐름을 <b>위저드</b>라 부르고, "
     "Material 은 <b>Stepper</b>, iOS 는 정해진 부품 없이 <b>페이지 컨트롤</b>이나 화면 전환으로 풉니다."),
    ("자주 잘못 부름",
     "<b>프로그레스 바</b> — <a href=\"progress.html\">프로그레스 바</a>는 <b>기계가 하는 일</b>의 진척이고, 스테퍼는 <b>사람이 하는 일</b>의 차례입니다.<br>"
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 <b>순서가 없는</b> 묶음 전환입니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 <b>계층</b>이고 스테퍼는 <b>차례</b>입니다."),
  ]),
  axes=ax("스테퍼"),
  oneline="<b>세 단계를 넘기면 의심하세요.</b> 단계를 늘리는 대신 한 화면에 담을 수 있는지 먼저 봅니다.",
  states=states([
    (steps([("장바구니", "done"), ("배송지", "now"), ("결제", ""), ("확인", "")], "152px", "1단계 끝, 2단계 중", True),
     "진행 중", "끝난 것과 <b>지금</b>이 다르게 보인다"),
    (steps([("장바구니", "done"), ("배송지", "done"), ("결제", "done"), ("확인", "done")], "152px", "다 끝났다", True),
     "완료", "마지막은 <b>결과 화면</b>으로 넘긴다"),
    (steps([("장바구니…", "done"), ("배…", "now"), ("결…", ""), ("확…", "")], "152px", "이름이 잘렸다", False),
     "좁은 화면", "<b>가로가 먼저</b> 무너진다"),
    (steps([("장바구니 확인", "done"), ("배송지 입력", "now"), ("결제 수단", "")], "152px", "세로로 두면 온전하다", True, True),
     "세로로", "폰에서는 <b>이 꼴</b>이 낫다"),
    (one(txt('<span style="display:block;font-size:9px;color:var(--danger)">배송지를 다시 적어 주세요</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:3px">2단계로 돌아감 · 적은 값은 그대로</span>'),
         "되돌아가기", True, "", "152px"),
     "되돌아가기", "<b>적은 값은 지우지 않는다</b>"),
    (steps([("장바구니", "done"), ("배송지", ""), ("결제", ""), ("확인", "")], "152px", "지금이 어디인지 모른다", False),
     "지금을 안 알림", "<b>색만</b>으로는 부족하다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("번호 · ✓", "끝났는지", "숫자가 <b>남은 양</b>을 말해 준다"),
    ("지금 단계", "색 + <code>aria-current</code>", "<b>소리로도</b> 들려야 한다"),
    ("단계 이름", "잘리면 안 됨", "줄이려면 <b>이름을 짧게</b>"),
    ("적은 값", "요약", "되돌아갈지 판단하게 한다"),
    ("되돌아가기", "끝낸 단계만", "앞 단계는 <b>못 가게</b> 막는다"),
    ("좁은 화면", "세로로", "가로 스테퍼는 <b>390px 에서 깨진다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스테퍼를 붙이기 전에 물어볼 것이 하나 있습니다 —
          <b>정말 나눠야 하나</b>입니다. 칸이 여덟 개인 폼을 네 단계로 쪼개면
          화면은 깔끔해지지만 <b>끝내는 사람은 줄어듭니다</b>.
          단계마다 사람이 그만둘 기회가 한 번씩 더 생기기 때문입니다.<br>
          나눠야 한다면 <b>뜻으로</b> 나눕니다 — '배송지'와 '결제 수단'은 서로 다른 일이라 나눌 만하고,
          '이름'과 '전화번호'를 나누는 것은 숫자만 늘립니다.</p>''',
  do=ul([
    "단계를 <b>세 개에서 다섯 개</b> 사이로 두기",
    "끝낸 단계는 <b>눌러서 되돌아갈</b> 수 있게 하기",
    "폰에서는 <b>세로</b>로 바꾸거나 '2/4' 같은 글로 줄이기",
  ]),
  dont=ul([
    "앞으로 <b>건너뛰게</b> 두기 — 뒤 단계가 앞 값에 기대고 있다",
    "되돌아가면 <b>적은 값을 지우기</b> — 가장 화나는 자리다",
    "단계 이름을 '1단계 · 2단계'로 두기 — <b>무엇을 하는지</b>를 적는다",
    "지금 단계를 <b>색으로만</b> 알리기",
  ]),
  instead='기계가 하는 일의 진척은 <a href="progress.html">프로그레스 바</a>, 순서 없는 묶음은 <a href="tabs.html">탭</a>, 계층은 <a href="breadcrumb.html">브레드크럼</a>, 흐름 전체 설계는 <a href="checkout.html">결제 흐름</a>.',
  cases=cases([
    (steps([("장바구니", "done"), ("배송지", "now"), ("결제", ""), ("확인", "")], "150px", "", True),
     "결제 흐름", "가장 흔한 자리"),
    (steps([("계정", "done"), ("사업자", "now"), ("정산 계좌", "")], "150px", "", True),
     "가입 · 심사", "서류가 여러 장일 때"),
    (one(txt('<span style="display:block;font-size:9px">2 / 4 단계</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:2px">배송지 입력</span>'),
         "글로 줄임", True, "폰에서 쓰는 가장 작은 꼴", "150px"),
     "폰", "<b>글 한 줄</b>이면 충분하다"),
  ]),
  code_lede="순서가 있는 목록이니 <code>&lt;ol&gt;</code>로 적고, 지금 단계만 <code>aria-current</code>로 알립니다.",
  code='''&lt;<span class="t">ol</span> <span class="a">class</span>=<span class="s">"stepper"</span>&gt;
  &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#cart"</span>&gt;&lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✓&lt;/<span class="t">span</span>&gt; 장바구니 확인&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;배송지 입력&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span>&gt;결제 수단&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span>&gt;주문 확인&lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ol</span>&gt;

<span class="c">/* 이름이 잘릴 바에는 줄을 바꾸는 게 낫다 */</span>
@media (max-width: <span class="a">480px</span>) {
  .stepper { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">6px</span>; }
}''',
  keys=kbd([
    ("Tab", "끝낸 단계의 링크만 받는다. <b>안 간 단계는 초점을 안 준다</b>"),
    ("Enter", "그 단계로 돌아간다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계. 페이지에 <b>하나만</b>"),
    ("<code>&lt;ol&gt;</code>", "순서가 있다는 뜻이 <b>소리로</b> 전해진다"),
    ("<code>aria-disabled</code>", "아직 못 가는 단계에 붙인다 — 초점은 받되 <b>안 간다</b>"),
    ("확인하는 법", "Tab 으로 돌며 <b>안 간 단계가 초점을 받는지</b> 본다"),
  ]),
  backend=rows([
    ("단계마다 저장", "마지막 단계에서 한 번에 보내면 <b>중간에 끊길 때</b> 전부 날아갑니다. 단계마다 임시 저장을 두면 돌아와서 이어 할 수 있습니다."),
    ("초안 id", "첫 단계에서 <code>draft_id</code> 를 받아 두고 이후 단계가 그것을 채웁니다."),
    ("검증은 단계마다", "그 단계의 칸만 검사해 돌려줍니다 — 마지막에 한꺼번에 돌려주면 <b>어디로 돌아가야 하는지</b> 모릅니다."),
  ]),
  plat_lede="웹과 안드로이드에 <b>부품이 있고</b>, iOS 에는 없습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     steps([("장바구니", "done"), ("배송지", "now"), ("결제", "")], "110px", "", True),
     "정해진 부품이 없습니다. <code>&lt;ol&gt;</code> 에 <code>aria-current</code> 를 붙여 만듭니다."),
    ("iOS", "없다 — 화면 전환",
     '''              <div class="phone" role="img" aria-label="iOS 단계 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;font-size:5px;color:var(--fg-muted);text-align:center">2 / 4</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:9px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "스테퍼 부품이 없습니다. 화면을 <b>밀어 넘기고</b> 제목에 '2/4' 를 적는 쪽이 HIG 의 길입니다."),
    ("안드로이드", "Stepper",
     '''              <div class="phone" role="img" aria-label="안드로이드 스테퍼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;display:flex;gap:4px;align-items:center">
                  <span style="width:9px;height:9px;border-radius:999px;background:var(--accent)"></span>
                  <span style="width:9px;height:9px;border-radius:999px;border:1.2px solid var(--accent)"></span>
                  <span style="width:9px;height:9px;border-radius:999px;border:1px solid var(--line)"></span></div></div></div>''',
     "Material 에 <b>가로·세로 스테퍼</b>가 정식으로 있습니다. 세로 쪽이 내용까지 품습니다."),
  ]),
  plat_note="iOS 에 스테퍼가 없는 것은 빠뜨린 게 아니라 <b>고른 것</b>입니다 — 단계 띠에 자리를 내주느니 화면을 넘기고 제목 한 줄로 알리자는 쪽입니다. 좁은 화면에서는 그 판단이 대체로 맞습니다. 웹에서도 폰 폭에서는 띠를 접고 <b>'2 / 4 단계'</b> 한 줄로 줄이는 것이 안전합니다. 안드로이드의 <b>세로 스테퍼</b>는 단계 아래에 그 단계의 내용까지 펼쳐 두는 꼴이라, 긴 서식에 쓸 만합니다.",
  siblings=siblings("stepper"),
  related='''        <li><a href="progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="checkout.html"><b>결제 흐름</b><em>13부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>''',
)
