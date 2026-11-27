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
  desc="화면 전체가 아니라 바뀌는 곳만 다시 그리는 방식. 초점과 입력값을 지키는 법.",
  lede="바뀌는 것은 한 줄인데 <b>화면 전체를 다시 그리면</b>, 치던 글과 커서가 함께 날아갑니다.",
  axes_lede="기다림을 보여 주는 방법들입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>검색 칸에 커서를 둔 채 <b>정산 상태 바꾸기</b>를 눌러 보세요.
          <b>화면 전체</b>를 다시 그리면 그 칸이 통째로 새로 만들어져서
          <b>커서가 날아가고 치던 글도 사라집니다</b> —
          데모가 초점이 어디로 갔는지와 입력칸의 값이 남았는지를 재서 적습니다.<br>
          <b>바뀐 줄만</b> 다시 그리면 초점도 값도 그대로이고,
          기다리는 동안 <b>그 줄만 흐려져</b> 나머지는 읽을 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "부분 로딩, 부분 갱신, 국소 갱신"),
    ("영어", "partial loading, partial update, granular loading"),
    ("같이 쓰는 말",
     "화면 일부만 서버에서 받아 바꾸는 방식을 <b>부분 렌더링</b>이라 하고, "
     "React 쪽에서는 바뀌는 자리를 <b>서스펜스 경계</b>(Suspense boundary)로 묶습니다. "
     "단추 안에서 도는 작은 표시는 <b>인라인 로더</b>(inline loader), "
     "그 단추만 잠그는 것은 <b>버튼 잠금</b>입니다."),
    ("자주 잘못 부름",
     "<b>스켈레톤</b> — <a href=\"skeleton.html\">스켈레톤</a>은 <b>처음 그릴 때</b> 자리를 잡아 둡니다.<br>"
     "<b>무한 스크롤</b> — <a href=\"infinite.html\">무한 스크롤</a>은 <b>뒤에 더 붙이는</b> 것입니다.<br>"
     "<b>낙관적 UI</b> — <a href=\"optimistic.html\">낙관적 UI</a>는 아예 <b>안 기다리는</b> 쪽입니다."),
  ]),
  axes=WAIT2,
  oneline="<b>바뀌는 곳만 다시 그리세요.</b> 전체를 갈아 끼우면 초점과 치던 글이 같이 날아갑니다.",
  s4_title="상태", s4_hint="무엇이 가려지는지가 다르다",
  states=states([
    (panel(R, -1, False, "", "평소", True), "평소", "다 읽을 수 있다"),
    (panel(R, 0, False, "", "그 줄만 흐려졌다", True), "부분 로딩", "<b>나머지는 그대로</b>"),
    (panel(R, -1, True, "", "화면이 통째로 가려졌다", False), "전체 스피너", "<b>멀쩡한 화면까지</b> 가린다"),
    (one(txt('<span style="display:flex;gap:5px;align-items:center;font-size:8.5px">'
             '<span style="border:1px solid var(--accent);border-radius:4px;padding:2px 7px;color:var(--accent)">'
             '○ 저장 중…</span></span>'),
         "단추 안 표시", True, "그 단추만 기다린다", "152px"),
     "단추 안", "<b>가장 좁은</b> 범위"),
    (panel(R, -1, False, "", "검색 칸이 새로 만들어졌다", False, "152px", ""),
     "전체를 갈아 끼움", "<b>치던 글이 사라졌다</b>"),
    (panel(R, 0, False, "", "aria-busy 로 알린다", True), "소리로 알림", "<b>바뀌는 중</b>임을 전한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바뀌는 곳만", "다시 그리기", "<b>그 줄</b>만"),
    ("흐리게", "그 줄만", "나머지는 <b>읽을 수 있다</b>"),
    ("전체 교체", "위험", "입력칸이 <b>새로 만들어진다</b>"),
    ("초점", "날아감", "치던 글도 <b>함께</b>"),
    ("단추 안", "가장 좁게", "그 단추만 기다린다"),
    ("<code>aria-busy</code>", "소리로", "바뀌는 중임을 알린다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '다시 그린다'가 <b>DOM 을 새로 만드는 것</b>인지
          <b>있는 것을 고치는 것</b>인지가 갈림길입니다.
          새로 만들면 그 안의 입력칸·스크롤 자리·열린 드롭다운이 전부 초기화됩니다 —
          화면은 똑같아 보여도 <b>쓰던 사람은 하던 일을 잃습니다</b>.<br>
          그래서 목록을 다시 그릴 때도 <b>줄마다 열쇠</b>를 주어
          바뀐 줄만 고치게 해야 합니다.
          React 의 <code>key</code>, Vue 의 <code>:key</code> 가 바로 그 열쇠인데,
          순서 번호를 쓰면 정렬이 바뀔 때 <b>엉뚱한 줄을 고칩니다</b>.</p>''',
  do=ul([
    "줄마다 <b>안 바뀌는 열쇠</b>를 주기",
    "기다리는 동안 <b>그 줄만</b> 흐리게 하기",
    "단추 하나로 끝나는 일은 <b>단추 안에</b> 표시하기",
  ]),
  dont=ul([
    "바뀐 줄 하나 때문에 <b>목록 전체</b>를 다시 만들기",
    "전체 스피너로 <b>읽던 화면</b>까지 가리기",
    "열쇠로 <b>순서 번호</b> 쓰기 — 정렬이 바뀌면 어긋난다",
    "바뀌는 동안 <b>아무 표시도</b> 안 하기",
  ]),
  instead='처음 그릴 때는 <a href="skeleton.html">스켈레톤</a>, 안 기다리게 하려면 <a href="optimistic.html">낙관적 UI</a>, 얼마나 남았는지는 <a href="progress.html">프로그레스 바</a>, 끝을 모르면 <a href="spinner.html">스피너</a>.',
  cases=cases([
    (panel(R, 0, False, "", "", True), "줄 상태 바꾸기", "<b>그 줄만</b>"),
    (one(txt('<span style="display:flex;gap:5px;align-items:center;font-size:8.5px">'
             '<span style="border:1px solid var(--accent);border-radius:4px;padding:2px 7px;color:var(--accent)">○ 보내는 중…</span></span>'),
         "보내기", True, "", "150px"),
     "폼 보내기", "<b>단추 안</b>에"),
    (panel(R, -1, False, "", "", True, "150px", "모란"), "검색 결과", "<b>목록만</b> 바꾼다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 갱신의 계약서",
  code_lede="바꾸는 자리를 <b>좁게</b> 잡고, 그 자리에만 <code>aria-busy</code> 를 붙입니다.",
  code='''<span class="c">&lt;!-- 바뀌는 자리에만 표시한다 --&gt;</span>
&lt;<span class="t">li</span> <span class="a">id</span>=<span class="s">"row-2411"</span> <span class="a">aria-busy</span>=<span class="s">"true"</span>&gt;
  모란상회 &lt;<span class="t">span</span>&gt;바꾸는 중…&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">li</span>&gt;

<span class="c">// 전체를 새로 만들지 않는다 — 그 줄만 고친다</span>
<span class="t">const</span> row = document.getElementById(<span class="s">'row-2411'</span>);
row.setAttribute(<span class="s">'aria-busy'</span>, <span class="s">'true'</span>);
<span class="t">const</span> next = <span class="t">await</span> api.toggle(<span class="s">'2411'</span>);
row.querySelector(<span class="s">'.status'</span>).textContent = next.status;
row.removeAttribute(<span class="s">'aria-busy'</span>);

<span class="c">/* ✕ 목록을 통째로 다시 만들면 입력칸·스크롤 자리가 초기화된다 */</span>
list.innerHTML = rows.map(renderRow).join(<span class="s">''</span>);''',
  keys=kbd([
    ("<code>aria-busy</code>", "그 자리가 <b>바뀌는 중</b>임을 알린다"),
    ("초점", "다시 그린 뒤 <b>있던 자리</b>로 되돌려 준다"),
    ("<code>aria-live</code>", "결과만 짧게 알린다 — <b>진행 중</b>은 안 읽힌다"),
    ("단추 잠금", "<code>disabled</code> 보다 <code>aria-disabled</code> 가 <b>초점을 지킨다</b>"),
    ("열쇠", "<code>key</code> 에 <b>순서 번호</b>를 쓰지 않는다"),
    ("확인하는 법", "입력칸에 글을 치다가 갱신을 일으켜 <b>글이 남는지</b> 본다"),
  ]),
  backend=rows([
    ("바뀐 것만 돌려준다", "줄 하나를 바꿨으면 <b>그 줄만</b> 응답에 담으면 됩니다 — 목록 전체를 다시 줄 필요가 없습니다."),
    ("열쇠", "줄의 <code>id</code> 가 있어야 화면이 <b>어디를 고칠지</b> 압니다."),
    ("버전", "<code>updated_at</code> 이 있으면 <b>늦게 온 응답</b>을 버릴 수 있습니다."),
  ]),
  plat_lede="<b>프레임워크가 다루는</b> 영역이라 이름이 제각각입니다.",
  plats=plats([
    ("웹", "부분 갱신",
     panel(R, 0, False, "", "", True, "110px"),
     "라이브러리마다 이름이 다릅니다 — 공통점은 <b>바뀌는 자리를 좁게 잡는</b> 것입니다."),
    ("iOS", "diffable 데이터 소스",
     '''              <div class="phone" role="img" aria-label="iOS 부분 갱신 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:8px;border-radius:2px;background:var(--accent-soft);opacity:.45"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>스냅샷을 견줘</b> 바뀐 줄만 고칩니다 — 열쇠가 있어야 한다는 점이 같습니다."),
    ("안드로이드", "DiffUtil",
     '''              <div class="phone" role="img" aria-label="안드로이드 부분 갱신 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:8px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:8px;border-radius:2px;background:var(--accent-soft);opacity:.45"></div>
                <div style="position:absolute;left:5px;right:5px;top:50px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<code>DiffUtil</code> 이 같은 일을 합니다. <code>notifyDataSetChanged()</code> 가 <b>전체 교체</b>입니다."),
  ]),
  plat_note="세 플랫폼이 모두 <b>'전체를 다시 그리는 쉬운 길'</b>과 <b>'바뀐 것만 고치는 바른 길'</b>을 같이 제공합니다 — 안드로이드의 <code>notifyDataSetChanged()</code> 가 딱 그 쉬운 길이고, 쓰면 스크롤 자리가 튑니다. 웹의 <code>innerHTML</code> 교체도 똑같습니다. <b>어느 쪽이 기본인지</b>를 모르고 쓰면 사고가 나는 자리라, 한 번 알아 두면 셋 다 통합니다.",
  siblings=siblings("partialload"),
  related='''        <li><a href="skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="spinner.html"><b>스피너</b><em>8부</em></a></li>''',
)
