# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품은 생김새로는 가르기 어렵습니다. 아래 네 가지로 가릅니다."

def fs(kind, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if kind == 'full':
        inner = ('<span style="position:absolute;inset:0;background:var(--surface)">'
                 '<span style="display:flex;gap:5px;align-items:center;padding:4px 6px;'
                 'border-bottom:1px solid var(--line);font-size:7.5px">'
                 '<span style="color:var(--accent)">✕</span><b>새 가게 등록</b>'
                 '<span style="margin-left:auto;color:var(--accent);font-weight:700">저장</span></span>'
                 '<span style="display:grid;gap:3px;padding:6px">'
                 '<span style="display:block;height:5px;border-radius:2px;background:var(--bg)"></span>'
                 '<span style="display:block;height:5px;width:80%;border-radius:2px;background:var(--bg)"></span>'
                 '<span style="display:block;height:5px;width:65%;border-radius:2px;background:var(--bg)"></span>'
                 '</span></span>')
    elif kind == 'modal':
        inner = ('<span style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 40%, transparent)"></span>'
                 '<span style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:72%;'
                 'border-radius:5px;background:var(--surface);padding:5px;display:grid;gap:3px">'
                 '<span style="display:flex;gap:4px;font-size:7.5px"><b>새 가게 등록</b>'
                 '<span style="margin-left:auto;color:var(--fg-muted)">✕</span></span>'
                 '<span style="display:block;height:5px;border-radius:2px;background:var(--bg)"></span>'
                 '<span style="display:block;height:5px;width:75%;border-radius:2px;background:var(--bg)"></span></span>')
    else:
        inner = ('<span style="display:grid;gap:3px;padding:6px">'
                 '<span style="font-size:7.5px;font-weight:700">가게 목록</span>'
                 '<span style="display:block;height:5px;border-radius:2px;background:var(--bg)"></span>'
                 '<span style="display:block;height:5px;width:72%;border-radius:2px;background:var(--bg)"></span></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);overflow:hidden">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">화면을 다 덮어 가림막이 보이지 않음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">뒤로가기가 아니라 닫기(✕)를 둠</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">제목으로 무엇을 하는 중인지 알림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">저장 · 완료 같은 주 동작은 오른쪽 위에</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">기록에 넣으면 시스템 백으로도 닫힘</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">새 화면처럼 보여도 뒤 화면이 남아 있음</div>
                </div>
              </div>'''

D = dict(
  slug="fullscreen", ko="전체 화면 레이어", en="Full-screen layer",
  desc="화면 전체를 덮는 겹침 부품입니다. 모달과 가르는 기준인 화면 폭, 그리고 닫기 단추와 시스템 백 처리를 다룹니다.",
  lede="전체 화면 레이어는 화면 전체를 덮기 때문에 <b>새 화면처럼 보이지만 실제로 화면이 바뀐 것은 아닙니다</b>. 뒤에 하던 화면이 그대로 남아 있어서, 레이어를 닫으면 그 화면으로 돌아옵니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 '새 가게 등록'이라도 <b>넓은 화면에서는 모달</b>로, <b>좁은 화면에서는 전체 화면</b>으로 띄우는 것이 맞습니다.
          390px 폭에 모달을 띄우면 모달 둘레에 여백이 생기는 만큼 내용을 담을 칸이 더 좁아지기 때문입니다.
          데모는 두 방식에서 <b>내용이 쓸 수 있는 폭</b>을 재서 비교합니다.<br>
          전체 화면 레이어에는 뒤로가기(‹)가 아니라 <b>닫기(✕)</b> 단추를 두고,
          제목 줄에는 <b>무엇을 하는 중인지</b> 적어야 합니다.
          또 레이어를 열 때 기록에 한 칸을 넣어 두면 <b>시스템 백</b>으로도 닫힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "전체 화면 레이어, 풀스크린 모달, 전체 화면 시트"),
    ("영어", "full-screen layer, full-screen modal, full-screen dialog, modal page"),
    ("같이 쓰는 말",
     "안드로이드에서는 <b>풀스크린 다이얼로그</b>, iOS에서는 <b>모달 프레젠테이션</b>(fullScreenCover)이라고 부릅니다. "
     "화면 폭에 따라 모달과 전체 화면을 바꿔 쓰는 방식은 <b>반응형 모달</b>이라고 하고, "
     "아래에서 화면 높이 끝까지 올라오는 모양은 <b>풀 시트</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>모달</b> — 화면을 다 덮지 않고 <b>가림막 위에 작게</b> 뜨면 <a href=\"modal.html\">모달</a>입니다.<br>"
     "<b>새 화면</b> — 실제로 화면이 바뀌면 <b>주소가 바뀌고 앞의 화면은 사라집니다</b>. 전체 화면 레이어는 뒤의 화면이 남아 있다는 점이 다릅니다.<br>"
     "<b>바텀시트</b> — 화면 <b>아래에서</b> 올라오고 보통 화면을 다 덮지 않으면 <a href=\"sheet.html\">바텀시트</a>입니다."),
  ]),
  axes=axis_table("전체 화면 레이어"),
  oneline="같은 내용이라도 화면 폭에 따라 <b>폰에서는 전체 화면으로, PC에서는 모달로</b> 바꿔 띄웁니다.",
  states=states([
    (fs("none", "", "평소에 보는 목록", True), "레이어를 열기 전", "레이어를 열기 전, 뒤에 있던 목록 화면입니다"),
    (fs("full", "", "화면을 다 덮음", True), "전체 화면으로 띄웠을 때", "<b>폰처럼 좁은 화면에서</b> 맞는 방식입니다"),
    (fs("modal", "", "가림막 위에 작게", True), "모달로 띄웠을 때", "<b>PC처럼 넓은 화면에서</b> 맞는 방식입니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">폰에서 모달로 띄움</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">내용 칸이 더 좁아짐</span>'),
         "폭을 따지지 않음", False, "", "152px"),
     "폰에서 모달로 띄웠을 때", "폰에 모달을 띄우면 둘레 여백 때문에 내용 <b>칸이 더 좁아집니다</b>"),
    (one(txt('<span style="display:block;font-size:8px">✕ 닫기 · 저장</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">‹ 뒤로 단추는 두지 않음</span>'),
         "머리 줄", True, "", "152px"),
     "닫기 단추와 뒤로 단추 고르기", "화면 위를 덮고 올라온 레이어이므로 <b>✕가 맞습니다</b>"),
    (one(txt('<span style="display:block;font-size:8px">시스템 백</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">기록에 넣으면 이것으로도 닫힘</span>'),
         "기록", True, "", "152px"),
     "시스템 백을 눌렀을 때", "폰 사용자는 <b>시스템 백으로도 닫히기를</b> 기대합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("덮는 범위", "화면 전체, 가림막 없음", "화면을 다 덮어서 뒤의 화면이 <b>보이지 않습니다</b>"),
    ("닫기", "✕", "<b>뒤로가기(‹)가 아니라</b> 닫기 단추(✕)를 둡니다"),
    ("제목", "무엇을 하는 중인지", "'새 가게 등록'처럼 지금 무엇을 하는 중인지 적습니다"),
    ("주 동작", "오른쪽 위", "저장이나 완료 같은 주 동작은 오른쪽 위에 둡니다"),
    ("기록", "기록에 넣어 두기", "열 때 기록에 한 칸을 넣어 두면 <b>시스템 백</b>으로도 닫힙니다"),
    ("뒤에 남은 화면", "닫으면 돌아옴", "뒤의 화면이 그대로 남아 있어서 닫으면 그 화면으로 <b>돌아옵니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>✕와 ‹ 중 무엇을 둘지</b> 자주 헷갈리는데,
          전체 화면 레이어는 지금 화면 위를 <b>덮고 올라온 것</b>이므로 <b>✕(닫기)</b>가 맞습니다.
          <b>‹(뒤로)</b>는 계층을 따라 한 단계 아래 화면으로 들어갔을 때 쓰는 표시입니다.
          그래서 덮고 올라온 레이어에 ‹를 쓰면 누를 때 어디로 돌아가는지 알기 어려워집니다.<br>
          폰 사용자는 <b>시스템 백</b>을 눌러도 레이어가 닫히기를 기대합니다.
          그런데 레이어를 기록에 넣지 않으면 시스템 백이 레이어를 닫는 대신 <b>그 뒤의 화면까지</b> 벗어나 버립니다.
          레이어를 열 때 기록에 한 칸을 넣어 두면 시스템 백이 레이어만 닫기 때문에 이 문제가 생기지 않습니다.</p>''',
  do_title="전체 화면 레이어를 만들 때 지킬 것",
  dont_title="전체 화면 레이어를 만들 때 피할 것",
  do=ul([
    "화면이 <b>좁으면 전체 화면, 넓으면 모달</b>로 바꾸기",
    "<b>✕(닫기)</b>를 쓰고 주 동작은 오른쪽 위에 두기",
    "<b>기록에 넣어</b> 시스템 백으로도 닫히게 하기",
  ]),
  dont=ul([
    "폰에서 <b>모달</b>로 띄우기. 둘레 여백 때문에 내용 칸이 더 좁아집니다",
    "<b>‹(뒤로)</b>를 쓰기. 누르면 어디로 가는지 알기 어렵습니다",
    "기록에 넣지 않기. <b>시스템 백을 누르면 뒤의 화면까지</b> 벗어납니다",
    "레이어 안에서 전체 화면을 또 띄우기. 레이어가 <b>겹치면 빠져나오는 길</b>이 복잡해집니다",
  ]),
  instead='가림막 위에 작게 띄우려면 <a href="modal.html">모달</a>을 쓰고, 화면 아래에서 올라오게 하려면 <a href="sheet.html">바텀시트</a>가 맞습니다. 실제로 화면을 바꾸는 것이라면 레이어 대신 주소를 바꾸고, 뒤로가기 처리는 <a href="systemback.html">시스템 백</a>에서 다룹니다.',
  cases=cases([
    (fs("full", "", "", True, "150px"), "입력 칸이 많은 등록 화면", "입력 칸이 <b>여러 개</b>인 등록 화면에 씁니다"),
    (fs("full", "", "", True, "150px"), "모달에 다 들어가지 않는 긴 폼", "모달에 <b>다 들어가지 않는</b> 긴 내용에 씁니다"),
    (fs("modal", "", "", True, "150px"), "PC에서는 같은 내용을 모달로", "넓은 화면에서는 같은 내용이 <b>모달</b>로 바뀝니다"),
  ]),
  code_lede="마크업은 <code>&lt;dialog&gt;</code> 하나를 그대로 쓰고, 화면 폭에 따라 <b>CSS로만</b> 모양을 바꿉니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"editor"</span> <span class="a">aria-label</span>=<span class="s">"새 가게 등록"</span>&gt;
  &lt;<span class="t">header</span>&gt;
    &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"닫기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">h2</span>&gt;새 가게 등록&lt;/<span class="t">h2</span>&gt;
    &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"primary"</span>&gt;저장&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">header</span>&gt;
  …
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 좁으면 전체 화면, 넓으면 모달. 마크업은 하나로 둔다 */</span>
dialog { <span class="a">width</span>: min(<span class="a">520px</span>, <span class="a">calc</span>(<span class="a">100%</span> - <span class="a">48px</span>)); <span class="a">border-radius</span>: <span class="a">var</span>(--radius-4); }
@media (max-width: <span class="a">480px</span>) {
  dialog { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">max-width</span>: none; <span class="a">height</span>: <span class="a">100dvh</span>;
    <span class="a">max-height</span>: none; <span class="a">margin</span>: <span class="a">0</span>; <span class="a">border-radius</span>: <span class="a">0</span>; }
}''',
  keys=kbd([
    ("Esc", "레이어를 닫습니다. 이때 적던 내용은 <b>저장되지 않습니다</b>"),
    ("Tab", "초점이 레이어 밖으로 나가지 않고 <b>안에서만</b> 돕니다"),
    ("열고 닫을 때의 초점", "열면 초점을 <b>닫기 단추나 첫 입력 칸</b>으로 옮기고, 닫으면 레이어를 <b>부른 자리</b>로 돌려놓습니다"),
    ("<code>aria-modal=\"true\"</code>", "보조 기술에 뒤의 화면은 <b>읽히지 않는다</b>고 알립니다"),
    ("<code>100dvh</code>", "폰에서 주소창이 숨어도 레이어 높이가 <b>흔들리지 않습니다</b>"),
    ("확인하는 방법", "폰 폭에서 레이어를 열고 <b>시스템 백</b>을 눌러 레이어만 닫히는지 확인합니다"),
  ]),
  backend=rows([
    ("적던 내용을 초안으로 저장하기", "폼이 길면 <b>중간 저장</b>을 두어, 레이어가 닫혀도 적던 내용이 사라지지 않게 합니다."),
    ("닫기 전에 한 번 묻기", "사용자가 적은 내용이 있으면 <b>그냥 닫지 않고</b> 닫을지 한 번 묻습니다. <a href=\"destructive.html\">위험한 동작</a>을 확인받는 것과 같은 이유입니다."),
  ]),
  plat_lede="폰에서는 모달보다 <b>전체 화면 레이어가 기본</b>입니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt; + 미디어 쿼리",
     fs("full", "", "", True, "110px"),
     "마크업 하나로 <b>모달과 전체 화면</b>을 오갈 수 있는 것이 장점입니다."),
    ("iOS", "fullScreenCover",
     '''              <div class="phone" role="img" aria-label="iOS 전체 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:var(--surface)"></div>
                <div style="position:absolute;left:4px;right:4px;top:20px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:4px;top:21px;font-size:5px;color:var(--accent)">✕</div></div></div>''',
     "<b>아래로 쓸어</b> 닫는 시트가 기본이고, 화면을 완전히 덮는 방식도 따로 있습니다."),
    ("안드로이드", "Full-screen dialog",
     '''              <div class="phone" role="img" aria-label="안드로이드 전체 화면 다이얼로그 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:var(--surface)"></div>
                <div style="position:absolute;left:0;right:0;top:18px;height:10px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:3px;top:20px;font-size:5px;color:var(--accent)">✕</div>
                <div style="position:absolute;right:3px;top:20px;font-size:5px;color:var(--accent)">저장</div></div></div>''',
     "Material에 <b>정식 부품</b>으로 있고, 머리 줄 왼쪽에 ✕, 오른쪽에 저장을 두는 것이 규격입니다."),
  ]),
  plat_note="Material의 <b>풀스크린 다이얼로그</b>는 머리 줄 규격까지 정해 두었는데, 왼쪽에 ✕, 가운데에 제목, 오른쪽에 저장을 둡니다. 이 배치는 웹에서 그대로 따라 써도 어색하지 않고, <b>무엇을 하는 중이고 어떻게 빠져나가는지</b>를 머리 줄 한 줄에 모두 보여 줍니다. 그래서 이 배치를 쓰면 지금 보는 것이 새 화면인지 레이어인지 사용자가 헷갈릴 일도 줄어듭니다.",
  siblings=siblings("fullscreen"),
  related='''        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>''',
)
