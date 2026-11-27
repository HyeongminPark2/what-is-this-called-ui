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
                  <div class="pin-out" data-pin="2" style="font-size:11px;color:var(--fg-muted)">줄 하나 전체가 <b style="color:var(--fg)">하나의 누를 것</b>임</div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span style="width:26px;height:26px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:10px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                    <span>앞자리는 <b style="color:var(--fg)">폭이 고정됨</b></span>
                  </div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted)">가운데는 <b style="color:var(--fg)">이 자리만 늘어남</b></div>
                  <div class="pin-out" data-pin="5" style="height:1px;background:var(--line-strong)"></div>
                  <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted);background:var(--surface);border-radius:6px;padding:5px 9px;justify-self:start">이번 주</div>
                </div>
              </div>'''

D = dict(
  slug="listitem", ko="리스트 아이템", en="List item · row",
  desc="리스트 아이템을 이루는 세 자리(앞·가운데·뒤)와 말줄임, 카드와의 차이를 실물과 해부도로 보여 주는 항목입니다.",
  lede="리스트 아이템은 목록에서 <b>한 줄에 한 건</b>을 담는 부품입니다. 담는 내용은 카드와 같지만, 여러 건을 세로로 훑어 비교하기 좋도록 줄을 가지런히 맞춰 둔다는 점이 다릅니다.",
  axes_lede="표시 부품은 모두 보여 주기만 합니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>줄 수를 바꿔 보고, <b>긴 글을 자르지 말고 접기</b>를 켜 보세요. 글이 모두 보이는 대신
          줄마다 높이가 달라집니다. 목록에서는 보통 <b>자르는 쪽</b>을 고릅니다.
          줄 높이가 일정해야 세로로 훑어 읽기 쉽고, 가상 스크롤도 높이가 일정할 때만 쓸 수 있기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "리스트 아이템, 목록 항목, 줄, 행"),
    ("영어", "list item, row, list row, cell(iOS)"),
    ("같이 쓰는 말",
     "줄 앞쪽의 아이콘이나 아바타 자리는 <b>리딩</b>(leading), 뒤쪽의 값이나 꺾쇠 자리는 <b>트레일링</b>(trailing)이라고 부릅니다.  "
     "줄 사이를 나누는 선은 <b>디바이더</b>(divider · separator), 여러 줄을 묶는 머리글은 <b>섹션 헤더</b>라고 합니다.  "
     "글이 몇 줄 들어가느냐에 따라 <b>한 줄·두 줄·세 줄</b>(one/two/three-line) 리스트 아이템으로 나눠 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>카드</b> — 가로형 카드와는 생김새가 거의 같아서, 둘을 가르는 기준은 생김새가 아니라 <b>여러 건이 어떻게 모이느냐</b>입니다.<br>"
     "<b>테이블 행</b> — 표의 행은 <b>열이 정해져</b> 있고 정렬과 선택 기능이 따라옵니다. 반면 리스트 아이템에는 내용을 자유롭게 넣는 세 자리만 있습니다.<br>"
     "<b>메뉴 아이템</b> — 메뉴는 하나를 누르면 메뉴째 <b>닫히는</b> 선택지 모음입니다. 리스트는 선택지가 아니라 화면에 보여 줄 내용 자체입니다."),
  ]),
  axes=ax("리스트 아이템"),
  oneline="리스트 아이템은 여러 건을 <b>세로로 비교하기 쉽도록</b> 줄을 맞춘 것입니다. 그래서 줄 높이가 제각각이면 세로로 훑어 비교하기 어려워져 리스트를 쓰는 의미가 줄어듭니다.",
  s4_title="상태", s4_hint="상태마다 달라지는 줄의 모습",
  states=states([
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV), "기본 구성", "앞, 가운데, 뒤의 <b>세 자리</b>로 이루어집니다"),
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV, style="background:var(--bg)"),
     "마우스를 올렸을 때", "<b>줄 전체</b>의 바탕색이 바뀌어 어디까지가 한 줄인지 알려 줍니다"),
    (row(AV, "정산 요청 #4821", "11월 1일 ~ 11월 7일", CHEV, style="outline:2px solid var(--accent);outline-offset:-2px"),
     "키보드로 포커스가 왔을 때", "포커스 테두리를 줄 <b>안쪽</b>에 그립니다. 바깥에 그리면 이웃한 줄을 덮기 때문입니다"),
    (row('<span style="width:14px;height:14px;border:1.5px solid var(--accent);background:var(--accent);border-radius:3px;flex:none;display:grid;place-items:center;color:#fff;font-size:9px">✓</span>',
         "정산 요청 #4821", "11월 1일 ~ 11월 7일", "", style="background:var(--accent-soft)"),
     "줄을 골랐을 때", "<b>앞자리에 체크박스</b>가 들어오고, 고른 줄은 바탕색이 바뀝니다"),
    (row(AV, "환불 확인 요청 — 카드 승인 취소가 늦어", "주문 TX-99120 · 승인 취소 대기", CHEV),
     "글이 길 때", "글이 한 줄을 넘지 않도록 <b>말줄임표(…)로 자르고</b>, 전체 내용은 상세 화면에서 보여 줍니다"),
    ('''              <div style="width:100%;max-width:168px;border:1px solid var(--line);border-radius:8px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px 9px">
                <span class="skl" style="width:22px;height:22px;border-radius:99px;flex:none"></span>
                <span style="flex:1;display:grid;gap:4px"><span class="skl" style="height:8px;width:70%"></span><span class="skl" style="height:7px;width:45%"></span></span>
              </div>''',
     "내용을 불러오는 중", "뼈대를 <b>실제 줄과 같은 높이</b>로 그립니다. 높이가 다르면 내용이 들어오는 순간 목록이 위아래로 밀립니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("목록", "list", "줄들을 감싸는 상자입니다. <code>&lt;ul&gt;</code>로 만들어야 스크린 리더가 모두 몇 건인지 읽어 줍니다"),
    ("줄", "list item · row", "한 건 전체를 <b>하나의 누를 것</b>으로 만듭니다. 제목만 링크로 두지 않습니다"),
    ("앞자리", "leading", "아바타, 아이콘, 체크박스가 들어갑니다. <b>폭을 고정</b>해야 줄끼리 세로로 가지런히 맞습니다"),
    ("가운데", "primary · secondary text", "제목과 보조 글이 들어갑니다. 세 자리 가운데 <b>여기만 늘어납니다</b>(<code>flex:1; min-width:0</code>)"),
    ("구분선", "divider", "줄 사이를 나누는 선입니다. 아바타가 있으면 보통 <b>앞자리 폭만큼 들여서</b> 긋습니다"),
    ("섹션 헤더", "section header", "'이번 주'처럼 여러 줄을 묶는 머리글입니다. 스크롤해도 화면 위쪽에 붙어 있게 만들기도 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          가운데 자리에 <code>min-width: 0</code>을 주지 않으면 말줄임이 <b>끝내 적용되지 않습니다.</b>
          플렉스나 그리드 자식의 기본 최소 너비가 '내용 길이만큼'이라서, 글이 길면 가운데 칸이 계속 넓어지면서
          뒤쪽의 값과 꺾쇠를 화면 밖으로 밀어내기 때문입니다. 리스트에서 특히 자주 생기는 레이아웃 오류입니다.</p>''',
  do=ul([
    "건이 많고 <b>같은 모양</b>으로 반복될 때",
    "세로로 훑으며 <b>찾거나 비교</b>할 때",
    "화면이 좁을 때. 카드보다 한 화면에 훨씬 많은 건이 들어갑니다",
    "설정처럼 <b>이름과 값의 짝</b>이 늘어설 때",
  ]),
  dont=ul([
    "사진을 보고 골라야 할 때. <a href=\"card.html\">카드</a>가 더 낫습니다",
    "열을 기준으로 정렬하거나 여러 값을 비교해야 할 때. 데이터 테이블을 씁니다",
    "줄마다 보여 줄 것이 너무 많을 때. 세 자리에 다 들어가지 않으면 <b>리스트 아이템이 아니라 카드</b>로 만듭니다",
  ]),
  instead='사진을 보고 골라야 하면 <a href="card.html">카드</a>를 쓰고, 열을 기준으로 정렬하거나 비교해야 하면 데이터 테이블(10부)을 씁니다. 누르면 닫히는 선택지 모음이라면 메뉴(6부)가 맞습니다.',
  cases=cases([
    (row(AV, "김철수", "네, 오후에 확인해 볼게요", '<span style="font-size:9.5px;color:var(--fg-muted);flex:none">14:02</span>', w="180px"),
     "메신저의 대화 목록", "앞에 아바타, 뒤에 보낸 시각을 둡니다. <b>메신저 첫 화면</b>에서 흔히 봅니다"),
    (row('<span style="width:22px;height:22px;border-radius:6px;background:var(--bg);flex:none"></span>',
         "알림", "", '<span style="width:30px;height:17px;border-radius:99px;background:var(--accent);flex:none;position:relative"><span style="position:absolute;right:2px;top:2px;width:13px;height:13px;border-radius:99px;background:#fff"></span></span>', w="180px"),
     "설정 화면의 스위치 줄", "뒤에 스위치가 옵니다. 줄 전체를 누르게 할지, <b>스위치만</b> 눌리게 할지 정해야 합니다"),
    (row('<span style="width:22px;height:22px;border-radius:4px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 5px,var(--ink-050) 5px 10px);flex:none"></span>',
         "접이식 캠핑 의자", "한빛아웃도어 · 1개", '<span style="font-size:10px;font-weight:700;flex:none">₩58,000</span>', w="180px"),
     "주문 내역의 금액 줄", "뒤에 금액이 옵니다. <b>금액은 오른쪽으로 맞추고</b> 자릿수도 맞춥니다"),
  ]),
  s8_title="최소 마크업과 키보드",
  code_lede="목록은 <code>&lt;ul&gt;</code>과 <code>&lt;li&gt;</code>로 만듭니다. 그래야 스크린 리더가 <b>'목록, 항목 3개 중 1번'</b>처럼 몇 번째 건인지 읽어 줍니다.",
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

