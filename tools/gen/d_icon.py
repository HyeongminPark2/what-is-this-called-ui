# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">현실의 물건을 그린 것(돋보기, 휴지통)</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">배워야 아는 것(톱니바퀴, 점 셋, 햄버거)</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">aria-hidden="true"로 그림은 읽지 않음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">이름은 <b>버튼 쪽</b>에 aria-label로 붙임</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">currentColor로 글자색을 따라감</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">글자를 함께 적으면 두 문제가 함께 풀림</div>
                </div>
              </div>'''

D = dict(
  slug="icon", ko="아이콘", en="Icon",
  desc="아이콘이 무엇인지, 보자마자 뜻이 통하는 아이콘과 배워야 아는 아이콘이 어떻게 다른지, 아이콘에 이름을 붙이는 법을 보여 주는 항목입니다.",
  lede="아이콘은 뜻을 그림 하나로 줄인 표시로, 보자마자 <b>뜻이 통하는 것과 배워야 아는 것</b>으로 나뉩니다. 두 가지가 섞인 화면에서는 사용자가 어느 아이콘을 알아볼지 알 수 없으므로 <b>글자를 함께 적어야</b> 합니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>돋보기나 휴지통처럼 현실의 물건을 그린 아이콘은 보자마자 뜻이 통하지만, 톱니바퀴나 점 세 개는
          <b>배워야</b> 아는 아이콘입니다. 데모는 글자 없이 뜻이 통하는 아이콘이 몇 개인지 세어 적습니다.<br>
          '아이콘만 쓸 때 이름 붙이기'를 끄면 스크린 리더가 <b>읽어 줄 이름이 없는 단추</b>가 생깁니다.
          화면에 글자를 함께 적으면 뜻이 통하고 읽을 이름도 생겨서
          <b>두 문제가 한꺼번에</b> 해결됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "아이콘, 픽토그램, 심벌"),
    ("영어", "icon, pictogram, glyph, symbol"),
    ("같이 쓰는 말",
     "선으로 그린 아이콘은 <b>아웃라인</b>(stroke · line), 면을 채운 아이콘은 <b>솔리드</b>(filled)라고 부릅니다.  "
     "세 줄짜리 메뉴 아이콘은 <b>햄버거</b>, 점 세 개는 <b>케밥</b>(세로)·<b>미트볼</b>(가로)이라고 합니다.  "
     "브랜드를 나타내는 것은 아이콘이 아니라 <b>로고</b>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>아이콘 크기</b> — <a href=\"iconsize.html\">아이콘 크기</a>는 아이콘을 몇 가지 크기 <b>단</b>으로 나눠 쓸지 정하는 규칙을 다룹니다.<br>"
     "<b>아이콘 글꼴</b> — <a href=\"iconfont.html\">아이콘 글꼴</a>은 아이콘 그림을 <b>글자로</b> 다루는 방식을 가리킵니다.<br>"
     "<b>이미지</b> — 작게 줄인 사진은 <a href=\"thumbnail.html\">썸네일</a>이라고 부르고, 아이콘은 뜻을 나타내는 <b>기호</b>입니다."),
  ]),
  axes=ax("아이콘"),
  oneline="<b>아이콘만 두고 싶다면 그 아이콘이 글자 없이도 뜻이 통하는지 먼저 확인하세요.</b> 대부분의 아이콘은 글자 없이는 뜻이 통하지 않습니다.",
  s4_title="아이콘의 종류", s4_hint="뜻이 통하는 정도와 이름에 따라 나눈 모습",
  states=states([
    (ic("🔍", "검색", "현실의 돋보기", True), "보자마자 뜻이 통하는 돋보기", "<b>거의 모든 사람이</b> 뜻을 압니다"),
    (ic("🗑", "삭제", "휴지통", True), "보자마자 뜻이 통하는 휴지통", "그림의 뜻이 <b>그대로</b> 통합니다"),
    (ic("⚙", "설정", "설정이라는 뜻은 관습임", False), "배워야 뜻을 아는 톱니바퀴", "톱니바퀴가 설정을 뜻하는 것은 <b>관습</b>일 뿐입니다"),
    (ic("⋯", "더 보기", "점 셋 모양에는 뜻이 없음", False), "배워야 뜻을 아는 점 세 개", "점 세 개라는 모양 자체에는 <b>뜻이 없습니다</b>"),
    (ic("⚙", "설정", "글자를 함께 적음", True, "152px", True), "글자를 함께 적었을 때", "글자를 함께 적으면 <b>누구에게나</b> 뜻이 통합니다"),
    (ic("⋯", "더 보기", "이름이 없어 스크린 리더가 읽을 말이 없음", False),
     "이름을 붙이지 않았을 때", "스크린 리더가 <b>읽을 이름이 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("통하는 그림", "현실의 물건을 그린 것", "돋보기, 휴지통, 더하기처럼 보자마자 뜻이 통하는 그림입니다"),
    ("배워야 아는 그림", "관습으로 뜻이 정해진 것", "톱니바퀴, 점 세 개, 햄버거처럼 뜻을 배워야 아는 그림입니다"),
    ("<code>aria-hidden</code>", "그림을 읽지 않게 하는 속성", "이름이 <b>두 번</b> 읽히지 않게 합니다"),
    ("이름", "버튼 쪽에 붙이는 것", "아이콘만 있는 버튼에는 <code>aria-label</code>로 이름을 붙입니다"),
    ("<code>currentColor</code>", "글자색을 따라가는 색", "호버·비활성 상태의 색이 저절로 따라 바뀝니다"),
    ("글자", "아이콘 옆에 함께 적는 것", "<b>뜻과 이름</b>이 한꺼번에 해결됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '아이콘만 두면 깔끔하다'는 말은 그 아이콘의 뜻을 <b>이미 아는 사람</b>에게만 맞습니다.
          처음 보는 사람은 누르기 전에 뜻을 <b>짐작해야</b> 하고, 짐작이 서지 않으면 누르지 않습니다.
          그래서 자주 쓰는 동작일수록 글자를 함께 적는 편이 낫고,
          자리가 도저히 없으면 <b>툴팁</b>을 붙입니다. 다만 툴팁은
          <a href="hover.html">호버가 없는 기기</a>에서는 보이지 않습니다.<br>
          한 화면에서는 <b>한 묶음</b>의 아이콘만 쓰세요.
          선 굵기와 모서리 처리가 다른 그림을 섞으면,
          무엇이 문제인지 딱 집어 말하기는 어려워도 화면이 <b>어수선해 보입니다</b>.</p>''',
  do_title="아이콘을 쓸 때 지킬 것", dont_title="아이콘을 쓸 때 피할 것",
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  do=ul([
    "자주 쓰는 동작에는 <b>글자를 같이</b> 적기",
    "아이콘만 둘 때는 <b><code>aria-label</code></b> 붙이기",
    "한 화면에서는 <b>한 묶음</b>의 아이콘만 쓰기",
  ]),
  dont=ul([
    "배워야 아는 그림을 <b>글자 없이</b> 혼자 두기",
    "그림과 버튼에 <b>둘 다</b> 이름을 붙이기. 이름이 두 번 읽힙니다",
    "여러 묶음을 섞어 쓰기. 선 <b>굵기가 달라서</b> 섞은 티가 납니다",
    "아이콘으로만 <b>상태</b> 알리기. <a href=\"statecolor.html\">상태 색</a>과 마찬가지로 글도 함께 둡니다",
  ]),
  instead='아이콘을 몇 가지 크기 단으로 나눠 쓸지는 <a href="iconsize.html">아이콘 크기</a>에서, 아이콘을 글자로 다루는 방식은 <a href="iconfont.html">아이콘 글꼴</a>에서 다룹니다. 작게 줄인 사진은 <a href="thumbnail.html">썸네일</a> 항목을 보고, 버튼에 이름을 붙이는 방법은 <a href="name.html">이름 붙이기</a>에서 자세히 설명합니다.',
  cases=cases([
    (ic("🔍", "검색", "", True), "검색 단추를 아이콘만으로 두기", "누구나 아는 그림이라 글자 없이 <b>아이콘만</b> 두어도 됩니다"),
    (ic("⚙", "설정", "", True, "150px", True), "설정 단추에 글자 함께 적기", "배워야 아는 그림이라 <b>글자와 함께</b> 둡니다"),
    (ic("✓", "완료", "", True, "150px", True), "모양과 글로 상태 알리기", "색만 쓰지 않고 <b>모양과 글</b>로도 상태를 알립니다"),
  ]),
  s8_title="최소 마크업과 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="그림은 스크린 리더가 읽지 않게 숨기고, <b>이름은 버튼에</b> 답니다. 버튼에 글자가 있으면 그 글자가 이름이 되므로 이름을 따로 붙이지 않습니다.",
  code='''<span class="c">&lt;!-- 아이콘만 있으면 버튼에 이름을 붙인다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"검색"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span> <span class="a">width</span>=<span class="s">"20"</span> <span class="a">height</span>=<span class="s">"20"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 글자가 있으면 이름을 또 붙이지 않는다 --&gt;</span>
&lt;<span class="t">button</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt; 설정
&lt;/<span class="t">button</span>&gt;

<span class="c">/* currentColor 를 쓰면 색을 따로 적지 않아도 된다 */</span>
svg { <span class="a">display</span>: block; <span class="a">stroke</span>: currentColor; }''',
  keys=kbd([
    ("그림에 <code>aria-hidden=\"true\"</code> 붙이기", "스크린 리더가 그림을 <b>읽지 않게</b> 합니다"),
    ("버튼에 <code>aria-label</code> 붙이기", "아이콘만 있는 버튼에는 <b>반드시</b> 붙입니다"),
    ("그림과 버튼에 이름을 겹쳐 붙이지 않기", "그림과 버튼에 <b>모두</b> 이름을 붙이면 이름이 두 번 읽힙니다"),
    ("<code>title</code>로 툴팁 띄우기", "툴팁으로 뜨지만 <b>터치 화면에서는 보이지 않습니다</b>"),
    ("색은 <code>currentColor</code>로 받기", "<code>:hover</code>나 <code>[disabled]</code> 상태에서 글자색이 바뀌면 아이콘 색도 따라 바뀝니다"),
    ("확인하는 방법", "화면을 끄고 스크린 리더 <b>소리만</b> 들으며 단추마다 이름이 들리는지 확인합니다"),
  ]),
  backend=rows([
    ("서버는 그림 대신 뜻을 보내기", "서버는 <code>status: \"pending\"</code> 같은 <b>뜻</b>을 보내고, 어떤 그림을 쓸지는 화면이 정합니다."),
    ("그림은 화면 쪽에서 고르기", "같은 상태라도 목록에서는 점으로, 상세 화면에서는 띠로 보여 줄 수 있습니다. 그런데 서버가 그림까지 정해서 보내면 화면마다 다르게 보여 줄 수 없게 됩니다."),
  ]),
  plat_lede="플랫폼마다 쓰는 아이콘 <b>묶음</b>이 따로 있습니다.",
  plats=plats([
    ("웹", "SVG 묶음",
     ic("🔍", "검색", "", None, "110px"),
     "Lucide나 Heroicons 같은 묶음 가운데 하나를 골라 쓰고, 한 제품에서는 <b>한 묶음만</b> 쓰는 것이 좋습니다."),
    ("iOS", "SF Symbols",
     '''              <div class="phone" role="img" aria-label="iOS 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:28px;width:12px;height:12px;border:1.2px solid var(--accent);border-radius:999px"></div>
                <div style="position:absolute;left:26px;right:6px;top:32px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "OS에 아이콘이 <b>수천 개</b> 들어 있고, 글자 크기와 굵기가 바뀌면 아이콘도 함께 바뀝니다. SF Symbols를 쓰면 화면이 iOS 기본 앱과 같은 인상으로 보입니다."),
    ("안드로이드", "Material Symbols",
     '''              <div class="phone" role="img" aria-label="안드로이드 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:28px;width:13px;height:13px;border:1.3px solid var(--accent);border-radius:3px"></div>
                <div style="position:absolute;left:28px;right:6px;top:32px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "채움, 굵기, 광학 크기를 각각의 <b>축</b>으로 조절하고, 웹에서도 글꼴로 받아 쓸 수 있습니다."),
  ]),
  plat_note="앱에서 OS 묶음을 쓰면 <b>그 플랫폼 사용자들이 이미 아는 그림</b>을 쓰게 되므로, 글자 없이 통하는 아이콘이 저절로 늘어납니다. 반면 웹에는 그런 공용 묶음이 없어서, 어떤 묶음을 고르든 사용자가 <b>처음 보는 그림</b>이 섞입니다. 그래서 웹에서는 되도록 글자를 함께 적는 편이 안전하고, 적어도 <b>자주 쓰지 않는 동작</b>에는 글자를 붙입니다.",
  siblings=siblings("icon"),
  related='''        <li><a href="iconsize.html"><b>아이콘 크기</b><em>2부</em></a></li>
        <li><a href="iconfont.html"><b>아이콘 글꼴</b><em>3부</em></a></li>
        <li><a href="name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="tooltip.html"><b>툴팁</b><em>6부</em></a></li>''',
)
