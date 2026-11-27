# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

def mo(label, note="", ok=None, w="152px", col=False, imgw="26px", title="한빛아웃도어", body="2026-11-12 정산 · 842,500원", wrap=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    img = ('<span style="display:block;width:' + ('100%' if col else imgw) + ';height:' + ('22px' if col else imgw) +
           ';border-radius:4px;background:var(--accent-soft);flex:none"></span>')
    txt_ = ('<span style="display:grid;gap:1px;min-width:0">'
            '<span style="font-size:8.5px;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + title + '</span>'
            '<span style="font-size:7.5px;color:var(--fg-muted)">' + body + '</span></span>')
    if wrap:
        inner = ('<span style="display:block">'
                 '<span style="float:left;margin:0 6px 2px 0">' + img + '</span>'
                 '<span style="font-size:8.5px;font-weight:700">' + title + '</span><br>'
                 '<span style="font-size:7.5px;color:var(--fg-muted)">' + body + '</span></span>')
    else:
        inner = ('<span style="display:flex;' + ('flex-direction:column;' if col else '') + 'gap:6px;align-items:' +
                 ('stretch' if col else 'flex-start') + '">' + img + txt_ + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);padding:6px">'
            + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">그림 — flex: none 으로 크기를 지킨다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">글 — min-width: 0 이어야 줄어든다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">float 로 붙이면 글이 그림 밑으로 돈다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">align-items: flex-start — 위를 맞춘다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">좁으면 위아래로 — 글 칸이 모자랄 때</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">전체를 누르게 하려면 바깥을 링크로</div>
                </div>
              </div>'''

D = dict(
  slug="media", ko="미디어 오브젝트", en="Media object",
  desc="그림 하나에 글 한 덩어리를 붙이는 묶음. flex와 float의 차이, 그림 크기 지키기.",
  lede="화면에서 가장 많이 쓰는 묶음입니다 — <b>그림 왼쪽, 글 오른쪽</b>. 이름이 있는 줄 모르고 쓰는 사람이 많습니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><code>float</code> 으로 붙이면 <b>글이 그림 밑으로 돌아 들어갑니다</b> —
          데모가 글의 줄들이 그림 아래까지 내려왔는지 재서 알려 줍니다.
          <code>flex</code> 에서는 글이 늘 <b>한 기둥</b>으로 섭니다.<br>
          그림은 <b>크기를 고정</b>하고(<code>flex: none</code>) 글 쪽만 줄어들게 둡니다 —
          안 그러면 좁은 화면에서 <b>그림이 먼저 찌그러집니다</b>.
          아주 좁아지면 위아래로 바꿉니다.</p>
        </div>''',
  names=rows([
    ("한국어", "미디어 오브젝트, 그림-글 묶음, 썸네일 목록 항목"),
    ("영어", "media object, media block, thumbnail + text"),
    ("같이 쓰는 말",
     "2010년 무렵 <b>미디어 오브젝트</b>라는 이름으로 널리 퍼진 꼴입니다. "
     "Bootstrap 의 <code>.media</code>, BEM 의 <code>media</code> 블록이 모두 같은 것입니다. "
     "그림 자리를 <b>figure</b>, 글 자리를 <b>body</b>라 부르는 관습이 있습니다."),
    ("자주 잘못 부름",
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>목록의 한 건</b>이고, 이건 그 안에 들어가는 <b>붙이는 법</b>입니다.<br>"
     "<b>카드</b> — <a href=\"card.html\">카드</a>는 <b>테두리를 두른 덩어리</b>입니다.<br>"
     "<b>썸네일</b> — <a href=\"thumbnail.html\">썸네일</a>은 그 안의 <b>그림 부품</b>입니다."),
  ]),
  axes=ax("미디어 오브젝트"),
  oneline="<b>그림은 <code>flex: none</code>, 글은 <code>min-width: 0</code>.</b> 이 두 줄이면 거의 다 끝납니다.",
  states=states([
    (mo("flex", "글이 한 기둥으로 선다", True), "<code>flex</code>", "<b>요즘 방식</b>"),
    (mo("float", "글이 그림 밑으로 돈다", False, "152px", False, "26px", "한빛아웃도어",
        "2026-11-12 정산 · 842,500원 · 세 건이 묶여 들어왔습니다", True),
     "<code>float</code>", "<b>옛 방식</b> — 모양이 흔들린다"),
    (mo("좁음", "글 칸만 줄어든다", True, "118px"), "좁을 때", "<b>그림은 그대로</b>"),
    (mo("위아래로", "아주 좁으면 바꾼다", True, "118px", True), "더 좁을 때", "<b>세로</b>로 바꾼다"),
    (mo("큰 그림", "그림이 주인공일 때", None, "152px", False, "40px"), "그림이 클 때", "글이 <b>곁들이</b>가 된다"),
    (mo("찌그러짐", "flex: none 이 없다", False, "118px", False, "14px"), "크기를 안 지킴", "<b>그림이 먼저</b> 줄어든다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그림", "<code>flex: none</code>", "크기를 <b>지킨다</b>"),
    ("글", "<code>min-width: 0</code>", "이게 없으면 <b>안 줄어든다</b>"),
    ("<code>float</code>", "글이 돌아 흐름", "줄 수에 따라 <b>모양이 흔들린다</b>"),
    ("위 맞춤", "<code>flex-start</code>", "글이 길어져도 <b>그림은 위에</b>"),
    ("세로 전환", "아주 좁을 때", "글 칸이 모자라면"),
    ("전체 누름", "바깥을 링크로", "안에 단추가 있으면 <b>따로</b> 막는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>min-width: 0</code></b> 은 플렉스에서 가장 자주 빠뜨리는 한 줄입니다.
          플렉스 자식의 최소 폭은 기본이 <code>auto</code>, 곧 <b>내용만큼</b>이라
          긴 이름이 들어오면 칸이 안 줄고 <b>밖으로 넘칩니다</b>.
          말줄임을 걸어도 안 먹는 이유가 대개 이것입니다.<br>
          <code>float</code> 은 지금도 동작하지만 <b>글의 줄 수에 따라 모양이 달라집니다</b> —
          두 줄이면 그림 옆에 가지런하고, 네 줄이면 밑으로 돌아 들어갑니다.
          <b>모양이 내용에 따라 흔들리는 것</b>이 문제라 요즘은 안 씁니다.</p>''',
  do=ul([
    "그림에 <b><code>flex: none</code></b>, 글에 <b><code>min-width: 0</code></b>",
    "<code>align-items: flex-start</code> 로 <b>위를 맞추기</b>",
    "아주 좁으면 <b>위아래</b>로 바꾸기",
  ]),
  dont=ul([
    "<code>float</code> 으로 붙이기 — <b>글 줄 수에 따라</b> 모양이 바뀐다",
    "그림에 크기를 안 주기 — <b>그림이 먼저</b> 찌그러진다",
    "<code>min-width: 0</code> 을 빠뜨리기 — 말줄임이 <b>안 먹는다</b>",
    "그림과 글을 <b>각각</b> 링크로 두기 — 누를 자리가 둘로 쪼개진다",
  ]),
  instead='목록의 한 건이면 <a href="listitem.html">리스트 아이템</a>, 테두리를 두르면 <a href="card.html">카드</a>, 그림 자체는 <a href="thumbnail.html">썸네일</a>, 줄 세우기는 <a href="flex.html">플렉스</a>.',
  cases=cases([
    (mo("댓글", "", True, "150px"), "댓글", "아바타 + 글"),
    (mo("알림", "", True, "150px"), "알림 목록", "아이콘 + 글"),
    (mo("상품", "", True, "150px", False, "40px"), "상품 줄", "<b>그림이 큰</b> 꼴"),
  ]),
  code_lede="두 줄이 핵심입니다 — 그림은 안 줄고, 글은 줄어듭니다.",
  code='''&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"media"</span> <span class="a">href</span>=<span class="s">"/s/2411"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">class</span>=<span class="s">"media__img"</span> <span class="a">src</span>=<span class="s">"/t/2411.jpg"</span> <span class="a">width</span>=<span class="s">"56"</span> <span class="a">height</span>=<span class="s">"56"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;
  &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"media__body"</span>&gt;
    &lt;<span class="t">b</span>&gt;한빛아웃도어 영등포타임스퀘어점&lt;/<span class="t">b</span>&gt;
    &lt;<span class="t">p</span>&gt;2026-11-12 정산 · 842,500원&lt;/<span class="t">p</span>&gt;
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">a</span>&gt;

.media { <span class="a">display</span>: flex; <span class="a">gap</span>: <span class="a">10px</span>; <span class="a">align-items</span>: flex-start; }
.media__img  { <span class="a">flex</span>: none; }        <span class="c">/* 그림은 안 줄어든다 */</span>
.media__body { <span class="a">min-width</span>: <span class="a">0</span>; }      <span class="c">/* 글은 줄어든다 — 이 줄이 핵심 */</span>

@media (max-width: <span class="a">380px</span>) { .media { <span class="a">flex-direction</span>: column; } }''',
  keys=kbd([
    ("바깥을 링크로", "그림과 글이 <b>한 번에</b> 눌린다 — Tab 도 한 번만 멈춘다"),
    ("<code>alt=\"\"</code>", "옆에 같은 글이 있으면 그림은 <b>안 읽게</b> 둔다"),
    ("안쪽 단추", "링크 안에 단추를 넣지 않는다 — <b>바깥에</b> 따로 둔다"),
    ("<code>min-width: 0</code>", "말줄임이 안 먹을 때 <b>가장 먼저</b> 의심한다"),
    ("<code>gap</code>", "margin 대신 쓴다 — 첫·마지막 예외가 없다"),
    ("확인하는 법", "아주 긴 이름을 넣고 <b>칸 밖으로 넘치는지</b> 본다"),
  ]),
  backend=rows([
    ("그림이 없을 때", "<code>thumb: null</code> 이면 화면이 <b>이니셜이나 기본 그림</b>으로 대신합니다 — 빈 네모를 두지 않습니다."),
    ("글 길이", "제목과 설명의 <b>대략 길이</b>를 알면 몇 줄로 자를지 정할 수 있습니다 — 화면에서 말줄임합니다."),
  ]),
  plat_lede="이름은 웹에서 생겼고, <b>꼴은 어디에나</b> 있습니다.",
  plats=plats([
    ("웹", "flex",
     mo("", "", True, "110px"),
     "<code>display: flex</code> 두 줄로 만듭니다. 예전에는 <code>float</code> 이 유일한 길이었습니다."),
    ("iOS", "HStack · List row",
     '''              <div class="phone" role="img" aria-label="iOS 그림-글 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:14px;height:14px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:23px;right:5px;top:28px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:23px;right:5px;top:36px;height:4px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "<code>HStack</code> 안에 그림과 <code>VStack</code> 을 넣습니다 — 구조가 <b>그대로</b>입니다."),
    ("안드로이드", "Row + Column",
     '''              <div class="phone" role="img" aria-label="안드로이드 그림-글 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:15px;height:15px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:25px;right:5px;top:28px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:25px;right:5px;top:37px;height:4px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "<code>Row { Image; Column { … } }</code> 입니다. <code>weight(1f)</code> 가 <code>min-width: 0</code> 자리입니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>가로 묶음 안에 세로 묶음</b>이라는 같은 구조를 씁니다 — 이름만 flex · HStack · Row 로 다릅니다. '글 쪽만 늘었다 줄었다 하게 한다'는 규칙도 같아서, 웹의 <code>min-width: 0</code> 은 안드로이드의 <code>weight(1f)</code> 와 같은 자리입니다. <b>한 번 익히면 셋 다 통하는</b> 드문 경우입니다.",
  siblings=siblings("media"),
  related='''        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="thumbnail.html"><b>썸네일</b><em>5부</em></a></li>
        <li><a href="flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
