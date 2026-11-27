# -*- coding: utf-8 -*-
from parts import *
from ax4 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px 26px 18px">
                  <div style="display:flex;align-items:baseline;gap:40px;margin-bottom:12px">
                    <span class="pin-out" data-pin="1" style="font-size:12px;font-weight:700">업무용 메일</span>
                    <span data-pin="2" style="color:var(--danger);font-size:12px;font-weight:700">*</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="border:1px solid var(--danger);border-radius:5px;padding:9px 11px;box-shadow:0 0 0 3px color-mix(in srgb,var(--danger) 16%,transparent);margin-bottom:12px">
                    <span class="pin-tr" data-pin="4" style="font-size:11.5px;color:var(--fg-faint)">name@company.com</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-size:11px;color:var(--danger);font-weight:600;margin-bottom:12px">메일 주소 형태가 아닙니다.</div>
                  <div class="pin-out" data-pin="6" style="font-size:11px;color:var(--fg-muted)">정산 안내를 이 주소로 보냅니다.</div>
                </div>
              </div>'''

D = dict(
  slug="field", ko="텍스트 필드", en="Text field · Input",
  desc="텍스트 필드가 무엇인지, 라벨과 자리글, 헬퍼 텍스트, 에러 메시지가 서로 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="텍스트 필드는 사용자가 글자를 직접 입력하는 칸입니다. 칸 자체보다 <b>칸 둘레에 붙는 요소</b>(라벨·헬퍼 텍스트·에러 메시지)가 쓰기 편한지를 더 크게 좌우하고, 잘못 만드는 경우도 이쪽이 더 많습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>칸을 비운 채 등록하기를 눌러 보세요.</b> 포커스가 첫 번째로 틀린 칸으로 옮겨 갑니다.
          그 칸을 고치기 시작하면 등록하기를 다시 누르지 않아도 에러 표시가 <b>바로</b> 풀립니다.<br>
          위의 체크를 켜면 라벨이 사라지고 자리글만 남는데, 이 상태에서 글자를 입력하기 시작하면 자리글마저 사라져서 <b>무엇을 적는 칸이었는지 알 수 없게 됩니다.</b>
          그래서 자리글은 라벨을 대신할 수 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "텍스트 필드, 입력칸, 인풋"),
    ("영어", "text field, text input, input"),
    ("같이 쓰는 말", "칸 위에 붙는 이름은 <b>라벨</b>, 칸 안에 흐리게 적힌 안내는 <b>자리글</b>(placeholder), 칸 아래 설명은 <b>헬퍼 텍스트</b>라고 부릅니다. 여러 줄을 입력하는 칸은 <b>텍스트에어리어</b>, 칸 앞뒤에 붙는 단위(₩·@)는 <b>어픽스</b>(affix)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>자리글을 라벨이라 부르기</b> — 특히 자주 일어나고 문제도 큰 혼동입니다. 자리글은 입력을 시작하면 사라지기 때문에 라벨 역할을 할 수 없습니다.<br>"
     "<b>힌트</b> — 헬퍼 텍스트는 '힌트'가 아니라 칸 아래에 <b>늘 보이는 설명</b>입니다.<br>"
     "<b>폼</b> — 폼은 여러 칸을 모은 입력 양식 전체이고, 필드는 그 안의 칸 하나입니다."),
  ]),
  axes=ax("텍스트 필드"),
  oneline="텍스트 필드를 잘 만들었는지는 <b>칸 바깥</b>을 보면 알 수 있습니다. 라벨이 늘 보이는지, 설명이 입력하기 전에 보이는지, 에러 메시지가 고쳐야 할 칸 바로 옆에 붙는지를 확인합니다.",
  states=states([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px"></div></div>', bars="", label="기본 상태"), "기본", "라벨은 <b>늘 보여야</b> 합니다. 라벨 없이 자리글만 두지 않습니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--accent);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></div></div>', bars="", label="포커스 상태"), "포커스", "포커스 링을 지우지 않습니다. 키보드로 쓰는 사람은 포커스 링을 보고 지금 어느 칸에 있는지 압니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">gildong@example.com</div></div>', bars="", label="값이 든 상태"), "채움", "값을 입력해도 라벨은 사라지지 않습니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--danger);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--danger) 18%,transparent)"></div><div style="font-size:6px;color:var(--danger);font-weight:700;margin-top:2px">형태가 아닙니다</div></div>', bars="", label="에러 상태"), "에러", "테두리 색만으로 알리지 않고, 무엇이 틀렸는지 <b>글로 적습니다</b>"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px;color:var(--fg-faint)">사업자번호</div><div style="height:12px;border:1px dashed var(--line-strong);border-radius:3px;background:var(--bg)"></div><div style="font-size:6px;color:var(--fg-muted);margin-top:2px">읽기 전용</div></div>', bars="", label="읽기 전용"), "읽기 전용", "값을 읽고 복사할 수는 있지만 고칠 수는 없습니다"),
    (mini('<div style="margin-top:9px;padding:0 6px;opacity:.45"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;background:var(--bg)"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:6px;color:var(--fg-muted)">왜 못 쓰는지 적어 둘 것</div>', bars="", label="비활성"), "비활성", "왜 쓸 수 없는지 <b>이유를 적지 않으면</b> 사용자는 다음에 무엇을 해야 할지 알 수 없습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("라벨", "label", "<b>늘 보이게</b> 둡니다. <code>&lt;label for&gt;</code>로 칸과 연결해 두면 라벨 글자를 눌러도 칸으로 포커스가 갑니다"),
    ("필수 표시", "required marker", "필수 칸마다 별표를 다는 방식만 고집하지 말고, 필수와 선택 중 <b>어느 쪽이 적은지</b> 보고 적은 쪽에 표시합니다. 대부분이 필수라면 선택 칸에 '선택'이라고 적는 편이 낫습니다"),
    ("입력칸", "input", "손가락으로도 정확히 누를 수 있도록 높이를 44px 이상으로 잡습니다"),
    ("자리글", "placeholder", "입력값의 <b>예시</b>를 적는 자리입니다. 설명을 여기에 넣으면 입력을 시작하는 순간 사라집니다"),
    ("에러 메시지", "error", "무엇이 틀렸는지와 <b>어떻게 고치면 되는지</b>까지 적어 칸 바로 아래에 둡니다"),
    ("헬퍼 텍스트", "helper text", "입력하기 전에 알아야 할 내용을 적습니다. <b>에러 메시지가 떠도 사라지지 않습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라벨을 칸 안에 두었다가 입력을 시작하면 칸 위쪽으로 올리는 방식(<b>플로팅 라벨</b>)도 있습니다. 세로 공간을 아낄 수 있지만,
          값이 들어오면 라벨이 작아져 읽기 어렵고, 빈 칸에서는 라벨이 자리글 자리에 들어가 있으므로 자리글을 함께 쓸 수 없습니다.</p>''',
  do=ul([
    "이름, 주소, 메모처럼 자유롭게 적어야 하는 값을 받을 때",
    "선택지가 너무 많아 늘어놓을 수 없을 때",
    "형식이 정해진 값을 받으면서 <code>inputmode</code>로 폰 키보드 종류를 맞춰 줄 때",
  ]),
  dont=ul([
    "선택지가 정해져 있을 때. 셀렉트나 라디오, 콤보박스를 씁니다",
    "자리글로 라벨을 대신할 때. 자리글은 입력을 시작하면 사라집니다",
    "형식을 알려 주지 않고 틀렸다고만 할 때. 헬퍼 텍스트로 형식을 <b>미리</b> 알립니다",
    "입력하는 도중에 글자를 마음대로 바꿀 때. 커서 위치가 갑자기 바뀌어 고치기 어려워집니다",
  ]),
  instead='정해진 것 중 하나면 <a href="select.html">셀렉트</a>, 많아서 걸러야 하면 <a href="combobox.html">콤보박스</a>, 범위에서 고르면 <a href="slider.html">슬라이더</a>, 켜고 끄면 <a href="switch.html">스위치</a>.',
  cases=cases([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">금액</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center"><span style="padding:0 3px;background:var(--bg);font-size:6px;border-right:1px solid var(--line)">₩</span><span style="font-size:6px;padding-left:3px">48,000</span></div></div>', bars="", tall=False, label="어픽스 재현"),
     "어픽스", "단위를 칸 안에 붙여 두면 사용자가 ₩를 직접 입력하지 않아도 됩니다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">메모</div><div style="height:20px;border:1px solid var(--line-strong);border-radius:3px"></div><div style="font-size:5.5px;color:var(--fg-muted);text-align:right;margin-top:2px">12 / 80</div></div>', bars="", tall=False, label="글자 수 재현"),
     "글자 수", "글자 수에 상한이 있으면 지금 몇 자인지 보여 줍니다. 다 쓰고 난 뒤에 잘리는 것보다 미리 아는 편이 낫습니다"),
    (mini('<div style="margin-top:12px;padding:0 6px;position:relative"><div style="height:16px;border:1px solid var(--accent);border-radius:3px"></div><div style="position:absolute;left:9px;top:14px;font-size:5px;color:var(--accent);font-weight:700;background:var(--surface);padding:0 2px">업무용 메일</div></div>', bars="", tall=False, label="플로팅 라벨 재현"),
     "플로팅 라벨", "자리를 아낄 수 있지만 라벨 글자가 작아지고 자리글을 함께 쓸 수 없습니다"),
  ]),
  code_lede="텍스트 필드의 접근성은 대부분 두 가지로 해결됩니다. <code>&lt;label for&gt;</code>로 라벨을 칸에 연결하고, <code>aria-describedby</code>로 헬퍼 텍스트와 에러 메시지를 칸에 연결합니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"em"</span>&gt;업무용 메일 &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;*&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"em"</span> <span class="a">type</span>=<span class="s">"email"</span> <span class="a">required</span>
       <span class="a">inputmode</span>=<span class="s">"email"</span> <span class="a">autocomplete</span>=<span class="s">"email"</span>
       <span class="a">aria-describedby</span>=<span class="s">"em-h"</span> <span class="a">placeholder</span>=<span class="s">"name@company.com"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"em-h"</span>&gt;정산 안내를 이 주소로 보냅니다.&lt;/<span class="t">p</span>&gt;

