# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def card(op, label, note="", ok=None, color=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    st = 'opacity:' + op + ';' if op else ''
    cl = 'color:' + color + ';' if color else ''
    return ('              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">'
            '<span style="display:block;width:116px;border:1px solid ' + col + ';border-radius:6px;'
            'background:var(--surface);padding:7px 8px;' + st + '">'
            '<span style="display:block;font-size:9.5px;' + cl + '">정산 2건이 밀렸습니다</span></span>'
            '<span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:11px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">opacity<span style="color:var(--fg-faint)"> ← 상자와 자식 <b>전부</b></span></div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">rgba(…, .5)<span style="color:var(--fg-faint)"> ← 그 색 하나만</span></div>
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">1 미만이면 <b>쌓임 문맥</b>이 생김</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">자식의 z-index가 그 안에 갇힘</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">대비비도 같이 떨어짐</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">흐린 색 토큰<span style="color:var(--fg-faint)"> ← 미리 맞춰 둔 값</span></div>
                </div>
              </div>'''

D = dict(
  slug="opacity", ko="불투명도", en="Opacity",
  desc="요소를 흐리게 하는 세 가지 방법의 차이와, opacity가 대비비와 z-index에 일으키는 부작용을 보여 주는 항목입니다.",
  lede="<code>opacity</code>는 <b>상자 안의 모든 것</b>을 한꺼번에 흐리게 합니다. 쓰기는 간단하지만 영향이 미치는 범위가 넓어서, 흔히 쓰는 만큼 잘못 쓰는 일도 많습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모는 글자의 <b>대비비를 재서 적어 줍니다</b>. 흰 바탕 위 글자를 <code>opacity: .5</code>로
          흐리면 대비비가 4.5:1 아래로 떨어지기 때문에, 비활성 상태를 이렇게 만들면 <b>읽기 어려운 글</b>이 됩니다.<br>
          눈에 잘 띄지 않는 문제도 하나 더 있습니다. <code>opacity</code>가 1보다 작아지면 그 상자가 새
          <b>쌓임 문맥</b>을 만들어서, 안에 있는 <code>z-index: 5</code> 배지가 바깥의
          <code>z-index: 2</code> 덮개 위로 올라가지 못합니다. 데모는 겹치는 자리를 실제로 찍어 어느 쪽이 위에 있는지 확인합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "불투명도, 투명도, 알파"),
    ("영어", "opacity, alpha, transparency"),
    ("같이 쓰는 말",
     "상자 전체에 거는 투명도는 <b>opacity</b>, 색 하나에만 거는 투명도는 <b>알파</b>(<code>rgba</code>·<code>#rrggbbaa</code>)입니다. "
     "둘은 겉보기가 비슷해도 <b>영향을 주는 범위와 부작용</b>이 다릅니다. "
     "모달 뒤에 까는 반투명 판은 따로 <b>가림막</b>(scrim · backdrop)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>visibility</b> — <code>visibility: hidden</code>은 <b>자리는 그대로 차지한 채</b> 보이지만 않게 합니다.<br>"
     "<b>display: none</b> — 요소가 화면에서 아예 빠지고, 스크린 리더도 읽어 주지 않습니다.<br>"
     "<b>disabled</b> — <a href=\"field.html\">비활성</a>은 요소의 <b>상태</b>이고, 흐리게 하는 것은 그 상태를 보여 주는 여러 방법 가운데 하나입니다."),
  ]),
  s4_title="요소를 흐리게 하는 방법", s4_hint="방법마다 다른 범위와 부작용",
  states=states([
    (card("", "그대로", "대비비 통과", True), "흐리지 않은 기준", "비교할 기준입니다"),
    (card(".5", "opacity: .5", "전부 흐려짐", False), "상자 전체에 opacity를 걸 때", "<b>글과 버튼, 배지까지</b> 함께 흐려집니다"),
    (card("", "rgba(…, .5)", "글자만 흐려짐", None, "rgba(32,35,42,.5)"),
     "색에만 알파를 걸 때", "그 색만 흐려지고 쌓임 문맥은 <b>생기지 않습니다</b>"),
    (card("", "--fg-muted", "미리 맞춰 둔 값", True, "var(--fg-muted)"),
     "흐린 색 토큰을 쓸 때", "미리 맞춰 둔 값이라 <b>대비비를 지킵니다</b>"),
    ('''              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">
                <span style="display:block;position:relative;width:116px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px 8px">
                  <span style="display:block;font-size:9.5px">정산 2건이 밀렸습니다</span>
                  <span style="position:absolute;inset:0;border-radius:6px;background:color-mix(in srgb, var(--fg) 45%, transparent)"></span>
                </span>
                <span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted)">가림막</span>
                <span style="font-size:10px;color:var(--fg-faint);text-align:center">위에 반투명 판을 덮음</span>
              </div>''',
     "가림막으로 덮을 때", "아래 내용을 흐린 것이 아니라 반투명 판으로 <b>덮은</b> 것입니다"),
    (card(".4", "opacity: .4", "z-index가 갇힘", False), "쌓임 문맥이 생길 때", "<b>안쪽 요소가 바깥 요소 위로 올라가지 못합니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>opacity</code>", "상자 전부", "자식 요소에서 <b>되돌릴 수 없습니다</b>"),
    ("알파", "그 색만", "영향 범위가 <b>좁아서</b> 안전합니다"),
    ("쌓임 문맥", "1 미만이면", "쌓임 문맥이 <b>생기고</b>, 자식 쪽에서는 이를 되돌릴 방법이 없습니다"),
    ("갇힌 z-index", "바깥을 못 넘음", "모달이나 툴팁이 <b>가려지는</b> 원인이 됩니다"),
    ("대비비", "같이 떨어짐", "비활성 글이 <b>잘 읽히지 않습니다</b>"),
    ("흐린 색 토큰", "미리 맞춘 값", "<b>권하는 방법</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'툴팁이 왜 안 보이지'</b> 하는 문제의 원인이 여기 있는 경우가 많습니다.
          조상 요소 어딘가에 <code>opacity: .99</code> 같은 값이 하나 걸려 있으면
          그 안의 <code>z-index</code>는 얼마나 키우든 그 조상 바깥의 요소보다 위로 올라가지 못합니다.
          <code>transform</code>·<code>filter</code>·<code>will-change</code>도 같은 결과를 만듭니다.<br>
          비활성 상태에서도 opacity는 문제를 일으킵니다. <code>opacity: .5</code>는 <b>글자뿐 아니라</b>
          테두리와 아이콘까지 함께 흐려서 모두의 대비비를 떨어뜨립니다.
          그래서 <b>흐린 색을 토큰으로 따로 두는 것</b>이 해결책입니다.</p>''',
  do_title="불투명도를 다룰 때 지킬 것",
  dont_title="불투명도를 다룰 때 피할 것",
  do=ul([
    "비활성은 <b>흐린 색 토큰</b>으로 만들기",
    "흐리게 할 것이 하나면 <b>알파</b>로 색에만 걸기",
    "가림막은 <code>opacity</code>가 아니라 <b>반투명 색</b>으로 덮기",
  ]),
  dont=ul([
    "<code>opacity: .5</code>로 비활성 만들기. <b>대비비가 기준에 못 미칩니다</b>",
    "조상에 <code>opacity: .99</code> 걸기. <b>그 안의 z-index가 바깥 요소 위로 올라가지 못합니다</b>",
    "<code>opacity: 0</code>으로 숨기기. 보이지 않아도 <b>여전히 눌리고 스크린 리더가 읽습니다</b>",
    "흐린 글을 <b>본문</b>에 쓰기. 읽으라고 쓴 글은 흐리게 두지 않습니다",
  ]),
  instead_title="함께 보면 좋은 항목",
  instead='요소를 감추는 올바른 방법은 <a href="semantics.html">시맨틱 태그</a> 항목에서, 요소가 겹치는 순서는 <a href="zindex.html">z-index</a> 항목에서 다룹니다. 글이 읽히는 밝기는 <a href="contrast.html">대비비</a> 항목에서, 색 자체를 정하는 방법은 <a href="color.html">색 토큰</a> 항목에서 설명합니다.',
  cases=cases([
    (card("", "비활성", "흐린 색 토큰 + aria-disabled", True, "var(--fg-muted)"),
     "버튼의 비활성 상태 만들기", "opacity 대신 <b>색으로</b> 흐리게 만듭니다"),
    (one(txt('<span style="display:block;position:relative;height:30px;border-radius:5px;background:var(--surface);border:1px solid var(--line)">'
             '<span style="position:absolute;inset:0;border-radius:5px;background:color-mix(in srgb, var(--fg) 45%, transparent)"></span></span>'),
         "가림막", True, "모달 뒤를 덮음", "116px"),
     "모달 뒤에 가림막 깔기", "흐리게 하는 것이 아니라 위에 덮는 <b>덮개</b>로 다룹니다"),
    (card("", "지도 위 글", "읽을 글은 흐리지 않음", True), "지도 위에 글 얹기", "읽어야 할 글은 흐리지 않고, 글 아래에 바탕을 <b>깔고</b> 씁니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="불투명도를 코드로 옮기는 방법",
  keys_heads="<th>값과 개념</th><th>알아 둘 점</th>",
  code_lede="흐린 색을 토큰으로 정해 두면 대비비를 처음 한 번만 재면 됩니다.",
  code='''<span class="c">/* 미리 대비비를 맞춰 둔 흐린 색 */</span>
:root {
  --fg-muted: <span class="a">#5c6370</span>;   <span class="c">/* 흰 바탕에서 4.9:1 */</span>
  --scrim: <span class="a">rgba</span>(20, 22, 26, <span class="a">.45</span>);
}

<span class="c">/* 비활성은 색으로 만든다 */</span>
.btn[disabled] { <span class="a">color</span>: <span class="a">var</span>(--fg-muted); <span class="a">background</span>: <span class="a">var</span>(--bg); <span class="a">cursor</span>: not-allowed; }

<span class="c">/* 가림막은 흐리는 것이 아니라 위에 덮는 것이다 */</span>
.scrim { <span class="a">position</span>: fixed; <span class="a">inset</span>: <span class="a">0</span>; <span class="a">background</span>: <span class="a">var</span>(--scrim); }

<span class="c">/* ✕ 대비비가 떨어지고 z-index 가 갇힌다 */</span>
.btn[disabled] { <span class="a">opacity</span>: <span class="a">.5</span>; }''',
  keys=kbd([
    ("<code>opacity: 0</code>", "보이지만 않을 뿐 <b>여전히 눌리고 읽힙니다</b>. 숨기려면 <code>hidden</code>을 씁니다"),
    ("쌓임 문맥", "<code>opacity</code>·<code>transform</code>·<code>filter</code>를 주면 생깁니다"),
    ("<code>color-mix()</code>", "요즘 브라우저에서 색에 <b>알파를 깔끔하게</b> 섞는 방법입니다"),
    ("대비비 4.5:1", "본문 글의 기준입니다. <b>흐린 글도 이 기준을 지켜야</b> 합니다"),
    ("<code>aria-disabled</code>", "스크린 리더 사용자에게도 비활성 상태를 <b>소리로</b> 알립니다"),
    ("확인하는 방법", "개발자 도구의 <b>대비비 검사</b>로 흐린 글을 찍어 봅니다"),
  ]),
  backend=rows([
    ("서버와 관계없는 화면 쪽 표현", "흐리게 보이는 방식은 화면 쪽에서 정합니다. 다만 <b>무엇이 비활성인지</b>는 서버가 정합니다."),
    ("서버가 비활성 이유를 함께 보내기", "서버가 권한이 없어서인지, 조건이 맞지 않아서인지를 함께 보내 주면 화면은 버튼을 <b>흐리게만 두지 않고 이유를 설명</b>할 수 있습니다."),
  ]),
  plat_lede="이름과 적용 범위는 세 플랫폼이 같지만, <b>쌓임 문맥 문제</b>는 웹에만 있습니다.",
  plats=plats([
    ("웹", "opacity",
     card(".5", "opacity", "", False),
     "1 미만이면 <b>쌓임 문맥</b>이 생기는데, 이 부작용은 웹에만 있습니다."),
    ("iOS", "alpha · opacity",
     '''              <div class="phone" role="img" aria-label="iOS 흐린 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:9px;border-radius:3px;background:var(--accent-soft);opacity:.4"></div></div></div>''',
     "<code>.opacity()</code>가 같은 일을 합니다. 겹침 순서는 <b>그리는 차례</b>로 정해지기 때문에 z-index가 갇히는 일이 없습니다."),
    ("안드로이드", "alpha",
     '''              <div class="phone" role="img" aria-label="안드로이드 흐린 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:9px;border-radius:3px;background:var(--accent-soft);opacity:.4"></div></div></div>''',
     "<code>.alpha()</code>를 씁니다. Material은 비활성 상태를 <b>38% 불투명도</b>로 정해 두었습니다."),
  ]),
  plat_note="안드로이드가 비활성을 <b>38%</b>로 정해 두었기 때문에 이 숫자가 웹으로 그대로 넘어오는 일이 많습니다. 그런데 Material의 색은 그 값에서도 대비비가 맞도록 고른 것이라서, <b>아무 색에나 38%를 걸면 대비비가 맞지 않습니다</b>. 그러니 숫자를 그대로 가져오지 말고 <b>흐리게 만든 결과의 대비비를 재세요</b>. 흐린 색 토큰을 한 번 정해 두면 그 뒤로는 다시 잴 필요가 없습니다.",
  siblings=siblings("opacity"),
  related='''        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>''',
)
