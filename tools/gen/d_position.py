# -*- coding: utf-8 -*-
from ax1 import ax
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">static — 기본. top · left 가 안 먹는다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">relative — 자리는 그대로, 보이기만 옮긴다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">absolute — 흐름에서 빠진다. 기준은 가까운 positioned 조상</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">fixed — 화면을 기준으로. 굴려도 안 움직인다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">sticky — relative 와 fixed 사이</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">transform 이 걸린 조상은 fixed 의 기준이 되어 버린다</div>
                </div>
              </div>'''

D = dict(
  slug="position", ko="포지션", en="Position",
  desc="다섯 값이 자리를 차지하는지와 무엇을 기준으로 움직이는지. absolute의 기준 찾기와 fixed의 함정.",
  lede="다섯 값이 다루는 것은 둘입니다 — <b>자리를 차지하는가</b>와 <b>무엇을 기준으로 움직이는가</b>.",
  axes_lede="뼈대는 눈에 안 보이지만 <b>모든 화면이 그 위에</b> 섭니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>값을 바꿔 가며 <b>점선 칸</b>을 보세요 — <code>absolute</code>·<code>fixed</code>는
          흐름에서 빠져 <b>자리를 안 차지합니다</b>.<br>
          <b>가까운 조상에 relative 걸기</b>를 켜고 끄면 <code>absolute</code>의 <b>기준이 통째로 바뀝니다</b>.
          이 한 줄이 '왜 엉뚱한 데 붙지' 의 거의 모든 답입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "포지션, 위치 지정, 절대 위치, 고정"),
    ("영어", "position, static / relative / absolute / fixed / sticky"),
    ("같이 쓰는 말",
     "<code>static</code>이 아닌 값이 걸린 요소를 <b>positioned</b> 라 하고, "
     "<code>absolute</code>는 가장 가까운 positioned 조상을 <b>포함 블록</b>(containing block)으로 삼습니다. "
     "<code>top</code>·<code>right</code>·<code>bottom</code>·<code>left</code>를 묶어 <b>오프셋</b>이라 하고, "
     "요즘은 <code>inset</code> 한 줄로 적습니다."),
    ("자주 잘못 부름",
     "<b>z-index</b> — <a href=\"../items/zindex.html\">z-index</a>는 <b>앞뒤</b>이고 포지션은 <b>자리</b>입니다. 다만 z-index 는 positioned 에서만 먹습니다.<br>"
     "<b>float</b> — 옛 배치 방법입니다. 지금은 <a href=\"../items/flex.html\">플렉스</a>·<a href=\"../items/grid.html\">그리드</a>를 씁니다.<br>"
     "<b>스티키</b> — <a href=\"../items/sticky.html\">스티키</a>는 포지션의 한 값이지만 다루는 바가 달라 따로 뒀습니다."),
  ]),
  axes=ax("포지션"),
  oneline="<b><code>absolute</code>가 엉뚱한 데 붙으면 조상에 <code>relative</code>가 없는 것입니다.</b> 이것이 거의 유일한 원인입니다.",
  s4_title="다섯 값", s4_hint="자리를 차지하나",
  states=states([
    (stage(flow('앞 줄', 5) + '<span style="position:absolute;left:5px;top:21px">' + BOX('') + '</span>' + flow('뒷 줄', 37),
           "152px", "78px", "static — 흐름대로"),
     "static", "기본값. <code>top</code>·<code>left</code>가 <b>안 먹는다</b>"),
    (stage(flow('앞 줄', 5) + '<span style="position:absolute;left:17px;top:27px">' + BOX('') + '</span>' + GHOST(21) + flow('뒷 줄', 37),
           "152px", "78px", "relative — 자리는 그대로", True),
     "relative", "<b>뒤 줄이 안 당겨진다</b>"),
    (stage(flow('앞 줄', 5) + flow('뒷 줄', 21) + '<span style="position:absolute;right:6px;top:6px">' + BOX('') + '</span>',
           "152px", "78px", "absolute — 흐름에서 빠짐"),
     "absolute", "<b>가까운 positioned 조상</b>이 기준"),
    (stage(flow('앞 줄', 5) + flow('뒷 줄', 21) + '<span style="position:absolute;right:6px;bottom:6px">' + BOX('') + '</span>',
           "152px", "78px", "fixed — 화면 기준"),
     "fixed", "굴려도 <b>안 움직인다</b>"),
    (stage(flow('굴림', 5) + '<span style="position:absolute;left:5px;top:5px">' + BOX('') + '</span>' + flow('아래', 21) + flow('계속', 37),
           "152px", "78px", "sticky — 둘 사이"),
     "sticky", "<a href=\"../items/sticky.html\">스티키</a>에서 자세히"),
    (stage('<span style="position:absolute;inset:5px;border:1px dashed var(--danger);border-radius:4px;display:grid;place-items:center;font-size:7.5px;color:var(--danger)">transform 걸린 조상</span>'
           + '<span style="position:absolute;right:9px;bottom:9px">' + BOX('') + '</span>',
           "152px", "78px", "fixed 가 화면이 아니라 이 상자를 따른다", False),
     "fixed 의 함정", "<b>transform 이 기준을 가로챈다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("static", "기본", "흐름대로. <b>오프셋이 안 먹는다</b>"),
    ("relative", "자리는 그대로", "보이기만 옮긴다. <b>기준점</b> 노릇도 한다"),
    ("absolute", "흐름에서 빠짐", "기준은 <b>가까운 positioned 조상</b>"),
    ("fixed", "화면 기준", "굴려도 안 움직인다"),
    ("sticky", "둘 사이", "자리는 차지하면서 <b>붙는다</b>"),
    ("가로채는 것", "transform", "걸린 조상이 <b>fixed 의 기준</b>이 되어 버린다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>fixed</code>가 화면에 안 붙는다</b>는 사고는 거의 늘
          조상 어딘가에 <code>transform</code>·<code>filter</code>·<code>will-change</code>가
          걸려 있어서입니다.
          그 속성들은 <b>새 기준점</b>을 만들기 때문에,
          <code>fixed</code>가 화면이 아니라 <b>그 상자</b>를 따릅니다.
          애니메이션을 넣으려고 <code>transform</code>을 건 부모가
          그 안의 떠 있는 메뉴를 가둬 버리는 식이라,
          <b>원인과 결과가 멀리 떨어져</b> 찾기 어렵습니다 — <a href="cheap.html">무엇을 움직이나</a>와 같은 뿌리입니다.</p>''',
  do=ul([
    "겹쳐 올리는 것 — 배지·닫기 버튼·떠 있는 메뉴",
    "기준을 만들 때 <b>부모에 <code>relative</code></b>",
    "화면에 붙여 둘 것 — <b>단, transform 조상을 확인</b>하고",
  ]),
  dont=ul([
    "배치를 <code>absolute</code>로 — <a href=\"../items/flex.html\">플렉스</a>·<a href=\"../items/grid.html\">그리드</a>가 먼저다",
    "<code>relative</code>를 아무 데나 — <b>기준이 엉뚱한 데</b> 생긴다",
    "<code>fixed</code>로 폰 바닥에 붙이기 — <a href=\"softkeyboard.html\">키보드가 덮는다</a>",
    "오프셋만 주고 <code>position</code>을 안 주기 — <b>아무 일도 안 난다</b>",
  ]),
  instead='한 방향 배치는 <a href="../items/flex.html">플렉스</a>, 두 방향은 <a href="../items/grid.html">그리드</a>, 붙었다 떨어지는 것은 <a href="../items/sticky.html">스티키</a>.',
  cases=cases([
    (stage('<span style="position:absolute;left:6px;top:20px;width:34px;height:34px;border-radius:5px;background:var(--ink-100)"></span>'
           '<span style="position:absolute;left:32px;top:16px;width:14px;height:14px;border-radius:50%;background:var(--danger);color:#fff;font-size:7px;display:grid;place-items:center">3</span>',
           "150px", "74px", "부모에 relative"), "배지", "<b>가장 흔한 쓰임</b>"),
    (stage('<span style="position:absolute;inset:6px;background:var(--surface);border:1px solid var(--line);border-radius:5px"></span>'
           '<span style="position:absolute;right:10px;top:10px;width:14px;height:14px;border-radius:3px;background:var(--bg);font-size:8px;display:grid;place-items:center">✕</span>',
           "150px", "74px", "모서리에 닫기"), "닫기 버튼", "<a href=\"../items/modal.html\">모달</a> 모서리"),
    (stage(flow('본문', 5) + flow('본문', 21) + '<span style="position:absolute;left:5px;right:5px;bottom:5px;height:16px;border-radius:3px;background:var(--accent)"></span>',
           "150px", "74px", "바닥에 고정"), "바닥 막대", "폰에서는 <a href=\"softkeyboard.html\">키보드</a>를 조심"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 자리의 계약서",
  code_lede="기준을 만들 부모에 <code>relative</code>를 걸고, 자식에 오프셋을 줍니다.",
  code='''.card {
  <span class="a">position</span>: relative;        <span class="c">/* 기준점을 만든다 */</span>
}
.card .badge {
  <span class="a">position</span>: absolute;
  <span class="a">top</span>: <span class="a">-6px</span>; <span class="a">right</span>: <span class="a">-6px</span>;   <span class="c">/* 또는 inset 한 줄로 */</span>
}

<span class="c">/* 바닥 막대 — 폰 키보드와 세이프 에어리어를 함께 */</span>
.cta-bar {
  <span class="a">position</span>: fixed;
  <span class="a">inset</span>: auto <span class="a">0</span> <span class="a">0</span> <span class="a">0</span>;
  <span class="a">padding-bottom</span>: <span class="a">env</span>(safe-area-inset-bottom);
}

<span class="c">/* ✕ 조상에 transform 이 있으면 fixed 가 화면이 아니라 그 상자를 따른다 */</span>
.animated-parent { <span class="a">transform</span>: translateY(<span class="a">0</span>); }''',
  keys=kbd([
    ("오프셋만으로는 안 된다", "<code>position</code>이 <code>static</code>이면 <code>top</code>·<code>left</code>가 <b>통째로 무시</b>된다"),
    ("<code>inset</code>", "네 방향을 한 줄로. <code>inset: 0</code>이 꽉 채우기다"),
    ("<a href=\"../items/zindex.html\">z-index</a>", "positioned 에서만 먹는다. <code>static</code>에는 안 통한다"),
    ("초점 순서는 안 바뀐다", "<code>absolute</code>로 옮겨도 <b>Tab 은 마크업 순서</b>다 — <a href=\"order.html\">보이는 순서와 읽는 순서</a>"),
    ("<code>fixed</code>와 <code>transform</code>", "조상에 걸려 있으면 <b>기준이 가로채진다</b>"),
    ("폰 바닥", "<code>fixed</code>는 <a href=\"softkeyboard.html\">키보드</a>를 모른다. <code>visualViewport</code>로 올려 준다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "전부 화면 쪽 배치입니다. 다만 <b>떠 있는 요소</b>가 많으면 그리기가 무거워집니다 — <a href=\"cheap.html\">무엇을 움직이나</a>."),
    ("인쇄", "<code>fixed</code>는 인쇄에서 <b>매 쪽에 찍히거나</b> 사라집니다. 인쇄용 스타일을 따로 둡니다."),
  ]),
  plat_lede="<b>흐름에서 빼낸다</b>는 생각은 어디나 같습니다.",
  plats=plats([
    ("웹", "position",
     stage(flow('줄', 5) + '<span style="position:absolute;right:6px;top:6px">' + BOX('') + '</span>', "110px", "56px"),
     "다섯 값이 있고 <b>기준 찾기</b>가 핵심입니다. transform 이 기준을 가로채는 것이 함정입니다."),
    ("iOS", "ZStack · overlay",
     '''              <div class="phone" role="img" aria-label="iOS 겹치기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:20px;height:20px;border-radius:4px;background:var(--ink-100)"></div>
                <div style="position:absolute;left:20px;top:26px;width:10px;height:10px;border-radius:50%;background:var(--danger)"></div></div></div>''',
     "<code>ZStack</code>·<code>.overlay()</code>로 겹칩니다. <b>기준은 감싼 뷰</b>라 헷갈릴 일이 적습니다."),
    ("안드로이드", "Box · Modifier",
     '''              <div class="phone" role="img" aria-label="안드로이드 겹치기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:20px;height:20px;border-radius:4px;background:var(--ink-100)"></div>
                <div style="position:absolute;left:20px;top:26px;width:10px;height:10px;border-radius:50%;background:var(--danger)"></div></div></div>''',
     "Compose 의 <code>Box</code> 안에서 <code>align</code>으로 붙입니다. 역시 <b>기준이 분명</b>합니다."),
  ]),
  plat_note="\"배지가 엉뚱한 데 붙어요\"와 \"고정 메뉴가 화면에 안 붙어요\"는 거의 늘 <b>기준 문제</b>입니다. 앞은 조상에 <code>relative</code>가 없는 것이고, 뒤는 조상에 <code>transform</code>이 있는 것입니다. 이 둘만 알아도 포지션 관련 버그의 대부분이 몇 분 안에 끝납니다.",
  siblings=siblings("position"),
  related='''        <li><a href="../items/sticky.html"><b>스티키</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="cheap.html"><b>무엇을 움직이나</b><em>9부</em></a></li>
        <li><a href="order.html"><b>보이는 순서와 읽는 순서</b><em>1부</em></a></li>''',
)
