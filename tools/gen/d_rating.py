# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def stars(pct, num="", cnt="", size=14):
    fill = ('<span style="position:absolute;left:0;top:0;overflow:hidden;white-space:nowrap;color:#e8a33d;width:%s">★★★★★</span>' % pct) if pct else ''
    out = ('<span style="position:relative;display:inline-block;line-height:1;font-size:%dpx;letter-spacing:1px;color:var(--line-strong)">★★★★★%s</span>'
           % (size, fill))
    if num:
        out += '<span style="font-size:11.5px;font-weight:700;font-variant-numeric:tabular-nums">%s</span>' % num
    if cnt:
        out += '<span style="font-size:10.5px;color:var(--fg-muted)">%s</span>' % cnt
    return '              <div style="display:inline-flex;align-items:center;gap:6px">%s</div>' % out

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:20px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:16px">
                  <div class="pin-out" data-pin="1" style="font-size:20px;letter-spacing:2px;color:var(--line-strong);line-height:1">★★★★★</div>
                  <div class="pin-out" data-pin="2" style="display:flex;align-items:center;gap:10px">
                    <span style="position:relative;display:inline-block;line-height:1;font-size:20px;letter-spacing:2px;color:var(--line-strong);flex:none">★★★★★<span style="position:absolute;left:0;top:0;overflow:hidden;white-space:nowrap;color:#e8a33d;width:86%">★★★★★</span></span>
                    <span style="font-size:10.5px;color:var(--fg-muted)">너비의 86%만 덮음</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="font-size:14px;font-weight:700;font-variant-numeric:tabular-nums">4.3</div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted)">리뷰 1,284개</div>
                  <div class="pin-out" data-pin="5" style="display:flex;gap:4px;font-size:18px;line-height:1;color:var(--line-strong)">
                    <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span>
                  </div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">img &nbsp;vs&nbsp; radiogroup</div>
                </div>
              </div>'''

D = dict(
  slug="rating", ko="별점", en="Rating · star rating",
  desc="읽기용 별점과 입력용 별점의 차이, 별을 부분만 칠하는 법, 리뷰 개수를 함께 적는 법을 실물과 해부도로 보여 주는 항목입니다.",
  lede="별점은 점수 하나를 별 다섯 개로 보여 주는 표시입니다. 점수를 보여 주기만 하는 <b>읽기용과 점수를 받는 입력용은 생김새만 같을 뿐 전혀 다른 부품</b>입니다.",
  axes_lede="표시 부품은 모두 보여 주기만 합니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>평균을 움직여 보세요. 4.3을 별 넷으로 반올림하지 않고 별 다섯 개 너비의 <b>86%만 칠합니다</b>.
          반올림하면 4.0과 4.4가 똑같이 별 넷으로 보이기 때문입니다.<br>
          아래 입력용 별점은 <b>라디오 그룹</b>이라서 <kbd>←</kbd><kbd>→</kbd>로 움직이고 하나만 고를 수 있습니다.
          반면 읽기용은 그림 하나(<code>role="img"</code>)라서 포커스도 가지 않습니다. <b>두 별점은 생김새가 아니라 이 점에서 갈립니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "별점, 평점, 평가, 등급"),
    ("영어", "rating, star rating, review score"),
    ("같이 쓰는 말",
     "반쯤 칠한 별은 <b>부분 별</b>(half star · partial fill), 점수별 비율을 보여 주는 막대는  "
     "<b>분포</b>(distribution · histogram)라고 부릅니다. 별 대신 좋아요와 싫어요 둘로만 받는 것은  "
     "<b>이진 평가</b>(thumbs), 0~10 사이 숫자로 받는 것은 <b>NPS</b>라고 따로 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>슬라이더</b> — 슬라이더는 <b>이어진 범위의 값</b>을 고르고, 별점은 <b>다섯 칸</b> 가운데 하나를 고릅니다.<br>"
     "<b>프로그레스 바</b> — 별점 분포에도 비슷한 막대를 쓰지만, 프로그레스 바는 <b>진행 정도</b>를, 별점은 <b>평가</b>를 보여 줍니다.<br>"
     "<b>좋아요</b> — 좋아요는 <b>켜거나 끄는 것</b>이라서 점수가 아닙니다."),
  ]),
  axes=ax("별점"),
  oneline="별점은 점수를 <b>읽는 것</b>과 점수를 <b>주는 것</b>이 서로 다른 부품입니다. 포커스가 가고 화살표 키로 점수를 바꿀 수 있으면 입력용이고, 그렇지 않으면 그림 하나인 읽기용입니다.",
  s4_title="상태", s4_hint="읽기용과 입력용 별점의 상태별 모습",
  states=states([
    (stars("86%", "4.3", "리뷰 1,284개"), "점수를 읽는 기본 모습", "<b>부분 별</b>과 숫자, 리뷰 개수를 함께 보여 줍니다. 세 가지가 함께 있어야 점수를 제대로 읽을 수 있습니다"),
    (stars("86%"), "숫자 없이 별만 있을 때", "숫자가 없으면 4.3인지 4.5인지 <b>알 수 없습니다</b>"),
    (stars("", "", "아직 리뷰가 없습니다"), "리뷰가 아직 없을 때", "빈 별 다섯 개를 보여 주지 말고 <b>아직 리뷰가 없다</b>고 적습니다"),
    (stars("100%", "5.0", "리뷰 1개"), "리뷰가 1개뿐일 때", "별이 다섯 개라도 <b>리뷰가 1개</b>뿐이면 믿을 만한 점수라고 보기 어렵습니다"),
    ('''              <div style="display:flex;gap:3px;font-size:19px;line-height:1;color:var(--line-strong)">
                <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span>
              </div>''',
     "입력용 별점에서 점수를 골랐을 때", "점수는 <b>별 한 칸 단위</b>로만 고를 수 있어서 4.3점을 줄 수는 없습니다"),
    ('''              <div style="display:flex;gap:3px;font-size:19px;line-height:1;color:var(--line-strong)">
                <span style="color:#e8a33d;outline:2px solid var(--accent);outline-offset:2px;border-radius:3px">★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>''',
     "입력용 별점에 포커스가 왔을 때", "키보드로 왔을 때의 모습입니다. 로빙 탭인덱스 방식이라 <b>별 하나에만</b> 포커스 테두리가 생깁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("빈 별 다섯", "track", "별점의 바닥입니다. <b>회색 별이 늘 다섯 개</b> 있어야 5점 만점이라는 것이 보입니다"),
    ("채운 부분", "fill", "평균 점수만큼 빈 별을 덮습니다. <b>별 개수가 아니라 너비</b>로 잘라서, 4.3점이면 전체 너비의 86%를 칠합니다"),
    ("숫자", "value", "별 옆에 4.3처럼 적는 숫자입니다. <b>별만으로는 점수를 정확히 읽을 수 없습니다</b>"),
    ("리뷰 개수", "count", "같은 높은 점수라도 4.3(1,284개)과 5.0(1개)은 믿을 수 있는 정도가 크게 다릅니다"),
    ("입력용 별", "radio", "읽기용과 달리 <b>누를 수 있는 별이 다섯 개</b> 있습니다"),
    ("역할", "role", "읽기용은 <code>img</code>, 입력용은 <code>radiogroup</code>입니다. <b>두 별점은 이 역할로 갈립니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          부분 별을 만드는 방법은 두 가지입니다. 하나는 반 칸짜리 별 그림을 따로 두는 방법인데, 이렇게 하면 <b>0.5 단위</b>로만 칠할 수 있습니다.
          다른 하나는 칠한 별 다섯 개를 빈 별 다섯 개 위에 겹치고 <b>너비를 잘라</b> 쓰는 방법으로, 어떤 소수점이든
          표현할 수 있어 흔히 씁니다. 다만 글자 사이 간격(<code>letter-spacing</code>)이 들어가면
          자르는 위치가 조금씩 어긋나므로, 정확히 맞춰야 할 때는 <b>SVG</b>로 그립니다.</p>''',
  do=ul([
    "상품, 숙소, 영화에 대한 <b>다른 사람들의 평가</b>를 한눈에 보여 줄 때",
    "목록에서 비교하는 기준처럼 점수가 <b>고르는 데 쓰일</b> 때",
    "리뷰를 쓰는 사람이 <b>점수를 줘야</b> 할 때(입력용)",
  ]),
  dont=ul([
    "리뷰가 <b>너무 적을</b> 때. 리뷰 1~2개로 낸 평균은 믿기 어렵습니다",
    "좋다, 나쁘다만 받으면 될 때. 좋아요와 싫어요 두 가지로 받는 편이 응답이 더 많이 모입니다",
    "별만 보여 주고 <b>숫자와 리뷰 개수를 뺄</b> 때",
    "노란색만으로 칠한 별을 구별할 때. 색을 구별하지 못하면 별 다섯 개가 모두 같아 보입니다",
  ]),
  instead='이어진 범위에서 값을 골라야 하면 <a href="../items/slider.html">슬라이더</a>를 쓰고, 좋다 나쁘다만 켜고 끄면 되면 좋아요 버튼을 씁니다. 평가가 아니라 진행 정도를 보여 주려면 <a href="../items/progress.html">프로그레스 바</a>가 맞습니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:170px;border:1px solid var(--line);border-radius:9px;background:var(--surface);overflow:hidden">
                <span style="display:block;aspect-ratio:4/3;background:repeating-linear-gradient(135deg,var(--ink-100) 0 7px,var(--ink-050) 7px 14px)"></span>
                <div style="padding:9px;display:grid;gap:4px">
                  <span style="font-size:11.5px;font-weight:700">무선 이어폰 2세대</span>
                  ''' + stars("86%", "4.3", "(1,284)", size=11).replace('              <div', '<div') + '''
                </div>
              </div>''',
     "상품 카드 안에 작게 넣기", "별점을 가장 흔히 보는 자리입니다. <b>작게 그리고 숫자를 함께</b> 적습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>5점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:57%;background:#e8a33d"></i></b><span style="text-align:right">57%</span></span>
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>4점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:27%;background:#e8a33d"></i></b><span style="text-align:right">27%</span></span>
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>3점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:9%;background:#e8a33d"></i></b><span style="text-align:right">9%</span></span>
              </div>''',
     "점수별 분포 보여 주기", "평균 하나로는 보이지 않는 것을 보여 줍니다. 평균이 같아도 <b>5점과 1점만 많은</b> 상품이 따로 있습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:7px;justify-items:center">
                <div style="display:flex;gap:4px;font-size:21px;line-height:1;color:var(--line-strong)"><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
                <span style="font-size:11px;color:var(--fg-muted)">4점 — 좋아요</span>
              </div>''',
     "리뷰를 쓰며 점수 주기", "4점이 좋다는 뜻인지 보통이라는 뜻인지 알 수 있도록 <b>별마다 설명을 붙여야</b> 합니다"),
  ]),
  s8_title="최소 마크업과 키보드",
  code_lede="읽기용은 <b>그림</b>으로, 입력용은 <b>라디오 그룹</b>으로 만듭니다. 두 별점을 같은 코드로 만들면 어느 쪽이든 하나는 잘못 만든 것이 됩니다.",
  code='''<span class="c">&lt;!-- 읽기용: 그림 하나로, 포커스가 가지 않는다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"img"</span> <span class="a">aria-label</span>=<span class="s">"5점 만점에 4.3점, 리뷰 1,284개"</span>&gt;
  ★★★★★&lt;<span class="t">i</span> <span class="a">style</span>=<span class="s">"width:86%"</span>&gt;★★★★★&lt;/<span class="t">i</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">&lt;!-- 입력용: 라디오 그룹으로, 하나만 고를 수 있다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"radiogroup"</span> <span class="a">aria-label</span>=<span class="s">"점수 주기"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>
          <span class="a">aria-label</span>=<span class="s">"1점 — 별로예요"</span>&gt;★&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"-1"</span> …&gt;★&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 칠한 별을 빈 별 위에 겹치고 너비로 자른다 */</span>
