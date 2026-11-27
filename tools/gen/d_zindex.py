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
                  <div class="pin-out" data-pin="5" style="background:var(--ink-900);color:#fff;border-radius:7px;padding:7px 10px;font-size:11px">형제 · z-index: 1 — 이쪽이 위에 그려집니다</div>
                </div>
              </div>'''

D = dict(
  slug="zindex", ko="z-index", en="z-index · stacking order",
  desc="z-index 를 사다리로 정해 두는 방법과, 쌓임 맥락 때문에 z-index 가 안 먹는 이유를 보여주는 항목.",
  lede="겹친 것들의 <b>앞뒤 순서</b>. 아무 숫자나 쓰는 칸이 아니라, 미리 정해 둔 <b>층의 사다리</b>입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>100·300·500처럼 <b>사이를 띄워</b> 두면 나중에 한 층을 끼워 넣을 자리가 남습니다.<br>
          <b>아무 값이나 쓰기</b>를 켜면 토스트가 9999가 됩니다. 당장은 맨 위로 오지만,
          다음 사람은 99999를 쓰게 되고 결국 <b>아무도 순서를 설명할 수 없게</b> 됩니다.
          여기서는 모달이 가림막에 덮여 글자가 안 읽히는 것으로 보여 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "z-인덱스, 쌓임 순서, 층 순서"),
    ("영어", "z-index, stacking order, stacking context, layer"),
    ("같이 쓰는 말",
     "앞뒤 비교가 일어나는 울타리를 <b>쌓임 맥락</b>(stacking context)이라 합니다. "
     "같은 맥락 안에서 번호 없이 늘어선 순서는 <b>그리는 순서</b>(painting order)이고, "
     "미리 정해 둔 층 목록은 보통 <b>레이어 스케일</b> 또는 <b>z 스케일</b>이라 부릅니다."),
    ("자주 잘못 부름",
     "<b>고도</b> — 고도는 <b>보이는 높이</b>(그림자), z-index 는 <b>그리는 순서</b>입니다. "
     "그림자가 커도 순서가 밀리면 아래에 깔립니다.<br>"
     "<b>레이어</b> — 디자인 도구의 레이어 패널과는 다릅니다. 브라우저의 순서는 <b>맥락 안에서만</b> 비교됩니다.<br>"
     "<b>position</b> — <code>position</code>이 <code>static</code>이면 z-index 는 <b>아예 안 먹습니다</b>."),
  ]),
  axes=ax("z-index"),
  oneline="z-index 는 <b>숫자 싸움이 아니라 층 이름</b>입니다. 9999가 보이면 그 화면에는 이미 사다리가 없는 것입니다.",
  s4_title="층", s4_hint="숫자가 아니라 이름으로 부른다",
  states=states([
    (layer("auto", "본문", "그리는 순서대로"), "본문", "번호를 안 준다. <b>대부분이 여기 있어야</b> 한다"),
    (layer("100", "상단 바", "스크롤해도 붙어 있는 것"), "붙박이", "머리말·꼬리말. 본문 위, 나머지 아래"),
    (layer("300", "드롭다운", "눌러서 연 것"), "떠 있는 것", "팝오버·툴팁. <b>곧 닫힌다</b>"),
    (layer("500", "가림막", "뒤를 덮는 막", "rgba(14,16,20,.55)", "#fff"), "가림막", "모달 바로 아래 한 칸"),
    (layer("600", "모달", "화면을 가로막은 것"), "모달", "가림막보다 <b>딱 한 칸</b> 위"),
    (layer("800", "토스트", "모달 위에도 떠야 하는 것", "var(--ink-900)", "#fff"), "토스트", "가장 위. 여기가 <b>천장</b>이다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("맥락 밖", "outer context", "여기서는 번호가 같은 울타리 안의 것들끼리만 비교된다"),
    ("쌓임 맥락", "stacking context", "이 울타리 안의 자식은 <b>아무리 커도 울타리를 못 넘는다</b>"),
    ("맥락을 만드는 속성", "transform · opacity · filter", "<code>transform</code>, <code>opacity</code>가 1 미만, <code>filter</code>, <code>will-change</code>, <code>position: fixed</code> 등이 새 울타리를 만든다"),
    ("갇힌 자식", "z-index: 9999", "9999 라도 <b>부모 울타리 안에서만</b> 9999 다"),
    ("바깥 형제", "z-index: 1", "울타리 바깥의 1 이 안쪽의 9999 를 이긴다. <b>이것이 'z-index 가 안 먹어요'의 정답</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          드롭다운이 카드에 가려 안 보이는 사고의 거의 전부가 이것입니다. 부모 어딘가에
          <code>transform</code>이나 <code>opacity: .99</code>가 걸려 있는 것이지요. 숫자를 올려서는
          절대 안 고쳐집니다. 해결은 두 가지입니다 — <b>맥락을 만드는 속성을 없애거나</b>,
          그 부품을 <code>&lt;body&gt;</code> 바로 밑으로 옮기는 것입니다(포털 · <code>popover</code> 속성).</p>''',
  do=ul([
    "겹쳐 뜨는 부품이 <b>둘 이상</b> 있을 때 — 모달과 토스트가 함께 있는 화면",
    "붙박이 머리말이 다른 것에 가릴 때",
    "층 목록을 <b>한 파일에 모아</b> 둘 때",
  ]),
  dont=ul([
    "본문 요소에 번호를 주는 것 — 대부분은 <b>번호 없이</b> 그리는 순서로 충분합니다",
    "급해서 숫자를 올리는 것 — 다음 사람이 더 올립니다. <b>한 번도 해결된 적이 없습니다</b>",
    "999·9999 같은 값 — 사다리를 못 쓰게 만듭니다",
    "맥락이 다른데 숫자로 맞추려는 것 — 원인이 다른 데 있습니다",
  ]),
  instead='떠 있어 <b>보이게</b> 하는 일은 <a href="elevation.html">고도</a>가 맡고, 어떤 것이 뒤를 막는지는 <a href="../items/modal.html">모달</a>·<a href="../items/toast.html">토스트</a>에 정리돼 있습니다.',
  cases=cases([
    ('''              <div style="display:grid;grid-template-columns:auto 1fr;gap:6px 10px;font-size:11.5px;align-items:baseline">
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">100</span><span>붙박이 머리말</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">300</span><span>드롭다운 · 툴팁</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">500</span><span>가림막</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">600</span><span>모달</span>
                <span style="color:var(--accent);font-family:var(--mono);text-align:right">800</span><span>토스트</span>
              </div>''',
     "층 목록", "한 파일에 모아 두고 <b>여기 없는 숫자는 금지</b>"),
    ('''              <div style="position:relative;width:100%;max-width:200px;height:92px">
                <span style="position:absolute;left:0;right:0;top:0;height:22px;border-radius:7px 7px 0 0;background:var(--surface);border:1px solid var(--line);font-size:10px;padding:4px 8px">상단 바</span>
                <span style="position:absolute;left:12px;top:30px;width:116px;border-radius:7px;background:var(--surface);border:1px solid var(--line);padding:7px 9px;font-size:10.5px;box-shadow:0 4px 12px rgba(20,22,26,.1)">계정 메뉴</span>
              </div>''',
     "메뉴와 머리말", "메뉴(300)가 머리말(100) 위. <b>순서가 반대면</b> 메뉴가 잘려 보인다"),
    ('''              <div style="width:100%;max-width:200px;display:grid;gap:6px">
                <span style="display:block;border-radius:7px;background:var(--surface);border:1px dashed var(--danger);padding:8px;font-size:10.5px">부모 · transform 있음</span>
                <span style="display:block;border-radius:7px;background:var(--danger-soft, #fdeceb);color:var(--danger);padding:8px;font-size:10.5px;font-weight:700">자식 z: 9999 — 그래도 아래</span>
              </div>''',
     "안 먹는 z-index", "숫자 문제가 아니라 <b>맥락 문제</b>다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 사다리의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="층을 <b>이름으로</b> 두고 그 이름만 씁니다. 숫자를 직접 적는 곳이 한 군데라도 생기면 사다리가 무너집니다.",
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

<span class="c">/* 또는 브라우저에 맡긴다 — 최상위 레이어로 올라간다 */</span>
&lt;<span class="t">dialog</span>&gt;, [<span class="a">popover</span>]''',
  keys=kbd([
    ("층을 먼저 정한다", "다섯~여섯 층이면 충분하다. 사이를 100씩 띄워 끼울 자리를 남긴다"),
    ("숫자를 직접 안 쓴다", "<code>var(--z-modal)</code>만 쓴다. 숫자가 보이면 리뷰에서 막는다"),
    ("<code>position</code>을 함께", "<code>static</code>에서는 z-index 가 무시된다. 가장 흔한 '안 먹어요'의 두 번째 원인"),
    ("맥락을 의심한다", "안 먹으면 숫자를 올리지 말고 부모의 <code>transform · opacity · filter</code>를 찾는다"),
    ("가림막과 모달은 한 칸 차이", "500 과 600 처럼 붙여 둔다. 사이에 다른 것이 끼면 반드시 사고가 난다"),
    ("<code>&lt;dialog&gt;</code>·<code>popover</code> 를 먼저", "브라우저가 <b>최상위 레이어</b>에 그려 줘서 맥락 문제 자체가 없어진다"),
  ]),
  backend=rows([
    ("z 스케일 = 우선순위 상수", "미들웨어 순서나 이벤트 핸들러 우선순위와 같은 꼴입니다. 비어 있는 값을 남겨 두는 이유도 같습니다 — <b>나중에 끼워 넣으려고</b>."),
    ("왜 9999 가 생기나", "급할 때 가장 싼 해결이기 때문입니다. 코드 리뷰에서 <b>숫자 리터럴을 막는</b> 규칙 하나가 이 문제의 대부분을 없앱니다."),
    ("서드파티 위젯", "채팅 상담, 결제창 같은 외부 스크립트가 <b>제멋대로 큰 값</b>을 씁니다. 우리 층 사다리의 천장을 그보다 높게 잡거나, 해당 구역을 따로 감쌉니다."),
    ("디버깅", "브라우저 개발자 도구의 <b>Layers</b> 패널에서 맥락을 볼 수 있습니다. 숫자를 바꿔 보기 전에 여기를 먼저 열면 시간이 줄어듭니다."),
  ]),
  plat_lede="웹에만 있는 문제입니다. 앱 쪽은 화면을 쌓는 방식 자체가 달라 이 사고가 거의 없습니다.",
  plats=plats([
    ("웹", "CSS z-index",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">z-index: 600<br>position: fixed</div>''',
     "<b>쌓임 맥락</b>이라는 함정이 있습니다. <code>&lt;dialog&gt;</code>와 <code>popover</code> 속성은 맥락을 넘어 <b>최상위 레이어</b>에 그려집니다."),
    ("iOS", "뷰 계층",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">zPosition<br>.zIndex(1)<br>.sheet / .alert</div>''',
     "화면을 <b>쌓아 올리는 구조</b>(present)라 순서 다툼이 적습니다. 같은 층 안의 순서만 <code>zIndex</code>로 조정합니다."),
    ("안드로이드", "Compose · elevation",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Modifier.zIndex(1f)<br>Dialog { }</div>''',
     "그리는 순서가 기본이고, 다이얼로그는 <b>별도 윈도</b>로 떠서 아예 다른 층이 됩니다."),
  ]),
  plat_note="\"z-index 가 안 먹어요\"는 <b>웹에서만 통하는 말</b>입니다. 앱 개발자에게는 같은 증상이 아예 없어서, 문제를 설명하려면 \"부모 때문에 이 요소가 바깥보다 위로 못 올라간다\"처럼 <b>맥락</b>으로 풀어 말해야 합니다.",
  siblings=siblings("zindex"),
  related='''        <li><a href="../items/toast.html"><b>토스트 · 스낵바</b><em>6부</em></a></li>
        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="../items/appbar.html"><b>앱바 · 헤더</b><em>7부</em></a></li>
        <li><span class="na"><b>스티키</b><em>1부</em></span></li>''',
)
