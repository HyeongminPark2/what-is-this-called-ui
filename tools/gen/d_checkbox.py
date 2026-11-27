# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
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
  desc="체크박스가 무엇이고 라디오·스위치와 어떻게 다른지, 중간 상태까지 실물과 상태와 해부도로 보여주는 항목.",
  lede="<b>여러 개를 각각</b> 켜고 끄는 네모 칸. 서로 독립이고, 보통 <b>저장을 눌러야</b> 적용됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>전체 선택을 보세요.</b> 일부만 켜져 있을 때는 체크도 빈칸도 아닌 <b>세 번째 모습</b>이 됩니다 —
          <b>중간 상태</b>(indeterminate)라 부르고, 체크박스에만 있습니다.<br>
          글자 아무 데나 눌러도 켜집니다. 라벨과 칸이 이어져 있기 때문이고, 손가락으로 쓸 때 큰 차이가 납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "체크박스, 확인란, 체크 상자"),
    ("영어", "checkbox"),
    ("같이 쓰는 말", "일부만 켜진 상태를 <b>중간 상태</b>(indeterminate·partial), 묶음 제목을 <b>그룹 레이블</b>(fieldset·legend)이라 합니다. 테두리를 두른 꼴은 <b>박스형 체크</b>."),
    ("자주 잘못 부름",
     "<b>스위치</b> — 스위치는 <b>누르는 즉시</b> 적용되고 저장 버튼이 없습니다. 가장 잦은 혼동입니다.<br>"
     "<b>라디오</b> — 라디오는 <b>하나만</b> 고릅니다. 하나만 고르게 할 거면 체크박스를 쓰면 안 됩니다.<br>"
     "<b>토글</b> — '토글'은 켜고 끄는 모든 것을 뭉뚱그린 말이라 가려지지 않습니다."),
  ]),
  axes=ax("체크박스"),
  oneline="체크박스는 <b>여럿을 각각</b> 고르는 것이고, <b>저장을 눌러야</b> 적용됩니다. 즉시 적용이면 스위치, 하나만이면 라디오입니다.",
  states=states([
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="꺼진 체크박스"), "끔", "빈 네모. 테두리가 또렷해야 있는 줄 안다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="켜진 체크박스"), "켬", "체크 표시. 색만으로 알리지 않는다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:7px;font-weight:800">–</span><span style="font-size:6.5px">전체 선택</span></div>', bars="", label="중간 상태"), "중간 상태", "일부만 켜짐. <b>체크박스에만 있는</b> 세 번째 모습"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--accent);border-radius:2px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="포커스"), "포커스", "키보드로 왔을 때. 링을 지우지 않는다"),
    (mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center;opacity:.45"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">보안 경고</span></div><div style="position:absolute;left:6px;bottom:6px;font-size:5.5px;color:var(--fg-muted)">끌 수 없음 — 이유를 적을 것</div>', bars="", label="비활성"), "비활성", "켠 채로 못 끄게 하는 일이 많다. <b>왜인지 적는다</b>"),
    (mini('<div style="margin-top:12px;padding:0 6px"><div style="display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;border:1px solid var(--danger);border-radius:2px"></span><span style="font-size:6.5px">약관에 동의</span></div><div style="font-size:5.5px;color:var(--danger);font-weight:700;margin-top:3px">동의해야 저장됩니다</div></div>', bars="", label="필수 미동의"), "필수인데 안 켬", "약관처럼 꼭 켜야 하는 것. 에러는 그 자리에"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그룹 제목", "legend · group label", "<code>&lt;fieldset&gt;</code>+<code>&lt;legend&gt;</code>. 스크린 리더가 <b>무엇에 대한 묶음인지</b> 먼저 읽어 준다"),
    ("부모 체크", "parent checkbox", "아래를 한 번에 켜고 끈다. 일부만 켜지면 <b>중간 상태</b>가 된다"),
    ("라벨", "label", "<b>칸과 이어 둔다.</b> 글자를 눌러도 켜져서 과녁이 몇 배 커진다"),
    ("체크 칸", "box", "최소 18px. 손가락 과녁은 라벨까지 합쳐 44px 이상"),
    ("항목 이름", "item label", "켰을 때 <b>무엇이 일어나는지</b>를 적는다"),
    ("보조 설명", "description", "조건이나 빈도. 라벨에 다 넣으려 하지 않는다"),
    ("비활성 항목", "disabled", "못 끄는 것. 흐리게만 두지 말고 <b>이유</b>를 적는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          중간 상태는 <b>CSS 로는 못 만듭니다.</b> <code>el.indeterminate = true</code> 로 자바스크립트에서만 켤 수 있고,
          값으로는 '켜짐'이 아닙니다 — 보내질 때는 꺼진 것으로 갑니다.</p>''',
  do=ul([
    "여러 개를 <b>각각</b> 켜고 끌 때",
    "약관 동의처럼 <b>하나만 있어도</b> 켜고 끄는 것일 때",
    "목록에서 여러 줄을 골라 한꺼번에 처리할 때",
  ]),
  dont=ul([
    "하나만 골라야 할 때 → 라디오",
    "누르는 즉시 적용될 때 → 스위치. 저장 버튼이 없으면 체크박스가 아닙니다",
    "선택지가 열 개 넘게 늘어설 때 → 콤보박스나 접어 두기",
    "라벨 없이 칸만 두기 — 무엇을 켜는지 알 수 없습니다",
  ]),
  instead='하나만 고르면 <a href="radio.html">라디오</a>, 즉시 적용이면 <a href="switch.html">스위치</a>, 둘셋 중 하나면 <a href="segmented.html">세그먼티드</a>, 많으면 <a href="combobox.html">콤보박스</a>.',
  cases=cases([
    (mini('<div style="margin-top:10px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px"></span><span style="font-size:6px">정산 확정</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:6px">입금 완료</span></div></div>', bars="", tall=False, label="목록형 체크박스 재현"),
     "목록형", "가장 흔한 모습. 설정 화면에서 자주 본다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:3px"><div style="border:1px solid var(--accent);background:var(--accent-soft);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;background:var(--accent);border-radius:2px"></span>이용약관 동의</div><div style="border:1px solid var(--line-strong);border-radius:3px;padding:3px 4px;font-size:5.5px;display:flex;gap:3px"><span style="width:7px;height:7px;border:1px solid var(--line-strong);border-radius:2px"></span>마케팅 수신</div></div>', bars="", tall=False, label="박스형 체크박스 재현"),
     "박스형", "테두리를 둘러 과녁을 키운다. 손가락으로 쓸 때 좋다"),
    (mini('<div style="margin-top:8px;padding:0 6px;display:grid;gap:4px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">–</span><span style="font-size:6px;font-weight:700">전체</span></div><div style="padding-left:12px;display:grid;gap:3px"><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;background:var(--accent);border-radius:2px"></span><span style="font-size:5.5px">정산 확정</span></div><div style="display:flex;gap:4px;align-items:center"><span style="width:8px;height:8px;border:1px solid var(--line-strong);border-radius:2px"></span><span style="font-size:5.5px">입금 완료</span></div></div></div>', bars="", tall=False, label="부모 자식 체크박스 재현"),
     "부모 · 자식", "표의 전체 선택이 대표적. 중간 상태가 꼭 필요한 자리"),
  ]),
  code_lede="네이티브 <code>&lt;input type=\"checkbox\"&gt;</code>를 쓰면 키보드와 스크린 리더가 공짜입니다. <code>accent-color</code> 한 줄로 색만 바꿉니다.",
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
    ("<kbd>Space</kbd>", "켜고 끈다. <kbd>Enter</kbd>는 <b>안 먹는다</b>(폼을 보낸다)"),
    ("<kbd>Tab</kbd>", "<b>칸마다 한 번씩</b> 지난다. 라디오 그룹이 한 번인 것과 다르다"),
    ("라벨 누름", "<code>&lt;label&gt;</code>로 감싸 두면 글자를 눌러도 켜진다"),
    ("그룹", "<code>&lt;fieldset&gt;</code>+<code>&lt;legend&gt;</code>로 묶으면 묶음 제목이 먼저 읽힌다"),
    ("중간 상태", "스크린 리더가 '부분 선택'으로 읽는다. 눈으로만 알리면 안 된다"),
  ]),
  backend=rows([
    ("체크박스 = 비트 집합", "서로 독립인 불리언 여럿입니다. 폼으로 보내면 <b>켜진 것만</b> 옵니다 — 꺼진 것은 키 자체가 안 와서, 서버는 '없음 = 꺼짐'으로 읽어야 합니다."),
    ("중간 상태는 값이 아니다", "보낼 때는 꺼진 것으로 갑니다. <b>화면에서만 쓰는 표시</b>라 서버에 '부분'을 보내려면 따로 설계해야 합니다."),
    ("전체 선택 = 범위 연산", "보이는 것만 켜는지, 조건에 맞는 <b>전부</b>를 켜는지는 전혀 다른 요청입니다. 10,000건을 '전부 선택'했을 때 ID 를 다 보낼지 조건을 보낼지 정해야 합니다."),
    ("약관 동의 = 감사 기록", "언제 어떤 판본에 동의했는지를 남겨야 합니다. 체크 하나가 불리언이 아니라 <b>이력</b>이 됩니다."),
  ]),
  plat_lede="모양은 조금씩 달라도 쓰임과 이름은 거의 같습니다.",
  plats=plats([
    ("웹", "<code>&lt;input type=\"checkbox\"&gt;</code>",
     mini('<div style="margin-top:12px;padding:0 6px;display:flex;gap:4px;align-items:center"><span style="width:9px;height:9px;background:var(--accent);border-radius:2px;display:grid;place-items:center;color:#fff;font-size:6px;font-weight:800">✓</span><span style="font-size:6.5px">정산 확정</span></div>', bars="", label="웹 체크박스 재현"),
     "<b>체크박스</b> · 네모가 표준이고, 라벨은 오른쪽입니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="display:flex;align-items:center;padding:5px 0;border-bottom:1px solid var(--line);font-size:8px"><span style="flex:1">정산 확정</span><span style="color:#0a84ff">✓</span></div><div style="display:flex;align-items:center;padding:5px 0;font-size:8px;color:var(--fg-muted)"><span style="flex:1">입금 완료</span></div></div>', "iOS 체크마크 재현"),
     "표준 체크박스가 <b>없습니다.</b> 목록 줄 오른쪽에 <b>체크마크</b>를 찍는 방식(Checkmark)이 관례이고, 켜고 끄는 설정은 거의 <b>스위치</b>로 풉니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px;display:grid;gap:6px"><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;background:var(--accent);border-radius:2px"></span><span style="font-size:8px">정산 확정</span></div><div style="display:flex;gap:5px;align-items:center"><span style="width:10px;height:10px;border:1.5px solid var(--line-strong);border-radius:2px"></span><span style="font-size:8px">입금 완료</span></div></div>', "안드로이드 체크박스 재현"),
     "<b>체크박스</b>(Checkbox) · 웹과 거의 같고, <b>중간 상태</b>도 표준으로 정의돼 있습니다."),
  ]),
  plat_note="iOS 에는 체크박스가 없다시피 합니다. 그래서 \"체크박스로 해 주세요\"가 iOS 쪽에는 <b>스위치나 체크마크 목록</b>으로 바뀌는데, 스위치로 바뀌면 <b>즉시 적용</b>이 되어 저장 버튼의 뜻이 사라집니다. 바꿔 그릴 때 그 점을 같이 정해야 합니다.",
  siblings=siblings("checkbox"),
  related='''        <li><span class="na"><b>데이터 테이블(행 선택)</b><em>10부</em></span></li>
        <li><span class="na"><b>필터와 패싯</b><em>10부</em></span></li>
        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
