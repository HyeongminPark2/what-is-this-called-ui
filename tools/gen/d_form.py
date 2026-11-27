# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fld(lab, val="", hint="", w="160px", err=""):
    return ('<div style="display:grid;gap:2px"><span style="font-size:9px;color:var(--fg-muted)">' + lab + '</span>'
            '<div style="border:1px solid ' + ('var(--danger)' if err else 'var(--line)') + ';border-radius:5px;background:var(--surface);'
            'padding:4px 7px;font-size:10.5px;' + ('color:var(--fg-muted)' if not val else '') + '">' + (val or '&nbsp;') + '</div>'
            + ('<span style="font-size:8.5px;color:var(--danger)">' + err + '</span>' if err else
               '<span style="font-size:8.5px;color:var(--fg-muted)">' + hint + '</span>' if hint else '') + '</div>')

def card(inner, w="160px"):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:7px">' + inner + '</div>')

def group(title, inner):
    return ('<div style="border:1px solid var(--line);border-radius:6px;padding:7px;display:grid;gap:6px">'
            '<span style="font-size:9px;font-weight:700">' + title + '</span>' + inner + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;form&gt;으로 감싸 엔터로 제출</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + group('가맹점', fld('상호', '모란상회') + fld('사업자번호', '', '- 없이 10자리')).strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한 줄에 한 칸씩 두어 시선이 곧게 내려감</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">칸 이름은 <b>위에</b>, 옆이면 폰에서 배치가 무너짐</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">선택 칸에 '(선택)'을 적고 별표를 세게 하지 않음</div>
                  <div class="pin-out" data-pin="6" style="max-width:220px;display:flex;gap:5px"><span style="font-size:10px;background:var(--accent);color:#fff;padding:3px 10px;border-radius:5px">저장</span><span style="font-size:10px;border:1px solid var(--line);padding:3px 10px;border-radius:5px">취소</span></div>
                </div>
              </div>'''

D = dict(
  slug="form", ko="폼 설계", en="Form design",
  desc="입력 칸을 어떻게 묶고 어떤 순서로 놓을지를 칸 수 줄이기, 레이블 자리, 단계 나누기, 임시 저장까지 다루는 항목입니다.",
  lede="폼 설계는 칸 하나하나의 모양보다 <b>여러 칸을 어떻게 묶고 얼마나 줄일지</b>를 정하는 일입니다. 칸이 적을수록 사용자가 끝까지 채울 가능성이 높아지므로 <b>짧은 폼</b>을 목표로 합니다.",
  axes_lede="데이터를 다루는 화면을 설계할 때는 '건수가 늘면 어떻게 되나'부터 따져야 합니다. 아래 네 가지를 물어보면 이 부의 항목들이 서로 어떻게 다른지 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>묶어 보기</b>를 켜고 꺼 보세요. 칸 수가 같은데도 묶어 두면 폼이 훨씬 짧아 보입니다.<br>
          <b>선택 칸 숨기기</b>를 켜면 꼭 채울 칸만 남습니다. 폼 설계에서 가장 효과가 큰 일이 이렇게 <b>칸 수를 줄이는 것</b>입니다.
          아래에는 지금 <b>몇 칸을 채워야 하는지</b>가 표시됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "폼, 입력 양식, 서식, 등록 화면"),
    ("영어", "form, form design, input form"),
    ("같이 쓰는 말",
     "입력 칸 하나는 <b>필드</b>(field), 칸 이름은 <b>레이블</b>, 칸 밑에 붙는 설명은 <b>헬프 텍스트</b>·<b>힌트</b>라고 부릅니다. "
     "여러 칸을 한데 묶은 것은 <b>필드셋</b>(fieldset)·<b>섹션</b>이라고 하고, "
     "폼을 여러 화면으로 나눈 것은 <b>위저드</b>(wizard)·<b>스텝 폼</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>필드</b> — <a href=\"../items/field.html\">입력 필드</a>는 칸 하나를 가리키고, 폼은 <b>여러 칸을 묶은 전체</b>를 가리킵니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 화면을 띄우는 방식이고, 폼은 그 모달 안에 들어가는 내용입니다.<br>"
     "<b>검증</b> — <a href=\"validation.html\">입력 검증</a>은 폼을 이루는 한 부분입니다."),
  ]),
  axes=ax("폼 설계"),
  oneline="폼을 설계할 때는 '칸을 어떻게 배치할까'보다 <b>'이 칸이 정말 필요한가'</b>를 먼저 묻습니다. 지워도 되는 칸을 지우는 것이 배치를 다듬는 것보다 효과가 큽니다.",
  s4_title="상태", s4_hint="칸 하나가 아닌 폼 전체의 상태",
  states=states([
    (card(fld('상호') + fld('사업자번호', '', '- 없이 10자리')), "처음 열어 비어 있을 때", "입력 형식을 알려 주는 <b>힌트</b>를 미리 둡니다. 틀린 뒤에야 알려 주면 사용자가 다시 입력해야 합니다"),
    (card(fld('상호', '모란상회') + fld('사업자번호', '1248100998')), "기존 값을 고칠 때", "값을 고치는 화면에서는 칸마다 <b>기존 값</b>이 들어 있어야 합니다"),
    (card(fld('상호', '모란상회') + fld('사업자번호', '124', err='10자리를 채워 주세요')), "틀린 값이 들어갔을 때", "틀린 값을 알려 주는 일은 <a href=\"validation.html\">검증</a>에서 다룹니다"),
    (card('<div style="display:grid;gap:5px"><span class="skl" style="height:24px"></span><span class="skl" style="height:24px"></span></div>'),
     "기존 값을 불러오는 중", "기존 값을 불러오는 동안에는 뼈대를 보여 줍니다. <b>빈 칸을 먼저 보여 주고 나중에 값을 채우면</b> 사용자가 그사이 입력한 글자를 덮어씁니다"),
    (card(fld('상호', '모란상회') + '<div style="display:flex;gap:5px"><span style="font-size:10px;background:var(--fg-muted);color:#fff;padding:3px 10px;border-radius:5px">저장 중…</span></div>'),
     "저장 요청을 보내는 중", "저장 버튼을 잠급니다. 버튼을 두 번 눌러 같은 건이 두 번 저장되는 일이 흔하기 때문입니다"),
    (card('<div style="border:1px solid var(--line);border-radius:6px;padding:8px;font-size:9.5px;color:var(--fg-muted)">1 · 2 · <b style="color:var(--accent)">3</b> 단계<br><span style="font-size:8.5px">작성한 내용은 저장돼 있습니다</span></div>'),
     "여러 단계로 나뉜 폼", "지금 <b>몇 번째 단계인지</b>와 <b>앞 단계로 돌아갈 수 있는지</b>를 보여 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("폼", "&lt;form&gt;", "칸들을 <code>&lt;form&gt;</code>으로 감싸야 <b>엔터로 제출</b>되고 브라우저 자동 채움도 잘 동작합니다"),
    ("묶음", "fieldset / legend", "성격이 같은 칸들을 묶습니다. 칸 수가 같아도 <b>묶어 두면 짧아 보입니다</b>"),
    ("한 줄에 한 칸", "single column", "한 줄에 한 칸씩 두면 시선이 위에서 아래로 한 줄기로 내려갑니다. 두 열로 놓으면 사용자가 <b>건너뛰는 칸</b>이 생깁니다"),
    ("레이블은 위", "label top", "레이블을 칸 위에 두면 좁은 폰 화면에서도 배치가 무너지지 않고, 레이블 글자가 길어져도 들어갑니다"),
    ("선택 칸 표시", "(선택)", "필수 칸에 <b>별표</b>를 다는 것보다 선택 칸에 '(선택)'을 적는 편이 읽기 쉽습니다"),
    ("버튼", "주 동작 하나", "<b>저장</b>은 오른쪽에 진한 색으로, <b>취소</b>는 눈에 덜 띄게 둡니다. 두 버튼을 같은 강조로 두지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>칸을 두 열로 놓지 않습니다.</b> 두 열로 놓으면 시선이 Z 자로 오가야 해서,
          사용자가 오른쪽 열을 통째로 보지 못하고 지나치는 일이 생깁니다.
          예외는 <b>따로 떼어 놓으면 오히려 어색한 값</b>뿐입니다. 시·도와 시·군·구, 시작일과 종료일,
          카드 유효기간의 월과 연도처럼 <b>한 덩어리로 읽히는 값</b>은 나란히 둡니다.</p>''',
  do_title="폼을 쓰는 경우",
  dont_title="폼을 쓰지 않거나 다르게 만들어야 하는 경우",
  instead_title="폼 대신 다른 것을 써야 하는 경우",
  do=ul([
    "받을 값이 <b>여러 개</b>이고 한 번에 보내야 할 때",
    "이미 있는 값을 <b>고치는</b> 화면일 때. 칸마다 기존 값이 들어 있어야 합니다",
    "단계가 있는 등록 화면일 때. 단계를 <b>나눠야</b> 사용자가 끝까지 채웁니다",
  ]),
  dont=ul([
    "칸이 <b>하나</b>일 때. <a href=\"../items/field.html\">입력 필드</a>와 버튼만 두면 됩니다",
    "'나중에 쓸지도 몰라서' 칸을 넣을 때. <b>지금 쓰지 않는 칸은 지웁니다</b>",
    "열 칸을 한 화면에 늘어놓을 때. 세 묶음 정도로 나누거나 단계로 쪼갭니다",
    "<code>&lt;form&gt;</code> 없이 <code>&lt;div&gt;</code>로 감쌀 때. 엔터로 제출할 수 없고 자동 채움도 제대로 동작하지 않습니다",
  ]),
  instead='받을 값이 하나뿐이면 <a href="../items/field.html">입력 필드</a> 하나로 충분하고, 정해진 값 가운데 고르기만 하면 <a href="../items/select.html">셀렉트</a>를 씁니다. 입력 없이 확인만 받으면 되는 경우에는 <a href="../items/dialog.html">다이얼로그</a>가 맞습니다.',
  cases=cases([
    (card(group('가맹점', fld('상호', '모란상회')) + group('정산', fld('계좌', '')), "150px"),
     "칸을 묶음으로 나누기", "칸 수는 같아도 <b>두 덩어리</b>로 나뉘어 보여 읽기 쉽습니다"),
    (card('<div style="display:flex;gap:4px;align-items:center;font-size:9px"><span style="width:14px;height:14px;border-radius:999px;background:var(--accent);color:#fff;display:grid;place-items:center">1</span><span style="flex:1;height:1px;background:var(--line)"></span><span style="width:14px;height:14px;border-radius:999px;border:1px solid var(--line);display:grid;place-items:center">2</span></div>' + fld('상호', '모란상회'), "150px"),
     "긴 폼을 단계로 나누기", "칸이 많으면 단계로 쪼개서 <b>남은 분량이 보이게</b> 합니다"),
    (card('<div style="display:grid;grid-template-columns:1fr 1fr;gap:5px">' + fld('시작일', '11/01') + fld('종료일', '11/07') + '</div>', "150px"),
     "두 열로 나란히 두어도 되는 값", "<b>한 덩어리로 읽히는 값</b>만 나란히 둡니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="폼을 만들 때 꼭 갖출 것",
  code_lede="칸 전체를 <code>&lt;form&gt;</code>으로 감싸고, 묶음은 <code>&lt;fieldset&gt;</code>으로, 칸 이름은 <code>&lt;label for&gt;</code>로 답니다.",
  code='''&lt;<span class="t">form</span> <span class="a">method</span>=<span class="s">"post"</span>&gt;
  &lt;<span class="t">fieldset</span>&gt;
    &lt;<span class="t">legend</span>&gt;가맹점&lt;/<span class="t">legend</span>&gt;
    &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"biz"</span>&gt;상호&lt;/<span class="t">label</span>&gt;
    &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"biz"</span> <span class="a">name</span>=<span class="s">"biz"</span> <span class="a">autocomplete</span>=<span class="s">"organization"</span> <span class="a">required</span>&gt;

    &lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"no"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
    &lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"no"</span> <span class="a">name</span>=<span class="s">"no"</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span>
           <span class="a">aria-describedby</span>=<span class="s">"no-hint"</span>&gt;
    &lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"no-hint"</span>&gt;- 없이 10자리&lt;/<span class="t">p</span>&gt;
  &lt;/<span class="t">fieldset</span>&gt;

  &lt;<span class="t">button</span>&gt;저장&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">form</span>&gt;''',
  keys=kbd([
    ("<kbd>Enter</kbd>", "칸이 <code>&lt;form&gt;</code> 안에 있으면 엔터로 제출됩니다. div로 감싸면 제출되지 않습니다"),
    ("<code>&lt;label for&gt;</code>", "칸마다 답니다. <b>레이블을 눌러도 칸에 포커스가 가서</b> 누를 수 있는 영역이 넓어집니다"),
    ("<code>autocomplete</code>", "이름·전화·주소·카드 칸에 적어 두면 브라우저가 값을 채워 줍니다. 폼에 넣을 수 있는 <b>효과가 가장 큰 한 줄</b>입니다"),
    ("<code>inputmode</code>", "폰 키보드 종류를 바꿉니다. 숫자 칸에 글자 키보드가 뜨면 사용자가 숫자 키보드로 직접 바꿔야 합니다"),
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "스크린 리더가 '가맹점 묶음, 상호 입력'처럼 묶음 이름과 함께 읽습니다"),
    ("<code>aria-describedby</code>", "힌트를 칸에 연결합니다. 칸 밑에 적기만 하면 칸에 포커스가 왔을 때 힌트를 읽어 주지 않습니다"),
  ]),
  backend=rows([
    ("서버에서 다시 검사하기", "브라우저에서 하는 검사는 사용자가 빨리 고치도록 <b>돕는 장치</b>이고 방어 수단은 아닙니다. 요청은 폼을 거치지 않고도 보낼 수 있기 때문입니다."),
    ("두 번 눌러 같은 건이 둘 생기는 문제", "저장 버튼을 두 번 눌러 같은 건이 둘 생기는 일이 흔합니다. 그래서 요청마다 <b>고유 키</b>(idempotency key)를 받아, 같은 키로 온 요청은 한 번만 처리합니다."),
    ("긴 폼의 임시 저장", "긴 폼은 사용자가 중간에 자리를 뜨거나 창을 닫아 끊기기 쉽습니다. <b>초안</b>을 따로 저장해 두면 다시 돌아왔을 때 이어서 쓸 수 있습니다."),
    ("오류를 칸별로 돌려주기", "<code>{\"errors\":{\"no\":\"10자리여야 합니다\"}}</code>처럼 오류가 <b>어느 칸의 것인지</b> 함께 보내야 화면에서 오류 문구를 그 칸에 붙일 수 있습니다."),
    ("칸을 추가했을 때 옛 데이터 다루기", "칸을 새로 추가하면 이미 저장된 옛 데이터에는 그 칸의 값이 없습니다. 새 칸은 <b>빈 값을 허용</b>하거나 기본값을 정해 둡니다."),
  ]),
  plat_lede="세 플랫폼은 <b>레이블 자리</b>와 <b>저장 버튼 위치</b>가 다릅니다.",
  plats=plats([
    ("웹", "&lt;form&gt;",
     card(fld('상호', '모란상회'), "115px"),
     "레이블은 칸 위에, 저장 버튼은 폼 <b>아래</b>에 둡니다. 브라우저 자동 채움 덕분에 사용자가 직접 입력할 칸이 크게 줄어듭니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 폼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="display:flex;padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)"><span style="width:30%">상호</span><span>모란상회</span></div></div>
                <div style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">저장</div></div></div>''',
     "설정 화면처럼 <b>왼쪽에 칸 이름, 오른쪽에 값</b>을 두고 줄지어 놓으며, 저장 버튼은 <b>오른쪽 위</b>에 둡니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 폼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-radius:4px 4px 0 0;border-bottom:1px solid var(--accent);padding:5px"><div style="font-size:5px;color:var(--accent)">상호</div><div style="font-size:6px">모란상회</div></div></div></div>''',
     "입력을 시작하면 칸 이름이 <b>칸 안에서 위로 올라가는</b> 텍스트 필드를 쓰고, 저장 버튼은 아래쪽에 둡니다."),
  ]),
  plat_note="\"폼 하나 만들어 주세요\"라는 요청에 드는 품은 <b>칸 수에 비례하지 않습니다.</b> 기존 값 불러오기, 임시 저장, 중복 제출 막기, 칸별 오류 표시가 늘 한 벌로 따라오고, 칸이 하나든 열이든 이 기본 구조는 같기 때문입니다. 반대로 칸을 세 개 지우는 일은 하루면 끝나는데도 사용자에게 주는 효과는 가장 큽니다.",
  siblings=siblings("form"),
  related='''        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>''',
)
