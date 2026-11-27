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
  desc="처음 쓰는 사람이 제품을 쓸 수 있게 이끄는 흐름입니다. 단계가 늘수록 완료율이 떨어지는 계산과 건너뛸 길을 두는 법을 다룹니다.",
  lede="온보딩은 처음 온 사람이 제품을 <b>바로 쓸 수 있는 상태</b>까지 이끄는 흐름입니다. 단계마다 일부가 떠나기 때문에, 단계가 늘수록 <b>끝까지 오는 사람은 곱셈으로</b> 줄어듭니다.",
  axes_lede="화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>오른쪽 숫자는 실제 측정값이 아니라, '단계마다 같은 비율이 떠난다'고 가정하고 곱한 <b>계산</b>입니다.
          가정은 단순하지만 경향은 분명해서, 한 단계에서 15%만 떠나도 <b>여섯 단계를 지나면 절반 아래</b>만 남습니다.<br>
          <b>건너뛸 길 주기</b>를 켜면 떠나는 비율이 줄어듭니다. 막힌 사용자가 앱을 나가는 대신 <b>건너뛰기</b>를 누르기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "온보딩, 첫 설정, 시작하기, 둘러보기"),
    ("영어", "onboarding, first-run experience, setup wizard, product tour"),
    ("같이 쓰는 말",
     "입력을 여러 화면으로 나눠 받는 것을 <b>위저드</b>(wizard)·<b>스텝 폼</b>이라 하고, "
     "화면 위에 떠서 기능을 하나씩 짚어 주는 것을 <b>코치마크</b>(coach mark)·<b>프로덕트 투어</b>라고 합니다. "
     "앱을 처음 켰을 때의 경험 전체는 <b>FRE</b>(first-run experience)라 부르고, "
     "단계마다 몇 명이 남는지 그린 것은 <b>퍼널</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>튜토리얼</b> — 튜토리얼은 기능을 설명하는 것이고, 온보딩은 사용자가 <b>실제로 쓸 수 있는 상태</b>까지 이끄는 것입니다. 설명만 하고 끝나면 온보딩이 아니라 튜토리얼입니다.<br>"
     "<b>가입</b> — 계정을 만드는 데까지가 가입이고, 온보딩은 그다음부터 시작합니다.<br>"
     "<b>빈 상태</b> — <a href=\"../items/empty.html\">빈 상태</a>도 온보딩 중에 만나는 화면이지만, 온보딩이 흐름 전체를 다루는 반면 빈 상태는 <b>화면 하나</b>를 다룹니다."),
  ]),
  axes=ax("온보딩"),
  oneline="온보딩을 고칠 때는 <b>단계를 줄이는 일</b>부터 합니다. 단계를 더 잘 다듬는 것보다 <b>단계를 아예 지우는</b> 편이 거의 언제나 효과가 큽니다.",
  s4_title="흐름", s4_hint="끝이 보이나",
  states=states([
    (steps(4, 0, "152px", "1 / 4 — 끝이 보인다"), "시작", "전체가 <b>몇 단계인지</b> 처음부터 알려 줍니다"),
    (steps(4, 2, "152px", "3 / 4 — 두 개 끝냈다"), "진행 중", "지나온 단계에 ✓를 표시하고, 그 단계로 <b>돌아갈 수</b> 있게 합니다"),
    (card('<span style="font-size:9.5px">어떤 일을 하시나요?</span>'
          '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:9px;color:var(--fg-muted)">입력</div>'
          '<div style="display:flex;gap:4px"><span style="flex:1;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">다음</span>'
          '<span style="text-align:center;border:1px solid var(--line);border-radius:4px;padding:3px 8px;font-size:9px">건너뛰기</span></div>'),
     "건너뛸 길 ✓", "막힌 사용자가 앱을 <b>나가는 대신 누릅니다</b>"),
    (card('<span style="font-size:9.5px">어떤 일을 하시나요?</span>'
          '<div style="border:1px solid var(--line);border-radius:4px;padding:3px 6px;font-size:9px;color:var(--fg-muted)">입력</div>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">다음</span>'
          '<span style="font-size:8px;color:var(--danger)">나갈 길이 없다</span>'),
     "건너뛸 길 ✕", "막힌 사용자는 <b>앱을 닫고 떠납니다</b>"),
    (card('<span style="font-size:9.5px;font-weight:700">거의 다 됐습니다</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">설정에서 언제든 바꿀 수 있어요</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">시작하기</span>'),
     "끝", "<b>무엇이 남았는지</b>, 나중에 바꿀 수 있다는 것을 알려 줍니다"),
    (card('<span style="font-size:9.5px">2단계까지 하셨어요</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">이어서 하기</span>'),
     "다시 들어왔을 때", "<b>어디까지 했는지</b> 기억해 둡니다. 처음부터 다시 하라고 하면 사용자가 하지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계 표시", "2 / 4", "남은 단계가 <b>몇 개인지 보여야</b> 사용자가 끝까지 갑니다"),
    ("돌아가기", "← 이전", "이전 단계로 돌아가도 적은 값은 <b>그대로 남아</b> 있어야 합니다"),
    ("건너뛸 길", "나중에 하기", "버튼 하나만 더하면 되는 <b>가장 손쉬운 개선</b>입니다. 막힌 사용자가 나가는 대신 누릅니다"),
    ("이어 하기", "서버에 기록", "서버에 기록해 두어야 다시 들어왔을 때 <b>처음부터</b> 하지 않아도 됩니다"),
    ("나중에 채우기", "설정에서", "건너뛴 항목을 나중에 <b>어디서</b> 채우는지 알려 줍니다"),
    ("단계 수", "적을수록 좋다", "단계마다 일부가 떠나기 때문에 남는 사람은 <b>곱셈으로 줄어듭니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          온보딩에서 가장 자주 섞이는 두 가지가 <b>'우리가 알고 싶은 것'</b>과
          <b>'사용자가 쓰려면 필요한 것'</b>입니다.
          예를 들어 직군·회사 규모·유입 경로는 <b>우리가 알고 싶은 것</b>이고,
          사용자가 첫 화면을 쓰는 데 필요한 값은 아닙니다.
          그런 칸은 온보딩에서 빼고 <b>나중에 물어도</b> 되는데,
          칸을 이렇게 한 번 나눠 보기만 해도 대개 단계가 절반으로 줄어듭니다.</p>''',
  do=ul([
    "<b>쓰려면 꼭 필요한 값</b>만 받을 때",
    "첫 화면이 <b>텅 비어</b> 있을 때. 샘플을 하나 만들어 보여 줍니다",
    "권한이 필요할 때. <a href=\"permission.html\">권한 요청</a>의 앞선 설명을 이 자리에서 보여 줍니다",
  ]),
  dont=ul([
    "<b>우리가 알고 싶은 것</b>을 물을 때. 그런 값은 나중에 물어도 됩니다",
    "기능 설명 슬라이드를 다섯 장씩 넘기게 할 때. <b>대부분 읽지 않고 넘깁니다</b>",
    "건너뛸 길을 두지 않을 때. 막힌 사용자는 <b>앱을 닫습니다</b>",
    "다시 들어온 사용자에게 처음부터 다시 하게 할 때. 이어서 할 수 있도록 진행 상황을 <b>기록</b>해 둡니다",
  ]),
  instead='칸이 여럿이면 <a href="form.html">폼 설계</a>, 첫 화면이 비면 <a href="../items/empty.html">빈 상태</a>, 기능을 짚어 주려면 <a href="../items/popover.html">팝오버</a>.',
  cases=cases([
    (steps(3, 1, "150px", "3단계 — 알맞다"), "짧은 위저드", "단계가 셋을 넘으면 사용자가 <b>끝이 어디인지 가늠하기 어렵습니다</b>"),
    (card('<span style="font-size:9.5px;font-weight:700">첫 가맹점을 만들어 볼까요?</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">예시로 하나 만들어 뒀습니다</span>'
          '<span style="display:block;text-align:center;background:var(--accent);color:#fff;border-radius:4px;padding:3px 0;font-size:9px">보러 가기</span>', "150px"),
     "빈 화면 대신", "사용자에게 묻는 대신 예시를 <b>먼저 만들어 줍니다.</b> 온보딩 방식 가운데 가장 효과가 좋습니다"),
    (card('<div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border-radius:50%;border:1px solid var(--accent)"></span><span style="font-size:9px">프로필 채우기</span></div>'
          '<div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border-radius:50%;background:var(--accent)"></span><span style="font-size:9px;color:var(--fg-muted)">가맹점 등록</span></div>'
          '<span style="font-size:8px;color:var(--fg-muted)">3개 중 1개 끝</span>', "150px"),
     "할 일 목록으로", "화면을 막지 않고 할 일을 <b>옆에 두는</b> 방식으로, 요즘 많이 씁니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
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

<span class="c">// 단계마다 서버에 적어 두면 다시 들어와도 이어서 할 수 있다</span>
<span class="k">await</span> fetch(<span class="s">'/api/onboarding'</span>, { method: <span class="s">'PATCH'</span>,
  body: JSON.stringify({ step: <span class="a">2</span>, skipped: [<span class="s">'team'</span>] }) });''',
  keys=kbd([
    ("단계마다 주소를 바꾼다", "<code>/start/2</code>처럼 단계마다 주소를 두면 <b>뒤로가기</b>를 눌렀을 때 전 단계로 갑니다(<a href=\"systemback.html\">시스템 백</a>)"),
    ("<code>aria-current=\"step\"</code>", "지금 단계를 알립니다. 색으로만 표시하면 스크린 리더가 읽지 못합니다"),
    ("<code>role=\"status\"</code>", "'3단계 중 2단계'처럼 단계가 바뀐 것을 <b>화면을 눈으로 보지 않는 사람</b>에게도 알립니다"),
    ("초점", "단계가 바뀌면 <b>새 제목</b>으로 초점을 옮깁니다. 옮기지 않으면 Tab을 눌렀을 때 페이지 처음부터 다시 돕니다"),
    ("건너뛰기는 <code>&lt;button&gt;</code>", "눈에 덜 띄게 만들더라도 <b>Tab으로 갈 수 있어야</b> 합니다"),
    ("자동으로 넘기지 않는다", "고르자마자 다음 단계로 넘어가 버리면 잘못 고른 값을 <b>고치러 돌아올 수</b> 없습니다"),
  ]),
  backend=rows([
    ("어디까지 했는지 저장", "진행 상황을 브라우저에만 저장하면 기기를 바꿨을 때 <b>처음부터</b> 다시 해야 합니다. 그래서 계정에 붙여 저장합니다."),
    ("건너뛴 것도 기록", "'안 한 것'과 '건너뛴 것'은 따로 기록합니다. 건너뛴 것으로 남겨 두면 <b>나중에 다시 권할</b> 수 있습니다."),
    ("부분 저장", "단계마다 서버로 보내 두면 중간에 끊겨도 앞 단계의 값이 남습니다. 반면 마지막에 한 번에 보내면 끊겼을 때 <b>입력한 값을 전부 잃습니다</b>."),
    ("필수 값이 비어 있을 수 있다", "건너뛸 길을 두면 <b>그 칸이 빈 계정</b>이 생깁니다. 그래서 뒤에 나오는 화면들은 그 값이 비어 있어도 문제없이 동작해야 합니다."),
    ("퍼널을 남긴다", "단계마다 지나간 사람 수를 기록해 두면 <b>어느 단계에서 많이 떠나는지</b> 알 수 있습니다. 이 기록이 없으면 어느 단계를 고쳐야 할지 판단할 근거가 없습니다."),
  ]),
  plat_lede="플랫폼에 따라 온보딩에 들어오는 횟수가 다릅니다. <b>앱은 한 번, 웹은 여러 번</b> 들어옵니다.",
  plats=plats([
    ("웹", "주소가 있는 단계",
     steps(4, 1, "110px"),
     "단계마다 주소가 있어서 <b>뒤로가기·공유·새로고침</b>이 그대로 동작하고, 중간에 떠나도 링크로 돌아올 수 있습니다."),
    ("iOS", "모달 흐름",
     '''              <div class="phone" role="img" aria-label="iOS 온보딩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:5px;top:14px;font-size:6px;color:var(--accent)">건너뛰기</span>
                <div style="position:absolute;left:5px;right:5px;top:34px;height:20px;border:1px solid var(--line);border-radius:3px"></div></div></div>''',
     "전체 화면 모달로 띄우고 <b>오른쪽 위에 건너뛰기</b>를 둡니다. 설치 직후 한 번만 보여 줍니다."),
    ("안드로이드", "전체 화면 흐름",
     '''              <div class="phone" role="img" aria-label="안드로이드 온보딩 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:6px;display:flex;justify-content:center;gap:3px"><span style="width:4px;height:4px;border-radius:50%;background:var(--accent)"></span><span style="width:4px;height:4px;border-radius:50%;background:var(--line)"></span><span style="width:4px;height:4px;border-radius:50%;background:var(--line)"></span></div></div></div>''',
     "화면 아래 <b>점 표시</b>로 몇 장인지 알리고 옆으로 넘기게 합니다. 이때 뒤로가기를 누르면 전 장으로 돌아가야 합니다."),
  ]),
  plat_note="\"첫 화면에서 몇 가지만 물어보죠\"로 시작한 온보딩이 어느새 여섯 단계로 늘어나는 일이 흔합니다. 요청을 받을 때 <b>칸마다 '이게 없으면 첫 화면이 안 되나요'</b>라고 물어보면, 대개 절반은 '나중에 물어도 되는 것'으로 옮겨집니다. 칸을 이렇게 한 번 나누는 일이 완료율에 가장 큰 영향을 줍니다.",
  siblings=siblings("onboarding"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="permission.html"><b>권한 요청</b><em>13부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>''',
)
