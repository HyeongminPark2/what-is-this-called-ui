# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:6px 10px 10px">
                <div data-pin="1" style="display:inline-block;border:1px solid var(--line-strong);border-radius:6px;padding:7px 13px;font-size:11.5px;font-weight:700;background:var(--surface)">필터 ▾</div>
                <div class="pin-tr" data-pin="2" style="height:12px;width:62px"></div>
                <div style="position:relative;width:200px">
                  <span class="pin-tr" data-pin="3" style="position:absolute;left:16px;top:-5px;width:9px;height:9px;transform:rotate(45deg);background:var(--surface);border-left:1px solid var(--line);border-top:1px solid var(--line);z-index:2"></span>
                  <div data-pin="4" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;box-shadow:var(--e3);padding:26px 26px 11px">
                    <div class="pin-out" data-pin="5" style="font-size:10px;font-weight:800;letter-spacing:.05em;color:var(--fg-muted);margin-bottom:7px">상태</div>
                    <div class="pin-out" data-pin="6" style="font-size:11.5px;line-height:1.9">☑ 승인<br>☐ 실패<br>☐ 대기</div>
                    <div class="pin-out" data-pin="7" style="border-top:1px solid var(--line);margin-top:9px;padding-top:9px;text-align:right">
                      <span style="background:var(--accent);color:#fff;border-radius:5px;padding:4px 11px;font-size:10.5px;font-weight:700">적용</span>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="popover", ko="팝오버", en="Popover · Flyout",
  desc="팝오버가 무엇인지, 툴팁이나 드롭다운 메뉴, 모달과는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="팝오버는 사용자가 누른 요소 <b>옆에 붙어서</b> 뜨는 작은 판입니다. 뒤쪽 화면을 막지 않으며, 툴팁과 달리 <b>안에 누를 수 있는 것이 들어 있습니다</b>.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>팝오버를 열어 둔 채로 아래 목록을 읽어 보세요.</b> 팝오버는 뒤쪽 화면을 막지 않습니다.
          오른쪽 끝의 '내 계정'은 그대로 열면 화면 밖으로 나가기 때문에 <b>반대쪽으로 뒤집혀</b> 열립니다.
          이 동작을 <b>플립</b>이라고 부르는데, 팝오버를 직접 만들 때 가장 자주 빠뜨리는 부분입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "팝오버, 팝업 메뉴, 플라이아웃"),
    ("영어", "popover, flyout"),
    ("같이 쓰는 말", "안에 든 것이 <b>메뉴 항목뿐</b>이면 <b>드롭다운 메뉴</b>라고 따로 부르고, 폼이나 설정이 들어가면 팝오버라고 부릅니다. 팝오버가 붙는 기준 요소는 <b>앵커</b>(anchor)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>툴팁</b> — 설명만 담으면 툴팁이고, 누를 것이 들어 있으면 툴팁이 아니라 팝오버입니다. 팝오버를 두고 가장 흔히 헷갈리는 이름입니다.<br>"
     "<b>모달</b> — 모달은 뒤쪽 화면을 막지만 팝오버는 막지 않습니다.<br>"
     "<b>팝업</b> — 브라우저가 새로 띄우는 팝업 창과 이름이 겹쳐서 헷갈립니다."),
  ]),
  states=states([
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>', bars="684", label="팝오버가 닫힌 모습"), "닫혀 있을 때", "앵커만 보이고, 앵커의 <code>aria-expanded</code> 값은 <code>\"false\"</code>입니다"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger" style="border-color:var(--accent);color:var(--accent)">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태"), bars="684", label="팝오버가 열린 모습"), "열렸을 때", "앵커 바로 아래에 뜨고, 앵커도 눌린 상태로 보입니다"),
    (mini('<div style="margin-top:8px;text-align:right"><span class="mini__trigger">계정 ▾</span></div>' + pop(["로그아웃"], pos="right:8px;top:32px", tail="right:10px;top:-4px"), bars="684", label="오른쪽 가장자리에서 뒤집힌 팝오버"), "반대쪽으로 뒤집혔을 때", "화면 밖으로 나갈 것 같으면 반대쪽으로 뒤집어 엽니다. 이것을 <b>플립</b>이라고 합니다"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:2px;top:32px", tail="left:14px;top:-4px"), bars="684", label="가장자리에서 밀린 팝오버"), "안쪽으로 밀렸을 때", "꼬리는 앵커를 가리킨 채로 두고 판만 화면 안쪽으로 옮깁니다. 이것을 <b>시프트</b>라고 합니다"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태") + '<div style="position:absolute;right:6px;bottom:6px;font-size:8px;color:var(--fg-muted)">바깥을 누름 ↘</div>', bars="684", label="바깥을 눌러 닫히는 팝오버"), "바깥을 눌렀을 때", "스크림이 없어서 바깥을 누를 때 닫는 처리를 <b>직접</b> 만들어야 합니다"),
    (mini('<div style="margin-top:8px;opacity:.3"><span class="mini__trigger">필터 ▾</span></div>', bars="684", label="앵커가 스크롤로 사라진 모습"), "스크롤로 앵커가 사라졌을 때", "스크롤해서 앵커가 화면 밖으로 나가면 팝오버도 함께 닫습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앵커 · 트리거", "anchor · trigger", "팝오버가 붙는 기준 요소입니다. 팝오버가 열려 있는 동안에는 눌린 상태로 보여 줍니다"),
    ("오프셋", "offset", "앵커와 판 사이의 빈 자리로, 보통 8~12px을 둡니다"),
    ("꼬리", "tail · arrow · caret", "팝오버가 어느 앵커에서 나왔는지 가리킵니다. 꼬리를 두지 않는 디자인도 많습니다"),
    ("패널", "panel · surface", "모달보다 화면에서 덜 떠 보이도록 그림자를 약하게 줍니다"),
    ("헤더", "header", "짧게 씁니다. 헤더가 길어질 만큼 내용이 많으면 팝오버에 담기에 너무 많은 것입니다"),
    ("내용", "content", "한눈에 들어오는 분량만 담습니다. 스크롤이 생기면 팝오버가 맞는 부품인지 다시 따져 봅니다"),
    ("액션 영역", "footer", "적용·초기화 버튼을 둡니다. 바꾸는 즉시 반영되도록 설계했다면 액션 영역을 아예 두지 않아도 됩니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않는 요소가 두 가지 더 있습니다. 화면 밖으로 나갈 것 같으면 반대쪽으로 뒤집어 여는 <b>플립</b>과,
          꼬리는 그대로 둔 채 판만 화면 안쪽으로 옮기는 <b>시프트</b>입니다. 둘 다 팝오버를 놓을 자리를 계산하는 규칙이라 그림에 따로 표시할 테두리가 없습니다.</p>''',
  do=ul([
    "추가 설정이나 필터처럼 화면을 떠나지 않고 조건만 바꿀 때",
    "입력 칸 한두 개로 끝나는 빠른 편집을 할 때",
    "사용자 카드나 미리보기처럼 보조 정보를 더 보여 줄 때",
  ]),
  dont=ul([
    "사용자가 꼭 답해야 할 때. 팝오버는 바깥을 누르면 사라지므로 모달을 씁니다",
    "폼이 길거나 단계가 여럿일 때. 페이지나 드로어를 씁니다",
    "모바일에서 손가락으로 누르기 어려울 만큼 작을 때. 바텀시트로 바꿉니다",
    "팝오버 안에서 팝오버를 또 열 때. 어느 팝오버의 바깥을 눌렀는지 가리는 처리가 금방 엉킵니다",
  ]),
  instead='사용자의 답을 꼭 받아야 하면 <a href="modal.html">모달</a>을 쓰고, 누를 것 없이 설명만 보여 주면 되면 <a href="tooltip.html">툴팁</a>으로 충분합니다. 폰에서는 <a href="sheet.html">바텀시트</a>로 바꾸고, 작업이 길면 <a href="drawer.html">드로어</a>에 담습니다.',
  cases=cases([
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패", "☐ 대기"], pos="left:8px;top:32px", head="상태"), bars="684", tall=False, label="필터 팝오버 재현"),
     "목록을 보면서 필터 바꾸기", "목록을 보면서 조건만 바꿉니다. 팝오버를 가장 흔하게 쓰는 자리입니다"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">2026-11-13</span></div>' + '<div class="mini__pop" style="left:8px;top:32px;width:86px"><span class="tail" style="left:10px;top:-4px"></span><b style="font-size:8px;display:block;margin-bottom:3px">11월</b><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:2px;font-size:6.5px;color:var(--fg-muted);text-align:center">' + "".join('<span%s>%d</span>' % (' style="background:var(--accent);color:#fff;border-radius:2px"' if d == 13 else "", d) for d in range(8, 29)) + '</div></div>', bars="684", tall=False, label="날짜 선택 팝오버 재현"),
     "입력 칸에 붙여 날짜 고르기", "입력 칸에 붙어서 뜨고, 안에 누를 수 있는 날짜가 가득합니다"),
    (mini('<div style="margin-top:8px;text-align:right"><span class="mini__trigger">길동</span></div>' + '<div class="mini__pop" style="right:8px;top:32px;width:84px"><span class="tail" style="right:10px;top:-4px"></span><b style="font-size:8.5px;display:block">홍길동</b><i>gildong@example.com</i><i style="color:var(--accent);font-weight:700;margin-top:3px">로그아웃</i></div>', bars="684", tall=False, label="사용자 카드 팝오버 재현"),
     "오른쪽 끝에서 사용자 카드 열기", "앵커가 화면 오른쪽 끝에 있어서 반대쪽으로 뒤집혀 열립니다"),
  ]),
  code_lede="팝오버에는 스크림이 없기 때문에 <b>바깥 클릭과 <kbd>Esc</kbd>를 직접 처리</b>해야 합니다. 모달에서는 <code>&lt;dialog&gt;</code> 요소가 알아서 해 주던 일을 여기서는 코드로 직접 만듭니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>&gt;필터 ▾&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">role</span>=<span class="s">"dialog"</span> <span class="a">aria-label</span>=<span class="s">"필터"</span> <span class="a">hidden</span>&gt;…&lt;/<span class="t">div</span>&gt;

<span class="c">// 바깥을 누르면 닫는다. 스크림이 없으니 직접 처리한다</span>
pop.addEventListener(<span class="s">'click'</span>, e =&gt; e.stopPropagation());
document.addEventListener(<span class="s">'click'</span>, closeAll);

<span class="c">// Esc 로 닫고 포커스를 앵커로 돌려준다</span>
document.addEventListener(<span class="s">'keydown'</span>, e =&gt; <span class="a">{</span>
  <span class="a">if</span> (e.key === <span class="s">'Escape'</span>) <span class="a">{</span> close(); btn.focus(); <span class="a">}</span>
<span class="a">}</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "팝오버가 닫히고 포커스가 앵커로 돌아갑니다"),
    ("<kbd>Tab</kbd>", "포커스가 팝오버 안을 지나 뒤쪽 화면으로 이어집니다. 메뉴 항목만 든 팝오버라면 포커스를 안에 가두고 화살표 키로 옮깁니다"),
    ("바깥을 눌렀을 때", "팝오버가 닫힙니다. 팝오버 안쪽을 누를 때는 이벤트 전파를 멈춰서 닫히지 않게 합니다"),
    ("팝오버가 열릴 때", "포커스가 팝오버의 첫 요소로 옮겨 가고, 앵커의 <code>aria-expanded</code> 값이 <code>true</code>로 바뀝니다"),
    ("화면을 스크롤할 때", "앵커가 화면 밖으로 나가면 팝오버도 함께 닫습니다. 닫지 않으면 팝오버만 가리킬 대상 없이 화면에 남습니다"),
  ]),
  backend=rows([
    ("열 때 내용 가져오기", "팝오버 내용은 팝오버를 열기 전에는 필요하지 않으므로, 열 때 가져오는 <b>지연 로드</b>를 쓰면 첫 화면이 가벼워집니다. 다만 열 때마다 서버를 다시 부르지 않도록 받아 온 내용은 캐시에 둡니다."),
    ("바깥 클릭 처리는 이벤트 전파 차단", "팝오버 안쪽을 눌러도 문서 전체에 걸어 둔 닫기 처리가 함께 실행되어 팝오버가 닫혀 버립니다. 그래서 안쪽 클릭에서 <code>stopPropagation</code>을 부르는데, 이벤트 버스에서 이벤트에 <b>처리 완료 표시</b>를 해서 더 퍼지지 않게 하는 것과 같습니다."),
    ("플립과 시프트는 경계 검사", "팝오버를 띄울 때마다 '화면 밖으로 나가는가'를 계산합니다. 값이 범위를 벗어나면 범위 안으로 되돌리는 clamp와 같은 일입니다."),
    ("바꾼 값을 먼저 반영하는 낙관적 적용", "체크를 바꾸자마자 목록을 걸러 보여 주고, 서버 응답은 나중에 받아 맞춰도 됩니다. 팝오버에서 바꾸는 필터 같은 값은 틀렸을 때 되돌리기 쉬워서 낙관적 처리가 잘 맞습니다."),
  ]),
  plat_lede="팝오버는 웹에서 가장 자유롭게 쓰지만, 모바일에서는 기기에 따라 다른 부품으로 바뀝니다.",
  plats=plats([
    ("웹", "<code>popover</code> 속성 · <code>anchor</code>",
     mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태"), bars="684", label="웹 팝오버 재현"),
     "<b>팝오버</b> · 요즘 브라우저는 <code>popover</code> 속성을 지원해서, 바깥을 누르면 닫는 처리와 겹침 순서를 브라우저가 대신 맡아 줍니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;background:color-mix(in srgb,var(--surface) 92%,var(--bg));border-radius:10px;padding:6px;box-shadow:0 6px 18px rgba(0,0,0,.25)"><i style="display:block;font-style:normal;font-size:8.5px;color:#0a84ff;padding:3px">공유</i><i style="display:block;font-style:normal;font-size:8.5px;color:#0a84ff;padding:3px">복제</i></div>', "iOS 팝오버 재현"),
     "<b>팝오버</b>(Popover) · 다만 <b>아이패드에서만 팝오버로 보이고 아이폰에서는 시트로 바뀝니다.</b> 그래서 같은 코드라도 기기에 따라 다른 부품으로 보입니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;right:10px;top:26px;background:var(--surface);border-radius:8px;padding:5px;box-shadow:0 6px 18px rgba(0,0,0,.3);min-width:62px"><i style="display:block;font-style:normal;font-size:8.5px;padding:3px 6px">이름 바꾸기</i><i style="display:block;font-style:normal;font-size:8.5px;padding:3px 6px">삭제</i></div>', "안드로이드 메뉴 재현"),
     "<b>메뉴</b>(Menu) · 꼬리는 거의 달지 않습니다. 입력 칸에 붙어서 뜨는 것은 <b>Exposed dropdown menu</b>라고 따로 부릅니다."),
  ]),
  plat_note="iOS의 팝오버는 <b>아이폰에서 자동으로 시트로 바뀝니다.</b> 그래서 디자인 검토를 아이패드에서만 하면, 아이폰에서는 검토 때와 전혀 다른 모양을 보게 됩니다. 팝오버 이야기를 할 때는 어느 기기를 기준으로 말하는지부터 맞추세요.",
  siblings=siblings("popover"),
  related='''        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>
        <li><a href="datepicker.html"><b>날짜 선택기</b><em>4부</em></a></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>''',
)
