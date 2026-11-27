# -*- coding: utf-8 -*-
from ax5 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L5 = "표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">&lt;dl&gt; — 이름과 값의 짝</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">&lt;dt&gt; 이름 · &lt;dd&gt; 값 — 둘을 묶는다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">라벨 폭 고정 — 값이 한 줄로 선다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">좁아지면 값이 먼저 잘린다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">좁으면 라벨을 위로 — 가지런함은 잃는다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">값이 없으면 '—' 가 아니라 왜 없는지</div>
                </div>
              </div>'''

D = dict(
  slug="keyvalue", ko="키-값 목록", en="Key-value list · description list",
  desc="이름과 값의 짝을 줄줄이 보여 주는 부품. 라벨 폭, 잘림, 좁을 때의 세로 전환.",
  lede="표가 아니라 <b>짝</b>입니다 — 줄마다 이름 하나와 값 하나. 상세 화면의 절반이 이걸로 차 있습니다.",
  axes_lede=L5,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>라벨 폭을 고정</b>하면 값이 한 줄로 가지런히 섭니다.
          대신 칸이 좁아지면 <b>값이 먼저 잘립니다</b> — 데모가 잘린 줄 수를 세서 적습니다.<br>
          '좁으면 위아래로'를 켜면 라벨을 값 위에 올립니다. 가지런함은 잃지만
          <b>아무것도 안 잘립니다</b> — 폰에서 쓰는 꼴입니다.<br>
          태그는 <code>&lt;dl&gt;</code>·<code>&lt;dt&gt;</code>·<code>&lt;dd&gt;</code> 입니다.
          소리로 읽을 때도 <b>짝이 유지</b>됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "키-값 목록, 정의 목록, 속성 목록, 상세 정보"),
    ("영어", "key-value list, description list, definition list, detail list"),
    ("같이 쓰는 말",
     "HTML 태그 이름을 따서 <b>정의 목록</b>(description list)이라 부르고, "
     "이름 쪽을 <b>라벨</b>·<b>키</b>, 값 쪽을 <b>값</b>이라 합니다. "
     "한 줄에 여러 짝을 넣는 꼴은 <b>인라인 KV</b>, "
     "값을 그 자리에서 고칠 수 있게 한 것은 <b>인라인 편집</b>입니다."),
    ("자주 잘못 부름",
     "<b>테이블</b> — <a href=\"table.html\">표</a>는 <b>여러 건</b>을 줄로 세웁니다. 이건 <b>한 건</b>입니다.<br>"
     "<b>폼</b> — <a href=\"form.html\">폼</a>은 <b>고치는</b> 화면입니다. 이건 <b>읽는</b> 화면입니다.<br>"
     "<b>리스트 아이템</b> — <a href=\"listitem.html\">리스트 아이템</a>은 <b>한 건 전체</b>가 한 줄입니다."),
  ]),
  axes=ax("키-값 목록"),
  oneline="<b>한 건의 속성을 읽는 자리입니다.</b> 고칠 수 있게 하려면 그건 폼이지 이게 아닙니다.",
  states=states([
    (kv(P, "기본", "라벨 폭을 고정했다", True), "기본", "값이 <b>한 줄로</b> 선다"),
    (kv(PLONG, "좁음", "값이 잘렸다", False), "좁을 때", "<b>값이 먼저</b> 잘린다"),
    (kv([("주문번호", "2411-0042-88231", False), ("가게", "한빛아웃도어 영등포타임스퀘어점", False)],
        "위아래로", "아무것도 안 잘린다", True, "152px", "52px", True),
     "세로로", "<b>가지런함</b>을 포기한다"),
    (kv([("주문번호", "2411-0042-88231", False), ("가게", "모란상회", False), ("정산일", "— 아직 정해지지 않았습니다", False)],
        "빈 값", "'—' 뒤에 이유를 적는다", True),
     "값이 없을 때", "<b>왜 없는지</b>까지"),
    (kv([("주문번호", "2411-0042-88231", False), ("상태", "정산 대기", False)], "짧게", "꼭 필요한 것만", True),
     "줄이 적을 때", "<b>세 줄</b>이면 충분한 화면도 많다"),
    (kv([("주", "A", False), ("문", "B", False), ("번", "C", False), ("호", "D", False), ("가", "E", False), ("게", "F", False)],
        "너무 많음", "열 줄을 넘으면 묶는다", False),
     "줄이 많을 때", "<b>묶어서</b> 접는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>&lt;dl&gt;</code>", "짝의 목록", "표가 아니라 <b>짝</b>이다"),
    ("<code>&lt;dt&gt;·&lt;dd&gt;</code>", "이름과 값", "소리로도 <b>짝이 유지</b>된다"),
    ("라벨 폭", "고정", "값이 <b>한 줄로</b> 선다"),
    ("좁을 때", "값이 잘림", "말줄임으로 <b>줄 높이</b>를 지킨다"),
    ("세로 전환", "라벨을 위로", "<b>폰</b>에서 쓰는 꼴"),
    ("빈 값", "이유까지", "'—' 하나만 두지 않는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라벨 폭을 <b>고정할지 내용에 맞출지</b>가 첫 결정입니다.
          고정하면 값이 가지런한 대신 긴 라벨이 잘리고,
          내용에 맞추면 라벨마다 값의 시작 위치가 달라져 <b>눈이 지그재그</b>로 움직입니다.
          줄이 다섯을 넘으면 <b>고정</b>하는 쪽이 읽기 편합니다.<br>
          값이 비었을 때 <b>'—' 하나만</b> 두는 것도 흔한데,
          그러면 '아직 안 정해진 것'인지 '해당 없음'인지 모릅니다.
          한 줄이라도 <b>왜 없는지</b>를 적어 두면 문의가 줄어듭니다.</p>''',
  do=ul([
    "<code>&lt;dl&gt;</code>·<code>&lt;dt&gt;</code>·<code>&lt;dd&gt;</code> 로 적기",
    "줄이 다섯을 넘으면 <b>라벨 폭을 고정</b>하기",
    "폰에서는 <b>라벨을 값 위로</b> 올리기",
  ]),
  dont=ul([
    "표 태그로 적기 — <b>한 건</b>인데 열 이름이 읽힌다",
    "값이 없을 때 <b>'—' 하나만</b> 두기",
    "값을 <b>고칠 수 있게</b> 섞어 두기 — 그건 폼이다",
    "줄을 열다섯씩 늘어놓기 — <b>묶어서</b> 접는다",
  ]),
  instead='여러 건을 줄로 세우면 <a href="table.html">데이터 테이블</a>, 고치는 화면은 <a href="form.html">폼 설계</a>, 묶어서 접으면 <a href="accordion.html">접히는 글</a>, 한 건 전체가 한 줄이면 <a href="listitem.html">리스트 아이템</a>.',
  cases=cases([
    (kv(P, "주문 상세", "", True), "주문 상세", "<b>가장 흔한</b> 자리"),
    (kv([("사업자번호", "000-00-00000", False), ("대표자", "홍길동", False)], "가게 정보", "", True),
     "가게 정보", "읽기만 하는 값들"),
    (kv([("크기", "1.2MB", False), ("올린 날", "2026-11-12", False)], "파일 속성", "", True),
     "파일 속성", "<b>짧게</b> 두 줄"),
  ]),
  code_lede="<code>&lt;dl&gt;</code> 안에서 <code>&lt;div&gt;</code> 로 한 짝씩 묶으면 격자로 세우기 쉽습니다.",
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
    ("<code>&lt;dl&gt;</code>", "소리로 읽을 때 <b>이름과 값이 짝으로</b> 전해진다"),
    ("<code>&lt;div&gt;</code> 로 묶기", "HTML 에서 <b>허용된</b> 방식이다 — 격자를 세우기 쉽다"),
    ("Tab", "읽기용이라 <b>멈추지 않는다</b> — 값에 링크가 있을 때만 멈춘다"),
    ("말줄임", "잘린 값은 <code>title</code> 로 <b>전체</b>를 띄워 준다"),
    ("복사", "<code>user-select</code> 를 막지 않는다 — 주문번호는 <b>복사하라고</b> 있는 값이다"),
    ("확인하는 법", "390px 로 줄여 <b>값이 몇 줄 잘리는지</b> 센다"),
  ]),
  backend=rows([
    ("온전한 값을 준다", "서버가 미리 자르면 <b>복사도 검색도</b> 안 됩니다 — 줄이는 것은 화면의 일입니다."),
    ("빈 값의 뜻", "<code>null</code>(아직 모름)과 <code>\"\"</code>(없음)을 가려 주면 화면이 <b>다른 문구</b>를 쓸 수 있습니다."),
    ("차례", "응답의 키 순서를 믿지 말고 <b>화면이 차례를 정합니다</b> — 중요한 것이 위로 가야 합니다."),
  ]),
  plat_lede="<b>이름-값 짝</b>이라는 생각은 어디서나 같습니다.",
  plats=plats([
    ("웹", "&lt;dl&gt;",
     kv([("주문번호", "2411-0042", False)], "", "", True, "110px", "44px"),
     "전용 태그가 있는 것이 웹의 장점입니다 — <b>소리로도</b> 짝이 유지됩니다."),
    ("iOS", "Form · LabeledContent",
     '''              <div class="phone" role="img" aria-label="iOS 상세 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:28px;width:16px;height:5px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;right:5px;top:28px;width:22px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;top:40px;width:14px;height:5px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;right:5px;top:40px;width:18px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>왼쪽에 라벨, 오른쪽에 값</b>이 iOS 의 기본 꼴입니다 — 우리 쪽 '좌우' 와 같습니다."),
    ("안드로이드", "ListItem",
     '''              <div class="phone" role="img" aria-label="안드로이드 상세 목록 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;top:26px;width:16px;height:4px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;left:5px;top:33px;width:26px;height:5px;border-radius:2px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:5px;top:44px;width:14px;height:4px;border-radius:2px;background:var(--line)"></div>
                <div style="position:absolute;left:5px;top:51px;width:22px;height:5px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "<b>라벨을 값 위에</b> 올리는 꼴이 많습니다 — 우리 쪽 '세로'와 같습니다."),
  ]),
  plat_note="두 플랫폼이 <b>좌우</b>와 <b>세로</b>를 각각 기본으로 고른 것이 재미있습니다. 좌우는 가지런하고 세로는 안 잘립니다 — 어느 쪽도 틀리지 않고, <b>값의 길이</b>가 고르면 좌우가, 들쭉날쭉하면 세로가 낫습니다. 웹에서는 한 줄의 미디어 쿼리로 <b>둘 다</b> 쓸 수 있으니, 폭에 따라 바꾸는 것이 가장 쉬운 답입니다.",
  siblings=siblings("keyvalue"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="semantics.html"><b>시맨틱 태그</b><em>12부</em></a></li>''',
)
