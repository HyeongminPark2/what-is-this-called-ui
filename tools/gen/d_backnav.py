# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def bar(label, title, note="", ok=None, w="152px", dead=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    btn = ('<span style="font-size:8.5px;color:' + ('var(--fg-muted)' if dead else 'var(--accent)') + '">‹ ' + label + '</span>') if label else ''
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            '<span style="display:flex;align-items:center;gap:6px;padding:5px 7px;border-bottom:1px solid var(--line)">'
            + btn + '<span style="font-size:8.5px;font-weight:700">' + title + '</span></span>'
            '<span style="display:block;padding:6px 7px;font-size:8px;color:var(--fg-muted)">주문번호 2411-0042</span>'
            '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def hist(items, cur, w="152px", note="", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for i, n in enumerate(items):
        st = ('border-color:var(--accent);color:var(--accent)' if i == cur else 'border-color:var(--line);color:var(--fg-muted)')
        out.append('<span style="font-family:var(--mono);font-size:7.5px;border:1px solid ' + st +
                   ';border-radius:999px;padding:1px 6px">' + n + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:3px;flex-wrap:wrap;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">뒤로(기록)는 history.back()으로 왔던 길로</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">위로(상위)는 늘 부모 화면으로 감</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">링크로 바로 들어오면 기록에 앞 화면이 없음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">'‹ 주문 목록'처럼 이름을 적음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">&lt;a href&gt;로 두면 새 탭으로도 열림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">뜻이 다른 닫기와 섞지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="backnav", ko="뒤로가기", en="Back · up navigation",
  desc="화면 안에 두는 뒤로가기 단추를 다루고, 방문 기록을 되돌리는 '뒤로'와 상위 화면으로 가는 '위로'가 어떻게 다른지 보여 주는 항목입니다.",
  lede="뒤로가기 단추는 겉보기에는 하나지만 실제로는 두 가지입니다. 하나는 <b>들어온 길</b>을 따라 되돌아가는 '뒤로'이고, 다른 하나는 어디서 들어왔든 <b>늘 상위 화면</b>으로 가는 '위로'입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 화면이라도 <b>어떻게 들어왔는지</b>에 따라 '뒤로'를 눌렀을 때 가는 곳이 달라집니다.
          받은 링크로 바로 들어오면 방문 기록에 앞 화면이 없어서 <b>돌아갈 곳이 없습니다</b>.
          데모는 방문 기록을 따로 저장해 두었다가 이런 경우를 표시해 줍니다.<br>
          반면 <b>위로</b>는 방문 기록과 상관없이 늘 상위 화면으로 가기 때문에,
          링크로 들어온 사람도 갈 곳이 있습니다.
          두 동작을 섞어 쓰면 사용자는 뒤로를 눌렀는데 예상과 다른 화면에 도착하게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "뒤로가기, 뒤로 단추, 위로 가기, 상위로"),
    ("영어", "back, up navigation, back link, ancestor navigation"),
    ("같이 쓰는 말",
     "브라우저나 OS의 방문 기록을 한 칸 되돌리는 것은 <b>뒤로</b>(back), "
     "계층에서 부모 화면으로 올라가는 것은 <b>위로</b>(up)라고 합니다. "
     "안드로이드는 이 둘을 지침에 <b>명시적으로 나눠</b> 적어 두었는데, "
     "시스템 백이 뒤로이고 앱바 왼쪽의 ←가 위로입니다."),
    ("자주 잘못 부르는 이름",
     "<b>닫기</b> — 닫기는 모달처럼 위에 뜬 <b>그 부품만</b> 없애고, 아래 화면은 바꾸지 않습니다.<br>"
     "<b>시스템 백</b> — <a href=\"systemback.html\">시스템 백</a>은 <b>OS가 처리하는</b> 동작이고, 뒤로가기는 화면 안에 둔 단추입니다.<br>"
     "<b>취소</b> — 취소는 화면을 옮기는 것이 아니라 <b>하던 일을 없던 일로 되돌리는</b> 동작입니다."),
  ]),
  states=states([
    (bar("주문 목록", "주문 상세", "목록에서 눌러 들어옴", True),
     "목록에서 들어왔을 때", "목록에서 들어왔으면 뒤로와 위로가 <b>같은 곳으로 갑니다</b>"),
    (bar("검색 결과", "주문 상세", "검색에서 눌러 들어옴"),
     "검색에서 들어왔을 때", "검색에서 들어왔으면 뒤로는 <b>검색 결과</b>로 갑니다"),
    (bar("", "주문 상세", "기록에 앞 화면이 없음", False, "152px", True),
     "링크로 바로 들어왔을 때", "방문 기록에 앞 화면이 없어서 뒤로는 <b>갈 곳이 없습니다</b>"),
    (bar("주문 목록", "주문 상세", "기록과 상관없이 상위로", True),
     "위로 단추를 둘 때", "어디서 들어왔든 <b>늘 같은 곳</b>으로 갑니다"),
    (hist(["홈", "주문 목록", "주문 상세"], 2, "152px", "기록 세 칸", True),
     "방문 기록이 쌓인 모습", "뒤로는 <b>이 방문 기록</b>을 한 칸씩 되돌립니다"),
    (hist(["주문 상세"], 0, "152px", "기록이 한 칸뿐이라 돌아갈 곳 없음", False),
     "기록이 한 칸뿐일 때", "링크나 새 탭으로 들어오면 기록이 한 칸뿐입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤로(기록)", "<code>history.back()</code>", "<b>들어온 길</b>을 따라 되돌아갑니다"),
    ("위로(상위)", "부모 화면", "어디서 들어왔든 <b>늘 같은 곳</b>으로 갑니다"),
    ("기록이 빈 경우", "링크로 들어옴", "뒤로를 눌러도 <b>갈 곳이 없습니다</b>"),
    ("이름 적기", "'‹ 주문 목록'", "누르기 전에 어디로 가는지 <b>미리</b> 알려 줍니다"),
    ("<code>&lt;a href&gt;</code>", "링크로 두기", "새 탭으로 열기와 마우스 가운데 버튼 클릭을 <b>따로 구현하지 않아도</b> 그대로 쓸 수 있습니다"),
    ("닫기와 구별", "뜻이 다름", "두 동작을 <b>섞어 쓰면</b> 사용자는 어느 단추가 무엇을 할지 예측할 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          실무에서 가장 안전한 선택은 <b>위로</b>입니다.
          방문 기록이 어떻든 <b>늘 같은 곳</b>으로 가고, 링크로 들어온 사람에게도 갈 곳이 있기 때문입니다.
          여기에 '‹ 주문 목록'처럼 <b>어디로 가는지 이름을 적어 두면</b>
          사용자가 누르기 전에 도착할 곳을 알 수 있어서 예상과 결과가 어긋나지 않습니다.<br>
          <code>history.back()</code>을 쓸 거라면 <b>방문 기록이 비었을 때 갈 곳</b>을 꼭 정해 두세요.
          예를 들어 <code>document.referrer</code>가 우리 도메인이 아니면
          상위 화면으로 보내는 식입니다. 이 처리를 빠뜨리면 눌러도 아무 일도 일어나지 않는 단추가 됩니다.</p>''',
  do=ul([
    "'‹ 주문 목록'처럼 <b>어디로 가는지 이름</b>을 적을 때",
    "<code>&lt;a href&gt;</code>로 둘 때. <b>새 탭</b>으로도 열 수 있습니다",
    "방문 기록이 비었을 때 갈 <b>기본 화면</b>을 정해 둘 때",
  ]),
  dont=ul([
    "<code>history.back()</code>만 쓰고 <b>방문 기록이 빈 경우</b>를 챙기지 않을 때",
    "'뒤로'라고 적어 두고 <b>상위 화면으로</b> 보낼 때. 단추 하나는 두 동작 중 하나만 합니다",
    "닫기 자리에 뒤로를 둘 때. 사용자는 누르면 <b>모달만 사라질 거라고</b> 생각합니다",
    "폰에서 <b>시스템 백과 다른 곳</b>으로 보낼 때",
  ]),
  instead='OS가 처리하는 뒤로 동작은 <a href="systemback.html">시스템 백</a> 항목에서 다루고, 계층 전체를 보여 주려면 <a href="breadcrumb.html">브레드크럼</a>을 씁니다. 위에 뜬 부품만 치우려면 <a href="modal.html">모달</a>의 닫기 단추를 두고, 하던 일을 되돌리는 방법은 <a href="destructive.html">위험한 동작</a> 항목에서 다룹니다.',
  cases=cases([
    (bar("주문 목록", "주문 상세", "", True), "상세 화면에서 목록으로 돌아가기", "돌아갈 화면의 <b>이름을 적습니다</b>"),
    (bar("설정", "알림 설정", "", True), "설정 하위 화면에서 위로 가기", "계층이 뚜렷하면 <b>위로</b>를 씁니다"),
    (one(txt('<span style="display:flex;align-items:center;gap:5px;font-size:8.5px">'
             '<span style="color:var(--fg-muted)">✕</span><span style="font-weight:700">새 주문</span></span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:4px">덮고 올라온 화면에는 닫기</span>'),
         "닫기", True, "", "150px"),
     "덮고 올라온 화면 닫기", "아래 화면을 덮고 올라온 화면에는 뒤로가 아니라 <b>닫기</b>를 둡니다"),
  ]),
  code_lede="대부분은 링크로 두는 것이 맞습니다. <code>history.back()</code>으로 방문 기록을 쓸 때만 기록이 빈 경우를 따로 처리합니다.",
  code='''<span class="c">&lt;!-- 대부분 이 방식이 맞다. 새 탭으로도 열리고, 기록이 비어도 간다 --&gt;</span>
&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"backlink"</span> <span class="a">href</span>=<span class="s">"/orders"</span>&gt;
  &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;‹&lt;/<span class="t">span</span>&gt; 주문 목록
&lt;/<span class="t">a</span>&gt;

<span class="c">// 기록을 쓸 거라면 빈 기록일 때 갈 곳을 정해 둔다</span>
<span class="t">function</span> goBack() {
  <span class="t">const</span> sameSite = document.referrer.startsWith(location.origin);
  <span class="t">if</span> (history.length &gt; <span class="a">1</span> &amp;&amp; sameSite) history.back();
  <span class="t">else</span> location.href = <span class="s">'/orders'</span>;   <span class="c">// 상위 화면</span>
}''',
  keys=kbd([
    ("Tab · Enter", "평범한 링크이므로 키보드 조작을 위해 <b>따로 붙일 것이 없습니다</b>"),
    ("Alt + ←", "브라우저의 뒤로입니다. <b>화면 안 단추와 같은 곳</b>으로 가야 사용자가 덜 헷갈립니다"),
    ("<code>aria-hidden</code>", "‹ 같은 기호는 읽지 않게 하고 <b>'주문 목록'</b>만 읽게 합니다"),
    ("Esc", "뒤로가 아니라 <b>닫기</b> 동작에 연결합니다"),
    ("<code>rel=\"up\"</code>", "링크의 뜻을 적어 두는 표시일 뿐이라서 <b>동작은 바뀌지 않습니다</b>"),
    ("제대로 됐는지 확인하는 방법", "새 탭에서 상세 화면 주소를 <b>직접 연 뒤</b> 단추를 눌러 봅니다"),
  ]),
  backend=rows([
    ("상위 주소를 응답에 함께 담기", "응답에 <code>parent_url</code>이나 <code>category_id</code>가 있으면 화면이 <b>위로</b> 단추를 만들 수 있습니다. 이 값이 없으면 화면이 상위 화면을 짐작해야 합니다."),
    ("들어온 길을 주소에 남기기", "주소에 <code>?from=search</code> 같은 표시를 붙여 두면 <b>돌아갈 곳</b>을 정확히 알 수 있습니다. 다만 그만큼 주소가 길고 복잡해집니다."),
    ("돌아갈 목록의 상태 되살리기", "목록으로 되돌아갈 때 <b>쪽 번호와 필터, 스크롤 위치</b>를 되살리려면 이 상태가 주소에 들어 있어야 합니다."),
  ]),
  plat_lede="이 항목은 <b>안드로이드가 뒤로와 위로를 나눠</b> 둔 데서 출발합니다.",
  plats=plats([
    ("웹", "링크 또는 history",
     bar("주문 목록", "주문 상세", "", True, "110px"),
     "브라우저에 이미 뒤로 버튼이 있으므로, 화면 안 단추는 <b>위로</b>로 두는 편이 역할이 덜 겹칩니다."),
    ("iOS", "내비게이션 바 ‹",
     '''              <div class="phone" role="img" aria-label="iOS 뒤로 단추 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;top:24px;font-size:6px;color:var(--accent)">‹ 주문</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "왼쪽 위 ‹ 옆에 <b>앞 화면 이름</b>이 붙습니다. 화면 왼쪽 가장자리에서 밀어도 같은 동작을 합니다."),
    ("안드로이드", "Up ←와 시스템 백",
     '''              <div class="phone" role="img" aria-label="안드로이드 위로 단추 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;top:24px;font-size:7px;color:var(--fg)">←</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱바의 ←는 <b>위로</b>, 시스템 백은 <b>뒤로</b>이므로 둘이 서로 다른 곳으로 가도 됩니다."),
  ]),
  plat_note="iOS처럼 ‹ 옆에 <b>앞 화면 이름</b>을 붙이는 방식은 웹에서도 그대로 따라 할 만합니다. 누르기 전에 어디로 가는지 알 수 있어서 예상과 결과가 어긋나지 않기 때문입니다. 안드로이드처럼 <b>뒤로와 위로를 나누는</b> 방식은 더 엄밀하지만, 웹에서는 브라우저의 뒤로 버튼이 이미 '뒤로'를 맡고 있으므로 <b>화면 안 단추는 위로</b>로 두는 편이 역할이 겹치지 않습니다.",
  siblings=siblings("backnav"),
  related='''        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="appbar.html"><b>앱바</b><em>7부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
