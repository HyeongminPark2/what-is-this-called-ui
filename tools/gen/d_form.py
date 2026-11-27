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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;form&gt; — 엔터로 보내진다</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + group('가맹점', fld('상호', '모란상회') + fld('사업자번호', '', '- 없이 10자리')).strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">한 줄에 한 칸 — 눈이 한 길로 내려간다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">칸 이름은 <b>위에</b>. 옆에 두면 폰에서 깨진다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">선택 입력에 '(선택)'을 적는다 — 별표를 세게 하지 않는다</div>
                  <div class="pin-out" data-pin="6" style="max-width:220px;display:flex;gap:5px"><span style="font-size:10px;background:var(--accent);color:#fff;padding:3px 10px;border-radius:5px">저장</span><span style="font-size:10px;border:1px solid var(--line);padding:3px 10px;border-radius:5px">취소</span></div>
                </div>
              </div>'''

D = dict(
  slug="form", ko="폼 설계", en="Form design",
  desc="입력 칸을 어떻게 묶고 어떤 순서로 놓을지. 칸 수 줄이기, 레이블 자리, 단계 나누기, 임시 저장까지.",
  lede="칸 하나하나가 아니라 <b>칸들을 어떻게 묶고 줄일지</b>의 문제. 좋은 폼은 <b>짧은 폼</b>입니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>묶어 보기</b>를 켜고 꺼 보세요. 같은 칸 수인데도 묶으면 훨씬 짧아 보입니다.<br>
          <b>선택 칸 숨기기</b>를 켜면 꼭 채울 칸만 남습니다 — <b>칸 수를 줄이는 것</b>이 폼 설계의 거의 전부입니다.
          아래에 지금 <b>몇 칸을 채워야 하는지</b>가 세어집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "폼, 입력 양식, 서식, 등록 화면"),
    ("영어", "form, form design, input form"),
    ("같이 쓰는 말",
     "칸 하나가 <b>필드</b>(field), 칸 이름이 <b>레이블</b>, 칸 밑 설명이 <b>헬프 텍스트</b>·<b>힌트</b>입니다. "
     "여러 칸을 묶은 것이 <b>필드셋</b>(fieldset)·<b>섹션</b>이고, "
     "여러 화면으로 나눈 것이 <b>위저드</b>(wizard)·<b>스텝 폼</b>입니다."),
    ("자주 잘못 부름",
     "<b>필드</b> — <a href=\"../items/field.html\">입력 필드</a>는 칸 하나, 폼은 <b>칸들의 묶음</b>입니다.<br>"
     "<b>모달</b> — <a href=\"../items/modal.html\">모달</a>은 띄우는 방식일 뿐, 그 안에 폼이 들어가는 것입니다.<br>"
     "<b>검증</b> — <a href=\"validation.html\">입력 검증</a>은 폼의 한 부분이지 폼 자체가 아닙니다."),
  ]),
  axes=ax("폼 설계"),
  oneline="폼 설계의 첫 질문은 '어떻게 배치할까'가 아니라 <b>'이 칸이 정말 필요한가'</b>입니다. 지울 수 있는 칸이 가장 좋은 칸입니다.",
  s4_title="상태", s4_hint="칸이 아니라 폼 전체의 상태",
  states=states([
    (card(fld('상호') + fld('사업자번호', '', '- 없이 10자리')), "빈 폼", "<b>힌트</b>를 미리 둔다. 틀린 뒤에 알려 주면 늦다"),
    (card(fld('상호', '모란상회') + fld('사업자번호', '1248100998')), "채워진 폼", "고칠 때는 <b>기존 값</b>이 들어 있어야 한다"),
    (card(fld('상호', '모란상회') + fld('사업자번호', '124', err='10자리를 채워 주세요')), "오류", "<a href=\"validation.html\">검증</a>으로 이어진다"),
    (card('<div style="display:grid;gap:5px"><span class="skl" style="height:24px"></span><span class="skl" style="height:24px"></span></div>'),
     "불러오는 중", "<b>빈 칸을 보여 주고 나중에 채우면</b> 치던 글자를 덮어쓴다"),
    (card(fld('상호', '모란상회') + '<div style="display:flex;gap:5px"><span style="font-size:10px;background:var(--fg-muted);color:#fff;padding:3px 10px;border-radius:5px">저장 중…</span></div>'),
     "보내는 중", "버튼을 잠근다. 두 번 눌러 두 건이 생기는 사고가 흔하다"),
    (card('<div style="border:1px solid var(--line);border-radius:6px;padding:8px;font-size:9.5px;color:var(--fg-muted)">1 · 2 · <b style="color:var(--accent)">3</b> 단계<br><span style="font-size:8.5px">작성한 내용은 저장돼 있습니다</span></div>'),
     "여러 단계", "<b>어디쯤인지</b>와 <b>돌아갈 수 있는지</b>를 보여 준다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("폼", "&lt;form&gt;", "감싸야 <b>엔터로 제출</b>되고 브라우저가 자동 채움을 돕는다"),
    ("묶음", "fieldset / legend", "성격이 같은 칸들. 같은 수라도 <b>묶으면 짧아 보인다</b>"),
    ("한 줄에 한 칸", "single column", "눈이 한 길로 내려간다. 두 열은 <b>건너뛰는 칸</b>을 만든다"),
    ("레이블은 위", "label top", "폰에서도 안 깨지고 글자가 길어져도 버틴다"),
    ("선택 칸 표시", "(선택)", "필수에 <b>별표</b>를 다는 것보다 선택을 적는 쪽이 읽기 쉽다"),
    ("버튼", "주 동작 하나", "<b>저장</b>은 오른쪽·진한 색, <b>취소</b>는 약하게. 둘을 같은 무게로 두지 않는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>칸을 두 열로 놓지 않습니다.</b> 두 열이면 눈이 Z 자로 움직이고,
          사용자가 오른쪽 열을 통째로 못 보고 지나가는 일이 생깁니다.
          예외는 <b>떼어 놓으면 더 이상한 것</b>뿐입니다 — 시·도와 시·군·구, 시작일과 종료일,
          카드 유효기간의 월과 연도처럼 <b>한 덩어리로 읽히는 값</b>들입니다.</p>''',
  do=ul([
    "받을 것이 <b>여러 개</b>이고 한 번에 보내야 할 때",
    "값을 <b>고치는</b> 화면 — 기존 값이 들어 있어야 한다",
    "단계가 있는 등록 — <b>나눠야</b> 끝까지 간다",
  ]),
  dont=ul([
    "칸이 <b>하나</b>일 때 → 그냥 <a href=\"../items/field.html\">입력 필드</a>와 버튼",
    "'나중에 쓸지도 몰라서' 넣는 칸 — <b>지금 안 쓰면 지운다</b>",
    "열 칸을 한 화면에 — 세 묶음으로 나누거나 단계로 쪼갠다",
    "<code>&lt;form&gt;</code> 없이 <code>&lt;div&gt;</code>로 — 엔터도 자동 채움도 죽는다",
  ]),
  instead='칸 하나면 <a href="../items/field.html">입력 필드</a>, 고르기만 하면 <a href="../items/select.html">셀렉트</a>, 확인만 받으면 <a href="../items/dialog.html">다이얼로그</a>.',
  cases=cases([
    (card(group('가맹점', fld('상호', '모란상회')) + group('정산', fld('계좌', '')), "150px"),
     "묶은 폼", "칸 수는 같아도 <b>덩어리가 둘</b>로 보인다"),
    (card('<div style="display:flex;gap:4px;align-items:center;font-size:9px"><span style="width:14px;height:14px;border-radius:999px;background:var(--accent);color:#fff;display:grid;place-items:center">1</span><span style="flex:1;height:1px;background:var(--line)"></span><span style="width:14px;height:14px;border-radius:999px;border:1px solid var(--line);display:grid;place-items:center">2</span></div>' + fld('상호', '모란상회'), "150px"),
     "단계로 나눔", "칸이 많으면 <b>끝이 보이게</b> 쪼갠다"),
    (card('<div style="display:grid;grid-template-columns:1fr 1fr;gap:5px">' + fld('시작일', '11/01') + fld('종료일', '11/07') + '</div>', "150px"),
     "두 열이 맞는 경우", "<b>한 덩어리로 읽히는 값</b>만 나란히 둔다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 폼의 계약서",
  code_lede="<code>&lt;form&gt;</code>으로 감싸고, 묶음은 <code>&lt;fieldset&gt;</code>, 칸 이름은 <code>&lt;label for&gt;</code>로 답니다.",
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
    ("<kbd>Enter</kbd>", "<code>&lt;form&gt;</code> 안이면 제출된다. div 로 감싸면 안 된다"),
    ("<code>&lt;label for&gt;</code>", "칸마다. <b>이름을 눌러도 칸이 잡히게</b> 되고 터치 영역이 넓어진다"),
    ("<code>autocomplete</code>", "이름·전화·주소·카드. 적어 주면 브라우저가 채워 준다 — <b>가장 효과 큰 한 줄</b>"),
    ("<code>inputmode</code>", "폰 키보드를 바꾼다. 숫자 칸에 글자 키보드가 뜨면 짜증이 난다"),
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "'가맹점 묶음, 상호 입력'으로 읽힌다"),
    ("<code>aria-describedby</code>", "힌트를 칸에 붙인다. 그냥 밑에 적으면 안 읽힌다"),
  ]),
  backend=rows([
    ("서버가 다시 검사한다", "브라우저 검사는 <b>친절함</b>이지 방어가 아닙니다. 요청은 폼 없이도 보낼 수 있습니다."),
    ("두 번 눌러 두 건", "저장을 두 번 눌러 같은 건이 둘 생기는 사고가 흔합니다. 요청마다 <b>고유 키</b>(idempotency key)를 받아 같은 키는 한 번만 처리합니다."),
    ("임시 저장", "긴 폼은 중간에 끊깁니다. <b>초안</b>을 따로 저장하면 돌아왔을 때 이어 쓸 수 있습니다."),
    ("오류를 칸별로 돌려준다", "<code>{\"errors\":{\"no\":\"10자리여야 합니다\"}}</code>처럼 <b>어느 칸인지</b>를 함께 보내야 화면에서 그 칸에 붙일 수 있습니다."),
    ("칸이 늘면 버전이 생긴다", "저장된 옛 데이터에는 새 칸이 없습니다. <b>빈 값을 허용</b>하거나 기본값을 정해 둡니다."),
  ]),
  plat_lede="세 곳의 차이는 <b>레이블 자리</b>와 <b>저장 버튼 위치</b>입니다.",
  plats=plats([
    ("웹", "&lt;form&gt;",
     card(fld('상호', '모란상회'), "115px"),
     "레이블은 위, 저장은 폼 <b>아래</b>에 둡니다. 브라우저 자동 채움이 큰 몫을 합니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 폼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="display:flex;padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)"><span style="width:30%">상호</span><span>모란상회</span></div></div>
                <div style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">저장</div></div></div>''',
     "설정 화면처럼 <b>왼쪽 이름 · 오른쪽 값</b>으로 줄지어 놓고, 저장은 <b>오른쪽 위</b>에 둡니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 폼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-radius:4px 4px 0 0;border-bottom:1px solid var(--accent);padding:5px"><div style="font-size:5px;color:var(--accent)">상호</div><div style="font-size:6px">모란상회</div></div></div></div>''',
     "칸 이름이 <b>칸 안에서 위로 올라가는</b> 텍스트 필드를 씁니다. 저장은 아래쪽 버튼입니다."),
  ]),
  plat_note="\"폼 하나 만들어 주세요\"의 품은 <b>칸 수에 비례하지 않습니다.</b> 불러오기·임시 저장·중복 제출 막기·칸별 오류 표시까지가 한 벌이고, 칸이 하나든 열이든 이 뼈대는 같습니다. 반대로 칸을 세 개 지우는 일은 하루면 되고 효과는 가장 큽니다.",
  siblings=siblings("form"),
  related='''        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="../items/error.html"><b>오류 메시지</b><em>8부</em></a></li>''',
)
