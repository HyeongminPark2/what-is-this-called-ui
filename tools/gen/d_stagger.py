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
  desc="여러 줄을 조금씩 늦게 들여보내는 연출입니다. 간격이 커지면 마지막 줄이 그만큼 늦어진다는 셈법을 보여 주는 항목입니다.",
  lede="차례로 들어오기는 여러 줄을 <b>조금씩 늦게</b> 들여보내는 연출입니다. 보기에는 멋있지만, <b>마지막 줄이 언제 나타나는지</b> 꼭 계산해 봐야 합니다.",
  axes_lede="움직임은 화면에서 무엇이 바뀌었는지 사용자에게 <b>알려 주는</b> 역할을 합니다. 아래 네 가지를 따져 보면 움직임을 다루는 항목들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>간격과 줄 수를 바꿔 보세요. 아래에 <b>마지막 줄이 다 보이기까지</b> 걸리는 시간이 계산됩니다.<br>
          간격 160ms로 스무 줄을 들여보내면 <b>3초가 넘게</b> 걸리는데, 그 사이에 사용자는 이미 스크롤을 시작합니다.
          한 줄은 200ms 만에 나타나는데도 전체가 3초나 걸리는 이유를 숫자로 확인할 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "차례로 들어오기, 시차 등장, 순차 등장"),
    ("영어", "stagger, staggered animation, cascade"),
    ("같이 쓰는 말",
     "줄마다 시작을 늦추는 값을 <b>딜레이</b>(delay)라고 하고, 줄 사이의 간격을 <b>스태거</b>라고 부릅니다. "
     "애니메이션 도구에서는 <b>stagger</b>·<b>offset</b>·<b>cascade</b>라는 이름으로 나옵니다. "
     "CSS만으로 만들려면 <code>--i</code> 같은 사용자 변수에 줄 번호를 넣고 간격을 곱합니다."),
    ("자주 잘못 부르는 이름",
     "<b>지속 시간</b> — <a href=\"duration.html\">길이</a>는 한 줄이 나타나는 데 걸리는 시간이고, 스태거는 <b>줄과 줄 사이의 시간 간격</b>입니다.<br>"
     "<b>스크롤 등장</b> — 요소가 화면에 들어올 때 나타나게 하는 것은 <b>관찰</b>(IntersectionObserver)로 만드는 연출이라 스태거와는 다릅니다.<br>"
     "<b>타이핑 효과</b> — 글자가 한 자씩 찍히는 것도 시차를 두는 연출이지만, 글을 다 찍을 때까지 <b>읽기를 막는다</b>는 점에서 성격이 다릅니다."),
  ]),
  axes=ax("차례로 들어오기"),
  oneline="간격은 <b>20~50ms</b>로 두고, 차례로 넣는 줄은 <b>앞 대여섯 줄</b>까지만 둡니다. 나머지 줄은 한꺼번에 띄웁니다.",
  s4_title="간격과 줄 수", s4_hint="마지막 줄까지 세어 본다",
  states=states([
    (rowsbox([1, 1, 1, 1], "150px", "간격 0ms — 한꺼번에"), "간격 0", "차례가 보이지 않지만 <b>그래도 문제는 없습니다</b>"),
    (rowsbox([1, .9, .75, .55], "150px", "간격 30ms — 결이 보인다"), "간격 30ms", "<b>가장 알맞은</b> 구간입니다. 사용자가 기다린다고 느끼기 전에 끝납니다"),
    (rowsbox([1, .6, .25, .05], "150px", "간격 80ms — 눈에 띈다"), "간격 80ms", "차례가 확실히 보입니다. 줄이 적을 때만 씁니다"),
    (rowsbox([1, .3, .06, 0], "150px", "간격 160ms — 마지막이 멀다"), "간격 160ms", "<b>스무 줄이면 3초</b>가 걸려서 사용자가 기다리게 됩니다"),
    (rowsbox([.08, .3, .7, 1], "150px", "아래에서 위로"), "방향이 거꾸로", "<b>읽는 방향과 어긋나서</b> 어색합니다"),
    (rowsbox([1, 1, 1, 1], "150px", "모션 줄이기 — 한꺼번에"), "줄이기에서", "시차를 <b>없애서</b> 모든 줄이 같이 나타납니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("줄들", "같은 연출", "길이와 곡선은 <b>모두 같고</b>, 시작 시각만 다릅니다"),
    ("간격", "delay = i × 40ms", "줄 번호에 간격을 곱해서 정합니다. <b>스태거는 이 계산 하나로</b> 만듭니다"),
    ("한 줄 길이", "200ms", "간격과 <b>따로</b> 정합니다. 둘을 섞으면 전체 시간 계산이 맞지 않습니다"),
    ("방향", "위 → 아래", "읽는 방향과 같게 둡니다. <b>방향이 거꾸로면 어색</b>합니다"),
    ("마지막 줄", "(n−1)×간격 + 길이", "이 값이 <b>사용자가 기다리는 시간</b>입니다"),
    ("자르기", "앞 여섯 줄만", "나머지 줄은 한꺼번에 띄웁니다. 그러지 않으면 <b>긴 목록에서 마지막 줄이 몇 초 뒤에야</b> 나타납니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          마지막 줄이 다 보이기까지 걸리는 시간은 <b>(줄 수 − 1) × 간격 + 한 줄 길이</b>로 계산합니다.
          한 줄이 200ms라도 간격 160ms로 스무 줄을 들여보내면 <b>3,240ms</b>가 걸립니다.
          디자인 시안은 보통 네댓 줄로 만들기 때문에 시안에서는 이 숫자가 드러나지 않고,
          실제 데이터가 들어온 뒤에야 문제가 보입니다.
          그래서 <b>시안을 받을 때 '줄이 스무 개면 어떻게 되나요?'라고 한 번 물어보면</b> 이런 문제를 대부분 미리 막을 수 있습니다.</p>''',
  do=ul([
    "빈 화면에 목록이 <b>처음 한 번</b> 그려질 때",
    "카드 묶음이나 메뉴 항목처럼 줄이 <b>대여섯</b> 개일 때",
    "묶음 사이에 <b>순서가 있다</b>는 것을 보여 주고 싶을 때",
  ]),
  dont=ul([
    "긴 목록 전체에 줄 때. <b>마지막 줄이 몇 초 뒤에야</b> 나타납니다",
    "목록 내용이 바뀔 때마다 줄 때. 필터를 누를 때마다 목록이 다시 차례로 움직이면 쓰기 불편합니다",
    "<b>스크롤할 때마다</b> 다시 줄 때. 두 번째부터는 방해가 됩니다",
    "간격을 100ms 넘게 줄 때. 대부분 과합니다",
  ]),
  instead='한 줄의 길이는 <a href="duration.html">지속 시간</a>, 들어오고 나가는 움직임의 짝은 <a href="enterexit.html">진입과 퇴장</a>, 아직 데이터가 없으면 <a href="../items/skeleton.html">스켈레톤</a>.',
  cases=cases([
    (rowsbox([1, .85, .6, .3], "150px"), "목록 첫 그리기", "차례로 들어오기를 가장 흔하게, 가장 안전하게 쓰는 자리입니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;grid-template-columns:1fr 1fr;gap:4px">
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.7"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.4"></span>
                <span style="height:32px;border-radius:5px;background:var(--surface);border:1px solid var(--line);opacity:.15"></span>
              </div>''',
     "격자에서는 대각선으로", "가로 번호와 세로 번호를 더한 값으로 늦춰서 <b>비스듬히</b> 들어오게 합니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9px;color:var(--fg-muted)">앞 6줄 — 차례로</span>
                <span style="height:5px;border-radius:3px;background:var(--accent)"></span>
                <span style="font-size:9px;color:var(--fg-muted)">나머지 — 한꺼번에</span>
                <span style="height:5px;border-radius:3px;background:var(--line-strong)"></span>
              </div>''',
     "앞쪽만 차례로", "긴 목록은 차례로 넣는 줄을 <b>앞쪽에서 자릅니다.</b> 아래쪽 줄은 어차피 처음 화면에 보이지 않습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="줄 번호를 CSS 변수로 넘기고 간격을 곱합니다. 시작은 <b>앞 몇 줄까지만</b> 늦춥니다.",
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
    ("<code>min()</code>으로 자른다", "<code>min(var(--i), 5)</code>로 상한을 두면 일곱 번째 줄부터는 더 늦어지지 않습니다"),
    ("읽는 순서는 안 바뀐다", "화면에 늦게 나타나도 <b>DOM 순서</b>는 그대로입니다. 스크린 리더는 시차를 기다리지 않고 읽습니다"),
    ("<code>transition-delay</code> vs <code>animation-delay</code>", "상태를 오가는 연출에는 <code>transition</code>, 한 번 재생하고 끝나는 연출에는 <code>animation</code>을 씁니다"),
    ("초점을 뺏지 않는다", "아직 투명한 줄에 초점이 가면 커서가 <b>보이지 않는 곳</b>에 있는 셈이 됩니다"),
    ("<code>prefers-reduced-motion</code>", "간격을 <b>0으로</b> 둡니다. 시차는 모션 줄이기에서 먼저 끄는 연출입니다"),
    ("다시 그릴 때 끈다", "필터를 누를 때마다 목록이 다시 차례로 움직이지 않도록 <b>처음 그릴 때만</b> 클래스를 붙입니다"),
  ]),
  backend=rows([
    ("데이터가 늦게 오면 두 번 기다린다", "응답에 600ms, 시차에 1,200ms가 걸리면 사용자는 모두 <b>1.8초</b>를 기다립니다. 사용자는 두 시간을 구분하지 못합니다."),
    ("쪽을 더 받을 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>로 다음 묶음이 올 때마다 시차를 다시 주면 <b>스크롤할 때마다 목록이 차례로 움직입니다</b>. 시차는 새로 온 줄에만 짧게 줍니다."),
    ("줄 수가 들쭉날쭉", "서버가 한 번에 100건을 보내면 시차만 10초가 걸립니다. 그래서 화면 쪽 코드에 차례로 넣는 줄 수의 <b>상한</b>이 반드시 있어야 합니다."),
  ]),
  plat_lede="플랫폼마다 이름은 다르지만 <b>줄 번호에 간격을 곱하는</b> 방식은 같습니다.",
  plats=plats([
    ("웹", "transition-delay",
     rowsbox([1, .7, .4], "105px"),
     "줄 번호를 CSS 변수로 넘겨 간격을 곱합니다. 애니메이션 라이브러리에는 <code>stagger()</code> 함수가 들어 있습니다."),
    ("iOS", "delay · PhaseAnimator",
     '''              <div class="phone" role="img" aria-label="iOS 시차 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;display:grid;gap:3px"><span style="height:8px;border-radius:2px;background:var(--line)"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.6"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.25"></span></div></div></div>''',
     "<code>.animation(.default.delay(…))</code>로 시차를 줍니다. 목록이 처음 나타날 때는 <b>시차를 거의 쓰지 않습니다</b>."),
    ("안드로이드", "Material motion",
     '''              <div class="phone" role="img" aria-label="Material 시차 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;display:grid;gap:3px"><span style="height:8px;border-radius:2px;background:var(--line)"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.6"></span><span style="height:8px;border-radius:2px;background:var(--line);opacity:.25"></span></div></div></div>''',
     "규격에서 <b>20~30ms</b> 간격을 권하고, 긴 목록에는 쓰지 말라고 정해 두었습니다."),
  ]),
  plat_note="차례로 들어오기는 시안에서 가장 멋있어 보이지만 실제 구현에서는 가장 자주 빠지는 연출입니다. <b>시안의 줄 수와 실제 데이터의 줄 수가 다르기</b> 때문입니다. 시안을 받을 때 '줄이 스무 개면 마지막 줄은 몇 초 뒤에 나타나나요?'라고 한 번 물으면, 대개 간격을 절반으로 줄이거나 앞쪽 줄에만 시차를 주는 쪽으로 정리됩니다.",
  siblings=siblings("stagger"),
  related='''        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>''',
)
