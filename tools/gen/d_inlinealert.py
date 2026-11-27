# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

def al(kind, text, label, note="", ok=None, w="152px", field=None, after=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if kind == 'err':
        st = ('background:color-mix(in srgb, var(--danger) 8%, var(--surface));color:var(--danger);'
              'border:1px solid color-mix(in srgb, var(--danger) 35%, transparent);')
        mark = '!'
    elif kind == 'warn':
        st = ('background:color-mix(in srgb, #9a6700 10%, var(--surface));color:#9a6700;'
              'border:1px solid color-mix(in srgb, #9a6700 32%, transparent);')
        mark = '!'
    else:
        st = ('background:color-mix(in srgb, #0969da 9%, var(--surface));color:#0969da;'
              'border:1px solid color-mix(in srgb, #0969da 30%, transparent);')
        mark = 'i'
    msg = ('<span style="display:flex;gap:4px;align-items:flex-start;border-radius:4px;padding:3px 6px;'
           'font-size:7.5px;' + st + '"><span aria-hidden="true">' + mark + '</span>'
           '<span>' + text + '</span></span>')
    fieldHtml = ''
    if field:
        fieldHtml = ('<span style="display:grid;gap:2px">'
                     '<span style="font-size:7px;color:var(--fg-muted)">' + field + '</span>'
                     '<span style="display:block;border:1px solid ' +
                     ('var(--danger)' if kind == 'err' else 'var(--line)') +
                     ';border-radius:4px;padding:3px 5px;font-size:7.5px">123</span></span>')
    inner = (fieldHtml + msg) if not after else (msg + fieldHtml)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:4px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">뜨지 않는다 — 흐름 안에 자리를 차지한다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">틀린 칸 바로 아래 — 거리가 0에 가깝다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-describedby 로 칸과 묶는다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">role="alert" — 오류는 그 자리에서 읽는다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">치우지 않아도 된다 — 고치면 사라진다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">맨 위에 모으면 어느 칸인지 찾아 내려가야 한다</div>
                </div>
              </div>'''

D = dict(
  slug="inlinealert", ko="인라인 얼럿", en="Inline alert",
  desc="흐름 안에 자리를 차지하는 알림. 틀린 칸과의 거리, 칸과 묶기, 토스트와의 차이.",
  lede="<b>뜨지 않습니다</b> — 흐름 안에 자리를 차지하고, 눌러서 치우지 않아도 됩니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>붙이는 자리를 바꿔 가며 데모가 <b>틀린 칸에서 메시지까지의 거리(px)</b>를 재서 적습니다.<br>
          <b>칸 바로 아래</b>면 거리가 0에 가깝고, <b>맨 위에 모으면</b> 수백 px 떨어져
          어느 칸이 틀렸는지 찾아 내려가야 합니다. <b>토스트</b>는 사라져서 다시 볼 수도 없습니다.<br>
          어느 쪽이든 <code>aria-describedby</code> 로 <b>칸과 메시지를 묶어야</b>
          소리로 들을 때 짝이 유지됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "인라인 얼럿, 인라인 메시지, 칸 아래 메시지"),
    ("영어", "inline alert, inline message, field error, callout"),
    ("같이 쓰는 말",
     "입력칸 아래에 붙는 것은 <b>필드 에러</b>(field error), "
     "글 안에 끼워 넣은 눈에 띄는 상자는 <b>콜아웃</b>(callout)이나 <b>어드모니션</b>(admonition)입니다. "
     "폼 맨 위에 모아 둔 것은 <b>에러 서머리</b>(error summary)라 부릅니다."),
    ("자주 잘못 부름",
     "<b>배너</b> — <a href=\"banner.html\">배너</a>는 <b>화면 전체</b>의 사정을 꼭대기에서 알립니다.<br>"
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 <b>떠서 사라집니다</b>.<br>"
     "<b>툴팁</b> — <a href=\"tooltip.html\">툴팁</a>은 <b>가리켜야</b> 보입니다."),
  ]),
  axes=axis_table("인라인 얼럿"),
  oneline="<b>틀린 칸 바로 아래가 가장 좋습니다.</b> 멀어질수록 사람이 찾아 내려가야 합니다.",
  states=states([
    (al("err", "사업자번호는 10자리입니다", "", "거리 0에 가깝다", True, "152px", "사업자번호"),
     "칸 바로 아래", "<b>가장 가깝다</b>"),
    (al("err", "고쳐야 할 칸이 2개 있습니다", "", "어느 칸인지 찾아 내려가야 한다", None, "152px", "사업자번호", True),
     "맨 위에 모음", "<b>개수는</b> 한눈에"),
    (al("warn", "이 계좌는 정산일에 확인이 한 번 더 필요합니다", "", "막지는 않는다", None),
     "주의", "<b>넘어갈 수는</b> 있다"),
    (al("info", "정산은 매주 수요일에 보냅니다", "", "그냥 알린다", True),
     "안내", "<b>오류가 아니다</b>"),
    (al("err", "사업자번호를 확인해 주세요", "", "칸과 안 묶였다", False),
     "칸과 안 묶임", "<b>소리로는</b> 짝이 안 간다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">고쳤더니 사라졌다</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">치울 필요가 없다</span>'),
         "고친 뒤", True, "", "152px"),
     "고친 뒤", "<b>저절로</b> 사라진다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("안 뜬다", "흐름 안", "자리를 <b>차지한다</b>"),
    ("자리", "칸 바로 아래", "거리가 <b>0에 가깝다</b>"),
    ("<code>aria-describedby</code>", "칸과 묶기", "소리로도 <b>짝이 간다</b>"),
    ("<code>role=\"alert\"</code>", "오류만", "그 자리에서 <b>읽어 준다</b>"),
    ("치우기", "필요 없음", "고치면 <b>저절로</b>"),
    ("맨 위에 모으기", "멀다", "<b>찾아 내려가야</b> 한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          칸이 열 개를 넘는 긴 폼에서는 <b>둘 다</b> 쓰는 것이 좋습니다 —
          맨 위에 '고쳐야 할 칸 2개'를 두어 <b>얼마나 남았는지</b>를 알리고,
          그 목록의 각 줄을 누르면 <b>그 칸으로 데려가며</b>,
          칸 아래에는 <b>구체적인 이유</b>를 적습니다.
          이것이 접근성 지침이 권하는 꼴이기도 합니다.<br>
          <code>role="alert"</code> 는 <b>하던 말을 끊고</b> 읽습니다 —
          그래서 오류에는 맞지만 안내에는 과합니다.
          안내는 <code>role="status"</code> 거나, 아예 역할을 안 주고
          <code>aria-describedby</code> 로 칸에 묶기만 해도 됩니다.</p>''',
  do=ul([
    "<b>틀린 칸 바로 아래</b>에 붙이기",
    "<code>aria-describedby</code> 로 <b>칸과 묶기</b>",
    "긴 폼이면 <b>맨 위 요약 + 칸 아래 이유</b>를 같이 두기",
  ]),
  dont=ul([
    "오류를 <b>토스트</b>로 띄우기 — 사라지면 다시 못 본다",
    "<b>색만</b>으로 알리기 — 빨간 테두리만으로는 이유를 모른다",
    "안내에 <code>role=\"alert\"</code> 쓰기 — <b>하던 말을 끊는다</b>",
    "메시지를 <b>칸 위</b>에 두기 — 칸을 가린다고 느껴진다",
  ]),
  instead='화면 전체 사정이면 <a href="banner.html">배너</a>, 떠서 사라지면 <a href="toast.html">토스트</a>, 가리켜야 보이면 <a href="tooltip.html">툴팁</a>, 검사 규칙은 <a href="validation.html">입력 검증</a>.',
  cases=cases([
    (al("err", "10자리로 적어 주세요", "", "", True, "150px", "사업자번호"), "입력 오류", "<b>가장 흔한</b> 자리"),
    (al("warn", "이 설정은 다음 정산부터 적용됩니다", "", "", None, "150px"), "주의", "막지 않는 알림"),
    (al("info", "정산 주기를 바꾸면 이번 주는 그대로입니다", "", "", True, "150px"), "안내", "<b>미리</b> 알린다"),
  ]),
  code_lede="칸과 메시지를 <code>aria-describedby</code> 로 묶습니다. 오류에만 <code>role=\"alert\"</code>.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"biz"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"biz"</span> <span class="a">aria-invalid</span>=<span class="s">"true"</span>
       <span class="a">aria-describedby</span>=<span class="s">"biz-err"</span> <span class="a">value</span>=<span class="s">"123"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"biz-err"</span> <span class="a">class</span>=<span class="s">"inline-alert inline-alert--error"</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;
  사업자번호는 10자리입니다 (지금 3자리)
&lt;/<span class="t">p</span>&gt;

<span class="c">/* 색만으로 알리지 않는다 — 기호와 글이 같이 있다 */</span>
.inline-alert--error { <span class="a">color</span>: <span class="a">var</span>(--color-text-danger);
  <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--color-border-danger); }''',
  keys=kbd([
    ("<code>aria-describedby</code>", "칸을 읽을 때 <b>이유도 같이</b> 읽힌다"),
    ("<code>aria-invalid</code>", "그 칸이 <b>틀렸다</b>고 알린다"),
    ("<code>role=\"alert\"</code>", "오류만. 안내에는 <b>과하다</b>"),
    ("초점", "제출했으면 <b>첫 틀린 칸</b>으로 옮긴다"),
    ("요약 목록", "맨 위 요약의 줄은 <b>그 칸으로 가는 링크</b>로 둔다"),
    ("확인하는 법", "칸에 Tab 으로 들어가 <b>이유가 읽히는지</b> 본다"),
  ]),
  backend=rows([
    ("칸마다 돌려준다", "<code>{field: \"biz_no\", message: \"10자리\"}</code> 처럼 <b>어느 칸인지</b>가 있어야 붙일 자리를 압니다."),
    ("사람이 읽을 말로", "<code>ERR_INVALID_FORMAT</code> 만 오면 화면이 말을 다시 지어야 합니다."),
    ("여러 개", "한 번에 다 돌려주면 <b>한 번에 고칠</b> 수 있습니다 — 하나씩 주면 왕복이 늘어납니다."),
  ]),
  plat_lede="<b>폼이 있는 곳이면</b> 어디나 같은 꼴입니다.",
  plats=plats([
    ("웹", "칸 아래 글",
     al("err", "10자리로", "", "", True, "110px", "사업자번호"),
     "<code>aria-describedby</code> 로 묶는 것이 <b>웹의 표준</b>입니다."),
    ("iOS", "칸 아래 글",
     '''              <div class="phone" role="img" aria-label="iOS 칸 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:3px;border:1px solid var(--danger)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:5px;border-radius:2px;background:color-mix(in srgb,var(--danger) 35%,transparent)"></div></div></div>''',
     "정해진 부품은 없고 <b>빨간 글 한 줄</b>을 칸 아래 둡니다."),
    ("안드로이드", "TextField helper/error",
     '''              <div class="phone" role="img" aria-label="안드로이드 칸 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:11px;border-radius:3px;border:1px solid var(--danger)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:5px;border-radius:2px;background:color-mix(in srgb,var(--danger) 35%,transparent)"></div></div></div>''',
     "텍스트 필드에 <b>오류 글 자리</b>가 아예 들어 있습니다 — 칸이 흔들리지 않습니다."),
  ]),
  plat_note="안드로이드의 텍스트 필드가 <b>오류 글 자리를 미리 비워 두는</b> 것은 그대로 베낄 만합니다 — 오류가 뜰 때 칸이 아래로 밀리지 않아 화면이 안 흔들립니다. 웹에서도 메시지 자리에 <b>최소 높이</b>를 주면 같은 효과를 얻습니다. 여러 칸에 오류가 한꺼번에 뜰 때 특히 티가 납니다.",
  siblings=siblings("inlinealert"),
  related='''        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="banner.html"><b>배너</b><em>6부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
