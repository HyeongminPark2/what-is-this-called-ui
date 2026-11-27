# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def dlg(title, b1, b2, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:5px">'
            '<span style="font-size:9.5px;font-weight:700">' + title + '</span>'
            '<div style="display:flex;gap:5px;justify-content:flex-end">' + btn(b1, False) + btn(b2, True) + '</div></div>'
            + ('<span style="font-size:8.5px;color:' + (col if ok is not None else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">누르면 무슨 일이 나는지 동사로 적음</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">두세 어절을 넘으면 버튼이 아니라 문장이 됨</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">조사 없이 ‘정산을 내보내기’ 대신 ‘내보내기’</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">취소 쪽은 색과 무게를 약하게 해 구별함</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">마침표는 찍지 않음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘확인’만으로는 무엇을 확인하는지 알 수 없음</div>
                </div>
              </div>'''

D = dict(
  slug="buttontext", ko="버튼 문구", en="Button label",
  desc="누르면 무슨 일이 일어나는지를 버튼 글자만으로 알리는 방법을 다룹니다. 동사를 써서 두세 어절 안에, 조사 없이 적습니다.",
  lede="버튼 글자는 <b>누르면 무슨 일이 일어나는지</b>를 버튼만 보고도 알 수 있게 적어야 합니다. 앞뒤 설명을 읽어야 뜻이 통하는 버튼은, 버튼 글자만 따로 읽히는 상황에서 무엇을 하는지 알 수 없기 때문입니다.",
  axes_lede="화면 문구는 사용자가 <b>무엇을 하면 되는지</b> 알려 줍니다. 아래 네 가지로 문구마다 다른 점을 봅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>버튼만 보고 맞히기</b>를 켜 보세요. 앞뒤 설명이 사라지면
          <code>확인</code>·<code>제출</code> 같은 버튼만으로는 무슨 일이 일어날지 전혀 알 수 없다는 것이 드러납니다.<br>
          판정 기준은 <b>동사가 있는가</b>, <b>두세 어절 안인가</b>,
          <b>빈 말이 아닌가</b> 세 가지입니다. 아래 칸에 버튼 문구를 직접 써 보면 이 기준으로 바로 판정해 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버튼 문구, 버튼 라벨, 레이블"),
    ("영어", "button label, call to action (CTA), action label"),
    ("같이 쓰는 말",
     "사용자가 다음 행동을 하도록 이끄는 주 버튼은 <b>CTA</b>(call to action)라고 부릅니다. "
     "화면 안의 짧은 글 전체는 <b>마이크로카피</b>(microcopy)라고 하고, "
     "그 가운데 버튼·레이블·힌트를 묶어 <b>UX 라이팅</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>레이블</b> — <a href=\"../items/field.html\">입력 필드</a>의 칸 이름도 레이블이라고 불러서 자주 섞이지만, 이 항목에서 다루는 것은 <b>버튼에 적힌 글자</b>입니다.<br>"
     "<b>이름 붙이기</b> — <a href=\"../items/name.html\">접근성의 이름</a>은 스크린 리더 같은 <b>보조기기가 읽는</b> 이름이라서, 눈에 보이는 버튼 글자와 다를 수 있습니다.<br>"
     "<b>카피</b> — 광고 문구를 가리킬 때도 쓰는 말이라서, 화면 안의 글은 <b>UX 라이팅</b>이라고 따로 부르는 편이 낫습니다."),
  ]),
  axes=ax("버튼 문구"),
  oneline="<b>앞뒤 설명을 가리고 버튼 글자만 읽어 보세요.</b> 그래도 누르면 무슨 일이 일어날지 알 수 없다면 그 버튼 문구는 더 고쳐야 합니다.",
  s4_title="흔한 버튼 문구와 고친 문구", s4_hint="버튼 글자만 보고 뜻을 알 수 있는지 견주기",
  states=states([
    (dlg('정산 128건을 내보낼까요?', '취소', '확인', "152px", "무엇을 확인하는지 알 수 없음", False),
     "‘확인’이라고 적은 버튼", "가장 흔히 쓰지만, 누르면 무슨 일이 일어나는지 <b>알려 주지 않습니다</b>"),
    (dlg('정산 128건을 내보낼까요?', '취소', '내보내기', "152px", "누르면 무슨 일이 나는지 보임", True),
     "‘내보내기’라고 적은 버튼", "동사 하나만으로 무슨 일이 일어나는지 알려 줍니다"),
    (dlg('저장하지 않은 내용이 있습니다', '아니오', '예', "152px", "무엇에 대한 예인지 알 수 없음", False),
     "‘예 / 아니오’로 답하게 한 버튼", "질문이 길면 <b>답만 보고</b>는 어느 쪽을 눌러야 할지 고를 수 없습니다"),
    (dlg('저장하지 않은 내용이 있습니다', '저장하지 않고 나가기', '저장', "152px", "길어도 뜻이 분명함", True),
     "두 버튼을 모두 동사로 적은 경우", "버튼이 조금 길어지더라도 <b>뜻이 분명한 쪽</b>을 고릅니다"),
    (one(btn('가맹점 삭제'), "", True, "무엇을 지우는지까지 적음"),
     "대상까지 적은 버튼", "같은 화면에 비슷한 버튼이 여럿이면 무엇에 대한 동작인지 대상까지 적습니다"),
    (one(btn('동료를 초대하고 메일을 발송합니다'), "", False, "버튼이 아니라 문장이 됨"),
     "버튼 문구가 너무 길 때", "네 어절이 넘으면 문구를 <b>줄이거나 버튼 밖 설명으로</b> 옮깁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("동사", "무슨 일이 나나", "'저장'·'삭제'·'보내기'처럼 누르면 일어나는 일을 동사로 적습니다. <b>버튼 문구에서 가장 중요한 부분</b>입니다"),
    ("길이", "두세 어절", "두세 어절을 넘기면 설명은 버튼 밖으로 빼고 <b>버튼은 짧게</b> 둡니다"),
    ("조사 없이", "‘내보내기’", "'정산을 내보내기'처럼 조사를 붙이지 않습니다. <b>버튼 문구는 문장이 아니기</b> 때문입니다"),
    ("약한 쪽", "취소", "색과 무게로 주 동작과 구별하고, 두 버튼을 <b>같은 무게로 두지 않습니다</b>"),
    ("마침표", "찍지 않음", "버튼 문구는 문장이 아니므로 마침표를 찍지 않습니다"),
    ("빈 말", "확인 · 제출", "누르면 무엇을 하는지 알려 주지 않습니다. <b>가장 흔한 실수</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'확인'도 앞 문장과 함께 보면 뜻이 통합니다.</b>
          그래서 화면을 만드는 사람 눈에는 문제가 잘 보이지 않습니다.
          문제는 <b>버튼 글자만 따로 읽히는 곳</b>에서 드러나는데,
          스크린 리더가 버튼 목록을 읽어 줄 때, 키보드로 버튼만 훑어 갈 때,
          알림에 버튼 두 개만 뜰 때가 그렇습니다. 버튼 문구의 기준을 '<b>앞 문장 없이도 뜻이 통하는가</b>'로 잡으면
          이런 경우를 모두 함께 막을 수 있습니다.</p>''',
  do=ul([
    "누르면 <b>무슨 일이 나는지</b> 동사로 적기",
    "같은 화면에 비슷한 버튼이 있으면 <b>대상까지</b> 적기",
    "주 동작과 취소를 <b>무게로</b> 가르기",
  ]),
  do_title="버튼 문구를 쓸 때 지킬 것", dont_title="버튼 문구에서 피할 것",
  instead_title="버튼 문구와 함께 보면 좋은 항목",
  dont=ul([
    "‘확인 / 취소’ · ‘예 / 아니오’로 적을 때. 앞 문장을 읽어야만 <b>뜻이 통하는</b> 문구입니다",
    "‘제출’로 적을 때. 사용자가 실제로 <b>무엇을 하는지</b>를 적습니다",
    "버튼에 문장을 쓸 때. 설명은 버튼 <b>위에</b> 따로 둡니다",
    "마침표를 찍을 때",
  ]),
  instead='설명이 길어져 버튼에 담기 어려우면 <a href="../items/dialog.html">다이얼로그</a> 본문에 적습니다. 보조기기가 읽는 이름은 <a href="../items/name.html">이름 붙이기</a>에서, 지우기처럼 위험한 동작에 붙일 문구는 <a href="destructive.html">위험한 동작</a>에서 다룹니다.',
  cases=cases([
    (ba('확인', '내보내기', '앞 문장 없이도 뜻이 통함'), "되묻는 창의 확인 버튼 고치기", "‘확인’ 같은 빈 말 버튼이 가장 자주 나오는 자리입니다"),
    (ba('제출', '신청하기', '‘제출’은 사용자가 쓰는 말이 아님'), "폼을 보내는 버튼 고치기", "<a href=\"form.html\">폼</a> 맨 끝에 두는 버튼입니다"),
    (ba('다음', '배송지 입력', '어디로 가는지 적음'), "여러 단계 화면의 다음 버튼 고치기", "<a href=\"checkout.html\">결제 흐름</a>·<a href=\"onboarding.html\">온보딩</a>처럼 단계가 나뉜 화면에서 자주 봅니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="버튼에 보이는 글자가 <b>그대로 접근성 이름</b>이 되도록 적습니다.",
  code='''<span class="c">&lt;!-- 좋음: 글자만 읽어도 뜻이 통한다 --&gt;</span>
&lt;<span class="t">button</span>&gt;내보내기&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"ghost"</span>&gt;취소&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘만 있을 때는 이름을 따로 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 내보내기"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 같은 글자가 여럿일 때: 보이는 글자는 짧게, 이름은 길게 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"모란상회 삭제"</span>&gt;삭제&lt;/<span class="t">button</span>&gt;''',
  keys_heads="<th>지킬 규칙과 마크업</th><th>지키는 방법과 이유</th>",
  keys=kbd([
    ("보이는 글자를 이름으로 쓰기", "<code>aria-label</code>에 보이는 글자와 <b>전혀 다른 말</b>을 넣으면, 음성 명령으로 화면을 다루는 사용자가 보이는 글자를 말해도 버튼을 누를 수 없습니다"),
    ("아이콘만 있는 버튼", "<code>aria-label</code>로 이름을 <b>반드시</b> 붙여야 합니다(<a href=\"../items/name.html\">이름 붙이기</a>)"),
    ("같은 글자의 버튼이 여럿일 때", "표에 '삭제' 버튼이 스무 개 있으면 <b>어느 줄의 버튼인지</b> 알 수 없으므로, 접근성 이름에 대상까지 적습니다"),
    ("<code>&lt;button&gt;</code>으로 만들기", "<code>&lt;div onclick&gt;</code>으로 만든 버튼은 <b>키보드로 누를 수 없습니다</b>(<a href=\"../items/semantics.html\">시맨틱 태그</a>)"),
    ("글자가 길어질 때", "글자가 길어지면 버튼 폭도 늘어나므로, <code>min-width</code>로 최소 폭을 잡고 <b>줄바꿈을 허용</b>합니다"),
    ("다른 언어로 옮길 때", "영어 문구는 짧고 한국어 문구는 길어지기 쉬워서, <b>영어 기준으로 폭을 잡으면</b> 한국어 글자가 버튼 밖으로 넘칩니다"),
  ]),
  backend=rows([
    ("문구를 코드 곳곳에 적지 않기", "버튼 글자는 화면에서 <b>가장 자주 바뀌는</b> 부분이라서, 코드 곳곳에 적지 않고 한곳에 모아 두면 고치기 쉽습니다."),
    ("같은 동작에는 같은 말 쓰기", "서버 응답 메시지와 버튼 글자가 ‘발송’과 ‘보내기’처럼 서로 다르면, 사용자에게는 같은 동작이 <b>다른 기능처럼</b> 보입니다."),
    ("분석 로그의 이벤트 이름 따로 두기", "분석 로그의 이벤트 이름은 버튼 글자와 <b>따로</b> 둡니다. 버튼 글자를 이벤트 이름으로 쓰면 문구를 고칠 때마다 이벤트 이름도 바뀌어서 지표가 끊기기 때문입니다."),
  ]),
  plat_lede="플랫폼마다 버튼을 <b>글자만으로 그리는지, 배경을 칠해 그리는지</b>가 다릅니다.",
  plats=plats([
    ("웹", "&lt;button&gt;",
     one(btn('내보내기') + ' ' + btn('취소', False), "", None, "", "110px"),
     "주 동작은 배경을 칠하고 취소는 테두리만 그립니다. 버튼 문구를 <b>동사로 적는</b> 관례는 다른 플랫폼과 같습니다."),
    ("iOS", "글자 버튼",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:5px;top:14px;font-size:6px;color:var(--accent)">취소</span>
                <span style="position:absolute;right:5px;top:14px;font-size:6px;color:var(--accent);font-weight:700">저장</span></div></div>''',
     "배경을 칠하지 않고 <b>글자에 색만 입힌</b> 버튼이 많습니다. 모양으로 구별할 단서가 적은 만큼 문구가 더 중요합니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:5px;bottom:10px;font-size:6px;color:var(--accent);font-weight:700">저장</span>
                <span style="position:absolute;right:28px;bottom:10px;font-size:6px;color:var(--accent)">취소</span></div></div>''',
     "다이얼로그 버튼은 <b>글자만</b>으로 그립니다. Material 지침도 '확인'보다 동사를 쓰라고 권합니다."),
  ]),
  plat_note="시안에 <b>'확인 / 취소'</b>라고 적혀 오면 그대로 옮겨 넣기 쉽습니다. 하지만 이런 문구는 디자이너가 고민해서 고른 말이라기보다 <b>아직 문구를 정하지 않고 채워 둔 자리</b>인 경우가 많습니다. 시안을 받을 때 \"이 버튼을 누르면 무슨 일이 납니까\"라고 한 번 물어보면 대개 그 자리에서 더 나은 문구가 나옵니다.",
  siblings=siblings("buttontext"),
  related='''        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
