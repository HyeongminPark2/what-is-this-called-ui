# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def stack(items, w="152px", note="", warn=False):
    es = ''.join('<span style="padding:3px 7px;border-radius:5px;font-size:9px;font-family:var(--mono);'
                 + ('background:var(--accent);color:#fff;font-weight:700' if top else
                    'background:var(--bg);border:1px solid var(--line);color:var(--fg-muted)')
                 + '">' + t + '</span>' for t, top in items)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:4px;flex-wrap:wrap">' + es + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:230px">''' + stack([("목록", False), ("상세", False), ("시트", True)], "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">열 때 history.pushState — 기록을 하나 쌓는다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">popstate — 뒤로가 눌렸다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">✕ 로 닫을 때는 history.back() — 기록을 되돌린다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;dialog&gt; 는 Esc 만 — 뒤로가기는 직접 잇는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">기록에 안 넣으면 뒤로가 앱을 나간다</div>
                </div>
              </div>'''

D = dict(
  slug="systemback", ko="시스템 백", en="System back",
  desc="OS가 주는 뒤로가기. 모달·시트를 기록에 넣어 뒤로가기로 닫히게 하는 법.",
  lede="폰에는 <b>OS가 주는 뒤로가기</b>가 있습니다. 사용자는 그걸로 <b>모달도 닫습니다</b>.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>기록에 넣기</b>를 끄고 시트를 연 뒤 <b>← 뒤로</b>를 눌러 보세요 —
          시트는 그대로 남고 <b>그 아래 화면이 사라집니다.</b> 한 번 더 누르면 앱을 나갑니다.<br>
          켜 두면 뒤로가기가 <b>시트만</b> 닫습니다. 기록 줄에서 무엇이 쌓이고 빠지는지 같이 보입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시스템 백, 뒤로가기, 뒤로 제스처"),
    ("영어", "system back, back navigation, predictive back"),
    ("같이 쓰는 말",
     "브라우저가 쌓아 두는 것이 <b>히스토리</b>(history)이고, 한 칸 쌓는 것이 "
     "<code>history.pushState</code>, 뒤로가 눌린 것을 받는 것이 <code>popstate</code>입니다. "
     "안드로이드 14부터는 뒤로 제스처 도중에 다음 화면을 미리 보여 주는 "
     "<b>프레딕티브 백</b>(predictive back)이 들어왔습니다."),
    ("자주 잘못 부름",
     "<b>브레드크럼</b> — <a href=\"../items/breadcrumb.html\">브레드크럼</a>은 '어디에 있나', 뒤로가기는 '<b>어떻게 왔나</b>'입니다.<br>"
     "<b>닫기</b> — 닫기는 그 부품만 치우고, 뒤로가기는 <b>기록을 하나 되돌립니다</b>. 결과가 같아 보여도 다릅니다.<br>"
     "<b>취소</b> — 취소는 <b>하던 일을 무르는</b> 것이라 뜻이 더 셉니다."),
  ]),
  axes=ax("시스템 백"),
  oneline="<b>화면을 덮는 것은 기록에 넣으세요.</b> 모달·시트·전체 화면 사진 보기 — 사용자는 전부 뒤로가기로 닫으려 합니다.",
  s4_title="기록과 화면", s4_hint="둘이 어긋나면 사고가 난다",
  states=states([
    (stack([("목록", True)], note="첫 화면"), "처음", "기록 하나. 여기서 뒤로 = <b>앱 나가기</b>"),
    (stack([("목록", False), ("상세", True)], note="화면을 하나 열었다"), "들어감", "기록 둘. 뒤로 = 목록으로"),
    (stack([("목록", False), ("상세", False), ("시트", True)], note="시트도 기록에 넣었다"), "시트 열림 ✓", "뒤로 = <b>시트만</b> 닫힌다"),
    (stack([("목록", False), ("상세", True)], note="뒤로 — 시트가 빠졌다"), "뒤로 누름", "<b>기대한 대로</b> 움직인다"),
    (stack([("목록", False), ("상세", True)], note="시트는 기록 밖 — 안 쌓였다", warn=True), "안 넣었을 때", "화면엔 시트가 있는데 <b>기록엔 없다</b>"),
    (stack([("목록", True)], note="뒤로 — 시트는 남고 뒤 화면이 사라졌다", warn=True), "그 상태로 뒤로", "<b>엉뚱한 것이 사라진다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("기록", "history stack", "OS·브라우저가 쌓아 둔다. <b>화면이 아니라 기록</b>을 되돌린다"),
    ("쌓기", "pushState", "덮는 것을 열 때 하나 쌓는다. 주소는 안 바꿔도 된다"),
    ("받기", "popstate", "뒤로가 눌렸다. <b>여기서 닫는다</b>"),
    ("✕ 로 닫을 때", "history.back()", "직접 닫지 말고 <b>기록을 되돌린다.</b> 안 그러면 기록이 쌓인 채 남는다"),
    ("<code>&lt;dialog&gt;</code>", "Esc 만 준다", "뒤로가기와는 <b>아무 상관이 없다.</b> 직접 이어 줘야 한다"),
    ("안 넣으면", "앱을 나간다", "쓰던 화면을 잃는다. <b>가장 싫어하는 사고</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>너무 많이 쌓는 것도 사고입니다.</b>
          <a href="filter.html">필터</a>를 누를 때마다 기록을 쌓으면,
          조건을 열 번 만진 사람은 뒤로가기를 <b>열 번</b> 눌러야 전 화면으로 갑니다.
          기준은 '<b>화면을 덮었나</b>'입니다 — 덮는 것(모달·시트·사진 보기)은 쌓고,
          같은 화면 안에서 값만 바뀌는 것(정렬·필터)은 <code>replaceState</code>로
          <b>기록을 갈아끼웁니다</b>.</p>''',
  do=ul([
    "<b>화면을 덮는 것</b> — 모달, 바텀시트, 전체 화면 사진",
    "여러 단계 폼 — 단계마다 쌓으면 <b>뒤로가 전 단계</b>가 된다",
    "<a href=\"../items/drawer.html\">드로어</a>로 연 메뉴",
  ]),
  dont=ul([
    "조건·정렬이 바뀔 때마다 쌓기 → <code>replaceState</code>",
    "뒤로가기를 <b>막기</b> — 사용자가 가장 싫어한다",
    "✕ 로 닫을 때 <b>직접 닫기</b> — 기록이 남아 뒤로가 한 번 헛돈다",
    "확인 없이 <b>저장 안 한 내용</b>을 날리기",
  ]),
  instead='같은 화면 안에서 값만 바뀌면 <code>replaceState</code>, 어디에 있는지 보여 주려면 <a href="../items/breadcrumb.html">브레드크럼</a>, 되돌릴 일이면 <a href="../items/toast.html">되돌리기</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--accent)">history.pushState({m:1}, '')</span>
                <span>dialog.showModal()</span>
              </div>''',
     "열 때", "<b>기록 먼저, 그다음</b> 연다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>onpopstate = () =&gt;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">dialog.close()</span></span>
              </div>''',
     "뒤로가 눌리면", "닫기만 한다. <b>기록은 이미 빠졌다</b>"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>closeBtn.onclick = () =&gt;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">history.back()</span></span>
              </div>''',
     "✕ 로 닫을 때", "직접 닫지 않는다. <b>한 길로 모은다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 기록의 계약서",
  code_lede="열 때 쌓고, <code>popstate</code>에서 닫고, ✕ 는 <code>back()</code>으로 모읍니다.",
  code='''<span class="k">function</span> openSheet() {
  history.pushState({ sheet: <span class="k">true</span> }, <span class="s">''</span>);   <span class="c">// 기록을 하나 쌓는다</span>
  dialog.showModal();
}

window.addEventListener(<span class="s">'popstate'</span>, () =&gt; {
  <span class="k">if</span> (dialog.open) dialog.close();      <span class="c">// 뒤로 = 닫기</span>
});

closeBtn.addEventListener(<span class="s">'click'</span>, () =&gt; history.back());  <span class="c">// 한 길로 모은다</span>

<span class="c">// Esc 로 닫혔을 때도 기록을 맞춰 준다</span>
dialog.addEventListener(<span class="s">'cancel'</span>, e =&gt; { e.preventDefault(); history.back(); });

<span class="c">// 조건이 바뀔 뿐이면 쌓지 말고 갈아끼운다</span>
history.replaceState(<span class="k">null</span>, <span class="s">''</span>, <span class="s">'?status=ok&amp;page=2'</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>와 뒤로를 <b>한 길로</b>", "<code>cancel</code> 이벤트를 막고 <code>back()</code>으로 보내면 둘이 어긋나지 않는다"),
    ("<code>pushState</code>는 주소를 안 바꿔도 된다", "두 번째 인자만 주고 세 번째를 빼면 주소는 그대로다"),
    ("<code>replaceState</code>와 가른다", "<b>덮는 것은 push, 값만 바뀌면 replace</b>"),
    ("저장 안 한 내용", "<code>beforeunload</code>는 뒤로가기엔 안 통할 수 있다. <b>확인 다이얼로그</b>를 직접 띄운다"),
    ("<code>&lt;dialog&gt;</code>", "Esc 는 공짜지만 <b>뒤로가기는 공짜가 아니다</b>"),
    ("초점", "뒤로로 닫혔을 때도 <b>부른 버튼</b>으로 초점을 되돌린다"),
  ]),
  backend=rows([
    ("주소에 담긴 것은 되살아난다", "뒤로가기로 돌아온 화면은 <b>주소로 다시 그려집니다.</b> 조건·쪽을 <a href=\"filter.html\">주소에 담아</a> 두면 공짜로 복원됩니다."),
    ("뒤로 캐시", "브라우저는 앞 화면을 통째로 얼려 뒀다 되살립니다(bfcache). <code>unload</code> 핸들러를 달면 <b>이 캐시가 꺼집니다</b>."),
    ("되살아난 화면은 낡았다", "뒤로로 돌아온 목록은 몇 분 전 데이터입니다. <code>pageshow</code>의 <code>persisted</code>를 보고 <b>다시 받을지</b> 정합니다."),
    ("POST 뒤에는", "저장 뒤 그 자리에 머물면 뒤로가기에서 재전송 경고가 뜹니다. <b>저장 뒤에는 다른 주소로</b> 보냅니다."),
  ]),
  plat_lede="<b>폰에만 있는 것</b>이라 PC 에서 시험하면 영영 안 보입니다.",
  plats=plats([
    ("웹", "history API",
     stack([("목록", False), ("상세", True)], "110px"),
     "브라우저 ← 가 곧 뒤로가기입니다. 폰 브라우저에서는 <b>OS 뒤로가기</b>도 같은 일을 합니다."),
    ("iOS", "가장자리 쓸기",
     '''              <div class="phone" role="img" aria-label="iOS 가장자리 쓸기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:5px;top:16px;font-size:7px;color:var(--accent)">‹ 정산</span>
                <span style="position:absolute;left:0;top:26px;bottom:0;width:6px;background:linear-gradient(90deg,rgba(47,109,246,.25),transparent)"></span></div></div>''',
     "<b>왼쪽 가장자리 쓸기</b>와 왼쪽 위 ‹ 가 같은 일을 합니다. 전용 버튼은 없습니다."),
    ("안드로이드", "뒤로 제스처 · 버튼",
     '''              <div class="phone" role="img" aria-label="안드로이드 뒤로 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:0;top:26px;bottom:0;width:5px;background:linear-gradient(90deg,rgba(47,109,246,.25),transparent)"></span>
                <span style="position:absolute;right:0;top:26px;bottom:0;width:5px;background:linear-gradient(270deg,rgba(47,109,246,.25),transparent)"></span></div></div>''',
     "<b>양쪽 가장자리 모두</b> 뒤로입니다. 모달을 기록에 안 넣으면 바로 앱이 꺼집니다."),
  ]),
  plat_note="PC 브라우저에서만 눌러 보면 이 사고는 <b>영영 안 보입니다.</b> ✕ 로만 닫아 보기 때문입니다. 폰에서 열어 뒤로가기를 한 번 눌러 보는 것이 이 항목의 유일한 시험법이고, 그 한 번으로 '모달이 안 닫히고 앱이 꺼진다'는 민원이 대부분 걸러집니다.",
  siblings=siblings("systemback"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>''',
)
