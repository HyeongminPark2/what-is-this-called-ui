# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def nrow(who, what, when, read=False, n=0):
    return ('<div style="display:flex;gap:5px;align-items:flex-start;padding:5px 0;border-top:1px solid var(--line);'
            + ('color:var(--fg-muted)' if read else '') + '">'
            '<span style="width:5px;height:5px;border-radius:50%;flex:none;margin-top:5px;background:'
            + ('transparent' if read else 'var(--accent)') + '"></span>'
            '<span style="flex:1;min-width:0;font-size:9px"><b>' + who + '</b> ' + what
            + ('<b> · ' + str(n) + '건</b>' if n > 1 else '') + '</span>'
            '<span style="font-size:8px;color:var(--fg-muted);white-space:nowrap">' + when + '</span></div>')

def box(inner, badge=None, w="152px", note="", warn=False):
    b = ('<span style="display:inline-grid;place-items:center;min-width:14px;height:14px;padding:0 4px;'
         'border-radius:999px;background:var(--danger);color:#fff;font-size:8px;font-weight:700">' + str(badge) + '</span>') if badge is not None else ''
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">'
            '<div style="padding:5px 8px;border-bottom:1px solid var(--line);background:var(--bg);font-size:9px;font-weight:700;'
            'display:flex;align-items:center;gap:5px">알림 ' + b + '</div>'
            '<div style="padding:2px 8px 6px">' + inner + '</div></div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">배지 — 안 읽은 수. 센 기준이 화면과 같아야 한다</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3), 6, "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">누른 것만 읽음 — 열었다고 전부 읽음으로 치지 않는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">같은 것끼리 묶는다 — 다섯 줄이 한 줄로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">모두 읽음 — 사용자가 직접 고르는 길</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">기기 사이에 읽음 상태가 안 맞으면 배지가 유령이 된다</div>
                </div>
              </div>'''

D = dict(
  slug="notifications", ko="알림 센터", en="Notification center",
  desc="놓친 것을 따라잡는 화면. 읽음 처리 시점, 묶기, 배지 숫자 맞추기.",
  lede="놓친 것을 <b>따라잡는</b> 화면. 어려운 쪽은 목록이 아니라 <b>언제 읽음으로 칠지</b>입니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>열면 전부 읽음</b>으로 바꿔 보세요 — 배지는 0이 되지만 <b>무엇을 봤는지는 모른 채</b>입니다.
          목록을 훑다 닫으면 다시 찾을 길이 없습니다.<br>
          <b>누른 것만 읽음</b>이 기본으로 맞습니다. <b>같은 것 묶기</b>를 끄면 한 곳에서 온 알림 다섯 개가
          다섯 줄을 차지합니다 — 배지 숫자가 크게 뛰는 흔한 이유입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "알림 센터, 알림함, 소식, 받은 알림"),
    ("영어", "notification center, inbox, activity feed"),
    ("같이 쓰는 말",
     "숫자가 붙은 동그라미가 <b>배지</b>(badge), 숫자 없이 점만 찍는 것이 <b>닷 배지</b>입니다. "
     "같은 것을 모아 한 줄로 만드는 것이 <b>그룹핑</b>·<b>코얼레싱</b>(coalescing), "
     "OS 가 띄우는 쪽은 <b>푸시 알림</b>이고 이 화면은 <b>앱 안의 기록</b>입니다. "
     "둘을 가려 부르면 대화가 훨씬 빨라집니다."),
    ("자주 잘못 부름",
     "<b>푸시 알림</b> — 푸시는 <b>보내는 길</b>이고, 알림 센터는 <b>쌓이는 곳</b>입니다. 푸시를 못 받아도 센터는 차 있어야 합니다.<br>"
     "<b>토스트</b> — <a href=\"../items/toast.html\">토스트</a>는 지나가고, 알림은 <b>남습니다</b>.<br>"
     "<b>메일함</b> — 답장이 오가면 메일함이고, 알림은 <b>한 방향</b>입니다."),
  ]),
  axes=ax("알림 센터"),
  oneline="<b>연 것과 본 것은 다릅니다.</b> 열었다고 전부 읽음으로 치면 배지는 깨끗해지고 사용자는 놓칩니다.",
  s4_title="상태", s4_hint="읽음을 언제 찍나",
  states=states([
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분'), 6),
     "안 읽음 있음", "<b>배지 숫자</b>와 점. 묶어도 <b>건수로</b> 센다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분'), 3),
     "누른 것만 읽음 ✓", "<b>나머지는 남는다.</b> 이어서 볼 수 있다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분', True), None,
         "152px", "열자마자 배지가 0 — 무엇을 봤는지는 모른다", True),
     "열면 전부 읽음 ✕", "<b>깨끗해 보이지만</b> 놓친다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금') + nrow('모란상회', '정산이 승인되었습니다', '1분')
         + nrow('모란상회', '정산이 승인되었습니다', '2분'), 6, "152px", "안 묶으면 같은 줄이 세 번", True),
     "안 묶었을 때", "<b>한 곳에서 온 것</b>이 목록을 채운다"),
    (box('<div style="padding:10px 0;text-align:center;font-size:8.5px;color:var(--fg-muted)">새 알림이 없습니다</div>', None),
     "빈 상태", "배지도 없다. <a href=\"../items/empty.html\">빈 상태</a>"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3), None, "152px", "다른 기기에서 읽었다"),
     "기기 사이", "<b>읽음이 안 맞으면</b> 배지가 유령이 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("배지", "안 읽은 수", "<b>세는 기준</b>이 화면과 같아야 한다"),
    ("안 읽음 표시", "점 · 바탕", "색만으로 가르지 않는다"),
    ("읽음 시점", "누른 것만", "<b>열었다고 전부</b>로 치지 않는다"),
    ("묶기", "같은 것끼리", "다섯 줄이 <b>한 줄 + 5건</b>이 된다"),
    ("모두 읽음", "직접 고르는 길", "사용자가 <b>스스로</b> 지우는 것은 괜찮다"),
    ("기기 사이", "읽음 맞추기", "안 맞으면 <b>사라지지 않는 배지</b>가 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>배지는 거짓말을 하기 쉽습니다.</b>
          화면은 묶어서 네 줄을 보여 주는데 배지는 여섯을 세고 있거나,
          다른 기기에서 읽었는데 이쪽 배지가 안 줄거나,
          푸시를 받은 수와 센터에 쌓인 수가 달라집니다.
          <b>센터에 쌓인 것만을 기준으로</b> 세고,
          읽음 상태는 <b>서버가 쥐고</b> 기기들이 그걸 따라가게 하는 것이
          결국 가장 적게 어긋납니다.</p>''',
  do=ul([
    "<b>놓쳐도 되는</b> 소식이 계속 생길 때",
    "푸시를 못 받는 사람에게도 <b>같은 내용</b>을 줘야 할 때",
    "한 곳에서 알림이 <b>몰려</b> 올 때 — 묶는다",
  ]),
  dont=ul([
    "열자마자 <b>전부 읽음</b> — 무엇을 봤는지 모른다",
    "안 묶기 — 한 곳이 목록을 <b>다 차지한다</b>",
    "중요한 것과 광고를 <b>같은 줄</b>에 — 전부 안 보게 된다",
    "배지만 띄우고 <b>눌러도 그 화면으로</b> 안 가기",
  ]),
  instead='지나가도 되는 것은 <a href="../items/toast.html">토스트</a>, 화면 안의 급한 알림은 인라인 얼럿, 설정은 <a href="settings.html">설정 화면</a>.',
  cases=cases([
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3), 6, "150px"),
     "묶어서 보여 주기", "<b>한 줄 + 건수.</b> 목록이 숨 쉰다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="display:flex;gap:4px;font-size:8.5px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:1px 7px">전체</span><span style="border:1px solid var(--line);border-radius:999px;padding:1px 7px">정산</span><span style="border:1px solid var(--line);border-radius:999px;padding:1px 7px">공지</span></div>
                <span style="font-size:8px;color:var(--fg-muted)">갈래로 나눠 두면 광고가 섞여도 덜 밉다</span>
              </div>''',
     "갈래 나누기", "중요한 것과 소식을 <b>갈라</b> 둔다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9px">알림을 누르면 <b>그 화면</b>으로</span>
                <span style="font-family:var(--mono);font-size:8.5px;color:var(--accent)">/settlements/2026-11-07</span>
              </div>''',
     "눌렀을 때", "<b>목록 맨 위</b>가 아니라 그 건으로 간다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="목록은 <code>&lt;ol&gt;</code>, 배지는 <b>읽히는 이름</b>과 함께 둡니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"알림, 안 읽음 6건"</span>&gt;
  🔔 &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;6&lt;/<span class="t">span</span>&gt;
