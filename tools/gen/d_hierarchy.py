# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def hi(flat=False, no_size=False, no_weight=False, no_color=False, w="160px", label=""):
    def st(size, weight, color):
        if flat:
            return "font-size:12px;font-weight:500;color:var(--fg)"
        s = []
        s.append("font-size:" + ("12px" if no_size else size))
        s.append("font-weight:" + ("500" if no_weight else weight))
        s.append("color:" + ("var(--fg)" if no_color else color))
        return ";".join(s)
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);padding:9px;display:grid;gap:3px">'
            '<span style="' + st("9.5px", "700", "var(--fg-faint)") + ';letter-spacing:.04em">11월 1주</span>'
            '<span style="' + st("15px", "800", "var(--fg)") + ';line-height:1.3">정산 요청 #4821</span>'
            '<span style="' + st("10.5px", "400", "var(--fg-muted)") + '">모란상회 · 홍길동</span>'
            '<span style="' + st("11px", "400", "var(--fg)") + ';line-height:1.7">수수료를 뺀 ₩1,245,480이 입금됩니다.</span>'
            '</div>'
            + ('<div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center;margin-top:6px">' + label + '</div>' if label else ''))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-size:10px;font-weight:700;color:var(--fg-faint);letter-spacing:.05em">11월 1주 정산</div>
                  <div class="pin-out" data-pin="2" style="font-size:18px;font-weight:800;line-height:1.3">정산 요청 #4821</div>
                  <div class="pin-out" data-pin="3" style="font-size:12px;color:var(--fg-muted)">모란상회 · 홍길동이 11월 7일에 올림</div>
                  <div class="pin-out" data-pin="4" style="font-size:12.5px;line-height:1.75;max-width:250px">수수료를 뺀 ₩1,245,480이 등록하신 계좌로 입금됩니다.</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">크기 · 굵기 · 색   — 도구는 셋뿐</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">h1~h6   — 보이는 크기와 별개인 구조</div>
                </div>
              </div>'''

D = dict(
  slug="hierarchy", ko="글자 위계", en="Typographic hierarchy",
  desc="크기·굵기·색 세 도구로 읽는 순서를 만드는 법과, 하나씩 뺐을 때 무엇이 무너지는지 보여주는 항목.",
  lede="무엇부터 읽어야 하는지를 <b>글자로 알려 주는 것</b>. 꾸밈이 아니라 길 안내입니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 도구를 <b>하나씩 꺼 보세요</b>. 아래에 '구별되는 층'이 몇 개로 줄어드는지 세어 줍니다.<br>
          <b>색을 끄면 가장 많이 무너집니다</b> — 보조 글이 본문과 같은 진하기가 되면
          무엇이 덜 중요한지가 안 보이기 때문입니다. 반대로 <b>크기만으로</b> 위계를 만들려 하면
          글자가 계속 커져야 해서 금세 한계가 옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "글자 위계, 위계, 정보 위계, 타이포 위계"),
    ("영어", "typographic hierarchy, visual hierarchy, information hierarchy"),
    ("같이 쓰는 말",
     "맨 위 제목을 <b>주 제목</b>(primary), 그 아래를 <b>부제</b>(secondary), "
     "덜 중요한 글을 <b>보조 글</b>(supporting · tertiary text)이라 합니다. "
     "<code>h1~h6</code>은 <b>문서 구조</b>이고, 보이는 크기와는 별개입니다."),
    ("자주 잘못 부름",
     "<b><code>h1~h6</code></b> — 크기를 정하는 태그가 아니라 <b>구조</b>입니다. "
     "<code>h2</code>를 작게 쓰는 화면도 정상입니다.<br>"
     "<b>강조</b> — 강조는 '한 군데를 튀게' 하는 것이고 위계는 <b>전체의 순서</b>입니다.<br>"
     "<b>타입 스케일</b> — 스케일은 <b>크기 사다리</b>이고, 위계는 그 사다리를 <b>무엇에 쓰느냐</b>입니다."),
  ]),
  axes=ax("글자 위계"),
  oneline="위계의 도구는 <b>크기·굵기·색 셋뿐</b>입니다. 셋을 조금씩 쓰는 편이, 하나를 크게 쓰는 것보다 늘 낫습니다.",
  s4_title="도구", s4_hint="하나씩 빼 보면 무엇이 무너지는지 보인다",
  states=states([
    (hi(label="셋 다"), "셋 다", "크기·굵기·색. <b>읽는 순서가 보인다</b>"),
    (hi(no_color=True, label="색 없이"), "색 없이", "<b>가장 많이 무너진다.</b> 보조 글이 본문과 같아진다"),
    (hi(no_size=True, label="크기 없이"), "크기 없이", "굵기와 색만으로도 <b>꽤 버틴다</b>"),
    (hi(no_weight=True, label="굵기 없이"), "굵기 없이", "제목이 <b>덜 또렷해진다</b>"),
    (hi(flat=True, label="전부 같게"), "전부 같게", "<b>어디부터 읽을지 알 수 없다</b>"),
    ('''              <div style="width:100%;max-width:160px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:9px;display:grid;gap:3px">
                <span style="font-size:15px;font-weight:800;line-height:1.3">정산 요청 #4821</span>
                <span style="font-size:14px;font-weight:800;color:var(--danger)">확인 필요</span>
                <span style="font-size:14px;font-weight:800;color:var(--accent)">새 메시지</span>
                <span style="font-size:13px;font-weight:700">모란상회</span>
              </div>''',
     "다 강조하면", "<b>전부 튀면 아무것도 안 튄다.</b> 한 화면에 주인공은 하나"),
  ]),
  anat=ANAT,
  pins=pins([
    ("꼬리표", "overline · eyebrow", "가장 작고 흐리다. <b>맥락</b>을 알려 주고 비켜선다"),
    ("제목", "title", "가장 크고 굵다. <b>이 덩어리가 무엇인지</b>"),
    ("부제·보조 글", "supporting text", "작고 흐리다. <b>색으로 한 단계 내려</b> 둔다"),
    ("본문", "body", "읽는 글. 크기는 보통이고 <b>행간이 넓다</b>"),
    ("도구 셋", "size · weight · color", "<b>이 셋이 전부.</b> 조금씩 함께 쓰는 쪽이 낫다"),
    ("문서 구조", "h1~h6", "보이는 크기와 <b>따로</b> 정한다. 스크린 리더는 이것으로 훑는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>h1~h6</code>은 <b>크기를 정하는 태그가 아닙니다.</b> 스크린 리더 사용자는
          제목만 따라 훑어 내려가며 화면의 뼈대를 파악하기 때문에, 단계가 건너뛰거나
          크기가 예뻐 보인다고 <code>h4</code>를 먼저 쓰면 <b>목차가 엉망이 됩니다.</b>
          구조는 <code>h1 → h2 → h3</code> 순서대로 두고, 보이는 크기는 <b>CSS 로 따로</b> 정합니다.</p>''',
  do=ul([
    "<b>글이 서넛 이상</b> 모이는 모든 덩어리 — 카드, 줄, 상세 화면",
    "한 화면에서 <b>무엇부터 읽을지</b>를 정해 줘야 할 때",
    "색을 못 쓰는 상황(인쇄·흑백)에 대비할 때 — 크기·굵기가 남습니다",
  ]),
  dont=ul([
    "층을 <b>다섯 개 넘게</b> 만드는 것 — 구별이 안 됩니다",
    "<b>전부 강조</b>하는 것 — 다 튀면 아무것도 안 튑니다",
    "<code>h1~h6</code>을 크기 때문에 고르는 것",
    "색<b>만으로</b> 위계를 만드는 것 — 색이 안 보이는 사람에게는 다 같습니다",
  ]),
  instead='크기 사다리 자체는 <a href="../items/typescale.html">타입 스케일</a>, 굵기 단은 <a href="weight.html">글자 굵기</a>, 색 쓰임은 <a href="../items/color.html">색 토큰</a>.',
  cases=cases([
    (hi(w="190px"), "카드 안", "꼬리표·제목·보조·본문 <b>네 층</b>이면 충분하다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:9px;display:grid;gap:2px">
                <span style="font-size:10px;color:var(--fg-muted)">이번 주 매출</span>
                <span style="font-size:22px;font-weight:800;line-height:1.1;font-variant-numeric:tabular-nums">₩1,284,000</span>
                <span style="font-size:11px;font-weight:700;color:#1f8a4c">▲ 12.4% <span style="font-weight:400;color:var(--fg-muted)">지난주 대비</span></span>
              </div>''',
     "스탯 타일", "<b>숫자가 주인공.</b> 라벨은 작게 비켜선다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:5px">
                <span style="font-size:14px;font-weight:800">정산 안내</span>
                <span style="font-size:11.5px;line-height:1.75;color:var(--fg-muted)">승인되면 영업일 기준 2일 안에 입금됩니다. 계좌가 바뀌면 다시 확인해야 합니다.</span>
                <span style="font-size:11px;color:var(--accent);text-decoration:underline">자세히 보기</span>
              </div>''',
     "안내 글", "<b>제목 · 본문 · 링크</b> 세 층. 링크만 색으로 띄운다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="도구는 셋뿐",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="보이는 크기와 <b>문서 구조</b>를 따로 둡니다. 둘을 섞으면 둘 다 망가집니다.",
  code='''<span class="c">&lt;!-- 구조는 순서대로 --&gt;</span>
&lt;<span class="t">article</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"eyebrow"</span>&gt;11월 1주 정산&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">class</span>=<span class="s">"title"</span>&gt;정산 요청 #4821&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"meta"</span>&gt;모란상회 · 홍길동&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">p</span>&gt;수수료를 뺀 ₩1,245,480이 입금됩니다.&lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">article</span>&gt;

<span class="c">/* 보이는 모습은 CSS 가 따로 정한다 */</span>
<span class="t">.eyebrow</span> { <span class="a">font-size</span>: <span class="a">11px</span>; <span class="a">font-weight</span>: <span class="a">700</span>; <span class="a">color</span>: <span class="t">var</span>(<span class="a">--fg-faint</span>); }
<span class="t">.title</span>   { <span class="a">font-size</span>: <span class="a">20px</span>; <span class="a">font-weight</span>: <span class="a">800</span>; <span class="a">line-height</span>: <span class="a">1.3</span>; }
<span class="t">.meta</span>    { <span class="a">font-size</span>: <span class="a">13px</span>; <span class="a">color</span>: <span class="t">var</span>(<span class="a">--fg-muted</span>); }''',
  keys=kbd([
    ("도구는 셋", "크기·굵기·색. <b>조금씩 함께</b> 쓰는 쪽이 하나를 크게 쓰는 것보다 낫다"),
    ("층은 네댓 개", "그 이상은 구별이 안 된다"),
    ("색만으로 하지 않는다", "색이 안 보이면 <b>층이 통째로 사라진다</b>"),
    ("<code>h1~h6</code>은 구조", "건너뛰지 않는다. 보이는 크기는 CSS 로 따로"),
    ("주인공은 하나", "한 화면에 가장 큰 글자는 하나. <b>둘이면 둘 다 안 보인다</b>"),
    ("굵기를 먼저 써 본다", "크기를 키우기 전에. <b>줄 높이가 안 흔들린다</b>"),
  ]),
  backend=rows([
    ("위계 = 응답의 중요도", "API 가 돌려준 필드 중 <b>무엇이 제목이고 무엇이 메타인지</b>를 화면이 정합니다. 그 결정을 컴포넌트 하나에 모아 두면 화면마다 달라지지 않습니다."),
    ("제목이 비었을 때", "제목이 빈 값이면 위계가 통째로 무너집니다. <b>대체 문구</b>(이름 없는 요청 #4821)를 정해 둡니다."),
    ("검색·SEO", "<code>h1</code>이 없거나 여럿이면 검색 엔진이 <b>문서의 주제</b>를 못 잡습니다. 페이지마다 하나로 둡니다."),
    ("번역", "길이가 달라지면 제목이 두 줄이 됩니다. <b>두 줄짜리 제목</b>으로도 레이아웃이 버티는지 봅니다."),
  ]),
  plat_lede="세 플랫폼 모두 <b>이름 붙은 단</b>을 쓰고, 그 이름이 곧 위계입니다.",
  plats=plats([
    ("웹", "h1~h6 + CSS",
     hi(w="120px"),
     "구조(<code>h1~h6</code>)와 보이는 크기를 <b>따로</b> 정합니다. 이 분리가 웹의 특징입니다."),
    ("iOS", "Dynamic Type",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.largeTitle<br>.headline<br>.body / .caption</div>''',
     "<b>쓰임 이름</b>으로 고릅니다(.headline/.body/.caption). 이름 자체가 위계라 어긋날 일이 적습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">headlineMedium<br>bodyLarge<br>labelSmall</div>''',
     "<b>Display · Headline · Title · Body · Label</b> 다섯 갈래가 곧 위계입니다."),
  ]),
  plat_note="두 OS 는 <b>이름이 곧 위계</b>라 \"이건 headline 이에요\" 한마디로 통합니다. 웹은 크기·굵기·색을 직접 적어야 해서 <b>같은 화면이 팀마다 다르게</b> 나옵니다. 시안에 px 대신 <b>'제목/부제/보조'</b>로 이름을 붙여 주면 세 쪽이 같은 말을 쓰게 됩니다.",
  siblings=siblings("hierarchy"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>''',
)
