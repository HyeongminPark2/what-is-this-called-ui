# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div class="pin-out" data-pin="1" style="font-size:12px;font-weight:700;margin-bottom:20px">정산 알림</div>
                  <div class="pin-out" data-pin="2" style="display:flex;align-items:center;gap:40px;padding-left:26px;margin-bottom:20px">
                    <span data-pin="3" style="width:17px;height:17px;border-radius:4px;background:var(--accent);flex:none;display:grid;place-items:center;color:#fff;font-size:10px;font-weight:800">–</span>
                    <span class="pin-out" data-pin="4" style="font-size:11.5px;font-weight:600">전체 선택</span>
                  </div>
                  <div style="padding-left:26px">
                    <div class="pin-out" data-pin="5" style="display:flex;align-items:center;gap:40px;padding-left:26px;margin-bottom:18px">
                      <span style="width:17px;height:17px;border-radius:4px;background:var(--accent);flex:none;display:grid;place-items:center;color:#fff;font-size:10px;font-weight:800">✓</span>
                      <span class="pin-out" data-pin="6" style="font-size:11.5px">정산 확정 <span style="color:var(--fg-muted);font-size:10.5px">· 매주 월요일</span></span>
                    </div>
                    <div class="pin-out" data-pin="7" style="display:flex;align-items:center;gap:40px;padding-left:26px;opacity:.5">
                      <span style="width:17px;height:17px;border-radius:4px;background:var(--accent);flex:none;display:grid;place-items:center;color:#fff;font-size:10px;font-weight:800">✓</span>
                      <span style="font-size:11.5px">보안 경고</span>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="checkbox", ko="체크박스", en="Checkbox",
  desc="체크박스가 무엇인지, 라디오나 스위치와는 어떻게 다른지를 중간 상태까지 포함해 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="체크박스는 <b>여러 항목을 하나하나 따로</b> 켜고 끄는 네모 칸입니다. 항목끼리 서로 영향을 주지 않고, 보통 <b>저장을 눌러야</b> 적용됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>전체 선택을 보세요.</b> 아래 항목이 일부만 켜져 있으면 전체 선택 칸은 체크도 빈칸도 아닌 <b>세 번째 모습</b>이 됩니다.
          이 모습을 <b>중간 상태</b>(indeterminate)라고 부르며, 체크박스에만 있습니다.<br>
          칸이 아니라 글자를 눌러도 켜지는데, 라벨과 칸이 연결되어 있기 때문입니다. 누를 수 있는 영역이 그만큼 넓어져서 손가락으로 쓸 때 차이가 큽니다.</p>
        </div>''',
  names=rows([
    ("한국어", "체크박스, 확인란, 체크 상자"),
    ("영어", "checkbox"),
    ("같이 쓰는 말", "일부만 켜진 상태는 <b>중간 상태</b>(indeterminate·partial), 묶음 제목은 <b>그룹 레이블</b>(fieldset·legend)이라고 부릅니다. 항목 둘레에 테두리를 두른 모양은 <b>박스형 체크</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>스위치</b> — 스위치는 <b>누르는 즉시</b> 적용되고 저장 버튼이 없습니다. 체크박스와 특히 자주 혼동합니다.<br>"
     "<b>라디오</b> — 라디오는 묶음에서 <b>하나만</b> 고릅니다. 하나만 고르게 하려면 체크박스가 아니라 라디오를 씁니다.<br>"
     "<b>토글</b> — '토글'은 켜고 끄는 것을 두루 가리키는 말이라서, 이렇게 부르면 체크박스와 스위치를 구별할 수 없습니다."),
  ]),
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="꺼진 체크박스"), "꺼져 있을 때", "빈 네모입니다. 테두리가 또렷해야 그 자리에 체크박스가 있는 줄 압니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="켜진 체크박스"), "켜져 있을 때", "체크 표시가 나타납니다. 색만 바꿔서 알리지 않습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:7px;font-weight:800">–</span><span style="font-size:6.5px">전체 선택</span></div>', bars="", label="중간 상태"), "중간 상태", "아래 항목이 일부만 켜졌을 때의 모습으로, <b>체크박스에만 있는</b> 세 번째 상태입니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--accent);border-radius:2px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="포커스"), "포커스를 받았을 때", "키보드로 포커스가 왔을 때의 모습입니다. 포커스 링을 지우지 않습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center;opacity:.45"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">보안 경고</span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">끌 수 없는 이유를 적어 둠</div>', bars="", label="비활성"), "비활성일 때", "켠 채로 끄지 못하게 막아 두는 경우가 많은데, 그럴 때는 <b>왜 끌 수 없는지 적습니다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--danger);border-radius:2px"></span><span style="font-size:6.5px">약관에 동의</span></div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:3px">동의해야 저장됩니다</div></div>', bars="", label="필수 미동의"), "필수 항목을 켜지 않았을 때", "약관 동의처럼 꼭 켜야 하는 항목을 켜지 않은 상태입니다. 에러 메시지는 그 항목 바로 아래에 띄웁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그룹 제목", "legend · group label", "<code>&lt;fieldset&gt;</code>+<code>&lt;legend&gt;</code>로 만듭니다. 그러면 스크린 리더가 <b>무엇에 대한 묶음인지</b> 먼저 읽어 줍니다"),
    ("부모 체크", "parent checkbox", "아래 항목을 한 번에 켜고 끕니다. 아래 항목이 일부만 켜지면 <b>중간 상태</b>가 됩니다"),
    ("라벨", "label", "<b>칸과 연결해 둡니다.</b> 그러면 글자를 눌러도 켜지므로 누를 수 있는 영역이 넓어집니다"),
    ("체크 칸", "box", "칸은 18px 이상으로 그리고, 손가락으로 누르는 영역은 라벨까지 합쳐 44px 이상으로 잡습니다"),
    ("항목 이름", "item label", "켰을 때 <b>무엇이 일어나는지</b> 적습니다"),
    ("보조 설명", "description", "조건이나 빈도 같은 부가 정보를 적습니다. 이런 내용까지 라벨에 다 넣으려 하지 않습니다"),
    ("비활성 항목", "disabled", "끌 수 없는 항목입니다. 흐리게만 두지 말고 <b>이유</b>를 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          중간 상태는 <b>CSS 로는 못 만듭니다.</b> 자바스크립트에서 <code>el.indeterminate = true</code> 로만 켤 수 있고,
          값으로 보면 '켜짐'이 아니어서 폼을 보낼 때는 꺼진 것으로 처리됩니다.</p>''',
  do=ul([
    "여러 개를 <b>각각</b> 켜고 끌 때",
    "약관 동의처럼 항목이 <b>하나뿐이어도</b> 켜고 끄는 값일 때",
    "목록에서 여러 줄을 골라 한꺼번에 처리할 때",
  ]),
  dont=ul([
    "하나만 골라야 할 때. 라디오를 씁니다",
    "누르는 즉시 적용될 때. 저장 버튼 없이 바로 적용되는 설정에는 체크박스가 아니라 스위치를 씁니다",
    "선택지가 열 개 넘게 늘어설 때. 콤보박스를 쓰거나 목록을 접어 둡니다",
    "라벨 없이 칸만 둘 때. 무엇을 켜는 칸인지 알 수 없습니다",
  ]),
  instead='하나만 골라야 하면 <a href="radio.html">라디오</a>를 쓰고, 누르는 즉시 적용되는 설정이면 <a href="switch.html">스위치</a>를 씁니다. 두세 개 가운데 하나를 고르는 값이면 <a href="segmented.html">세그먼티드</a> 컨트롤이 맞고, 선택지가 많으면 <a href="combobox.html">콤보박스</a>로 걸러서 고르게 합니다.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px"></span><span style="font-size:6px">정산 확정</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:6px">입금 완료</span></div></div>', bars="", tall=False, label="목록형 체크박스 재현"),
     "한 줄에 하나씩 놓은 목록형", "가장 흔한 모습으로, 설정 화면에서 자주 봅니다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:3px"><div style="border:1px solid var(--accent);background:var(--accent-soft);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;background:var(--accent);border-radius:2px"></span>이용약관 동의</div><div style="border:1px solid var(--line-strong);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;border:1px solid var(--line-strong);border-radius:2px"></span>마케팅 수신</div></div>', bars="", tall=False, label="박스형 체크박스 재현"),
     "테두리를 두른 박스형", "항목 둘레에 테두리를 둘러 누를 수 있는 영역을 넓힙니다. 손가락으로 쓰는 화면에 알맞습니다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">–</span><span style="font-size:6px;font-weight:700">전체</span></div><div style="padding-left:12px;display:grid;gap:3px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px"></span><span style="font-size:5.5px">정산 확정</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:5.5px">입금 완료</span></div></div></div>', bars="", tall=False, label="부모 자식 체크박스 재현"),
     "전체 선택과 하위 항목", "표의 전체 선택 칸이 대표적인 예입니다. 중간 상태가 꼭 필요한 곳입니다"),
  ]),
  code_lede="네이티브 <code>&lt;input type=\"checkbox\"&gt;</code>를 쓰면 키보드 조작과 스크린 리더 지원을 따로 만들지 않아도 됩니다. 색은 <code>accent-color</code> 한 줄로 바꿉니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;정산 알림&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;
    &lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"checkbox"</span> <span class="a">name</span>=<span class="s">"notify"</span> <span class="a">value</span>=<span class="s">"settled"</span>&gt;
    정산 확정
  &lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

