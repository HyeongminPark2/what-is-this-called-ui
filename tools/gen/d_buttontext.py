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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">동사로 — 누르면 무슨 일이 나는가</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">두세 어절 — 넘으면 버튼이 아니라 문장이다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">조사 없이 — ‘정산을 내보내기’가 아니라 ‘내보내기’</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">취소 쪽은 약하게 — 색과 무게로 가른다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">마침표를 찍지 않는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">‘확인’은 무엇을 확인하는지 안 알려 준다</div>
                </div>
              </div>'''

D = dict(
  slug="buttontext", ko="버튼 문구", en="Button label",
  desc="누르면 무슨 일이 나는지를 버튼 글자만으로 알리는 법. 동사로, 두세 어절로, 조사 없이.",
  lede="버튼은 <b>누르면 무슨 일이 나는지</b>를 그 자리에서 말해야 합니다. 앞뒤 설명에 기대면 안 됩니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>버튼만 보고 맞히기</b>를 켜 보세요 — 앞뒤 설명이 사라지면
          <code>확인</code>·<code>제출</code>이 아무것도 안 알려 준다는 게 드러납니다.<br>
          판정은 세 가지만 봅니다. <b>동사가 있는가</b>, <b>두세 어절 안인가</b>,
          <b>빈 말이 아닌가</b>. 아래 칸에 직접 써 보면 바로 매겨집니다.</p>
        </div>''',
  names=rows([
    ("한국어", "버튼 문구, 버튼 라벨, 레이블"),
    ("영어", "button label, call to action (CTA), action label"),
    ("같이 쓰는 말",
     "사용자를 움직이게 하는 주 버튼을 <b>CTA</b>(call to action)라 부릅니다. "
     "화면 안의 짧은 글 전체는 <b>마이크로카피</b>(microcopy)이고, "
     "그 가운데 버튼·레이블·힌트를 묶어 <b>UX 라이팅</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>레이블</b> — <a href=\"../items/field.html\">입력 필드</a>의 칸 이름도 레이블이라 자주 섞입니다. 이쪽은 <b>버튼에 적힌 글자</b>입니다.<br>"
     "<b>이름 붙이기</b> — <a href=\"../items/name.html\">접근성의 이름</a>은 <b>기계가 읽는</b> 이름입니다. 눈에 보이는 글자와 다를 수 있습니다.<br>"
     "<b>카피</b> — 광고 문구를 뜻하기도 해서, 화면 안 글은 <b>UX 라이팅</b>으로 가려 부르는 편이 낫습니다."),
  ]),
  axes=ax("버튼 문구"),
  oneline="<b>버튼 글자만 가리고 읽어 보세요.</b> 무슨 일이 날지 모르겠으면 그 버튼은 아직 안 끝난 것입니다.",
  s4_title="문구별로", s4_hint="글자만 보고 알 수 있나",
  states=states([
    (dlg('정산 128건을 내보낼까요?', '취소', '확인', "152px", "무엇을 확인하는지 모른다", False),
     "‘확인’", "가장 흔하고 가장 <b>안 알려 주는</b> 말"),
    (dlg('정산 128건을 내보낼까요?', '취소', '내보내기', "152px", "누르면 무슨 일이 나는지 보인다", True),
     "‘내보내기’", "동사 하나로 끝난다"),
    (dlg('저장하지 않은 내용이 있습니다', '아니오', '예', "152px", "무엇에 대한 예인지 모른다", False),
     "‘예 / 아니오’", "질문이 길면 <b>답만 보고</b>는 못 고른다"),
    (dlg('저장하지 않은 내용이 있습니다', '저장하지 않고 나가기', '저장', "152px", "길어도 뜻이 분명하다", True),
     "둘 다 동사", "<b>길이보다 분명함</b>이 먼저다"),
    (one(btn('가맹점 삭제'), "", True, "무엇을 지우는지까지 적었다"),
     "대상까지", "같은 화면에 비슷한 버튼이 여럿일 때"),
    (one(btn('동료를 초대하고 메일을 발송합니다'), "", False, "버튼이 아니라 문장이다"),
     "너무 긴 것", "네 어절이 넘으면 <b>줄이거나 설명으로</b> 뺀다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("동사", "무슨 일이 나나", "'저장'·'삭제'·'보내기'. <b>이것이 버튼 문구의 전부</b>다"),
    ("길이", "두세 어절", "넘으면 설명으로 빼고 <b>버튼은 짧게</b>"),
    ("조사 없이", "‘내보내기’", "'정산을 내보내기'가 아니다. <b>버튼은 문장이 아니다</b>"),
    ("약한 쪽", "취소", "색과 무게로 가른다. <b>같은 무게로 두지 않는다</b>"),
    ("마침표", "찍지 않는다", "버튼은 문장이 아니다"),
    ("빈 말", "확인 · 제출", "무엇을 하는지 안 알려 준다. <b>가장 흔한 실수</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'확인'이 나쁜 말이라는 게 아닙니다.</b>
          앞 문장과 함께 보면 알아들을 수 있기 때문에,
          만들 때는 문제가 안 보입니다.
          문제가 드러나는 자리는 <b>글자만 따로 읽히는 곳</b>입니다 —
          스크린 리더가 버튼 목록을 읽어 줄 때, 키보드로 버튼만 훑을 때,
          알림에 버튼 두 개만 뜰 때. 그래서 기준을 '<b>앞 문장 없이도 되는가</b>'로 두면
          그 모든 경우가 한 번에 해결됩니다.</p>''',
  do=ul([
    "누르면 <b>무슨 일이 나는지</b> 동사로 적기",
    "같은 화면에 비슷한 버튼이 있으면 <b>대상까지</b>",
    "주 동작과 취소를 <b>무게로</b> 가르기",
  ]),
  dont=ul([
    "‘확인 / 취소’ · ‘예 / 아니오’ — <b>앞 문장에 기댄다</b>",
    "‘제출’ — 시험지가 아니다. <b>무엇을 하는지</b> 적는다",
    "버튼에 문장 쓰기 — 설명은 <b>위에</b> 둔다",
    "마침표 찍기",
  ]),
  instead='설명이 길어지면 <a href="../items/dialog.html">다이얼로그</a> 본문으로, 기계가 읽는 이름은 <a href="../items/name.html">이름 붙이기</a>, 위험한 동작의 문구는 <a href="destructive.html">위험한 동작</a>.',
  cases=cases([
    (ba('확인', '내보내기', '앞 문장 없이도 뜻이 선다'), "되묻는 창", "가장 자주 걸리는 자리"),
    (ba('제출', '신청하기', '‘제출’은 사용자의 말이 아니다'), "폼 보내기", "<a href=\"form.html\">폼</a> 끝의 버튼"),
    (ba('다음', '배송지 입력', '어디로 가는지 적는다'), "여러 단계", "<a href=\"checkout.html\">결제 흐름</a>·<a href=\"onboarding.html\">온보딩</a>에서"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 문구의 계약서",
  code_lede="보이는 글자가 <b>곧 이름</b>이 되게 적습니다.",
  code='''<span class="c">&lt;!-- 좋음: 글자만 읽어도 뜻이 선다 --&gt;</span>
&lt;<span class="t">button</span>&gt;내보내기&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"ghost"</span>&gt;취소&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 아이콘만 있을 때는 이름을 따로 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"정산 내보내기"</span>&gt;
  &lt;<span class="t">svg</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">svg</span>&gt;
&lt;/<span class="t">button</span>&gt;

<span class="c">&lt;!-- 같은 글자가 여럿일 때: 보이는 글자는 짧게, 이름은 길게 --&gt;</span>
&lt;<span class="t">button</span> <span class="a">aria-label</span>=<span class="s">"모란상회 삭제"</span>&gt;삭제&lt;/<span class="t">button</span>&gt;''',
  keys=kbd([
    ("보이는 글자 = 이름", "<code>aria-label</code>로 <b>전혀 다른 말</b>을 넣으면 음성으로 말하는 사람이 못 누른다"),
    ("아이콘만 있으면", "<code>aria-label</code>이 <b>반드시</b> 필요하다 — <a href=\"../items/name.html\">이름 붙이기</a>"),
    ("같은 글자가 여럿", "표에 '삭제'가 스무 개면 <b>어느 줄인지</b> 모른다. 이름에 대상까지 적는다"),
    ("<code>&lt;button&gt;</code>으로", "<code>&lt;div onclick&gt;</code>은 <b>키보드로 안 눌린다</b> — <a href=\"../items/semantics.html\">시맨틱 태그</a>"),
    ("글자가 길어지면", "버튼 폭이 늘어난다. <code>min-width</code>로 잡고 <b>줄바꿈을 허용</b>한다"),
    ("번역", "영어는 짧고 한국어는 길다. <b>영어 기준으로 폭을 잡으면</b> 한국어에서 넘친다"),
  ]),
  backend=rows([
    ("문구를 코드에 박지 않는다", "버튼 글자는 <b>가장 자주 바뀌는</b> 것입니다. 한곳에 모아 두면 고치기 쉽습니다."),
    ("같은 동작에 같은 말", "서버 응답 메시지와 버튼 글자가 다르면(‘발송’ vs ‘보내기’) <b>다른 기능처럼</b> 보입니다."),
    ("기록에 남길 이름", "분석 로그의 이벤트 이름과 버튼 글자를 <b>따로</b> 둡니다. 글자가 바뀔 때마다 지표가 끊기면 안 됩니다."),
  ]),
  plat_lede="<b>글자 버튼이냐 칠한 버튼이냐</b>가 갈립니다.",
  plats=plats([
    ("웹", "&lt;button&gt;",
     one(btn('내보내기') + ' ' + btn('취소', False), "", None, "", "110px"),
     "주 동작은 칠하고 취소는 테두리만. <b>동사로 적는</b> 관례는 같습니다."),
    ("iOS", "글자 버튼",
     '''              <div class="phone" role="img" aria-label="iOS 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:5px;top:14px;font-size:6px;color:var(--accent)">취소</span>
                <span style="position:absolute;right:5px;top:14px;font-size:6px;color:var(--accent);font-weight:700">저장</span></div></div>''',
     "칠하지 않고 <b>색만 입힌 글자</b>가 많습니다. 그래서 문구가 더 중요합니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 버튼 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;right:5px;bottom:10px;font-size:6px;color:var(--accent);font-weight:700">저장</span>
                <span style="position:absolute;right:28px;bottom:10px;font-size:6px;color:var(--accent)">취소</span></div></div>''',
     "다이얼로그 버튼은 <b>글자만</b>. 역시 '확인'보다 동사를 권합니다."),
  ]),
  plat_note="시안에 <b>'확인 / 취소'</b>라고 적혀 오면 그대로 넣기 쉽습니다. 그런데 이건 디자이너가 문구를 안 정한 것이지 <b>정해서 그렇게 쓴 것이 아닌</b> 경우가 많습니다. 받을 때 \"이 버튼을 누르면 무슨 일이 납니까\"를 한 번 물어보면 대개 그 자리에서 더 나은 말이 나옵니다.",
  siblings=siblings("buttontext"),
  related='''        <li><a href="../items/dialog.html"><b>다이얼로그</b><em>6부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
