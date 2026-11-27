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
                    <span style="font-size:10.5px;color:var(--fg-muted)">너비 86%만 덮는다</span>
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
  desc="읽기용 별점과 입력용 별점의 차이, 부분 채우기와 리뷰 개수 표기를 실물과 해부도로 보여주는 항목.",
  lede="점수 하나를 별 다섯 개로 보여 주는 표시. <b>읽기용과 입력용은 생김새만 같고 전혀 다른 부품</b>입니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>평균을 움직여 보세요. 4.3을 별 넷으로 반올림하지 않고 <b>86%만 칠합니다</b> —
          반올림하면 4.0과 4.4가 같아 보입니다.<br>
          아래 입력용은 <b>라디오 그룹</b>이라 <kbd>←</kbd><kbd>→</kbd>로 움직이고 하나만 골라집니다.
          읽기용은 그냥 그림(<code>role="img"</code>)이라 포커스도 안 갑니다 — <b>이게 둘의 진짜 차이</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "별점, 평점, 평가, 등급"),
    ("영어", "rating, star rating, review score"),
    ("같이 쓰는 말",
     "반쯤 칠한 별을 <b>부분 별</b>(half star · partial fill), 점수별 비율 막대를 "
     "<b>분포</b>(distribution · histogram)라 합니다. 별이 아니라 좋아요/싫어요 둘로만 받는 것은 "
     "<b>이진 평가</b>(thumbs), 0~10으로 받는 것은 <b>NPS</b> 라고 따로 부릅니다."),
    ("자주 잘못 부름",
     "<b>슬라이더</b> — 슬라이더는 <b>이어진 값</b>이고 별점은 <b>다섯 칸</b> 중 하나입니다.<br>"
     "<b>프로그레스 바</b> — 생김새가 비슷한 막대를 쓰지만 프로그레스는 <b>진행</b>, 별점은 <b>평가</b>입니다.<br>"
     "<b>좋아요</b> — 좋아요는 <b>켜고 끄는 것</b>이라 점수가 아닙니다."),
  ]),
  axes=ax("별점"),
  oneline="별점은 <b>읽는 것</b>과 <b>주는 것</b>이 다른 부품입니다. 포커스가 가고 화살표로 움직이면 입력용, 아니면 그림입니다.",
  s4_title="상태", s4_hint="읽기용과 입력용을 섞지 않는다",
  states=states([
    (stars("86%", "4.3", "리뷰 1,284개"), "읽기용", "<b>부분 별</b>과 숫자와 개수. 셋이 함께 가야 뜻이 산다"),
    (stars("86%"), "별만", "숫자가 없으면 4.3인지 4.5인지 <b>알 수 없다</b>"),
    (stars("", "", "아직 리뷰가 없습니다"), "리뷰 없음", "별 0개가 아니라 <b>'아직 없다'</b>고 적는다"),
    (stars("100%", "5.0", "리뷰 1개"), "리뷰 1개", "별 다섯인데 <b>개수가 1</b>이면 전혀 다른 이야기다"),
    ('''              <div style="display:flex;gap:3px;font-size:19px;line-height:1;color:var(--line-strong)">
                <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span>
              </div>''',
     "입력용 — 고름", "<b>칸 단위</b>로만 고른다. 4.3점을 줄 수는 없다"),
    ('''              <div style="display:flex;gap:3px;font-size:19px;line-height:1;color:var(--line-strong)">
                <span style="color:#e8a33d;outline:2px solid var(--accent);outline-offset:2px;border-radius:3px">★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>''',
     "입력용 — 포커스", "키보드로 왔을 때. <b>별 하나에만</b> 테가 생긴다(로빙 탭인덱스)"),
  ]),
  anat=ANAT,
  pins=pins([
    ("빈 별 다섯", "track", "바닥. <b>회색 별이 늘 다섯 개</b> 있어야 '5점 만점'이 보인다"),
    ("채운 부분", "fill", "평균만큼 덮는다. <b>별 개수가 아니라 너비</b>로 자른다(4.3 → 86%)"),
    ("숫자", "value", "별 옆의 4.3. <b>별만으로는 정확히 못 읽는다</b>"),
    ("리뷰 개수", "count", "4.3(1,284개)와 5.0(1개)은 전혀 다른 이야기다"),
    ("입력용 별", "radio", "읽기용과 달리 <b>누를 수 있는 것 다섯 개</b>다"),
    ("역할", "role", "읽기용은 <code>img</code>, 입력용은 <code>radiogroup</code> — <b>여기서 갈린다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          부분 별을 만드는 방법은 둘입니다. 반 칸짜리 별 그림을 따로 두거나(<b>0.5 단위</b>로만 가능),
          칠한 별 다섯을 빈 별 다섯 위에 겹치고 <b>너비를 잘라</b> 쓰는 것입니다. 뒤쪽이 어떤 소수점도
          표현할 수 있어 흔히 씁니다. 다만 글자 사이 간격(<code>letter-spacing</code>)이 들어가면
          자르는 위치가 미세하게 어긋나니, 정확히 맞춰야 하면 <b>SVG</b>로 그립니다.</p>''',
  do=ul([
    "<b>남들의 평가</b>를 한눈에 보여 줄 때 — 상품, 숙소, 영화",
    "점수가 <b>고르는 데 쓰일</b> 때 — 목록에서 비교하는 기준",
    "쓴 사람이 <b>점수를 줘야</b> 할 때(입력용)",
  ]),
  dont=ul([
    "리뷰가 <b>너무 적을</b> 때 — 1~2개짜리 평균은 거의 뜻이 없습니다",
    "좋다/나쁘다만 받으면 될 때 → 좋아요·싫어요 둘이 더 많이 모입니다",
    "별만 보여 주고 <b>숫자와 개수를 빼는</b> 것",
    "색(노랑)만으로 채움을 말하는 것 — 색이 안 보이면 다섯 개가 다 같습니다",
  ]),
  instead='이어진 값이면 <a href="../items/slider.html">슬라이더</a>, 켜고 끄는 것이면 좋아요 버튼, 진행이면 <a href="../items/progress.html">프로그레스 바</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:170px;border:1px solid var(--line);border-radius:9px;background:var(--surface);overflow:hidden">
                <span style="display:block;aspect-ratio:4/3;background:repeating-linear-gradient(135deg,var(--ink-100) 0 7px,var(--ink-050) 7px 14px)"></span>
                <div style="padding:9px;display:grid;gap:4px">
                  <span style="font-size:11.5px;font-weight:700">무선 이어폰 2세대</span>
                  ''' + stars("86%", "4.3", "(1,284)", size=11).replace('              <div', '<div') + '''
                </div>
              </div>''',
     "상품 카드 속", "가장 흔한 자리. <b>작게, 숫자와 함께</b>"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>5점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:57%;background:#e8a33d"></i></b><span style="text-align:right">57%</span></span>
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>4점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:27%;background:#e8a33d"></i></b><span style="text-align:right">27%</span></span>
                <span class="rate-bar" style="display:grid;grid-template-columns:22px 1fr 28px;align-items:center;gap:6px;font-size:10px;color:var(--fg-muted)"><span>3점</span><b style="display:block;height:6px;border-radius:99px;background:var(--ink-100);overflow:hidden"><i style="display:block;height:100%;width:9%;background:#e8a33d"></i></b><span style="text-align:right">9%</span></span>
              </div>''',
     "분포", "평균 하나로는 안 보이는 것. <b>5점과 1점만 많은</b> 상품이 따로 있다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:7px;justify-items:center">
                <div style="display:flex;gap:4px;font-size:21px;line-height:1;color:var(--line-strong)"><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
                <span style="font-size:11px;color:var(--fg-muted)">4점 — 좋아요</span>
              </div>''',
     "점수 주기", "<b>별마다 말이 붙어야</b> 한다 — 4점이 좋은 건지 보통인지"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 부품의 계약서",
  code_lede="읽기용은 <b>그림</b>, 입력용은 <b>라디오 그룹</b>입니다. 한 파일에 두 개를 같은 코드로 만들면 둘 다 잘못됩니다.",
  code='''<span class="c">&lt;!-- 읽기용: 그림 하나. 포커스가 가지 않는다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"img"</span> <span class="a">aria-label</span>=<span class="s">"5점 만점에 4.3점, 리뷰 1,284개"</span>&gt;
  ★★★★★&lt;<span class="t">i</span> <span class="a">style</span>=<span class="s">"width:86%"</span>&gt;★★★★★&lt;/<span class="t">i</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">&lt;!-- 입력용: 라디오 그룹. 하나만 골라진다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"radiogroup"</span> <span class="a">aria-label</span>=<span class="s">"점수 주기"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"0"</span>
          <span class="a">aria-label</span>=<span class="s">"1점 — 별로예요"</span>&gt;★&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"radio"</span> <span class="a">aria-checked</span>=<span class="s">"false"</span> <span class="a">tabindex</span>=<span class="s">"-1"</span> …&gt;★&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 칠한 별을 빈 별 위에 겹치고 너비로 자른다 */</span>
<span class="t">i</span> { <span class="a">position</span>: absolute; <span class="a">left</span>: <span class="a">0</span>; <span class="a">overflow</span>: hidden; <span class="a">white-space</span>: nowrap; }''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "입력용 별 <b>다섯 개가 한 번</b>. 다섯 번 멈추면 잘못 만든 것이다"),
    ("<kbd>←</kbd><kbd>→</kbd>", "점수를 한 칸씩 올리고 내린다"),
    ("<kbd>Enter</kbd> · <kbd>Space</kbd>", "그 점수로 정한다"),
    ("별마다 이름", "<code>aria-label=\"4점 — 좋아요\"</code>. 그냥 '별'이면 다섯 개가 다 같은 말이다"),
    ("읽기용은 <code>role=\"img\"</code>", "별 다섯 개가 따로 읽히면 '★★★★★'가 열 번 들린다. <b>한 문장으로</b> 묶는다"),
    ("지울 수 있게", "잘못 누른 점수를 <b>되돌릴 방법</b>이 있어야 한다"),
  ]),
  backend=rows([
    ("평균은 저장해 둔다", "리뷰가 1,284개면 매번 평균을 내는 것은 낭비입니다. <b>합계와 개수</b>를 들고 있다가 새 리뷰가 올 때만 고칩니다."),
    ("소수점 자리", "4.25를 4.3으로 보일지 4.2로 보일지, 반올림을 <b>서버에서 할지 화면에서 할지</b>를 정합니다. 섞이면 같은 상품이 화면마다 다르게 보입니다."),
    ("개수가 적을 때", "리뷰 1개짜리 5.0을 그대로 1등으로 올리면 목록이 망가집니다. <b>개수가 적으면 평균을 깎는</b> 보정(베이즈 평균)을 흔히 씁니다."),
    ("한 사람 한 번", "같은 사람이 여러 번 주면 평균이 흔들립니다. <b>사용자당 하나</b>로 묶고 수정은 덮어쓰기로 받습니다."),
    ("분포도 함께", "평균만 주면 5점과 1점만 많은 상품을 구별할 수 없습니다. <b>점수별 개수 다섯 개</b>를 같이 보내면 화면에서 막대를 그릴 수 있습니다."),
  ]),
  plat_lede="두 OS 모두 전용 부품이 있지만 쓰임이 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     stars("86%", "4.3", size=12),
     "직접 만듭니다. <code>&lt;input type=\"radio\"&gt;</code> 다섯 개에 별 모양을 입히는 방법도 흔합니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 별점 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:2px;font-size:9px;color:var(--line-strong)">
                  <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
              </div></div>''',
     "<b>SF Symbols</b> 의 별 아이콘으로 직접 만듭니다. 앱스토어 평점 화면의 관례가 사실상 기준입니다."),
    ("안드로이드", "Material · RatingBar",
     '''              <div class="phone" role="img" aria-label="Material 별점 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;gap:2px;font-size:9px;color:var(--line-strong)">
                  <span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span style="color:#e8a33d">★</span><span>★</span></div>
              </div></div>''',
     "<b>RatingBar</b> 라는 오래된 부품이 있습니다. M3 에는 없어서 요즘은 직접 그립니다."),
  ]),
  plat_note="\"별점 붙여 주세요\"가 <b>읽기용인지 입력용인지</b>로 일의 크기가 완전히 달라집니다. 읽기용은 그림 하나지만 입력용은 키보드·포커스·되돌리기까지 딸려 옵니다. 시안에 별 다섯이 그려져 있으면 <b>누를 수 있는지부터</b> 물어보세요.",
  siblings=siblings("rating"),
  related='''        <li><a href="../items/slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="../items/radio.html"><b>라디오 그룹</b><em>4부</em></a></li>
        <li><a href="../items/card.html"><b>카드</b><em>5부</em></a></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>''',
)