<span class="c">// 중간 상태는 속성이 아니라 프로퍼티다. HTML 로는 못 쓴다</span>
all.indeterminate = on &gt; <span class="a">0</span> &amp;&amp; on &lt; kids.length;

<span class="c">/* 색만 바꾼다. 직접 그리면 키보드 조작을 다시 만들어야 한다 */</span>
input[type=checkbox] <span class="a">{</span> <span class="t">accent-color</span>: var(--accent); <span class="a">}</span>''',
  keys=kbd([
    ("<kbd>Space</kbd>", "켜고 끕니다. <kbd>Enter</kbd>로는 <b>켜지지 않고</b> 폼이 제출됩니다"),
    ("<kbd>Tab</kbd>", "체크박스 <b>칸마다 한 번씩</b> 멈춥니다. 라디오 그룹 전체에서 한 번만 멈추는 것과 다릅니다"),
    ("라벨을 눌렀을 때", "<code>&lt;label&gt;</code>로 감싸 두면 글자를 눌러도 켜집니다"),
    ("여러 칸을 묶을 때", "<code>&lt;fieldset&gt;</code>+<code>&lt;legend&gt;</code>로 묶으면 스크린 리더가 묶음 제목을 먼저 읽습니다"),
    ("중간 상태를 읽을 때", "스크린 리더가 '부분 선택'으로 읽습니다. 모양만 바꾸지 말고 스크린 리더도 이 상태를 읽을 수 있게 해야 합니다"),
  ]),
  backend=rows([
    ("서로 독립인 불리언 여러 개", "체크박스 묶음은 서로 독립인 불리언 여러 개입니다. 폼으로 보내면 <b>켜진 항목만</b> 전송되고 꺼진 항목은 키 자체가 오지 않으므로, 서버는 키가 없으면 꺼진 것으로 읽어야 합니다."),
    ("중간 상태는 화면에만 있는 표시", "중간 상태인 칸은 보낼 때 꺼진 것으로 처리됩니다. <b>화면에서만 쓰는 표시</b>이므로, 서버에 '일부 선택'을 알려야 한다면 따로 설계해야 합니다."),
    ("전체 선택은 범위를 정하는 요청", "화면에 보이는 줄만 켜는 것과 조건에 맞는 <b>전부</b>를 켜는 것은 서버에 전혀 다른 요청입니다. 예를 들어 10,000건을 '전부 선택'했다면 ID를 모두 보낼지, 검색 조건을 보낼지 정해야 합니다."),
    ("약관 동의는 이력으로 남기기", "사용자가 언제 어떤 판본의 약관에 동의했는지 기록으로 남겨야 합니다. 그래서 약관 동의 체크는 불리언 하나가 아니라 <b>이력</b>으로 저장합니다."),
  ]),
  plat_lede="플랫폼마다 모양은 조금씩 달라도 쓰임과 이름은 거의 같습니다.",
  plats=plats([
    ("웹", "<code>&lt;input type=\"checkbox\"&gt;</code>",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="웹 체크박스 재현"),
     "<b>체크박스</b> · 네모 모양이 표준이고, 라벨은 칸 오른쪽에 둡니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="display:flex;align-items:center;padding:5px 0;border-bottom:1px solid var(--line);font-size:8px"><span style="flex:1">정산 확정</span><span style="color:#0a84ff">✓</span></div><div style="display:flex;align-items:center;padding:5px 0;font-size:8px;color:var(--fg-muted)"><span style="flex:1">입금 완료</span></div></div>', "iOS 체크마크 재현"),
     "표준 체크박스가 <b>없습니다.</b> 목록 줄 오른쪽에 <b>체크마크</b>를 찍는 방식(Checkmark)이 관례이고, 켜고 끄는 설정은 대부분 <b>스위치</b>로 만듭니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:grid;gap:6px"><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;background:var(--accent);border-radius:2px"></span><span style="font-size:8px">정산 확정</span></div><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;border:1.5px solid var(--line-strong);border-radius:2px"></span><span style="font-size:8px">입금 완료</span></div></div>', "안드로이드 체크박스 재현"),
     "<b>체크박스</b>(Checkbox) · 웹과 거의 같고, <b>중간 상태</b>도 표준으로 정의돼 있습니다."),
  ]),
  plat_note="iOS 에는 체크박스가 거의 없습니다. 그래서 \"체크박스로 해 주세요\"라는 요청은 iOS 에서 <b>스위치나 체크마크 목록</b>으로 바뀌는데, 스위치로 바꾸면 누르는 즉시 적용되므로 <b>저장 버튼이 할 일이 없어집니다</b>. iOS 화면을 그릴 때는 저장 버튼을 남길지, 즉시 적용으로 바꿀지를 함께 정해야 합니다.",
  siblings=siblings("checkbox"),
  related='''        <li><span class="na"><b>데이터 테이블(행 선택)</b><em>10부</em></span></li>
        <li><a href="filter.html"><b>필터와 패싯</b><em>10부</em></a></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>''',
)
