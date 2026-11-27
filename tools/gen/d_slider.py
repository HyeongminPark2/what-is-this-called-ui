# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div style="display:flex;align-items:center;gap:40px;margin-bottom:24px">
                    <span class="pin-out" data-pin="1" style="font-size:12px;font-weight:700">이 금액을 넘으면 알림</span>
                    <span class="pin-tr" data-pin="2" style="font-size:12px;font-weight:800;font-variant-numeric:tabular-nums">₩300,000</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="position:relative;height:7px;border-radius:99px;background:var(--line);margin:0 26px 26px">
                    <span class="pin-tr" data-pin="4" style="position:absolute;left:0;top:0;bottom:0;width:30%;border-radius:99px;background:var(--accent)"></span>
                    <span data-pin="5" style="position:absolute;left:30%;top:50%;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:50%;background:var(--surface);border:2px solid var(--accent);box-shadow:var(--e1)"></span>
                  </div>
                  <div class="pin-out" data-pin="6" style="display:flex;justify-content:space-between;font-size:10.5px;color:var(--fg-muted);padding:0 26px"><span>0</span><span>50만</span><span>100만</span></div>
                </div>
              </div>'''

D = dict(
  slug="slider", ko="슬라이더", en="Slider · Range",
  desc="슬라이더가 무엇인지, 숫자 입력이나 세그먼티드 컨트롤과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="슬라이더는 정해진 <b>범위 안에서</b> 손잡이를 끌어 값을 고르는 막대입니다. 값을 대략 맞추기에는 빠르지만, 정확한 값을 맞추기는 어렵습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>손잡이를 잡고 <kbd>←</kbd><kbd>→</kbd>를 눌러 보세요. 손잡이가 눈금 한 칸씩 움직이고, <kbd>Home</kbd>·<kbd>End</kbd>를 누르면 양 끝까지 갑니다.<br>
          이번에는 첫 칸에 <b>123,456</b>을 적어 보세요. 눈금(step)이 1만 원 단위라서 값이 <b>120,000으로 맞춰집니다</b>.
          이처럼 눈금을 정하면 눈금 사이의 값은 고를 수 없게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "슬라이더, 범위 입력, 레인지"),
    ("영어", "slider, range input"),
    ("같이 쓰는 말", "잡고 끄는 동그라미는 <b>손잡이</b>(thumb), 바탕 막대는 <b>트랙</b>, 손잡이가 지나온 쪽은 <b>채움</b>(fill), 손잡이가 멈추는 간격은 <b>눈금</b>(step), 양 끝에 적는 글자는 <b>눈금 표시</b>라고 부릅니다. 손잡이가 둘이면 <b>범위 슬라이더</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>프로그레스 바</b> — 생김새는 닮았지만 프로그레스 바는 사용자가 <b>조작할 수 없는</b> 읽기 전용 표시입니다.<br>"
     "<b>스위치</b> — 손잡이가 움직인다고 모두 슬라이더는 아닙니다. 스위치는 켜고 끄는 일만 합니다.<br>"
     "<b>캐러셀</b> — 밀어서 움직이는 동작은 닮았지만, 캐러셀은 값을 고르지 않고 내용을 넘깁니다."),
  ]),
  axes=ax("슬라이더"),
  oneline="슬라이더는 값을 <b>대략 맞추기</b>에는 좋지만 <b>정확히 맞추기</b>에는 알맞지 않습니다. 그래서 정확한 값이 필요하면 숫자 칸을 옆에 함께 둡니다.",
  states=states([
    (mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:30%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:30%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span></div>', bars="", label="기본 슬라이더"), "기본", "채운 쪽과 채우지 않은 쪽이 구분되어야 합니다"),
    (mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:62%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:62%;top:50%;width:9px;height:9px;margin:-4.5px 0 0 -4.5px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></span></span></div>', bars="", label="끄는 중"), "끄는 중", "손잡이가 커지고 둘레에 링이 생깁니다. 손가락에 가려도 지금 끌고 있다는 것을 알 수 있게 하려는 표시입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div style="font-size:7px;font-weight:800;text-align:center;margin-bottom:3px">₩620,000</div><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:62%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:62%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span></div>', bars="", label="값이 보이는 슬라이더"), "값 표시", "<b>지금 값이 숫자로 보이지 않으면 쓸 수 없으므로</b> 손잡이 위나 옆에 꼭 적습니다"),
    (mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:28%;top:0;bottom:0;width:38%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:28%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span><span style="position:absolute;left:66%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span></div>', bars="", label="범위 슬라이더"), "범위", "손잡이 두 개로 최솟값과 최댓값을 함께 고릅니다. 두 손잡이가 서로를 넘어가지 않게 막습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:50%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:50%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span><div style="display:flex;justify-content:space-between;font-size:5px;color:var(--fg-muted);margin-top:3px"><span>작게</span><span>보통</span><span>크게</span></div></div>', bars="", label="눈금이 적은 슬라이더"), "눈금 셋", "고를 수 있는 칸이 셋뿐이면 <b>세그먼티드 컨트롤이 더 분명합니다</b>"),
    (mini('<div style="margin-top:14px;padding:0 6px;opacity:.45"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:30%;background:var(--line-strong);border-radius:99px"></span><span style="position:absolute;left:30%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--line-strong)"></span></span></div>', bars="", label="비활성 슬라이더"), "비활성", "움직일 수 없는 슬라이더입니다. 왜 움직일 수 없는지 적어 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("라벨", "label", "무엇을 정하는 값인지 단위까지 적습니다"),
    ("지금 값", "value", "<b>지금 값을 숫자로 보여 줍니다.</b> 숫자가 없으면 지금 얼마를 골랐는지 알 수 없어서 슬라이더를 쓸 수 없습니다"),
    ("트랙", "track", "고를 수 있는 전체 범위를 나타내며, 양 끝이 어디인지 보여 줍니다"),
    ("채움", "fill", "손잡이가 지나온 쪽을 채워서 지금 값이 범위의 어디쯤인지 한눈에 알립니다"),
    ("손잡이", "thumb · knob", "끌기 위해 잡는 부분입니다. 손가락으로 잡으려면 지름이 20px 이상이어야 합니다"),
    ("눈금 표시", "tick labels", "양 끝과 가운데만 적어도 충분합니다. 눈금마다 다 적으면 글자가 많아 읽기 어렵습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않지만 <b>눈금</b>(step)도 슬라이더를 이루는 요소입니다. 눈금을 1만 원 단위로 정하면 123,456을 넣어도 120,000으로 맞춰집니다.
          덕분에 값을 고르기는 쉬워지지만, 눈금 사이의 값은 고를 수 없게 됩니다.</p>''',
  do=ul([
    "밝기, 소리, 글자 크기처럼 <b>대략</b> 맞추면 되는 값일 때",
    "최솟값과 최댓값이 얼마인지, 범위가 눈에 보여야 할 때",
    "밝기를 끄는 동안 화면이 밝아지는 것처럼, 값을 바꾸면 <b>결과가 바로 보일 때</b>",
  ]),
  dont=ul([
    "정확한 값이 필요할 때. 숫자 칸을 옆에 함께 두지 않으면 정확히 맞출 수 없습니다",
    "범위가 1~10,000처럼 아주 넓을 때. 손잡이를 1픽셀만 움직여도 값이 수십씩 바뀝니다",
    "고를 칸이 두세 개뿐일 때. 세그먼티드 컨트롤이나 라디오를 씁니다",
    "값을 숫자로 보여 주지 않을 때. 지금 얼마인지 모르면 슬라이더를 쓸 수 없습니다",
  ]),
  instead='정확한 값이면 <a href="field.html">텍스트 필드</a>(숫자), 칸이 셋이면 <a href="segmented.html">세그먼티드</a>, 읽기만 하면 <a href="progress.html">프로그레스 바</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="flex:1;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:40%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:40%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span><span style="border:1px solid var(--line-strong);border-radius:2px;font-size:5px;padding:1px 3px">400,000</span></div>', bars="", tall=False, label="숫자 칸을 붙인 재현"),
     "숫자 칸과 함께", "슬라이더를 끌어 대략 맞추고, 숫자 칸에 적어 정확히 맞춥니다. <b>슬라이더를 쓸 때 가장 쓸모 있는 조합</b>입니다"),
    (mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:28%;top:0;bottom:0;width:38%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:28%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span><span style="position:absolute;left:66%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span></div>', bars="", tall=False, label="범위 슬라이더 재현"),
     "범위", "가격대 필터처럼 최솟값과 최댓값을 함께 고를 때 씁니다"),
    (mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:66%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:66%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span><div style="display:flex;justify-content:space-between;font-size:5px;color:var(--fg-muted);margin-top:3px"><span>🔈</span><span>🔊</span></div></div>', bars="", tall=False, label="즉시 반영 재현"),
     "즉시 반영", "소리나 밝기처럼 손잡이를 끄는 동안 결과가 함께 바뀝니다"),
  ]),
  code_lede="<code>&lt;input type=\"range\"&gt;</code>를 쓰면 키보드 조작과 스크린 리더 지원을 따로 만들지 않아도 됩니다. 반면 슬라이더를 직접 그리면 이 기능을 모두 다시 만들어야 합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"amt"</span>&gt;이 금액을 넘으면 알림&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"range"</span> <span class="a">id</span>=<span class="s">"amt"</span>
       <span class="a">min</span>=<span class="s">"0"</span> <span class="a">max</span>=<span class="s">"1000000"</span> <span class="a">step</span>=<span class="s">"10000"</span> <span class="a">value</span>=<span class="s">"300000"</span>&gt;
