# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div class="pin-out" data-pin="1" style="font-size:12px;font-weight:700;margin-bottom:16px">입금 은행</div>
                  <div class="pin-out" data-pin="2" style="display:flex;align-items:center;border:1px solid var(--line-strong);border-radius:5px;padding:12px 26px;margin-bottom:20px">
                    <span class="pin-out" data-pin="3" style="flex:1;font-size:11.5px">신한</span>
                    <span class="pin-tr" data-pin="4" style="color:var(--fg-muted);font-size:9px">▾</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="border:1px solid var(--line);border-radius:6px;box-shadow:var(--e2);padding:14px 26px">
                    <div class="pin-out" data-pin="6" style="font-size:9.5px;color:var(--fg-muted);font-weight:700;margin-bottom:16px">시중은행</div>
                    <div class="pin-out" data-pin="7" style="font-size:11px;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px">신한</div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="select", ko="셀렉트", en="Select · Dropdown",
  desc="셀렉트가 무엇인지, 콤보박스나 라디오와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="셀렉트는 정해진 선택지 가운데 <b>하나</b>를 고르는 칸입니다. 평소에는 접혀 있어 자리를 적게 차지하고, 펼쳐야 선택지가 보입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 칸을 비교해 보세요. 은행처럼 선택지가 <b>10개 안팎</b>이면 셀렉트가 알맞습니다.
          반면 주기처럼 선택지가 <b>셋뿐</b>이면, 펼쳐 보지 않아도 선택지가 다 보이는 라디오나 세그먼티드 컨트롤이 낫습니다.
          소재지는 선택지가 <b>229개</b>나 되어 셀렉트로는 원하는 항목을 찾기 어려운데, 선택지가 이만큼 많아지면 콤보박스로 바꿀 때입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "셀렉트, 선택 상자, 드롭다운"),
    ("영어", "select, dropdown, picker"),
    ("같이 쓰는 말", "선택지 묶음은 <b>옵션 그룹</b>(optgroup), 펼쳐진 목록은 <b>리스트박스</b>, 오른쪽의 화살표는 <b>셰브런</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>드롭다운 메뉴</b> — 메뉴는 이름 바꾸기나 삭제 같은 <b>동작</b>을 고르고, 셀렉트는 <b>값</b>을 고릅니다. 생김새가 닮아서 특히 자주 섞어 부릅니다.<br>"
     "<b>콤보박스</b> — 글자를 입력해 선택지를 걸러 낼 수 있으면 셀렉트가 아니라 콤보박스입니다.<br>"
     "<b>스피너</b> — 안드로이드에서는 셀렉트를 Spinner라고 부르는데, 웹에서 스피너라고 하는 로딩 표시와는 전혀 다른 부품입니다."),
  ]),
  axes=ax("셀렉트"),
  oneline="셀렉트는 <b>선택지를 접어서 감추는</b> 대신 자리를 아낍니다. 그래서 선택지가 셋뿐이면 접어서 아낄 자리가 거의 없고, 수십 개가 넘으면 펼쳐도 눈으로 찾기 어렵습니다.",
  states=states([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">고르세요</span>▾</div></div>', bars="", label="아직 안 고른 셀렉트"), "아직 고르지 않았을 때", "기본값을 함부로 넣지 않습니다. 사용자가 확인하지 않은 기본값이 그대로 저장될 수 있기 때문입니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="고른 셀렉트"), "값을 골랐을 때", "고른 값이 접힌 칸에 보입니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></div><div style="border:1px solid var(--line);border-radius:3px;box-shadow:0 2px 6px rgba(0,0,0,.15);margin-top:3px;padding:3px;background:var(--surface)"><div style="font-size:6px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">신한</div><div style="font-size:6px;color:var(--fg-muted);padding:1px 3px">하나</div></div></div>', bars="", label="펼친 셀렉트"), "목록을 펼쳤을 때", "목록이 펼쳐집니다. 이 목록은 브라우저가 띄우기 때문에 모양을 바꿀 수 없습니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">서울 1구역</span>▾</div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:2px">229개라 눈으로 찾기 어려움</div></div>', bars="", label="선택지가 너무 많은 셀렉트"), "선택지가 너무 많을 때", "목록을 한참 스크롤해야 하고 글자로 걸러 낼 수도 없습니다. <b>콤보박스로 바꿀 때</b>입니다"),
    (mini('<div style="margin-top:10px;padding:0 6px;opacity:.45"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;background:var(--bg);display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="비활성 셀렉트"), "비활성일 때", "왜 고를 수 없는지 칸 옆에 적습니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--danger);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">고르세요</span>▾</div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:2px">은행을 골라 주세요</div></div>', bars="", label="에러 상태"), "고르지 않고 보냈을 때", "고르지 않고 보냈을 때 나타나며, 에러 메시지는 칸 아래에 적습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("라벨", "label", "접혀 있을 때는 고른 값만 보이므로 <b>무엇을 고르는 칸인지</b> 라벨로 분명히 알려야 합니다"),
    ("셀렉트 상자", "select · trigger", "선택지가 접혀 있는 상자입니다. 높이는 44px 이상으로 잡습니다"),
    ("고른 값", "selected value", "지금 고른 값이 여기에 보입니다. 아직 고르지 않았다면 '고르세요' 같은 안내를 적습니다"),
    ("셰브런", "chevron", "눌러서 펼칠 수 있다는 것을 알려 주는 어포던스입니다. 셰브런이 없으면 읽기 전용 칸처럼 보입니다"),
    ("리스트박스", "listbox · popup", "펼친 목록은 브라우저(또는 OS)가 띄우기 때문에 모양을 마음대로 바꿀 수 없습니다"),
    ("옵션 그룹", "optgroup", "선택지를 묶음으로 나눠 보여 줍니다. 선택지가 10개를 넘으면 거의 꼭 필요합니다"),
    ("현재 항목", "selected option", "지금 고른 값입니다. 목록을 열면 이 항목이 보이도록 스크롤되어 있어야 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          펼친 목록은 <b>브라우저나 운영체제가 그립니다.</b> 그래서 폰에서는 휠이나 전체 화면 목록이 뜹니다.
          모양을 꾸미려고 목록을 직접 만들면 첫 글자로 건너뛰기, 폰의 큰 목록, 화면 밖으로 나가지 않게 잡아 주는 위치 계산까지 모두 새로 구현해야 합니다.</p>''',
  do=ul([
    "선택지가 <b>5~15개쯤</b>일 때",
    "은행, 국가, 통화처럼 선택지가 잘 바뀌지 않고 이름이 분명할 때",
    "폼이 길고 칸이 많아서 자리를 아껴야 할 때",
  ]),
  dont=ul([
    "선택지가 2~4개일 때. 라디오나 세그먼티드 컨트롤을 쓰면 펼치지 않아도 선택지가 다 보입니다",
    "선택지가 수십 개를 넘을 때. 글자를 입력해 좁혀 갈 수 있는 콤보박스를 씁니다",
    "값이 아니라 동작을 고를 때. 이때는 드롭다운 메뉴를 씁니다",
    "모양을 바꾸려고 직접 만들 때. 키보드 조작과 폰 목록을 모두 다시 만들어야 합니다",
  ]),
  instead='선택지가 두세 개뿐이면 <a href="radio.html">라디오</a>나 <a href="segmented.html">세그먼티드</a> 컨트롤을 쓰고, 선택지가 많아 글자로 걸러야 하면 <a href="combobox.html">콤보박스</a>를 씁니다. 여러 개를 함께 골라야 하면 <a href="checkbox.html">체크박스</a>가 맞습니다.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", tall=False, label="기본 셀렉트 재현"),
     "폼 안의 기본 셀렉트", "폼 안에서 가장 흔히 보는 모습입니다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:flex;gap:3px"><div style="flex:1;height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:5.5px"><span style="flex:1">2026</span>▾</div><div style="flex:1;height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:5.5px"><span style="flex:1">11월</span>▾</div></div>', bars="", tall=False, label="여러 칸으로 나눈 재현"),
     "단위마다 칸을 나눈 셀렉트", "날짜처럼 여러 단위로 이루어진 값은 단위마다 칸을 나눠 두면 고르기 쉽습니다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">먼저 은행을 고르세요</span>▾</div></div>', bars="", tall=False, label="연결된 셀렉트 재현"),
     "앞 칸을 골라야 열리는 셀렉트", "앞 칸을 골라야 뒤 칸을 고를 수 있으므로, 뒤 칸에는 왜 비활성인지 적어 둡니다"),
  ]),
  code_lede="브라우저가 제공하는 <code>&lt;select&gt;</code>를 쓰면 키보드 조작과 폰 목록이 따로 구현하지 않아도 동작합니다. 반면 셀렉트를 직접 만들면 이 기능을 모두 다시 만들어야 합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"bank"</span>&gt;입금 은행&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">select</span> <span class="a">id</span>=<span class="s">"bank"</span> <span class="a">name</span>=<span class="s">"bank"</span> <span class="a">required</span>&gt;
  &lt;<span class="t">option</span> <span class="a">value</span>=<span class="s">""</span>&gt;고르세요&lt;/<span class="t">option</span>&gt;
  &lt;<span class="t">optgroup</span> <span class="a">label</span>=<span class="s">"시중은행"</span>&gt;
    &lt;<span class="t">option</span>&gt;신한&lt;/<span class="t">option</span>&gt;
    &lt;<span class="t">option</span>&gt;하나&lt;/<span class="t">option</span>&gt;
  &lt;/<span class="t">optgroup</span>&gt;
&lt;/<span class="t">select</span>&gt;

<span class="c">/* 모양은 테두리까지만 바꾼다. 펼친 목록은 못 바꾼다 */</span>
select <span class="a">{</span> <span class="t">appearance</span>: none; <span class="t">background-image</span>: url(chevron.svg); <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Space</kbd> · <kbd>Enter</kbd>", "목록을 펼칩니다"),
    ("<kbd>↑</kbd><kbd>↓</kbd>", "선택지를 옮깁니다. 데스크톱에서는 목록을 닫은 채로도 값이 바뀝니다"),
    ("글자 키를 눌렀을 때", "<b>그 글자로 시작하는 선택지로 건너뜁니다.</b> '하'를 누르면 하나은행으로 갑니다. 셀렉트를 직접 만들 때 특히 자주 빠뜨리는 기능입니다"),
    ("<kbd>Esc</kbd>", "고르지 않고 목록을 닫습니다"),
    ("폰에서", "운영체제가 제공하는 큰 목록이나 휠이 뜹니다. 손가락으로 고르기 좋게 이미 만들어져 있습니다"),
  ]),
  backend=rows([
    ("값과 보이는 이름을 따로 두기", "<code>value</code>에는 <code>SHINHAN</code> 같은 코드를 넣고, 화면에 보이는 글자는 사람이 읽는 이름으로 둡니다. 보이는 글자를 그대로 서버에 보내면 <b>은행 이름이 바뀔 때 기존 데이터와 맞지 않게 됩니다.</b>"),
    ("빈 값으로 고르지 않은 상태 나타내기", "<code>value=\"\"</code>인 첫 옵션으로 '아직 고르지 않음'을 나타냅니다. 기본값을 임의로 넣어 두면 <b>사용자가 확인하지 않고 보낸 값</b>이 저장됩니다."),
    ("선택지를 어디서 가져올지", "선택지를 코드에 하드코딩하면 선택지가 바뀔 때마다 다시 배포해야 합니다. 서버에서 받아 오면 다시 배포할 필요는 없지만, 캐시를 관리하고 '저장된 값이 지금 목록에는 없는' 경우를 처리해야 합니다."),
    ("앞 칸 값에 따라 달라지는 조회", "앞 칸의 값이 정해져야 뒤 칸의 선택지를 가져올 수 있습니다. 앞 칸을 바꾸면 <b>뒤 칸의 값을 비워야</b> 하는데, 비우지 않으면 서로 맞지 않는 값 한 쌍이 저장됩니다."),
  ]),
  plat_lede="셀렉트는 펼친 목록을 <b>운영체제가 그리기</b> 때문에 플랫폼마다 모양 차이가 특히 큽니다.",
  plats=plats([
    ("웹", "<code>&lt;select&gt;</code>",
     mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="웹 셀렉트 재현"),
     "<b>셀렉트</b> · 접힌 칸만 꾸밀 수 있고, 펼친 목록은 브라우저가 그립니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:0;background:color-mix(in srgb,var(--surface) 92%,var(--bg));border-radius:10px 10px 0 0;padding:8px 6px;text-align:center"><div style="font-size:7px;color:var(--fg-faint)">국민</div><div style="font-size:9px;font-weight:700;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:4px 0">신한</div><div style="font-size:7px;color:var(--fg-faint)">하나</div></div>', "iOS 피커 재현"),
     "<b>피커</b>(Picker) · 화면 아래에서 <b>휠</b>이 올라오고, 선택지가 적으면 <b>메뉴</b>로 뜨기도 합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><div style="border:1px solid var(--line-strong);border-radius:4px;padding:6px;font-size:7px;display:flex"><span style="flex:1">신한</span>▾</div><div style="background:var(--surface);border-radius:4px;box-shadow:0 4px 12px rgba(0,0,0,.25);margin-top:3px;padding:3px"><div style="font-size:7px;padding:3px 5px;background:var(--accent-soft);color:var(--accent);border-radius:3px">신한</div><div style="font-size:7px;padding:3px 5px;color:var(--fg-muted)">하나</div></div></div>', "안드로이드 드롭다운 재현"),
     "<b>Exposed dropdown menu</b> · 텍스트 필드처럼 생긴 칸 아래로 목록이 펼쳐지며, 예전 이름은 <b>Spinner</b>입니다."),
  ]),
  plat_note="안드로이드에서 <b>Spinner</b>는 이 항목의 셀렉트를 가리킵니다. 웹에서 \"스피너 넣어 주세요\"라고 하면 <a href=\"spinner.html\">돌아가는 로딩 표시</a>를 뜻하지만, 안드로이드 개발자는 <b>선택 상자</b>로 알아듣습니다. 같은 이름이 플랫폼에 따라 전혀 다른 부품을 가리키므로, 웹 개발자와 안드로이드 개발자가 함께 일할 때 특히 오해가 잦습니다.",
  siblings=siblings("select"),
  related='''        <li><a href="menu.html"><b>드롭다운 메뉴</b><em>6부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="datepicker.html"><b>날짜 선택기</b><em>4부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
