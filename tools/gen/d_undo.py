# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

SAFE = table(
  ["사용자를 언제 멈춰 세우는가", "언제 되돌릴 수 있는가", "몇 번 멈춰 세우는가", "되돌릴 수 없는 일에 맞는가"],
  [["되돌리기", "<b>멈춰 세우지 않음</b>", "몇 초 안에만 가능", "0번", "맞지 않음"],
   ["되묻기", "<b>실행하기 전에</b>", "되묻는 순간에만", "<b>실행할 때마다</b>", "맞음"],
   ["이름 적어 확인", "실행하기 전에", "'아니오'를 고르면", "실행할 때마다", "<b>가장 강한 확인 방법</b>"],
   ["유예 기간", "멈춰 세우지 않음", "<b>며칠 동안</b>", "0번", "계정 삭제 같은 일에 맞음"]],
  me="되돌리기")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">'영수증을 지웠습니다'처럼 한 일을 적음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">되돌리기는 한 번만 누르면 됨</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">남은 시간은 5초 안팎</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">띠가 닫히면 되돌릴 수 없음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">role="status"를 달아 소리로도 알림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">되돌릴 수 없는 일에는 되묻기를 씀</div>
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
  desc="지운 뒤에 되돌릴 기회를 주는 방식을 다룹니다. 되묻기와는 어떻게 다른지, 되돌릴 수 있는 시간은 얼마인지, 어떤 한계가 있는지를 보여 주는 항목입니다.",
  lede="되돌리기는 지운 뒤 잠깐 띠를 띄워, 방금 한 일을 무를 기회를 주는 방식입니다. 되묻기는 사용자를 <b>지울 때마다 멈춰 세우지만</b>, 되돌리기는 멈춰 세우지 않는 대신 <b>몇 초 안에만</b> 되돌릴 수 있습니다.",
  axes_lede="되돌릴 수 없는 일을 다루는 방법들입니다. 아래 네 가지로 견줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>되묻기는 지울 때마다 <b>사용자를 멈춰 세우기</b> 때문에, 열 번 지우면 열 번 멈춥니다. 데모는 지우는 동안 몇 번 멈춰 세웠는지 셉니다.<br>
          되돌리기는 멈춰 세우지 않는 대신 <b>시간이 지나면 더는 되돌릴 수 없습니다</b>.
          띠가 닫힌 뒤에 되돌리기를 눌러 보면 데모가 <b>너무 늦은 되돌리기</b>로 셉니다.
          되돌릴 수 있는 시간은 보통 <b>5초 안팎</b>으로 잡고,
          정말 되돌릴 수 없는 일에는 되돌리기 대신 되묻기를 씁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "되돌리기, 실행 취소, 언두"),
    ("영어", "undo, undo toast, undo snackbar"),
    ("같이 쓰는 말",
     "지운 뒤 잠깐 뜨는 띠는 <b>언두 스낵바</b>(undo snackbar)라고 부릅니다. "
     "지운 것을 바로 없애지 않고 일정 기간 남겨 두는 것은 <b>소프트 삭제</b>(soft delete), "
     "그 기간은 <b>유예 기간</b>(grace period)이라고 합니다. "
     "여러 단계를 거슬러 되돌릴 수 있게 쌓아 두는 기록은 <b>되돌리기 기록</b>(undo stack)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>취소</b> — 취소는 <b>하기 전에</b> 그만두는 것이고, 되돌리기는 <b>이미 한 뒤에</b> 무르는 것입니다.<br>"
     "<b>되묻기</b> — <a href=\"destructive.html\">위험한 동작</a>의 확인은 실행하기 전에 <b>사용자를 멈춰 세우는</b> 방식이라 되돌리기와 다릅니다.<br>"
     "<b>휴지통</b> — 휴지통은 지운 것을 <b>며칠</b> 동안 남겨 두는 유예 기간이고, 되돌리기는 <b>몇 초</b> 동안만 기회를 줍니다."),
  ]),
  axes=SAFE,
  oneline="<b>되돌릴 수 있는 일이라면 미리 묻지 않습니다.</b> 실행하기 전에 되물어야 하는 것은 되돌릴 수 없는 일뿐입니다.",
  s4_title="상태", s4_hint="시간이 지나면 닫히는 되돌리기 띠",
  states=states([
    (bar("영수증을 지웠습니다", "되돌리기", "5초", "152px", "누르면 돌아옴", True),
     "띠가 뜬 직후", "<b>5초</b> 안에 되돌리기를 누를 수 있습니다"),
    (bar("영수증을 지웠습니다", "되돌리기", "1초", "152px", "곧 닫힘", None),
     "남은 시간이 끝나 갈 때", "남은 시간을 <b>보여 줍니다</b>"),
    (bar("영수증이 돌아왔습니다", "", "", "152px", "되돌림", True),
     "되돌린 뒤", "지운 것이 <b>돌아왔다고</b> 알립니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">띠가 사라짐</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">이제는 되돌릴 수 없음</span>'),
         "시간이 끝남", False, "", "152px"),
     "띠가 닫힌 뒤", "띠가 닫히면 <b>더는 되돌릴 수 없습니다</b>"),
    (bar("3개를 지웠습니다", "되돌리기", "5초", "152px", "하나로 묶어 띄움", True),
     "여러 개를 지웠을 때", "여러 개를 지워도 띠를 <b>쌓지 않고</b> 하나로 묶습니다"),
    (one(txt('<span style="display:block;font-size:8.5px">정말 지울까요?</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">취소 · 지우기</span>'),
         "되묻기", None, "되돌릴 수 없는 일에만", "152px"),
     "되묻기를 쓸 때", "지울 <b>때마다</b> 사용자를 멈춰 세웁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("무엇을 했는지", "한 줄로 적음", "'영수증을 지웠습니다'처럼 방금 한 일을 한 줄로 적습니다"),
    ("되돌리기", "한 번만 누름", "한 번 누르면 되돌아가게 하고, 두 단계로 만들지 않습니다"),
    ("남은 시간", "5초 안팎", "남은 시간을 <b>보여 주면</b> 사용자가 덜 불안해합니다"),
    ("띠가 닫히는 때", "되돌리기 끝", "띠가 닫힌 뒤에는 <b>되돌릴 방법이 없습니다</b>"),
    ("<code>role=\"status\"</code>", "소리로도 알림", "스크린 리더로 띠가 떴다는 것을 알립니다"),
    ("되묻기", "되돌릴 수 없을 때", "되돌릴 수 없는 일에만 씁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          모든 삭제에 되묻기를 붙이면 <b>사용자가 확인 창을 읽지 않게</b> 됩니다.
          매번 뜨는 창은 몇 번 겪고 나면 읽지 않고 '예'를 누르는 습관이 되어 버려서,
          정작 막아야 할 때 막지 못합니다.
          그래서 <b>되돌릴 수 있는 일은 묻지 않고</b>, 되묻기는
          정말 되돌릴 수 없는 일에만 씁니다.<br>
          키보드만 쓰는 사람에게는 <b>5초가 짧습니다</b>.
          띠가 떴다는 것을 알아채고, Tab으로 되돌리기 버튼까지 가서 누르는 데 걸리는 시간을 생각해야 합니다.
          그래서 (알림이라면) 띠로 초점을 옮기거나, 적어도 <code>role="status"</code>로
          <b>띠가 떴다는 것을 알려야</b> 합니다.</p>''',
  do=ul([
    "되돌릴 수 있는 일을 처리할 때. 미리 <b>묻지 않고</b> 되돌리기 띠를 띄웁니다",
    "되돌릴 수 있는 <b>남은 시간</b>을 보여 줄 때",
    "여러 개를 지웠을 때. 띠를 <b>하나로</b> 묶어 보여 줍니다",
  ]),
  dont=ul([
    "모든 삭제에 <b>되묻기</b>를 붙일 때. 사용자가 확인 창을 읽지 않게 됩니다",
    "되돌리기를 <b>두 단계</b>로 만들 때. 한 번 누르면 되돌아가야 합니다",
    "띠를 <b>쌓아</b> 띄울 때. 셋을 지우면 띠 셋이 떠서 화면을 덮습니다",
    "<b>스크린 리더로 알리지 않을 때</b>. 화면을 보지 못하는 사용자는 띠가 떴는지도 모릅니다",
  ]),
  instead='되돌릴 수 없는 일에는 <a href="destructive.html">위험한 동작</a>에서 다루는 되묻기를 쓰고, 띠 부품 자체는 <a href="toast.html">토스트</a> 항목에서 다룹니다. 지운 것을 며칠 동안 남겨 두려면 휴지통(소프트 삭제)을 쓰고, 보내기 전에 확인을 받아야 하면 <a href="dialog.html">다이얼로그</a>를 씁니다.',
  cases=cases([
    (bar("메일을 보냈습니다", "보내기 취소", "5초", "150px", "", True),
     "보낸 메일 되돌리기", "메일을 <b>보낸 뒤</b>에도 잠깐 동안 무를 수 있습니다"),
    (bar("1건을 보관함으로", "되돌리기", "5초", "150px", "", True),
     "보관함으로 옮긴 것 되돌리기", "보관은 다시 꺼내기 쉬운 일이라 되돌리기가 <b>가장 잘 맞습니다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">계정을 지우면 30일 뒤 삭제됩니다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">그 안에는 되살릴 수 있습니다</span>'),
         "유예 기간", True, "", "150px"),
     "계정 삭제에 유예 기간 두기", "되돌릴 수 있는 기간을 <b>며칠</b> 둡니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="띠는 <code>role=\"status\"</code>로 알리고, 되돌리기는 <b>평범한 버튼</b>으로 만듭니다.",
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
    ("<code>role=\"status\"</code>", "스크린 리더가 <b>읽던 내용을 마친 뒤</b> 띠가 떴다고 읽어 줍니다"),
    ("Tab", "Tab으로 띠의 되돌리기 버튼까지 <b>갈 수 있어야</b> 합니다"),
    ("띠로 초점을 옮길지", "띠로 초점을 <b>가져가지는 않습니다</b>. 초점을 가져가면 사용자가 하던 일이 끊깁니다"),
    ("Ctrl + Z", "글 편집기라면 되돌리기 버튼과 <b>같은 동작</b>으로 묶어 둡니다"),
    ("띠가 떠 있는 시간", "5초는 키보드 사용자에게 <b>짧습니다</b>. 시간을 멈추는 버튼을 두거나 시간을 늘립니다"),
    ("확인하는 방법", "마우스를 쓰지 않고 <b>Tab만으로</b> 되돌려 봅니다"),
  ]),
  backend=rows([
    ("바로 지우지 않고 표시만 해 두기", "처음에는 <b>지웠다는 표시만 해 두고</b> 몇 초 뒤에 실제로 지웁니다. 되돌리기 요청은 그 사이에 들어옵니다."),
    ("되돌리기 토큰 돌려주기", "지울 때 <code>undo_token</code>을 돌려주면 되돌리기 요청이 왔을 때 <b>무엇을 되살릴지</b>가 분명해집니다."),
    ("여러 개를 묶어 지웠을 때", "여러 개를 묶어서 지웠다면 <b>묶음 단위</b>로 되살려야 합니다. 하나씩 되살리면 순서가 꼬입니다."),
    ("큰 것에는 유예 기간 두기", "계정이나 프로젝트처럼 큰 것을 지울 때는 유예 기간을 <b>며칠</b> 둡니다. 그동안은 데이터를 지우지 않고 목록에서만 숨깁니다."),
  ]),
  plat_lede="세 플랫폼 가운데 <b>안드로이드가 되돌리기를 가장 적극적으로</b> 씁니다.",
  plats=plats([
    ("웹", "직접 만듦",
     bar("지웠습니다", "되돌리기", "5초", "110px", "", True),
     "토스트에 버튼을 붙여 만듭니다. <b>스크린 리더로 알리는 처리</b>를 빠뜨리기 쉽습니다."),
    ("iOS", "흔들어 취소 · 세 손가락",
     '''              <div class="phone" role="img" aria-label="iOS 되돌리기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:12px;border-radius:4px;background:var(--fg);opacity:.85"></div></div></div>''',
     "글을 편집할 때는 <b>세 손가락 쓸기</b>로 되돌릴 수 있습니다. 목록에서 지울 때는 되돌리기보다 되묻기를 더 많이 씁니다."),
    ("안드로이드", "Snackbar + UNDO",
     '''              <div class="phone" role="img" aria-label="안드로이드 스낵바 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;bottom:6px;height:11px;border-radius:3px;background:var(--fg);opacity:.9"></div>
                <div style="position:absolute;right:7px;bottom:9px;width:10px;height:4px;border-radius:2px;background:var(--accent)"></div></div></div>''',
     "Material이 <b>스낵바에 UNDO를 붙이는 방식</b>을 표준으로 정해 두었기 때문에, 목록에서 지울 때 되묻기를 거의 쓰지 않습니다."),
  ]),
  plat_note="안드로이드는 <b>'지우고 되돌리기'</b>를 표준으로 삼았기 때문에 안드로이드 앱에서는 삭제 확인 창이 드물고, 그만큼 쓰면서 덜 거슬립니다. 반대로 iOS는 되묻기를 더 많이 쓰지만, <b>흔들어 취소</b>라는 잘 알려지지 않은 기능이 있어서 글을 편집할 때는 되돌릴 수 있습니다. 웹에서는 두 방식 모두 직접 만들어야 하므로, <b>어느 쪽을 기본으로 삼을지</b>를 팀에서 한 번 정해 두면 화면마다 방식이 달라지는 일을 막을 수 있습니다.",
  siblings=siblings("undo"),
  related='''        <li><a href="toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
