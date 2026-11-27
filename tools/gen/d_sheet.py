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
  desc="바텀시트가 무엇인지, 모달이나 드로어와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="바텀시트는 화면 <b>아래에서 올라오는</b> 판으로, 손가락이 쉽게 닿는 자리에 선택지를 두려고 씁니다. 좁은 화면에서는 모달도 가운데 대신 이 모양으로 띄우는 경우가 많습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>핸들을 아래로 끌어 보세요.</b> 끌어서 닫는 조작은 시트에만 있고 모달에는 없습니다.
          <kbd>Esc</kbd>를 누르거나 시트 바깥을 눌러도 닫힙니다. 폭을 <b>넓게</b>로 바꾸면 같은 시트가 화면 가운데로 옮겨 가는데,
          넓은 화면에서는 손가락이 닿는 자리를 따질 필요가 없어 아래에 붙여 둘 이유가 없기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "바텀시트, 시트, 하단 시트"),
    ("영어", "bottom sheet, sheet"),
    ("같이 쓰는 말", "뒤쪽 화면을 막는 것은 <b>모달 시트</b>, 막지 않고 내용 위에 걸쳐 있는 것은 <b>스탠더드 시트</b>라고 나눠 부릅니다. 시트가 위로 조금만 올라와 있는 상태는 <b>엿보기</b>(peek)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>하단 팝업</b> — 실무에서 많이 쓰는 말이지만 표준 용어는 아닙니다.<br>"
     "<b>모달</b> — 좁은 화면에서 모달이 시트 모양으로 바뀌는 것은 맞지만, 두 이름은 가리키는 것이 다릅니다. 시트는 <b>어디서 뜨는가</b>를, 모달은 <b>뒤를 막는가</b>를 가리킵니다.<br>"
     "<b>액션 시트</b> — iOS에서 선택지를 늘어놓는 시트만 가리키는 좁은 말이라, 바텀시트 전체를 부르는 이름으로 쓰면 범위가 맞지 않습니다."),
  ]),
  axes=axis_table("바텀시트"),
  oneline="시트인지 아닌지는 <b>아래에서 올라오느냐</b>로 정해집니다. 뒤쪽 화면을 막는지는 이와 <b>따로</b> 정하기 때문에, 뒤를 막는 시트와 막지 않는 시트가 모두 있습니다.",
  states=states([
    (mini(trigger("⋯ 더 보기"), bars="684", label="시트가 닫힌 목록 화면"), "닫혀 있을 때", "트리거만 보입니다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기"], style="transform:translateY(40%);opacity:.6"), bars="684", label="시트가 올라오는 중"), "아래에서 올라오는 중", "0.25초 동안 아래에서 밀려 올라옵니다"),
    (mini(sheet("해질녘 공원", ["공유하기"], scrim=False), bars="684", label="엿보기 상태의 시트"), "조금만 올라온 엿보기 상태", "조금만 올라와 있는 상태로, 뒤를 막지 않는 시트에서 흔히 씁니다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기", "즐겨찾기"]), bars="684", label="반쯤 열린 시트"), "반쯤 열린 기본 높이", "기본 높이입니다. 내용이 짧으면 이 높이에서 멈춥니다"),
    (mini('<div class="mini__scrim" style="padding:0;place-items:end stretch"><div class="mini__sheet" style="top:6px;border-radius:6px 6px 0 0"><span class="grab"></span><b>해질녘 공원</b><i>공유하기</i><i>내려받기</i><i>즐겨찾기에 넣기</i><i>이름 바꾸기</i></div></div>', bars="684", label="전체로 펼친 시트"), "화면 전체로 펼쳤을 때", "내용이 길면 화면을 거의 다 덮는데, 이때는 모달과 다를 것이 없습니다"),
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기"], style="transform:translateY(30%)"), bars="684", label="아래로 끌어 내리는 중"), "아래로 끌어 내리는 중", "일정 거리를 넘겨 끌면 닫히고, 넘기지 않으면 제자리로 돌아갑니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크림", "scrim · backdrop", "뒤를 막는 시트에만 있습니다. 스크림이 없으면 뒤쪽 화면을 누를 수 있습니다"),
    ("시트 몸통", "sheet · surface", "아래쪽은 화면 끝에 붙어 있으므로 위쪽 모서리만 둥글게 깎습니다"),
    ("그래브 핸들", "grab handle · drag handle", "끌어서 크기를 바꿀 수 있다는 것을 알려 주는 표시로, 어포던스의 한 예입니다"),
    ("헤더", "header", "무엇에 대한 시트인지 알려 줍니다. 내용이 길면 헤더만 고정하고 그 아래를 스크롤합니다"),
    ("내용", "content", "이 영역만 스크롤합니다. 시트 전체가 스크롤되면 끌어서 닫는 동작과 부딪칩니다"),
    ("액션 영역", "action area", "폰에서는 버튼을 가로로 길게 늘려 세로로 쌓습니다"),
    ("세이프 에어리어 여백", "safe area inset", "홈 인디케이터가 버튼을 가리지 않도록 아래에 더 비워 두는 자리입니다"),
  ]),
  anat_note="",
  do=ul([
    "손가락으로 고를 선택지가 여럿일 때",
    "지도나 영상처럼 <b>뒤쪽 화면을 계속 보여 주면서</b> 조작해야 할 때. 이때는 뒤를 막지 않는 시트를 씁니다",
    "좁은 화면에서 모달 대신 쓸 때. 손가락이 닿기 쉽고, 키보드가 올라와도 가리지 않습니다",
  ]),
  dont=ul([
    "넓은 데스크톱 화면일 때. 손가락이 닿는 자리를 따질 필요가 없어서 아래에 붙여 둘 이유가 없습니다",
    "입력 칸이 많은 폼을 담을 때. 키보드가 올라오면 시트에 남는 높이가 너무 작아집니다",
    "단계가 여럿인 작업일 때. 별도 페이지로 보냅니다",
    "끌어서 닫기와 안쪽 스크롤이 같은 자리에서 겹칠 때. 둘 다 세로로 끄는 제스처라 서로 부딪칩니다",
  ]),
  instead='넓은 화면에서는 가운데 뜨는 <a href="modal.html">모달</a>을 쓰고, 화면 옆에서 밀려 나와야 하면 <a href="drawer.html">드로어</a>를 씁니다. 결과를 알리기만 하면 된다면 <a href="toast.html">토스트</a>로 충분합니다.',
  cases=cases([
    (mini(sheet("해질녘 공원", ["공유하기", "내려받기", "삭제"]), bars="684", tall=False, label="액션 시트 재현"),
     "고를 선택지 늘어놓기", "가장 흔한 형태입니다. 선택지를 누르면 시트가 바로 닫힙니다"),
    (mini(sheet("TX-8812 · ₩48,000", ["승인 14:02:11", "신한카드 ••42"]), bars="684", tall=False, label="상세 시트 재현"),
     "목록 위에서 한 건의 상세 보기", "목록에서 한 건을 눌렀을 때 띄웁니다. 다른 화면으로 넘어가지 않고 목록 위에서 상세를 봅니다"),
    (mini(sheet("근처 카페 12곳", ["블루보틀 성수 · 220m", "앤트러사이트 · 410m"], scrim=False), bars="684", tall=False, label="지도 위 엿보기 시트 재현"),
     "지도를 가리지 않고 엿보기", "지도를 가리지 않으려고 조금만 올라와 있고, 뒤쪽 지도를 막지 않습니다"),
  ]),
  code_lede="<code>&lt;dialog&gt;</code> 요소를 화면 아래에 붙이면 바텀시트가 됩니다. 가운데 뜨는 모달과 코드에서 다른 곳은 <code>margin</code>을 정하는 한 줄뿐입니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">class</span>=<span class="s">"sheet"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"grab"</span>&gt;&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;해질녘 공원&lt;/<span class="t">h2</span>&gt;
  …
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 가운데가 아니라 아래에 붙인다. 모달과 시트는 이 한 줄만 다르다 */</span>
dialog.sheet <span class="a">{</span> <span class="t">margin</span>: auto auto 0; <span class="t">width</span>: 100%; <span class="a">}</span>

