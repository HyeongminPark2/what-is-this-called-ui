# -*- coding: utf-8 -*-
import math
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def spath(bounce, w=140.0, h=84.0, steps=120):
    z = 1 - bounce / 100.0
    om = 9 + bounce / 6.0
    wd = om * math.sqrt(max(1 - z * z, 0))
    pts = []
    for i in range(steps + 1):
        t = i / float(steps)
        v = 1 - math.exp(-z * om * t) * math.cos(wd * t)
        pts.append("%.1f,%.1f" % (i * w / steps, 120 - v * h))
    return "M " + " L ".join(pts)

def curve(bounce, w="140px", label=""):
    return ('              <svg viewBox="0 0 140 130" role="img" aria-label="' + label + '" '
            'style="width:100%;max-width:' + w + ';height:auto;display:block;background:var(--bg);'
            'border:1px solid var(--line);border-radius:6px">'
            '<line x1="0" y1="36" x2="140" y2="36" stroke="var(--line-strong)" stroke-width="1" stroke-dasharray="3 3"/>'
            '<path d="' + spath(bounce) + '" fill="none" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/></svg>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:160px">''' + curve(28, "160px", "스프링 곡선").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">점선인 목표를 한 번 지나침</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뻣뻣함(stiffness)은 당기는 힘의 세기</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">감쇠(damping)는 흔들림이 잦아드는 빠르기</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">끌던 속도를 그대로 이어받음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">끝나는 때가 정해져 있지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="spring", ko="스프링", en="Spring",
  desc="목표를 지나쳤다가 돌아오는 물리 기반 움직임입니다. 끌던 속도를 이어받을 수 있지만 끝나는 시점이 정해져 있지 않다는 점을 보여 주는 항목입니다.",
  lede="스프링은 정해진 곡선이 아니라 <b>용수철의 움직임을 계산</b>해서 만드는 애니메이션입니다. <b>손으로 민 것 같은</b> 느낌을 낼 수 있지만, 끝나는 시점이 미리 정해져 있지 않습니다.",
  axes_lede="움직임은 무엇이 바뀌었는지 <b>알려 주는</b> 수단입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위 공은 <b>끝에서 멈추는</b> 곡선으로, 아래 공은 <b>지나쳤다가 돌아오는</b> 스프링으로 움직입니다.<br>
          튕김을 0으로 내리면 두 움직임이 거의 같아지고, 끝까지 올리면 <b>글자를 읽기 전에</b> 또 움직입니다.
          오른쪽 그래프의 점선이 목표이고, 선이 점선을 <b>넘었다가 돌아오는</b> 모양이 스프링의 특징입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스프링, 용수철, 물리 기반 애니메이션"),
    ("영어", "spring animation, physics-based animation"),
    ("같이 쓰는 말",
     "목표 쪽으로 세게 당기는 정도를 <b>뻣뻣함</b>(stiffness·tension), "
     "흔들림이 잦아드는 정도를 <b>감쇠</b>(damping·friction), "
     "움직이는 물체의 무게를 <b>질량</b>(mass)이라고 합니다. "
     "목표를 지나치는 것은 <b>오버슈트</b>(overshoot), 흔들림이 잦아들며 자리 잡는 것은 <b>세틀링</b>이라고 부릅니다. "
     "목표를 지나치지 않도록 감쇠를 딱 맞춘 상태는 <b>임계 감쇠</b>(critically damped)입니다."),
    ("자주 잘못 부르는 이름",
     "<b>바운스</b> — 튕기는 느낌을 내는 <a href=\"easing.html\">이징 곡선</a>도 있지만, 그건 스프링이 아니라 <b>길이가 정해진</b> 곡선입니다.<br>"
     "<b>이징</b> — 스프링은 미리 그려 둔 곡선이 아니라 <b>매 프레임 계산</b>해서 움직입니다. <code>cubic-bezier</code>로는 비슷하게 흉내만 낼 수 있습니다.<br>"
     "<b>관성 스크롤</b> — 손을 뗀 뒤에도 미끄러지듯 계속 움직이는 것은 <a href=\"gesture.html\">제스처</a>에서 다룹니다."),
  ]),
  axes=ax("스프링"),
  oneline="<b>끌어서 다루는 것</b>에는 스프링을, <b>순서대로 이어지는 연출</b>에는 곡선을 씁니다. 끝나는 시점을 알아야 하는 곳에는 스프링이 맞지 않습니다.",
  s4_title="튕김 정도에 따른 차이", s4_hint="튕김에 따라 목표를 지나치는 정도",
  states=states([
    (curve(0, "140px", "튕김 없음"), "튕김이 0일 때", "목표를 지나치지 않아서 <b>ease-out과 거의 같습니다</b>"),
    (curve(16, "140px", "약한 튕김"), "튕김이 약할 때", "살짝 지나쳤다가 바로 멈춥니다. <b>가장 무난한 설정</b>입니다"),
    (curve(36, "140px", "보통 튕김"), "튕김이 보통일 때", "두어 번 흔들립니다. <b>끌어서 넘기는 것</b>에 맞습니다"),
    (curve(64, "140px", "강한 튕김"), "튕김이 셀 때", "오래 흔들려서 <b>글자를 읽기 어렵습니다</b>"),
    (curve(88, "140px", "지나친 튕김"), "튕김이 지나치게 셀 때", "여러 번 크게 튀어서 <b>장난감 같은 느낌</b>이 납니다"),
    ('''              <div style="width:100%;max-width:140px;height:72px;border:1px solid var(--line);border-radius:6px;background:var(--bg);display:grid;place-items:center">
                <span style="font-size:9.5px;color:var(--fg-muted)">모션 줄이기에서는 튕김 없음</span>
              </div>''',
     "모션 줄이기를 켰을 때", "<b>목표를 지나치지 않게</b> 0으로 둡니다. 흔들림이 가장 어지럽기 때문입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("곡선", "감쇠 진동", "목표를 <b>지나쳤다가 돌아옵니다.</b> 용수철이 움직이는 모양입니다"),
    ("목표선", "1.0", "점선으로 표시합니다. 이 선에서 바로 멈추지 않고 <b>이 선을 중심으로</b> 흔들리다 멈춥니다"),
    ("뻣뻣함", "stiffness", "값이 클수록 목표 쪽으로 <b>빨리</b> 당겨지고, 작으면 느리게 늘어집니다"),
    ("감쇠", "damping", "값이 클수록 흔들림이 <b>빨리 잦아들고</b>, 작으면 오래 흔들립니다"),
    ("이어받는 속도", "initial velocity", "끌던 손가락의 속도를 그대로 이어받습니다. <b>스프링을 쓰는 가장 큰 이유</b>입니다"),
    ("끝나는 때", "정해져 있지 않음", "목표에 충분히 가까워지면 계산을 멈춥니다. 그래서 <b>몇 ms가 걸릴지 미리 알 수 없습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스프링을 쓰는 이유는 보기 좋아서라기보다 <b>끌던 속도를 이어받을 수 있기</b> 때문입니다.
          손가락으로 시트를 빠르게 튕기면 시트가 그 속도 그대로 움직이고,
          천천히 밀면 천천히 자리를 잡습니다. 손의 속도와 화면의 움직임을 이렇게 이어 주는 일은 <b>길이가 정해진 곡선으로는 할 수 없습니다</b>.
          반대로 <b>끝나는 시점을 알아야 하는</b> 곳에는 스프링이 맞지 않습니다.
          '애니메이션이 끝나면 다음 애니메이션 시작'처럼 이어 붙이는 연출은 길이가 정해진 곡선으로 만드는 편이 쉽습니다.</p>''',
  instead_title="스프링 대신 쓰거나 함께 볼 것",
  do=ul([
    "시트, 카드 넘기기, 당겨서 새로고침처럼 <b>끌어서 다루는 것</b>을 만들 때",
    "손을 뗀 뒤에 <b>이어지는 움직임</b>을 만들 때",
    "버튼이 살짝 눌렸다 돌아오는 것처럼 작고 자주 보는 <b>누르는 느낌</b>을 낼 때",
  ]),
  dont=ul([
    "읽을 글이 들어 있는 요소에 쓸 때. 글을 읽으려는데 <b>또 움직여서</b> 읽기를 방해합니다",
    "<b>순서대로 이어 붙이는</b> 연출에 쓸 때. 끝나는 시점을 알 수 없어서 다음 연출을 시작할 때를 잡기 어렵습니다",
    "세 번 넘게 흔들리게 할 때. 대부분 과합니다",
    "<a href=\"reducedmotion.html\">모션 줄이기</a>를 켠 사람에게 보여 줄 때. 움직임 가운데 <b>흔들림이 가장 어지럽습니다</b>",
  ]),
  instead='움직임이 끝나는 시점을 알아야 하면 <a href="easing.html">이징 곡선</a>을 씁니다. 손가락을 따라가는 규칙은 <a href="gesture.html">제스처</a>에서, 여러 줄이 차례로 들어오게 하는 방법은 <a href="stagger.html">차례로 들어오기</a>에서 다룹니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="height:28px;border-radius:7px;background:var(--surface);border:1px solid var(--line);display:grid;place-items:center;font-size:9.5px;transform:scale(.96)">눌린 버튼</div>
                <span style="font-size:9px;color:var(--fg-muted)">0.96에서 1로 돌아옴</span>
              </div>''',
     "버튼을 누르는 느낌 내기", "움직임을 아주 작게 줍니다. <b>뻣뻣함을 크게 해서 거의 흔들리지 않게</b> 합니다"),
    ('''              <div style="width:100%;max-width:150px;height:62px;position:relative;border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">
                <div style="position:absolute;left:0;right:0;bottom:-6px;height:58%;background:var(--surface);border-top:1px solid var(--line);border-radius:6px 6px 0 0"></div>
              </div>''',
     "끌어 올린 시트에 속도 이어 주기", "손가락의 속도를 <b>그대로 이어받습니다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:flex;gap:4px;overflow:hidden">
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--bg);border:1px dashed var(--line)"></span>
              </div>''',
     "카드를 넘겨 다음 칸에 멈추기", "손을 놓는 순간의 <b>속도로</b> 움직여 다음 칸에 맞춰 멈춥니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="웹에는 표준 스프링이 없어서 <b>매 프레임 직접 계산</b>하거나 라이브러리를 씁니다.",
  code='''<span class="c">// 감쇠 진동: 목표를 지나쳤다 돌아온다</span>
<span class="k">function</span> spring(el, to, v0) {
  <span class="k">const</span> k = <span class="a">180</span>, c = <span class="a">22</span>, m = <span class="a">1</span>;     <span class="c">// 뻣뻣함 · 감쇠 · 질량</span>
  <span class="k">let</span> x = <span class="a">0</span>, v = v0 || <span class="a">0</span>, last = performance.now();

  (<span class="k">function</span> step(now) {
    <span class="k">const</span> dt = Math.min((now - last) / <span class="a">1000</span>, <span class="a">0.032</span>); last = now;
    <span class="k">const</span> a = (-k * (x - to) - c * v) / m;
    v += a * dt; x += v * dt;
    el.style.transform = <span class="s">`translateY(${</span>x.toFixed(<span class="a">2</span>)<span class="s">}px)`</span>;
    <span class="c">// 충분히 가까워지고 느려지면 끊는다</span>
    <span class="k">if</span> (Math.abs(x - to) &gt; <span class="a">0.4</span> || Math.abs(v) &gt; <span class="a">0.4</span>) requestAnimationFrame(step);
    <span class="k">else</span> el.style.transform = <span class="s">`translateY(${</span>to<span class="s">}px)`</span>;
  })(last);
}''',
  keys_heads="<th>알아 둘 규칙</th><th>자세한 내용</th>",
  keys=kbd([
    ("웹 표준에 스프링이 없는 점", "CSS에는 스프링이 없습니다. 대신 <code>linear()</code>로 스프링 <b>곡선을 점으로 찍어 옮기는</b> 방법이 생겼습니다"),
    ("계산을 멈추는 조건", "목표까지 거리와 속도가 <b>둘 다</b> 작아졌을 때 멈춥니다. 하나만 보면 제대로 멈추지 않습니다"),
    ("<code>dt</code>에 상한 두기", "탭을 다시 열면 <code>dt</code>가 몇 초로 커져서 요소가 <b>한 번에 멀리 튀어 나갑니다</b>"),
    ("이어받을 속도 구하기", "<code>pointerup</code> 직전 몇 프레임의 평균 속도를 씁니다. 마지막 한 프레임만 쓰면 값이 <b>튀기 쉽습니다</b>"),
    ("<code>prefers-reduced-motion</code>", "목표를 지나치지 않게 튕김을 0으로 내리거나, 움직임 없이 바로 끝 값으로 보냅니다"),
    ("초점을 옮기는 때", "스프링이 끝나기를 기다렸다가 초점을 옮기지 않습니다. <b>언제 끝날지 알 수 없기</b> 때문입니다"),
  ]),
  backend=rows([
    ("화면 쪽에서만 하는 계산", "모두 화면 쪽에서 계산합니다. 다만 <b>매 프레임 실행되는 코드</b>라서 느린 기기에서는 다른 작업이 늦어집니다."),
    ("멈추기를 기다려 요청하지 않기", "끝나는 시점이 정해져 있지 않기 때문에, 움직임이 멈추기를 기다렸다가 저장하면 저장이 <b>언제 시작될지 알 수 없습니다</b>."),
    ("배경 탭에서 멈추는 계산", "<code>requestAnimationFrame</code>은 배경 탭에서 멈춥니다. 그래서 탭으로 돌아오면 요소를 <b>끝 값으로 바로</b> 보냅니다."),
  ]),
  plat_lede="앱 플랫폼에서는 <b>스프링이 기본</b>이고, 웹에서만 직접 만들어야 합니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     curve(28, "105px", "웹 스프링"),
     "표준이 없어서 라이브러리(Motion, React Spring)를 쓰거나 직접 계산합니다. <code>linear()</code>로 곡선을 옮겨 넣기도 합니다."),
    ("iOS", "UISpringTimingParameters",
     '''              <div class="phone" role="img" aria-label="iOS 스프링 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:52%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"></div></div></div>''',
     "<b>시스템 애니메이션 대부분이 스프링</b>입니다. SwiftUI에서는 <code>.spring(response:dampingFraction:)</code>으로 적습니다."),
    ("안드로이드", "SpringAnimation",
     '''              <div class="phone" role="img" aria-label="안드로이드 스프링 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:26px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "<code>DynamicAnimation</code>과 Compose의 <code>spring()</code>을 씁니다. 뻣뻣함과 감쇠에는 <b>이름 붙은 기본값</b>이 몇 가지 있습니다."),
  ]),
  plat_note="\"아이폰처럼 자연스럽게 해 주세요\"라는 요청은 상당 부분 <b>스프링</b>을 말하는 것입니다. iOS는 시스템 애니메이션 대부분이 스프링이라서 웹에서 곡선만 쓰면 어딘가 다르게 느껴집니다. 다만 웹에는 표준이 없어서 <b>라이브러리를 들이거나 직접 계산</b>해야 하므로, 그만큼 일이 늘어난다는 점을 미리 말해 두는 편이 낫습니다.",
  siblings=siblings("spring"),
  related='''        <li><a href="easing.html"><b>이징 곡선</b><em>9부</em></a></li>
        <li><a href="gesture.html"><b>제스처</b><em>9부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>''',
)
