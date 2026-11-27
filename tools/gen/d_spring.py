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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">점선 = 목표 — 한 번 지나친다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뻣뻣함(stiffness) — 얼마나 세게 당기나</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">감쇠(damping) — 얼마나 빨리 잦아드나</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">끌던 속도를 그대로 이어받는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">끝나는 때가 정해져 있지 않다</div>
                </div>
              </div>'''

D = dict(
  slug="spring", ko="스프링", en="Spring",
  desc="목표를 지나쳤다 돌아오는 물리 기반 움직임. 끌던 속도를 이어받지만 끝나는 때가 정해져 있지 않다.",
  lede="곡선이 아니라 <b>용수철 계산</b>. <b>손으로 민 것 같은</b> 느낌을 내지만 끝나는 때가 정해져 있지 않습니다.",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>위 공은 <b>끝에서 멎는</b> 곡선, 아래 공은 <b>지나쳤다 돌아오는</b> 스프링입니다.<br>
          튕김을 0 으로 내리면 둘이 거의 같아지고, 끝까지 올리면 <b>글자가 읽히기 전에</b> 또 움직입니다.
          오른쪽 그래프에서 점선이 목표입니다 — 선이 점선을 <b>넘었다 돌아오는</b> 것이 스프링의 전부입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스프링, 용수철, 물리 기반 애니메이션"),
    ("영어", "spring animation, physics-based animation"),
    ("같이 쓰는 말",
     "세게 당기는 정도가 <b>뻣뻣함</b>(stiffness·tension), "
     "흔들림이 잦아드는 정도가 <b>감쇠</b>(damping·friction), "
     "움직이는 것의 무게가 <b>질량</b>(mass)입니다. "
     "목표를 지나치는 것을 <b>오버슈트</b>(overshoot), 잦아드는 흔들림을 <b>세틀링</b>이라 합니다. "
     "지나치지 않게 딱 맞춘 상태가 <b>임계 감쇠</b>(critically damped)입니다."),
    ("자주 잘못 부름",
     "<b>바운스</b> — 튕기는 느낌을 내는 <a href=\"easing.html\">이징 곡선</a>도 있지만, 그건 <b>길이가 정해진</b> 곡선입니다.<br>"
     "<b>이징</b> — 스프링은 곡선표가 아니라 <b>매 프레임 계산</b>입니다. <code>cubic-bezier</code>로 흉내만 냅니다.<br>"
     "<b>관성 스크롤</b> — 손을 떼도 미끄러지는 것은 <a href=\"gesture.html\">제스처</a> 쪽입니다."),
  ]),
  axes=ax("스프링"),
  oneline="<b>끌어서 다루는 것</b>에는 스프링, <b>순서대로 이어지는 것</b>에는 곡선. 끝나는 때를 알아야 하면 스프링은 맞지 않습니다.",
  s4_title="튕김별로", s4_hint="목표를 얼마나 지나치나",
  states=states([
    (curve(0, "140px", "튕김 없음"), "튕김 0", "지나치지 않는다. <b>ease-out 과 거의 같다</b>"),
    (curve(16, "140px", "약한 튕김"), "약하게", "살짝 지나쳤다 바로 선다. <b>가장 무난한 설정</b>"),
    (curve(36, "140px", "보통 튕김"), "보통", "두어 번 흔들린다. <b>끌어 넘기는 것</b>에 맞는다"),
    (curve(64, "140px", "강한 튕김"), "세게", "오래 흔들린다. <b>글자를 읽기 어렵다</b>"),
    (curve(88, "140px", "지나친 튕김"), "너무 세게", "고무공 같다. <b>장난감 느낌</b>이 난다"),
    ('''              <div style="width:100%;max-width:140px;height:72px;border:1px solid var(--line);border-radius:6px;background:var(--bg);display:grid;place-items:center">
                <span style="font-size:9.5px;color:var(--fg-muted)">모션 줄이기 — 튕김 없음</span>
              </div>''',
     "줄이기에서", "<b>지나침을 0 으로.</b> 흔들림이 가장 어지럽다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("곡선", "감쇠 진동", "목표를 <b>지나쳤다 돌아온다.</b> 이게 용수철의 모양이다"),
    ("목표선", "1.0", "점선. 여기서 멈추는 게 아니라 <b>여기를 중심으로</b> 흔들린다"),
    ("뻣뻣함", "stiffness", "클수록 <b>빨리</b> 당겨진다. 작으면 흐느적거린다"),
    ("감쇠", "damping", "클수록 <b>빨리 잦아든다.</b> 작으면 오래 흔들린다"),
    ("이어받는 속도", "initial velocity", "끌던 손가락 속도를 그대로 받는다 — <b>스프링의 진짜 값어치</b>"),
    ("끝", "정해져 있지 않다", "충분히 가까워지면 끊는다. <b>몇 ms 인지 미리 알 수 없다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스프링의 값어치는 '예뻐서'가 아니라 <b>끌던 속도를 이어받기</b> 때문입니다.
          손가락으로 시트를 빠르게 튕기면 그 속도 그대로 날아가고,
          천천히 밀면 천천히 자리 잡습니다 — <b>곡선으로는 흉내 낼 수 없는</b> 연결입니다.
          반대로 <b>끝나는 때를 알아야 하는</b> 곳에는 맞지 않습니다.
          '애니메이션이 끝나면 다음 것' 같은 이어 붙이기는 길이가 정해진 곡선 쪽이 쉽습니다.</p>''',
  do=ul([
    "<b>끌어서 다루는 것</b> — 시트, 카드 넘기기, 당겨서 새로고침",
    "손을 뗀 뒤 <b>이어지는 움직임</b>",
    "작고 자주 보는 <b>누르는 느낌</b> — 살짝 눌렸다 돌아오기",
  ]),
  dont=ul([
    "읽을 글이 실린 것 — <b>또 움직여서</b> 읽기를 방해한다",
    "<b>순서대로 이어 붙이는</b> 연출 — 끝나는 때를 모른다",
    "흔들림을 세 번 이상 — 거의 늘 과하다",
    "<a href=\"reducedmotion.html\">모션 줄이기</a>를 켠 사람에게 — <b>흔들림이 가장 어지럽다</b>",
  ]),
  instead='길이를 알아야 하면 <a href="easing.html">이징 곡선</a>, 손가락을 따라가는 규칙은 <a href="gesture.html">제스처</a>, 줄이 차례로면 <a href="stagger.html">차례로 들어오기</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="height:28px;border-radius:7px;background:var(--surface);border:1px solid var(--line);display:grid;place-items:center;font-size:9.5px;transform:scale(.96)">눌린 버튼</div>
                <span style="font-size:9px;color:var(--fg-muted)">0.96 → 1 로 돌아온다</span>
              </div>''',
     "누르는 느낌", "아주 작게. <b>뻣뻣하게, 거의 안 흔들리게</b>"),
    ('''              <div style="width:100%;max-width:150px;height:62px;position:relative;border:1px solid var(--line);border-radius:6px;background:var(--bg);overflow:hidden">
                <div style="position:absolute;left:0;right:0;bottom:-6px;height:58%;background:var(--surface);border-top:1px solid var(--line);border-radius:6px 6px 0 0"></div>
              </div>''',
     "끌어 올리는 시트", "손가락 속도를 <b>그대로 이어받는다</b>"),
    ('''              <div style="width:100%;max-width:150px;display:flex;gap:4px;overflow:hidden">
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="flex:none;width:52px;height:46px;border-radius:6px;background:var(--bg);border:1px dashed var(--line)"></span>
              </div>''',
     "카드 넘기기", "놓는 순간의 <b>속도로</b> 다음 칸에 붙는다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 스프링의 계약서",
  code_lede="웹에는 표준 스프링이 없어 <b>매 프레임 계산</b>하거나 라이브러리를 씁니다.",
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
  keys=kbd([
    ("표준이 없다", "CSS 에는 스프링이 없다. <code>linear()</code>로 <b>곡선을 베껴 넣는</b> 방법이 생겼다"),
    ("끝을 끊는 조건", "거리와 속도가 <b>둘 다</b> 작아졌을 때. 하나만 보면 안 멈춘다"),
    ("<code>dt</code>에 상한을 둔다", "탭을 다시 열면 <code>dt</code>가 몇 초가 되어 <b>튕겨 나간다</b>"),
    ("이어받는 속도", "<code>pointerup</code> 직전 몇 프레임의 평균을 쓴다. 마지막 한 프레임만 쓰면 <b>튄다</b>"),
    ("<code>prefers-reduced-motion</code>", "지나침을 0 으로 내리거나 그냥 끝 값으로 보낸다"),
    ("초점·읽기", "스프링이 끝나기를 기다렸다 초점을 옮기지 않는다 — <b>끝나는 때를 모른다</b>"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "전부 화면 쪽 계산입니다. 다만 <b>매 프레임 도는 코드</b>라 느린 기기에서 다른 일을 밀어냅니다."),
    ("끝을 기다려 요청하지 않는다", "끝나는 때가 정해져 있지 않으니, 움직임이 멎기를 기다렸다 저장하면 <b>얼마나 걸릴지 모릅니다</b>."),
    ("탭이 쉬면 멈춘다", "<code>requestAnimationFrame</code>은 배경 탭에서 멎습니다. 돌아오면 <b>끝 값으로 바로</b> 보냅니다."),
  ]),
  plat_lede="앱 쪽은 <b>스프링이 기본</b>이고, 웹만 직접 만듭니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     curve(28, "105px", "웹 스프링"),
     "표준이 없어 라이브러리(Motion, React Spring)를 쓰거나 계산합니다. <code>linear()</code>로 베껴 넣기도 합니다."),
    ("iOS", "UISpringTimingParameters",
     '''              <div class="phone" role="img" aria-label="iOS 스프링 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:52%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line)"></div></div></div>''',
     "<b>거의 모든 시스템 애니메이션이 스프링</b>입니다. SwiftUI 는 <code>.spring(response:dampingFraction:)</code>로 적습니다."),
    ("안드로이드", "SpringAnimation",
     '''              <div class="phone" role="img" aria-label="안드로이드 스프링 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:26px;border-radius:6px;background:var(--surface);border:1px solid var(--line)"></div></div></div>''',
     "<code>DynamicAnimation</code>·Compose 의 <code>spring()</code>이 있습니다. 뻣뻣함과 감쇠에 <b>이름 붙은 기본값</b>이 몇 개 있습니다."),
  ]),
  plat_note="\"아이폰처럼 자연스럽게\"라는 요청의 상당 부분이 사실 <b>스프링</b>입니다. iOS 는 시스템 애니메이션이 거의 다 스프링이라 웹에서 곡선만 쓰면 어딘가 다르게 느껴집니다. 다만 웹에 표준이 없어 <b>라이브러리를 들이거나 직접 계산</b>해야 하고, 그 비용을 미리 말해 두는 편이 낫습니다.",
  siblings=siblings("spring"),
  related='''        <li><a href="easing.html"><b>이징 곡선</b><em>9부</em></a></li>
        <li><a href="gesture.html"><b>제스처</b><em>9부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>''',
)
