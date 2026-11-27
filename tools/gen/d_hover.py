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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">@media (hover: hover) — 올려놓기가 되는 기기</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">(pointer: fine) — 마우스처럼 뾰족한 포인터</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">(pointer: coarse) — 손가락</div>
                  <div class="pin-out" data-pin="4" style="max-width:230px">''' + row('모란상회', X, False, "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">호버는 <b>덤</b> — 호버로만 되는 일을 두지 않는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">:hover 만 쓰면 키보드 사용자도 같은 처지가 된다</div>
                </div>
              </div>'''

D = dict(
  slug="hover", ko="호버가 없는 세계", en="No hover",
  desc="손가락에는 '올려놓기'가 없다. 호버로만 되는 일을 없애고, 키보드도 같이 챙기는 법.",
  lede="손가락에는 <b>'올려놓기'가 없습니다.</b> 호버로만 되는 일은 폰에서 영영 안 됩니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>왼쪽 넷은 <b>마우스를 올려야</b> 보이는 정보입니다.
          <b>손가락으로 쓰는 기기로 보기</b>를 켜면 그 순간 <b>영영 볼 수 없는 정보</b>가 됩니다.<br>
          오른쪽 둘은 같은 정보를 처음부터 보이게 하거나 눌러서 보게 고친 것입니다 —
          켜도 그대로 쓸 수 있습니다. 위에 이 기기의 실제 설정도 나옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "호버, 마우스 올리기, 포인터 없는 기기"),
    ("영어", "hover, pointer, hover-capable device"),
    ("같이 쓰는 말",
     "CSS 로는 <code>:hover</code>이고, 기기를 가리는 질의가 "
     "<code>@media (hover: hover)</code>·<code>(pointer: fine)</code>입니다. "
     "손가락으로 한 번 눌렀을 때 호버만 걸리고 클릭이 안 되는 현상을 <b>더블 탭 문제</b>라 부릅니다. "
     "손가락이 닿기 전에 미리 알 수 없다는 뜻으로 <b>호버 없는 입력</b>이라고도 합니다."),
    ("자주 잘못 부름",
     "<b>마우스 오버</b> — 옛 이벤트 이름(<code>onmouseover</code>)이고 지금은 <b>포인터 이벤트</b>로 묶여 있습니다.<br>"
     "<b>툴팁</b> — <a href=\"../items/tooltip.html\">툴팁</a>은 호버로 띄우는 <b>한 부품</b>이고, 이쪽은 그 전제에 대한 이야기입니다.<br>"
     "<b>모바일 대응</b> — 폭의 문제가 아닙니다. <b>입력 방식</b>의 문제라 큰 태블릿에서도 똑같습니다."),
  ]),
  axes=ax("호버가 없는 세계"),
  oneline="<b>호버는 덤이어야 합니다.</b> 호버로 되는 일은 반드시 <b>눌러서도</b> 되어야 하고, 그러면 키보드 사용자도 같이 구제됩니다.",
  s4_title="호버가 없으면", s4_hint="무엇이 사라지나",
  states=states([
    (row('모란상회', X), "PC — 줄에 올렸을 때", "✕ 가 나타난다. <b>깔끔해 보인다</b>"),
    (row('모란상회'), "폰 — 올릴 수가 없다", "<b>지울 방법이 없다</b>"),
    (row('모란상회', X), "고친 것 ①", "✕ 를 <b>늘 보여 준다.</b> 조금 복잡해도 된다"),
    (row('모란상회', DOTS), "고친 것 ②", "<b>⋯ 를 눌러</b> 메뉴를 연다. 줄이 깨끗하다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">
                <span style="font-size:10px">ⓘ 수수료란?</span>
                <span style="font-size:9px;color:var(--fg-muted)">눌러서 펼친다</span>
              </div>''',
     "툴팁 대신", "설명을 <b>눌러서 펼치게</b> 한다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">
                <span style="font-size:10px;font-weight:700">한빛아웃도어</span>
                <span style="font-size:9px;color:var(--danger);font-weight:700">9,820원 <span style="color:var(--fg-muted);font-weight:400;text-decoration:line-through">12,000원</span></span>
              </div>''',
     "할인가도 마찬가지", "호버에 숨기면 <b>폰에서 못 본다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("기기를 묻는 질의", "@media (hover: hover)", "<b>올려놓기가 되는 기기</b>에만 호버 규칙을 준다"),
    ("뾰족한 포인터", "(pointer: fine)", "마우스·펜. 작은 것도 정확히 누른다"),
    ("뭉툭한 포인터", "(pointer: coarse)", "손가락. <a href=\"touchtarget.html\">터치 타깃</a>을 키워야 한다"),
    ("늘 보이는 길", "버튼·메뉴", "호버로 되는 일은 <b>눌러서도</b> 되게 둔다"),
    ("호버는 덤", "progressive", "없어도 쓸 수 있고, 있으면 조금 더 편한 것"),
    ("키보드도 같은 처지", ":focus-visible", "<code>:hover</code>만 쓰면 <b>Tab 으로 온 사람</b>도 못 본다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>기기는 한 가지가 아닙니다.</b> 노트북에 터치스크린이 달려 있고,
          아이패드에 마우스를 붙이고, 폰을 모니터에 연결해 씁니다.
          그래서 <code>(hover: hover)</code>가 참이어도 <b>손가락으로 만질 수</b> 있고,
          거짓이어도 <b>키보드로 다닐 수</b> 있습니다.
          '폰이냐 PC냐'로 갈라 두면 그 중간이 전부 깨집니다 —
          <b>호버는 덤으로 두고 나머지는 모두에게 주는</b> 쪽이 결국 더 적게 일합니다.</p>''',
  do=ul([
    "호버를 <b>미리보기·강조</b>로 쓰기 — 없어도 되는 것",
    "<code>@media (hover: hover)</code> 안에만 호버 규칙 두기",
    "같은 일을 <b>버튼이나 메뉴</b>로도 할 수 있게",
  ]),
  dont=ul([
    "호버에만 있는 <b>동작</b> — 삭제·편집·하위 메뉴",
    "호버에만 있는 <b>정보</b> — 가격, 아이콘 뜻, 전체 글",
    "<code>:hover</code>만 쓰고 <code>:focus-visible</code>을 빼먹기",
    "폭으로 가르기 — <b>큰 태블릿</b>도 손가락이다",
  ]),
  instead='설명이면 눌러서 펼치는 <a href="../items/popover.html">팝오버</a>, 동작이면 ⋯ 메뉴나 <a href="../items/listitem.html">줄 안의 버튼</a>, 미리보기면 <b>없어도 되게</b>.',
  cases=cases([
    (row('모란상회', DOTS), "⋯ 로 모으기", "줄은 깨끗하고 <b>어디서나 눌린다</b>"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>@media (hover: hover) {</span>
                <span>&nbsp;&nbsp;.row:hover .del {</span>
                <span>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:var(--accent)">opacity: 1</span></span>
                <span>&nbsp;&nbsp;}</span><span>}</span>
              </div>''',
     "호버 규칙을 가둔다", "손가락 기기에는 <b>아예 안 들어간다</b>"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.row:hover .del,</span>
                <span><span style="color:var(--accent)">.row:focus-within .del</span> {</span>
                <span>&nbsp;&nbsp;opacity: 1</span><span>}</span>
              </div>''',
     "키보드도 같이", "<code>:focus-within</code> 한 줄로 <b>Tab 사용자</b>가 구제된다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 전제의 계약서",
  code_lede="호버 규칙은 <b>되는 기기에만</b> 주고, 키보드를 같이 적습니다.",
  code='''<span class="c">/* 늘 되는 길 — 모두에게 준다 */</span>
.row .del { <span class="a">opacity</span>: <span class="a">1</span>; }

<span class="c">/* 덤 — 올려놓기가 되는 기기에서만 숨겼다 보여 준다 */</span>
@media (hover: hover) and (pointer: fine) {
  .row .del { <span class="a">opacity</span>: <span class="a">0</span>; <span class="a">transition</span>: opacity <span class="a">120ms</span>; }
  .row:hover .del,
  .row:focus-within .del { <span class="a">opacity</span>: <span class="a">1</span>; }   <span class="c">/* 키보드도 같이 */</span>
}

<span class="c">// 자바스크립트에서 물어볼 때</span>
<span class="k">if</span> (matchMedia(<span class="s">'(hover: none)'</span>).matches) showActionsAlways();''',
  keys=kbd([
    ("<code>:focus-within</code>을 짝으로", "<code>:hover</code>를 쓸 때마다 함께 적는다. <b>한 줄로 키보드가 구제된다</b>"),
    ("<code>@media (hover: hover)</code>", "손가락 기기는 이 블록을 아예 안 읽는다. <b>숨기는 코드가 안 들어간다</b>"),
    ("<code>(pointer: fine)</code>과 함께", "펜·마우스. 둘을 같이 걸면 터치 노트북에서 덜 어긋난다"),
    ("<code>:hover</code>가 손가락에서 남는다", "한 번 누른 뒤 호버 상태가 <b>그대로 붙어</b> 있을 수 있다. 질의로 가두면 안 생긴다"),
    ("<code>title</code> 속성", "호버로만 뜨고 손가락에서는 안 보인다. <b>설명을 title 에만 두지 않는다</b>"),
    ("<a href=\"../items/tooltip.html\">툴팁</a>", "호버와 <b>초점</b> 둘 다로 떠야 한다. 초점으로 안 뜨면 키보드에서 없는 것과 같다"),
  ]),
  backend=rows([
    ("미리 받아 두는 것", "호버할 때 미리 데이터를 받는 방식은 손가락 기기에서 <b>아무 효과가 없습니다.</b> 그쪽에는 다른 전략이 필요합니다."),
    ("쓰임이 다르게 찍힌다", "같은 기능이 폰에서만 거의 안 쓰인다면 <b>호버에 숨어 있어서</b>일 수 있습니다. 숫자만 보고 '안 쓰는 기능'으로 지우면 틀립니다."),
  ]),
  plat_lede="<b>기기가 아니라 입력 방식</b>의 문제라 셋 모두 같습니다.",
  plats=plats([
    ("웹", "hover · pointer 질의",
     row('모란상회', X, False, "110px"),
     "브라우저가 <b>기기를 물어볼 길</b>을 줍니다. 다만 기기가 섞여 있어 참·거짓이 늘 명확하진 않습니다."),
    ("iOS", "호버가 없다",
     '''              <div class="phone" role="img" aria-label="iOS 롱프레스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:4px;font-size:6px">길게 눌러 메뉴</div></div></div>''',
     "숨은 동작은 <b>길게 누르기</b>나 <b>쓸어넘기기</b>로 꺼냅니다. 아이패드에 마우스를 붙이면 호버가 생깁니다."),
    ("안드로이드", "호버가 없다",
     '''              <div class="phone" role="img" aria-label="안드로이드 오버플로 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:6px;top:30px;font-size:9px">⋮</span></div></div>''',
     "<b>오버플로 메뉴(⋮)</b>가 관례입니다. 숨길 동작은 거기 모읍니다."),
  ]),
  plat_note="\"줄에 올리면 삭제 버튼이 나오게\"는 PC 시안에서 가장 깔끔해 보이는 안이고, <b>폰에서 기능이 통째로 사라지는</b> 안이기도 합니다. 받을 때 \"폰에서는 어떻게 지웁니까\"를 한 번 물어보면, 대개 ⋯ 메뉴나 쓸어넘기기로 정리됩니다.",
  siblings=siblings("hover"),
  related='''        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>
        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>''',
)
