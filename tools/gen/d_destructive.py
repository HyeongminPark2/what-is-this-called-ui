# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(inner, w="152px", note="", warn=False, border="var(--line)"):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + border + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">'
            + inner + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

DEL = '<span style="justify-self:start;border:1px solid var(--danger);color:var(--danger);border-radius:4px;padding:2px 8px;font-size:8.5px">삭제</span>'

def two(a, b):
    return ('<div style="display:flex;gap:5px"><span style="border:1px solid var(--line);border-radius:4px;padding:2px 8px;font-size:8.5px">' + a + '</span>'
            '<span style="background:var(--danger);color:#fff;border-radius:4px;padding:2px 8px;font-size:8.5px">' + b + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">무엇이 사라지는지 — ‘정산 내역 128건이 함께’</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">되돌릴 수 있는지 — 있으면 그렇게 적는다</div>
                  <div class="pin-out" data-pin="3" style="max-width:220px">''' + two('취소', '삭제').strip() + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">버튼 이름은 동사로 — ‘확인’이 아니라 ‘삭제’</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">되돌리기가 있으면 묻지 않아도 된다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">세 번째부터는 읽지 않고 누른다</div>
                </div>
              </div>'''

D = dict(
  slug="destructive", ko="위험한 동작", en="Destructive action",
  desc="되돌릴 수 없는 일을 다루는 법입니다. 네 가지 확인 방식을 비교하고, 되묻는 것보다 나중에 무를 수 있게 하는 편이 나은 이유를 설명합니다.",
  lede="삭제처럼 되돌리기 어려운 일을 할 때는, 누르기 전에 되묻는 것보다 <b>누른 뒤에 무를 수 있게 하는 편</b>이 거의 언제나 낫습니다.",
  axes_lede="화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 가지 방식을 바꿔 가며 <b>삭제</b>를 눌러 보세요.<br>
          <b>바로 지운다</b>는 손가락이 잘못 닿기만 해도 되돌릴 수 없고, <b>한 번 되묻는다</b>는 세 번째쯤부터
          사용자가 문구를 읽지 않고 누릅니다. <b>이름을 치게 한다</b>는 확실하지만 번거롭습니다.<br>
          대개는 <b>되돌릴 틈을 주는</b> 방식이 가장 낫습니다. 묻지 않으니 빠르고, 실수로 지워도 되살릴 수 있기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "위험한 동작, 파괴적 동작, 삭제 확인"),
    ("영어", "destructive action, confirmation dialog, type-to-confirm"),
    ("같이 쓰는 말",
     "되묻는 창을 <b>확인 다이얼로그</b>라 하고, 지울 대상의 이름을 그대로 치게 하는 방식을 "
     "<b>타이프 투 컨펌</b>(type-to-confirm)이라고 합니다. "
     "지운 것을 바로 없애지 않고 잠시 두는 곳은 <b>휴지통</b>·<b>소프트 삭제</b>(soft delete)라 하고, "
     "지운 뒤 되돌릴 틈을 주는 줄은 <b>언두 스낵바</b>라고 부릅니다. "
     "위험한 동작을 설정 맨 아래에 모아 두는 자리는 <b>위험 구역</b>(danger zone)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>경고</b> — 경고는 상황을 <b>알리는</b> 것이고, 위험한 동작의 확인은 실수를 <b>막는</b> 장치입니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 화면에 띄우는 방식이고, 확인은 <b>그 안에 담는 내용</b>입니다.<br>"
     "<b>되돌리기</b> — 되돌리기는 확인의 <b>반대말이 아니라 대안</b>입니다. 그래서 둘을 함께 쓰면 지나칩니다."),
  ]),
  axes=ax("위험한 동작"),
  oneline="<b>되물을지, 나중에 무르게 할지 하나만 고르세요.</b> 둘 다 하면 번거롭기만 하고, 둘 다 하지 않으면 사고가 납니다.",
  s4_title="확인 방식 넷", s4_hint="무엇을 막고 무엇을 치르나",
  states=states([
    (box('<span style="font-size:9px">모란상회</span>' + DEL, "152px", "누르면 바로 지워진다", True),
     "바로 지운다", "빠르지만 <b>잘못 누르면 되돌릴 수 없습니다</b>"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">‘모란상회’를 지울까요?</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">정산 내역 128건이 함께 지워집니다</span>' + two('취소', '삭제'),
         "152px", "가장 흔하다", False, "var(--danger)"),
     "한 번 되묻는다", "<b>세 번째쯤부터는</b> 문구를 읽지 않고 누릅니다"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">이름을 그대로 쳐 주세요</span>'
         '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:8.5px;color:var(--fg-muted)">모란상회</div>'
         + two('취소', '삭제'), "152px", "확실하지만 번거롭다", False, "var(--danger)"),
     "이름을 치게 한다", "번거로우므로 <b>정말 위험한 것</b>에만 씁니다"),
    (box('<span style="display:flex;align-items:center;gap:6px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px 7px;font-size:8.5px">'
         '<span style="flex:1">‘모란상회’ 을(를) 지웠습니다</span><span style="color:#9ec1ff;font-weight:700">되돌리기</span></span>',
         "152px", "묻지 않고 지운 뒤 5초"),
     "되돌릴 틈을 준다 ✓", "묻지 않아 <b>빠르면서도 안전해서</b> 대개 이 방식이 낫습니다"),
    (box('<span style="font-size:9px;color:var(--fg-muted)">휴지통 · 30일 뒤 완전 삭제</span>'
         '<span style="font-size:8px;color:var(--accent)">복구하기</span>', "152px", "소프트 삭제"),
     "휴지통", "크거나 많은 것을 지울 때 씁니다. 지운 것을 보관하므로 <b>저장 공간을 더 씁니다</b>"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">계정 삭제</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">메일로 보낸 링크를 눌러야 끝납니다</span>', "152px", "한 단계 더"),
     "되돌릴 수 없는 것", "메일 링크처럼 <b>다른 통로</b>를 한 번 더 거치게 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이 사라지나", "숫자로", "'정산 내역 <b>128건</b>이 함께'처럼 숫자로 적습니다. 막연하게 적으면 사용자가 읽지 않습니다"),
    ("되돌릴 수 있나", "그대로 적는다", "되돌릴 수 있으면 그렇다고 적고, 없으면 <b>없다고</b> 적습니다"),
    ("버튼 두 개", "취소 · 삭제", "취소를 <b>기본</b> 버튼으로 두되, 눈에 덜 띄게 만듭니다"),
    ("버튼 이름", "동사로", "'확인'이 아니라 <b>'삭제'</b>처럼 버튼을 누르면 무엇을 하는지 적습니다"),
    ("되돌리기", "묻기의 대안", "되돌리기가 있으면 <b>묻지 않아도 됩니다.</b> 둘을 함께 쓰면 지나칩니다"),
    ("길들여짐", "세 번째부터", "확인 창을 자주 볼수록 사용자는 <b>읽지 않고 누릅니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          확인 창은 <b>자주 띄울수록 효과가 떨어집니다.</b>
          세 번쯤 보고 나면 문구를 읽지 않고 오른쪽 버튼을 누르는 손버릇이 생기고,
          그때부터는 확인 창이 있어도 사고가 납니다.
          그래서 되돌릴 수 있는 일에는 <b>묻지 말고 되돌리기를</b> 주고,
          확인 창은 <b>정말 되돌릴 수 없는 것</b>에만 남겨 두는 편이 좋습니다.
          드물게 뜨는 창이어야 사용자가 문구를 읽기 때문입니다.</p>''',
  do=ul([
    "되돌릴 수 있는 일일 때. <b>묻지 말고 되돌리기</b>를 줍니다",
    "되돌릴 수 없는 일일 때. <b>한 번 묻습니다</b>",
    "큰 것을 지울 때. <b>이름 치기</b>나 메일 확인을 한 단계 더 둡니다",
  ]),
  dont=ul([
    "모든 동작에 확인 창을 띄울 때. 사용자가 <b>읽지 않고 누르게</b> 됩니다",
    "버튼을 '확인 / 취소'로 적을 때. <b>무엇을 확인하는지</b> 알 수 없습니다",
    "삭제를 <b>기본 버튼</b>으로 둘 때. 엔터만 눌러도 지워집니다",
    "되돌리기와 확인 창을 <b>둘 다</b> 쓸 때. 번거롭기만 합니다",
  ]),
  instead='알리기만 하면 <a href="../items/error.html">오류 메시지</a>, 결과와 되돌리기는 <a href="../items/toast.html">토스트</a>, 여러 건이면 <a href="bulk.html">일괄 선택</a>의 범위 확인.',
  cases=cases([
    (box('<span style="display:flex;align-items:center;gap:6px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px 7px;font-size:8.5px">'
         '<span style="flex:1">1건 삭제됨</span><span style="color:#9ec1ff;font-weight:700">되돌리기</span></span>', "150px"),
     "되돌리기 줄", "<b>지메일이 널리 퍼뜨린</b> 방식입니다"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">128건을 반려할까요?</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">되돌릴 수 없습니다</span>' + two('취소', '반려'), "150px", "", False, "var(--danger)"),
     "큰 범위", "<b>건수를 문장 안에</b> 적습니다(<a href=\"bulk.html\">일괄 선택</a> 참고)"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">위험 구역</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">계정 삭제 · 조직 나가기</span>', "150px", "", False, "var(--danger)"),
     "위험 구역", "<a href=\"settings.html\">설정</a> 맨 아래에 따로 모아 둡니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="확인 창은 <code>&lt;dialog&gt;</code>로 만들고 <b>취소를 기본</b> 버튼으로 둡니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"confirm"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span> <span class="a">aria-describedby</span>=<span class="s">"d"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;‘모란상회’를 지울까요?&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"d"</span>&gt;정산 내역 128건이 함께 지워집니다. 되돌릴 수 없습니다.&lt;/<span class="t">p</span>&gt;

  &lt;<span class="t">form</span> <span class="a">method</span>=<span class="s">"dialog"</span>&gt;
    &lt;<span class="t">button</span> <span class="a">value</span>=<span class="s">"cancel"</span> <span class="a">autofocus</span>&gt;취소&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">button</span> <span class="a">value</span>=<span class="s">"delete"</span> <span class="a">class</span>=<span class="s">"danger"</span>&gt;삭제&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">form</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 되돌릴 수 있으면 묻지 말고, 5초 뒤에 진짜로 보낸다</span>
<span class="k">function</span> removeWithUndo(id) {
  hideFromList(id);
  <span class="k">const</span> t = setTimeout(() =&gt; api.remove(id), <span class="a">5000</span>);
  showUndoBar(() =&gt; { clearTimeout(t); restore(id); });
}''',
  keys=kbd([
    ("<code>autofocus</code>는 <b>취소</b>에", "창이 열리자마자 엔터를 쳐도 <b>지워지지 않습니다</b>"),
    ("<kbd>Esc</kbd> = 취소", "<code>&lt;dialog&gt;</code>는 이 동작을 기본으로 제공합니다. 위험한 쪽이 기본 동작이 되면 안 됩니다"),
    ("<code>aria-describedby</code>", "무엇이 사라지는지까지 읽히게 합니다. 제목만 읽히면 무엇이 함께 지워지는지 알 수 없습니다"),
    ("버튼 이름은 동사", "'확인'이라고만 적으면 <b>무엇을 확인하는지</b> 알 수 없습니다"),
    ("되돌리기 줄은 <code>role=\"status\"</code>", "<a href=\"../items/toast.html\">토스트</a>와 같은 방식으로, 초점을 가져가지 않고 알립니다"),
    ("되돌리기에 닿을 시간", "5초는 키보드·스크린 리더 사용자에게 짧습니다. 그래서 초점이나 마우스가 <b>머무르는 동안에는 시간이 멈추게</b> 합니다"),
  ]),
  backend=rows([
    ("되돌리기는 <b>안 보내는</b> 것으로", "화면에서 먼저 지우고 5초 뒤에 서버로 보내면, 되돌리기는 <b>타이머를 취소</b>하는 것만으로 끝납니다. 구현 방법 가운데 가장 간단합니다."),
    ("소프트 삭제", "삭제 요청을 미룰 수 없다면 <code>deleted_at</code>에 시각을 기록해 두고 나중에 실제로 지웁니다. 대신 <b>모든 질의가 그 칸을 확인해야</b> 합니다."),
    ("딸린 것들", "가맹점을 지우면 거기에 딸린 정산과 사용자도 같이 지워집니다. 그래서 <b>무엇이 함께 지워지는지</b> 화면 문구에도 적습니다."),
    ("권한을 다시 본다", "삭제 권한은 <b>서버에서 다시 확인</b>합니다. 화면에서 버튼을 숨기는 것만으로는 요청을 직접 보내는 사람을 막을 수 없습니다."),
    ("기록을 남긴다", "누가 언제 무엇을 지웠는지 기록해 두면 나중에 들어오는 <b>복구 요청</b>에 답할 수 있습니다."),
    ("되돌릴 수 없는 것", "계정이나 조직을 지울 때는 <b>유예 기간</b>(30일)을 두는 편이 민원이 적습니다."),
  ]),
  plat_lede="플랫폼마다 확인 창의 <b>버튼 순서와 색</b>이 다릅니다. 자세한 차이는 <a href=\"platformdiff.html\">HIG와 Material</a>에서 다룹니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt;",
     box('<span style="font-size:8.5px;font-weight:700">지울까요?</span>' + two('취소', '삭제'), "112px", "", False, "var(--danger)"),
     "버튼을 오른쪽 아래에 두고 <b>확인 버튼을 바깥쪽</b>에 놓습니다. 위험한 동작의 버튼은 빨간색으로 칠합니다."),
    ("iOS", "Alert · Action Sheet",
     '''              <div class="phone" role="img" aria-label="iOS 확인 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:7px;right:7px;top:28px;background:var(--surface);border-radius:6px;border:1px solid var(--line)">
                  <div style="padding:4px;text-align:center;font-size:5px">지울까요?</div>
                  <div style="display:flex;border-top:1px solid var(--line);font-size:5px"><span style="flex:1;text-align:center;padding:2px;border-right:1px solid var(--line);color:var(--accent)">취소</span><span style="flex:1;text-align:center;padding:2px;color:var(--danger);font-weight:700">삭제</span></div></div></div></div>''',
     "버튼 자리를 <b>반반으로 나누고</b> 위험한 쪽을 빨간색으로 표시합니다. 목록에서는 <b>쓸어넘기기</b>로도 지울 수 있습니다."),
    ("안드로이드", "Dialog · 스낵바",
     '''              <div class="phone" role="img" aria-label="안드로이드 되돌리기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--ink-900);color:#fff;border-radius:4px;padding:3px;font-size:5px;display:flex"><span style="flex:1">1건 삭제됨</span><span style="color:#9ec1ff">실행취소</span></div></div></div>''',
     "<b>스낵바와 실행취소</b> 조합이 규격에 들어 있고, 되묻기보다 나중에 무르게 하는 방식을 권합니다."),
  ]),
  plat_note="\"삭제할 때 한 번 물어봐 주세요\"는 가장 쉬운 해결책이지만 효과는 가장 약합니다. 그런 요청을 받으면 그 삭제를 <b>되돌릴 수 있는지</b>부터 따져 보고, 되돌릴 수 있다면 묻지 말고 되돌리기를 주는 쪽으로 바꾸세요. 그러면 화면도 빨라지고 사고도 줄어듭니다. 되돌리기는 <b>나중에 붙이기 가장 어려운</b> 기능이라서, 처음 설계할 때 정해 두는 편이 훨씬 수월합니다.",
  siblings=siblings("destructive"),
  related='''        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="settings.html"><b>설정 화면</b><em>13부</em></a></li>''',
)
