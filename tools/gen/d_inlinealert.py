# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

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
                  <div class="pin-out" data-pin="1" style="color:var(--accent)">뜨지 않고 흐름 안에 자리를 차지함</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">틀린 칸 바로 아래라 거리가 0에 가까움</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">aria-describedby로 칸과 묶음</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">role="alert"면 오류를 바로 읽어 줌</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">고치면 사라져서 치울 필요가 없음</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">맨 위에 모으면 어느 칸인지 찾아 내려가야 함</div>
                </div>
              </div>'''

D = dict(
  slug="inlinealert", ko="인라인 얼럿", en="Inline alert",
  desc="화면 위에 뜨지 않고 문서 흐름 안에 자리를 차지하는 알림입니다. 틀린 칸과 얼마나 가까이 두는지, 칸과 어떻게 묶는지, 토스트와는 어떻게 다른지 다룹니다.",
  lede="인라인 얼럿은 화면 위에 <b>뜨지 않고</b> 문서 흐름 안에 자리를 차지하는 알림입니다. 사용자가 눌러서 치울 필요가 없고, 문제를 고치면 저절로 사라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>메시지를 붙이는 자리를 바꿔 보세요. 데모가 <b>틀린 칸에서 메시지까지의 거리(px)</b>를 재서 적어 줍니다.<br>
          <b>칸 바로 아래</b>에 붙이면 거리가 0에 가깝지만, <b>맨 위에 모으면</b> 수백 px 떨어져서
          사용자가 어느 칸이 틀렸는지 찾아 내려가야 합니다. <b>토스트</b>로 띄우면 메시지가 사라져서 다시 볼 수도 없습니다.<br>
          어느 자리에 붙이든 <code>aria-describedby</code>로 <b>칸과 메시지를 묶어야</b>
          스크린 리더로 들을 때도 어느 칸의 메시지인지 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "인라인 얼럿, 인라인 메시지, 칸 아래 메시지"),
    ("영어", "inline alert, inline message, field error, callout"),
    ("같이 쓰는 말",
     "입력칸 아래에 붙는 것은 <b>필드 에러</b>(field error), "
     "글 안에 끼워 넣어 눈에 띄게 만든 상자는 <b>콜아웃</b>(callout)이나 <b>어드모니션</b>(admonition)이라고 부릅니다. "
     "폼 맨 위에 오류를 모아 둔 것은 <b>에러 서머리</b>(error summary)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>배너</b> — <a href=\"banner.html\">배너</a>는 특정 자리가 아니라 <b>화면 전체</b>에 해당하는 사정을 화면 꼭대기에서 알립니다.<br>"
     "<b>토스트</b> — <a href=\"toast.html\">토스트</a>는 화면 위에 <b>떴다가 저절로 사라집니다</b>.<br>"
     "<b>툴팁</b> — <a href=\"tooltip.html\">툴팁</a>은 대상에 마우스를 <b>올려야</b> 보입니다."),
  ]),
  states=states([
    (al("err", "사업자번호는 10자리입니다", "", "거리가 0에 가까움", True, "152px", "사업자번호"),
     "틀린 칸 바로 아래에 붙였을 때", "틀린 칸과 <b>가장 가깝습니다</b>"),
    (al("err", "고쳐야 할 칸이 2개 있습니다", "", "어느 칸인지 찾아 내려가야 함", None, "152px", "사업자번호", True),
     "맨 위에 모았을 때", "고칠 칸이 <b>몇 개인지</b> 한눈에 보입니다"),
    (al("warn", "이 계좌는 정산일에 확인이 한 번 더 필요합니다", "", "하던 일을 막지 않음", None),
     "주의를 줄 때", "확인하고 <b>넘어갈 수</b> 있습니다"),
    (al("info", "정산은 매주 수요일에 보냅니다", "", "알리기만 함", True),
     "안내만 할 때", "<b>오류가 아니라</b> 알아 둘 내용을 알립니다"),
    (al("err", "사업자번호를 확인해 주세요", "", "칸과 묶이지 않음", False),
     "칸과 묶지 않았을 때", "<b>스크린 리더로 들으면</b> 어느 칸의 메시지인지 알 수 없습니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">고치자 사라짐</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">치울 필요가 없음</span>'),
         "고친 뒤", True, "", "152px"),
     "값을 고친 뒤", "칸을 고치면 <b>저절로</b> 사라집니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("놓이는 방식", "뜨지 않고 흐름 안", "화면 위에 뜨지 않고 흐름 안에서 자리를 <b>차지합니다</b>"),
    ("자리", "칸 바로 아래", "틀린 칸과의 거리가 <b>0에 가깝습니다</b>"),
    ("<code>aria-describedby</code>", "칸과 묶기", "스크린 리더로 들어도 <b>어느 칸의 메시지인지</b> 알 수 있습니다"),
    ("<code>role=\"alert\"</code>", "오류에만 씀", "오류가 생기면 스크린 리더가 <b>바로 읽어 줍니다</b>"),
    ("치우기", "치울 필요 없음", "칸을 고치면 <b>저절로</b> 사라집니다"),
    ("맨 위에 모으기", "칸에서 멀어짐", "어느 칸인지 <b>찾아 내려가야</b> 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          칸이 열 개를 넘는 긴 폼에서는 맨 위 요약과 칸 아래 메시지를 <b>함께</b> 쓰는 것이 좋습니다.
          맨 위에는 '고쳐야 할 칸 2개'처럼 <b>얼마나 남았는지</b> 알리는 목록을 두고,
          목록의 각 줄을 누르면 <b>해당 칸으로 이동</b>하게 합니다.
          그리고 칸 아래에는 <b>무엇이 틀렸는지 구체적인 이유</b>를 적습니다.
          접근성 지침이 권하는 방식도 이와 같습니다.<br>
          <code>role="alert"</code>를 단 메시지는 스크린 리더가 <b>읽던 말을 끊고</b> 바로 읽습니다.
          그래서 오류에는 맞지만 단순한 안내에 쓰기에는 지나칩니다.
          안내에는 <code>role="status"</code>를 쓰거나, 역할을 주지 않고
          <code>aria-describedby</code>로 칸에 묶기만 해도 됩니다.</p>''',
  do_title="인라인 얼럿을 알맞게 쓰는 경우",
  dont_title="인라인 얼럿을 잘못 쓰는 경우",
  do=ul([
    "메시지를 <b>틀린 칸 바로 아래</b>에 붙일 때",
    "<code>aria-describedby</code>로 메시지를 <b>칸과 묶을</b> 때",
    "긴 폼에 <b>맨 위 요약과 칸 아래 이유</b>를 함께 둘 때",
  ]),
  dont=ul([
    "오류를 <b>토스트</b>로 띄울 때. 토스트가 사라지면 오류 내용을 다시 볼 수 없습니다",
    "<b>색만</b>으로 오류를 알릴 때. 빨간 테두리만으로는 무엇이 틀렸는지 알 수 없습니다",
    "안내에 <code>role=\"alert\"</code>를 쓸 때. 스크린 리더가 <b>읽던 말을 끊습니다</b>",
    "메시지를 <b>칸 위</b>에 둘 때. 사용자는 메시지가 칸을 가린다고 느낍니다",
  ]),
  instead='화면 전체에 해당하는 사정이면 <a href="banner.html">배너</a>, 잠깐 떴다 사라져도 되는 알림이면 <a href="toast.html">토스트</a>, 마우스를 올렸을 때만 보여 주려면 <a href="tooltip.html">툴팁</a>을 씁니다. 입력값을 검사하는 규칙은 <a href="validation.html">입력 검증</a>에서 다룹니다.',
  cases=cases([
    (al("err", "10자리로 적어 주세요", "", "", True, "150px", "사업자번호"), "입력 오류 알리기", "인라인 얼럿을 <b>가장 흔하게</b> 쓰는 자리입니다"),
    (al("warn", "이 설정은 다음 정산부터 적용됩니다", "", "", None, "150px"), "주의할 점 알리기", "하던 일을 막지 않고 주의할 점만 알립니다"),
    (al("info", "정산 주기를 바꾸면 이번 주는 그대로입니다", "", "", True, "150px"), "바꾼 결과 미리 알리기", "설정을 바꾸기 전에 결과를 <b>미리</b> 알립니다"),
  ]),
  code_lede="칸과 메시지는 <code>aria-describedby</code>로 묶고, <code>role=\"alert\"</code>는 오류 메시지에만 붙입니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"biz"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"biz"</span> <span class="a">aria-invalid</span>=<span class="s">"true"</span>
       <span class="a">aria-describedby</span>=<span class="s">"biz-err"</span> <span class="a">value</span>=<span class="s">"123"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"biz-err"</span> <span class="a">class</span>=<span class="s">"inline-alert inline-alert--error"</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;
  사업자번호는 10자리입니다 (지금 3자리)
