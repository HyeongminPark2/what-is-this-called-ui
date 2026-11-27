# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def btn(label, kind="primary", w=""):
    if kind == 'primary':
        st = 'background:var(--accent);color:#fff;border:1px solid var(--accent);'
    elif kind == 'ghost':
        st = 'background:var(--surface);color:var(--fg);border:1px solid var(--line);'
    elif kind == 'danger':
        st = 'background:var(--danger);color:#fff;border:1px solid var(--danger);'
    elif kind == 'danger-ghost':
        st = 'background:var(--surface);color:var(--danger);border:1px solid var(--danger);'
    else:
        st = 'background:none;color:var(--accent);border:1px solid transparent;'
    return ('<span style="' + st + 'border-radius:4px;padding:3px 8px;font-size:8px;white-space:nowrap">'
            + label + '</span>')

def row(btns, label, note="", ok=None, w="152px"):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;gap:4px;flex-wrap:wrap;align-items:center;border:1px solid ' + c + ';'
            'border-radius:6px;background:var(--surface);padding:6px">' + ''.join(btns) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">주 버튼은 한 화면에 하나만</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">보조 버튼은 테두리만 그림</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">텍스트 버튼은 가장 약하게 표시</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">위험한 동작은 빨갛게 하되 주 버튼으로 두지 않음</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">주 동작은 늘 같은 쪽에 둠</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">진한 버튼이 둘이면 주 동작을 알 수 없음</div>
                </div>
              </div>'''

D = dict(
  slug="buttonlevel", ko="버튼 위계", en="Button hierarchy",
  s4_title="버튼 배치", s4_hint="버튼을 늘어놓는 방식에 따라 달라지는 위계",
  do_title="버튼 위계를 잡을 때 지킬 것", dont_title="버튼 위계를 잡을 때 피할 것", instead_title="함께 보면 좋은 항목",
  desc="버튼을 주 · 보조 · 텍스트 · 위험 네 단계로 나누는 규칙과, 진한 버튼을 하나만 두는 이유를 보여 주는 항목입니다.",
  lede="버튼 위계는 화면에서 <b>사용자의 눈이 어느 버튼으로 먼저 가는지</b>를 정하는 일입니다. 진한 버튼이 둘이면 어느 쪽으로도 눈이 먼저 가지 않아서 <b>둘 다 주 동작으로 읽히지 않습니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>주 버튼 수를 늘려 보세요. 데모가 <b>가장 진한 버튼이 몇 개인지</b> 세어서,
          둘을 넘으면 '어느 것이 주 동작인지 알 수 없다'고 적습니다.<br>
          <b>위험한 동작을 주 버튼으로</b>를 켜면 가장 눈에 띄는 자리에 '지우기'가 오는데,
          그 자리는 실수로 누르기도 가장 쉬운 곳입니다.<br>
          주 동작을 왼쪽과 오른쪽 중 <b>어느 쪽에 둘지</b>는 한 서비스 안에서 <b>한쪽으로 고정</b>해야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버튼 위계, 버튼 단계, 주 버튼 · 보조 버튼"),
    ("영어", "button hierarchy, primary/secondary button, call to action"),
    ("같이 쓰는 말",
     "가장 진한 버튼은 <b>프라이머리</b>, 테두리만 있는 버튼은 <b>세컨더리</b>·<b>아웃라인</b>, "
     "바탕도 테두리도 없는 버튼은 <b>텍스트 버튼</b>·<b>고스트</b>라고 부릅니다. "
     "되돌릴 수 없는 일에 쓰는 빨간 버튼은 <b>데스트럭티브</b>(destructive), "
     "그 화면에서 사용자가 가장 해 주기를 바라는 동작은 <b>CTA</b>(call to action)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>색</b> — 위계를 가르는 것은 <b>색이 아니라 세기</b>입니다. 같은 파랑이라도 바탕을 채우면 주 버튼, 테두리만 두르면 보조 버튼입니다.<br>"
     "<b>크기</b> — 버튼 크기로 위계를 나누면 작은 버튼이 <a href=\"touchtarget.html\">터치 타깃</a> 기준에 못 미치게 됩니다.<br>"
     "<b>링크</b> — <a href=\"linkbutton.html\">링크와 버튼</a>은 세기가 아니라 <b>뜻</b>이 다릅니다."),
  ]),
  states=states([
    (row([btn('저장'), btn('취소', 'ghost')], "", "주 버튼 하나와 보조 하나", True),
     "주 버튼 하나와 보조 버튼 하나", "<b>하나만</b> 진합니다"),
    (row([btn('저장'), btn('임시 저장'), btn('취소', 'ghost')], "", "둘 다 진함", False),
     "주 버튼이 둘일 때", "주 동작이 <b>어느 쪽인지</b> 알 수 없습니다"),
    (row([btn('저장'), btn('취소', 'ghost'), btn('지우기', 'danger-ghost')], "", "위험한 동작은 약하게", True),
     "위험한 동작이 함께 있을 때", "<b>빨갛되 약하게</b> 표시합니다"),
    (row([btn('지우기', 'danger'), btn('취소', 'ghost')], "", "되묻는 창에서만 이렇게 둠", None),
     "되묻는 확인 창 안에서", "되묻는 창 안에서는 <b>지우기가 주 버튼</b>입니다"),
    (row([btn('저장'), btn('취소', 'text'), btn('도움말', 'text')], "", "덜 중요한 동작은 글자로만", True),
     "덜 중요한 동작에 텍스트 버튼", "<b>가장 약하게</b> 보입니다"),
    (row([btn('취소', 'ghost'), btn('저장')], "", "주 동작을 오른쪽에 둠", True),
     "주 동작의 자리 고정하기", "주 동작의 자리를 한쪽으로 <b>고정</b>합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("주 버튼", "한 화면에 하나", "한 화면에 <b>하나만</b> 둡니다"),
    ("보조 버튼", "테두리만 그림", "주 동작과 함께 놓이는 동작에 씁니다"),
    ("텍스트 버튼", "가장 약한 단계", "덜 중요한 동작에 씁니다"),
    ("위험한 동작", "빨간색이지만 약한 세기", "<b>주 버튼으로</b> 두지 않습니다"),
    ("주 동작의 자리", "늘 같은 쪽", "화면마다 자리가 바뀌면 사용자가 <b>헷갈립니다</b>"),
    ("진한 버튼이 둘일 때", "주 동작이 드러나지 않음", "둘 중 하나를 보조 버튼으로 <b>내립니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '둘 다 중요하니 둘 다 진하게' 두는 것이 가장 흔한 실수입니다.
          그런데 두 버튼이 똑같이 진하면 <b>사용자의 눈이 어느 쪽으로도 먼저 가지 않아서</b>,
          결국 둘 다 평범한 버튼과 다를 바 없어집니다.
          정말 둘 다 중요하다면 둘을 함께 진하게 두지 말고
          <b>화면을 나눠</b> 화면마다 주 동작을 하나씩 두는 편이 낫습니다.<br>
          위험한 동작을 주 버튼으로 두는 경우도 자주 보는데,
          그렇게 해도 되는 곳은 <b>되묻는 창 안</b>뿐입니다.
          목록이나 상세 화면에서는 '지우기'가 가장 눈에 띄면 안 됩니다.</p>''',
  do=ul([
    "한 화면에는 <b>진한 버튼을 하나만</b> 두기",
    "위험한 동작은 <b>빨간색으로 하되 약하게</b> 표시하기",
    "주 동작의 <b>좌우 자리</b>를 서비스 안에서 고정하기",
  ]),
  dont=ul([
    "진한 버튼을 <b>둘</b> 두기. 어느 쪽도 주 동작으로 읽히지 않습니다",
    "크기로 위계 나누기. <b>작은 버튼</b>은 손가락으로 누르기 어렵습니다",
    "'지우기'를 <b>주 버튼</b>으로 두기(확인 창 제외)",
    "화면마다 <b>자리를 바꾸기</b>",
  ]),
  instead='이동과 동작처럼 뜻을 가르는 문제는 <a href="linkbutton.html">링크와 버튼</a>에서, 버튼에 다른 동작 갈래가 붙는 경우는 <a href="splitbutton.html">분할 버튼</a>에서 다룹니다. 되돌릴 수 없는 일을 다루는 방법은 <a href="destructive.html">위험한 동작</a>, 버튼 색 자체를 정하는 기준은 <a href="statecolor.html">상태 색</a> 항목에 있습니다.',
  cases=cases([
    (row([btn('저장'), btn('취소', 'ghost')], "", "", True, "150px"), "폼에서 저장하기", "<b>저장 버튼 하나</b>만 진하게 둡니다"),
    (row([btn('결제하기')], "", "", True, "150px"), "결제 화면", "결제하기 버튼 <b>하나만</b> 둡니다"),
    (row([btn('지우기', 'danger'), btn('취소', 'ghost')], "", "", None, "150px"), "지우기 전에 되묻는 창", "되묻는 창에서는 <b>지우기가 주 버튼</b>입니다"),
  ]),
  code_lede="버튼의 세기는 <b>클래스 하나</b>로 나눕니다. 색을 버튼마다 따로 적지 않습니다.",
  code='''&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"btn btn--primary"</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"btn"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"btn btn--text"</span>&gt;도움말&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"btn btn--danger"</span>&gt;지우기&lt;/<span class="t">button</span>&gt;

.btn { <span class="a">background</span>: <span class="a">var</span>(--color-bg-surface); <span class="a">color</span>: <span class="a">var</span>(--color-text);
  <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--color-border); <span class="a">min-height</span>: <span class="a">44px</span>; }
.btn--primary { <span class="a">background</span>: <span class="a">var</span>(--color-bg-brand); <span class="a">color</span>: <span class="a">var</span>(--color-text-onbrand);
  <span class="a">border-color</span>: transparent; }
.btn--text    { <span class="a">background</span>: none; <span class="a">border-color</span>: transparent; <span class="a">color</span>: <span class="a">var</span>(--color-text-brand); }
.btn--danger  { <span class="a">color</span>: <span class="a">var</span>(--color-text-danger); <span class="a">border-color</span>: <span class="a">var</span>(--color-border-danger); }''',
  keys=kbd([
    ("Tab", "세기와 상관없이 <b>마크업 순서대로</b> 멈춥니다"),
    ("Enter · Space", "버튼을 누릅니다. <code>&lt;button&gt;</code> 요소라면 따로 만들지 않아도 <b>저절로</b> 동작합니다"),
    ("<code>type=\"button\"</code>", "폼 안에서는 꼭 적어 둡니다. 적지 않으면 버튼을 눌렀을 때 폼이 <b>제출</b>됩니다"),
    ("<code>autofocus</code>", "쓰지 않습니다. 사용자가 보던 곳에서 초점을 <b>가져가 버립니다</b>"),
    ("<code>44px</code>", "세기를 낮춰도 <b>크기는 줄이지 않습니다</b>"),
    ("위계를 확인하는 방법", "화면을 흑백으로 바꿔도 <b>어느 것이 주 버튼인지</b> 보인다면 위계를 잘 나눈 것입니다"),
  ]),
  backend=rows([
    ("사용자에게 권한이 있는지", "사용자에게 권한이 없으면 <b>단추를 아예 지웁니다</b>. 흐리게만 두면 사용자가 '왜 안 되나'를 묻게 됩니다."),
    ("두 번 눌리지 않게 막기", "주 버튼은 요청을 보내는 동안 <b>잠가</b> 두어 두 번 눌리지 않게 합니다. 이 처리는 <a href=\"success.html\">성공 확인</a>과 함께 설계합니다."),
  ]),
  plat_lede="플랫폼이 달라도 <b>버튼의 세기를 나누는 방식</b>은 같고, 단계의 이름만 다릅니다.",
  plats=plats([
    ("웹", "CSS 클래스로 구분",
     row([btn('저장'), btn('취소', 'ghost')], "", "", True, "110px"),
     "표준으로 정해진 이름이 없어서 팀마다 다르게 부르므로, 팀 안에서 이름을 <b>먼저 정해 두는</b> 편이 낫습니다."),
    ("iOS", "borderedProminent 등",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;height:11px;border-radius:5px;background:var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;bottom:25px;height:11px;border-radius:5px;border:1px solid var(--line)"></div></div></div>''',
     "<code>.borderedProminent</code> · <code>.bordered</code> · <code>.plain</code> 세 단계가 있습니다."),
    ("안드로이드", "Filled · Outlined · Text",
     '''              <div class="phone" role="img" aria-label="안드로이드 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:5px;bottom:10px;width:30px;height:11px;border-radius:999px;background:var(--accent)"></div>
                <div style="position:absolute;right:40px;bottom:10px;width:24px;height:11px;border-radius:999px;border:1px solid var(--line)"></div></div></div>''',
     "Material 지침이 <b>Filled · Tonal · Outlined · Text · Elevated</b> 다섯 단계를 정해 두었습니다."),
  ]),
  plat_note="Material 의 <b>다섯 단계</b>는 많아 보이지만, 그 가운데 <b>토널</b>(연한 바탕) 버튼은 실제로 쓸모가 큽니다. 주 버튼만큼 세지 않으면서도 테두리만 있는 버튼보다는 눈에 잘 띄기 때문입니다. 웹에서도 단계를 하나 더 둔다면 토널 버튼이 가장 쓸 만합니다. 다만 단계가 늘수록 <b>어느 것을 쓸지 고민</b>도 늘어나므로, 세 단계로 시작해 모자랄 때 늘리는 편이 좋습니다.",
  siblings=siblings("buttonlevel"),
  related='''        <li><a href="linkbutton.html"><b>링크와 버튼</b><em>4부</em></a></li>
        <li><a href="splitbutton.html"><b>분할 버튼</b><em>4부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="buttontext.html"><b>버튼 문구</b><em>14부</em></a></li>''',
)
