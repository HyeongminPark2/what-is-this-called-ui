# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT = table(
  ["끝나는 때를 아는가", "들어올 내용의 자리를 미리 잡는가", "사용자가 기다려야 하는가", "내용이 들어올 때 화면이 덜컥거리는가"],
  [["스피너", "모름", "잡지 않음", "기다림", "덜컥거림"],
   ["스켈레톤", "모름", "잡아 둠", "기다림", "덜컥거리지 않음"],
   ["프로그레스 바", "알고 있음", "잡기도 함", "기다림", "덜컥거리지 않음"],
   ["낙관적 UI", "해당 없음", "잡아 둠", "기다리지 않음", "덜컥거리지 않음"]],
  me="스켈레톤")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:10px">
                <div data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;height:76px;display:flex;align-items:center;gap:26px;padding:0 26px">
                  <span data-pin="2" style="width:34px;height:34px;border-radius:50%;background:var(--ink-100);flex:none"></span>
                  <span style="flex:1;display:grid;gap:12px">
                    <span data-pin="3" style="height:12px;width:58%;border-radius:4px;background:var(--ink-100)"></span>
                    <span class="pin-out" data-pin="4" style="height:10px;width:34%;border-radius:4px;background:var(--ink-100)"></span>
                  </span>
                  <span class="pin-tr" data-pin="5" style="height:12px;width:62px;border-radius:4px;background:var(--ink-100)"></span>
                </div>
              </div>'''

D = dict(
  slug="skeleton", ko="스켈레톤", en="Skeleton · Placeholder",
  desc="스켈레톤이 무엇인지, 스피너와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="스켈레톤은 들어올 내용의 <b>모양대로 미리 자리를 잡아 두는</b> 회색 뼈대입니다. 기다림이 짧게 느껴지고, 내용이 이미 잡아 둔 자리에 들어오기 때문에 화면이 덜컥거리지 않습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>두 버튼을 번갈아 눌러 보세요.</b> 누를 때마다 화면이 몇 px 흔들렸는지 아래에 적힙니다.
          스켈레톤은 <b>0px</b>이고 스피너는 수십 px입니다. 내용이 들어오면서 화면이 이렇게 흔들리는 것을 <b>레이아웃 시프트</b>라고 부르는데,
          스켈레톤은 레이아웃 시프트를 없애려고 씁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스켈레톤, 스켈레톤 화면, 뼈대 화면"),
    ("영어", "skeleton, skeleton screen, placeholder, ghost element"),
    ("같이 쓰는 말", "뼈대 위로 지나가는 빛은 <b>시머</b>(shimmer), 회색 덩어리 하나하나는 <b>플레이스홀더</b>라고 부릅니다. 실제 내용과 모양이 거의 똑같은 뼈대는 <b>고스트</b>라고도 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>로딩</b> — 스피너와 한데 묶어 부르면 '들어올 자리를 미리 잡느냐'라는 중요한 차이가 드러나지 않습니다.<br>"
     "<b>와이어프레임</b> — 와이어프레임은 설계 단계에서 그리는 그림이고, 스켈레톤은 <b>실제로 돌아가는 화면의 한 상태</b>입니다.<br>"
     "<b>더미 데이터</b> — 자리에 가짜 글자를 채워 넣는 더미 데이터와 달리, 스켈레톤에는 <b>글자를 넣지 않습니다</b>."),
  ]),
  axes=WAIT,
  oneline="스켈레톤은 <b>들어올 내용의 모양을 알 때만</b> 쓸 수 있습니다. 모양을 모르는 채로 아무 뼈대나 깔아 두면 실제 내용과 크기가 맞지 않아, 내용이 들어올 때 결국 화면이 덜컥거립니다.",
  states=states([
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div><div class="skl" style="height:7px;width:62%"></div></div>', bars="", label="스켈레톤이 깔린 모습"), "뼈대를 깔아 둔 상태", "들어올 줄 수와 줄 길이만큼 미리 자리를 잡아 둡니다"),
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div><div style="position:absolute;right:6px;top:8px;font-size:7px;color:var(--accent);font-weight:800">빛이 지나감</div>', bars="", label="시머가 지나가는 모습"), "시머가 지나갈 때", "빛이 한 방향으로 지나가면서 화면이 멈춘 것이 아니라 불러오는 중이라는 것을 알립니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w40"></div></div>', bars="", label="내용이 들어온 모습"), "내용이 들어왔을 때", "뼈대가 있던 <b>같은 자리에</b> 글자가 들어차므로 화면이 밀리지 않습니다"),
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:7px;color:var(--danger);font-weight:700">모양이 달라 덜컥거림</div>', bars="", label="모양이 안 맞아 덜컥거리는 모습"), "뼈대와 내용의 모양이 다를 때", "뼈대와 실제 내용의 줄 수나 높이가 다르면 <b>스피너를 쓸 때와 똑같이</b> 덜컥거립니다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:7px;top:26px;right:7px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div>', bars="", label="일부만 스켈레톤인 모습"), "일부만 뼈대로 둘 때", "먼저 도착한 내용은 바로 보여 주고, 아직 오지 않은 칸만 뼈대로 둡니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;padding:8px"><span style="font-size:8px;color:var(--danger);font-weight:700">불러오지 못했습니다</span><span class="mini__btn" style="font-size:7.5px;padding:2px 6px">다시 시도</span></div>', bars="", label="실패로 끝난 모습"), "실패로 끝났을 때", "불러오기에 실패했는데 뼈대가 계속 반짝이면 안 됩니다. 실패 화면으로 바뀌는 경로를 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("줄 틀", "row · container", "<b>실제 줄과 높이가 같아야 합니다.</b> 높이가 어긋나면 내용이 들어올 때 화면이 밀리므로 스켈레톤을 쓴 효과가 없어집니다"),
    ("동그란 자리", "avatar placeholder", "아바타가 들어올 자리입니다. 크기와 모양까지 실제 아바타에 맞춥니다"),
    ("긴 글줄 자리", "line placeholder", "제목이 들어올 자리입니다. 줄마다 길이를 조금씩 다르게 해야 실제 목록처럼 보입니다"),
    ("짧은 글줄 자리", "secondary line", "보조 설명이 들어올 자리입니다. 모든 줄을 같은 길이로 깔면 목록이 아니라 표처럼 보입니다"),
    ("끝 열 자리", "trailing placeholder", "금액이나 시각처럼 줄 오른쪽 끝에 붙는 값의 자리입니다. 뼈대를 그릴 때 빠뜨리기 쉽습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          회색 덩어리 위로 지나가는 빛을 <b>시머</b>(shimmer)라고 부르는데, 테두리가 없는 효과라서 그림에 번호를 붙이지 못했습니다.
          사용자가 움직임을 줄여 달라는 설정을 켜 두었다면 <b>시머를 꺼야</b> 합니다.</p>''',
  do=ul([
    "목록·카드·표처럼 <b>모양이 정해진 것</b>을 불러올 때",
    "첫 화면을 불러올 때. 자리를 잡아 두면 사용자가 느끼는 속도가 눈에 띄게 빨라집니다",
    "내용이 들어오면서 화면이 밀리는 곳을 고칠 때. 레이아웃 시프트를 없앱니다",
  ]),
  dont=ul([
    "들어올 모양을 모를 때. 실제 내용과 맞지 않는 뼈대는 스피너보다 나쁩니다",
    "0.3초 안에 끝나는 일을 기다릴 때. 뼈대가 깜빡이기만 하고 사라집니다",
    "버튼 하나처럼 자리가 작을 때. 스피너를 씁니다",
    "뼈대에 가짜 글자를 넣을 때. 사용자가 진짜 내용으로 오해하므로 <b>글자는 넣지 않습니다</b>",
  ]),
  instead='들어올 내용의 모양을 모르면 <a href="spinner.html">스피너</a>를 쓰고, 끝나는 때를 알면 <a href="progress.html">프로그레스 바</a>를 씁니다. 기다림 자체를 없앨 수 있다면 <a href="optimistic.html">낙관적 UI</a>가 낫고, 불러올 것이 아예 없을 때는 <a href="empty.html">빈 상태</a>를 보여 줍니다.',
  cases=cases([
    (mini('<div style="margin-top:8px;display:flex;gap:6px;align-items:center"><div class="skl skl--circle" style="width:16px;height:16px"></div><div style="flex:1;display:grid;gap:4px"><div class="skl" style="height:6px;width:60%"></div><div class="skl" style="height:5px;width:40%"></div></div></div><div style="margin-top:7px;display:flex;gap:6px;align-items:center"><div class="skl skl--circle" style="width:16px;height:16px"></div><div style="flex:1;display:grid;gap:4px"><div class="skl" style="height:6px;width:70%"></div><div class="skl" style="height:5px;width:35%"></div></div></div>', bars="", tall=False, label="목록 스켈레톤 재현"),
     "목록이 들어올 자리 잡아 두기", "줄마다 같은 뼈대를 반복하되, 줄 길이만 조금씩 다르게 합니다"),
    (mini('<div style="margin-top:8px;display:grid;grid-template-columns:1fr 1fr;gap:6px"><div><div class="skl" style="height:26px"></div><div class="skl" style="height:5px;width:70%;margin-top:4px"></div></div><div><div class="skl" style="height:26px"></div><div class="skl" style="height:5px;width:55%;margin-top:4px"></div></div></div>', bars="", tall=False, label="카드 그리드 스켈레톤 재현"),
     "카드 그리드가 들어올 자리 잡아 두기", "썸네일 비율까지 맞춰 두어야 이미지가 들어올 때 카드가 밀리지 않습니다"),
    (mini('<div class="mini__bg" style="padding-top:7px"><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:7px;right:7px;top:24px;display:grid;gap:5px"><div class="skl" style="height:6px;width:80%"></div><div class="skl" style="height:6px;width:55%"></div></div>', bars="", tall=False, label="일부만 스켈레톤인 재현"),
     "제목은 먼저 보여 주고 본문만 뼈대로 두기", "제목은 캐시에서 꺼내 바로 보여 주고 본문만 뼈대로 둡니다. 세 가지 가운데 가장 빨라 보이는 방법입니다"),
  ]),
  code_lede="반짝이는 회색 상자는 쉽게 만들 수 있고, 손이 많이 가는 부분은 <b>뼈대를 실제 줄과 같은 높이로 맞추는 일</b>입니다. 줄 높이를 고정해 두면 뼈대와 실제 줄의 높이가 거의 저절로 맞습니다.",
  code='''<span class="c">&lt;!-- 글자를 넣지 않는다. 읽을 것이 없다고 알린다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"row"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"skl skl--circle"</span>&gt;&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"skl"</span> <span class="a">style</span>=<span class="s">"height:12px;width:58%"</span>&gt;&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 줄 높이를 고정해야 뼈대와 실제 줄이 딱 맞는다 */</span>
.row <span class="a">{</span> <span class="t">height</span>: 72px; <span class="a">}</span>

<span class="c">/* 움직임을 줄여 달라면 반짝임을 끈다 */</span>
@media (prefers-reduced-motion: reduce) <span class="a">{</span>
  .skl::after <span class="a">{</span> <span class="t">animation</span>: none; <span class="a">}</span>
<span class="a">}</span>''',
  keys_heads="<th>상황</th><th>그때 일어나야 하는 일</th>",
  keys=kbd([
    ("스크린 리더로 읽을 때", "뼈대에는 읽을 내용이 없으므로 <code>aria-hidden=\"true\"</code>로 숨기고, 바깥 영역에 <code>aria-busy=\"true\"</code>를 겁니다"),
    ("포커스를 다룰 때", "뼈대에는 누를 것이 없으니 포커스가 가지 않습니다"),
    ("내용이 들어올 때", "<code>aria-busy</code>를 지웁니다. 뼈대가 사라질 때 포커스가 사라진 요소에 남아 있지 않게 합니다"),
    ("움직임 줄이기 설정이 켜져 있을 때", "시머를 끕니다. 회색 자리만 남겨도 내용이 들어올 자리를 잡아 두는 역할은 그대로 합니다"),
    ("불러오기에 실패했을 때", "뼈대를 치우고 다시 시도할 수 있는 버튼을 보여 줍니다"),
  ]),
  backend=rows([
    ("응답의 스키마를 미리 아는 것과 같은 상황", "스켈레톤을 그린다는 것은 응답을 받기 전에 그 응답의 <b>모양을 알고 있다</b>는 뜻이고, 타입이 정해진 응답과 같은 상황입니다. 응답의 모양을 모르면 뼈대를 그릴 수 없습니다."),
    ("레이아웃 시프트는 배열 재할당과 같은 일", "크기를 모르는 채로 자리를 잡았다가 내용이 들어오면서 늘어나는 것은, 용량을 정하지 않은 배열에 값을 넣다가 공간이 모자라 다시 할당하는 것과 같습니다. <b>두 경우 모두 미리 크기를 잡아 두면 다시 할당하거나 화면이 흔들리는 일이 없습니다.</b>"),
    ("일부만 뼈대로 두는 것은 부분 응답과 같은 구조", "캐시에 있는 것은 바로 그리고, 캐시에 없는 칸만 뼈대로 둡니다. 캐시 값을 먼저 쓰고 뒤에서 새 값을 받아 오는 stale-while-revalidate와 같은 구조입니다."),
    ("사용자가 느끼는 지연 줄이기", "스켈레톤을 쓴다고 실제 응답이 빨라지지는 않고, 사용자가 <b>기다린다고 느끼는 시간</b>만 줄어듭니다. 그래도 사용자는 느끼는 시간으로 속도를 판단하기 때문에 쓸 가치가 있습니다."),
  ]),
  plat_lede="스켈레톤은 웹에서 나온 기법이라서 모바일 디자인 지침에는 따로 정해진 이름이 없습니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div>', bars="", label="웹 스켈레톤 재현"),
     "<b>스켈레톤</b> · 웹에서 가장 널리 쓰이고, 스켈레톤이라는 이름도 웹에서 자리 잡았습니다. 시머를 넣는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:6px"><div style="height:8px;border-radius:3px;background:#2a2f39;opacity:.35"></div><div style="height:8px;width:60%;border-radius:3px;background:#2a2f39;opacity:.35"></div></div>', "iOS 자리 표시 재현"),
     "<b>이름이 따로 없습니다.</b> 지침에는 '<b>자리 표시 내용</b>(placeholder content)을 보여 주라'는 말만 있고, 시머를 쓰는 앱과 쓰지 않는 앱이 모두 많습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:6px"><div style="height:8px;border-radius:4px;background:var(--line-strong);opacity:.6"></div><div style="height:8px;width:55%;border-radius:4px;background:var(--line-strong);opacity:.6"></div></div>', "안드로이드 로딩 자리 재현"),
     "<b>플레이스홀더</b>(Placeholder) · iOS와 마찬가지로 따로 정한 부품은 없고, '로딩 중 자리 표시' 패턴으로 다룹니다."),
  ]),
  plat_note="\"스켈레톤 넣어 주세요\"라는 요청은 웹 개발자에게는 바로 통하지만, 네이티브 앱에는 그런 이름의 표준 부품이 없습니다. 그래서 <b>어떤 모양으로 몇 줄을 깔지</b>도 함께 정해 주어야 합니다. 이 부분을 정하지 않으면 뼈대가 실제 줄과 맞지 않아 내용이 들어올 때 결국 덜컥거립니다.",
  siblings=siblings("skeleton"),
  related='''        <li><span class="na"><b>레이아웃 시프트</b><em>1부</em></span></li>
        <li><a href="thumbnail.html"><b>썸네일과 종횡비</b><em>5부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="virtual.html"><b>가상 스크롤</b><em>10부</em></a></li>''',
)
