# -*- coding: utf-8 -*-
from ax13 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L13 = "화면 단위 패턴은 사용자가 <b>끝내야 하는 일</b> 하나로 나눕니다. 아래 네 가지로 서로 가릅니다."

def card(fields, who, w="152px", note="", ok=None, act="메시지 보내기", av="길동"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    rs = []
    for name, val, bad in fields:
        bg = 'background:color-mix(in srgb, var(--danger) 8%, transparent);' if bad else ''
        cl = 'color:var(--danger);' if bad else ''
        rs.append('<span style="display:flex;gap:5px;padding:2px 5px;font-size:8px;' + bg + '">'
                  '<span style="width:40px;color:var(--fg-muted);flex:none">' + name + '</span>'
                  '<span style="' + cl + 'min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'
                  + val + '</span></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + c + ';border-radius:6px;background:var(--surface);overflow:hidden">'
            '<span style="display:block;height:18px;background:linear-gradient(135deg, var(--accent) 0%, var(--accent-soft) 100%)"></span>'
            '<span style="display:flex;gap:5px;align-items:center;padding:0 6px 5px;margin-top:-8px">'
            '<span style="width:20px;height:20px;border-radius:999px;border:1.5px solid var(--surface);'
            'background:var(--accent-soft);display:grid;place-items:center;font-size:6.5px;color:var(--accent);flex:none">' + av + '</span>'
            '<span style="display:grid;min-width:0"><span style="font-size:8.5px;font-weight:700">홍길동</span>'
            '<span style="font-size:7px;color:var(--fg-muted)">' + who + '</span></span>'
            '<span style="margin-left:auto;font-size:7px;color:var(--accent);white-space:nowrap">' + act + '</span></span>'
            '<span style="display:grid;gap:1px;border-top:1px solid var(--line);padding:3px 0">' + ''.join(rs) + '</span>'
            '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">같은 주소라도 <b>보는 사람마다 다른 화면</b></div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">주 동작은 나에게 '수정', 남에게 '메시지'</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">칸마다 <b>공개 범위</b>가 따로 있음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">기본은 좁게 두고 넓히는 건 본인이 함</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">빈 프로필은 채우라고 권하되 막지 않음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">사진이 없으면 아바타를 이니셜로 표시</div>
                </div>
              </div>'''

D = dict(
  slug="profile", ko="프로필", en="Profile page",
  desc="같은 주소인데 보는 사람에 따라 다르게 보이는 화면입니다. 공개 범위, 주 동작, 빈 프로필을 다루는 법을 설명합니다.",
  lede="프로필은 주소는 하나지만 <b>보는 사람에 따라 여러 화면</b>이 됩니다. 내가 볼 때와 같은 팀이 볼 때, 남이 볼 때 보이는 칸과 버튼이 모두 다릅니다.",
  axes_lede=L13,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>보는 사람을 바꿔 보세요. 같은 주소인데 나에게는 '수정' 버튼이, 남에게는 '메시지' 버튼이 뜹니다.
          데모는 <b>지금 몇 칸이 보이는지</b>와 <b>보이면 안 되는 칸이 몇 개 드러나 있는지</b>를 세어 보여 줍니다.<br>
          '모든 칸을 다 보여 주기'를 켜면 전화번호·생일·인사 메모까지 남에게 보이는데,
          빨간 줄로 표시된 것이 <b>남에게 보이면 안 되는</b> 칸입니다. 그래서 공개 범위는 <b>기본값을 좁게</b> 두고
          본인이 필요할 때 넓히게 하는 편이 안전합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "프로필, 프로필 화면, 내 정보, 사용자 페이지"),
    ("영어", "profile page, user page, account page"),
    ("같이 쓰는 말",
     "내가 보는 내 프로필을 <b>마이 페이지</b>, 남이 보는 프로필을 <b>공개 프로필</b>이라고 구별해 부릅니다. "
     "맨 위의 큰 띠 모양 그림은 <b>커버</b>(cover · banner), 동그란 사진은 <b>아바타</b>라고 합니다. "
     "값을 고치는 화면은 보통 <b>프로필 편집</b>이라는 이름으로 따로 둡니다."),
    ("자주 잘못 부르는 이름",
     "<b>설정</b> — <a href=\"settings.html\">설정 화면</a>은 <b>내 쪽에서 앱이 동작하는 방식</b>을 바꾸고, 프로필은 <b>남에게 보이는 정보</b>를 다룹니다.<br>"
     "<b>계정</b> — 계정은 프로필보다 <b>로그인 수단과 보안</b>에 가까운 개념입니다.<br>"
     "<b>아바타</b> — <a href=\"avatar.html\">아바타</a>는 프로필 화면 안에 들어가는 <b>부품</b> 하나입니다."),
  ]),
  axes=ax("프로필"),
  oneline="<b>'누가 보고 있나'를 먼저 정하세요.</b> 보는 사람의 종류를 정해 두지 않으면 칸마다 공개 범위를 정할 수 없습니다.",
  do_title="프로필 화면을 만들 때 할 일",
  dont_title="프로필 화면을 잘못 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  s4_title="보는 사람에 따라 달라지는 화면", s4_hint="같은 주소라도 보는 사람마다 다르게 보임",
  states=states([
    (card([("이름", "홍길동", False), ("소속", "모란상회 · 정산팀", False), ("전화", "010-0000-0000", False)],
          "내 프로필", "152px", "다 보이고 다 고칠 수 있음", True, "프로필 수정"),
     "내가 볼 때", "주 동작이 <b>수정</b>입니다"),
    (card([("이름", "홍길동", False), ("소속", "모란상회 · 정산팀", False), ("자리", "3층 B열", False)],
          "같은 팀이 보는 화면", "152px", "사내 칸까지 보임", True),
     "같은 팀이 볼 때", "남보다 <b>사내 칸이 더</b> 보입니다"),
    (card([("이름", "홍길동", False), ("소속", "모란상회 · 정산팀", False), ("맡은 일", "정산 검수", False)],
          "남이 보는 화면", "152px", "공개 칸만 보임", True),
     "남이 볼 때", "공개 칸 <b>세 개</b>만 보입니다"),
    (card([("이름", "홍길동", False), ("전화", "010-0000-0000 ⚠", True), ("메모", "승진 대상 ⚠", True)],
          "남이 보는 화면", "152px", "보이면 안 되는 값이 드러남", False),
     "공개 범위를 잘못 정했을 때", "보이면 안 되는 값이 <b>남에게 드러납니다</b>"),
    (card([("이름", "홍길동", False), ("소속", "— 아직 안 적음", False), ("맡은 일", "— 아직 안 적음", False)],
          "남이 보는 화면", "152px", "막지 않고 권하기만 함", None),
     "프로필이 비어 있을 때", "칸을 <b>적지 않아도</b> 서비스를 쓸 수 있어야 합니다"),
    (card([("이름", "탈퇴한 사용자", False), ("소속", "—", False), ("맡은 일", "—", False)],
          "없는 사람", "152px", "404 대신 이 화면을 보여 줌", None, "", "—"),
     "탈퇴했거나 없는 사람일 때", "탈퇴한 사람이 <b>남긴 글</b>은 그대로 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("같은 주소", "다른 화면", "<b>보는 사람</b>에 따라 화면이 달라집니다"),
    ("주 동작", "하나만", "주 동작은 하나만 둡니다. 나에게는 수정, 남에게는 메시지입니다"),
    ("공개 범위", "칸마다", "공개 범위를 칸마다 따로 두고, 여러 칸을 <b>한 덩어리로</b> 묶지 않습니다"),
    ("기본값", "좁게", "기본값은 좁게 두고, 범위를 넓히는 일은 <b>본인</b>이 합니다"),
    ("빈 프로필", "막지 않기", "채우라고 권하되, 채우지 않아도 <b>쓸 수 있게</b> 합니다"),
    ("아바타", "사진이 없으면 이니셜", "사진이 없으면 이니셜로 표시하고, 사진은 <b>선택</b>으로 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          프로필에서 나는 사고는 거의 전부 <b>공개 범위</b>에서 생깁니다.
          칸마다 공개 범위가 다른데 화면은 한 장이어서, '이 칸이 누구에게 보이는지'를
          만드는 사람도 쓰는 사람도 헷갈리기 때문입니다.<br>
          가장 손쉬운 해법은 공개 범위를 <b>화면에 적어 두는 것</b>입니다.
          칸 옆에 '사내 공개'·'나만' 같은 표시를 두면
          본인이 화면을 보면서 범위를 고칠 수 있습니다.
          여기에 <b>남이 보는 화면을 미리 보여 주는</b> 단추까지 두면
          남에게 보이면 안 되는 칸을 본인이 먼저 찾아낼 수 있습니다.</p>''',
  do=ul([
    "칸마다 <b>공개 범위</b>를 두고 그 범위를 화면에 적을 때",
    "<b>남이 보는 화면 미리 보기</b> 단추를 둘 때",
    "프로필이 비어 있어도 <b>하던 일은 계속할 수 있게</b> 할 때",
  ]),
  dont=ul([
    "공개 범위를 <b>한 덩어리</b>로 묶을 때. 소속을 공개하면 전화번호까지 함께 공개됩니다",
    "프로필을 다 채우기 전에는 <b>다음으로 못 가게</b> 막을 때",
    "탈퇴한 사람의 프로필을 <b>404</b>로 보낼 때. 그 사람이 남긴 글의 맥락이 끊깁니다",
    "'수정'과 '메시지'를 <b>둘 다</b> 띄울 때. 누구의 화면인지 모호해집니다",
  ]),
  instead='앱이 내 쪽에서 동작하는 방식을 바꾸는 일은 <a href="settings.html">설정 화면</a>에서, 동그란 사진 부품은 <a href="avatar.html">아바타</a>에서 다룹니다. 남에게 무언가를 보여 주는 범위는 <a href="share.html">공유하기</a>에서, 로그인과 계정은 <a href="login.html">로그인</a>에서 다룹니다.',
  cases=cases([
    (card([("이름", "홍길동", False), ("소속", "모란상회", False)], "남이 보는 화면", "150px", "", True),
     "사내 주소록에 보이는 프로필", "<b>공개 칸만</b> 보여 줍니다"),
    (card([("이름", "홍길동", False), ("한 줄 소개", "정산을 맡고 있습니다", False)], "내 프로필", "150px", "", True, "프로필 수정"),
     "커뮤니티의 자기소개 프로필", "본인이 <b>스스로 적은</b> 내용을 위주로 보여 줍니다"),
    (card([("가게", "모란상회", False), ("업종", "식료품", False)], "손님이 보는 화면", "150px", "", True, "문의하기"),
     "사람 대신 가게를 보여 주는 프로필", "<b>사람이 아닌 대상</b>에도 같은 틀을 씁니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="보는 사람에 따라 <b>그리는 내용 자체를</b> 바꿉니다. 다 그려 놓고 일부를 숨기는 방식으로 처리하지 않습니다.",
  code='''<span class="c">&lt;!-- 서버가 이미 걸러서 주므로 화면이 CSS로 숨기지 않는다 --&gt;</span>
&lt;<span class="t">main</span>&gt;
  &lt;<span class="t">h1</span>&gt;홍길동&lt;/<span class="t">h1</span>&gt;
  &lt;<span class="t">p</span>&gt;모란상회 · 정산팀&lt;/<span class="t">p</span>&gt;

  &lt;<span class="t">dl</span>&gt;
    &lt;<span class="t">dt</span>&gt;맡은 일&lt;/<span class="t">dt</span>&gt;&lt;<span class="t">dd</span>&gt;정산 검수&lt;/<span class="t">dd</span>&gt;
  &lt;/<span class="t">dl</span>&gt;

  &lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/messages/new?to=gildong"</span>&gt;메시지 보내기&lt;/<span class="t">a</span>&gt;
&lt;/<span class="t">main</span>&gt;

<span class="c">/* ✕ 이렇게 하면 소스에 값이 그대로 남아 있다 */</span>
.private { <span class="a">display</span>: none; }''',
  keys=kbd([
    ("Tab", "Tab을 눌렀을 때 주 동작이 <b>맨 앞</b>에 오도록 마크업 순서를 정합니다"),
    ("<code>&lt;dl&gt;</code>", "이름과 값이 짝을 이루므로 <b>스크린 리더가 읽을 때</b>도 짝이 유지됩니다"),
    ("<code>&lt;h1&gt;</code>", "사람 이름을 그 화면의 <b>제목</b>으로 둡니다"),
    ("<code>aria-label</code>", "아바타에는 <b>이름을 다시</b> 적지 않습니다. 적으면 이름이 두 번 읽힙니다"),
    ("보이면 안 되는 칸 숨기기", "보이면 안 되는 칸은 <b>서버에서 거릅니다</b>. <code>display:none</code>으로 숨긴 값은 소스에 그대로 남습니다"),
    ("확인하는 방법", "로그아웃한 창에서 <b>같은 주소</b>를 열어 봅니다"),
  ]),
  backend=rows([
    ("볼 수 있는 칸만 걸러서 보내기", "응답 자체에 <b>볼 수 있는 칸만</b> 담습니다. 모든 칸을 보내 놓고 화면에서 숨기면 값이 <b>소스에 그대로</b> 남습니다."),
    ("보는 사람에 따라 달라지는 응답", "요청한 사람이 누구인지에 따라 응답이 달라집니다. <b>같은 URL에 다른 응답 본문</b>이 오므로 캐시를 조심해야 합니다."),
    ("칸마다 공개 범위 값 두기", "칸마다 <code>visibility: \"org\" | \"team\" | \"self\"</code> 값이 있어야 화면이 공개 범위 표시를 그릴 수 있습니다."),
    ("탈퇴한 사람의 데이터", "탈퇴한 사람의 데이터는 지우지 않고 <b>표시만</b> 바꿉니다. 남긴 글의 작성자 자리가 비면 글의 맥락이 끊기기 때문입니다."),
  ]),
  plat_lede="<b>화면 구성은 플랫폼마다 비슷</b>하고, 공개 범위를 어디서 다루는지만 다릅니다.",
  plats=plats([
    ("웹", "주소 하나",
     card([("이름", "홍길동", False), ("소속", "모란상회", False)], "남이 보는 화면", "110px", "", True),
     "주소 하나가 보는 사람에 따라 <b>여러 화면</b>으로 보입니다. 로그아웃 상태로 열어 보는 것이 가장 빠른 검사입니다."),
    ("iOS", "프로필 화면",
     '''              <div class="phone" role="img" aria-label="iOS 프로필 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:50%;top:24px;transform:translateX(-50%);width:16px;height:16px;border-radius:999px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:8px;right:8px;top:44px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:54px;height:7px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "아바타를 <b>가운데</b> 두는 구성이 흔하고, 공개 범위는 설정 쪽에 따로 둡니다."),
    ("안드로이드", "프로필 화면",
     '''              <div class="phone" role="img" aria-label="안드로이드 프로필 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:24px;width:16px;height:16px;border-radius:999px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:26px;right:6px;top:28px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;right:5px;top:46px;height:7px;border-radius:2px;background:var(--bg)"></div></div></div>''',
     "아바타를 <b>왼쪽</b>에 두고 오른쪽에 이름을 적는 구성이 많지만, 전체 틀은 iOS와 같습니다."),
  ]),
  plat_note="앱은 로그인한 사람이 대부분 쓰기 때문에 만들 때 <b>'남이 볼 때'를 잊기 쉽습니다</b>. 반면 웹 프로필은 로그아웃 상태에서도 그냥 열리므로 공개 범위 실수가 바로 드러나고, 그래서 오히려 일찍 고칠 수 있습니다. <b>로그아웃한 창에서 같은 주소를 열어 보는 것</b>을 마무리 검사로 넣어 두면 공개 범위 사고는 대부분 미리 잡힙니다.",
  siblings=siblings("profile"),
  related='''        <li><a href="avatar.html"><b>아바타</b><em>5부</em></a></li>
        <li><a href="settings.html"><b>설정 화면</b><em>13부</em></a></li>
        <li><a href="share.html"><b>공유하기</b><em>13부</em></a></li>
        <li><a href="login.html"><b>로그인</b><em>13부</em></a></li>''',
)
