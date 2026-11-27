# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(inner, note, w="152px"):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="height:62px;border:1px solid var(--line);border-radius:6px;background:var(--bg);'
            'position:relative;overflow:hidden">' + inner + '</div>'
            '<span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">' + note + '</span></div>')

BAR = ('<div style="position:absolute;left:0;right:0;top:0;height:16px;background:var(--surface);'
       'border-bottom:1px solid var(--line)"></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뒤로 — iOS 는 ‹ 와 이전 화면 이름, 안드로이드는 ← 만</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">주 동작 — iOS 는 오른쪽 위, 안드로이드는 오른쪽 아래 FAB</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">확인·취소 — iOS 는 반반, 안드로이드는 둘 다 오른쪽</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">탭 — iOS 는 색만, M3 는 알약 바탕까지</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">웹은 제3의 자리 — 흉내보다 웹 관례</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한쪽 규격을 그대로 옮기면 둘 다에서 어색하다</div>
                </div>
              </div>'''

D = dict(
  slug="platformdiff", ko="HIG와 Material의 차이", en="HIG vs Material",
  desc="같은 화면을 iOS·안드로이드·웹이 다르게 그린다. 자리와 차례가 어떻게 다르고 무엇을 따를지.",
  lede="같은 화면을 세 곳에서 그리면 <b>자리가 달라집니다.</b> 어느 쪽이 옳은 게 아니라 <b>이미 배운 자리</b>가 다릅니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>보고 싶은 것을 골라 보세요 — <b>뒤로 가는 길 · 주 동작의 자리 · 켜고 끄는 부품 ·
          알림의 버튼 차례 · 아래 탭</b>이 세 곳에서 어떻게 다른지 나란히 나옵니다.<br>
          아래 한 줄은 그 차이를 <b>웹에서 어떻게 다룰지</b>에 대한 정리입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "애플 휴먼 인터페이스 가이드라인, 머티리얼 디자인, 플랫폼 관례"),
    ("영어", "Apple HIG (Human Interface Guidelines), Material Design 3"),
    ("같이 쓰는 말",
     "애플 쪽이 <b>HIG</b>, 구글 쪽이 <b>머티리얼</b>(현재 M3)입니다. "
     "OS 가 정해 둔 모양을 그대로 쓰는 것을 <b>네이티브 느낌</b>이라 하고, "
     "한 벌로 양쪽에 올리는 것을 <b>크로스 플랫폼</b>이라 합니다. "
     "어느 쪽도 아닌 자기 모양을 쓰는 것은 <b>브랜드 UI</b>입니다."),
    ("자주 잘못 부름",
     "<b>디자인 시스템</b> — HIG·M3 는 OS 의 <b>관례 모음</b>이고, 디자인 시스템은 한 조직의 <b>부품 모음</b>입니다.<br>"
     "<b>머티리얼</b> — 구글 제품의 모양이지 '안드로이드의 유일한 답'은 아닙니다.<br>"
     "<b>네이티브</b> — 기술(스위프트·코틀린)을 가리키기도 하고 <b>모양</b>을 가리키기도 해 말이 자주 엇갈립니다."),
  ]),
  axes=ax("HIG와 Material의 차이"),
  oneline="<b>웹은 제3의 자리입니다.</b> 세 곳을 다 흉내 내려다 셋 모두에서 어색해지느니, <b>웹의 관례</b>를 지키는 편이 낫습니다.",
  s4_title="같은 화면, 다른 자리", s4_hint="무엇이 어디로 가나",
  states=states([
    (box(BAR + '<span style="position:absolute;left:4px;top:4px;font-size:8px;color:var(--accent)">‹ 정산</span>'
         '<span style="position:absolute;left:50%;top:4px;transform:translateX(-50%);font-size:8px;font-weight:700">모란상회</span>',
         "iOS — ‹ + 이전 화면 이름"),
     "뒤로 가는 길", "안드로이드는 <b>← 만</b>, 웹은 브라우저가 준다"),
    (box(BAR + '<span style="position:absolute;right:4px;top:4px;font-size:8px;color:var(--accent);font-weight:700">저장</span>'
         '<span style="position:absolute;left:4px;top:4px;font-size:8px;color:var(--accent)">취소</span>',
         "iOS — 오른쪽 위 글자 버튼"),
     "주 동작의 자리", "안드로이드는 <b>오른쪽 아래 FAB</b>, 웹은 폼 아래"),
    (box('<span style="position:absolute;left:5px;top:22px;font-size:8px">알림 받기</span>'
         '<span style="position:absolute;right:5px;top:20px;width:22px;height:13px;border-radius:999px;background:var(--accent)">'
         '<span style="position:absolute;right:1px;top:1px;width:11px;height:11px;border-radius:50%;background:#fff"></span></span>',
         "iOS — 누르면 바로 적용"),
     "켜고 끄는 부품", "M3 는 <b>✓ 가 붙고</b>, 웹은 저장 버튼이 있으면 체크박스"),
    (box('<div style="position:absolute;left:8px;right:8px;top:8px;bottom:8px;background:var(--surface);border:1px solid var(--line);border-radius:5px">'
         '<span style="position:absolute;left:5px;top:4px;font-size:8px;font-weight:700">지울까요?</span>'
         '<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);font-size:7px">'
         '<span style="flex:1;text-align:center;padding:2px 0;border-right:1px solid var(--line);color:var(--accent)">취소</span>'
         '<span style="flex:1;text-align:center;padding:2px 0;color:var(--danger);font-weight:700">삭제</span></div></div>',
         "iOS — 반반으로 나눈다"),
     "알림의 버튼 차례", "안드로이드는 <b>둘 다 오른쪽 아래</b>, 웹은 확인이 바깥쪽"),
    (box('<div style="position:absolute;left:0;right:0;bottom:0;height:18px;border-top:1px solid var(--line);background:var(--surface);display:flex;font-size:6px;text-align:center;align-items:center">'
         '<span style="flex:1;color:var(--accent)">정산</span><span style="flex:1;color:var(--fg-muted)">가맹점</span><span style="flex:1;color:var(--fg-muted)">설정</span></div>',
         "iOS — 색으로만 가른다"),
     "아래 탭", "M3 는 <b>알약 바탕</b>, 웹은 탭이 <b>위</b>에 있다"),
    (box('<span style="position:absolute;left:5px;top:8px;font-size:8px;font-weight:700">웹</span>'
         '<span style="position:absolute;left:5px;top:24px;font-size:7px;color:var(--fg-muted)">브라우저 ← · 폼 아래 버튼</span>'
         '<span style="position:absolute;left:5px;top:36px;font-size:7px;color:var(--fg-muted)">위쪽 탭 · 확인이 바깥쪽</span>',
         "웹 — 제3의 자리"),
     "웹의 관례", "셋을 흉내 내기보다 <b>한 가지로 통일</b>한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤로", "‹ 이름 / ← / 브라우저", "iOS 만 <b>이전 화면 이름</b>을 함께 적는다"),
    ("주 동작", "오른쪽 위 / FAB / 폼 아래", "안드로이드만 <b>떠 있는 동그란 버튼</b>을 쓴다"),
    ("확인·취소", "반반 / 오른쪽 / 오른쪽", "iOS 만 <b>반으로 나눠</b> 놓는다"),
    ("탭", "색 / 알약 / 위쪽", "M3 는 <b>색만으로 안 가른다</b>"),
    ("웹", "제3의 자리", "흉내 내기보다 <b>웹 관례</b>를 따른다"),
    ("섞으면", "둘 다 어색", "아이폰의 FAB, 안드로이드의 ‹ 는 <b>둘 다 틀린</b> 모양"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          실무에서 자주 나오는 결론은 <b>'하나로 통일한다'</b>입니다.
          OS 마다 확인·취소 차례를 바꾸면 코드가 갈리고 시험할 화면이 두 배가 되는데,
          얻는 것은 <b>미묘한 익숙함</b>뿐입니다.
          다만 <b>뒤로가기</b>만은 예외입니다 — 그건 취향이 아니라
          <a href="systemback.html">OS 가 쥐고 있는 동작</a>이라, 따르지 않으면
          앱이 꺼지는 쪽으로 바로 드러납니다.</p>''',
  do=ul([
    "<b>뒤로가기</b>는 OS 를 따른다 — 선택이 아니다",
    "셋 다 올리는 앱이라면 <b>한 가지로 통일</b>하고 그렇게 적어 둔다",
    "OS 부품을 쓸 때는 <b>그 OS 의 자리</b>에",
  ]),
  dont=ul([
    "iOS 화면에 <b>FAB</b> — 그 자리에 아무것도 없는 OS 다",
    "안드로이드에서 <b>‹ 이전 화면 이름</b> — 거기선 ← 만 쓴다",
    "웹에 아래 탭을 <b>PC 폭에서도</b> — 아래쪽은 웹의 자리가 아니다",
    "OS 마다 <b>확인·취소를 바꾸기</b> — 얻는 것보다 비싸다",
  ]),
  instead='웹의 자리는 <a href="../items/appbar.html">앱바</a>·<a href="../items/tabs.html">탭</a>·<a href="../items/dialog.html">다이얼로그</a> 항목에 정리돼 있다. 뒤로가기는 <a href="systemback.html">시스템 백</a>.',
  cases=cases([
    (box(BAR + '<span style="position:absolute;right:4px;top:4px;font-size:8px;color:var(--accent);font-weight:700">저장</span>', "iOS — 오른쪽 위"),
     "저장 버튼", "같은 버튼이 <b>세 자리</b>에 간다"),
    (box('<div style="position:absolute;right:6px;bottom:6px;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:11px">+</div>', "안드로이드 — FAB"),
     "새로 만들기", "<b>엄지가 닿는 자리</b>에 둔 것"),
    (box('<div style="position:absolute;left:5px;bottom:6px;display:flex;gap:4px">'
         '<span style="font-size:7px;padding:2px 6px;border-radius:4px;background:var(--accent);color:#fff">저장</span>'
         '<span style="font-size:7px;padding:2px 6px;border-radius:4px;border:1px solid var(--line)">취소</span></div>', "웹 — 폼 아래 왼쪽"),
     "웹의 자리", "주 동작이 먼저, 취소는 <b>약하게</b> 옆에"),
  ]),
  s8_title="따를 것과 정할 것", s8_hint="이 관례의 계약서",
  code_lede="따라야 하는 것과 <b>정하면 되는 것</b>을 갈라 적어 둡니다.",
  code='''<span class="c">// 반드시 OS 를 따른다 — 안 따르면 바로 사고가 난다</span>
- 뒤로가기 (시스템 백 · 가장자리 제스처)
- 세이프 에어리어 · 노치 · 홈 인디케이터
- 글자 크기 설정 · 모션 줄이기 · 다크 모드

<span class="c">// 팀이 정하면 되는 것 — 하나로 통일하는 편이 싸다</span>
- 확인 · 취소의 차례
- 주 동작의 자리
- 스위치냐 체크박스냐
- 탭을 위에 둘지 아래에 둘지

<span class="c">/* 웹에서 폰 폭일 때만 아래 탭을 쓰고 싶다면 */</span>
@media (max-width: 560px) {
  .tabs { <span class="a">position</span>: fixed; <span class="a">bottom</span>: <span class="a">0</span>; <span class="a">padding-bottom</span>: <span class="a">env</span>(safe-area-inset-bottom); }
}''',
  keys=kbd([
    ("OS 부품을 쓰면 접근성이 딸려 온다", "시스템 스위치·날짜 선택기는 스크린 리더 대응이 <b>이미 들어 있다</b>"),
    ("직접 만들면 직접 챙긴다", "모양만 흉내 내고 <code>role</code>·키보드를 빼면 <b>껍데기</b>가 된다"),
    ("글자 크기 설정", "두 OS 모두 사용자가 키울 수 있다. <b>px 로 못 박으면</b> 안 커진다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>·다크 모드", "OS 설정이라 어느 쪽에서든 따라야 한다"),
    ("<a href=\"../items/safearea.html\">세이프 에어리어</a>", "노치·홈 인디케이터는 <b>협상 대상이 아니다</b>"),
    ("<a href=\"systemback.html\">뒤로가기</a>", "따르지 않으면 <b>앱이 꺼진다.</b> 가장 먼저 확인할 것"),
  ]),
  backend=rows([
    ("화면이 둘이면 API 도 둘이 된다", "OS 마다 흐름을 다르게 만들면 <b>단계와 응답</b>도 갈립니다. 통일하면 서버가 한 벌로 끝납니다."),
    ("기기별 통계", "같은 기능이 한쪽 OS 에서만 안 쓰인다면 <b>자리가 달라서</b>일 수 있습니다."),
    ("푸시 알림", "두 OS 의 체계가 완전히 달라 <b>서버 쪽 작업이 두 벌</b>입니다. 일정에 따로 잡습니다."),
  ]),
  plat_lede="이 항목 자체가 세 곳의 비교라, 표로 적어 둡니다.",
  plats=plats([
    ("웹", "관례",
     box('<span style="position:absolute;left:4px;top:4px;font-size:7px">← → ⟳</span>'
         '<span style="position:absolute;left:4px;top:22px;font-size:7px;color:var(--fg-muted)">위쪽 탭 · 폼 아래 버튼</span>', "브라우저가 뒤로를 준다", "105px"),
     "표준 부품이 적고 관례가 넓습니다. 그래서 <b>팀이 정해 적어 두는</b> 일이 중요합니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 관례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px;color:var(--accent)">‹ 정산</span>
                <span style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">저장</span>
                <div style="position:absolute;left:0;right:0;bottom:0;height:12px;border-top:1px solid var(--line);display:flex;font-size:5px;text-align:center;align-items:center"><span style="flex:1;color:var(--accent)">정산</span><span style="flex:1;color:var(--fg-muted)">설정</span></div></div></div>''',
     "<b>글자 버튼</b>이 많고 색으로 누를 수 있음을 알립니다. 위쪽 좌우가 동작 자리입니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 관례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px">← 모란상회</span>
                <div style="position:absolute;right:4px;bottom:16px;width:14px;height:14px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:8px">+</div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:12px;border-top:1px solid var(--line);display:flex;font-size:5px;text-align:center;align-items:center"><span style="flex:1"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:0 4px">정산</span></span><span style="flex:1;color:var(--fg-muted)">설정</span></div></div></div>''',
     "<b>면과 바탕</b>으로 상태를 알립니다. 주 동작은 아래쪽 FAB 입니다."),
  ]),
  plat_note="\"아이폰처럼 만들어 주세요\"와 \"안드로이드도 되게\"가 같은 문장 안에 오면 <b>자리 다툼이 시작된 것</b>입니다. 이때 쓸 수 있는 가장 싼 답은 \"뒤로가기와 세이프 에어리어는 OS 를 따르고, 나머지는 한 가지로 통일합니다\"입니다 — 사고가 나는 쪽은 앞의 둘뿐이고, 뒤의 것들은 통일해도 아무도 불평하지 않습니다.",
  siblings=siblings("platformdiff"),
  related='''        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/switch.html"><b>스위치</b><em>4부</em></a></li>''',
)
