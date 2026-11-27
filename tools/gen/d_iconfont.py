# -*- coding: utf-8 -*-
from ax3 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

TRASH = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" aria-hidden="true">'
         '<path d="M4 7h16M9 7V5h6v2M7 7l1 13h8l1-13"/></svg>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자 자리에 그림을 넣은 글꼴</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">color · font-size 가 그대로 먹는다 — 옛 장점</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">못 받으면 네모나 엉뚱한 글자가 남는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">스크린 리더가 그 글자를 읽어 버린다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">안 쓰는 아이콘까지 통째로 받는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">SVG — currentColor 로 색이 따라오고 안 깨진다</div>
                </div>
              </div>'''

D = dict(
  slug="iconfont", ko="아이콘 글꼴", en="Icon font",
  desc="글자 자리에 그림을 넣은 글꼴. 색과 크기가 공짜였지만 못 받으면 깨지고 엉뚱하게 읽힌다.",
  lede="<b>글자 자리에 그림을 넣은 글꼴</b>. 색과 크기가 공짜였지만, 지금은 <b>SVG 가 거의 모든 면에서</b> 낫습니다.",
  axes_lede="글자는 읽히려고 있습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꿔 보세요 — 아이콘 글꼴은 <code>color</code>, SVG 는 <code>stroke</code> 로 따라옵니다.
          둘 다 되는 것이 옛 장점이었습니다.<br>
          <b>글꼴을 못 받았을 때</b>를 켜면 그 자리에 <b>엉뚱한 글자나 네모</b>가 남습니다.
          아래 표에서 나머지 차이도 함께 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "아이콘 글꼴, 아이콘 폰트, 글립 아이콘"),
    ("영어", "icon font, glyph icon, webfont icon"),
    ("같이 쓰는 말",
     "글꼴 안의 글자 하나가 <b>글립</b>(glyph)이고, 아이콘을 넣어 두는 자리가 "
     "<b>사용자 영역</b>(Private Use Area)입니다. "
     "여러 SVG 를 한 파일에 모아 <code>&lt;use&gt;</code>로 꺼내 쓰는 것이 <b>SVG 스프라이트</b>, "
     "HTML 안에 직접 적는 것이 <b>인라인 SVG</b>입니다."),
    ("자주 잘못 부름",
     "<b>웹폰트</b> — <a href=\"../items/webfont.html\">웹폰트</a>는 <b>글자를 그리는</b> 글꼴입니다. 받는 방식만 같습니다.<br>"
     "<b>이모지</b> — 이모지는 OS 가 가진 그림이라 <b>우리가 모양을 못 정합니다</b>.<br>"
     "<b>아이콘</b> — 아이콘은 그림 자체, 이쪽은 <b>그것을 넘기는 방식</b>입니다 — <a href=\"assets.html\">에셋 내보내기</a>."),
  ]),
  axes=ax("아이콘 글꼴"),
  oneline="<b>새로 만든다면 SVG 입니다.</b> 아이콘 글꼴은 이미 쓰고 있는 곳에서만 남겨 둘 이유가 있습니다.",
  s4_title="두 방식", s4_hint="무엇이 다른가",
  states=states([
    (one('<span style="font-size:20px;color:var(--accent)">🗑</span>', "아이콘 글꼴", None, "color · font-size 가 먹는다"),
     "글꼴 — 정상", "글자라서 <b>CSS 가 그대로</b> 먹는다"),
    (one('<span style="font-size:16px;color:var(--danger)">&#9633;</span>', "글꼴을 못 받음", False, "네모나 엉뚱한 글자가 남는다"),
     "글꼴 — 실패", "<b>그 자리만 깨진다</b>"),
    (one(TRASH, "SVG", True, "currentColor 로 색이 따라온다"), "SVG — 정상", "안 받아져도 <b>깨질 것이 없다</b>"),
    (one(mono('aria-hidden="true"', 'var(--accent)'), "읽히지 않게", True, "옆에 글자가 있을 때"),
     "읽는 방식", "글꼴은 <b>글자를 읽어 버린다</b>"),
    (one(mono('icons.woff2 — 320개 중 12개 사용', 'var(--danger)'), "받는 양", False, "안 쓰는 것까지 통째로"),
     "받는 양", "SVG 는 <b>쓰는 것만</b>"),
    (one('<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">'
         '<circle cx="12" cy="12" r="9" fill="var(--accent-soft)"/>'
         '<path d="M8 12l3 3 5-6" fill="none" stroke="var(--accent)" stroke-width="2"/></svg>', "두 색", True, "글꼴은 한 색뿐이다"),
     "여러 색", "SVG 만 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("글립", "글자 자리의 그림", "<b>글자</b>라서 글꼴 규칙을 그대로 따른다"),
    ("색 · 크기", "color · font-size", "<b>옛 장점.</b> 지금은 SVG 도 된다"),
    ("못 받으면", "네모가 남는다", "글꼴이 늦거나 막히면 <b>그 자리만</b> 깨진다"),
    ("읽히는 방식", "글자를 읽는다", "<code>aria-hidden</code>이 없으면 <b>엉뚱하게 읽힌다</b>"),
    ("받는 양", "통째로", "320개 중 12개만 써도 <b>전부</b> 받는다"),
    ("SVG", "currentColor", "색이 따라오고 <b>깨질 것이 없다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          아이콘 글꼴이 널리 쓰인 것은 <b>그때는 그게 가장 쉬웠기</b> 때문입니다 —
          색과 크기를 CSS 로 바꾸는 것이 SVG 로는 번거롭던 시절이 있었습니다.
          지금은 <code>fill="currentColor"</code> 한 줄이면 같은 일이 되고,
          <b>깨짐·읽힘·용량</b> 쪽은 여전히 글꼴이 불리합니다.
          그래서 <b>새로 만들면 SVG</b>이고,
          이미 글꼴로 되어 있는 곳은 <code>aria-hidden</code>만 제대로 붙여 두면
          굳이 급히 걷어낼 이유는 없습니다.</p>''',
  do=ul([
    "<b>이미 글꼴로 되어 있고</b> 바꿀 일정이 없을 때",
    "아이콘이 <b>아주 많고</b> 전부 한 색일 때",
    "쓸 때는 <code>aria-hidden</code>을 <b>반드시</b>",
  ]),
  dont=ul([
    "새로 시작하면서 아이콘 글꼴 고르기",
    "<code>aria-hidden</code> 없이 쓰기 — <b>엉뚱하게 읽힌다</b>",
    "열두 개 쓰려고 <b>320개짜리</b> 글꼴 받기",
    "두 색이 필요한 아이콘을 글꼴로",
  ]),
  instead='거의 모든 경우 <a href="assets.html">SVG</a>, 글자용 글꼴은 <a href="../items/webfont.html">웹폰트</a>, 배율 이야기는 <a href="dpr.html">화면 밀도</a>.',
  cases=cases([
    (one(TRASH + ' ' + txt('삭제', "11px"), "글자 옆 아이콘", True, "아이콘은 aria-hidden"),
     "글자와 함께", "아이콘은 <b>장식</b>이다"),
    (one(TRASH, "아이콘만", True, "버튼에 aria-label 이 필요하다"),
     "아이콘만", "<a href=\"../items/name.html\">이름 붙이기</a>가 필수"),
    (code(['&lt;svg aria-hidden="true"', '  fill="currentColor"&gt;', '  &lt;use href="#trash"/&gt;', '&lt;/svg&gt;'], "150px", "스프라이트에서 꺼내 쓴다", True),
     "SVG 스프라이트", "요청은 하나, 쓰는 것만"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 아이콘의 계약서",
  code_lede="어느 방식이든 <b>읽히는 방식</b>을 정해야 합니다.",
  code='''<span class="c">&lt;!-- 글자 옆이면 아이콘은 장식이다 --&gt;</span>
&lt;<span class="t">button</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span> <span class="a">fill</span>=<span class="s">"currentColor"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
  삭제
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘만 있으면 이름을 준다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"모란상회 삭제"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘 글꼴을 쓴다면 — 글자가 읽히지 않게 --&gt;</span>
&lt;<span class="t">i</span> <span class="a">class</span>=<span class="s">"icon icon-trash"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;&lt;/<span class="t">i</span>&gt;''',
  keys=kbd([
    ("<code>aria-hidden=\"true\"</code>", "글꼴이든 SVG 든 <b>장식이면 숨긴다</b>"),
    ("아이콘만이면 이름", "<code>aria-label</code>이 없으면 <b>이름 없는 버튼</b>이 된다"),
    ("<code>&lt;i&gt;</code> 태그", "원래 뜻은 기울임이다. 아이콘 자리로 쓰는 것은 관례일 뿐 <b>의미가 없다</b>"),
    ("<code>currentColor</code>", "글자색을 따라간다. <a href=\"../items/dark.html\">다크 모드</a>가 공짜로 해결된다"),
    ("<a href=\"../items/contrast.html\">대비비</a>", "아이콘도 <b>3:1</b>은 넘어야 한다 — 흐린 회색 아이콘이 흔한 사고"),
    ("<a href=\"touchtarget.html\">눌리는 넓이</a>", "아이콘이 24px 이어도 <b>44px</b>은 눌려야 한다"),
  ]),
  backend=rows([
    ("글꼴은 캐시가 잘 먹는다", "한 파일이라 <b>한 번 받으면</b> 계속 씁니다. 그게 옛 장점이었습니다."),
    ("SVG 스프라이트", "여러 아이콘을 한 파일에 모아 <code>&lt;use&gt;</code>로 꺼내면 <b>요청은 하나</b>입니다."),
    ("쓰는 것만 추리기", "빌드에서 쓰인 아이콘만 모으면 글꼴이든 스프라이트든 <b>크기가 확 줄어듭니다</b>."),
    ("받은 SVG 를 훑는다", "남이 만든 SVG 에 <code>id</code>·<code>style</code>이 섞여 와 <b>다른 그림과 부딪힙니다</b>."),
  ]),
  plat_lede="앱 쪽은 <b>시스템 아이콘</b>이 있어 내보낼 일이 적습니다.",
  plats=plats([
    ("웹", "SVG 가 기본",
     one(TRASH, "", True, "", "110px"),
     "인라인 SVG·스프라이트를 씁니다. 아이콘 글꼴은 <b>옛 프로젝트</b>에 남아 있습니다."),
    ("iOS", "SF Symbols",
     '''              <div class="phone" role="img" aria-label="SF Symbols 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Image(systemName: "trash")</div></div></div>''',
     "OS 가 수천 개를 가지고 있습니다. <b>글자 굵기·크기에 맞춰</b> 따라옵니다."),
    ("안드로이드", "벡터 드로어블",
     '''              <div class="phone" role="img" aria-label="안드로이드 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">ic_delete.xml</div></div></div>''',
     "SVG 를 XML 로 바꿔 넣습니다. <b>Material Symbols</b> 가 기본 묶음입니다."),
  ]),
  plat_note="\"아이콘이 가끔 네모로 나와요\"는 거의 늘 아이콘 글꼴입니다 — 글꼴이 늦게 오거나 막혔을 때 그 자리만 깨집니다. 급히 고칠 거라면 <b>그 아이콘만 SVG 로</b> 바꿔도 되고, 당장 못 바꾼다면 <code>aria-hidden</code>이라도 붙여 <b>엉뚱하게 읽히는 일</b>부터 막는 것이 낫습니다.",
  siblings=siblings("iconfont"),
  related='''        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="alttext.html"><b>대체 텍스트</b><em>12부</em></a></li>''',
)
