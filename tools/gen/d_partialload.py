# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT2 = table(
  ["무엇을 가리나", "하던 일이 끊기나", "초점이 남나", "쓰기 쉬운가"],
  [["전체 스피너", "<b>화면 전부</b>", "끊긴다", "날아간다", "가장 쉽다"],
   ["부분 로딩", "<b>바뀌는 곳만</b>", "안 끊긴다", "남는다", "손이 더 간다"],
   ["버튼 안 표시", "그 단추만", "안 끊긴다", "남는다", "쉽다"],
   ["<a href=\"skeleton.html\">스켈레톤</a>", "들어올 자리", "처음에만", "해당 없음", "쉽다"]],
  me="부분 로딩")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">바뀌는 곳만 다시 그린다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">그 줄만 흐리게 — 나머지는 읽을 수 있다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">전체를 다시 그리면 입력칸이 새로 만들어진다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">초점과 치던 글이 함께 날아간다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">단추 안 표시 — 그 단추만 기다린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">aria-busy — 바뀌는 중임을 알린다</div>
                </div>
              </div>'''

def panel(rows_, busy=-1, allbusy=False, label="", note="", ok=None, w="152px", q="모란"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    head = ('<span style="display:flex;gap:5px;align-items:center;padding:4px 6px;border-bottom:1px solid var(--line);font-size:8px">'
            '<span style="font-weight:700">정산 목록</span>'
            '<span style="margin-left:auto;border:1px solid var(--line);border-radius:3px;padding:1px 5px;'
            'font-size:7px;color:' + ('var(--fg)' if q else 'var(--fg-faint)') + '">' + (q or '검색') + '</span></span>')
    if allbusy:
        body = ('<span style="display:grid;place-items:center;min-height:42px;font-size:8px;color:var(--fg-muted)">'
                '불러오는 중…</span>')
    else:
        body = ''.join('<span style="display:flex;gap:5px;padding:3px 6px;font-size:8px;'
                       + ('opacity:.45;' if i == busy else '') + '">'
                       '<span>' + r[0] + '</span>'
                       '<span style="margin-left:auto;font-family:var(--mono);font-size:7px;color:var(--fg-muted)">'
                       + ('바꾸는 중…' if i == busy else r[1]) + '</span></span>'
                       for i, r in enumerate(rows_))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            + head + '<span style="display:grid;padding:3px 0">' + body + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

R = [("모란상회", "정산 대기"), ("한빛아웃도어", "정산 대기"), ("새벽상사", "정산 완료")]

D = dict(
  slug="partialload", ko="부분 로딩", en="Partial loading",
  desc="화면 전체가 아니라 바뀌는 곳만 다시 그리는 방식과, 그렇게 해서 초점과 입력값을 지키는 방법을 보여 주는 항목입니다.",
  lede="부분 로딩은 데이터가 바뀐 곳만 다시 그리는 방식입니다. 바뀐 것은 한 줄인데 <b>화면 전체를 다시 그리면</b> 사용자가 치던 글과 커서까지 함께 사라집니다.",
  axes_lede="기다림을 보여 주는 방법들을 모았습니다. 아래 네 가지를 물어보면 방법마다 차이가 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>검색 칸에 커서를 둔 채 <b>정산 상태 바꾸기</b>를 눌러 보세요.
          <b>화면 전체</b>를 다시 그리면 검색 칸이 통째로 새로 만들어지기 때문에
          <b>커서가 사라지고 치던 글도 지워집니다</b>.
          데모는 초점이 어디로 갔는지와 입력칸의 값이 남았는지를 확인해서 적습니다.<br>
          반면 <b>바뀐 줄만</b> 다시 그리면 초점과 입력값이 그대로 남고,
          기다리는 동안 <b>그 줄만 흐려지므로</b> 나머지 줄은 계속 읽을 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "부분 로딩, 부분 갱신, 국소 갱신"),
    ("영어", "partial loading, partial update, granular loading"),
    ("같이 쓰는 말",
     "화면 일부만 서버에서 받아 바꾸는 방식은 <b>부분 렌더링</b>이라고 하고, "
     "React에서는 바뀌는 자리를 <b>서스펜스 경계</b>(Suspense boundary)로 묶습니다. "
     "버튼 안에서 도는 작은 표시는 <b>인라인 로더</b>(inline loader), "
     "그 버튼만 잠그는 것은 <b>버튼 잠금</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>스켈레톤</b> — <a href=\"skeleton.html\">스켈레톤</a>은 화면을 <b>처음 그릴 때</b> 자리를 잡아 두는 것이고, 부분 로딩은 이미 그린 화면의 일부를 바꾸는 것입니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"infinite.html\">무한 스크롤</a>은 목록 <b>뒤에 항목을 더 붙이는</b> 것이고, 이미 있는 줄을 바꾸지 않습니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 응답을 아예 <b>기다리지 않는</b> 방식이라 기다리는 자리를 표시하는 부분 로딩과 다릅니다."),
  ]),
  axes=WAIT2,
  oneline="<b>데이터가 바뀐 곳만 다시 그립니다.</b> 화면 전체를 갈아 끼우면 초점과 사용자가 치던 글까지 함께 사라집니다.",
  s4_title="상태", s4_hint="방식마다 가려지는 범위",
  states=states([
    (panel(R, -1, False, "", "평소", True), "평소", "모든 줄을 읽을 수 있습니다"),
    (panel(R, 0, False, "", "그 줄만 흐려졌다", True), "부분 로딩", "바뀌는 줄만 흐려지고 <b>나머지는 그대로</b> 보입니다"),
    (panel(R, -1, True, "", "화면이 통째로 가려졌다", False), "전체 스피너", "<b>바뀌지 않는 부분까지</b> 가립니다"),
    (one(txt('<span style="display:flex;gap:5px;align-items:center;font-size:8.5px">'
             '<span style="border:1px solid var(--accent);border-radius:4px;padding:2px 7px;color:var(--accent)">'
             '○ 저장 중…</span></span>'),
         "단추 안 표시", True, "그 단추만 기다린다", "152px"),
     "단추 안", "기다림을 표시하는 범위가 <b>가장 좁습니다</b>"),
    (panel(R, -1, False, "", "검색 칸이 새로 만들어졌다", False, "152px", ""),
     "전체를 갈아 끼움", "검색 칸이 새로 만들어져서 <b>치던 글이 사라집니다</b>"),
    (panel(R, 0, False, "", "aria-busy 로 알린다", True), "소리로 알림", "스크린 리더에 그 줄이 <b>바뀌는 중</b>이라고 알립니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바뀌는 곳만", "다시 그리기", "데이터가 바뀐 <b>그 줄</b>만 다시 그립니다"),
    ("흐리게", "그 줄만", "기다리는 줄만 흐리게 하므로 나머지는 <b>계속 읽을 수 있습니다</b>"),
    ("전체 교체", "위험", "전체를 다시 그리면 입력칸이 <b>새로 만들어집니다</b>"),
    ("초점", "날아감", "입력칸이 새로 만들어지면 초점과 치던 글이 <b>함께</b> 사라집니다"),
    ("단추 안", "가장 좁게", "누른 버튼만 기다리는 상태로 둡니다"),
    ("<code>aria-busy</code>", "소리로", "스크린 리더에 그 자리가 바뀌는 중임을 알립니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '다시 그린다'는 말이 <b>DOM을 새로 만드는 것</b>을 뜻하는지,
          <b>이미 있는 DOM을 고치는 것</b>을 뜻하는지에 따라 결과가 달라집니다.
          DOM을 새로 만들면 그 안의 입력칸과 스크롤 위치, 열려 있던 드롭다운이 모두 초기화되기 때문에,
          화면은 똑같아 보여도 <b>사용자는 하던 일을 잃습니다</b>.<br>
          그래서 목록을 다시 그릴 때도 <b>줄마다 열쇠</b>(key)를 주어
          바뀐 줄만 고치게 해야 합니다.
          React의 <code>key</code>와 Vue의 <code>:key</code>가 이 열쇠인데,
          열쇠로 순서 번호를 쓰면 정렬이 바뀔 때 <b>엉뚱한 줄을 고칩니다</b>.</p>''',
  do=ul([
    "목록을 다시 그릴 때. 줄마다 <b>바뀌지 않는 열쇠</b>를 줍니다",
    "줄 하나의 응답을 기다릴 때. 기다리는 동안 <b>그 줄만</b> 흐리게 합니다",
    "버튼 하나로 끝나는 일을 기다릴 때. 기다림을 <b>버튼 안에</b> 표시합니다",
  ]),
  dont=ul([
    "바뀐 줄은 하나인데 <b>목록 전체</b>를 다시 만들 때",
    "전체 스피너로 사용자가 <b>읽던 화면</b>까지 가릴 때",
    "열쇠로 <b>순서 번호</b>를 쓸 때. 정렬이 바뀌면 열쇠와 줄이 어긋납니다",
    "바뀌는 동안 <b>아무 표시도</b> 하지 않을 때",
  ]),
  instead='처음 그릴 때는 <a href="skeleton.html">스켈레톤</a>, 안 기다리게 하려면 <a href="optimistic.html">낙관적 UI</a>, 얼마나 남았는지는 <a href="progress.html">프로그레스 바</a>, 끝을 모르면 <a href="spinner.html">스피너</a>.',
  cases=cases([
    (panel(R, 0, False, "", "", True), "줄 상태 바꾸기", "상태를 바꾼 <b>그 줄만</b> 다시 그립니다"),
    (one(txt('<span style="display:flex;gap:5px;align-items:center;font-size:8.5px">'
             '<span style="border:1px solid var(--accent);border-radius:4px;padding:2px 7px;color:var(--accent)">○ 보내는 중…</span></span>'),
         "보내기", True, "", "150px"),
     "폼 보내기", "보내는 중이라는 표시를 <b>버튼 안</b>에 둡니다"),
    (panel(R, -1, False, "", "", True, "150px", "모란"), "검색 결과", "검색 칸은 그대로 두고 <b>결과 목록만</b> 바꿉니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  code_lede="다시 그리는 자리를 <b>좁게</b> 잡고, 그 자리에만 <code>aria-busy</code>를 붙입니다.",
  code='''<span class="c">&lt;!-- 바뀌는 자리에만 표시한다 --&gt;</span>
&lt;<span class="t">li</span> <span class="a">id</span>=<span class="s">"row-2411"</span> <span class="a">aria-busy</span>=<span class="s">"true"</span>&gt;
  모란상회 &lt;<span class="t">span</span>&gt;바꾸는 중…&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">li</span>&gt;

<span class="c">// 전체를 새로 만들지 않고 그 줄만 고친다</span>
<span class="t">const</span> row = document.getElementById(<span class="s">'row-2411'</span>);
row.setAttribute(<span class="s">'aria-busy'</span>, <span class="s">'true'</span>);
<span class="t">const</span> next = <span class="t">await</span> api.toggle(<span class="s">'2411'</span>);
row.querySelector(<span class="s">'.status'</span>).textContent = next.status;
row.removeAttribute(<span class="s">'aria-busy'</span>);

<span class="c">/* ✕ 목록을 통째로 다시 만들면 입력칸·스크롤 자리가 초기화된다 */</span>
list.innerHTML = rows.map(renderRow).join(<span class="s">''</span>);''',
  keys=kbd([
    ("<code>aria-busy</code>", "그 자리가 <b>바뀌는 중</b>임을 알립니다"),
    ("초점", "다시 그린 뒤 초점을 <b>원래 있던 자리</b>로 되돌려 줍니다"),
    ("<code>aria-live</code>", "결과만 짧게 알립니다. <b>진행 중</b>이라는 사실은 읽히지 않습니다"),
    ("단추 잠금", "<code>disabled</code>를 쓰면 버튼이 초점을 잃으므로, <code>aria-disabled</code>를 써서 <b>초점을 그대로 둡니다</b>"),
    ("열쇠", "<code>key</code>에 <b>순서 번호</b>를 쓰지 않습니다"),
    ("확인하는 법", "입력칸에 글을 치다가 갱신을 일으킨 뒤 <b>글이 남아 있는지</b> 봅니다"),
  ]),
  backend=rows([
    ("바뀐 것만 돌려준다", "줄 하나를 바꿨다면 응답에 <b>그 줄만</b> 담으면 되고, 목록 전체를 다시 보낼 필요는 없습니다."),
    ("열쇠", "응답에 줄의 <code>id</code>가 있어야 화면이 <b>어느 줄을 고칠지</b> 압니다."),
    ("버전", "응답에 <code>updated_at</code>이 있으면 이미 더 새 값을 받은 뒤에 <b>늦게 도착한 옛 응답</b>을 가려내 버릴 수 있습니다."),
  ]),
  plat_lede="부분 갱신은 <b>프레임워크가 처리하는</b> 영역이라서 플랫폼마다 부르는 이름이 제각각입니다.",
  plats=plats([
    ("웹", "부분 갱신",
     panel(R, 0, False, "", "", True, "110px"),
     "라이브러리마다 이름은 다르지만, <b>다시 그리는 자리를 좁게 잡는다</b>는 점은 같습니다."),
    ("iOS", "diffable 데이터 소스",
     '''              <div class="phone" role="img" aria-label="iOS 부분 갱신 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:8px;border-radius:2px;background:var(--accent-soft);opacity:.45"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "이전과 새 <b>스냅샷을 비교해</b> 바뀐 줄만 고칩니다. 줄마다 열쇠가 있어야 한다는 점은 웹과 같습니다."),
    ("안드로이드", "DiffUtil",
     '''              <div class="phone" role="img" aria-label="안드로이드 부분 갱신 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:8px;border-radius:2px;background:var(--accent-soft);opacity:.45"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<code>DiffUtil</code>이 바뀐 줄만 찾아 고칩니다. 반대로 <code>notifyDataSetChanged()</code>는 <b>목록 전체를 교체</b>합니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>전체를 다시 그리는 간단한 방법</b>과 <b>바뀐 것만 고치는 방법</b>을 함께 제공합니다. 안드로이드의 <code>notifyDataSetChanged()</code>가 전체를 다시 그리는 방법인데, 이 방법을 쓰면 스크롤 위치가 튑니다. 웹에서 <code>innerHTML</code>을 통째로 바꾸는 것도 마찬가지입니다. 지금 쓰는 방법이 <b>어느 쪽인지</b> 모르고 쓰면 입력값이나 스크롤 위치를 잃는 문제가 생기는데, 이 구분은 세 플랫폼에 똑같이 적용됩니다.",
  siblings=siblings("partialload"),
  related='''        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="spinner.html"><b>스피너</b><em>8부</em></a></li>''',
)
