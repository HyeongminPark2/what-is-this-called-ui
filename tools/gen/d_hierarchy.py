# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">크기 · 굵기 · 색   위계를 만드는 세 도구</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">h1~h6   보이는 크기와 따로 정하는 구조</div>
                </div>
              </div>'''

D = dict(
  slug="hierarchy", ko="글자 위계", en="Typographic hierarchy",
  desc="크기·굵기·색 세 도구로 읽는 순서를 만드는 법과, 도구를 하나씩 뺐을 때 위계가 어떻게 흐려지는지 보여 주는 항목입니다.",
  lede="글자 위계는 글자의 크기와 굵기, 색을 달리해서 무엇부터 읽어야 하는지를 <b>글자 모양으로 알려 주는 방법</b>입니다. 화면을 꾸미려는 것이 아니라 읽는 순서를 정해 주려고 씁니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 도구를 <b>하나씩 꺼 보세요</b>. 아래에 '구별되는 층'이 몇 개로 줄어드는지 세어 줍니다.<br>
          <b>색을 끄면 층이 가장 많이 줄어듭니다</b>. 보조 글이 본문과 같은 진하기가 되면
          무엇이 덜 중요한지 구별할 수 없기 때문입니다. 반대로 <b>크기만으로</b> 위계를 만들려 하면
          층을 하나 늘릴 때마다 글자를 더 키워야 해서 금세 한계가 옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "글자 위계, 위계, 정보 위계, 타이포 위계"),
    ("영어", "typographic hierarchy, visual hierarchy, information hierarchy"),
    ("같이 쓰는 말",
     "맨 위 제목을 <b>주 제목</b>(primary), 그 아래 제목을 <b>부제</b>(secondary), "
     "덜 중요한 글을 <b>보조 글</b>(supporting · tertiary text)이라고 합니다. "
     "<code>h1~h6</code>은 <b>문서 구조</b>를 나타내며, 화면에 보이는 크기와는 별개입니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>h1~h6</code></b> — 크기를 정하는 태그가 아니라 <b>구조</b>를 나타내는 태그입니다. "
     "그래서 <code>h2</code>를 작은 글자로 보여 주는 화면도 문제가 없습니다.<br>"
     "<b>강조</b> — 강조는 한 군데를 눈에 띄게 하는 것이고, 위계는 화면 <b>전체를 읽는 순서</b>를 정하는 것입니다.<br>"
     "<b>타입 스케일</b> — 타입 스케일은 미리 정해 둔 <b>글자 크기 단계</b>이고, 위계는 그 단계를 <b>어느 글에 쓸지</b> 정하는 일입니다."),
  ]),
  s4_title="도구를 하나씩 뺐을 때의 위계", s4_hint="빠진 도구에 따라 흐려지는 층",
  states=states([
    (hi(label="셋 다"), "세 도구를 모두 쓸 때", "크기와 굵기, 색을 모두 써서 <b>읽는 순서가 잘 보입니다</b>"),
    (hi(no_color=True, label="색 없이"), "색을 뺐을 때", "<b>층이 가장 많이 줄어듭니다.</b> 보조 글이 본문과 같은 진하기가 됩니다"),
    (hi(no_size=True, label="크기 없이"), "크기를 뺐을 때", "굵기와 색만으로도 <b>층이 꽤 잘 구별됩니다</b>"),
    (hi(no_weight=True, label="굵기 없이"), "굵기를 뺐을 때", "제목이 <b>덜 또렷해집니다</b>"),
    (hi(flat=True, label="전부 같게"), "모든 글을 같게 했을 때", "<b>어디부터 읽어야 할지 알 수 없습니다</b>"),
    ('''              <div style="width:100%;max-width:160px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:9px;display:grid;gap:3px">
                <span style="font-size:15px;font-weight:800;line-height:1.3">정산 요청 #4821</span>
                <span style="font-size:14px;font-weight:800;color:var(--danger)">확인 필요</span>
                <span style="font-size:14px;font-weight:800;color:var(--accent)">새 메시지</span>
                <span style="font-size:13px;font-weight:700">모란상회</span>
              </div>''',
     "모든 글을 강조했을 때", "<b>모든 글을 강조하면 어느 것도 눈에 띄지 않습니다.</b> 한 화면에서 가장 강조할 글은 하나로 정합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("꼬리표", "overline · eyebrow", "가장 작고 흐리게 씁니다. 제목 위에서 <b>맥락</b>만 알려 주고 눈에 띄지 않게 둡니다"),
    ("제목", "title", "가장 크고 굵게 써서 <b>이 덩어리가 무엇인지</b> 알려 줍니다"),
    ("부제·보조 글", "supporting text", "작고 흐리게 씁니다. <b>색을 한 단계 연하게</b> 해서 본문보다 덜 중요해 보이게 합니다"),
    ("본문", "body", "실제로 읽는 글입니다. 크기는 보통이고 <b>행간을 넓게</b> 잡습니다"),
    ("세 가지 도구", "size · weight · color", "<b>위계를 만드는 도구는 이 셋이 전부입니다.</b> 셋을 조금씩 함께 쓰는 편이 낫습니다"),
    ("문서 구조", "h1~h6", "보이는 크기와 <b>따로</b> 정합니다. 스크린 리더 사용자는 이 제목 단계를 따라 화면을 훑습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>h1~h6</code>은 <b>크기를 정하는 태그가 아닙니다.</b> 스크린 리더 사용자는
          제목만 따라 훑어 내려가며 화면 구성을 파악하기 때문에, 제목 단계를 건너뛰거나
          크기가 보기 좋다는 이유로 <code>h4</code>를 먼저 쓰면 <b>제목 목차의 순서가 뒤섞입니다.</b>
          구조는 <code>h1</code>, <code>h2</code>, <code>h3</code> 순서대로 두고, 보이는 크기는 <b>CSS로 따로</b> 정합니다.</p>''',
  do=ul([
    "카드나 목록 줄, 상세 화면처럼 <b>글이 서넛 이상</b> 모이는 덩어리를 만들 때",
    "한 화면에서 <b>무엇부터 읽을지</b>를 정해 줘야 할 때",
    "인쇄나 흑백처럼 색을 쓸 수 없는 상황에 대비할 때. 색이 없어도 크기와 굵기로 위계가 남습니다",
  ]),
  dont=ul([
    "층을 <b>다섯 개 넘게</b> 만들 때. 층끼리 구별되지 않습니다",
    "<b>모든 글을 강조</b>할 때. 모두 강조하면 어느 것도 눈에 띄지 않습니다",
    "보이는 크기 때문에 <code>h1~h6</code> 단계를 고를 때",
    "색<b>만으로</b> 위계를 만들 때. 색을 구별하지 못하는 사람에게는 모든 글이 같아 보입니다",
  ]),
  do_title="글자 위계를 세워야 하는 경우", dont_title="글자 위계를 세울 때 피할 것",
  instead_title="글자 위계와 이어지는 주제를 다루는 항목",
  instead='글자 크기 단계를 정하는 방법은 <a href="../items/typescale.html">타입 스케일</a>에서, 굵기 단계는 <a href="weight.html">글자 굵기</a>에서 다룹니다. 색을 쓰임별로 나누는 방법은 <a href="../items/color.html">색 토큰</a>을 보세요.',
  cases=cases([
    (hi(w="190px"), "카드 안을 네 층으로 나누기", "꼬리표, 제목, 보조 글, 본문, 이렇게 <b>네 층</b>이면 충분합니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:9px;display:grid;gap:2px">
                <span style="font-size:10px;color:var(--fg-muted)">이번 주 매출</span>
                <span style="font-size:22px;font-weight:800;line-height:1.1;font-variant-numeric:tabular-nums">₩1,284,000</span>
                <span style="font-size:11px;font-weight:700;color:#1f8a4c">▲ 12.4% <span style="font-weight:400;color:var(--fg-muted)">지난주 대비</span></span>
              </div>''',
     "스탯 타일에서 숫자 돋보이게 하기", "<b>숫자를 가장 크게</b> 보여 주고, 라벨은 작고 흐리게 둡니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:5px">
                <span style="font-size:14px;font-weight:800">정산 안내</span>
                <span style="font-size:11.5px;line-height:1.75;color:var(--fg-muted)">승인되면 영업일 기준 2일 안에 입금됩니다. 계좌가 바뀌면 다시 확인해야 합니다.</span>
                <span style="font-size:11px;color:var(--accent);text-decoration:underline">자세히 보기</span>
              </div>''',
     "안내 글을 세 층으로 나누기", "<b>제목, 본문, 링크</b> 세 층으로 나누고, 링크만 색으로 구별합니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구조는 HTML로, 모습은 CSS로 정하기",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="보이는 크기와 <b>문서 구조</b>는 따로 정합니다. 크기에 맞춰 제목 태그를 고르면 화면 모양과 문서 구조가 모두 어긋납니다.",
  code='''<span class="c">&lt;!-- 구조는 순서대로 --&gt;</span>
&lt;<span class="t">article</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"eyebrow"</span>&gt;11월 1주 정산&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">h2</span> <span class="a">class</span>=<span class="s">"title"</span>&gt;정산 요청 #4821&lt;/<span class="t">h2</span>&gt;
  &lt;<span class="t">p</span> <span class="a">class</span>=<span class="s">"meta"</span>&gt;모란상회 · 홍길동&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">p</span>&gt;수수료를 뺀 ₩1,245,480이 입금됩니다.&lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">article</span>&gt;

<span class="c">/* 보이는 모습은 CSS로 따로 정한다 */</span>
<span class="t">.eyebrow</span> { <span class="a">font-size</span>: <span class="a">11px</span>; <span class="a">font-weight</span>: <span class="a">700</span>; <span class="a">color</span>: <span class="t">var</span>(<span class="a">--fg-faint</span>); }
<span class="t">.title</span>   { <span class="a">font-size</span>: <span class="a">20px</span>; <span class="a">font-weight</span>: <span class="a">800</span>; <span class="a">line-height</span>: <span class="a">1.3</span>; }
<span class="t">.meta</span>    { <span class="a">font-size</span>: <span class="a">13px</span>; <span class="a">color</span>: <span class="t">var</span>(<span class="a">--fg-muted</span>); }''',
  keys=kbd([
    ("세 도구를 조금씩 함께 쓰기", "크기와 굵기, 색을 <b>조금씩 함께</b> 쓰는 편이 하나를 크게 바꾸는 것보다 낫습니다"),
    ("층은 네댓 개까지만", "그보다 많으면 층끼리 구별되지 않습니다"),
    ("색만으로 위계를 만들지 않기", "색을 구별하지 못하면 <b>색으로 만든 층은 모두 사라집니다</b>"),
    ("<code>h1~h6</code>은 구조에 맞춰 쓰기", "제목 단계를 건너뛰지 않고, 보이는 크기는 CSS로 따로 정합니다"),
    ("가장 큰 글자는 하나만 두기", "한 화면에서 가장 큰 글자는 하나만 둡니다. <b>둘이면 어느 쪽도 눈에 띄지 않습니다</b>"),
    ("크기보다 굵기를 먼저 바꿔 보기", "크기를 키우기 전에 굵기부터 바꿔 봅니다. 굵기는 바꿔도 <b>줄 높이가 흔들리지 않습니다</b>"),
  ]),
  backend=rows([
    ("응답 필드의 중요도는 화면에서 정하기", "API가 돌려준 필드 가운데 <b>무엇이 제목이고 무엇이 메타 정보인지</b>는 화면에서 정합니다. 이 결정을 컴포넌트 하나에 모아 두면 화면마다 위계가 달라지지 않습니다."),
    ("제목이 비었을 때", "제목이 빈 값이면 가장 눈에 띄어야 할 자리가 비어서 위계가 성립하지 않습니다. 그래서 '이름 없는 요청 #4821' 같은 <b>대체 문구</b>를 정해 둡니다."),
    ("검색 엔진이 읽는 h1", "<code>h1</code>이 없거나 여러 개면 검색 엔진이 <b>문서의 주제</b>를 제대로 파악하지 못합니다. 그래서 <code>h1</code>은 페이지마다 하나만 둡니다."),
    ("번역으로 길어진 제목", "번역하면 글 길이가 달라져 제목이 두 줄이 되기도 합니다. 그래서 <b>두 줄짜리 제목</b>을 넣어도 레이아웃이 깨지지 않는지 확인합니다."),
  ]),
  plat_lede="세 플랫폼 모두 글자 단계에 <b>이름</b>을 붙여 쓰고, 그 이름이 곧 위계를 나타냅니다.",
  plats=plats([
    ("웹", "h1~h6 + CSS",
     hi(w="120px"),
     "구조(<code>h1~h6</code>)와 보이는 크기를 <b>따로</b> 정한다는 점이 웹의 특징입니다."),
    ("iOS", "Dynamic Type",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.largeTitle<br>.headline<br>.body / .caption</div>''',
     "글자 스타일을 <b>쓰임 이름</b>으로 고릅니다(.headline/.body/.caption). 이름 자체가 위계를 나타내서 화면마다 어긋날 일이 적습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">headlineMedium<br>bodyLarge<br>labelSmall</div>''',
     "<b>Display · Headline · Title · Body · Label</b> 다섯 갈래가 곧 위계를 나타냅니다."),
  ]),
  plat_note="두 OS는 <b>스타일 이름이 곧 위계</b>라서 \"이건 headline이에요\" 한마디로 뜻이 전해집니다. 반면 웹은 크기와 굵기, 색을 직접 적어야 해서 <b>같은 화면이 팀마다 다르게</b> 나옵니다. 시안에 px 값 대신 <b>'제목/부제/보조'</b>처럼 이름을 붙여 주면 웹과 두 앱 개발자가 같은 이름으로 이야기할 수 있습니다.",
  siblings=siblings("hierarchy"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>''',
)
