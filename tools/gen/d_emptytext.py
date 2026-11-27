# -*- coding: utf-8 -*-
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def mock(h, p, act="", w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--bg);padding:12px 8px;'
            'text-align:center;display:grid;gap:3px;place-items:center">'
            '<span style="font-size:9.5px;font-weight:700">' + h + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted);max-width:22ch">' + p + '</span>' if p else '')
            + (btn(act) if act else '') + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">왜 비었는지 가름(아직 없음 / 0건 / 못 봄 / 다 끝냄 / 실패)</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">제목 한 줄은 명사로 끝내지 않고 문장으로</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">설명 한 줄에는 채우면 어떻게 되는지</div>
                  <div class="pin-out" data-pin="4" style="max-width:220px">''' + btn('가맹점 등록') + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">다 끝낸 화면은 좋은 소식이라 버튼이 없어도 됨</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘데이터가 없습니다’는 다섯 경우를 한 문장으로 뭉뚱그림</div>
                </div>
              </div>'''

D = dict(
  slug="emptytext", ko="빈 상태 문구", en="Empty state copy",
  desc="화면이 왜 비었는지에 따라 적을 말이 달라집니다. 아직 없음·0건·못 봄·다 끝냄·실패를 가려 쓰는 방법을 다룹니다.",
  lede="빈 화면에 적을 말은 <b>왜 비었는지</b>에 따라 전혀 다릅니다. 아직 만든 것이 없을 때와 검색 결과가 0건일 때, 불러오지 못했을 때는 사용자가 할 일이 서로 다르기 때문입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>아직 만든 것이 없을 때, 찾았는데 0건일 때, 볼 수 없을 때,
          다 끝냈을 때, 불러오지 못했을 때까지 다섯 가지 빈 상태를 눌러 가며 견줘 보세요.<br>
          <b>‘데이터가 없습니다’</b>는 이 다섯 경우를 한 문장으로 뭉뚱그린 말이라서 <b>어느 경우에도 맞지 않습니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "빈 상태 문구, 빈 화면 안내, 제로 스테이트"),
    ("영어", "empty state copy, zero state, blank slate"),
    ("같이 쓰는 말",
     "처음 들어와 아직 아무것도 없는 상태는 <b>제로 스테이트</b>·<b>블랭크 슬레이트</b>라고 하고, "
     "그 자리를 사용법 설명으로 채운 것을 <b>온보딩 빈 상태</b>라고 부르기도 합니다. "
     "검색 결과가 하나도 없는 경우는 따로 <b>노 리절트</b>(no results)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>빈 상태</b> — <a href=\"../items/empty.html\">빈 상태</a>는 비어 있는 <b>화면 모습</b>이고, 빈 상태 문구는 <b>그 화면에 적는 말</b>입니다.<br>"
     "<b>에러</b> — 목록을 불러오지 못한 것은 <b>비어 있는 것이 아니라 실패한</b> 것입니다. 실패를 빈 상태처럼 보여 주면 사용자는 원래 없는 줄 알고 기다리거나 다시 시도하지 않습니다.<br>"
     "<b>스켈레톤</b> — <a href=\"../items/skeleton.html\">스켈레톤</a>은 내용을 <b>아직 불러오는 중</b>일 때 보여 주고, 빈 상태는 불러온 결과에 <b>보여 줄 내용이 없을</b> 때 보여 줍니다."),
  ]),
  s4_title="다섯 가지 빈 화면", s4_hint="비어 있는 이유에 따라 달라지는 문구",
  states=states([
    (mock('아직 등록한 가맹점이 없어요', '가맹점을 등록하면 정산이 여기 쌓입니다', '가맹점 등록', "152px", "처음 온 사람에게는 빈 화면이 첫 설명이 됨", True),
     "아직 만든 것이 없을 때", "<b>무엇을 하면 되는지</b> 적습니다"),
    (mock('‘모란닭강정’에 맞는 가맹점이 없습니다', '철자를 확인하거나 조건을 줄여 보세요', '조건 지우기', "152px", "사용자가 친 검색어를 그대로 적음", True),
     "찾았는데 0건일 때", "조건을 바꾸는 방법을 알려 주고, <b>더 할 일이 없는 화면</b>으로 두지 않습니다"),
    (mock('이 목록은 볼 수 없습니다', '가맹점 관리자만 볼 수 있어요', '관리자에게 요청', "152px", "없는 것과 못 보는 것은 다름", True),
     "볼 권한이 없을 때", "권한이 없는 것을 내용이 없다고 적으면 사용자가 <b>엉뚱한 곳을 찾아다닙니다</b>"),
    (mock('처리할 정산이 없습니다', '오늘 들어온 12건을 모두 끝내셨어요', '', "152px", "할 일을 다 끝낸 좋은 소식", True),
     "할 일을 다 끝냈을 때", "할 일을 모두 끝낸 상태이므로 <b>텅 빈 화면</b>처럼 보이게 두지 않습니다"),
    (mock('목록을 불러오지 못했습니다', '연결을 확인하고 다시 시도해 주세요', '다시 시도', "152px", "비어 있는 게 아니라 실패한 것", True),
     "불러오지 못했을 때", "비어 있는 것이 아니라 실패한 것이므로 <a href=\"errortext.html\">오류 문구</a>로 다룹니다"),
    (mock('데이터가 없습니다', '', '', "152px", "다섯 경우를 한 문장으로 뭉뚱그림", False),
     "다섯 경우를 뭉뚱그린 문구", "다섯 경우 <b>어디에도 맞지 않습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("왜 비었나", "다섯 가지 경우", "<b>왜 비었는지를 먼저 가르지</b> 않으면 알맞은 문구를 쓸 수 없습니다"),
    ("제목", "문장으로", "'아직 등록한 가맹점이 없어요'처럼 문장으로 쓰고 <b>명사로 끝내지 않습니다</b>"),
    ("설명", "채우면 어떻게 되나", "'등록하면 정산이 여기 쌓입니다'처럼 채우고 나면 어떻게 되는지 적습니다"),
    ("버튼", "할 수 있는 일 하나", "할 수 있는 일을 <b>하나만</b> 버튼으로 둡니다. 버튼 셋을 늘어놓으면 사용자가 어느 것도 고르지 않기 쉽습니다"),
    ("좋은 소식", "다 끝냈을 때", "버튼이 없어도 됩니다. 일을 다 끝낸 것을 알려 주고 <b>칭찬하는 자리</b>입니다"),
    ("뭉뚱그린 문구", "데이터가 없습니다", "다섯 경우를 한 문장으로 뭉뚱그린 문구로, <b>가장 흔한 실수</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>빈 화면에는 큰 그림보다 문장 한 줄이 더 쓸모 있습니다.</b>
          빈 상태 시안에는 큰 일러스트가 자주 들어가지만,
          사용자가 그 화면에서 알고 싶은 것은 <b>'왜 비었고 무엇을 하면 되나'</b>이고
          그림만으로는 이 물음에 답할 수 없습니다.
          또 처음 온 사람에게 빈 화면은 <b>제품을 처음 설명하는 자리</b>이기도 합니다.
          <a href="onboarding.html">온보딩</a> 단계를 따로 두는 대신
          빈 화면에 한 줄로 사용법을 알려 주면 온보딩 단계를 하나 줄일 수 있습니다.</p>''',
  do=ul([
    "<b>왜 비었는지</b>부터 가르기",
    "채우면 어떻게 되는지 <b>한 줄</b>로 적기",
    "할 수 있는 일을 <b>버튼 하나</b>로 두기",
  ]),
  do_title="빈 상태 문구를 쓸 때 지킬 것", dont_title="빈 상태 문구에서 피할 것",
  instead_title="빈 상태 문구와 함께 보면 좋은 항목",
  dont=ul([
    "‘데이터가 없습니다’라고 적을 때. 다섯 경우를 한 문장으로 뭉뚱그린 말입니다",
    "불러오기 실패를 빈 상태처럼 보여 줄 때. 사용자가 원래 없는 줄 알고 <b>기다리지 않게</b> 됩니다",
    "큰 그림만 두고 <b>할 일은 적지 않을 때</b>",
    "다 끝낸 화면을 <b>텅 빈 것</b>처럼 보여 줄 때",
  ]),
  instead='비어 있는 화면의 모습은 <a href="../items/empty.html">빈 상태</a>에서 다룹니다. 불러오기에 실패했다면 <a href="errortext.html">오류 문구</a>를 쓰고, 내용이 아직 오는 중이라면 <a href="../items/skeleton.html">스켈레톤</a>을 보여 줍니다.',
  cases=cases([
    (mock('아직 등록한 가맹점이 없어요', '등록하면 정산이 여기 쌓입니다', '가맹점 등록', "150px"), "처음 온 사용자의 첫 화면", "처음 온 사용자에게 <b>제품을 처음 설명하는</b> 자리입니다"),
    (mock('‘모란닭강정’에 맞는 것이 없습니다', '조건을 줄여 보세요', '조건 지우기', "150px"), "검색 결과가 0건인 화면", "<a href=\"searchresults.html\">검색 결과</a> 화면에서 씁니다"),
    (mock('처리할 정산이 없습니다', '오늘 12건을 모두 끝내셨어요', '', "150px"), "할 일을 다 끝낸 화면", "할 일을 다 끝냈다는 <b>좋은 소식</b>으로 적습니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="빈 상태도 <b>제목이 있는 구역</b>으로 마크업합니다.",
  code='''&lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"e-t"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"empty.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;        <span class="c">&lt;!-- 장식이면 alt 를 비운다 --&gt;</span>
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"e-t"</span>&gt;아직 등록한 가맹점이 없어요&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span>&gt;가맹점을 등록하면 정산이 여기 쌓입니다.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"btn"</span> <span class="a">href</span>=<span class="s">"/stores/new"</span>&gt;가맹점 등록&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">section</span>&gt;

<span class="c">&lt;!-- 검색 0건은 결과 수를 함께 알린다 --&gt;</span>
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;‘모란닭강정’ 검색 결과 0건&lt;/<span class="t">p</span>&gt;''',
  keys_heads="<th>지킬 규칙과 마크업</th><th>지키는 방법과 이유</th>",
  keys=kbd([
    ("제목은 <code>&lt;h2&gt;</code>로 적기", "빈 상태 문구의 제목을 구역 제목으로 적으면, 스크린 리더 사용자가 제목 단위로 <b>건너뛰며 읽을</b> 수 있습니다"),
    ("장식 그림은 <code>alt=\"\"</code>로 비우기", "장식용 그림이면 alt를 비웁니다. 스크린 리더가 <b>'빈 상자 그림'</b>이라고 읽어 줘도 사용자에게 도움이 되지 않습니다"),
    ("<code>role=\"status\"</code>", "검색 결과가 0건으로 바뀐 것을 알립니다. <b>목록만 비우면</b> 화면을 눈으로 보지 않는 사용자는 결과가 없다는 것을 알 수 없습니다"),
    ("0건일 때의 초점", "검색 결과가 0건이어도 <b>초점을 옮기지 않습니다.</b> 사용자가 아직 검색어를 치고 있을 수 있기 때문입니다"),
    ("버튼 대신 <code>&lt;a&gt;</code>를 쓸 때", "다른 화면으로 이동하면 링크로, 그 자리에서 동작하면 버튼으로 만듭니다(<a href=\"../items/semantics.html\">시맨틱 태그</a>)"),
    ("흐린 글자의 대비비", "빈 상태 글은 <b>흐린 색으로 쓰기 쉬운데</b>, 그래도 대비비 4.5:1은 지킵니다(<a href=\"../items/contrast.html\">대비비</a>)"),
  ]),
  backend=rows([
    ("왜 비었는지를 함께 보내기", "<code>{\"items\":[],\"reason\":\"no_permission\"}</code>처럼 이유를 함께 보냅니다. 빈 배열만 오면 화면이 <b>다섯 경우를 가를 수 없습니다</b>."),
    ("0건과 실패 구별하기", "불러오기에 실패했는데 빈 배열을 돌려주면, 화면은 실제로는 있을 수 있는 내용을 <b>'없다'고 잘못 알리게</b> 됩니다."),
    ("검색 조건을 함께 돌려주기", "0건일 때 <b>어떤 조건으로 찾았는지</b>를 함께 받아야 화면에 '‘모란닭강정’에 맞는 것이 없습니다'라고 쓸 수 있습니다."),
    ("처음 온 계정인지 알려 주기", "처음부터 아무것도 없는 '아직 없음'과 만들었다가 모두 지운 '다 지움'은 다른 상황입니다. 서버가 <b>한 번이라도 만든 적이 있는지</b>를 알려 주면 화면이 두 경우에 맞는 문구를 따로 쓸 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 빈 상태를 <b>문구와 버튼 하나</b>로 구성합니다.",
  plats=plats([
    ("웹", "섹션으로",
     mock('아직 없어요', '등록하면 쌓입니다', '등록', "110px"),
     "제목과 설명, 버튼으로 구성하고 그림은 넣어도 되고 빼도 됩니다. 검색 결과 <b>0건은 따로</b> 다룹니다."),
    ("iOS", "ContentUnavailableView",
     '''              <div class="phone" role="img" aria-label="iOS 빈 상태 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:6px">아직 없어요<br><span style="color:var(--fg-muted);font-size:5px">등록하면 쌓입니다</span></div></div></div>''',
     "OS가 빈 상태용 <b>정식 부품</b>을 제공하고, 아이콘·제목·설명·버튼 자리가 정해져 있습니다."),
    ("안드로이드", "Material",
     '''              <div class="phone" role="img" aria-label="안드로이드 빈 상태 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:6px">아직 없어요</div></div></div>''',
     "정해진 부품은 없고, 문구를 <b>짧게 쓰라</b>는 지침과 그림을 크게 넣지 말라는 지침이 있습니다."),
  ]),
  plat_note="시연용 계정에는 데이터가 가득하기 때문에 빈 상태는 <b>시연에서 거의 보이지 않습니다</b>. 그래서 '데이터가 없습니다' 같은 문구가 출시 뒤까지 남고, 그 화면은 <b>처음 온 사용자만</b> 보게 됩니다. 기능을 만들 때 <b>비어 있는 계정으로 한 번 열어 보면</b> 이런 문구를 미리 찾아 고칠 수 있습니다.",
  siblings=siblings("emptytext"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