&lt;<span class="t">input</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">aria-label</span>=<span class="s">"금액 직접 입력"</span>&gt;

<span class="c">// 막대와 숫자 칸을 양쪽으로 잇는다</span>
range.addEventListener(<span class="s">'input'</span>, () =&gt; num.value = fmt(range.value));
num.addEventListener(<span class="s">'input'</span>, () =&gt; range.value = clamp(parse(num.value)));

<span class="c">/* 색만 바꾼다 */</span>
input[type=range] <span class="a">{</span> <span class="t">accent-color</span>: var(--accent); <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>←</kbd><kbd>→</kbd>", "눈금 한 칸씩 움직입니다"),
    ("<kbd>PageUp</kbd><kbd>PageDown</kbd>", "한 번에 크게 움직입니다. 범위가 넓을 때 꼭 필요합니다"),
    ("<kbd>Home</kbd><kbd>End</kbd>", "최솟값이나 최댓값으로 바로 갑니다"),
    ("스크린 리더", "<code>aria-valuenow</code>와 함께 <code>aria-valuetext</code>로 <b>사람이 알아듣기 쉬운 값</b>을 줍니다. 예를 들어 '300000' 대신 '30만 원'으로 읽게 합니다"),
    ("손가락", "손잡이는 20px 이상으로 그립니다. 트랙은 얇게 그려도 되지만, 손가락으로 누를 수 있는 영역은 크게 둡니다"),
  ]),
  backend=rows([
    ("눈금 = 양자화", "<code>step</code>은 고를 수 있는 값을 일정한 간격의 값으로 제한합니다. 이 간격은 저장할 값의 정밀도와 맞춰야 하는데, 화면은 1만 원 단위인데 DB 는 원 단위라면 단위가 다른 값이 섞여 들어옵니다."),
    ("끄는 동안 보낼 것인가", "<code>input</code> 이벤트는 끄는 내내 일어나고, <code>change</code> 이벤트는 손을 뗄 때 한 번 일어납니다. 그래서 값을 서버에 보낸다면 <b><code>change</code>에서</b> 보내거나 디바운스를 겁니다."),
    ("범위 슬라이더 = 구간", "최솟값과 최댓값 두 개를 보내고, 서버는 <b>min ≤ max</b>인지 다시 검증해야 합니다. 화면에서 막아 두어도 요청 자체는 조작될 수 있기 때문입니다."),
    ("기본값이 곧 질의", "슬라이더 기본값이 첫 화면에서 보내는 질의의 조건을 정합니다. 기본 범위를 넓게 잡아 두면 첫 질의가 가장 많은 데이터를 다루게 되어 무거워집니다."),
  ]),
  plat_lede="슬라이더는 플랫폼이 달라도 이름과 쓰임이 잘 통하는 편이고, 손잡이 크기와 값을 보여 주는 방식만 다릅니다.",
  plats=plats([
    ("웹", "<code>&lt;input type=\"range\"&gt;</code>",
     mini('<div style="margin-top:14px;padding:0 6px"><span style="display:block;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:40%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:40%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--surface);border:1.5px solid var(--accent)"></span></span></div>', bars="", label="웹 슬라이더 재현"),
     "<b>슬라이더</b> · 손잡이가 둘인 범위 슬라이더는 표준 부품이 없어서 직접 만들어야 합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px;display:flex;align-items:center;gap:4px"><span style="font-size:7px">🔈</span><span style="flex:1;position:relative;height:3px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:55%;background:#0a84ff;border-radius:99px"></span><span style="position:absolute;left:55%;top:50%;width:11px;height:11px;margin:-5.5px 0 0 -5.5px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.3)"></span></span><span style="font-size:7px">🔊</span></div>', "iOS 슬라이더 재현"),
     "<b>슬라이더</b>(Slider) · 손잡이가 크고 하얗습니다. 트랙 양 끝에 <b>아이콘</b>을 두어 무엇을 조절하는지 알리는 관례가 있습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px"><span style="display:block;position:relative;height:4px;border-radius:99px;background:var(--line)"><span style="position:absolute;left:0;top:0;bottom:0;width:55%;background:var(--accent);border-radius:99px"></span><span style="position:absolute;left:55%;top:50%;width:4px;height:14px;margin:-7px 0 0 -2px;border-radius:99px;background:var(--accent)"></span></span><div style="position:absolute;left:48%;top:-12px;background:var(--accent);color:#fff;font-size:6px;border-radius:99px;padding:1px 4px">55</div></div>', "안드로이드 슬라이더 재현"),
     "<b>슬라이더</b>(Slider) · 손잡이가 <b>세로 막대</b> 모양이고, 끄는 동안 지금 값이 손잡이 위에 <b>말풍선</b>으로 뜹니다."),
  ]),
  plat_note="안드로이드에서는 끄는 동안 값이 <b>말풍선으로 손잡이 위에</b> 뜹니다. 손가락이 손잡이를 가려서 값을 볼 수 없는 문제를 해결하려는 장치인데, 웹에서 슬라이더를 직접 만들 때 특히 자주 빠뜨립니다. 값을 라벨 옆에 적어 두어도 같은 문제를 해결할 수 있습니다.",
  siblings=siblings("slider"),
  related='''        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><span class="na"><b>스테퍼</b><em>4부</em></span></li>
        <li><span class="na"><b>필터와 패싯</b><em>10부</em></span></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