&lt;/<span class="t">button</span>&gt;

&lt;<span class="t">ol</span> <span class="a">aria-label</span>=<span class="s">"알림 목록"</span>&gt;
  &lt;<span class="t">li</span>&gt;
    &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/settlements/2026-11-07"</span>&gt;
      &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"sr-only"</span>&gt;안 읽음&lt;/<span class="t">span</span>&gt;
      &lt;<span class="t">b</span>&gt;모란상회&lt;/<span class="t">b</span>&gt; 정산이 승인되었습니다 · 3건
      &lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-14T09:12"</span>&gt;방금&lt;/<span class="t">time</span>&gt;
    &lt;/<span class="t">a</span>&gt;
  &lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ol</span>&gt;

<span class="c">// 누른 것만 읽음으로</span>
link.addEventListener(<span class="s">'click'</span>, () =&gt; markRead(group.ids));''',
  keys=kbd([
    ("배지 숫자는 <code>aria-hidden</code>", "'6'만 읽히면 뜻이 없다. <b>버튼 이름에 '안 읽음 6건'</b>을 적는다"),
    ("안 읽음은 <b>글자로도</b>", "점과 색만으로는 안 읽힌다. <code>sr-only</code> 로 '안 읽음'을 넣는다"),
    ("<code>&lt;ol&gt;</code>", "순서가 뜻을 지닌다. 최신이 위라는 것도 정보다"),
    ("<code>&lt;time datetime&gt;</code>", "'방금'은 사람용, 속성은 기계용"),
    ("줄 전체가 링크", "<a href=\"touchtarget.html\">터치 타깃</a>이 저절로 커진다"),
    ("<code>role=\"status\"</code>", "새 알림이 오면 조용히 알린다. <code>alert</code>는 과하다"),
  ]),
  backend=rows([
    ("읽음은 서버가 쥔다", "기기마다 따로 세면 <b>한쪽에서 읽어도 다른 쪽 배지가</b> 안 줄어듭니다."),
    ("묶기는 서버에서", "화면마다 다르게 묶으면 배지와 목록이 어긋납니다. <b>묶은 결과를</b> 보냅니다."),
    ("푸시와 센터를 같이 만든다", "푸시만 보내면 못 받은 사람은 영영 모릅니다. <b>보낼 때 센터에도 쌓습니다</b>."),
    ("오래된 것은 지운다", "쌓이기만 하면 목록이 영원히 길어집니다. <b>보관 기간</b>을 정해 둡니다."),
    ("배지 수를 따로 주지 않는다", "목록과 다른 셈법으로 숫자를 만들면 반드시 어긋납니다. <b>같은 질의</b>에서 셉니다."),
  ]),
  plat_lede="<b>OS 가 쥔 배지</b>와 앱 안 배지가 또 다릅니다.",
  plats=plats([
    ("웹", "앱 안 배지",
     box(nrow('모란상회', '정산 승인', '방금'), 6, "112px"),
     "탭 제목이나 파비콘에 숫자를 넣기도 합니다. <b>OS 배지</b>는 설치형(PWA)에서만 됩니다."),
    ("iOS", "앱 아이콘 배지",
     '''              <div class="phone" role="img" aria-label="iOS 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:32px;width:18px;height:18px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:22px;top:28px;background:var(--danger);color:#fff;border-radius:999px;font-size:5px;padding:0 3px">6</span></div></div>''',
     "<b>앱 아이콘에 숫자</b>가 붙습니다. 서버가 그 숫자를 보내 줘야 해서 <b>읽음 맞추기</b>가 더 중요합니다."),
    ("안드로이드", "점 · 묶음 알림",
     '''              <div class="phone" role="img" aria-label="안드로이드 묶음 알림 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:3px;font-size:5px">모란상회 · 3건</div></div></div>''',
     "기본은 <b>점</b>이고 숫자는 길게 눌러야 보입니다. OS 가 <b>묶음 알림</b>을 거들어 줍니다."),
  ]),
  plat_note="\"안 읽은 알림 배지가 안 사라져요\"는 거의 늘 <b>세는 기준이 둘</b>이어서 생깁니다 — 화면은 묶어서 세고 배지는 건수로 세거나, 다른 기기에서 읽은 것이 안 돌아오거나. 만들 때 <b>'배지 숫자는 어디서 오나'</b>를 한 줄 적어 두면, 나중에 유령 배지를 쫓는 일이 없습니다.",
  siblings=siblings("notifications"),
  related='''        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
