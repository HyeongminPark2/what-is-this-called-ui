# -*- coding: utf-8 -*-
from ax7 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LEDE7 = "길 안내 부품은 모두 '누르면 어디론가 간다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">href="#s3" — 같은 문서 안의 자리</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-current="true" — 지금 보는 절</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">scroll-margin-top — 고정 머리만큼 떼기</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">position: sticky — 굴려도 따라온다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">IntersectionObserver — 보는 절을 고른다</div>
                </div>
              </div>'''

D = dict(
  slug="anchornav", ko="앵커 내비", en="Anchor navigation · on-page nav",
  desc="한 문서 안에서 절로 뛰는 목차. 고정 머리에 가려지는 문제와 지금 보는 절 밝히기.",
  lede="<b>같은 문서 안</b>에서만 움직입니다. 화면을 갈아 치우지 않고 <b>굴려서</b> 데려다 줍니다.",
  axes_lede=LEDE7,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>목차를 눌러 보세요. <b>고정 머리</b>가 있는 문서에서는 앵커로 뛰면 제목이
          머리 <b>밑으로 숨습니다</b> — 데모가 뛴 뒤 제목의 자리를 재서 적습니다.
          <code>scroll-margin-top</code> 을 주면 머리 높이만큼 미리 떼어 놓아 제목이 보입니다.<br>
          목차는 <b>지금 보는 절</b>을 밝혀 줘야 길잡이가 됩니다. 끄면 어디쯤인지 알 수 없습니다 —
          긴 문서에서 목차가 있으나 마나 해지는 이유입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "앵커 내비, 목차, 페이지 내 목차, 스크롤 목차"),
    ("영어", "anchor navigation, on-page nav, table of contents, scrollspy"),
    ("같이 쓰는 말",
     "지금 보는 절을 저절로 밝혀 주는 동작을 <b>스크롤스파이</b>(scrollspy)라 부릅니다. "
     "글 안에 심는 목차는 <b>TOC</b>(table of contents), "
     "오른쪽에 붙어 따라오는 꼴은 <b>sticky TOC</b> 라고 합니다. "
     "뛰어가는 자리를 가리키는 <code>id</code> 를 <b>앵커</b>(anchor)라 부릅니다."),
    ("자주 잘못 부름",
     "<b>탭</b> — <a href=\"tabs.html\">탭</a>은 <b>내용을 갈아 끼우고</b>, 앵커 내비는 <b>굴릴 뿐</b>입니다.<br>"
     "<b>사이드바</b> — <a href=\"sidebar.html\">사이드바</a>는 <b>다른 화면</b>으로 데려갑니다.<br>"
     "<b>브레드크럼</b> — <a href=\"breadcrumb.html\">브레드크럼</a>은 <b>위로</b> 가는 길입니다."),
  ]),
  axes=ax("앵커 내비"),
  oneline="<b>굴려서 간다는 걸 느끼게 하세요.</b> 순간이동하면 어디로 왔는지 모릅니다.",
  states=states([
    (toc([("정산 주기", True), ("수수료", False), ("세금계산서", False), ("환불", False)], "152px", "첫 절을 보는 중", True),
     "맨 위", "첫 항목이 밝다"),
    (toc([("정산 주기", False), ("수수료", False), ("세금계산서", True), ("환불", False)], "152px", "굴리면 따라 바뀐다", True),
     "굴리는 중", "<b>보는 절</b>이 밝다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted);background:var(--accent-soft);padding:3px 5px;border-radius:3px">고정 머리</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">▲ 제목이 이 밑에 숨었다</span>'
             '<span style="display:block;font-size:8.5px;margin-top:3px">매주 수요일에 지난주 매출을…</span>'),
         "가려짐", False, "scroll-margin-top 이 없다", "152px"),
     "머리에 가려짐", "<b>제목이 안 보인다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted);background:var(--accent-soft);padding:3px 5px;border-radius:3px">고정 머리</span>'
             '<span style="display:block;font-size:8.5px;font-weight:700;margin-top:4px">세금계산서</span>'
             '<span style="display:block;font-size:8.5px;color:var(--fg-muted)">매달 1일에 지난달 몫을…</span>'),
         "제대로", True, "머리 높이만큼 떼어 놓았다", "152px"),
     "<code>scroll-margin-top</code>", "<b>제목이 보인다</b>"),
    (toc([("정산 주기", False), ("수수료", False), ("세금계산서", False), ("환불", False)], "152px", "어디쯤인지 모른다", False),
     "안 밝힘", "목차가 <b>있으나 마나</b>"),
    (toc([("정산", False), ("수수료", False), ("세금", False), ("환불", False), ("문의", False),
          ("기타", False), ("약관", False), ("부록", False)], "152px", "너무 많다", False),
     "항목이 많음", "<b>열둘</b>을 넘으면 못 읽는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>&lt;nav&gt;</code>", "이름을 붙인다", "화면에 <b>nav 가 여럿</b>이라 구별이 필요하다"),
    ("<code>href=\"#s3\"</code>", "같은 문서", "주소에 남아 <b>공유할 수 있다</b>"),
    ("<code>aria-current</code>", "보는 절", "색 말고 <b>소리로도</b>"),
    ("<code>scroll-margin-top</code>", "머리만큼 떼기", "<b>한 줄로</b> 고쳐진다"),
    ("<code>sticky</code>", "따라온다", "굴려도 목차가 <b>안 사라진다</b>"),
    ("관찰자", "보는 절 고르기", "<code>IntersectionObserver</code>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>제목이 머리 밑에 숨는 것</b>은 고정 머리를 쓰는 사이트라면 거의 다 겪습니다.
          예전에는 보이지 않는 빈 상자를 제목 위에 끼워 넣어 밀어내곤 했는데,
          지금은 <code>scroll-margin-top</code> <b>한 줄</b>이면 끝납니다.
          값은 머리 높이와 같게 두되, 머리 높이가 바뀌는 화면이라면
          <code>var(--header-h)</code> 같은 변수로 묶어 둡니다.<br>
          <b>지금 보는 절</b>을 고를 때는 '화면 위쪽 어디에 걸렸는가'를 기준으로 삼습니다 —
          가운데를 기준으로 삼으면 짧은 절에서 영영 안 밝아집니다.</p>''',
  do=ul([
    "<code>scroll-margin-top</code> 을 <b>머리 높이</b>만큼 주기",
    "<b>지금 보는 절</b>을 밝히고 <code>aria-current</code> 도 같이 붙이기",
    "항목을 <b>다섯에서 열둘</b> 사이로 두기 — 넘으면 절을 묶는다",
  ]),
  dont=ul([
    "항목마다 <b>깊이를 세 단</b>까지 두기 — 목차가 본문보다 길어진다",
    "<code>scrollIntoView</code> 로만 가고 <b>주소를 안 바꾸기</b> — 공유가 안 된다",
    "<code>behavior: smooth</code> 를 <b>늘</b> 켜 두기 — 모션 줄이기를 켠 사람에게는 끈다",
    "목차를 <b>본문 폭 안</b>에 끼워 넣기 — 폰에서는 접어 둔다",
  ]),
  instead='다른 화면으로 가면 <a href="sidebar.html">사이드바</a>, 내용을 갈아 끼우면 <a href="tabs.html">탭</a>, 위로 가면 <a href="breadcrumb.html">브레드크럼</a>, 따라붙는 동작은 <a href="sticky.html">스티키</a>.',
  cases=cases([
    (toc([("설치", False), ("설정", True), ("API", False)], "150px", "", True),
     "문서 사이트", "오른쪽에 <b>붙여</b> 둔다"),
    (toc([("요약", False), ("상세", True), ("환불 규정", False)], "150px", "", True),
     "긴 약관", "읽는 자리를 <b>표시</b>해 준다"),
    (one(txt('<span style="display:block;font-size:8.5px;border:1px solid var(--line);border-radius:4px;padding:3px 6px">목차 ▾</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">폰에서는 접어 둔다</span>'),
         "폰", True, "", "150px"),
     "폰", "<b>접어 두고</b> 눌러서 편다"),
  ]),
  code_lede="평범한 링크입니다. 두 줄의 CSS 가 나머지를 합니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"이 문서 안에서"</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#fee"</span> <span class="a">aria-current</span>=<span class="s">"true"</span>&gt;수수료&lt;/<span class="t">a</span>&gt;
  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"#tax"</span>&gt;세금계산서&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">nav</span>&gt;

