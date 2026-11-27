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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">이 그림이 없으면 무엇을 잃나 — 기준은 이 하나</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">아무것도 안 잃으면 alt="" — 건너뛴다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뜻을 잃으면 그 뜻을 적는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자가 박힌 그림은 그 글자를 그대로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘이미지’ · 파일 이름 — 건너뛰지도 못한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">차트는 숫자를 표로 한 벌 더 둔다</div>
                </div>
              </div>'''

D = dict(
  slug="alttext", ko="대체 텍스트", en="Alt text",
  desc="그림을 글로 대신하는 일. 기준은 '이 그림이 없으면 무엇을 잃나' 하나다.",
  lede="그림을 글로 대신하는 일. 기준은 하나입니다 — <b>이 그림이 없으면 무엇을 잃나</b>.",
  axes_lede="접근성은 따로 붙이는 것이 아니라 <b>빠뜨리지 않는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>여덟 가지를 <b>스크린 리더로 읽어</b> 보면 차이가 바로 드러납니다.<br>
          아무것도 안 잃는 그림은 <code>alt=""</code>로 비워 <b>건너뛰게</b> 하고, 뜻을 잃으면 그 뜻을 적습니다.
          <b>파일 이름</b>과 <b>‘이미지’</b>는 아무것도 주지 않으면서 <b>건너뛰지도 못하게</b> 만듭니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대체 텍스트, 대체 글, 이미지 설명"),
    ("영어", "alt text, alternative text, text alternative"),
    ("같이 쓰는 말",
     "<code>alt</code> 속성에 적는 글이 <b>대체 텍스트</b>이고, "
     "길게 설명해야 할 때 따로 두는 글이 <b>긴 설명</b>(long description)입니다. "
     "그림이 설명 없이 혼자 뜻을 지니면 <b>정보 전달 이미지</b>, "
     "없어도 아무 일 없으면 <b>장식 이미지</b>라 가릅니다."),
    ("자주 잘못 부름",
     "<b>캡션</b> — <code>&lt;figcaption&gt;</code>은 <b>모두에게</b> 보이는 글입니다. alt 는 그림을 못 보는 사람에게만 갑니다.<br>"
     "<b>타이틀</b> — <code>title</code> 속성은 호버로만 떠서 <a href=\"hover.html\">폰에서는 안 보입니다</a>.<br>"
     "<b>이름 붙이기</b> — <a href=\"../items/name.html\">이름</a>은 누를 수 있는 것의 이름이고, alt 는 <b>그림의 뜻</b>입니다."),
  ]),
  axes=ax("대체 텍스트"),
  oneline="<b>그림을 가리고 그 자리에 무엇을 써야 뜻이 통하는지</b>를 생각하면 거의 맞습니다.",
  s4_title="여덟 가지", s4_hint="무엇을 잃나",
  states=states([
    (pic('🌿', 'alt=""  → 아무것도 안 읽는다', "장식", True, "없어도 아무것도 안 잃는다"),
     "장식 그림", "<b>비워서 건너뛰게</b> 한다"),
    (pic('⚠️', 'alt="승인 대기"', "뜻이 있는 아이콘", True, "옆에 글자가 없다"),
     "뜻이 있는 아이콘", "<b>상태를 적는다</b>"),
    (pic('🏷️', 'alt="11월 정산 마감 11월 20일"', "글자가 박힌 그림", True, "그림 속 글자를 그대로"),
     "글자 그림", "<b>적힌 글을 옮긴다</b>"),
    (pic('🖼️', 'alt="IMG_2481.png"', "파일 이름", False, "아무 정보가 없는데 건너뛰지도 못한다"),
     "파일 이름", "<b>가장 흔한 사고</b>"),
    (pic('🗑️', 'alt="삭제" + 옆 글자 "삭제"', "두 번 읽힘", False, "아이콘은 장식이다"),
     "글자 옆 아이콘", "<code>alt=\"\"</code>로 <b>비운다</b>"),
    (pic('📊', 'alt="매출 차트"', "차트", False, "숫자를 못 읽는다"),
     "차트", "<a href=\"chart.html\">표를 한 벌 더</a> 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("기준", "무엇을 잃나", "<b>이 하나로 거의 다 갈린다</b>"),
    ("장식", "alt=\"\"", "비우면 <b>건너뛴다.</b> 속성 자체를 빼면 안 된다"),
    ("뜻이 있는 것", "그 뜻을 적는다", "그림의 생김새가 아니라 <b>무슨 뜻인지</b>"),
    ("글자 그림", "그대로 옮긴다", "로고·배너에 적힌 글"),
    ("안 되는 것", "‘이미지’ · 파일 이름", "아무것도 안 주면서 <b>건너뛰지도 못한다</b>"),
    ("차트", "표를 함께", "숫자는 <b>글로도</b> 있어야 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>alt</code> 속성을 아예 빼는 것과 비우는 것은 다릅니다.</b>
          <code>alt=""</code>는 '이건 장식이니 건너뛰라'는 <b>분명한 말</b>이고,
          속성이 없으면 보조기기가 알 길이 없어
          <b>파일 이름을 대신 읽어</b> 주기도 합니다.
          그래서 장식 이미지에도 <code>alt=""</code>는 <b>반드시 적습니다</b> —
          '안 적는 것'이 아니라 '비워서 적는 것'입니다.</p>''',
  do=ul([
    "<b>뜻을 지닌</b> 모든 그림에",
    "장식이면 <code>alt=\"\"</code>로 <b>비워서</b> 적기",
    "글자가 박힌 그림은 <b>그 글자를</b> 옮기기",
  ]),
  dont=ul([
    "‘이미지’·‘사진’ — <b>이미 안다</b>",
    "파일 이름 남기기 — <code>IMG_2481.png</code>",
    "옆에 글자가 있는데 아이콘에도 alt — <b>두 번 읽힌다</b>",
    "<code>alt</code> 속성 자체를 빼기 — <b>비우는 것과 다르다</b>",
  ]),
  instead='누를 수 있는 것의 이름은 <a href="../items/name.html">이름 붙이기</a>, 모두에게 보이는 설명은 <code>&lt;figcaption&gt;</code>, 차트는 <a href="chart.html">차트 고르기</a>.',
  cases=cases([
    (pic('🧑', 'alt="모란상회 대표 홍길동"', "사람 사진", True, "누구인지가 뜻이다"), "프로필 사진", "<b>누구인지</b>를 적는다"),
    (pic('🏬', 'alt=""', "목록 썸네일", True, "옆에 가게 이름이 있다"), "목록 그림", "이름이 옆에 있으면 <b>장식</b>이다"),
    (pic('📈', 'alt="" + 숨은 표', "차트", True, "숫자는 표로"), "차트", "그림은 비우고 <b>표를 둔다</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 글의 계약서",
  code_lede="장식이면 비우고, 뜻이 있으면 그 뜻을 적습니다.",
  code='''<span class="c">&lt;!-- 장식 — 비워서 건너뛰게 한다 (속성은 반드시 적는다) --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"pattern.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;

<span class="c">&lt;!-- 뜻이 있다 — 그 뜻을 적는다 --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"status-wait.svg"</span> <span class="a">alt</span>=<span class="s">"승인 대기"</span>&gt;

<span class="c">&lt;!-- 옆에 글자가 있으면 아이콘은 장식이다 --&gt;</span>
&lt;<span class="t">button</span>&gt;&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"trash.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt; 삭제&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 차트 — 그림은 비우고 숫자는 표로 --&gt;</span>
&lt;<span class="t">figure</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"chart.svg"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;
  &lt;<span class="t">figcaption</span>&gt;11월 가맹점별 매출&lt;/<span class="t">figcaption</span>&gt;
  &lt;<span class="t">table</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;…&lt;/<span class="t">table</span>&gt;
&lt;/<span class="t">figure</span>&gt;''',
  keys=kbd([
    ("<code>alt=\"\"</code>와 <b>속성 없음</b>은 다르다", "비우면 건너뛰고, 없으면 <b>파일 이름을 읽기도</b> 한다"),
    ("배경 이미지", "CSS 배경은 <code>alt</code>를 못 준다. <b>뜻이 있으면</b> <code>&lt;img&gt;</code>로 넣는다"),
    ("SVG", "<code>role=\"img\"</code> + <code>aria-label</code>, 장식이면 <code>aria-hidden</code> — <a href=\"iconfont.html\">아이콘 글꼴</a>"),
    ("<code>&lt;figcaption&gt;</code>", "<b>모두에게</b> 보인다. alt 와 같은 말을 두 번 쓰지 않는다"),
    ("링크 안의 그림", "그림이 링크의 <b>유일한 내용</b>이면 alt 가 곧 링크 이름이 된다"),
    ("확인하는 법", "브라우저에서 <b>이미지를 끄고</b> 읽어 본다 — 가장 빠른 점검"),
  ]),
  backend=rows([
    ("올린 그림의 alt", "사용자가 올린 사진에는 <b>적을 사람이 없습니다.</b> 올릴 때 설명 칸을 함께 두는 편이 낫습니다."),
    ("자동 생성", "기계가 만든 설명은 <b>틀릴 수</b> 있습니다. 그대로 쓰기보다 <b>고칠 수 있게</b> 둡니다."),
    ("빈 값과 null", "'아직 안 적음'과 '장식이라 비움'은 다릅니다. <b>가려 저장</b>해야 나중에 채울 것을 찾을 수 있습니다."),
  ]),
  plat_lede="<b>그림의 뜻을 글로</b>라는 생각은 어디나 같습니다.",
  plats=plats([
    ("웹", "alt 속성",
     pic('🌿', 'alt=""', "", True, "", "110px"),
     "<code>&lt;img alt&gt;</code>가 표준입니다. <b>비우는 것</b>도 분명한 뜻을 가집니다."),
    ("iOS", "accessibilityLabel",
     '''              <div class="phone" role="img" aria-label="iOS 대체 텍스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">.accessibilityLabel("승인 대기")</div></div></div>''',
     "장식이면 <code>.accessibilityHidden(true)</code>로 숨깁니다."),
    ("안드로이드", "contentDescription",
     '''              <div class="phone" role="img" aria-label="안드로이드 대체 텍스트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">contentDescription = null</div></div></div>''',
     "장식이면 <code>null</code>을 넣습니다 — 웹의 <code>alt=\"\"</code>와 같은 자리입니다."),
  ]),
  plat_note="대체 텍스트는 <b>나중에 몰아서 채우기 가장 어려운</b> 항목입니다. 몇 달 지나면 그 그림이 왜 거기 있었는지 아무도 모르기 때문입니다. 그림을 넣을 때 <b>'이게 없으면 뭘 잃지'</b>를 그 자리에서 한 번 묻는 것이 가장 쌉니다 — 대개 '아무것도'라서 <code>alt=\"\"</code>로 끝납니다.",
  siblings=siblings("alttext"),
  related='''        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>
        <li><a href="chart.html"><b>차트 고르기</b><em>10부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>''',
)
