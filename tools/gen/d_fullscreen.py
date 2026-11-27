# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">화면을 다 덮는다 — 가림막이 안 보인다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">닫기(✕)이지 뒤로가기가 아니다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">제목 — 무엇을 하는 중인지</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">주 동작은 오른쪽 위 — 저장 · 완료</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">기록에 넣으면 시스템 백으로도 닫힌다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">화면처럼 보이지만 화면이 아니다 — 뒤가 남아 있다</div>
                </div>
              </div>'''

D = dict(
  slug="fullscreen", ko="전체 화면 레이어", en="Full-screen layer",
  desc="화면을 다 덮는 겹침. 모달과 가르는 기준(폭)과 닫기·시스템 백 처리.",
  lede="<b>화면처럼 보이지만 화면이 아닙니다</b> — 뒤에 하던 일이 그대로 있고, 닫으면 돌아옵니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 '새 가게 등록'이라도 <b>넓은 화면에서는 모달</b>, <b>좁은 화면에서는 전체 화면</b>이 맞습니다 —
          390px 에 뜬 모달은 가장자리 여백만 남기고 내용 칸을 더 좁힙니다.
          데모가 <b>내용이 쓸 수 있는 폭</b>을 재서 둘을 견줍니다.<br>
          전체 화면 레이어는 <b>닫기(✕)</b>이지 뒤로가기가 아니고,
          제목 줄에 <b>무엇을 하는 중인지</b>를 적어야 합니다.
          기록에 넣어 두면 <b>시스템 백</b>으로도 닫힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "전체 화면 레이어, 풀스크린 모달, 전체 화면 시트"),
    ("영어", "full-screen layer, full-screen modal, full-screen dialog, modal page"),
    ("같이 쓰는 말",
     "안드로이드에서는 <b>풀스크린 다이얼로그</b>, iOS 에서는 <b>모달 프레젠테이션</b>(fullScreenCover)이라 부릅니다. "
     "폭에 따라 모달과 전체 화면을 바꿔 쓰는 것을 <b>반응형 모달</b>이라 하고, "
     "아래에서 전체 높이까지 올라오는 꼴은 <b>풀 시트</b>입니다."),
    ("자주 잘못 부름",
     "<b>모달</b> — <a href=\"modal.html\">모달</a>은 <b>가림막 위에 작게</b> 뜹니다.<br>"
     "<b>새 화면</b> — 진짜 화면 전환은 <b>주소가 바뀌고 뒤가 사라집니다</b>.<br>"
     "<b>바텀시트</b> — <a href=\"sheet.html\">바텀시트</a>는 <b>아래에서</b> 올라오고 보통 덜 덮습니다."),
  ]),
  axes=axis_table("전체 화면 레이어"),
  oneline="<b>폰에서는 전체 화면, PC 에서는 모달.</b> 같은 내용이라도 폭에 따라 바꿉니다.",
  states=states([
    (fs("none", "", "평소 — 목록", True), "닫힘", "뒤에 있던 화면"),
    (fs("full", "", "화면을 다 덮는다", True), "전체 화면", "<b>폰에서</b> 맞다"),
    (fs("modal", "", "가림막 위에 작게", True), "모달", "<b>PC 에서</b> 맞다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">폰인데 모달</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">내용 칸이 더 좁아진다</span>'),
         "폭을 안 따짐", False, "", "152px"),
     "폰에 모달", "<b>칸이 더 좁아진다</b>"),
    (one(txt('<span style="display:block;font-size:8px">✕ 닫기 · 저장</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">‹ 뒤로가 아니다</span>'),
         "머리 줄", True, "", "152px"),
     "닫기 vs 뒤로", "<b>✕ 가 맞다</b>"),
    (one(txt('<span style="display:block;font-size:8px">시스템 백</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">기록에 넣으면 이것으로도 닫힌다</span>'),
         "기록", True, "", "152px"),
     "시스템 백", "<b>폰의 기본 기대</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("다 덮음", "가림막 없음", "뒤가 <b>안 보인다</b>"),
    ("닫기", "✕", "<b>뒤로가 아니다</b>"),
    ("제목", "무엇을 하는 중", "'새 가게 등록'"),
    ("주 동작", "오른쪽 위", "저장 · 완료"),
    ("기록", "넣어 두기", "<b>시스템 백</b>으로도 닫힌다"),
    ("화면 아님", "뒤가 남음", "닫으면 <b>돌아온다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>✕ 와 ‹ 중 무엇을 둘지</b>가 자주 헷갈립니다 —
          전체 화면 레이어는 <b>덮고 올라온 것</b>이니 <b>✕(닫기)</b> 가 맞습니다.
          <b>‹(뒤로)</b> 는 계층을 타고 내려갔을 때 쓰는 표시라,
          덮고 올라온 것에 쓰면 '어디로 돌아가는지'가 모호해집니다.<br>
          폰에서는 <b>시스템 백</b>으로도 닫히는 것이 기본 기대입니다 —
          안 그러면 시스템 백이 레이어를 지나쳐 <b>그 뒤 화면까지</b> 날려 버립니다.
          기록에 한 칸을 넣어 두면 그 문제가 통째로 사라집니다.</p>''',
  do=ul([
    "<b>좁으면 전체 화면, 넓으면 모달</b>로 바꾸기",
    "<b>✕(닫기)</b> 를 쓰고 주 동작은 오른쪽 위에",
    "<b>기록에 넣어</b> 시스템 백으로도 닫히게 하기",
  ]),
  dont=ul([
    "폰에서 <b>모달</b>로 띄우기 — 내용 칸이 더 좁아진다",
    "<b>‹(뒤로)</b> 를 쓰기 — 어디로 가는지 모호하다",
    "기록에 안 넣기 — <b>시스템 백이 뒤 화면까지</b> 지운다",
    "안에서 또 전체 화면을 띄우기 — <b>겹치면 나올 길</b>이 복잡해진다",
  ]),
  instead='가림막 위에 작게 뜨면 <a href="modal.html">모달</a>, 아래에서 올라오면 <a href="sheet.html">바텀시트</a>, 진짜 화면 전환이면 주소를 바꾸고, 뒤로가기 처리는 <a href="systemback.html">시스템 백</a>.',
  cases=cases([
    (fs("full", "", "", True, "150px"), "새로 만들기", "칸이 <b>여러 개</b>일 때"),
    (fs("full", "", "", True, "150px"), "긴 폼", "모달에 <b>안 들어가는</b> 내용"),
    (fs("modal", "", "", True, "150px"), "PC 에서 같은 일", "<b>모달</b>로 바뀐다"),
  ]),
  code_lede="같은 <code>&lt;dialog&gt;</code> 를 쓰고 <b>CSS 로만</b> 모양을 바꿉니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"editor"</span> <span class="a">aria-label</span>=<span class="s">"새 가게 등록"</span>&gt;
  &lt;<span class="t">header</span>&gt;
    &lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"닫기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">h2</span>&gt;새 가게 등록&lt;/<span class="t">h2</span>&gt;
    &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"primary"</span>&gt;저장&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">header</span>&gt;
  …
