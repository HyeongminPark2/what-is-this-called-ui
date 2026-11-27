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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">열 때 history.pushState로 기록을 하나 쌓음</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">popstate는 뒤로가기가 눌렸다는 신호</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">✕로 닫을 때는 history.back()으로 기록을 되돌림</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;dialog&gt;는 Esc만 지원해 뒤로가기는 직접 연결</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">기록에 넣지 않으면 뒤로가기로 앱을 나감</div>
                </div>
              </div>'''

D = dict(
  slug="systemback", ko="시스템 백", en="System back",
  desc="OS가 제공하는 뒤로가기와, 모달이나 시트를 방문 기록에 넣어 뒤로가기로 닫히게 하는 법을 보여 주는 항목입니다.",
  lede="폰에는 앱과 상관없이 <b>OS가 제공하는 뒤로가기</b>가 있고, 사용자는 이 뒤로가기로 <b>모달도 닫으려고 합니다</b>.",
  axes_lede="PC와 폰의 차이는 기계 자체보다 화면을 쓰는 <b>전제</b>에 있습니다. 아래 네 가지를 물어보면 두 환경이 어디서 갈리는지 알 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>모달을 뒤로가기 기록에 넣기</b>를 끄고 시트를 연 뒤 <b>← 뒤로</b>를 눌러 보세요.
          시트는 그대로 남고 <b>그 아래 화면이 사라지며</b>, 한 번 더 누르면 앱을 나갑니다.<br>
          이 설정을 켜 두면 뒤로가기가 <b>시트만</b> 닫습니다. 아래 기록 줄에서는 무엇이 쌓이고 빠지는지 함께 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "시스템 백, 뒤로가기, 뒤로 제스처"),
    ("영어", "system back, back navigation, predictive back"),
    ("같이 쓰는 말",
     "브라우저가 방문한 화면을 쌓아 두는 목록을 <b>히스토리</b>(history)라고 합니다. 이 목록에 한 칸을 쌓는 함수가 "
     "<code>history.pushState</code>이고, 뒤로가기가 눌린 것을 알려 주는 이벤트가 <code>popstate</code>입니다. "
     "안드로이드 14부터는 뒤로 제스처를 하는 도중에 돌아갈 화면을 미리 보여 주는 "
     "<b>프레딕티브 백</b>(predictive back)이 들어왔습니다."),
    ("자주 잘못 부르는 이름",
     "<b>브레드크럼</b> — <a href=\"../items/breadcrumb.html\">브레드크럼</a>은 지금 '어디에 있는지'를 보여 주고, 뒤로가기는 '<b>어떻게 왔는지</b>'를 따라 되돌아갑니다.<br>"
     "<b>닫기</b> — 닫기는 그 부품만 화면에서 치우고, 뒤로가기는 <b>기록을 하나 되돌립니다</b>. 화면에 보이는 결과가 같아도 기록에 남는 상태가 다릅니다.<br>"
     "<b>취소</b> — 취소는 <b>하던 일을 무르는</b> 것이라 뒤로가기보다 뜻이 셉니다."),
  ]),
  axes=ax("시스템 백"),
  oneline="<b>화면을 덮는 것은 기록에 넣으세요.</b> 모달이나 시트, 전체 화면 사진 보기 같은 것을 사용자는 모두 뒤로가기로 닫으려 하기 때문입니다.",
  s4_title="뒤로가기 기록과 화면", s4_hint="기록과 화면이 어긋날 때 생기는 문제",
  do_title="뒤로가기 기록을 쌓아야 하는 경우",
  dont_title="뒤로가기 기록을 잘못 다루는 경우",
  instead_title="기록을 쌓는 대신 다른 방법이 맞는 경우",
  states=states([
    (stack([("목록", True)], note="첫 화면"), "첫 화면에 있을 때", "기록이 하나뿐이라서, 여기서 뒤로가기를 누르면 <b>앱을 나갑니다</b>"),
    (stack([("목록", False), ("상세", True)], note="화면을 하나 연 상태"), "상세 화면으로 들어갔을 때", "기록이 둘이 되어, 뒤로가기를 누르면 목록으로 돌아갑니다"),
    (stack([("목록", False), ("상세", False), ("시트", True)], note="시트도 기록에 넣은 상태"), "시트를 기록에 넣어 열었을 때 ✓", "뒤로가기를 누르면 <b>시트만</b> 닫힙니다"),
    (stack([("목록", False), ("상세", True)], note="뒤로가기로 시트가 빠짐"), "그 상태에서 뒤로가기를 눌렀을 때", "사용자가 <b>기대한 대로</b> 시트만 사라집니다"),
    (stack([("목록", False), ("상세", True)], note="시트가 기록에 쌓이지 않음", warn=True), "시트를 기록에 넣지 않았을 때", "화면에는 시트가 있는데 <b>기록에는 없습니다</b>"),
    (stack([("목록", True)], note="뒤로가기에 시트는 남고 뒤 화면이 사라짐", warn=True), "그 상태로 뒤로가기를 눌렀을 때", "시트 대신 그 아래 화면이 사라져서 <b>엉뚱한 것이 닫힙니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("기록", "history stack", "OS와 브라우저가 쌓아 둡니다. 뒤로가기는 <b>화면이 아니라 이 기록</b>을 되돌립니다"),
    ("기록 쌓기", "pushState", "화면을 덮는 것을 열 때 기록을 하나 쌓습니다. 주소는 바꾸지 않아도 됩니다"),
    ("뒤로가기 신호", "popstate", "뒤로가기가 눌렸다는 신호입니다. <b>이 이벤트에서 시트를 닫습니다</b>"),
    ("✕ 로 닫을 때", "history.back()", "시트를 직접 닫지 않고 <b>기록을 되돌립니다.</b> 직접 닫으면 쌓아 둔 기록이 그대로 남습니다"),
    ("<code>&lt;dialog&gt;</code>", "Esc만 지원", "Esc로 닫히는 기능만 있고 뒤로가기와는 <b>연결되어 있지 않습니다.</b> 뒤로가기로 닫히게 하려면 직접 연결해야 합니다"),
    ("기록에 넣지 않은 경우", "앱을 나감", "사용자가 쓰던 화면을 잃어버리는, <b>사용자가 가장 싫어하는 실수</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>기록을 너무 많이 쌓아도 문제가 생깁니다.</b>
          예를 들어 <a href="filter.html">필터</a>를 누를 때마다 기록을 쌓으면,
          조건을 열 번 바꾼 사용자는 뒤로가기를 <b>열 번</b> 눌러야 전 화면으로 돌아갈 수 있습니다.
          쌓을지 말지는 '<b>화면을 덮었는가</b>'로 가릅니다. 화면을 덮는 것(모달·시트·사진 보기)은 기록을 쌓고,
          같은 화면 안에서 값만 바뀌는 것(정렬·필터)은 <code>replaceState</code>로
          <b>지금 기록을 바꿔 씁니다</b>.</p>''',
  do=ul([
    "모달, 바텀시트, 전체 화면 사진처럼 <b>화면을 덮는 것</b>을 열 때",
    "여러 단계로 된 폼을 만들 때. 단계마다 기록을 쌓으면 <b>뒤로가기가 전 단계로</b> 돌아갑니다",
    "<a href=\"../items/drawer.html\">드로어</a>로 메뉴를 열 때",
  ]),
  dont=ul([
    "조건이나 정렬이 바뀔 때마다 기록을 쌓을 때. 이때는 <code>replaceState</code>를 씁니다",
    "뒤로가기를 <b>막을</b> 때. 사용자가 가장 싫어하는 동작입니다",
    "✕로 닫을 때 <b>시트를 직접 닫을</b> 때. 기록이 남아서 다음 뒤로가기가 한 번 아무 일도 하지 않습니다",
    "확인 없이 <b>저장하지 않은 내용</b>을 버릴 때",
  ]),
  instead='같은 화면 안에서 값만 바뀌면 <code>replaceState</code>를 쓰고, 어디에 있는지 보여 주려면 <a href="../items/breadcrumb.html">브레드크럼</a>, 방금 한 일을 무르게 하려면 <a href="../items/toast.html">되돌리기</a>를 씁니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--accent)">history.pushState({m:1}, '')</span>
                <span>dialog.showModal()</span>
              </div>''',
     "시트를 열 때", "<b>기록을 먼저 쌓고, 그다음에</b> 시트를 엽니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>onpopstate = () =&gt;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">dialog.close()</span></span>
              </div>''',
     "뒤로가기가 눌렸을 때", "시트를 닫기만 합니다. <b>기록은 이미 빠진 상태</b>입니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>closeBtn.onclick = () =&gt;</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">history.back()</span></span>
              </div>''',
     "✕ 버튼으로 닫을 때", "시트를 직접 닫지 않고 기록을 되돌려서, <b>닫는 경로를 뒤로가기 하나로 모읍니다</b>"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="열 때 기록을 쌓고 <code>popstate</code>에서 닫으며, ✕ 버튼도 <code>back()</code>을 불러 같은 경로로 닫습니다.",
  code='''<span class="k">function</span> openSheet() {
  history.pushState({ sheet: <span class="k">true</span> }, <span class="s">''</span>);   <span class="c">// 기록을 하나 쌓는다</span>
  dialog.showModal();
}

