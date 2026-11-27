# -*- coding: utf-8 -*-
from ax4 import ax
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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">rows — 처음 보이는 줄 수</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">내용만큼 늘어나기 — 작은 창에서 안 굴린다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">남은 글자 수 — 넘치기 전에 보인다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">maxlength — 붙여넣은 글이 소리 없이 잘린다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">resize — 세로만 열어 두는 편이 안전하다</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">Enter 로 보내기와 줄바꿈은 같이 못 쓴다</div>
                </div>
              </div>'''

D = dict(
  slug="textarea", ko="여러 줄 입력", en="Textarea",
  desc="줄바꿈이 있는 글을 받는 칸. 자동 높이, 글자 수, 넘쳤을 때 자르기의 대가.",
  lede="줄바꿈이 들어가는 순간 <b>다른 부품</b>이 됩니다 — 높이가 변하고, 한도가 생기고, Enter 의 뜻이 달라집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>'<b>160자짜리 글 붙여넣기</b>'를 눌러 보세요 — '아예 못 치게'를 켜면
          <b>붙여넣은 글이 소리 없이 잘립니다</b>. 데모가 <b>잘려 나간 글자 수</b>를 세서 적습니다.
          넘치더라도 <b>치게 두고 빨갛게 알리는</b> 쪽이 고치기 쉽습니다.<br>
          <b>내용만큼 늘어나기</b>를 켜면 줄이 늘 때 칸도 같이 커집니다.
          <b>Enter 로 보내기</b>를 메모 칸에 켜면 <b>줄바꿈을 못 하게</b> 됩니다 —
          둘은 같이 쓸 수 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "여러 줄 입력, 텍스트 영역, 메모 칸"),
    ("영어", "textarea, multi-line input, text area"),
    ("같이 쓰는 말",
     "내용만큼 높이가 늘어나는 것을 <b>오토그로</b>(auto-grow), "
     "모서리를 끌어 크기를 바꾸는 손잡이를 <b>리사이저</b>라 합니다. "
     "서식(굵게·목록)이 들어가면 <b>리치 텍스트 편집기</b>로, 전혀 다른 부품이 됩니다."),
    ("자주 잘못 부름",
     "<b>텍스트 필드</b> — <a href=\"field.html\">텍스트 필드</a>는 <b>한 줄</b>입니다.<br>"
     "<b>에디터</b> — 굵게·목록이 들어가면 <b>리치 텍스트</b>라 다른 것입니다.<br>"
     "<b>코드 칸</b> — 들여쓰기·Tab 처리가 달라 따로 만듭니다."),
  ]),
  axes=ax("여러 줄 입력"),
  oneline="<b>한도를 넘기면 자르지 말고 알려 주세요.</b> 잘린 글은 되돌릴 수 없습니다.",
  states=states([
    (ta(['100%', '70%'], "118자 남음", "", "평소", True), "기본", "<b>두세 줄</b>로 시작"),
    (ta(['100%', '100%', '100%', '85%'], "12자 남음", "", "내용만큼 늘어났다", True),
     "늘어남", "<b>안 굴려도</b> 된다"),
    (ta(['100%', '80%'], "20자 넘음", "", "넘쳤다고 알린다", True, "152px", True),
     "넘침", "<b>치게 두고</b> 알린다"),
    (ta(['100%', '60%'], "0자 남음", "", "붙여넣은 20자가 사라졌다", False),
     "잘림", "<b>소리 없이</b> 사라진다"),
    (ta(['100%', '70%'], "", "", "남은 글자 수가 없다", None),
     "글자 수 없음", "<b>넘치고 나서</b> 안다"),
    (one(txt('<span style="display:block;font-size:8px">Enter 로 보내기</span>'
             '<span style="display:block;font-size:8px;color:var(--danger);margin-top:2px">줄바꿈을 못 한다</span>'),
         "Enter", False, "", "152px"),
     "Enter 로 보내기", "<b>둘 다는 못 한다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("<code>rows</code>", "처음 줄 수", "두세 줄로 시작"),
    ("자동 높이", "안 굴림", "내용만큼 커진다"),
    ("글자 수", "미리 보임", "넘치기 <b>전에</b>"),
    ("<code>maxlength</code>", "소리 없이 잘림", "<b>붙여넣기</b>에서 특히"),
    ("<code>resize</code>", "세로만", "가로로 늘면 <b>칸이 깨진다</b>"),
    ("Enter", "둘 중 하나", "보내기 <b>또는</b> 줄바꿈"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>maxlength</code> 는 쉬워 보이지만 <b>붙여넣기에서 가장 나쁩니다</b> —
          길게 써 둔 글을 붙여넣으면 한도까지만 들어가고
          <b>나머지는 아무 말 없이 사라집니다</b>.
          사용자는 다 들어간 줄 알고 보냅니다.<br>
          그래서 한도는 <b>막는 것</b>이 아니라 <b>알리는 것</b>으로 두는 편이 낫습니다 —
          넘치면 빨갛게 하고 보내기를 막되, <b>글은 그대로 두는</b> 것입니다.
          그래야 사용자가 보면서 줄일 수 있습니다.</p>''',
  do=ul([
    "남은 글자 수를 <b>미리</b> 보이기",
    "넘치면 <b>치게 두고</b> 보내기를 막기",
    "<code>resize: vertical</code> 로 <b>세로만</b> 열어 두기",
  ]),
  dont=ul([
    "<code>maxlength</code> 로 <b>잘라 버리기</b>",
    "메모 칸에 <b>Enter 로 보내기</b> 켜기 — 줄바꿈을 못 한다",
    "높이를 <b>한 줄</b>로 두기 — 쓰면서 아무것도 안 보인다",
    "글자 수를 <b>보낸 뒤에</b> 알리기",
  ]),
  instead='한 줄이면 <a href="field.html">텍스트 필드</a>, 서식이 들어가면 리치 텍스트, 검사 규칙은 <a href="validation.html">입력 검증</a>, 문구는 <a href="placeholder.html">자리글과 헬퍼 텍스트</a>.',
  cases=cases([
    (ta(['100%', '70%'], "118자 남음", "", "", True, "150px"), "메모", "<b>줄바꿈</b>이 필요하다"),
    (ta(['100%'], "", "", "", True, "150px"), "댓글", "<b>한 줄</b>로 시작해 늘어난다"),
    (ta(['100%', '100%', '80%'], "", "", "", True, "150px"), "문의 내용", "<b>넉넉하게</b> 연다"),
  ]),
  code_lede="자동 높이는 <code>field-sizing</code> 한 줄, 안 되면 <code>scrollHeight</code> 로 맞춥니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"memo"</span>&gt;정산 메모&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">textarea</span> <span class="a">id</span>=<span class="s">"memo"</span> <span class="a">rows</span>=<span class="s">"3"</span> <span class="a">aria-describedby</span>=<span class="s">"memo-cnt"</span>&gt;&lt;/<span class="t">textarea</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"memo-cnt"</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;118자 남음&lt;/<span class="t">p</span>&gt;

