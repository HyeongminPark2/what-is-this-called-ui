# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def kv(pairs, label, note="", ok=None, w="152px", kw="52px", stack=False, cut=True):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    cutst = 'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;' if cut else ''
    out = []
    for k, v, bad in pairs:
        cl = 'color:var(--danger);' if bad else ''
        if stack:
            out.append('<span style="display:grid;gap:0;padding:2px 0;border-top:1px solid var(--line);font-size:8px">'
                       '<span style="color:var(--fg-muted);' + cutst + '">' + k + '</span>'
                       '<span style="' + cl + cutst + '">' + v + '</span></span>')
        else:
            out.append('<span style="display:grid;grid-template-columns:' + kw + ' 1fr;gap:6px;padding:2px 0;'
                       'border-top:1px solid var(--line);font-size:8px">'
                       '<span style="color:var(--fg-muted);min-width:0;' + cutst + '">' + k + '</span>'
                       '<span style="min-width:0;' + cl + cutst + '">' + v + '</span></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:5px 7px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

P = [("주문번호", "2411-0042-88231", False), ("가게", "모란상회", False), ("상태", "정산 대기", False)]
PLONG = [("주문번호", "2411-0042-88231", True), ("가게", "한빛아웃도어 영등포타임…", True), ("상태", "정산 대기", False)]

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">&lt;dl&gt;은 이름과 값의 짝을 담음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">&lt;dt&gt; 이름과 &lt;dd&gt; 값을 한 짝으로 묶음</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">라벨 폭을 고정하면 값이 가지런히 맞음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">좁아지면 값이 먼저 잘림</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">좁으면 라벨을 위로 올리고 가지런함은 포기함</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">값이 없으면 '—' 대신 없는 이유를 적음</div>
                </div>
              </div>'''

D = dict(
  slug="keyvalue", ko="키-값 목록", en="Key-value list · description list",
  desc="이름과 값의 짝을 줄줄이 보여 주는 키-값 목록의 라벨 폭과 값 잘림, 화면이 좁을 때 세로로 바꾸는 법을 보여 주는 항목입니다.",
  lede="키-값 목록은 줄마다 이름 하나와 값 하나를 <b>짝</b>으로 보여 주는 부품으로, 여러 건을 열로 세우는 표와는 다릅니다. 상세 화면의 절반쯤이 이 부품으로 채워집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>라벨 폭을 고정</b>하면 값이 세로로 가지런히 줄을 맞춥니다.
          대신 칸이 좁아지면 <b>값이 먼저 잘리는데</b>, 데모는 잘린 줄 수를 세어 적습니다.<br>
          '좁으면 라벨을 위로 올리기'를 켜면 라벨을 값 위에 올립니다. 값의 시작 위치가 가지런하지는 않지만
          <b>아무것도 잘리지 않아서</b>, 폰 화면에서 흔히 씁니다.<br>
          태그는 <code>&lt;dl&gt;</code>·<code>&lt;dt&gt;</code>·<code>&lt;dd&gt;</code>를 씁니다.
          그래서 스크린 리더로 읽을 때도 이름과 값이 <b>짝으로 전해집니다</b>.</p>
        </div>''',
  names=rows([
    ("한국어", "키-값 목록, 정의 목록, 속성 목록, 상세 정보"),
    ("영어", "key-value list, description list, definition list, detail list"),
    ("같이 쓰는 말",
     "HTML 태그 이름을 따서 <b>정의 목록</b>(description list)이라고 부르고,  "
     "이름 쪽은 <b>라벨</b>이나 <b>키</b>, 값 쪽은 <b>값</b>이라고 합니다.  "
     "한 줄에 여러 짝을 넣는 방식은 <b>인라인 KV</b>,  "
     "값을 그 자리에서 고칠 수 있게 한 것은 <b>인라인 편집</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>테이블</b> — <a href=\"table.html\">표</a>는 <b>여러 건</b>을 줄로 세우고, 키-값 목록은 <b>한 건</b>의 속성을 보여 줍니다.<br>"
     "<b>폼</b> — <a href=\"form.html\">폼</a>은 값을 <b>고치는</b> 화면이고, 키-값 목록은 값을 <b>읽는</b> 화면입니다.<br>"
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>한 건 전체</b>를 한 줄에 담고, 키-값 목록은 한 건의 속성 하나를 한 줄에 담습니다."),
  ]),
  states=states([
    (kv(P, "기본", "라벨 폭을 고정함", True), "라벨 폭을 고정했을 때", "값이 세로로 <b>가지런히</b> 줄을 맞춥니다"),
    (kv(PLONG, "좁음", "값이 잘림", False), "칸이 좁을 때", "라벨보다 <b>값이 먼저</b> 잘립니다"),
    (kv([("주문번호", "2411-0042-88231", False), ("가게", "한빛아웃도어 영등포타임스퀘어점", False)],
        "위아래로", "아무것도 잘리지 않음", True, "152px", "52px", True),
     "라벨을 값 위로 올렸을 때", "값의 <b>가지런함</b>을 포기하는 대신 잘리지 않습니다"),
    (kv([("주문번호", "2411-0042-88231", False), ("가게", "모란상회", False), ("정산일", "— 아직 정해지지 않았습니다", False)],
        "빈 값", "'—' 뒤에 이유를 적음", True),
     "값이 없을 때", "값이 <b>왜 없는지</b>까지 적습니다"),
    (kv([("주문번호", "2411-0042-88231", False), ("상태", "정산 대기", False)], "짧게", "꼭 필요한 것만", True),
     "줄이 적을 때", "<b>세 줄</b>이면 충분한 화면도 많습니다"),
    (kv([("주", "A", False), ("문", "B", False), ("번", "C", False), ("호", "D", False), ("가", "E", False), ("게", "F", False)],
        "너무 많음", "열 줄을 넘으면 묶음", False),
     "줄이 많을 때", "관련된 줄끼리 <b>묶어서</b> 접어 둡니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>&lt;dl&gt;</code>", "짝의 목록", "표가 아니라 이름과 값의 <b>짝</b>을 담습니다"),
    ("<code>&lt;dt&gt;·&lt;dd&gt;</code>", "이름과 값", "스크린 리더로 읽을 때도 <b>짝으로 전해집니다</b>"),
    ("라벨 폭", "고정한 폭", "값이 세로로 <b>가지런히</b> 맞춰집니다"),
    ("좁을 때", "값이 잘리는 경우", "말줄임으로 <b>줄 높이</b>를 지킵니다"),
    ("세로 전환", "라벨을 값 위로 올리는 배치", "<b>폰</b> 화면에서 흔히 씁니다"),
    ("빈 값", "없는 이유까지 적는 칸", "'—' 하나만 두지 않고 값이 왜 없는지 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          가장 먼저 정할 것은 라벨 폭을 <b>고정할지 내용에 맞출지</b>입니다.
          고정하면 값이 가지런해지는 대신 긴 라벨이 잘리고,
          내용에 맞추면 줄마다 값의 시작 위치가 달라져서 <b>시선이 좌우로 오가며</b> 읽게 됩니다.
          그래서 줄이 다섯 개를 넘으면 <b>폭을 고정</b>하는 쪽이 읽기 편합니다.<br>
          값이 비었을 때 <b>'—' 하나만</b> 두는 경우도 흔한데,
          그러면 아직 정해지지 않은 것인지 해당 사항이 없는 것인지 알 수 없습니다.
          짧게라도 값이 <b>왜 없는지</b>를 적어 두면 문의가 줄어듭니다.</p>''',
  do_title="키-값 목록을 만들 때 지킬 것", dont_title="키-값 목록을 만들 때 피할 것",
  do=ul([
    "<code>&lt;dl&gt;</code>·<code>&lt;dt&gt;</code>·<code>&lt;dd&gt;</code>로 적기",
    "줄이 다섯 개를 넘으면 <b>라벨 폭을 고정</b>하기",
    "폰에서는 <b>라벨을 값 위로</b> 올리기",
  ]),
  dont=ul([
    "표 태그로 적기. <b>한 건</b>의 속성인데 스크린 리더가 열 이름까지 읽습니다",
    "값이 없을 때 <b>'—' 하나만</b> 두기",
    "값을 <b>고칠 수 있는</b> 칸을 섞어 두기. 고치는 화면은 폼으로 만듭니다",
    "줄을 열다섯 개씩 늘어놓기. 관련된 줄끼리 <b>묶어서</b> 접어 둡니다",
  ]),
  instead='여러 건을 줄로 세워야 하면 <a href="table.html">데이터 테이블</a>을 쓰고, 값을 고치는 화면은 <a href="form.html">폼 설계</a>를 따릅니다. 관련된 줄끼리 묶어 접어 두려면 <a href="accordion.html">접히는 글</a>을, 한 건 전체를 한 줄에 담으려면 <a href="listitem.html">리스트 아이템</a>을 씁니다.',
  cases=cases([
    (kv(P, "주문 상세", "", True), "주문 상세 정보 보여 주기", "키-값 목록을 <b>가장 흔히</b> 보는 자리입니다"),
    (kv([("사업자번호", "000-00-00000", False), ("대표자", "홍길동", False)], "가게 정보", "", True),
     "읽기만 하는 가게 정보 보여 주기", "읽기만 하고 고치지 않는 값들을 보여 줍니다"),
    (kv([("크기", "1.2MB", False), ("올린 날", "2026-11-12", False)], "파일 속성", "", True),
     "파일 속성을 짧게 보여 주기", "두 줄로 <b>짧게</b> 보여 줍니다"),
  ]),
  keys_heads="<th>키와 마크업</th><th>지켜야 할 점</th>",
  code_lede="<code>&lt;dl&gt;</code> 안에서 <code>&lt;div&gt;</code>로 이름과 값을 한 짝씩 묶으면 CSS 격자로 배치하기 쉽습니다.",
  code='''&lt;<span class="t">dl</span> <span class="a">class</span>=<span class="s">"kv"</span>&gt;
  &lt;<span class="t">div</span>&gt;&lt;<span class="t">dt</span>&gt;주문번호&lt;/<span class="t">dt</span>&gt;&lt;<span class="t">dd</span>&gt;2411-0042-88231&lt;/<span class="t">dd</span>&gt;&lt;/<span class="t">div</span>&gt;
  &lt;<span class="t">div</span>&gt;&lt;<span class="t">dt</span>&gt;가게&lt;/<span class="t">dt</span>&gt;&lt;<span class="t">dd</span>&gt;모란상회&lt;/<span class="t">dd</span>&gt;&lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">dl</span>&gt;

.kv &gt; div { <span class="a">display</span>: grid; <span class="a">grid-template-columns</span>: <span class="a">90px</span> <span class="a">1fr</span>; <span class="a">gap</span>: <span class="a">10px</span>; }
.kv dt, .kv dd { <span class="a">min-width</span>: <span class="a">0</span>; <span class="a">white-space</span>: nowrap;
  <span class="a">overflow</span>: hidden; <span class="a">text-overflow</span>: ellipsis; }
.kv dd { <span class="a">margin</span>: <span class="a">0</span>; }

@media (max-width: <span class="a">480px</span>) {
  .kv &gt; div { <span class="a">grid-template-columns</span>: <span class="a">1fr</span>; }   <span class="c">/* 라벨을 값 위로 */</span>
}''',
  keys=kbd([
    ("<code>&lt;dl&gt;</code>로 적기", "스크린 리더로 읽을 때 <b>이름과 값이 짝으로</b> 전해집니다"),
    ("짝마다 <code>&lt;div&gt;</code>로 묶기", "HTML 규칙에서 <b>허용하는</b> 방식이고, CSS 격자로 배치하기 쉽습니다"),
    ("Tab", "읽기용이라 포커스가 <b>멈추지 않고</b>, 값에 링크가 있을 때만 멈춥니다"),
    ("값이 말줄임으로 잘렸을 때", "잘린 값은 <code>title</code>로 <b>전체 값</b>을 띄워 줍니다"),
    ("값을 복사할 수 있게 두기", "<code>user-select</code>를 막지 않습니다. 주문번호 같은 값은 사용자가 <b>복사해서 쓰는</b> 경우가 많습니다"),
    ("확인하는 방법", "화면을 390px로 줄여 <b>값이 몇 줄 잘리는지</b> 셉니다"),
  ]),
  backend=rows([
    ("서버는 자르지 않은 값 보내기", "서버가 값을 미리 잘라 보내면 잘린 부분은 <b>복사도 검색도</b> 할 수 없습니다. 값을 줄여 보이는 일은 화면에서 합니다."),
    ("값이 빈 이유 구별해 보내기", "<code>null</code>(아직 모름)과 <code>\"\"</code>(없음)을 구별해서 보내 주면 화면에서 두 경우에 <b>다른 문구</b>를 쓸 수 있습니다."),
    ("줄의 차례는 화면에서 정하기", "응답에 담긴 키 순서는 보장되지 않을 수 있으므로 <b>화면에서 차례를 정합니다</b>. 중요한 값이 위에 오도록 화면이 순서를 정해 둡니다."),
  ]),
  plat_lede="이름과 값을 <b>짝</b>으로 보여 준다는 점은 세 플랫폼이 모두 같습니다.",
  plats=plats([
    ("웹", "&lt;dl&gt;",
     kv([("주문번호", "2411-0042", False)], "", "", True, "110px", "44px"),
     "전용 태그가 있는 것이 웹의 장점입니다. 덕분에 <b>스크린 리더로 읽을 때도</b> 짝이 유지됩니다."),
    ("iOS", "Form · LabeledContent",
     '''              <div class="phone" role="img" aria-label="iOS 상세 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:16px;height:5px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;right:5px;top:28px;width:22px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;top:40px;width:14px;height:5px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;right:5px;top:40px;width:18px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>왼쪽에 라벨, 오른쪽에 값</b>을 두는 것이 iOS의 기본 배치로, 이 항목에서 말하는 좌우 배치와 같습니다."),
    ("안드로이드", "ListItem",
     '''              <div class="phone" role="img" aria-label="안드로이드 상세 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:16px;height:4px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;left:5px;top:33px;width:26px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;top:44px;width:14px;height:4px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;left:5px;top:51px;width:22px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>라벨을 값 위에</b> 올리는 배치를 많이 쓰고, 이 항목에서 말하는 세로 배치와 같습니다."),
  ]),
  plat_note="iOS와 안드로이드는 각각 <b>좌우</b>와 <b>세로</b> 배치를 기본으로 골랐습니다. 좌우 배치는 값이 가지런하고 세로 배치는 값이 잘리지 않아서 어느 쪽이 틀렸다고 할 수는 없고, <b>값의 길이</b>가 고르면 좌우가, 들쭉날쭉하면 세로가 낫습니다. 웹에서는 미디어 쿼리 한 줄로 <b>두 배치를 모두</b> 쓸 수 있으므로, 화면 폭에 따라 바꾸는 것이 가장 쉬운 방법입니다.",
  siblings=siblings("keyvalue"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="semantics.html"><b>시맨틱 태그</b><em>12부</em></a></li>''',
)
