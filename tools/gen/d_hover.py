# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def row(name, extra="", dim=False, w="152px"):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<div style="display:flex;align-items:center;gap:6px;padding:7px 8px;font-size:10px">'
            '<span style="flex:1;min-width:0">' + name + '</span>' + extra + '</div></div>')

X = '<span style="width:18px;height:18px;border-radius:4px;background:var(--bg);display:grid;place-items:center;font-size:9px;color:var(--fg-muted)">✕</span>'
DOTS = '<span style="width:18px;height:18px;border-radius:4px;background:var(--bg);display:grid;place-items:center;font-size:9px;color:var(--fg-muted)">⋯</span>'

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">@media (hover: hover)는 올려놓기가 되는 기기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">(pointer: fine)은 마우스처럼 뾰족한 포인터</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">(pointer: coarse)는 손가락 입력</div>
                  <div class="pin-out" data-pin="4" style="max-width:230px">''' + row('모란상회', X, False, "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">호버는 <b>부가 기능</b>이라 호버로만 되는 일은 없앰</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">:hover만 쓰면 키보드 사용자도 볼 수 없음</div>
                </div>
              </div>'''

D = dict(
  slug="hover", ko="호버가 없는 세계", en="No hover",
  desc="손가락으로 쓰는 기기에는 '올려놓기'가 없다는 전제에서, 호버로만 되는 일을 없애고 키보드 사용자까지 함께 챙기는 법을 보여 주는 항목입니다.",
  lede="손가락으로 쓰는 화면에는 마우스처럼 <b>'올려놓기'가 없습니다.</b> 그래서 호버로만 할 수 있게 만든 일은 폰에서는 할 방법이 없습니다.",
  axes_lede="PC와 폰의 차이는 기계 자체보다 화면을 쓰는 <b>전제</b>에 있습니다. 아래 네 가지를 물어보면 두 환경이 어디서 갈리는지 알 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>왼쪽 넷은 <b>마우스를 올려야</b> 보이는 정보입니다.
          <b>손가락으로 쓰는 기기로 보기</b>를 켜면 이 정보는 <b>볼 방법이 없는 정보</b>가 됩니다.<br>
          오른쪽 둘은 같은 정보를 처음부터 보이게 하거나 눌러서 보게 고친 것이라서,
          켜도 그대로 쓸 수 있습니다. 위쪽에는 지금 보는 기기의 실제 설정도 나옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "호버, 마우스 올리기, 포인터 없는 기기"),
    ("영어", "hover, pointer, hover-capable device"),
    ("같이 쓰는 말",
     "CSS에서는 <code>:hover</code>로 적고, 호버가 되는 기기인지 묻는 미디어 쿼리는 "
     "<code>@media (hover: hover)</code>와 <code>(pointer: fine)</code>입니다. "
     "손가락으로 한 번 눌렀을 때 호버 상태만 걸리고 클릭은 되지 않는 현상을 <b>더블 탭 문제</b>라고 부릅니다. "
     "손가락이 화면에 닿기 전에는 어디를 가리키는지 미리 알 수 없다는 뜻으로 <b>호버 없는 입력</b>이라고도 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>마우스 오버</b> — 옛 이벤트 이름(<code>onmouseover</code>)에서 온 말이고, 지금은 마우스·펜·손가락 입력이 <b>포인터 이벤트</b>로 묶여 있습니다.<br>"
     "<b>툴팁</b> — <a href=\"../items/tooltip.html\">툴팁</a>은 호버로 띄우는 <b>부품 하나</b>이고, 이 항목은 호버라는 전제 자체를 다룹니다.<br>"
     "<b>모바일 대응</b> — 호버가 없는 것은 화면 폭이 아니라 <b>입력 방식</b>의 문제라서, 화면이 큰 태블릿에서도 똑같이 일어납니다."),
  ]),
  axes=ax("호버가 없는 세계"),
  oneline="<b>호버는 없어도 되는 부가 기능으로 두어야 합니다.</b> 호버로 되는 일은 반드시 <b>눌러서도</b> 할 수 있어야 하고, 그렇게 만들면 키보드 사용자도 같은 기능을 쓸 수 있게 됩니다.",
  s4_title="호버가 없을 때 달라지는 것", s4_hint="사라지는 것과 고친 모습",
  do_title="호버를 써도 되는 경우",
  dont_title="호버에 기대면 안 되는 경우",
  instead_title="호버 대신 쓸 수 있는 방법",
  states=states([
    (row('모란상회', X), "PC에서 줄에 마우스를 올렸을 때", "✕가 나타납니다. 평소에는 숨어 있어서 <b>깔끔해 보입니다</b>"),
    (row('모란상회'), "폰에서 마우스를 올릴 수 없을 때", "✕가 나타나지 않으므로 <b>지울 방법이 없습니다</b>"),
    (row('모란상회', X), "✕를 늘 보이게 고친 모습", "✕를 <b>늘 보여 줍니다.</b> 화면이 조금 복잡해져도 괜찮습니다"),
    (row('모란상회', DOTS), "⋯ 메뉴로 고친 모습", "<b>⋯를 눌러</b> 메뉴를 엽니다. 줄에는 ⋯만 있어서 깔끔합니다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">
                <span style="font-size:10px">ⓘ 수수료란?</span>
                <span style="font-size:9px;color:var(--fg-muted)">눌러서 펼침</span>
              </div>''',
     "툴팁 대신 눌러서 펼치기", "설명을 <b>눌러서 펼치게</b> 합니다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">
                <span style="font-size:10px;font-weight:700">한빛아웃도어</span>
                <span style="font-size:9px;color:var(--danger);font-weight:700">9,820원 <span style="color:var(--fg-muted);font-weight:400;text-decoration:line-through">12,000원</span></span>
              </div>''',
     "할인가를 호버에 숨겼을 때", "할인가를 호버에 숨기면 <b>폰에서는 볼 수 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("기기를 묻는 질의", "@media (hover: hover)", "<b>올려놓기가 되는 기기</b>에만 호버 규칙을 적용합니다"),
    ("뾰족한 포인터", "(pointer: fine)", "마우스나 펜처럼 작은 것도 정확히 누를 수 있는 입력입니다"),
    ("뭉툭한 포인터", "(pointer: coarse)", "손가락 입력입니다. <a href=\"touchtarget.html\">터치 타깃</a>을 키워야 합니다"),
    ("늘 보이는 버튼", "버튼·메뉴", "호버로 되는 일은 <b>눌러서도</b> 할 수 있게 둡니다"),
    ("호버는 부가 기능", "progressive", "호버가 없어도 쓸 수 있고, 있으면 조금 더 편해지는 정도로 둡니다"),
    ("키보드 포커스", ":focus-visible", "<code>:hover</code>만 쓰면 <b>Tab으로 포커스를 옮긴 사용자</b>도 볼 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          실제 기기에는 <b>입력 방식이 섞여 있습니다.</b> 터치스크린이 달린 노트북도 있고,
          아이패드에 마우스를 붙이거나 폰을 모니터에 연결해 쓰기도 합니다.
          그래서 <code>(hover: hover)</code>가 참이어도 사용자가 <b>손가락으로 화면을 만질 수</b> 있고,
          거짓이어도 <b>키보드로 화면을 옮겨 다닐 수</b> 있습니다.
          '폰이냐 PC냐'로만 갈라 두면 이렇게 섞인 기기에서 화면이 깨지기 때문에,
          <b>호버는 부가 기능으로 두고 나머지 기능은 모든 기기에 똑같이 주는</b> 편이 결국 손이 덜 갑니다.</p>''',
  do=ul([
    "호버를 <b>미리보기나 강조</b>처럼 없어도 되는 효과에 쓸 때",
    "호버 규칙을 <code>@media (hover: hover)</code> 안에만 둘 때",
    "호버로 하는 일을 <b>버튼이나 메뉴</b>로도 할 수 있게 해 둘 때",
  ]),
  dont=ul([
    "삭제, 편집, 하위 메뉴 같은 <b>동작</b>을 호버에만 둘 때",
    "가격, 아이콘의 뜻, 잘린 글의 전체 같은 <b>정보</b>를 호버에만 둘 때",
    "<code>:hover</code>만 쓰고 <code>:focus-visible</code>을 빼먹을 때",
    "화면 폭으로 호버 여부를 가를 때. <b>화면이 큰 태블릿</b>도 손가락으로 씁니다",
  ]),
  instead='설명을 보여 줘야 하면 눌러서 펼치는 <a href="../items/popover.html">팝오버</a>를 쓰고, 동작이라면 ⋯ 메뉴나 <a href="../items/listitem.html">줄 안의 버튼</a>으로 꺼내 둡니다. 미리보기는 <b>없어도 쓰는 데 지장이 없게</b> 만듭니다.',
  cases=cases([
    (row('모란상회', DOTS), "동작을 ⋯ 메뉴로 모으기", "줄이 깔끔하고, 어떤 기기에서든 <b>눌러서 쓸 수</b> 있습니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>@media (hover: hover) {</span>
                <span>&nbsp;&nbsp;.row:hover .del {</span>
                <span>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:var(--accent)">opacity: 1</span></span>
                <span>&nbsp;&nbsp;}</span><span>}</span>
              </div>''',
     "호버 규칙을 미디어 쿼리 안에 두기", "손가락으로 쓰는 기기에는 이 규칙이 <b>아예 적용되지 않습니다</b>"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.row:hover .del,</span>
                <span><span style="color:var(--accent)">.row:focus-within .del</span> {</span>
                <span>&nbsp;&nbsp;opacity: 1</span><span>}</span>
              </div>''',
     "키보드 포커스에도 같이 보여 주기", "<code>:focus-within</code> 한 줄을 더하면 <b>Tab으로 다니는 사용자</b>도 같은 버튼을 볼 수 있습니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="호버 규칙은 <b>호버가 되는 기기에만</b> 적용하고, 키보드 포커스 규칙을 함께 적습니다.",
  code='''<span class="c">/* 늘 보이는 길은 모든 기기에 준다 */</span>
.row .del { <span class="a">opacity</span>: <span class="a">1</span>; }

<span class="c">/* 올려놓기가 되는 기기에서만 숨겼다가 보여 준다 */</span>
@media (hover: hover) and (pointer: fine) {
  .row .del { <span class="a">opacity</span>: <span class="a">0</span>; <span class="a">transition</span>: opacity <span class="a">120ms</span>; }
  .row:hover .del,
  .row:focus-within .del { <span class="a">opacity</span>: <span class="a">1</span>; }   <span class="c">/* 키보드도 같이 */</span>
}

<span class="c">// 자바스크립트에서 물어볼 때</span>
<span class="k">if</span> (matchMedia(<span class="s">'(hover: none)'</span>).matches) showActionsAlways();''',
  keys=kbd([
    ("<code>:focus-within</code>을 짝으로 적기", "<code>:hover</code>를 쓸 때마다 함께 적습니다. <b>이 한 줄로 키보드 사용자도</b> 같은 것을 볼 수 있습니다"),
    ("<code>@media (hover: hover)</code> 안에 두기", "손가락으로 쓰는 기기는 이 블록을 적용하지 않으므로 <b>숨기는 규칙이 아예 걸리지 않습니다</b>"),
    ("<code>(pointer: fine)</code>과 함께 걸기", "펜이나 마우스를 가리킵니다. 두 조건을 같이 걸면 터치 노트북에서 덜 어긋납니다"),
    ("손가락으로 누른 뒤 남는 <code>:hover</code>", "손가락으로 한 번 누른 뒤 호버 상태가 <b>풀리지 않고 남아</b> 있을 수 있습니다. 호버 규칙을 미디어 쿼리 안에 두면 이 문제가 생기지 않습니다"),
    ("<code>title</code> 속성으로 띄운 설명", "호버로만 뜨기 때문에 손가락으로 쓰는 기기에서는 보이지 않습니다. <b>설명을 title에만 두지 않습니다</b>"),
    ("<a href=\"../items/tooltip.html\">툴팁</a>을 띄우는 조건", "호버와 <b>포커스</b> 양쪽에서 떠야 합니다. 포커스로 뜨지 않으면 키보드 사용자는 툴팁을 볼 수 없습니다"),
  ]),
  backend=rows([
    ("호버할 때 데이터를 미리 받아 두기", "마우스를 올렸을 때 다음 화면의 데이터를 미리 받아 두는 방식은 손가락으로 쓰는 기기에서 <b>아무 효과가 없습니다.</b> 이런 기기를 위해서는 다른 시점에 미리 받는 방법이 필요합니다."),
    ("폰에서만 사용량이 낮게 나올 때", "같은 기능이 폰에서만 거의 쓰이지 않는다면, 그 기능이 <b>호버로만 보이게 숨어 있어서</b>일 수 있습니다. 사용량 숫자만 보고 '안 쓰는 기능'으로 판단해 지우면 잘못된 결정이 됩니다."),
  ]),
  plat_lede="호버가 없는 것은 <b>기기가 아니라 입력 방식</b>의 문제라서, 세 플랫폼 모두 사정이 같습니다.",
  plats=plats([
    ("웹", "hover · pointer 질의",
     row('모란상회', X, False, "110px"),
     "브라우저가 hover·pointer 미디어 쿼리로 <b>입력 방식을 물어볼 방법</b>을 줍니다. 다만 입력 방식이 섞인 기기가 많아서 참과 거짓이 늘 명확하지는 않습니다."),
    ("iOS", "호버가 없는 환경",
     '''              <div class="phone" role="img" aria-label="iOS 롱프레스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:4px;font-size:6px">길게 눌러 열기</div></div></div>''',
     "숨겨 둔 동작은 <b>길게 누르기</b>나 <b>쓸어넘기기</b>로 꺼냅니다. 아이패드에 마우스를 연결하면 호버도 쓸 수 있습니다."),
    ("안드로이드", "호버가 없는 환경",
     '''              <div class="phone" role="img" aria-label="안드로이드 오버플로 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:6px;top:30px;font-size:9px">⋮</span></div></div>''',
     "숨길 동작은 <b>오버플로 메뉴(⋮)</b>에 모으는 것이 관례입니다."),
  ]),
  plat_note="\"줄에 마우스를 올리면 삭제 버튼이 나오게\" 해 달라는 안은 PC 시안에서는 깔끔해 보이지만, 폰에서는 <b>삭제 기능이 통째로 사라집니다</b>. 이런 요청을 받으면 \"폰에서는 어떻게 지웁니까\"를 한 번 물어보세요. 대개 ⋯ 메뉴나 쓸어넘기기로 정리됩니다.",
  siblings=siblings("hover"),
  related='''        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>''',
)
