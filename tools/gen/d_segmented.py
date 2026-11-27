# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:14px 12px">
                <div class="pin-out" data-pin="1" style="display:inline-flex;padding:4px 26px;gap:3px;background:var(--surface);border:1px solid var(--line);border-radius:99px;margin-bottom:22px">
                  <span class="pin-out" data-pin="2" style="background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:7px 16px;font-size:11.5px;font-weight:700;box-shadow:var(--e1)">전체</span>
                  <span data-pin="3" style="padding:7px 16px;font-size:11.5px;color:var(--fg-muted)">카드</span>
                  <span class="pin-tr" data-pin="4" style="padding:7px 16px;font-size:11.5px;color:var(--fg-muted)">계좌</span>
                </div>
                <div class="pin-out" data-pin="5" style="border:1px solid var(--line);border-radius:6px;padding:12px 26px;font-size:11px;color:var(--fg-muted)">아래 목록만 걸러지고 화면은 그대로 있음</div>
              </div>'''

D = dict(
  slug="segmented", ko="세그먼티드 컨트롤", en="Segmented control",
  desc="세그먼티드 컨트롤이 무엇인지, 탭이나 라디오와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="세그먼티드 컨트롤은 선택지 두세 개를 <b>가로로 붙여 놓고 그중 하나</b>를 고르게 하는 띠입니다. 라디오 그룹을 다른 모양으로 그린 것이고, 보통 <b>누르는 즉시</b> 반영됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>같은 화면에 탭도 함께 두었습니다.</b> 세그먼티드 컨트롤을 누르면 아래 목록이 <b>걸러질 뿐</b> 화면은 그대로입니다.
          반면 탭을 누르면 <b>내용 묶음 자체</b>가 바뀝니다. 이 예에서 거래와 정산은 아예 다른 화면입니다.
          두 부품은 생김새가 닮아서 특히 자주 섞어 씁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "세그먼티드 컨트롤, 분할 컨트롤, 토글 그룹"),
    ("영어", "segmented control, segmented button, toggle group"),
    ("같이 쓰는 말", "칸 하나는 <b>세그먼트</b>, 바깥의 알약 모양은 <b>트랙</b>이라고 부릅니다. 안드로이드에서는 이 부품을 <b>세그먼티드 버튼</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>탭</b> — 특히 자주 혼동합니다. 탭은 <b>화면을 바꾸고</b>, 세그먼티드 컨트롤은 <b>값을 고릅니다</b>.<br>"
     "<b>버튼 그룹</b> — 버튼 그룹은 칸마다 <b>동작</b>을 실행하기 때문에 고른 상태가 남지 않습니다.<br>"
     "<b>필터</b> — 필터는 이 부품을 쓰는 목적을 가리키는 말이고, 부품 이름은 아닙니다."),
  ]),
  axes=ax("세그먼티드"),
  oneline="세그먼티드 컨트롤은 <b>값을 고르는</b> 부품이고, 탭은 <b>화면을 바꾸는</b> 부품입니다. 누른 뒤에도 같은 화면에 머물면 세그먼티드 컨트롤입니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="첫 칸이 골라진 모습"), "한 칸을 골랐을 때", "고른 칸만 도드라져 보입니다. <b>늘 하나는 골라져 있습니다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">전체</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="가운데 칸으로 옮긴 모습"), "다른 칸으로 옮길 때", "선택 표시가 옆 칸으로 부드럽게 옮겨 가서, 어느 칸에서 어느 칸으로 바뀌었는지 보입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">전체</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700;box-shadow:0 0 0 1.5px var(--accent)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="포커스"), "포커스를 받았을 때", "<kbd>←</kbd><kbd>→</kbd>로 옮깁니다. 라디오 그룹과 같은 규칙입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">전체</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">카드결…</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">계좌이…</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">간편…</span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--danger);font-weight:700">칸이 너무 많아 글자가 잘림</div>', bars="", label="칸이 너무 많은 모습"), "칸이 너무 많을 때", "칸이 넷을 넘으면 글자가 잘립니다. <b>셀렉트로 바꿀 때</b>입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-faint);opacity:.5">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="한 칸만 비활성"), "칸 하나를 비활성으로 둘 때", "결과가 0건인 칸을 흐리게 표시한 모습입니다. 보통은 그 칸도 누를 수 있게 두고 빈 상태를 보여 주는 편이 낫습니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div><div style="font-size:5px;color:var(--danger);font-weight:700;margin-top:4px">← 이쪽은 탭임</div></div>', bars="", label="탭과의 비교"), "탭과 견주어 본 모습", "고른 칸에 밑줄이 그어진 모양이면 보통 탭이고, 누르면 <b>화면 자체가 바뀝니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("트랙", "track", "바깥의 알약 모양으로, 칸들이 <b>하나의 묶음</b>이라는 것을 보여 줍니다"),
    ("고른 칸", "selected segment", "도드라져 보이게 합니다. 색만으로는 구별이 약하므로 그림자나 배경을 함께 씁니다"),
    ("안 고른 칸", "segment", "글자가 잘 읽혀야 하고, 눌러서 고를 수 있다는 것도 알아볼 수 있어야 합니다"),
    ("칸 글자", "label", "짧게 적습니다. 글자가 길면 잘리고, 잘린 칸은 무엇을 고르는지 알 수 없습니다"),
    ("영향받는 영역", "controlled region", "세그먼티드 컨트롤이 바꾸는 곳은 <b>같은 화면 안</b>에 있습니다. 화면이 통째로 바뀐다면 그건 세그먼티드 컨트롤이 아니라 탭입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          역할로 보면 세그먼티드 컨트롤은 <b>라디오 그룹</b>입니다(<code>role="radiogroup"</code>). 생김새만 가로로 붙어 있을 뿐이어서
          키보드 규칙도 라디오와 같습니다. <kbd>Tab</kbd> 한 번으로 묶음에 들어가고 화살표로 칸을 옮깁니다.</p>''',
  do=ul([
    "선택지가 <b>2~4개</b>이고 늘 다 보여야 할 때",
    "전체 / 카드 / 계좌처럼 같은 목록을 <b>거르는</b> 조건일 때",
    "목록 / 격자처럼 누르는 즉시 반영되는 보기 전환일 때",
  ]),
  dont=ul([
    "선택지가 다섯 개를 넘을 때. 글자가 잘리므로 셀렉트로 바꿉니다",
    "화면 자체가 바뀔 때. 이때는 탭을 씁니다",
    "칸마다 동작을 실행할 때. 이때는 버튼 그룹을 씁니다",
    "선택지 글자가 길 때. 가로로 붙이면 글자가 모두 잘립니다",
  ]),
  instead='누르면 화면 자체가 바뀌어야 하면 탭(7부)을 쓰고, 선택지가 많으면 <a href="select.html">셀렉트</a>를 씁니다. 선택지마다 설명이 길게 붙으면 <a href="radio.html">라디오</a>가 낫고, 켜고 끄는 값이면 <a href="switch.html">스위치</a>가 맞습니다.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", tall=False, label="필터형 재현"),
     "같은 목록 거르기", "가장 흔한 쓰임으로, 누르면 아래 목록만 바뀝니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;text-align:right"><span style="display:inline-flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:6px;padding:2px 6px">▤</span><span style="font-size:6px;padding:2px 6px;color:var(--fg-muted)">▦</span></span></div>', bars="684", tall=False, label="보기 전환 재현"),
     "목록 보기와 격자 보기 바꾸기", "목록 보기와 격자 보기를 바꿉니다. 칸에 아이콘만 둘 때는 툴팁으로 이름을 알려 줍니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">작게</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">보통</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">크게</span></span></div>', bars="", tall=False, label="설정값 재현"),
     "세 단계 설정값 고르기", "단계가 셋뿐인 설정에 씁니다. 슬라이더보다 지금 어느 단계인지 분명하게 보입니다"),
  ]),
  code_lede="세그먼티드 컨트롤의 역할은 라디오 그룹입니다. 그래서 <code>role=\"radiogroup\"</code>과 <code>aria-checked</code>를 붙이고, 화살표 조작도 라디오와 같은 규칙으로 맞춥니다.",
  code='''&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"radiogroup"</span> <span class="a">aria-label</span>=<span class="s">"결제 수단"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"true"</span>&gt;전체&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span>&gt;카드&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 화살표로 옮긴다. 라디오 그룹과 같은 규칙</span>
<span class="a">if</span> (e.key === <span class="s">'ArrowRight'</span>) next().click();

<span class="c">// 탭이라면 role 이 전혀 다르다. 섞어 쓰지 않는다</span>
<span class="c">// role="tablist" / role="tab" / role="tabpanel"</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "묶음 전체를 <b>한 번</b>에 지나갑니다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "칸을 옮기며, <b>옮기는 즉시</b> 반영됩니다"),
    ("<kbd>Space</kbd>", "짚은 칸을 고릅니다"),
    ("스크린 리더로 읽을 때", "<code>radiogroup</code>으로 만들면 '3개 중 1번째'처럼 읽습니다. 탭으로 만들면 전혀 다르게 읽으므로 두 역할을 섞지 않습니다"),
    ("손가락으로 누를 때", "칸 하나가 44px 이상이어야 합니다. 칸이 셋을 넘으면 좁은 화면에서는 이 너비를 지키기 어렵습니다"),
  ]),
  backend=rows([
    ("고른 값은 목록 질의의 조건", "고른 값은 보통 목록을 불러오는 질의의 필터로 쓰입니다. 이 값을 <b>주소(URL)에 담아 두면</b> 뒤로가기와 링크 공유가 따로 만들지 않아도 동작합니다."),
    ("탭과 다른 불러오기 방식", "탭은 보통 서로 다른 <b>리소스</b>를 불러오고, 세그먼티드 컨트롤은 같은 리소스에 조건만 바꿔 불러옵니다. 그래서 캐시 전략도 달라집니다."),
    ("결과가 0건인 칸 다루기", "칸마다 결과 개수를 미리 받아 적어 주면(전체 12 · 카드 9 · 계좌 3), 사용자가 결과가 없는 칸을 눌러 보는 일이 줄어듭니다. 개수를 받는 질의가 하나 더 필요하지만 쓰기에는 훨씬 편해집니다."),
    ("처음에 골라 둘 기본값", "세그먼티드 컨트롤은 늘 하나가 골라져 있습니다. 이 기본값이 <b>첫 화면에서 보내는 질의</b>를 정하므로, 가장 많이 쓰는 값을 기본값으로 둡니다."),
  ]),
  plat_lede="세그먼티드 컨트롤이라는 <b>이름은 iOS 에서 자리 잡았고</b>, 다른 플랫폼에서는 비슷한 부품을 다른 이름으로 부릅니다.",
  plats=plats([
    ("웹", "표준 부품이 없음",
     mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span></span></div>', bars="", label="웹 세그먼티드 재현"),
     "라디오 그룹을 꾸며서 만들며, 알약 모양이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><span style="display:flex;background:color-mix(in srgb,var(--line) 70%,transparent);border-radius:7px;padding:2px;gap:2px"><span style="flex:1;background:var(--surface);border-radius:5px;font-size:7px;text-align:center;padding:3px 0;font-weight:600">전체</span><span style="flex:1;font-size:7px;text-align:center;padding:3px 0;color:var(--fg-muted)">카드</span></span></div>', "iOS 세그먼티드 컨트롤 재현"),
     "<b>세그먼티드 컨트롤</b>(Segmented control) · 이 이름이 처음 쓰인 곳입니다. 모서리를 조금만 둥글린 <b>사각 알약</b> 모양이 표준입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><span style="display:flex;border:1px solid var(--line-strong);border-radius:99px;overflow:hidden"><span style="flex:1;background:var(--accent-soft);color:var(--accent);font-size:7px;text-align:center;padding:4px 0;font-weight:700">✓ 전체</span><span style="flex:1;font-size:7px;text-align:center;padding:4px 0;color:var(--fg-muted);border-left:1px solid var(--line-strong)">카드</span></span></div>', "안드로이드 세그먼티드 버튼 재현"),
     "<b>세그먼티드 버튼</b>(Segmented button) · 고른 칸에 <b>체크 아이콘</b>이 붙고, 여럿 고르는 모드도 표준에 있습니다."),
  ]),
  plat_note="안드로이드의 세그먼티드 버튼은 <b>여럿 고르기(multi-select)도 표준</b>으로 지원합니다. 여럿을 고르게 하면 역할이 라디오가 아니라 체크박스가 되고 키보드 규칙도 달라집니다. 그래서 \"세그먼티드로 해 주세요\"라는 요청을 받으면 <b>하나만 고르는지, 여럿을 고르는지</b>부터 물어야 합니다.",
  siblings=siblings("segmented"),
  related='''        <li><a href="tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="filter.html"><b>필터 칩</b><em>10부</em></a></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>''',
)