<span class="c">// 틀렸을 때는 에러 설명을 잇고 invalid 를 켠다</span>
el.setAttribute(<span class="s">'aria-invalid'</span>, <span class="s">'true'</span>);
el.setAttribute(<span class="s">'aria-describedby'</span>, <span class="s">'em-h em-e'</span>);

<span class="c">// 보내기를 기다리지 말고 고쳐지는 즉시 풀어 준다</span>
el.addEventListener(<span class="s">'input'</span>, () =&gt; <span class="a">{</span> <span class="a">if</span> (ok(el)) clearError(el); <span class="a">}</span>);''',
  keys=kbd([
    ("라벨 누름", "<code>for</code>로 연결해 두었다면 칸으로 포커스가 갑니다. 라벨까지 누를 수 있는 영역이 되므로 손가락으로 누를 곳이 넓어집니다"),
    ("<kbd>Tab</kbd>", "칸을 차례로 옮겨 갑니다. 이 순서는 화면에 보이는 순서와 같아야 합니다"),
    ("보낼 때", "<b>첫 번째로 틀린 칸에 포커스를 옮깁니다</b>"),
    ("<code>autocomplete</code>", "브라우저가 저장해 둔 값을 채워 줍니다. 이 속성을 적지 않으면 자동 채움이 제대로 동작하지 않습니다"),
    ("<code>inputmode</code>", "폰에서 뜨는 키보드 종류를 고릅니다. 숫자를 넣는 칸에 글자 키보드가 뜨면 사용자가 키보드를 직접 바꿔야 합니다"),
  ]),
  backend=rows([
    ("화면 검증 = 빠른 실패", "화면에서 하는 검증은 서버 검증을 대신하지 않습니다. 서버까지 갔다 오지 않고 틀린 값을 일찍 걸러 내려는 장치이므로, 같은 값을 <b>서버에서 다시 검증해야</b> 합니다."),
    ("<code>maxlength</code> = 스키마", "입력칸의 글자 수 상한은 DB 컬럼 길이와 맞아야 합니다. 둘이 어긋나면 서버에서 값이 잘리거나 저장 오류가 납니다."),
    ("정규화 시점", "공백을 지우거나 대소문자를 통일하는 처리는 입력하는 도중이 아니라 <b>보낼 때</b> 합니다. 입력 중에 글자를 바꾸면 커서 위치가 갑자기 바뀌기 때문입니다."),
    ("<code>autocomplete</code> = 표준 필드 이름", "<code>autocomplete</code> 값은 브라우저가 알아듣도록 표준으로 정해 둔 이름입니다. 표준 이름 대신 필드 이름을 임의로 지어 쓰면 자동 채움이 동작하지 않습니다."),
  ]),
  plat_lede="입력칸 자체는 플랫폼마다 비슷하고, <b>라벨을 어디에 두는지</b>가 다릅니다.",
  plats=plats([
    ("웹", "<code>&lt;input&gt;</code>",
     mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px"></div></div>', bars="", label="웹 텍스트 필드 재현"),
     "<b>텍스트 필드</b> · 라벨을 <b>칸 위</b>에 두는 방식이 가장 흔합니다. 값을 입력해도 라벨이 가려지지 않아 안전합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="display:flex;align-items:center;gap:6px;border-bottom:1px solid var(--line);padding:5px 0"><span style="font-size:8px;color:var(--fg-muted);width:40px">메일</span><span style="font-size:8px;color:var(--fg-faint)">name@…</span></div></div>', "iOS 텍스트 필드 재현"),
     "<b>텍스트 필드</b>(Text field) · 설정 화면에서는 라벨을 <b>왼쪽에</b> 두고 값을 오른쪽에 두는 줄 형태가 많습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="border:1px solid var(--line-strong);border-radius:4px;padding:8px 6px 4px;position:relative"><span style="position:absolute;top:-4px;left:5px;background:var(--surface);padding:0 3px;font-size:6px;color:var(--accent)">메일</span><span style="font-size:7px;color:var(--fg-faint)">name@…</span></div><div style="font-size:6px;color:var(--fg-muted);margin-top:3px">정산 안내를 보냅니다</div></div>', "안드로이드 텍스트 필드 재현"),
     "<b>텍스트 필드</b> · 라벨이 <b>테두리 선 위로 올라가 걸리는</b> 모양이 표준이고, 칸 아래 설명은 <b>서포팅 텍스트</b>라고 부릅니다."),
  ]),
  plat_note="안드로이드에서 라벨은 기본적으로 <b>칸 안에 있다가 입력을 시작하면 위로 올라가는</b> 방식입니다. 그래서 \"라벨을 칸 위에 놓아 주세요\"라는 요청은 안드로이드 디자이너에게 표준에서 벗어난 요구가 됩니다. 어느 방식을 쓰든 <b>값이 들어와도 라벨이 보인다</b>는 조건만 지키면 됩니다.",
  siblings=siblings("field"),
  related='''        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>
        <li><span class="na"><b>헬퍼 텍스트 문구</b><em>14부</em></span></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
