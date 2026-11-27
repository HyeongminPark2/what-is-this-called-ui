# -*- coding: utf-8 -*-
from ax13 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L13 = "화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">범위 — 나만 · 고른 사람 · 사내 · 링크 있는 누구나</div>
                  <div class="pin-out" data-pin="2" style="color:var(--danger)">기본은 <b>가장 좁게</b> — 넓히는 건 본인이</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">권한 — 볼 수만 · 댓글 · 고칠 수 있음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">지금 누가 볼 수 있는지 <b>이름으로</b> 보인다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">좁히면 이미 나간 링크가 막힌다 — 알려야 한다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">만료 · 암호 — 넓은 범위를 덜 위험하게</div>
                </div>
              </div>'''

D = dict(
  slug="share", ko="공유하기", en="Share · permissions",
  desc="남에게 보여 주는 화면. 범위의 기본값, 권한, 이미 나간 링크를 다루는 법.",
  lede="공유 화면의 실패는 거의 늘 <b>기본값이 너무 넓은 것</b>입니다. 사고는 거기서 납니다.",
  axes_lede=L13,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>범위를 바꿔 보세요 — 데모가 지금 범위에서 <b>볼 수 있는 사람 수</b>를 어림해 적고,
          사내 밖까지 열리면 경고를 띄웁니다.<br>
          '처음부터 링크 있는 누구나로 두기'를 켜면 아무것도 안 골라도
          <b>가장 넓은 범위</b>에서 시작합니다 — 쓰기는 편하고 사고는 여기서 납니다.<br>
          범위를 바꾸면 <b>이미 나간 링크</b>가 어떻게 되는지도 같이 알려 줘야 합니다.
          좁히면 그 링크는 그 자리에서 막힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "공유하기, 공유 설정, 권한 설정, 링크 공유"),
    ("영어", "share, sharing settings, permissions, link sharing"),
    ("같이 쓰는 말",
     "<b>누가</b> 볼 수 있는지가 <b>범위</b>(scope · audience), "
     "<b>무엇을</b> 할 수 있는지가 <b>권한</b>(permission · role)입니다. "
     "링크만 있으면 로그인 없이 열리는 것을 <b>링크 공유</b>(link sharing), "
     "그 링크에 붙는 임의의 문자열을 <b>토큰</b>이라 부릅니다. "
     "OS 가 띄우는 앱 고르기 판은 <b>공유 시트</b>(share sheet)입니다."),
    ("자주 잘못 부름",
     "<b>초대</b> — 초대는 <b>이름을 적어</b> 부르는 쪽, 링크 공유는 <b>가진 사람 누구나</b>입니다.<br>"
     "<b>게시</b> — 게시는 <b>찾아지게</b> 만드는 것이고 링크 공유는 <b>안 찾아집니다</b>.<br>"
     "<b>내보내기</b> — <a href=\"exportdata.html\">내보내기</a>는 <b>파일로 떼어 주는</b> 일입니다."),
  ]),
  axes=ax("공유하기"),
  oneline="<b>기본은 가장 좁게.</b> 넓히는 것은 쉬워도, 넓게 나간 링크를 거두는 건 어렵습니다.",
  s4_title="범위", s4_hint="넓어질수록 거두기 어렵다",
  states=states([
    (panel([("나만", "아무도 못 본다", True), ("고른 사람만", "", False), ("링크 있는 누구나", "", False)],
            "", "볼 수 있는 사람 1명", "", "152px", True),
     "나만", "<b>가장 좁다</b>"),
    (panel([("나만", "", False), ("고른 사람만", "홍길동 · 김철수", True), ("링크 있는 누구나", "", False)],
            "example.com/s/2411", "홍길동 · 김철수 · 나", "", "152px", True),
     "고른 사람만", "<b>이름으로</b> 건넨다"),
    (panel([("고른 사람만", "", False), ("모란상회 구성원", "로그인하면 누구나", True), ("링크 있는 누구나", "", False)],
            "example.com/s/2411", "모란상회 48명", "", "152px", True),
     "사내 전체", "<b>로그인이 벽</b>이 된다"),
    (panel([("모란상회 구성원", "", False), ("링크 있는 누구나", "로그인 없이 열린다", True)],
            "example.com/s/2411?t=9fa3", "링크를 받은 누구나",
            "⚠ 전달되면 막을 수 없다", "152px", False),
     "링크 있는 누구나", "<b>사내 밖까지</b>"),
    (one(txt('<span style="display:block;font-size:8px">볼 수만 ▾</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">댓글 · 고칠 수 있음</span>'),
         "권한", True, "범위와 따로 고른다", "152px"),
     "권한", "범위와 <b>다른 축</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--danger)">범위를 좁혔다</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">이미 나간 링크는 이제 안 열립니다</span>'),
         "좁힘", None, "되돌림이 아니라 차단이다", "152px"),
     "좁힐 때", "<b>알려 줘야</b> 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("범위", "누가 보나", "넷이면 충분하다"),
    ("기본값", "가장 좁게", "<b>넓히는 건 본인이</b>"),
    ("권한", "무엇을 하나", "범위와 <b>따로</b> 고른다"),
    ("지금 누가", "이름으로", "<b>세어서</b> 보여 준다"),
    ("좁힐 때", "차단된다", "'이미 나간 링크가 막힌다'고 적는다"),
    ("만료 · 암호", "덜 위험하게", "넓은 범위를 <b>시간으로</b> 묶는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          공유 사고는 <b>악의가 아니라 기본값</b>에서 납니다.
          급한 사람은 가장 빠른 길을 고르는데,
          그 길이 '링크 있는 누구나'면 그게 선택이 됩니다.
          그래서 기본은 <b>좁게</b> 두고, 넓히는 자리에
          <b>무슨 일이 일어나는지</b>를 한 줄로 적어 두는 것이 전부입니다.<br>
          넓은 범위를 꼭 써야 한다면 <b>만료</b>를 붙이세요 —
          '7일 뒤 만료'는 거의 모든 경우에 충분하고,
          잊고 열어 둔 링크를 <b>저절로</b> 닫아 줍니다.</p>''',
  do=ul([
    "기본을 <b>가장 좁게</b> 두기",
    "지금 누가 볼 수 있는지 <b>세어서</b> 보여 주기",
    "넓은 범위에는 <b>만료</b> 붙이기",
  ]),
  dont=ul([
    "기본을 <b>'링크 있는 누구나'</b>로 두기 — 사고가 여기서 난다",
    "범위와 권한을 <b>한 덩어리</b>로 묶기 — '볼 수만'이 사라진다",
    "좁힐 때 <b>말없이</b> 막기 — 받은 사람은 왜 안 열리는지 모른다",
    "링크를 <b>짐작할 수 있게</b> 만들기 — 토큰은 길고 임의로",
  ]),
  instead='파일로 떼어 주면 <a href="exportdata.html">내보내기</a>, 남에게 보이는 내 정보는 <a href="profile.html">프로필</a>, 기기 기능은 <a href="permission.html">권한 요청</a>, 되돌릴 수 없는 일은 <a href="destructive.html">위험한 동작</a>.',
  cases=cases([
    (panel([("고른 사람만", "홍길동 · 김철수", True)], "example.com/s/2411", "3명", "", "150px", True),
     "문서 공유", "<b>이름으로</b> 건넨다"),
    (panel([("링크 있는 누구나", "7일 뒤 만료", True)], "example.com/s/2411?t=9fa3", "링크를 받은 누구나", "", "150px", None),
     "외부 공유", "<b>만료</b>를 붙인다"),
    (one(txt('<span style="display:block;font-size:8px">공유 시트</span>'
             '<span style="display:block;font-size:7px;color:var(--fg-muted);margin-top:2px">메시지 · 메일 · 복사…</span>'),
         "폰", True, "OS 가 앱 고르기를 맡는다", "150px"),
     "폰", "<b>OS 공유 시트</b>를 쓴다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="범위는 <b>라디오</b>입니다 — 하나만 고르는 값이고, 기본은 가장 좁은 쪽입니다.",
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
    ("↑ ↓", "라디오 사이를 옮긴다 — <b>Tab 이 아니다</b>"),
    ("Enter · Space", "복사 단추를 누른다"),
    ("<code>role=\"status\"</code>", "'복사했습니다'를 <b>소리로도</b> 알린다"),
    ("<code>readonly</code>", "링크 칸은 고르기는 되고 <b>고쳐지지는</b> 않는다"),
    ("<code>&lt;fieldset&gt;</code>", "범위 묶음에 이름을 준다 — 무엇을 고르는지 <b>소리로</b> 전해진다"),
    ("확인하는 법", "로그아웃한 창에서 <b>복사한 링크</b>를 열어 본다"),
  ]),
  backend=rows([
    ("토큰은 길고 임의로", "짧은 번호를 쓰면 <b>짐작해서</b> 남의 것이 열립니다. 길이와 무작위성이 유일한 벽입니다."),
    ("좁히면 즉시 막기", "범위를 좁힌 순간부터 옛 토큰은 <b>거절</b>해야 합니다 — 캐시에 남아 열리면 좁힌 적이 없는 셈입니다."),
    ("만료", "<code>expires_at</code> 을 두고 서버가 검사합니다. 화면에만 적어 두면 아무 소용이 없습니다."),
    ("누가 열었나", "링크 공유는 <b>누가 봤는지 모릅니다</b> — 그게 필요하면 로그인을 요구하는 범위를 써야 합니다."),
  ]),
  plat_lede="<b>폰에는 OS 공유 시트</b>가 있어 앱 고르기를 맡아 줍니다.",
  plats=plats([
    ("웹", "직접 만듦 + Web Share",
     panel([("고른 사람만", "", True)], "example.com/s/2411", "3명", "", "110px", True),
     "범위 고르기는 직접 만들고, 보내는 자리에서는 <code>navigator.share()</code> 를 쓸 수 있습니다."),
    ("iOS", "공유 시트",
     '''              <div class="phone" role="img" aria-label="iOS 공유 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:3px;right:3px;bottom:3px;top:34px;border-radius:5px 5px 2px 2px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:6px;top:40px;display:flex;gap:3px">
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>UIActivityViewController</code> 가 <b>어디로 보낼지</b>를 맡습니다. 범위는 앱이 따로 정합니다."),
    ("안드로이드", "Sharesheet",
     '''              <div class="phone" role="img" aria-label="안드로이드 공유 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:3px;right:3px;bottom:3px;top:38px;border-radius:5px 5px 2px 2px;background:var(--surface);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:6px;top:44px;display:flex;gap:3px">
                  <span style="width:10px;height:10px;border-radius:999px;background:var(--accent-soft)"></span>
                  <span style="width:10px;height:10px;border-radius:999px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>Intent.ACTION_SEND</code> 입니다. 자주 쓰는 상대를 <b>맨 앞</b>에 올려 줍니다."),
  ]),
  plat_note="공유는 <b>두 가지 일</b>이 한 단추에 섞여 있습니다 — <b>누가 볼 수 있게 할지</b>(범위)와 <b>어디로 보낼지</b>(앱·메신저). 폰은 뒤쪽을 OS 가 맡아 주지만 범위는 여전히 앱이 정합니다. 웹에서는 <code>navigator.share()</code> 로 뒤쪽만 빌려 쓸 수 있고, 범위 고르기는 어차피 직접 만들어야 합니다. <b>둘을 한 화면에 섞지 말고</b> 범위를 먼저 정한 뒤 보내기로 넘기는 차례가 덜 헷갈립니다.",
  siblings=siblings("share"),
  related='''        <li><a href="profile.html"><b>프로필</b><em>13부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="radio.html"><b>라디오 그룹</b><em>4부</em></a></li>''',
)
