# -*- coding: utf-8 -*-
from ax10 import ax
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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">indeterminate — 일부만 골랐을 때의 세 번째 모양</div>
                  <div class="pin-out" data-pin="3" style="max-width:230px">''' + BAR + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">'이 쪽 5건' 과 '조건에 맞는 128건' 은 다른 말이다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">쪽을 넘기면 선택이 풀리는가 — 먼저 정한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">끝난 뒤 "5건 승인됨 · 되돌리기"</div>
                </div>
              </div>'''

D = dict(
  slug="bulk", ko="일괄 선택", en="Bulk selection",
  desc="여러 건을 골라 한꺼번에 처리하는 화면. 반쯤 켜진 체크박스, '이 쪽'과 '전체'의 차이, 되돌리기까지.",
  lede="여러 건을 골라 <b>한꺼번에</b> 처리하는 장치. 사고는 거의 전부 <b>'전체'가 무엇을 뜻하느냐</b>에서 납니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>맨 위 체크박스를 눌러 보세요. 일부만 골랐을 때 <b>반쯤 켜진 모양</b>(indeterminate)이 됩니다 —
          체크박스에 상태가 셋이라는 것을 모르면 못 만드는 모양입니다.<br>
          전체를 고르면 <b>'이 쪽 5건'</b>과 <b>'조건에 맞는 128건'</b> 중 어느 쪽인지 묻는 줄이 뜹니다.
          이걸 묻지 않으면 사용자는 128건을 지운 줄 모르고 5건만 지운 줄 압니다.</p>
        </div>''',
  names=rows([
    ("한국어", "일괄 선택, 다중 선택, 묶음 처리"),
    ("영어", "bulk selection, multi-select, batch action"),
    ("같이 쓰는 말",
     "고른 뒤 뜨는 막대가 <b>벌크 액션 바</b>·<b>선택 툴바</b>·<b>컨텍스추얼 액션 바</b>입니다. "
     "맨 위 체크박스가 <b>전체 선택</b>(select all), "
     "일부만 켜진 상태가 <b>인디터미닛</b>(indeterminate)입니다."),
    ("자주 잘못 부름",
     "<b>체크박스</b> — <a href=\"../items/checkbox.html\">체크박스</a>는 부품 하나, 일괄 선택은 <b>줄들에 걸친 장치</b>입니다.<br>"
     "<b>필터</b> — <a href=\"filter.html\">필터</a>는 보이는 것을 줄이고, 일괄 선택은 <b>처리할 것을 고릅니다</b>. 걸러 놓고 전체 선택하면 둘이 만납니다.<br>"
     "<b>멀티 셀렉트</b> — 입력 부품의 여러 값 고르기와는 다릅니다."),
  ]),
  axes=ax("일괄 선택"),
  oneline="'전체 선택'이 <b>이 쪽인지 조건에 맞는 전부인지</b>를 먼저 정하세요. 안 정하면 되돌릴 수 없는 사고가 납니다.",
  s4_title="상태", s4_hint="체크박스에 상태가 셋이다",
  states=states([
    (tbl(hrow('off', '가맹점'), [rrow('off', '모란상회'), rrow('off', '한빛아웃도어')]),
     "아무것도 안 골랐을 때", "막대는 <b>안 보인다</b>. 자리는 미리 비워 둔다"),
    (tbl(hrow('mid', '가맹점'), [rrow('on', '모란상회'), rrow('off', '한빛아웃도어')]),
     "일부", "맨 위는 <b>반쯤 켜진</b> 모양. 켜짐도 꺼짐도 아니다"),
    (tbl(hrow('on', '가맹점'), [rrow('on', '모란상회'), rrow('on', '한빛아웃도어')]),
     "이 쪽 전부", "맨 위가 켜진다. 하지만 아직 <b>이 쪽</b>뿐이다"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">'''
     + hrow('on', '가맹점')
     + '<div style="padding:5px 8px;font-size:9px;background:var(--warn-soft);border-top:1px solid var(--line)">이 쪽 5건을 골랐습니다 · <b style="color:var(--accent);text-decoration:underline">조건에 맞는 128건 모두 고르기</b></div>'
     + rrow('on', '모란상회') + '</div>',
     "전체로 넓히기", "<b>묻고 나서</b> 넓힌다. 저절로 넓히지 않는다"),
    (tbl(BAR, [rrow('on', '모란상회'), rrow('on', '한빛아웃도어')]),
     "동작 막대", "고른 <b>건수</b>와 할 수 있는 <b>동작</b>. 위든 아래든 한 자리에 고정"),
    ('''              <div style="width:100%;max-width:180px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b>5건 승인됨</b> · <span style="color:var(--accent);text-decoration:underline">되돌리기</span>
              </div>''',
     "끝난 뒤", "<b>몇 건이</b> 어떻게 됐는지. 되돌릴 길을 함께 준다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("맨 위 체크박스", "select all", "<b>이 쪽</b>을 켠다. 전부가 아니다"),
    ("반쯤 켜진 모양", "indeterminate", "<code>el.indeterminate = true</code> — <b>속성이 아니라 자바스크립트로</b>만 켜진다"),
    ("동작 막대", "bulk action bar", "고른 게 있을 때만. <b>건수를 적는다</b>"),
    ("범위를 묻는 줄", "this page / all", "'이 쪽 5건' 과 '조건에 맞는 128건'은 <b>다른 말</b>이다"),
    ("쪽을 넘길 때", "선택 유지 여부", "유지하면 안 보이는 선택이 생기고, 풀면 지금까지가 날아간다. <b>정하고 적어 둔다</b>"),
    ("결과와 되돌리기", "undo", "묶음 처리는 되돌릴 수 있어야 쓴다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'전체 선택'의 뜻이 두 가지</b>라는 것이 이 부품의 전부입니다.
          맨 위 체크박스는 거의 늘 <b>지금 보이는 쪽</b>만 켭니다.
          그런데 사용자는 <b>조건에 맞는 전부</b>라고 읽습니다.
          그래서 지메일부터 깃허브까지 모두 전체를 켠 뒤
          <b>"조건에 맞는 128건 모두 고르기"</b>라는 줄을 따로 띄웁니다 —
          묻지 않고 넓히면 128건을 지우고도 5건인 줄 압니다.</p>''',
  do=ul([
    "같은 동작을 <b>여러 건에</b> 되풀이할 때 — 승인, 내보내기, 태그 달기",
    "건수가 많아 <b>하나씩 누르면 지치는</b> 화면",
    "되돌릴 수 있는 동작 — 되돌리기가 없으면 범위를 더 좁게 묻는다",
  ]),
  dont=ul([
    "건수가 서넛일 때 — <b>줄마다 버튼</b>이 더 빠르다",
    "되돌릴 수 없는 삭제에 '전체 선택' — 적어도 <b>건수를 치게</b> 한다",
    "고른 게 없는데 막대를 띄우는 것",
    "쪽을 넘겼을 때 선택이 <b>조용히</b> 풀리는 것",
  ]),
  instead='한 건이면 줄 안의 <a href="../items/card.html">카드</a>·메뉴 버튼, 거르기만 하면 <a href="filter.html">필터</a>, 확인이 필요하면 <a href="../items/dialog.html">다이얼로그</a>.',
  cases=cases([
    (tbl(BAR, [rrow('on', '모란상회')], "150px"), "위 고정 막대", "표 위에. 굴려도 따라온다"),
    ('''              <div style="width:100%;max-width:150px;position:relative;height:60px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="padding:5px 8px;font-size:10px">모란상회</div>
                <div style="position:absolute;left:4px;right:4px;bottom:4px;background:var(--fg);color:var(--surface);border-radius:999px;padding:4px 8px;font-size:9px;display:flex;gap:5px"><span style="flex:1">5건</span><span>승인</span></div>
              </div>''',
     "아래 떠 있는 막대", "폰에서. <b>엄지 닿는 자리</b>에 둔다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                정말 <b>128건</b>을 반려하시겠습니까?<br>
                <span style="color:var(--fg-muted);font-size:8.5px">되돌릴 수 없습니다</span>
              </div>''',
     "큰 범위는 되묻기", "건수를 <b>문장 안에</b> 적는다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 선택의 계약서",
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
    ("<kbd>Space</kbd>", "체크박스를 켠다. <code>&lt;input type=\"checkbox\"&gt;</code>면 공짜로 된다"),
    ("<kbd>Shift</kbd>+클릭", "<b>사이 전부</b>를 고른다. 긴 목록에서는 거의 필수다"),
    ("<code>indeterminate</code>", "읽기는 'mixed'. 자바스크립트로만 켜지고 <b>껐다 켜면 사라진다</b>"),
    ("<code>aria-label</code>", "맨 위 체크박스에. 빈 칸만 있으면 무엇을 켜는지 모른다"),
    ("<code>role=\"status\"</code>", "'5건 선택됨'. 막대가 떠도 눈으로 안 보는 사람에겐 안 보인다"),
    ("막대가 뜨며 <b>초점을 뺏지 않는다</b>", "고르던 자리에 그대로 있어야 다음 줄을 계속 고른다"),
  ]),
  backend=rows([
    ("'전체'는 <b>조건</b>으로 보낸다", "128건의 ID 를 전부 보내면 요청이 터집니다. <code>{\"filter\":{\"status\":\"pending\"}}</code>로 <b>조건</b>을 보내고 서버가 고르게 합니다."),
    ("일부만 성공할 수 있다", "128건 중 3건이 실패하면 <b>무엇이 실패했는지</b> 돌려줘야 합니다. 전부 성공 아니면 전부 실패로 묶을지도 정해야 합니다."),
    ("오래 걸린다", "수천 건이면 요청 하나로 못 끝냅니다. <b>작업 번호를 먼저 돌려주고</b> 진행률을 따로 묻게 합니다."),
    ("되돌리기", "묶음 처리의 되돌리기는 <b>처리 전 상태를 기록</b>해 둬야 가능합니다. 사후에 만들면 거의 불가능합니다."),
    ("두 번 눌림", "막대의 버튼도 두 번 눌립니다. <a href=\"form.html\">폼</a>과 같은 <b>고유 키</b>를 씁니다."),
  ]),
  plat_lede="폰은 <b>길게 눌러 선택 모드로 들어가는</b> 방식이 표준입니다.",
  plats=plats([
    ("웹", "체크박스 열",
     tbl(hrow('mid', '가맹점'), [rrow('on', '모란상회')], "120px"),
     "맨 앞에 체크박스 열을 둡니다. <kbd>Shift</kbd>+클릭 범위 선택이 기대되는 동작입니다."),
    ("iOS", "Edit 모드",
     '''              <div class="phone" role="img" aria-label="iOS 편집 모드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">편집</div>
                <div style="position:absolute;left:0;right:0;top:28px"><div style="display:flex;gap:3px;padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)"><span>◉</span><span>모란상회</span></div></div></div></div>''',
     "오른쪽 위 <b>'편집'</b>을 눌러야 동그라미가 나타납니다. 평소에는 체크박스를 안 보여 줍니다."),
    ("안드로이드", "Contextual action bar",
     '''              <div class="phone" role="img" aria-label="Material CAB 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:12px;background:var(--accent);color:#fff;font-size:6px;padding:3px 5px">5건 선택됨</div></div></div>''',
     "항목을 <b>길게 누르면</b> 선택 모드가 되고 앱바가 통째로 바뀝니다. 뒤로가기로 빠져나옵니다."),
  ]),
  plat_note="\"여러 개 골라서 한 번에 처리\"를 받으면 <b>되돌리기부터</b> 물어보세요. 되돌릴 수 있으면 범위를 넓게 줘도 되고, 없으면 '조건에 맞는 전부'를 아예 막거나 건수를 치게 하는 편이 낫습니다. 뒤에 붙이기 가장 어려운 기능이 되돌리기입니다.",
  siblings=siblings("bulk"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/checkbox.html"><b>체크박스</b><em>4부</em></a></li>
        <li><a href="../items/toast.html"><b>토스트</b><em>8부</em></a></li>
        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>''',
)
