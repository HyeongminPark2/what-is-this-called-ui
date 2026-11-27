# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

SAFE = table(
  ["언제 멈추나", "되돌릴 수 있나", "몇 번 멈추나", "되돌릴 수 없는 일에"],
  [["되돌리기", "<b>안 멈춘다</b>", "몇 초 안에 가능", "0번", "안 맞는다"],
   ["되묻기", "<b>하기 전에</b>", "되묻는 순간에만", "<b>할 때마다</b>", "맞는다"],
   ["이름 적어 확인", "하기 전에", "아니오를 고르면", "할 때마다", "<b>가장 센 확인</b>"],
   ["유예 기간", "안 멈춘다", "<b>며칠 동안</b>", "0번", "계정 삭제 같은 일"]],
  me="되돌리기")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">무엇을 했는지 — '영수증을 지웠습니다'</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">되돌리기 — 한 번 누르면 끝</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">남은 시간 — 5초 안팎</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">창이 닫히면 되돌릴 수 없다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">role="status" — 소리로도 알린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">되돌릴 수 없는 일에는 되묻기를 쓴다</div>
                </div>
              </div>'''

def bar(msg, act="되돌리기", left="5초", w="152px", note="", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;align-items:center;gap:6px;border-radius:6px;background:var(--fg);'
            'color:var(--surface);padding:5px 8px;font-size:8px;border:1px solid ' + c + '">'
            '<span style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + msg + '</span>'
            + ('<span style="font-weight:700;text-decoration:underline;white-space:nowrap">' + act + '</span>' if act else '')
            + ('<span style="margin-left:auto;font-family:var(--mono);opacity:.7;white-space:nowrap">' + left + '</span>' if left else '')
            + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

D = dict(
  slug="undo", ko="되돌리기", en="Undo",
  desc="지운 뒤에 되돌릴 길을 주는 방식. 되묻기와의 차이, 되돌릴 수 있는 시간, 한계.",
  lede="되묻기는 <b>할 때마다 멈춰 세웁니다</b>. 되돌리기는 안 멈추는 대신 <b>몇 초 안에만</b> 됩니다.",
  axes_lede="되돌릴 수 없는 일을 다루는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>되묻기는 <b>매번 멈춰 세웁니다</b> — 데모가 지우는 동안 몇 번 멈춰 세웠는지 셉니다.
          열 번 지우면 열 번 멈춥니다.<br>
          되돌리기는 안 멈추는 대신 <b>시간이 지나면 끝</b>입니다.
          창이 닫힌 뒤에 눌러 보면 데모가 <b>너무 늦은 되돌리기</b>를 셉니다.
          그래서 되돌릴 수 있는 시간은 <b>5초 안팎</b>이 보통이고,
          정말 되돌릴 수 없는 일에는 되묻기를 씁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "되돌리기, 실행 취소, 언두"),
    ("영어", "undo, undo toast, undo snackbar"),
    ("같이 쓰는 말",
     "지운 뒤 잠깐 뜨는 띠를 <b>언두 스낵바</b>(undo snackbar)라 부릅니다. "
     "지운 것을 바로 없애지 않고 일정 기간 두는 것을 <b>소프트 삭제</b>(soft delete), "
     "그 기간을 <b>유예 기간</b>(grace period)이라 합니다. "
     "여러 단계를 되돌리는 것은 <b>되돌리기 기록</b>(undo stack)입니다."),
    ("자주 잘못 부름",
     "<b>취소</b> — 취소는 <b>하기 전에</b> 그만두는 것입니다. 되돌리기는 <b>한 뒤에</b>입니다.<br>"
     "<b>되묻기</b> — <a href=\"destructive.html\">위험한 동작</a>의 확인은 <b>막아 세우는</b> 쪽입니다.<br>"
     "<b>휴지통</b> — 휴지통은 <b>며칠</b> 두는 유예 기간이고, 되돌리기는 <b>몇 초</b>입니다."),
  ]),
  axes=SAFE,
  oneline="<b>되돌릴 수 있으면 묻지 마세요.</b> 묻는 것이 맞는 일은 되돌릴 수 없는 일뿐입니다.",
  s4_title="상태", s4_hint="시간이 지나면 끝난다",
  states=states([
    (bar("영수증을 지웠습니다", "되돌리기", "5초", "152px", "눌리면 돌아온다", True),
     "뜬 직후", "<b>5초</b> 안에 누를 수 있다"),
    (bar("영수증을 지웠습니다", "되돌리기", "1초", "152px", "곧 닫힌다", None),
     "끝나 갈 때", "남은 시간을 <b>보여 준다</b>"),
    (bar("영수증이 돌아왔습니다", "", "", "152px", "되돌렸다", True),
     "되돌린 뒤", "<b>돌아왔다고</b> 알린다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">띠가 사라졌다</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">이제는 못 되돌린다</span>'),
         "시간이 끝남", False, "", "152px"),
     "창이 닫힘", "<b>끝</b>이다"),
    (bar("3개를 지웠습니다", "되돌리기", "5초", "152px", "묶어서 하나로", True),
     "여러 개", "띠를 <b>쌓지 않는다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">정말 지울까요?</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">취소 · 지우기</span>'),
         "되묻기", None, "되돌릴 수 없는 일에만", "152px"),
     "되묻기", "<b>할 때마다</b> 멈춘다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇을 했는지", "한 줄", "'영수증을 지웠습니다'"),
    ("되돌리기", "한 번", "두 단계로 만들지 않는다"),
    ("남은 시간", "5초 안팎", "<b>보여 주면</b> 덜 불안하다"),
    ("창이 닫힘", "끝", "그 뒤에는 <b>방법이 없다</b>"),
    ("<code>role=\"status\"</code>", "소리로", "띠가 떴다는 것을 알린다"),
    ("되묻기", "되돌릴 수 없을 때", "<b>그때만</b> 쓴다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          되묻기를 기본으로 두면 <b>사람이 그것을 안 읽게</b> 됩니다 —
          매번 뜨는 창은 몇 번 지나면 '예'를 누르는 동작이 되어 버려
          정작 막아야 할 때 못 막습니다.
          그래서 <b>되돌릴 수 있는 일은 묻지 않고</b>, 되묻기는
          정말 되돌릴 수 없는 일에 아껴 둡니다.<br>
          키보드만 쓰는 사람에게는 <b>5초가 짧습니다</b> —
          띠가 떴다는 것을 알고, Tab 으로 가서, 누르기까지의 시간입니다.
          띠에 초점을 옮기거나(알림이라면), 적어도 <code>role="status"</code> 로
          <b>떴다는 것을 알려야</b> 합니다.</p>''',
  do=ul([
    "되돌릴 수 있는 일은 <b>묻지 않기</b>",
    "<b>남은 시간</b>을 보여 주기",
    "여러 개를 지우면 띠를 <b>하나로</b> 묶기",
  ]),
  dont=ul([
    "모든 삭제에 <b>되묻기</b> 붙이기 — 읽지 않게 된다",
    "되돌리기를 <b>두 단계</b>로 만들기 — 한 번이면 된다",
    "띠를 <b>쌓기</b> — 셋을 지우면 셋이 떠 화면을 덮는다",
    "<b>소리로 안 알리기</b> — 띠가 떴는지도 모른다",
  ]),
  instead='되돌릴 수 없는 일은 <a href="destructive.html">위험한 동작</a>, 띠 부품 자체는 <a href="toast.html">토스트</a>, 며칠 두는 것은 휴지통(소프트 삭제), 보내기 전 확인은 <a href="dialog.html">다이얼로그</a>.',
  cases=cases([
    (bar("메일을 보냈습니다", "보내기 취소", "5초", "150px", "", True),
     "메일 보내기", "<b>보낸 뒤</b>에도 무를 수 있다"),
    (bar("1건을 보관함으로", "되돌리기", "5초", "150px", "", True),
     "보관", "되돌리기가 <b>가장 잘 맞는</b> 자리"),
    (one(txt('<span style="display:block;font-size:8.5px">계정을 지우면 30일 뒤 삭제됩니다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">그 안에는 되살릴 수 있습니다</span>'),
         "유예 기간", True, "", "150px"),
     "계정 삭제", "<b>며칠</b>을 둔다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 띠의 계약서",
  code_lede="띠는 <code>role=\"status\"</code> 로 알리고, 되돌리기는 <b>평범한 버튼</b>입니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"undo-bar"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;
  &lt;<span class="t">span</span>&gt;영수증_2411_01.jpg 을 지웠습니다&lt;/<span class="t">span</span>&gt;
  &lt;<span class="t">button</span>&gt;되돌리기&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"left"</span>&gt;5초&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 서버에는 바로 보내되, 되돌릴 수 있게 둔다</span>
<span class="t">const</span> id = <span class="t">await</span> api.softDelete(fileId);   <span class="c">// 표시만 지움</span>
<span class="t">const</span> t = setTimeout(() =&gt; api.purge(id), <span class="a">5000</span>);

undoBtn.onclick = <span class="t">async</span> () =&gt; {
  clearTimeout(t);
  <span class="t">await</span> api.restore(id);
  announce(<span class="s">'영수증이 돌아왔습니다'</span>);
};''',
  keys=kbd([
    ("<code>role=\"status\"</code>", "띠가 떴다고 <b>하던 말이 끝난 뒤</b> 읽어 준다"),
    ("Tab", "띠의 되돌리기로 <b>갈 수 있어야</b> 한다"),
    ("초점 옮기기", "띠로 초점을 <b>뺏지는 않는다</b> — 하던 일이 끊긴다"),
    ("Ctrl + Z", "글 편집기라면 <b>같이</b> 묶어 둔다"),
    ("시간", "5초는 키보드 사용자에게 <b>짧다</b> — 멈춤 단추를 두거나 늘린다"),
    ("확인하는 법", "마우스를 안 쓰고 <b>Tab 만으로</b> 되돌려 본다"),
  ]),
  backend=rows([
    ("바로 지우지 않는다", "<b>표시만 지우고</b> 몇 초 뒤에 정말 지웁니다 — 그 사이에 되돌리기가 옵니다."),
    ("되돌리기 열쇠", "지울 때 <code>undo_token</code> 을 돌려주면 <b>무엇을 되살릴지</b>가 분명해집니다."),
    ("여러 개", "묶어서 지웠으면 <b>묶음 단위</b>로 되살려야 합니다 — 하나씩이면 순서가 꼬입니다."),
    ("유예 기간", "계정·프로젝트처럼 큰 것은 <b>며칠</b>을 둡니다. 그동안은 목록에서만 숨깁니다."),
  ]),
  plat_lede="<b>안드로이드가 이 방식을 가장 적극적으로</b> 씁니다.",
  plats=plats([
    ("웹", "직접 만듦",
     bar("지웠습니다", "되돌리기", "5초", "110px", "", True),
     "토스트에 단추를 붙여 만듭니다. <b>소리로 알리는 것</b>을 빠뜨리기 쉽습니다."),
    ("iOS", "흔들어 취소 · 세 손가락",
     '''              <div class="phone" role="img" aria-label="iOS 되돌리기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:12px;border-radius:4px;background:var(--fg);opacity:.85"></div></div></div>''',
     "글 편집에는 <b>세 손가락 쓸기</b>가 있습니다. 목록 삭제에는 되묻기를 더 씁니다."),
    ("안드로이드", "Snackbar + UNDO",
     '''              <div class="phone" role="img" aria-label="안드로이드 스낵바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;bottom:6px;height:11px;border-radius:3px;background:var(--fg);opacity:.9"></div>
                <div style="position:absolute;right:7px;bottom:9px;width:10px;height:4px;border-radius:2px;background:var(--accent)"></div></div></div>''',
     "Material 이 <b>스낵바 + UNDO</b> 를 표준으로 못박아, 목록에서 되묻기를 거의 안 씁니다."),
  ]),
  plat_note="안드로이드가 <b>'지우고 되돌리기'</b>를 표준으로 삼은 덕에 그쪽 앱에서는 삭제 확인 창이 드뭅니다 — 쓰다 보면 훨씬 덜 거슬립니다. iOS 는 반대로 되묻기를 더 쓰는데, <b>흔들어 취소</b>라는 숨은 기능이 있어 글 편집에서는 되돌리기가 됩니다. 웹에서는 둘 다 직접 만들어야 하니 <b>어느 쪽을 기본으로 삼을지</b>를 팀에서 한 번 정해 두면 화면마다 다르게 되는 일이 없습니다.",
  siblings=siblings("undo"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