<span class="t">i</span> { <span class="a">position</span>: absolute; <span class="a">left</span>: <span class="a">0</span>; <span class="a">overflow</span>: hidden; <span class="a">white-space</span>: nowrap; }''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "입력용 별 <b>다섯 개 전체에서 한 번</b>만 멈춥니다. 다섯 번 멈춘다면 잘못 만든 것입니다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "점수를 한 칸씩 올리고 내립니다"),
    ("<kbd>Enter</kbd> · <kbd>Space</kbd>", "지금 고른 점수로 정합니다"),
    ("별마다 이름 붙이기", "<code>aria-label=\"4점 — 좋아요\"</code>처럼 이름을 붙입니다. 그냥 '별'이라고 하면 다섯 개가 모두 같은 이름으로 읽힙니다"),
    ("읽기용은 <code>role=\"img\"</code>로 묶기", "별 열 개(빈 별 다섯, 칠한 별 다섯)가 하나씩 읽히면 듣기 번거로우므로, '5점 만점에 4.3점'처럼 <b>한 문장으로</b> 묶습니다"),
    ("고른 점수를 지울 수 있게 하기", "잘못 누른 점수를 <b>되돌릴 방법</b>이 있어야 합니다"),
  ]),
  backend=rows([
    ("평균 대신 합계와 개수 저장하기", "리뷰가 1,284개인데 화면을 열 때마다 평균을 새로 내면 계산이 낭비됩니다. 그래서 <b>점수 합계와 리뷰 개수</b>를 저장해 두고, 새 리뷰가 들어올 때만 두 값을 고칩니다."),
    ("소수점 반올림을 할 곳", "4.25를 4.3으로 보일지 4.2로 보일지, 반올림을 <b>서버에서 할지 화면에서 할지</b>를 정해 둡니다. 두 방식이 섞이면 같은 상품의 점수가 화면마다 다르게 보입니다."),
    ("리뷰가 적을 때의 평균 보정", "리뷰가 1개뿐인 5.0점 상품을 그대로 1등으로 올리면 점수순 목록을 믿을 수 없게 됩니다. 그래서 <b>리뷰 개수가 적을수록 평균을 낮춰 잡는</b> 보정(베이즈 평균)을 흔히 씁니다."),
    ("사용자 한 명에게 점수 하나만 받기", "같은 사람이 여러 번 점수를 주면 평균이 한쪽으로 쏠립니다. 그래서 점수는 <b>사용자당 하나</b>만 받고, 점수를 고치면 기존 점수를 덮어씁니다."),
    ("점수별 분포도 함께 보내기", "평균만 보내면 5점과 1점만 많은 상품을 구별할 수 없습니다. <b>점수별 개수 다섯 개</b>를 함께 보내면 화면에서 분포 막대를 그릴 수 있습니다."),
  ]),
  plat_lede="두 OS 모두 전용 부품이 있지만 쓰임이 서로 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     stars("86%", "4.3", size=12),
     "별점을 직접 만듭니다. <code>&lt;input type=\"radio\"&gt;</code> 다섯 개를 별 모양으로 꾸미는 방법도 흔히 씁니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 별점 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:2px;font-size:9px;color:var(--line-strong)">
                  <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
              </div></div>''',
     "<b>SF Symbols</b>의 별 아이콘으로 직접 만들고, 앱스토어 평점 화면의 관례가 사실상 기준 역할을 합니다."),
    ("안드로이드", "Material · RatingBar",
     '''              <div class="phone" role="img" aria-label="Material 별점 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:2px;font-size:9px;color:var(--line-strong)">
                  <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
              </div></div>''',
     "<b>RatingBar</b>라는 오래된 부품이 있지만, M3에는 별점 부품이 없어서 요즘은 직접 그립니다."),
  ]),
  plat_note="\"별점 붙여 주세요\"라는 요청은 <b>읽기용인지 입력용인지</b>에 따라 작업량이 크게 달라집니다. 읽기용은 그림 하나로 끝나지만, 입력용은 키보드 조작과 포커스, 점수 되돌리기까지 만들어야 하기 때문입니다. 그래서 시안에 별 다섯 개가 그려져 있으면 <b>누를 수 있는 별인지부터</b> 물어보세요.",
  siblings=siblings("rating"),
  related='''        <li><a href="../items/slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="../items/radio.html"><b>라디오 그룹</b><em>4부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
