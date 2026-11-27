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
                <div class="pin-out" data-pin="5" style="border:1px solid var(--line);border-radius:6px;padding:12px 26px;font-size:11px;color:var(--fg-muted)">아래 목록이 걸러집니다 — 화면은 그대로</div>
              </div>'''

D = dict(
  slug="segmented", ko="세그먼티드 컨트롤", en="Segmented control",
  desc="세그먼티드 컨트롤이 무엇이고 탭·라디오와 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="선택지 둘셋을 <b>가로로 붙여 놓고 하나</b>를 고르는 띠. 라디오 그룹의 다른 모양이고, 보통 <b>누르는 즉시</b> 반영됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>같은 화면에 탭도 같이 뒀습니다.</b> 세그먼티드를 누르면 아래 목록이 <b>걸러질 뿐</b> 화면은 그대로입니다.
          탭을 누르면 <b>내용 묶음 자체</b>가 바뀝니다 — 거래와 정산은 아예 다른 화면입니다.
          생김새가 닮아서 가장 자주 섞이는 둘입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "세그먼티드 컨트롤, 분할 컨트롤, 토글 그룹"),
    ("영어", "segmented control, segmented button, toggle group"),
    ("같이 쓰는 말", "칸 하나를 <b>세그먼트</b>, 바깥 알약을 <b>트랙</b>이라 합니다. 안드로이드는 <b>세그먼티드 버튼</b>이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>탭</b> — 가장 잦습니다. 탭은 <b>화면을 바꾸고</b> 세그먼티드는 <b>값을 고릅니다</b>.<br>"
     "<b>버튼 그룹</b> — 버튼 그룹은 각 칸이 <b>동작</b>이라 고른 상태가 남지 않습니다.<br>"
     "<b>필터</b> — 쓰임이지 부품 이름이 아닙니다."),
  ]),
  axes=ax("세그먼티드"),
  oneline="세그먼티드는 <b>값을 고르는</b> 것이고 탭은 <b>화면을 바꾸는</b> 것입니다. 누른 뒤 같은 화면에 머물면 세그먼티드입니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="첫 칸이 골라진 모습"), "고름", "고른 칸만 떠 보인다. <b>늘 하나는 골라져 있다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">전체</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="가운데 칸으로 옮긴 모습"), "옮김", "표시가 미끄러지듯 움직인다. 어디서 어디로 갔는지 보인다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">전체</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700;box-shadow:0 0 0 1.5px var(--accent)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="포커스"), "포커스", "<kbd>←</kbd><kbd>→</kbd>로 옮긴다. 라디오 그룹과 같은 규칙"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">전체</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">카드결…</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">계좌이…</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted);overflow:hidden">간편…</span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--danger);font-weight:700">글자가 잘림 — 칸이 너무 많다</div>', bars="", label="칸이 너무 많은 모습"), "너무 많음", "넷을 넘기면 글자가 잘린다. <b>셀렉트로 갈 때</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-faint);opacity:.5">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", label="한 칸만 비활성"), "칸 하나 비활성", "결과가 0건인 칸을 흐리게. 누를 수 있게 두고 빈 상태를 보여 주는 쪽이 보통 낫다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="display:flex;gap:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="font-size:5.5px;color:var(--accent);font-weight:800;border-bottom:1.5px solid var(--accent);padding-bottom:1px">거래</span><span style="font-size:5.5px;color:var(--fg-muted)">정산</span></div><div style="font-size:5px;color:var(--danger);font-weight:700;margin-top:4px">← 이건 탭이다</div></div>', bars="", label="탭과의 비교"), "탭과 비교", "밑줄 꼴이면 보통 탭. <b>화면 자체가 바뀐다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("트랙", "track", "바깥 알약. 칸들이 <b>하나의 묶음</b>이라는 표시다"),
    ("고른 칸", "selected segment", "떠 보이게 한다. 색만으로는 약해서 그림자나 배경을 같이 쓴다"),
    ("안 고른 칸", "segment", "읽히되 눌러도 된다는 느낌이 있어야 한다"),
    ("칸 글자", "label", "짧게. 길면 잘리고, 잘리면 고를 수가 없다"),
    ("영향받는 영역", "controlled region", "<b>같은 화면 안</b>이다. 화면이 바뀌면 그건 탭이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          역할로는 <b>라디오 그룹</b>입니다(<code>role="radiogroup"</code>). 생김새만 가로로 붙어 있을 뿐이라,
          키보드 규칙도 라디오와 같습니다 — <kbd>Tab</kbd> 한 번으로 들어가고 화살표로 옮깁니다.</p>''',
  do=ul([
    "선택지가 <b>2~4개</b>이고 늘 다 보여야 할 때",
    "같은 목록을 <b>거르는</b> 조건일 때 — 전체 / 카드 / 계좌",
    "누르는 즉시 반영되는 보기 전환 — 목록 / 격자",
  ]),
  dont=ul([
    "다섯 개를 넘을 때 — 글자가 잘립니다. 셀렉트로 바꿉니다",
    "화면 자체가 바뀔 때 → 탭입니다",
    "각 칸이 동작일 때 → 버튼 그룹입니다",
    "글자가 긴 선택지 — 가로로 붙이면 다 잘립니다",
  ]),
  instead='화면이 바뀌면 탭(7부), 선택지가 많으면 <a href="select.html">셀렉트</a>, 설명이 길면 <a href="radio.html">라디오</a>, 켜고 끄기면 <a href="switch.html">스위치</a>.',
  cases=cases([
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">계좌</span></span></div>', bars="", tall=False, label="필터형 재현"),
     "목록 거르기", "가장 흔한 쓰임. 아래 목록만 바뀐다"),
    (mini('<div style="margin-top:12px;padding:0 6px;text-align:right"><span style="display:inline-flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:6px;padding:2px 6px">▤</span><span style="font-size:6px;padding:2px 6px;color:var(--fg-muted)">▦</span></span></div>', bars="684", tall=False, label="보기 전환 재현"),
     "보기 전환", "목록 / 격자. 아이콘만 쓸 때는 툴팁으로 이름을 준다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">작게</span><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">보통</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">크게</span></span></div>', bars="", tall=False, label="설정값 재현"),
     "설정값", "단계가 셋인 설정. 슬라이더보다 분명하다"),
  ]),
  code_lede="역할은 라디오 그룹입니다. <code>role=\"radiogroup\"</code>과 <code>aria-checked</code>를 붙이면 화살표 조작까지 라디오와 같은 규칙으로 맞출 수 있습니다.",
  code='''&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"radiogroup"</span> <span class="a">aria-label</span>=<span class="s">"결제 수단"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"true"</span>&gt;전체&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span>&gt;카드&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 화살표로 옮긴다 — 라디오 그룹과 같은 규칙</span>
<span class="a">if</span> (e.key === <span class="s">'ArrowRight'</span>) next().click();

<span class="c">// 탭이라면 role 이 전혀 다르다. 섞어 쓰지 않는다</span>
<span class="c">// role="tablist" / role="tab" / role="tabpanel"</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "묶음 전체를 <b>한 번</b>에 지난다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "칸을 옮기고 <b>옮기는 즉시</b> 반영된다"),
    ("<kbd>Space</kbd>", "짚은 칸을 고른다"),
    ("스크린 리더", "<code>radiogroup</code>이면 '3개 중 1번째'로 읽힌다. 탭이면 전혀 다르게 읽히니 역할을 섞지 않는다"),
    ("손가락", "칸 하나가 44px 이상이어야 한다. 셋을 넘기면 좁은 화면에서 먼저 무너진다"),
  ]),
  backend=rows([
    ("세그먼티드 = 질의 조건", "고른 값은 보통 목록 질의의 필터입니다. <b>주소(URL)에 담아 두면</b> 뒤로가기와 공유가 공짜로 됩니다."),
    ("탭과 다른 점", "탭은 보통 다른 <b>리소스</b>를 부릅니다. 세그먼티드는 같은 리소스에 조건만 바뀝니다 — 캐시 전략이 달라집니다."),
    ("0건인 칸", "미리 개수를 받아 칸에 적어 주면(전체 12 · 카드 9 · 계좌 3) 헛걸음이 줄어듭니다. 질의가 하나 더 필요한 대신 체감이 크게 좋아집니다."),
    ("기본값", "늘 하나는 골라져 있습니다. 그 기본값이 <b>첫 화면의 질의</b>를 정하므로 가장 흔한 것을 둡니다."),
  ]),
  plat_lede="이 부품은 <b>iOS 에서 이름이 굳었고</b>, 다른 곳은 비슷한 것을 다른 이름으로 부릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px"><span style="display:flex;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:1.5px;gap:1px"><span style="flex:1;background:var(--accent-soft);color:var(--accent);border-radius:99px;font-size:5.5px;text-align:center;padding:2px 0;font-weight:700">전체</span><span style="flex:1;font-size:5.5px;text-align:center;padding:2px 0;color:var(--fg-muted)">카드</span></span></div>', bars="", label="웹 세그먼티드 재현"),
     "라디오 그룹을 꾸며서 만듭니다. 알약 꼴이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><span style="display:flex;background:color-mix(in srgb,var(--line) 70%,transparent);border-radius:7px;padding:2px;gap:2px"><span style="flex:1;background:var(--surface);border-radius:5px;font-size:7px;text-align:center;padding:3px 0;font-weight:600">전체</span><span style="flex:1;font-size:7px;text-align:center;padding:3px 0;color:var(--fg-muted)">카드</span></span></div>', "iOS 세그먼티드 컨트롤 재현"),
     "<b>세그먼티드 컨트롤</b>(Segmented control) · 이 이름의 고향입니다. 모서리를 적게 깎은 <b>사각 알약</b>이 표준입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><span style="display:flex;border:1px solid var(--line-strong);border-radius:99px;overflow:hidden"><span style="flex:1;background:var(--accent-soft);color:var(--accent);font-size:7px;text-align:center;padding:4px 0;font-weight:700">✓ 전체</span><span style="flex:1;font-size:7px;text-align:center;padding:4px 0;color:var(--fg-muted);border-left:1px solid var(--line-strong)">카드</span></span></div>', "안드로이드 세그먼티드 버튼 재현"),
     "<b>세그먼티드 버튼</b>(Segmented button) · 고른 칸에 <b>체크 아이콘</b>이 붙고, 여럿 고르는 모드도 표준에 있습니다."),
  ]),
  plat_note="안드로이드의 세그먼티드 버튼은 <b>여럿 고르기(multi-select)도 표준</b>입니다. 그러면 역할이 라디오가 아니라 체크박스가 되고 키보드 규칙도 달라집니다 — \"세그먼티드로 해 주세요\"를 받으면 <b>하나만인지 여럿인지</b>를 먼저 물어야 합니다.",
  siblings=siblings("segmented"),
  related='''        <li><span class="na"><b>탭</b><em>7부</em></span></li>
        <li><span class="na"><b>필터 칩</b><em>5부</em></span></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
