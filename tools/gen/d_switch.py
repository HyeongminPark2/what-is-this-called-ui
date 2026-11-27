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
  desc="스위치가 무엇이고 체크박스와 어떻게 다른지, 즉시 적용과 되돌림까지 실물과 상태와 해부도로 보여주는 항목.",
  lede="켜고 끄는 손잡이. 체크박스와 생김새만 다른 게 아니라, <b>누르는 즉시 적용된다</b>는 약속이 다릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>같은 설정을 두 방식으로 뒀습니다.</b> 위는 누르는 즉시 적용되고 저장 버튼이 없습니다.
          아래는 바꿔도 아무 일이 없고 <b>저장</b>을 눌러야 합니다. 한 화면에 섞으면 무엇이 저장됐는지 알 수 없어
          <b>하나만 고르는 것</b>이 규칙입니다.<br>
          세 번째 스위치는 서버가 거절해 <b>되돌아갑니다</b> — 즉시 적용의 값은 여기서 치릅니다.</p>
        </div>''',
  names=rows([
    ("한국어", "스위치, 토글, 토글 스위치, 온오프"),
    ("영어", "switch, toggle"),
    ("같이 쓰는 말", "움직이는 동그라미를 <b>손잡이</b>(knob·thumb), 바탕 알약을 <b>트랙</b>이라 합니다. 옆에 적는 '켬/끔'은 <b>상태 글자</b>."),
    ("자주 잘못 부름",
     "<b>체크박스</b> — 가장 잦은 혼동입니다. 저장 버튼이 있으면 스위치를 쓰면 안 됩니다.<br>"
     "<b>토글</b> — 넓게는 맞지만, 토글은 켜고 끄는 <b>모든 것</b>을 가리켜 토글 버튼·세그먼티드까지 섞입니다.<br>"
     "<b>슬라이더</b> — 손잡이가 움직인다고 슬라이더가 아닙니다. 슬라이더는 <b>범위에서</b> 고릅니다."),
  ]),
  axes=ax("스위치"),
  oneline="스위치는 <b>누르는 즉시</b> 적용됩니다. 저장 버튼이 있는 화면에 스위치를 두면, 사용자는 무엇이 저장됐는지 알 수 없습니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="꺼진 스위치"), "끔", "손잡이가 왼쪽. 트랙이 회색"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="켜진 스위치"), "켬", "손잡이가 오른쪽. <b>누르는 순간</b> 이렇게 된다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);opacity:.65;position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">서버에 보내는 중</div>', bars="", label="보류 중"), "보류 중", "아주 옅게만. <b>눈에 띄면 기다리게 된다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">제품 소식</span><span style="width:16px;height:9px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>' + toast("바꾸지 못해 되돌렸습니다", ""), bars="", label="되돌아간 스위치"), "되돌림", "거절당하면 원래대로. <b>소리 없이 되돌리지 않는다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px;opacity:.45"><span style="flex:1;font-size:6.5px">보안 경고</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">끌 수 없음 — 이유를 적을 것</div>', bars="", label="비활성 스위치"), "비활성", "켠 채로 못 끄게 하는 일이 많다. 이유를 적는다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="포커스"), "포커스", "<kbd>Space</kbd>로 바꾼다. 링을 지우지 않는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("항목 이름", "label", "<b>켜면 무엇이 되는지</b>를 적는다. '알림 끄기' 같은 부정형은 켰을 때 뜻이 꼬인다"),
    ("보조 설명", "description", "언제·얼마나 자주. 스위치는 되물을 자리가 없어 여기서 다 설명해야 한다"),
    ("상태 글자", "state label", "켬/끔을 글자로도. 색과 위치만으로는 색각 이상인 사람에게 안 전해진다"),
    ("트랙", "track", "알약 모양 바탕. 켜지면 색이 바뀐다"),
    ("손잡이", "knob · thumb", "좌우로 움직인다. 이 움직임이 '방금 바뀌었다'를 알린다"),
    ("비활성 스위치", "disabled", "못 바꾸는 것. 흐리게만 두지 말고 <b>이유</b>를 적는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          스위치에는 <b>중간 상태가 없습니다.</b> 체크박스와 갈리는 또 하나의 지점이고,
          '일부만 켜짐'을 나타내야 하면 스위치로는 안 됩니다.</p>''',
  do=ul([
    "누르는 즉시 적용되는 설정 — 알림, 다크 모드, 공개 여부",
    "결과가 <b>바로 보이는</b> 것 — 켜면 뭔가 달라지는 게 눈에 보일 때",
    "되돌리기 쉬운 것 — 다시 누르면 끝나는 일",
  ]),
  dont=ul([
    "저장 버튼이 있는 폼 안 → 체크박스를 씁니다",
    "약관 동의 — 동의는 <b>보낼 때</b> 확정되는 것이라 즉시 적용이 아닙니다",
    "둘 중 하나를 고르는 것 → 켜고 끄기가 아니라 선택이면 라디오나 세그먼티드",
    "되돌리기 어려운 일 — 즉시 적용은 확인할 틈이 없습니다",
  ]),
  instead='저장을 눌러야 하면 <a href="checkbox.html">체크박스</a>, 둘 중 하나를 고르면 <a href="segmented.html">세그먼티드</a>나 <a href="radio.html">라디오</a>, 되돌릴 틈이 필요하면 <a href="toast.html">되돌리기 토스트</a>.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px;display:grid;gap:5px"><div style="display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">멘션과 답글</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div><div style="display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">주간 요약</span><span style="width:15px;height:8px;border-radius:99px;background:var(--line-strong);position:relative"><span style="position:absolute;top:1.5px;left:1.5px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div></div>', bars="", tall=False, label="설정 목록 재현"),
     "설정 목록", "가장 흔한 자리. 저장 버튼이 아예 없다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">다크 모드</span><span style="font-size:5.5px;color:var(--fg-muted)">켬</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div>', bars="", tall=False, label="상태 글자가 붙은 재현"),
     "상태 글자", "켬/끔을 글자로도 적는다. 색만으로는 안 전해진다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6px">공개</span><span style="width:15px;height:8px;border-radius:99px;background:var(--accent);opacity:.6;position:relative"><span style="position:absolute;top:1.5px;left:8px;width:5px;height:5px;border-radius:50%;background:#fff"></span></span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--accent);font-weight:700">바뀌는 중…</div>', bars="", tall=False, label="보류 중 재현"),
     "보류 중", "서버 응답 전. 옅게만 표시하고 스피너는 띄우지 않는다"),
  ]),
  code_lede="네이티브 스위치는 없습니다. <code>&lt;button role=\"switch\"&gt;</code>로 만드는 쪽이 체크박스를 꾸미는 쪽보다 뜻이 분명합니다.",
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
    ("<kbd>Space</kbd>", "켜고 끈다. <code>&lt;button&gt;</code>으로 만들면 <kbd>Enter</kbd>도 먹는다"),
    ("<kbd>Tab</kbd>", "칸마다 한 번씩 지난다"),
    ("스크린 리더", "<code>role=\"switch\"</code> + <code>aria-checked</code> 로 '켜짐/꺼짐'으로 읽힌다. 체크박스는 '선택됨'으로 읽혀 뜻이 다르다"),
    ("되돌릴 때", "라이브 리전으로 이유를 알린다. 손잡이만 되돌리면 눈을 뗀 사람은 모른다"),
    ("라벨", "<code>aria-label</code>이나 이어진 글자가 꼭 있어야 한다. 동그라미만으로는 무엇인지 알 수 없다"),
  ]),
  backend=rows([
    ("스위치 = 즉시 쓰기", "누를 때마다 요청이 한 번 갑니다. 연타하면 요청이 쌓이니 <b>마지막 것만</b> 반영하고, 멱등 키를 붙입니다."),
    ("되돌림이 설계의 전부", "<a href=\"optimistic.html\">낙관적 UI</a>와 같은 구조입니다. 되돌릴 수 없는 일이면 스위치를 쓰면 안 됩니다."),
    ("저장 시점이 다르다", "체크박스는 폼을 보낼 때 한 번, 스위치는 누를 때마다. <b>API 모양이 아예 달라집니다</b> — 한 번의 PUT 과 여러 번의 PATCH."),
    ("기본값과 상속", "'시스템 설정 따르기' 같은 제3의 상태가 필요하면 스위치로는 못 담습니다. 그때는 선택지가 셋인 라디오입니다."),
  ]),
  plat_lede="스위치는 <b>iOS 에서 굳은 부품</b>이고, 그래서 모바일 설정 화면의 기본값처럼 쓰입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;align-items:center;gap:4px"><span style="flex:1;font-size:6.5px">주간 요약</span><span style="width:16px;height:9px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:1.5px;left:8.5px;width:6px;height:6px;border-radius:50%;background:#fff"></span></span></div>', bars="", label="웹 스위치 재현"),
     "<b>스위치</b> · 네이티브 부품이 없어 직접 만듭니다. <code>role=\"switch\"</code>를 붙이는 것이 핵심입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px;display:grid;gap:8px"><div style="display:flex;align-items:center;gap:5px"><span style="flex:1;font-size:8px">알림</span><span style="width:22px;height:13px;border-radius:99px;background:#34c759;position:relative"><span style="position:absolute;top:1.5px;left:10.5px;width:10px;height:10px;border-radius:50%;background:#fff"></span></span></div></div>', "iOS 스위치 재현"),
     "<b>스위치</b>(Switch) · 설정 화면의 기본 부품이고 <b>초록색</b>이 표준입니다. 이 부품의 고향입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:flex;align-items:center;gap:5px"><span style="flex:1;font-size:8px">알림</span><span style="width:24px;height:14px;border-radius:99px;background:var(--accent);position:relative"><span style="position:absolute;top:2px;left:12px;width:10px;height:10px;border-radius:50%;background:#fff;display:grid;place-items:center;color:var(--accent);font-size:6px">✓</span></span></div>', "안드로이드 스위치 재현"),
     "<b>스위치</b>(Switch) · 손잡이 안에 <b>체크 표시</b>가 들어가 색 말고도 켜짐을 알립니다."),
  ]),
  plat_note="안드로이드의 스위치는 손잡이 안에 <b>체크 아이콘</b>을 넣습니다 — 색만으로 알리지 않으려는 장치입니다. 웹에서 직접 만들 때 가장 자주 빠뜨리는 부분이고, 켬/끔 글자를 옆에 적는 것으로도 같은 효과를 냅니다.",
  siblings=siblings("switch"),
  related='''        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><span class="na"><b>다크 모드</b><em>2부</em></span></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>''',
)
