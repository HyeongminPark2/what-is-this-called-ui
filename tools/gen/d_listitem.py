# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(lead, t, s="", end="", w="168px", style=""):
    return ('              <div style="width:100%%;max-width:%s;border:1px solid var(--line);border-radius:8px;'
            'background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px 9px;%s">'
            '%s<span style="flex:1;min-width:0;display:grid;gap:2px">'
            '<span style="font-size:11.5px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block">%s</span>'
            '%s</span>%s</div>'
            ) % (w, style, lead, t,
                 '<span style="font-size:10px;color:var(--fg-muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block">%s</span>' % s if s else '',
                 end)

AV = '<span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:9px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>'
CHEV = '<span style="color:var(--fg-faint);font-size:12px;flex:none">›</span>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:16px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:9px 11px;display:flex;align-items:center;gap:9px">
                    <span style="width:26px;height:26px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                    <span style="flex:1;min-width:0;display:grid;gap:2px">
                      <span style="font-size:12px;font-weight:600">정산 요청 #4821</span>
                      <span style="font-size:10.5px;color:var(--fg-muted)">11월 1일 ~ 11월 7일</span>
                    </span>
                    <span style="font-size:11px;color:var(--fg-muted);flex:none">₩1,245,480</span>
                    <span style="color:var(--fg-faint);font-size:13px;flex:none">›</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-size:11px;color:var(--fg-muted)">줄 하나가 통째로 <b style="color:var(--fg)">하나의 누를 것</b>이다</div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span style="width:26px;height:26px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                    <span>앞자리 — <b style="color:var(--fg)">폭이 고정</b></span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted)">가운데 — <b style="color:var(--fg)">여기만 늘어난다</b></div>
                  <div class="pin-out" data-pin="5" style="height:1px;background:var(--line-strong)"></div>
                  <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted);background:var(--surface);border-radius:6px;padding:5px 9px;justify-self:start">이번 주</div>
                </div>
              </div>'''

D = dict(
  slug="listitem", ko="리스트 아이템", en="List item · row",
  desc="리스트 아이템의 세 자리(앞·가운데·뒤)와 말줄임, 카드와의 차이를 실물과 해부도로 보여주는 항목.",
  lede="목록에서 <b>한 줄이 곧 한 건</b>. 카드와 담는 내용은 같은데, 세로로 훑어 비교하기 좋게 줄을 맞춰 둔 것이 다릅니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>줄 수를 바꿔 보고, <b>자르지 말고 접기</b>를 켜 보세요. 글이 다 보이는 대신
          줄 높이가 제각각이 됩니다. 목록은 보통 <b>자르는 쪽</b>을 고릅니다 —
          높이가 일정해야 눈이 세로로 미끄러지고, 가상 스크롤도 그때만 쓸 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "리스트 아이템, 목록 항목, 줄, 행"),
    ("영어", "list item, row, list row, cell(iOS)"),
    ("같이 쓰는 말",
     "앞의 아이콘·아바타 자리를 <b>리딩</b>(leading), 뒤의 값·꺾쇠 자리를 <b>트레일링</b>(trailing)이라 합니다. "
     "줄 사이를 나누는 선은 <b>디바이더</b>(divider · separator), 묶음의 머리글은 <b>섹션 헤더</b>입니다. "
     "글이 몇 줄이냐로 <b>한 줄·두 줄·세 줄</b>(one/two/three-line)이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>카드</b> — 가로형 카드와 거의 같아 보입니다. 가르는 것은 생김새가 아니라 <b>어떻게 모이느냐</b>입니다.<br>"
     "<b>테이블 행</b> — 표의 행은 <b>열이 정해져</b> 있고 정렬·선택이 따릅니다. 리스트 아이템은 자유로운 세 자리뿐입니다.<br>"
     "<b>메뉴 아이템</b> — 메뉴는 <b>눌러서 사라지는</b> 선택지입니다. 리스트는 내용 그 자체입니다."),
  ]),
  axes=ax("리스트 아이템"),
  oneline="리스트 아이템은 <b>세로로 비교하라고</b> 줄을 맞춘 것입니다. 줄 높이가 제각각이면 이미 리스트의 일을 못 하고 있습니다.",
  s4_title="상태", s4_hint="그림 한 장으로는 못 배운다",
  states=states([
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV), "기본", "앞 · 가운데 · 뒤. <b>세 자리</b>가 전부다"),
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV, style="background:var(--bg)"),
     "호버", "<b>줄 전체</b>가 밝아진다 — 어디까지가 한 줄인지 알려 준다"),
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV, style="outline:2px solid var(--accent);outline-offset:-2px"),
     "포커스", "테두리를 <b>안쪽</b>에 그린다. 바깥에 그리면 옆 줄을 덮는다"),
    (row('<span style="width:14px;height:14px;border:1.5px solid var(--accent);background:var(--accent);border-radius:3px;flex:none;display:grid;place-items:center;color:#fff;font-size:9px">✓</span>',
         "정산 요청 #4821", "11월 1일 ~ 11월 7일", "", style="background:var(--accent-soft)"),
     "고름", "<b>체크박스가 앞자리로</b> 들어온다. 고른 줄은 바탕이 바뀐다"),
    (row(AV, "환불 확인 요청 — 카드 승인 취소가 늦어", "주문 TX-99120 · 승인 취소 대기", CHEV),
     "긴 글", "한 줄을 넘지 않는다. <b>…으로 자르고</b> 전체는 상세에서 본다"),
    ('''              <div style="width:100%;max-width:168px;border:1px solid var(--line);border-radius:8px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px 9px">
                <span class="skl" style="width:22px;height:22px;border-radius:99px;flex:none"></span>
                <span style="flex:1;display:grid;gap:4px"><span class="skl" style="height:8px;width:70%"></span><span class="skl" style="height:7px;width:45%"></span></span>
              </div>''',
     "로딩", "<b>진짜 줄과 같은 높이</b>로. 다르면 들어올 때 목록이 덜컥거린다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("목록", "list", "줄들을 감싸는 상자. <code>&lt;ul&gt;</code>이라야 '모두 몇 건'이 읽힌다"),
    ("줄", "list item · row", "한 건 전체가 <b>하나의 누를 것</b>이다 — 제목만 링크로 두지 않는다"),
    ("앞자리", "leading", "아바타·아이콘·체크박스. <b>폭이 고정</b>이라야 줄끼리 세로로 맞는다"),
    ("가운데", "primary · secondary text", "제목과 보조 글. <b>여기만 늘어난다</b>(<code>flex:1; min-width:0</code>)"),
    ("구분선", "divider", "줄 사이. 아바타가 있으면 보통 <b>앞자리만큼 들여</b> 긋는다"),
    ("섹션 헤더", "section header", "'이번 주'처럼 줄들을 묶는 머리글. 스크롤해도 붙어 있게 만들기도 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          가운데 자리에 <code>min-width: 0</code>을 안 주면 말줄임이 <b>영영 안 걸립니다.</b>
          플렉스·그리드 자식의 기본 최소 너비가 '내용만큼'이라, 글이 길면 칸을 밀어내고
          뒤쪽의 값과 꺾쇠를 화면 밖으로 쫓아냅니다. 리스트에서 가장 자주 나는 레이아웃 사고입니다.</p>''',
  do=ul([
    "건이 많고 <b>같은 모양</b>으로 반복될 때",
    "세로로 훑으며 <b>찾거나 비교</b>할 때",
    "좁은 화면 — 카드보다 한 화면에 훨씬 많이 들어갑니다",
    "설정처럼 <b>이름과 값의 짝</b>이 늘어설 때",
  ]),
  dont=ul([
    "사진이 고르는 데 결정적일 때 → <a href=\"card.html\">카드</a>가 낫습니다",
    "열을 정렬하거나 여러 값을 비교해야 할 때 → 데이터 테이블",
    "줄마다 보여 줄 것이 너무 많을 때 — 세 자리에 다 안 들어가면 <b>줄이 아니라 카드</b>입니다",
  ]),
  instead='사진이 중요하면 <a href="card.html">카드</a>, 열로 다루면 데이터 테이블(10부), 눌러서 사라지는 선택지면 메뉴(6부).',
  cases=cases([
    (row(AV, "김철수", "네, 오후에 확인해 볼게요", '<span style="font-size:9.5px;color:var(--fg-muted);flex:none">14:02</span>', w="180px"),
     "대화 목록", "앞에 아바타, 뒤에 시각. <b>메신저의 첫 화면</b>"),
    (row('<span style="width:22px;height:22px;border-radius:6px;background:var(--bg);flex:none"></span>',
         "알림", "", '<span style="width:30px;height:17px;border-radius:99px;background:var(--accent);flex:none;position:relative"><span style="position:absolute;right:2px;top:2px;width:13px;height:13px;border-radius:99px;background:#fff"></span></span>', w="180px"),
     "설정 줄", "뒤에 스위치가 온다. <b>줄 전체가 아니라 스위치만</b> 눌리게 할지 정해야 한다"),
    (row('<span style="width:22px;height:22px;border-radius:4px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 5px,var(--ink-050) 5px 10px);flex:none"></span>',
         "접이식 캠핑 의자", "한빛아웃도어 · 1개", '<span style="font-size:10px;font-weight:700;flex:none">₩58,000</span>', w="180px"),
     "주문 내역", "뒤에 값. <b>금액은 오른쪽 맞춤</b>에 자릿수를 맞춘다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 부품의 계약서",
  code_lede="목록은 <code>&lt;ul&gt;</code>·<code>&lt;li&gt;</code>로 둡니다. 그래야 스크린 리더가 <b>'목록, 항목 3개 중 1번'</b>이라고 읽어 줍니다.",
  code='''&lt;<span class="t">ul</span> <span class="a">class</span>=<span class="s">"list"</span>&gt;
  &lt;<span class="t">li</span>&gt;
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settle/4821"</span> <span class="a">class</span>=<span class="s">"li"</span>&gt;
      &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"av"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;길동&lt;/<span class="t">span</span>&gt;
      &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"li__main"</span>&gt;
        &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"li__t"</span>&gt;정산 요청 #4821&lt;/<span class="t">span</span>&gt;
        &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"li__s"</span>&gt;11월 1일 ~ 11월 7일&lt;/<span class="t">span</span>&gt;
      &lt;/<span class="t">span</span>&gt;
      &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"li__end"</span>&gt;₩1,245,480&lt;/<span class="t">span</span>&gt;
    &lt;/<span class="t">a</span>&gt;
  &lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ul</span>&gt;

<span class="c">/* 이 한 줄이 없으면 말줄임이 안 걸린다 */</span>
<span class="t">.li__main</span> { <span class="a">flex</span>: <span class="a">1</span>; <span class="a">min-width</span>: <span class="a">0</span>; }
<span class="t">.li__t</span> { <span class="a">overflow</span>: hidden; <span class="a">text-overflow</span>: ellipsis; <span class="a">white-space</span>: nowrap; }''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "줄마다 <b>한 번</b>. 줄 안에 누를 것이 둘이면 두 번 멈춘다"),
    ("<kbd>Enter</kbd>", "그 줄을 연다"),
    ("<code>&lt;ul&gt;</code>로 감싼다", "'목록, 항목 12개'가 읽힌다. <code>&lt;div&gt;</code>만 쌓으면 <b>몇 건인지 알 길이 없다</b>"),
    ("앞자리 아바타", "<code>aria-hidden=\"true\"</code> — 이름이 바로 옆에 또 있으므로 두 번 읽히면 시끄럽다"),
    ("뒤의 스위치", "줄 전체를 누르는 것과 <b>겹치지 않게</b> 한다. 보통 줄은 안 누르게 두고 스위치만 누른다"),
  ]),
  backend=rows([
    ("줄 하나 = 레코드 하나", "목록 API 의 한 행이 줄 하나입니다. 줄에 보이는 값은 <b>그 행 안에</b> 다 있어야 합니다 — 줄마다 이름을 따로 조회하면 N+1 입니다."),
    ("높이가 일정해야 하는 이유", "줄 높이가 같으면 <b>가상 스크롤</b>을 쓸 수 있어 수만 줄도 그립니다. 높이가 제각각이면 매 줄을 재야 해서 스크롤이 튑니다."),
    ("커서 페이징", "무한 스크롤로 이어 붙일 때 <code>offset</code>을 쓰면 새 글이 끼어들며 <b>같은 줄이 두 번</b> 나옵니다. 마지막 줄의 커서를 넘기는 쪽이 안전합니다."),
    ("빈 목록", "0건일 때 <b>빈 줄 하나</b>를 돌려주지 말고 빈 배열을 주고, 화면에서 <a href=\"../items/empty.html\">빈 상태</a>를 그립니다."),
  ]),
  plat_lede="목록은 세 플랫폼 모두 가장 기본 부품이고, 규격이 가장 또렷한 쪽이기도 합니다.",
  plats=plats([
    ("웹", "ul · li",
     row(AV, "정산 요청", "11월 1일~", CHEV, w="120px"),
     "표준 태그가 있습니다. 생김새는 전부 CSS 로 만들고, <b>세 자리</b>는 플렉스로 잡습니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 리스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px;background:var(--surface)">
                  <div style="display:flex;align-items:center;gap:5px;padding:5px 8px;font-size:7px"><span style="flex:1">알림</span><span style="color:var(--fg-faint)">›</span></div>
                  <div style="height:1px;background:var(--line);margin-left:8px"></div>
                  <div style="display:flex;align-items:center;gap:5px;padding:5px 8px;font-size:7px"><span style="flex:1">소리</span><span style="color:var(--fg-faint)">›</span></div>
                </div>
              </div></div>''',
     "줄을 <b>셀</b>(cell)이라 부릅니다. 구분선은 앞자리만큼 들여 긋고, <b>그룹 리스트</b>는 모서리가 둥급니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 리스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="display:flex;align-items:center;gap:5px;padding:6px 8px;font-size:7px"><span style="width:12px;height:12px;border-radius:99px;background:var(--accent-soft)"></span><span style="flex:1">정산 요청</span></div>
                  <div style="display:flex;align-items:center;gap:5px;padding:6px 8px;font-size:7px"><span style="width:12px;height:12px;border-radius:99px;background:var(--accent-soft)"></span><span style="flex:1">환불 확인</span></div>
                </div>
              </div></div>''',
     "<b>List</b> 가 정식 부품이고 <b>한 줄·두 줄·세 줄</b>마다 높이(56·72·88dp)가 규격에 박혀 있습니다."),
  ]),
  plat_note="iOS 의 <b>셀</b>과 안드로이드의 <b>리스트 아이템</b>은 같은 것입니다. 다만 두 OS 모두 <b>줄 높이가 규격</b>으로 정해져 있어서, 웹 시안의 어중간한 높이를 그대로 넘기면 \"표준에서 벗어난다\"는 말을 듣습니다. 줄 수(한 줄/두 줄/세 줄)로 이야기하면 세 쪽이 같은 말을 쓰게 됩니다.",
  siblings=siblings("listitem"),
  related='''        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>데이터 테이블</b><em>10부</em></span></li>''',
)