<span class="c">/* min-width: 0 이 없으면 말줄임이 적용되지 않는다 */</span>
<span class="t">.li__main</span> { <span class="a">flex</span>: <span class="a">1</span>; <span class="a">min-width</span>: <span class="a">0</span>; }
<span class="t">.li__t</span> { <span class="a">overflow</span>: hidden; <span class="a">text-overflow</span>: ellipsis; <span class="a">white-space</span>: nowrap; }''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "포커스가 줄마다 <b>한 번</b> 멈춥니다. 줄 안에 누를 것이 둘이면 두 번 멈춥니다"),
    ("<kbd>Enter</kbd>", "포커스가 있는 줄을 엽니다"),
    ("<code>&lt;ul&gt;</code>로 감쌌을 때", "스크린 리더가 '목록, 항목 12개'라고 읽어 줍니다. <code>&lt;div&gt;</code>만 쌓으면 <b>몇 건인지 알 수 없습니다</b>"),
    ("앞자리에 아바타가 있을 때", "<code>aria-hidden=\"true\"</code>을 붙입니다. 바로 옆에 이름이 또 있어서 아바타까지 읽으면 이름을 두 번 듣게 됩니다"),
    ("뒤에 스위치가 있을 때", "줄 전체를 누르는 동작과 <b>겹치지 않게</b> 합니다. 보통 줄은 눌리지 않게 두고 스위치만 누르게 합니다"),
  ]),
  backend=rows([
    ("줄 하나는 레코드 하나", "목록 API가 돌려주는 한 행이 줄 하나가 됩니다. 줄에 보이는 값은 <b>그 행 안에</b> 모두 들어 있어야 하는데, 줄마다 이름을 따로 조회하면 N+1 문제(목록 1번에 줄 수만큼 추가 조회)가 생기기 때문입니다."),
    ("높이가 일정해야 하는 이유", "줄 높이가 같으면 화면에 보이는 줄만 그리는 <b>가상 스크롤</b>을 쓸 수 있어서 수만 줄도 그릴 수 있습니다. 반면 높이가 제각각이면 줄마다 높이를 재야 해서 스크롤 위치가 갑자기 건너뜁니다."),
    ("무한 스크롤에는 커서 페이징", "무한 스크롤로 목록을 이어 붙일 때 <code>offset</code>을 쓰면, 그사이 새 글이 앞에 끼어들어 <b>같은 줄이 두 번</b> 나옵니다. 그래서 마지막 줄의 커서를 넘겨 다음 묶음을 받는 쪽이 안전합니다."),
    ("결과가 없을 때 돌려줄 값", "결과가 0건이면 <b>빈 줄 하나</b>를 돌려주지 말고 빈 배열을 돌려준 뒤, 화면에서 <a href=\"../items/empty.html\">빈 상태</a>를 그립니다."),
  ]),
  plat_lede="목록은 세 플랫폼 모두에서 가장 기본이 되는 부품이고, 규격도 특히 또렷하게 정해져 있습니다.",
  plats=plats([
    ("웹", "ul · li",
     row(AV, "정산 요청", "11월 1일~", CHEV, w="120px"),
     "표준 태그가 있습니다. 생김새는 모두 CSS로 만들고, <b>세 자리</b>는 플렉스로 배치합니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 리스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px;background:var(--surface)">
                  <div style="display:flex;align-items:center;gap:5px;padding:5px 8px;font-size:7px"><span style="flex:1">알림</span><span style="color:var(--fg-faint)">›</span></div>
                  <div style="height:1px;background:var(--line);margin-left:8px"></div>
                  <div style="display:flex;align-items:center;gap:5px;padding:5px 8px;font-size:7px"><span style="flex:1">소리</span><span style="color:var(--fg-faint)">›</span></div>
                </div>
              </div></div>''',
     "줄을 <b>셀</b>(cell)이라고 부릅니다. 구분선은 앞자리 폭만큼 들여서 긋고, <b>그룹 리스트</b>는 모서리가 둥급니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 리스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px">
                  <div style="display:flex;align-items:center;gap:5px;padding:6px 8px;font-size:7px"><span style="width:12px;height:12px;border-radius:99px;background:var(--accent-soft)"></span><span style="flex:1">정산 요청</span></div>
                  <div style="display:flex;align-items:center;gap:5px;padding:6px 8px;font-size:7px"><span style="width:12px;height:12px;border-radius:99px;background:var(--accent-soft)"></span><span style="flex:1">환불 확인</span></div>
                </div>
              </div></div>''',
     "<b>List</b>가 정식 부품으로 있고, <b>한 줄·두 줄·세 줄</b>마다 높이(56·72·88dp)가 규격으로 정해져 있습니다."),
  ]),
  plat_note="iOS의 <b>셀</b>과 안드로이드의 <b>리스트 아이템</b>은 같은 부품입니다. 다만 두 OS 모두 <b>줄 높이를 규격</b>으로 정해 두었기 때문에, 규격에 맞지 않는 웹 시안의 줄 높이를 그대로 넘기면 \"표준에서 벗어난다\"는 말을 듣습니다. 줄 높이 대신 줄 수(한 줄/두 줄/세 줄)로 이야기하면 웹, iOS, 안드로이드가 같은 기준으로 이야기할 수 있습니다.",
  siblings=siblings("listitem"),
  related='''        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
