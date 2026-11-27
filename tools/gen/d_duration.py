# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def lane(pct, label, warn=False, w="150px"):
    col = "var(--danger)" if warn else "var(--accent)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<div style="height:22px;border-radius:999px;background:var(--bg);border:1px solid var(--line);position:relative">'
            '<span style="position:absolute;top:3px;left:calc(3px + ' + str(pct) + '% * 0.86);width:14px;height:14px;border-radius:50%;background:' + col + '"></span></div>'
            '<span style="font-family:var(--mono);font-size:9.5px;color:' + (col if warn else 'var(--fg-muted)') + '">' + label + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">툴팁 · 색 바뀜 — <b>100ms</b></div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">드롭다운 · 토글 — <b>150ms</b></div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">모달 · 시트 열기 — <b>250ms</b></div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">화면 전체 전환 — <b>350ms</b></div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">400ms 넘으면 기다리게 된다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">100ms 아래는 깜빡인 것처럼 보인다</div>
                </div>
              </div>'''

D = dict(
  slug="duration", ko="지속 시간", en="Duration",
  desc="움직임의 길이를 정하는 기준표. 거리와 크기에 따라 100~350ms, 자주 보는 것일수록 짧게.",
  lede="움직임이 <b>얼마나 걸릴지</b>. 한 번은 멋있는 길이가 <b>백 번째에는</b> 답답합니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 길이만 바꿔 보세요. <b>같은 움직임</b>이 전혀 다르게 느껴집니다.<br>
          <b>0ms</b>는 순간이동이라 무엇이 어디서 왔는지 모르고, <b>100ms 아래</b>는 깜빡인 것처럼 보이고,
          <b>400ms 위</b>부터는 기다리게 됩니다. 아래 표에서 지금 길이에 맞는 쓰임이 밝아집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "지속 시간, 길이, 재생 시간"),
    ("영어", "duration, transition duration"),
    ("같이 쓰는 말",
     "CSS 로는 <code>transition-duration</code>·<code>animation-duration</code>입니다. "
     "시작을 늦추는 것이 <b>딜레이</b>(delay), "
     "값들을 <code>--duration-fast</code>처럼 이름 붙여 두면 <b>모션 토큰</b>이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>이징</b> — <a href=\"easing.html\">이징</a>은 '어떻게', 길이는 '<b>얼마나</b>'입니다.<br>"
     "<b>딜레이</b> — 늦게 시작하는 것과 오래 걸리는 것은 다릅니다. 딜레이는 <a href=\"stagger.html\">차례로</a>에 씁니다.<br>"
     "<b>FPS</b> — 초당 프레임 수는 <b>매끄러움</b>의 문제라 <a href=\"cheap.html\">무엇을 움직이나</a> 쪽입니다."),
  ]),
  axes=ax("지속 시간"),
  oneline="길이는 <b>거리와 크기</b>를 따릅니다. 그리고 <b>자주 보는 것일수록 짧게</b> — 이 두 줄이 기준표의 전부입니다.",
  s4_title="길이별로", s4_hint="같은 움직임, 다른 길이",
  states=states([
    (lane(100, "0ms — 어디서 왔는지 모른다", True), "0ms", "순간이동. <b>무엇이 바뀌었는지</b> 못 쫓아간다"),
    (lane(60, "80ms — 깜빡인 것 같다", True), "100ms 아래", "눈이 못 따라간다. <b>있으나 마나</b>"),
    (lane(45, "150ms — 토글 · 드롭다운"), "100~200ms", "짧은 거리. <b>가장 많이 쓰는</b> 구간"),
    (lane(30, "250ms — 모달 · 시트"), "200~300ms", "화면 절반쯤 움직일 때"),
    (lane(18, "350ms — 화면 전환"), "300~400ms", "화면 하나가 통째로 바뀔 때. <b>여기까지가 상한</b>"),
    (lane(6, "800ms — 기다리게 된다", True), "400ms 위", "연출은 되지만 <b>일을 막는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("아주 짧게", "100ms", "자리가 거의 안 변하는 것 — 색, 테두리, 툴팁"),
    ("짧게", "150ms", "토글·드롭다운처럼 <b>손가락 하나 거리</b>"),
    ("보통", "250ms", "모달·시트. <b>어디서 왔는지</b>를 보여 줄 시간이 필요하다"),
    ("길게", "350ms", "화면 전체 전환. 이보다 길면 거의 늘 과하다"),
    ("상한", "400ms", "넘으면 <b>애니메이션이 일을 막기</b> 시작한다"),
    ("하한", "100ms", "아래로 내리면 <b>움직임이 안 읽힌다.</b> 차라리 0 이 낫다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          기준표의 숫자보다 중요한 것은 <b>'몇 번 보느냐'</b>입니다.
          온보딩처럼 한 번 보는 화면은 400ms 도 괜찮지만,
          목록에서 하루에 백 번 여는 메뉴가 300ms 면 <b>하루에 30초</b>를 기다리는 셈입니다.
          <b>자주 쓰는 것일수록 짧게</b> — 이 규칙이 거리·크기보다 앞섭니다.</p>''',
  do=ul([
    "<b>토큰 서넛</b>으로 정해 두고 그것만 쓰기 — fast · base · slow",
    "거리가 멀거나 크면 조금 더 길게",
    "자주 보는 것은 <b>짧게</b> — 하루에 백 번이면 100ms 도 길다",
  ]),
  dont=ul([
    "화면마다 숫자를 손으로 적기 — <b>400, 350, 420</b>이 뒤섞인다",
    "<b>멋있다고 길게</b> — 두 번째부터는 답답하다",
    "100ms 아래 — 안 보일 바에는 <b>0</b>이 낫다",
    "데이터를 기다리는 시간을 애니메이션으로 때우기 → <a href=\"../items/skeleton.html\">스켈레톤</a>",
  ]),
  instead='속도를 나눠 쓰는 방식은 <a href="easing.html">이징</a>, 줄마다 늦게 들어오는 것은 <a href="stagger.html">차례로</a>, 기다림을 보여 주는 것은 <a href="../items/spinner.html">스피너</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:3px;font-family:var(--mono);font-size:9.5px">
                <span style="color:var(--accent)">--dur-fast: 120ms</span>
                <span style="color:var(--accent)">--dur-base: 220ms</span>
                <span style="color:var(--accent)">--dur-slow: 340ms</span>
              </div>''',
     "토큰 셋", "값이 아니라 <b>이름</b>을 쓰게 한다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b>열 때 250ms</b><br><span style="color:var(--fg-muted)">닫을 때 180ms</span>
              </div>''',
     "들고 날 때 다르게", "<a href=\"enterexit.html\">진입과 퇴장</a>에서 자세히"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted)">
                @media (prefers-reduced-motion: reduce) {<br>
                &nbsp;&nbsp;* { <span style="color:var(--accent)">animation-duration: .01ms</span> }<br>}
              </div>''',
     "줄이기에서는 0 에 가깝게", "완전히 0 으로 두면 <code>animationend</code>가 안 오는 코드가 있다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 길이의 계약서",
  code_lede="길이도 <b>토큰</b>으로 두고, 모션 줄이기에서는 거의 0 으로 내립니다.",
  code=''':root {
  <span class="a">--dur-fast</span>: <span class="a">120ms</span>;   <span class="c">/* 색 · 툴팁 */</span>
  <span class="a">--dur-base</span>: <span class="a">220ms</span>;   <span class="c">/* 토글 · 드롭다운 */</span>
  <span class="a">--dur-slow</span>: <span class="a">340ms</span>;   <span class="c">/* 모달 · 화면 전환 */</span>
}

