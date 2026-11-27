# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

def ic(glyph, label, note="", ok=None, w="152px", withText=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    inner = ('<span style="display:flex;align-items:center;gap:5px;border:1px solid var(--line);'
             'border-radius:5px;padding:4px 8px;font-size:9px">'
             '<span style="font-size:13px" aria-hidden="true">' + glyph + '</span>'
             + ('<span>' + label + '</span>' if withText else '') + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:start">'
            '<div style="display:flex;gap:5px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px;width:100%">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">현실의 물건을 그린 것 — 돋보기 · 휴지통</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">배워야 아는 것 — 톱니바퀴 · 점 셋 · 햄버거</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">aria-hidden="true" — 그림은 안 읽는다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">이름은 <b>버튼 쪽</b>에 — aria-label</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">currentColor — 글자색을 따라간다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">글자를 같이 적으면 둘 다 풀린다</div>
                </div>
              </div>'''

D = dict(
  slug="icon", ko="아이콘", en="Icon",
  desc="뜻을 그림 하나로 줄인 표시. 통하는 아이콘과 배워야 아는 아이콘, 이름 붙이기.",
  lede="아이콘은 <b>뜻이 통하는 것과 배워야 아는 것</b>으로 갈립니다. 섞어 쓰면 <b>글자가 필요해집니다</b>.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>돋보기·휴지통처럼 현실의 물건을 그린 것은 통하고, 톱니바퀴나 점 셋은
          <b>배워서</b> 아는 것입니다 — 데모가 글자 없이 뜻이 통하는 아이콘 수를 세서 적습니다.<br>
          '아이콘만 쓸 때 이름 붙이기'를 끄면 <b>소리로 읽을 이름이 없는 단추</b>가 생깁니다.
          화면에 글자를 적으면 <b>그 둘이 한꺼번에</b> 풀립니다 —
          뜻도 통하고 읽을 이름도 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "아이콘, 픽토그램, 심벌"),
    ("영어", "icon, pictogram, glyph, symbol"),
    ("같이 쓰는 말",
     "선으로 그린 것이 <b>아웃라인</b>(stroke · line), 면으로 채운 것이 <b>솔리드</b>(filled)입니다. "
     "세 줄짜리 메뉴 아이콘은 <b>햄버거</b>, 점 세 개는 <b>케밥</b>(세로)·<b>미트볼</b>(가로)이라 부릅니다. "
     "브랜드를 나타내는 것은 아이콘이 아니라 <b>로고</b>입니다."),
    ("자주 잘못 부름",
     "<b>아이콘 크기</b> — <a href=\"iconsize.html\">아이콘 크기</a>는 <b>단</b>을 정하는 규칙입니다.<br>"
     "<b>아이콘 글꼴</b> — <a href=\"iconfont.html\">아이콘 글꼴</a>은 그림을 <b>글자로</b> 다루는 방식입니다.<br>"
     "<b>이미지</b> — 사진은 <a href=\"thumbnail.html\">썸네일</a>이고 아이콘은 <b>뜻의 기호</b>입니다."),
  ]),
  axes=ax("아이콘"),
  oneline="<b>아이콘만 두고 싶으면 그 아이콘이 통하는지 먼저 물어보세요.</b> 대부분은 안 통합니다.",
  states=states([
    (ic("🔍", "검색", "현실의 돋보기", True), "통하는 그림", "<b>거의 모두가</b> 안다"),
    (ic("🗑", "삭제", "휴지통", True), "통하는 그림", "뜻이 <b>그대로</b> 통한다"),
    (ic("⚙", "설정", "톱니바퀴가 왜 설정인가", False), "배워야 아는 그림", "<b>관습</b>일 뿐이다"),
    (ic("⋯", "더 보기", "점 셋은 그림이 아니다", False), "배워야 아는 그림", "모양에 <b>뜻이 없다</b>"),
    (ic("⚙", "설정", "글자를 적었다", True, "152px", True), "글자와 함께", "<b>누구에게나</b> 통한다"),
    (ic("⋯", "더 보기", "이름이 없다 — 소리로 아무것도 안 들린다", False),
     "이름 없음", "<b>읽을 것이 없다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("통하는 그림", "현실의 물건", "돋보기 · 휴지통 · 더하기"),
    ("배워야 아는 그림", "관습", "톱니바퀴 · 점 셋 · 햄버거"),
    ("<code>aria-hidden</code>", "그림은 안 읽음", "<b>두 번</b> 읽히지 않게"),
    ("이름", "버튼 쪽에", "<code>aria-label</code>"),
    ("<code>currentColor</code>", "색이 따라옴", "호버·비활성이 저절로"),
    ("글자", "같이 적기", "<b>뜻과 이름</b>이 한꺼번에"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '아이콘만 두면 깔끔하다'는 말은 <b>이미 아는 사람</b>에게만 맞습니다.
          처음 보는 사람은 누르기 전에 <b>맞혀야</b> 하고, 맞히기 싫으면 안 누릅니다.
          그래서 자주 쓰는 동작일수록 글자를 같이 적는 편이 낫고,
          자리가 정 없으면 <b>툴팁</b>을 붙입니다 — 다만 툴팁은
          <a href="hover.html">호버가 없는 세계</a>에서는 안 보입니다.<br>
          한 화면에서는 <b>한 묶음</b>의 아이콘만 쓰세요.
          선 굵기와 모서리 처리가 다른 그림을 섞으면
          딱 집어 말하기 어려운데 <b>어수선해 보입니다</b>.</p>''',
  do=ul([
    "자주 쓰는 동작에는 <b>글자를 같이</b> 적기",
    "아이콘만 둘 때는 <b><code>aria-label</code></b> 붙이기",
    "한 화면에서는 <b>한 묶음</b>의 아이콘만 쓰기",
  ]),
  dont=ul([
    "배워야 아는 그림을 <b>글자 없이</b> 혼자 두기",
    "그림과 버튼에 <b>둘 다</b> 이름을 붙이기 — 두 번 읽힌다",
    "묶음을 섞어 쓰기 — <b>굵기가 달라</b> 티가 난다",
    "아이콘으로만 <b>상태</b> 알리기 — <a href=\"statecolor.html\">상태 색</a>처럼 말도 같이 둔다",
  ]),
  instead='크기 단은 <a href="iconsize.html">아이콘 크기</a>, 글자로 다루면 <a href="iconfont.html">아이콘 글꼴</a>, 사진은 <a href="thumbnail.html">썸네일</a>, 이름 붙이기는 <a href="name.html">이름 붙이기</a>.',
  cases=cases([
    (ic("🔍", "검색", "", True), "검색 단추", "통하는 그림이라 <b>혼자</b> 선다"),
    (ic("⚙", "설정", "", True, "150px", True), "설정", "<b>글자와 함께</b>"),
    (ic("✓", "완료", "", True, "150px", True), "상태 표시", "색 말고 <b>모양과 말</b>도"),
  ]),
  code_lede="그림은 숨기고 <b>이름은 버튼에</b> 답니다. 글자가 있으면 이름은 따로 안 붙입니다.",
  code='''<span class="c">&lt;!-- 아이콘만 — 버튼에 이름을 붙인다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"검색"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span> <span class="a">width</span>=<span class="s">"20"</span> <span class="a">height</span>=<span class="s">"20"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 글자가 있으면 이름을 또 붙이지 않는다 --&gt;</span>
&lt;<span class="t">button</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt; 설정
&lt;/<span class="t">button</span>&gt;

<span class="c">/* 색을 따로 안 적어도 된다 */</span>
svg { <span class="a">display</span>: block; <span class="a">stroke</span>: currentColor; }''',
  keys=kbd([
    ("<code>aria-hidden=\"true\"</code>", "그림을 <b>안 읽게</b> 한다"),
    ("<code>aria-label</code>", "아이콘만 있는 버튼에는 <b>반드시</b>"),
    ("둘 다 금지", "그림과 버튼에 <b>같이</b> 이름을 붙이면 두 번 읽힌다"),
    ("<code>title</code>", "툴팁으로 뜨지만 <b>터치에서는 안 보인다</b>"),
    ("<code>currentColor</code>", "<code>:hover</code>·<code>[disabled]</code> 에서 색이 따라온다"),
    ("확인하는 법", "화면을 끄고 <b>소리만</b> 들어 본다 — 단추 이름이 들리는가"),
  ]),
  backend=rows([
    ("아이콘 이름을 주고받지 않는다", "서버는 <code>status: \"pending\"</code> 같은 <b>뜻</b>을 보내고, 어떤 그림을 쓸지는 화면이 정합니다."),
    ("쓰는 쪽이 고른다", "같은 상태라도 목록에서는 점, 상세에서는 띠로 보일 수 있습니다 — 그림을 서버가 정하면 그게 막힙니다."),
  ]),
  plat_lede="<b>묶음</b>이 플랫폼마다 따로 있습니다.",
  plats=plats([
    ("웹", "SVG 묶음",
     ic("🔍", "검색", "", None, "110px"),
     "Lucide · Heroicons 같은 묶음을 골라 씁니다. <b>한 묶음만</b> 쓰는 것이 요령입니다."),
    ("iOS", "SF Symbols",
     '''              <div class="phone" role="img" aria-label="iOS 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:28px;width:12px;height:12px;border:1.2px solid var(--accent);border-radius:999px"></div>
                <div style="position:absolute;left:26px;right:6px;top:32px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "OS 가 <b>수천 개</b>를 들고 있고 글자와 같은 축으로 움직입니다. 쓰면 'iOS 답게' 보입니다."),
    ("안드로이드", "Material Symbols",
     '''              <div class="phone" role="img" aria-label="안드로이드 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:28px;width:13px;height:13px;border:1.3px solid var(--accent);border-radius:3px"></div>
                <div style="position:absolute;left:28px;right:6px;top:32px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "채움·굵기·광학 크기를 <b>축</b>으로 조절합니다. 웹에서도 글꼴로 받아 쓸 수 있습니다."),
  ]),
  plat_note="앱 쪽은 OS 묶음을 쓰면 <b>그 플랫폼 사람들이 이미 아는 그림</b>을 쓰게 됩니다 — 통하는 아이콘이 저절로 늘어납니다. 웹에는 그런 공용 묶음이 없어서, 어떤 묶음을 고르든 <b>처음 보는 그림</b>이 섞입니다. 그래서 웹에서는 글자를 같이 적는 쪽으로 기우는 편이 안전하고, 적어도 <b>자주 안 쓰는 동작</b>에는 글자를 답니다.",
  siblings=siblings("icon"),
  related='''        <li><a href="iconsize.html"><b>아이콘 크기</b><em>2부</em></a></li>
        <li><a href="iconfont.html"><b>아이콘 글꼴</b><em>3부</em></a></li>
        <li><a href="name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="tooltip.html"><b>툴팁</b><em>6부</em></a></li>''',
)
