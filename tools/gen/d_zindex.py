# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def layer(z, name, use, bg="var(--surface)", fg="var(--fg)"):
    return ('              <div style="display:grid;gap:7px;justify-items:center;width:100%%">'
            '<span style="display:block;width:100%%;max-width:120px;border-radius:8px;background:%s;color:%s;'
            'border:1px solid var(--line);padding:9px 10px;font-size:11px;text-align:center">%s</span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--accent);font-weight:700">z: %s</span>'
            '<span style="font-size:10.5px;color:var(--fg-faint);text-align:center">%s</span></div>'
            ) % (bg, fg, name, z, use)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:16px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:13px">
                  <div class="pin-out" data-pin="1" style="font-size:11.5px;color:var(--fg-muted)">부모에 <code>transform</code>이 걸려 있으면 여기서 새 맥락이 시작됩니다</div>
                  <div class="pin-out" data-pin="2" style="border:1px dashed var(--accent);border-radius:9px;padding:12px 10px 12px 0;background:var(--surface)">
                    <div style="padding-left:26px;display:grid;gap:11px">
                      <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:11px;color:var(--fg-muted)">transform: translateZ(0)</div>
                      <div class="pin-out" data-pin="4" style="background:var(--accent-soft);color:var(--accent);border-radius:7px;padding:7px 10px;font-size:11px;font-weight:700">자식 · z-index: 9999</div>
                    </div>
                  </div>
                  <div class="pin-out" data-pin="5" style="background:var(--ink-900);color:#fff;border-radius:7px;padding:7px 10px;font-size:11px">형제 · z-index: 1, 이쪽이 위에 그려짐</div>
                </div>
              </div>'''

D = dict(
  slug="zindex", ko="z-index", en="z-index · stacking order",
  desc="z-index 값을 미리 정해 둔 층 목록에서만 고르는 방법과, 쌓임 맥락 때문에 z-index가 적용되지 않는 이유를 보여 주는 항목입니다.",
  lede="z-index는 겹친 요소들의 <b>앞뒤 순서</b>를 정하는 값입니다. 아무 숫자나 적는 칸이 아니라, 미리 정해 둔 <b>층 목록</b>에서 골라 쓰는 값입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 값을 어떻게 쓸지 <b>정해 둔 규칙</b>입니다. 그래서 생김새 대신 아래 네 가지를 물어보면 토큰끼리 무엇이 다른지 가려집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>100, 300, 500처럼 층 사이를 <b>띄워</b> 두면 나중에 층을 하나 끼워 넣을 자리가 남습니다.<br>
          <b>아무 값이나 쓰기</b>를 켜면 토스트가 9999가 됩니다. 당장은 맨 위로 올라오지만,
          다음 사람은 그보다 큰 99999를 쓰게 되고, 이런 일이 쌓이면 <b>왜 이 순서인지 아무도 설명할 수 없게</b> 됩니다.
          이 데모에서는 그 결과로 모달이 가림막에 덮여 글자를 읽을 수 없게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "z-인덱스, 쌓임 순서, 층 순서"),
    ("영어", "z-index, stacking order, stacking context, layer"),
    ("같이 쓰는 말",
     "z-index 값끼리 앞뒤를 비교하는 범위를 <b>쌓임 맥락</b>(stacking context)이라고 합니다. "
     "같은 맥락 안에서 z-index 번호 없이 정해지는 순서는 <b>그리는 순서</b>(painting order)이고, "
     "미리 정해 둔 층 목록은 보통 <b>레이어 스케일</b> 또는 <b>z 스케일</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>고도</b> — 고도는 그림자로 나타내는 <b>보이는 높이</b>이고, z-index는 <b>그리는 순서</b>입니다. "
     "그래서 그림자가 커도 그리는 순서가 뒤로 밀리면 다른 요소 아래에 깔립니다.<br>"
     "<b>레이어</b> — 디자인 도구의 레이어 패널과는 다릅니다. 브라우저에서는 순서를 <b>같은 맥락 안에서만</b> 비교합니다.<br>"
     "<b>position</b> — <code>position</code>이 <code>static</code>이면 z-index는 <b>아예 적용되지 않습니다</b>."),
  ]),
  axes=ax("z-index"),
  oneline="z-index는 <b>큰 숫자를 겨루는 값이 아니라 층의 이름</b>입니다. 코드에 9999가 보인다면 그 화면에는 정해 둔 층 목록이 없거나 지켜지지 않고 있다는 뜻입니다.",
  s4_title="층 목록과 층마다 놓이는 부품", s4_hint="숫자 대신 이름으로 부르는 층",
  states=states([
    (layer("auto", "본문", "그리는 순서대로"), "본문 층", "z-index 번호를 주지 않습니다. <b>대부분의 요소가 이 층에</b> 있어야 합니다"),
    (layer("100", "상단 바", "스크롤해도 붙어 있는 것"), "붙박이 머리말 층", "머리말과 꼬리말이 놓이는 층으로, 본문보다는 위이고 나머지 층보다는 아래입니다"),
    (layer("300", "드롭다운", "눌러서 연 것"), "잠깐 떠 있는 부품 층", "팝오버나 툴팁처럼 <b>곧 닫히는</b> 부품이 놓입니다"),
    (layer("500", "가림막", "뒤를 덮는 막", "rgba(14,16,20,.55)", "#fff"), "가림막 층", "모달 바로 아래 한 칸에 둡니다"),
    (layer("600", "모달", "화면을 가로막은 것"), "모달 층", "가림막보다 <b>딱 한 칸</b> 위에 둡니다"),
    (layer("800", "토스트", "모달 위에도 떠야 하는 것", "var(--ink-900)", "#fff"), "토스트 층", "가장 위층입니다. 이보다 높은 층은 <b>만들지 않습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("맥락 밖", "outer context", "z-index 번호는 같은 쌓임 맥락 안에 있는 요소끼리만 비교됩니다"),
    ("쌓임 맥락", "stacking context", "이 맥락 안의 자식은 z-index가 얼마나 크든 <b>맥락 바깥의 요소와는 순서를 비교하지 않습니다</b>"),
    ("맥락을 만드는 속성", "transform · opacity · filter", "<code>transform</code>, 1 미만의 <code>opacity</code>, <code>filter</code>, <code>will-change</code>, <code>position: fixed</code> 등을 주면 새 쌓임 맥락이 생깁니다"),
    ("갇힌 자식", "z-index: 9999", "z-index가 9999라도 그 값은 <b>부모가 만든 맥락 안에서만</b> 의미가 있습니다"),
    ("바깥 형제", "z-index: 1", "맥락 바깥에 있는 z-index 1인 요소가 안쪽의 9999보다 위에 그려집니다. <b>'z-index가 안 먹어요'라는 문제는 대부분 이 때문에 생깁니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          드롭다운이 카드에 가려 보이지 않는 문제는 거의 모두 부모 어딘가에
          <code>transform</code>이나 <code>opacity: .99</code>가 걸려 있어서 생깁니다. 이때는 z-index 숫자를 올려도
          고쳐지지 않습니다. 해결 방법은 두 가지로, <b>맥락을 만드는 속성을 없애거나</b>
          그 부품을 <code>&lt;body&gt;</code> 바로 밑으로 옮기는 것입니다(포털 · <code>popover</code> 속성).</p>''',
  do=ul([
    "모달과 토스트가 함께 있는 화면처럼 겹쳐 뜨는 부품이 <b>둘 이상</b> 있을 때",
    "붙박이 머리말이 다른 것에 가릴 때",
    "층 목록을 <b>한 파일에 모아</b> 둘 때",
  ]),
  dont=ul([
    "본문 요소에 번호를 줄 때. 대부분은 <b>번호 없이</b> 그리는 순서만으로 충분합니다",
    "급하다고 숫자만 올릴 때. 다음 사람이 그보다 더 큰 숫자를 쓰게 되어 <b>같은 문제가 되풀이됩니다</b>",
    "999나 9999 같은 값을 쓸 때. 정해 둔 층 목록이 쓸모없어집니다",
    "쌓임 맥락이 달라서 생긴 문제를 숫자로 맞추려 할 때. 원인이 숫자가 아니라 맥락에 있어서 고쳐지지 않습니다",
  ]),
  instead_title="z-index와 함께 보면 좋은 항목",
  instead='요소가 떠 <b>보이게</b> 하는 방법은 <a href="elevation.html">고도</a> 항목에서 다루고, 어떤 부품이 뒤 화면을 막는지는 <a href="../items/modal.html">모달</a> 항목과 <a href="../items/toast.html">토스트</a> 항목에 정리돼 있습니다.',
  cases=cases([
    ('''              <div style="display:grid;grid-template-columns:auto 1fr;gap:6px 10px;font-size:11.5px;align-items:baseline">
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">100</span><span>붙박이 머리말</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">300</span><span>드롭다운 · 툴팁</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">500</span><span>가림막</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">600</span><span>모달</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">800</span><span>토스트</span>
              </div>''',
     "층 목록을 한 파일에 모으기", "층 목록을 한 파일에 모아 두고, <b>목록에 없는 숫자는 쓰지 않습니다</b>"),
    ('''              <div style="position:relative;width:100%;max-width:200px;height:92px">
                <span style="position:absolute;left:0;right:0;top:0;height:22px;border-radius:7px 7px 0 0;background:var(--surface);border:1px solid var(--line);font-size:10px;padding:4px 8px">상단 바</span>
                <span style="position:absolute;left:12px;top:30px;width:116px;border-radius:7px;background:var(--surface);border:1px solid var(--line);padding:7px 9px;font-size:10.5px;box-shadow:0 4px 12px rgba(20,22,26,.1)">계정 메뉴</span>
              </div>''',
     "메뉴를 머리말보다 위에 두기", "메뉴(300)가 머리말(100)보다 위에 놓입니다. <b>순서가 반대면</b> 메뉴가 머리말에 가려 잘려 보입니다"),
    ('''              <div style="width:100%;max-width:200px;display:grid;gap:6px">
                <span style="display:block;border-radius:7px;background:var(--surface);border:1px dashed var(--danger);padding:8px;font-size:10.5px">부모 · transform 있음</span>
                <span style="display:block;border-radius:7px;background:var(--danger-soft, #fdeceb);color:var(--danger);padding:8px;font-size:10.5px;font-weight:700">자식 z: 9999라도 아래에 깔림</span>
              </div>''',
     "z-index가 적용되지 않는 경우", "숫자를 잘못 준 것이 아니라 <b>쌓임 맥락</b> 때문에 생긴 문제입니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="층 목록을 코드로 옮기는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
  code_lede="층을 <b>이름으로</b> 정해 두고 코드에서는 그 이름만 씁니다. 숫자를 직접 적는 곳이 한 군데라도 생기면 층 목록과 실제 값이 어긋나기 시작합니다.",
  code='''<span class="t">:root</span> {
  <span class="a">--z-sticky</span>: <span class="s">100</span>;
  <span class="a">--z-dropdown</span>: <span class="s">300</span>;
  <span class="a">--z-scrim</span>: <span class="s">500</span>;
  <span class="a">--z-modal</span>: <span class="s">600</span>;
  <span class="a">--z-toast</span>: <span class="s">800</span>;
}

<span class="c">/* position 이 static 이면 z-index 는 아무 일도 하지 않는다 */</span>
<span class="t">.site-header</span> { <span class="a">position</span>: sticky; <span class="a">z-index</span>: <span class="t">var</span>(<span class="a">--z-sticky</span>); }
<span class="t">.toast-area</span>  { <span class="a">position</span>: fixed;  <span class="a">z-index</span>: <span class="t">var</span>(<span class="a">--z-toast</span>); }

<span class="c">// 맥락에 갇히지 않으려면 body 밑으로 옮긴다(포털)</span>
<span class="t">document</span>.body.appendChild(toastEl);

<span class="c">/* 또는 브라우저에 맡겨 최상위 레이어로 올린다 */</span>
&lt;<span class="t">dialog</span>&gt;, [<span class="a">popover</span>]''',
  keys=kbd([
    ("층 목록부터 정하기", "다섯~여섯 층이면 충분합니다. 층 사이를 100씩 띄워 나중에 끼워 넣을 자리를 남깁니다"),
    ("코드에 숫자를 직접 쓰지 않기", "<code>var(--z-modal)</code>처럼 이름만 씁니다. 코드에 숫자가 보이면 리뷰에서 막습니다"),
    ("<code>position</code>을 함께 지정하기", "<code>position</code>이 <code>static</code>이면 z-index가 무시됩니다. 'z-index가 안 먹어요'라는 문제의 두 번째로 흔한 원인입니다"),
    ("쌓임 맥락부터 확인하기", "z-index가 적용되지 않으면 숫자를 올리지 말고 부모에 걸린 <code>transform · opacity · filter</code>부터 찾습니다"),
    ("가림막과 모달은 한 칸 차이로 두기", "500과 600처럼 바로 이웃한 층에 둡니다. 둘 사이에 다른 층이 끼면 그 층의 요소가 가림막 위로 드러납니다"),
    ("<code>&lt;dialog&gt;</code>와 <code>popover</code>를 먼저 쓰기", "브라우저가 <b>최상위 레이어</b>에 그려 주기 때문에 쌓임 맥락 문제가 아예 생기지 않습니다"),
  ]),
  backend=rows([
    ("우선순위 상수와 같은 구조", "미들웨어 순서나 이벤트 핸들러 우선순위와 같은 구조입니다. 값 사이를 비워 두는 이유도 <b>나중에 끼워 넣기 위해서</b>라는 점에서 같습니다."),
    ("9999 같은 값이 생기는 이유", "급할 때 가장 손쉽게 쓸 수 있는 해결책이기 때문입니다. 코드 리뷰에서 <b>숫자 리터럴을 막는</b> 규칙 하나만 두어도 이 문제는 대부분 사라집니다."),
    ("외부 위젯이 쓰는 큰 값", "채팅 상담이나 결제창 같은 외부 스크립트는 <b>미리 알 수 없는 큰 값</b>을 씁니다. 그래서 우리 층 목록의 맨 위층을 그보다 높게 잡거나, 해당 구역을 따로 감싸 둡니다."),
    ("쌓임 맥락을 확인하는 방법", "브라우저 개발자 도구의 <b>Layers</b> 패널에서 쌓임 맥락을 볼 수 있습니다. 숫자를 바꿔 보기 전에 이 패널부터 열어 보면 원인을 더 빨리 찾을 수 있습니다."),
  ]),
  plat_lede="쌓임 맥락 문제는 웹에만 있습니다. 앱은 화면을 쌓는 방식 자체가 달라서 이런 문제가 거의 생기지 않습니다.",
  plats=plats([
    ("웹", "CSS z-index",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">z-index: 600<br>position: fixed</div>''',
     "<b>쌓임 맥락</b> 때문에 z-index가 뜻대로 적용되지 않는 일이 생깁니다. <code>&lt;dialog&gt;</code>와 <code>popover</code> 속성을 쓰면 맥락과 상관없이 <b>최상위 레이어</b>에 그려집니다."),
    ("iOS", "뷰 계층",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">zPosition<br>.zIndex(1)<br>.sheet / .alert</div>''',
     "새 화면을 기존 화면 위에 <b>쌓아 올리는 구조</b>(present)라서 순서가 엉킬 일이 적습니다. 같은 층 안의 순서만 <code>zIndex</code>로 조정합니다."),
    ("안드로이드", "Compose · elevation",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Modifier.zIndex(1f)<br>Dialog { }</div>''',
     "기본적으로 그리는 순서를 따르고, 다이얼로그는 <b>별도 윈도</b>로 떠서 아예 다른 층에 그려집니다."),
  ]),
  plat_note="\"z-index가 안 먹어요\"는 <b>웹 개발자끼리만 통하는 말</b>입니다. 앱 개발자는 같은 증상을 겪지 않기 때문에, 문제를 설명할 때는 \"부모 때문에 이 요소가 바깥 요소보다 위로 못 올라간다\"처럼 <b>맥락</b>을 풀어서 말해야 합니다.",
  siblings=siblings("zindex"),
  related='''        <li><a href="../items/toast.html"><b>토스트 · 스낵바</b><em>6부</em></a></li>
        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><a href="sticky.html"><b>스티키</b><em>1부</em></a></li>''',
)
