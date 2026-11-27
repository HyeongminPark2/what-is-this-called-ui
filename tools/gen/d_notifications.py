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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">배지의 안 읽은 수는 목록과 같은 기준으로 셈</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3), 6, "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">열었다고 전부가 아니라 누른 것만 읽음 처리</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">같은 알림 다섯 줄을 한 줄로 묶음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">모두 읽음은 사용자가 직접 고를 때만</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">기기 사이에 읽음 상태가 안 맞으면 배지가 남음</div>
                </div>
              </div>'''

D = dict(
  slug="notifications", ko="알림 센터", en="Notification center",
  desc="놓친 소식을 따라잡는 화면입니다. 언제 읽음으로 처리할지, 같은 알림을 어떻게 묶을지, 배지 숫자를 목록과 어떻게 맞출지 다룹니다.",
  lede="알림 센터는 사용자가 놓친 소식을 <b>따라잡는</b> 화면입니다. 목록을 그리는 일보다 <b>언제 읽음으로 처리할지</b> 정하는 일이 더 까다롭습니다.",
  axes_lede="화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>열면 전부 읽음</b>으로 바꿔 보세요. 배지는 0이 되지만 사용자가 <b>실제로 무엇을 봤는지는 알 수 없습니다</b>.
          목록을 훑다가 닫으면 안 본 알림도 읽음으로 바뀌어서 나중에 다시 찾을 방법이 없습니다.<br>
          그래서 기본값은 <b>누른 것만 읽음</b>이 맞습니다. <b>같은 알림 묶기</b>를 끄면 한 곳에서 온 알림 다섯 개가
          다섯 줄을 차지하는데, 배지 숫자가 갑자기 크게 늘어나는 흔한 이유가 이것입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "알림 센터, 알림함, 소식, 받은 알림"),
    ("영어", "notification center, inbox, activity feed"),
    ("같이 쓰는 말",
     "숫자가 붙은 동그라미를 <b>배지</b>(badge), 숫자 없이 점만 찍는 것을 <b>닷 배지</b>라고 합니다. "
     "같은 알림을 모아 한 줄로 만드는 것은 <b>그룹핑</b>·<b>코얼레싱</b>(coalescing)이라고 합니다. "
     "OS가 띄우는 것은 <b>푸시 알림</b>이고, 이 화면은 <b>앱 안에 남는 기록</b>입니다. "
     "둘을 구별해서 부르면 회의에서 말이 엇갈리는 일이 훨씬 줄어듭니다."),
    ("자주 잘못 부르는 이름",
     "<b>푸시 알림</b> — 푸시는 알림을 <b>보내는 수단</b>이고, 알림 센터는 알림이 <b>쌓이는 곳</b>입니다. 사용자가 푸시를 받지 못했더라도 센터에는 알림이 쌓여 있어야 합니다.<br>"
     "<b>토스트</b> — <a href=\"../items/toast.html\">토스트</a>는 잠깐 떴다가 사라지지만, 알림 센터의 알림은 <b>남아 있습니다</b>.<br>"
     "<b>메일함</b> — 답장이 오가면 메일함이고, 알림은 <b>한 방향</b>으로만 전달됩니다."),
  ]),
  axes=ax("알림 센터"),
  oneline="<b>알림 센터를 연 것과 알림을 본 것은 다릅니다.</b> 열었다고 전부 읽음으로 처리하면 배지는 사라지지만, 사용자는 안 본 알림을 놓치게 됩니다.",
  do_title="알림 센터를 두면 좋은 경우",
  dont_title="알림 센터를 잘못 만드는 경우",
  instead_title="알림 센터 말고 다른 곳에서 다룰 것",
  s4_title="알림 센터의 상태", s4_hint="언제 읽음으로 처리하는가",
  states=states([
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분'), 6),
     "안 읽은 알림이 있을 때", "<b>배지 숫자</b>와 점으로 표시합니다. 묶어서 보여 줘도 배지는 <b>건수로</b> 셉니다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분'), 3),
     "누른 것만 읽음으로 처리할 때 ✓", "<b>누르지 않은 알림은 안 읽음으로 남아서</b> 이어서 볼 수 있습니다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3) + nrow('한빛아웃도어', '새 주문 12건', '10분', True), None,
         "152px", "열자마자 배지가 0, 무엇을 봤는지 모름", True),
     "열자마자 전부 읽음으로 처리할 때 ✕", "배지가 사라져 <b>정리된 것처럼 보이지만</b> 안 본 알림을 놓칩니다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금') + nrow('모란상회', '정산이 승인되었습니다', '1분')
         + nrow('모란상회', '정산이 승인되었습니다', '2분'), 6, "152px", "안 묶으면 같은 줄이 세 번", True),
     "같은 알림을 묶지 않았을 때", "<b>한 곳에서 온 알림</b>이 목록을 가득 채웁니다"),
    (box('<div style="padding:10px 0;text-align:center;font-size:8.5px;color:var(--fg-muted)">새 알림이 없습니다</div>', None),
     "새 알림이 없을 때", "배지도 표시하지 않습니다. 화면은 <a href=\"../items/empty.html\">빈 상태</a>로 보여 줍니다"),
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', True, 3), None, "152px", "다른 기기에서 읽음"),
     "다른 기기에서 읽었을 때", "기기 사이에 <b>읽음 상태가 맞지 않으면</b> 다 읽었는데도 배지가 남습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("배지", "안 읽은 수", "배지가 <b>세는 기준</b>은 목록 화면과 같아야 합니다"),
    ("안 읽음 표시", "점 · 바탕", "읽음과 안 읽음을 색만으로 구별하지 않습니다"),
    ("읽음 시점", "누른 것만", "센터를 <b>열었다고 전부</b> 읽음으로 처리하지 않습니다"),
    ("묶기", "같은 것끼리", "같은 알림 다섯 줄을 <b>한 줄 + 5건</b>으로 묶습니다"),
    ("모두 읽음", "사용자가 직접 고를 때", "사용자가 <b>스스로</b> 골라서 한꺼번에 읽음으로 바꾸는 것은 괜찮습니다"),
    ("기기 사이 동기화", "읽음 맞추기", "기기 사이에 읽음 상태가 맞지 않으면 <b>사라지지 않는 배지</b>가 생깁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>배지 숫자는 실제와 쉽게 어긋납니다.</b>
          화면은 알림을 묶어서 네 줄을 보여 주는데 배지는 여섯을 세고 있거나,
          다른 기기에서 읽었는데 이쪽 배지가 줄지 않거나,
          푸시로 받은 수와 센터에 쌓인 수가 달라지는 일이 흔합니다.
          그래서 배지는 <b>센터에 쌓인 알림만을 기준으로</b> 세고,
          읽음 상태는 <b>서버에 두고</b> 기기들이 서버의 상태를 따라가게 합니다.
          이렇게 하는 편이 숫자가 가장 적게 어긋납니다.</p>''',
  do=ul([
    "<b>놓쳐도 되는</b> 소식이 계속 생길 때",
    "푸시를 받지 않는 사람에게도 <b>같은 내용</b>을 전해야 할 때",
    "한 곳에서 알림이 <b>몰려</b> 올 때. 같은 알림을 한 줄로 묶습니다",
  ]),
  dont=ul([
    "센터를 열자마자 <b>전부 읽음</b>으로 처리할 때. 사용자가 무엇을 봤는지 알 수 없습니다",
    "같은 알림을 묶지 않을 때. 한 곳에서 온 알림이 목록을 <b>다 차지합니다</b>",
    "중요한 알림과 광고를 <b>같은 목록</b>에 섞을 때. 사용자가 알림 전체를 보지 않게 됩니다",
    "배지만 띄우고, 알림을 <b>눌러도 해당 화면으로</b> 가지 않을 때",
  ]),
  instead='잠깐 보여 주고 지나가도 되는 소식은 <a href="../items/toast.html">토스트</a>로 띄우고, 지금 보는 화면 안의 급한 알림은 인라인 얼럿으로 보여 줍니다. 어떤 알림을 받을지 정하는 일은 <a href="settings.html">설정 화면</a>에서 다룹니다.',
  cases=cases([
    (box(nrow('모란상회', '정산이 승인되었습니다', '방금', False, 3), 6, "150px"),
     "묶어서 보여 주기", "<b>한 줄에 건수를 붙여</b> 보여 주면 목록이 짧아져 훑어보기 쉽습니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="display:flex;gap:4px;font-size:8.5px"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:1px 7px">전체</span><span style="border:1px solid var(--line);border-radius:999px;padding:1px 7px">정산</span><span style="border:1px solid var(--line);border-radius:999px;padding:1px 7px">공지</span></div>
                <span style="font-size:8px;color:var(--fg-muted)">갈래로 나눠 두면 광고가 섞여도 덜 밉다</span>
              </div>''',
     "중요한 알림과 소식 나눠 두기", "중요한 알림과 일반 소식을 <b>나눠</b> 둡니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <span style="font-size:9px">알림을 누르면 <b>그 화면</b>으로</span>
                <span style="font-family:var(--mono);font-size:8.5px;color:var(--accent)">/settlements/2026-11-07</span>
              </div>''',
     "누르면 해당 건으로 바로 가기", "<b>목록 맨 위</b>가 아니라 그 알림이 가리키는 건으로 바로 갑니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="목록은 <code>&lt;ol&gt;</code>로 적고, 배지는 스크린 리더가 <b>읽을 수 있는 이름</b>과 함께 둡니다.",
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
    ("배지 숫자에 <code>aria-hidden</code> 달기", "'6'만 읽히면 무슨 숫자인지 알 수 없으므로 <b>버튼 이름에 '안 읽음 6건'</b>을 적습니다"),
    ("안 읽음을 <b>글자로도</b> 알리기", "점과 색만으로는 스크린 리더가 읽지 못하므로 <code>sr-only</code>로 '안 읽음'을 넣습니다"),
    ("<code>&lt;ol&gt;</code>", "알림은 순서에 뜻이 있어서 순서 있는 목록으로 적습니다. 최신 알림이 위에 있다는 것도 정보입니다"),
    ("<code>&lt;time datetime&gt;</code>", "'방금'은 사람이 읽는 글자이고, <code>datetime</code> 속성은 기계가 읽는 값입니다"),
    ("줄 전체를 링크로 만들기", "줄 전체를 링크로 만들면 <a href=\"touchtarget.html\">터치 타깃</a>이 따로 손대지 않아도 커집니다"),
    ("<code>role=\"status\"</code>", "새 알림이 오면 읽던 것을 끊지 않고 알립니다. 새 알림은 급한 내용이 아니라서 <code>alert</code>는 지나칩니다"),
  ]),
  backend=rows([
    ("읽음 상태는 서버에 두기", "기기마다 읽음 상태를 따로 세면 <b>한쪽에서 읽어도 다른 쪽 배지가</b> 줄어들지 않습니다. 그래서 읽음 상태는 서버에 둡니다."),
    ("알림 묶기는 서버에서 하기", "화면마다 다르게 묶으면 배지와 목록이 어긋납니다. 그래서 서버가 <b>묶은 결과를</b> 내려보냅니다."),
    ("푸시를 보낼 때 센터에도 쌓기", "푸시만 보내면 푸시를 받지 못한 사람은 그 소식을 끝내 모릅니다. 그래서 푸시를 <b>보낼 때 센터에도 쌓습니다</b>."),
    ("보관 기간이 지난 알림 지우기", "알림이 쌓이기만 하면 목록이 끝없이 길어집니다. 그래서 <b>보관 기간</b>을 정해 두고 지난 알림은 지웁니다."),
    ("배지 수를 목록과 같은 질의로 세기", "목록과 다른 방식으로 배지 숫자를 계산하면 언젠가는 반드시 어긋납니다. 그래서 목록과 <b>같은 질의</b>로 셉니다."),
  ]),
  plat_lede="<b>OS가 표시하는 배지</b>와 앱 안의 배지는 또 따로 관리됩니다.",
  plats=plats([
    ("웹", "앱 안 배지",
     box(nrow('모란상회', '정산 승인', '방금'), 6, "112px"),
     "탭 제목이나 파비콘에 숫자를 넣기도 합니다. <b>OS 배지</b>는 설치형 웹 앱(PWA)에서만 쓸 수 있습니다."),
    ("iOS", "앱 아이콘 배지",
     '''              <div class="phone" role="img" aria-label="iOS 배지 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;top:32px;width:18px;height:18px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:22px;top:28px;background:var(--danger);color:#fff;border-radius:999px;font-size:5px;padding:0 3px">6</span></div></div>''',
     "<b>앱 아이콘에 숫자</b>가 붙습니다. 서버가 그 숫자를 보내 줘야 하므로 기기 사이의 <b>읽음 맞추기</b>가 더 중요합니다."),
    ("안드로이드", "점 · 묶음 알림",
     '''              <div class="phone" role="img" aria-label="안드로이드 묶음 알림 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:3px;font-size:5px">모란상회 · 3건</div></div></div>''',
     "기본으로는 <b>점</b>만 찍히고, 숫자는 아이콘을 길게 눌러야 보입니다. <b>묶음 알림</b>은 OS가 기능으로 지원합니다."),
  ]),
  plat_note="\"안 읽은 알림 배지가 안 사라져요\"라는 문제는 거의 언제나 <b>세는 기준이 두 가지</b>여서 생깁니다. 예를 들어 화면은 묶어서 세는데 배지는 건수로 세거나, 다른 기기에서 읽은 기록이 이쪽에 전달되지 않는 경우입니다. 처음 만들 때 <b>'배지 숫자는 어디서 오나'</b>를 한 줄 적어 두면, 나중에 사라지지 않는 배지의 원인을 찾아 헤매는 일이 없습니다.",
  siblings=siblings("notifications"),
  related='''        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>6부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
