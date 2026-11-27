# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양만 보고는 구별하기 어렵지만, 아래 네 가지를 따져 보면 어느 부품인지 가려낼 수 있습니다."

def cc(tips, label, note="", ok=None, w="152px", skip=True, hole=True):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    for (x, y, title, body) in tips:
        out.append('<span style="position:absolute;left:' + str(x) + 'px;top:' + str(y) + 'px;'
                   'border-radius:5px;background:var(--fg);color:var(--surface);padding:4px 6px;'
                   'font-size:7px;max-width:84px;z-index:4">'
                   '<b style="display:block;font-size:7.5px;margin-bottom:1px">' + title + '</b>' + body
                   + '<span style="display:flex;gap:5px;margin-top:3px;font-size:6.5px">'
                   + ('<span style="text-decoration:underline">건너뛰기</span>' if skip else '')
                   + '<span style="margin-left:auto;font-weight:700">다음</span></span></span>')
    hl = ('<span style="position:absolute;left:6px;top:6px;width:42px;height:13px;border-radius:3px;'
          'box-shadow:0 0 0 9999px color-mix(in srgb, var(--fg) 50%, transparent);z-index:2"></span>'
          if hole else
          '<span style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 50%, transparent);z-index:2"></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<span style="position:absolute;left:6px;top:6px;border:1px solid var(--line);border-radius:3px;'
            'padding:1px 5px;font-size:7px;background:var(--surface);z-index:3">내보내기</span>'
            '<span style="position:absolute;right:6px;top:6px;border:1px solid var(--line);border-radius:3px;'
            'padding:1px 5px;font-size:7px;background:var(--surface)">필터 ▾</span>'
            '<span style="position:absolute;left:6px;bottom:6px;border:1px solid var(--line);border-radius:3px;'
            'padding:1px 5px;font-size:7px;background:var(--surface)">도움말</span>'
            + hl + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">한 번에 하나만 짚는다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">구멍 — 짚는 것만 밝게 남긴다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">몇 번째인지 — 1 / 4</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">건너뛸 길 — 없으면 갇힌다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--danger)">한 번만 띄운다 — 본 사람에게 또 띄우지 않는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">같은 설명을 도움말에도 남긴다</div>
                </div>
              </div>'''

D = dict(
  slug="coachmark", ko="코치마크", en="Coach mark · product tour",
  desc="처음 쓰는 사람에게 화면의 한 곳을 짚어 설명하는 겹침 부품입니다. 한 번만 띄우는 법과 건너뛸 길을 두어야 하는 이유를 다룹니다.",
  lede="코치마크는 처음 쓰는 사람에게 화면의 <b>한 곳을 짚어</b> 그 기능을 설명하는 말풍선입니다. 한 번에 여러 곳을 짚으면 읽을 말풍선이 한꺼번에 늘어나서 <b>어느 것도 제대로 읽히지 않습니다</b>.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>한 번에 짚는 수를 늘려 보세요. <b>한꺼번에 읽어야 하는 말풍선 수</b>를 데모가 세어 적습니다.
          말풍선이 둘을 넘으면 사람들은 <b>어느 것도 제대로 읽지 않습니다</b>.<br>
          <b>건너뛸 길</b>을 끄고 다시 보면 '다음'만 누를 수 있어서, 안내가 끝날 때까지 빠져나갈 수 없습니다.
          데모는 빠져나갈 수 있는 길의 수도 셉니다.<br>
          코치마크는 <b>한 번만</b> 보여 줘야 합니다. 한 번 본 사람에게는 다시 띄우지 않고,
          다시 봐야 할 때를 대비해 <b>도움말</b> 안에 같은 설명을 남겨 둡니다.</p>
        </div>''',
  names=rows([
    ("한국어", "코치마크, 안내 말풍선, 기능 투어, 스포트라이트"),
    ("영어", "coach mark, product tour, onboarding tooltip, spotlight"),
    ("같이 쓰는 말",
     "코치마크 여러 개를 차례로 이어 붙인 것은 <b>프로덕트 투어</b>(product tour), "
     "짚는 곳만 밝게 남기는 효과는 <b>스포트라이트</b>라고 합니다. "
     "새 기능 하나만 알리는 작은 점은 <b>뉴 뱃지</b>나 <b>힌트 점</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>툴팁</b> — 사용자가 대상을 <b>가리켜야</b> 뜨고 설명만 담으면 코치마크가 아니라 <a href=\"tooltip.html\">툴팁</a>입니다.<br>"
     "<b>온보딩</b> — <a href=\"onboarding.html\">온보딩</a>은 처음 쓰는 사람을 안내하는 <b>흐름 전체</b>를 가리키고, 코치마크는 그 흐름에 쓰는 방법 가운데 하나입니다.<br>"
     "<b>모달</b> — 처음 들어왔을 때 한 장 띄우는 설명 화면은 코치마크가 아니라 <b>모달</b>입니다."),
  ]),
  axes=axis_table("코치마크"),
  oneline="코치마크는 <b>한 번에 하나씩, 모두 합쳐 셋까지</b>만 띄웁니다. 그보다 많으면 사람들이 끝까지 읽지 않습니다.",
  states=states([
    (cc([(16, 26, '여기서 내보내요', '엑셀로 받을 수 있습니다')], "", "하나만 짚는다", True),
     "하나", "한 곳만 짚으면 말풍선이 <b>읽힙니다</b>"),
    (cc([(10, 24, '내보내기', '엑셀로'), (66, 24, '필터', '좁혀 보기'),
         (10, 48, '도움말', '막히면 여기')], "", "셋을 한꺼번에 — 아무것도 안 읽는다", False, "152px", True, False),
     "여럿", "세 곳을 한꺼번에 짚으면 <b>어느 것도 읽지 않습니다</b>"),
    (cc([(16, 26, '여기서 내보내요', '1 / 4')], "", "몇 번째인지 보인다", True),
     "몇 번째", "1 / 4처럼 적어 두면 <b>얼마나 남았는지</b> 알 수 있습니다"),
    (cc([(16, 26, '여기서 내보내요', '엑셀로')], "", "건너뛸 길이 없다", False, "152px", False),
     "건너뛰기 없음", "'다음'만 있으면 안내가 끝날 때까지 <b>빠져나갈 수 없습니다</b>"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">이미 본 사람</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">다시 안 띄운다</span>'),
         "본 적 있음", True, "", "152px"),
     "두 번째부터", "이미 본 사람에게는 <b>다시 띄우지 않습니다</b>"),
    (one(txt('<span style="display:block;font-size:8px">도움말 › 내보내기</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">같은 설명이 여기에도 있다</span>'),
         "도움말", True, "", "152px"),
     "나중에 찾을 때", "같은 설명을 <b>도움말</b>에 남겨 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("하나씩", "한 번에 하나", "말풍선이 한꺼번에 둘만 떠도 사람들이 <b>읽지 않습니다</b>"),
    ("구멍", "짚는 것만 밝게", "짚는 곳만 밝게 남기면 어디를 설명하는지 <b>분명해집니다</b>"),
    ("몇 번째", "1 / 4", "전체 가운데 몇 번째인지 보여 주면 얼마나 남았는지 알 수 있습니다"),
    ("건너뛰기", "있어야 함", "건너뛰기가 없으면 안내가 끝날 때까지 <b>빠져나갈 수 없습니다</b>"),
    ("한 번만", "본 뒤엔 안 띄움", "본 적이 있는지 <b>기억</b>해 두고 다시 띄우지 않습니다"),
    ("도움말", "같은 설명", "나중에 다시 <b>찾을 수 있게</b> 도움말에도 같은 설명을 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          코치마크는 <b>만드는 쪽은 편하지만 쓰는 쪽은 불편한</b> 대표적인 부품입니다.
          화면을 고치지 않고도 설명을 덧붙일 수 있어서 만드는 쪽은 자꾸 코치마크를 쓰게 되는데,
          사용자는 <b>빨리 시작하고 싶어서</b> 대부분 건너뜁니다.<br>
          그래서 코치마크를 붙이고 싶어지면, 먼저 그 기능이
          <b>화면만으로는 알기 어려운 이유</b>를 찾아보는 것이 좋습니다.
          단추 이름이 모호하거나, 단추가 엉뚱한 자리에 있거나, 빈 상태 화면에 아무 안내가 없는 경우가 많습니다.
          이런 원인을 고치면 코치마크로 설명을 덧붙일 필요가 없어집니다.</p>''',
  do=ul([
    "<b>한 번에 하나씩</b>, 모두 합쳐 셋까지만 띄우기",
    "<b>건너뛸 길</b>을 늘 두기",
    "같은 설명을 <b>도움말</b>에도 남기기",
  ]),
  dont=ul([
    "처음 들어오자마자 <b>다섯 단계</b> 띄우기",
    "<b>건너뛰기 없이</b> 다음으로만 가게 하기",
    "이미 본 사람에게 <b>또</b> 띄우기",
    "화면을 고치는 대신 <b>설명을 덧붙이기</b>",
  ]),
  instead='가리켜야 뜨면 <a href="tooltip.html">툴팁</a>, 흐름 전체는 <a href="onboarding.html">온보딩</a>, 빈 화면에서 가르치면 <a href="empty.html">빈 상태</a>, 기능이 많으면 <a href="commandpalette.html">커맨드 팔레트</a>.',
  cases=cases([
    (cc([(16, 26, '여기서 내보내요', '1 / 2')], "", "", True, "150px"), "새 기능", "새로 생긴 기능 <b>하나만</b> 짚어 알립니다"),
    (one(txt('<span style="display:block;font-size:8px">내보내기 <span style="color:var(--accent)">●</span></span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">점 하나로도 충분할 때가 있다</span>'),
         "힌트 점", True, "", "150px"),
     "작은 알림", "말풍선 없이 <b>점 하나</b>만 찍어도 충분할 때가 있습니다"),
    (one(txt('<span style="display:block;font-size:8px">아직 정산이 없습니다</span>'
             '<span style="display:block;font-size:8px;color:var(--accent);margin-top:2px">첫 가게 등록하기 ›</span>'),
         "빈 상태로", True, "설명 대신 할 일을 준다", "150px"),
     "빈 화면", "설명을 띄우기보다 할 일을 보여 주는 <a href=\"empty.html\">빈 상태</a>가 더 낫습니다"),
  ]),
  code_lede="말풍선에는 <code>role=\"dialog\"</code>를 붙이고, 사용자가 투어를 <b>본 적이 있는지</b> 꼭 저장해 둡니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"coach"</span> <span class="a">role</span>=<span class="s">"dialog"</span> <span class="a">aria-label</span>=<span class="s">"여기서 내보내요"</span>&gt;
  &lt;<span class="t">b</span>&gt;여기서 내보내요&lt;/<span class="t">b</span>&gt;
  &lt;<span class="t">p</span>&gt;정산 내역을 엑셀로 받을 수 있습니다.&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">p</span>&gt;1 / 4&lt;/<span class="t">p</span>&gt;
  &lt;<span class="t">button</span> <span class="a">data-skip</span>&gt;건너뛰기&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">data-next</span>&gt;다음&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">/* 짚는 곳만 밝게 남긴다. 바깥은 큰 그림자 한 줄로 어둡게 덮는다 */</span>
.coach-hole { <span class="a">box-shadow</span>: <span class="a">0</span> <span class="a">0</span> <span class="a">0</span> <span class="a">9999px</span> <span class="a">rgba</span>(20, 22, 26, <span class="a">.5</span>); }

<span class="c">// 한 번만 띄운다. 본 뒤에는 다시 띄우지 않는다</span>
<span class="t">if</span> (!localStorage.getItem(<span class="s">'tour:v2'</span>)) startTour();
<span class="t">function</span> endTour() { localStorage.setItem(<span class="s">'tour:v2'</span>, <span class="s">'done'</span>); }''',
  keys=kbd([
    ("Esc", "<b>건너뛰기</b>를 누른 것과 같이 투어를 끝냅니다"),
    ("Tab", "초점이 말풍선 안에서만 돌아서 <b>건너뛰기와 다음</b> 두 단추 사이를 오갑니다"),
    ("초점", "투어를 열면 초점을 <b>말풍선</b>으로 옮기고, 끝나면 <b>짚던 요소</b>로 돌려놓습니다"),
    ("<code>aria-describedby</code>", "짚는 요소와 말풍선을 이 속성으로 <b>연결해</b> 둘 수도 있습니다"),
    ("모션", "<a href=\"reducedmotion.html\">모션 줄이기</a>를 켠 사람에게는 <b>움직임을 끕니다</b>"),
    ("확인하는 법", "Esc 키만으로 <b>빠져나갈 수 있는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("본 적이 있나", "본 적이 있다는 기록을 계정에 저장하면 <b>다른 기기에서도</b> 다시 뜨지 않습니다. 반면 브라우저 저장소에만 저장하면 기기를 바꿀 때마다 또 뜹니다."),
    ("투어 버전", "<code>tour:v2</code>처럼 저장하는 이름에 버전을 붙여 두면, 기능이 바뀌었을 때 <b>바뀐 기능만</b> 다시 안내할 수 있습니다."),
    ("누구에게", "이미 그 기능을 써 본 사람에게는 <b>안 띄우는</b> 것이 맞습니다."),
  ]),
  plat_lede="코치마크는 대개 <b>정식 부품이 없어서</b> 직접 만듭니다.",
  plats=plats([
    ("웹", "직접 만듦",
     cc([(16, 26, '여기서 내보내요', '1 / 4')], "", "", True, "110px"),
     "투어를 만드는 라이브러리는 많지만, <b>한 번만 띄우기</b>는 직접 챙겨야 합니다."),
    ("iOS", "TipKit",
     '''              <div class="phone" role="img" aria-label="iOS 팁 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:16px;border-radius:4px;background:var(--fg);opacity:.9"></div></div></div>''',
     "팁을 <b>언제, 몇 번 띄울지</b>까지 OS가 규칙으로 관리해 줍니다(iOS 17 이상)."),
    ("안드로이드", "Tooltip · 직접",
     '''              <div class="phone" role="img" aria-label="안드로이드 팁 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:14px;border-radius:4px;background:var(--fg);opacity:.9"></div></div></div>''',
     "정식 부품이 드물어서 대개 직접 만들고, 짚는 곳만 밝게 남기는 효과도 직접 그립니다."),
  ]),
  plat_note="iOS의 <b>TipKit</b>에서 눈여겨볼 점은 팁을 '어떻게 그릴지'보다 <b>'언제, 몇 번 띄울지'</b>를 OS가 관리해 준다는 것입니다. 같은 팁은 세 번까지만 띄우고 다른 팁과 겹치지 않게 하는 식의 규칙을 모든 앱이 똑같이 따릅니다. 웹에는 이런 장치가 없기 때문에 <b>우리가 직접 그 규칙을 만들어야</b> 합니다. 적어도 <b>한 번만 띄우기</b>와 <b>겹쳐 띄우지 않기</b>, 이 두 가지는 정해 두는 편이 좋습니다.",
  siblings=siblings("coachmark"),
  related='''        <li><a href="tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="onboarding.html"><b>온보딩</b><em>13부</em></a></li>
        <li><a href="empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="reducedmotion.html"><b>모션 줄이기</b><em>9부</em></a></li>''',
)