textarea { <span class="a">resize</span>: vertical; <span class="a">field-sizing</span>: content; <span class="a">max-height</span>: <span class="a">14em</span>; }

<span class="c">// field-sizing 을 못 쓰는 곳에서는 — 높이를 재서 맞춘다</span>
el.addEventListener(<span class="s">'input'</span>, () =&gt; {
  el.style.height = <span class="s">'auto'</span>;
  el.style.height = Math.min(<span class="a">240</span>, el.scrollHeight) + <span class="s">'px'</span>;
});''',
  keys=kbd([
    ("Enter", "<b>줄바꿈</b>이 기본이다"),
    ("Shift + Enter", "보내기를 Enter 에 걸었다면 <b>여기로</b> 줄바꿈을 옮긴다"),
    ("Tab", "다음 칸으로 간다 — <b>들여쓰기가 아니다</b>"),
    ("<code>aria-describedby</code>", "글자 수를 칸과 <b>묶어</b> 둔다"),
    ("<code>role=\"status\"</code>", "남은 글자 수를 <b>조용히</b> 알린다"),
    ("확인하는 법", "긴 글을 <b>붙여넣어</b> 잘리는지 본다"),
  ]),
  backend=rows([
    ("한도는 서버에도", "화면의 한도는 친절이고, <b>서버 검사가 진짜</b>입니다."),
    ("줄바꿈 보존", "저장할 때 줄바꿈이 사라지면 <b>쓴 모양</b>이 달라집니다 — 보여 줄 때 <code>white-space: pre-wrap</code> 이 필요합니다."),
    ("글자 수 세는 법", "이모지·한글은 <b>코드 단위</b>로 세면 어긋납니다 — 서버와 화면이 <b>같은 방식</b>으로 세야 합니다."),
  ]),
  plat_lede="<b>자동 높이</b>를 누가 맡는지가 다릅니다.",
  plats=plats([
    ("웹", "&lt;textarea&gt;",
     ta(['100%', '70%'], "118자 남음", "", "", True, "110px"),
     "<code>field-sizing: content</code> 가 생겨 <b>한 줄로</b> 자동 높이가 됩니다."),
    ("iOS", "TextEditor · TextField(axis:)",
     '''              <div class="phone" role="img" aria-label="iOS 여러 줄 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:22px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "<code>TextField(axis: .vertical)</code> 이면 <b>저절로</b> 늘어납니다."),
    ("안드로이드", "TextField(singleLine=false)",
     '''              <div class="phone" role="img" aria-label="안드로이드 여러 줄 칸 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:26px;height:24px;border-radius:4px;border:1px solid var(--line)"></div></div></div>''',
     "<code>maxLines</code> 로 <b>얼마까지 늘어날지</b>를 정합니다."),
  ]),
  plat_note="앱 쪽은 <b>자동 높이가 기본</b>이라 따로 챙길 것이 없는데, 웹에서는 오래도록 자바스크립트로 높이를 재야 했습니다. <code>field-sizing: content</code> 가 그 수고를 없애 주지만 아직 모든 브라우저에 있지는 않아, <b>한동안은 둘 다</b> 써야 합니다. <b>최대 높이</b>를 두는 것은 어느 쪽이든 필요합니다 — 안 두면 긴 글에서 칸이 화면을 다 먹습니다.",
  siblings=siblings("textarea"),
  related='''        <li><a href="field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="placeholder.html"><b>자리글과 헬퍼 텍스트</b><em>14부</em></a></li>
        <li><a href="softkeyboard.html"><b>폰 키보드</b><em>11부</em></a></li>''',
)
