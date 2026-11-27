# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def stage(inner, w="152px", h="78px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="height:' + h + ';position:relative;border:1px solid ' + col + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden;padding:5px">' + inner + '</div>'
            + ('<span style="font-family:var(--mono);font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def flow(t, top):
    return ('<span style="position:absolute;left:5px;right:5px;top:' + str(top) + 'px;height:14px;border-radius:3px;'
            'background:var(--ink-100);font-size:7.5px;color:var(--fg-muted);display:flex;align-items:center;padding:0 5px">' + t + '</span>')

BOX = lambda style: ('<span style="width:52px;height:14px;border-radius:3px;background:var(--accent);color:#fff;'
                     'font-size:7px;display:grid;place-items:center;' + style + '">상자</span>')
GHOST = lambda top: ('<span style="position:absolute;left:5px;right:5px;top:' + str(top) + 'px;height:14px;'
                     'border:1px dashed var(--line-strong);border-radius:3px"></span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">static   기본값, top·left가 적용되지 않음</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">relative   자리는 남기고 보이는 위치만 옮김</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">absolute   흐름에서 빠지고 가까운 positioned 조상이 기준</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">fixed   화면이 기준이라 스크롤해도 그대로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">sticky   relative와 fixed의 중간</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">transform이 걸린 조상이 fixed의 기준이 됨</div>
                </div>
              </div>'''

D = dict(
  slug="position", ko="포지션", en="Position",
  desc="포지션의 다섯 값이 자리를 차지하는지, 무엇을 기준으로 움직이는지를 보여 주고, absolute의 기준을 찾는 법과 fixed가 화면에 붙지 않는 함정을 다루는 항목입니다.",
  lede="포지션의 다섯 값은 요소가 <b>자리를 차지하는가</b>와 <b>무엇을 기준으로 움직이는가</b>, 이 두 가지를 정합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>값을 바꿔 가며 <b>점선 칸</b>을 보세요. <code>absolute</code>와 <code>fixed</code>는
          흐름에서 빠지기 때문에 <b>자리를 차지하지 않습니다</b>.<br>
          <b>가까운 조상에 relative 걸기</b>를 켜고 끄면 <code>absolute</code>의 <b>기준이 완전히 바뀝니다</b>.
          요소가 엉뚱한 곳에 붙는 문제는 거의 다 이 한 줄로 설명됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포지션, 위치 지정, 절대 위치, 고정"),
    ("영어", "position, static / relative / absolute / fixed / sticky"),
    ("같이 쓰는 말",
     "<code>static</code>이 아닌 값이 걸린 요소는 <b>positioned</b>라고 하고, "
     "<code>absolute</code>는 가장 가까운 positioned 조상을 <b>포함 블록</b>(containing block)으로 삼습니다. "
     "<code>top</code>·<code>right</code>·<code>bottom</code>·<code>left</code>를 묶어 <b>오프셋</b>이라고 부르며, "
     "요즘은 <code>inset</code> 한 줄로 적습니다."),
    ("자주 잘못 부르는 이름",
     "<b>z-index</b> — <a href=\"../items/zindex.html\">z-index</a>는 <b>앞뒤 순서</b>를 정하고 포지션은 <b>자리</b>를 정합니다. 다만 z-index는 positioned 요소에서만 적용됩니다.<br>"
     "<b>float</b> — 예전에 쓰던 배치 방법이고, 지금은 <a href=\"../items/flex.html\">플렉스</a>·<a href=\"../items/grid.html\">그리드</a>를 씁니다.<br>"
     "<b>스티키</b> — <a href=\"../items/sticky.html\">스티키</a>도 포지션 값 가운데 하나지만, 다룰 내용이 많아서 항목을 따로 두었습니다."),
  ]),
  s4_title="포지션의 다섯 값", s4_hint="값마다 달라지는 차지하는 자리와 기준",
  states=states([
    (stage(flow('앞 줄', 5) + '<span style="position:absolute;left:5px;top:21px">' + BOX('') + '</span>' + flow('뒷 줄', 37),
           "152px", "78px", "static은 흐름대로"),
     "<code>static</code>(기본값)일 때", "기본값입니다. <code>top</code>·<code>left</code>를 줘도 <b>적용되지 않습니다</b>"),
    (stage(flow('앞 줄', 5) + '<span style="position:absolute;left:17px;top:27px">' + BOX('') + '</span>' + GHOST(21) + flow('뒷 줄', 37),
           "152px", "78px", "relative는 자리를 남김", True),
     "<code>relative</code>로 옮길 때", "옮겨도 원래 자리가 남아서 <b>뒤 줄이 당겨지지 않습니다</b>"),
    (stage(flow('앞 줄', 5) + flow('뒷 줄', 21) + '<span style="position:absolute;right:6px;top:6px">' + BOX('') + '</span>',
           "152px", "78px", "absolute는 흐름에서 빠짐"),
     "<code>absolute</code>로 흐름에서 뺄 때", "<b>가장 가까운 positioned 조상</b>을 기준으로 놓입니다"),
    (stage(flow('앞 줄', 5) + flow('뒷 줄', 21) + '<span style="position:absolute;right:6px;bottom:6px">' + BOX('') + '</span>',
           "152px", "78px", "fixed는 화면이 기준"),
     "<code>fixed</code>로 화면에 붙일 때", "스크롤해도 <b>움직이지 않습니다</b>"),
    (stage(flow('굴림', 5) + '<span style="position:absolute;left:5px;top:5px">' + BOX('') + '</span>' + flow('아래', 21) + flow('계속', 37),
           "152px", "78px", "sticky는 둘의 중간"),
     "<code>sticky</code>로 둘 때", "자세한 내용은 <a href=\"../items/sticky.html\">스티키</a>에서 다룹니다"),
    (stage('<span style="position:absolute;inset:5px;border:1px dashed var(--danger);border-radius:4px;display:grid;place-items:center;font-size:7.5px;color:var(--danger)">transform이 걸린 조상</span>'
           + '<span style="position:absolute;right:9px;bottom:9px">' + BOX('') + '</span>',
           "152px", "78px", "fixed가 화면 대신 이 상자를 따름", False),
     "조상에 transform이 걸려 있을 때", "조상에 <b>transform이 있으면 그 상자가 fixed의 기준</b>이 됩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("static", "기본값", "흐름대로 놓이고, <b>오프셋이 적용되지 않습니다</b>"),
    ("relative", "자리를 남김", "보이는 위치만 옮깁니다. absolute 자식의 <b>기준점</b> 역할도 합니다"),
    ("absolute", "흐름에서 빠짐", "<b>가장 가까운 positioned 조상</b>을 기준으로 놓입니다"),
    ("fixed", "화면이 기준", "스크롤해도 움직이지 않습니다"),
    ("sticky", "relative와 fixed의 중간", "자리를 차지하면서 정해진 선에 <b>붙습니다</b>"),
    ("기준을 바꾸는 조상", "transform", "transform이 걸린 조상이 <b>fixed의 기준</b>이 됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>fixed</code> 요소가 화면에 붙지 않는</b> 문제는 거의 항상
          조상 어딘가에 <code>transform</code>·<code>filter</code>·<code>will-change</code>가
          걸려 있어서 생깁니다.
          이 속성들은 <b>새 기준점</b>을 만들기 때문에
          <code>fixed</code> 요소가 화면이 아니라 <b>그 상자</b>를 기준으로 놓입니다.
          예를 들어 애니메이션을 넣으려고 부모에 <code>transform</code>을 걸면,
          그 안의 떠 있는 메뉴가 부모 상자 안에 갇힙니다.
          이처럼 <b>원인과 결과가 멀리 떨어져 있어서</b> 찾기 어렵습니다. 같은 원리는 <a href="cheap.html">무엇을 움직이나</a>에서도 다룹니다.</p>''',
  do=ul([
    "배지, 닫기 버튼, 떠 있는 메뉴처럼 다른 요소 위에 겹쳐 올릴 때",
    "absolute의 기준을 만들 때. <b>부모에 <code>relative</code></b>를 겁니다",
    "화면에 붙여 둘 요소를 만들 때. <b>단, transform이 걸린 조상이 없는지 확인</b>합니다",
  ]),
  dont=ul([
    "전체 배치를 <code>absolute</code>로 짤 때. <a href=\"../items/flex.html\">플렉스</a>·<a href=\"../items/grid.html\">그리드</a>를 먼저 씁니다",
    "<code>relative</code>를 아무 데나 걸 때. <b>기준이 엉뚱한 곳에</b> 생깁니다",
    "<code>fixed</code>로 폰 화면 바닥에 붙일 때. <a href=\"softkeyboard.html\">키보드가 덮습니다</a>",
    "오프셋만 주고 <code>position</code>을 주지 않을 때. <b>아무 일도 일어나지 않습니다</b>",
  ]),
  instead='요소를 한 방향으로 늘어놓는 배치는 <a href="../items/flex.html">플렉스</a>로, 가로와 세로 두 방향 배치는 <a href="../items/grid.html">그리드</a>로 짭니다. 평소에는 흐름을 따르다가 스크롤하면 붙는 요소는 <a href="../items/sticky.html">스티키</a>를 씁니다.',
  cases=cases([
    (stage('<span style="position:absolute;left:6px;top:20px;width:34px;height:34px;border-radius:5px;background:var(--ink-100)"></span>'
           '<span style="position:absolute;left:32px;top:16px;width:14px;height:14px;border-radius:50%;background:var(--danger);color:#fff;font-size:7px;display:grid;place-items:center">3</span>',
           "150px", "74px", "부모에 relative"), "아이콘 모서리에 배지 붙이기", "포지션을 <b>가장 흔하게 쓰는</b> 자리입니다"),
    (stage('<span style="position:absolute;inset:6px;background:var(--surface);border:1px solid var(--line);border-radius:5px"></span>'
           '<span style="position:absolute;right:10px;top:10px;width:14px;height:14px;border-radius:3px;background:var(--bg);font-size:8px;display:grid;place-items:center">✕</span>',
           "150px", "74px", "모서리에 닫기 버튼"), "모달 모서리에 닫기 버튼 놓기", "<a href=\"../items/modal.html\">모달</a> 모서리에 닫기 버튼을 겹쳐 놓습니다"),
    (stage(flow('본문', 5) + flow('본문', 21) + '<span style="position:absolute;left:5px;right:5px;bottom:5px;height:16px;border-radius:3px;background:var(--accent)"></span>',
           "150px", "74px", "바닥에 고정"), "화면 바닥에 막대 고정하기", "폰에서는 <a href=\"softkeyboard.html\">키보드</a>가 막대를 덮지 않는지 확인합니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="포지션을 쓸 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="기준을 만들 부모에 <code>relative</code>를 걸고, 자식에 오프셋을 줍니다.",
  code='''.card {
  <span class="a">position</span>: relative;        <span class="c">/* 기준점을 만든다 */</span>
}
.card .badge {
  <span class="a">position</span>: absolute;
  <span class="a">top</span>: <span class="a">-6px</span>; <span class="a">right</span>: <span class="a">-6px</span>;   <span class="c">/* 또는 inset 한 줄로 */</span>
}

<span class="c">/* 바닥 막대. 폰 키보드와 세이프 에어리어를 함께 챙긴다 */</span>
.cta-bar {
  <span class="a">position</span>: fixed;
  <span class="a">inset</span>: auto <span class="a">0</span> <span class="a">0</span> <span class="a">0</span>;
  <span class="a">padding-bottom</span>: <span class="a">env</span>(safe-area-inset-bottom);
}

<span class="c">/* ✕ 조상에 transform이 있으면 fixed가 화면이 아니라 그 상자를 따른다 */</span>
.animated-parent { <span class="a">transform</span>: translateY(<span class="a">0</span>); }''',
  keys=kbd([
    ("오프셋을 줄 때 <code>position</code>도 함께 주기", "<code>position</code>이 <code>static</code>이면 <code>top</code>·<code>left</code>가 <b>모두 무시됩니다</b>"),
    ("네 방향 오프셋은 <code>inset</code>으로 적기", "네 방향 오프셋을 한 줄로 적습니다. <code>inset: 0</code>은 기준 상자를 꽉 채웁니다"),
    ("<a href=\"../items/zindex.html\">z-index</a>는 positioned 요소에만 주기", "positioned 요소에서만 적용되고, <code>static</code>에는 적용되지 않습니다"),
    ("자리를 옮겨도 초점 순서는 그대로라는 점 기억하기", "<code>absolute</code>로 자리를 옮겨도 <b>Tab 순서는 마크업 순서</b>를 따릅니다(<a href=\"order.html\">보이는 순서와 읽는 순서</a> 참고)"),
    ("<code>fixed</code> 요소의 조상에 <code>transform</code>이 있는지 보기", "조상에 transform이 걸려 있으면 <b>fixed의 기준이 그 조상으로 바뀝니다</b>"),
    ("폰 바닥에 붙인 요소는 키보드 위로 올리기", "<code>fixed</code>는 <a href=\"softkeyboard.html\">키보드</a>가 올라온 것을 반영하지 않으므로 <code>visualViewport</code>로 위치를 올려 줍니다"),
  ]),
  backend=rows([
    ("화면 쪽에서만 처리하는 배치", "포지션은 모두 화면 쪽에서 처리하는 배치입니다. 다만 <b>떠 있는 요소</b>가 많으면 화면을 그리는 부담이 커집니다(<a href=\"cheap.html\">무엇을 움직이나</a> 참고)."),
    ("인쇄할 때 fixed 요소 처리", "<code>fixed</code> 요소는 인쇄할 때 <b>매 쪽에 찍히거나</b> 아예 사라지기 때문에 인쇄용 스타일을 따로 둡니다."),
  ]),
  plat_lede="요소를 <b>흐름에서 빼낸다</b>는 생각은 세 플랫폼 모두 같습니다.",
  plats=plats([
    ("웹", "position",
     stage(flow('줄', 5) + '<span style="position:absolute;right:6px;top:6px">' + BOX('') + '</span>', "110px", "56px"),
     "다섯 값이 있고, 요소가 어디를 <b>기준으로 놓이는지</b> 찾는 것이 핵심입니다. 조상의 transform이 fixed의 기준을 바꿔 버리는 것이 함정입니다."),
    ("iOS", "ZStack · overlay",
     '''              <div class="phone" role="img" aria-label="iOS 겹치기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:20px;height:20px;border-radius:4px;background:var(--ink-100)"></div>
                <div style="position:absolute;left:20px;top:26px;width:10px;height:10px;border-radius:50%;background:var(--danger)"></div></div></div>''',
     "<code>ZStack</code>·<code>.overlay()</code>로 겹칩니다. <b>기준이 항상 감싼 뷰</b>라서 헷갈릴 일이 적습니다."),
    ("안드로이드", "Box · Modifier",
     '''              <div class="phone" role="img" aria-label="안드로이드 겹치기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:20px;height:20px;border-radius:4px;background:var(--ink-100)"></div>
                <div style="position:absolute;left:20px;top:26px;width:10px;height:10px;border-radius:50%;background:var(--danger)"></div></div></div>''',
     "Compose의 <code>Box</code> 안에서 <code>align</code>으로 붙이며, 여기서도 <b>기준이 분명</b>합니다."),
  ]),
  plat_note="\"배지가 엉뚱한 데 붙어요\"와 \"고정 메뉴가 화면에 안 붙어요\"는 거의 항상 <b>기준 문제</b>입니다. 앞의 경우는 조상에 <code>relative</code>가 없고, 뒤의 경우는 조상에 <code>transform</code>이 있습니다. 이 두 가지만 알아도 포지션 관련 버그는 대부분 몇 분 안에 고칠 수 있습니다.",
  siblings=siblings("position"),
  related='''        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="cheap.html"><b>무엇을 움직이나</b><em>9부</em></a></li>
        <li><a href="order.html"><b>보이는 순서와 읽는 순서</b><em>1부</em></a></li>''',
)
