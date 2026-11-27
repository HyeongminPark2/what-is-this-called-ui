# -*- coding: utf-8 -*-
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def cb(kind):
    base = 'display:inline-block;width:10px;height:10px;border-radius:2px;border:1px solid var(--line);vertical-align:-1px;'
    if kind == 'on':
        return '<span style="' + base + 'background:var(--accent);border-color:var(--accent);color:#fff;font-size:7px;line-height:9px;text-align:center">✓</span>'
    if kind == 'mid':
        return '<span style="' + base + 'background:var(--accent);border-color:var(--accent);position:relative"><span style="position:absolute;left:2px;right:2px;top:4px;height:1.5px;background:#fff"></span></span>'
    return '<span style="' + base + '"></span>'

def tbl(head, rws, w="180px"):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">'
            + head + ''.join(rws) + '</div>')

def hrow(k, txt):
    return ('<div style="display:flex;align-items:center;gap:6px;padding:5px 8px;background:var(--bg);font-size:9.5px;font-weight:700;color:var(--fg-muted)">'
            + cb(k) + '<span>' + txt + '</span></div>')

def rrow(k, name):
    return ('<div style="display:flex;align-items:center;gap:6px;padding:5px 8px;font-size:10.5px;border-top:1px solid var(--line);'
            + ('background:var(--accent-soft);' if k == 'on' else '') + '">' + cb(k) + '<span>' + name + '</span></div>')

