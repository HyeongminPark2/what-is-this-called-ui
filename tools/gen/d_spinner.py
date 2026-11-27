# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT = table(
  ["끝나는 때를 아나", "들어올 자리를 잡나", "사용자가 기다리나", "화면이 덜컥거리나"],
  [["스피너", "모른다", "안 잡는다", "기다린다", "덜컥거린다"],
   ["스켈레톤", "모른다", "잡는다", "기다린다", "안 덜컥거린다"],
   ["프로그레스 바", "안다", "잡기도 한다", "기다린다", "안 덜컥거린다"],
   ["낙관적 UI", "해당 없음", "잡는다", "안 기다린다", "안 덜컥거린다"]],
  me="스피너")

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
  desc="스피너가 무엇이고 스켈레톤·프로그레스 바와 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="<b>얼마나 걸릴지 모르는 기다림</b>을 알리는 돌아가는 고리. 아는 게 '지금 뭔가 하고 있다' 뿐일 때 씁니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>빠르게</b>를 눌러 보세요. 스피너가 <b>아예 안 뜹니다.</b>
          0.3초 안에 끝나는 일에 스피너를 띄우면 깜빡이고 사라져서 오히려 더 느리게 느껴집니다.
          <b>느리게</b>는 띄우되, 한번 띄웠으면 최소 0.5초는 유지합니다 — 이 두 숫자가 스피너의 거의 전부입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스피너, 로딩 아이콘, 로딩 표시"),
    ("영어", "spinner, loading indicator, busy indicator, throbber"),
    ("같이 쓰는 말", "연한 고리를 <b>트랙</b>, 도는 진한 부분을 <b>인디케이터</b>라 합니다. 끝을 모르는 표시라 <b>비결정형</b>(indeterminate)으로 분류합니다."),
    ("자주 잘못 부름",
     "<b>프로그레스 바</b> — 둘 다 기다림을 알리지만, 프로그레스 바는 <b>끝나는 때를 압니다</b>. 모르면서 퍼센트를 지어내면 안 됩니다.<br>"
     "<b>로딩</b> — '로딩 띄워 주세요'는 스피너인지 스켈레톤인지 가려지지 않습니다.<br>"
     "<b>버퍼링</b> — 영상이 잠깐 끊길 때만 쓰는 말입니다."),
  ]),
  axes=WAIT,
  oneline="스피너는 <b>아는 게 없을 때</b> 씁니다. 들어올 모양을 알면 스켈레톤, 끝나는 때를 알면 프로그레스 바가 더 나은 답입니다.",
  states=states([
    (mini('<div style="margin-top:14px;text-align:center;font-size:8px;color:var(--fg-faint)">아무 표시 없음</div>', bars="684", label="0.3초 안에는 아무 표시가 없다"), "0 ~ 0.3초", "<b>아무것도 안 띄운다.</b> 여기서 끝나면 깜빡임만 남는다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm"></span></div>', bars="", label="스피너가 떠 있는 모습"), "0.3초 ~", "그제야 띄운다. 띄웠으면 최소 0.5초는 둔다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7.5px;color:var(--fg-muted)">불러오는 중…</span></div>', bars="", label="문구가 붙은 스피너"), "문구를 붙인 것", "무엇을 기다리는지 적어 주면 훨씬 덜 답답하다"),
    (mini('<div style="margin-top:9px"><span class="mini__btn" style="opacity:.75">저장 중…</span></div>', bars="486", label="버튼 안의 작은 스피너"), "버튼 안", "누른 그 자리에서 돈다. 두 번 눌리는 것도 같이 막는다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7px;color:var(--fg-muted)">조금 오래 걸리고 있습니다</span></div>', bars="", label="오래 걸릴 때 문구가 바뀐 모습"), "10초 넘김", "문구를 바꿔 준다. 같은 화면이 10초 넘게 그대로면 멈춘 줄 안다"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;padding:8px"><span style="font-size:8px;color:var(--danger);font-weight:700">불러오지 못했습니다</span><span class="mini__btn" style="font-size:7.5px;padding:2px 6px">다시 시도</span></div>', bars="", label="실패로 끝난 모습"), "실패로 끝남", "스피너는 <b>영원히 돌면 안 된다.</b> 끝나는 길을 반드시 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("자리", "container", "끝나면 <b>여기에 내용이 들어온다</b>. 스피너가 차지한 높이와 실제 내용의 높이가 다르면 덜컥거린다"),
    ("트랙", "track", "연한 고리. 없는 디자인도 많다"),
    ("인디케이터", "indicator", "도는 진한 부분. 이것만으로는 <b>얼마나 남았는지 알 수 없다</b>"),
    ("안내 문구", "label", "무엇을 기다리는지. <code>aria-label</code>로도 같이 알린다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에 없는 두 숫자가 사실 이 부품의 전부입니다 — <b>지연</b>(0.3초 전에는 안 띄운다)과
          <b>최소 표시 시간</b>(띄웠으면 0.5초는 둔다). 둘 다 깜빡임을 없애려는 장치입니다.</p>''',
  do=ul([
    "얼마나 걸릴지 <b>정말로 모를 때</b>",
    "들어올 내용의 모양도 모를 때 (검색 결과 첫 조회 등)",
    "버튼 하나의 처리처럼 <b>자리가 작을 때</b>",
  ]),
  dont=ul([
    "0.3초 안에 끝나는 일 — 깜빡임만 남깁니다",
    "들어올 모양을 아는 목록·카드 → 스켈레톤이 낫습니다",
    "퍼센트를 알 수 있는 업로드 → 프로그레스 바",
    "화면 전체를 스피너로 덮기 — 자리를 안 잡아 두면 내용이 들어올 때 덜컥거립니다",
  ]),
  instead='들어올 모양을 알면 <a href="skeleton.html">스켈레톤</a>, 끝나는 때를 알면 <a href="progress.html">프로그레스 바</a>, 기다림 자체를 없앨 수 있으면 <a href="optimistic.html">낙관적 UI</a>.',
  cases=cases([
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:5px"><span class="spn spn--sm"></span><span style="font-size:7.5px;color:var(--fg-muted)">불러오는 중…</span></div>', bars="", tall=False, label="영역 스피너 재현"),
     "영역 안", "한 칸만 바뀔 때. 나머지 화면은 그대로 쓴다"),
    (mini('<div style="margin-top:12px;text-align:center"><span class="mini__btn" style="opacity:.75">저장 중…</span></div>', bars="486", tall=False, label="버튼 안 스피너 재현"),
     "버튼 안", "누른 자리에서 돈다. 두 번 눌리는 것도 막힌다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--line)"><i style="display:block;height:100%;width:38%;background:var(--accent)"></i></div>', bars="684", tall=False, label="맨 위 얇은 띠 재현"),
     "꼭대기 띠", "화면 전환에 흔히 쓴다. 자리를 안 뺏는 것이 장점"),
  ]),
  code_lede="돌아가는 모양은 CSS 한 줄이고, 어려운 건 <b>언제 띄우고 언제 치우느냐</b>입니다.",
  code='''&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"panel"</span> <span class="a">aria-busy</span>=<span class="s">"true"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"spn"</span> <span class="a">role</span>=<span class="s">"status"</span> <span class="a">aria-label</span>=<span class="s">"불러오는 중"</span>&gt;&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 0.3초를 넘길 때만 띄운다</span>
<span class="a">const</span> t = setTimeout(show, <span class="a">300</span>);

<span class="c">// 빨리 끝나면 아예 안 띄운 채로 끝낸다</span>
<span class="a">await</span> load(); clearTimeout(t);

<span class="c">// 이미 띄웠으면 최소 0.5초는 둔다 — 깜빡임 방지</span>
<span class="a">if</span> (shown) <span class="a">await</span> wait(<span class="a">500</span> - (Date.now() - shownAt));

<span class="c">/* 움직임을 줄여 달라는 설정은 지킨다 */</span>
@media (prefers-reduced-motion: reduce) <span class="a">{</span> .spn <span class="a">{</span> <span class="t">animation-duration</span>: 2.4s; <span class="a">}</span> <span class="a">}</span>''',
  keys=kbd([
    ("포커스", "스피너는 <b>포커스를 뺏지 않는다.</b> 하던 입력이 끊긴다"),
    ("스크린 리더", "<code>aria-busy=\"true\"</code>를 바뀌는 영역에 걸고, 안내는 <code>role=\"status\"</code>로 알린다"),
    ("끝났을 때", "<code>aria-busy</code>를 지우고, 바뀐 내용 쪽으로 포커스를 옮길지 따로 정한다"),
    ("움직임 줄이기", "<code>prefers-reduced-motion</code>이 켜져 있으면 천천히 돌리거나 정적인 표시로 바꾼다"),
    ("실패", "돌다가 멈추는 것이 아니라 <b>실패 화면으로 바뀌어야</b> 한다"),
  ]),
  backend=rows([
    ("스피너 = 진행률 없는 폴링", "응답이 올 때까지 아무 정보도 없는 상태입니다. 서버가 진행률을 줄 수 있으면 그걸 받아 <b>프로그레스 바로 바꾸는 쪽</b>이 언제나 낫습니다."),
    ("지연 = 디바운스", "0.3초 안에 끝날 일에 표시를 띄우지 않는 것은, 짧은 요청에 로그를 안 남기는 것과 같은 절약입니다."),
    ("최소 표시 시간 = 안정화", "깜빡임을 막으려고 일부러 늦추는 것입니다. 지표가 요동칠 때 창을 두고 평균 내는 것과 같습니다."),
    ("타임아웃", "스피너는 영원히 돌 수 있지만 요청에는 상한이 있어야 합니다. 상한이 없으면 사용자는 <b>멈춘 화면</b>을 봅니다."),
  ]),
  plat_lede="이 부품은 플랫폼마다 모양이 다르고 이름도 다릅니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm"></span></div>', bars="", label="웹 스피너 재현"),
     "<b>스피너</b> · 고리 모양이 가장 흔합니다. 브라우저가 주는 기본 부품은 없어서 직접 그립니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center"><span style="display:inline-block;width:16px;height:16px;position:relative">' + "".join('<i style="position:absolute;left:7px;top:0;width:2px;height:5px;border-radius:2px;background:var(--fg-muted);opacity:%.2f;transform-origin:1px 8px;transform:rotate(%ddeg)"></i>' % (0.25 + i*0.09, i*45) for i in range(8)) + '</span></div>', "iOS 액티비티 인디케이터 재현"),
     "<b>액티비티 인디케이터</b>(Activity indicator) · 고리가 아니라 <b>돌아가는 막대</b>입니다. 이름도 '스피너'가 아닙니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;display:grid;place-items:center"><span class="spn spn--sm" style="border-color:var(--line);border-top-color:var(--accent)"></span></div>', "안드로이드 프로그레스 인디케이터 재현"),
     "<b>비결정형 프로그레스 인디케이터</b>(Indeterminate progress indicator) · 원형과 띠 두 가지가 있고, <b>프로그레스와 같은 부품의 한 모드</b>로 봅니다."),
  ]),
  plat_note="안드로이드에서는 스피너와 프로그레스 바가 <b>같은 부품의 두 모드</b>입니다(결정형 / 비결정형). 더 헷갈리는 건, 안드로이드에 <b>Spinner 라는 전혀 다른 부품</b>이 따로 있다는 것입니다 — 그건 <b>셀렉트(드롭다운)</b>입니다. \"스피너 넣어 주세요\"가 거기서는 선택 상자가 됩니다.",
  siblings=siblings("spinner"),
  related='''        <li><span class="na"><b>레이아웃 시프트</b><em>1부</em></span></li>
        <li><span class="na"><b>모션 줄이기</b><em>9부</em></span></li>
        <li><span class="na"><b>라이브 리전</b><em>12부</em></span></li>
        <li><a href="../index.html#toc"><b>한 화면의 다섯 얼굴</b><em>8부</em></a></li>''',
)
