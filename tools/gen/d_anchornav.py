# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 누르면 다른 곳으로 옮겨 갑니다. 아래 네 가지로 서로 가릅니다."

def toc(items, w="152px", note="", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for name, on in items:
        st = ('border-left:2px solid var(--accent);background:var(--accent-soft);color:var(--accent);'
              if on else 'border-left:2px solid transparent;color:var(--fg-muted);')
        out.append('<span style="display:block;padding:2px 6px;font-size:8.5px;' + st + '">' + name + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:1px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:5px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">&lt;nav aria-label="이 문서 안에서"&gt;</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">href="#s3"는 같은 문서 안의 자리</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-current="true"로 보는 절 표시</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">scroll-margin-top으로 고정 머리만큼 띄움</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">position: sticky로 스크롤해도 따라옴</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">IntersectionObserver로 보는 절을 고름</div>
                </div>
              </div>'''

D = dict(
  slug="anchornav", ko="앵커 내비", en="Anchor navigation · on-page nav",
  desc="한 문서 안에서 원하는 절로 바로 이동하는 목차를, 고정 머리에 제목이 가려지는 문제와 지금 보는 절을 표시하는 방법까지 함께 다루는 항목입니다.",
  lede="앵커 내비는 <b>같은 문서 안</b>에서만 이동하는 목차입니다. 다른 화면으로 바꾸지 않고, 누른 절이 있는 곳까지 문서를 <b>스크롤해서</b> 보여 줍니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목차를 눌러 보세요. 위쪽에 <b>고정 머리</b>가 있는 문서에서는 앵커로 이동하면 절 제목이
          머리 <b>밑에 가려집니다</b>. 데모는 이동한 뒤 제목의 위치를 재서 가려졌는지 적어 줍니다.
          <code>scroll-margin-top</code>을 주면 머리 높이만큼 여유를 두고 멈추기 때문에 제목이 보입니다.<br>
          목차는 <b>지금 보는 절</b>을 표시해 줘야 위치를 알려 주는 역할을 합니다. 이 표시를 끄면 문서의 어디쯤을 읽고 있는지 알 수 없어서,
          긴 문서에서는 목차가 있어도 쓸모가 줄어듭니다.</p>
        </div>''',
  names=rows([
    ("한국어", "앵커 내비, 목차, 페이지 내 목차, 스크롤 목차"),
    ("영어", "anchor navigation, on-page nav, table of contents, scrollspy"),
    ("같이 쓰는 말",
     "지금 보는 절을 목차에 저절로 표시해 주는 동작은 <b>스크롤스파이</b>(scrollspy)라고 부릅니다. "
     "글 안에 넣는 목차는 <b>TOC</b>(table of contents), "
     "화면 오른쪽에 붙어서 스크롤해도 따라오는 목차는 <b>sticky TOC</b>라고 합니다. "
     "이동할 위치를 가리키는 <code>id</code>는 <b>앵커</b>(anchor)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 보이는 <b>내용을 바꿔 끼우고</b>, 앵커 내비는 같은 문서를 <b>스크롤하기만</b> 합니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 <b>다른 화면</b>으로 옮겨 가고, 앵커 내비는 같은 문서 안에서만 움직입니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 계층에서 <b>위 단계로</b> 가는 링크이고, 앵커 내비는 같은 문서의 다른 절로 가는 링크입니다."),
  ]),
  axes=ax("앵커 내비"),
  oneline="<b>문서가 스크롤되며 이동하는 과정이 보이게 하세요.</b> 화면이 한 번에 바뀌면 문서의 어디로 왔는지 알기 어렵습니다.",
  states=states([
    (toc([("정산 주기", True), ("수수료", False), ("세금계산서", False), ("환불", False)], "152px", "첫 절을 보는 중", True),
     "문서 맨 위에 있을 때", "문서 맨 위에서는 첫 항목이 강조됩니다"),
    (toc([("정산 주기", False), ("수수료", False), ("세금계산서", True), ("환불", False)], "152px", "스크롤하면 따라 바뀜", True),
     "문서를 스크롤하는 중", "스크롤하는 동안 <b>지금 보는 절</b>이 강조됩니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted);background:var(--accent-soft);padding:3px 5px;border-radius:3px">고정 머리</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">▲ 제목이 이 밑에 가려짐</span>'
             '<span style="display:block;font-size:8.5px;margin-top:3px">매주 수요일에 지난주 매출을…</span>'),
         "가려짐", False, "scroll-margin-top이 없음", "152px"),
     "고정 머리에 제목이 가려질 때", "고정 머리에 가려 <b>절 제목이 보이지 않습니다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted);background:var(--accent-soft);padding:3px 5px;border-radius:3px">고정 머리</span>'
             '<span style="display:block;font-size:8.5px;font-weight:700;margin-top:4px">세금계산서</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted)">매달 1일에 지난달 몫을…</span>'),
         "제대로 보임", True, "머리 높이만큼 띄워 둠", "152px"),
     "<code>scroll-margin-top</code>을 줬을 때", "머리 높이만큼 여유를 둬서 <b>제목이 보입니다</b>"),
    (toc([("정산 주기", False), ("수수료", False), ("세금계산서", False), ("환불", False)], "152px", "어디쯤인지 알 수 없음", False),
     "보는 절을 표시하지 않을 때", "지금 위치를 알 수 없어서 목차가 <b>제 역할을 하지 못합니다</b>"),
    (toc([("정산", False), ("수수료", False), ("세금", False), ("환불", False), ("문의", False),
          ("기타", False), ("약관", False), ("부록", False)], "152px", "항목이 너무 많음", False),
     "항목이 너무 많을 때", "항목이 <b>열두 개</b>를 넘으면 목차를 한눈에 읽기 어렵습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>&lt;nav&gt;</code>", "이름 붙이기", "한 화면에 <b>nav가 여러 개</b> 있으므로 이름을 붙여 구별합니다"),
    ("<code>href=\"#s3\"</code>", "같은 문서", "주소에 남기 때문에 그 절을 링크로 <b>공유할 수 있습니다</b>"),
    ("<code>aria-current</code>", "보는 절", "지금 보는 절을 색뿐 아니라 <b>소리로도</b> 알립니다"),
    ("<code>scroll-margin-top</code>", "머리 높이만큼 띄우기", "제목이 가려지는 문제를 CSS <b>한 줄로</b> 고칩니다"),
    ("<code>sticky</code>", "스크롤해도 따라옴", "스크롤해도 목차가 <b>화면에서 사라지지 않습니다</b>"),
    ("관찰자", "보는 절 고르기", "<code>IntersectionObserver</code>로 지금 화면에 걸린 절을 찾습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>절 제목이 고정 머리 밑에 가려지는 문제</b>는 고정 머리를 쓰는 사이트라면 거의 모두 겪습니다.
          예전에는 보이지 않는 빈 상자를 제목 위에 끼워 넣어 제목을 아래로 밀어냈지만,
          지금은 <code>scroll-margin-top</code> <b>한 줄</b>이면 해결됩니다.
          값은 머리 높이와 같게 두고, 화면에 따라 머리 높이가 바뀐다면
          <code>var(--header-h)</code> 같은 변수 하나로 두 값을 함께 관리합니다.<br>
          <b>지금 보는 절</b>을 고를 때는 절이 화면 위쪽에 걸렸는지를 기준으로 삼습니다.
          화면 가운데를 기준으로 삼으면 짧은 절은 가운데에 걸리기 전에 지나가 버려서 끝내 강조되지 않습니다.</p>''',
  do=ul([
    "<code>scroll-margin-top</code>을 <b>머리 높이</b>만큼 줄 때",
    "<b>지금 보는 절</b>을 강조하고 <code>aria-current</code>도 함께 붙일 때",
    "항목을 <b>다섯 개에서 열두 개</b> 사이로 둘 때. 그보다 많으면 절을 묶습니다",
  ]),
  dont=ul([
    "항목마다 <b>깊이를 세 단</b>까지 둘 때. 목차가 본문보다 길어집니다",
    "<code>scrollIntoView</code>로 이동만 하고 <b>주소는 바꾸지 않을</b> 때. 그 절을 링크로 공유할 수 없습니다",
    "<code>behavior: smooth</code>를 <b>늘</b> 켜 둘 때. 모션 줄이기를 켠 사용자에게는 끕니다",
    "목차를 <b>본문 폭 안</b>에 끼워 넣을 때. 폰에서는 목차를 접어 둡니다",
  ]),
  instead='다른 화면으로 옮겨 가야 하면 <a href="sidebar.html">사이드바</a>를 쓰고, 보이는 내용을 갈아 끼우려면 <a href="tabs.html">탭</a>을 씁니다. 계층의 위 단계로 올라가는 길은 <a href="breadcrumb.html">브레드크럼</a>이 맡고, 스크롤해도 화면에 따라붙게 만드는 방법은 <a href="sticky.html">스티키</a> 항목에서 다룹니다.',
  cases=cases([
    (toc([("설치", False), ("설정", True), ("API", False)], "150px", "", True),
     "문서 사이트 오른쪽에 목차 붙이기", "목차를 화면 오른쪽에 <b>붙여</b> 둡니다"),
    (toc([("요약", False), ("상세", True), ("환불 규정", False)], "150px", "", True),
     "긴 약관에서 읽는 절 표시하기", "지금 읽고 있는 절을 <b>표시</b>해 줍니다"),
    (one(txt('<span style="display:block;font-size:8.5px;border:1px solid var(--line);border-radius:4px;padding:3px 6px">목차 ▾</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">폰에서는 접어 둠</span>'),
         "폰", True, "", "150px"),
     "폰에서 목차 접어 두기", "목차를 <b>접어 두었다가</b> 누르면 펼칩니다"),
  ]),
  code_lede="마크업은 평범한 링크이고, 제목 가림과 부드러운 스크롤은 CSS 두 줄로 처리합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"이 문서 안에서"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#fee"</span> <span class="a">aria-current</span>=<span class="s">"true"</span>&gt;수수료&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#tax"</span>&gt;세금계산서&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

&lt;<span class="t">section</span> <span class="a">id</span>=<span class="s">"fee"</span>&gt;&lt;<span class="t">h2</span>&gt;수수료&lt;/<span class="t">h2</span>&gt;…&lt;/<span class="t">section</span>&gt;

<span class="c">/* 고정 머리에 가리지 않게 한다. 이 한 줄이 핵심이다 */</span>
:target, section[id] { <span class="a">scroll-margin-top</span>: <span class="a">var</span>(--header-h); }

<span class="c">/* 모션 줄이기를 켠 사람에게는 부드러운 스크롤을 끈다 */</span>
@media (prefers-reduced-motion: no-preference) {
  html { <span class="a">scroll-behavior</span>: smooth; }
}''',
  keys=kbd([
    ("Tab · Enter", "평범한 링크이므로 키보드 조작을 위해 <b>따로 붙일 것이 없습니다</b>"),
    ("절로 이동한 뒤의 포커스", "브라우저가 그 절로 <b>포커스도</b> 옮깁니다. 그래서 키보드 사용자가 다음에 <kbd>Tab</kbd>을 누르면 그 절에서부터 이어집니다"),
    ("<code>tabindex=\"-1\"</code>", "제목이 포커스를 받지 못하면 붙여 둡니다"),
    ("<code>aria-current=\"true\"</code>", "지금 보는 절에 답니다. 값은 <code>page</code>가 아니라 <code>true</code>입니다"),
    ("<code>:target</code>", "이동한 절을 CSS로 <b>잠깐 강조할</b> 수 있습니다"),
    ("제대로 됐는지 확인하는 방법", "이동한 다음 <b><kbd>Tab</kbd>을 한 번</b> 눌러 포커스가 어디로 가는지 확인합니다"),
  ]),
  backend=rows([
    ("서버를 거치지 않는 이동", "주소에서 <code>#</code> 뒤 부분은 서버로 보내지 않기 때문에, 앵커 이동은 모두 브라우저 안에서 처리됩니다."),
    ("절 id를 바뀌지 않게 두기", "문서를 새로 낼 때마다 id가 바뀌면 <b>다른 사람이 공유해 둔 링크로 들어와도 그 절로 이동하지 않습니다</b>. 그래서 id는 제목 글자에서 만들지 말고 <b>바뀌지 않는 키</b>로 만듭니다."),
    ("절마다 따로 받는 긴 문서", "절마다 데이터를 따로 받아 오는 구조라면 <b>이동하기 전에 그 절의 내용을 이미 받았는지</b> 확인해야 합니다."),
  ]),
  plat_lede="앵커 내비는 <b>웹 문서에서 쓰는 부품</b>이라서 앱에는 대응하는 부품이 거의 없습니다.",
  plats=plats([
    ("웹", "#앵커",
     toc([("수수료", True), ("환불", False)], "110px", "", True),
     "이동한 위치가 주소에 남아서 링크로 <b>공유할 수 있다는</b> 점이 웹만의 장점입니다."),
    ("iOS", "목차 대신 섹션 인덱스",
     '''              <div class="phone" role="img" aria-label="iOS 색인 띠 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:3px;top:26px;display:grid;gap:2px;font-size:4px;color:var(--accent)">
                  <span>ㄱ</span><span>ㄴ</span><span>ㄷ</span><span>ㄹ</span></div>
                <div style="position:absolute;left:5px;right:14px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "목차 대신 화면 오른쪽 가장자리에 <b>색인 띠</b>(sectionIndexTitles)를 둡니다. 가나다 같은 글자를 눌러 그 글자로 시작하는 절로 이동하는 방식입니다."),
    ("안드로이드", "정해진 부품 없음",
     '''              <div class="phone" role="img" aria-label="안드로이드 긴 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "정해진 부품이 없어서 <b>접히는 머리</b>나 칩을 늘어놓은 줄로 비슷하게 만듭니다."),
  ]),
  plat_note="앱에서 목차를 보기 드문 이유는 <b>화면이 좁기</b> 때문입니다. 목차용 세로 띠를 둘 자리가 없어서, iOS는 화면 가장자리에 <b>글자 한 자 폭의 색인</b>을 두는 방식을 택했습니다. 웹에서도 폰 폭에서는 같은 문제가 생기는데, <b>목차를 접어 두고 '목차 ▾' 한 줄</b>로 줄이는 방법이 가장 무난합니다. 펼쳤을 때 목차가 아래에서 시트로 올라오게 하면 한 손으로 다루기도 편합니다.",
  siblings=siblings("anchornav"),
  related='''        <li><a href="sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="scrolllink.html"><b>스크롤 연동</b><em>9부</em></a></li>
        <li><a href="tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="scrollbehavior.html"><b>스크롤 동작</b><em>1부</em></a></li>''',
)
