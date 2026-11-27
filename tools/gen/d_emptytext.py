# -*- coding: utf-8 -*-
from ax14 import ax
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">왜 비었나 — 아직 없음 / 0건 / 못 봄 / 다 끝냄 / 실패</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">제목 한 줄 — 문장으로, 명사로 끝내지 않는다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">설명 한 줄 — 채우면 어떻게 되는지</div>
                  <div class="pin-out" data-pin="4" style="max-width:220px">''' + btn('가맹점 등록') + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">다 끝낸 것은 좋은 소식이다 — 버튼이 없어도 된다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘데이터가 없습니다’ — 다섯 경우를 한 문장으로 뭉갰다</div>
                </div>
              </div>'''

D = dict(
  slug="emptytext", ko="빈 상태 문구", en="Empty state copy",
  desc="왜 비었는지에 따라 할 말이 다르다. 아직 없음·0건·못 봄·다 끝냄·실패를 가르는 법.",
  lede="빈 화면은 한 가지가 아닙니다. <b>왜 비었는지</b>에 따라 할 말이 전혀 다릅니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>다섯 가지 빈 상태를 눌러 가며 봐 보세요 — 아직 만든 게 없을 때, 찾았는데 0건일 때,
          볼 수 없을 때, 다 끝냈을 때, 못 불러왔을 때.<br>
          <b>‘데이터가 없습니다’</b>는 이 다섯을 한 문장으로 뭉갠 말이라 <b>어느 경우에도 안 맞습니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "빈 상태 문구, 빈 화면 안내, 제로 스테이트"),
    ("영어", "empty state copy, zero state, blank slate"),
    ("같이 쓰는 말",
     "처음 와서 아무것도 없는 상태를 <b>제로 스테이트</b>·<b>블랭크 슬레이트</b>, "
     "그 자리를 설명으로 채우는 것을 <b>온보딩 빈 상태</b>라 부르기도 합니다. "
     "검색에서 아무것도 안 나온 것은 따로 <b>노 리절트</b>(no results)라 가릅니다."),
    ("자주 잘못 부름",
     "<b>빈 상태</b> — <a href=\"../items/empty.html\">빈 상태</a>는 <b>화면의 모습</b>, 이쪽은 <b>거기 적는 말</b>입니다.<br>"
     "<b>에러</b> — 못 불러온 것은 <b>비어 있는 게 아니라 실패한</b> 것입니다. 섞으면 사용자가 기다리지 않습니다.<br>"
     "<b>스켈레톤</b> — <a href=\"../items/skeleton.html\">스켈레톤</a>은 <b>아직 오는 중</b>입니다. 빈 상태는 <b>안 오는 것</b>입니다."),
  ]),
  axes=ax("빈 상태 문구"),
  oneline="<b>왜 비었는지부터 가르세요.</b> 다섯 경우는 다섯 가지 말이 필요하고, 하나로 쓰면 다섯 번 틀립니다.",
  s4_title="다섯 가지 빈 화면", s4_hint="왜 비었나",
  states=states([
    (mock('아직 등록한 가맹점이 없어요', '가맹점을 등록하면 정산이 여기 쌓입니다', '가맹점 등록', "152px", "처음 온 사람에게는 빈 화면이 첫 설명이다", True),
     "아직 없음", "<b>무엇을 하면 되는지</b> 적는다"),
    (mock('‘모란닭강정’에 맞는 가맹점이 없습니다', '철자를 확인하거나 조건을 줄여 보세요', '조건 지우기', "152px", "친 글자를 그대로 적는다", True),
     "찾았는데 0건", "<b>막다른 길</b>로 두지 않는다"),
    (mock('이 목록은 볼 수 없습니다', '가맹점 관리자만 볼 수 있어요', '관리자에게 요청', "152px", "없는 것과 못 보는 것은 다르다", True),
     "볼 수 없음", "없다고 하면 <b>엉뚱한 데를 찾는다</b>"),
    (mock('처리할 정산이 없습니다', '오늘 들어온 12건을 모두 끝내셨어요', '', "152px", "이건 좋은 소식이다", True),
     "다 끝냄", "<b>텅 빈 화면</b>으로 보이게 두지 않는다"),
    (mock('목록을 불러오지 못했습니다', '연결을 확인하고 다시 시도해 주세요', '다시 시도', "152px", "비어 있는 게 아니라 실패한 것", True),
     "못 불러옴", "<a href=\"errortext.html\">오류 문구</a>로 넘어간다"),
    (mock('데이터가 없습니다', '', '', "152px", "다섯 경우를 한 문장으로 뭉갰다", False),
     "뭉갠 문구", "<b>어느 경우에도 안 맞는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("왜 비었나", "다섯 갈래", "<b>이걸 먼저 가르지</b> 않으면 문구를 못 쓴다"),
    ("제목", "문장으로", "'아직 등록한 가맹점이 없어요'. <b>명사로 끝내지 않는다</b>"),
    ("설명", "채우면 어떻게 되나", "'등록하면 정산이 여기 쌓입니다'"),
    ("버튼", "할 수 있는 일 하나", "<b>하나만.</b> 셋을 늘어놓으면 아무것도 안 고른다"),
    ("좋은 소식", "다 끝냈을 때", "버튼이 없어도 된다. <b>칭찬하는 자리</b>다"),
    ("뭉갠 문구", "데이터가 없습니다", "다섯을 한 말로 — <b>가장 흔한 실수</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>그림을 크게 그리는 것보다 문장 하나가 낫습니다.</b>
          빈 상태 시안에는 큰 일러스트가 자주 들어오는데,
          사용자가 거기서 원하는 것은 <b>'왜 비었고 뭘 하면 되나'</b>입니다.
          그림은 그 답을 못 합니다.
          그리고 처음 온 사람에게 이 화면은 <b>제품의 첫 설명</b>이기도 합니다 —
          <a href="onboarding.html">온보딩</a>으로 따로 묻는 대신
          여기서 한 줄로 알려 주면 단계 하나가 통째로 사라집니다.</p>''',
  do=ul([
    "<b>왜 비었는지</b>부터 가르기",
    "채우면 어떻게 되는지 <b>한 줄</b>",
    "할 수 있는 일을 <b>버튼 하나</b>로",
  ]),
  dont=ul([
    "‘데이터가 없습니다’ — 다섯을 한 말로 뭉갠다",
    "실패를 빈 상태로 보이게 하기 — <b>기다리지 않게</b> 된다",
    "큰 그림만 두고 <b>할 일은 안 적기</b>",
    "다 끝낸 화면을 <b>텅 빈 것</b>처럼 보여 주기",
  ]),
  instead='화면 모습은 <a href="../items/empty.html">빈 상태</a>, 실패면 <a href="errortext.html">오류 문구</a>, 아직 오는 중이면 <a href="../items/skeleton.html">스켈레톤</a>.',
  cases=cases([
    (mock('아직 등록한 가맹점이 없어요', '등록하면 정산이 여기 쌓입니다', '가맹점 등록', "150px"), "첫 화면", "<b>제품의 첫 설명</b>이 되는 자리"),
    (mock('‘모란닭강정’에 맞는 것이 없습니다', '조건을 줄여 보세요', '조건 지우기', "150px"), "0건", "<a href=\"searchresults.html\">검색 결과</a>에서"),
    (mock('처리할 정산이 없습니다', '오늘 12건을 모두 끝내셨어요', '', "150px"), "다 끝냄", "<b>좋은 소식</b>으로 적는다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 문구의 계약서",
  code_lede="빈 상태도 <b>제목이 있는 구역</b>입니다.",
  code='''&lt;<span class="t">section</span> <span class="a">aria-labelledby</span>=<span class="s">"e-t"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"empty.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;        <span class="c">&lt;!-- 장식이면 alt 를 비운다 --&gt;</span>
  &lt;<span class="t">h2</span> <span class="a">id</span>=<span class="s">"e-t"</span>&gt;아직 등록한 가맹점이 없어요&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span>&gt;가맹점을 등록하면 정산이 여기 쌓입니다.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"btn"</span> <span class="a">href</span>=<span class="s">"/stores/new"</span>&gt;가맹점 등록&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">section</span>&gt;

<span class="c">&lt;!-- 검색 0건은 결과 수를 함께 알린다 --&gt;</span>
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;‘모란닭강정’ 검색 결과 0건&lt;/<span class="t">p</span>&gt;''',
  keys=kbd([
    ("<code>&lt;h2&gt;</code>로 적는다", "구역의 제목이다. <b>건너뛰어 읽을</b> 수 있게 된다"),
    ("그림은 <code>alt=\"\"</code>", "장식이면 비운다. <b>'빈 상자 그림'</b>을 읽어 줘 봐야 쓸모없다"),
    ("<code>role=\"status\"</code>", "0건으로 바뀐 것을 알린다. <b>목록만 비면</b> 눈으로 안 보는 사람은 모른다"),
    ("초점", "검색 0건일 때 <b>초점을 옮기지 않는다.</b> 계속 치고 있을 수 있다"),
    ("버튼은 <code>&lt;a&gt;</code>일 수도", "이동이면 링크, 동작이면 버튼 — <a href=\"../items/semantics.html\">시맨틱 태그</a>"),
    ("대비비", "빈 상태 글은 <b>흐리게 쓰기 쉽다.</b> 4.5:1 을 지킨다 — <a href=\"../items/contrast.html\">대비비</a>"),
  ]),
  backend=rows([
    ("왜 비었는지를 함께 보낸다", "<code>{\"items\":[],\"reason\":\"no_permission\"}</code>. 빈 배열만 오면 화면이 <b>다섯 경우를 못 가릅니다</b>."),
    ("0건과 실패를 가른다", "실패를 빈 배열로 돌려주면 <b>'없다'고 거짓말</b>하게 됩니다."),
    ("조건을 함께 돌려준다", "0건일 때 <b>무엇으로 찾았는지</b>를 받아야 '‘모란닭강정’에 맞는 것이 없습니다'라고 쓸 수 있습니다."),
    ("처음 온 계정인지", "'아직 없음'과 '다 지움'은 다릅니다. <b>한 번이라도 만든 적이 있는지</b>를 알면 문구가 달라집니다."),
  ]),
  plat_lede="<b>문구 + 버튼 하나</b>라는 꼴은 셋이 같습니다.",
  plats=plats([
    ("웹", "섹션으로",
     mock('아직 없어요', '등록하면 쌓입니다', '등록', "110px"),
     "제목·설명·버튼. 그림은 선택입니다. <b>0건은 따로</b> 다룹니다."),
    ("iOS", "ContentUnavailableView",
     '''              <div class="phone" role="img" aria-label="iOS 빈 상태 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:6px">아직 없어요<br><span style="color:var(--fg-muted);font-size:5px">등록하면 쌓입니다</span></div></div></div>''',
     "OS 가 <b>정식 부품</b>을 줍니다. 아이콘·제목·설명·버튼 자리가 정해져 있습니다."),
    ("안드로이드", "Material",
     '''              <div class="phone" role="img" aria-label="안드로이드 빈 상태 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:6px">아직 없어요</div></div></div>''',
     "정해진 부품은 없고 <b>짧게 쓰라</b>는 지침이 있습니다. 그림을 크게 넣지 말라고 적어 두었습니다."),
  ]),
  plat_note="빈 상태는 <b>시연에서 안 보이는 화면</b>입니다 — 시연용 계정에는 데이터가 가득하기 때문입니다. 그래서 '데이터가 없습니다'가 끝까지 남고, <b>처음 온 사람만</b> 그 화면을 봅니다. 기능을 만들 때 <b>비어 있는 계정으로 한 번 열어 보는</b> 것이 이 항목의 유일한 점검법입니다.",
  siblings=siblings("emptytext"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="searchresults.html"><b>검색 결과 화면</b><em>13부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