&lt;<span class="t">section</span> <span class="a">id</span>=<span class="s">"fee"</span>&gt;&lt;<span class="t">h2</span>&gt;수수료&lt;/<span class="t">h2</span>&gt;…&lt;/<span class="t">section</span>&gt;

<span class="c">/* 고정 머리에 안 가리게 — 이 한 줄이 핵심이다 */</span>
:target, section[id] { <span class="a">scroll-margin-top</span>: <span class="a">var</span>(--header-h); }

<span class="c">/* 모션 줄이기를 켠 사람에게는 부드럽게를 끈다 */</span>
@media (prefers-reduced-motion: no-preference) {
  html { <span class="a">scroll-behavior</span>: smooth; }
}''',
  keys=kbd([
    ("Tab · Enter", "평범한 링크다 — <b>따로 붙일 것이 없다</b>"),
    ("뛴 뒤 초점", "브라우저가 그 절로 <b>초점도</b> 옮긴다 — 키보드 사용자의 다음 Tab 이 거기서 이어진다"),
    ("<code>tabindex=\"-1\"</code>", "제목이 초점을 못 받으면 붙여 둔다"),
    ("<code>aria-current=\"true\"</code>", "보는 절. <code>page</code> 가 아니라 <code>true</code>"),
    ("<code>:target</code>", "뛰어간 절을 CSS 로 <b>잠깐 밝힐</b> 수 있다"),
    ("확인하는 법", "뛴 다음 <b>Tab 을 한 번</b> 눌러 어디로 가는지 본다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "<code>#</code> 뒤는 서버로 가지 않습니다. 전부 브라우저 안의 일입니다."),
    ("절 id 를 고정", "문서를 다시 낼 때마다 id 가 바뀌면 <b>남이 공유한 링크가 깨집니다</b> — 제목 글자가 아니라 <b>안 바뀌는 열쇠</b>로 만듭니다."),
    ("긴 문서", "절마다 따로 받아 오는 구조라면 <b>뛰기 전에 그 절이 와 있는지</b> 확인해야 합니다."),
  ]),
  plat_lede="<b>웹 문서의 부품</b>입니다. 앱에는 대응이 거의 없습니다.",
  plats=plats([
    ("웹", "#앵커",
     toc([("수수료", True), ("환불", False)], "110px", "", True),
     "주소에 남아 <b>공유할 수 있는</b> 것이 웹만의 장점입니다."),
    ("iOS", "없다 — 섹션 인덱스",
     '''              <div class="phone" role="img" aria-label="iOS 색인 띠 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:3px;top:26px;display:grid;gap:2px;font-size:4px;color:var(--accent)">
                  <span>ㄱ</span><span>ㄴ</span><span>ㄷ</span><span>ㄹ</span></div>
                <div style="position:absolute;left:5px;right:14px;top:28px;height:8px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "목차 대신 오른쪽 가장자리의 <b>색인 띠</b>(sectionIndexTitles)를 씁니다 — 가나다로 뛰는 꼴입니다."),
    ("안드로이드", "없다",
     '''              <div class="phone" role="img" aria-label="안드로이드 긴 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:7px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:7px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "정해진 부품이 없습니다. <b>접히는 머리</b>나 칩 줄로 비슷하게 만듭니다."),
  ]),
  plat_note="앱에 목차가 드문 것은 <b>화면이 좁아서</b>입니다. 목차에 세로 띠를 내줄 자리가 없으니, iOS 는 가장자리에 <b>글자 한 줄 폭의 색인</b>을 두는 쪽으로 풀었습니다. 웹에서도 폰 폭에서는 같은 고민이 생기는데, <b>목차를 접어 두고 '목차 ▾' 한 줄</b>로 줄이는 것이 가장 무난합니다. 펴면 시트로 올라오게 하면 손도 편합니다.",
  siblings=siblings("anchornav"),
  related='''        <li><a href="sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="scrolllink.html"><b>스크롤 연동</b><em>9부</em></a></li>
        <li><a href="tabs.html"><b>탭</b><em>7부</em></a></li>
        <li><a href="scrollbehavior.html"><b>스크롤 동작</b><em>1부</em></a></li>''',
)
