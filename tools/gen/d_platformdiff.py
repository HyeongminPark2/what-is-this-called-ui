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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">뒤로 버튼은 iOS가 ‹와 이전 화면 이름, 안드로이드가 ←만</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">주 동작은 iOS가 오른쪽 위, 안드로이드가 오른쪽 아래 FAB</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">확인·취소는 iOS가 반반, 안드로이드가 둘 다 오른쪽</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">고른 탭은 iOS가 색만, M3가 알약 바탕까지 표시</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">웹은 흉내 대신 웹 관례를 따름</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한쪽 규격을 그대로 옮기면 양쪽에서 어색함</div>
                </div>
              </div>'''

D = dict(
  slug="platformdiff", ko="HIG와 Material의 차이", en="HIG vs Material",
  desc="같은 화면을 iOS와 안드로이드, 웹이 어떻게 다르게 그리는지, 버튼의 자리와 차례가 어디서 갈리고 그중 무엇을 따라야 하는지 보여 주는 항목입니다.",
  lede="같은 화면이라도 iOS와 안드로이드, 웹에서 그리면 버튼이 놓이는 <b>자리가 달라집니다.</b> 어느 쪽이 옳다기보다, 각 플랫폼 사용자가 <b>이미 익숙해진 자리</b>가 서로 다릅니다.",
  axes_lede="PC와 폰의 차이는 기계 자체보다 화면을 쓰는 <b>전제</b>에 있습니다. 아래 네 가지를 물어보면 두 환경이 어디서 갈리는지 알 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>보고 싶은 것을 골라 보세요. <b>뒤로 가는 방법 · 주 동작 버튼의 자리 · 켜고 끄는 부품 ·
          알림 창의 버튼 차례 · 아래 탭의 모양</b>이 세 플랫폼에서 어떻게 다른지 나란히 보여 줍니다.<br>
          아래 한 줄에는 그 차이를 <b>웹에서 어떻게 다룰지</b> 정리해 두었습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "애플 휴먼 인터페이스 가이드라인, 머티리얼 디자인, 플랫폼 관례"),
    ("영어", "Apple HIG (Human Interface Guidelines), Material Design 3"),
    ("같이 쓰는 말",
     "애플이 낸 지침이 <b>HIG</b>이고, 구글이 낸 지침이 <b>머티리얼</b>(현재 M3)입니다. "
     "OS가 정해 둔 모양을 그대로 쓰는 것을 <b>네이티브 느낌</b>이라고 하고, "
     "코드 한 벌로 두 OS에 앱을 올리는 것을 <b>크로스 플랫폼</b>이라고 합니다. "
     "어느 OS의 모양도 따르지 않고 자기 회사만의 모양을 쓰면 <b>브랜드 UI</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>디자인 시스템</b> — HIG와 M3는 OS가 정한 <b>관례 모음</b>이고, 디자인 시스템은 한 조직이 만들어 쓰는 <b>부품 모음</b>입니다.<br>"
     "<b>머티리얼</b> — 머티리얼은 구글 제품의 모양일 뿐, 안드로이드 앱이 꼭 따라야 하는 유일한 모양은 아닙니다.<br>"
     "<b>네이티브</b> — 스위프트나 코틀린 같은 개발 기술을 가리킬 때도 있고 OS 고유의 <b>모양</b>을 가리킬 때도 있어서, 대화에서 뜻이 자주 엇갈립니다."),
  ]),
  axes=ax("HIG와 Material의 차이"),
  oneline="<b>웹에는 iOS나 안드로이드와 다른 웹만의 관례가 있습니다.</b> 두 OS의 모양을 다 흉내 내다 보면 어느 쪽에서도 어색해지므로, 웹에서는 <b>웹의 관례</b>를 지키는 편이 낫습니다.",
  s4_title="플랫폼마다 다른 버튼 자리", s4_hint="같은 화면에서 버튼이 놓이는 자리",
  do_title="플랫폼 관례를 다룰 때 지킬 것",
  dont_title="플랫폼 관례에서 피할 것",
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  states=states([
    (box(BAR + '<span style="position:absolute;left:4px;top:4px;font-size:8px;color:var(--accent)">‹ 정산</span>'
         '<span style="position:absolute;left:50%;top:4px;transform:translateX(-50%);font-size:8px;font-weight:700">모란상회</span>',
         "iOS는 ‹와 이전 화면 이름"),
     "뒤로 가는 방법", "안드로이드는 <b>←만</b> 두고, 웹에서는 브라우저가 뒤로가기를 제공합니다"),
    (box(BAR + '<span style="position:absolute;right:4px;top:4px;font-size:8px;color:var(--accent);font-weight:700">저장</span>'
         '<span style="position:absolute;left:4px;top:4px;font-size:8px;color:var(--accent)">취소</span>',
         "iOS는 오른쪽 위 글자 버튼"),
     "주 동작 버튼의 자리", "안드로이드는 <b>오른쪽 아래 FAB</b>에, 웹은 폼 아래에 둡니다"),
    (box('<span style="position:absolute;left:5px;top:22px;font-size:8px">알림 받기</span>'
         '<span style="position:absolute;right:5px;top:20px;width:22px;height:13px;border-radius:999px;background:var(--accent)">'
         '<span style="position:absolute;right:1px;top:1px;width:11px;height:11px;border-radius:50%;background:#fff"></span></span>',
         "iOS는 누르면 바로 적용"),
     "켜고 끄는 부품", "M3 스위치에는 <b>✓가 붙고</b>, 웹에서는 저장 버튼이 따로 있으면 체크박스를 씁니다"),
    (box('<div style="position:absolute;left:8px;right:8px;top:8px;bottom:8px;background:var(--surface);border:1px solid var(--line);border-radius:5px">'
         '<span style="position:absolute;left:5px;top:4px;font-size:8px;font-weight:700">지울까요?</span>'
         '<div style="position:absolute;left:0;right:0;bottom:0;display:flex;border-top:1px solid var(--line);font-size:7px">'
         '<span style="flex:1;text-align:center;padding:2px 0;border-right:1px solid var(--line);color:var(--accent)">취소</span>'
         '<span style="flex:1;text-align:center;padding:2px 0;color:var(--danger);font-weight:700">삭제</span></div></div>',
         "iOS는 반반으로 나눔"),
     "알림 창의 버튼 차례", "안드로이드는 <b>두 버튼을 모두 오른쪽 아래</b>에 두고, 웹은 확인 버튼을 바깥쪽에 둡니다"),
    (box('<div style="position:absolute;left:0;right:0;bottom:0;height:18px;border-top:1px solid var(--line);background:var(--surface);display:flex;font-size:6px;text-align:center;align-items:center">'
         '<span style="flex:1;color:var(--accent)">정산</span><span style="flex:1;color:var(--fg-muted)">가맹점</span><span style="flex:1;color:var(--fg-muted)">설정</span></div>',
         "iOS는 색으로만 구별"),
     "아래 탭의 모양", "M3는 고른 탭에 <b>알약 모양 바탕</b>을 깔고, 웹은 탭을 <b>위</b>에 둡니다"),
    (box('<span style="position:absolute;left:5px;top:8px;font-size:8px;font-weight:700">웹</span>'
         '<span style="position:absolute;left:5px;top:24px;font-size:7px;color:var(--fg-muted)">브라우저 ← · 폼 아래 버튼</span>'
         '<span style="position:absolute;left:5px;top:36px;font-size:7px;color:var(--fg-muted)">위쪽 탭 · 확인이 바깥쪽</span>',
         "웹은 웹 관례를 따름"),
     "웹에서 따를 관례", "세 플랫폼을 흉내 내기보다 <b>한 가지로 통일</b>합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("뒤로 버튼", "‹ 이름 / ← / 브라우저", "iOS만 뒤로 버튼에 <b>이전 화면 이름</b>을 함께 적습니다"),
    ("주 동작", "오른쪽 위 / FAB / 폼 아래", "안드로이드만 화면 위에 <b>떠 있는 동그란 버튼</b>을 씁니다"),
    ("확인·취소", "반반 / 오른쪽 / 오른쪽", "iOS만 확인과 취소를 <b>반씩 나눠</b> 놓습니다"),
    ("고른 탭 표시", "색 / 알약 / 위쪽", "M3는 고른 탭을 <b>색만으로 구분하지 않고</b> 바탕까지 깝니다"),
    ("웹의 자리", "웹 관례", "두 OS를 흉내 내기보다 <b>웹 관례</b>를 따릅니다"),
    ("관례를 섞은 경우", "양쪽 모두 어색함", "아이폰 앱의 FAB와 안드로이드 앱의 ‹는 <b>둘 다 그 OS의 관례에 맞지 않는</b> 모양입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          실무에서는 <b>'하나로 통일한다'</b>는 결론이 자주 나옵니다.
          OS마다 확인·취소 차례를 바꾸면 코드가 둘로 갈리고 시험할 화면이 두 배가 되지만,
          그 대가로 얻는 것은 사용자가 <b>조금 더 익숙하게 느끼는 정도</b>입니다.
          다만 <b>뒤로가기</b>는 예외입니다. 뒤로가기는 취향의 문제가 아니라
          <a href="systemback.html">OS가 처리하는 동작</a>이기 때문에, 따르지 않으면
          뒤로가기를 눌렀을 때 앱이 꺼지는 식으로 문제가 바로 드러납니다.</p>''',
  do=ul([
    "<b>뒤로가기</b>를 다룰 때. 고를 수 있는 문제가 아니므로 OS를 따릅니다",
    "세 플랫폼에 모두 올리는 앱을 만들 때. <b>한 가지로 통일</b>하고 그 결정을 문서로 적어 둡니다",
    "OS가 제공하는 부품을 쓸 때. 부품을 <b>그 OS의 자리</b>에 둡니다",
  ]),
  dont=ul([
    "iOS 화면에 <b>FAB</b>를 둘 때. iOS에는 화면 오른쪽 아래에 버튼을 띄우는 관례가 없습니다",
    "안드로이드 화면에 <b>‹ 이전 화면 이름</b>을 적을 때. 안드로이드에서는 ←만 씁니다",
    "웹에서 <b>PC 폭일 때도</b> 아래 탭을 둘 때. 웹에서는 탭을 아래에 두는 관례가 없습니다",
    "OS마다 <b>확인·취소 차례를 바꿀</b> 때. 들이는 비용에 비해 얻는 것이 적습니다",
  ]),
  instead='웹에서 부품을 놓는 자리는 <a href="../items/appbar.html">앱바</a>·<a href="../items/tabs.html">탭</a>·<a href="../items/dialog.html">다이얼로그</a> 항목에 정리해 두었고, 뒤로가기는 <a href="systemback.html">시스템 백</a> 항목에서 다룹니다.',
  cases=cases([
    (box(BAR + '<span style="position:absolute;right:4px;top:4px;font-size:8px;color:var(--accent);font-weight:700">저장</span>', "iOS는 오른쪽 위"),
     "저장 버튼의 자리", "같은 저장 버튼이 플랫폼마다 <b>세 군데 다른 자리</b>에 놓입니다"),
    (box('<div style="position:absolute;right:6px;bottom:6px;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:11px">+</div>', "안드로이드는 FAB"),
     "새로 만들기 버튼의 자리", "한 손으로 폰을 쥐었을 때 <b>엄지가 닿는 자리</b>에 둔 버튼입니다"),
    (box('<div style="position:absolute;left:5px;bottom:6px;display:flex;gap:4px">'
         '<span style="font-size:7px;padding:2px 6px;border-radius:4px;background:var(--accent);color:#fff">저장</span>'
         '<span style="font-size:7px;padding:2px 6px;border-radius:4px;border:1px solid var(--line)">취소</span></div>', "웹은 폼 아래 왼쪽"),
     "웹 폼의 버튼 자리", "주 동작 버튼을 먼저 두고, 취소는 <b>눈에 덜 띄게</b> 그 옆에 둡니다"),
  ]),
  s8_title="OS를 따를 것과 팀이 정할 것", s8_hint="팀 문서에 적어 둘 목록",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="OS를 반드시 따라야 하는 것과 <b>팀이 정하면 되는 것</b>을 나눠 적어 둡니다.",
  code='''<span class="c">// 반드시 OS를 따른다. 따르지 않으면 바로 문제가 생긴다</span>
- 뒤로가기 (시스템 백 · 가장자리 제스처)
- 세이프 에어리어 · 노치 · 홈 인디케이터
- 글자 크기 설정 · 모션 줄이기 · 다크 모드

<span class="c">// 팀이 정하면 되는 것. 하나로 통일하는 편이 비용이 적게 든다</span>
- 확인 · 취소의 차례
- 주 동작의 자리
- 스위치냐 체크박스냐
- 탭을 위에 둘지 아래에 둘지

<span class="c">/* 웹에서 폰 폭일 때만 아래 탭을 쓰고 싶다면 */</span>
@media (max-width: 560px) {
  .tabs { <span class="a">position</span>: fixed; <span class="a">bottom</span>: <span class="a">0</span>; <span class="a">padding-bottom</span>: <span class="a">env</span>(safe-area-inset-bottom); }
}''',
  keys=kbd([
    ("OS 부품에 들어 있는 접근성 대응", "시스템이 제공하는 스위치나 날짜 선택기에는 스크린 리더 대응이 <b>이미 들어 있습니다</b>"),
    ("직접 만든 부품의 접근성 챙기기", "모양만 흉내 내고 <code>role</code>과 키보드 조작을 빼면 <b>보기에만 같고 스크린 리더나 키보드로는 쓸 수 없는</b> 부품이 됩니다"),
    ("OS 글자 크기 설정 따르기", "두 OS 모두 사용자가 글자 크기를 키울 수 있습니다. 글자 크기를 <b>px로 고정하면</b> 설정을 바꿔도 커지지 않습니다"),
    ("<a href=\"reducedmotion.html\">모션 줄이기</a>·다크 모드 설정 따르기", "사용자가 OS에서 고른 설정이므로 어느 플랫폼에서든 따라야 합니다"),
    ("<a href=\"../items/safearea.html\">세이프 에어리어</a> 비워 두기", "노치와 홈 인디케이터가 차지하는 자리는 <b>팀이 정할 수 있는 것이 아니므로</b> 반드시 비워 둡니다"),
    ("<a href=\"systemback.html\">뒤로가기</a>를 먼저 확인하기", "따르지 않으면 <b>뒤로가기 한 번에 앱이 꺼집니다.</b> 가장 먼저 확인해야 합니다"),
  ]),
  backend=rows([
    ("OS별 화면 흐름과 API", "OS마다 화면 흐름을 다르게 만들면 API의 <b>단계와 응답</b>도 OS별로 갈립니다. 흐름을 통일하면 서버 쪽도 한 벌로 끝납니다."),
    ("OS별 사용량 통계 읽기", "같은 기능이 한쪽 OS에서만 거의 쓰이지 않는다면, 그 OS에서 버튼이 <b>다른 자리에 있어서</b>일 수 있습니다."),
    ("OS마다 다른 푸시 알림", "두 OS의 푸시 알림 체계가 완전히 달라서 <b>서버 쪽 작업을 두 번</b> 해야 합니다. 그래서 일정을 따로 잡습니다."),
  ]),
  plat_lede="이 항목은 그 자체가 세 플랫폼을 비교하는 내용이라서, 차이를 아래에 나란히 적어 둡니다.",
  plats=plats([
    ("웹", "관례",
     box('<span style="position:absolute;left:4px;top:4px;font-size:7px">← → ⟳</span>'
         '<span style="position:absolute;left:4px;top:22px;font-size:7px;color:var(--fg-muted)">위쪽 탭 · 폼 아래 버튼</span>', "브라우저가 뒤로가기를 제공", "105px"),
     "표준으로 정해진 부품이 적고 관례가 허용하는 폭이 넓습니다. 그래서 <b>팀이 직접 정해 문서로 적어 두는</b> 일이 중요합니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 관례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px;color:var(--accent)">‹ 정산</span>
                <span style="position:absolute;right:4px;top:14px;font-size:6px;color:var(--accent)">저장</span>
                <div style="position:absolute;left:0;right:0;bottom:0;height:12px;border-top:1px solid var(--line);display:flex;font-size:5px;text-align:center;align-items:center"><span style="flex:1;color:var(--accent)">정산</span><span style="flex:1;color:var(--fg-muted)">설정</span></div></div></div>''',
     "<b>글자 버튼</b>을 많이 쓰고, 글자 색으로 누를 수 있다는 것을 알립니다. 동작 버튼은 화면 위쪽 왼편과 오른편에 둡니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 관례 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <span style="position:absolute;left:4px;top:14px;font-size:6px">← 모란상회</span>
                <div style="position:absolute;right:4px;bottom:16px;width:14px;height:14px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:8px">+</div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:12px;border-top:1px solid var(--line);display:flex;font-size:5px;text-align:center;align-items:center"><span style="flex:1"><span style="background:var(--accent);color:#fff;border-radius:999px;padding:0 4px">정산</span></span><span style="flex:1;color:var(--fg-muted)">설정</span></div></div></div>''',
     "<b>면과 바탕색</b>으로 상태를 알리고, 주 동작은 화면 아래쪽 FAB에 둡니다."),
  ]),
  plat_note="\"아이폰처럼 만들어 주세요\"와 \"안드로이드도 되게\"가 한 요청에 같이 들어오면, 버튼을 어느 OS의 자리에 둘지 <b>정해야 할 일이 생깁니다</b>. 이때 비용이 가장 적게 드는 답은 \"뒤로가기와 세이프 에어리어는 OS를 따르고, 나머지는 한 가지로 통일합니다\"입니다. 따르지 않았을 때 실제로 문제가 생기는 것은 앞의 두 가지뿐이고, 나머지는 통일해도 사용자가 불편을 거의 느끼지 않기 때문입니다.",
  siblings=siblings("platformdiff"),
  related='''        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>
        <li><a href="../items/bottomnav.html"><b>바텀 탭바</b><em>7부</em></a></li>
        <li><a href="../items/switch.html"><b>스위치</b><em>4부</em></a></li>''',
)