window.addEventListener(<span class="s">'popstate'</span>, () =&gt; {
  <span class="k">if</span> (dialog.open) dialog.close();      <span class="c">// 뒤로 = 닫기</span>
});

closeBtn.addEventListener(<span class="s">'click'</span>, () =&gt; history.back());  <span class="c">// 닫는 경로를 하나로 모은다</span>

<span class="c">// Esc 로 닫혔을 때도 기록을 맞춰 준다</span>
dialog.addEventListener(<span class="s">'cancel'</span>, e =&gt; { e.preventDefault(); history.back(); });

<span class="c">// 조건이 바뀔 뿐이면 쌓지 말고 갈아끼운다</span>
history.replaceState(<span class="k">null</span>, <span class="s">''</span>, <span class="s">'?status=ok&amp;page=2'</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>와 뒤로가기를 <b>같은 경로로</b> 닫기", "<code>cancel</code> 이벤트의 기본 동작을 막고 <code>back()</code>을 부르면, Esc와 뒤로가기가 같은 경로로 닫혀서 기록이 어긋나지 않습니다"),
    ("<code>pushState</code>로 주소를 바꾸지 않고 쌓기", "두 번째 인자만 주고 세 번째 인자를 빼면 주소는 그대로 남습니다"),
    ("<code>replaceState</code>와 구분해 쓰기", "<b>화면을 덮는 것은 push, 값만 바뀌는 것은 replace</b>로 처리합니다"),
    ("저장하지 않은 내용 지키기", "<code>beforeunload</code>는 뒤로가기에는 작동하지 않을 수 있으므로 <b>확인 다이얼로그</b>를 직접 띄웁니다"),
    ("<code>&lt;dialog&gt;</code>를 쓸 때", "Esc로 닫히는 기능은 따로 만들지 않아도 있지만, <b>뒤로가기로 닫히게 하려면 직접 만들어야 합니다</b>"),
    ("포커스 되돌리기", "뒤로가기로 닫혔을 때도 <b>시트를 연 버튼</b>으로 포커스를 되돌립니다"),
  ]),
  backend=rows([
    ("주소에 담아 둔 조건은 그대로 복원됨", "뒤로가기로 돌아온 화면은 <b>주소를 보고 다시 그립니다.</b> 그래서 조건과 쪽 번호를 <a href=\"filter.html\">주소에 담아</a> 두면 따로 저장하지 않아도 그대로 복원됩니다."),
    ("뒤로가기 캐시(bfcache)", "브라우저는 떠난 화면을 메모리에 통째로 보관해 두었다가 뒤로가기를 누르면 그대로 다시 보여 줍니다(bfcache). 그런데 <code>unload</code> 핸들러를 달면 <b>이 캐시를 쓰지 않습니다</b>."),
    ("캐시에서 되살린 화면의 오래된 데이터", "bfcache에서 되살아난 목록은 몇 분 전 데이터를 보여 줍니다. <code>pageshow</code> 이벤트의 <code>persisted</code> 값을 보고 데이터를 <b>다시 받을지</b> 정합니다."),
    ("POST로 저장한 뒤의 이동", "폼을 POST로 저장한 뒤 그 화면에 머물면, 뒤로가기를 눌렀을 때 양식을 다시 보낼지 묻는 경고가 뜹니다. 그래서 <b>저장한 뒤에는 다른 주소로</b> 이동시킵니다."),
  ]),
  plat_lede="OS 뒤로가기는 <b>폰에만 있어서</b> PC에서만 시험하면 문제를 발견할 수 없습니다.",
  plats=plats([
    ("웹", "history API",
     stack([("목록", False), ("상세", True)], "110px"),
     "브라우저의 ← 버튼이 뒤로가기입니다. 폰 브라우저에서는 <b>OS 뒤로가기</b>도 같은 일을 합니다."),
    ("iOS", "가장자리 쓸기",
     '''              <div class="phone" role="img" aria-label="iOS 가장자리 쓸기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:5px;top:16px;font-size:7px;color:var(--accent)">‹ 정산</span>
                <span style="position:absolute;left:0;top:26px;bottom:0;width:6px;background:linear-gradient(90deg,rgba(47,109,246,.25),transparent)"></span></div></div>''',
     "<b>왼쪽 가장자리에서 쓸기</b>와 왼쪽 위 ‹ 버튼이 같은 일을 합니다. 뒤로가기 전용 버튼은 없습니다."),
    ("안드로이드", "뒤로 제스처 · 버튼",
     '''              <div class="phone" role="img" aria-label="안드로이드 뒤로 제스처 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:0;top:26px;bottom:0;width:5px;background:linear-gradient(90deg,rgba(47,109,246,.25),transparent)"></span>
                <span style="position:absolute;right:0;top:26px;bottom:0;width:5px;background:linear-gradient(270deg,rgba(47,109,246,.25),transparent)"></span></div></div>''',
     "화면 <b>양쪽 가장자리 어디서든</b> 쓸면 뒤로가기가 됩니다. 모달을 기록에 넣지 않으면 뒤로가기 한 번에 앱이 바로 꺼질 수 있습니다."),
  ]),
  plat_note="PC 브라우저에서는 모달을 ✕로만 닫아 보기 때문에, 이 문제를 <b>발견할 수 없습니다.</b> 폰에서 모달을 열고 뒤로가기를 한 번 눌러 보는 것이 이 문제를 확인하는 유일한 방법이고, 그 한 번의 확인으로 '모달이 안 닫히고 앱이 꺼진다'는 민원을 대부분 막을 수 있습니다.",
  siblings=siblings("systemback"),
  related='''        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="../items/breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>''',
)
