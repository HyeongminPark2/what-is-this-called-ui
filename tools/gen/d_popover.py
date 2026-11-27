# -*- coding: utf-8 -*-
from parts import *
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

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
  desc="팝오버가 무엇이고 툴팁·드롭다운 메뉴·모달과 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="누른 것 <b>옆에 붙어서</b> 뜨는 작은 판. 뒤를 막지 않고, <b>안에 누를 것이 들어 있습니다</b> — 이 점이 툴팁과 다릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>열어 둔 채로 아래 목록을 읽어 보세요.</b> 뒤가 안 막힙니다.
          오른쪽 끝 '내 계정'은 화면 밖으로 나가지 않으려고 <b>반대쪽으로 뒤집혀</b> 열립니다 —
          이걸 <b>플립</b>이라 부르고, 팝오버를 직접 만들 때 가장 자주 빠뜨리는 부분입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "팝오버, 팝업 메뉴, 플라이아웃"),
    ("영어", "popover, flyout"),
    ("같이 쓰는 말", "안에 든 것이 <b>메뉴 항목뿐</b>이면 <b>드롭다운 메뉴</b>라 따로 부릅니다. 폼이나 설정이 들어가면 팝오버입니다. 붙는 기준이 되는 요소는 <b>앵커</b>(anchor)."),
    ("자주 잘못 부름",
     "<b>툴팁</b> — 설명만 하면 툴팁, 누를 것이 있으면 팝오버입니다. 가장 흔한 혼동입니다.<br>"
     "<b>모달</b> — 팝오버는 뒤를 안 막습니다.<br>"
     "<b>팝업</b> — 브라우저가 띄우는 새 창과 섞입니다."),
  ]),
  axes=axis_table("팝오버"),
  oneline="팝오버인지 툴팁인지는 <b>안에 누를 것이 있느냐</b>로 갈립니다. 누를 것이 생기는 순간 툴팁이 아니라 팝오버입니다.",
  states=states([
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>', bars="684", label="팝오버가 닫힌 모습"), "닫힘", "앵커만 보인다. <code>aria-expanded=\"false\"</code>"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger" style="border-color:var(--accent);color:var(--accent)">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태"), bars="684", label="팝오버가 열린 모습"), "열림", "앵커 바로 아래. 앵커도 눌린 상태로 보인다"),
    (mini('<div style="margin-top:8px;text-align:right"><span class="mini__trigger">계정 ▾</span></div>' + pop(["로그아웃"], pos="right:8px;top:32px", tail="right:10px;top:-4px"), bars="684", label="오른쪽 가장자리에서 뒤집힌 팝오버"), "뒤집힘", "화면 밖으로 나갈 것 같으면 반대쪽으로. <b>플립</b>"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:2px;top:32px", tail="left:14px;top:-4px"), bars="684", label="가장자리에서 밀린 팝오버"), "밀림", "꼬리는 앵커를 가리킨 채 판만 안으로 민다. <b>시프트</b>"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태") + '<div style="position:absolute;right:6px;bottom:6px;font-size:8px;color:var(--fg-muted)">바깥 누름 ↘</div>', bars="684", label="바깥을 눌러 닫히는 팝오버"), "바깥 누름", "스크림이 없으니 <b>직접</b> 닫아 줘야 한다"),
    (mini('<div style="margin-top:8px;opacity:.3"><span class="mini__trigger">필터 ▾</span></div>', bars="684", label="앵커가 스크롤로 사라진 모습"), "앵커가 사라짐", "스크롤로 앵커가 화면 밖에 나가면 팝오버도 따라 닫는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("앵커 · 트리거", "anchor · trigger", "팝오버가 붙는 기준. 열려 있는 동안 눌린 상태로 보여 준다"),
    ("오프셋", "offset", "앵커와 판 사이의 빈 자리. 보통 8~12px"),
    ("꼬리", "tail · arrow · caret", "어디서 나온 것인지 가리킨다. 없는 디자인도 많다"),
    ("패널", "panel · surface", "모달보다 그림자를 약하게 준다. 덜 떠 있어야 한다"),
    ("헤더", "header", "짧게. 길면 팝오버에 담을 내용이 아니다"),
    ("내용", "content", "한눈에 들어오는 분량만. 스크롤이 생기면 다시 생각할 때다"),
    ("액션 영역", "footer", "적용·초기화. 바로 반영되는 설계면 아예 없어도 된다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          여기 안 보이는 두 가지가 더 있습니다 — <b>플립</b>(화면 밖으로 나갈 것 같으면 반대쪽으로 뒤집기)과
          <b>시프트</b>(꼬리는 둔 채 판만 안으로 밀기). 둘 다 자리 계산 규칙이라 그림에 테두리가 없습니다.</p>''',
  do=ul([
    "추가 설정·필터 — 화면을 떠나지 않고 조건만 바꿀 때",
    "한두 칸짜리 빠른 편집",
    "보조 정보 더 보기 — 사용자 카드, 미리보기",
  ]),
  dont=ul([
    "꼭 답해야 하는 것 → 모달. 팝오버는 바깥을 누르면 사라집니다",
    "긴 폼이나 여러 단계 → 페이지나 드로어",
    "모바일에서 손가락으로 쓰기 어려운 크기 → 바텀시트로 바꿉니다",
    "팝오버 안에서 또 팝오버 — 바깥 클릭 처리가 바로 엉킵니다",
  ]),
  instead='꼭 답을 받아야 하면 <a href="modal.html">모달</a>, 설명만이면 <a href="tooltip.html">툴팁</a>, 폰에서는 <a href="sheet.html">바텀시트</a>, 긴 작업이면 <a href="drawer.html">드로어</a>.',
  cases=cases([
    (mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패", "☐ 대기"], pos="left:8px;top:32px", head="상태"), bars="684", tall=False, label="필터 팝오버 재현"),
     "필터", "목록을 보면서 조건만 바꾼다. 가장 흔한 쓰임"),
    (mini('<div style="margin-top:8px"><span class="mini__trigger">2026-11-13</span></div>' + '<div class="mini__pop" style="left:8px;top:32px;width:86px"><span class="tail" style="left:10px;top:-4px"></span><b style="font-size:8px;display:block;margin-bottom:3px">11월</b><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:2px;font-size:6.5px;color:var(--fg-muted);text-align:center">' + "".join('<span%s>%d</span>' % (' style="background:var(--accent);color:#fff;border-radius:2px"' if d == 13 else "", d) for d in range(8, 29)) + '</div></div>', bars="684", tall=False, label="날짜 선택 팝오버 재현"),
     "날짜 선택기", "입력칸에 붙어서 뜬다. 안에 누를 것이 가득하다"),
    (mini('<div style="margin-top:8px;text-align:right"><span class="mini__trigger">길동</span></div>' + '<div class="mini__pop" style="right:8px;top:32px;width:84px"><span class="tail" style="right:10px;top:-4px"></span><b style="font-size:8.5px;display:block">홍길동</b><i>gildong@example.com</i><i style="color:var(--accent);font-weight:700;margin-top:3px">로그아웃</i></div>', bars="684", tall=False, label="사용자 카드 팝오버 재현"),
     "사용자 카드", "오른쪽 끝이라 반대쪽으로 뒤집혀 열린다"),
  ]),
  code_lede="스크림이 없으니 <b>바깥 클릭과 <kbd>Esc</kbd>를 직접 처리</b>해야 합니다. 모달이 공짜로 주던 것을 여기서는 손으로 만듭니다.",
  code='''&lt;<span class="t">button</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span> <span class="a">aria-controls</span>=<span class="s">"p1"</span>&gt;필터 ▾&lt;/<span class="t">button</span>&gt;
&lt;<span class="t">div</span> <span class="a">id</span>=<span class="s">"p1"</span> <span class="a">role</span>=<span class="s">"dialog"</span> <span class="a">aria-label</span>=<span class="s">"필터"</span> <span class="a">hidden</span>&gt;…&lt;/<span class="t">div</span>&gt;

<span class="c">// 바깥을 누르면 닫는다 — 스크림이 없으니 직접</span>
pop.addEventListener(<span class="s">'click'</span>, e =&gt; e.stopPropagation());
document.addEventListener(<span class="s">'click'</span>, closeAll);

<span class="c">// Esc 로 닫고 포커스를 앵커로 돌려준다</span>
document.addEventListener(<span class="s">'keydown'</span>, e =&gt; <span class="a">{</span>
  <span class="a">if</span> (e.key === <span class="s">'Escape'</span>) <span class="a">{</span> close(); btn.focus(); <span class="a">}</span>
<span class="a">}</span>);''',
  keys=kbd([
    ("<kbd>Esc</kbd>", "닫히고 포커스가 앵커로 돌아간다"),
    ("<kbd>Tab</kbd>", "팝오버 안을 지나 뒤쪽으로 이어진다. 메뉴형이면 가두고 화살표로 움직인다"),
    ("바깥 누름", "닫힌다. 안쪽 클릭은 전파를 멈춰 안 닫히게 한다"),
    ("열릴 때", "포커스가 첫 요소로. <code>aria-expanded</code> 가 <code>true</code> 가 된다"),
    ("스크롤", "앵커가 화면 밖으로 나가면 같이 닫는다. 안 그러면 허공에 뜬다"),
  ]),
  backend=rows([
    ("열 때 가져오기", "팝오버 내용은 열기 전에는 필요 없습니다. <b>지연 로드</b>하면 첫 화면이 가벼워집니다. 열 때마다 또 부르지 않게 캐시를 둡니다."),
    ("바깥 클릭 = 전파 차단", "문서 전체에 걸린 닫기 처리와 안쪽 클릭이 부딪칩니다. <code>stopPropagation</code> 은 이벤트 버스에서 <b>소비 표시</b>를 하는 것과 같습니다."),
    ("플립·시프트 = 경계 검사", "'화면 밖으로 나가는가'를 매번 계산합니다. 범위를 벗어나면 되접는 clamp 와 같은 일입니다."),
    ("낙관적 적용", "체크를 바꾸자마자 목록을 걸러 보여 주고 서버 응답은 나중에 맞춰도 됩니다. 팝오버는 되돌리기 비용이 싸서 낙관적 처리가 잘 맞습니다."),
  ]),
  plat_lede="팝오버는 웹에서 가장 자유롭게 쓰이고, 모바일에서는 기기에 따라 다른 부품으로 바뀝니다.",
  plats=plats([
    ("웹", "<code>popover</code> 속성 · <code>anchor</code>",
     mini('<div style="margin-top:8px"><span class="mini__trigger">필터 ▾</span></div>' + pop(["☑ 승인", "☐ 실패"], pos="left:8px;top:32px", head="상태"), bars="684", label="웹 팝오버 재현"),
     "<b>팝오버</b> · 최근에는 브라우저가 <code>popover</code> 속성으로 가벼운 닫기와 겹침 순서를 거들어 줍니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px;background:color-mix(in srgb,var(--surface) 92%,var(--bg));border-radius:10px;padding:6px;box-shadow:0 6px 18px rgba(0,0,0,.25)"><i style="display:block;font-style:normal;font-size:8.5px;color:#0a84ff;padding:3px">공유</i><i style="display:block;font-style:normal;font-size:8.5px;color:#0a84ff;padding:3px">복제</i></div>', "iOS 팝오버 재현"),
     "<b>팝오버</b>(Popover) · 다만 <b>아이패드에서만 팝오버로 보이고 아이폰에서는 시트로 바뀝니다.</b> 같은 코드가 기기에 따라 다른 부품이 됩니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;right:10px;top:26px;background:var(--surface);border-radius:8px;padding:5px;box-shadow:0 6px 18px rgba(0,0,0,.3);min-width:62px"><i style="display:block;font-style:normal;font-size:8.5px;padding:3px 6px">이름 바꾸기</i><i style="display:block;font-style:normal;font-size:8.5px;padding:3px 6px">삭제</i></div>', "안드로이드 메뉴 재현"),
     "<b>메뉴</b>(Menu) · 꼬리를 거의 안 씁니다. 입력칸에 붙는 것은 <b>Exposed dropdown menu</b>로 따로 부릅니다."),
  ]),
  plat_note="iOS 에서 팝오버는 <b>아이폰에서 자동으로 시트가 됩니다.</b> 디자인 검토를 아이패드에서만 하면 아이폰에서 전혀 다른 모양을 보게 됩니다. 어느 기기로 보고 말하는지를 먼저 맞추세요.",
  siblings=siblings("popover"),
  related='''        <li><span class="na"><b>드롭다운 메뉴</b><em>7부</em></span></li>
        <li><span class="na"><b>고도와 z-index</b><em>2부</em></span></li>
        <li><span class="na"><b>날짜 선택기</b><em>4부</em></span></li>
        <li><span class="na"><b>필터와 패싯</b><em>10부</em></span></li>''',
)
