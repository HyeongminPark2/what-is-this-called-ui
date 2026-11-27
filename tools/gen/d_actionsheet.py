# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

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
  desc="지금 고른 것에 할 수 있는 일을 아래에서 올려 보여 주는 겹침. 위험한 항목과 취소의 자리.",
  lede="<b>지금 고른 것</b>에 할 수 있는 일을 아래에서 올려 줍니다. 손가락이 닿는 자리라 폰에서 특히 잘 맞습니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>항목을 늘려 보세요 — 데모가 <b>시트가 화면의 몇 %를 덮는지</b>를 재서 적습니다.
          절반을 넘어가면 시트가 아니라 <b>화면 한 장</b>으로 만드는 편이 낫습니다.<br>
          <b>위험한 항목</b>은 빨갛게 두고 <b>맨 아래</b>에 둡니다 — 손가락이 먼저 닿는 자리를 피하는 것입니다.
          <b>취소</b>는 한 칸 떼어 둬야 실수로 안 눌립니다. 체크를 끄면 취소가 목록에 붙어 버립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "액션 시트, 동작 시트, 아래 메뉴"),
    ("영어", "action sheet, bottom action sheet"),
    ("같이 쓰는 말",
     "iOS 의 <code>UIAlertController(.actionSheet)</code> 에서 온 이름입니다. "
     "Material 쪽에서는 <b>모달 바텀시트</b> 안에 목록을 넣은 꼴로 만듭니다. "
     "위험한 항목을 가리키는 <b>destructive</b>, 취소를 가리키는 <b>cancel</b> 이 "
     "지침에 정해진 역할 이름입니다."),
    ("자주 잘못 부름",
     "<b>바텀시트</b> — <a href=\"sheet.html\">바텀시트</a>는 <b>아무 내용</b>이나 담는 그릇입니다. 액션 시트는 <b>동작 목록</b>만 담습니다.<br>"
     "<b>드롭다운 메뉴</b> — <a href=\"menu.html\">드롭다운 메뉴</a>는 <b>누른 단추 옆에</b> 붙어 뜹니다.<br>"
     "<b>다이얼로그</b> — <a href=\"dialog.html\">다이얼로그</a>는 <b>묻고 답을 받습니다</b>."),
  ]),
  axes=axis_table("액션 시트"),
  oneline="<b>동작 셋에서 다섯이 알맞습니다.</b> 그보다 많으면 시트가 아니라 화면입니다.",
  states=states([
    (sheet([("영수증 다시 보내기", False), ("이름 바꾸기", False), ("지우기", True)], "", "셋 — 알맞다", True),
     "알맞은 수", "<b>셋에서 다섯</b>"),
    (sheet([("열기", False), ("이름 바꾸기", False), ("복사", False), ("보관", False),
            ("공유", False), ("지우기", True)], "", "절반을 넘게 덮는다", False),
     "너무 많음", "<b>화면 한 장</b>이 낫다"),
    (sheet([("영수증 다시 보내기", False), ("지우기", True)], "", "위험한 것이 맨 아래", True),
     "위험한 항목", "<b>빨갛게 · 맨 아래</b>"),
    (sheet([("영수증 다시 보내기", False), ("지우기", True)], "", "취소가 목록에 붙었다", False, "152px", False),
     "취소가 붙음", "<b>실수로 눌린다</b>"),
    (one(txt('<span style="display:block;font-size:8.5px">정말 지울까요?</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">취소 · 지우기</span>'),
         "되묻기", None, "되돌릴 수 없으면 한 번 더", "152px"),
     "되돌릴 수 없는 일", "<b>한 번 더</b> 묻는다"),
    (one(txt('<span style="display:block;font-size:8.5px;color:var(--fg-muted)">가림막을 눌렀다</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:2px">아무 일도 안 일어난다</span>'),
         "닫기", True, "가림막·Esc·취소 — 셋 다 닫는다", "152px"),
     "닫기", "<b>빠져나갈 길</b>이 셋"),
  ]),
  anat=ANAT,
  pins=pins([
    ("가림막", "뒤를 막음", "뒤가 <b>안 눌린다</b>"),
    ("아래에서", "손 가까이", "폰에서 <b>엄지</b>가 닿는다"),
    ("제목", "무엇에 대한 일", "파일 이름이나 한 줄"),
    ("위험한 항목", "빨갛게·맨 아래", "손가락이 <b>먼저 닿지 않게</b>"),
    ("취소", "떼어 둠", "한 칸 띄운다"),
    ("크기", "절반까지", "넘으면 <b>화면 한 장</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          위험한 항목을 <b>맨 아래</b>에 두는 것은 iOS 지침이 정해 둔 규칙인데,
          이유가 분명합니다 — 아래에서 올라오는 시트에서
          <b>엄지가 가장 먼저 닿는 곳이 맨 아래</b>이기 때문입니다.
          그래서 취소를 더 아래, 한 칸 떼어 두어
          <b>잘못 눌러도 아무 일이 안 일어나게</b> 합니다.<br>
          안드로이드에는 액션 시트라는 이름이 없고
          <b>모달 바텀시트</b> 안에 목록을 넣습니다 —
          그쪽에서는 위험한 항목을 맨 아래에 두는 규칙도 없어서,
          두 플랫폼을 같이 만들 때 <b>차례가 달라지는</b> 자리입니다.</p>''',
  do=ul([
    "동작을 <b>셋에서 다섯</b>으로 두기",
    "위험한 항목은 <b>빨갛게, 맨 아래</b>",
    "취소를 <b>한 칸 떼어</b> 두기",
  ]),
  dont=ul([
    "동작을 <b>여덟 개</b>씩 넣기 — 화면 한 장으로 만든다",
    "위험한 항목을 <b>맨 위</b>에 두기",
    "취소를 <b>목록에 붙이기</b>",
    "넓은 화면에서도 아래에서 올리기 — PC 에서는 <a href=\"menu.html\">메뉴</a>가 맞다",
  ]),
  instead='아무 내용이나 담으면 <a href="sheet.html">바텀시트</a>, 단추 옆에 붙으면 <a href="menu.html">드롭다운 메뉴</a>, 묻고 답을 받으면 <a href="dialog.html">다이얼로그</a>, 누른 자리에 뜨면 <a href="contextmenu.html">컨텍스트 메뉴</a>.',
  cases=cases([
    (sheet([("영수증 보내기", False), ("이름 바꾸기", False), ("지우기", True)], "", "", True),
     "파일 하나", "<b>가장 흔한</b> 자리"),
    (sheet([("사진 찍기", False), ("앨범에서 고르기", False)], "", "", True),
     "사진 올리기", "길이 둘뿐일 때"),
    (sheet([("카드로", False), ("계좌이체로", False), ("간편결제로", False)], "", "", True),
     "결제 수단", "<b>값 고르기</b>에도 쓴다"),
  ]),
  code_lede="바텀시트와 같은 뼈대입니다 — 목록이 들어갈 뿐입니다.",
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
    ("Esc", "닫는다. 취소를 누른 것과 <b>같다</b>"),
    ("Tab", "시트 안에 <b>갇힌다</b> — 뒤로 안 나간다"),
    ("<code>aria-modal=\"true\"</code>", "뒤가 <b>안 읽힌다</b>고 알린다"),
    ("<code>aria-label</code>", "<b>무엇에 대한</b> 시트인지 적는다"),
    ("초점", "열면 <b>첫 항목</b>, 닫으면 <b>부른 자리</b>로"),
    ("세이프 에어리어", "맨 아래 취소가 <b>홈 바에 가리지 않게</b>"),
  ]),
  backend=rows([
    ("할 수 있는 일이 다르다", "줄마다 권한이 다르면 <code>can_delete</code> 같은 값으로 <b>항목을 지웁니다</b> — 흐리게 두지 않습니다."),
    ("되돌릴 수 있나", "지우기가 <a href=\"undo.html\">되돌리기</a>로 무를 수 있는지에 따라 <b>되묻기를 붙일지</b>가 갈립니다."),
  ]),
  plat_lede="<b>iOS 에서 온 부품</b>이라 그쪽 규칙이 가장 또렷합니다.",
  plats=plats([
    ("웹", "직접 만듦",
     sheet([("보내기", False), ("지우기", True)], "", "", True, "110px"),
     "시트 뼈대에 목록을 넣어 만듭니다. <b>세이프 에어리어</b>를 빠뜨리기 쉽습니다."),
    ("iOS", "actionSheet",
     '''              <div class="phone" role="img" aria-label="iOS 액션 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 35%, transparent)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:12px;height:20px;border-radius:4px;background:var(--surface)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:3px;height:7px;border-radius:3px;background:var(--surface)"></div></div></div>''',
     "정식 부품입니다. <b>destructive</b> 와 <b>cancel</b> 역할이 지침에 정해져 있습니다."),
    ("안드로이드", "모달 바텀시트",
     '''              <div class="phone" role="img" aria-label="안드로이드 모달 바텀시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 35%, transparent)"></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:30px;border-radius:6px 6px 0 0;background:var(--surface)"></div>
                <div style="position:absolute;left:50%;transform:translateX(-50%);bottom:26px;width:12px;height:2px;border-radius:2px;background:var(--line)"></div></div></div>''',
     "액션 시트라는 이름이 없습니다. <b>바텀시트</b>에 목록을 넣고 <b>화면 끝까지</b> 붙입니다."),
  ]),
  plat_note="<b>생김새가 다릅니다</b> — iOS 는 가장자리를 띄워 둥근 카드 둘(목록 + 취소)로 두고, 안드로이드는 화면 끝까지 붙인 시트 하나에 손잡이를 답니다. 웹에서 둘 다 흉내 낼 필요는 없고, <b>한 가지를 골라 일관되게</b> 쓰는 편이 낫습니다. 다만 <b>취소를 떼어 두는 것</b>과 <b>위험한 항목을 아래에 두는 것</b>은 어느 쪽을 고르든 지킬 만합니다.",
  siblings=siblings("actionsheet"),
  related='''        <li><a href="sheet.html"><b>바텀시트</b><em>6부</em></a></li>
        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
