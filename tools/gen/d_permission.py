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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">첫 화면이 아니라 기능을 쓰려는 순간에 물음</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + box('<span style="font-size:9px;font-weight:700">알림을 보내도 될까요?</span><span style="font-size:8px;color:var(--fg-muted)">정산이 들어온 순간에만 보냅니다</span>', "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">앞선 설명에서 거절하면 OS 창은 아껴 둠</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">OS 창은 한 번만 뜸</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">거절당하면 설정으로 가는 길을 둠</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">권한 없이도 앱을 쓸 수 있어야 함</div>
                </div>
              </div>'''

D = dict(
  slug="permission", ko="권한 요청", en="Permission request",
  desc="OS 권한을 묻는 순간을 다룹니다. 한 번뿐인 OS 창을 아껴 두는 앞선 설명과, 거절당한 뒤 사용자에게 보여 줄 길을 설명합니다.",
  lede="OS 권한 창은 <b>한 번만</b> 띄울 수 있습니다. 사용자가 거절하면 앱이 그 창을 다시 띄울 방법이 없습니다.",
  axes_lede="화면 단위 패턴은 사용자가 <b>끝내야 하는 일</b> 하나로 나눕니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>앞선 설명 띄우기</b>를 켜면 OS 창을 띄우기 전에 우리 화면에서 먼저 묻습니다. 여기서 '나중에'를 고르면
          <b>OS 창은 아직 쓰지 않은 채</b>로 남기 때문에, 다음에 다시 물어볼 수 있습니다.<br>
          반대로 앞선 설명을 끄고 OS 창에서 거절한 뒤 다시 눌러 보면 <b>아무 일도 일어나지 않습니다.</b>
          권한 요청 화면은 결국 이 한 번의 OS 창을 언제 쓸지 정하는 일입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "권한 요청, 접근 허용, 퍼미션"),
    ("영어", "permission request, permission prompt, pre-permission"),
    ("같이 쓰는 말",
     "OS 창을 띄우기 전에 우리 화면에서 먼저 묻는 것을 "
     "<b>프리프롬프트</b>(pre-prompt)·<b>프라이밍</b>(priming)이라고 합니다. "
     "웹에서는 <code>navigator.permissions.query()</code>로 지금 권한 상태를 확인할 수 있고, "
     "돌아오는 값은 <code>granted</code>·<code>denied</code>·<code>prompt</code> 세 가지입니다. "
     "클릭 같은 사용자 동작 없이는 권한 창을 띄우지 못하게 막는 규칙을 <b>사용자 제스처 요구</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>약관 동의</b> — 약관 동의는 법적인 동의이고, 권한은 <b>OS가 관리하는 기기 기능</b>을 쓰도록 허락받는 것이라 전혀 다릅니다.<br>"
     "<b>로그인</b> — 누구인지 확인하는 일과 기기 기능을 쓰는 일은 서로 다릅니다.<br>"
     "<b>설정</b> — 앱의 <a href=\"settings.html\">설정</a>에서 기능을 끌 수는 있지만, 한 번 거절한 권한을 다시 켜는 일은 <b>OS 설정 앱</b>에서만 됩니다."),
  ]),
  axes=ax("권한 요청"),
  oneline="권한은 <b>사용자가 그 기능을 쓰려는 순간에, 왜 필요한지 먼저 말한 뒤</b> 묻습니다. 첫 화면에서 권한 다섯 개를 한꺼번에 묻는 것이 가장 나쁜 방식입니다.",
  do_title="권한을 물어도 되는 때",
  dont_title="권한을 이렇게 물으면 안 되는 경우",
  instead_title="상황에 따라 함께 볼 항목",
  s4_title="권한을 묻는 흐름", s4_hint="한 번뿐인 OS 창을 언제 쓰는가",
  states=states([
    (box('<span style="font-size:9px;font-weight:700">정산 알림</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">새 정산이 들어오면 알려 드립니다</span>'
         '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:8.5px">알림 받기</span>',
         "152px", "기능을 쓰려는 순간에 물음"),
     "권한을 묻기 전", "<b>왜 필요한지</b>가 화면에서 드러나는 자리에서 묻습니다"),
    (dlg('알림을 보내도 될까요?', '정산이 들어온 순간에만 보냅니다', '나중에', '좋아요', "152px", "우리 화면에 띄운 앞선 설명"),
     "앞선 설명을 띄웠을 때", "여기서 거절해도 <b>OS 창은 쓰지 않은 채로 남습니다</b>"),
    (dlg('‘정산관리’에서 알림을 보내도록 허용하시겠습니까?', '', '허용 안 함', '허용', "152px", "한 번만 뜨는 OS 창"),
     "OS 창이 떴을 때", "모양도 문구도 앱이 <b>바꿀 수 없습니다</b>"),
    (box('<span style="font-size:9px;color:var(--accent);font-weight:700">알림을 받습니다</span>', "152px", "granted"),
     "사용자가 허용했을 때", "기능을 그대로 쓰면 됩니다"),
    (box('<span style="font-size:9px;color:var(--danger)">알림이 꺼져 있습니다</span>'
         '<span style="justify-self:start;border:1px solid var(--line);border-radius:4px;padding:2px 7px;font-size:8.5px">기기 설정에서 켜기 →</span>',
         "152px", "denied, 설정으로 안내할 수밖에 없음"),
     "사용자가 거절했을 때", "앱은 기기 설정으로 가는 길을 알려 주는 것 <b>말고는 할 수 있는 일이 없습니다</b>"),
    (box('<span style="font-size:9px;font-weight:700">알림 없이도 됩니다</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">목록에 새 표시로 보여 드려요</span>', "152px", "권한 없이도 쓸 수 있게"),
     "권한 없이도 쓰게 할 때", "권한이 필요한 <b>그 기능만</b> 빠지고 나머지는 쓸 수 있게 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("묻는 시점", "쓰려는 순간", "첫 화면이 아니라 사용자가 <b>그 기능을 누를 때</b> 묻습니다"),
    ("앞선 설명", "우리 화면", "권한이 <b>왜 필요한지</b> 우리 화면에서 우리 말로 적습니다"),
    ("나중에 버튼", "OS 창을 아껴 둠", "여기서 거절하면 <b>OS 창을 쓰지 않고</b> 아껴 둡니다"),
    ("OS 창", "한 번뿐", "문구도 모양도 바꿀 수 없고, <b>한 번 거절되면 다시 띄울 수 없습니다</b>"),
    ("거절된 뒤 안내", "설정 앱으로", "OS 창을 다시 띄울 수 없으니 설정으로 가는 <b>길만 알려 줄</b> 수 있습니다"),
    ("권한이 없을 때", "그래도 쓸 수 있게", "권한이 없어도 <b>그 기능만</b> 빠지고 앱은 쓸 수 있게 만듭니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>앞선 설명은 사용자에게 한 번 더 묻는 일이라 번거로워 보이지만, 실제로는 권한을 받을 기회를 늘립니다.</b>
          OS 창은 한 번만 띄울 수 있어서, 사용자가 그 창에서 거절하면 그 기능을 다시 요청할 기회가 사라집니다.
          반면 앞선 설명에서 '나중에'를 고른 사람에게는 <b>OS 창을 아직 띄우지 않았으므로</b>,
          그 기능이 정말 필요해진 순간에 다시 물어볼 수 있습니다.
          OS 창을 바로 띄웠다가 거절당하면 나중에 사용자가 마음을 바꿔도
          <b>앱이 할 수 있는 일이 없고</b>, 설정 앱으로 가는 길을 알려 주는 것밖에 남지 않습니다.</p>''',
  do=ul([
    "사용자가 <b>그 기능을 쓰려는 순간</b>일 때",
    "묻기 전에 <b>왜 필요한지</b> 한 줄로 설명할 수 있을 때",
    "거절당해도 <b>나머지 기능은 쓸 수 있게</b> 만들 수 있을 때",
  ]),
  dont=ul([
    "첫 화면에서 권한을 <b>몰아서 물을 때</b>. 대부분 거절당합니다",
    "앞선 설명 없이 바로 OS 창을 띄울 때. <b>한 번뿐인 기회</b>를 잃습니다",
    "거절한 사람에게 <b>계속 다시 요청할</b> 때",
    "권한이 없으면 <b>앱을 아예 못 쓰게</b> 막을 때",
  ]),
  instead='처음 설정하는 흐름에서 묻는다면 <a href="onboarding.html">온보딩</a> 안에 앞선 설명을 넣습니다. 권한이 꺼져 있다고 알릴 때는 <a href="../items/empty.html">빈 상태</a>를, 권한 없이 설명만 하면 될 때는 <a href="../items/popover.html">팝오버</a>를 씁니다.',
  cases=cases([
    (box('<span style="font-size:9px;font-weight:700">가까운 가맹점 보기</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">위치를 알면 가까운 순으로 보여 드려요</span>'
         '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:8.5px">내 위치 쓰기</span>', "150px"),
     "위치 권한 묻기", "첫 화면이 아니라 사용자가 버튼을 <b>누르는 순간</b>에 묻습니다"),
    (box('<span style="font-size:9px;font-weight:700">영수증 찍기</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">사진은 기기에만 저장됩니다</span>', "150px"),
     "카메라 권한 묻기", "사진이 <b>어디에 저장되는지</b>까지 적으면 허용률이 오릅니다"),
    (box('<span style="font-size:9px;color:var(--fg-muted)">알림이 꺼져 있어요</span>'
         '<span style="font-size:8px;color:var(--fg-muted)">대신 목록에 새 표시로 보여 드립니다</span>', "150px"),
     "거절당한 뒤 다른 방법 보여 주기", "다시 <b>요청하지 않고</b>, 권한 없이 같은 정보를 얻을 다른 방법을 보여 줍니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="먼저 지금 권한 상태를 확인하고, 앞선 설명을 거친 뒤에만 OS 창을 띄웁니다.",
  code='''<span class="c">// 사용자가 이미 결정했을 수 있으니 지금 상태부터 확인한다</span>
<span class="k">const</span> st = (<span class="k">await</span> navigator.permissions.query({ name: <span class="s">'notifications'</span> })).state;

<span class="k">if</span> (st === <span class="s">'denied'</span>) {
  showSettingsHint();          <span class="c">// OS 창은 다시 못 띄우니 설정으로 가는 길만 알려 준다</span>
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
    ("사용자 동작 안에서만 부르기", "클릭 핸들러 밖에서 부르면 <b>브라우저가 막습니다</b>. 그래서 페이지를 불러오자마자 띄울 수는 없습니다"),
    ("<code>permissions.query</code>", "<code>granted</code>·<code>denied</code>·<code>prompt</code> 가운데 어느 상태인지 <b>묻기 전에 확인</b>합니다"),
    ("앞선 설명은 <a href=\"../items/dialog.html\">다이얼로그</a>로 만들기", "초점을 다이얼로그 안에 가두고 <kbd>Esc</kbd>로 닫히게 합니다. <b>기본 선택은 '나중에'</b>로 둡니다"),
    ("OS 창은 꾸밀 수 없음", "문구·버튼·순서를 모두 OS가 정합니다. 앱이 손댈 수 있는 것은 <b>앞선 설명뿐</b>입니다"),
    ("거절된 뒤 설정 경로 안내하기", "'설정 › 알림'처럼 <b>찾아갈 경로를 적어</b> 줍니다. 브라우저는 권한 설정 화면을 자동으로 열어 주지 못합니다"),
    ("<code>role=\"status\"</code>", "권한 상태가 바뀌면 알립니다. 아이콘만 바뀌면 화면을 보지 않는 사람은 알 수 없습니다"),
  ]),
  backend=rows([
    ("서버는 권한 상태를 알 수 없음", "허용 여부는 <b>기기에만</b> 기록됩니다. 서버는 구독 정보가 들어왔는지를 보고 짐작할 수 있을 뿐입니다."),
    ("끊긴 구독 지우기", "사용자가 나중에 기기 설정에서 알림을 끄면 서버에는 아무 신호도 오지 않고 발송만 <b>조용히</b> 실패합니다. 그래서 발송 실패 응답을 보고 그 구독을 지워야 합니다."),
    ("알림 대신 쓸 전달 수단 두기", "알림을 받지 않는 사람에게는 <b>메일이나 화면 안 표시</b>로 같은 정보를 전합니다."),
    ("앞선 설명의 허용률 기록하기", "앞선 설명을 거친 사용자와 거치지 않은 사용자의 <b>허용률 차이</b>를 재 보면, 앞선 설명이 실제로 효과가 있는지 확인할 수 있습니다."),
  ]),
  plat_lede="OS 권한 창을 <b>한 번뿐인 기회</b>로 다뤄야 한다는 점은 세 플랫폼이 모두 같습니다.",
  plats=plats([
    ("웹", "Permissions API",
     dlg('알림을 허용하시겠습니까?', '', '차단', '허용', "112px"),
     "브라우저가 권한 창을 띄웁니다. 요즘 브라우저는 <b>사용자 동작 없이는</b> 권한 창을 아예 띄우지 못하게 막습니다."),
    ("iOS", "한 번만 묻고 이후는 설정에서",
     '''              <div class="phone" role="img" aria-label="iOS 권한 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:6px;box-shadow:var(--e2);padding:4px;text-align:center;font-size:5px">알림을 보내도록<br>허용하시겠습니까?</div></div></div>''',
     "알림 권한은 <b>딱 한 번</b>만 물을 수 있습니다. 위치 권한에는 '앱을 쓰는 동안만' 같은 중간 선택지가 있습니다."),
    ("안드로이드", "두 번 거절하면 다시 못 물음",
     '''              <div class="phone" role="img" aria-label="안드로이드 권한 창 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;background:var(--surface);border-radius:6px;box-shadow:var(--e2);padding:4px;text-align:center;font-size:5px">알림을 보내도록<br>허용하시겠습니까?</div></div></div>''',
     "한 번 거절해도 한 번 더 물을 수 있지만, <b>두 번 거절하면 다시 물을 수 없습니다</b>. 안드로이드 13부터는 알림도 권한을 받아야 보낼 수 있습니다."),
  ]),
  plat_note="\"첫 화면에서 권한을 다 받아 놓죠\"라는 결정은 나중에 가장 큰 손실로 돌아옵니다. 첫 화면에서 한꺼번에 물으면 <b>다섯 개 가운데 네 개는 거절당하고</b>, 나중에 그 기능이 필요해져도 되돌릴 방법이 없습니다. 권한을 <b>쓰려는 순간에 하나씩</b> 묻도록 바꾸기만 해도 허용률이 크게 달라지고, 그 차이는 직접 재서 보여 줄 수 있습니다.",
  siblings=siblings("permission"),
  related='''        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="notifications.html"><b>알림 센터</b><em>13부</em></a></li>
        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
