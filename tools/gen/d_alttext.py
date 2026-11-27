# -*- coding: utf-8 -*-
from ax12 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def pic(emoji, reads, tag="", ok=None, note="", w="152px"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">'
            + ('<span style="font-size:8px;font-weight:700;color:' + col + '">' + tag + '</span>' if tag else '')
            + '<span style="height:34px;border-radius:4px;background:var(--bg);display:grid;place-items:center;font-size:17px">' + emoji + '</span>'
            + '<span style="font-family:var(--mono);font-size:8.5px;color:' + col + '">' + reads + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">이 그림이 없으면 무엇을 잃는지가 유일한 기준</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">잃는 것이 없으면 alt=""로 건너뜀</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뜻을 잃으면 그 뜻을 적음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자가 박힌 그림은 그 글자를 그대로 적음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘이미지’나 파일 이름은 건너뛰지도 못함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">차트는 숫자를 표로 한 벌 더 둠</div>
                </div>
              </div>'''

D = dict(
  slug="alttext", ko="대체 텍스트", en="Alt text",
  desc="그림을 글로 대신하는 대체 텍스트를 다루는 항목입니다. 무엇을 적을지는 '이 그림이 없으면 무엇을 잃나'라는 기준 하나로 정합니다.",
  lede="대체 텍스트는 그림을 볼 수 없는 사람에게 그림 대신 읽어 주는 글입니다. 무엇을 적을지는 <b>이 그림이 없으면 무엇을 잃나</b>라는 기준 하나로 정합니다.",
  axes_lede="접근성은 다 만든 뒤가 아니라 <b>만드는 동안</b> 챙깁니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>여덟 가지 그림을 <b>스크린 리더로 읽어</b> 보면 차이가 바로 드러납니다.<br>
          없어도 아무것도 잃지 않는 그림은 <code>alt=""</code>로 비워서 <b>건너뛰게</b> 하고, 없으면 뜻을 잃는 그림은 그 뜻을 적습니다.
          반면 <b>파일 이름</b>이나 <b>‘이미지’</b>를 적어 두면 아무 정보도 주지 못하는데도 스크린 리더가 그 글을 읽느라 <b>건너뛰지도 못합니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "대체 텍스트, 대체 글, 이미지 설명"),
    ("영어", "alt text, alternative text, text alternative"),
    ("같이 쓰는 말",
     "<code>alt</code> 속성에 적는 글을 <b>대체 텍스트</b>라고 하고, "
     "그림을 길게 설명해야 할 때 따로 두는 글은 <b>긴 설명</b>(long description)이라고 합니다. "
     "그림 자체가 정보를 담고 있으면 <b>정보 전달 이미지</b>, "
     "없어도 잃는 정보가 없으면 <b>장식 이미지</b>로 나눕니다."),
    ("자주 잘못 부르는 이름",
     "<b>캡션</b> — <code>&lt;figcaption&gt;</code>은 <b>모든 사용자에게</b> 보이는 글이고, alt는 그림을 볼 수 없는 사람에게만 전달됩니다.<br>"
     "<b>타이틀</b> — <code>title</code> 속성은 마우스를 올렸을 때만 뜨기 때문에 <a href=\"hover.html\">폰에서는 보이지 않습니다</a>.<br>"
     "<b>이름 붙이기</b> — <a href=\"../items/name.html\">이름</a>은 누를 수 있는 요소를 부르는 말이고, alt는 <b>그림이 전하는 뜻</b>을 적은 글입니다."),
  ]),
  axes=ax("대체 텍스트"),
  oneline="<b>그림을 가렸을 때 그 자리에 어떤 글을 써야 뜻이 통하는지</b> 생각해 보면 대부분 알맞은 대체 텍스트를 쓸 수 있습니다.",
  s4_title="그림 종류별 대체 텍스트", s4_hint="그림이 없으면 무엇을 잃는지에 따라 달라지는 alt",
  states=states([
    (pic('🌿', 'alt=""  → 아무것도 읽지 않음', "장식", True, "없어도 잃는 것이 없음"),
     "장식 그림", "alt를 <b>비워서 건너뛰게</b> 합니다"),
    (pic('⚠️', 'alt="승인 대기"', "뜻이 있는 아이콘", True, "옆에 글자가 없음"),
     "뜻이 있는 아이콘", "아이콘이 나타내는 <b>상태를 적습니다</b>"),
    (pic('🏷️', 'alt="11월 정산 마감 11월 20일"', "글자가 박힌 그림", True, "그림 속 글자를 그대로 옮김"),
     "글자가 박힌 그림", "그림에 <b>적힌 글을 그대로 옮깁니다</b>"),
    (pic('🖼️', 'alt="IMG_2481.png"', "파일 이름", False, "정보가 없는데 건너뛰지도 못함"),
     "파일 이름을 적었을 때", "<b>가장 흔한 사고</b>입니다"),
    (pic('🗑️', 'alt="삭제" + 옆 글자 "삭제"', "두 번 읽힘", False, "이 아이콘은 장식"),
     "글자 옆에 붙은 아이콘", "옆에 같은 글자가 있으므로 <code>alt=\"\"</code>로 <b>비웁니다</b>"),
    (pic('📊', 'alt="매출 차트"', "차트", False, "숫자를 읽을 수 없음"),
     "차트", "숫자를 읽을 수 있도록 <a href=\"chart.html\">같은 데이터를 표로</a> 한 번 더 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("판단 기준", "무엇을 잃는가", "<b>이 기준 하나로 대부분의 경우를 판단할 수 있습니다</b>"),
    ("장식 그림", "alt=\"\"", "alt를 비우면 스크린 리더가 <b>건너뜁니다.</b> 속성 자체를 빼면 안 됩니다"),
    ("뜻이 있는 그림", "그 뜻을 적음", "그림이 어떻게 생겼는지보다 <b>무슨 뜻인지</b>를 적습니다"),
    ("글자가 박힌 그림", "그대로 옮김", "로고나 배너에 적힌 글을 그대로 옮깁니다"),
    ("쓰면 안 되는 글", "‘이미지’ · 파일 이름", "아무 정보도 주지 못하면서 스크린 리더가 <b>건너뛰지도 못합니다</b>"),
    ("차트", "표를 함께 둠", "차트의 숫자는 <b>글로도</b> 읽을 수 있어야 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>alt</code> 속성을 아예 빼는 것과 비우는 것은 다릅니다.</b>
          <code>alt=""</code>는 이 그림이 장식이니 건너뛰라고 <b>분명하게 알리는 표시</b>입니다.
          반면 속성이 없으면 보조기기는 그림이 장식인지 알 수 없어서
          <b>파일 이름을 대신 읽기도</b> 합니다.
          그래서 장식 이미지에도 <code>alt=""</code>는 <b>반드시 적습니다</b>.
          alt를 생략하는 것이 아니라, 빈 값으로 적어 두는 것입니다.</p>''',
  do=ul([
    "<b>뜻을 지닌</b> 그림을 넣을 때",
    "장식 그림을 넣을 때. <code>alt=\"\"</code>로 <b>비워서</b> 적습니다",
    "글자가 박힌 그림을 넣을 때. 그림에 적힌 <b>글자를 그대로</b> 옮깁니다",
  ]),
  dont=ul([
    "alt에 ‘이미지’나 ‘사진’이라고 적을 때. 그림이라는 것은 스크린 리더가 <b>이미 알려 줍니다</b>",
    "<code>IMG_2481.png</code>처럼 파일 이름을 그대로 남길 때",
    "옆에 글자가 있는데 아이콘에도 같은 alt를 줄 때. 같은 말이 <b>두 번 읽힙니다</b>",
    "<code>alt</code> 속성 자체를 뺄 때. 속성을 빼는 것은 <b>비우는 것과 다르게</b> 처리됩니다",
  ]),
  dont_title="대체 텍스트를 잘못 쓰는 경우",
  instead='누를 수 있는 요소의 이름을 정할 때는 <a href="../items/name.html">이름 붙이기</a>를 따르고, 모든 사용자에게 보여야 하는 설명은 <code>&lt;figcaption&gt;</code>으로 그림 아래에 적습니다. 차트를 어떤 모양으로 그릴지는 <a href="chart.html">차트 고르기</a>에서 다룹니다.',
  cases=cases([
    (pic('🧑', 'alt="모란상회 대표 홍길동"', "사람 사진", True, "누구인지가 그림의 뜻"), "프로필 사진에 누구인지 적기", "사진 속 사람이 <b>누구인지</b> 적습니다"),
    (pic('🏬', 'alt=""', "목록 썸네일", True, "옆에 가게 이름이 있음"), "목록 썸네일을 장식으로 비우기", "가게 이름이 옆에 글자로 있으면 썸네일은 <b>장식</b>입니다"),
    (pic('📈', 'alt="" + 숨은 표', "차트", True, "숫자는 표로 둠"), "차트의 숫자를 표로 두기", "그림의 alt는 비우고 숫자는 <b>표로 둡니다</b>"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>상황과 규칙</th><th>지키는 방법</th>",
  code_lede="장식 그림이면 alt를 비우고, 뜻이 있는 그림이면 그 뜻을 적습니다.",
  code='''<span class="c">&lt;!-- 장식은 비워서 건너뛰게 한다 (속성은 반드시 적는다) --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"pattern.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;

<span class="c">&lt;!-- 뜻이 있으면 그 뜻을 적는다 --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"status-wait.svg"</span> <span class="a">alt</span>=<span class="s">"승인 대기"</span>&gt;

<span class="c">&lt;!-- 옆에 글자가 있으면 아이콘은 장식이다 --&gt;</span>
&lt;<span class="t">button</span>&gt;&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"trash.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt; 삭제&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 차트는 그림을 비우고 숫자를 표로 둔다 --&gt;</span>
&lt;<span class="t">figure</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"chart.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;
  &lt;<span class="t">figcaption</span>&gt;11월 가맹점별 매출&lt;/<span class="t">figcaption</span>&gt;
  &lt;<span class="t">table</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;…&lt;/<span class="t">table</span>&gt;
&lt;/<span class="t">figure</span>&gt;''',
  keys=kbd([
    ("<code>alt=\"\"</code>와 <b>속성 없음</b>의 차이", "alt를 비우면 스크린 리더가 건너뛰지만, 속성이 없으면 <b>파일 이름을 읽기도</b> 합니다"),
    ("CSS 배경 이미지일 때", "CSS 배경 이미지에는 <code>alt</code>를 줄 수 없으므로, <b>뜻이 있는 그림</b>은 <code>&lt;img&gt;</code>로 넣습니다"),
    ("SVG 그림일 때", "<code>role=\"img\"</code>와 <code>aria-label</code>로 뜻을 적고, 장식이면 <code>aria-hidden</code>으로 숨깁니다. 자세한 내용은 <a href=\"iconfont.html\">아이콘 글꼴</a>에서 다룹니다"),
    ("<code>&lt;figcaption&gt;</code>과 함께 쓸 때", "캡션은 <b>모든 사용자에게</b> 보이므로 alt와 같은 말을 두 번 쓰지 않습니다"),
    ("링크 안의 그림", "그림이 링크의 <b>유일한 내용</b>이면 alt가 그대로 링크 이름이 됩니다"),
    ("확인하는 방법", "브라우저에서 <b>이미지를 끄고</b> 페이지를 읽어 봅니다. 가장 빠르게 점검할 수 있는 방법입니다"),
  ]),
  backend=rows([
    ("사용자가 올린 그림의 alt", "사용자가 올린 사진에는 <b>대체 텍스트를 적어 줄 사람이 따로 없습니다.</b> 그래서 사진을 올리는 화면에 설명 칸을 함께 두는 편이 낫습니다."),
    ("자동으로 만든 설명 다루기", "자동으로 만든 설명은 <b>틀릴 수</b> 있으므로, 그대로 쓰기보다 사람이 <b>고칠 수 있게</b> 둡니다."),
    ("빈 값과 null 구별하기", "'아직 적지 않음'과 '장식이라 비움'은 다른 상태입니다. 두 상태를 <b>구별해서 저장</b>해 두어야 나중에 채워야 할 그림을 찾을 수 있습니다."),
  ]),
  plat_lede="<b>그림의 뜻을 글로 전한다</b>는 원칙은 웹, iOS, 안드로이드가 모두 같습니다.",
  plats=plats([
    ("웹", "alt 속성",
     pic('🌿', 'alt=""', "", True, "", "110px"),
     "<code>&lt;img alt&gt;</code>가 표준이고, alt를 <b>비우는 것</b>도 장식이라는 분명한 뜻을 전합니다."),
    ("iOS", "accessibilityLabel",
     '''              <div class="phone" role="img" aria-label="iOS 대체 텍스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">.accessibilityLabel("승인 대기")</div></div></div>''',
     "<code>accessibilityLabel</code>로 그림의 뜻을 적고, 장식이면 <code>.accessibilityHidden(true)</code>로 숨깁니다."),
    ("안드로이드", "contentDescription",
     '''              <div class="phone" role="img" aria-label="안드로이드 대체 텍스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">contentDescription = null</div></div></div>''',
     "장식이면 <code>contentDescription</code>에 <code>null</code>을 넣는데, 웹의 <code>alt=\"\"</code>와 같은 역할입니다."),
  ]),
  plat_note="대체 텍스트는 <b>나중에 몰아서 채우기가 특히 어려운</b> 항목입니다. 몇 달이 지나면 그 그림을 왜 그 자리에 넣었는지 기억하는 사람이 없기 때문입니다. 그래서 그림을 넣는 그 자리에서 <b>'이게 없으면 뭘 잃지'</b>를 한 번 묻는 것이 가장 적은 품으로 끝내는 방법입니다. 대개는 잃는 것이 없어서 <code>alt=\"\"</code>로 끝납니다.",
  siblings=siblings("alttext"),
  related='''        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>''',
)
