# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ta(lines, cnt="", label="", note="", ok=None, w="152px", over=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    body = ''.join('<span style="display:block;height:4px;border-radius:2px;background:var(--bg);'
                   'width:' + wd + '"></span>' for wd in lines)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="display:grid;gap:3px;border:1px solid ' + ('var(--danger)' if over else c) + ';'
            'border-radius:4px;background:var(--surface);padding:5px">' + body + '</span>'
            + ('<span style="font-size:7.5px;text-align:right;color:' + ('var(--danger)' if over else 'var(--fg-muted)') + '">' + cnt + '</span>' if cnt else '')
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">rows는 처음 보이는 줄 수</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">내용만큼 늘어나 작은 창에서 굴리지 않음</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">남은 글자 수는 넘치기 전에 보여 줌</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">maxlength는 붙여넣은 글을 안내 없이 자름</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">resize는 세로만 열어 두는 편이 안전함</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">Enter 하나로 보내기와 줄바꿈을 같이 못 씀</div>
                </div>
              </div>'''

D = dict(
  slug="textarea", ko="여러 줄 입력", en="Textarea",
  desc="줄바꿈이 들어가는 글을 받는 여러 줄 입력에서 자동 높이와 글자 수, 넘친 글을 잘랐을 때 생기는 문제를 다루는 항목입니다.",
  lede="입력 칸에 줄바꿈이 들어가면 한 줄 칸과는 <b>다른 부품</b>이 됩니다. 글이 길어지면 높이가 변하고, 글자 수 한도를 다뤄야 하고, Enter를 눌렀을 때 하는 일도 달라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>160자짜리 글 붙여넣기</b>'를 눌러 보세요. '넘치면 아예 못 치게 막기'를 켜 두면
          <b>붙여넣은 글이 아무 안내 없이 잘리고</b>, 데모가 <b>잘려 나간 글자 수</b>를 세어 적어 줍니다.
          한도를 넘더라도 <b>글은 그대로 두고 빨갛게 알리는</b> 편이 사용자가 고치기 쉽습니다.<br>
          <b>내용만큼 늘어나기</b>를 켜면 줄이 늘 때 칸도 함께 커집니다.
          반면 메모 칸에 <b>Enter로 보내기</b>를 켜면 Enter가 보내기에 쓰이기 때문에 <b>줄바꿈을 할 수 없게</b> 됩니다.
          두 기능은 같은 키를 쓰므로 함께 쓸 수 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "여러 줄 입력, 텍스트 영역, 메모 칸"),
    ("영어", "textarea, multi-line input, text area"),
    ("같이 쓰는 말",
     "내용만큼 높이가 늘어나는 것은 <b>오토그로</b>(auto-grow), "
     "모서리를 끌어 크기를 바꾸는 손잡이는 <b>리사이저</b>라고 부릅니다. "
     "굵게나 목록 같은 서식이 들어가면 <b>리치 텍스트 편집기</b>라는 전혀 다른 부품이 됩니다."),
    ("자주 잘못 부르는 이름",
     "<b>텍스트 필드</b> — <a href=\"field.html\">텍스트 필드</a>는 <b>한 줄</b>만 받는 칸입니다.<br>"
     "<b>에디터</b> — 굵게나 목록 같은 서식이 들어가면 여러 줄 입력이 아니라 <b>리치 텍스트</b> 편집기입니다.<br>"
     "<b>코드 칸</b> — 코드를 받는 칸은 들여쓰기와 Tab 키를 다르게 처리해야 해서 따로 만듭니다."),
  ]),
  states=states([
    (ta(['100%', '70%'], "118자 남음", "", "처음 연 모습", True), "평소 상태", "<b>두세 줄</b> 높이로 시작합니다"),
    (ta(['100%', '100%', '100%', '85%'], "12자 남음", "", "내용만큼 늘어남", True),
     "내용이 길어져 칸이 늘어났을 때", "칸이 내용만큼 커져서 <b>굴리지 않아도</b> 됩니다"),
    (ta(['100%', '80%'], "20자 넘음", "", "넘쳤다고 알림", True, "152px", True),
     "한도를 넘었을 때 알리기", "한도를 넘어도 <b>계속 치게 두고</b> 넘쳤다고 알립니다"),
    (ta(['100%', '60%'], "0자 남음", "", "붙여넣은 20자가 사라짐", False),
     "넘친 글을 잘랐을 때", "한도를 넘은 글이 <b>아무 안내 없이</b> 사라집니다"),
    (ta(['100%', '70%'], "", "", "남은 글자 수가 안 보임", None),
     "남은 글자 수를 보여 주지 않을 때", "남은 글자 수가 안 보여서 <b>넘친 뒤에야</b> 알게 됩니다"),
    (one(txt('<span style="display:block;font-size:8px">Enter 로 보내기</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">줄바꿈을 못 함</span>'),
         "Enter", False, "", "152px"),
     "Enter에 보내기를 걸었을 때", "Enter 하나로 보내기와 줄바꿈을 <b>둘 다 할 수는 없습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>rows</code>", "처음 보이는 줄 수", "처음에는 두세 줄 높이로 시작합니다"),
    ("자동 높이", "굴리지 않게 하기", "칸이 내용만큼 커지므로 작은 창 안에서 굴리지 않아도 됩니다"),
    ("글자 수", "미리 보여 주기", "남은 글자 수를 넘치기 <b>전에</b> 보여 줍니다"),
    ("<code>maxlength</code>", "안내 없이 잘림", "한도를 넘는 글을 자르는데, <b>붙여넣기</b>에서 특히 문제가 됩니다"),
    ("<code>resize</code>", "세로로만 늘리기", "가로로 늘리게 두면 <b>칸이 레이아웃을 깨뜨립니다</b>"),
    ("Enter", "한 가지 일만 맡기기", "Enter에는 보내기 <b>또는</b> 줄바꿈 중 하나만 맡깁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>maxlength</code>는 쓰기 쉬워 보이지만 <b>붙여넣기에서 문제가 가장 큽니다</b>.
          다른 곳에 길게 써 둔 글을 붙여넣으면 한도까지만 들어가고
          <b>나머지는 아무 안내 없이 사라지기</b> 때문에,
          사용자는 글이 다 들어간 줄 알고 그대로 보냅니다.<br>
          그래서 한도는 입력을 <b>막는 데</b> 쓰지 말고 <b>알리는 데</b> 쓰는 편이 낫습니다.
          글이 넘치면 칸을 빨갛게 표시하고 보내기를 막되, <b>쓴 글은 그대로 둡니다</b>.
          그래야 사용자가 전체 글을 보면서 어디를 줄일지 고를 수 있습니다.</p>''',
  do=ul([
    "남은 글자 수를 <b>미리</b> 보여 주기",
    "한도를 넘어도 <b>치게 두고</b> 보내기만 막기",
    "<code>resize: vertical</code>로 크기 조절을 <b>세로만</b> 열어 두기",
  ]),
  dont=ul([
    "<code>maxlength</code>로 넘친 글을 <b>잘라 버리기</b>",
    "메모 칸에 <b>Enter로 보내기</b> 켜기. 줄바꿈을 할 수 없게 됩니다",
    "높이를 <b>한 줄</b>로 두기. 쓰는 동안 앞에 쓴 내용이 보이지 않습니다",
    "글자 수가 넘쳤다는 사실을 <b>보낸 뒤에</b> 알리기",
  ]),
  instead='한 줄만 받으면 되는 칸에는 <a href="field.html">텍스트 필드</a>를 쓰고, 굵게나 목록 같은 서식이 들어가야 하면 리치 텍스트 편집기를 씁니다. 글자 수 같은 검사 규칙은 <a href="validation.html">입력 검증</a>에서, 칸 안팎에 적는 안내 문구는 <a href="placeholder.html">자리글과 헬퍼 텍스트</a>에서 다룹니다.',
  cases=cases([
    (ta(['100%', '70%'], "118자 남음", "", "", True, "150px"), "메모 적기", "여러 줄로 적어야 하므로 <b>줄바꿈</b>이 필요합니다"),
    (ta(['100%'], "", "", "", True, "150px"), "댓글 달기", "<b>한 줄</b> 높이로 시작해 글이 길어지면 늘어납니다"),
    (ta(['100%', '100%', '80%'], "", "", "", True, "150px"), "문의 내용 받기", "긴 글이 들어올 자리라서 처음부터 <b>넉넉한 높이</b>로 엽니다"),
  ]),
  code_lede="자동 높이는 CSS <code>field-sizing</code> 한 줄로 만들 수 있고, 이 속성을 지원하지 않는 브라우저에서는 <code>scrollHeight</code>를 재서 높이를 맞춥니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"memo"</span>&gt;정산 메모&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">textarea</span> <span class="a">id</span>=<span class="s">"memo"</span> <span class="a">rows</span>=<span class="s">"3"</span> <span class="a">aria-describedby</span>=<span class="s">"memo-cnt"</span>&gt;&lt;/<span class="t">textarea</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"memo-cnt"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;118자 남음&lt;/<span class="t">p</span>&gt;

