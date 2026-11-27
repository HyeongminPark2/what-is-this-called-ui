# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div class="pin-out" data-pin="1" style="border:1px solid var(--accent);border-radius:5px;padding:12px 26px;margin-bottom:20px;box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 20%,transparent)">
                    <span class="pin-out" data-pin="2" style="font-size:11.5px">블루보틀</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="border:1px solid var(--line);border-radius:6px;box-shadow:var(--e2);padding:14px 26px">
                    <div class="pin-out" data-pin="4" style="display:flex;align-items:center;gap:40px;font-size:11px;background:var(--accent-soft);border-radius:4px;padding:5px 7px;margin-bottom:16px">
                      <span style="flex:1"><b style="color:var(--accent)">블루보틀</b> 성수 5호</span>
                      <span class="pin-tr" data-pin="5" style="font-size:9.5px;color:var(--fg-muted)">M1004</span>
                    </div>
                    <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted)">229개 중 2개</div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="combobox", ko="콤보박스", en="Combobox · Autocomplete",
  desc="콤보박스가 무엇인지, 셀렉트와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="콤보박스는 <b>글자를 입력해 선택지를 좁힌 뒤</b> 고르는 칸입니다. 입력칸과 목록을 붙여 놓은 부품이라서, 선택지가 수십·수백 개일 때는 사실상 콤보박스 말고는 쓸 만한 방법이 없습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><kbd>↓</kbd><kbd>↑</kbd>로 항목을 옮기고 <kbd>Enter</kbd>로 고르고 <kbd>Esc</kbd>로 목록을 닫을 수 있어서, 키보드에서 손을 떼지 않고도 끝까지 고를 수 있습니다.<br>
          위의 체크를 켜면 <b>목록에 없는 값도</b> 받고, 끄면 목록 안에서만 고를 수 있습니다.
          이 설정 하나에 따라 콤보박스는 '검색되는 셀렉트'가 되기도 하고 '자동완성이 붙은 입력칸'이 되기도 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "콤보박스, 자동완성, 검색 선택"),
    ("영어", "combobox, autocomplete, typeahead"),
    ("같이 쓰는 말", "입력한 글자에 맞춰 선택지를 걸러 주는 동작은 <b>타입어헤드</b>, 키보드로 짚고 있는 항목은 <b>활성 항목</b>(active descendant), 입력한 글자와 맞는 부분을 굵게 표시하는 것은 <b>하이라이트</b>라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>셀렉트</b> — 글자를 입력해 선택지를 걸러 낼 수 있으면 셀렉트가 아니라 콤보박스입니다.<br>"
     "<b>검색창</b> — 검색창은 검색 결과 <b>화면</b>으로 넘어가지만, 콤보박스는 <b>그 자리에서 값 하나를</b> 정합니다.<br>"
     "<b>드롭다운</b> — 아래로 펼쳐지는 것을 두루 가리키는 말이라서, 이렇게 부르면 셀렉트와 메뉴, 콤보박스를 구별할 수 없습니다."),
  ]),
  axes=ax("콤보박스"),
  oneline="콤보박스는 <b>글자를 입력해 선택지를 좁힐 수 있는 셀렉트</b>입니다. 목록에 없는 값을 받을지는 따로 정해야 하는데, 이 설정에 따라 서버가 받는 값과 검증 방식까지 달라집니다.",
  states=states([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px;color:var(--fg-faint)">이름을 입력하세요</div></div>', bars="", label="닫힌 콤보박스"), "목록이 닫혀 있을 때", "입력칸처럼 보이며, 자리글로 <b>글자를 입력하라</b>고 알려 줍니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px"></div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:3px;background:var(--surface);box-shadow:0 2px 6px rgba(0,0,0,.15)"><div style="font-size:6px;padding:1px 3px">모란상회 1호</div><div style="font-size:6px;padding:1px 3px;color:var(--fg-muted)">모란김밥 2호</div></div></div>', bars="", label="열린 콤보박스"), "목록을 열었을 때", "아직 아무것도 입력하지 않았다면 선택지 가운데 <b>앞쪽 몇 개</b>를 보여 줍니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">블루보틀</div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:3px;background:var(--surface);box-shadow:0 2px 6px rgba(0,0,0,.15)"><div style="font-size:6px;padding:1px 3px;background:var(--accent-soft);border-radius:2px"><b style="color:var(--accent)">블루보틀</b> 성수</div></div></div>', bars="", label="걸러진 목록"), "글자로 걸렀을 때", "입력한 글자와 맞는 부분을 굵게 표시해서 <b>이 항목이 왜 걸렸는지</b> 보여 줍니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">없는가게</div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:4px;background:var(--surface);font-size:5.5px;color:var(--fg-muted)">맞는 것이 없습니다</div></div>', bars="", label="결과 없음"), "맞는 결과가 없을 때", "'없음'만 띄우고 끝내지 않습니다. 입력한 값을 <b>그대로 쓰기</b>나 다시 찾는 방법을 함께 보여 줍니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px"></div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:4px;background:var(--surface);display:flex;align-items:center;gap:4px"><span class="spn spn--sm" style="width:8px;height:8px;border-width:1.5px"></span><span style="font-size:5.5px;color:var(--fg-muted)">찾는 중…</span></div></div>', bars="", label="서버에서 찾는 중"), "서버에서 찾는 중", "서버에서 목록을 가져오는 중입니다. <b>디바운스</b>를 걸어 글자 하나 칠 때마다 서버를 부르지 않게 합니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">블루보틀 성수 5호</div><div style="font-size:5.5px;color:#1f8a4c;font-weight:700;margin-top:2px">M1004 선택됨</div></div>', bars="", label="고른 뒤"), "값을 고른 뒤", "목록이 닫히고 고른 값이 칸에 남습니다. 이때 이름과 함께 <b>코드도 같이</b> 기억해 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("입력칸", "combobox input", "<code>role=\"combobox\"</code>를 달고, 목록이 열렸는지를 <code>aria-expanded</code>로 알립니다"),
    ("입력한 글자", "query", "선택지를 걸러 내는 기준입니다. 글자를 지우면 다시 전체 목록이 나옵니다"),
    ("목록", "listbox", "입력칸 바로 아래에 띄웁니다. 화면 아래로 넘칠 것 같으면 입력칸 위쪽에 띄웁니다"),
    ("활성 항목", "active option", "키보드로 짚고 있는 항목이며 <code>aria-activedescendant</code>로 알립니다. 이때 <b>포커스는 입력칸에 그대로 둡니다</b>"),
    ("보조 정보", "secondary text", "같은 이름이 여럿일 때 서로 구별하게 해 주는 코드, 지역, 날짜 같은 정보입니다"),
    ("결과 수", "result count", "선택지가 몇 개로 좁혀졌는지 보여 줍니다. 라이브 리전으로 스크린 리더가 읽게 하면 더 좋습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          그림에는 보이지 않지만 콤보박스에서 특히 중요한 결정이 <b>목록에 없는 값을 받을 것인가</b>입니다.
          받으면 자동완성이 붙은 자유 입력칸이 되고, 받지 않으면 검색되는 셀렉트가 됩니다.
          어느 쪽을 고르느냐에 따라 서버가 받는 값의 형태부터 달라집니다.</p>''',
  do=ul([
    "가맹점, 도시, 사용자처럼 선택지가 <b>수십 개 넘게</b> 있을 때",
    "찾는 항목의 이름을 이미 알고 있을 때. 이름을 입력하는 쪽이 목록을 훑는 것보다 빠릅니다",
    "목록이 서버에 있어 한 번에 다 못 받을 때",
  ]),
  dont=ul([
    "선택지가 열 개 안팎일 때. 셀렉트가 더 단순합니다",
    "이름을 모르고 둘러보며 골라야 할 때. 무엇을 입력해 걸러야 할지 모르면 쓸 수 없습니다",
    "결과가 없을 때 '없음'만 띄우고 끝낼 때. 입력한 값을 그대로 쓰거나 다시 찾을 방법을 줍니다",
    "포커스를 목록으로 옮길 때. 포커스가 입력칸을 떠나면 이어서 입력할 수 없습니다",
  ]),
  instead='선택지가 열 개 안팎이면 <a href="select.html">셀렉트</a>로 충분하고, 정해진 선택지 없이 자유롭게 적는 값이면 <a href="field.html">텍스트 필드</a>를 씁니다. 여러 개를 함께 골라야 하면 <a href="checkbox.html">체크박스</a>나 태그 입력이 맞습니다.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">블루보틀</div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:3px;background:var(--surface);box-shadow:0 2px 6px rgba(0,0,0,.15)"><div style="font-size:6px;padding:1px 3px;display:flex"><span style="flex:1"><b style="color:var(--accent)">블루보틀</b> 성수</span><span style="color:var(--fg-muted);font-size:5px">M1004</span></div></div></div>', bars="", tall=False, label="단일 선택 콤보박스 재현"),
     "값 하나 고르기", "가장 흔한 모습입니다. 하나를 고르면 목록이 닫힙니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="min-height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;gap:2px;padding:2px;flex-wrap:wrap"><span style="background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:0 3px;font-size:5.5px">성수 ✕</span><span style="background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:0 3px;font-size:5.5px">삼청 ✕</span></div></div>', bars="", tall=False, label="여러 개 고른 재현"),
     "여러 개 고르기", "고른 항목이 칸 안에 <b>칩</b>으로 하나씩 붙고, 칩마다 지울 수 있어야 합니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">새로운가게</div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:4px;background:var(--surface);font-size:5.5px"><b>“새로운가게”</b> 그대로 쓰기</div></div>', bars="", tall=False, label="없는 값 허용 재현"),
     "목록에 없는 값도 받기", "목록에 없는 값도 받는 방식입니다. 태그나 키워드를 입력하는 칸에서 흔히 씁니다"),
  ]),
  code_lede="콤보박스는 브라우저가 제공하는 부품이 없어서 <b>직접 만들어야</b> 합니다. 그래서 키보드 조작과 스크린 리더 처리를 빠뜨리기 쉽습니다.",
  code='''&lt;<span class="t">input</span> <span class="a">role</span>=<span class="s">"combobox"</span> <span class="a">aria-expanded</span>=<span class="s">"false"</span>
       <span class="a">aria-controls</span>=<span class="s">"list"</span> <span class="a">aria-autocomplete</span>=<span class="s">"list"</span>
       <span class="a">autocomplete</span>=<span class="s">"off"</span>&gt;
&lt;<span class="t">ul</span> <span class="a">id</span>=<span class="s">"list"</span> <span class="a">role</span>=<span class="s">"listbox"</span> <span class="a">hidden</span>&gt;
  &lt;<span class="t">li</span> <span class="a">role</span>=<span class="s">"option"</span> <span class="a">id</span>=<span class="s">"o0"</span> <span class="a">aria-selected</span>=<span class="s">"true"</span>&gt;…&lt;/<span class="t">li</span>&gt;
&lt;/<span class="t">ul</span>&gt;

<span class="c">// 포커스는 입력칸에 두고, 짚고 있는 항목만 가리킨다</span>
input.setAttribute(<span class="s">'aria-activedescendant'</span>, <span class="s">'o0'</span>);

<span class="c">// 서버에서 찾을 때는 한 글자마다 부르지 않는다</span>
clearTimeout(t); t = setTimeout(search, <span class="a">250</span>);''',
  keys=kbd([
    ("<kbd>↓</kbd><kbd>↑</kbd>", "항목을 옮기고, 목록이 닫혀 있으면 엽니다. 이때도 <b>포커스는 입력칸에 그대로 둡니다</b>"),
    ("<kbd>Enter</kbd>", "짚고 있는 항목을 고릅니다. 목록에 없는 값을 받는 설정이면 입력한 글자를 그대로 값으로 씁니다"),
    ("<kbd>Esc</kbd>", "고르지 않고 목록을 닫습니다. 한 번 더 누르면 입력한 글자도 지웁니다"),
    ("<kbd>Home</kbd><kbd>End</kbd>", "입력한 글자의 처음이나 끝으로 커서를 옮깁니다. 이 키는 목록이 아니라 <b>입력칸</b>이 받습니다"),
    ("스크린 리더로 읽을 때", "<code>aria-activedescendant</code>로 짚은 항목을 읽어 주고, 결과 수는 라이브 리전으로 알립니다"),
  ]),
  backend=rows([
    ("선택지를 어디서 걸러 낼지", "목록이 작으면 화면에서 거르고, 크면 서버에서 거릅니다. 서버에서 거를 때는 <b>디바운스</b>를 250ms쯤 걸어 글자 하나 칠 때마다 요청을 보내지 않게 합니다."),
    ("응답 순서가 뒤섞이는 문제", "'블', '블루', '블루보'를 차례로 보냈어도 응답은 거꾸로 올 수 있습니다. 그래서 <b>마지막으로 보낸 질의의 결과만</b> 반영해야 하고, 그렇지 않으면 지금 입력한 글자와 맞지 않는 목록이 남습니다."),
    ("보이는 이름 대신 코드 보내기", "고른 뒤 서버에 보내야 하는 값은 화면에 보이는 이름이 아니라 <b>코드</b>입니다. 이름만 보내면 이름이 같은 사람이나 가맹점이 있을 때 어느 쪽인지 구별할 수 없습니다."),
    ("없는 값을 받으면 달라지는 API", "목록에 없는 값을 받으면 서버가 <b>새 값을 만들</b> 수 있어야 하고, 받지 않으면 서버가 그 값이 <b>목록에 있는지 다시 검증</b>해야 합니다. 화면의 설정 하나에 따라 API의 형태가 달라집니다."),
  ]),
  plat_lede="웹에는 콤보박스 표준 부품이 없고, 모바일에서는 플랫폼마다 제공하는 검색 화면으로 해결합니다.",
  plats=plats([
    ("웹", "표준 부품이 없음",
     mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">블루보틀</div><div style="border:1px solid var(--line);border-radius:3px;margin-top:3px;padding:3px;background:var(--surface)"><div style="font-size:6px;padding:1px 3px"><b style="color:var(--accent)">블루보틀</b> 성수</div></div></div>', bars="", label="웹 콤보박스 재현"),
     "<b>콤보박스</b> · <code>&lt;datalist&gt;</code>가 비슷한 일을 하지만 모양을 바꿀 수 없고 브라우저마다 동작이 달라서, 대부분 직접 만듭니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:30px"><div style="background:var(--bg);border-radius:8px;padding:4px 6px;font-size:7px;color:var(--fg-muted)">⌕ 블루보틀</div><div style="margin-top:5px"><div style="font-size:7px;padding:3px 0;border-bottom:1px solid var(--line)">블루보틀 성수</div><div style="font-size:7px;padding:3px 0;color:var(--fg-muted)">블루보틀 삼청</div></div></div>', "iOS 검색 화면 재현"),
     "<b>검색 화면</b>으로 해결하는 경우가 많습니다. 칸을 누르면 전체 화면 검색으로 넘어가고, 항목을 고르면 원래 화면으로 돌아옵니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:36px"><div style="border:1px solid var(--accent);border-radius:4px;padding:5px;font-size:7px">블루보틀</div><div style="background:var(--surface);border-radius:4px;box-shadow:0 4px 12px rgba(0,0,0,.25);margin-top:3px;padding:3px"><div style="font-size:7px;padding:3px 5px">블루보틀 성수</div></div></div>', "안드로이드 Exposed dropdown 재현"),
     "<b>Exposed dropdown menu</b>의 편집 가능 모드나 <b>Search bar</b>를 씁니다. 둘 다 표준 부품으로 정리되어 있습니다."),
  ]),
  plat_note="폰에서는 <b>칸 아래에 목록을 띄우는 방식이 잘 안 맞습니다.</b> 키보드가 올라오면 목록이 가려지기 때문입니다. 그래서 모바일에서는 전체 화면 검색이나 <a href=\"sheet.html\">바텀시트</a>로 바꾸는 편이 낫습니다. 모바일에서 어느 방식을 쓸지는 디자인 시안에 함께 그려 두어야 합니다.",
  siblings=siblings("combobox"),
  related='''        <li><span class="na"><b>태그 입력(칩 입력)</b><em>4부</em></span></li>
        <li><a href="searchresults.html"><b>검색과 결과</b><em>13부</em></a></li>
        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>''',
)
