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
  desc="셀렉트가 무엇이고 콤보박스·라디오와 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="정해진 선택지 <b>하나</b>를 고르는 칸. 평소에는 접혀 있어 자리를 안 먹고, 열어야 선택지가 보입니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 칸을 비교해 보세요. 은행처럼 <b>10개 안팎</b>이면 셀렉트가 알맞고,
          주기처럼 <b>셋뿐</b>이면 라디오나 세그먼티드가 낫습니다 — 열어 보지 않아도 다 보이니까요.
          소재지는 <b>229개</b>라 셀렉트가 무너집니다. 그 지점이 콤보박스로 넘어갈 때입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "셀렉트, 선택 상자, 드롭다운"),
    ("영어", "select, dropdown, picker"),
    ("같이 쓰는 말", "선택지 묶음을 <b>옵션 그룹</b>(optgroup), 펼쳐진 목록을 <b>리스트박스</b>, 오른쪽 화살표를 <b>셰브런</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>드롭다운 메뉴</b> — 메뉴는 <b>동작</b>을 고르는 것이고(이름 바꾸기, 삭제), 셀렉트는 <b>값</b>을 고릅니다. 생김새가 닮아 가장 자주 섞입니다.<br>"
     "<b>콤보박스</b> — 타이핑으로 걸러지면 콤보박스입니다.<br>"
     "<b>스피너</b> — 안드로이드에서는 셀렉트를 Spinner 라 부릅니다. 웹의 로딩 표시와는 전혀 다른 것입니다."),
  ]),
  axes=ax("셀렉트"),
  oneline="셀렉트는 <b>선택지가 보이지 않는다</b>는 대가로 자리를 아낍니다. 선택지가 셋뿐이면 아낄 자리가 없고, 수십 개면 눈으로 못 찾습니다.",
  states=states([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">고르세요</span>▾</div></div>', bars="", label="아직 안 고른 셀렉트"), "안 고름", "기본값을 함부로 넣지 않는다. 잘못 보낸 값이 남는다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="고른 셀렉트"), "고름", "고른 값이 접힌 칸에 보인다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--accent);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></div><div style="border:1px solid var(--line);border-radius:3px;box-shadow:0 2px 6px rgba(0,0,0,.15);margin-top:3px;padding:3px;background:var(--surface)"><div style="font-size:6px;background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 3px">신한</div><div style="font-size:6px;color:var(--fg-muted);padding:1px 3px">하나</div></div></div>', bars="", label="펼친 셀렉트"), "펼침", "목록이 뜬다. 브라우저가 띄우므로 모양을 못 바꾼다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">서울 1구역</span>▾</div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:2px">229개 — 눈으로 못 찾음</div></div>', bars="", label="선택지가 너무 많은 셀렉트"), "너무 많음", "스크롤이 길고 걸러낼 수 없다. <b>콤보박스로 갈 때</b>"),
    (mini('<div style="margin-top:10px;padding:0 6px;opacity:.45"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;background:var(--bg);display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="비활성 셀렉트"), "비활성", "왜 못 고르는지 옆에 적는다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--danger);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">고르세요</span>▾</div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:2px">은행을 골라 주세요</div></div>', bars="", label="에러 상태"), "에러", "안 고르고 보냈을 때. 칸 아래에 적는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("라벨", "label", "접혀 있을 때 고른 값만 보이므로 <b>무엇을 고르는 칸인지</b>가 더 중요하다"),
    ("셀렉트 상자", "select · trigger", "접힌 상태. 높이는 44px 이상"),
    ("고른 값", "selected value", "여기에 보인다. 아직 안 골랐으면 '고르세요' 같은 안내"),
    ("셰브런", "chevron", "펼쳐진다는 어포던스. 이게 없으면 그냥 읽기 전용 칸처럼 보인다"),
    ("리스트박스", "listbox · popup", "브라우저(또는 OS)가 띄운다. 그래서 모양을 마음대로 못 바꾼다"),
    ("옵션 그룹", "optgroup", "선택지를 묶어 준다. 10개가 넘으면 거의 필수다"),
    ("현재 항목", "selected option", "지금 값. 열면 여기로 스크롤돼 있어야 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          펼친 목록은 <b>브라우저나 운영체제가 그립니다.</b> 그래서 폰에서는 휠이나 전체 화면 목록이 뜨고,
          모양을 꾸미려고 직접 만들면 그 편의를 전부 잃습니다 — 첫 글자로 건너뛰기, 폰의 큰 목록, 화면 밖으로 안 나가는 위치까지.</p>''',
  do=ul([
    "선택지가 <b>5~15개쯤</b>일 때",
    "선택지가 바뀌지 않고 이름이 분명할 때 — 은행, 국가, 통화",
    "자리를 아껴야 할 때 — 폼이 길고 칸이 많을 때",
  ]),
  dont=ul([
    "선택지가 2~4개 → 라디오나 세그먼티드. 열어 보지 않아도 다 보입니다",
    "수십 개가 넘을 때 → 콤보박스. 타이핑으로 좁혀야 합니다",
    "동작을 고를 때 → 드롭다운 메뉴입니다",
    "모양을 바꾸려고 직접 만들기 — 키보드·폰 목록을 전부 다시 만들어야 합니다",
  ]),
  instead='둘셋이면 <a href="radio.html">라디오</a>나 <a href="segmented.html">세그먼티드</a>, 많으면 <a href="combobox.html">콤보박스</a>, 여럿 고르면 <a href="checkbox.html">체크박스</a>.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", tall=False, label="기본 셀렉트 재현"),
     "기본", "폼 안에서 가장 흔한 모습"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:flex;gap:3px"><div style="flex:1;height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:5.5px"><span style="flex:1">2026</span>▾</div><div style="flex:1;height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:5.5px"><span style="flex:1">11월</span>▾</div></div>', bars="", tall=False, label="여러 칸으로 나눈 재현"),
     "쪼갠 셀렉트", "날짜처럼 자릿수가 다른 값은 나눠 두면 고르기 쉽다"),
    (mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1;color:var(--fg-faint)">먼저 은행을 고르세요</span>▾</div></div>', bars="", tall=False, label="연결된 셀렉트 재현"),
     "묶인 셀렉트", "앞 칸을 골라야 뒤 칸이 열린다. 비활성 이유를 적어 둔다"),
  ]),
  code_lede="브라우저가 주는 <code>&lt;select&gt;</code>를 쓰면 키보드 조작과 폰 목록이 전부 공짜입니다. 직접 만들면 그걸 다 다시 만들어야 합니다.",
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
    ("<kbd>Space</kbd> · <kbd>Enter</kbd>", "펼친다"),
    ("<kbd>↑</kbd><kbd>↓</kbd>", "선택지를 옮긴다. 데스크톱에서는 닫힌 채로도 움직인다"),
    ("글자 키", "<b>첫 글자로 건너뛴다.</b> '하'를 누르면 하나은행으로. 직접 만들면 가장 자주 빠뜨리는 기능"),
    ("<kbd>Esc</kbd>", "고르지 않고 닫는다"),
    ("폰", "운영체제의 큰 목록이나 휠이 뜬다. 손가락에 맞춰 이미 만들어져 있다"),
  ]),
  backend=rows([
    ("값과 라벨은 다른 것", "<code>value</code>는 코드(<code>SHINHAN</code>), 보이는 글자는 사람 말입니다. 보이는 글자를 그대로 보내면 <b>이름이 바뀔 때 데이터가 깨집니다.</b>"),
    ("빈 값 = 안 고름", "<code>value=\"\"</code>인 첫 옵션으로 '안 고름'을 나타냅니다. 기본값을 임의로 넣으면 <b>사용자가 안 보고 보낸 값</b>이 들어옵니다."),
    ("선택지 출처", "하드코딩이면 바뀔 때마다 배포해야 합니다. 서버에서 받으면 캐시와 '값은 있는데 목록에 없는' 경우를 다뤄야 합니다."),
    ("묶인 셀렉트 = 의존 질의", "앞 칸이 정해져야 뒤 칸을 가져올 수 있습니다. 앞을 바꾸면 <b>뒤 값을 비워야</b> 합니다 — 안 비우면 말이 안 되는 짝이 저장됩니다."),
  ]),
  plat_lede="셀렉트는 펼친 목록을 <b>운영체제가 그려서</b>, 플랫폼마다 모양이 가장 크게 다릅니다.",
  plats=plats([
    ("웹", "<code>&lt;select&gt;</code>",
     mini('<div style="margin-top:10px;padding:0 6px"><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 4px;font-size:6px"><span style="flex:1">신한</span>▾</div></div>', bars="", label="웹 셀렉트 재현"),
     "<b>셀렉트</b> · 접힌 칸만 꾸밀 수 있고 펼친 목록은 브라우저 몫입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:0;right:0;bottom:0;background:color-mix(in srgb,var(--surface) 92%,var(--bg));border-radius:10px 10px 0 0;padding:8px 6px;text-align:center"><div style="font-size:7px;color:var(--fg-faint)">국민</div><div style="font-size:9px;font-weight:700;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:4px 0">신한</div><div style="font-size:7px;color:var(--fg-faint)">하나</div></div>', "iOS 피커 재현"),
     "<b>피커</b>(Picker) · 아래에서 <b>휠</b>이 올라옵니다. 선택지가 적으면 <b>메뉴</b>로 뜨기도 합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><div style="border:1px solid var(--line-strong);border-radius:4px;padding:6px;font-size:7px;display:flex"><span style="flex:1">신한</span>▾</div><div style="background:var(--surface);border-radius:4px;box-shadow:0 4px 12px rgba(0,0,0,.25);margin-top:3px;padding:3px"><div style="font-size:7px;padding:3px 5px;background:var(--accent-soft);color:var(--accent);border-radius:3px">신한</div><div style="font-size:7px;padding:3px 5px;color:var(--fg-muted)">하나</div></div></div>', "안드로이드 드롭다운 재현"),
     "<b>Exposed dropdown menu</b> · 텍스트 필드처럼 생긴 칸 아래로 목록이 펼쳐집니다. 옛 이름이 <b>Spinner</b>입니다."),
  ]),
  plat_note="안드로이드에서 <b>Spinner</b>는 이 부품(셀렉트)입니다. 웹에서 \"스피너 넣어 주세요\"는 <a href=\"spinner.html\">돌아가는 로딩 표시</a>인데, 안드로이드 개발자는 <b>선택 상자</b>로 알아듣습니다. 같은 자리에서 가장 크게 어긋나는 이름입니다.",
  siblings=siblings("select"),
  related='''        <li><span class="na"><b>드롭다운 메뉴</b><em>7부</em></span></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><span class="na"><b>날짜 선택기</b><em>4부</em></span></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>''',
)
