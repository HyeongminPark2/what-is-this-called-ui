# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def dlg(title, sub, b1, b2, w="152px", note="", warn=False, os=True):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:7px;background:var(--surface);'
            'box-shadow:var(--e2);padding:7px;text-align:center;display:grid;gap:3px">'
            '<span style="font-size:9px;font-weight:700">' + title + '</span>'
            + ('<span style="font-size:8px;color:var(--fg-muted)">' + sub + '</span>' if sub else '')
            + '<div style="display:flex;border-top:1px solid var(--line);margin:3px -7px -7px">'
              '<span style="flex:1;padding:4px 0;font-size:8.5px;color:var(--accent);border-right:1px solid var(--line)">' + b1 + '</span>'
              '<span style="flex:1;padding:4px 0;font-size:8.5px;color:var(--accent);font-weight:700">' + b2 + '</span></div></div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

def box(inner, w="152px", note="", warn=False):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">'
            + inner + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">쓰려는 바로 그 순간에 — 첫 화면에서가 아니라</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + box('<span style="font-size:9px;font-weight:700">알림을 보내도 될까요?</span><span style="font-size:8px;color:var(--fg-muted)">정산이 들어온 순간에만 보냅니다</span>', "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">앞선 설명 — 여기서 거절해도 OS 창은 안 쓴다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">OS 창 — 한 번뿐이다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">거절당하면 설정으로 가는 길을 둔다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">권한 없이도 쓸 수 있는 길이 있어야 한다</div>
                </div>
              </div>'''

D = dict(
  slug="permission", ko="권한 요청", en="Permission request",
  desc="OS 권한을 묻는 순간. 한 번뿐인 기회를 아끼는 앞선 설명과 거절당한 뒤의 길.",
  lede="OS 권한 창은 <b>한 번뿐</b>입니다. 거절당하면 앱은 다시 띄울 수 없습니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>앞선 설명 띄우기</b>를 켜면 우리 화면에서 먼저 묻습니다. 여기서 '나중에'를 고르면
          <b>OS 창은 아직 쓰지 않은 채</b>로 남아, 다음에 다시 물어볼 수 있습니다.<br>
          끄고 거절해 본 뒤 다시 눌러 보세요 — <b>아무 일도 일어나지 않습니다.</b>
          그 한 번을 아끼는 것이 이 화면의 전부입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "권한 요청, 접근 허용, 퍼미션"),
    ("영어", "permission request, permission prompt, pre-permission"),
    ("같이 쓰는 말",
     "OS 창을 띄우기 전에 우리 화면에서 먼저 묻는 것을 "
     "<b>프리프롬프트</b>(pre-prompt)·<b>프라이밍</b>(priming)이라 합니다. "
     "웹에서는 <code>navigator.permissions.query()</code>로 지금 상태를 물어볼 수 있고, "
     "값은 <code>granted</code>·<code>denied</code>·<code>prompt</code> 셋입니다. "
     "사용자의 동작 없이 띄우지 못하게 막는 것을 <b>사용자 제스처 요구</b>라 합니다."),
    ("자주 잘못 부름",
     "<b>약관 동의</b> — 법적 동의이고, 권한은 <b>OS 가 쥔 기능</b>입니다. 전혀 다릅니다.<br>"
     "<b>로그인</b> — 누구인지 확인하는 것과 기기 기능을 쓰는 것은 다릅니다.<br>"
     "<b>설정</b> — <a href=\"settings.html\">설정</a>에서 끌 수는 있지만, 켜는 건 <b>OS 설정 앱</b>에서만 됩니다."),
  ]),
  axes=ax("권한 요청"),
  oneline="<b>쓰려는 그 순간에, 왜 필요한지 먼저 말하고 묻습니다.</b> 첫 화면에서 다섯 개를 몰아 묻는 것이 최악입니다.",
  s4_title="흐름", s4_hint="한 번뿐인 기회를 어떻게 쓰나",
  states=states([
    (box('<span style="font-size:9px;font-weight:700">정산 알림</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">새 정산이 들어오면 알려 드립니다</span>'
         '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:8.5px">알림 받기</span>',
         "152px", "쓰려는 그 순간에"),
     "묻기 전", "<b>왜 필요한지</b>가 보이는 자리에서"),
    (dlg('알림을 보내도 될까요?', '정산이 들어온 순간에만 보냅니다', '나중에', '좋아요', "152px", "앞선 설명 — 우리 화면"),
     "앞선 설명", "여기서 거절해도 <b>OS 창은 그대로 남는다</b>"),
    (dlg('‘정산관리’에서 알림을 보내도록 허용하시겠습니까?', '', '허용 안 함', '허용', "152px", "OS 창 — 한 번뿐"),
     "OS 창", "모양도 문구도 <b>바꿀 수 없다</b>"),
    (box('<span style="font-size:9px;color:var(--accent);font-weight:700">알림을 받습니다</span>', "152px", "granted"),
     "허용됨", "쓰면 된다"),
    (box('<span style="font-size:9px;color:var(--danger)">알림이 꺼져 있습니다</span>'
         '<span style="justify-self:start;border:1px solid var(--line);border-radius:4px;padding:2px 7px;font-size:8.5px">기기 설정에서 켜기 →</span>',
         "152px", "denied — 설정으로 보내는 수밖에"),
     "거절됨", "<b>앱이 할 수 있는 건 여기까지</b>"),
    (box('<span style="font-size:9px;font-weight:700">알림 없이도 됩니다</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">목록에 새 표시로 보여 드려요</span>', "152px", "권한 없이도 쓸 수 있게"),
     "없어도 쓰이게", "<b>그 기능만</b> 못 쓰고 나머지는 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("묻는 때", "쓰려는 순간", "첫 화면이 아니라 <b>그 기능을 누를 때</b>"),
    ("앞선 설명", "우리 화면", "<b>왜 필요한지</b>를 우리 말로 적는다"),
    ("아낀 기회", "나중에", "여기서 거절해도 <b>OS 창은 안 쓴다</b>"),
    ("OS 창", "한 번뿐", "문구도 모양도 못 바꾼다. <b>이게 전부</b>다"),
    ("거절 뒤", "설정으로", "다시 못 띄운다. <b>길만 알려 줄</b> 수 있다"),
    ("없을 때", "쓸 수 있게", "권한이 없어도 <b>그 기능만</b> 빠지게 만든다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>앞선 설명이 더 묻는 일이라 나빠 보이지만 반대입니다.</b>
          OS 창은 한 번뿐이라 '지금 쓸지 말지'를 판돈으로 겁니다.
          앞선 설명에서 '나중에'를 고른 사람은 <b>OS 창을 아직 안 쓴 사람</b>이라,
          그 기능이 정말 필요해진 순간에 다시 물어볼 수 있습니다.
          반대로 바로 띄웠다 거절당하면, 나중에 그 사람이 마음을 바꿔도
          <b>우리는 아무것도 할 수 없습니다</b> — 설정 앱으로 가는 길을 알려 주는 것이 전부입니다.</p>''',
  do=ul([
    "<b>그 기능을 쓰려는 순간</b>에 묻기",
    "묻기 전에 <b>왜 필요한지</b> 한 줄",
    "거절당해도 <b>나머지는 쓰이게</b> 만들기",
  ]),
  dont=ul([
    "첫 화면에서 <b>몰아 묻기</b> — 다 거절당한다",
    "앞선 설명 없이 바로 OS 창 — <b>한 번뿐인 기회</b>를 버린다",
    "거절한 사람에게 <b>계속 조르기</b>",
    "권한이 없으면 <b>앱을 못 쓰게</b> 막기",
  ]),
  instead='첫 설정 흐름이면 <a href="onboarding.html">온보딩</a> 안에서, 꺼져 있다고 알릴 때는 <a href="../items/empty.html">빈 상태</a>, 설명만이면 <a href="../items/popover.html">팝오버</a>.',
  cases=cases([
    (box('<span style="font-size:9px;font-weight:700">가까운 가맹점 보기</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">위치를 알면 가까운 순으로 보여 드려요</span>'
         '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:8.5px">내 위치 쓰기</span>', "150px"),
     "위치", "<b>누르는 순간</b>에 묻는다. 첫 화면이 아니라"),
    (box('<span style="font-size:9px;font-weight:700">영수증 찍기</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">사진은 기기에만 저장됩니다</span>', "150px"),
     "카메라", "<b>어디에 저장되는지</b>까지 적으면 허용률이 오른다"),
    (box('<span style="font-size:9px;color:var(--fg-muted)">알림이 꺼져 있어요</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">대신 목록에 새 표시로 보여 드립니다</span>', "150px"),
     "거절당한 뒤", "<b>조르지 말고</b> 다른 길을 준다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 요청의 계약서",
  code_lede="먼저 상태를 물어보고, 앞선 설명을 거친 뒤에만 OS 창을 씁니다.",
  code='''<span class="c">// 지금 상태부터 물어본다 — 이미 결정났을 수 있다</span>
<span class="k">const</span> st = (<span class="k">await</span> navigator.permissions.query({ name: <span class="s">'notifications'</span> })).state;

<span class="k">if</span> (st === <span class="s">'denied'</span>) {
  showSettingsHint();          <span class="c">// 다시 못 띄운다. 길만 알려 준다</span>
} <span class="k">else if</span> (st === <span class="s">'granted'</span>) {
  subscribe();
} <span class="k">else</span> {
  <span class="k">const</span> wants = <span class="k">await</span> showPrePrompt();   <span class="c">// 우리 화면에서 먼저</span>
  <span class="k">if</span> (!wants) <span class="k">return</span>;                    <span class="c">// OS 창은 아직 안 썼다</span>
  <span class="k">const</span> res = <span class="k">await</span> Notification.requestPermission();
  <span class="k">if</span> (res === <span class="s">'granted'</span>) subscribe();
  <span class="k">else</span> showSettingsHint();
}''',
  keys=kbd([
    ("사용자 동작 안에서만", "클릭 핸들러 밖에서 부르면 <b>브라우저가 막는다</b>. 페이지 로드 직후는 안 된다"),
    ("<code>permissions.query</code>", "<code>granted</code>·<code>denied</code>·<code>prompt</code>. <b>묻기 전에 확인</b>한다"),
    ("앞선 설명은 <a href=\"../items/dialog.html\">다이얼로그</a>", "초점을 가두고 <kbd>Esc</kbd>로 닫히게. <b>'나중에'가 기본</b>"),
    ("OS 창은 못 꾸민다", "문구·버튼·순서 전부 OS 것이다. <b>우리가 할 수 있는 건 앞선 설명뿐</b>"),
    ("거절 뒤 안내", "'설정 › 알림'처럼 <b>경로를 적어</b> 준다. 브라우저는 자동으로 못 열어 준다"),
    ("<code>role=\"status\"</code>", "권한 상태가 바뀌면 알린다. 아이콘만 바뀌면 모른다"),
  ]),
  backend=rows([
    ("서버는 권한을 모른다", "허용 여부는 <b>기기에만</b> 있습니다. 서버는 구독 정보가 들어왔는지로만 짐작합니다."),
    ("구독은 끊길 수 있다", "사용자가 나중에 설정에서 끄면 <b>조용히</b> 실패합니다. 발송 실패를 보고 구독을 지워야 합니다."),
    ("대체 길을 둔다", "알림을 못 보내는 사람에게는 <b>메일이나 화면 안 표시</b>로 같은 정보를 줍니다."),
    ("허용률을 기록한다", "앞선 설명을 거친 쪽과 아닌 쪽의 <b>허용률 차이</b>를 재 보면 이 설계가 값을 하는지 알 수 있습니다."),
  ]),
  plat_lede="<b>한 번뿐</b>이라는 성질은 셋 모두 같습니다.",
  plats=plats([
    ("웹", "Permissions API",
     dlg('알림을 허용하시겠습니까?', '', '차단', '허용', "112px"),
     "브라우저 창이 뜹니다. 요즘은 <b>사용자 동작 없이는</b> 아예 못 띄우게 막혀 있습니다."),
    ("iOS", "한 번뿐 · 설정에서만",
     '''              <div class="phone" role="img" aria-label="iOS 권한 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:6px;box-shadow:var(--e2);padding:4px;text-align:center;font-size:5px">알림을 보내도록<br>허용하시겠습니까?</div></div></div>''',
     "알림은 <b>딱 한 번</b>만 물을 수 있습니다. 위치는 '앱을 쓰는 동안만' 같은 중간 선택지가 있습니다."),
    ("안드로이드", "두 번 거절하면 영구",
     '''              <div class="phone" role="img" aria-label="안드로이드 권한 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:6px;box-shadow:var(--e2);padding:4px;text-align:center;font-size:5px">알림을 보내도록<br>허용하시겠습니까?</div></div></div>''',
     "거절해도 한 번 더 물을 수 있지만 <b>두 번 거절하면 영구</b>입니다. 13부터는 알림도 권한입니다."),
  ]),
  plat_note="\"첫 화면에서 권한 다 받아 놓죠\"는 가장 비싸게 치르는 결정입니다. 받아 둘 때는 <b>다섯 개 중 넷을 잃고</b>, 나중에 그 기능이 필요해져도 되돌릴 길이 없습니다. <b>쓰려는 순간에 하나씩</b>으로 바꾸는 것만으로 허용률이 크게 달라지고, 그 차이는 재서 보여 줄 수 있습니다.",
  siblings=siblings("permission"),
  related='''        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