&lt;/<span class="t">dialog</span>&gt;

<span class="c">/* 좁으면 전체 화면, 넓으면 모달 — 마크업은 하나다 */</span>
dialog { <span class="a">width</span>: min(<span class="a">520px</span>, <span class="a">calc</span>(<span class="a">100%</span> - <span class="a">48px</span>)); <span class="a">border-radius</span>: <span class="a">var</span>(--radius-4); }
@media (max-width: <span class="a">480px</span>) {
  dialog { <span class="a">width</span>: <span class="a">100%</span>; <span class="a">max-width</span>: none; <span class="a">height</span>: <span class="a">100dvh</span>;
    <span class="a">max-height</span>: none; <span class="a">margin</span>: <span class="a">0</span>; <span class="a">border-radius</span>: <span class="a">0</span>; }
}''',
  keys=kbd([
    ("Esc", "닫는다 — <b>저장은 안 된다</b>"),
    ("Tab", "레이어 안에 <b>갇힌다</b>"),
    ("초점", "열면 <b>닫기나 첫 칸</b>, 닫으면 <b>부른 자리</b>로"),
    ("<code>aria-modal=\"true\"</code>", "뒤가 <b>안 읽힌다</b>고 알린다"),
    ("<code>100dvh</code>", "폰 주소창이 숨어도 <b>안 흔들린다</b>"),
    ("확인하는 법", "폰 폭에서 열고 <b>시스템 백</b>을 눌러 본다"),
  ]),
  backend=rows([
    ("초안 저장", "긴 폼이면 <b>중간 저장</b>을 두어 닫혀도 안 날아가게 합니다."),
    ("닫을 때 확인", "적은 것이 있으면 <b>그냥 닫지 않고</b> 한 번 묻습니다 — <a href=\"destructive.html\">위험한 동작</a>과 같은 생각입니다."),
  ]),
  plat_lede="<b>폰에서는 이쪽이 기본</b>입니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt; + 미디어 쿼리",
     fs("full", "", "", True, "110px"),
     "마크업 하나로 <b>모달과 전체 화면</b>을 오갈 수 있는 것이 장점입니다."),
    ("iOS", "fullScreenCover",
     '''              <div class="phone" role="img" aria-label="iOS 전체 화면 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:var(--surface)"></div>
                <div style="position:absolute;left:4px;right:4px;top:20px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:4px;top:21px;font-size:5px;color:var(--accent)">✕</div></div></div>''',
     "<b>아래로 쓸어</b> 닫는 시트가 기본이고, 완전히 덮는 꼴도 따로 있습니다."),
    ("안드로이드", "Full-screen dialog",
     '''              <div class="phone" role="img" aria-label="안드로이드 전체 화면 다이얼로그 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:var(--surface)"></div>
                <div style="position:absolute;left:0;right:0;top:18px;height:10px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:3px;top:20px;font-size:5px;color:var(--accent)">✕</div>
                <div style="position:absolute;right:3px;top:20px;font-size:5px;color:var(--accent)">저장</div></div></div>''',
     "Material 에 <b>정식 부품</b>으로 있습니다 — 왼쪽 ✕, 오른쪽 저장이 규격입니다."),
  ]),
  plat_note="Material 의 <b>풀스크린 다이얼로그</b>는 머리 줄 규격까지 정해 두었습니다 — 왼쪽에 ✕, 가운데 제목, 오른쪽에 저장. 웹에서 그대로 따라도 어색하지 않고, <b>무엇을 하는 중이고 어떻게 빠져나가는지</b>가 한 줄에 다 들어갑니다. 이 꼴을 쓰면 '이게 화면인가 레이어인가'를 사용자가 헷갈릴 일도 줄어듭니다.",
  siblings=siblings("fullscreen"),
  related='''        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>''',
)
