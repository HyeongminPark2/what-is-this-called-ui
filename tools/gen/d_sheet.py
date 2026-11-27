# -*- coding: utf-8 -*-
from parts import *
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" data-pin="1" style="background:rgba(14,16,20,.5);border-radius:var(--r2);padding:30px 10px 0">
                <div data-pin="2" style="background:var(--surface);border-radius:12px 12px 0 0;padding:0 26px;box-shadow:0 -6px 20px rgba(0,0,0,.25)">
                  <span class="pin-out" data-pin="3" style="display:block;width:38px;height:4px;border-radius:99px;background:var(--line-strong);margin:11px auto 9px"></span>
                  <div class="pin-out" data-pin="4" style="font-size:13px;font-weight:750;padding-bottom:9px">해질녘 공원</div>
                  <div class="pin-out" data-pin="5" style="border-top:1px solid var(--line);padding:9px 0;font-size:11.5px;color:var(--fg-muted);line-height:2">공유하기<br>원본 내려받기<br>즐겨찾기에 넣기</div>
                  <div class="pin-out" data-pin="6" style="border-top:1px solid var(--line);padding:11px 0">
                    <span style="display:block;text-align:center;border:1px solid var(--line-strong);border-radius:6px;padding:7px;font-size:11.5px;font-weight:700">취소</span>
                  </div>
                  <div class="pin-out" data-pin="7" style="height:16px"></div>
                </div>
              </div>'''

D = dict(
  slug="sheet", ko="바텀시트", en="Bottom sheet · Sheet",
  desc="바텀시트가 무엇이고 모달·드로어와 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="화면 <b>아래에서 올라오는</b> 판. 손가락이 닿는 자리에 선택지를 두려고 씁니다. 좁은 화면에서 모달이 취하는 모습이기도 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>핸들을 아래로 끌어 보세요.</b> 시트에만 있는 조작입니다 — 모달에는 없습니다.
          <kbd>Esc</kbd>와 바깥 누르기도 됩니다. 폭을 <b>넓게</b>로 바꾸면 같은 시트가 가운데로 모입니다.
          넓은 화면에서는 아래에 붙여 둘 이유가 없기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "바텀시트, 시트, 하단 시트"),
    ("영어", "bottom sheet, sheet"),
    ("같이 쓰는 말", "뒤를 막는 것을 <b>모달 시트</b>, 안 막고 내용 위에 걸쳐 있는 것을 <b>스탠더드 시트</b>라 가릅니다. 위로 조금만 올라와 있는 상태는 <b>엿보기</b>(peek)."),
    ("자주 잘못 부름",
     "<b>하단 팝업</b> — 실무에서 많이 쓰지만 표준 용어는 아닙니다.<br>"
     "<b>모달</b> — 좁은 화면에서 모달이 시트로 바뀌는 건 맞지만, 둘은 다른 이름입니다. 시트는 <b>어디서 뜨는가</b>를 가리키고 모달은 <b>뒤를 막는가</b>를 가리킵니다.<br>"
     "<b>액션 시트</b> — iOS 에서 선택지를 늘어놓는 시트만 가리키는 좁은 말입니다."),
  ]),
  axes=axis_table("바텀시트"),
  oneline="시트인지는 <b>아래에서 올라오느냐</b>로 정해집니다. 뒤를 막는지는 <b>따로</b> 정해지므로, 막는 시트와 안 막는 시트가 둘 다 있습니다.",
  states=states([
    (mini(trigger("⋯ 더 보기"), bars="684", label="시트가 닫힌 목록 화면"), "닫힘", "트리거만 보인다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기"], style="transform:translateY(40%);opacity:.6"), bars="684", label="시트가 올라오는 중"), "올라오는 중", "0.25초. 아래에서 밀려 올라온다"),
    (mini(sheet("해질녘 공원", ["공유하기"], scrim=False), bars="684", label="엿보기 상태의 시트"), "엿보기", "조금만 올라와 있다. 뒤를 안 막는 시트에서 흔하다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기", "즐겨찾기"]), bars="684", label="반쯤 열린 시트"), "반 열림", "기본 높이. 내용이 짧으면 여기서 멈춘다"),
    (mini('<div class="mini__scrim" style="padding:0;place-items:end stretch"><div class="mini__sheet" style="top:6px;border-radius:6px 6px 0 0"><span class="grab"></span><b>해질녘 공원</b><i>공유하기</i><i>내려받기</i><i>즐겨찾기에 넣기</i><i>이름 바꾸기</i></div></div>', bars="684", label="전체로 펼친 시트"), "전체", "내용이 길면 화면을 거의 덮는다. 이때는 모달과 같아진다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기"], style="transform:translateY(30%)"), bars="684", label="아래로 끌어 내리는 중"), "끌어 내리는 중", "일정 거리를 넘기면 닫힌다. 안 넘기면 제자리로 돌아간다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크림", "scrim · backdrop", "막는 시트에만 있다. 이게 없으면 뒤를 만질 수 있다"),
    ("시트 몸통", "sheet · surface", "위 모서리만 깎는다. 아래는 화면에 붙어 있으므로"),
    ("그래브 핸들", "grab handle · drag handle", "끌어서 크기를 바꿀 수 있다는 표시. 어포던스다"),
    ("헤더", "header", "무엇에 대한 시트인지. 길면 여기만 고정하고 아래를 스크롤시킨다"),
    ("내용", "content", "여기만 스크롤된다. 시트 전체가 스크롤되면 끌어 닫기와 부딪친다"),
    ("액션 영역", "action area", "폰에서는 버튼을 가로로 늘려 쌓는다"),
    ("세이프 에어리어 여백", "safe area inset", "홈 인디케이터에 버튼이 가리지 않게 아래에 더 두는 빈 자리"),
  ]),
  anat_note="",
  do=ul([
    "손가락으로 고르는 선택지가 여럿일 때",
    "지도나 영상처럼 <b>뒤를 계속 보여 주면서</b> 조작해야 할 때 (안 막는 시트)",
    "좁은 화면에서 모달 대신 — 손이 닿고 키보드에 안 가립니다",
  ]),
  dont=ul([
    "넓은 데스크톱 화면 — 아래에 붙여 둘 이유가 없습니다",
    "입력이 많은 폼 — 키보드가 올라오면 시트가 쪼그라듭니다",
    "단계가 여럿일 때 → 페이지로 보냅니다",
    "끌어 닫기와 안쪽 스크롤이 겹치게 만들기 — 둘 다 세로 제스처라 부딪칩니다",
  ]),
  instead='넓은 화면이면 <a href="modal.html">모달</a>, 옆에서 나와야 하면 <a href="drawer.html">드로어</a>, 알려만 주면 되면 <a href="toast.html">토스트</a>.',
  cases=cases([
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기", "삭제"]), bars="684", tall=False, label="액션 시트 재현"),
     "선택지 늘어놓기", "가장 흔한 형태. 누르면 바로 닫힌다"),
    (mini(sheet("TX-8812 · ₩48,000", ["승인 14:02:11", "신한카드 ••42"]), bars="684", tall=False, label="상세 시트 재현"),
     "상세 보기", "목록에서 한 건을 눌렀을 때. 뒤로 돌아가지 않고 본다"),
    (mini(sheet("근처 카페 12곳", ["블루보틀 성수 · 220m", "앤트러사이트 · 410m"], scrim=False), bars="684", tall=False, label="지도 위 엿보기 시트 재현"),
     "엿보기", "지도를 가리지 않으려고 조금만 올라와 있다. 뒤를 안 막는다"),
  ]),
  code_lede="<code>&lt;dialog&gt;</code>를 아래에 붙이면 됩니다. <code>margin</code> 한 줄이 가운데 모달과 바텀시트를 가릅니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">class</span>=<span class="s">"sheet"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"grab"</span>&gt;&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;해질녘 공원&lt;/<span class="t">h2</span>&gt;
  …
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 가운데가 아니라 아래에 붙인다 — 이 한 줄이 모달과 시트를 가른다 */</span>
dialog.sheet <span class="a">{</span> <span class="t">margin</span>: auto auto 0; <span class="t">width</span>: 100%; <span class="a">}</span>

<span class="c">// 끌어 내려 닫기. 일정 거리를 넘길 때만 닫는다</span>
<span class="a">if</span> (dy &gt; 70) dlg.close();

<span class="c">// 홈 인디케이터에 버튼이 가리지 않게</span>
<span class="t">padding-bottom</span>: <span class="a">calc</span>(16px + env(safe-area-inset-bottom));''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "닫힌다. 막는 시트든 아니든"),
    ("<kbd>Tab</kbd>", "막는 시트에서는 시트 안에서만 돈다"),
    ("아래로 끌기", "일정 거리를 넘기면 닫힌다. 안 넘기면 제자리로 돌아간다"),
    ("열릴 때", "포커스가 시트 안으로. 파괴적 선택지가 있으면 거기에 두지 않는다"),
    ("닫힐 때", "포커스가 열었던 버튼으로 돌아간다"),
  ]),
  backend=rows([
    ("스냅 포인트 = 상태 머신", "엿보기 / 반 / 전체는 세 가지 상태이고 사이를 오가는 규칙이 있습니다. 끌다가 손을 떼면 <b>가장 가까운 상태로 수렴</b>합니다. 상태가 늘수록 규칙이 급히 복잡해집니다."),
    ("막는 시트 = 블로킹 호출", "뒤를 막으면 답이 올 때까지 기다리는 셈입니다. 안 막는 시트는 비동기에 가깝습니다."),
    ("부분 로드와 궁합", "엿보기에서는 요약만, 끌어 올리면 상세를 더 가져옵니다. 커서 페이지네이션과 같은 모양입니다."),
    ("세이프 에어리어 = 예약 영역", "쓸 수 있는 폭과 실제로 그려도 되는 폭이 다릅니다. 헤더 크기를 빼고 페이로드를 계산하는 것과 같습니다."),
  ]),
  plat_lede="이 부품은 iOS 와 안드로이드가 각각 다른 이름 체계를 갖고 있고, 웹은 둘을 섞어 씁니다.",
  plats=plats([
    ("웹", "표준 지침 없음 · <code>&lt;dialog&gt;</code>",
     mini(sheet("해질녘 공원", ["공유하기", "내려받기"]), bars="684", label="웹 바텀시트 재현"),
     "<b>바텀시트</b> · 좁은 폭에서 모달을 대신하는 쓰임이 가장 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-sheet"><div class="ios-sheet__stack"><div class="ios-sheet__group"><span>공유하기</span><span>내려받기</span><span class="destructive">삭제</span></div><div class="ios-sheet__group"><span class="cancel">취소</span></div></div></div>', "iOS 액션 시트 재현"),
     "<b>시트</b>(Sheet) · 높이를 <b>디텐트</b>(detent — medium / large)로 정합니다. 선택지만 늘어놓는 것은 <b>액션 시트</b>로 따로 부릅니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;background:rgba(0,0,0,.4)"></div><div style="position:absolute;left:0;right:0;bottom:0;background:var(--surface);border-radius:16px 16px 0 0;padding:6px 8px 10px"><span style="display:block;width:22px;height:3px;border-radius:99px;background:var(--line-strong);margin:0 auto 6px"></span><b style="font-size:9px">해질녘 공원</b><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:2px 0">공유하기</i><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:2px 0">내려받기</i></div>', "안드로이드 모달 바텀시트 재현"),
     "<b>바텀시트</b>(Bottom sheet) · <b>Modal</b>(막음) / <b>Standard</b>(안 막음) / <b>Expanding</b>으로 나눠 부릅니다. 이 부품의 이름이 굳어진 곳입니다."),
  ]),
  plat_note="\"시트 띄워 주세요\"가 iOS 에서는 <b>화면 전환 방식</b>을 뜻할 수 있습니다. iOS 의 시트는 모달 프레젠테이션의 한 형태라서, 웹에서 생각하는 '아래에서 올라오는 작은 판'보다 범위가 넓습니다. 역할로 말하는 편이 안전합니다.",
  siblings=siblings("sheet"),
  related='''        <li><span class="na"><b>세이프 에어리어</b><em>11부</em></span></li>
        <li><span class="na"><b>제스처</b><em>9부</em></span></li>
        <li><span class="na"><b>포커스 트랩</b><em>12부</em></span></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
