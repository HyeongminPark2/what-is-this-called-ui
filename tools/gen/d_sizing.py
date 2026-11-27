# -*- coding: utf-8 -*-
from ax1 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sz(lab, style, text="정산 내역을 모아 보여 줍니다", w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--accent)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<span style="font-family:var(--mono);font-size:8.5px;color:var(--fg-muted)">' + lab + '</span>'
            '<div style="border:1px dashed var(--line-strong);border-radius:5px;padding:4px;overflow:hidden">'
            '<span style="display:block;box-sizing:border-box;background:var(--accent-soft);border:1px solid ' + col + ';'
            'border-radius:4px;padding:4px 6px;font-size:9px;' + style + '">' + text + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">width   줄어들지 않아 좁은 칸에서 넘침</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">max-width   칸이 좁아지면 함께 줄어듦</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">min-content   가장 긴 낱말만큼</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">max-content   끊지 않고 한 줄로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">fit-content   내용만큼 쓰되 칸은 넘지 않음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">clamp(최소, 기본, 최대)   세 값을 한 줄로</div>
                </div>
              </div>'''

D = dict(
  slug="sizing", ko="크기 정하기", en="Sizing",
  desc="width·max-width와 min-content·max-content·fit-content·clamp를 비교하고, 칸이 좁아질 때 어떤 값이 줄어들지 않고 넘치는지 보여 주는 항목입니다.",
  lede="크기를 정하는 값은 여럿이지만, 서로 갈리는 지점은 <b>칸이 좁아질 때 함께 줄어드는가</b> 하나입니다.",
  axes_lede="뼈대는 눈에 보이지 않지만 <b>모든 화면의 배치</b>를 정합니다. 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>칸 폭을 좁히면서 <b>어떤 값이 넘치는지</b> 보세요. 넘친 줄은 빨갛게 표시됩니다.<br>
          <code>width: 300px</code>은 줄어들지 않아서 넘치고, <code>max-width: 300px</code>은 칸과 함께 줄어듭니다.
          글을 <b>끊기지 않는 긴 낱말</b>로 바꾸면 더 많은 값이 칸을 넘칩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "크기, 폭, 최소·최대 크기, 내용 기준 크기"),
    ("영어", "sizing, intrinsic sizing, min-content / max-content / fit-content, clamp()"),
    ("같이 쓰는 말",
     "내용이 크기를 정하는 방식은 <b>내용 기준 크기</b>(intrinsic sizing)라고 하고, "
     "<code>min-content</code>·<code>max-content</code>·<code>fit-content</code>가 이 방식의 값입니다. "
     "최소·기본·최대를 한 줄로 적는 함수는 <code>clamp()</code>이고, "
     "테두리와 패딩을 크기에 넣을지는 <code>box-sizing</code>이 정합니다."),
    ("자주 잘못 부르는 이름",
     "<b>반응형</b> — 폭에 따라 배치를 바꾸는 것은 <a href=\"breakpoint.html\">브레이크포인트</a>입니다. 크기 값은 브레이크포인트로 <b>끊지 않아도</b> 폭에 따라 달라집니다.<br>"
     "<b>종횡비</b> — <a href=\"aspectratio.html\">종횡비</a>는 폭에 따라 <b>높이</b>를 정하는 값입니다.<br>"
     "<b>컨테이너</b> — <a href=\"../items/container.html\">컨테이너와 최대 폭</a>은 이 값들을 활용하는 <b>패턴 하나</b>입니다."),
  ]),
  axes=ax("크기 정하기"),
  oneline="<b>폭은 대부분 <code>width</code>가 아니라 <code>max-width</code>로 적습니다.</b> 이 차이 하나로 반응형 화면에서 생기는 넘침 문제의 상당수가 해결됩니다.",
  s4_title="크기를 정하는 여섯 가지 값", s4_hint="칸이 좁아질 때 값마다 달라지는 결과",
  do_title="상황에 맞는 크기 값 고르기",
  dont_title="크기를 정할 때 피할 것",
  instead_title="크기 정하기와 함께 보면 좋은 항목",
  states=states([
    (sz("width: 300px", "width:300px", "정산 내역", "152px", "줄어들지 않아 넘침", False), "<code>width</code>로 고정할 때", "칸 폭을 <b>무시하고</b> 넘칩니다"),
    (sz("max-width: 300px", "max-width:300px", "정산 내역을 모아 보여 줍니다", "152px", "칸과 함께 줄어듦", True), "<code>max-width</code>로 상한만 둘 때", "<b>대부분 이쪽</b>이 맞습니다"),
    (sz("min-content", "width:min-content", "정산 내역을 모아", "152px", "가장 긴 낱말만큼"), "<code>min-content</code>로 둘 때", "줄이 자주 바뀌어 <b>세로로 길어집니다</b>"),
    (sz("max-content", "width:max-content", "정산 내역을 모아 보여 줍니다", "152px", "끊지 않고 한 줄로", False), "<code>max-content</code>로 둘 때", "줄을 바꾸지 않아서 <b>칸을 넘기 쉽습니다</b>"),
    (sz("fit-content", "width:fit-content", "정산 내역", "152px", "내용만큼 쓰되 칸 안에서", True), "<code>fit-content</code>로 둘 때", "<b>내용만큼</b> 차지하되 <b>칸을 넘지는 않습니다</b>"),
    (sz("clamp(80px, 50%, 300px)", "width:clamp(80px, 50%, 300px)", "정산 내역", "152px", "최소·기본·최대를 한 줄로", True),
     "<code>clamp()</code>로 범위를 줄 때", "최소·기본·최대 세 값을 <b>한 줄에</b> 적습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("width", "줄어들지 않음", "칸이 좁아지면 <b>넘칩니다</b>"),
    ("max-width", "함께 줄어듦", "반응형 화면에서 <b>기본으로 쓰는 값</b>입니다"),
    ("min-content", "가장 긴 낱말", "더는 줄일 수 없는 폭입니다"),
    ("max-content", "줄을 바꾸지 않음", "칸을 <b>넘기 쉬워서</b> 표 칸 정도에만 씁니다"),
    ("fit-content", "내용만큼, 칸 안에서", "내용만큼 쓰되 <b>칸을 넘지 않습니다</b>"),
    ("clamp()", "최소·기본·최대", "<b>한 줄로</b> 세 값을 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>플렉스·그리드 자식에는 숨은 최소 크기가 있습니다.</b>
          기본값이 <code>min-width: auto</code>라서
          <b>내용보다 작아지지 않기</b> 때문에, 긴 글이나 긴 낱말이 들어가면
          칸이 줄지 않고 <b>통째로 넘칩니다</b>.
          <code>min-width: 0</code> 한 줄을 주면 이 최소 크기가 풀립니다.
          <a href="../items/flex.html">플렉스</a>·<a href="../items/grid.html">그리드</a>에서
          되풀이해 나오는 그 한 줄이고,
          <a href="../items/truncate.html">말줄임</a>이 걸리지 않는 이유이기도 합니다.</p>''',
  do=ul([
    "폭을 정할 때. <b>대부분 <code>max-width</code></b>로 적습니다",
    "버튼이나 칩처럼 내용만큼만 차지해야 할 때. <code>fit-content</code>를 씁니다",
    "글줄 길이를 정할 때. <code>clamp()</code>나 <code>ch</code> 단위를 씁니다",
  ]),
  dont=ul([
    "<code>width</code>로 폭을 고정할 때. <b>좁은 화면에서 넘칩니다</b>",
    "<code>max-content</code>를 본문에 쓸 때. 글이 줄을 바꾸지 않고 한 줄로 늘어납니다",
    "플렉스 자식에 <code>min-width: 0</code>을 빠뜨릴 때",
    "높이를 고정할 때. <a href=\"textzoom.html\">글자를 키우면 잘립니다</a>",
  ]),
  instead='폭에 맞춰 높이를 정하는 방법은 <a href="aspectratio.html">종횡비</a>에서, 읽기 좋은 글줄 길이는 <a href="../items/container.html">컨테이너</a>에서 다룹니다. 내용이 넘쳤을 때 어떻게 처리할지는 <a href="../items/overflow.html">넘침</a>에서 봅니다.',
  cases=cases([
    (sz("max-width: 68ch", "max-width:68ch", "읽기 좋은 글줄 길이", "150px", "글줄은 ch로"), "본문 글줄 길이 정하기", "자세한 내용은 <a href=\"../items/container.html\">컨테이너</a>에서 다룹니다"),
    (sz("fit-content", "width:fit-content", "저장", "150px", "내용만큼"), "버튼·칩을 글자 길이만큼 두기", "<b>글자 길이만큼만</b> 차지합니다"),
    (sz("clamp(16px, 4vw, 40px)", "width:clamp(16px, 4vw, 40px);min-height:16px", "", "150px", "폭에 따라 커지되 상한이 있음"),
     "여백·아이콘을 폭에 맞춰 늘리기", "폭에 따라 늘리되 <b>상한을 둡니다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="크기를 정할 때 지킬 것",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="<code>max-width</code>를 기본으로 두고, 플렉스 자식에는 <code>min-width: 0</code>을 잊지 않습니다.",
  code='''<span class="c">/* 대부분 이쪽 */</span>
.panel { <span class="a">max-width</span>: <span class="a">480px</span>; <span class="a">width</span>: <span class="a">100%</span>; }

<span class="c">/* 글줄 길이는 글자 수로 */</span>
.prose { <span class="a">max-width</span>: <span class="a">68ch</span>; }

<span class="c">/* 버튼 · 칩은 내용만큼만 */</span>
.chip { <span class="a">width</span>: fit-content; }

<span class="c">/* 최소 · 기본 · 최대를 한 줄로 */</span>
.gap { <span class="a">padding-inline</span>: <span class="a">clamp</span>(<span class="a">16px</span>, <span class="a">4vw</span>, <span class="a">40px</span>); }

<span class="c">/* 플렉스 · 그리드 자식의 숨은 최소 크기를 푼다 */</span>
.row &gt; * { <span class="a">min-width</span>: <span class="a">0</span>; }''',
  keys=kbd([
    ("<code>box-sizing: border-box</code> 쓰기", "테두리와 패딩을 크기에 넣습니다. <b>넣지 않으면 계산이 어긋납니다</b>"),
    ("플렉스·그리드 자식에 <code>min-width: 0</code> 주기", "플렉스·그리드 자식의 <b>숨은 최소 크기</b>를 풉니다"),
    ("글줄 길이는 <code>ch</code> 단위로 정하기", "글자 폭을 기준으로 하기 때문에 <b>글줄 길이</b>를 정하기에 알맞습니다"),
    ("<code>clamp()</code>의 가운데 값에 <code>rem</code> 섞기", "<code>vw</code>만 쓰면 <a href=\"textzoom.html\">글자를 키워도</a> 커지지 않으므로 <code>rem</code>을 섞습니다"),
    ("높이는 <code>min-height</code>로 주기", "높이를 고정하면 글이 커질 때 <b>잘립니다</b>"),
    ("<code>max-content</code>로 가로 스크롤을 만들지 않기", "글이 한 줄로 늘어나 <b>가로 스크롤</b>이 생기면 화면을 확대한 사람이 읽기 어렵습니다"),
  ]),
  backend=rows([
    ("가장 긴 실제 값으로 확인하기", "시안은 보통 짧은 글로 그려지기 때문에, <b>가장 긴 실제 값</b>으로 한 번 채워 보면 어디가 깨지는지 보입니다."),
    ("번역하면 달라지는 글 길이", "같은 뜻이라도 언어마다 글 길이가 다르기 때문에, <code>width</code>로 고정해 두면 <b>다른 언어에서 레이아웃이 깨집니다</b>."),
  ]),
  plat_lede="<b>내용이 크기를 정하게</b> 한다는 생각은 세 플랫폼 모두 같습니다.",
  plats=plats([
    ("웹", "max-width · clamp",
     sz("max-width", "max-width:100px", "정산", "110px"),
     "<code>min-content</code>·<code>fit-content</code> 같은 <b>내용 기준 값</b>이 표준에 있습니다."),
    ("iOS", "frame · layoutPriority",
     '''              <div class="phone" role="img" aria-label="iOS 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:14px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<code>.frame(maxWidth:)</code>가 <code>max-width</code>에 해당하고, 레이아웃 우선순위로 어느 뷰가 먼저 줄어들지 정합니다."),
    ("안드로이드", "weight · wrapContent",
     '''              <div class="phone" role="img" aria-label="안드로이드 크기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;height:14px;border-radius:3px;background:var(--accent-soft);border:1px solid var(--accent)"></div></div></div>''',
     "<code>wrapContent</code>가 <code>fit-content</code>, <code>weight</code>가 <code>flex: 1</code>에 해당합니다."),
  ]),
  plat_note="\"좁은 화면에서 삐져나와요\"라는 문제는 거의 다 <code>width</code>를 써서 생깁니다. 시안에 '폭 300'이라고 적혀 오면 그대로 <code>width: 300px</code>로 옮기기 쉽지만, 대개는 <b>'최대 300'</b>이라는 뜻입니다. 핸드오프할 때 <b>어느 쪽인지</b> 한 번 물어보면 이런 수정 요청이 오가는 일이 없어집니다.",
  siblings=siblings("sizing"),
  related='''        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/truncate.html"><b>말줄임</b><em>3부</em></a></li>
        <li><a href="textzoom.html"><b>확대와 글자 크기</b><em>12부</em></a></li>''',
)
