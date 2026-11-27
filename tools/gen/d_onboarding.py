# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def steps(n, cur, w="152px", note=""):
    es = []
    for i in range(n):
        on = i == cur
        done = i < cur
        es.append('<span style="width:15px;height:15px;border-radius:50%;display:grid;place-items:center;font-size:8px;'
                  + ('background:var(--accent);color:#fff;font-weight:700' if on else
                     'background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)' if done else
                     'background:var(--surface);color:var(--fg-muted);border:1px solid var(--line)')
                  + '">' + ('✓' if done else str(i + 1)) + '</span>')
    line = '<span style="flex:1;height:1px;background:var(--line);min-width:6px"></span>'
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;align-items:center;gap:3px">' + line.join(es) + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def card(inner, w="152px"):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);padding:8px;display:grid;gap:5px">' + inner + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:200px">''' + steps(4, 1, "200px").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">끝이 보인다 — 2 / 4</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">건너뛰기 · 나중에 하기 — 나가는 대신 누른다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">어디까지 왔는지 서버에 적어 둔다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">건너뛴 것은 설정에서 마저 채울 수 있다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">단계마다 15%가 떠나면 여섯 단계는 절반 아래</div>
                </div>
              </div>'''

D = dict(
  slug="onboarding", ko="온보딩", en="Onboarding",
  desc="처음 쓰는 사람을 쓸 수 있게 만드는 흐름. 단계가 늘수록 떨어지는 계산과 건너뛸 길.",
  lede="처음 온 사람을 <b>쓸 수 있게</b> 만드는 흐름. 단계가 늘수록 <b>끝까지 오는 사람이 곱으로</b> 줍니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>오른쪽은 <b>계산</b>입니다 — 실제 측정값이 아니라 '단계마다 같은 비율이 떠난다'고 두고 곱한 것입니다.
          그래도 요점은 분명합니다. 한 단계에서 15%만 떠나도 <b>여섯 단계면 절반 아래</b>입니다.<br>
          <b>건너뛸 길 주기</b>를 켜면 떠나는 비율이 줄어듭니다 — 막히면 나가는 대신 <b>건너뛰기</b>를 누르기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "온보딩, 첫 설정, 시작하기, 둘러보기"),
    ("영어", "onboarding, first-run experience, setup wizard, product tour"),
    ("같이 쓰는 말",
     "여러 화면으로 나눈 것이 <b>위저드</b>(wizard)·<b>스텝 폼</b>, "
     "화면 위에 떠서 하나씩 짚어 주는 것이 <b>코치마크</b>(coach mark)·<b>프로덕트 투어</b>입니다. "
     "처음 켰을 때의 경험 전체를 <b>FRE</b>(first-run experience)라 부르고, "
     "단계마다 몇 명이 남는지를 그린 것이 <b>퍼널</b>입니다."),
    ("자주 잘못 부름",
     "<b>튜토리얼</b> — 기능 설명이고, 온보딩은 <b>쓸 수 있게 만드는</b> 것입니다. 설명만 하고 끝나면 온보딩이 아닙니다.<br>"
     "<b>가입</b> — 계정을 만드는 것까지가 가입이고, 그다음이 온보딩입니다.<br>"
     "<b>빈 상태</b> — <a href=\"../items/empty.html\">빈 상태</a>도 온보딩의 한 자리지만 <b>화면 하나</b>의 문제입니다."),
  ]),
  axes=ax("온보딩"),
  oneline="<b>온보딩은 줄이는 일입니다.</b> 단계를 더 잘 만드는 것보다 <b>단계를 지우는</b> 쪽이 거의 늘 낫습니다.",
  s4_title="흐름", s4_hint="끝이 보이나",
  states=states([
    (steps(4, 0, "152px", "1 / 4 — 끝이 보인다"), "시작", "<b>몇 단계인지</b> 처음부터 알려 준다"),
    (steps(4, 2, "152px", "3 / 4 — 두 개 끝냈다"), "진행 중", "지나온 것에 ✓. <b>돌아갈 수</b> 있어야 한다"),
    (card('<span style="font-size:9.5px">어떤 일을 하시나요?</span>'
          '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:9px;color:var(--fg-muted)">입력</div>'
          '<div style="display:flex;gap:4px"><span style="flex:1;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">다음</span>'
          '<span style="text-align:center;border:1px solid var(--line);border-radius:4px;padding:3px 8px;font-size:9px">건너뛰기</span></div>'),
     "건너뛸 길 ✓", "막히면 <b>나가는 대신 누른다</b>"),
    (card('<span style="font-size:9.5px">어떤 일을 하시나요?</span>'
          '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:9px;color:var(--fg-muted)">입력</div>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">다음</span>'
          '<span style="font-size:8px;color:var(--danger)">나갈 길이 없다</span>'),
     "건너뛸 길 ✕", "<b>막히면 앱을 닫는다</b>"),
    (card('<span style="font-size:9.5px;font-weight:700">거의 다 됐습니다</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">설정에서 언제든 바꿀 수 있어요</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">시작하기</span>'),
     "끝", "<b>무엇이 남았는지</b>와 바꿀 수 있다는 말"),
    (card('<span style="font-size:9.5px">2단계까지 하셨어요</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">이어서 하기</span>'),
     "다시 들어왔을 때", "<b>어디까지 했는지</b> 기억한다. 처음부터면 안 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계 표시", "2 / 4", "<b>끝이 보여야</b> 끝까지 간다"),
    ("돌아가기", "← 이전", "적은 값은 <b>그대로 남아</b> 있어야 한다"),
    ("건너뛸 길", "나중에 하기", "<b>가장 값싼 한 줄.</b> 나가는 대신 누른다"),
    ("이어 하기", "서버에 기록", "다시 들어왔을 때 <b>처음부터</b>면 안 한다"),
    ("나중에 채우기", "설정에서", "건너뛴 것이 <b>어디 있는지</b> 알려 준다"),
    ("단계 수", "적을수록 좋다", "단계마다 사람이 샌다. <b>곱으로 줄어든다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          온보딩에서 가장 자주 섞이는 두 가지가 <b>'우리가 알고 싶은 것'</b>과
          <b>'사용자가 쓰려면 필요한 것'</b>입니다.
          직군·회사 규모·유입 경로는 <b>우리가 알고 싶은 것</b>이지
          사용자가 첫 화면을 쓰는 데 필요한 값이 아닙니다.
          그런 칸은 온보딩에서 빼고 <b>나중에 물어도</b> 됩니다 —
          대개 이 한 번의 분류만으로 단계가 절반이 됩니다.</p>''',
  do=ul([
    "<b>쓰려면 꼭 필요한 값</b>만 받을 때",
    "첫 화면이 <b>텅 비어</b> 있을 때 — 샘플을 하나 만들어 준다",
    "권한이 필요할 때 — <a href=\"permission.html\">권한 요청</a>의 앞선 설명 자리",
  ]),
  dont=ul([
    "<b>우리가 알고 싶은 것</b>을 묻기 — 나중에 물어도 된다",
    "기능 설명 슬라이드 다섯 장 — <b>아무도 안 읽는다</b>",
    "건너뛸 길 없이 — 막히면 <b>앱을 닫는다</b>",
    "처음부터 다시 — 이어 할 수 있게 <b>기록</b>한다",
  ]),
  instead='칸이 여럿이면 <a href="form.html">폼 설계</a>, 첫 화면이 비면 <a href="../items/empty.html">빈 상태</a>, 기능을 짚어 주려면 <a href="../items/popover.html">팝오버</a>.',
  cases=cases([
    (steps(3, 1, "150px", "3단계 — 알맞다"), "짧은 위저드", "셋을 넘기면 <b>끝이 안 보인다</b>"),
    (card('<span style="font-size:9.5px;font-weight:700">첫 가맹점을 만들어 볼까요?</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">예시로 하나 만들어 뒀습니다</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">보러 가기</span>', "150px"),
     "빈 화면 대신", "묻지 말고 <b>만들어 준다.</b> 가장 좋은 온보딩"),
    (card('<div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border-radius:50%;border:1px solid var(--accent)"></span><span style="font-size:9px">프로필 채우기</span></div>'
          '<div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border-radius:50%;background:var(--accent)"></span><span style="font-size:9px;color:var(--fg-muted)">가맹점 등록</span></div>'
          '<span style="font-size:8px;color:var(--fg-muted)">3개 중 1개 끝</span>', "150px"),
     "할 일 목록으로", "막지 않고 <b>옆에 두는</b> 방식. 요즘 많이 쓴다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 흐름의 계약서",
  code_lede="단계마다 <b>주소를 바꾸고</b>, 어디까지 왔는지 서버에 적어 둡니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"시작하기 단계"</span>&gt;
  &lt;<span class="t">ol</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/start/1"</span>&gt;이름&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;회사&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span>&gt;팀&lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ol</span>&gt;
&lt;/<span class="t">nav</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;3단계 중 2단계&lt;/<span class="t">p</span>&gt;

&lt;<span class="t">button</span>&gt;다음&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"ghost"</span>&gt;나중에 하기&lt;/<span class="t">button</span>&gt;

<span class="c">// 단계마다 서버에 적어 둔다 — 다시 들어와도 이어서</span>
<span class="k">await</span> fetch(<span class="s">'/api/onboarding'</span>, { method: <span class="s">'PATCH'</span>,
  body: JSON.stringify({ step: <span class="a">2</span>, skipped: [<span class="s">'team'</span>] }) });''',
  keys=kbd([
    ("단계마다 주소를 바꾼다", "<code>/start/2</code>. <b>뒤로가기</b>가 전 단계가 된다 — <a href=\"systemback.html\">시스템 백</a>"),
    ("<code>aria-current=\"step\"</code>", "지금 단계를 알린다. 색만으로는 안 읽힌다"),
    ("<code>role=\"status\"</code>", "'3단계 중 2단계'. 단계가 바뀐 것을 <b>눈으로 안 보는 사람</b>에게"),
    ("초점", "단계가 바뀌면 <b>새 제목</b>으로 초점을 옮긴다. 안 그러면 Tab 이 처음부터 돈다"),
    ("건너뛰기는 <code>&lt;button&gt;</code>", "약하게 보이되 <b>Tab 으로 닿아야</b> 한다"),
    ("자동으로 넘기지 않는다", "고르자마자 다음 단계로 가면 <b>고치러 돌아올 수</b> 없다"),
  ]),
  backend=rows([
    ("어디까지 했는지 저장", "브라우저에만 두면 기기를 바꿨을 때 <b>처음부터</b>가 됩니다. 계정에 붙여 둡니다."),
    ("건너뛴 것도 기록", "'안 한 것'과 '건너뛴 것'은 다릅니다. 건너뛴 것은 <b>나중에 다시 권할</b> 수 있습니다."),
    ("부분 저장", "단계마다 보내면 중간에 끊겨도 남습니다. 마지막에 한 번 보내면 <b>전부 날아갑니다</b>."),
    ("필수 값이 비어 있을 수 있다", "건너뛸 길을 주는 순간 <b>그 칸이 빈 계정</b>이 생깁니다. 뒤의 화면들이 그걸 견뎌야 합니다."),
    ("퍼널을 남긴다", "단계마다 지나간 수를 기록해 두면 <b>어디서 떨어지는지</b>가 보입니다. 이 숫자 없이는 고칠 데를 모릅니다."),
  ]),
  plat_lede="<b>앱은 한 번, 웹은 여러 번</b> 들어옵니다.",
  plats=plats([
    ("웹", "주소가 있는 단계",
     steps(4, 1, "110px"),
     "단계마다 주소가 있어 <b>뒤로가기·공유·새로고침</b>이 됩니다. 중간에 떠나도 링크로 돌아올 수 있습니다."),
    ("iOS", "모달 흐름",
     '''              <div class="phone" role="img" aria-label="iOS 온보딩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:5px;top:14px;font-size:6px;color:var(--accent)">건너뛰기</span>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:20px;border:1px solid var(--line);border-radius:3px"></div></div></div>''',
     "전체 화면 모달로 띄우고 <b>오른쪽 위에 건너뛰기</b>를 둡니다. 설치 직후 한 번만 보여 줍니다."),
    ("안드로이드", "전체 화면 흐름",
     '''              <div class="phone" role="img" aria-label="안드로이드 온보딩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:6px;display:flex;justify-content:center;gap:3px"><span style="width:4px;height:4px;border-radius:50%;background:var(--accent)"></span><span style="width:4px;height:4px;border-radius:50%;background:var(--line)"></span><span style="width:4px;height:4px;border-radius:50%;background:var(--line)"></span></div></div></div>''',
     "아래 <b>점 표시</b>로 몇 장인지 알리고 옆으로 넘깁니다. 뒤로가기가 전 장으로 가야 합니다."),
  ]),
  plat_note="\"첫 화면에서 몇 가지만 물어보죠\"로 시작한 온보딩이 여섯 단계가 되는 일이 흔합니다. 받을 때 <b>칸마다 '이게 없으면 첫 화면이 안 되나요'</b>를 물어보면, 대개 절반이 '나중에 물어도 되는 것'으로 넘어갑니다. 그 분류 한 번이 완료율을 가장 크게 움직입니다.",
  siblings=siblings("onboarding"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>''',
)
