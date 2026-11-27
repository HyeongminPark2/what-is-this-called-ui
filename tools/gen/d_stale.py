# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

ST = table(
  ["다시 받는 동안", "언제 숫자인지", "틀린 값을 보일 위험", "쓸 만한 자리"],
  [["옛 값을 보임", "<b>읽을 수 있다</b>", "적어야 한다", "있다 — 그래서 적는다", "목록 · 대시보드"],
   ["비우고 스피너", "<b>아무것도 못 읽는다</b>", "필요 없다", "없다", "처음 들어올 때"],
   ["<a href=\"skeleton.html\">스켈레톤</a>", "자리만 보인다", "필요 없다", "없다", "처음 들어올 때"],
   ["옛 값 + 흐리게", "읽을 수 있다", "적어야 한다", "작다 — 바뀌는 중이 보인다", "<b>거의 늘 이쪽</b>"]],
  me="오래된 데이터")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">옛 값을 그대로 둔다 — 빈 화면을 안 만든다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">언제 숫자인지 — '3분 전 기준'</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">다시 받는 중에는 흐리게</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">적지 않으면 방금 값인 줄 안다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">새로 고침 단추 — 사람이 직접 부를 길</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">돈 · 재고처럼 틀리면 안 되는 값은 예외</div>
                </div>
              </div>'''

def val(v, asof, label, note="", ok=None, w="152px", dim=False, blank=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    body = ('<span style="display:grid;place-items:center;min-height:26px;font-size:8px;color:var(--fg-muted)">'
            '불러오는 중…</span>' if blank else
            '<span style="display:block;font-size:15px;font-weight:700;'
            + ('color:var(--fg-muted);opacity:.55;' if dim else '') + '">' + v + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:2px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px 8px">'
            '<span style="font-size:7.5px;color:var(--fg-muted)">이번 주 정산액</span>'
            + body
            + ('<span style="font-size:7.5px;color:' + ('#9a6700' if '전' in asof else 'var(--fg-muted)') + '">' + asof + '</span>' if asof else '')
            + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

D = dict(
  slug="stale", ko="오래된 데이터", en="Stale data",
  desc="다시 받는 동안 옛 값을 그대로 보이는 방식. 언제 숫자인지 적기와 그 한계.",
  lede="다시 받는 동안 <b>화면을 비우면</b> 그동안 아무것도 못 읽습니다. 옛 값을 두되 <b>언제 숫자인지</b>를 적습니다.",
  axes_lede="다시 받는 동안 보여 주는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>비우면 그동안 <b>아무것도 못 읽습니다</b> — 데모가 <b>숫자가 사라져 있던 시간(ms)</b>을
          재서 적습니다. 옛 값을 두면 그 시간이 <b>0</b>입니다.<br>
          대신 옛 값에는 <b>언제 숫자인지</b>를 붙여야 합니다 — '3분 전 기준'이 없으면
          방금 받은 값인 줄 압니다. 체크를 끄고 보면 숫자만 덩그러니 남습니다.<br>
          다시 받는 동안에는 숫자를 <b>흐리게</b> 해 지금 바뀌는 중임을 알립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오래된 데이터, 묵은 값, 캐시된 값"),
    ("영어", "stale data, stale-while-revalidate, cached value"),
    ("같이 쓰는 말",
     "옛 값을 보여 주면서 뒤에서 새로 받아 오는 방식을 <b>stale-while-revalidate</b> 라 부릅니다. "
     "값이 만들어진 시각을 <b>as of</b>(기준 시각), 얼마나 묵었는지를 <b>나이</b>(age)라 하고, "
     "'3분 전 기준' 같은 표시를 <b>신선도 표시</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>캐시</b> — 캐시는 <b>저장하는 장치</b>이고, 이건 <b>보여 주는 방식</b>입니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 <b>앞으로 될 값</b>을 미리 보입니다. 이건 <b>지난 값</b>입니다.<br>"
     "<b>오프라인</b> — <a href=\"offline.html\">오프라인</a>은 <b>연결이 없을 때</b>입니다."),
  ]),
  axes=ST,
  oneline="<b>옛 값이라도 보여 주세요.</b> 대신 언제 숫자인지를 반드시 적습니다.",
  s4_title="상태", s4_hint="빈 화면을 만드는가",
  states=states([
    (val("1,284만", "방금 기준", "", "막 받았다", True), "막 받음", "<b>가장 좋은</b> 상태"),
    (val("1,284만", "3분 전 기준", "", "묵었지만 읽힌다", None), "묵음", "<b>읽을 수 있다</b>"),
    (val("1,284만", "다시 받는 중…", "", "흐리게 — 바뀌는 중", True, "152px", True),
     "다시 받는 중", "<b>옛 값 + 흐리게</b>"),
    (val("", "", "", "그동안 아무것도 못 읽는다", False, "152px", False, True),
     "비우고 스피너", "<b>빈 화면</b>이 된다"),
    (val("1,284만", "", "", "방금 값인 줄 안다", False), "기준 시각 없음", "<b>거짓말이 된다</b>"),
    (val("1,284만", "1시간 전 기준 · 새로 고침 ›", "", "너무 묵으면 권한다", None),
     "너무 묵음", "<b>새로 받으라고</b> 권한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("옛 값", "그대로 둠", "<b>빈 화면</b>을 안 만든다"),
    ("기준 시각", "'3분 전'", "<b>반드시</b> 적는다"),
    ("흐리게", "다시 받는 중", "바뀌는 중임을 알린다"),
    ("안 적으면", "거짓말", "<b>방금 값인 줄</b> 안다"),
    ("새로 고침", "사람이 부를 길", "기다리기 싫을 때"),
    ("예외", "돈 · 재고", "<b>틀리면 안 되는</b> 값"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이 방식에는 분명한 예외가 있습니다 —
          <b>틀린 값을 보이면 안 되는 자리</b>입니다.
          남은 재고, 계좌 잔액, 경매 남은 시간 같은 것은
          3분 전 값을 보이면 <b>사람이 잘못된 판단</b>을 합니다.
          그런 자리에서는 차라리 비우고 기다리게 하거나,
          <b>'확인 중'</b>이라고 적고 동작을 막습니다.<br>
          반대로 목록·대시보드처럼 <b>대충 맞으면 되는</b> 값은
          옛 값을 보이는 쪽이 늘 낫습니다 —
          화면이 깜빡이지 않고, 굴린 자리도 안 튑니다.</p>''',
  do=ul([
    "다시 받는 동안 <b>옛 값을 그대로</b> 두기",
    "<b>'○분 전 기준'</b>을 숫자 옆에 적기",
    "너무 묵으면 <b>새로 고침</b>을 권하기",
  ]),
  dont=ul([
    "다시 받을 때마다 <b>화면 비우기</b> — 깜빡이고 자리가 튄다",
    "기준 시각을 <b>안 적기</b> — 방금 값인 줄 안다",
    "재고·잔액 같은 값에 <b>옛 값</b> 쓰기",
    "'마지막 업데이트' 를 <b>절대 시각</b>으로만 적기 — '3분 전'이 더 읽기 쉽다",
  ]),
  instead='처음 그릴 때는 <a href="skeleton.html">스켈레톤</a>, 앞으로 될 값은 <a href="optimistic.html">낙관적 UI</a>, 연결이 없으면 <a href="offline.html">오프라인</a>, 바뀌는 자리만 고치려면 <a href="partialload.html">부분 로딩</a>.',
  cases=cases([
    (val("1,284만", "3분 전 기준", "", "", True), "대시보드", "<b>대충 맞으면</b> 되는 값"),
    (val("12건", "방금 기준", "", "", True), "목록", "굴린 자리가 <b>안 튄다</b>"),
    (val("", "확인 중…", "", "", None, "150px", False, True), "재고 · 잔액", "<b>옛 값을 쓰면 안 된다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 값의 계약서",
  code_lede="옛 값을 지우지 않고, 기준 시각을 <code>&lt;time&gt;</code> 으로 적습니다.",
  code='''&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"big"</span> <span class="a">aria-busy</span>=<span class="s">"true"</span>&gt;1,284만원&lt;/<span class="t">p</span>&gt;
&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"asof"</span>&gt;
  &lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-14T09:00"</span>&gt;3분 전&lt;/<span class="t">time</span>&gt; 기준
  &lt;<span class="t">button</span>&gt;새로 고침&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">p</span>&gt;

<span class="c">// 다시 받는 동안 옛 값을 지우지 않는다</span>
state.loading = <span class="t">true</span>;              <span class="c">// data 는 그대로 둔다</span>
state.data = <span class="t">await</span> api.get();      <span class="c">// 온 뒤에만 바꾼다</span>
state.asOf = Date.now();
state.loading = <span class="t">false</span>;

/* 바뀌는 중에는 흐리게 */
[aria-busy="true"] { <span class="a">opacity</span>: <span class="a">.55</span>; <span class="a">transition</span>: opacity <span class="a">.15s</span>; }''',
  keys=kbd([
    ("<code>aria-busy</code>", "다시 받는 중임을 <b>그 자리에</b> 붙인다"),
    ("<code>&lt;time datetime&gt;</code>", "기준 시각을 <b>기계도 읽게</b> 적는다"),
    ("<code>aria-live</code>", "숫자가 저절로 바뀌면 조심한다 — <b>계속 읽어 댄다</b>"),
    ("새로 고침 단추", "자동만 믿지 말고 <b>사람이 부를 길</b>을 둔다"),
    ("초점", "다시 받아도 <b>초점이 날아가지 않게</b>"),
    ("확인하는 법", "네트워크를 느리게 걸고 <b>빈 화면이 생기는지</b> 본다"),
  ]),
  backend=rows([
    ("기준 시각을 같이", "<code>as_of</code> 가 응답에 있어야 화면이 <b>'3분 전'</b>을 적을 수 있습니다."),
    ("얼마나 묵어도 되나", "<code>max-age</code> 를 정해 주면 화면이 <b>언제 새로 받을지</b> 압니다."),
    ("<code>ETag</code>", "안 바뀌었으면 <b>304</b> 로 답해 통신을 아낍니다."),
    ("정확해야 하는 값", "재고·잔액은 <b>캐시하지 말라</b>고 응답에 적어 주는 편이 안전합니다."),
  ]),
  plat_lede="<b>생각이 같고</b> 이름이 다릅니다.",
  plats=plats([
    ("웹", "stale-while-revalidate",
     val("1,284만", "3분 전 기준", "", "", True, "110px"),
     "HTTP 헤더와 쿼리 라이브러리 양쪽에 같은 이름이 있습니다."),
    ("iOS", "캐시 + 당겨서 새로 고침",
     '''              <div class="phone" role="img" aria-label="iOS 당겨서 새로 고침 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:24px;transform:translateX(-50%);width:8px;height:8px;border-radius:999px;border:1.2px solid var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft);opacity:.55"></div></div></div>''',
     "<b>당겨서 새로 고침</b>이 표준이라 '사람이 부르는 길'이 늘 있습니다."),
    ("안드로이드", "SwipeRefresh",
     '''              <div class="phone" role="img" aria-label="안드로이드 당겨서 새로 고침 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:24px;transform:translateX(-50%);width:8px;height:8px;border-radius:999px;border:1.2px solid var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft);opacity:.55"></div></div></div>''',
     "같은 꼴입니다. 옛 값을 보이면서 위에 고리가 돕니다."),
  ]),
  plat_note="폰의 <b>당겨서 새로 고침</b>은 '옛 값을 보이다가 사람이 부르면 새로 받는다'를 한 몸짓으로 만든 것입니다 — 그래서 앱에서는 이 방식이 기본처럼 자리 잡았습니다. 웹에는 그 몸짓이 없으니 <b>새로 고침 단추</b>를 눈에 띄게 두는 편이 낫고, <b>기준 시각 옆에</b> 두면 '묵었구나 → 눌러야겠다'가 한 줄에서 이어집니다.",
  siblings=siblings("stale"),
  related='''        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="offline.html"><b>오프라인</b><em>8부</em></a></li>
        <li><a href="dashboard.html"><b>대시보드</b><em>13부</em></a></li>''',
)
