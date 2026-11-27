# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 '누르면 어디론가 간다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">뒤로(기록) — history.back(), 들어온 길로</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">위로(상위) — 늘 부모 화면으로</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">링크로 바로 들어오면 기록에 앞이 없다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">이름을 적는다 — '‹ 주문 목록'</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">&lt;a href&gt; 로 둔다 — 새 탭으로도 열린다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">닫기와 섞지 않는다 — 뜻이 다르다</div>
                </div>
              </div>'''

D = dict(
  slug="backnav", ko="뒤로가기", en="Back · up navigation",
  desc="화면 안의 뒤로가기 단추. 기록을 되돌리는 '뒤로'와 상위로 가는 '위로'의 차이.",
  lede="같은 단추처럼 보이지만 둘입니다 — <b>들어온 길</b>로 되돌아가는 '뒤로'와 <b>늘 상위</b>로 가는 '위로'.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 화면이라도 <b>어떻게 들어왔는지</b>에 따라 '뒤로'가 데려가는 곳이 달라집니다.
          받은 링크로 바로 들어오면 기록에 앞 화면이 없어 <b>갈 데가 없습니다</b> —
          데모가 기록을 들고 있다가 그 경우를 짚어 줍니다.<br>
          <b>위로</b>는 다릅니다. 기록과 상관없이 늘 상위 화면으로 가서,
          링크로 들어온 사람에게도 갈 곳이 있습니다.
          둘을 섞으면 '뒤로를 눌렀는데 엉뚱한 데로 간다'가 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "뒤로가기, 뒤로 단추, 위로 가기, 상위로"),
    ("영어", "back, up navigation, back link, ancestor navigation"),
    ("같이 쓰는 말",
     "브라우저·OS 의 기록을 되감는 것이 <b>뒤로</b>(back), "
     "계층에서 부모로 올라가는 것이 <b>위로</b>(up)입니다. "
     "안드로이드가 이 둘을 <b>명시적으로 나눠</b> 지침에 적어 두었습니다 — "
     "시스템 백은 뒤로, 앱바 왼쪽의 ← 는 위로입니다."),
    ("자주 잘못 부름",
     "<b>닫기</b> — 닫기는 <b>그 부품만</b> 치웁니다. 화면을 안 바꿉니다.<br>"
     "<b>시스템 백</b> — <a href=\"systemback.html\">시스템 백</a>은 <b>OS 가 쥔</b> 동작이고 이건 화면 안의 단추입니다.<br>"
     "<b>취소</b> — 취소는 <b>하던 일을 무르는</b> 것이지 자리 이동이 아닙니다."),
  ]),
  axes=ax("뒤로가기"),
  oneline="<b>단추 하나에 하나만 맡기세요.</b> '뒤로'라고 적었으면 기록대로, '목록으로'라고 적었으면 늘 목록으로.",
  states=states([
    (bar("주문 목록", "주문 상세", "목록에서 눌러 들어왔다", True),
     "목록에서", "뒤로 = 위로, <b>둘이 같다</b>"),
    (bar("검색 결과", "주문 상세", "검색에서 눌러 들어왔다"),
     "검색에서", "뒤로는 <b>검색 결과</b>로"),
    (bar("", "주문 상세", "기록에 앞 화면이 없다", False, "152px", True),
     "링크로 바로", "<b>갈 데가 없다</b>"),
    (bar("주문 목록", "주문 상세", "기록과 상관없이 상위로", True),
     "위로", "<b>늘 같은 곳</b>으로"),
    (hist(["홈", "주문 목록", "주문 상세"], 2, "152px", "기록 세 칸", True),
     "기록", "뒤로는 <b>이 줄</b>을 되감는다"),
    (hist(["주문 상세"], 0, "152px", "기록 한 칸 — 되감을 것이 없다", False),
     "기록 한 칸", "링크·새 탭으로 들어온 경우"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤로(기록)", "<code>history.back()</code>", "<b>들어온 길</b>로"),
    ("위로(상위)", "부모 화면", "<b>늘 같은 곳</b>으로"),
    ("기록이 빈 경우", "링크로 들어옴", "뒤로는 <b>갈 데가 없다</b>"),
    ("이름을 적는다", "'‹ 주문 목록'", "어디로 가는지 <b>미리</b> 알린다"),
    ("<code>&lt;a href&gt;</code>", "링크로", "새 탭·마우스 가운데 버튼이 <b>그냥 된다</b>"),
    ("닫기와 구별", "뜻이 다름", "<b>섞으면</b> 둘 다 못 믿는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          실무에서 가장 안전한 선택은 <b>위로</b>입니다 —
          기록이 어떻든 <b>늘 같은 곳</b>으로 가고, 링크로 들어온 사람에게도 갈 곳이 있습니다.
          그리고 <b>어디로 가는지 이름을 적어 두면</b>('‹ 주문 목록')
          누르기 전에 알 수 있어 기대와 결과가 어긋나지 않습니다.<br>
          <code>history.back()</code> 을 쓸 거라면 <b>기록이 비었을 때의 길</b>을 꼭 정해 두세요 —
          <code>document.referrer</code> 가 우리 도메인이 아니면
          상위 화면으로 보내는 식입니다. 이걸 안 하면 아무 일도 안 일어나는 단추가 됩니다.</p>''',
  do=ul([
    "<b>어디로 가는지 이름</b>을 적기 — '‹ 주문 목록'",
    "<code>&lt;a href&gt;</code> 로 두기 — <b>새 탭</b>으로도 열린다",
    "기록이 비었을 때 갈 <b>기본 자리</b>를 정해 두기",
  ]),
  dont=ul([
    "<code>history.back()</code> 만 쓰고 <b>빈 기록</b>을 안 챙기기",
    "'뒤로'라고 적고 <b>상위로</b> 보내기 — 둘 중 하나만 한다",
    "닫기 자리에 뒤로를 두기 — <b>모달이 사라지는 줄</b> 안다",
    "폰에서 <b>시스템 백과 다른 곳</b>으로 보내기",
  ]),
  instead='OS 쪽 동작은 <a href="systemback.html">시스템 백</a>, 계층 전체를 보이려면 <a href="breadcrumb.html">브레드크럼</a>, 부품만 치우는 것은 <a href="modal.html">모달</a>의 닫기, 되돌리기는 <a href="destructive.html">위험한 동작</a>.',
  cases=cases([
    (bar("주문 목록", "주문 상세", "", True), "상세 화면", "<b>이름을 적는다</b>"),
    (bar("설정", "알림 설정", "", True), "설정 하위", "계층이 뚜렷하면 <b>위로</b>"),
    (one(txt('<span style="display:flex;align-items:center;gap:5px;font-size:8.5px">'
             '<span style="color:var(--fg-muted)">✕</span><span style="font-weight:700">새 주문</span></span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:4px">덮고 올라온 화면은 닫기다</span>'),
         "닫기", True, "", "150px"),
     "덮고 올라온 화면", "뒤로가 아니라 <b>닫기</b>"),
  ]),
  code_lede="링크로 두는 것이 거의 늘 맞습니다. 기록을 쓸 때만 빈 기록을 챙깁니다.",
  code='''<span class="c">&lt;!-- 거의 늘 이쪽 — 새 탭으로도 열리고, 기록이 비어도 간다 --&gt;</span>
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
    ("Tab · Enter", "링크다 — <b>따로 붙일 것이 없다</b>"),
    ("Alt + ←", "브라우저의 뒤로. <b>화면 안 단추와 같은 곳</b>으로 가야 덜 헷갈린다"),
    ("<code>aria-hidden</code>", "‹ 같은 기호는 안 읽게 하고 <b>'주문 목록'</b>만 읽힌다"),
    ("Esc", "뒤로가 아니라 <b>닫기</b>에 묶는다"),
    ("<code>rel=\"up\"</code>", "뜻을 적어 두는 표시. <b>동작은 안 바뀐다</b>"),
    ("확인하는 법", "새 탭에서 상세 주소를 <b>직접 열고</b> 단추를 눌러 본다"),
  ]),
  backend=rows([
    ("상위 주소를 같이", "응답에 <code>parent_url</code> 이나 <code>category_id</code> 가 있으면 <b>위로</b>를 만들 수 있습니다 — 없으면 화면이 짐작해야 합니다."),
    ("들어온 길", "<code>?from=search</code> 같은 표시를 붙여 두면 <b>돌아갈 곳</b>을 정확히 알 수 있습니다. 다만 주소가 지저분해집니다."),
    ("목록 상태", "되돌아갈 때 <b>쪽·필터·굴린 자리</b>를 살리려면 그 상태가 주소에 있어야 합니다."),
  ]),
  plat_lede="<b>안드로이드가 뒤로와 위로를 나눠</b> 둔 것이 이 항목의 출발점입니다.",
  plats=plats([
    ("웹", "링크 또는 history",
     bar("주문 목록", "주문 상세", "", True, "110px"),
     "브라우저의 뒤로가 이미 있어서, 화면 안 단추는 <b>위로</b>로 두는 쪽이 덜 겹칩니다."),
    ("iOS", "내비게이션 바 ‹",
     '''              <div class="phone" role="img" aria-label="iOS 뒤로 단추 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;top:24px;font-size:6px;color:var(--accent)">‹ 주문</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "왼쪽 위 ‹ 에 <b>앞 화면 이름</b>이 붙습니다. 가장자리를 밀어도 같은 동작입니다."),
    ("안드로이드", "Up ← + 시스템 백",
     '''              <div class="phone" role="img" aria-label="안드로이드 위로 단추 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;top:24px;font-size:7px;color:var(--fg)">←</div>
                <div style="position:absolute;left:5px;right:5px;top:36px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱바의 ← 는 <b>위로</b>, 시스템 백은 <b>뒤로</b>입니다. 둘이 다른 곳으로 가도 됩니다."),
  ]),
  plat_note="iOS 의 ‹ 에 <b>앞 화면 이름</b>이 붙는 것은 그대로 베낄 만합니다 — 누르기 전에 어디로 가는지 알 수 있어 기대와 결과가 어긋나지 않습니다. 안드로이드가 <b>둘을 나눠</b> 둔 것은 더 엄밀하지만, 웹에서는 브라우저 뒤로가 이미 '뒤로'를 맡고 있으니 <b>화면 안 단추는 위로</b>로 두는 쪽이 겹치지 않습니다.",
  siblings=siblings("backnav"),
  related='''        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="breadcrumb.html"><b>브레드크럼</b><em>7부</em></a></li>
        <li><a href="appbar.html"><b>앱바</b><em>7부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>''',
)
