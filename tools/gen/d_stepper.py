# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 누르면 다른 곳으로 옮겨 갑니다. 아래 네 가지로 서로 가릅니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">번호나 ✓로 끝났는지 한눈에 보임</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">지금 단계는 색과 aria-current="step"</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">단계 이름은 <b>잘리면 안 됨</b></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">적은 값을 '모란상회'처럼 요약</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">끝낸 단계는 <b>눌러서 되돌아감</b></div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">좁으면 가로 배치가 깨지므로 세로로</div>
                </div>
              </div>'''

D = dict(
  slug="stepper", ko="스테퍼", en="Stepper · wizard",
  desc="여러 단계로 나뉜 흐름에서 어디까지 왔는지 알려 주는 스테퍼를, 되돌아가기와 좁은 화면 처리까지 함께 다루는 항목입니다.",
  lede="스테퍼는 긴 입력 과정을 <b>몇 단계로 나누고</b>, 지금 몇 번째 단계인지와 <b>얼마나 남았는지</b>를 함께 보여 줍니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계 이름은 <b>잘리면 안 됩니다</b>. 데모는 칸마다 이름 글자 전체의 폭과 실제로 보이는 폭을 비교해서
          이름이 잘린 단계가 몇 개인지 셉니다. 가로 배치 그대로 폭을 줄이면 단계 이름부터 잘리고,
          '좁으면 세로로 늘어놓기'를 켜면 같은 폭에서도 이름이 잘리지 않습니다.<br>
          <b>끝낸 단계는 눌러서 되돌아갈 수 있어야</b> 합니다. 이 기능을 끄면 끝낸 단계를 눌러도 이동하지 않는데,
          그러면 배송지를 잘못 적은 사용자가 처음부터 다시 해야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스테퍼, 단계 표시, 진행 단계, 위저드"),
    ("영어", "stepper, wizard, progress steps, multi-step form"),
    ("같이 쓰는 말",
     "앞 단계를 끝내야만 다음 단계로 갈 수 있는 것은 <b>선형</b>(linear), "
     "아무 단계나 오갈 수 있는 것은 <b>비선형</b>(non-linear)이라고 합니다. "
     "한 화면에 한 단계씩 보여 주는 긴 흐름은 <b>위저드</b>라고 부릅니다. "
     "Material에는 <b>Stepper</b>라는 부품이 있고, iOS에는 정해진 부품이 없어서 <b>페이지 컨트롤</b>이나 화면 전환으로 단계를 보여 줍니다."),
    ("자주 잘못 부르는 이름",
     "<b>프로그레스 바</b> — <a href=\"progress.html\">프로그레스 바</a>는 <b>기계가 하는 일</b>이 얼마나 진행됐는지 보여 주고, 스테퍼는 <b>사람이 해야 할 일</b>의 차례를 보여 줍니다.<br>"
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 <b>순서 없이</b> 내용 묶음을 바꿔 보여 주는 부품이고, 스테퍼는 정해진 순서대로 나아갑니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 <b>계층</b>을 보여 주고, 스테퍼는 <b>차례</b>를 보여 줍니다."),
  ]),
  axes=ax("스테퍼"),
  oneline="단계가 <b>셋을 넘으면 정말 그만큼 나눠야 하는지 다시 따져 봅니다.</b> 단계를 늘리기 전에 한 화면에 담을 수 있는지부터 확인합니다.",
  states=states([
    (steps([("장바구니", "done"), ("배송지", "now"), ("결제", ""), ("확인", "")], "152px", "1단계 끝, 2단계 진행 중", True),
     "단계를 진행하는 중", "끝난 단계와 <b>지금 단계</b>가 다르게 보입니다"),
    (steps([("장바구니", "done"), ("배송지", "done"), ("결제", "done"), ("확인", "done")], "152px", "모두 끝남", True),
     "모든 단계를 마쳤을 때", "모든 단계를 마치면 <b>결과 화면</b>으로 넘어갑니다"),
    (steps([("장바구니…", "done"), ("배…", "now"), ("결…", ""), ("확…", "")], "152px", "이름이 잘림", False),
     "좁은 화면에 가로로 둘 때", "화면이 좁아지면 <b>가로 배치에서 단계 이름부터</b> 잘립니다"),
    (steps([("장바구니 확인", "done"), ("배송지 입력", "now"), ("결제 수단", "")], "152px", "세로로 두면 이름이 다 보임", True, True),
     "단계를 세로로 늘어놓을 때", "폰에서는 <b>단계를 세로로 늘어놓는 편</b>이 낫습니다"),
    (one(txt('<span style="display:block;font-size:9px;color:var(--danger)">배송지를 다시 적어 주세요</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:3px">2단계로 돌아가도 적은 값은 그대로</span>'),
         "되돌아가기", True, "", "152px"),
     "앞 단계로 되돌아갈 때", "앞 단계로 돌아가도 <b>이미 적은 값은 지우지 않습니다</b>"),
    (steps([("장바구니", "done"), ("배송지", ""), ("결제", ""), ("확인", "")], "152px", "지금 단계를 알 수 없음", False),
     "지금 단계를 알리지 않을 때", "지금 단계를 <b>색만</b>으로 표시하면 알아보기 어렵습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("번호 · ✓", "끝났는지 표시", "단계 번호를 보면 <b>몇 단계가 남았는지</b> 알 수 있습니다"),
    ("지금 단계", "색 + <code>aria-current</code>", "스크린 리더 사용자도 알 수 있도록 <b>소리로도</b> 전해져야 합니다"),
    ("단계 이름", "잘리면 안 됨", "자리가 모자라면 <b>이름을 짧게</b> 고칩니다"),
    ("적은 값", "요약", "앞 단계에서 적은 값을 보여 줘서 되돌아갈지 판단할 수 있게 합니다"),
    ("되돌아가기", "끝낸 단계로만", "아직 안 간 뒤 단계로는 <b>건너뛰지 못하게</b> 막습니다"),
    ("좁은 화면", "세로로 배치", "가로 스테퍼는 <b>390px 폭에서 이름이 잘리고 배치가 깨집니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스테퍼를 붙이기 전에 먼저 <b>정말 단계를 나눠야 하는지</b> 따져 봐야 합니다.
          입력 칸이 여덟 개인 폼을 네 단계로 나누면 화면은 깔끔해지지만 <b>끝까지 마치는 사람은 줄어듭니다</b>.
          단계를 넘어갈 때마다 사용자가 그만둘 기회가 한 번씩 더 생기기 때문입니다.<br>
          나눠야 한다면 <b>하는 일의 성격에 따라</b> 나눕니다. 예를 들어 '배송지'와 '결제 수단'은 서로 다른 일이라 나눌 만하지만,
          '이름'과 '전화번호'를 다른 단계로 나누면 단계 수만 늘어납니다.</p>''',
  do=ul([
    "단계를 <b>세 개에서 다섯 개</b> 사이로 둘 때",
    "끝낸 단계는 <b>눌러서 되돌아갈</b> 수 있게 할 때",
    "폰에서는 <b>세로</b>로 바꾸거나 '2/4' 같은 글로 줄일 때",
  ]),
  dont=ul([
    "아직 안 간 단계로 <b>건너뛰게</b> 둘 때. 뒤 단계는 앞 단계에서 적은 값을 바탕으로 진행됩니다",
    "되돌아갈 때 <b>이미 적은 값을 지울</b> 때. 사용자가 같은 내용을 다시 적어야 해서 가장 크게 불만을 느끼는 부분입니다",
    "단계 이름을 '1단계 · 2단계'로 둘 때. 이름에는 그 단계에서 <b>무엇을 하는지</b>를 적습니다",
    "지금 단계를 <b>색으로만</b> 알릴 때",
  ]),
  instead='기계가 하는 일이 얼마나 진행됐는지 보여 주려면 <a href="progress.html">프로그레스 바</a>를 쓰고, 순서 없이 내용 묶음을 바꿔 보여 주려면 <a href="tabs.html">탭</a>을 씁니다. 계층을 보여 주는 데는 <a href="breadcrumb.html">브레드크럼</a>이 맞고, 흐름 전체를 어떻게 짤지는 <a href="checkout.html">결제 흐름</a> 항목에서 다룹니다.',
  cases=cases([
    (steps([("장바구니", "done"), ("배송지", "now"), ("결제", ""), ("확인", "")], "150px", "", True),
     "결제 단계 보여 주기", "스테퍼를 가장 흔하게 쓰는 곳입니다"),
    (steps([("계정", "done"), ("사업자", "now"), ("정산 계좌", "")], "150px", "", True),
     "가입과 심사 서류 나눠 받기", "적어 내야 할 서류가 여러 장일 때 씁니다"),
    (one(txt('<span style="display:block;font-size:9px">2 / 4 단계</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:2px">배송지 입력</span>'),
         "글 한 줄로 줄임", True, "폰에서 쓰는 가장 작은 형태", "150px"),
     "폰에서 글 한 줄로 줄이기", "단계 띠 대신 <b>글 한 줄</b>로 보여 줘도 충분합니다"),
  ]),
  code_lede="단계는 순서가 있는 목록이므로 <code>&lt;ol&gt;</code>로 적고, 지금 단계에만 <code>aria-current</code>를 달아 알립니다.",
  code='''&lt;<span class="t">ol</span> <span class="a">class</span>=<span class="s">"stepper"</span>&gt;
  &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#cart"</span>&gt;&lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✓&lt;/<span class="t">span</span>&gt; 장바구니 확인&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;배송지 입력&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span>&gt;결제 수단&lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span>&gt;주문 확인&lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ol</span>&gt;

<span class="c">/* 이름이 잘리는 것보다 세로로 늘어놓는 편이 낫다 */</span>
@media (max-width: <span class="a">480px</span>) {
  .stepper { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">6px</span>; }
}''',
  keys=kbd([
    ("Tab", "끝낸 단계의 링크만 포커스를 받고, <b>아직 안 간 단계는 포커스를 받지 않습니다</b>"),
    ("Enter", "포커스가 있는 단계로 돌아갑니다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계에 답니다. 한 페이지에 <b>하나만</b> 있어야 합니다"),
    ("<code>&lt;ol&gt;</code>", "단계에 순서가 있다는 정보가 스크린 리더에서 <b>소리로</b> 전해집니다"),
    ("<code>aria-disabled</code>", "아직 갈 수 없는 단계에 붙입니다. 포커스는 받지만 눌러도 <b>이동하지 않습니다</b>"),
    ("제대로 됐는지 확인하는 방법", "<kbd>Tab</kbd>으로 단계를 돌면서 <b>아직 안 간 단계가 포커스를 받는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("단계마다 임시 저장하기", "입력 내용을 마지막 단계에서 한 번에 보내면 <b>중간에 연결이 끊기거나 창을 닫았을 때</b> 적은 내용이 모두 사라집니다. 단계마다 임시 저장해 두면 사용자가 나중에 돌아와 이어서 할 수 있습니다."),
    ("초안 id로 단계 잇기", "첫 단계에서 <code>draft_id</code>를 받아 두고, 이후 단계에서는 그 초안에 값을 채워 넣습니다."),
    ("단계마다 입력 검증하기", "단계마다 그 단계의 입력 칸만 검사해서 결과를 돌려줍니다. 마지막에 모든 오류를 한꺼번에 돌려주면 사용자는 <b>어느 단계로 돌아가야 하는지</b> 알 수 없습니다."),
  ]),
  plat_lede="웹과 안드로이드에서는 <b>스테퍼를 쓰지만</b>, iOS에는 스테퍼 부품이 없습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     steps([("장바구니", "done"), ("배송지", "now"), ("결제", "")], "110px", "", True),
     "정해진 부품이 없어서 <code>&lt;ol&gt;</code>에 <code>aria-current</code>를 붙여 직접 만듭니다."),
    ("iOS", "부품 없이 화면 전환",
     '''              <div class="phone" role="img" aria-label="iOS 단계 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;font-size:5px;color:var(--fg-muted);text-align:center">2 / 4</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:9px;border-radius:3px;background:var(--accent-soft)"></div></div></div>''',
     "스테퍼 부품이 없습니다. HIG에 맞는 방식은 단계마다 화면을 <b>넘기고</b> 제목에 '2/4'처럼 적는 것입니다."),
    ("안드로이드", "Stepper",
     '''              <div class="phone" role="img" aria-label="안드로이드 스테퍼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;display:flex;gap:4px;align-items:center">
                  <span style="width:9px;height:9px;border-radius:999px;background:var(--accent)"></span>
                  <span style="width:9px;height:9px;border-radius:999px;border:1.2px solid var(--accent)"></span>
                  <span style="width:9px;height:9px;border-radius:999px;border:1px solid var(--line)"></span></div></div></div>''',
     "Material에는 <b>가로 스테퍼와 세로 스테퍼</b>가 정식 부품으로 있습니다. 세로 스테퍼는 단계 아래에 그 단계의 내용까지 펼쳐 보여 줍니다."),
  ]),
  plat_note="iOS에 스테퍼가 없는 것은 빠뜨려서가 아니라 <b>일부러 그렇게 정했기</b> 때문입니다. 단계 띠에 화면 자리를 쓰는 대신 화면을 넘기고 제목 한 줄로 단계를 알리는 방식인데, 좁은 화면에서는 이 방식이 대체로 낫습니다. 그래서 웹에서도 폰 폭에서는 단계 띠를 접고 <b>'2 / 4 단계'</b> 한 줄로 줄이는 것이 안전합니다. 안드로이드의 <b>세로 스테퍼</b>는 단계 아래에 그 단계의 내용까지 펼쳐 두는 형태라서 긴 서식에 쓰기 좋습니다.",
  siblings=siblings("stepper"),
  related='''        <li><a href="progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="checkout.html"><b>결제 흐름</b><em>13부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>''',
)
