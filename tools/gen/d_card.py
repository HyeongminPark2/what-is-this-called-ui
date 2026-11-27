# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def minicard(title, meta, foot="", media=True, w="150px", extra=""):
    return ('              <div style="width:100%%;max-width:%s;border:1px solid var(--line);border-radius:9px;'
            'background:var(--surface);overflow:hidden;%s">'
            '%s<div style="padding:9px;display:grid;gap:4px">'
            '<span style="font-size:11.5px;font-weight:700;display:block">%s</span>'
            '<span style="font-size:10.5px;color:var(--fg-muted);display:block">%s</span>%s</div></div>'
            ) % (w, extra,
                 '<span style="display:block;aspect-ratio:4/3;background:repeating-linear-gradient(135deg,var(--ink-100) 0 7px,var(--ink-050) 7px 14px)"></span>' if media else '',
                 title, meta, foot)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:14px 10px 14px 0">
                <div style="padding-left:26px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;box-shadow:var(--e1);overflow:visible">
                    <div class="pin-out" data-pin="2" style="display:block;aspect-ratio:16/7;background:repeating-linear-gradient(135deg,var(--ink-100) 0 9px,var(--ink-050) 9px 18px);border-radius:10px 10px 0 0;margin-left:26px"></div>
                    <div style="padding:11px 11px 12px;padding-left:26px;display:grid;gap:9px">
                      <div class="pin-out" data-pin="3" style="font-size:13px;font-weight:700">무선 이어폰 2세대</div>
                      <div class="pin-out" data-pin="4" style="font-size:11.5px;color:var(--fg-muted)">모란상회 · ₩129,000</div>
                      <div class="pin-out" data-pin="5" style="display:inline-block;border:1px solid var(--line-strong);border-radius:7px;padding:5px 10px;font-size:11px;justify-self:start">장바구니</div>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="card", ko="카드", en="Card",
  desc="카드가 무엇이고 리스트 아이템과 어떻게 다른지, 전체를 누르게 만들 때 생기는 문제를 실물과 해부도로 보여주는 항목.",
  lede="한 대상에 딸린 것들을 <b>테두리 하나로 묶은 상자</b>. 묶는 것이 일이라서, 안에 누를 것이 여럿이면 바로 문제가 생깁니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'장바구니'를 눌러 보고, 그다음 카드의 빈 데를 눌러 보세요. <b>둘이 따로 동작합니다</b> —
          카드 전체가 링크인데도 안의 버튼이 카드를 열지 않습니다(<code>stopPropagation</code>).
          이걸 안 막으면 장바구니를 누를 때마다 상세 화면으로 끌려갑니다.<br>
          <b>제목이 긴 상품 섞기</b>를 켜면 카드 높이가 제각각이 됩니다. 데이터가 길이를 정하기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "카드, 카드 뷰, 상품 카드"),
    ("영어", "card, tile, media object"),
    ("같이 쓰는 말",
     "위의 사진 자리를 <b>미디어</b>(media · thumbnail), 글이 있는 부분을 <b>본문</b>(body · content), "
     "맨 아래 버튼 줄을 <b>액션 영역</b>(actions · footer)이라 합니다. "
     "카드를 격자로 깐 것을 <b>카드 그리드</b>, 가로로 미는 것을 <b>캐러셀</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>타일</b> — 보통 같은 뜻이지만, 윈도우·대시보드 쪽에서는 <b>정사각형에 가까운 칸</b>을 가리킵니다.<br>"
     "<b>패널</b> — 패널은 화면을 나눈 <b>구역</b>이고 카드는 <b>한 건</b>입니다. 패널 안에 카드가 여럿 들어갑니다.<br>"
     "<b>모달</b> — 떠서 뒤를 막으면 모달입니다. 카드는 <b>흐름 안에</b> 놓입니다."),
  ]),
  axes=ax("카드"),
  oneline="카드는 <b>하나로 셀 수 있는 것</b>을 묶습니다. '이 안의 것이 다 같은 한 건인가'에 아니라고 답하면 카드가 아니라 구역입니다.",
  s4_title="상태", s4_hint="그림 한 장으로는 못 배운다",
  states=states([
    (minicard("무선 이어폰 2세대", "₩129,000"), "기본", "사진 · 제목 · 메타. 가장 흔한 짜임"),
    (minicard("무선 이어폰 2세대", "₩129,000", extra="box-shadow:0 6px 16px rgba(20,22,26,.14);transform:translateY(-2px)"),
     "호버", "<b>떠오르거나</b> 테두리가 진해진다. 누를 수 있다는 신호"),
    (minicard("무선 이어폰 2세대", "₩129,000", extra="outline:2px solid var(--accent);outline-offset:2px"),
     "포커스", "키보드로 왔을 때. 호버와 <b>같은 모양이면 안 된다</b>"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:9px;background:var(--surface);overflow:hidden">
                <span class="skl" style="display:block;aspect-ratio:4/3;border-radius:0"></span>
                <div style="padding:9px;display:grid;gap:5px"><span class="skl" style="height:9px;width:80%"></span><span class="skl" style="height:8px;width:50%"></span></div>
              </div>''',
     "로딩", "<b>같은 높이의</b> 뼈대. 높이가 다르면 들어올 때 화면이 덜컥거린다"),
    (minicard("무선 이어폰 2세대 블루투스 5.3 노이즈 캔슬링 케이스 포함", "₩129,000"),
     "긴 제목", "데이터가 길이를 정한다. <b>늘어나게 둘지 자를지</b>를 먼저 정해 둔다"),
    ('''              <div style="width:100%;max-width:150px;border:1px dashed var(--line-strong);border-radius:9px;background:var(--surface);display:grid;place-items:center;padding:18px 9px;gap:5px;text-align:center">
                <span style="font-size:15px;color:var(--fg-faint)">+</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">상품 추가</span>
              </div>''',
     "빈 카드", "새로 만드는 자리. <b>점선</b>으로 '아직 아무것도 없다'를 말한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("카드", "card · container", "테두리와 모서리와 그림자. <b>이 셋이 '한 덩어리'를 만든다</b>"),
    ("미디어", "media · thumbnail", "사진 자리. <b>비율을 못 박아</b> 둬야 사진마다 카드 높이가 달라지지 않는다"),
    ("제목", "title", "무엇인지. 카드 안에서 가장 진하고 큰 글"),
    ("메타", "meta · supporting text", "값·날짜·만든 이. 제목보다 작고 흐리게"),
    ("보조 동작", "actions", "카드 전체가 링크일 때 <b>여기서 사고가 난다</b> — 눌림이 위로 번지지 않게 막는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          카드 전체를 누르게 만드는 방법은 두 가지인데 결과가 다릅니다. <b>카드 전체를 <code>&lt;a&gt;</code>로 감싸면</b>
          안의 버튼이 링크 안에 들어가 버려 HTML 이 어긋나고 눌림이 겹칩니다. 그래서 보통은
          <b>제목만 링크로 두고</b> 그 링크를 투명하게 카드 전체로 늘립니다(<code>::after { inset: 0 }</code>).
          이러면 스크린 리더에는 링크가 하나만 읽히고, 버튼은 그 위에 따로 올려 둘 수 있습니다.</p>''',
  do=ul([
    "한 대상에 딸린 것이 <b>서너 가지</b>라 한 줄에 안 들어갈 때",
    "사진이 <b>고르는 데 도움이 될</b> 때 — 상품, 숙소, 영상",
    "건마다 길이가 들쭉날쭉할 때 — 카드는 높이가 늘어나도 괜찮습니다",
  ]),
  dont=ul([
    "<b>세로로 훑어 비교</b>해야 할 때 → 리스트 아이템이나 표가 낫습니다",
    "보여 줄 것이 제목 하나뿐일 때 — 테두리만 늘어납니다",
    "건수가 아주 많을 때 — 카드는 자리를 많이 먹어 한 화면에 몇 개 안 들어갑니다",
    "모든 것을 카드에 넣는 것 — <b>다 묶으면 아무것도 안 묶인 것</b>과 같습니다",
  ]),
  instead='줄 세워 비교하려면 <a href="listitem.html">리스트 아이템</a>, 숫자 하나면 <a href="stat.html">스탯 타일</a>, 표로 다룰 양이면 데이터 테이블(10부).',
  cases=cases([
    (minicard("무선 이어폰 2세대", "모란상회 · ₩129,000", foot='<span style="font-size:10px;color:#e8a33d">★ 4.3 <span style="color:var(--fg-muted)">(1,284)</span></span>', w="160px"),
     "상품 카드", "사진이 크고 값이 또렷하다. <b>별점과 리뷰 수</b>가 거의 늘 붙는다"),
    (minicard("정산 요청 #4821", "11월 1일 ~ 11월 7일 · ₩1,284,000", foot='<span class="bdg bdg--warn" style="height:16px;padding:0 6px;font-size:9px">검토 중</span>', media=False, w="160px"),
     "업무 카드", "사진이 없다. <b>상태 배지</b>가 사진 자리를 대신한다"),
    ('''              <div style="width:100%;max-width:160px;display:flex;border:1px solid var(--line);border-radius:9px;background:var(--surface);overflow:hidden">
                <span style="width:52px;flex:none;background:repeating-linear-gradient(135deg,var(--ink-100) 0 7px,var(--ink-050) 7px 14px)"></span>
                <span style="padding:9px;display:grid;gap:3px;min-width:0">
                  <span style="font-size:11.5px;font-weight:700">접이식 캠핑 의자</span>
                  <span style="font-size:10.5px;color:var(--fg-muted)">₩58,000</span>
                </span>
              </div>''',
     "가로형 카드", "좁은 화면에서 쓴다. <b>리스트 아이템과 거의 구별이 안 된다</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 부품의 계약서",
  code_lede="카드 자체에는 정해진 역할(role)이 없습니다. <b>무엇으로 감싸느냐</b>가 전부입니다 — 목록이면 <code>&lt;li&gt;</code>, 기사면 <code>&lt;article&gt;</code>.",
  code='''&lt;<span class="t">article</span> <span class="a">class</span>=<span class="s">"card"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"…"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;          <span class="c">&lt;!-- 장식이면 alt 를 비운다 --&gt;</span>
  &lt;<span class="t">h3</span>&gt;
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/p/128"</span> <span class="a">class</span>=<span class="s">"stretch"</span>&gt;무선 이어폰 2세대&lt;/<span class="t">a</span>&gt;
  &lt;/<span class="t">h3</span>&gt;
  &lt;<span class="t">p</span>&gt;모란상회 · ₩129,000&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"over"</span>&gt;장바구니&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">article</span>&gt;

<span class="c">/* 링크 하나를 카드 전체로 늘린다 — 읽히는 링크는 그대로 하나 */</span>
<span class="t">.card</span> { <span class="a">position</span>: relative; }
<span class="t">.stretch</span>::<span class="t">after</span> { <span class="a">content</span>: <span class="s">""</span>; <span class="a">position</span>: absolute; <span class="a">inset</span>: <span class="a">0</span>; }
<span class="t">.over</span> { <span class="a">position</span>: relative; <span class="a">z-index</span>: <span class="a">1</span>; } <span class="c">/* 버튼은 그 위로 */</span>''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "카드마다 <b>한 번</b>만 멈추는 것이 이상적이다. 링크가 셋이면 세 번 멈춘다"),
    ("<kbd>Enter</kbd>", "카드의 주된 곳으로 간다"),
    ("안의 버튼", "<code>event.stopPropagation()</code> 또는 링크를 늘리는 방식으로 <b>겹침을 푼다</b>"),
    ("제목", "<code>h2</code>~<code>h4</code>로 두면 스크린 리더가 제목만 훑어 목록을 넘길 수 있다"),
    ("사진", "뜻이 있으면 <code>alt</code>를 쓰고, 제목이 이미 말해 주면 <b>비워 둔다</b>"),
  ]),
  backend=rows([
    ("카드 하나 = 응답 한 건", "목록 API 가 돌려주는 한 줄이 카드 하나입니다. 카드에 보이는 값은 <b>전부 그 한 줄 안에</b> 있어야 합니다 — 카드마다 따로 부르면 20장이면 요청이 20번입니다."),
    ("사진 비율", "올라오는 사진은 비율이 제각각입니다. 서버에서 <b>미리 잘라</b> 두거나 <code>object-fit: cover</code>로 맞춥니다. 안 맞추면 카드 높이가 흔들립니다."),
    ("글 길이", "제목 길이는 <b>데이터가 정합니다.</b> 가장 긴 값으로 한 번 그려 보지 않으면 운영에서 깨집니다. 길이를 서버에서 자를지 화면에서 자를지도 정해 둡니다."),
    ("카드 수", "한 화면에 카드 20장이면 사진도 20장입니다. 지연 로딩(<code>loading=\"lazy\"</code>)과 작은 썸네일이 <b>첫 화면 속도</b>를 좌우합니다."),
  ]),
  plat_lede="세 플랫폼 모두 '카드'라는 말을 쓰지만, 그림자와 모서리의 기본값이 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     minicard("카드", "제목 · 메타", media=False, w="120px"),
     "정해진 태그가 없습니다. <code>&lt;article&gt;</code>이나 <code>&lt;li&gt;</code>에 테두리를 준 것이 전부입니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 카드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:28px;background:var(--surface);border-radius:10px;padding:8px;box-shadow:0 1px 3px rgba(20,22,26,.12)">
                  <span style="font-size:7.5px;font-weight:700;display:block">무선 이어폰</span>
                  <span style="font-size:6.5px;color:var(--fg-muted)">₩129,000</span></div>
              </div></div>''',
     "부품 이름이 따로 없습니다. <b>그룹 리스트</b>(inset grouped)가 카드 구실을 하고, 모서리가 둥글고 그림자는 아주 옅습니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 카드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:28px;background:var(--surface);border-radius:12px;padding:8px;border:1px solid var(--line)">
                  <span style="font-size:7.5px;font-weight:700;display:block">무선 이어폰</span>
                  <span style="font-size:6.5px;color:var(--fg-muted)">₩129,000</span></div>
              </div></div>''',
     "<b>Card</b> 가 정식 부품이고 <b>Elevated · Filled · Outlined</b> 세 갈래가 규격에 있습니다."),
  ]),
  plat_note="\"카드로 해 주세요\"가 안드로이드에서는 <b>정해진 부품 이름</b>이라 세 갈래 중 어느 것인지까지 정해야 하고, iOS 에서는 <b>그런 부품이 없어서</b> 보통 그룹 리스트로 풀립니다. 시안의 그림자를 그대로 옮기면 iOS 화면에서 혼자 둥둥 떠 보입니다.",
  siblings=siblings("card"),
  related='''        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/elevation.html"><b>고도</b><em>2부</em></a></li>
        <li><a href="../items/spacing.html"><b>간격 체계</b><em>2부</em></a></li>
        <li><span class="na"><b>데이터 테이블</b><em>10부</em></span></li>''',
)
