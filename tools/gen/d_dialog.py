# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:var(--r2);padding:12px;position:relative;min-height:188px">
                <div style="font-size:10.5px;color:var(--fg-muted);line-height:1.9">이관 자체는 예정보다 이틀 빨리 끝났지만,<br>장애 대응 절차가 문서로 남아 있지 않아<br>새벽에 연락이 두 번 더 오갔다.</div>
                <div data-pin="2" style="position:absolute;right:12px;top:30px;width:190px;background:var(--surface);border:1px solid var(--line);border-radius:8px;box-shadow:var(--e3)">
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:8px;padding:9px 26px 8px;border-bottom:1px solid var(--line)">
                    <b style="flex:1;font-size:11.5px">찾기</b>
                    <span class="pin-tr" data-pin="4" style="color:var(--fg-muted);font-size:13px;line-height:1">&times;</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="padding:10px 26px 8px">
                    <span style="display:block;border:1px solid var(--line-strong);border-radius:5px;padding:5px 8px;font-size:10.5px">결제</span>
                  </div>
                  <div class="pin-out" data-pin="6" style="padding:0 26px 11px;display:flex;align-items:center;gap:9px">
                    <span style="flex:1;font-size:9.5px;color:var(--fg-muted)">2 / 4곳</span>
                    <span style="background:var(--accent);color:#fff;border-radius:5px;padding:4px 10px;font-size:10px;font-weight:700">다음</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="dialog", ko="다이얼로그", en="Dialog (modeless · modal)",
  desc="다이얼로그가 무엇인지, 모달과는 어떤 관계인지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="다이얼로그는 사용자에게 무언가를 묻거나 입력을 받으려고 화면 위에 띄우는 <b>대화 상자</b>입니다. 뒤쪽 화면을 막으면 <b>모달</b>, 막지 않으면 <b>비모달</b>이라고 부르기 때문에 모달은 다이얼로그의 한 종류입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>찾기를 열어 둔 채 뒤쪽 글을 읽어 보세요.</b> 비모달이라서 뒤쪽 글을 스크롤할 수도 있고 글자를 선택할 수도 있습니다.
          옆의 <b>나가기 확인</b>은 같은 <code>&lt;dialog&gt;</code> 요소를 <code>showModal()</code>로 연 것인데, 이렇게 열면 뒤쪽 화면이 막히고 <kbd>Tab</kbd>으로 옮기는 포커스도 다이얼로그 안에서만 돕니다.
          <b>모달과 비모달은 어느 메서드로 여느냐로만 갈립니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "다이얼로그, 대화 상자"),
    ("영어", "dialog"),
    ("같이 쓰는 말", "뒤쪽 화면을 막는 것은 <b>모달 다이얼로그</b>, 막지 않는 것은 <b>비모달</b>(modeless·non-modal)이라고 부릅니다. 답 하나를 받으려고 띄우는 작은 모달은 <b>얼럿 다이얼로그</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>모달</b> — 모달은 다이얼로그의 <b>한 종류</b>일 뿐이어서, 뒤를 막지 않는 다이얼로그를 모달이라고 부르면 틀립니다.<br>"
     "<b>팝업</b> — 브라우저가 새로 여는 팝업 창과 이름이 겹쳐서 헷갈립니다.<br>"
     "<b>창</b> — 운영체제의 윈도와 헷갈립니다. 다이얼로그는 별도의 창이 아니라 페이지 안에 그려집니다."),
  ]),
  states=states([
    (mini(trigger("찾기"), bars="684", label="다이얼로그가 닫힌 화면"), "닫혀 있을 때", "트리거만 보입니다"),
    (mini('<div class="mini__pop" style="right:5px;top:14px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div>', bars="684", label="비모달 다이얼로그가 열린 모습"), "비모달로 열었을 때", "<b>스크림이 없어서</b> 뒤쪽 글이 그대로 밝게 보이고, 누르거나 선택할 수도 있습니다"),
    (mini('<div class="mini__scrim"><div class="mini__card"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="mini__btns"><span class="mini__btn mini__btn--ghost">계속</span><span class="mini__btn">나가기</span></div></div></div>', bars="684", label="모달 다이얼로그가 열린 모습"), "모달로 열었을 때", "같은 부품을 <code>showModal()</code>로 열었기 때문에 뒤쪽 화면이 막힙니다"),
    (mini('<div class="mini__pop" style="right:5px;top:10px;width:66px"><b style="font-size:8px;display:block">찾기</b><i>결제</i></div><div class="mini__pop" style="right:16px;top:40px;width:66px"><b style="font-size:8px;display:block">서식</b><i>굵게 · 기울임</i></div>', bars="684", label="비모달 다이얼로그 두 개가 열린 모습"), "여러 개를 함께 띄웠을 때", "비모달은 <b>동시에 여러 개</b> 띄울 수 있지만, 모달은 여러 개를 겹쳐 띄우면 안 됩니다"),
    (mini('<div class="mini__pop" style="right:14px;top:22px;width:70px;transform:rotate(-2deg)"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div><div style="position:absolute;left:6px;bottom:6px;font-size:7.5px;color:var(--fg-muted)">제목 줄을 끌어 옮김</div>', bars="684", label="다이얼로그를 옮기는 중"), "끌어서 옮기는 중", "다이얼로그가 뒤쪽 내용을 가리면 끌어서 옮길 수 있어야 합니다. 모달에는 없는 조작입니다"),
    (mini('<div class="mini__pop" style="right:5px;top:14px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div><div style="position:absolute;left:7px;top:34px;background:#ffe08a;border-radius:2px;padding:0 3px;font-size:8px;color:#14161a">결제</div>', bars="684", label="뒤쪽에서 결과가 바뀌는 모습"), "뒤쪽 화면이 계속 바뀔 때", "다이얼로그를 띄워 둔 채로 뒤쪽 내용이 바뀝니다. 비모달을 쓰는 이유가 이것입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤쪽 내용", "background content", "<b>어두워지지 않습니다.</b> 스크림이 없다는 점이 비모달과 모달을 가르는 가장 큰 차이입니다"),
    ("다이얼로그", "dialog surface", "모달보다 작고 그림자도 약하며, 화면 구석에 붙여 두는 경우가 많습니다"),
    ("제목 줄", "title bar", "무엇을 하는 다이얼로그인지 알려 주고, 끌어서 옮기는 손잡이 역할도 합니다"),
    ("닫기", "close", "비모달은 사용자가 닫을 때까지 계속 떠 있기 때문에 모달보다 닫기 버튼이 더 중요합니다"),
    ("내용", "content", "뒤쪽 화면을 보면서 쓰는 것이라 작고 단순하게 만듭니다"),
    ("액션 영역", "actions", "'다음 찾기'처럼 <b>여러 번 누르는</b> 버튼이 놓입니다. 모달에서는 버튼을 한 번 누르면 다이얼로그가 닫힙니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          모달의 해부도(<a href="modal.html#s5">모달 ⑤칸</a>)와 비교해 보면 <b>스크림이 없다</b>는 점만
          다릅니다. 하지만 스크림이 없으면 뒤쪽 화면을 계속 쓸 수 있으므로, 포커스를 가두지 않고 배경 스크롤도 잠그지 않으며 다른 창과의 겹침 순서도 따로 정해야 합니다.</p>''',
  do=ul([
    "찾기·바꾸기처럼 <b>뒤쪽 화면을 보면서</b> 일할 때",
    "도구 창이나 속성 패널처럼 열어 둔 채 여러 번 쓸 때",
    "보조 정보를 오래 띄워 두고 참고할 때",
  ]),
  dont=ul([
    "꼭 답을 받아야 할 때. 비모달은 사용자가 무시하고 지나갈 수 있으니 모달을 씁니다",
    "되돌릴 수 없는 작업을 확인받을 때. 이때도 모달을 씁니다",
    "화면이 좁을 때. 다이얼로그를 띄우면 뒤쪽을 볼 자리가 남지 않아서 비모달로 둘 이유가 없습니다",
    "비모달을 여러 개 띄우면서 겹침 순서를 정하지 않을 때",
  ]),
  instead='사용자의 답을 꼭 받아야 하면 <a href="modal.html">모달</a>을 쓰고, 누른 요소 바로 옆에 붙어 떠야 하면 <a href="popover.html">팝오버</a>가 맞습니다. 화면 옆에 길게 열어 두고 쓸 것이라면 <a href="drawer.html">드로어</a>를, 결과를 알리기만 하면 된다면 <a href="toast.html">토스트</a>를 씁니다.',
  cases=cases([
    (mini('<div class="mini__pop" style="right:5px;top:12px;width:72px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기 · 바꾸기</b><i>결제 ▸ 4곳</i><i>바꿀 말</i></div>', bars="684", tall=False, label="찾기 바꾸기 다이얼로그 재현"),
     "문서를 보면서 찾기·바꾸기", "비모달을 쓰는 대표적인 예입니다. 찾은 글자를 뒤쪽 문서에서 확인해야 하므로 뒤쪽 글이 보여야 합니다"),
    (mini('<div class="mini__pop" style="right:5px;top:10px;width:64px"><b style="font-size:8px;display:block;margin-bottom:3px">서식</b><i>굵게 · 기울임</i><i>글자 크기</i></div>', bars="684", tall=False, label="서식 패널 재현"),
     "도구 창을 열어 두고 여러 번 쓰기", "열어 둔 채 여러 번 쓰는 창이라, 사용자가 닫기 전에는 닫으라고 요구하지 않습니다"),
    (mini('<div class="mini__scrim"><div class="mini__card"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="mini__btns"><span class="mini__btn mini__btn--ghost">계속</span><span class="mini__btn mini__btn--danger">나가기</span></div></div></div>', bars="684", tall=False, label="모달 다이얼로그 재현"),
     "같은 부품을 모달로 열기", "같은 부품을 다른 방식으로 연 것입니다. 모달은 답하기 전에는 뒤쪽 화면으로 돌아갈 수 없습니다"),
  ]),
  code_lede="모달과 비모달은 같은 <code>&lt;dialog&gt;</code> 요소를 어느 메서드로 여느냐만 다릅니다. 아래 코드의 <code>show()</code>와 <code>showModal()</code> 두 줄이 그 차이입니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"dlg"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;…&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 비모달. 뒤를 막지 않고 포커스도 가두지 않는다</span>
dlg.show();

<span class="c">// 모달. 뒤가 inert 가 되고 포커스가 안에 갇힌다</span>
dlg.showModal();

<span class="c">// 지금 어느 쪽으로 열려 있는지 물어볼 수 있다</span>
dlg.matches(<span class="s">':modal'</span>);   <span class="c">// showModal() 로 열었으면 true</span>

<span class="c">// 비모달은 자리를 직접 잡아 줘야 한다 (모달처럼 가운데로 안 온다)</span>
dialog.dlg <span class="a">{</span> <span class="t">position</span>: fixed; <span class="t">top</span>: 72px; <span class="t">right</span>: 20px; <span class="t">margin</span>: 0; <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "모달과 비모달 모두 닫힙니다. <code>&lt;dialog&gt;</code> 요소가 알아서 처리합니다"),
    ("<kbd>Tab</kbd>", "<b>모달에서만</b> 포커스가 안에 갇히고, 비모달에서는 뒤쪽 화면으로 이어집니다"),
    ("뒤쪽 화면의 스크롤", "모달일 때만 잠급니다. 비모달은 뒤쪽 화면을 쓰려고 띄우는 것이라 그대로 둡니다"),
    ("다이얼로그가 열릴 때", "포커스를 첫 입력 칸으로 옮깁니다. 비모달은 사용자가 뒤쪽에서 하던 일이 있으니 포커스를 옮길지 더 신중하게 정합니다"),
    ("다이얼로그가 닫힐 때", "포커스를 다이얼로그를 열었던 요소로 돌려보냅니다. 모달과 비모달 모두 이 처리를 직접 해야 합니다"),
  ]),
  backend=rows([
    ("show()는 비동기 호출, showModal()은 동기 호출", "비모달은 띄워 놓고 다른 일을 계속하는 반면, 모달은 사용자의 답이 올 때까지 흐름을 멈춥니다. 비동기 호출에 <code>await</code>를 붙이느냐 붙이지 않느냐를 고르는 것과 같습니다."),
    ("여러 비모달은 동시에 열린 세션과 같음", "비모달은 여러 개가 동시에 떠 있을 수 있어서 <b>겹침 순서와 포커스를 관리</b>해야 합니다. 모달은 한 번에 하나만 띄우므로 이런 관리가 필요 없습니다."),
    ("뒤쪽 화면의 상태와 묶여 있음", "찾기 다이얼로그는 뒤쪽 문서의 내용을 계속 읽어 와야 합니다. 그래서 다이얼로그를 띄우면서 뒤쪽 화면의 상태 갱신을 멈추면 찾기 기능이 동작하지 않습니다."),
    ("무시할 수 있어 처리를 보장하지 않음", "비모달은 사용자가 응답하지 않고 지나칠 수 있기 때문에 <b>반드시 처리돼야 하는 일은 비모달에 담지 않습니다.</b>"),
  ]),
  plat_lede="모바일은 화면이 좁아서 비모달 다이얼로그를 거의 쓰지 않습니다. 그래서 모바일에서 '다이얼로그'라고 하면 대개 모달을 뜻합니다.",
  plats=plats([
    ("웹", "<code>&lt;dialog&gt;</code>",
     mini('<div class="mini__pop" style="right:5px;top:12px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div>', bars="684", label="웹 비모달 다이얼로그 재현"),
     "<b>다이얼로그</b> · <code>&lt;dialog&gt;</code> 요소 하나로 모달과 비모달을 모두 만듭니다. 모달과 비모달을 또렷하게 나누는 곳은 웹뿐입니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-alert"><div class="ios-alert__box"><div><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p></div><div class="ios-alert__btns"><span>계속</span><span style="color:#ff453a">나가기</span></div></div></div>', "iOS 얼럿 재현"),
     "<b>얼럿</b>(Alert) · <b>모달만</b> 있습니다. 비모달에 해당하는 것은 macOS의 <b>패널</b>(panel)이고, iOS에는 이에 해당하는 부품이 거의 없습니다."),
    ("안드로이드", "Material 3",
     phone('<div class="md-dialog"><div class="md-dialog__box"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="md-dialog__btns"><span>계속</span><span class="filled">나가기</span></div></div></div>', "안드로이드 다이얼로그 재현"),
     "<b>다이얼로그</b>(Dialog) · 기본이 모달입니다. 뒤를 막지 않아야 하면 다이얼로그가 아니라 <b>바텀시트</b>나 <b>스낵바</b>를 씁니다."),
  ]),
  plat_note="모바일에서는 \"다이얼로그 띄워 주세요\"라는 말을 <b>모달</b>을 띄워 달라는 뜻으로 알아듣습니다. 그래서 뒤를 막지 않는 창을 원한다면 '뒤쪽 화면을 보면서 쓰는 창'처럼 역할을 함께 말해야 합니다.",
  siblings=siblings("dialog"),
  related='''        <li><a href="focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>
        <li><a href="commandpalette.html"><b>커맨드 팔레트</b><em>6부</em></a></li>
        <li><span class="na"><b>확인 요청의 수준</b><em>8부</em></span></li>''',
)
