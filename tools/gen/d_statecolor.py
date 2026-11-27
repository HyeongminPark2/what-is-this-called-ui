# -*- coding: utf-8 -*-
from ax2 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def alert(c, mark, text, label, note="", ok=None, cues=True):
    return ('              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">'
            '<span style="display:flex;align-items:center;gap:5px;width:124px;border-radius:6px;'
            'padding:5px 7px;background:color-mix(in srgb, ' + c + ' 12%, var(--surface));'
            'border:1px solid color-mix(in srgb, ' + c + ' 40%, transparent)">'
            + ('<span style="display:grid;place-items:center;width:13px;height:13px;border-radius:999px;'
               'background:' + c + ';color:#fff;font-size:8px;line-height:1;flex:none">' + mark + '</span>'
               if cues else
               '<span style="display:block;width:11px;height:11px;border-radius:999px;background:' + c + ';flex:none"></span>')
            + '<span style="font-size:9px;color:var(--fg)">' + text + '</span></span>'
            '<span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--color-success<span style="color:var(--fg-faint)"> ← 끝났다 · 맞다</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">--color-warning<span style="color:var(--fg-faint)"> ← 되지만 봐 달라</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">--color-danger<span style="color:var(--fg-faint)"> ← 안 됐다 · 지운다</span></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">--color-info<span style="color:var(--fg-faint)"> ← 그냥 알린다</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">각각 <b>바탕 · 글 · 테두리</b> 세 자리</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">색만으로는 <b>못 가르는 사람</b>이 있다</div>
                </div>
              </div>'''

D = dict(
  slug="statecolor", ko="상태 색", en="Semantic status colors",
  desc="성공·주의·오류·정보 네 색을 토큰으로 두는 법과, 색만으로는 못 가르는 사람이 있다는 사실.",
  lede="상태 색은 <b>네 가지면 충분</b>합니다. 그리고 색은 <b>혼자 두면 안 되는</b> 단서입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색만으로 상태를 가르면 <b>적록 색각인 분에게는 성공과 오류가 같은 색</b>이 됩니다 —
          데모가 두 색의 거리를 재서 적습니다. 흉내 변환은 <b>어림한 값</b>이라
          실제로 그렇게 보인다는 뜻은 아니고, '충분히 가까워 못 가른다'를 숫자로 보이려는 것입니다.<br>
          고치는 법은 <b>색을 바꾸는 게 아니라 단서를 더하는 것</b>입니다 —
          모양(✓ · !)과 말('승인됨')을 붙이면 색을 못 봐도 읽힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "상태 색, 시맨틱 컬러, 의미 색"),
    ("영어", "semantic colors, status colors, feedback colors"),
    ("같이 쓰는 말",
     "성공 · 주의 · 오류 · 정보 넷을 묶어 <b>피드백 색</b>이라 부르기도 합니다. "
     "각 색은 보통 <b>바탕 · 글 · 테두리</b> 세 자리로 나눠 둡니다 — "
     "<code>--color-danger-bg</code> · <code>-fg</code> · <code>-border</code>. "
     "색 하나를 세 군데에 그대로 쓰면 <b>대비비가 안 맞습니다</b>."),
    ("자주 잘못 부름",
     "<b>브랜드 색</b> — <a href=\"color.html\">색 토큰</a>의 주된 색은 <b>누구인가</b>를, 상태 색은 <b>무슨 일이 생겼는가</b>를 말합니다.<br>"
     "<b>빨강 = 삭제</b> — 빨강은 <b>되돌릴 수 없음</b>이지 삭제 전용이 아닙니다.<br>"
     "<b>초록 = 켜짐</b> — <a href=\"switch.html\">스위치</a>의 켜짐은 보통 <b>주된 색</b>을 씁니다."),
  ]),
  axes=ax("상태 색"),
  oneline="<b>색은 두 번째 단서여야 합니다.</b> 모양이나 말이 먼저 있고, 색이 그걸 거듭 말해 줍니다.",
  s4_title="네 색", s4_hint="무슨 일이 생겼는지를 말한다",
  states=states([
    (alert("#1a7f37", "✓", "정산이 들어왔습니다", "success", "끝났다 · 맞다", True), "성공", "<b>할 일이 없다</b>"),
    (alert("#9a6700", "!", "정산이 하루 밀렸습니다", "warning", "되지만 봐 달라"), "주의", "막지는 않는다"),
    (alert("#cf222e", "✕", "계좌가 맞지 않습니다", "danger", "안 됐다 · 지운다"), "오류", "<b>고쳐야</b> 넘어간다"),
    (alert("#0969da", "i", "다음 정산은 금요일", "info", "그냥 알린다"), "정보", "상태가 아니라 안내"),
    (alert("#1a7f37", "", "정산이 들어왔습니다", "색만", "단서가 하나뿐", False, False),
     "색만", "<b>색을 못 보면</b> 끝이다"),
    (alert("#8a8f99", "·", "불러오는 중입니다", "neutral", "아직 모른다"), "중립", "결과가 <b>아직</b> 없다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("성공", "끝났다", "할 일이 <b>없다</b>는 뜻"),
    ("주의", "봐 달라", "막지는 <b>않는다</b>"),
    ("오류", "안 됐다", "<b>고쳐야</b> 넘어간다"),
    ("정보", "알린다", "상태가 아니라 <b>안내</b>"),
    ("세 자리", "바탕·글·테두리", "같은 색을 <b>그대로 쓰면</b> 대비비가 깨진다"),
    ("색만", "위험하다", "<b>모양과 말</b>을 같이 둔다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          남성 스무 명 가운데 한 명쯤이 <b>적록 색각</b>입니다.
          그분들에게 성공의 초록과 오류의 빨강은 거의 같은 색으로 보입니다 —
          데모가 재는 숫자가 그것입니다.
          그래서 WCAG 는 <b>색을 유일한 단서로 쓰지 말라</b>고 못박아 두었습니다.<br>
          고치는 방법은 색을 바꾸는 게 아닙니다. <b>모양을 더하는 것</b>입니다 —
          ✓ 와 ✕ 는 색이 안 보여도 다릅니다.
          거기에 '승인됨' · '실패' 같은 <b>말</b>까지 붙으면
          소리로 듣는 분에게도 상태가 전해집니다.</p>''',
  do=ul([
    "색마다 <b>바탕 · 글 · 테두리</b> 세 값을 따로 두기",
    "색 옆에 <b>모양</b>을 두기 — ✓ · ! · ✕",
    "되돌릴 수 없는 일에만 <b>오류 색</b>을 쓰기",
  ]),
  dont=ul([
    "색 하나로만 상태 알리기 — <b>색을 못 보는 사람</b>이 있다",
    "같은 색을 바탕과 글에 <b>그대로</b> 쓰기 — 대비비가 안 맞는다",
    "상태 색을 <b>브랜드 색</b>으로 쓰기 — 뜻이 흐려진다",
    "주의와 오류를 <b>섞어 쓰기</b> — 둘 다 무시당하게 된다",
  ]),
  instead='색 체계 전체는 <a href="color.html">색 토큰</a>, 읽히는 밝기는 <a href="contrast.html">대비비</a>, 오류 문구는 <a href="errortext.html">오류 문구</a>, 알림 부품은 <a href="toast.html">토스트</a>.',
  cases=cases([
    (alert("#cf222e", "✕", "계좌 번호를 확인해 주세요", "입력 오류", "", True), "입력 오류", "칸 옆에 <b>붙여서</b>"),
    (alert("#1a7f37", "✓", "저장했습니다", "토스트", "", True), "저장 확인", "짧게 뜨고 사라진다"),
    (alert("#9a6700", "!", "3건이 기한을 넘겼습니다", "배지", "", True), "배지", "숫자와 <b>같이</b> 쓴다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 색의 계약서",
  code_lede="색마다 세 자리를 두고, 마크업에는 <b>모양과 말</b>을 같이 넣습니다.",
  code='''<span class="c">/* 색 하나가 세 자리를 가진다 */</span>
:root {
  --danger-bg: <span class="a">#fff1f0</span>;
  --danger-fg: <span class="a">#cf222e</span>;   <span class="c">/* 바탕 위에서 4.5:1 넘김 */</span>
  --danger-border: <span class="a">#f5b5b0</span>;
}

<span class="c">/* 색 말고도 단서가 둘 더 있다 — 모양과 말 */</span>
&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"alert alert--danger"</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✕&lt;/<span class="t">span</span>&gt;
  계좌가 맞지 않습니다 &lt;<span class="t">b</span>&gt;실패&lt;/<span class="t">b</span>&gt;
&lt;/<span class="t">p</span>&gt;

<span class="c">/* ✕ 색이 유일한 단서다 */</span>
.row.is-error { <span class="a">color</span>: red; }''',
  keys=kbd([
    ("<code>role=\"alert\"</code>", "오류는 <b>그 자리에서</b> 읽어 준다"),
    ("<code>role=\"status\"</code>", "성공·안내는 <b>하던 말이 끝난 뒤</b> 읽어 준다"),
    ("<code>aria-invalid</code>", "틀린 입력칸에 붙인다 — 색과 <b>따로</b> 전해진다"),
    ("<code>aria-hidden</code>", "✓·✕ 같은 기호는 <b>안 읽게</b> 하고 말로 따로 적는다"),
    ("대비비 4.5:1", "상태 글자도 <b>본문과 같은 기준</b>이다"),
    ("확인하는 법", "화면을 <b>흑백으로</b> 놓고도 상태가 읽히는지 본다"),
  ]),
  backend=rows([
    ("상태는 <b>이름</b>으로", "<code>status: \"failed\"</code> 처럼 보내면 화면이 색과 모양을 고릅니다. 색 코드나 문구를 보내지 않습니다."),
    ("이유를 같이", "<code>reason: \"account_mismatch\"</code> 가 있으면 <b>무엇을 고쳐야 하는지</b>까지 쓸 수 있습니다."),
    ("가짓수를 좁게", "상태가 열 가지로 늘면 색이 모자랍니다 — <b>네 갈래로 묶어</b> 주고 자세한 것은 글로 적습니다."),
  ]),
  plat_lede="네 색이라는 틀은 같고, <b>쓰는 색조</b>가 조금씩 다릅니다.",
  plats=plats([
    ("웹", "직접 정함",
     alert("#cf222e", "✕", "계좌가 맞지 않습니다", "danger", "", True),
     "정해진 규격이 없습니다. 어두운 모드까지 <b>두 벌</b>을 손으로 맞춰야 합니다."),
    ("iOS", "systemRed 등",
     '''              <div class="phone" role="img" aria-label="iOS 상태 색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:11px;border-radius:3px;background:#ffd9d6"></div>
                <div style="position:absolute;left:6px;right:6px;top:46px;height:11px;border-radius:3px;background:#d7f2de"></div></div></div>''',
     "OS 가 <code>systemRed</code>·<code>systemGreen</code>을 줍니다. <b>어두운 모드와 고대비</b>까지 따라옵니다."),
    ("안드로이드", "error · tertiary",
     '''              <div class="phone" role="img" aria-label="안드로이드 상태 색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:11px;border-radius:3px;background:#f9dedc"></div>
                <div style="position:absolute;left:6px;right:6px;top:46px;height:11px;border-radius:3px;background:#d8f3dc"></div></div></div>''',
     "Material 은 <b>error</b> 만 정식 역할로 두고 나머지는 직접 정합니다. 쌍으로 <code>onError</code> 가 따라옵니다."),
  ]),
  plat_note="앱 쪽은 <b>OS 가 준 색</b>을 쓰면 어두운 모드와 고대비 설정까지 저절로 따라옵니다. 웹에는 그런 선물이 없어서 <b>두 벌을 손으로</b> 맞춰야 하고, 그래서 어두운 모드에서 상태 색이 탁해지는 일이 잦습니다. Material 이 색마다 <code>onError</code> 같은 <b>짝을 묶어 두는 방식</b>은 그대로 베낄 만합니다 — 바탕색을 고를 때 그 위에 올릴 글자색을 <b>같이</b> 정하게 되기 때문입니다.",
  siblings=siblings("statecolor"),
  related='''        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="badge.html"><b>배지</b><em>5부</em></a></li>''',
)
