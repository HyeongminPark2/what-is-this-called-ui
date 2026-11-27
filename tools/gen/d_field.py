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
  desc="텍스트 필드가 무엇이고 라벨·자리글·헬퍼 텍스트·에러가 어떻게 다른지 실물과 상태와 해부도로 보여주는 항목.",
  lede="글자를 직접 넣는 칸. 칸 자체보다 <b>둘레에 붙는 것들</b>(라벨·헬퍼·에러)이 더 중요하고, 더 자주 틀립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>빈칸으로 등록하기를 눌러 보세요.</b> 첫 번째 틀린 칸으로 포커스가 갑니다.
          고치기 시작하면 <b>보내기 전에</b> 에러가 풀립니다.<br>
          위의 체크를 켜면 라벨이 사라지고 자리글만 남습니다 — <b>입력을 시작하는 순간 무슨 칸이었는지 사라집니다.</b>
          자리글은 라벨을 대신할 수 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "텍스트 필드, 입력칸, 인풋"),
    ("영어", "text field, text input, input"),
    ("같이 쓰는 말", "위에 붙는 이름이 <b>라벨</b>, 칸 안의 흐린 안내가 <b>자리글</b>(placeholder), 아래 설명이 <b>헬퍼 텍스트</b>, 여러 줄짜리는 <b>텍스트에어리어</b>. 앞뒤에 붙는 단위(₩·@)는 <b>어픽스</b>(affix)."),
    ("자주 잘못 부름",
     "<b>자리글을 라벨이라 부르기</b> — 가장 잦고 가장 해로운 혼동입니다. 자리글은 입력하면 사라집니다.<br>"
     "<b>힌트</b> — 헬퍼 텍스트는 '힌트'가 아니라 <b>늘 보이는 설명</b>입니다.<br>"
     "<b>폼</b> — 폼은 칸들을 모은 전체이고, 필드는 그중 하나입니다."),
  ]),
  axes=ax("텍스트 필드"),
  oneline="텍스트 필드의 설계는 <b>칸 바깥</b>에 있습니다 — 라벨이 늘 보이는가, 설명이 입력 전에 보이는가, 에러가 고칠 곳 옆에 붙는가.",
  states=states([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px"></div></div>', bars="", label="기본 상태"), "기본", "라벨은 <b>늘 보인다</b>. 자리글만 두지 않는다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--accent);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)"></div></div>', bars="", label="포커스 상태"), "포커스", "포커스 링을 지우지 않는다. 키보드로 쓰는 사람의 전부다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center;padding:0 3px;font-size:6px">gildong@example.com</div></div>', bars="", label="값이 든 상태"), "채움", "값이 들어도 라벨이 안 사라진다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--danger);border-radius:3px;box-shadow:0 0 0 2px color-mix(in srgb,var(--danger) 18%,transparent)"></div><div style="font-size:6px;color:var(--danger);font-weight:700;margin-top:2px">형태가 아닙니다</div></div>', bars="", label="에러 상태"), "에러", "테두리 색만으로 알리지 않는다. <b>글로 적는다</b>"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px;color:var(--fg-faint)">사업자번호</div><div style="height:12px;border:1px dashed var(--line-strong);border-radius:3px;background:var(--bg)"></div><div style="font-size:6px;color:var(--fg-muted);margin-top:2px">읽기 전용</div></div>', bars="", label="읽기 전용"), "읽기 전용", "값은 읽히고 복사도 된다. 못 고칠 뿐"),
    (mini('<div style="margin-top:9px;padding:0 6px;opacity:.45"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;background:var(--bg)"></div></div><div style="position:absolute;left:6px;bottom:6px;font-size:6px;color:var(--fg-muted)">왜 못 쓰는지 적어 둘 것</div>', bars="", label="비활성"), "비활성", "<b>이유를 안 적으면</b> 사용자는 막힌 채 끝난다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("라벨", "label", "<b>늘 보인다.</b> <code>&lt;label for&gt;</code>로 칸과 이어 두면 글자를 눌러도 포커스가 간다"),
    ("필수 표시", "required marker", "별표만 두지 말고 <b>어느 쪽이 적은지</b>로 고른다 — 대부분 필수면 '선택'을 적는 게 낫다"),
    ("입력칸", "input", "높이를 44px 이상으로. 손가락이 닿아야 한다"),
    ("자리글", "placeholder", "<b>예시</b>를 적는 자리다. 설명을 여기 넣으면 입력하는 순간 사라진다"),
    ("에러 메시지", "error", "무엇이 틀렸고 <b>어떻게 고치는지</b>까지. 칸 바로 아래"),
    ("헬퍼 텍스트", "helper text", "입력 전에 알아야 하는 것. <b>에러가 떠도 안 사라진다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라벨을 칸 안에 띄워 두는 방식(<b>플로팅 라벨</b>)도 있습니다. 자리를 아끼지만
          값이 들어오면 라벨이 작아져 읽기 어려워지고, 자리글을 같이 쓸 수 없습니다.</p>''',
  do=ul([
    "자유롭게 적어야 하는 값 — 이름, 주소, 메모",
    "선택지가 너무 많아 늘어놓을 수 없을 때",
    "형식이 정해진 값 — <code>inputmode</code>로 폰 키보드를 맞춰 줄 때",
  ]),
  dont=ul([
    "선택지가 정해져 있을 때 → 셀렉트·라디오·콤보박스",
    "자리글로 라벨을 대신하기 — 입력하면 사라집니다",
    "형식을 안 알려 주고 틀렸다고만 하기 — 헬퍼 텍스트로 <b>미리</b> 알립니다",
    "입력 중에 글자를 마음대로 바꾸기 — 커서가 튀어 고치기 어려워집니다",
  ]),
  instead='정해진 것 중 하나면 <a href="select.html">셀렉트</a>, 많아서 걸러야 하면 <a href="combobox.html">콤보박스</a>, 범위에서 고르면 <a href="slider.html">슬라이더</a>, 켜고 끄면 <a href="switch.html">스위치</a>.',
  cases=cases([
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">금액</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px;display:flex;align-items:center"><span style="padding:0 3px;background:var(--bg);font-size:6px;border-right:1px solid var(--line)">₩</span><span style="font-size:6px;padding-left:3px">48,000</span></div></div>', bars="", tall=False, label="어픽스 재현"),
     "어픽스", "단위를 칸 안에 붙여 둔다. 사용자가 ₩를 안 쳐도 된다"),
    (mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">메모</div><div style="height:20px;border:1px solid var(--line-strong);border-radius:3px"></div><div style="font-size:5.5px;color:var(--fg-muted);text-align:right;margin-top:2px">12 / 80</div></div>', bars="", tall=False, label="글자 수 재현"),
     "글자 수", "상한이 있으면 보여 준다. 다 쓰고 잘리는 것보다 낫다"),
    (mini('<div style="margin-top:12px;padding:0 6px;position:relative"><div style="height:16px;border:1px solid var(--accent);border-radius:3px"></div><div style="position:absolute;left:9px;top:14px;font-size:5px;color:var(--accent);font-weight:700;background:var(--surface);padding:0 2px">업무용 메일</div></div>', bars="", tall=False, label="플로팅 라벨 재현"),
     "플로팅 라벨", "자리를 아끼지만 라벨이 작아지고 자리글을 못 쓴다"),
  ]),
  code_lede="<code>&lt;label for&gt;</code>와 <code>aria-describedby</code> 두 줄이 이 부품의 접근성 거의 전부입니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"em"</span>&gt;업무용 메일 &lt;<span class="t">span</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;*&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"em"</span> <span class="a">type</span>=<span class="s">"email"</span> <span class="a">required</span>
       <span class="a">inputmode</span>=<span class="s">"email"</span> <span class="a">autocomplete</span>=<span class="s">"email"</span>
       <span class="a">aria-describedby</span>=<span class="s">"em-h"</span> <span class="a">placeholder</span>=<span class="s">"name@company.com"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"em-h"</span>&gt;정산 안내를 이 주소로 보냅니다.&lt;/<span class="t">p</span>&gt;

<span class="c">// 틀렸을 때 — 설명을 잇고 invalid 를 켠다</span>
el.setAttribute(<span class="s">'aria-invalid'</span>, <span class="s">'true'</span>);
el.setAttribute(<span class="s">'aria-describedby'</span>, <span class="s">'em-h em-e'</span>);

<span class="c">// 보내기를 기다리지 말고 고쳐지는 즉시 풀어 준다</span>
el.addEventListener(<span class="s">'input'</span>, () =&gt; <span class="a">{</span> <span class="a">if</span> (ok(el)) clearError(el); <span class="a">}</span>);''',
  keys=kbd([
    ("라벨 누름", "<code>for</code>로 이어 뒀으면 칸으로 포커스가 간다. 손가락 과녁이 몇 배 커진다"),
    ("<kbd>Tab</kbd>", "칸을 차례로 지난다. 순서는 화면에 보이는 순서와 같아야 한다"),
    ("보낼 때", "<b>첫 번째 틀린 칸으로 포커스를 옮긴다</b>"),
    ("<code>autocomplete</code>", "브라우저가 저장해 둔 값을 채워 준다. 안 적으면 그 편의가 통째로 사라진다"),
    ("<code>inputmode</code>", "폰에서 뜨는 키보드를 고른다. 숫자 칸에 글자 키보드가 뜨면 바로 성가시다"),
  ]),
  backend=rows([
    ("화면 검증 = 빠른 실패", "서버 검증을 대신하지 않습니다. 왕복을 아끼는 캐시일 뿐이라 <b>서버에서 또 검증해야</b> 합니다."),
    ("<code>maxlength</code> = 스키마", "칸의 상한은 DB 컬럼 길이와 맞아야 합니다. 어긋나면 서버에서 잘리거나 터집니다."),
    ("정규화 시점", "공백 제거·대소문자 통일은 <b>보낼 때</b> 하지 입력 중에 하지 않습니다. 입력 중에 바꾸면 커서가 튑니다."),
    ("<code>autocomplete</code> = 표준 필드 이름", "브라우저와 합의된 이름입니다. 폼 필드 이름을 멋대로 지으면 자동 채움이 안 먹습니다."),
  ]),
  plat_lede="칸 자체는 비슷하고, <b>라벨을 어디 두느냐</b>가 갈립니다.",
  plats=plats([
    ("웹", "<code>&lt;input&gt;</code>",
     mini('<div style="margin-top:9px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">업무용 메일</div><div style="height:12px;border:1px solid var(--line-strong);border-radius:3px"></div></div>', bars="", label="웹 텍스트 필드 재현"),
     "<b>텍스트 필드</b> · 라벨을 <b>칸 위</b>에 두는 것이 가장 흔하고 가장 안전합니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="display:flex;align-items:center;gap:6px;border-bottom:1px solid var(--line);padding:5px 0"><span style="font-size:8px;color:var(--fg-muted);width:40px">메일</span><span style="font-size:8px;color:var(--fg-faint)">name@…</span></div></div>', "iOS 텍스트 필드 재현"),
     "<b>텍스트 필드</b>(Text field) · 설정 화면에서는 라벨을 <b>왼쪽에</b> 두고 값을 오른쪽에 두는 줄 형태가 많습니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:8px;right:8px;top:36px"><div style="border:1px solid var(--line-strong);border-radius:4px;padding:8px 6px 4px;position:relative"><span style="position:absolute;top:-4px;left:5px;background:var(--surface);padding:0 3px;font-size:6px;color:var(--accent)">메일</span><span style="font-size:7px;color:var(--fg-faint)">name@…</span></div><div style="font-size:6px;color:var(--fg-muted);margin-top:3px">정산 안내를 보냅니다</div></div>', "안드로이드 텍스트 필드 재현"),
     "<b>텍스트 필드</b> · 라벨이 <b>테두리 위로 올라앉는</b> 모양이 표준이고, 아래 설명은 <b>서포팅 텍스트</b>라 부릅니다."),
  ]),
  plat_note="안드로이드의 라벨은 기본이 <b>칸 안에 있다가 입력하면 위로 올라가는</b> 방식입니다. 그래서 \"라벨 위에 놓아 주세요\"가 안드로이드 디자이너에게는 표준에서 벗어나는 요구로 들립니다. 어느 쪽이든 <b>값이 들어와도 라벨이 보인다</b>는 조건만 지키면 됩니다.",
  siblings=siblings("field"),
  related='''        <li><a href="../items/error.html"><b>에러 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>
        <li><span class="na"><b>헬퍼 텍스트 문구</b><em>14부</em></span></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
