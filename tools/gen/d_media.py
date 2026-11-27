# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">그림은 flex: none으로 크기를 지킴</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">글은 min-width: 0이어야 줄어듦</div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">float로 붙이면 글이 그림 밑까지 흘러내림</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">align-items: flex-start로 위쪽을 맞춤</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">글 칸이 모자라면 위아래로 쌓음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">전체를 누르게 하려면 바깥을 링크로 만듦</div>
                </div>
              </div>'''

D = dict(
  slug="media", ko="미디어 오브젝트", en="Media object",
  desc="그림 하나 옆에 글 한 덩어리를 붙이는 미디어 오브젝트를 flex와 float의 차이, 그림 크기를 지키는 법으로 나눠 보여 주는 항목입니다.",
  lede="미디어 오브젝트는 <b>왼쪽에 그림, 오른쪽에 글</b>을 두는 묶음으로, 화면에서 특히 많이 씁니다. 그런데도 이런 이름이 있다는 것을 모르고 쓰는 사람이 많습니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><code>float</code>으로 그림을 붙이면 글이 길어질 때 <b>그림 아래쪽까지 감싸며 흘러내립니다</b>.
          데모는 글줄이 그림 아래까지 내려왔는지 재서 알려 줍니다.
          반면 <code>flex</code>에서는 글이 늘 그림 옆에 <b>한 단</b>으로 놓입니다.<br>
          그림은 <b>크기를 고정</b>하고(<code>flex: none</code>) 글 쪽만 줄어들게 둡니다.
          그러지 않으면 좁은 화면에서 <b>그림이 먼저 찌그러집니다</b>.
          화면이 아주 좁아지면 그림과 글을 위아래로 바꿔 놓습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "미디어 오브젝트, 그림-글 묶음, 썸네일 목록 항목"),
    ("영어", "media object, media block, thumbnail + text"),
    ("같이 쓰는 말",
     "2010년 무렵 <b>미디어 오브젝트</b>라는 이름으로 널리 퍼진 배치입니다.  "
     "Bootstrap 의 <code>.media</code>, BEM 의 <code>media</code> 블록이 모두 같은 배치를 가리킵니다.  "
     "그림 자리는 <b>figure</b>, 글 자리는 <b>body</b>라고 부르는 관습이 있습니다."),
    ("자주 잘못 부르는 이름",
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>목록의 한 건</b>이고, 미디어 오브젝트는 그 안에서 그림과 글을 <b>붙이는 방법</b>입니다.<br>"
     "<b>카드</b> — <a href=\"card.html\">카드</a>는 <b>테두리를 두른 상자</b>이고, 미디어 오브젝트는 테두리 없이 그림과 글을 붙이는 배치입니다.<br>"
     "<b>썸네일</b> — <a href=\"thumbnail.html\">썸네일</a>은 미디어 오브젝트 안에 들어가는 <b>그림 부품</b>입니다."),
  ]),
  axes=ax("미디어 오브젝트"),
  oneline="<b>그림에는 <code>flex: none</code>, 글에는 <code>min-width: 0</code>을 줍니다.</b> 미디어 오브젝트는 대부분 이 두 줄로 만들 수 있습니다.",
  s4_title="붙이는 방식과 상태", s4_hint="붙이는 방식과 폭에 따라 달라지는 모습",
  states=states([
    (mo("flex", "글이 한 단으로 놓임", True), "<code>flex</code>로 붙였을 때", "요즘 쓰는 방식입니다"),
    (mo("float", "글이 그림 밑까지 흘러내림", False, "152px", False, "26px", "한빛아웃도어",
        "2026-11-12 정산 · 842,500원 · 세 건이 묶여 들어왔습니다", True),
     "<code>float</code>로 붙였을 때", "<b>예전 방식</b>으로, 글 길이에 따라 모양이 달라집니다"),
    (mo("좁음", "글 칸만 줄어듦", True, "118px"), "폭이 좁을 때", "글 칸만 줄어들고 <b>그림은 그대로</b>입니다"),
    (mo("위아래로", "아주 좁으면 세로로 쌓음", True, "118px", True), "폭이 아주 좁을 때", "그림과 글을 <b>세로</b>로 쌓습니다"),
    (mo("큰 그림", "그림이 중심일 때", None, "152px", False, "40px"), "그림이 클 때", "그림이 중심이 되고 글은 <b>보조 설명</b>이 됩니다"),
    (mo("찌그러짐", "flex: none이 없음", False, "118px", False, "14px"), "그림 크기를 지키지 않았을 때", "폭이 좁아지면 <b>그림이 먼저</b> 줄어듭니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그림", "<code>flex: none</code>", "그림 크기를 <b>지킵니다</b>"),
    ("글", "<code>min-width: 0</code>", "이 값이 없으면 글 칸이 <b>줄어들지 않습니다</b>"),
    ("<code>float</code>", "글이 그림을 감싸며 흐르는 방식", "글 줄 수에 따라 <b>모양이 달라집니다</b>"),
    ("위 맞춤", "<code>flex-start</code>", "글이 길어져도 <b>그림은 위쪽</b>에 맞춰 둡니다"),
    ("세로 전환", "아주 좁을 때의 배치", "글 칸이 모자라면 위아래로 바꿉니다"),
    ("전체 누름", "바깥을 링크로 감싸기", "안에 단추가 있으면 단추의 눌림을 <b>따로</b> 막습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>min-width: 0</code></b> 은 플렉스에서 특히 자주 빠뜨리는 한 줄입니다.
          플렉스 자식의 최소 폭은 기본값이 <code>auto</code>, 즉 <b>내용 길이만큼</b>이라서
          긴 이름이 들어오면 칸이 줄어들지 않고 <b>밖으로 넘칩니다</b>.
          말줄임을 걸어도 적용되지 않는다면 대개 이 값이 빠진 것입니다.<br>
          <code>float</code>은 지금도 동작하지만 <b>글의 줄 수에 따라 모양이 달라집니다</b>.
          글이 두 줄이면 그림 옆에 가지런히 놓이고, 네 줄이면 그림 아래까지 감싸며 흘러내립니다.
          이렇게 <b>내용에 따라 모양이 달라지기</b> 때문에 요즘은 미디어 오브젝트에 쓰지 않습니다.</p>''',
  do_title="미디어 오브젝트를 만들 때 지킬 것", dont_title="미디어 오브젝트를 만들 때 피할 것",
  instead_title="미디어 오브젝트 대신 쓸 부품과 함께 볼 항목",
  do=ul([
    "그림에는 <b><code>flex: none</code></b>, 글에는 <b><code>min-width: 0</code></b> 주기",
    "<code>align-items: flex-start</code>로 <b>위쪽을 맞추기</b>",
    "아주 좁으면 <b>위아래</b>로 바꾸기",
  ]),
  dont=ul([
    "<code>float</code>으로 붙이기. <b>글 줄 수에 따라</b> 모양이 바뀝니다",
    "그림에 크기를 주지 않기. 폭이 좁아지면 <b>그림이 먼저</b> 찌그러집니다",
    "<code>min-width: 0</code>을 빠뜨리기. 말줄임이 <b>적용되지 않습니다</b>",
    "그림과 글을 <b>각각</b> 링크로 두기. 같은 곳으로 가는 링크가 둘로 나뉩니다",
  ]),
  instead='목록의 한 건 전체를 다루려면 <a href="listitem.html">리스트 아이템</a>을, 테두리를 둘러 상자로 묶으려면 <a href="card.html">카드</a>를 씁니다. 그림 부품 자체는 <a href="thumbnail.html">썸네일</a>에서, 요소를 한 줄로 늘어놓는 방법은 <a href="flex.html">플렉스</a>에서 다룹니다.',
  cases=cases([
    (mo("댓글", "", True, "150px"), "아바타 옆에 댓글 붙이기", "아바타 옆에 댓글을 붙입니다"),
    (mo("알림", "", True, "150px"), "아이콘 옆에 알림 붙이기", "아이콘 옆에 알림 내용을 붙입니다"),
    (mo("상품", "", True, "150px", False, "40px"), "상품 사진을 크게 두기", "<b>그림을 크게</b> 둡니다"),
  ]),
  keys_heads="<th>키와 마크업</th><th>지켜야 할 점</th>",
  code_lede="그림은 줄어들지 않고 글만 줄어들게 하는 두 줄이 핵심입니다.",
  code='''&lt;<span class="t">a</span> <span class="a">class</span>=<span class="s">"media"</span> <span class="a">href</span>=<span class="s">"/s/2411"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">class</span>=<span class="s">"media__img"</span> <span class="a">src</span>=<span class="s">"/t/2411.jpg"</span> <span class="a">width</span>=<span class="s">"56"</span> <span class="a">height</span>=<span class="s">"56"</span> <span class="a">alt</span>=<span class="s">""</span>&gt;
  &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"media__body"</span>&gt;
    &lt;<span class="t">b</span>&gt;한빛아웃도어 영등포타임스퀘어점&lt;/<span class="t">b</span>&gt;
    &lt;<span class="t">p</span>&gt;2026-11-12 정산 · 842,500원&lt;/<span class="t">p</span>&gt;
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">a</span>&gt;

.media { <span class="a">display</span>: flex; <span class="a">gap</span>: <span class="a">10px</span>; <span class="a">align-items</span>: flex-start; }
.media__img  { <span class="a">flex</span>: none; }        <span class="c">/* 그림은 줄어들지 않는다 */</span>
.media__body { <span class="a">min-width</span>: <span class="a">0</span>; }      <span class="c">/* 글은 줄어든다. 이 줄이 핵심 */</span>

@media (max-width: <span class="a">380px</span>) { .media { <span class="a">flex-direction</span>: column; } }''',
  keys=kbd([
    ("바깥을 링크로 감싸기", "그림과 글이 <b>한 번에</b> 눌리고, Tab 포커스도 한 번만 멈춥니다"),
    ("그림에 <code>alt=\"\"</code> 두기", "옆에 같은 내용의 글이 있으면 그림은 <b>읽지 않게</b> 둡니다"),
    ("안쪽 단추는 링크 바깥에 두기", "링크 안에 단추를 넣지 않고 <b>링크 바깥에</b> 따로 둡니다"),
    ("글 칸의 <code>min-width: 0</code>", "말줄임이 적용되지 않을 때 <b>가장 먼저</b> 확인합니다"),
    ("간격은 <code>gap</code>으로 주기", "margin 대신 씁니다. 첫 요소와 마지막 요소를 따로 처리할 필요가 없습니다"),
    ("확인하는 방법", "아주 긴 이름을 넣어 보고 <b>칸 밖으로 넘치는지</b> 봅니다"),
  ]),
  backend=rows([
    ("그림이 없을 때", "<code>thumb: null</code>이면 화면에서 <b>이니셜이나 기본 그림</b>으로 대신하고, 빈 네모를 두지 않습니다."),
    ("제목과 설명의 길이 알려 주기", "제목과 설명이 <b>대략 얼마나 긴지</b> 알면 몇 줄에서 자를지 정할 수 있습니다. 자르는 것은 서버가 아니라 화면에서 말줄임으로 합니다."),
  ]),
  plat_lede="미디어 오브젝트라는 이름은 웹에서 생겼지만, <b>같은 배치는 어느 플랫폼에나</b> 있습니다.",
  plats=plats([
    ("웹", "flex",
     mo("", "", True, "110px"),
     "<code>display: flex</code>로 두 줄이면 만들 수 있습니다. 예전에는 <code>float</code>밖에 방법이 없었습니다."),
    ("iOS", "HStack · List row",
     '''              <div class="phone" role="img" aria-label="iOS 그림-글 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:14px;height:14px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:23px;right:5px;top:28px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:23px;right:5px;top:36px;height:4px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "<code>HStack</code> 안에 그림과 <code>VStack</code>을 넣어 만들고, 구조가 웹과 <b>똑같습니다</b>."),
    ("안드로이드", "Row + Column",
     '''              <div class="phone" role="img" aria-label="안드로이드 그림-글 줄 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:15px;height:15px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:25px;right:5px;top:28px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:25px;right:5px;top:37px;height:4px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "<code>Row { Image; Column { … } }</code>로 만들고, <code>weight(1f)</code>가 웹의 <code>min-width: 0</code> 역할을 합니다."),
  ]),
  plat_note="세 플랫폼 모두 <b>가로 묶음 안에 세로 묶음</b>을 넣는 같은 구조를 쓰고, 이름만 flex, HStack, Row로 다릅니다. 글 쪽만 늘거나 줄게 한다는 규칙도 같아서, 웹의 <code>min-width: 0</code>은 안드로이드의 <code>weight(1f)</code>와 같은 역할을 합니다. <b>한 번 익히면 세 플랫폼에 모두 통하는</b> 드문 경우입니다.",
  siblings=siblings("media"),
  related='''        <li><a href="listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="thumbnail.html"><b>썸네일</b><em>5부</em></a></li>
        <li><a href="flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>''',
)
