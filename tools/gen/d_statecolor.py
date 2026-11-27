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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">--color-success<span style="color:var(--fg-faint)"> ← 끝남 · 맞음</span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">--color-warning<span style="color:var(--fg-faint)"> ← 되지만 확인 필요</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">--color-danger<span style="color:var(--fg-faint)"> ← 실패함 · 지움</span></div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">--color-info<span style="color:var(--fg-faint)"> ← 안내만 함</span></div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">각각 <b>바탕 · 글 · 테두리</b> 세 자리</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">색만으로는 <b>구별하지 못하는 사람</b>도 있음</div>
                </div>
              </div>'''

D = dict(
  slug="statecolor", ko="상태 색", en="Semantic status colors",
  desc="성공·주의·오류·정보 네 가지 상태 색을 토큰으로 정해 두는 방법과, 색만으로는 상태를 구별하지 못하는 사람이 있다는 점을 보여 주는 항목입니다.",
  lede="상태 색은 <b>네 가지면 충분</b>합니다. 다만 색만으로는 상태를 알아보지 못하는 사람이 있으므로, 색은 <b>다른 단서와 함께</b> 써야 합니다.",
  axes_lede="토큰은 부품이 아니라 <b>값을 쓰는 규칙</b>입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색만으로 상태를 가르면 <b>적록 색각인 사람에게는 성공과 오류가 거의 같은 색</b>으로 보입니다.
          데모는 두 색이 얼마나 다른지를 거리로 재서 적어 줍니다. 색각 흉내 변환은 <b>어림한 값</b>이라서
          실제로 꼭 그렇게 보인다는 뜻은 아니고, 두 색이 '구별하기 어려울 만큼 가깝다'는 것을 숫자로 보여 주려는 것입니다.<br>
          해결 방법은 <b>색을 바꾸는 것이 아니라 단서를 더하는 것</b>입니다.
          모양(✓ · !)과 말('승인됨')을 함께 붙이면 색을 구별하지 못해도 상태를 읽을 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "상태 색, 시맨틱 컬러, 의미 색"),
    ("영어", "semantic colors, status colors, feedback colors"),
    ("같이 쓰는 말",
     "성공 · 주의 · 오류 · 정보 네 가지를 묶어 <b>피드백 색</b>이라고 부르기도 합니다. "
     "각 색은 보통 <code>--color-danger-bg</code> · <code>-fg</code> · <code>-border</code>처럼 "
     "<b>바탕 · 글 · 테두리</b> 세 자리로 나눠 둡니다. "
     "색 하나를 세 자리에 그대로 쓰면 <b>대비비가 맞지 않기</b> 때문입니다."),
    ("자주 잘못 부르는 이름",
     "<b>브랜드 색</b> — <a href=\"color.html\">색 토큰</a>의 주된 색은 <b>어느 브랜드인지</b>를 나타내고, 상태 색은 <b>무슨 일이 생겼는지</b>를 나타냅니다.<br>"
     "<b>빨강은 삭제 색</b> — 빨강은 <b>되돌릴 수 없는 일</b>을 나타내는 색이지, 삭제에만 쓰는 색이 아닙니다.<br>"
     "<b>초록은 켜짐 색</b> — <a href=\"switch.html\">스위치</a>가 켜진 상태에는 보통 <b>주된 색</b>을 씁니다."),
  ]),
  axes=ax("상태 색"),
  oneline="<b>색은 두 번째 단서로 써야 합니다.</b> 모양이나 말로 먼저 상태를 알리고, 색은 같은 내용을 한 번 더 보여 주는 데 씁니다.",
  s4_title="상태를 알리는 네 가지 색", s4_hint="무슨 일이 생겼는지 알리는 색",
  states=states([
    (alert("#1a7f37", "✓", "정산이 들어왔습니다", "success", "끝남 · 맞음", True), "성공을 알릴 때", "사용자가 더 <b>할 일이 없습니다</b>"),
    (alert("#9a6700", "!", "정산이 하루 밀렸습니다", "warning", "되지만 확인 필요"), "주의를 줄 때", "진행을 막지는 않습니다"),
    (alert("#cf222e", "✕", "계좌가 맞지 않습니다", "danger", "실패함 · 지움"), "오류를 알릴 때", "문제를 <b>고쳐야</b> 다음으로 넘어갈 수 있습니다"),
    (alert("#0969da", "i", "다음 정산은 금요일", "info", "안내만 함"), "안내를 전할 때", "상태가 아니라 안내를 전합니다"),
    (alert("#1a7f37", "", "정산이 들어왔습니다", "색만", "단서가 하나뿐", False, False),
     "색만으로 알릴 때", "<b>색을 구별하지 못하면</b> 상태를 알 수 없습니다"),
    (alert("#8a8f99", "·", "불러오는 중입니다", "neutral", "결과를 아직 모름"), "결과를 기다리는 중립 상태", "결과가 <b>아직</b> 나오지 않았습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("성공", "success", "더 할 일이 <b>없다</b>는 뜻입니다"),
    ("주의", "warning", "진행을 막지는 <b>않습니다</b>"),
    ("오류", "danger · error", "문제를 <b>고쳐야</b> 넘어갈 수 있습니다"),
    ("정보", "info", "상태가 아니라 <b>안내</b>를 전합니다"),
    ("세 자리", "bg · fg · border", "같은 색을 세 자리에 <b>그대로 쓰면</b> 대비비가 맞지 않습니다"),
    ("색만", "color only", "색 옆에 <b>모양과 말</b>을 함께 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          남성 스무 명 가운데 한 명쯤이 <b>적록 색각</b>입니다.
          적록 색각인 사람에게는 성공을 뜻하는 초록과 오류를 뜻하는 빨강이 거의 같은 색으로 보이는데,
          데모가 재는 숫자가 이 차이입니다.
          그래서 WCAG는 <b>색을 유일한 단서로 쓰지 말라</b>고 정해 두었습니다.<br>
          해결 방법은 색을 바꾸는 것이 아니라 <b>모양을 더하는 것</b>입니다.
          ✓와 ✕는 색을 구별하지 못해도 모양이 다르기 때문입니다.
          여기에 '승인됨' · '실패' 같은 <b>말</b>까지 붙이면
          스크린 리더로 듣는 사람에게도 상태가 전해집니다.</p>''',
  do_title="상태 색을 쓸 때 지킬 것",
  dont_title="상태 색을 쓸 때 피할 것",
  do=ul([
    "색마다 <b>바탕 · 글 · 테두리</b> 세 값을 따로 두기",
    "색 옆에 ✓ · ! · ✕ 같은 <b>모양</b>을 두기",
    "되돌릴 수 없는 일에만 <b>오류 색</b>을 쓰기",
  ]),
  dont=ul([
    "색 하나로만 상태 알리기. <b>색을 구별하지 못하는 사람</b>에게는 상태가 전해지지 않습니다",
    "같은 색을 바탕과 글에 <b>그대로</b> 쓰기. 대비비가 맞지 않습니다",
    "상태 색을 <b>브랜드 색</b>으로 쓰기. 그 색이 상태를 뜻하는지 장식인지 가릴 수 없게 됩니다",
    "주의와 오류를 <b>섞어 쓰기</b>. 사용자가 둘을 구별하지 못해 결국 둘 다 대수롭지 않게 넘깁니다",
  ]),
  instead_title="함께 보면 좋은 항목",
  instead='색 체계 전체는 <a href="color.html">색 토큰</a> 항목에서, 글이 읽히는 밝기는 <a href="contrast.html">대비비</a> 항목에서 다룹니다. 오류를 알리는 글은 <a href="errortext.html">오류 문구</a> 항목에서, 알림을 띄우는 부품은 <a href="toast.html">토스트</a> 항목에서 설명합니다.',
  cases=cases([
    (alert("#cf222e", "✕", "계좌 번호를 확인해 주세요", "입력 오류", "", True), "입력 오류를 입력칸 옆에 알리기", "틀린 입력칸 옆에 <b>붙여서</b> 보여 줍니다"),
    (alert("#1a7f37", "✓", "저장했습니다", "토스트", "", True), "저장했다고 잠깐 알리기", "짧게 떴다가 사라집니다"),
    (alert("#9a6700", "!", "3건이 기한을 넘겼습니다", "배지", "", True), "배지에 숫자와 함께 쓰기", "숫자와 <b>함께</b> 씁니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="상태 색을 코드로 옮기는 방법",
  keys_heads="<th>속성과 기준</th><th>쓰면 일어나는 일</th>",
  code_lede="색마다 세 자리의 값을 두고, 마크업에는 <b>모양과 말</b>을 함께 넣습니다.",
  code='''<span class="c">/* 색 하나에 세 자리 값을 둔다 */</span>
:root {
  --danger-bg: <span class="a">#fff1f0</span>;
  --danger-fg: <span class="a">#cf222e</span>;   <span class="c">/* 바탕 위에서 4.5:1 넘김 */</span>
  --danger-border: <span class="a">#f5b5b0</span>;
}

<span class="c">/* 색 말고도 모양과 말, 두 가지 단서를 더 둔다 */</span>
&lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"alert alert--danger"</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;✕&lt;/<span class="t">span</span>&gt;
  계좌가 맞지 않습니다 &lt;<span class="t">b</span>&gt;실패&lt;/<span class="t">b</span>&gt;
&lt;/<span class="t">p</span>&gt;

<span class="c">/* ✕ 색이 유일한 단서다 */</span>
.row.is-error { <span class="a">color</span>: red; }''',
  keys=kbd([
    ("<code>role=\"alert\"</code>", "오류는 <b>그 자리에서 바로</b> 읽어 줍니다"),
    ("<code>role=\"status\"</code>", "성공과 안내는 스크린 리더가 <b>읽던 내용을 마친 뒤</b> 읽어 줍니다"),
    ("<code>aria-invalid</code>", "틀린 입력칸에 붙입니다. 색과는 <b>별도로</b> 오류 상태가 전해집니다"),
    ("<code>aria-hidden</code>", "✓·✕ 같은 기호는 <b>읽지 않게</b> 하고, 상태는 말로 따로 적습니다"),
    ("대비비 4.5:1", "상태를 알리는 글자도 <b>본문과 같은 기준</b>을 지킵니다"),
    ("확인하는 방법", "화면을 <b>흑백으로</b> 바꿔도 상태가 읽히는지 봅니다"),
  ]),
  backend=rows([
    ("상태는 <b>이름</b>으로 보내기", "서버가 <code>status: \"failed\"</code>처럼 상태 이름을 보내면 화면이 색과 모양을 고릅니다. 서버는 색 코드나 문구를 보내지 않습니다."),
    ("상태의 이유도 함께 보내기", "<code>reason: \"account_mismatch\"</code>처럼 이유까지 보내면 화면에 <b>무엇을 고쳐야 하는지</b>까지 적을 수 있습니다."),
    ("상태 가짓수를 네 갈래로 묶기", "상태가 열 가지로 늘어나면 색이 모자랍니다. 그래서 상태는 <b>네 갈래로 묶어</b> 보내고, 자세한 내용은 글로 적습니다."),
  ]),
  plat_lede="네 가지 색을 쓴다는 틀은 같지만, 플랫폼마다 <b>쓰는 색조</b>가 조금씩 다릅니다.",
  plats=plats([
    ("웹", "직접 정함",
     alert("#cf222e", "✕", "계좌가 맞지 않습니다", "danger", "", True),
     "정해진 규격이 없어서, 어두운 모드용까지 <b>두 벌</b>을 직접 맞춰야 합니다."),
    ("iOS", "systemRed 등",
     '''              <div class="phone" role="img" aria-label="iOS 상태 색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:11px;border-radius:3px;background:#ffd9d6"></div>
                <div style="position:absolute;left:6px;right:6px;top:46px;height:11px;border-radius:3px;background:#d7f2de"></div></div></div>''',
     "OS가 <code>systemRed</code>·<code>systemGreen</code> 같은 색을 제공하고, 이 색들은 <b>어두운 모드와 고대비</b> 설정에 맞춰 저절로 바뀝니다."),
    ("안드로이드", "error · tertiary",
     '''              <div class="phone" role="img" aria-label="안드로이드 상태 색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:11px;border-radius:3px;background:#f9dedc"></div>
                <div style="position:absolute;left:6px;right:6px;top:46px;height:11px;border-radius:3px;background:#d8f3dc"></div></div></div>''',
     "Material은 <b>error</b>만 정식 색 역할로 두고 나머지 상태 색은 직접 정하게 합니다. error에는 그 위에 올릴 글자색인 <code>onError</code>가 짝으로 붙어 있습니다."),
  ]),
  plat_note="앱에서는 <b>OS가 제공하는 색</b>을 쓰면 어두운 모드와 고대비 설정에 맞춰 색이 저절로 바뀝니다. 웹에는 그런 장치가 없어서 <b>두 벌을 직접</b> 맞춰야 하고, 그 때문에 어두운 모드에서 상태 색이 탁해지는 일이 잦습니다. Material이 색마다 <code>onError</code> 같은 <b>짝을 묶어 두는 방식</b>은 웹에서도 그대로 따라 할 만합니다. 바탕색을 고를 때 그 위에 올릴 글자색도 <b>함께</b> 정하게 되기 때문입니다.",
  siblings=siblings("statecolor"),
  related='''        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="badge.html"><b>배지</b><em>5부</em></a></li>''',
)
