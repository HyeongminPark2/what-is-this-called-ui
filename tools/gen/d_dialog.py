# -*- coding: utf-8 -*-
from parts import *
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

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
  desc="다이얼로그가 무엇이고 모달과 어떤 관계인지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="사용자와 주고받으려고 띄우는 <b>대화 상자</b>. 뒤를 막으면 <b>모달</b>, 안 막으면 <b>비모달</b>입니다 — 모달은 다이얼로그의 한 종류입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>찾기를 열어 둔 채 뒤쪽 글을 읽어 보세요.</b> 스크롤도 되고 글자도 선택됩니다.
          옆의 <b>나가기 확인</b>은 똑같은 <code>&lt;dialog&gt;</code>를 <code>showModal()</code>로 연 것입니다 — 뒤가 막히고 <kbd>Tab</kbd>이 갇힙니다.
          <b>메서드 한 글자가 모달과 비모달을 가릅니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "다이얼로그, 대화 상자"),
    ("영어", "dialog"),
    ("같이 쓰는 말", "뒤를 막는 것이 <b>모달 다이얼로그</b>, 안 막는 것이 <b>비모달</b>(modeless·non-modal). 답을 하나 받으려고 띄우는 작은 모달은 <b>얼럿 다이얼로그</b>."),
    ("자주 잘못 부름",
     "<b>모달</b> — 모달은 다이얼로그의 <b>한 종류</b>입니다. 모든 다이얼로그가 모달은 아닙니다.<br>"
     "<b>팝업</b> — 브라우저의 새 창과 섞입니다.<br>"
     "<b>창</b> — 운영체제의 윈도와 헷갈립니다. 다이얼로그는 페이지 안에 있습니다."),
  ]),
  axes=axis_table("다이얼로그"),
  oneline="다이얼로그는 <b>상위 개념</b>이고, 뒤를 막는지로 모달과 비모달이 갈립니다. 코드로는 <code>showModal()</code> 이냐 <code>show()</code> 냐 한 글자 차이입니다.",
  states=states([
    (mini(trigger("찾기"), bars="684", label="다이얼로그가 닫힌 화면"), "닫힘", "트리거만 보인다"),
    (mini('<div class="mini__pop" style="right:5px;top:14px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div>', bars="684", label="비모달 다이얼로그가 열린 모습"), "비모달 열림", "<b>스크림이 없다.</b> 뒤쪽 글이 그대로 밝고 만져진다"),
    (mini('<div class="mini__scrim"><div class="mini__card"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="mini__btns"><span class="mini__btn mini__btn--ghost">계속</span><span class="mini__btn">나가기</span></div></div></div>', bars="684", label="모달 다이얼로그가 열린 모습"), "모달 열림", "같은 부품인데 <code>showModal()</code> 로 열었다. 뒤가 막힌다"),
    (mini('<div class="mini__pop" style="right:5px;top:10px;width:66px"><b style="font-size:8px;display:block">찾기</b><i>결제</i></div><div class="mini__pop" style="right:16px;top:40px;width:66px"><b style="font-size:8px;display:block">서식</b><i>굵게 · 기울임</i></div>', bars="684", label="비모달 다이얼로그 두 개가 열린 모습"), "여러 개", "비모달은 <b>동시에 여럿</b> 띄울 수 있다. 모달은 쌓으면 안 된다"),
    (mini('<div class="mini__pop" style="right:14px;top:22px;width:70px;transform:rotate(-2deg)"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div><div style="position:absolute;left:6px;bottom:6px;font-size:7.5px;color:var(--fg-muted)">제목 줄을 끌어 옮긴다</div>', bars="684", label="다이얼로그를 옮기는 중"), "옮기는 중", "뒤를 가릴 때 치울 수 있어야 한다. 모달에는 없는 조작"),
    (mini('<div class="mini__pop" style="right:5px;top:14px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div><div style="position:absolute;left:7px;top:34px;background:#ffe08a;border-radius:2px;padding:0 3px;font-size:8px;color:#14161a">결제</div>', bars="684", label="뒤쪽에서 결과가 바뀌는 모습"), "뒤쪽이 살아 있음", "다이얼로그를 둔 채 뒤쪽 내용이 바뀐다. 비모달의 존재 이유"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤쪽 내용", "background content", "<b>어둡지 않다.</b> 스크림이 없다는 것이 비모달의 전부라 해도 된다"),
    ("다이얼로그", "dialog surface", "모달보다 작고 그림자도 약하다. 화면 구석에 붙여 두는 일이 많다"),
    ("제목 줄", "title bar", "무엇을 하는 창인지. 끌어서 옮기는 손잡이를 겸한다"),
    ("닫기", "close", "비모달은 사용자가 닫을 때까지 떠 있으니 닫기가 더 중요하다"),
    ("내용", "content", "뒤쪽을 보면서 하는 일이라 작고 단순해야 한다"),
    ("액션 영역", "actions", "'다음 찾기'처럼 <b>여러 번 누르는</b> 버튼이 온다. 모달은 한 번 누르면 끝이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          모달의 해부도(<a href="modal.html#s5">모달 ⑤칸</a>)와 비교해 보면 <b>스크림이 없다</b>는 것 하나가
          다릅니다. 그 하나가 포커스·스크롤·겹침 순서까지 전부 바꿉니다.</p>''',
  do=ul([
    "찾기·바꾸기처럼 <b>뒤쪽을 보면서</b> 하는 일",
    "도구 창·속성 패널 — 열어 둔 채 여러 번 쓰는 것",
    "길게 띄워 두고 참고하는 보조 정보",
  ]),
  dont=ul([
    "꼭 답을 받아야 할 때 → 모달. 비모달은 무시하고 지나갈 수 있습니다",
    "되돌릴 수 없는 일의 확인 → 모달",
    "좁은 화면 — 뒤쪽을 볼 자리가 없어 비모달의 이점이 사라집니다",
    "비모달을 여러 개 띄워 두고 겹침 순서를 안 정하기",
  ]),
  instead='답을 꼭 받아야 하면 <a href="modal.html">모달</a>, 누른 것 옆에 붙어야 하면 <a href="popover.html">팝오버</a>, 옆에 길게 두고 쓰면 <a href="drawer.html">드로어</a>, 알려만 주면 <a href="toast.html">토스트</a>.',
  cases=cases([
    (mini('<div class="mini__pop" style="right:5px;top:12px;width:72px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기 · 바꾸기</b><i>결제 ▸ 4곳</i><i>바꿀 말</i></div>', bars="684", tall=False, label="찾기 바꾸기 다이얼로그 재현"),
     "찾기 · 바꾸기", "비모달의 교과서. 뒤쪽 글이 보여야 쓸 수 있다"),
    (mini('<div class="mini__pop" style="right:5px;top:10px;width:64px"><b style="font-size:8px;display:block;margin-bottom:3px">서식</b><i>굵게 · 기울임</i><i>글자 크기</i></div>', bars="684", tall=False, label="서식 패널 재현"),
     "도구 창", "열어 둔 채 여러 번 쓴다. 닫으라고 조르지 않는다"),
    (mini('<div class="mini__scrim"><div class="mini__card"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="mini__btns"><span class="mini__btn mini__btn--ghost">계속</span><span class="mini__btn mini__btn--danger">나가기</span></div></div></div>', bars="684", tall=False, label="모달 다이얼로그 재현"),
     "모달 다이얼로그", "같은 부품의 다른 열기 방식. 이쪽은 답하기 전에는 못 지나간다"),
  ]),
  code_lede="같은 요소를 어떻게 여느냐만 다릅니다. 이 두 줄이 이 항목의 전부입니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"dlg"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span>&gt;…&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 비모달 — 뒤를 막지 않는다. 포커스도 안 가둔다</span>
dlg.show();

<span class="c">// 모달 — 뒤가 inert 가 되고 포커스가 갇힌다</span>
dlg.showModal();

<span class="c">// 지금 어느 쪽으로 열려 있는지 물어볼 수 있다</span>
dlg.matches(<span class="s">':modal'</span>);   <span class="c">// showModal() 로 열었으면 true</span>

<span class="c">// 비모달은 자리를 직접 잡아 줘야 한다 (모달처럼 가운데로 안 온다)</span>
dialog.dlg <span class="a">{</span> <span class="t">position</span>: fixed; <span class="t">top</span>: 72px; <span class="t">right</span>: 20px; <span class="t">margin</span>: 0; <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "양쪽 다 닫힌다. <code>&lt;dialog&gt;</code>가 해 준다"),
    ("<kbd>Tab</kbd>", "<b>모달만</b> 갇힌다. 비모달은 뒤쪽 화면으로 이어진다"),
    ("배경 스크롤", "모달만 잠근다. 비모달은 그대로 둔다 — 그게 쓰는 이유다"),
    ("열릴 때", "포커스를 첫 입력칸으로. 비모달은 뒤에서 하던 일이 있으니 더 조심한다"),
    ("닫힐 때", "포커스가 열었던 곳으로 돌아간다. 양쪽 다 직접 해 줘야 한다"),
  ]),
  backend=rows([
    ("show() = 비동기 · showModal() = 동기", "비모달은 띄워 놓고 다른 일을 계속합니다. 모달은 답이 올 때까지 멈춥니다. <code>await</code> 를 붙이느냐 안 붙이느냐와 같은 선택입니다."),
    ("비모달 여럿 = 동시 세션", "여러 개가 동시에 떠 있을 수 있어 <b>겹침 순서와 포커스 관리</b>가 필요합니다. 모달은 한 번에 하나라 그 고민이 없습니다."),
    ("상태가 뒤쪽과 묶여 있다", "찾기 다이얼로그는 뒤쪽 문서를 계속 읽습니다. 다이얼로그를 띄우면서 뒤쪽을 얼려 버리면 쓸 수가 없습니다."),
    ("무시 가능 = 보장 없음", "비모달은 사용자가 그냥 지나칠 수 있습니다. <b>반드시 처리돼야 하는 일은 담지 않습니다.</b>"),
  ]),
  plat_lede="모바일은 화면이 좁아 비모달 다이얼로그가 거의 없습니다. 그래서 모바일에서 '다이얼로그'라고 하면 사실상 모달을 뜻합니다.",
  plats=plats([
    ("웹", "<code>&lt;dialog&gt;</code>",
     mini('<div class="mini__pop" style="right:5px;top:12px;width:70px"><b style="font-size:8.5px;display:block;margin-bottom:3px">찾기</b><i>결제 ▸ 4곳</i></div>', bars="684", label="웹 비모달 다이얼로그 재현"),
     "<b>다이얼로그</b> · 한 요소로 모달과 비모달을 둘 다 만듭니다. 웹에서만 이 구분이 또렷합니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-alert"><div class="ios-alert__box"><div><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p></div><div class="ios-alert__btns"><span>계속</span><span style="color:#ff453a">나가기</span></div></div></div>', "iOS 얼럿 재현"),
     "<b>얼럿</b>(Alert) · <b>모달만</b> 있습니다. 비모달에 해당하는 것은 맥의 <b>패널</b>(panel)이고, iOS 에는 사실상 없습니다."),
    ("안드로이드", "Material 3",
     phone('<div class="md-dialog"><div class="md-dialog__box"><b>저장하지 않고 나갈까요?</b><p>고친 내용이 사라집니다.</p><div class="md-dialog__btns"><span>계속</span><span class="filled">나가기</span></div></div></div>', "안드로이드 다이얼로그 재현"),
     "<b>다이얼로그</b>(Dialog) · 기본이 모달입니다. 안 막는 것은 다이얼로그가 아니라 <b>바텀시트</b>나 <b>스낵바</b>로 풉니다."),
  ]),
  plat_note="\"다이얼로그 띄워 주세요\"는 모바일에서 <b>모달</b>로 알아듣습니다. 뒤를 안 막는 것을 원한다면 그 말만으로는 전달되지 않습니다 — '뒤를 보면서 쓰는 창'이라고 역할로 말해야 합니다.",
  siblings=siblings("dialog"),
  related='''        <li><span class="na"><b>포커스 트랩</b><em>12부</em></span></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>
        <li><span class="na"><b>커맨드 팔레트</b><em>6부</em></span></li>
        <li><span class="na"><b>확인 요청의 수준</b><em>8부</em></span></li>''',
)
