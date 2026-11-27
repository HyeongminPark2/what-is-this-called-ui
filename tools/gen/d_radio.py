# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div class="pin-out" data-pin="2" style="font-size:12px;font-weight:700;margin-bottom:20px">정산 주기</div>
                  <div class="pin-out" data-pin="3" style="border:1px solid var(--accent);background:var(--accent-soft);border-radius:6px;padding:12px 26px;margin-bottom:20px">
                    <div style="display:flex;align-items:center;gap:40px">
                      <span data-pin="4" style="width:16px;height:16px;border-radius:50%;border:2px solid var(--accent);flex:none;display:grid;place-items:center">
                        <span style="width:7px;height:7px;border-radius:50%;background:var(--accent)"></span>
                      </span>
                      <span class="pin-out" data-pin="5" style="flex:1;font-size:11.5px;font-weight:600">주 1회</span>
                    </div>
                    <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted);margin-top:16px">월요일에 지난주 몫을 한 번에</div>
                  </div>
                  <div class="pin-out" data-pin="7" style="display:flex;align-items:center;gap:40px;padding-left:26px;opacity:.5">
                    <span style="width:16px;height:16px;border-radius:50%;border:2px solid var(--line-strong);flex:none"></span>
                    <span style="font-size:11.5px">발행하지 않음</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="radio", ko="라디오 그룹", en="Radio group",
  desc="라디오 그룹이 무엇인지, 체크박스나 셀렉트와는 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="라디오 그룹은 선택지를 <b>모두 보여 주면서 그중 하나만</b> 고르게 하는 동그란 칸의 묶음입니다. 선택지끼리 서로 배타적이어서 하나를 켜면 나머지는 꺼집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>한 칸을 고른 뒤 <kbd>↓</kbd><kbd>↑</kbd>를 눌러 보세요. 그룹 안에서 선택이 옮겨 가고, 옮기는 즉시 그 값이 골라집니다.
          반면 <kbd>Tab</kbd>은 그룹 전체를 <b>한 칸</b>으로 보고 지나가므로, 선택지가 열 개여도 Tab 한 번이면 그룹을 벗어납니다.<br>
          또 라디오는 <b>한 번 고르면 아무것도 고르지 않은 상태로 되돌릴 수 없습니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "라디오 버튼, 라디오 그룹, 단일 선택"),
    ("영어", "radio button, radio group"),
    ("같이 쓰는 말", "낱개는 <b>라디오 버튼</b>, 같은 <code>name</code>으로 묶인 전체는 <b>라디오 그룹</b>이라고 부릅니다. 옛 자동차 라디오의 눌러 둔 버튼에서 온 이름입니다."),
    ("자주 잘못 부르는 이름",
     "<b>체크박스</b> — 체크박스는 여러 항목을 각각 고릅니다. 동그라미와 네모라는 모양 차이가 '하나만'과 '여럿'을 알리는 약속입니다.<br>"
     "<b>셀렉트</b> — 똑같이 하나를 고르지만, 셀렉트는 선택지가 접혀 있어서 펼치기 전에는 보이지 않습니다.<br>"
     "<b>토글</b> — 켜고 끄는 것을 두루 가리키는 말이라서, 이렇게 부르면 라디오와 체크박스, 스위치를 구별할 수 없습니다."),
  ]),
  axes=ax("라디오 그룹"),
  oneline="라디오는 <b>선택지를 모두 보여 주면서 하나만</b> 고르게 하는 부품입니다. 선택지를 다 보여 줄 자리가 없으면 셀렉트를, 여럿을 고르게 하려면 체크박스를 씁니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:6.5px">매일</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:6.5px">주 1회</span></div></div>', bars="", label="아직 안 고른 상태"), "아직 고르지 않았을 때", "기본값을 함부로 넣지 않습니다. 사용자가 <b>직접 고르게 하는 것</b>이 목적이라면 비워 둡니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--accent);border-radius:50%;display:grid;place-items:center"><span style="width:4px;height:4px;border-radius:50%;background:var(--accent)"></span></span><span style="font-size:6.5px">매일</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:6.5px">주 1회</span></div></div>', bars="", label="하나 고른 상태"), "하나를 골랐을 때", "하나를 켜면 나머지는 저절로 꺼집니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--accent);border-radius:50%;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></span><span style="font-size:6.5px">주 1회</span></div>', bars="", label="포커스"), "포커스를 받았을 때", "그룹 안에서는 화살표 키로 옮기고, 옮기면 바로 그 값이 골라집니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center;opacity:.45"><span style="width:9px;height:9px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:6.5px">발행하지 않음</span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">사업자만 고를 수 있음</div>', bars="", label="비활성 선택지"), "고를 수 없는 선택지가 있을 때", "선택지 하나만 고르지 못하게 막을 때는 <b>그 이유를 바로 옆에</b> 적습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--danger);border-radius:50%"></span><span style="font-size:6.5px">매일</span></div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:3px">주기를 골라 주세요</div></div>', bars="", label="필수인데 안 고름"), "필수인데 고르지 않았을 때", "에러 메시지는 칸마다 붙이지 않고 <b>그룹 아래</b>에 하나만 띄웁니다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:3px"><div style="border:1px solid var(--accent);background:var(--accent-soft);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;border:1.5px solid var(--accent);border-radius:50%"></span>주 1회</div><div style="border:1px solid var(--line-strong);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;border:1.5px solid var(--line-strong);border-radius:50%"></span>월 1회</div></div>', bars="", label="카드형 라디오"), "카드형으로 그렸을 때", "설명이 길면 선택지 둘레에 테두리를 둘러 누를 수 있는 영역을 넓힙니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그룹", "radio group · fieldset", "같은 <code>name</code>으로 묶인 라디오 버튼 전체가 하나의 부품입니다"),
    ("그룹 제목", "legend", "<b>무엇을 고르는 묶음인지</b> 적습니다. 스크린 리더가 이 제목을 먼저 읽습니다"),
    ("고른 항목", "selected option", "테두리와 배경으로도 골랐다는 것을 알립니다. 동그라미 안의 작은 점 하나만으로는 잘 보이지 않습니다"),
    ("동그란 칸", "radio", "<b>동그라미는 하나만 고른다</b>는 약속입니다. 라디오를 네모로 그리면 체크박스처럼 보여서 이 약속이 통하지 않습니다"),
    ("항목 이름", "label", "이 선택지를 고르면 무엇이 되는지 적습니다. 선택지끼리 뜻이 겹치지 않게 씁니다"),
    ("보조 설명", "description", "수수료나 주기처럼 선택지끼리 실제로 다른 점을 적습니다"),
    ("비활성 항목", "disabled option", "고를 수 없는 선택지입니다. 숨기지 말고 <b>이유가 보이게</b> 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라디오는 한 번 고르면 <b>아무것도 고르지 않은 상태로 되돌릴 방법이 없습니다.</b> 고르지 않은 상태에도 뜻이 있다면
          '선택 안 함' 같은 선택지를 직접 넣어 주거나 체크박스를 써야 합니다.</p>''',
  do=ul([
    "선택지가 <b>2~6개</b>이고 하나만 고를 때",
    "요금제나 배송 방법처럼 선택지를 <b>나란히 놓고 비교해야</b> 할 때",
    "선택지마다 설명이 붙어야 할 때. 셀렉트에는 설명을 넣을 자리가 없습니다",
  ]),
  dont=ul([
    "선택지가 일곱 개를 넘을 때. 셀렉트나 콤보박스를 씁니다",
    "여럿을 고를 수 있을 때. 체크박스를 씁니다",
    "누르는 즉시 적용될 때. 세그먼티드 컨트롤이 더 알맞습니다",
    "선택지가 둘뿐이고 켜고 끄는 뜻일 때. 스위치나 체크박스 하나로 충분합니다",
  ]),
  instead='여러 개를 고르게 하려면 <a href="checkbox.html">체크박스</a>를 쓰고, 선택지가 많으면 <a href="select.html">셀렉트</a>나 <a href="combobox.html">콤보박스</a>를 씁니다. 누르는 즉시 적용되는 값이면 <a href="segmented.html">세그먼티드</a> 컨트롤이나 <a href="switch.html">스위치</a>가 맞습니다.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1.5px solid var(--accent);border-radius:50%;display:grid;place-items:center"><span style="width:3px;height:3px;border-radius:50%;background:var(--accent)"></span></span><span style="font-size:6px">자동 발행</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:6px">직접 발행</span></div></div>', bars="", tall=False, label="기본 라디오 재현"),
     "선택지를 세로로 쌓은 기본형", "설명이 짧을 때 쓰며, 선택지를 세로로 쌓습니다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:3px"><div style="border:1px solid var(--accent);background:var(--accent-soft);border-radius:3px;padding:3px 4px;font-size:5.5px"><b>주 1회</b><div style="color:var(--fg-muted);font-size:5px">수수료 0.8%</div></div><div style="border:1px solid var(--line-strong);border-radius:3px;padding:3px 4px;font-size:5.5px"><b>월 1회</b><div style="color:var(--fg-muted);font-size:5px">수수료 0.5%</div></div></div>', bars="", tall=False, label="카드형 라디오 재현"),
     "설명이 긴 선택지를 카드로 묶기", "요금제 고르기처럼 선택지마다 설명이 길 때 씁니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:3px"><span style="flex:1;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:2px;display:flex;gap:1px"><span style="flex:1;background:var(--accent);color:#fff;border-radius:99px;font-size:5px;text-align:center;padding:2px 0">매일</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted)">주</span><span style="flex:1;font-size:5px;text-align:center;padding:2px 0;color:var(--fg-muted)">월</span></span></div>', bars="", tall=False, label="세그먼티드로 바꾼 재현"),
     "세그먼티드 컨트롤로 바꾼 모양", "같은 라디오 그룹을 가로로 붙여 놓은 모양입니다. 누르는 즉시 적용할 때 씁니다"),
  ]),
  code_lede="라디오 버튼에 같은 <code>name</code>을 주면 브라우저가 알아서 한 그룹으로 묶고 화살표 키 조작까지 처리해 줍니다. 반면 라디오를 직접 만들면 이 규칙을 모두 다시 구현해야 합니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;정산 주기&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"cycle"</span> <span class="a">value</span>=<span class="s">"daily"</span>&gt; 매일&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"cycle"</span> <span class="a">value</span>=<span class="s">"weekly"</span>&gt; 주 1회&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

<span class="c">// 같은 name 이 곧 그룹이다. 묶는 코드를 따로 쓰지 않는다</span>
form.querySelector(<span class="s">'[name=cycle]:checked'</span>).value;

<span class="c">// 안 고른 상태로 되돌리려면 직접 지워야 한다 (사용자는 못 한다)</span>
form.querySelectorAll(<span class="s">'[name=cycle]'</span>).forEach(r =&gt; r.checked = <span class="a">false</span>);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "그룹 전체를 <b>한 칸</b>으로 보고 지나갑니다. 아직 고르지 않은 그룹이면 첫 칸으로 들어갑니다"),
    ("<kbd>↑</kbd><kbd>↓</kbd><kbd>←</kbd><kbd>→</kbd>", "그룹 안에서 선택을 옮기며, <b>옮기는 즉시 그 값이 골라집니다</b>"),
    ("<kbd>Space</kbd>", "짚고 있는 선택지를 고릅니다"),
    ("라벨을 눌렀을 때", "<code>&lt;label&gt;</code>로 감싸 두면 글자를 눌러도 골라집니다"),
    ("그룹 제목을 달았을 때", "<code>&lt;legend&gt;</code>가 있어야 스크린 리더가 '무엇을 고르는지'부터 읽어 줍니다"),
  ]),
  backend=rows([
    ("라디오 값은 정해진 열거형", "라디오 값은 정해진 집합 가운데 하나입니다. 그래서 서버에서도 <code>enum</code>으로 받고, <b>목록에 없는 값은 거절</b>해야 합니다."),
    ("기본값을 미리 켜 둘 때의 문제", "기본값을 미리 켜 두면 사용자 대부분이 그대로 보냅니다. 그래서 서버가 받은 값이 편의를 위해 둔 기본값인지, <b>사용자가 확인하지 않고 넘긴 값</b>인지 구별할 수 없습니다. 돈이나 권한이 걸린 선택이면 비워 둡니다."),
    ("고르지 않은 상태로 돌아갈 수 없는 점", "라디오는 한 번 고르면 '없음'으로 돌아갈 수 없습니다. '없음'에도 뜻이 있다면 그것을 <b>선택지로 넣어야</b> 하고, 그러면 서버에도 그 값을 받을 자리가 필요합니다."),
    ("선택지가 바뀔 때", "선택지가 바뀌면 예전에 저장된 값이 지금 목록에는 없을 수 있습니다. 이때 화면이 <b>아무것도 고르지 않은 것</b>처럼 보이지 않도록, 지난 값을 어떻게 보여 줄지 정해야 합니다."),
  ]),
  plat_lede="라디오는 플랫폼이 달라도 이름과 쓰임이 잘 통하는 편입니다.",
  plats=plats([
    ("웹", "<code>&lt;input type=\"radio\"&gt;</code>",
     mini('<div style="margin-top:12px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1.5px solid var(--accent);border-radius:50%;display:grid;place-items:center"><span style="width:4px;height:4px;border-radius:50%;background:var(--accent)"></span></span><span style="font-size:6.5px">주 1회</span></div></div>', bars="", label="웹 라디오 재현"),
     "<b>라디오 버튼</b> · 같은 <code>name</code>을 준 라디오 버튼끼리 한 그룹이 됩니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="display:flex;align-items:center;padding:5px 0;border-bottom:1px solid var(--line);font-size:8px"><span style="flex:1">주 1회</span><span style="color:#0a84ff">✓</span></div><div style="display:flex;align-items:center;padding:5px 0;font-size:8px;color:var(--fg-muted)"><span style="flex:1">월 1회</span></div></div>', "iOS 체크마크 목록 재현"),
     "표준 라디오가 <b>없습니다.</b> 목록 줄에 <b>체크마크</b>를 찍어 하나만 고르게 하거나, 선택지가 적으면 <b>세그먼티드 컨트롤</b>을 씁니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:grid;gap:6px"><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;border:1.5px solid var(--accent);border-radius:50%;display:grid;place-items:center"><span style="width:5px;height:5px;border-radius:50%;background:var(--accent)"></span></span><span style="font-size:8px">주 1회</span></div><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;border:1.5px solid var(--line-strong);border-radius:50%"></span><span style="font-size:8px">월 1회</span></div></div>', "안드로이드 라디오 재현"),
     "<b>라디오 버튼</b>(Radio button) · 웹과 거의 같습니다."),
  ]),
  plat_note="iOS 에서 '하나만 고르기'는 보통 <b>체크마크가 붙는 목록</b>으로 만듭니다. 그래서 동그란 라디오를 그려 가면 iOS 쪽에서는 낯설게 봅니다. 모양이 달라도 사용자가 <b>하나만 고를 수 있다</b>는 것을 알아볼 수 있으면 됩니다.",
  siblings=siblings("radio"),
  related='''        <li><span class="na"><b>요금제 비교</b><em>13부</em></span></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><span class="na"><b>포커스 순서</b><em>12부</em></span></li>''',
)
