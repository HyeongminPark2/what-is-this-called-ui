# -*- coding: utf-8 -*-
from ax3 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

TRASH = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" aria-hidden="true">'
         '<path d="M4 7h16M9 7V5h6v2M7 7l1 13h8l1-13"/></svg>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글자 자리에 그림을 넣은 글꼴</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">color · font-size 가 그대로 적용되는 옛 장점</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">못 받으면 네모나 엉뚱한 글자가 남음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">스크린 리더가 그 글자를 그대로 읽음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">안 쓰는 아이콘까지 통째로 받음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">SVG는 currentColor 로 색이 바뀌고 깨지지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="iconfont", ko="아이콘 글꼴", en="Icon font",
  desc="글자 자리에 그림을 넣은 아이콘 글꼴이 무엇인지, 글꼴을 받지 못하면 왜 깨지고 엉뚱하게 읽히는지, SVG와는 무엇이 다른지 보여 주는 항목입니다.",
  lede="아이콘 글꼴은 <b>글자 자리에 그림을 넣은 글꼴</b>입니다. 글자처럼 CSS로 색과 크기를 바로 바꿀 수 있어서 널리 쓰였지만, 지금은 <b>SVG가 거의 모든 면에서</b> 낫습니다.",
  axes_lede="글자 항목은 모두 글을 잘 읽히게 하려고 씁니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꿔 보세요. 아이콘 글꼴은 <code>color</code>로, SVG는 <code>stroke</code>로 색이 바뀝니다.
          CSS로 색을 바꿀 수 있다는 점이 아이콘 글꼴의 옛 장점이었는데, 지금은 SVG도 똑같이 됩니다.<br>
          <b>글꼴을 못 받았을 때</b>를 켜면 아이콘 자리에 <b>엉뚱한 글자나 네모</b>가 남습니다.
          나머지 차이는 아래 표에서 함께 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "아이콘 글꼴, 아이콘 폰트, 글립 아이콘"),
    ("영어", "icon font, glyph icon, webfont icon"),
    ("같이 쓰는 말",
     "글꼴 안의 글자 하나를 <b>글립</b>(glyph)이라고 하고, 아이콘을 넣어 두는 글자 번호 영역을 "
     "<b>사용자 영역</b>(Private Use Area)이라고 합니다. "
     "여러 SVG를 한 파일에 모아 두고 <code>&lt;use&gt;</code>로 꺼내 쓰는 방식은 <b>SVG 스프라이트</b>, "
     "HTML 안에 SVG를 직접 적는 방식은 <b>인라인 SVG</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>웹폰트</b> — <a href=\"../items/webfont.html\">웹폰트</a>는 <b>글자를 그리는</b> 글꼴이고, 아이콘 글꼴과는 받아 오는 방식만 같습니다.<br>"
     "<b>이모지</b> — 이모지는 OS에 들어 있는 그림이라서 <b>만드는 쪽이 모양을 정할 수 없습니다</b>.<br>"
     "<b>아이콘</b> — 아이콘은 그림 자체를 가리키고, 아이콘 글꼴은 <b>그 그림을 화면에 넘기는 방식</b>입니다. 자세한 내용은 <a href=\"assets.html\">에셋 내보내기</a>를 보세요."),
  ]),
  axes=ax("아이콘 글꼴"),
  oneline="<b>새로 만든다면 SVG를 씁니다.</b> 아이콘 글꼴은 이미 쓰고 있는 곳에서만 남겨 둘 이유가 있습니다.",
  s4_title="아이콘 글꼴과 SVG의 차이", s4_hint="두 방식을 나란히 본 모습",
  states=states([
    (one('<span style="font-size:20px;color:var(--accent)">🗑</span>', "아이콘 글꼴", None, "color · font-size 가 적용됨"),
     "아이콘 글꼴이 제대로 뜰 때", "글자라서 <b>CSS가 그대로</b> 적용됩니다"),
    (one('<span style="font-size:16px;color:var(--danger)">&#9633;</span>', "글꼴을 못 받음", False, "네모나 엉뚱한 글자가 남음"),
     "아이콘 글꼴을 못 받았을 때", "글꼴을 받지 못하면 <b>아이콘 자리만 깨집니다</b>"),
    (one(TRASH, "SVG", True, "currentColor 로 글자색을 따라감"), "SVG로 그릴 때", "따로 받아 올 글꼴이 없으므로 <b>깨질 일이 없습니다</b>"),
    (one(mono('aria-hidden="true"', 'var(--accent)'), "읽히지 않게", True, "옆에 글자가 있을 때"),
     "스크린 리더가 읽는 방식", "아이콘 글꼴은 스크린 리더가 <b>그 글자를 그대로 읽습니다</b>"),
    (one(mono('icons.woff2, 320개 중 12개만 사용', 'var(--danger)'), "받는 양", False, "안 쓰는 것까지 통째로 받음"),
     "내려받는 양", "SVG는 <b>쓰는 아이콘만</b> 받습니다"),
    (one('<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">'
         '<circle cx="12" cy="12" r="9" fill="var(--accent-soft)"/>'
         '<path d="M8 12l3 3 5-6" fill="none" stroke="var(--accent)" stroke-width="2"/></svg>', "두 색", True, "글꼴은 한 색만 가능"),
     "한 아이콘에 여러 색 쓰기", "한 아이콘에 여러 색을 쓰는 것은 SVG만 됩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("글립", "글자 자리의 그림", "<b>글자</b>로 취급되므로 글꼴 규칙을 그대로 따릅니다"),
    ("색 · 크기", "color · font-size", "<b>아이콘 글꼴의 옛 장점</b>이었지만, 지금은 SVG도 똑같이 됩니다"),
    ("글꼴을 못 받았을 때", "네모가 남음", "글꼴이 늦게 오거나 막히면 <b>아이콘 자리만</b> 깨집니다"),
    ("읽히는 방식", "글자를 그대로 읽음", "<code>aria-hidden</code>이 없으면 스크린 리더가 <b>엉뚱한 글자로 읽습니다</b>"),
    ("받는 양", "통째로 받음", "320개 가운데 12개만 써도 <b>320개 전부</b>를 받습니다"),
    ("SVG", "currentColor", "글자색을 따라 색이 바뀌고, <b>깨질 일이 없습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          아이콘 글꼴이 널리 쓰인 것은 <b>그때는 그 방법이 가장 쉬웠기</b> 때문입니다.
          SVG로는 색과 크기를 CSS로 바꾸기가 번거롭던 시절이 있었습니다.
          지금은 <code>fill="currentColor"</code> 한 줄이면 SVG도 같은 일을 할 수 있고,
          <b>깨짐과 스크린 리더 읽기, 용량</b> 면에서는 여전히 글꼴이 불리합니다.
          그래서 <b>새로 만들 때는 SVG</b>를 쓰고,
          이미 글꼴로 되어 있는 곳은 <code>aria-hidden</code>만 제대로 붙여 두면
          굳이 급히 걷어낼 필요는 없습니다.</p>''',
  do=ul([
    "<b>이미 글꼴로 되어 있고</b> 바꿀 일정이 없을 때",
    "아이콘이 <b>아주 많고</b> 전부 한 색일 때",
    "아이콘 글꼴을 쓸 때. <code>aria-hidden</code>을 <b>반드시</b> 붙입니다",
  ]),
  dont=ul([
    "새 프로젝트를 시작하면서 아이콘 방식을 고를 때",
    "<code>aria-hidden</code> 없이 쓸 때. 스크린 리더가 <b>엉뚱한 글자로 읽습니다</b>",
    "아이콘 열두 개를 쓰려고 <b>320개짜리</b> 글꼴을 받을 때",
    "두 색이 필요한 아이콘을 만들 때. 글꼴은 한 색만 낼 수 있습니다",
  ]),
  instead='거의 모든 경우에는 아이콘 글꼴 대신 <a href="assets.html">SVG</a>를 씁니다. 글자를 그리는 글꼴은 <a href="../items/webfont.html">웹폰트</a>에서, 화면 배율에 따른 차이는 <a href="dpr.html">화면 밀도</a>에서 다룹니다.',
  cases=cases([
    (one(TRASH + ' ' + txt('삭제', "11px"), "글자 옆 아이콘", True, "아이콘은 aria-hidden"),
     "글자 옆에 놓인 아이콘", "옆에 글자가 있으면 아이콘은 <b>장식</b>이므로 스크린 리더에서 숨깁니다"),
    (one(TRASH, "아이콘만", True, "버튼에 aria-label 이 필요함"),
     "아이콘만 있는 버튼", "버튼에 <a href=\"../items/name.html\">이름 붙이기</a>가 꼭 필요합니다"),
    (code(['&lt;svg aria-hidden="true"', '  fill="currentColor"&gt;', '  &lt;use href="#trash"/&gt;', '&lt;/svg&gt;'], "150px", "스프라이트에서 꺼내 씀", True),
     "SVG 스프라이트로 모아 쓰기", "요청 한 번으로 쓰는 아이콘만 받습니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="스크린 리더가 아이콘을 읽는 방식 정하기",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="글꼴이든 SVG든 스크린 리더에서 아이콘이 <b>어떻게 읽힐지</b>를 정해야 합니다.",
  code='''<span class="c">&lt;!-- 글자 옆이면 아이콘은 장식이다 --&gt;</span>
&lt;<span class="t">button</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span> <span class="a">fill</span>=<span class="s">"currentColor"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
  삭제
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘만 있으면 이름을 준다 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"모란상회 삭제"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘 글꼴을 쓴다면 글자가 읽히지 않게 한다 --&gt;</span>
&lt;<span class="t">i</span> <span class="a">class</span>=<span class="s">"icon icon-trash"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;&lt;/<span class="t">i</span>&gt;''',
  keys=kbd([
    ("장식 아이콘에는 <code>aria-hidden=\"true\"</code>", "글꼴이든 SVG든 <b>장식이면 스크린 리더에서 숨깁니다</b>"),
    ("아이콘만 있으면 이름 붙이기", "아이콘만 있는 버튼에 <code>aria-label</code>이 없으면 <b>이름 없는 버튼</b>이 됩니다"),
    ("<code>&lt;i&gt;</code> 태그에는 아이콘이라는 뜻이 없음", "원래 뜻은 기울임입니다. 아이콘 자리로 쓰는 것은 관례이고, 태그 자체에 아이콘이라는 <b>의미는 없습니다</b>"),
    ("<code>currentColor</code>로 글자색 따르기", "아이콘 색이 글자색을 따라가므로 <a href=\"../items/dark.html\">다크 모드</a>에서도 따로 손대지 않아도 됩니다"),
    ("아이콘도 <a href=\"../items/contrast.html\">대비비</a> 맞추기", "아이콘도 대비비가 <b>3:1</b>은 넘어야 합니다. 흐린 회색 아이콘이 이 기준을 자주 놓칩니다"),
    ("<a href=\"touchtarget.html\">눌리는 넓이</a>는 넉넉하게", "아이콘이 24px이어도 눌리는 넓이는 <b>44px</b>은 되어야 합니다"),
  ]),
  backend=rows([
    ("한 파일이라 캐시하기 쉬운 글꼴", "모든 아이콘이 한 파일이라 <b>한 번 받으면</b> 캐시에서 계속 씁니다. 이것이 아이콘 글꼴의 옛 장점이었습니다."),
    ("SVG 스프라이트로 요청 줄이기", "여러 아이콘을 한 파일에 모아 두고 <code>&lt;use&gt;</code>로 꺼내 쓰면 <b>요청이 하나</b>로 줄어듭니다."),
    ("쓰는 아이콘만 추려 내기", "빌드 단계에서 실제로 쓰인 아이콘만 모으면 글꼴이든 스프라이트든 <b>파일 크기가 크게 줄어듭니다</b>."),
    ("받은 SVG를 한 번 정리하기", "다른 사람이 만든 SVG에는 <code>id</code>나 <code>style</code>이 섞여 있어서, 그대로 쓰면 <b>다른 그림의 id나 스타일과 충돌합니다</b>. 그래서 받은 SVG는 한 번 훑어서 정리합니다."),
  ]),
  plat_lede="앱은 OS가 제공하는 <b>시스템 아이콘</b>이 있어서 아이콘을 따로 내보낼 일이 적습니다.",
  plats=plats([
    ("웹", "SVG 가 기본",
     one(TRASH, "", True, "", "110px"),
     "인라인 SVG나 스프라이트를 씁니다. 아이콘 글꼴은 <b>예전에 만든 프로젝트</b>에 남아 있습니다."),
    ("iOS", "SF Symbols",
     '''              <div class="phone" role="img" aria-label="SF Symbols 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">Image(systemName: "trash")</div></div></div>''',
     "OS에 아이콘이 수천 개 들어 있고, 옆에 놓인 <b>글자의 굵기와 크기에 맞춰</b> 함께 바뀝니다."),
    ("안드로이드", "벡터 드로어블",
     '''              <div class="phone" role="img" aria-label="안드로이드 아이콘 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">ic_delete.xml</div></div></div>''',
     "SVG를 XML로 바꿔서 넣습니다. 기본 아이콘 묶음은 <b>Material Symbols</b>입니다."),
  ]),
  plat_note="\"아이콘이 가끔 네모로 나와요\"라는 제보는 거의 늘 아이콘 글꼴에서 생깁니다. 글꼴이 늦게 오거나 막히면 아이콘 자리만 깨지기 때문입니다. 급히 고쳐야 한다면 <b>깨지는 아이콘만 SVG로</b> 바꿔도 되고, 당장 바꿀 수 없다면 <code>aria-hidden</code>이라도 붙여 <b>엉뚱한 글자로 읽히는 일</b>부터 막는 편이 낫습니다.",
  siblings=siblings("iconfont"),
  related='''        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="assets.html"><b>에셋 내보내기</b><em>15부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="alttext.html"><b>대체 텍스트</b><em>12부</em></a></li>''',
)