textarea { <span class="a">resize</span>: vertical; <span class="a">field-sizing</span>: content; <span class="a">max-height</span>: <span class="a">14em</span>; }

<span class="c">// field-sizing을 못 쓰는 곳에서는 높이를 재서 맞춘다</span>
el.addEventListener(<span class="s">'input'</span>, () =&gt; {
  el.style.height = <span class="s">'auto'</span>;
  el.style.height = Math.min(<span class="a">240</span>, el.scrollHeight) + <span class="s">'px'</span>;
});''',
  keys=kbd([
    ("Enter", "기본 동작은 <b>줄바꿈</b>입니다"),
    ("Shift + Enter", "Enter에 보내기를 걸었다면 줄바꿈을 <b>이 조합으로</b> 옮깁니다"),
    ("Tab", "다음 칸으로 넘어갑니다. <b>들여쓰기가 아닙니다</b>"),
    ("<code>aria-describedby</code>", "글자 수 안내를 칸과 <b>연결해</b> 둡니다"),
    ("<code>role=\"status\"</code>", "남은 글자 수를 입력을 방해하지 않고 <b>조용히</b> 알립니다"),
    ("확인하는 방법", "긴 글을 <b>붙여넣어</b> 보고 잘리는지 확인합니다"),
  ]),
  backend=rows([
    ("글자 수 한도는 서버에서도 검사하기", "화면에 보이는 한도는 사용자를 돕는 안내이고, 실제로 넘친 글을 막는 일은 <b>서버 검사</b>가 맡아야 합니다."),
    ("줄바꿈을 그대로 지키기", "저장하거나 보여 줄 때 줄바꿈이 사라지면 사용자가 <b>쓴 모양</b>과 달라집니다. 화면에 보여 줄 때는 <code>white-space: pre-wrap</code>이 필요합니다."),
    ("글자 수를 세는 방법 맞추기", "이모지나 한글을 <b>코드 단위</b>로 세면 사람이 보는 글자 수와 어긋납니다. 서버와 화면이 <b>같은 방식</b>으로 세야 한도가 맞습니다."),
  ]),
  plat_lede="플랫폼마다 <b>자동 높이</b>를 누가 맡는지가 다릅니다.",
  plats=plats([
    ("웹", "&lt;textarea&gt;",
     ta(['100%', '70%'], "118자 남음", "", "", True, "110px"),
     "<code>field-sizing: content</code> 속성이 생겨서 CSS <b>한 줄로</b> 자동 높이를 만들 수 있습니다."),
    ("iOS", "TextEditor · TextField(axis:)",
     '''              <div class="phone" role="img" aria-label="iOS 여러 줄 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:22px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "<code>TextField(axis: .vertical)</code>로 만들면 내용만큼 <b>저절로</b> 늘어납니다."),
    ("안드로이드", "TextField(singleLine=false)",
     '''              <div class="phone" role="img" aria-label="안드로이드 여러 줄 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:24px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "<code>maxLines</code>로 칸이 <b>몇 줄까지 늘어날지</b>를 정합니다."),
  ]),
  plat_note="앱에서는 <b>자동 높이가 기본</b>이라 따로 챙길 것이 없지만, 웹에서는 오랫동안 자바스크립트로 높이를 재서 맞춰야 했습니다. <code>field-sizing: content</code>를 쓰면 그 코드가 필요 없지만 아직 모든 브라우저가 지원하지는 않으므로, <b>한동안은 두 방법을 함께</b> 써야 합니다. 어느 플랫폼이든 <b>최대 높이</b>는 정해 두어야 합니다. 최대 높이가 없으면 글이 길어질 때 칸이 화면 전체를 차지합니다.",
  siblings=siblings("textarea"),
  related='''        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="placeholder.html"><b>자리글과 헬퍼 텍스트</b><em>14부</em></a></li>
        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>''',
)
