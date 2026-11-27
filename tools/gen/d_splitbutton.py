# -*- coding: utf-8 -*-
from ax4 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sb(main="CSV 로 내보내기", arrow=True, note="", ok=None, w="154px", menu=None, whole=False, div=True):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if whole:
        btn = ('<span style="display:inline-flex;align-items:center;gap:5px;border:1px solid var(--accent);'
               'border-radius:4px;background:var(--accent);color:#fff;font-size:8px;padding:4px 8px">'
               + main + '<span style="opacity:.8">▾</span></span>')
    else:
        btn = ('<span style="display:inline-flex;align-items:stretch">'
               '<span style="border:1px solid var(--accent);border-right:0;border-radius:4px 0 0 4px;'
               'background:var(--accent);color:#fff;font-size:8px;padding:4px 8px">' + main + '</span>'
               + ('<span style="border:1px solid var(--accent);border-left:'
                  + ('1px solid rgba(255,255,255,.55)' if div else '0')
                  + ';border-radius:0 4px 4px 0;background:var(--accent);color:#fff;font-size:8px;padding:4px 6px">▾</span>'
                  if arrow else '') + '</span>')
    m = ''
    if menu:
        m = ('<span style="display:block;border:1px solid var(--line);border-radius:4px;background:var(--surface);'
             'box-shadow:0 2px 6px rgba(0,0,0,.08);padding:3px;width:max-content;max-width:100%">'
             + ''.join('<span style="display:block;font-size:7.5px;padding:2px 6px;color:var(--fg-muted);'
                       'border-radius:3px' + (';background:var(--bg);color:var(--fg)' if i == 0 else '') + '">'
                       + t + '</span>' for i, t in enumerate(menu)) + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px;justify-items:start">'
            + btn + m
            + ('<span style="font-size:8.5px;color:' + (c if ok is False else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">왼쪽 — 가장 많이 쓰는 동작 하나, 한 번에 끝난다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">가는 선 — 여기가 갈린다는 신호</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">화살표 — 나머지를 연다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">왼쪽 이름이 없으면 뭐가 될지 모른다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">초점 둘 — Tab 으로 따로 받는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">화살표에만 붙는 이름</div>
                </div>
              </div>'''

D = dict(
  slug="splitbutton", ko="분할 버튼", en="Split button",
  desc="주 동작 하나를 꺼내 두고 나머지는 화살표 안에 넣는 단추. 한 번에 끝내려고 쓴다.",
  lede="메뉴를 여는 단추가 아닙니다 — <b>가장 많이 쓰는 하나를 한 번에</b> 끝내려고 가르는 것입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>데모가 <b>주 동작까지 몇 번 눌러야 하는지</b>를 세서 둘을 견줍니다 —
          분할 버튼은 <b>한 번</b>, 전체가 메뉴를 여는 쪽은 <b>늘 두 번</b>입니다.<br>
          대신 분할 버튼은 왼쪽을 눌렀을 때 <b>무엇이 일어날지</b>를
          이름으로 적어 두지 않으면 아무도 못 누릅니다.
          '마지막에 고른 것을 기본으로'를 켜 두면 왼쪽 이름이 따라 바뀝니다.</p>
        </div>''',
  names=rows([
    ("한국어", "분할 버튼, 갈라진 버튼, 주 동작 버튼"),
    ("영어", "split button, split-action button, dropdown button"),
    ("같이 쓰는 말",
     "왼쪽을 <b>주 동작</b>(primary action), 화살표 쪽을 <b>더 보기</b>라 합니다. "
     "전체가 메뉴를 여는 쪽은 <b>드롭다운 버튼</b>이라 부르며 분할 버튼과 구별합니다. "
     "마지막에 고른 것을 왼쪽에 남기는 방식은 <b>기억하는 기본값</b>입니다."),
    ("자주 잘못 부름",
     "<b>셀렉트</b> — <a href=\"select.html\">셀렉트</a>는 <b>값을 고르는</b> 칸입니다. 눌러도 아무 일이 안 일어납니다.<br>"
     "<b>메뉴</b> — <a href=\"menu.html\">메뉴</a>는 동작 목록 자체입니다.<br>"
     "<b>세그먼티드</b> — <a href=\"segmented.html\">세그먼티드 컨트롤</a>은 <b>보기를 바꾸는</b> 것입니다."),
  ]),
  axes=ax("분할 버튼"),
  oneline="<b>왼쪽에 무엇이 걸렸는지를 이름으로 적으세요.</b> 안 적으면 아무도 안 누릅니다.",
  states=states([
    (sb("CSV 로 내보내기", True, "한 번이면 끝난다", True), "기본", "<b>주 동작</b>이 보인다"),
    (sb("내보내기", True, "뭐가 될지 모른다", False), "이름이 모호", "<b>안 누른다</b>"),
    (sb("CSV 로 내보내기", True, "", None, "154px",
        ["CSV 로 내보내기", "엑셀로 내보내기", "PDF 로 내보내기"]), "열린 상태", "나머지가 <b>보인다</b>"),
    (sb("내보내기", False, "늘 두 번 눌러야 한다", None, "154px", None, True), "전체가 메뉴", "<b>모호하지 않다</b>"),
    (sb("엑셀로 내보내기", True, "마지막에 고른 것", True), "기억한 기본", "<b>따라 바뀐다</b>"),
    (sb("내보내기", True, "선이 없어 안 갈려 보인다", False, "154px", None, False, False), "선 없음", "<b>한 덩이</b>로 보인다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("왼쪽", "주 동작", "<b>한 번</b>에 끝"),
    ("가는 선", "갈림", "두 자리라는 <b>신호</b>"),
    ("화살표", "나머지", "메뉴를 <b>연다</b>"),
    ("이름", "무엇이 걸렸나", "없으면 <b>못 누른다</b>"),
    ("초점 둘", "Tab 둘", "따로 <b>받는다</b>"),
    ("화살표 이름", "aria-label", "'다른 형식으로'"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          분할 버튼이 맞는 자리는 좁습니다 —
          <b>선택지 가운데 하나가 압도적으로 많이 쓰일 때</b>뿐입니다.
          고르게 나뉘어 있으면 전체가 메뉴를 여는 쪽이 낫습니다.
          어느 쪽을 누를지 매번 생각하게 만드는 값이 <b>한 번 아끼는 품</b>보다 큽니다.<br>
          마지막에 고른 것을 왼쪽에 남기면 자주 쓰는 사람에게는 편하지만,
          <b>누를 때마다 이름이 달라지는</b> 단추가 되기도 합니다 —
          위험한 동작에는 쓰지 마세요.</p>''',
  do=ul([
    "왼쪽에 <b>무엇이 일어날지</b>를 이름으로 적기",
    "두 자리가 <b>갈려 보이게</b> 선을 두기",
    "화살표에 <b>따로 이름</b> 붙이기",
    "선택지 하나가 <b>압도적일 때만</b> 쓰기",
  ]),
  dont=ul([
    "왼쪽 이름을 <b>'내보내기'</b> 로만 두기 — 무엇이 될지 모른다",
    "<b>지우기</b> 같은 되돌릴 수 없는 동작을 왼쪽에 걸기",
    "두 자리를 <b>한 덩이</b>로 보이게 두기",
    "선택지가 <b>고르게 나뉠 때</b> 쓰기 — 매번 생각하게 된다",
  ]),
  instead='동작 목록만 필요하면 <a href="menu.html">메뉴</a>, 값을 고르면 <a href="select.html">셀렉트</a>, 보기를 바꾸면 <a href="segmented.html">세그먼티드 컨트롤</a>, 단추 사이 무게는 <a href="buttonlevel.html">버튼 위계</a>.',
  cases=cases([
    (sb("CSV 로 내보내기", True, "", True, "150px"), "내보내기", "<b>하나가</b> 압도적"),
    (sb("초안 저장", True, "", True, "150px"), "저장 방식", "기본이 <b>정해져</b> 있다"),
    (sb("지우기", True, "", False, "150px"), "지우기", "<b>실수</b>가 난다"),
  ]),
  code_lede="두 개의 <code>&lt;button&gt;</code> 입니다 — 하나로 만들면 초점이 하나가 됩니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"split"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span>&gt;CSV 로 내보내기&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">type</span>=<span class="s">"button"</span> <span class="a">aria-haspopup</span>=<span class="s">"menu"</span>
          <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"m"</span>
          <span class="a">aria-label</span>=<span class="s">"다른 형식으로 내보내기"</span>&gt;▾&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"m"</span> <span class="a">role</span>=<span class="s">"menu"</span> <span class="a">hidden</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"menuitem"</span>&gt;엑셀로 내보내기&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"menuitem"</span>&gt;PDF 로 내보내기&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;''',
  keys=kbd([
    ("Tab", "두 자리가 <b>따로</b> 초점을 받습니다 — 하나로 묶으면 화살표를 못 누릅니다"),
    ("Enter · Space", "선 자리의 동작을 합니다"),
    ("↓ · Alt+↓", "화살표에 초점이 있을 때 <b>메뉴를 엽니다</b>"),
    ("Esc", "메뉴를 닫고 <b>화살표로</b> 초점을 돌립니다"),
    ("<code>aria-label</code>", "화살표는 '▾' 뿐이라 <b>이름이 없습니다</b> — 꼭 붙입니다"),
    ("확인하는 법", "소리를 켜고 <b>화살표만</b> 들어 무엇을 여는지 알 수 있나 봅니다"),
  ]),
  backend=rows([
    ("기억한 기본값", "마지막에 고른 형식을 <b>사용자별로</b> 둡니다 — 기기마다 다르면 더 헷갈립니다."),
    ("동작은 둘 다 같은 길로", "왼쪽과 메뉴가 <b>같은 API</b> 를 부르게 합니다 — 가른 것은 화면뿐입니다."),
    ("오래 걸리면", "내보내기가 길어지면 <a href=\"progress.html\">진행 표시</a>나 메일로 보내는 쪽으로 넘깁니다."),
  ]),
  plat_lede="<b>데스크톱 쪽 관습</b>이라 모바일에는 거의 없습니다.",
  plats=plats([
    ("웹", "button 둘",
     sb("CSV 로 내보내기", True, "", True, "110px"),
     "기본 부품이 없어 <b>직접</b> 만듭니다 — 초점 둘만 지키면 됩니다."),
    ("iOS", "없다 — 길게 눌러",
     '''              <div class="phone" role="img" aria-label="iOS 주 동작 단추 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;right:6px;top:26px;height:18px;border-radius:5px;background:var(--accent)"></div>
                <div style="position:absolute;left:9px;top:32px;width:30px;height:5px;border-radius:2px;background:var(--surface);opacity:.85"></div></div></div>''',
     "분할 버튼이 없습니다 — 단추를 <b>길게 눌러</b> 메뉴를 띄우는 쪽입니다."),
    ("안드로이드", "없다 — FAB 메뉴",
     '''              <div class="phone" role="img" aria-label="안드로이드 FAB 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:7px;bottom:9px;width:19px;height:19px;border-radius:7px;background:var(--accent)"></div>
                <div style="position:absolute;right:10px;bottom:32px;width:13px;height:5px;border-radius:2px;background:var(--line)"></div></div></div>''',
     "Material 에도 없습니다 — <b>FAB 메뉴</b>가 비슷한 자리를 맡습니다."),
  ]),
  plat_note="모바일에 분할 버튼이 없는 까닭은 <b>손가락이 그만큼 정확하지 않기</b> 때문입니다. 두 자리를 가르면 각각이 작아지고, 작아지면 <a href=\"touchtarget.html\">터치 영역</a> 44px 을 못 맞춥니다. 좁은 화면에서는 가르지 말고 <b>단추 하나 + 액션 시트</b>로 보내는 편이 낫습니다.",
  siblings=siblings("splitbutton"),
  related='''        <li><a href="menu.html"><b>메뉴</b><em>6부</em></a></li>
        <li><a href="buttonlevel.html"><b>버튼 위계</b><em>4부</em></a></li>
        <li><a href="actionsheet.html"><b>액션 시트</b><em>6부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 영역</b><em>14부</em></a></li>''',
)
