# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def scene(inner, w="160px", h="86px"):
    return ('              <div style="position:relative;width:100%;max-width:' + w + ';height:' + h + ';'
            'border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">' + inner + '</div>')

BG = ('<div style="position:absolute;left:8px;top:8px;display:flex;gap:5px">'
      '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 1</span>'
      '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 2</span></div>')

def modal(extra=""):
    return ('<div style="position:absolute;inset:0;background:rgba(14,16,20,.45)"></div>'
            '<div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);width:112px;'
            'background:var(--surface);border-radius:7px;padding:9px;box-shadow:var(--e3);' + extra + '">'
            '<span style="font-size:10px;font-weight:700;display:block;margin-bottom:5px">확정할까요?</span>'
            '<span style="display:flex;gap:4px;justify-content:flex-end">'
            '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:2px 6px;font-size:8.5px">취소</span>'
            '<span style="background:var(--accent);color:#fff;border-radius:4px;padding:2px 6px;font-size:8.5px">확정</span>'
            '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:240px"><div style="position:relative;height:110px;border:1px solid var(--line);border-radius:7px;background:var(--surface);overflow:hidden">
                    <div style="position:absolute;left:10px;top:10px;display:flex;gap:6px">
                      <span style="border:1px solid var(--line-strong);border-radius:5px;padding:4px 8px;font-size:10px">배경 버튼</span>
                    </div>
                    <div style="position:absolute;inset:0;background:rgba(14,16,20,.45)"></div>
                    <div style="position:absolute;left:50%;top:54%;transform:translate(-50%,-50%);width:150px;background:var(--surface);border-radius:8px;padding:11px;box-shadow:var(--e3)">
                      <span style="font-size:11px;font-weight:700;display:block;margin-bottom:6px">정산을 확정할까요?</span>
                      <span style="display:flex;gap:5px;justify-content:flex-end">
                        <span style="border:1px solid var(--line-strong);border-radius:5px;padding:3px 8px;font-size:9.5px;outline:2px solid var(--accent);outline-offset:1px">취소</span>
                        <span style="background:var(--accent);color:#fff;border-radius:5px;padding:3px 8px;font-size:9.5px">확정</span>
                      </span>
                    </div>
                  </div></div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">showModal( )   — 브라우저가 포커스를 가둠</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">열 때 첫 요소에 focus( )로 옮김</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">닫을 때 모달을 연 버튼으로 돌려줌</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">Esc로 닫힘</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">show( ) · 직접 만든 모달   — 포커스가 밖으로 나감</div>
                </div>
              </div>'''

D = dict(
  slug="focustrap", ko="포커스 트랩", en="Focus trap",
  desc="모달이 열려 있는 동안 키보드 포커스를 모달 안에 가두는 이유와, 모달을 열고 닫을 때 포커스를 옮기는 세 가지 규칙을 다루는 항목입니다.",
  lede="포커스 트랩은 모달이 열려 있는 동안 키보드 포커스가 <b>모달 안에서만</b> 움직이게 하는 동작입니다. 포커스를 가두지 않으면 가림막에 가려 보이지 않는 배경 버튼으로 포커스가 넘어갑니다.",
  axes_lede="접근성은 눈으로는 보이지 않는 부분까지 챙기는 일입니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 가를 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>모달을 열고 <kbd>Tab</kbd>을 여러 번 눌러 보세요. 기록에 <b>'모달 밖'</b>이 찍히면 포커스가 모달 밖으로 빠져나간 것입니다.<br>
          <b>가두지 않고 열기</b>를 켜면 모달이 <code>show()</code>로 열리기 때문에 포커스가 모달 밖으로 빠져나갑니다.
          반면 <code>showModal()</code>로 열면 <b>브라우저가 포커스를 알아서 가두므로</b>, 이제는 포커스 트랩을 직접 만들 일이 거의 없습니다.<br>
          모달을 닫을 때 <b>모달을 연 버튼으로 포커스가 돌아가는 것</b>도 기록에 찍힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포커스 트랩, 포커스 가두기"),
    ("영어", "focus trap, focus containment, inert"),
    ("같이 쓰는 말",
     "모달 밖의 요소를 한꺼번에 포커스도 클릭도 받지 않게 만드는 속성은 <b><code>inert</code></b>이고, "
     "브라우저가 모달을 그리는 맨 위 층은 <b>최상위 레이어</b>(top layer)라고 부릅니다. "
     "모달을 닫은 뒤 포커스를 원래 자리로 돌려주는 것은 <b>포커스 복원</b>(focus restoration)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>모달</b> — 모달은 <b>부품</b>이고, 포커스 트랩은 모달이 해야 하는 <b>동작</b> 가운데 하나입니다.<br>"
     "<b>스크롤 잠금</b> — 배경이 스크롤되지 않게 막는 것은 포커스 트랩과 다른 문제이고, 모달에는 둘 다 필요합니다.<br>"
     "<b><code>aria-modal</code></b> — 이름은 비슷하지만 이 속성은 <b>포커스를 가두지 않습니다.</b> 지금 모달이 열려 있다고 스크린 리더에게 알리는 표시입니다."),
  ]),
  axes=ax("포커스 트랩"),
  oneline="포커스 트랩은 <b>세 가지 규칙을 함께</b> 지켜야 합니다. 모달을 열 때 포커스를 모달 안으로 옮기고, 열려 있는 동안에는 모달 안에서만 돌게 하고, 닫을 때는 모달을 연 버튼으로 돌려줍니다.",
  s4_title="포커스가 있어야 할 자리", s4_hint="모달을 열기 전부터 닫은 뒤까지",
  states=states([
    (scene(BG), "모달을 열기 전", "배경 버튼에 포커스가 있습니다"),
    (scene(BG + modal("outline:2px solid var(--accent);outline-offset:2px")),
     "모달을 열 때", "포커스를 <b>모달 안으로</b> 옮깁니다. 옮기지 않으면 포커스가 body에 남습니다"),
    (scene(BG + modal()), "모달이 열려 있는 동안", "Tab을 누르면 포커스가 <b>모달 안에서만</b> 돕니다"),
    (scene('<div style="position:absolute;left:8px;top:8px;display:flex;gap:5px">'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px;outline:2px solid var(--accent);outline-offset:1px">배경 1</span>'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 2</span></div>' + modal()),
     "포커스가 모달 밖으로 나갔을 때", "포커스가 <b>가림막 뒤</b>의 배경 버튼에 가 있지만, 가려져 있어서 눈으로는 보이지 않습니다"),
    (scene('<div style="position:absolute;left:8px;top:8px;display:flex;gap:5px">'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 1</span>'
           '<span style="background:var(--accent);color:#fff;border-radius:4px;padding:3px 7px;font-size:9px;outline:2px solid var(--accent);outline-offset:2px">열기</span></div>'),
     "모달을 닫은 뒤", "포커스가 <b>모달을 연 버튼</b>으로 돌아옵니다. 돌려주지 않으면 포커스가 페이지 맨 위로 가 버립니다"),
    (scene(BG + modal() + '<span style="position:absolute;right:7px;top:7px;font-size:8.5px;background:var(--ink-900);color:#fff;border-radius:3px;padding:2px 5px">Esc</span>'),
     "Esc를 눌렀을 때", "<kbd>Esc</kbd>를 누르면 모달이 <b>반드시 닫혀야</b> 합니다. 포커스가 갇힌 채 빠져나갈 방법이 없으면 가두지 않은 것보다 더 나쁩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("모달과 배경", "dialog + backdrop", "가림막 뒤의 배경은 <b>보이지도 눌리지도 않아야</b> 합니다"),
    ("가두기", "showModal()", "<b>브라우저가 알아서</b> 포커스를 가두고 배경을 <code>inert</code> 상태로 만듭니다"),
    ("열 때 포커스 옮기기", "focus()", "포커스를 모달 안의 <b>첫 요소</b>로 보냅니다. 보내지 않으면 포커스가 body에 남습니다"),
    ("닫을 때 포커스 돌려주기", "복원", "포커스를 <b>모달을 연 버튼</b>으로 돌려줍니다. 돌려주지 않으면 포커스가 화면 맨 위로 가 버립니다"),
    ("Esc로 닫기", "cancel", "모달을 닫을 방법이 반드시 있어야 합니다. <code>&lt;dialog&gt;</code>는 따로 코드를 쓰지 않아도 Esc로 닫힙니다"),
    ("직접 만든 모달", "div + position:fixed", "포커스가 모달 밖으로 빠져나가는 일은 <b>대부분 직접 만든 모달에서</b> 생깁니다. 가능하면 직접 만들지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>&lt;dialog&gt;</code>를 <code>showModal()</code>로 열면 <b>포커스 가두기, 배경 끄기, Esc로 닫기, 최상위 레이어</b>를
          브라우저가 모두 처리합니다. 모달을 직접 만들면 이 네 가지를 모두 코드로 짜야 하는데, 그중에서도
          <b>배경을 <code>inert</code>로 만드는 일</b>을 빠뜨리기 쉽습니다. 배경을 끄지 않으면 가림막에 가려 보이지 않는 배경 버튼을
          스크린 리더는 계속 읽습니다. 이 도감의 <a href="../items/modal.html">모달</a> 항목에서도 같은 내용을 다룹니다.</p>''',
  do=ul([
    "<b>모달 다이얼로그</b>처럼 뒤의 화면을 막는 부품을 띄울 때",
    "<b>바텀시트나 드로어</b>가 뒤의 화면을 막을 때",
    "전체 화면을 덮는 메뉴를 띄울 때",
  ]),
  dont=ul([
    "<b>뒤의 화면을 막지 않는</b> 부품을 띄울 때. 팝오버, 툴팁, 토스트에서는 포커스를 가두지 않습니다",
    "포커스를 가두기만 하고 <b>Esc로 닫을 수 없게</b> 만들 때. 빠져나갈 방법이 없으면 가두지 않은 것보다 더 나쁩니다",
    "모달을 닫은 뒤 포커스를 <b>돌려주지 않을</b> 때",
    "모달을 직접 만들면서 <code>inert</code>를 빠뜨릴 때",
  ]),
  dont_title="포커스 트랩을 쓰지 않거나 잘못 쓰는 경우",
  instead='뒤쪽 화면을 막지 않는 부품이라면 포커스를 가두지 않는 <a href="../items/popover.html">팝오버</a>나 <a href="../items/dialog.html">다이얼로그</a>를 씁니다. 모달이라는 부품 자체는 <a href="../items/modal.html">모달</a> 항목에서, 포커스 테두리는 <a href="focus.html">포커스</a> 항목에서 다룹니다.',
  cases=cases([
    (scene(BG + modal(), "190px"), "확인 모달에서 포커스 가두기", "포커스 트랩이 가장 흔하게 쓰이는 자리입니다. <code>showModal()</code> 한 줄이면 됩니다"),
    (scene('<div style="position:absolute;inset:0;background:rgba(14,16,20,.45)"></div>'
           '<div style="position:absolute;left:0;right:0;bottom:0;background:var(--surface);border-radius:8px 8px 0 0;padding:9px">'
           '<span style="display:block;width:26px;height:3px;border-radius:99px;background:var(--line-strong);margin:0 auto 6px"></span>'
           '<span style="font-size:10px;font-weight:700">정렬 기준</span></div>', "190px"),
     "뒤를 막는 바텀시트에서 가두기", "바텀시트도 뒤의 화면을 막는다면 모달과 <b>똑같이 포커스를 가둬야</b> 합니다"),
    (scene('<div style="position:absolute;inset:0;background:var(--surface)"></div>'
           '<div style="position:absolute;left:9px;top:9px;font-size:10px;font-weight:700">전체 화면 메뉴</div>'
           '<div style="position:absolute;right:9px;top:8px;font-size:11px">×</div>', "190px"),
     "전체 화면 메뉴에서 가두기", "폰에서 흔히 쓰는 메뉴입니다. <b>배경이 아예 보이지 않더라도</b> 포커스를 가둬야 합니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="포커스를 직접 가두지 말고 <b>브라우저에 맡깁니다</b>. 그러면 직접 적을 코드는 포커스를 옮기는 두 줄뿐입니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"dlg"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;정산을 확정할까요?&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"cancel"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"ok"</span>&gt;확정&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 열 때는 가두기를 브라우저에 맡기고, 포커스 이동만 직접 한다</span>
dlg.showModal();
cancel.focus();

<span class="c">// 닫을 때는 모달을 연 버튼으로 포커스를 돌려준다</span>
dlg.addEventListener(<span class="s">'close'</span>, () =&gt; openBtn.focus());

<span class="c">/* 직접 만든다면 배경을 꺼야 한다 */</span>
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"app"</span> <span class="a">inert</span>&gt;…&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "포커스가 모달 <b>안에서만</b> 돕니다. 마지막 요소 다음에는 첫 번째 요소로 갑니다"),
    ("<kbd>Shift</kbd>+<kbd>Tab</kbd>", "거꾸로 돕니다. 첫 번째 요소 앞에서는 마지막 요소로 갑니다"),
    ("<kbd>Esc</kbd>", "모달이 <b>반드시 닫혀야 합니다.</b> <code>&lt;dialog&gt;</code>는 기본으로 닫힙니다"),
    ("모달을 열 때", "모달 안의 첫 요소에 <code>.focus()</code>를 호출합니다. 제목에 <code>tabindex=\"-1\"</code>을 주고 제목으로 포커스를 보내기도 합니다"),
    ("모달을 닫을 때", "포커스를 <b>모달을 연 버튼</b>으로 돌려줍니다. 그 버튼이 사라졌다면 가장 가까운 요소로 보냅니다"),
    ("<code>inert</code>", "모달을 직접 만들 때는 배경에 <code>inert</code>를 걸어야 배경이 <b>스크린 리더에도</b> 읽히지 않습니다"),
  ]),
  backend=rows([
    ("모달을 라우팅으로 열 때", "주소가 바뀌면서 모달이 열린다면 <b>뒤로가기를 눌렀을 때 모달이 닫히는지</b>까지 정해야 합니다. 모달이 닫힌 뒤 포커스를 어디로 돌려줄지도 함께 정합니다."),
    ("모달 안에서 화면이 바뀌면", "모달 안에서 다음 단계로 넘어가면 이전 단계의 요소와 함께 포커스가 사라지므로, 포커스를 <b>새 단계의 제목</b>으로 옮겨 줘야 합니다."),
    ("모달 위에 모달을 열 때", "모달 위에 모달을 열면 포커스 가두기가 겹칩니다. <code>&lt;dialog&gt;</code>는 최상위 레이어에 차례로 쌓이므로 브라우저가 알아서 처리하지만, 모달을 직접 만들었다면 겹친 순서를 <b>직접 관리</b>해야 합니다."),
    ("포커스가 새는지 자동 검사", "모달을 열고 <kbd>Tab</kbd>을 20번 눌러 보면서 <b>모달 밖 요소에 포커스가 가는지</b> 확인하면 됩니다. 이 검사는 CI에서도 돌릴 수 있습니다."),
  ]),
  plat_lede="iOS와 안드로이드는 모달을 열면 <b>기본으로 포커스를 가둬</b> 줍니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt; showModal()",
     scene(BG + modal(), "120px", "72px"),
     "<code>showModal()</code>이 포커스 가두기, 배경 끄기, Esc로 닫기를 모두 처리합니다. 모달을 직접 만들면 이 기능을 모두 코드로 짜야 합니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.sheet { }<br>.alert { }</div>''',
     "화면을 <b>모달로 띄우면 포커스가 자동으로 갇힙니다</b>. VoiceOver도 모달 안의 내용만 읽습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Dialog { }<br>ModalBottomSheet</div>''',
     "다이얼로그가 <b>별도 윈도</b>로 뜨기 때문에 iOS처럼 포커스가 자동으로 갇힙니다. TalkBack도 그 윈도 안의 내용만 읽습니다."),
  ]),
  plat_note="앱에서는 <b>모달을 띄우기만 하면 포커스가 자동으로 갇혀서</b> 포커스가 빠져나가는 문제가 거의 생기지 않습니다. 웹에서도 <code>&lt;dialog&gt;</code>를 쓰면 앱과 같아지지만, <b>직접 만든 모달</b>에서는 여전히 포커스가 밖으로 빠져나갑니다. \"모달 접근성\" 문제로 이야기되는 사례는 대부분 직접 만든 모달에서 생깁니다.",
  siblings=siblings("focustrap"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>''',
)