.menu { <span class="a">transition</span>: opacity <span class="a">var</span>(--dur-base) <span class="a">var</span>(--ease-out); }

@media (prefers-reduced-motion: reduce) {
  :root { <span class="a">--dur-fast</span>: <span class="a">1ms</span>; <span class="a">--dur-base</span>: <span class="a">1ms</span>; <span class="a">--dur-slow</span>: <span class="a">1ms</span>; }
}''',
  keys=kbd([
    ("단위를 빼먹지 않는다", "<code>transition: transform 200</code>은 <b>통째로 무시</b>된다. <code>200ms</code>나 <code>.2s</code>"),
    ("<code>0s</code>와 <code>0.01ms</code>", "완전히 0 이면 <code>transitionend</code>·<code>animationend</code>가 안 온다. 그 이벤트를 기다리는 코드가 멎는다"),
    ("속성마다 다르게", "<code>transition: transform 240ms, opacity 140ms</code> — 투명도는 더 짧아도 된다"),
    ("<code>prefers-reduced-motion</code>", "길이를 1ms 로 내리는 것이 가장 안전한 대응이다"),
    ("초점이 옮겨 갈 때", "애니메이션이 끝나기를 기다려 초점을 옮기면 <b>키보드 사용자가 멈춰 선다</b>. 초점은 먼저 옮긴다"),
    ("<code>&lt;dialog&gt;</code> 닫기", "<code>close()</code>는 바로 사라진다. 나가는 연출을 보려면 <b>끝난 뒤</b>에 호출한다"),
  ]),
  backend=rows([
    ("응답보다 애니메이션이 길면", "데이터가 50ms 에 와도 전환이 400ms 면 사용자는 400ms 를 기다립니다. <b>느린 쪽이 서버가 아닐 수</b> 있습니다."),
    ("요청은 먼저 보낸다", "'애니메이션이 끝나면 부르기'로 짜면 길이만큼 늦어집니다. 요청과 연출은 <b>같이 시작</b>합니다."),
    ("지표에 섞인다", "LCP·INP 같은 숫자에 연출 시간이 들어갑니다. 느리게 나타나는 히어로는 <b>점수를 깎습니다</b>."),
    ("최소 표시 시간", "스피너가 50ms 만 보이고 사라지면 깜빡임이 됩니다. <b>띄웠으면 300ms 는 유지</b>하는 쪽이 덜 어지럽습니다."),
  ]),
  plat_lede="세 곳의 권장값이 거의 같습니다 — <b>100~400ms</b>.",
  plats=plats([
    ("웹", "토큰으로",
     lane(40, "220ms", False, "110px"),
     "표준 권장값이 없어 <b>팀이 정합니다.</b> 그래서 정해 두지 않으면 화면마다 달라집니다."),
    ("iOS", "0.2~0.35s",
     lane(35, "0.3s", False, "110px"),
     "시스템 전환이 약 0.35초입니다. 요즘은 길이 대신 <b>스프링의 뻣뻣함</b>으로 정합니다."),
    ("안드로이드", "Material 3",
     lane(42, "200ms", False, "110px"),
     "<b>short · medium · long</b>으로 50~600ms 를 구간별로 정해 두었습니다. 기본은 200ms 안팎입니다."),
  ]),
  plat_note="\"애니메이션이 느려요\"와 \"화면이 느려요\"는 <b>다른 문제</b>인데 사용자는 같은 말로 신고합니다. 길이를 토큰으로 묶어 두면 한 줄만 고쳐 전체를 빠르게 만들어 볼 수 있어, <b>원인이 어느 쪽인지</b>를 금방 가릅니다.",
  siblings=siblings("duration"),
  related='''        <li><a href="easing.html"><b>이징 곡선</b><em>9부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
