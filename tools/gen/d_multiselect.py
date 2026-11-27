# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ms(tokens, more=0, label="", note="", ok=None, w="152px", count=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if count is not None:
        inner = '<span style="font-size:8px;color:var(--fg-muted)">' + count + '</span>'
    else:
        inner = ''.join('<span style="display:inline-flex;gap:3px;align-items:center;border:1px solid var(--accent);'
                        'background:var(--accent-soft);color:var(--accent);border-radius:999px;'
                        'padding:1px 4px 1px 7px;font-size:7.5px">' + t
                        + '<span style="opacity:.6">✕</span></span>' for t in tokens)
        if more:
            inner += '<span style="font-size:7.5px;color:var(--fg-muted)">+' + str(more) + '</span>'
        if not tokens and not more:
            inner = '<span style="font-size:7.5px;color:var(--fg-faint)">아직 안 골랐습니다</span>'
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:flex;gap:3px;flex-wrap:wrap;align-items:center;border:1px solid ' + c + ';'
            'border-radius:4px;background:var(--surface);padding:4px 5px;min-height:22px">' + inner + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">고른 것 — 알약으로 보이면 무엇인지 안다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">+N — 넘치면 접어 높이를 지킨다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">목록 — 체크박스가 가장 분명하다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">기본 multiple 셀렉트는 Ctrl 을 눌러야 한다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">숫자만 보이면 높이는 고정이지만 이름을 모른다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">많으면 검색 칸을 붙인다</div>
                </div>
              </div>'''

D = dict(
  slug="multiselect", ko="여러 개 고르기", en="Multi-select",
  desc="여러 값을 고르는 부품에서 고른 것을 보여 주는 세 가지 방법과 브라우저 기본 multiple 셀렉트의 한계를 다루는 항목입니다.",
  lede="여러 개 고르기에서는 고르는 동작보다 <b>고른 것을 보여 주는 방법</b>이 더 어렵습니다. 고른 것을 알약으로 늘어놓으면 칸이 점점 길어지고, 개수만 숫자로 보여 주면 무엇을 골랐는지 알 수 없기 때문입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>고른 것을 알약으로 늘어놓으면 <b>무엇을 골랐는지</b> 한눈에 보이지만 줄 수가 늘어납니다.
          데모가 <b>고른 것 칸의 높이</b>를 재서 적어 주니 확인해 보세요.<br>
          '<b>최대 보일 알약</b>'을 줄이면 넘치는 알약이 <code>+N</code>으로 접힙니다.
          개수만 숫자로 보여 주면 높이는 변하지 않지만 <b>무엇을 골랐는지 알 수 없습니다</b>.<br>
          브라우저 기본 <code>multiple</code> 셀렉트는 <b>Ctrl을 누른 채</b> 눌러야 여러 개가 골라지기 때문에,
          체크박스 목록으로 만드는 편이 훨씬 알아보기 쉽습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "여러 개 고르기, 다중 선택, 멀티 셀렉트"),
    ("영어", "multi-select, multiple selection, token input"),
    ("같이 쓰는 말",
     "고른 것이 알약으로 쌓이는 꼴은 <b>토큰 입력</b>(token input), "
     "글자를 쳐서 목록을 걸러 가며 고르는 꼴은 <b>멀티 콤보박스</b>라고 부릅니다. "
     "넘치는 알약을 <code>+N</code>으로 접는 것은 <b>오버플로 카운트</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>체크박스</b> — <a href=\"checkbox.html\">체크박스</a>는 고를 수 있는 항목이 처음부터 <b>모두 보이는</b> 부품입니다.<br>"
     "<b>콤보박스</b> — <a href=\"combobox.html\">콤보박스</a>는 <b>하나</b>만 고릅니다.<br>"
     "<b>태그</b> — <a href=\"tag.html\">태그</a>는 고르는 부품이 아니라 값을 <b>보여 주는</b> 부품입니다."),
  ]),
  axes=ax("여러 개 고르기"),
  oneline="<b>무엇을 골랐는지 보이게 하세요.</b> 개수만 보여 주면 사용자는 고른 것을 확인하려고 목록을 다시 열어야 합니다.",
  states=states([
    (ms(["모란상회", "한빛아웃도어"], 0, "", "둘을 골랐다", True), "조금", "고른 것의 <b>이름이</b> 모두 보입니다"),
    (ms(["모란상회", "한빛아웃도어", "새벽상사"], 5, "", "넘치면 +N 으로", True), "많이", "넘치는 것은 <b>+N</b>으로 접습니다"),
    (ms([], 0, "", "숫자만 — 무엇인지 모른다", False, "152px", "8곳 골랐습니다"),
     "숫자만", "무엇을 골랐는지 보려면 목록을 <b>다시 열어</b> 봐야 합니다"),
    (ms([], 0, "", "아직 안 골랐다", None), "빈 상태", "아직 고른 것이 없으면 <b>무엇을 고르는 칸인지</b> 적어 둡니다"),
    (one(txt('<span style="display:block;font-size:8px">⌃ Ctrl + 클릭</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">모르는 사람이 많다</span>'),
         "기본 셀렉트", False, "", "152px"),
     "<code>multiple</code>", "여러 개를 고르려면 <b>Ctrl을 누른 채</b> 눌러야 합니다"),
    (one(txt('<span style="display:block;font-size:8px">🔍 모란</span>'
             '<span style="display:block;font-size:7.5px;color:var(--fg-muted);margin-top:2px">☑ 모란상회</span>'
             '<span style="display:block;font-size:7.5px;color:var(--fg-muted)">☐ 모란상회 2호점</span>'),
         "많을 때", True, "검색 칸을 붙인다", "152px"),
     "항목이 많음", "목록 위에 <b>검색</b> 칸을 붙입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("고른 것", "알약으로", "고른 것이 <b>무엇인지</b> 이름으로 보입니다"),
    ("<code>+N</code>", "넘치면 접기", "넘치는 알약을 접어 칸 높이가 늘어나지 않게 합니다"),
    ("목록", "체크박스", "무엇이 골라졌는지 가장 <b>분명하게</b> 보입니다"),
    ("<code>multiple</code>", "Ctrl 필요", "Ctrl을 눌러야 한다는 것을 <b>모르는 사람</b>이 많습니다"),
    ("숫자만", "높이 고정", "칸 높이는 일정하지만 고른 것의 <b>이름을 알 수 없습니다</b>"),
    ("검색", "많을 때", "항목이 스무 개를 넘으면 검색 칸을 붙입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          브라우저 기본 <code>&lt;select multiple&gt;</code>은 실제 화면에서 <b>거의 쓰이지 않습니다</b>.
          Ctrl(⌘)을 누른 채 눌러야 여러 개가 골라지는데,
          이 방법을 아는 사람이 적고 화면 <b>어디에도 안내가 없기</b> 때문입니다.
          게다가 Ctrl 없이 한 항목을 그냥 누르면 <b>이미 고른 것이 모두 풀립니다</b>.<br>
          그래서 체크박스 목록이나 토큰 입력으로 만드는 편이 낫고,
          항목이 스무 개를 넘으면 <b>검색 칸</b>을 붙입니다.
          고른 것을 목록 위에 알약으로 쌓아 두면
          <b>목록을 열지 않고도</b> 무엇을 골랐는지 알 수 있습니다.</p>''',
  do=ul([
    "고른 것을 <b>알약으로</b> 보여 주기",
    "알약이 넘치면 <b><code>+N</code></b>으로 접기",
    "항목이 스무 개를 넘으면 <b>검색 칸</b> 붙이기",
  ]),
  dont=ul([
    "<code>&lt;select multiple&gt;</code>을 그대로 쓰기. 사용자 대부분이 <b>Ctrl을 눌러야 한다는 것을 모릅니다</b>",
    "개수를 <b>숫자로만</b> 보여 주기. 고른 것을 확인하려고 목록을 다시 열어야 합니다",
    "알약을 <b>모두 늘어놓기</b>. 칸이 길어져 화면을 많이 차지합니다",
    "고른 것을 <b>빼는 방법</b>을 주지 않기",
  ]),
  instead='항목을 모두 늘어놓아도 되면 <a href="checkbox.html">체크박스</a>, 하나만 고르면 <a href="combobox.html">콤보박스</a>, 값을 보여 주기만 하면 <a href="tag.html">태그</a>, 조건으로 목록을 거르는 화면은 <a href="filter.html">필터와 패싯</a>.',
  cases=cases([
    (ms(["모란상회", "한빛아웃도어"], 2, "", "", True, "150px"), "가게 고르기", "<b>알약</b>으로 보여 주고 넘치면 <b><code>+N</code></b>으로 접습니다"),
    (ms(["카드", "계좌이체"], 0, "", "", True, "150px"), "결제 수단", "고를 수 있는 항목이 <b>몇 개 안 되어서</b> 알약을 모두 보여 줍니다"),
    (ms([], 0, "", "", True, "150px", "조건 3개"), "필터", "개수만 숫자로 보여 줘도 괜찮은 자리입니다"),
  ]),
  code_lede="체크박스 목록으로 만들면 무엇이 골라졌는지 가장 분명하게 보입니다. 고른 것은 목록 위에 알약으로 쌓습니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;정산에 넣을 가게&lt;/<span class="t">legend</span>&gt;

  &lt;<span class="t">ul</span> <span class="a">class</span>=<span class="s">"tokens"</span> <span class="a">aria-label</span>=<span class="s">"고른 가게"</span>&gt;
    &lt;<span class="t">li</span>&gt;모란상회
      &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-label</span>=<span class="s">"모란상회 빼기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
    &lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ul</span>&gt;

  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">value</span>=<span class="s">"moran"</span> <span class="a">checked</span>&gt; 모란상회&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">value</span>=<span class="s">"hanbit"</span>&gt; 한빛아웃도어&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;''',
  keys=kbd([
    ("Space", "체크박스를 켜고 끕니다"),
    ("Tab", "체크박스 <b>하나하나</b>에 멈추기 때문에, 항목이 많으면 묶음을 접어 둡니다"),
    ("Backspace", "토큰 입력에서는 관습적으로 <b>마지막 알약</b>을 지웁니다"),
    ("<code>&lt;fieldset&gt;</code>", "묶음에 이름을 붙여 스크린 리더가 <b>무엇을 고르는 묶음인지</b> 읽어 줍니다"),
    ("<code>aria-label</code>", "✕ 단추에 <b>무엇을 빼는지</b> 적습니다"),
    ("확인하는 법", "스크린 리더로 들으며 <b>몇 개 골랐는지</b> 알 수 있는지 확인합니다"),
  ]),
  backend=rows([
    ("배열로 받는다", "고른 값은 <code>shops: [\"moran\", \"hanbit\"]</code>처럼 배열로 주고받습니다. 쉼표로 이은 문자열로 보내면 <b>이름에 쉼표</b>가 든 값에서 나누는 자리가 틀어집니다."),
    ("최대 개수", "고를 수 있는 개수에 한도가 있으면 서버가 그 값을 내려 줘야 화면에서 <b>미리 막을 수</b> 있습니다."),
    ("전체 선택", "'조건에 맞는 전부'를 고를 때는 항목 목록 대신 <b>개수만</b> 주고받는 편이 가볍습니다. 자세한 내용은 <a href=\"bulk.html\">일괄 선택</a> 항목에 있습니다."),
  ]),
  plat_lede="여러 개 고르기는 플랫폼이 주는 <b>기본 부품만으로는 부족한</b> 경우가 많습니다.",
  plats=plats([
    ("웹", "select multiple · 직접",
     ms(["모란상회"], 2, "", "", True, "110px"),
     "기본 부품은 쓰기 어려워서 <b>대부분 직접</b> 만듭니다."),
    ("iOS", "목록 + 체크",
     '''              <div class="phone" role="img" aria-label="iOS 여러 개 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;right:7px;top:27px;font-size:5px;color:var(--accent)">✓</div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:8px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "목록의 각 줄 오른쪽에 <b>체크 표시</b>를 두는 꼴이 표준입니다."),
    ("안드로이드", "Chip · 체크박스",
     '''              <div class="phone" role="img" aria-label="안드로이드 여러 개 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:20px;height:8px;border-radius:999px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:28px;top:26px;width:16px;height:8px;border-radius:999px;border:1px solid var(--line)"></div></div></div>''',
     "<b>필터 칩</b>을 늘어놓는 꼴을 많이 쓰는데, 이렇게 하면 고른 것이 바로 보입니다."),
  ]),
  plat_note="안드로이드처럼 <b>필터 칩을 늘어놓는 꼴</b>은 고르는 곳과 고른 결과를 보여 주는 곳이 <b>같은 자리</b>여서 알약을 따로 쌓을 필요가 없습니다. 항목이 열 개 안쪽이면 웹에서도 이 꼴이 가장 간단합니다. 항목이 그보다 많으면 <b>목록과 알약</b>을 함께 쓰는 편이 낫습니다.",
  siblings=siblings("multiselect"),
  related='''        <li><a href="checkbox.html"><b>체크박스</b><em>4부</em></a></li>
        <li><a href="combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><a href="tag.html"><b>태그</b><em>5부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>''',
)