&lt;/<span class="t">p</span>&gt;

<span class="c">/* 색만으로 알리지 않도록 기호와 글을 함께 둔다 */</span>
.inline-alert--error { <span class="a">color</span>: <span class="a">var</span>(--color-text-danger);
  <span class="a">border</span>: <span class="a">1px</span> solid <span class="a">var</span>(--color-border-danger); }''',
  keys=kbd([
    ("<code>aria-describedby</code>", "스크린 리더가 칸을 읽을 때 <b>오류 이유도 함께</b> 읽어 줍니다"),
    ("<code>aria-invalid</code>", "그 칸의 값이 <b>틀렸다</b>고 알립니다"),
    ("<code>role=\"alert\"</code>", "오류에만 씁니다. 안내에 쓰기에는 <b>지나칩니다</b>"),
    ("제출한 뒤의 초점", "제출했는데 오류가 있으면 <b>첫 번째 틀린 칸</b>으로 초점을 옮깁니다"),
    ("맨 위 요약 목록", "맨 위 요약의 각 줄은 <b>해당 칸으로 가는 링크</b>로 만듭니다"),
    ("확인하는 방법", "Tab으로 칸에 들어가 스크린 리더가 <b>오류 이유를 읽는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("오류를 칸마다 나눠 돌려주기", "<code>{field: \"biz_no\", message: \"10자리\"}</code>처럼 오류 응답에 <b>어느 칸의 오류인지</b> 들어 있어야 화면이 메시지를 붙일 자리를 알 수 있습니다."),
    ("사람이 읽을 문장으로 돌려주기", "응답에 <code>ERR_INVALID_FORMAT</code> 같은 코드만 오면 화면 쪽에서 사용자에게 보여 줄 문장을 따로 만들어야 합니다."),
    ("여러 오류를 한 번에 돌려주기", "오류를 한 번에 모두 돌려주면 사용자가 <b>한 번에 고칠</b> 수 있습니다. 하나씩 돌려주면 고치고 다시 제출하는 왕복이 늘어납니다."),
  ]),
  plat_lede="<b>폼이 있는 화면이면</b> 플랫폼과 상관없이 거의 같은 모양으로 씁니다.",
  plats=plats([
    ("웹", "칸 아래에 적는 글",
     al("err", "10자리로", "", "", True, "110px", "사업자번호"),
     "칸과 메시지를 <code>aria-describedby</code>로 묶는 것이 <b>웹의 표준</b> 방식입니다."),
    ("iOS", "칸 아래에 적는 글",
     '''              <div class="phone" role="img" aria-label="iOS 칸 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:9px;border-radius:3px;border:1px solid var(--danger)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:5px;border-radius:2px;background:color-mix(in srgb,var(--danger) 35%,transparent)"></div></div></div>''',
     "정해진 부품은 없고, 칸 아래에 <b>빨간 글 한 줄</b>을 둡니다."),
    ("안드로이드", "TextField helper/error",
     '''              <div class="phone" role="img" aria-label="안드로이드 칸 오류 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:11px;border-radius:3px;border:1px solid var(--danger)"></div>
                <div style="position:absolute;left:5px;right:5px;top:40px;height:5px;border-radius:2px;background:color-mix(in srgb,var(--danger) 35%,transparent)"></div></div></div>''',
     "텍스트 필드 부품에 <b>오류 글을 넣는 자리</b>가 처음부터 들어 있어서, 오류가 떠도 칸이 움직이지 않습니다."),
  ]),
  plat_note="안드로이드의 텍스트 필드처럼 <b>오류 글 자리를 미리 비워 두는</b> 방식은 웹에서도 그대로 따라 할 만합니다. 자리를 비워 두면 오류가 뜰 때 아래 칸들이 밀려 내려가지 않아 화면이 흔들리지 않습니다. 웹에서는 메시지 자리에 <b>최소 높이</b>를 주면 같은 효과를 얻을 수 있고, 여러 칸에 오류가 한꺼번에 뜰 때 차이가 특히 크게 보입니다.",
  siblings=siblings("inlinealert"),
  related='''        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="banner.html"><b>배너</b><em>6부</em></a></li>
        <li><a href="live.html"><b>라이브 리전</b><em>12부</em></a></li>''',
)
