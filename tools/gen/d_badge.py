# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def anchor(badge, icon="✉"):
    return ('              <div style="display:grid;place-items:center"><span style="position:relative;display:inline-block">'
            '<span style="display:grid;place-items:center;width:34px;height:34px;border-radius:9px;background:var(--surface);border:1px solid var(--line);font-size:15px">%s</span>'
            '%s</span></div>') % (icon, badge)

def num(txt, bg="var(--danger)", fg="#fff"):
    return ('<span style="position:absolute;top:-6px;right:-8px;min-width:18px;height:18px;padding:0 5px;'
            'border-radius:99px;background:%s;color:%s;font-size:10.5px;font-weight:800;display:grid;'
            'place-items:center;line-height:1">%s</span>') % (bg, fg, txt)

def lab(txt, cls="bdg--neutral"):
    return '              <span class="bdg %s" style="height:20px;padding:0 9px;font-size:11px">%s</span>' % (cls, txt)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:20px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:17px">
                  <div class="pin-out" data-pin="1" style="display:flex;align-items:center;gap:12px">
                    <span style="position:relative;display:inline-block;flex:none;margin-left:4px">
                      <span style="display:grid;place-items:center;width:34px;height:34px;border-radius:9px;background:var(--surface);font-size:15px">✉</span>
                      <span style="position:absolute;top:-6px;right:-8px;min-width:18px;height:18px;padding:0 5px;border-radius:99px;background:var(--danger);color:#fff;font-size:10.5px;font-weight:800;display:grid;place-items:center;line-height:1">3</span>
                    </span>
                    <span style="font-size:11px;color:var(--fg-muted)">배지는 <b style="color:var(--fg)">혼자 서지 않는다</b> — 늘 무엇에 붙는다</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">top: -6px;  right: -8px</div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span class="bdg" style="height:18px;padding:0 6px;font-size:10px">99+</span><span>세 자리가 되면 이렇게 줄인다</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span class="bdg bdg--ok" style="height:19px;padding:0 8px;font-size:10.5px">승인됨</span><span>한 낱말짜리 라벨 배지</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-label="읽지 않음 3건"</div>
                </div>
              </div>'''

D = dict(
  slug="badge", ko="배지", en="Badge · notification badge",
  desc="배지의 갈래(점·숫자·라벨)와 99+ 처리, 칩과의 차이를 실물과 해부도로 보여주는 항목.",
  lede="다른 것에 <b>붙어서 한마디 보태는</b> 작은 표시. 혼자 서지 않습니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끝까지 밀어 보세요. 세 자리가 되면 <b><code>99+</code></b>로 줄어듭니다 —
          안 줄이면 배지가 길어져 붙어 있던 아이콘을 밀어냅니다.
          <b>0으로 내리면 배지가 아예 사라집니다.</b> '0건'을 보여 줄 이유가 없습니다.<br>
          화면 아래에 <b>스크린 리더가 읽는 말</b>이 같이 바뀝니다. 빨간 동그라미는 그 자체로 아무 뜻이 아니라서,
          붙은 쪽에 말로 적어 둬야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배지, 알림 배지, 뱃지, 상태 라벨, 태그"),
    ("영어", "badge, notification badge, dot badge, status label, pill"),
    ("같이 쓰는 말",
     "숫자 없이 점만 찍은 것을 <b>점 배지</b>(dot badge), 숫자가 든 것을 <b>카운트 배지</b>(count badge), "
     "글자가 든 알약 모양을 <b>라벨 배지</b> 또는 <b>필</b>(pill)이라 합니다. "
     "배지가 붙는 쪽(아이콘·줄)은 <b>앵커</b>(anchor)입니다."),
    ("자주 잘못 부름",
     "<b>칩</b> — 가장 잦은 혼동입니다. 칩은 <b>눌러서 거르거나 뗄 수 있고</b>, 배지는 붙어서 알리기만 합니다.<br>"
     "<b>태그</b> — 태그는 내가 <b>붙인 분류</b>입니다. 배지는 시스템이 말해 주는 상태입니다.<br>"
     "<b>토스트</b> — 토스트는 떠서 알리고 <b>사라집니다</b>. 배지는 붙어서 남습니다."),
  ]),
  axes=ax("배지"),
  oneline="배지는 <b>붙어 있어야</b> 배지입니다. 혼자 서 있고 누를 수 있으면 그건 <a href=\"chip.html\">칩</a>입니다.",
  s4_title="갈래", s4_hint="같은 모양이 다른 일을 한다",
  states=states([
    (anchor('<span style="position:absolute;top:-3px;right:-3px;width:9px;height:9px;border-radius:99px;'
            'background:var(--danger);box-shadow:0 0 0 2px var(--bg);display:block"></span>', '🔔'),
     "점", "<b>있다/없다</b>만 말한다. 개수를 셀 수 없을 때"),
    (anchor(num('3')), "숫자", "몇 건인지 말한다. <b>셀 수 있을 때만</b>"),
    (anchor(num('99+')), "넘침", "세 자리는 <b>99+</b>. 안 줄이면 아이콘을 밀어낸다"),
    (lab("승인됨", "bdg--ok"), "라벨 — 좋음", "상태를 한 낱말로. <b>초록은 끝난 것</b>"),
    (lab("검토 중", "bdg--warn"), "라벨 — 진행", "아직 결정 안 난 것"),
    (lab("거절됨", ""), "라벨 — 나쁨", "<b>색만으로 말하지 않는다</b> — 글자가 이미 다 말하고 있다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앵커", "anchor", "배지가 붙는 쪽. 아이콘·줄·탭. <b>이것 없이는 배지가 없다</b>"),
    ("자리", "position", "보통 오른쪽 위 모서리. 앵커에 <code>position: relative</code> 한 줄이 빠지면 화면 구석으로 날아간다"),
    ("넘침 규칙", "overflow · 99+", "두 자리까지만 보이고 그 위는 <b>99+</b>. 숫자가 아니라 규칙을 먼저 정한다"),
    ("라벨 배지", "status label", "숫자가 아니라 <b>한 낱말</b>. 목록의 뒤쪽 자리에 자주 온다"),
    ("읽히는 말", "aria-label", "빨간 점은 <b>소리로는 아무것도 아니다</b>. 앵커에 말로 적어 둔다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          배지를 붙일 때 가장 자주 나는 사고 둘입니다. ① 앵커에 <code>position: relative</code>를 안 줘서
          배지가 <b>화면 구석</b>으로 날아갑니다. ② 앵커나 그 위 상자에 <code>overflow: hidden</code>이 걸려 있어
          <b>모서리 밖으로 나간 배지가 잘립니다.</b> 둘 다 '배지가 안 보여요'로 제보되는데 원인이 다릅니다.</p>''',
  do=ul([
    "<b>안 읽은 것·처리할 것</b>이 몇 건인지 알릴 때",
    "목록에서 <b>상태를 한 낱말로</b> 보여 줄 때 — 승인됨·검토 중·거절됨",
    "탭이나 메뉴에 '여기 새것이 있다'를 표시할 때",
  ]),
  dont=ul([
    "<b>늘 켜 두는 것</b> — 안 꺼지는 빨간 점은 금세 안 보이게 됩니다",
    "누르게 만드는 것 → 그건 <a href=\"chip.html\">칩</a>이나 버튼입니다",
    "0건을 '0'으로 보여 주는 것 — <b>없으면 없애야</b> 합니다",
    "색만으로 뜻을 말하는 것 — 빨강/초록은 색맹에게 같은 회색입니다",
  ]),
  instead='눌러서 거르면 <a href="chip.html">칩</a>, 떠서 알리고 사라지면 <a href="../items/toast.html">토스트</a>, 진행 정도면 <a href="../items/progress.html">프로그레스 바</a>.',
  cases=cases([
    ('''              <div style="display:flex;gap:18px;align-items:center">''' +
     anchor(num('3'), '✉').replace('              <div style="display:grid;place-items:center">', '<span>').replace('</div>', '</span>') + '''</div>''',
     "안 읽은 메일", "가장 익숙한 자리. 아이콘 오른쪽 위"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:8px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px 9px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:9px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                <span style="flex:1;min-width:0;font-size:11.5px;font-weight:600">정산 요청 #4821</span>
                <span class="bdg bdg--warn" style="height:18px;padding:0 7px;font-size:10px;flex:none">검토 중</span>
              </div>''',
     "줄 끝의 상태", "목록에서 <b>지금 어디까지 왔는지</b>를 한 낱말로"),
    ('''              <div style="display:flex;gap:14px;border-bottom:1px solid var(--line);padding-bottom:5px;width:100%;max-width:190px">
                <span style="font-size:11px;color:var(--accent);font-weight:700;border-bottom:2px solid var(--accent);padding-bottom:4px;margin-bottom:-6px">전체</span>
                <span style="font-size:11px;color:var(--fg-muted);display:flex;align-items:center;gap:4px">문의
                  <span class="bdg" style="height:15px;min-width:15px;padding:0 4px;font-size:9px">3</span></span>
              </div>''',
     "탭 위의 숫자", "<b>안 열어 본 탭</b>에 몇 건이 있는지"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 부품의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="배지에는 정해진 역할이 없습니다. 중요한 것은 <b>붙는 쪽이 말을 갖는 것</b>입니다.",
  code='''&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/inbox"</span> <span class="a">class</span>=<span class="s">"anchor"</span>
   <span class="a">aria-label</span>=<span class="s">"메일 — 읽지 않음 3건"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"bdg"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;3&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">a</span>&gt;

<span class="t">.anchor</span> { <span class="a">position</span>: relative; }   <span class="c">/* 이게 없으면 배지가 날아간다 */</span>
<span class="t">.bdg</span> { <span class="a">position</span>: absolute; <span class="a">top</span>: -<span class="a">6px</span>; <span class="a">right</span>: -<span class="a">8px</span>; }
<span class="t">.bdg</span>[<span class="a">hidden</span>] { <span class="a">display</span>: none; } <span class="c">/* inline-flex 가 hidden 을 이긴다 */</span>

<span class="c">// 숫자는 화면용으로만 줄이고, 읽히는 말에는 원래 수를 둔다</span>
badge.textContent = n &gt; <span class="a">99</span> ? <span class="s">'99+'</span> : n;
badge.hidden = (n === <span class="a">0</span>);''',
  keys=kbd([
    ("앵커에 <code>position: relative</code>", "빠지면 배지가 <b>화면 구석</b>에 가서 붙는다. 제보 1위"),
    ("<code>overflow: hidden</code>을 조심", "모서리 밖으로 나간 배지가 <b>잘린다</b>. 안쪽 요소가 모서리를 깎게 바꾼다"),
    ("0이면 없앤다", "<code>hidden</code>을 주되 <code>display</code>가 이기지 않는지 확인한다"),
    ("99+ 로 줄인다", "길어지면 앵커를 밀어낸다. <b>글자 수가 아니라 폭</b>이 문제다"),
    ("말은 앵커가 갖는다", "배지 자체는 <code>aria-hidden</code>으로 숨기고, 앵커의 <code>aria-label</code>에 적는다"),
    ("실시간이면 <code>aria-live</code>", "숫자가 저절로 바뀌는 자리면 <code>polite</code>로 알린다 — 다만 자주 바뀌면 시끄럽다"),
  ]),
  backend=rows([
    ("개수는 어디서 오나", "배지 숫자는 보통 <b>따로 세는 API</b>입니다. 목록을 다 받아 세면 느리고, 목록이 100건을 넘으면 틀립니다. <code>unread_count</code> 하나를 돌려주는 쪽이 낫습니다."),
    ("99+ 로 줄이는 이유", "정확한 수가 필요 없으면 <b>세는 비용도 줄일 수 있습니다.</b> 'COUNT(*) LIMIT 100' 처럼 100까지만 세고 멈추는 질의가 훨씬 쌉니다."),
    ("언제 줄어드나", "읽음 처리와 배지 감소 사이에 <b>시차</b>가 생기면 '읽었는데 안 없어져요'가 됩니다. 화면에서 먼저 줄이고(<a href=\"../items/optimistic.html\">낙관적 UI</a>) 서버 응답으로 맞춥니다."),
    ("밀어 주기", "웹소켓이나 푸시로 수를 밀어 주면 새로고침 없이 바뀝니다. 다만 <b>한 번에 몰아 보내면</b> 숫자가 깜빡여 보이니 묶어서 보냅니다."),
  ]),
  plat_lede="두 OS 는 배지가 <b>OS 기능</b>이기도 합니다 — 앱 아이콘 위의 그 숫자입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     anchor(num('3')),
     "직접 그립니다. 브라우저 탭 제목에 <code>(3)</code>을 넣거나 <b>앱 배지 API</b>로 설치형 앱 아이콘에 붙일 수 있습니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 앱 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:34px;transform:translateX(-50%);position:relative"></div>
                <div style="position:absolute;left:14px;top:34px"><span style="display:block;width:22px;height:22px;border-radius:6px;background:var(--accent-soft)"></span>
                  <span style="position:absolute;top:-5px;right:-6px;min-width:12px;height:12px;padding:0 3px;border-radius:99px;background:var(--danger);color:#fff;font-size:7px;font-weight:800;display:grid;place-items:center">3</span></div>
              </div></div>''',
     "<b>앱 배지</b>가 OS 기능입니다. 홈 화면 아이콘의 빨간 숫자는 앱이 아니라 <b>시스템이 그립니다.</b>"),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:space-around">
                  <span style="position:relative"><span style="display:block;width:16px;height:16px;border-radius:5px;background:var(--accent-soft)"></span>
                    <span style="position:absolute;top:-4px;right:-5px;min-width:11px;height:11px;padding:0 3px;border-radius:99px;background:var(--danger);color:#fff;font-size:6.5px;font-weight:800;display:grid;place-items:center">3</span></span>
                  <span style="display:block;width:16px;height:16px;border-radius:5px;background:var(--line)"></span>
                </div>
              </div></div>''',
     "<b>Badge</b> 가 정식 부품이고 <b>작은 배지</b>(점)와 <b>큰 배지</b>(숫자) 두 갈래입니다. 런처 아이콘의 점은 OS 가 그립니다."),
  ]),
  plat_note="앱에서 \"배지 붙여 주세요\"는 <b>앱 아이콘의 빨간 숫자</b>를 뜻하기도 합니다. 그건 화면 안의 배지와 전혀 다른 일이고 <b>푸시 알림과 묶여</b> 있어 서버 쪽 작업이 따로 필요합니다. 어느 쪽인지 먼저 확인하세요.",
  siblings=siblings("badge"),
  related='''        <li><a href="../items/chip.html"><b>칩</b><em>5부</em></a></li>
        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><span class="na"><b>알림 센터</b><em>13부</em></span></li>''',
)
