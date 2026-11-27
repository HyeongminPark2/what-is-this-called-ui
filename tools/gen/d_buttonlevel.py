# -*- coding: utf-8 -*-
from ax4 import ax
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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">주 버튼 — 한 화면에 하나</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">보조 버튼 — 테두리만</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">텍스트 버튼 — 가장 약하게</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">위험한 동작 — 빨갛되 주 버튼으로 두지 않는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">자리 — 주 동작을 늘 같은 쪽에</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">진한 버튼이 둘이면 둘 다 안 읽힌다</div>
                </div>
              </div>'''

D = dict(
  slug="buttonlevel", ko="버튼 위계", en="Button hierarchy",
  desc="주 · 보조 · 텍스트 · 위험 네 단계로 버튼을 나누는 규칙. 하나만 진하게 두는 이유.",
  lede="버튼 위계는 <b>눈이 어디로 먼저 가는가</b>를 정하는 일입니다. 진한 버튼이 둘이면 <b>둘 다 안 읽힙니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>주 버튼을 늘려 보세요 — 데모가 <b>가장 진한 버튼이 몇 개인지</b> 세고,
          둘을 넘으면 '어느 것이 주 동작인지 알 수 없다'고 적습니다.<br>
          <b>위험한 동작을 주 버튼으로</b> 켜면 가장 눈에 띄는 자리에 '지우기'가 옵니다 —
          실수로 누르기 가장 쉬운 자리입니다.<br>
          주 동작의 <b>좌우 자리</b>는 한 서비스 안에서 <b>한 쪽으로 고정</b>하는 것이 중요합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버튼 위계, 버튼 단계, 주 버튼 · 보조 버튼"),
    ("영어", "button hierarchy, primary/secondary button, call to action"),
    ("같이 쓰는 말",
     "가장 진한 것이 <b>프라이머리</b>, 테두리만 있는 것이 <b>세컨더리</b>·<b>아웃라인</b>, "
     "바탕도 테두리도 없는 것이 <b>텍스트 버튼</b>·<b>고스트</b>입니다. "
     "되돌릴 수 없는 일에 쓰는 빨간 버튼은 <b>데스트럭티브</b>(destructive), "
     "화면에서 가장 바라는 동작은 <b>CTA</b>(call to action)라 부릅니다."),
    ("자주 잘못 부름",
     "<b>색</b> — 위계는 <b>색이 아니라 세기</b>입니다. 같은 파랑이라도 채우면 주, 테두리만이면 보조입니다.<br>"
     "<b>크기</b> — 크기로 위계를 내면 <a href=\"touchtarget.html\">터치 타깃</a>이 어긋납니다.<br>"
     "<b>링크</b> — <a href=\"linkbutton.html\">링크와 버튼</a>은 <b>뜻</b>이 다른 것이지 세기가 아닙니다."),
  ]),
  axes=ax("버튼 위계"),
  oneline="<b>한 화면에 진한 버튼은 하나.</b> 둘을 쓰고 싶으면 하나를 보조로 내리세요.",
  states=states([
    (row([btn('저장'), btn('취소', 'ghost')], "", "주 하나 · 보조 하나", True),
     "기본", "<b>하나만</b> 진하다"),
    (row([btn('저장'), btn('임시 저장'), btn('취소', 'ghost')], "", "둘 다 진하다", False),
     "주가 둘", "<b>어느 쪽인지</b> 모른다"),
    (row([btn('저장'), btn('취소', 'ghost'), btn('지우기', 'danger-ghost')], "", "위험한 것은 약하게", True),
     "위험한 동작", "<b>빨갛되 약하게</b>"),
    (row([btn('지우기', 'danger'), btn('취소', 'ghost')], "", "되묻는 창에서만 이렇게", None),
     "확인 창", "거기서는 <b>지우기가 주</b>"),
    (row([btn('저장'), btn('취소', 'text'), btn('도움말', 'text')], "", "덜 중요한 것은 글자만", True),
     "텍스트 버튼", "<b>가장 약하게</b>"),
    (row([btn('취소', 'ghost'), btn('저장')], "", "주 동작이 오른쪽", True),
     "자리", "한 쪽으로 <b>고정</b>한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("주 버튼", "하나", "한 화면에 <b>하나</b>"),
    ("보조 버튼", "테두리만", "같이 쓰는 동작"),
    ("텍스트 버튼", "가장 약하게", "덜 중요한 것"),
    ("위험한 동작", "빨갛되 약하게", "<b>주 버튼으로</b> 두지 않는다"),
    ("자리", "늘 같은 쪽", "화면마다 바뀌면 <b>헷갈린다</b>"),
    ("둘이면", "안 읽힌다", "하나를 <b>내린다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          '둘 다 중요해서 둘 다 진하게' 가 가장 흔한 실수입니다.
          그런데 둘이 똑같이 진하면 <b>눈이 어느 쪽도 먼저 고르지 못하고</b>,
          결국 둘 다 그냥 버튼이 됩니다.
          정말 둘 다 중요하다면 <b>화면을 나누는 것</b>이 답이지
          둘을 같이 진하게 두는 것이 답은 아닙니다.<br>
          위험한 동작을 주 버튼으로 두는 것도 자주 봅니다 —
          <b>되묻는 창 안에서만</b> 그게 맞습니다.
          목록이나 상세 화면에서는 '지우기'가 가장 눈에 띄면 안 됩니다.</p>''',
  do=ul([
    "한 화면에 <b>진한 버튼 하나</b>",
    "위험한 동작은 <b>빨갛되 약하게</b>",
    "주 동작의 <b>좌우 자리</b>를 서비스 안에서 고정하기",
  ]),
  dont=ul([
    "진한 버튼을 <b>둘</b> 두기 — 둘 다 안 읽힌다",
    "크기로 위계 내기 — <b>작은 버튼</b>이 안 눌린다",
    "'지우기'를 <b>주 버튼</b>으로 두기(확인 창 제외)",
    "화면마다 <b>자리를 바꾸기</b>",
  ]),
  instead='뜻이 다른 것은 <a href="linkbutton.html">링크와 버튼</a>, 갈래가 붙으면 <a href="splitbutton.html">분할 버튼</a>, 되돌릴 수 없는 일은 <a href="destructive.html">위험한 동작</a>, 색 자체는 <a href="statecolor.html">상태 색</a>.',
  cases=cases([
    (row([btn('저장'), btn('취소', 'ghost')], "", "", True, "150px"), "폼", "<b>저장 하나</b>만 진하게"),
    (row([btn('결제하기')], "", "", True, "150px"), "결제", "<b>하나만</b> 둔다"),
    (row([btn('지우기', 'danger'), btn('취소', 'ghost')], "", "", None, "150px"), "되묻는 창", "여기서는 <b>지우기가 주</b>"),
  ]),
  code_lede="세기는 <b>클래스 하나</b>로 가릅니다 — 색을 자리마다 적지 않습니다.",
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
    ("Tab", "세기와 상관없이 <b>차례대로</b> 멈춘다 — 마크업 순서가 차례다"),
    ("Enter · Space", "버튼을 누른다. <code>&lt;button&gt;</code> 이면 <b>저절로</b>"),
    ("<code>type=\"button\"</code>", "폼 안에서는 적어 둔다 — 안 적으면 <b>제출</b>이 된다"),
    ("<code>autofocus</code>", "쓰지 않는다 — 초점을 <b>뺏는다</b>"),
    ("<code>44px</code>", "세기를 낮춰도 <b>크기는 안 낮춘다</b>"),
    ("확인하는 법", "화면을 흑백으로 두고 <b>어느 것이 주인지</b> 보인다면 잘 된 것"),
  ]),
  backend=rows([
    ("할 수 있는지", "권한이 없으면 <b>단추를 지웁니다</b> — 흐리게 두면 '왜 안 되나'를 묻게 됩니다."),
    ("두 번 누름", "주 버튼은 보내는 동안 <b>잠가</b> 둡니다 — <a href=\"success.html\">성공 확인</a>과 짝입니다."),
  ]),
  plat_lede="<b>세기를 나누는 생각</b>은 같고 이름이 다릅니다.",
  plats=plats([
    ("웹", "클래스로",
     row([btn('저장'), btn('취소', 'ghost')], "", "", True, "110px"),
     "정해진 이름이 없어 팀마다 다릅니다 — <b>먼저 정해 두는</b> 편이 낫습니다."),
    ("iOS", "borderedProminent 등",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;height:11px;border-radius:5px;background:var(--accent)"></div>
                <div style="position:absolute;left:5px;right:5px;bottom:25px;height:11px;border-radius:5px;border:1px solid var(--line)"></div></div></div>''',
     "<code>.borderedProminent</code> · <code>.bordered</code> · <code>.plain</code> 세 단계가 있습니다."),
    ("안드로이드", "Filled · Outlined · Text",
     '''              <div class="phone" role="img" aria-label="안드로이드 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:5px;bottom:10px;width:30px;height:11px;border-radius:999px;background:var(--accent)"></div>
                <div style="position:absolute;right:40px;bottom:10px;width:24px;height:11px;border-radius:999px;border:1px solid var(--line)"></div></div></div>''',
     "<b>Filled · Tonal · Outlined · Text · Elevated</b> 다섯 단계를 지침이 정해 두었습니다."),
  ]),
  plat_note="Material 의 <b>다섯 단계</b>는 많아 보이지만, 가운데의 <b>토널</b>(연한 바탕)이 실제로 쓸모가 큽니다 — 주 버튼만큼 세지 않으면서 테두리만 있는 것보다는 눈에 띕니다. 웹에서도 한 단계 더 둘 거라면 이 자리가 가장 쓸 만합니다. 다만 단계가 늘수록 <b>어느 것을 쓸지 고민</b>이 늘어서, 세 단계로 시작해 모자랄 때 늘리는 편이 좋습니다.",
  siblings=siblings("buttonlevel"),
  related='''        <li><a href="linkbutton.html"><b>링크와 버튼</b><em>4부</em></a></li>
        <li><a href="splitbutton.html"><b>분할 버튼</b><em>4부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="buttontext.html"><b>버튼 문구</b><em>14부</em></a></li>''',
)