<span class="c">// 끌어 내려 닫기. 일정 거리를 넘길 때만 닫는다</span>
<span class="a">if</span> (dy &gt; 70) dlg.close();

<span class="c">// 홈 인디케이터에 버튼이 가리지 않게</span>
<span class="t">padding-bottom</span>: <span class="a">calc</span>(16px + env(safe-area-inset-bottom));''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "뒤를 막는 시트든 막지 않는 시트든 닫힙니다"),
    ("<kbd>Tab</kbd>", "뒤를 막는 시트에서는 포커스가 시트 안에서만 돕니다"),
    ("시트를 아래로 끌 때", "일정 거리를 넘겨 끌면 닫히고, 넘기지 않으면 제자리로 돌아갑니다"),
    ("시트가 열릴 때", "포커스를 시트 안으로 옮깁니다. 삭제처럼 되돌릴 수 없는 선택지가 있으면 그 선택지에는 포커스를 두지 않습니다"),
    ("시트가 닫힐 때", "포커스가 시트를 열었던 버튼으로 돌아갑니다"),
  ]),
  backend=rows([
    ("스냅 포인트는 상태 머신과 같은 구조", "엿보기·반 열림·전체는 세 가지 상태이고, 상태 사이를 오가는 규칙이 정해져 있습니다. 시트를 끌다가 손을 떼면 <b>가장 가까운 상태로 맞춰</b> 멈춥니다. 상태 수가 늘어날수록 오가는 규칙은 빠르게 복잡해집니다."),
    ("뒤를 막는 시트는 블로킹 호출과 같음", "뒤를 막는 시트는 사용자의 답이 올 때까지 기다리는 블로킹 호출과 같습니다. 반면 뒤를 막지 않는 시트는 비동기 호출에 가깝습니다."),
    ("데이터를 나눠 불러오기에 잘 맞음", "엿보기 상태에서는 요약만 보여 주고, 사용자가 끌어 올리면 상세 데이터를 더 가져옵니다. 필요한 만큼 이어서 받는다는 점에서 커서 페이지네이션과 구조가 같습니다."),
    ("세이프 에어리어는 미리 떼어 둔 영역", "화면 전체 크기와 실제로 그려도 되는 영역의 크기가 다릅니다. 패킷 전체 크기에서 헤더 크기를 빼고 페이로드 크기를 계산하는 것과 같습니다."),
  ]),
  plat_lede="바텀시트는 iOS와 안드로이드가 서로 다른 이름 체계로 부르고, 웹은 두 쪽 이름을 섞어 씁니다.",
  plats=plats([
    ("웹", "표준 지침 없음 · <code>&lt;dialog&gt;</code>",
     mini(sheet("해질녘 공원", ["공유하기", "내려받기"]), bars="684", label="웹 바텀시트 재현"),
     "<b>바텀시트</b> · 좁은 화면에서 모달 대신 쓰는 경우가 가장 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-sheet"><div class="ios-sheet__stack"><div class="ios-sheet__group"><span>공유하기</span><span>내려받기</span><span class="destructive">삭제</span></div><div class="ios-sheet__group"><span class="cancel">취소</span></div></div></div>', "iOS 액션 시트 재현"),
     "<b>시트</b>(Sheet) · 시트가 멈출 높이를 <b>디텐트</b>(detent, medium과 large)로 정합니다. 선택지만 늘어놓는 시트는 <b>액션 시트</b>라고 따로 부릅니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;inset:0;background:rgba(0,0,0,.4)"></div><div style="position:absolute;left:0;right:0;bottom:0;background:var(--surface);border-radius:16px 16px 0 0;padding:6px 8px 10px"><span style="display:block;width:22px;height:3px;border-radius:99px;background:var(--line-strong);margin:0 auto 6px"></span><b style="font-size:9px">해질녘 공원</b><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:2px 0">공유하기</i><i style="display:block;font-style:normal;font-size:8.5px;color:var(--fg-muted);padding:2px 0">내려받기</i></div>', "안드로이드 모달 바텀시트 재현"),
     "<b>바텀시트</b>(Bottom sheet) · 뒤를 막는 <b>Modal</b>, 막지 않는 <b>Standard</b>, 그리고 <b>Expanding</b>으로 나눠 부릅니다. 바텀시트라는 이름은 Material에서 굳어졌습니다."),
  ]),
  plat_note="iOS에서는 \"시트 띄워 주세요\"라는 말이 <b>화면 전환 방식</b>을 뜻할 수 있습니다. iOS의 시트는 모달 프레젠테이션의 한 형태여서, 웹에서 떠올리는 '아래에서 올라오는 작은 판'보다 가리키는 범위가 넓기 때문입니다. 그래서 무엇을 하는 판인지 역할을 함께 말해야 오해가 없습니다.",
  siblings=siblings("sheet"),
  related='''        <li><a href="safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="gesture.html"><b>제스처</b><em>9부</em></a></li>
        <li><a href="focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>''',
)
