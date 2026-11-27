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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">showModal( )   — 브라우저가 가둔다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">열 때 안으로 — 첫 요소에 focus( )</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">닫을 때 — 부른 버튼으로 돌려준다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">Esc 로 닫힌다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">show( ) · 직접 만든 모달   — 밖으로 샌다</div>
                </div>
              </div>'''

D = dict(
  slug="focustrap", ko="포커스 트랩", en="Focus trap",
  desc="모달이 열린 동안 키보드를 그 안에 가두는 이유와, 열고 닫을 때 포커스를 옮기는 세 가지 규칙을 다루는 항목.",
  lede="모달이 열린 동안 키보드를 <b>그 안에만</b> 두는 것. 안 가두면 보이지도 않는 배경 버튼에 포커스가 가 있게 됩니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>모달을 열고 <kbd>Tab</kbd>을 여러 번 눌러 보세요. 기록에 <b>'모달 밖'</b>이 찍히면 그게 사고입니다.<br>
          <b>가두지 않고 열기</b>를 켜면 <code>show()</code>로 열려 포커스가 샙니다.
          <code>showModal()</code>로 열면 <b>브라우저가 알아서 가둡니다</b> — 직접 만들 일이 거의 없어졌습니다.<br>
          닫을 때 <b>부른 버튼으로 포커스가 돌아가는 것</b>도 기록에 찍힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포커스 트랩, 포커스 가두기"),
    ("영어", "focus trap, focus containment, inert"),
    ("같이 쓰는 말",
     "모달 밖을 통째로 끄는 속성이 <b><code>inert</code></b>이고, "
     "브라우저가 모달을 그리는 맨 위 층을 <b>최상위 레이어</b>(top layer)라 합니다. "
     "닫은 뒤 포커스를 돌려주는 것을 <b>포커스 복원</b>(focus restoration)이라 합니다."),
    ("자주 잘못 부름",
     "<b>모달</b> — 모달은 <b>부품</b>이고 포커스 트랩은 그 안의 <b>동작</b>입니다.<br>"
     "<b>스크롤 잠금</b> — 배경 스크롤을 막는 것은 다른 문제입니다. 둘 다 필요합니다.<br>"
     "<b><code>aria-modal</code></b> — 이름이 비슷하지만 <b>가두지 않습니다.</b> 스크린 리더에게 알리는 표시일 뿐입니다."),
  ]),
  axes=ax("포커스 트랩"),
  oneline="포커스 트랩은 <b>세 가지가 한 세트</b>입니다 — 열 때 안으로, 도는 동안 안에서, 닫을 때 부른 버튼으로.",
  s4_title="상태", s4_hint="열고 돌고 닫는 세 순간",
  states=states([
    (scene(BG), "열기 전", "배경 버튼에 포커스가 있다"),
    (scene(BG + modal("outline:2px solid var(--accent);outline-offset:2px")),
     "열 때", "<b>모달 안으로</b> 포커스를 넣는다. 안 넣으면 body 에 남는다"),
    (scene(BG + modal()), "도는 동안", "Tab 이 <b>모달 안에서만</b> 돈다"),
    (scene('<div style="position:absolute;left:8px;top:8px;display:flex;gap:5px">'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px;outline:2px solid var(--accent);outline-offset:1px">배경 1</span>'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 2</span></div>' + modal()),
     "샜을 때", "<b>가림막 뒤</b>에 포커스가 가 있다. 눈으로는 안 보인다"),
    (scene('<div style="position:absolute;left:8px;top:8px;display:flex;gap:5px">'
           '<span style="border:1px solid var(--line-strong);border-radius:4px;padding:3px 7px;font-size:9px">배경 1</span>'
           '<span style="background:var(--accent);color:#fff;border-radius:4px;padding:3px 7px;font-size:9px;outline:2px solid var(--accent);outline-offset:2px">열기</span></div>'),
     "닫은 뒤", "<b>부른 버튼</b>으로 돌아온다. 안 돌려주면 맨 위로 튕긴다"),
    (scene(BG + modal() + '<span style="position:absolute;right:7px;top:7px;font-size:8.5px;background:var(--ink-900);color:#fff;border-radius:3px;padding:2px 5px">Esc</span>'),
     "Esc", "<b>반드시 닫혀야</b> 한다. 갇힌 채 못 나가면 더 나쁘다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("모달과 배경", "dialog + backdrop", "가림막 뒤의 배경은 <b>보이지도 눌리지도 않아야</b> 한다"),
    ("가두기", "showModal()", "<b>브라우저가 알아서</b> 가두고 배경을 <code>inert</code> 로 만든다"),
    ("열 때", "focus()", "모달 안 <b>첫 요소</b>로 보낸다. 안 보내면 포커스가 body 에 남는다"),
    ("닫을 때", "복원", "<b>부른 버튼</b>으로 돌려준다. 안 돌려주면 화면 맨 위로 튕긴다"),
    ("Esc", "cancel", "닫을 길이 반드시 있어야 한다. <code>&lt;dialog&gt;</code>는 공짜로 해 준다"),
    ("직접 만든 모달", "div + position:fixed", "<b>여기서 전부 새는</b> 일이 생긴다. 가능하면 안 만든다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>&lt;dialog&gt;</code>를 <code>showModal()</code>로 열면 <b>가두기·배경 끄기·Esc·최상위 레이어</b>가
          전부 따라옵니다. 직접 만들면 그 넷을 다 짜야 하고, 특히
          <b>배경을 <code>inert</code>로 만드는 것</b>을 빠뜨리기 쉽습니다 — 그러면 눈에 안 보이는 배경 버튼이
          스크린 리더에는 계속 읽힙니다. 이 도감의 <a href="../items/modal.html">모달</a> 항목과 같은 이야기입니다.</p>''',
  do=ul([
    "<b>모달 다이얼로그</b> — 뒤를 막는 모든 것",
    "<b>바텀시트·드로어</b>가 뒤를 막을 때",
    "전체 화면을 덮는 메뉴",
  ]),
  dont=ul([
    "<b>뒤를 안 막는</b> 것에 거는 것 — 팝오버·툴팁·토스트는 가두지 않습니다",
    "가두기만 하고 <b>Esc 를 안 주는</b> 것 — 못 나가면 더 나쁩니다",
    "닫은 뒤 포커스를 <b>안 돌려주는</b> 것",
    "직접 만들면서 <code>inert</code>를 빠뜨리는 것",
  ]),
  instead='뒤를 안 막으면 <a href="../items/popover.html">팝오버</a>·<a href="../items/dialog.html">다이얼로그</a>, 부품 자체는 <a href="../items/modal.html">모달</a>, 테두리는 <a href="focus.html">포커스</a>.',
  cases=cases([
    (scene(BG + modal(), "190px"), "확인 모달", "가장 흔한 자리. <code>showModal()</code> 한 줄이면 된다"),
    (scene('<div style="position:absolute;inset:0;background:rgba(14,16,20,.45)"></div>'
           '<div style="position:absolute;left:0;right:0;bottom:0;background:var(--surface);border-radius:8px 8px 0 0;padding:9px">'
           '<span style="display:block;width:26px;height:3px;border-radius:99px;background:var(--line-strong);margin:0 auto 6px"></span>'
           '<span style="font-size:10px;font-weight:700">정렬 기준</span></div>', "190px"),
     "바텀시트", "뒤를 막으면 <b>똑같이 가둬야</b> 한다"),
    (scene('<div style="position:absolute;inset:0;background:var(--surface)"></div>'
           '<div style="position:absolute;left:9px;top:9px;font-size:10px;font-weight:700">전체 화면 메뉴</div>'
           '<div style="position:absolute;right:9px;top:8px;font-size:11px">×</div>', "190px"),
     "전체 화면 메뉴", "폰에서 흔하다. <b>배경이 아예 안 보여도</b> 가둬야 한다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 동작의 계약서",
  code_lede="직접 가두지 말고 <b>브라우저에 맡깁니다</b>. 적을 것은 포커스를 옮기는 두 줄뿐입니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"dlg"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;정산을 확정할까요?&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"cancel"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"ok"</span>&gt;확정&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 열 때 — 가두기는 브라우저가, 포커스만 내가</span>
dlg.showModal();
cancel.focus();

<span class="c">// 닫을 때 — 부른 버튼으로 돌려준다</span>
dlg.addEventListener(<span class="s">'close'</span>, () =&gt; openBtn.focus());

<span class="c">/* 직접 만든다면 배경을 꺼야 한다 */</span>
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"app"</span> <span class="a">inert</span>&gt;…&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "모달 <b>안에서만</b> 돈다. 마지막 다음은 첫 번째로"),
    ("<kbd>Shift</kbd>+<kbd>Tab</kbd>", "거꾸로. 첫 번째 앞은 마지막으로"),
    ("<kbd>Esc</kbd>", "<b>반드시 닫힌다.</b> <code>&lt;dialog&gt;</code>는 기본으로 해 준다"),
    ("열 때", "모달 안 첫 요소로 <code>.focus()</code>. 제목에 <code>tabindex=\"-1\"</code>을 주고 거기로 보내기도 한다"),
    ("닫을 때", "<b>부른 버튼</b>으로 돌려준다. 그 버튼이 사라졌으면 가까운 곳으로"),
    ("<code>inert</code>", "직접 만들 때는 배경을 꺼야 <b>스크린 리더에도</b> 안 읽힌다"),
  ]),
  backend=rows([
    ("모달을 라우팅으로 열 때", "주소가 바뀌며 열리면 <b>뒤로가기로 닫히는지</b>까지 정해야 합니다. 닫힌 뒤 포커스를 어디로 돌려줄지도 같이 정합니다."),
    ("모달 안에서 화면이 바뀌면", "단계가 넘어가면 포커스가 사라집니다. <b>새 단계의 제목</b>으로 옮겨 줘야 합니다."),
    ("여러 겹의 모달", "모달 위에 모달을 열면 가두기가 겹칩니다. <code>&lt;dialog&gt;</code>는 최상위 레이어에 쌓여 알아서 되지만, 직접 만들면 <b>직접 관리</b>해야 합니다."),
    ("자동 검사", "모달을 열고 <kbd>Tab</kbd>을 20번 눌러 <b>모달 밖 요소에 포커스가 가는지</b> 보면 됩니다. CI 에서 돌릴 수 있습니다."),
  ]),
  plat_lede="두 OS 는 모달을 열면 <b>기본으로 가둬</b> 줍니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt; showModal()",
     scene(BG + modal(), "120px", "72px"),
     "<code>showModal()</code> 이 가두기·배경 끄기·Esc 를 전부 해 줍니다. 직접 만들면 다 짜야 합니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.sheet { }<br>.alert { }</div>''',
     "<b>모달로 띄우면 자동</b>입니다. VoiceOver 도 그 안만 읽습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Dialog { }<br>ModalBottomSheet</div>''',
     "<b>별도 윈도</b>로 떠서 역시 자동입니다. TalkBack 도 그 안만 읽습니다."),
  ]),
  plat_note="앱에서는 <b>모달을 띄우면 가두기가 공짜</b>라 이 문제 자체가 거의 없습니다. 웹에서도 <code>&lt;dialog&gt;</code>를 쓰면 같아지는데, <b>직접 만든 모달</b>에서만 여전히 샙니다 — \"모달 접근성\" 이야기의 대부분이 그 경우입니다.",
  siblings=siblings("focustrap"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/drawer.html"><b>드로어</b><em>6부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>''',
)
