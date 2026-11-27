# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div style="display:flex;align-items:flex-start;gap:40px">
                    <span style="flex:1">
                      <span class="pin-out" data-pin="1" style="display:block;font-size:12px;font-weight:650">멘션과 답글</span>
                      <span class="pin-out" data-pin="2" style="display:block;font-size:10.5px;color:var(--fg-muted);margin-top:5px">누가 나를 부르면 바로 알립니다</span>
                    </span>
                    <span class="pin-out" data-pin="3" style="font-size:10.5px;color:var(--fg-muted);align-self:center">켬</span>
                    <span data-pin="4" style="position:relative;width:44px;height:26px;border-radius:99px;background:var(--accent);flex:none;align-self:center">
                      <span class="pin-tr" data-pin="5" style="position:absolute;top:3px;left:21px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:var(--e1)"></span>
                    </span>
                  </div>
                  <div style="display:flex;align-items:center;gap:40px;margin-top:18px;opacity:.5">
                    <span style="flex:1;font-size:12px;font-weight:650">보안 경고</span>
                    <span data-pin="6" style="position:relative;width:44px;height:26px;border-radius:99px;background:var(--accent);flex:none">
                      <span style="position:absolute;top:3px;left:21px;width:20px;height:20px;border-radius:50%;background:#fff"></span>
                    </span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="switch", ko="스위치", en="Switch · Toggle",
  desc="스위치가 무엇인지, 체크박스와는 어떻게 다른지를 즉시 적용과 되돌림까지 포함해 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="스위치는 손잡이를 좌우로 옮겨 설정을 켜고 끄는 부품입니다. 체크박스와는 생김새만 다른 것이 아니라, <b>누르는 즉시 적용된다</b>는 약속이 다릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>같은 설정을 두 방식으로 만들어 두었습니다.</b> 위쪽 스위치는 누르는 즉시 적용되고 저장 버튼이 없습니다.
          반면 아래쪽 체크박스는 바꿔도 아무 일이 일어나지 않고 <b>저장</b>을 눌러야 적용됩니다. 두 방식을 한 화면에 섞으면 무엇이 이미 저장됐는지 알 수 없으므로
          화면마다 <b>한 가지 방식만 쓰는 것</b>이 규칙입니다.<br>
          세 번째 스위치는 서버가 요청을 거절해서 <b>원래대로 되돌아갑니다</b>. 즉시 적용 방식을 쓰려면 이렇게 실패했을 때 되돌리고 이유를 알리는 처리까지 만들어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스위치, 토글, 토글 스위치, 온오프"),
    ("영어", "switch, toggle"),
    ("같이 쓰는 말", "움직이는 동그라미는 <b>손잡이</b>(knob·thumb), 바탕의 알약 모양은 <b>트랙</b>이라고 부릅니다. 옆에 적는 '켬/끔'은 <b>상태 글자</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>체크박스</b> — 스위치와 특히 자주 혼동합니다. 저장 버튼이 있는 화면이면 스위치가 아니라 체크박스를 씁니다.<br>"
     "<b>토글</b> — 넓은 뜻으로는 맞는 말이지만, 토글은 켜고 끄는 <b>모든 것</b>을 가리키기 때문에 토글 버튼이나 세그먼티드 컨트롤까지 함께 섞입니다.<br>"
     "<b>슬라이더</b> — 손잡이가 움직인다고 모두 슬라이더는 아닙니다. 슬라이더는 <b>범위 안에서</b> 값을 고르는 부품입니다."),
  ]),
  axes=ax("스위치"),
  oneline="스위치는 <b>누르는 즉시</b> 적용됩니다. 그래서 저장 버튼이 있는 화면에 스위치를 두면 사용자는 무엇이 이미 저장됐는지 알 수 없습니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="꺼진 스위치"), "끔", "손잡이가 왼쪽에 있고 트랙은 회색입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="켜진 스위치"), "켬", "손잡이가 오른쪽으로 옮겨 갑니다. <b>누르는 순간</b> 바로 이 모습이 됩니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);opacity:.65;position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">서버에 보내는 중</div>', bars="", label="보류 중"), "보류 중", "서버 응답을 기다리는 동안 아주 옅게만 표시합니다. <b>표시가 눈에 띄면 사용자가 응답을 기다리게 됩니다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">제품 소식</span><span style="width:16px;height:9px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>' + toast("바꾸지 못해 되돌렸습니다", ""), bars="", label="되돌아간 스위치"), "되돌림", "서버가 거절하면 원래 상태로 되돌립니다. 이때 <b>아무 말 없이 되돌리지 않고</b> 이유를 알립니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px;opacity:.45"><span style="flex:1;font-size:6.5px">보안 경고</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">끌 수 없음 — 이유를 적을 것</div>', bars="", label="비활성 스위치"), "비활성", "켠 채로 끄지 못하게 막아 두는 경우가 많은데, 그럴 때는 이유를 적습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="포커스"), "포커스", "<kbd>Space</kbd>로 켜고 끕니다. 포커스 링을 지우지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("항목 이름", "label", "<b>켜면 무엇이 되는지</b> 적습니다. '알림 끄기'처럼 부정형으로 적으면 스위치를 켰을 때 알림이 꺼지는 셈이라 뜻이 헷갈립니다"),
    ("보조 설명", "description", "언제, 얼마나 자주 적용되는지 적습니다. 스위치는 누르는 즉시 적용되어 다시 확인을 물을 자리가 없으므로, 필요한 설명을 여기에 다 적어야 합니다"),
    ("상태 글자", "state label", "켬/끔을 글자로도 적습니다. 색과 손잡이 위치만으로는 색각 이상이 있는 사람에게 상태가 잘 전해지지 않습니다"),
    ("트랙", "track", "알약 모양의 바탕이며, 켜지면 색이 바뀝니다"),
    ("손잡이", "knob · thumb", "좌우로 움직이며, 이 움직임으로 상태가 방금 바뀌었다는 것을 알립니다"),
    ("비활성 스위치", "disabled", "바꿀 수 없는 스위치입니다. 흐리게만 두지 말고 <b>이유</b>를 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스위치에는 <b>중간 상태가 없다</b>는 점도 체크박스와 다릅니다.
          그래서 '일부만 켜짐'을 나타내야 하는 자리에는 스위치를 쓸 수 없습니다.</p>''',
  do=ul([
    "알림, 다크 모드, 공개 여부처럼 누르는 즉시 적용되는 설정을 바꿀 때",
    "켜자마자 무언가 달라지는 것이 <b>바로 눈에 보일</b> 때",
    "다시 한 번 누르면 원래대로 돌아가는, 되돌리기 쉬운 설정일 때",
  ]),
  dont=ul([
    "저장 버튼이 있는 폼 안에 둘 때. 체크박스를 씁니다",
    "약관 동의를 받을 때. 동의는 폼을 <b>보낼 때</b> 확정되므로 즉시 적용되는 일이 아닙니다",
    "켜고 끄는 것이 아니라 둘 중 하나를 고를 때. 라디오나 세그먼티드 컨트롤을 씁니다",
    "되돌리기 어려운 일을 할 때. 즉시 적용되므로 사용자가 다시 확인할 기회가 없습니다",
  ]),
  instead='저장을 눌러야 하면 <a href="checkbox.html">체크박스</a>, 둘 중 하나를 고르면 <a href="segmented.html">세그먼티드</a>나 <a href="radio.html">라디오</a>, 되돌릴 틈이 필요하면 <a href="toast.html">되돌리기 토스트</a>.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px;display:grid;gap:5px"><div style="display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">멘션과 답글</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div><div style="display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">주간 요약</span><span style="width:15px;height:8px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div></div>', bars="", tall=False, label="설정 목록 재현"),
     "설정 목록", "스위치를 가장 흔히 쓰는 곳으로, 저장 버튼이 아예 없습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">다크 모드</span><span style="font-size:5.5px;color:var(--fg-muted)">켬</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div>', bars="", tall=False, label="상태 글자가 붙은 재현"),
     "상태 글자", "켬/끔을 글자로도 적습니다. 색만으로는 상태가 모든 사람에게 전해지지 않습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">공개</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);opacity:.6;position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--accent);font-weight:700">바뀌는 중…</div>', bars="", tall=False, label="보류 중 재현"),
     "보류 중", "서버 응답을 받기 전의 모습입니다. 옅게만 표시하고 스피너는 띄우지 않습니다"),
  ]),
  code_lede="HTML 에는 네이티브 스위치가 없습니다. 체크박스를 스위치 모양으로 꾸미는 것보다 <code>&lt;button role=\"switch\"&gt;</code>로 만드는 편이 스위치라는 뜻을 더 분명하게 전합니다.",
  code='''&lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"switch"</span> <span class="a">aria-checked</span>=<span class="s">"true"</span>
        <span class="a">aria-label</span>=<span class="s">"멘션과 답글 알림"</span>&gt;&lt;/<span class="t">button</span>&gt;

<span class="c">// 1) 바로 바꾼다  2) 보낸다  3) 거절당하면 되돌린다</span>
btn.setAttribute(<span class="s">'aria-checked'</span>, String(!was));
<span class="a">try</span> <span class="a">{</span> <span class="a">await</span> api.set(!was); <span class="a">}</span>
<span class="a">catch</span> <span class="a">{</span>
  btn.setAttribute(<span class="s">'aria-checked'</span>, String(was));
  toast(<span class="s">'바꾸지 못해 되돌렸습니다'</span>);
<span class="a">}</span>

<span class="c">/* 움직임을 줄여 달라면 손잡이를 미끄러뜨리지 않는다 */</span>
@media (prefers-reduced-motion: reduce) <span class="a">{</span> .sw__btn::after <span class="a">{</span> <span class="t">transition</span>: none; <span class="a">}</span> <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Space</kbd>", "켜고 끕니다. <code>&lt;button&gt;</code>으로 만들면 <kbd>Enter</kbd>로도 바뀝니다"),
    ("<kbd>Tab</kbd>", "스위치마다 한 번씩 멈춥니다"),
    ("스크린 리더", "<code>role=\"switch\"</code> + <code>aria-checked</code> 를 달면 '켜짐/꺼짐'으로 읽습니다. 체크박스는 '선택됨'으로 읽어서 전해지는 뜻이 다릅니다"),
    ("되돌릴 때", "라이브 리전으로 되돌린 이유를 알립니다. 손잡이만 되돌리면 화면에서 눈을 뗀 사람은 되돌아간 줄 모릅니다"),
    ("라벨", "<code>aria-label</code>이나 연결된 라벨 글자가 꼭 있어야 합니다. 손잡이와 트랙만으로는 무엇을 켜는 스위치인지 알 수 없습니다"),
  ]),
  backend=rows([
    ("스위치 = 즉시 쓰기", "스위치는 누를 때마다 요청을 한 번씩 보냅니다. 여러 번 빠르게 누르면 요청이 쌓이므로 <b>마지막 요청만</b> 반영하고, 요청마다 멱등 키를 붙입니다."),
    ("되돌림이 설계의 전부", "<a href=\"optimistic.html\">낙관적 UI</a>와 같은 구조로, 화면을 먼저 바꾸고 서버가 거절하면 되돌립니다. 그래서 되돌릴 수 없는 일에는 스위치를 쓰면 안 됩니다."),
    ("저장 시점이 다르다", "체크박스는 폼을 보낼 때 한 번 저장하고, 스위치는 누를 때마다 저장합니다. 그래서 체크박스는 PUT 한 번, 스위치는 PATCH 여러 번이 되어 <b>API 형태가 아예 달라집니다</b>."),
    ("기본값과 상속", "'시스템 설정 따르기'처럼 켬과 끔 말고 세 번째 상태가 필요하면 스위치로는 나타낼 수 없습니다. 이때는 선택지가 셋인 라디오를 씁니다."),
  ]),
  plat_lede="스위치는 <b>iOS 에서 자리 잡은 부품</b>이라서, 모바일 설정 화면에서는 기본 부품처럼 쓰입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="웹 스위치 재현"),
     "<b>스위치</b> · 네이티브 부품이 없어서 직접 만들며, 이때 <code>role=\"switch\"</code>를 꼭 붙여야 합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px;display:grid;gap:8px"><div style="display:flex;align-items:center;gap:5px"><span style="flex:1;font-size:8px">알림</span><span style="width:22px;height:13px;border-radius:99px;background:#34c759;position:relative"><span style="position:absolute;top:1.5px;left:10.5px;width:10px;height:10px;border-radius:50%;background:#fff"></span></span></div></div>', "iOS 스위치 재현"),
     "<b>스위치</b>(Switch) · 설정 화면의 기본 부품이고 <b>초록색</b>이 표준입니다. 스위치라는 부품이 처음 자리 잡은 플랫폼입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:5px"><span style="flex:1;font-size:8px">알림</span><span style="width:24px;height:14px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:2px;left:12px;width:10px;height:10px;border-radius:50%;background:#fff;display:grid;place-items:center;color:var(--accent);font-size:6px">✓</span></span></div>', "안드로이드 스위치 재현"),
     "<b>스위치</b>(Switch) · 손잡이 안에 <b>체크 표시</b>가 들어가서 색이 아닌 방법으로도 켜짐을 알립니다."),
  ]),
  plat_note="안드로이드의 스위치는 손잡이 안에 <b>체크 아이콘</b>을 넣어서 색만으로 상태를 알리지 않게 합니다. 웹에서 스위치를 직접 만들 때 특히 자주 빠뜨리는 부분인데, 켬/끔 글자를 옆에 적어도 같은 효과를 낼 수 있습니다.",
  siblings=siblings("switch"),
  related='''        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><span class="na"><b>다크 모드</b><em>2부</em></span></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>''',
)
