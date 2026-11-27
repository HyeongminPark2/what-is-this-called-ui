# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def panel(opts, link, who, warn="", w="152px", ok=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    os_ = []
    for name, desc, on in opts:
        st = ('border-color:var(--accent);background:var(--accent-soft);' if on else 'border-color:var(--line);')
        os_.append('<span style="display:block;border:1px solid ' + st + 'border-radius:4px;padding:3px 5px">'
                   '<span style="display:block;font-size:8px">' + ('● ' if on else '○ ') + name + '</span>'
                   + ('<span style="display:block;font-size:7px;color:var(--fg-muted)">' + desc + '</span>' if desc else '')
                   + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:4px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">'
            + ''.join(os_)
            + ('<span style="display:flex;gap:4px;align-items:center">'
               '<span style="flex:1;min-width:0;font-family:var(--mono);font-size:7px;border:1px solid var(--line);'
               'border-radius:3px;padding:2px 4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + link + '</span>'
               '<span style="font-size:7px;color:#fff;background:var(--accent);border-radius:3px;padding:2px 5px">복사</span></span>'
               if link else '')
            + '<span style="font-size:7px;color:var(--fg-muted)">' + who + '</span>'
            + ('<span style="font-size:7px;color:var(--danger)">' + warn + '</span>' if warn else '')
            + '</div></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">범위는 나만 · 고른 사람 · 사내 · 링크 있는 누구나</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">기본은 <b>가장 좁게</b> 두고 넓히는 건 본인이 함</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">권한은 볼 수만 · 댓글 · 고칠 수 있음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">지금 누가 볼 수 있는지 <b>이름으로</b> 보임</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">좁히면 이미 나간 링크가 막힌다고 알림</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">넓은 범위에는 만료 · 암호를 붙여 위험을 줄임</div>
                </div>
              </div>'''

D = dict(
  slug="share", ko="공유하기", en="Share · permissions",
  desc="남에게 보여 주는 범위를 정하는 화면입니다. 범위의 기본값, 권한, 이미 나간 링크를 다루는 법을 설명합니다.",
  lede="공유 화면에서 생기는 사고는 거의 언제나 <b>공유 범위의 기본값이 너무 넓어서</b> 일어납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>범위를 바꿔 보세요. 데모는 지금 범위에서 <b>볼 수 있는 사람 수</b>를 어림해 적고,
          사내 밖까지 열리면 경고를 띄웁니다.<br>
          '처음부터 링크 있는 누구나로 두기'를 켜면 아무것도 고르지 않아도
          <b>가장 넓은 범위</b>에서 시작합니다. 쓰기에는 편하지만 공유 사고는 대부분 이 설정에서 일어납니다.<br>
          범위를 바꿀 때는 <b>이미 나간 링크</b>가 어떻게 되는지도 함께 알려 줘야 합니다.
          범위를 좁히면 이미 보낸 링크도 그 순간부터 열리지 않기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "공유하기, 공유 설정, 권한 설정, 링크 공유"),
    ("영어", "share, sharing settings, permissions, link sharing"),
    ("같이 쓰는 말",
     "<b>누가</b> 볼 수 있는지를 <b>범위</b>(scope · audience), "
     "<b>무엇을</b> 할 수 있는지를 <b>권한</b>(permission · role)이라고 합니다. "
     "링크만 있으면 로그인 없이 열리는 방식은 <b>링크 공유</b>(link sharing)라 하고, "
     "그 링크에 붙는 임의의 문자열은 <b>토큰</b>이라고 부릅니다. "
     "OS가 띄우는, 보낼 앱을 고르는 화면은 <b>공유 시트</b>(share sheet)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>초대</b> — 초대는 상대의 <b>이름을 적어</b> 부르는 방식이고, 링크 공유는 링크를 <b>가진 사람 누구나</b> 열 수 있는 방식입니다.<br>"
     "<b>게시</b> — 게시는 다른 사람이 검색이나 목록으로 <b>찾을 수 있게</b> 만드는 것이고, 링크 공유는 링크를 모르면 <b>찾을 수 없습니다</b>.<br>"
     "<b>내보내기</b> — <a href=\"exportdata.html\">내보내기</a>는 데이터를 <b>파일로 떼어 주는</b> 일입니다."),
  ]),
  do_title="공유 화면을 만들 때 할 일",
  dont_title="공유 화면을 잘못 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  s4_title="공유 범위", s4_hint="범위가 넓을수록 거두기 어려움",
  states=states([
    (panel([("나만", "아무도 못 봄", True), ("고른 사람만", "", False), ("링크 있는 누구나", "", False)],
            "", "볼 수 있는 사람 1명", "", "152px", True),
     "나만 볼 때", "<b>가장 좁은</b> 범위입니다"),
    (panel([("나만", "", False), ("고른 사람만", "홍길동 · 김철수", True), ("링크 있는 누구나", "", False)],
            "example.com/s/2411", "홍길동 · 김철수 · 나", "", "152px", True),
     "고른 사람에게만 열 때", "볼 사람을 <b>이름으로</b> 골라 건넵니다"),
    (panel([("고른 사람만", "", False), ("모란상회 구성원", "로그인하면 누구나", True), ("링크 있는 누구나", "", False)],
            "example.com/s/2411", "모란상회 48명", "", "152px", True),
     "사내 전체에 열 때", "<b>로그인해야</b> 열리므로 사내 사람만 볼 수 있습니다"),
    (panel([("모란상회 구성원", "", False), ("링크 있는 누구나", "로그인 없이 열림", True)],
            "example.com/s/2411?t=9fa3", "링크를 받은 누구나",
            "⚠ 전달되면 막을 수 없음", "152px", False),
     "링크 있는 누구나 열 수 있을 때", "링크가 전달되면 <b>사내 밖까지</b> 열립니다"),
    (one(txt('<span style="display:block;font-size:8px">볼 수만 ▾</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">댓글 · 고칠 수 있음</span>'),
         "권한", True, "범위와 따로 고름", "152px"),
     "권한을 고를 때", "범위와는 <b>따로 정하는 값</b>입니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">범위를 좁혔습니다</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">이미 나간 링크는 이제 안 열립니다</span>'),
         "좁힘", None, "되돌리는 게 아니라 차단함", "152px"),
     "범위를 좁힐 때", "이미 나간 링크가 막힌다는 것을 <b>알려 줘야</b> 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("범위", "누가 보는가", "범위는 네 가지면 충분합니다"),
    ("기본값", "가장 좁게", "기본값은 가장 좁게 두고, <b>넓히는 일은 본인이</b> 합니다"),
    ("권한", "무엇을 할 수 있는가", "범위와 <b>따로</b> 고르게 합니다"),
    ("지금 볼 수 있는 사람", "이름으로", "지금 볼 수 있는 사람을 이름으로 적고 <b>몇 명인지 세어</b> 보여 줍니다"),
    ("범위를 좁힐 때", "이미 나간 링크 차단", "'이미 나간 링크가 막힙니다'라고 화면에 적습니다"),
    ("만료 · 암호", "위험을 줄이는 장치", "넓은 범위로 공유할 때는 열 수 있는 <b>기간을 정해</b> 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          공유 사고는 대개 <b>악의가 아니라 기본값</b> 때문에 일어납니다.
          급한 사람은 가장 빨리 끝나는 쪽을 고르는데,
          기본값이 '링크 있는 누구나'라면 그대로 그 범위로 공유하게 됩니다.
          그래서 기본값은 <b>좁게</b> 두고, 범위를 넓히는 자리에
          넓히면 <b>무슨 일이 일어나는지</b> 한 줄로 적어 두면 됩니다.<br>
          넓은 범위를 꼭 써야 한다면 <b>만료</b>를 붙이세요.
          '7일 뒤 만료' 정도면 거의 모든 경우에 충분하고,
          깜빡 잊고 열어 둔 링크도 기한이 지나면 <b>자동으로</b> 닫힙니다.</p>''',
  do=ul([
    "기본값을 <b>가장 좁게</b> 둘 때",
    "지금 누가 볼 수 있는지 <b>세어서</b> 보여 줄 때",
    "넓은 범위에 <b>만료</b>를 붙일 때",
  ]),
  dont=ul([
    "기본값을 <b>'링크 있는 누구나'</b>로 둘 때. 공유 사고가 대부분 여기서 일어납니다",
    "범위와 권한을 <b>한 덩어리</b>로 묶을 때. '볼 수만' 있게 하는 선택지가 사라집니다",
    "범위를 좁히면서 <b>아무 안내 없이</b> 링크를 막을 때. 링크를 받은 사람은 왜 안 열리는지 알 수 없습니다",
    "링크를 <b>짐작할 수 있게</b> 만들 때. 토큰은 길고 무작위로 만듭니다",
  ]),
  instead='데이터를 파일로 떼어 주는 일은 <a href="exportdata.html">내보내기</a>에서, 남에게 보이는 내 정보는 <a href="profile.html">프로필</a>에서 다룹니다. 기기 기능을 쓰도록 허락받는 일은 <a href="permission.html">권한 요청</a>에서, 되돌릴 수 없는 일은 <a href="destructive.html">위험한 동작</a>에서 설명합니다.',
  cases=cases([
    (panel([("고른 사람만", "홍길동 · 김철수", True)], "example.com/s/2411", "3명", "", "150px", True),
     "고른 사람에게 문서 공유하기", "볼 사람을 <b>이름으로</b> 골라 건넵니다"),
    (panel([("링크 있는 누구나", "7일 뒤 만료", True)], "example.com/s/2411?t=9fa3", "링크를 받은 누구나", "", "150px", None),
     "만료를 붙여 외부에 공유하기", "링크에 <b>만료</b>를 붙입니다"),
    (one(txt('<span style="display:block;font-size:8px">공유 시트</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">메시지 · 메일 · 복사…</span>'),
         "폰", True, "OS가 앱 고르기를 맡음", "150px"),
     "폰에서 보낼 곳 고르기", "보낼 곳을 고를 때는 <b>OS 공유 시트</b>를 씁니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="범위는 하나만 고르는 값이므로 <b>라디오</b>로 만들고, 기본 선택은 가장 좁은 쪽에 둡니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;누가 볼 수 있나&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"scope"</span> <span class="a">value</span>=<span class="s">"named"</span> <span class="a">checked</span>&gt;
    고른 사람만&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"scope"</span> <span class="a">value</span>=<span class="s">"any"</span>&gt;
    링크 있는 누구나
    &lt;<span class="t">small</span>&gt;로그인 없이 열립니다&lt;/<span class="t">small</span>&gt;&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

&lt;<span class="t">label</span>&gt;공유 링크
  &lt;<span class="t">input</span> <span class="a">readonly</span> <span class="a">value</span>=<span class="s">"https://example.com/s/2411-0042"</span>&gt;
&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">button</span>&gt;링크 복사&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;복사했습니다&lt;/<span class="t">p</span>&gt;''',
  keys=kbd([
    ("↑ ↓", "라디오 사이를 옮깁니다. 라디오 사이는 <b>Tab이 아니라</b> 화살표로 옮깁니다"),
    ("Enter · Space", "복사 단추를 누릅니다"),
    ("<code>role=\"status\"</code>", "'복사했습니다'를 스크린 리더로도 <b>소리 내어</b> 알립니다"),
    ("<code>readonly</code>", "링크 칸의 글자를 선택할 수는 있지만 <b>고칠 수는</b> 없게 합니다"),
    ("<code>&lt;fieldset&gt;</code>", "범위 묶음에 이름을 붙여서 무엇을 고르는 자리인지 스크린 리더로도 <b>전해지게</b> 합니다"),
    ("확인하는 방법", "로그아웃한 창에서 <b>복사한 링크</b>를 열어 봅니다"),
  ]),
  backend=rows([
    ("토큰은 길고 무작위로 만들기", "짧은 번호를 쓰면 번호를 <b>짐작해서</b> 남의 문서를 열 수 있습니다. 링크 공유에서는 토큰의 길이와 무작위성 말고는 막아 주는 장치가 없습니다."),
    ("범위를 좁히면 즉시 막기", "범위를 좁힌 순간부터 옛 토큰은 <b>거절</b>해야 합니다. 캐시에 남은 응답 때문에 계속 열린다면 범위를 좁힌 효과가 없습니다."),
    ("만료 날짜는 서버에서 검사하기", "<code>expires_at</code>을 저장해 두고 서버가 요청마다 검사합니다. 만료 날짜를 화면에만 적어 두면 기한이 지나도 링크가 열립니다."),
    ("누가 열었는지 알 수 없음", "링크 공유로는 <b>누가 봤는지 알 수 없습니다</b>. 열어 본 사람을 알아야 한다면 로그인을 요구하는 범위를 써야 합니다."),
  ]),
  plat_lede="<b>폰에는 OS 공유 시트</b>가 있어서, 어느 앱으로 보낼지 고르는 일은 OS가 맡습니다.",
  plats=plats([
    ("웹", "직접 만듦 + Web Share",
     panel([("고른 사람만", "", True)], "example.com/s/2411", "3명", "", "110px", True),
     "범위를 고르는 화면은 직접 만들고, 보내는 단계에서는 <code>navigator.share()</code>를 쓸 수 있습니다."),
    ("iOS", "공유 시트",
     '''              <div class="phone" role="img" aria-label="iOS 공유 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:3px;right:3px;bottom:3px;top:34px;border-radius:5px 5px 2px 2px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:6px;top:40px;display:flex;gap:3px">
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>UIActivityViewController</code>가 <b>어디로 보낼지</b> 고르는 화면을 띄웁니다. 공유 범위는 앱이 따로 정합니다."),
    ("안드로이드", "Sharesheet",
     '''              <div class="phone" role="img" aria-label="안드로이드 공유 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:3px;right:3px;bottom:3px;top:38px;border-radius:5px 5px 2px 2px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:6px;top:44px;display:flex;gap:3px">
                  <span style="width:10px;height:10px;border-radius:999px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:999px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>Intent.ACTION_SEND</code>로 띄웁니다. 자주 보내는 상대를 <b>맨 앞</b>에 보여 줍니다."),
  ]),
  plat_note="공유 단추 하나에는 <b>누가 볼 수 있게 할지</b>(범위)와 <b>어디로 보낼지</b>(앱·메신저)라는 <b>두 가지 일</b>이 섞여 있습니다. 폰에서는 보낼 곳을 고르는 일을 OS가 맡지만, 범위는 여전히 앱이 정합니다. 웹에서도 <code>navigator.share()</code>로 보낼 곳 고르기만 맡길 수 있고, 범위를 고르는 화면은 직접 만들어야 합니다. 그러니 <b>두 가지를 한 화면에 섞지 말고</b>, 범위를 먼저 정한 뒤 보내기로 넘어가게 하면 사용자가 덜 헷갈립니다.",
  siblings=siblings("share"),
  related='''        <li><a href="profile.html"><b>프로필</b><em>13부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="radio.html"><b>라디오 그룹</b><em>4부</em></a></li>''',
)