BAR = ('<div style="display:flex;align-items:center;gap:6px;padding:5px 8px;background:var(--accent);color:#fff;font-size:9.5px">'
       '<span style="flex:1">5건 선택됨</span><span style="text-decoration:underline">승인</span><span style="text-decoration:underline">내보내기</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:230px">''' + hrow('mid', '가맹점') + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">indeterminate는 일부만 골랐을 때의 세 번째 모양</div>
                  <div class="pin-out" data-pin="3" style="max-width:230px">''' + BAR + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">'이 쪽 5건'과 '조건에 맞는 128건'은 범위가 다름</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">쪽을 넘길 때 선택을 풀지 먼저 정함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">처리가 끝나면 "5건 승인됨 · 되돌리기"</div>
                </div>
              </div>'''

D = dict(
  slug="bulk", ko="일괄 선택", en="Bulk selection",
  desc="여러 건을 골라 한꺼번에 처리하는 화면을 반쯤 켜진 체크박스, '이 쪽'과 '전체'의 차이, 되돌리기까지 다루는 항목입니다.",
  lede="일괄 선택은 여러 건을 골라 <b>한꺼번에</b> 처리하는 장치입니다. 일괄 선택에서 생기는 사고는 대부분 <b>'전체'가 어디까지를 뜻하는지</b> 사용자와 화면이 서로 다르게 이해해서 일어납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>줄을 일부만 골라 보세요. 맨 위 체크박스가 <b>반쯤 켜진 모양</b>(indeterminate)이 되는데,
          체크박스에 켜짐·꺼짐 말고 세 번째 상태가 있다는 것을 알아야 만들 수 있는 모양입니다.<br>
          맨 위 체크박스로 전체를 고르면 <b>'이 쪽 5건'</b>과 <b>'조건에 맞는 128건'</b> 가운데 어느 쪽인지 묻는 줄이 뜹니다.
          이 질문이 없으면 사용자는 실제로 128건을 지우고도 5건만 지웠다고 알고 넘어갈 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "일괄 선택, 다중 선택, 묶음 처리"),
    ("영어", "bulk selection, multi-select, batch action"),
    ("같이 쓰는 말",
     "줄을 고른 뒤 뜨는 막대는 <b>벌크 액션 바</b>·<b>선택 툴바</b>·<b>컨텍스추얼 액션 바</b>라고 부릅니다. "
     "맨 위 체크박스는 <b>전체 선택</b>(select all), "
     "일부만 골랐을 때 맨 위 체크박스가 반쯤 켜진 상태는 <b>인디터미닛</b>(indeterminate)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>체크박스</b> — <a href=\"../items/checkbox.html\">체크박스</a>는 부품 하나이고, 일괄 선택은 체크박스와 동작 막대가 <b>여러 줄에 걸쳐 함께 움직이는 장치</b>입니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터</a>는 화면에 보이는 건을 줄이고, 일괄 선택은 <b>처리할 건을 고릅니다</b>. 필터로 걸러 놓고 전체 선택을 하면 두 기능을 함께 쓰게 됩니다.<br>"
     "<b>멀티 셀렉트</b> — 입력 부품에서 여러 값을 고르는 멀티 셀렉트와는 다른 장치입니다."),
  ]),
  s4_title="상태", s4_hint="맨 위 체크박스의 세 가지 상태",
  states=states([
    (tbl(hrow('off', '가맹점'), [rrow('off', '모란상회'), rrow('off', '한빛아웃도어')]),
     "아무것도 안 골랐을 때", "동작 막대는 <b>보이지 않습니다</b>. 막대가 나타날 자리는 미리 비워 둡니다"),
    (tbl(hrow('mid', '가맹점'), [rrow('on', '모란상회'), rrow('off', '한빛아웃도어')]),
     "일부만 골랐을 때", "맨 위 체크박스는 켜짐도 꺼짐도 아닌 <b>반쯤 켜진</b> 모양이 됩니다"),
    (tbl(hrow('on', '가맹점'), [rrow('on', '모란상회'), rrow('on', '한빛아웃도어')]),
     "이 쪽을 전부 골랐을 때", "맨 위 체크박스가 켜지지만, 고른 범위는 아직 <b>이 쪽</b>뿐입니다"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">'''
     + hrow('on', '가맹점')
     + '<div style="padding:5px 8px;font-size:9px;background:var(--warn-soft);border-top:1px solid var(--line)">이 쪽 5건을 골랐습니다 · <b style="color:var(--accent);text-decoration:underline">조건에 맞는 128건 모두 고르기</b></div>'
     + rrow('on', '모란상회') + '</div>',
     "조건에 맞는 전체로 넓힐 때", "사용자에게 <b>물어본 뒤에</b> 범위를 넓힙니다. 저절로 넓히지 않습니다"),
    (tbl(BAR, [rrow('on', '모란상회'), rrow('on', '한빛아웃도어')]),
     "동작 막대가 떴을 때", "고른 <b>건수</b>와 할 수 있는 <b>동작</b>을 보여 줍니다. 위든 아래든 한 자리에 고정합니다"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b>5건 승인됨</b> · <span style="color:var(--accent);text-decoration:underline">되돌리기</span>
              </div>''',
     "처리가 끝난 뒤", "<b>몇 건이</b> 어떻게 처리됐는지 알리고, 되돌리기 버튼을 함께 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("맨 위 체크박스", "select all", "<b>지금 보이는 쪽</b>만 고릅니다. 조건에 맞는 전부를 고르는 것이 아닙니다"),
    ("반쯤 켜진 모양", "indeterminate", "<code>el.indeterminate = true</code>처럼 <b>HTML 속성이 아니라 자바스크립트로</b>만 켤 수 있습니다"),
    ("동작 막대", "bulk action bar", "고른 것이 있을 때만 띄우고, 고른 <b>건수를 적습니다</b>"),
    ("범위를 묻는 줄", "this page / all", "'이 쪽 5건'과 '조건에 맞는 128건'은 <b>범위가 다르므로</b> 어느 쪽인지 묻습니다"),
    ("쪽을 넘길 때", "선택 유지 여부", "선택을 유지하면 화면에 보이지 않는 선택이 생기고, 풀면 지금까지 고른 것이 사라집니다. 어느 쪽으로 할지 <b>정해서 화면에 적어 둡니다</b>"),
    ("결과와 되돌리기", "undo", "묶음 처리는 되돌릴 수 있어야 사용자가 안심하고 씁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          일괄 선택을 설계할 때 가장 주의할 점은 <b>'전체 선택'이 두 가지 뜻으로 읽힌다</b>는 것입니다.
          맨 위 체크박스는 거의 언제나 <b>지금 보이는 쪽</b>만 고르는데,
          사용자는 이것을 <b>조건에 맞는 전부</b>를 고른 것으로 받아들입니다.
          그래서 지메일과 깃허브 같은 서비스는 모두 전체를 켠 뒤
          <b>"조건에 맞는 128건 모두 고르기"</b>라는 줄을 따로 띄웁니다.
          묻지 않고 범위를 넓히면 사용자는 128건을 지우고도 5건만 지웠다고 생각합니다.</p>''',
  do=ul([
    "승인, 내보내기, 태그 달기처럼 같은 동작을 <b>여러 건에</b> 되풀이할 때",
    "건수가 많아서 <b>하나씩 누르기에는 너무 번거로울</b> 때",
    "되돌릴 수 있는 동작일 때. 되돌리기가 없으면 범위를 더 좁게 묻습니다",
  ]),
  dont=ul([
    "건수가 서너 개일 때. <b>줄마다 버튼</b>을 두는 편이 더 빠릅니다",
    "되돌릴 수 없는 삭제에 '전체 선택'을 붙일 때. 적어도 사용자가 <b>건수를 직접 입력하게</b> 합니다",
    "고른 것이 없는데 동작 막대를 띄울 때",
    "쪽을 넘겼을 때 선택이 <b>아무 안내 없이</b> 풀릴 때",
  ]),
  instead='한 건씩만 처리하면 되는 경우에는 줄 안의 <a href="../items/card.html">카드</a>나 메뉴 버튼으로 충분하고, 목록을 거르기만 하려면 <a href="filter.html">필터</a>를 씁니다. 처리하기 전에 사용자의 확인을 받아야 하면 <a href="../items/dialog.html">다이얼로그</a>를 띄웁니다.',
  cases=cases([
    (tbl(BAR, [rrow('on', '모란상회')], "150px"), "표 위에 동작 막대 고정하기", "표 위에 두고, 표를 스크롤해도 같은 자리에 머뭅니다"),
    ('''              <div style="width:100%;max-width:150px;position:relative;height:60px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:5px 8px;font-size:10px">모란상회</div>
                <div style="position:absolute;left:4px;right:4px;bottom:4px;background:var(--fg);color:var(--surface);border-radius:999px;padding:4px 8px;font-size:9px;display:flex;gap:5px"><span style="flex:1">5건</span><span>승인</span></div>
              </div>''',
     "폰 화면 아래에 막대 띄우기", "폰에서 씁니다. <b>엄지가 닿는 자리</b>에 둡니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                정말 <b>128건</b>을 반려하시겠습니까?<br>
                <span style="color:var(--fg-muted);font-size:8.5px">되돌릴 수 없습니다</span>
              </div>''',
     "범위가 크면 건수를 넣어 되묻기", "확인 문구 <b>안에 건수를</b> 적어서 몇 건을 처리하는지 다시 보여 줍니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="일괄 선택을 만들 때 꼭 갖출 것",
  code_lede="<code>indeterminate</code>는 HTML 속성이 아니라 <b>자바스크립트 프로퍼티</b>입니다.",
  code='''&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">id</span>=<span class="s">"all"</span> <span class="a">aria-label</span>=<span class="s">"이 쪽 전체 선택"</span>&gt;
…
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;5건 선택됨&lt;/<span class="t">div</span>&gt;

<span class="c">// 세 번째 상태는 속성으로 못 켠다</span>
<span class="k">const</span> n = rows.filter(r =&gt; r.checked).length;
all.checked = n === rows.length;
all.indeterminate = n &gt; <span class="a">0</span> &amp;&amp; n &lt; rows.length;

<span class="c">// 범위를 넓힐 때는 묻는다</span>
<span class="k">if</span> (all.checked &amp;&amp; total &gt; rows.length) showScopeBanner(total);''',
  keys=kbd([
    ("<kbd>Space</kbd>", "체크박스를 켭니다. <code>&lt;input type=\"checkbox\"&gt;</code>를 쓰면 따로 만들지 않아도 됩니다"),
    ("<kbd>Shift</kbd>+클릭", "마지막으로 누른 줄과 지금 누른 줄 <b>사이를 전부</b> 고릅니다. 긴 목록에서는 거의 반드시 있어야 하는 기능입니다"),
    ("<code>indeterminate</code>", "스크린 리더는 'mixed'로 읽습니다. 자바스크립트로만 켤 수 있고, 사용자가 체크박스를 <b>누르면 사라집니다</b>"),
    ("<code>aria-label</code>", "맨 위 체크박스에 답니다. 글자 없이 빈 칸만 있으면 무엇을 고르는 체크박스인지 알 수 없습니다"),
    ("<code>role=\"status\"</code>", "'5건 선택됨'처럼 알립니다. 동작 막대가 떠도 화면을 보지 않는 사람은 알아챌 수 없기 때문입니다"),
    ("막대가 떠도 <b>포커스는 그대로 두기</b>", "포커스가 고르던 자리에 그대로 있어야 다음 줄을 이어서 고를 수 있습니다"),
  ]),
  backend=rows([
    ("'전체'는 ID 목록 대신 <b>조건</b>으로 보내기", "128건의 ID를 전부 담아 보내면 건수가 늘수록 요청이 지나치게 커집니다. <code>{\"filter\":{\"status\":\"pending\"}}</code>처럼 <b>조건</b>을 보내고 대상은 서버가 고르게 합니다."),
    ("일부만 성공했을 때 알려 주기", "128건 가운데 3건이 실패하면 <b>어느 건이 실패했는지</b> 돌려줘야 합니다. 일부 실패를 허용할지, 전부 성공하거나 전부 실패하도록 묶을지도 미리 정해야 합니다."),
    ("오래 걸리는 묶음 처리", "수천 건이면 요청 하나가 끝나기를 기다릴 수 없습니다. 서버가 <b>작업 번호를 먼저 돌려주고</b>, 화면은 그 번호로 진행률을 따로 묻게 합니다."),
    ("되돌리기를 위한 기록", "묶음 처리를 되돌리려면 <b>처리 전 상태를 기록</b>해 두어야 합니다. 기록 없이 처리한 뒤에는 되돌리기 기능을 붙이기가 거의 불가능합니다."),
    ("버튼이 두 번 눌리는 문제", "동작 막대의 버튼도 두 번 눌릴 수 있습니다. <a href=\"form.html\">폼</a>에서처럼 요청마다 <b>고유 키</b>를 붙입니다."),
  ]),
  plat_lede="폰에서는 항목을 <b>길게 누르거나 편집을 눌러 선택 모드로 들어가는</b> 방식이 표준입니다.",
  plats=plats([
    ("웹", "체크박스 열",
     tbl(hrow('mid', '가맹점'), [rrow('on', '모란상회')], "120px"),
     "표 맨 앞에 체크박스 열을 둡니다. 사용자는 <kbd>Shift</kbd>+클릭으로 범위를 고를 수 있으리라고 기대합니다."),
    ("iOS", "Edit 모드",
     '''              <div class="phone" role="img" aria-label="iOS 편집 모드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">편집</div>
                <div style="position:absolute;left:0;right:0;top:28px"><div style="display:flex;gap:3px;padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)"><span>◉</span><span>모란상회</span></div></div></div></div>''',
     "평소에는 체크박스를 보여 주지 않다가, 오른쪽 위 <b>'편집'</b>을 누르면 줄마다 고르는 동그라미가 나타납니다."),
    ("안드로이드", "Contextual action bar",
     '''              <div class="phone" role="img" aria-label="Material CAB 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:12px;background:var(--accent);color:#fff;font-size:6px;padding:3px 5px">5건 선택됨</div></div></div>''',
     "항목을 <b>길게 누르면</b> 선택 모드로 바뀌고 앱바가 선택용 막대로 바뀝니다. 선택 모드는 뒤로가기로 빠져나옵니다."),
  ]),
  plat_note="\"여러 개 골라서 한 번에 처리\"하는 기능을 요청받으면 <b>되돌리기가 되는지부터</b> 물어보세요. 되돌릴 수 있으면 선택 범위를 넓게 열어 줘도 되지만, 되돌릴 수 없으면 '조건에 맞는 전부'를 아예 막거나 건수를 직접 입력하게 하는 편이 낫습니다. 되돌리기는 처리 전 상태를 기록하는 구조가 필요해서 나중에 덧붙이기가 가장 어려운 기능입니다.",
  siblings=siblings("bulk"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/checkbox.html"><b>체크박스</b><em>4부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>8부</em></a></li>
        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>''',
)
