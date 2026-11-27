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
  desc="되돌릴 수 없는 일을 다루는 법. 네 가지 확인 방식과, 묻는 것보다 무를 수 있게 하는 쪽.",
  lede="되돌릴 수 없는 일. <b>묻는 것보다 무를 수 있게 하는 쪽</b>이 거의 늘 낫습니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>네 가지 방식을 바꿔 가며 <b>삭제</b>를 눌러 보세요.<br>
          <b>바로 지운다</b>는 손가락이 미끄러지면 끝이고, <b>한 번 되묻는다</b>는 세 번째부터
          읽지 않고 누릅니다. <b>이름을 치게 한다</b>는 확실하지만 번거롭습니다.<br>
          <b>되돌릴 틈을 주는</b> 쪽이 대개 가장 낫습니다 — 묻지 않아 빠르고, 실수해도 살아납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "위험한 동작, 파괴적 동작, 삭제 확인"),
    ("영어", "destructive action, confirmation dialog, type-to-confirm"),
    ("같이 쓰는 말",
     "되묻는 창이 <b>확인 다이얼로그</b>, 이름을 그대로 치게 하는 것이 "
     "<b>타이프 투 컨펌</b>(type-to-confirm)입니다. "
     "지운 것을 잠시 두는 곳이 <b>휴지통</b>·<b>소프트 삭제</b>(soft delete), "
     "되돌릴 틈을 주는 줄이 <b>언두 스낵바</b>입니다. "
     "설정 맨 아래 모아 두는 자리는 <b>위험 구역</b>(danger zone)입니다."),
    ("자주 잘못 부름",
     "<b>경고</b> — 경고는 <b>알리는</b> 것이고, 이건 <b>막는</b> 장치입니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 띄우는 방식이고, 확인은 <b>그 안에 담는 내용</b>입니다.<br>"
     "<b>되돌리기</b> — 되돌리기는 확인의 <b>반대말이 아니라 대안</b>입니다. 둘 다 쓰면 과합니다."),
  ]),
  axes=ax("위험한 동작"),
  oneline="<b>물어볼지 무르게 할지 하나만 고르세요.</b> 둘 다 하면 번거롭고, 둘 다 안 하면 사고가 납니다.",
  s4_title="확인 방식 넷", s4_hint="무엇을 막고 무엇을 치르나",
  states=states([
    (box('<span style="font-size:9px">모란상회</span>' + DEL, "152px", "누르면 바로 지워진다", True),
     "바로 지운다", "빠르지만 <b>미끄러지면 끝</b>이다"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">‘모란상회’를 지울까요?</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">정산 내역 128건이 함께 지워집니다</span>' + two('취소', '삭제'),
         "152px", "가장 흔하다", False, "var(--danger)"),
     "한 번 되묻는다", "<b>세 번째부터는</b> 읽지 않고 누른다"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">이름을 그대로 쳐 주세요</span>'
         '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:8.5px;color:var(--fg-muted)">모란상회</div>'
         + two('취소', '삭제'), "152px", "확실하지만 번거롭다", False, "var(--danger)"),
     "이름을 치게 한다", "<b>정말 위험한 것</b>에만 쓴다"),
    (box('<span style="display:flex;align-items:center;gap:6px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px 7px;font-size:8.5px">'
         '<span style="flex:1">‘모란상회’ 을(를) 지웠습니다</span><span style="color:#9ec1ff;font-weight:700">되돌리기</span></span>',
         "152px", "묻지 않고 지운 뒤 5초"),
     "되돌릴 틈을 준다 ✓", "<b>빠르고 안전하다.</b> 대개 이쪽이 낫다"),
    (box('<span style="font-size:9px;color:var(--fg-muted)">휴지통 · 30일 뒤 완전 삭제</span>'
         '<span style="font-size:8px;color:var(--accent)">복구하기</span>', "152px", "소프트 삭제"),
     "휴지통", "큰 것·많은 것에. <b>저장소를 더 쓴다</b>"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">계정 삭제</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">메일로 보낸 링크를 눌러야 끝납니다</span>', "152px", "한 단계 더"),
     "되돌릴 수 없는 것", "<b>다른 통로</b>를 하나 더 거치게 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇이 사라지나", "숫자로", "'정산 내역 <b>128건</b>이 함께'. 막연하면 안 읽는다"),
    ("되돌릴 수 있나", "그대로 적는다", "있으면 쓰고, 없으면 <b>없다고</b> 쓴다"),
    ("버튼 두 개", "취소 · 삭제", "취소가 <b>기본</b>이고 약하게"),
    ("버튼 이름", "동사로", "'확인'이 아니라 <b>'삭제'</b>. 무엇을 하는지 적는다"),
    ("되돌리기", "묻기의 대안", "있으면 <b>안 물어도 된다.</b> 둘 다는 과하다"),
    ("길들여짐", "세 번째부터", "되물을수록 <b>안 읽고 누른다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          확인 창은 <b>쓸수록 약해집니다.</b>
          세 번쯤 보고 나면 문구를 읽지 않고 오른쪽 버튼을 누르는 손버릇이 생기고,
          그때부터는 창이 있어도 사고가 납니다.
          그래서 되돌릴 수 있는 일에는 <b>묻지 말고 되돌리기를</b> 주고,
          확인 창은 <b>정말 되돌릴 수 없는 것</b>에만 남겨 두는 쪽이 좋습니다 —
          드물게 뜨는 창이라야 읽힙니다.</p>''',
  do=ul([
    "되돌릴 수 있는 일 → <b>묻지 말고 되돌리기</b>",
    "되돌릴 수 없는 일 → <b>한 번 묻기</b>",
    "큰 것을 지울 때 → <b>이름 치기</b>나 메일 한 단계 더",
  ]),
  dont=ul([
    "모든 것에 확인 창 — <b>안 읽고 누르게</b> 된다",
    "'확인 / 취소' — <b>무엇을 확인하는지</b> 모른다",
    "삭제를 <b>기본 버튼</b>으로 — 엔터로 지워진다",
    "되돌리기와 확인 창을 <b>둘 다</b> — 번거롭기만 하다",
  ]),
  instead='알리기만 하면 <a href="../items/error.html">오류 메시지</a>, 결과와 되돌리기는 <a href="../items/toast.html">토스트</a>, 여러 건이면 <a href="bulk.html">일괄 선택</a>의 범위 확인.',
  cases=cases([
    (box('<span style="display:flex;align-items:center;gap:6px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px 7px;font-size:8.5px">'
         '<span style="flex:1">1건 삭제됨</span><span style="color:#9ec1ff;font-weight:700">되돌리기</span></span>', "150px"),
     "되돌리기 줄", "<b>지메일이 널리 퍼뜨린</b> 방식"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">128건을 반려할까요?</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">되돌릴 수 없습니다</span>' + two('취소', '반려'), "150px", "", False, "var(--danger)"),
     "큰 범위", "<b>건수를 문장 안에</b> 적는다 — <a href=\"bulk.html\">일괄 선택</a>"),
    (box('<span style="font-size:9px;font-weight:700;color:var(--danger)">위험 구역</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">계정 삭제 · 조직 나가기</span>', "150px", "", False, "var(--danger)"),
     "위험 구역", "<a href=\"settings.html\">설정</a> 맨 아래 따로 가둔다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 확인의 계약서",
  code_lede="<code>&lt;dialog&gt;</code>를 쓰고 <b>취소를 기본</b>으로 둡니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"confirm"</span> <span class="a">aria-labelledby</span>=<span class="s">"t"</span> <span class="a">aria-describedby</span>=<span class="s">"d"</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"t"</span>&gt;‘모란상회’를 지울까요?&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"d"</span>&gt;정산 내역 128건이 함께 지워집니다. 되돌릴 수 없습니다.&lt;/<span class="t">p</span>&gt;

  &lt;<span class="t">form</span> <span class="a">method</span>=<span class="s">"dialog"</span>&gt;
    &lt;<span class="t">button</span> <span class="a">value</span>=<span class="s">"cancel"</span> <span class="a">autofocus</span>&gt;취소&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">button</span> <span class="a">value</span>=<span class="s">"delete"</span> <span class="a">class</span>=<span class="s">"danger"</span>&gt;삭제&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">form</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 되돌릴 수 있으면 묻지 말고 — 5초 뒤에 진짜로 보낸다</span>
<span class="k">function</span> removeWithUndo(id) {
  hideFromList(id);
  <span class="k">const</span> t = setTimeout(() =&gt; api.remove(id), <span class="a">5000</span>);
  showUndoBar(() =&gt; { clearTimeout(t); restore(id); });
}''',
  keys=kbd([
    ("<code>autofocus</code>는 <b>취소</b>에", "열리자마자 엔터를 쳐도 <b>안 지워진다</b>"),
    ("<kbd>Esc</kbd> = 취소", "<code>&lt;dialog&gt;</code>가 공짜로 준다. 위험한 쪽이 기본이면 안 된다"),
    ("<code>aria-describedby</code>", "무엇이 사라지는지까지 읽히게 한다. 제목만 읽히면 모른다"),
    ("버튼 이름은 동사", "'확인'은 <b>무엇을 확인하는지</b> 안 알려 준다"),
    ("되돌리기 줄은 <code>role=\"status\"</code>", "<a href=\"../items/toast.html\">토스트</a>와 같다. 초점을 뺏지 않는다"),
    ("되돌리기에 닿을 시간", "5초는 키보드·스크린 리더 사용자에게 짧다. <b>머무르면 멈추게</b> 한다"),
  ]),
  backend=rows([
    ("되돌리기는 <b>안 보내는</b> 것으로", "화면에서 지우고 5초 뒤에 보내면 되돌리기는 <b>타이머 취소</b>뿐입니다. 가장 간단합니다."),
    ("소프트 삭제", "바로 못 미루면 <code>deleted_at</code>을 찍어 두고 나중에 비웁니다. 대신 <b>모든 질의가 그 칸을 봐야</b> 합니다."),
    ("딸린 것들", "가맹점을 지우면 정산·사용자가 같이 지워집니다. <b>무엇이 딸려 가는지</b>를 화면 문구에도 적습니다."),
    ("권한을 다시 본다", "삭제는 <b>서버가 다시 확인</b>합니다. 버튼을 숨긴 것은 방어가 아닙니다."),
    ("기록을 남긴다", "누가 언제 무엇을 지웠는지 남겨 두면 <b>복구 요청</b>에 답할 수 있습니다."),
    ("되돌릴 수 없는 것", "계정·조직 삭제는 <b>유예 기간</b>(30일)을 두는 쪽이 민원이 적습니다."),
  ]),
  plat_lede="<b>버튼 차례와 색</b>이 갈립니다 — <a href=\"platformdiff.html\">HIG와 Material</a> 참고.",
  plats=plats([
    ("웹", "&lt;dialog&gt;",
     box('<span style="font-size:8.5px;font-weight:700">지울까요?</span>' + two('취소', '삭제'), "112px", "", False, "var(--danger)"),
     "오른쪽 아래, <b>확인이 바깥쪽</b>. 위험한 것은 빨갛게 칠합니다."),
    ("iOS", "Alert · Action Sheet",
     '''              <div class="phone" role="img" aria-label="iOS 확인 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:7px;right:7px;top:28px;background:var(--surface);border-radius:6px;border:1px solid var(--line)">
                  <div style="padding:4px;text-align:center;font-size:5px">지울까요?</div>
                  <div style="display:flex;border-top:1px solid var(--line);font-size:5px"><span style="flex:1;text-align:center;padding:2px;border-right:1px solid var(--line);color:var(--accent)">취소</span><span style="flex:1;text-align:center;padding:2px;color:var(--danger);font-weight:700">삭제</span></div></div></div></div>''',
     "<b>반반으로 나누고</b> 위험한 쪽을 빨갛게. 목록에서는 <b>쓸어넘기기</b>로도 지웁니다."),
    ("안드로이드", "Dialog · 스낵바",
     '''              <div class="phone" role="img" aria-label="안드로이드 되돌리기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:8px;background:var(--ink-900);color:#fff;border-radius:4px;padding:3px;font-size:5px;display:flex"><span style="flex:1">1건 삭제됨</span><span style="color:#9ec1ff">실행취소</span></div></div></div>''',
     "<b>스낵바 + 실행취소</b>가 규격에 있습니다. 묻기보다 무르게 하는 쪽을 권합니다."),
  ]),
  plat_note="\"삭제할 때 한 번 물어봐 주세요\"는 가장 쉬운 답이지만 가장 약한 답이기도 합니다. <b>되돌릴 수 있는지</b>를 먼저 물어보고, 되돌릴 수 있으면 묻지 말고 되돌리기를 주는 쪽으로 바꾸면 화면도 빨라지고 사고도 줍니다. 되돌리기는 <b>나중에 붙이기 가장 어려운</b> 기능이라, 처음에 정해 두는 값이 큽니다.",
  siblings=siblings("destructive"),
  related='''        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="settings.html"><b>설정 화면</b><em>13부</em></a></li>''',
)
