# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def rowsbox(opa, w="150px", note=""):
    items = ''.join(
      '<div style="display:flex;align-items:center;gap:5px;padding:4px 7px;border:1px solid var(--line);'
      'border-radius:5px;background:var(--surface);font-size:9.5px;opacity:' + str(o) + ';'
      + ('transform:translateY(4px);' if o < 1 else '') + '">'
      '<span style="width:6px;height:6px;border-radius:50%;background:var(--accent);flex:none"></span>'
      '<span>' + n + '</span></div>'
      for o, n in zip(opa, ['모란상회', '한빛아웃도어', '새벽상사', '대림유통']))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">' + items
            + ('<span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:220px">''' + rowsbox([1, .66, .33, .12], "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">transition-delay: 번호 × 40ms</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한 줄의 길이는 그대로 200ms</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">위에서 아래로 — 읽는 방향과 같게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">마지막 줄 = (줄 수 − 1) × 간격 + 길이</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">앞 여섯 줄만 차례로, 나머지는 한꺼번에</div>
                </div>
              </div>'''

D = dict(
  slug="stagger", ko="차례로 들어오기", en="Stagger",
  desc="여러 줄을 조금씩 늦게 들여보내는 연출. 간격이 커지면 마지막 줄이 늦어진다는 셈법.",
  lede="여러 줄을 <b>조금씩 늦게</b> 들여보내는 것. 멋있어 보이지만 <b>마지막 줄까지</b> 세어 봐야 합니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>간격과 줄 수를 바꿔 보세요. 아래에 <b>마지막 줄이 다 보이기까지</b> 걸리는 시간이 계산됩니다.<br>
          간격 160ms × 스무 줄이면 <b>3초가 넘습니다</b> — 그 사이 사용자는 이미 스크롤하고 있습니다.
          한 줄은 200ms 인데 전체는 3초인 상황이 어떻게 생기는지 숫자로 보입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "차례로 들어오기, 시차 등장, 순차 등장"),
    ("영어", "stagger, staggered animation, cascade"),
    ("같이 쓰는 말",
     "줄마다 시작을 늦추는 값이 <b>딜레이</b>(delay)이고, 그 간격을 <b>스태거</b>라 부릅니다. "
     "애니메이션 도구에서는 <b>stagger</b>·<b>offset</b>·<b>cascade</b>로 나옵니다. "
     "CSS 만으로 하려면 <code>--i</code> 같은 사용자 변수에 번호를 넣어 곱합니다."),
    ("자주 잘못 부름",
     "<b>지속 시간</b> — <a href=\"duration.html\">길이</a>는 한 줄이 걸리는 시간, 스태거는 <b>줄 사이의 틈</b>입니다.<br>"
     "<b>스크롤 등장</b> — 화면에 들어올 때 나타나는 것은 <b>관찰</b>(IntersectionObserver)이고 스태거와는 다릅니다.<br>"
     "<b>타이핑 효과</b> — 글자가 한 자씩 찍히는 것도 시차지만 <b>읽기를 막는</b> 쪽이라 성격이 다릅니다."),
  ]),
  axes=ax("차례로 들어오기"),
  oneline="간격은 <b>20~50ms</b>, 차례로 넣는 줄은 <b>앞 대여섯 줄</b>까지. 나머지는 한꺼번에 띄웁니다.",
  s4_title="간격과 줄 수", s4_hint="마지막 줄까지 세어 본다",
  states=states([
    (rowsbox([1, 1, 1, 1], "150px", "간격 0ms — 한꺼번에"), "간격 0", "차례가 안 보인다. <b>그래도 문제는 없다</b>"),
    (rowsbox([1, .9, .75, .55], "150px", "간격 30ms — 결이 보인다"), "간격 30ms", "<b>가장 알맞은</b> 구간. 눈치채기 전에 끝난다"),
    (rowsbox([1, .6, .25, .05], "150px", "간격 80ms — 눈에 띈다"), "간격 80ms", "확실히 보인다. 줄이 적을 때만"),
    (rowsbox([1, .3, .06, 0], "150px", "간격 160ms — 마지막이 멀다"), "간격 160ms", "<b>스무 줄이면 3초.</b> 기다리게 된다"),
    (rowsbox([.08, .3, .7, 1], "150px", "아래에서 위로"), "방향이 거꾸로", "<b>읽는 방향과 어긋난다.</b> 어색하다"),
    (rowsbox([1, 1, 1, 1], "150px", "모션 줄이기 — 한꺼번에"), "줄이기에서", "시차를 <b>없앤다.</b> 전부 같이 나타난다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("줄들", "같은 연출", "길이와 곡선은 <b>모두 같다.</b> 다른 것은 시작 시각뿐"),
    ("간격", "delay = i × 40ms", "번호에 곱한다. <b>이게 스태거의 전부</b>다"),
    ("한 줄 길이", "200ms", "간격과 <b>따로</b> 정한다. 둘을 섞으면 셈이 안 맞는다"),
    ("방향", "위 → 아래", "읽는 방향과 같게. <b>거꾸로면 어색</b>하다"),
    ("마지막 줄", "(n−1)×간격 + 길이", "이 숫자가 <b>사용자가 기다리는 시간</b>이다"),
    ("자르기", "앞 여섯 줄만", "나머지는 한꺼번에. 안 그러면 <b>긴 목록이 지옥</b>이 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          셈법이 전부입니다 — <b>(줄 수 − 1) × 간격 + 한 줄 길이</b>.
          한 줄이 200ms 라도 간격 160ms 에 스무 줄이면 <b>3,240ms</b>입니다.
          디자인 시안은 보통 네댓 줄로 만들기 때문에 이 숫자가 안 드러나고,
          실제 데이터가 들어오고 나서야 문제가 보입니다.
          <b>시안을 받을 때 '줄이 스무 개면?'을 한 번 물어보는</b> 것으로 대부분 막힙니다.</p>''',
  do=ul([
    "<b>처음 한 번</b> 그려지는 목록 — 빈 화면에서 내용이 들어올 때",
    "줄이 <b>대여섯</b>일 때 — 카드 묶음, 메뉴 항목",
    "묶음끼리 <b>순서가 있다</b>고 말하고 싶을 때",
  ]),
  dont=ul([
    "긴 목록 전체에 — <b>마지막 줄이 몇 초 뒤</b>가 된다",
    "줄이 바뀔 때마다 — 필터를 누를 때마다 춤추면 못 쓴다",
    "<b>스크롤할 때마다</b> 다시 — 두 번째부터는 방해다",
    "간격을 100ms 넘게 — 거의 늘 과하다",
  ]),
  instead='한 줄의 길이는 <a href="duration.html">지속 시간</a>, 들고 나는 짝은 <a href="enterexit.html">진입과 퇴장</a>, 아직 데이터가 없으면 <a href="../items/skeleton.html">스켈레톤</a>.',
  cases=cases([
    (rowsbox([1, .85, .6, .3], "150px"), "목록 첫 그리기", "가장 흔하고 가장 안전한 자리"),
    ('''              <div style="width:100%;max-width:150px;display:grid;grid-template-columns:1fr 1fr;gap:4px">
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.7"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.4"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.15"></span>
              </div>''',
     "격자에서는 대각선으로", "가로 번호 + 세로 번호로 <b>비스듬히</b> 들어온다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9px;color:var(--fg-muted)">앞 6줄 — 차례로</span>
                <span style="height:5px;border-radius:3px;background:var(--accent)"></span>
                <span style="font-size:9px;color:var(--fg-muted)">나머지 — 한꺼번에</span>
                <span style="height:5px;border-radius:3px;background:var(--line-strong)"></span>
              </div>''',
     "앞쪽만 차례로", "긴 목록은 <b>잘라 둔다.</b> 아래는 어차피 안 보인다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 시차의 계약서",
  code_lede="번호를 CSS 변수로 넘기고 곱합니다. <b>앞 몇 줄까지만</b> 늦춥니다.",
  code='''&lt;<span class="t">li</span> <span class="a">style</span>=<span class="s">"--i:0"</span>&gt;…&lt;/<span class="t">li</span>&gt;
&lt;<span class="t">li</span> <span class="a">style</span>=<span class="s">"--i:1"</span>&gt;…&lt;/<span class="t">li</span>&gt;

<span class="t">li</span> {
  <span class="a">opacity</span>: <span class="a">0</span>; <span class="a">transform</span>: translateY(<span class="a">8px</span>);
  <span class="a">transition</span>: opacity <span class="a">200ms</span> <span class="a">var</span>(--ease-out), transform <span class="a">200ms</span> <span class="a">var</span>(--ease-out);
  <span class="a">transition-delay</span>: <span class="a">calc</span>(<span class="a">min</span>(<span class="a">var</span>(--i), <span class="a">5</span>) * <span class="a">40ms</span>);   <span class="c">/* 앞 6줄까지만 */</span>
}
<span class="t">li</span>.in { <span class="a">opacity</span>: <span class="a">1</span>; <span class="a">transform</span>: none; }

@media (prefers-reduced-motion: reduce) {
  <span class="t">li</span> { <span class="a">transition-delay</span>: <span class="a">0s</span>; <span class="a">transform</span>: none; }
}''',
  keys=kbd([
    ("<code>min()</code>으로 자른다", "<code>min(var(--i), 5)</code> — 일곱 번째부터는 더 안 늦어진다"),
    ("읽는 순서는 안 바뀐다", "시각적으로 늦게 나타나도 <b>DOM 순서</b>는 그대로다. 스크린 리더는 기다리지 않는다"),
    ("<code>transition-delay</code> vs <code>animation-delay</code>", "상태를 오가면 <code>transition</code>, 한 번 재생이면 <code>animation</code>"),
    ("초점을 뺏지 않는다", "아직 투명한 줄에 초점이 가면 <b>안 보이는 곳</b>에 커서가 있는 셈이 된다"),
    ("<code>prefers-reduced-motion</code>", "간격을 <b>0 으로</b>. 시차는 줄이기에서 가장 먼저 끄는 것 중 하나다"),
    ("다시 그릴 때 끈다", "필터를 누를 때마다 춤추지 않게 <b>첫 그리기에만</b> 클래스를 붙인다"),
  ]),
  backend=rows([
    ("데이터가 늦게 오면 두 번 기다린다", "응답 600ms + 시차 1,200ms = <b>1.8초</b>입니다. 사용자는 둘을 구분하지 못합니다."),
    ("쪽을 더 받을 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>로 다음 묶음이 올 때마다 시차를 다시 주면 <b>스크롤할 때마다 춤춥니다</b>. 새로 온 줄만 짧게."),
    ("줄 수가 들쭉날쭉", "서버가 한 번에 100건을 주면 시차가 10초가 됩니다. <b>자르는 상한</b>이 화면 쪽에 반드시 있어야 합니다."),
  ]),
  plat_lede="이름은 다르지만 <b>번호에 간격을 곱하는</b> 것은 같습니다.",
  plats=plats([
    ("웹", "transition-delay",
     rowsbox([1, .7, .4], "105px"),
     "번호를 CSS 변수로 넘겨 곱합니다. 라이브러리들은 <code>stagger()</code> 함수를 제공합니다."),
    ("iOS", "delay · PhaseAnimator",
     '''              <div class="phone" role="img" aria-label="iOS 시차 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;display:grid;gap:3px"><span style="height:8px;border-radius:2px;background:var(--line)"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.6"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.25"></span></div></div></div>''',
     "<code>.animation(.default.delay(…))</code>로 줍니다. 목록 기본 등장에는 <b>시차를 거의 안 씁니다</b>."),
    ("안드로이드", "Material motion",
     '''              <div class="phone" role="img" aria-label="Material 시차 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;display:grid;gap:3px"><span style="height:8px;border-radius:2px;background:var(--line)"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.6"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.25"></span></div></div></div>''',
     "규격에 <b>20~30ms</b> 간격을 권합니다. 긴 목록에는 쓰지 말라고 못 박아 두었습니다."),
  ]),
  plat_note="시안에서 가장 멋있어 보이고 실제로는 가장 자주 빠지는 연출입니다. <b>시안의 줄 수와 실제 줄 수가 다르기</b> 때문입니다. 받을 때 '줄이 스무 개일 때 마지막은 몇 초 뒤입니까'를 한 번 물으면, 대개 간격이 절반으로 줄거나 앞쪽만 하기로 정리됩니다.",
  siblings=siblings("stagger"),
  related='''        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>''',
)
