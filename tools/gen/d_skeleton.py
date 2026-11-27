# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT = table(
  ["끝나는 때를 아나", "들어올 자리를 잡나", "사용자가 기다리나", "화면이 덜컥거리나"],
  [["스피너", "모른다", "안 잡는다", "기다린다", "덜컥거린다"],
   ["스켈레톤", "모른다", "잡는다", "기다린다", "안 덜컥거린다"],
   ["프로그레스 바", "안다", "잡기도 한다", "기다린다", "안 덜컥거린다"],
   ["낙관적 UI", "해당 없음", "잡는다", "안 기다린다", "안 덜컥거린다"]],
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
  desc="스켈레톤이 무엇이고 스피너와 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="들어올 내용의 <b>모양대로 미리 자리를 잡아 두는</b> 회색 뼈대. 기다림이 짧게 느껴지고, 내용이 들어올 때 화면이 덜컥거리지 않습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>두 버튼을 번갈아 눌러 보세요.</b> 아래에 화면이 몇 px 흔들렸는지 적힙니다.
          스켈레톤은 <b>0px</b>, 스피너는 수십 px입니다. 이 흔들림을 <b>레이아웃 시프트</b>라 부르고,
          스켈레톤이 존재하는 이유가 바로 이걸 없애는 것입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스켈레톤, 스켈레톤 화면, 뼈대 화면"),
    ("영어", "skeleton, skeleton screen, placeholder, ghost element"),
    ("같이 쓰는 말", "지나가는 빛을 <b>시머</b>(shimmer), 회색 덩어리 하나하나를 <b>플레이스홀더</b>라 합니다. 모양이 거의 똑같으면 <b>고스트</b>라고도 합니다."),
    ("자주 잘못 부름",
     "<b>로딩</b> — 스피너와 뭉뚱그려 부르면 '자리를 잡느냐'라는 결정적 차이가 사라집니다.<br>"
     "<b>와이어프레임</b> — 와이어프레임은 설계 단계의 그림이고, 스켈레톤은 <b>실제로 돌아가는 화면의 한 상태</b>입니다.<br>"
     "<b>더미 데이터</b> — 가짜 글자를 넣는 것과는 다릅니다. 스켈레톤에는 <b>글자를 넣지 않습니다</b>."),
  ]),
  axes=WAIT,
  oneline="스켈레톤은 <b>들어올 모양을 알 때만</b> 쓸 수 있습니다. 모양을 모르면서 아무 뼈대나 깔면 내용이 들어올 때 결국 덜컥거립니다.",
  states=states([
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div><div class="skl" style="height:7px;width:62%"></div></div>', bars="", label="스켈레톤이 깔린 모습"), "표시", "들어올 줄 수와 길이를 미리 잡아 둔다"),
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div><div style="position:absolute;right:6px;top:8px;font-size:7px;color:var(--accent);font-weight:800">→ 반짝임</div>', bars="", label="시머가 지나가는 모습"), "시머", "빛이 한 방향으로 지나간다. '멈춘 게 아니다'라는 신호"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w60"></div><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w40"></div></div>', bars="", label="내용이 들어온 모습"), "내용 들어옴", "<b>같은 자리에</b> 글자가 들어찬다. 밀리지 않는다"),
    (mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:7px;color:var(--danger);font-weight:700">모양이 다름 → 덜컥</div>', bars="", label="모양이 안 맞아 덜컥거리는 모습"), "안 맞는 뼈대", "줄 수나 높이가 다르면 <b>스피너와 똑같이</b> 덜컥거린다"),
    (mini('<div class="mini__bg"><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:7px;top:26px;right:7px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div>', bars="", label="일부만 스켈레톤인 모습"), "일부만", "먼저 온 것은 보여 주고 아직 안 온 칸만 뼈대로 둔다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;padding:8px"><span style="font-size:8px;color:var(--danger);font-weight:700">불러오지 못했습니다</span><span class="mini__btn" style="font-size:7.5px;padding:2px 6px">다시 시도</span></div>', bars="", label="실패로 끝난 모습"), "실패로 끝남", "뼈대가 계속 반짝이면 안 된다. 끝나는 길을 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("줄 틀", "row · container", "<b>실제 줄과 높이가 같아야 한다.</b> 여기가 어긋나면 스켈레톤을 쓴 보람이 없다"),
    ("동그란 자리", "avatar placeholder", "아바타가 들어올 자리. 크기와 모양까지 맞춘다"),
    ("긴 글줄 자리", "line placeholder", "제목이 들어올 자리. 길이를 조금씩 다르게 해야 진짜처럼 보인다"),
    ("짧은 글줄 자리", "secondary line", "보조 설명 자리. 모든 줄을 같은 길이로 깔면 표처럼 보인다"),
    ("끝 열 자리", "trailing placeholder", "금액·시각처럼 오른쪽에 붙는 것. 빠뜨리기 쉬운 칸이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          회색 덩어리 위로 지나가는 빛이 <b>시머</b>(shimmer)입니다. 테두리가 없어 번호를 못 붙였습니다.
          움직임을 줄여 달라는 설정이 켜져 있으면 <b>시머를 꺼야</b> 합니다.</p>''',
  do=ul([
    "목록·카드·표처럼 <b>모양이 정해진 것</b>을 불러올 때",
    "첫 화면 — 자리를 잡아 두면 체감 속도가 눈에 띄게 빨라집니다",
    "내용이 들어오며 화면이 밀리는 곳 (레이아웃 시프트를 없앱니다)",
  ]),
  dont=ul([
    "들어올 모양을 모를 때 — 안 맞는 뼈대는 스피너보다 나쁩니다",
    "0.3초 안에 끝나는 일 — 깜빡임만 남습니다",
    "버튼 하나처럼 자리가 작을 때 → 스피너",
    "가짜 글자를 넣기 — 진짜 내용으로 오해합니다. <b>글자는 넣지 않습니다</b>",
  ]),
  instead='모양을 모르면 <a href="spinner.html">스피너</a>, 끝나는 때를 알면 <a href="progress.html">프로그레스 바</a>, 기다림을 없앨 수 있으면 <a href="optimistic.html">낙관적 UI</a>, 불러올 것이 아예 없으면 <a href="empty.html">빈 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:8px;display:flex;gap:6px;align-items:center"><div class="skl skl--circle" style="width:16px;height:16px"></div><div style="flex:1;display:grid;gap:4px"><div class="skl" style="height:6px;width:60%"></div><div class="skl" style="height:5px;width:40%"></div></div></div><div style="margin-top:7px;display:flex;gap:6px;align-items:center"><div class="skl skl--circle" style="width:16px;height:16px"></div><div style="flex:1;display:grid;gap:4px"><div class="skl" style="height:6px;width:70%"></div><div class="skl" style="height:5px;width:35%"></div></div></div>', bars="", tall=False, label="목록 스켈레톤 재현"),
     "목록", "줄마다 같은 뼈대를 반복한다. 길이만 조금씩 다르게"),
    (mini('<div style="margin-top:8px;display:grid;grid-template-columns:1fr 1fr;gap:6px"><div><div class="skl" style="height:26px"></div><div class="skl" style="height:5px;width:70%;margin-top:4px"></div></div><div><div class="skl" style="height:26px"></div><div class="skl" style="height:5px;width:55%;margin-top:4px"></div></div></div>', bars="", tall=False, label="카드 그리드 스켈레톤 재현"),
     "카드 그리드", "썸네일 비율까지 맞춰 둬야 이미지가 들어올 때 안 밀린다"),
    (mini('<div class="mini__bg" style="padding-top:7px"><div class="mini__bar mini__bar--w60"></div></div><div style="position:absolute;left:7px;right:7px;top:24px;display:grid;gap:5px"><div class="skl" style="height:6px;width:80%"></div><div class="skl" style="height:6px;width:55%"></div></div>', bars="", tall=False, label="일부만 스켈레톤인 재현"),
     "일부만", "제목은 캐시에서 바로, 본문만 뼈대로. 가장 빨라 보이는 방법"),
  ]),
  code_lede="어려운 건 반짝이는 회색 상자가 아니라 <b>실제 줄과 높이를 맞추는 일</b>입니다. 줄 높이를 고정해 두면 거의 저절로 맞습니다.",
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
  keys=kbd([
    ("스크린 리더", "뼈대는 읽을 것이 없다. <code>aria-hidden=\"true\"</code>로 숨기고, 바깥 영역에 <code>aria-busy=\"true\"</code>를 건다"),
    ("포커스", "뼈대에는 누를 것이 없으니 포커스가 가지 않는다"),
    ("내용이 들어올 때", "<code>aria-busy</code>를 지운다. 포커스가 사라진 요소에 머물지 않게 한다"),
    ("움직임 줄이기", "시머를 끈다. 회색 자리만 남겨도 제 일은 다 한다"),
    ("실패", "뼈대를 치우고 다시 시도할 길을 보여 준다"),
  ]),
  backend=rows([
    ("스켈레톤 = 스키마를 미리 아는 것", "응답을 받기 전에 <b>모양을 알고 있다</b>는 뜻입니다. 타입이 정해진 응답과 같습니다. 모양을 모르면 뼈대를 그릴 수 없습니다."),
    ("레이아웃 시프트 = 재할당", "크기를 모르고 담았다가 내용이 들어오며 늘어나는 것은, 용량을 안 잡고 배열에 넣다가 다시 할당하는 것과 같습니다. <b>미리 크기를 잡아 두면 둘 다 안 흔들립니다.</b>"),
    ("일부만 뼈대 = 부분 응답", "캐시에 있는 것은 바로 그리고 없는 칸만 뼈대로 둡니다. stale-while-revalidate 와 같은 모양입니다."),
    ("체감 지연", "실제로 빨라지지는 않습니다. <b>기다리는 느낌</b>만 줄어듭니다. 그래도 그게 사용자에게는 진짜입니다."),
  ]),
  plat_lede="스켈레톤은 웹에서 나온 기법이라 모바일 지침에는 이름이 또렷하지 않습니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="margin-top:8px;display:grid;gap:6px"><div class="skl" style="height:7px;width:70%"></div><div class="skl" style="height:7px;width:50%"></div></div>', bars="", label="웹 스켈레톤 재현"),
     "<b>스켈레톤</b> · 가장 널리 쓰이고 이름도 여기서 굳었습니다. 시머를 넣는 것이 관례입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:6px"><div style="height:8px;border-radius:3px;background:#2a2f39;opacity:.35"></div><div style="height:8px;width:60%;border-radius:3px;background:#2a2f39;opacity:.35"></div></div>', "iOS 자리 표시 재현"),
     "<b>이름이 따로 없습니다.</b> 지침은 '<b>자리 표시 내용</b>(placeholder content)을 보여 주라'고만 합니다. 시머를 쓰는 앱도 안 쓰는 앱도 많습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;display:grid;gap:6px"><div style="height:8px;border-radius:4px;background:var(--line-strong);opacity:.6"></div><div style="height:8px;width:55%;border-radius:4px;background:var(--line-strong);opacity:.6"></div></div>', "안드로이드 로딩 자리 재현"),
     "<b>플레이스홀더</b>(Placeholder) · 역시 별도 부품이 아니라 '로딩 중 자리 표시' 패턴으로 다룹니다."),
  ]),
  plat_note="\"스켈레톤 넣어 주세요\"는 웹에서는 바로 통하지만, 네이티브 앱 쪽에는 그 이름의 표준 부품이 없습니다. <b>어떤 모양으로 몇 줄을 깔지</b>를 같이 정해 줘야 합니다 — 그걸 안 정하면 뼈대가 실제 줄과 안 맞아 결국 덜컥거립니다.",
  siblings=siblings("skeleton"),
  related='''        <li><span class="na"><b>레이아웃 시프트</b><em>1부</em></span></li>
        <li><span class="na"><b>썸네일과 종횡비</b><em>5부</em></span></li>
        <li><span class="na"><b>모션 줄이기</b><em>9부</em></span></li>
        <li><span class="na"><b>가상 스크롤</b><em>10부</em></span></li>''',
)
