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
  desc="데이터를 다시 받는 동안 옛 값을 그대로 보여 주는 방식과, 그 값이 언제 기준인지 적는 법, 이 방식의 한계를 보여 주는 항목입니다.",
  lede="오래된 데이터는 새 값을 받기 전까지 화면에 남겨 두는 이전 값입니다. 다시 받는 동안 <b>화면을 비우면</b> 사용자는 그동안 아무것도 읽을 수 없으므로, 옛 값을 그대로 두되 그 값이 <b>언제 기준인지</b> 함께 적습니다.",
  axes_lede="데이터를 다시 받는 동안 화면에 보여 주는 방법들을 모았습니다. 아래 네 가지를 물어보면 방법마다 차이가 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>다시 받는 동안 화면을 비우면 사용자는 그동안 <b>아무것도 읽을 수 없습니다</b>. 데모는 <b>숫자가 사라져 있던 시간(ms)</b>을
          재서 적는데, 옛 값을 그대로 두면 이 시간이 <b>0</b>이 됩니다.<br>
          그 대신 옛 값에는 <b>언제 기준인 숫자인지</b>를 붙여야 합니다. '3분 전 기준'이 없으면
          사용자는 방금 받은 값인 줄 압니다. 체크를 끄면 기준 시각 없이 숫자만 남는 모습을 볼 수 있습니다.<br>
          다시 받는 동안에는 숫자를 <b>흐리게</b> 해서 지금 값이 바뀌는 중이라는 것을 알립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "오래된 데이터, 묵은 값, 캐시된 값"),
    ("영어", "stale data, stale-while-revalidate, cached value"),
    ("같이 쓰는 말",
     "옛 값을 보여 주면서 뒤에서 새 값을 받아 오는 방식은 <b>stale-while-revalidate</b>라고 부릅니다. "
     "값이 만들어진 시각은 <b>as of</b>(기준 시각), 값이 만들어진 뒤 지난 시간은 <b>나이</b>(age)라고 하고, "
     "'3분 전 기준' 같은 표시는 <b>신선도 표시</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>캐시</b> — 캐시는 데이터를 <b>저장하는 장치</b>이고, 오래된 데이터는 그 값을 화면에 <b>보여 주는 방식</b>입니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 <b>앞으로 바뀔 값</b>을 미리 보여 주고, 오래된 데이터는 <b>이미 받아 둔 지난 값</b>을 보여 줍니다.<br>"
     "<b>오프라인</b> — <a href=\"offline.html\">오프라인</a> 처리는 <b>연결이 없을 때</b>의 대응이고, 오래된 데이터는 연결된 상태에서 새 값을 기다리는 동안의 표시입니다."),
  ]),
  axes=ST,
  oneline="새 값을 받는 동안에는 <b>옛 값이라도 보여 줍니다.</b> 대신 그 값이 언제 기준인지를 반드시 적습니다.",
  s4_title="상태", s4_hint="빈 화면이 생기는지에 따른 차이",
  states=states([
    (val("1,284만", "방금 기준", "", "막 받았다", True), "막 받음", "<b>가장 좋은</b> 상태입니다"),
    (val("1,284만", "3분 전 기준", "", "묵었지만 읽힌다", None), "묵음", "시간이 지난 값이지만 <b>읽을 수 있습니다</b>"),
    (val("1,284만", "다시 받는 중…", "", "흐리게 — 바뀌는 중", True, "152px", True),
     "다시 받는 중", "<b>옛 값을 흐리게</b> 보여 줍니다"),
    (val("", "", "", "그동안 아무것도 못 읽는다", False, "152px", False, True),
     "비우고 스피너", "다시 받는 동안 <b>빈 화면</b>이 됩니다"),
    (val("1,284만", "", "", "방금 값인 줄 안다", False), "기준 시각 없음", "옛 값이 <b>방금 받은 값처럼 보입니다</b>"),
    (val("1,284만", "1시간 전 기준 · 새로 고침 ›", "", "너무 묵으면 권한다", None),
     "너무 묵음", "사용자에게 <b>새로 받으라고</b> 권합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("옛 값", "그대로 둠", "옛 값을 그대로 두어 <b>빈 화면</b>이 생기지 않게 합니다"),
    ("기준 시각", "'3분 전'", "값이 언제 기준인지 <b>반드시</b> 적습니다"),
    ("흐리게", "다시 받는 중", "값이 바뀌는 중임을 알립니다"),
    ("안 적으면", "거짓말", "기준 시각을 적지 않으면 사용자는 <b>방금 받은 값인 줄</b> 압니다"),
    ("새로 고침", "사람이 부를 길", "자동 갱신을 기다리기 싫을 때 사용자가 직접 누릅니다"),
    ("예외", "돈 · 재고", "돈이나 재고처럼 <b>틀리면 안 되는</b> 값에는 이 방식을 쓰지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이 방식은 <b>틀린 값을 보이면 안 되는 자리</b>에는 쓰지 않습니다.
          남은 재고나 계좌 잔액, 경매 남은 시간 같은 값은
          3분 전 값을 보여 주면 <b>사용자가 잘못된 판단</b>을 하게 됩니다.
          이런 자리에서는 차라리 화면을 비우고 기다리게 하거나,
          <b>'확인 중'</b>이라고 적고 관련 동작을 막습니다.<br>
          반대로 목록이나 대시보드처럼 <b>대략 맞으면 되는</b> 값은
          옛 값을 보여 주는 편이 늘 낫습니다.
          화면이 깜빡이지 않고, 스크롤해 둔 위치도 튀지 않기 때문입니다.</p>''',
  do=ul([
    "데이터를 다시 받는 동안 <b>옛 값을 그대로</b> 둘 때",
    "숫자 옆에 <b>'○분 전 기준'</b>을 적을 때",
    "값이 너무 오래됐을 때. 사용자에게 <b>새로 고침</b>을 권합니다",
  ]),
  dont=ul([
    "다시 받을 때마다 <b>화면을 비울 때</b>. 화면이 깜빡이고 스크롤 위치가 튑니다",
    "기준 시각을 <b>적지 않을 때</b>. 사용자가 방금 받은 값인 줄 압니다",
    "재고나 잔액 같은 값에 <b>옛 값</b>을 보여 줄 때",
    "'마지막 업데이트'를 <b>절대 시각</b>으로만 적을 때. '3분 전'처럼 적는 편이 더 읽기 쉽습니다",
  ]),
  instead='처음 그릴 때는 <a href="skeleton.html">스켈레톤</a>, 앞으로 될 값은 <a href="optimistic.html">낙관적 UI</a>, 연결이 없으면 <a href="offline.html">오프라인</a>, 바뀌는 자리만 고치려면 <a href="partialload.html">부분 로딩</a>.',
  cases=cases([
    (val("1,284만", "3분 전 기준", "", "", True), "대시보드", "<b>대략 맞으면</b> 되는 값이라 옛 값을 보여 줘도 됩니다"),
    (val("12건", "방금 기준", "", "", True), "목록", "옛 값을 그대로 두므로 스크롤 위치가 <b>튀지 않습니다</b>"),
    (val("", "확인 중…", "", "", None, "150px", False, True), "재고 · 잔액", "<b>옛 값을 보여 주면 안 되는</b> 값입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="다시 받는 동안 옛 값을 지우지 않고, 기준 시각은 <code>&lt;time&gt;</code> 요소로 적습니다.",
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
    ("<code>aria-busy</code>", "다시 받는 중이라는 표시를 값이 있는 <b>그 자리에</b> 붙입니다"),
    ("<code>&lt;time datetime&gt;</code>", "기준 시각을 <b>프로그램도 읽을 수 있게</b> 적습니다"),
    ("<code>aria-live</code>", "숫자가 저절로 바뀌는 자리에 쓸 때는 조심합니다. 값이 바뀔 때마다 스크린 리더가 <b>계속 읽어 줍니다</b>"),
    ("새로 고침 단추", "자동 갱신만 믿지 말고 <b>사용자가 직접 새로 받을 수 있는</b> 버튼을 둡니다"),
    ("초점", "다시 받아도 <b>초점이 사라지지 않게</b> 합니다"),
    ("확인하는 법", "네트워크 속도를 느리게 설정하고 <b>빈 화면이 생기는지</b> 봅니다"),
  ]),
  backend=rows([
    ("기준 시각을 같이", "응답에 <code>as_of</code>가 있어야 화면에 <b>'3분 전'</b>을 적을 수 있습니다."),
    ("얼마나 묵어도 되나", "서버가 <code>max-age</code>를 정해 주면 화면이 <b>언제 새로 받아야 할지</b> 알 수 있습니다."),
    ("<code>ETag</code>", "값이 바뀌지 않았으면 서버가 <b>304</b>로 답해 본문을 다시 보내지 않으므로 통신량이 줄어듭니다."),
    ("정확해야 하는 값", "재고나 잔액 응답에는 <b>캐시하지 말라</b>는 지시를 적어 주는 편이 안전합니다."),
  ]),
  plat_lede="플랫폼마다 <b>원리는 같고</b> 부르는 이름만 다릅니다.",
  plats=plats([
    ("웹", "stale-while-revalidate",
     val("1,284만", "3분 전 기준", "", "", True, "110px"),
     "HTTP 헤더와 쿼리 라이브러리 양쪽에 같은 이름의 기능이 있습니다."),
    ("iOS", "캐시 + 당겨서 새로 고침",
     '''              <div class="phone" role="img" aria-label="iOS 당겨서 새로 고침 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:24px;transform:translateX(-50%);width:8px;height:8px;border-radius:999px;border:1.2px solid var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft);opacity:.55"></div></div></div>''',
     "<b>당겨서 새로 고침</b>이 표준이라서 사용자가 직접 새 값을 받는 방법이 늘 있습니다."),
    ("안드로이드", "SwipeRefresh",
     '''              <div class="phone" role="img" aria-label="안드로이드 당겨서 새로 고침 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:24px;transform:translateX(-50%);width:8px;height:8px;border-radius:999px;border:1.2px solid var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft);opacity:.55"></div></div></div>''',
     "iOS와 같은 방식입니다. 옛 값을 보여 주는 동안 화면 위쪽에서 고리가 돕니다."),
  ]),
  plat_note="휴대폰의 <b>당겨서 새로 고침</b>은 '옛 값을 보여 주다가 사용자가 원하면 새로 받는다'는 동작을 몸짓 하나로 만든 것입니다. 그래서 앱에서는 오래된 데이터를 보여 주는 방식이 기본처럼 자리 잡았습니다. 웹에는 이런 몸짓이 없으므로 <b>새로 고침 버튼</b>을 눈에 띄게 두는 편이 낫습니다. 버튼을 <b>기준 시각 옆에</b> 두면 사용자가 값이 오래된 것을 확인하고 바로 이어서 새로 고침을 누를 수 있습니다.",
  siblings=siblings("stale"),
  related='''        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="offline.html"><b>오프라인</b><em>8부</em></a></li>
        <li><a href="dashboard.html"><b>대시보드</b><em>13부</em></a></li>''',
)
