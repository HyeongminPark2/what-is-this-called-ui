# -*- coding: utf-8 -*-
from ax2 import ax
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
                  <div class="pin-out" data-pin="3" style="color:var(--danger)">1 미만이면 <b>쌓임 문맥</b>이 생긴다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">자식의 z-index 가 그 안에 갇힌다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">대비비가 같이 떨어진다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--accent)">흐린 색 토큰<span style="color:var(--fg-faint)"> ← 미리 맞춰 둔 값</span></div>
                </div>
              </div>'''

D = dict(
  slug="opacity", ko="불투명도", en="Opacity",
  desc="흐리게 하는 방법 셋의 차이. opacity가 대비비와 z-index에 남기는 자국.",
  lede="<code>opacity</code>는 <b>상자 안의 모든 것</b>을 한꺼번에 흐리게 합니다. 그래서 흔한 도구이면서 가장 자주 잘못 쓰입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모가 <b>대비비를 재서 적습니다</b> — 흰 바탕 위 글자를 <code>opacity: .5</code> 로
          흐리면 4.5:1 아래로 떨어집니다. 비활성 상태를 이렇게 만들면 <b>읽을 수 없는 글</b>이 됩니다.<br>
          더 조용한 사고가 하나 더 있습니다 — <code>opacity</code>가 1보다 작아지면 그 상자가
          <b>쌓임 문맥</b>이 되어, 안의 <code>z-index: 5</code> 배지가 바깥의
          <code>z-index: 2</code> 덮개 위로 못 올라갑니다. 겹치는 자리를 실제로 찍어 누가 위인지 잽니다.</p>
        </div>''',
  names=rows([
    ("한국어", "불투명도, 투명도, 알파"),
    ("영어", "opacity, alpha, transparency"),
    ("같이 쓰는 말",
     "상자 전체에 거는 것이 <b>opacity</b>, 색 하나에만 거는 것이 <b>알파</b>(<code>rgba</code>·<code>#rrggbbaa</code>)입니다. "
     "둘은 보이기가 비슷해도 <b>미치는 범위와 뒤탈</b>이 다릅니다. "
     "모달 뒤에 까는 반투명 판은 <b>가림막</b>(scrim · backdrop)이라 따로 부릅니다."),
    ("자주 잘못 부름",
     "<b>visibility</b> — <code>visibility: hidden</code>은 <b>자리를 차지한 채</b> 안 보입니다.<br>"
     "<b>display: none</b> — 아예 없어집니다. 읽어 주지도 않습니다.<br>"
     "<b>disabled</b> — <a href=\"field.html\">비활성</a>은 <b>상태</b>이고, 흐리게 하는 것은 그 상태를 보이는 한 가지 방법일 뿐입니다."),
  ]),
  axes=ax("불투명도"),
  oneline="<b>비활성은 opacity 로 만들지 마세요.</b> 흐린 색 토큰을 따로 두면 대비비를 지킬 수 있습니다.",
  s4_title="흐리게 하는 법", s4_hint="범위와 뒤탈이 다르다",
  states=states([
    (card("", "그대로", "대비비 통과", True), "기본", "기준값"),
    (card(".5", "opacity: .5", "전부 흐려진다", False), "상자 전체", "<b>글·버튼·배지까지</b> 같이"),
    (card("", "rgba(…, .5)", "글자만 흐려진다", None, "rgba(32,35,42,.5)"),
     "색에만", "쌓임 문맥은 <b>안 생긴다</b>"),
    (card("", "--fg-muted", "미리 맞춰 둔 값", True, "var(--fg-muted)"),
     "흐린 색 토큰", "<b>대비비를 지킨다</b>"),
    ('''              <div style="display:grid;gap:6px;justify-items:center;padding:4px 0">
                <span style="display:block;position:relative;width:116px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px 8px">
                  <span style="display:block;font-size:9.5px">정산 2건이 밀렸습니다</span>
                  <span style="position:absolute;inset:0;border-radius:6px;background:color-mix(in srgb, var(--fg) 45%, transparent)"></span>
                </span>
                <span style="font-family:var(--mono);font-size:10px;color:var(--fg-muted)">가림막</span>
                <span style="font-size:10px;color:var(--fg-faint);text-align:center">위에 반투명 판을 덮는다</span>
              </div>''',
     "가림막", "흐린 게 아니라 <b>덮은</b> 것"),
    (card(".4", "opacity: .4", "z-index 가 갇힌다", False), "쌓임 문맥", "<b>안쪽 층이 바깥을 못 넘는다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>opacity</code>", "상자 전부", "자식이 <b>되돌릴 수 없다</b>"),
    ("알파", "그 색만", "범위가 <b>좁아서</b> 안전하다"),
    ("쌓임 문맥", "1 미만이면", "<b>생긴다</b> — 되돌릴 방법이 없다"),
    ("갇힌 z-index", "바깥을 못 넘음", "모달·툴팁이 <b>가려지는</b> 원인"),
    ("대비비", "같이 떨어짐", "비활성 글이 <b>안 읽힌다</b>"),
    ("흐린 색 토큰", "미리 맞춘 값", "<b>권하는 길</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'툴팁이 왜 안 보이지'</b>의 범인이 자주 여기 있습니다.
          조상 어딘가에 <code>opacity: .99</code> 같은 값이 하나 걸려 있으면
          그 안의 <code>z-index</code>는 아무리 키워도 바깥으로 못 나옵니다.
          <code>transform</code>·<code>filter</code>·<code>will-change</code>도 같은 일을 합니다.<br>
          비활성도 마찬가지입니다. <code>opacity: .5</code>는 <b>글자만</b>이 아니라
          테두리·아이콘까지 같이 흐려 대비비를 두 번 깎습니다.
          <b>흐린 색을 토큰으로 따로 두는 것</b>이 답입니다.</p>''',
  do=ul([
    "비활성은 <b>흐린 색 토큰</b>으로 만들기",
    "흐리게 할 것이 하나면 <b>알파</b>로 색에만 걸기",
    "가림막은 <code>opacity</code>가 아니라 <b>반투명 색</b>으로 덮기",
  ]),
  dont=ul([
    "<code>opacity: .5</code>로 비활성 만들기 — <b>대비비가 미달</b>이 된다",
    "조상에 <code>opacity: .99</code> 걸기 — <b>그 안의 z-index 가 갇힌다</b>",
    "<code>opacity: 0</code>으로 숨기기 — <b>여전히 눌리고 읽힌다</b>",
    "흐린 글을 <b>본문</b>에 쓰기 — 읽으라고 쓴 글은 흐리면 안 된다",
  ]),
  instead='감추는 방법은 <a href="semantics.html">시맨틱 태그</a>, 겹침은 <a href="zindex.html">z-index</a>, 읽히는 밝기는 <a href="contrast.html">대비비</a>, 색 자체는 <a href="color.html">색 토큰</a>.',
  cases=cases([
    (card("", "비활성", "흐린 색 토큰 + aria-disabled", True, "var(--fg-muted)"),
     "비활성", "색으로, <b>opacity 말고</b>"),
    (one(txt('<span style="display:block;position:relative;height:30px;border-radius:5px;background:var(--surface);border:1px solid var(--line)">'
             '<span style="position:absolute;inset:0;border-radius:5px;background:color-mix(in srgb, var(--fg) 45%, transparent)"></span></span>'),
         "가림막", True, "모달 뒤를 덮는다", "116px"),
     "가림막", "<b>덮개</b>로 생각한다"),
    (card("", "지도 위 글", "읽을 글은 안 흐린다", True), "겹친 글", "바탕을 <b>깔고</b> 쓴다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 값의 계약서",
  code_lede="흐린 색을 토큰으로 두면 대비비를 한 번만 재고 끝납니다.",
  code='''<span class="c">/* 미리 대비비를 맞춰 둔 흐린 색 */</span>
:root {
  --fg-muted: <span class="a">#5c6370</span>;   <span class="c">/* 흰 바탕에서 4.9:1 */</span>
  --scrim: <span class="a">rgba</span>(20, 22, 26, <span class="a">.45</span>);
}

<span class="c">/* 비활성 — 색으로 만든다 */</span>
.btn[disabled] { <span class="a">color</span>: <span class="a">var</span>(--fg-muted); <span class="a">background</span>: <span class="a">var</span>(--bg); <span class="a">cursor</span>: not-allowed; }

<span class="c">/* 가림막 — 덮는 것이지 흐리는 것이 아니다 */</span>
.scrim { <span class="a">position</span>: fixed; <span class="a">inset</span>: <span class="a">0</span>; <span class="a">background</span>: <span class="a">var</span>(--scrim); }

<span class="c">/* ✕ 대비비가 떨어지고 z-index 가 갇힌다 */</span>
.btn[disabled] { <span class="a">opacity</span>: <span class="a">.5</span>; }''',
  keys=kbd([
    ("<code>opacity: 0</code>", "보이지만 않을 뿐 <b>눌리고 읽힌다</b> — 숨기려면 <code>hidden</code>"),
    ("쌓임 문맥", "<code>opacity</code>·<code>transform</code>·<code>filter</code>가 만든다"),
    ("<code>color-mix()</code>", "요즘 브라우저에서 <b>알파를 깔끔하게</b> 섞는 법"),
    ("대비비 4.5:1", "본문 글의 기준. <b>흐린 글도 지켜야</b> 한다"),
    ("<code>aria-disabled</code>", "비활성을 <b>소리로도</b> 알린다"),
    ("확인하는 법", "개발자 도구의 <b>대비비 검사</b>로 흐린 글을 찍어 본다"),
  ]),
  backend=rows([
    ("서버와는 상관없다", "흐리기는 화면의 일입니다. 다만 <b>무엇이 비활성인지</b>는 서버가 정합니다."),
    ("비활성의 이유", "권한이 없어서인지, 조건이 안 맞아서인지를 같이 주면 <b>흐리게만 두지 않고 설명</b>할 수 있습니다."),
  ]),
  plat_lede="이름과 범위는 같고, <b>쌓임 문맥 사고</b>는 웹에만 있습니다.",
  plats=plats([
    ("웹", "opacity",
     card(".5", "opacity", "", False),
     "1 미만이면 <b>쌓임 문맥</b>이 생깁니다. 이 부작용이 웹의 특징입니다."),
    ("iOS", "alpha · opacity",
     '''              <div class="phone" role="img" aria-label="iOS 흐린 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:9px;border-radius:3px;background:var(--accent-soft);opacity:.4"></div></div></div>''',
     "<code>.opacity()</code>가 같은 일을 합니다. 겹침 순서는 <b>그리는 차례</b>라 갇히는 일이 없습니다."),
    ("안드로이드", "alpha",
     '''              <div class="phone" role="img" aria-label="안드로이드 흐린 글 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:30px;height:9px;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:6px;right:6px;top:44px;height:9px;border-radius:3px;background:var(--accent-soft);opacity:.4"></div></div></div>''',
     "<code>.alpha()</code>입니다. Material 은 비활성을 <b>38% 불투명도</b>로 못박아 두었습니다."),
  ]),
  plat_note="안드로이드가 비활성을 <b>38%</b>로 정해 둔 탓에 그 숫자가 웹으로 넘어오는 일이 많습니다. 그런데 Material 의 색은 그 값에서도 대비비가 맞게 고른 것이고, <b>아무 색에나 38%를 걸면 맞지 않습니다</b>. 숫자를 베끼지 말고 <b>결과를 재세요</b> — 흐린 색 토큰을 한 번 정해 두면 그 뒤로는 잴 일이 없습니다.",
  siblings=siblings("opacity"),
  related='''        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><a href="color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>''',
)
