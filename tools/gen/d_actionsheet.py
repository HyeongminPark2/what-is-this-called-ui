# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양만 보고는 구별하기 어렵지만, 아래 네 가지를 따져 보면 어느 부품인지 가려낼 수 있습니다."

def sheet(items, label, note="", ok=None, w="152px", sep=True, cancel=True):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    btns = ''.join('<span style="display:block;border-top:1px solid var(--line);padding:3px 6px;'
                   'font-size:7.5px;text-align:center;color:' + ('var(--danger)' if d else 'var(--accent)') + '">'
                   + t + '</span>' for t, d in items)
    body = ('<span style="display:block;border-radius:5px;background:var(--surface);overflow:hidden">'
            + btns + ('' if sep or not cancel else
                      '<span style="display:block;border-top:1px solid var(--line);padding:3px 6px;'
                      'font-size:7.5px;text-align:center;color:var(--accent)">취소</span>') + '</span>')
    if sep and cancel:
        body += ('<span style="display:block;margin-top:4px;border-radius:5px;background:var(--surface);'
                 'padding:3px 6px;font-size:7.5px;text-align:center;font-weight:700;color:var(--accent)">취소</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:104px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden">'
            '<span style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 40%, transparent)"></span>'
            '<span style="position:absolute;left:5px;right:5px;bottom:5px">' + body + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">가림막 — 뒤를 막는다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">아래에서 올라온다 — 손가락이 닿는 자리</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">무엇에 대한 일인지 — 제목이나 파일 이름</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">위험한 항목은 빨갛게 · 맨 아래에</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">취소는 한 칸 떼어 둔다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">절반을 넘게 덮으면 화면 한 장이 낫다</div>
                </div>
              </div>'''

D = dict(
  slug="actionsheet", ko="액션 시트", en="Action sheet",
  desc="지금 고른 것에 할 수 있는 일을 화면 아래에서 올려 보여 주는 겹침 부품입니다. 위험한 항목과 취소 버튼을 어디에 두는지 다룹니다.",
  lede="액션 시트는 <b>지금 고른 것</b>에 할 수 있는 일을 화면 아래에서 올려 보여 줍니다. 화면 아래쪽은 폰을 쥔 손가락이 쉽게 닿는 자리라서 폰에서 특히 잘 맞습니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>항목 수를 늘려 보세요. 데모가 <b>시트가 화면의 몇 %를 덮는지</b> 재서 적어 줍니다.
          시트가 화면의 절반을 넘게 덮으면 시트보다 <b>화면 한 장</b>으로 만드는 편이 낫습니다.<br>
          <b>위험한 항목</b>은 빨간 글자로 <b>목록 맨 아래</b>에 둡니다. 시트를 연 손가락이 처음 닿는 자리에 위험한 항목이 오지 않게 하려는 것입니다.
          <b>취소</b>는 목록과 한 칸 떼어 둬야 실수로 누르지 않습니다. 체크를 끄면 취소가 목록에 붙은 모습을 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "액션 시트, 동작 시트, 아래 메뉴"),
    ("영어", "action sheet, bottom action sheet"),
    ("같이 쓰는 말",
     "액션 시트는 iOS의 <code>UIAlertController(.actionSheet)</code>에서 온 이름입니다. "
     "Material에서는 <b>모달 바텀시트</b> 안에 목록을 넣는 방식으로 같은 것을 만듭니다. "
     "iOS 지침은 항목의 역할 이름도 정해 두었는데, 위험한 항목은 <b>destructive</b>, "
     "취소는 <b>cancel</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>바텀시트</b> — <a href=\"sheet.html\">바텀시트</a>에는 <b>어떤 내용</b>이든 담을 수 있지만, 액션 시트에는 <b>동작 목록</b>만 담습니다.<br>"
     "<b>드롭다운 메뉴</b> — <a href=\"menu.html\">드롭다운 메뉴</a>는 화면 아래가 아니라 <b>누른 단추 옆에</b> 붙어 뜹니다.<br>"
     "<b>다이얼로그</b> — <a href=\"dialog.html\">다이얼로그</a>는 할 일을 늘어놓는 대신 사용자에게 <b>묻고 답을 받습니다</b>."),
  ]),
  axes=axis_table("액션 시트"),
  oneline="액션 시트에는 <b>동작을 셋에서 다섯 개 두는 것이 알맞습니다.</b> 그보다 많으면 시트가 화면을 너무 많이 덮기 때문에 화면 한 장으로 만듭니다.",
  states=states([
    (sheet([("영수증 다시 보내기", False), ("이름 바꾸기", False), ("지우기", True)], "", "셋 — 알맞다", True),
     "알맞은 수", "<b>셋에서 다섯</b>"),
    (sheet([("열기", False), ("이름 바꾸기", False), ("복사", False), ("보관", False),
            ("공유", False), ("지우기", True)], "", "절반을 넘게 덮는다", False),
     "너무 많음", "<b>화면 한 장</b>으로 만드는 편이 낫습니다"),
    (sheet([("영수증 다시 보내기", False), ("지우기", True)], "", "위험한 것이 맨 아래", True),
     "위험한 항목", "<b>빨갛게 · 맨 아래</b>"),
    (sheet([("영수증 다시 보내기", False), ("지우기", True)], "", "취소가 목록에 붙었다", False, "152px", False),
     "취소가 붙음", "취소를 <b>실수로 누르기 쉽습니다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">정말 지울까요?</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">취소 · 지우기</span>'),
         "되묻기", None, "되돌릴 수 없으면 한 번 더", "152px"),
     "되돌릴 수 없는 일", "<b>한 번 더</b> 묻습니다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">가림막을 눌렀다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">아무 일도 안 일어난다</span>'),
         "닫기", True, "가림막·Esc·취소 — 셋 다 닫는다", "152px"),
     "닫기", "가림막, Esc, 취소 세 가지로 <b>닫을 수 있습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("가림막", "뒤를 막음", "시트 뒤의 화면은 <b>누를 수 없습니다</b>"),
    ("아래에서", "손 가까이", "폰을 쥔 손의 <b>엄지</b>가 닿는 자리입니다"),
    ("제목", "무엇에 대한 일", "파일 이름이나 한 줄 설명을 적습니다"),
    ("위험한 항목", "빨갛게·맨 아래", "손가락이 <b>먼저 닿지 않는</b> 자리에 둡니다"),
    ("취소", "떼어 둠", "목록과 한 칸 띄워 둡니다"),
    ("크기", "절반까지", "화면 절반을 넘으면 <b>화면 한 장</b>으로 만듭니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          위험한 항목을 <b>맨 아래</b>에 두는 것은 iOS 지침이 정해 둔 규칙입니다.
          아래에서 올라오는 시트에서는 <b>엄지가 가장 먼저 닿는 곳이 맨 아래</b>이기 때문에,
          그보다 더 아래에 취소를 한 칸 떼어 두어
          엄지가 <b>잘못 눌러도 아무 일이 일어나지 않게</b> 합니다.<br>
          안드로이드에는 액션 시트라는 이름이 없고,
          <b>모달 바텀시트</b> 안에 목록을 넣어 같은 역할을 하게 합니다.
          안드로이드 쪽에는 위험한 항목을 맨 아래에 두는 규칙이 없어서,
          두 플랫폼을 함께 만들 때는 항목 <b>차례가 서로 달라질 수 있습니다</b>.</p>''',
  do=ul([
    "동작이 <b>셋에서 다섯</b> 개일 때",
    "위험한 항목을 <b>빨갛게, 맨 아래</b>에 둘 때",
    "취소를 목록과 <b>한 칸 떼어</b> 둘 때",
  ]),
  dont=ul([
    "동작을 <b>여덟 개</b>씩 넣을 때. 그만큼 많으면 화면 한 장으로 만듭니다",
    "위험한 항목을 <b>맨 위</b>에 둘 때",
    "취소를 <b>목록에 붙여</b> 둘 때",
    "넓은 화면에서도 아래에서 올릴 때. PC에서는 <a href=\"menu.html\">메뉴</a>가 맞습니다",
  ]),
  instead='동작 목록이 아닌 다른 내용을 담으려면 <a href="sheet.html">바텀시트</a>, 단추 옆에 붙여 띄우려면 <a href="menu.html">드롭다운 메뉴</a>, 묻고 답을 받으려면 <a href="dialog.html">다이얼로그</a>, 누른 자리에 띄우려면 <a href="contextmenu.html">컨텍스트 메뉴</a>를 씁니다.',
  cases=cases([
    (sheet([("영수증 보내기", False), ("이름 바꾸기", False), ("지우기", True)], "", "", True),
     "파일 하나", "액션 시트를 <b>가장 흔하게</b> 쓰는 자리입니다"),
    (sheet([("사진 찍기", False), ("앨범에서 고르기", False)], "", "", True),
     "사진 올리기", "고를 수 있는 방법이 둘뿐일 때도 씁니다"),
    (sheet([("카드로", False), ("계좌이체로", False), ("간편결제로", False)], "", "", True),
     "결제 수단", "동작뿐 아니라 <b>값을 고를 때</b>도 씁니다"),
  ]),
  code_lede="구조는 바텀시트와 같고, 안에 동작 목록이 들어간다는 점만 다릅니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"scrim"</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"action-sheet"</span> <span class="a">role</span>=<span class="s">"dialog"</span> <span class="a">aria-modal</span>=<span class="s">"true"</span>
     <span class="a">aria-label</span>=<span class="s">"영수증_2411_01.jpg 에 할 수 있는 일"</span>&gt;
  &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"group"</span>&gt;
    &lt;<span class="t">button</span>&gt;영수증 다시 보내기&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">button</span>&gt;이름 바꾸기&lt;/<span class="t">button</span>&gt;
    &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"danger"</span>&gt;지우기&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">div</span>&gt;
  &lt;<span class="t">button</span> <span class="a">class</span>=<span class="s">"cancel"</span>&gt;취소&lt;/<span class="t">button</span>&gt;
&lt;/<span class="t">div</span>&gt;

.action-sheet { <span class="a">position</span>: fixed; <span class="a">left</span>: <span class="a">8px</span>; <span class="a">right</span>: <span class="a">8px</span>;
  <span class="a">bottom</span>: <span class="a">calc</span>(<span class="a">8px</span> + <span class="a">env</span>(safe-area-inset-bottom)); }''',
  keys=kbd([
    ("Esc", "시트를 닫습니다. 취소를 누른 것과 <b>같습니다</b>"),
    ("Tab", "포커스가 시트 안에서만 돌고 <b>뒤 화면으로 나가지 않습니다</b>"),
    ("<code>aria-modal=\"true\"</code>", "시트 뒤의 화면은 <b>읽지 않는다</b>고 스크린 리더에 알립니다"),
    ("<code>aria-label</code>", "<b>무엇에 대한</b> 시트인지 적습니다"),
    ("초점", "열면 <b>첫 항목</b>으로, 닫으면 시트를 <b>부른 자리</b>로 옮깁니다"),
    ("세이프 에어리어", "맨 아래 취소 버튼이 <b>홈 바에 가리지 않게</b> 띄웁니다"),
  ]),
  backend=rows([
    ("할 수 있는 일이 다르다", "줄마다 권한이 다르면 <code>can_delete</code> 같은 값을 보고 할 수 없는 <b>항목은 목록에서 뺍니다</b>. 흐리게 남겨 두지 않습니다."),
    ("되돌릴 수 있나", "지운 것을 <a href=\"undo.html\">되돌리기</a>로 무를 수 있는지에 따라 <b>한 번 더 물을지</b>가 정해집니다."),
  ]),
  plat_lede="액션 시트는 <b>iOS에서 온 부품</b>이라서 iOS 지침의 규칙이 가장 자세합니다.",
  plats=plats([
    ("웹", "직접 만듦",
     sheet([("보내기", False), ("지우기", True)], "", "", True, "110px"),
     "시트 구조에 목록을 넣어 직접 만듭니다. 이때 <b>세이프 에어리어</b>를 빠뜨리기 쉽습니다."),
    ("iOS", "actionSheet",
     '''              <div class="phone" role="img" aria-label="iOS 액션 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 35%, transparent)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:12px;height:20px;border-radius:4px;background:var(--surface)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:3px;height:7px;border-radius:3px;background:var(--surface)"></div></div></div>''',
     "정식 부품이고, <b>destructive</b>와 <b>cancel</b> 역할이 지침에 정해져 있습니다."),
    ("안드로이드", "모달 바텀시트",
     '''              <div class="phone" role="img" aria-label="안드로이드 모달 바텀시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 35%, transparent)"></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:30px;border-radius:6px 6px 0 0;background:var(--surface)"></div>
                <div style="position:absolute;left:50%;transform:translateX(-50%);bottom:26px;width:12px;height:2px;border-radius:2px;background:var(--line)"></div></div></div>''',
     "액션 시트라는 이름이 없어서 <b>바텀시트</b>에 목록을 넣고, 시트를 <b>화면 끝까지</b> 붙입니다."),
  ]),
  plat_note="두 플랫폼은 <b>생김새가 다릅니다</b>. iOS는 화면 가장자리에서 띄운 둥근 카드 두 장(목록과 취소)으로 보여 주고, 안드로이드는 화면 끝까지 붙인 시트 한 장에 손잡이를 답니다. 웹에서는 둘 다 흉내 낼 필요 없이 <b>한 가지를 골라 일관되게</b> 쓰는 편이 낫습니다. 다만 <b>취소를 떼어 두는 것</b>과 <b>위험한 항목을 아래에 두는 것</b>은 어느 쪽을 고르든 지키는 것이 좋습니다.",
  siblings=siblings("actionsheet"),
  related='''        <li><a href="sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
