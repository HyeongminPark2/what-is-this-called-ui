# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:10px">
                <div data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;min-height:120px;display:grid;place-items:center;gap:11px;padding:20px">
                  <span style="position:relative;display:inline-block;width:34px;height:34px">
                    <span class="pin-out" data-pin="2" style="position:absolute;inset:0;border:3px solid var(--line);border-radius:50%"></span>
                    <span class="pin-tr" data-pin="3" style="position:absolute;inset:0;border:3px solid transparent;border-top-color:var(--accent);border-radius:50%"></span>
                  </span>
                  <span class="pin-out" data-pin="4" style="font-size:11.5px;color:var(--fg-muted)">불러오는 중…</span>
                </div>
              </div>'''

D = dict(
  slug="spinner", ko="스피너", en="Spinner · Loading indicator",
  desc="스피너가 무엇인지, 스켈레톤·프로그레스 바와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="스피너는 <b>얼마나 걸릴지 모르는 기다림</b>을 알리려고 띄우는, 빙글빙글 도는 고리입니다. 화면이 알려 줄 수 있는 것이 '지금 무언가를 처리하고 있다'는 사실 하나뿐일 때 씁니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>빠르게</b>를 눌러 보면 스피너가 <b>아예 뜨지 않습니다.</b>
          0.3초 안에 끝나는 일에 스피너를 띄우면 잠깐 깜빡이고 사라지는데, 이 깜빡임 때문에 오히려 더 느리게 느껴지기 때문입니다.
          <b>느리게</b>를 누르면 스피너를 띄우고, 한번 띄운 스피너는 최소 0.5초 동안 그대로 둡니다. 스피너를 다룰 때 정해야 할 것은 대부분 이 두 시간입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스피너, 로딩 아이콘, 로딩 표시"),
    ("영어", "spinner, loading indicator, busy indicator, throbber"),
    ("같이 쓰는 말", "바탕에 깔린 연한 고리는 <b>트랙</b>, 그 위에서 도는 진한 부분은 <b>인디케이터</b>라고 부릅니다. 언제 끝날지 모르는 상태를 나타내는 표시라서 <b>비결정형</b>(indeterminate)으로 분류합니다."),
    ("자주 잘못 부르는 이름",
     "<b>프로그레스 바</b> — 둘 다 기다림을 알리지만, 프로그레스 바는 <b>끝나는 때를 알 때</b> 씁니다. 진행률을 모르는데 퍼센트를 지어내 보여 주면 안 됩니다.<br>"
     "<b>로딩</b> — '로딩 띄워 주세요'라고만 하면 스피너를 말하는지 스켈레톤을 말하는지 알 수 없습니다.<br>"
     "<b>버퍼링</b> — 영상 재생이 잠깐 끊겼을 때만 쓰는 말입니다."),
  ]),
  states=states([
    (mini('<div style="margin-top:14px;text-align:center;font-size:8px;color:var(--fg-faint)">아무것도 띄우지 않음</div>', bars="684", label="0.3초 안에는 아무 표시도 없음"), "0.3초가 지나기 전", "<b>아무것도 띄우지 않습니다.</b> 이 사이에 끝나는 일에 스피너를 띄우면 깜빡임만 남습니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm"></span></div>', bars="", label="스피너가 떠 있는 모습"), "0.3초가 지난 뒤", "0.3초가 지나면 그때 띄우고, 띄운 뒤에는 최소 0.5초 동안 둡니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7.5px;color:var(--fg-muted)">불러오는 중…</span></div>', bars="", label="문구가 붙은 스피너"), "안내 문구를 붙였을 때", "무엇을 기다리는지 적어 주면 사용자가 훨씬 덜 답답해합니다"),
    (mini('<div style="margin-top:9px"><span class="mini__btn" style="opacity:.75">저장 중…</span></div>', bars="486", label="버튼 안의 작은 스피너"), "버튼 안에서 돌 때", "사용자가 누른 버튼 자리에서 돌고, 버튼이 두 번 눌리는 것도 함께 막습니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7px;color:var(--fg-muted)">조금 오래 걸리고 있습니다</span></div>', bars="", label="오래 걸릴 때 문구가 바뀐 모습"), "10초를 넘겼을 때", "문구를 바꿔 줍니다. 같은 화면이 10초 넘게 그대로면 사용자는 화면이 멈춘 줄 압니다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;padding:8px"><span style="font-size:8px;color:var(--danger);font-weight:700">불러오지 못했습니다</span><span class="mini__btn" style="font-size:7.5px;padding:2px 6px">다시 시도</span></div>', bars="", label="실패로 끝난 모습"), "실패로 끝났을 때", "스피너가 <b>끝없이 돌게 두면 안 됩니다.</b> 실패했을 때 실패 화면으로 바뀌는 경로를 반드시 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자리", "container", "로딩이 끝나면 <b>이 자리에 내용이 들어옵니다</b>. 스피너가 차지한 높이와 실제 내용의 높이가 다르면 화면이 덜컥거립니다"),
    ("트랙", "track", "바탕의 연한 고리입니다. 트랙을 그리지 않는 디자인도 많습니다"),
    ("인디케이터", "indicator", "도는 진한 부분입니다. 계속 돌기만 하므로 <b>얼마나 남았는지는 알 수 없습니다</b>"),
    ("안내 문구", "label", "무엇을 기다리는지 적습니다. 같은 내용을 <code>aria-label</code>로도 알립니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않지만 스피너에서 특히 중요한 값이 두 가지 있습니다. 0.3초가 지나기 전에는 띄우지 않는 <b>지연</b>과,
          한번 띄우면 0.5초는 두는 <b>최소 표시 시간</b>입니다. 두 값 모두 스피너가 잠깐 떴다 사라지는 깜빡임을 없애려고 둡니다.</p>''',
  do=ul([
    "얼마나 걸릴지 <b>정말로 모를 때</b>",
    "들어올 내용의 모양도 모를 때(검색 결과를 처음 조회할 때 등)",
    "버튼 하나의 처리처럼 <b>자리가 작을 때</b>",
  ]),
  dont=ul([
    "0.3초 안에 끝나는 일을 기다릴 때. 스피너가 깜빡이기만 하고 사라집니다",
    "들어올 모양을 아는 목록이나 카드를 불러올 때. 스켈레톤이 더 알맞습니다",
    "퍼센트를 알 수 있는 업로드를 기다릴 때. 프로그레스 바를 씁니다",
    "화면 전체를 스피너로 덮을 때. 내용이 들어올 자리를 잡아 두지 않았기 때문에 내용이 들어오는 순간 화면이 덜컥거립니다",
  ]),
  instead='들어올 내용의 모양을 알면 <a href="skeleton.html">스켈레톤</a>을 쓰고, 끝나는 때를 알면 <a href="progress.html">프로그레스 바</a>를 씁니다. 기다림 자체를 없앨 수 있다면 <a href="optimistic.html">낙관적 UI</a>가 더 낫습니다.',
  cases=cases([
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7.5px;color:var(--fg-muted)">불러오는 중…</span></div>', bars="", tall=False, label="영역 스피너 재현"),
     "화면의 한 영역만 불러오기", "화면의 한 칸만 바뀔 때 씁니다. 나머지 화면은 기다리는 동안에도 그대로 쓸 수 있습니다"),
    (mini('<div style="margin-top:12px;text-align:center"><span class="mini__btn" style="opacity:.75">저장 중…</span></div>', bars="486", tall=False, label="버튼 안 스피너 재현"),
     "버튼을 누른 뒤 처리 기다리기", "누른 버튼 자리에서 돌고, 그동안 버튼이 두 번 눌리지 않습니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--line)"><i style="display:block;height:100%;width:38%;background:var(--accent)"></i></div>', bars="684", tall=False, label="맨 위 얇은 띠 재현"),
     "화면 전환을 맨 위 띠로 알리기", "화면을 전환할 때 흔히 씁니다. 화면 맨 위의 얇은 띠라서 내용이 들어갈 자리를 차지하지 않습니다"),
  ]),
  code_lede="도는 모양은 CSS 한 줄로 만들 수 있습니다. 정작 신경 써야 하는 부분은 <b>언제 띄우고 언제 치울지</b>입니다.",
  code='''&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"panel"</span> <span class="a">aria-busy</span>=<span class="s">"true"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"spn"</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">aria-label</span>=<span class="s">"불러오는 중"</span>&gt;&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 0.3초를 넘길 때만 띄운다</span>
<span class="a">const</span> t = setTimeout(show, <span class="a">300</span>);

<span class="c">// 빨리 끝나면 아예 안 띄운 채로 끝낸다</span>
<span class="a">await</span> load(); clearTimeout(t);

<span class="c">// 이미 띄웠으면 깜빡이지 않도록 최소 0.5초는 둔다</span>
<span class="a">if</span> (shown) <span class="a">await</span> wait(<span class="a">500</span> - (Date.now() - shownAt));

<span class="c">/* 움직임을 줄여 달라는 설정은 지킨다 */</span>
@media (prefers-reduced-motion: reduce) <span class="a">{</span> .spn <span class="a">{</span> <span class="t">animation-duration</span>: 2.4s; <span class="a">}</span> <span class="a">}</span>''',
  keys_heads="<th>상황</th><th>그때 일어나야 하는 일</th>",
  keys=kbd([
    ("포커스를 다룰 때", "스피너가 <b>포커스를 가져가지 않게 합니다.</b> 포커스를 가져가면 사용자가 하던 입력이 끊깁니다"),
    ("스크린 리더로 읽을 때", "<code>aria-busy=\"true\"</code>를 내용이 바뀌는 영역에 걸고, 안내 문구는 <code>role=\"status\"</code>로 알립니다"),
    ("끝났을 때", "<code>aria-busy</code>를 지웁니다. 바뀐 내용 쪽으로 포커스를 옮길지는 화면에 맞게 따로 정합니다"),
    ("움직임 줄이기 설정이 켜져 있을 때", "<code>prefers-reduced-motion</code>이 켜져 있으면 천천히 돌리거나 움직이지 않는 표시로 바꿉니다"),
    ("불러오기에 실패했을 때", "스피너가 돌다가 그대로 멈추면 안 되고, <b>실패 화면으로 바뀌어야</b> 합니다"),
  ]),
  backend=rows([
    ("진행률 없이 응답만 기다리는 상태", "스피너는 응답이 올 때까지 진행 정보를 하나도 받지 못한 상태를 나타냅니다. 서버가 진행률을 알려 줄 수 있다면 그 값을 받아 <b>프로그레스 바로 바꾸는 편</b>이 언제나 낫습니다."),
    ("지연은 디바운스와 같은 원리", "0.3초 안에 끝날 일에는 표시를 띄우지 않습니다. 짧은 요청까지 일일이 로그로 남기지 않는 것처럼, 금방 끝나는 일에는 표시를 아끼는 셈입니다."),
    ("최소 표시 시간으로 깜빡임 막기", "깜빡임을 막으려고 스피너를 치우는 시점을 일부러 늦춥니다. 지표가 요동칠 때 일정한 시간 창을 두고 평균을 내서 값을 안정시키는 것과 같은 방법입니다."),
    ("요청 쪽에 시간 상한 두기", "스피너 자체는 끝없이 돌 수 있기 때문에 요청 쪽에 시간 상한을 두어야 합니다. 상한이 없으면 응답이 오지 않을 때 사용자는 <b>멈춘 화면</b>을 계속 보게 됩니다."),
  ]),
  plat_lede="스피너는 플랫폼마다 모양도 다르고 부르는 이름도 다릅니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm"></span></div>', bars="", label="웹 스피너 재현"),
     "<b>스피너</b> · 고리 모양이 가장 흔합니다. 브라우저가 기본으로 주는 부품이 없어서 직접 그립니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center"><span style="display:inline-block;width:16px;height:16px;position:relative">' + "".join('<i style="position:absolute;left:7px;top:0;width:2px;height:5px;border-radius:2px;background:var(--fg-muted);opacity:%.2f;transform-origin:1px 8px;transform:rotate(%ddeg)"></i>' % (0.25 + i*0.09, i*45) for i in range(8)) + '</span></div>', "iOS 액티비티 인디케이터 재현"),
     "<b>액티비티 인디케이터</b>(Activity indicator) · 고리가 아니라 <b>여러 개의 막대가 둥글게 돌아가는 모양</b>이고, 이름도 '스피너'가 아닙니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm" style="border-color:var(--line);border-top-color:var(--accent)"></span></div>', "안드로이드 프로그레스 인디케이터 재현"),
     "<b>비결정형 프로그레스 인디케이터</b>(Indeterminate progress indicator) · 원형과 띠 두 가지 모양이 있고, <b>프로그레스 바와 같은 부품의 한 모드</b>로 다룹니다."),
  ]),
  plat_note="안드로이드에서는 스피너와 프로그레스 바가 <b>같은 부품의 두 모드</b>(결정형과 비결정형)입니다. 게다가 안드로이드에는 <b>Spinner라는 이름의 전혀 다른 부품</b>이 따로 있는데, 이 부품은 <b>셀렉트(드롭다운)</b>입니다. 그래서 안드로이드에서 \"스피너 넣어 주세요\"라고 하면 선택 상자를 넣어 달라는 말로 알아듣습니다.",
  siblings=siblings("spinner"),
  related='''        <li><span class="na"><b>레이아웃 시프트</b><em>1부</em></span></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>
        <li><a href="../index.html#toc"><b>한 화면의 다섯 얼굴</b><em>8부</em></a></li>''',
)
