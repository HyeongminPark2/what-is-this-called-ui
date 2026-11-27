# -*- coding: utf-8 -*-
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
                    <span style="font-size:11px;color:var(--fg-muted)">배지는 <b style="color:var(--fg)">혼자 놓이지 않고</b> 늘 무언가에 붙음</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">top: -6px;  right: -8px</div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span class="bdg" style="height:18px;padding:0 6px;font-size:10px">99+</span><span>세 자리가 되면 이렇게 줄임</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="display:flex;align-items:center;gap:9px;font-size:11px;color:var(--fg-muted)">
                    <span class="bdg bdg--ok" style="height:19px;padding:0 8px;font-size:10.5px">승인됨</span><span>한 낱말짜리 라벨 배지</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">aria-label="읽지 않음 3건"</div>
                </div>
              </div>'''

D = dict(
  slug="badge", ko="배지", en="Badge · notification badge",
  desc="배지의 갈래(점·숫자·라벨)와 99+ 처리, 칩과의 차이를 실물과 해부도로 보여 주는 항목입니다.",
  lede="배지는 아이콘이나 목록 줄 같은 다른 요소에 <b>붙어서 정보를 하나 더 알려 주는</b> 작은 표시입니다. 배지만 따로 떨어져 놓이는 일은 없습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끝까지 밀어 보세요. 숫자가 세 자리가 되면 <b><code>99+</code></b>로 줄어드는데,
          줄이지 않으면 배지가 길어져서 붙어 있던 아이콘을 밀어내기 때문입니다.
          반대로 <b>0으로 내리면 배지가 아예 사라집니다.</b> 알릴 것이 없을 때 '0건'을 굳이 보여 줄 이유가 없기 때문입니다.<br>
          화면 아래의 <b>스크린 리더가 읽는 말</b>도 함께 바뀝니다. 빨간 동그라미만으로는 스크린 리더가 아무것도 읽어 줄 수 없으므로,
          배지가 붙은 요소에 뜻을 글로 적어 두어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "배지, 알림 배지, 뱃지, 상태 라벨, 태그"),
    ("영어", "badge, notification badge, dot badge, status label, pill"),
    ("같이 쓰는 말",
     "숫자 없이 점만 찍은 것은 <b>점 배지</b>(dot badge), 숫자가 든 것은 <b>카운트 배지</b>(count badge),  "
     "글자가 든 알약 모양은 <b>라벨 배지</b> 또는 <b>필</b>(pill)이라고 부릅니다.  "
     "배지가 붙는 아이콘이나 줄은 <b>앵커</b>(anchor)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>칩</b> — 배지와 가장 자주 헷갈리는 부품입니다. 칩은 <b>눌러서 목록을 거르거나 뗄 수 있고</b>, 배지는 다른 요소에 붙어서 알리기만 합니다.<br>"
     "<b>태그</b> — 태그는 사용자가 <b>직접 붙인 분류</b>이고, 배지는 시스템이 알려 주는 상태입니다.<br>"
     "<b>토스트</b> — 토스트는 화면에 잠깐 떠서 알린 뒤 <b>사라지고</b>, 배지는 요소에 붙은 채로 남아 있습니다."),
  ]),
  s4_title="배지의 종류", s4_hint="종류마다 알리는 내용",
  states=states([
    (anchor('<span style="position:absolute;top:-3px;right:-3px;width:9px;height:9px;border-radius:99px;'
            'background:var(--danger);box-shadow:0 0 0 2px var(--bg);display:block"></span>', '🔔'),
     "있고 없음만 알리는 점", "새 소식이 <b>있는지 없는지</b>만 알립니다. 개수를 셀 수 없을 때 씁니다"),
    (anchor(num('3')), "건수를 알리는 숫자", "몇 건인지 알립니다. <b>개수를 셀 수 있을 때만</b> 씁니다"),
    (anchor(num('99+')), "숫자가 세 자리를 넘을 때", "세 자리 숫자는 <b>99+</b>로 줄입니다. 줄이지 않으면 배지가 길어져 아이콘을 밀어냅니다"),
    (lab("승인됨", "bdg--ok"), "처리가 끝난 상태의 라벨", "상태를 한 낱말로 보여 줍니다. <b>초록은 처리가 끝난 것</b>을 뜻합니다"),
    (lab("검토 중", "bdg--warn"), "진행 중인 상태의 라벨", "아직 결정이 나지 않은 상태입니다"),
    (lab("거절됨", ""), "거절된 상태의 라벨", "<b>색만으로 뜻을 전하지 않습니다</b>. 색이 없어도 글자만으로 상태를 알 수 있습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앵커", "anchor", "배지가 붙는 아이콘, 줄, 탭입니다. <b>배지는 앵커 없이 혼자 쓰지 않습니다</b>"),
    ("자리", "position", "보통 앵커의 오른쪽 위 모서리에 붙습니다. 앵커에 <code>position: relative</code> 한 줄이 빠지면 배지가 화면 구석으로 가서 붙습니다"),
    ("넘침 규칙", "overflow · 99+", "두 자리까지만 그대로 보여 주고 그보다 크면 <b>99+</b>로 줄입니다. 숫자가 몇이든 같은 규칙이 적용되도록 규칙부터 정해 둡니다"),
    ("라벨 배지", "status label", "숫자 대신 <b>한 낱말</b>을 담습니다. 목록 줄의 뒤쪽 자리에 자주 놓입니다"),
    ("읽히는 말", "aria-label", "빨간 점은 <b>스크린 리더가 읽어 줄 내용이 없습니다</b>. 그래서 앵커에 뜻을 글로 적어 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          배지를 붙일 때 특히 자주 생기는 오류가 두 가지 있습니다. ① 앵커에 <code>position: relative</code>를 주지 않아서
          배지가 <b>화면 구석</b>에 가서 붙습니다. ② 앵커나 그 바깥 상자에 <code>overflow: hidden</code>이 걸려 있어서
          <b>모서리 밖으로 나간 배지가 잘립니다.</b> 두 오류 모두 '배지가 안 보여요'라는 제보로 들어오지만 원인은 서로 다릅니다.</p>''',
  do=ul([
    "<b>안 읽은 것이나 처리할 것</b>이 몇 건인지 알릴 때",
    "목록에서 승인됨, 검토 중, 거절됨처럼 <b>상태를 한 낱말로</b> 보여 줄 때",
    "탭이나 메뉴에 새로 들어온 것이 있다고 표시할 때",
  ]),
  dont=ul([
    "배지를 <b>늘 켜 둘 때</b>. 꺼지지 않는 빨간 점에는 사용자가 금세 익숙해져서 더는 눈여겨보지 않습니다",
    "배지를 누를 수 있게 만들 때. 누르는 것이라면 배지가 아니라 <a href=\"chip.html\">칩</a>이나 버튼입니다",
    "0건을 '0'으로 보여 줄 때. 알릴 것이 <b>없으면 배지를 없애야</b> 합니다",
    "색만으로 뜻을 전할 때. 빨강과 초록은 색맹인 사람에게 같은 회색으로 보입니다",
  ]),
  instead='눌러서 목록을 걸러야 하면 <a href="chip.html">칩</a>을 쓰고, 잠깐 떠서 알린 뒤 사라져야 하면 <a href="../items/toast.html">토스트</a>를 씁니다. 일이 얼마나 진행됐는지 보여 주려면 <a href="../items/progress.html">프로그레스 바</a>가 맞습니다.',
  cases=cases([
    ('''              <div style="display:flex;gap:18px;align-items:center">''' +
     anchor(num('3'), '✉').replace('              <div style="display:grid;place-items:center">', '<span>').replace('</div>', '</span>') + '''</div>''',
     "안 읽은 메일 수 알리기", "배지를 가장 흔히 보는 자리로, 아이콘 오른쪽 위에 붙습니다"),
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:8px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px 9px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:9px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                <span style="flex:1;min-width:0;font-size:11.5px;font-weight:600">정산 요청 #4821</span>
                <span class="bdg bdg--warn" style="height:18px;padding:0 7px;font-size:10px;flex:none">검토 중</span>
              </div>''',
     "목록 줄 끝에 상태 보여 주기", "목록의 각 건이 <b>지금 어느 단계에 있는지</b>를 한 낱말로 보여 줍니다"),
    ('''              <div style="display:flex;gap:14px;border-bottom:1px solid var(--line);padding-bottom:5px;width:100%;max-width:190px">
                <span style="font-size:11px;color:var(--accent);font-weight:700;border-bottom:2px solid var(--accent);padding-bottom:4px;margin-bottom:-6px">전체</span>
                <span style="font-size:11px;color:var(--fg-muted);display:flex;align-items:center;gap:4px">문의
                  <span class="bdg" style="height:15px;min-width:15px;padding:0 4px;font-size:9px">3</span></span>
              </div>''',
     "탭에 새로 온 건수 알리기", "<b>아직 열어 보지 않은 탭</b>에 몇 건이 있는지 알려 줍니다"),
  ]),
  s8_title="최소 마크업과 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="배지에는 따로 정해진 역할(role)이 없습니다. 그래서 스크린 리더가 읽을 말은 배지가 아니라 <b>배지가 붙는 앵커에 적어 두는 것</b>이 중요합니다.",
  code='''&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/inbox"</span> <span class="a">class</span>=<span class="s">"anchor"</span>
   <span class="a">aria-label</span>=<span class="s">"메일 — 읽지 않음 3건"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
  &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"bdg"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;3&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">a</span>&gt;

<span class="t">.anchor</span> { <span class="a">position</span>: relative; }   <span class="c">/* 이 줄이 없으면 배지가 화면 구석으로 간다 */</span>
<span class="t">.bdg</span> { <span class="a">position</span>: absolute; <span class="a">top</span>: -<span class="a">6px</span>; <span class="a">right</span>: -<span class="a">8px</span>; }
<span class="t">.bdg</span>[<span class="a">hidden</span>] { <span class="a">display</span>: none; } <span class="c">/* 이 줄이 없으면 inline-flex 가 hidden 보다 우선한다 */</span>

<span class="c">// 숫자는 화면용으로만 줄이고, 읽히는 말에는 원래 수를 둔다</span>
badge.textContent = n &gt; <span class="a">99</span> ? <span class="s">'99+'</span> : n;
badge.hidden = (n === <span class="a">0</span>);''',
  keys=kbd([
    ("앵커에 <code>position: relative</code> 주기", "빠지면 배지가 <b>화면 구석</b>에 가서 붙습니다. 배지 관련 제보 가운데 가장 많습니다"),
    ("<code>overflow: hidden</code>에 잘리지 않게 하기", "모서리 밖으로 나간 배지가 <b>잘립니다</b>. 앵커 대신 안쪽 요소가 모서리를 깎도록 바꿉니다"),
    ("0건이면 배지 없애기", "<code>hidden</code>을 주되, <code>display</code> 값이 <code>hidden</code>보다 우선해서 배지가 그대로 보이지 않는지 확인합니다"),
    ("세 자리 숫자는 99+로 줄이기", "배지가 길어지면 앵커를 밀어냅니다. <b>글자 수보다 배지 폭</b>이 늘어나는 것이 문제입니다"),
    ("읽힐 말은 앵커에 적기", "배지 자체는 <code>aria-hidden</code>으로 숨기고, 읽힐 말은 앵커의 <code>aria-label</code>에 적습니다"),
    ("숫자가 저절로 바뀌면 <code>aria-live</code> 쓰기", "숫자가 저절로 바뀌는 자리라면 <code>polite</code>로 알립니다. 다만 너무 자주 바뀌면 스크린 리더가 계속 읽어서 번거롭습니다"),
  ]),
  backend=rows([
    ("배지 숫자를 받아 오는 곳", "배지 숫자는 보통 <b>개수만 따로 세는 API</b>에서 받습니다. 목록을 모두 받아 화면에서 세면 느리고, 목록이 100건을 넘으면 받은 만큼만 세게 되어 숫자가 틀립니다. 그래서 <code>unread_count</code> 값 하나를 돌려주는 쪽이 낫습니다."),
    ("99+로 줄이면 가벼워지는 세기", "화면에 99+까지만 보여 준다면 정확한 수가 필요 없으므로 <b>세는 비용도 줄일 수 있습니다.</b> 'COUNT(*) LIMIT 100' 처럼 100까지만 세고 멈추는 질의가 전체를 세는 질의보다 훨씬 가볍습니다."),
    ("읽은 뒤 숫자가 줄어드는 시점", "읽음 처리와 배지 숫자가 줄어드는 시점 사이에 <b>시차</b>가 생기면 '읽었는데 배지가 안 없어져요'라는 문의가 들어옵니다. 그래서 화면에서 먼저 숫자를 줄이고(<a href=\"../items/optimistic.html\">낙관적 UI</a>) 서버 응답이 오면 그 값으로 맞춥니다."),
    ("서버가 숫자를 밀어 줄 때", "웹소켓이나 푸시로 서버가 숫자를 보내 주면 새로고침하지 않아도 배지가 바뀝니다. 다만 변경을 <b>짧은 사이에 연달아 보내면</b> 숫자가 깜빡이는 것처럼 보이므로, 여러 변경을 묶어서 보냅니다."),
  ]),
  plat_lede="iOS와 안드로이드에서는 배지가 <b>OS 기능</b>이기도 합니다. 홈 화면의 앱 아이콘 위에 붙는 숫자가 그것입니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     anchor(num('3')),
     "배지를 직접 그려야 합니다. 브라우저 탭 제목에 <code>(3)</code>을 넣거나, <b>앱 배지 API</b>로 설치형 웹 앱 아이콘에 숫자를 붙일 수 있습니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 앱 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:34px;transform:translateX(-50%);position:relative"></div>
                <div style="position:absolute;left:14px;top:34px"><span style="display:block;width:22px;height:22px;border-radius:6px;background:var(--accent-soft)"></span>
                  <span style="position:absolute;top:-5px;right:-6px;min-width:12px;height:12px;padding:0 3px;border-radius:99px;background:var(--danger);color:#fff;font-size:7px;font-weight:800;display:grid;place-items:center">3</span></div>
              </div></div>''',
     "<b>앱 배지</b>가 OS 기능으로 있습니다. 홈 화면 아이콘의 빨간 숫자는 앱이 아니라 <b>시스템이 그립니다.</b>"),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:space-around">
                  <span style="position:relative"><span style="display:block;width:16px;height:16px;border-radius:5px;background:var(--accent-soft)"></span>
                    <span style="position:absolute;top:-4px;right:-5px;min-width:11px;height:11px;padding:0 3px;border-radius:99px;background:var(--danger);color:#fff;font-size:6.5px;font-weight:800;display:grid;place-items:center">3</span></span>
                  <span style="display:block;width:16px;height:16px;border-radius:5px;background:var(--line)"></span>
                </div>
              </div></div>''',
     "<b>Badge</b>가 정식 부품으로 있고, 점만 찍는 <b>작은 배지</b>와 숫자를 넣는 <b>큰 배지</b> 두 가지로 나뉩니다. 런처 아이콘에 붙는 점은 OS가 그립니다."),
  ]),
  plat_note="앱에서 \"배지 붙여 주세요\"라는 요청은 <b>앱 아이콘 위의 빨간 숫자</b>를 뜻하기도 합니다. 앱 아이콘 배지는 화면 안의 배지와 구현이 전혀 다르고 <b>푸시 알림과 묶여</b> 있어서 서버 쪽 작업이 따로 필요하므로, 어느 쪽을 말하는지 먼저 확인하세요.",
  siblings=siblings("badge"),
  related='''        <li><a href="../items/chip.html"><b>칩</b><em>5부</em></a></li>
        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>''',
)
