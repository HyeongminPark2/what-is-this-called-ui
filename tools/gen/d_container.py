# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def cont(inner_w="60%", w="170px", label="", mark=""):
    return ('              <div style="width:100%;max-width:' + w + ';background:var(--bg);border:1px dashed var(--line-strong);'
            'border-radius:6px;padding:7px">'
            '<div style="width:' + inner_w + ';margin-inline:auto;background:var(--accent-soft);border:1px dashed var(--accent);'
            'border-radius:4px;padding:6px;font-size:9.5px;line-height:1.7;color:var(--accent)">' + (label or '내용') + '</div>'
            + (('<div style="font-family:var(--mono);font-size:9px;color:var(--fg-muted);margin-top:5px;text-align:center">' + mark + '</div>') if mark else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:250px;background:var(--surface);border:1px dashed var(--line-strong);border-radius:7px;padding:9px">
                    <div class="pin-out" data-pin="2" style="max-width:160px;margin-inline:auto;background:var(--accent-soft);border:1px dashed var(--accent);border-radius:5px;padding:8px;font-size:10.5px;line-height:1.8;color:var(--accent);margin-left:26px">글줄이 너무 길면 눈이 다음 줄의 첫 글자를 못 찾습니다.</div>
                  </div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">max-width: 65ch</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">margin-inline: auto</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">padding-inline: 16px   — 좁은 화면의 양옆</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">width: 1200px   — 좁은 화면에서 가로 스크롤</div>
                </div>
              </div>'''

D = dict(
  slug="container", ko="컨테이너와 최대 폭", en="Container · max-width",
  desc="내용이 들어가는 가운데 칸을 만드는 두 줄과 글줄 길이 상한, width 와 max-width 의 차이를 보여주는 항목.",
  lede="내용이 들어가는 <b>가운데 칸</b>. 거의 모든 사이트가 <b>같은 두 줄</b>로 만듭니다 — 상한을 걸고 가운데에 둡니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 움직이면 <b>한 줄에 실제로 몇 글자가 들어가는지</b>를 재서 알려 줍니다.
          읽는 글은 <b>45~75자</b>가 편합니다.<br>
          <b>상한 없애기</b>를 켜 보세요. 넓은 화면에서 글줄이 끝까지 늘어나
          다음 줄의 첫 글자를 눈이 못 찾게 됩니다 — 긴 글을 읽기 힘든 이유가 글꼴이 아니라
          <b>줄 길이</b>일 때가 많습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "컨테이너, 최대 폭, 가운데 칸, 래퍼"),
    ("영어", "container, wrapper, max-width, measure, line length"),
    ("같이 쓰는 말",
     "한 줄의 글자 수를 <b>글줄 길이</b>(measure · line length)라 하고, "
     "폭을 재는 단위 <b><code>ch</code></b>는 글꼴의 '0' 한 글자 너비입니다. "
     "화면 양옆에 남기는 여백은 <b>거터</b>나 <b>페이지 마진</b>, "
     "폭에 따라 짜임을 바꾸는 것은 <b>컨테이너 쿼리</b>(container query)입니다."),
    ("자주 잘못 부름",
     "<b><code>width</code>와 <code>max-width</code></b> — <code>width: 1200px</code>은 <b>좁은 화면에서도 1200px</b>이라 "
     "가로 스크롤이 생깁니다. <code>max-width</code>는 '이보다 커지지만 마라'입니다.<br>"
     "<b>컨테이너 쿼리</b> — 부모 폭에 반응하는 다른 기능입니다. 이름만 비슷합니다.<br>"
     "<b>컨테이너</b>(도커) — 완전히 다른 말입니다."),
  ]),
  axes=ax("컨테이너와 최대 폭"),
  oneline="컨테이너는 <b>'이보다 넓어지지 마라'</b>입니다. <code>width</code>로 못 박으면 좁은 화면이 깨지고, <code>max-width</code>면 알아서 줄어듭니다.",
  s4_title="상태", s4_hint="화면 폭이 바뀌면 달라진다",
  states=states([
    (cont("100%", "170px", "넓은 화면에서 상한에 걸린 모습", "max-width 에서 멈춤"), "넓은 화면", "<b>상한에서 멈추고</b> 양옆에 여백이 남는다"),
    (cont("100%", "120px", "좁아지면 상한은 아무 일도 안 한다", "폭을 다 쓴다"), "좁은 화면", "상한이 안 걸린다. <b>양옆 패딩만</b> 남는다"),
    (cont("100%", "170px", "상한이 없으면 끝까지 늘어나 읽기 힘들어집니다. 눈이 다음 줄을 못 찾습니다.", "상한 없음"), "상한 없음", "글줄이 길어져 <b>다음 줄을 못 찾는다</b>"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;overflow-x:auto">
                <div style="width:230px;background:var(--warn-soft);border:1px dashed var(--warn);border-radius:4px;padding:6px;font-size:9.5px;color:var(--warn)">width: 230px 로 못 박음</div>
              </div>''',
     "width 로 못 박기", "<b>좁은 화면에서 가로 스크롤</b>. 거의 늘 틀린 선택"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;display:grid;gap:5px">
                <div style="background:var(--accent-soft);border:1px dashed var(--accent);border-radius:4px;padding:5px;font-size:9px;color:var(--accent);text-align:center">읽는 글 · 65ch</div>
                <div style="background:var(--bg);border:1px dashed var(--line-strong);border-radius:4px;padding:5px;font-size:9px;color:var(--fg-muted);text-align:center">표 · 더 넓게</div>
              </div>''',
     "두 겹 상한", "읽는 글은 좁게, <b>표나 그리드는 넓게</b> — 상한이 하나일 필요는 없다"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px">
                <div style="background:var(--accent-soft);border:1px dashed var(--accent);border-radius:4px;padding:6px;font-size:9.5px;color:var(--accent)">가운데 칸 안의 사진만 끝까지</div>
                <div style="margin:5px -7px 0;height:22px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 6px,var(--ink-050) 6px 12px);border-radius:2px"></div>
              </div>''',
     "밖으로 빼기", "사진·배경만 <b>상한을 넘겨</b> 끝까지 보내는 기법"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바깥 칸", "page", "화면 전체. 여기엔 폭 제한을 두지 않는다"),
    ("컨테이너", "container · wrapper", "내용이 들어가는 가운데 칸. <b>이것 하나가 사이트의 뼈대</b>다"),
    ("최대 폭", "max-width", "'이보다 넓어지지 마라'. 읽는 글은 <code>65ch</code>쯤"),
    ("가운데 두기", "margin-inline: auto", "남은 자리를 양옆에 똑같이 나눈다. <b>가로 전용</b>"),
    ("양옆 패딩", "padding-inline", "좁은 화면에서 글이 <b>가장자리에 붙지 않게</b>. 빠뜨리기 쉽다"),
    ("못 박힌 폭", "width (쓰지 않는다)", "<code>width: 1200px</code>은 좁은 화면에서 <b>가로 스크롤</b>을 만든다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          상한은 <b>하나일 필요가 없습니다.</b> 읽는 글은 65ch 쯤으로 좁게, 카드 그리드나 표는
          1200px 쯤으로 넓게 — 같은 페이지에서 <b>두세 겹</b>을 쓰는 것이 보통입니다.
          '컨테이너 하나로 전부'라고 정해 두면 글이 너무 넓거나 표가 너무 좁아집니다.</p>''',
  do=ul([
    "<b>읽는 글</b>이 있는 모든 화면 — 기사, 설명, 약관",
    "넓은 모니터에서 내용이 <b>끝까지 늘어나면 안 될</b> 때",
    "화면마다 양옆 여백을 <b>똑같이</b> 맞추고 싶을 때",
  ]),
  dont=ul([
    "<code>width</code>로 못 박는 것 — <b>좁은 화면에서 가로 스크롤</b>이 생깁니다",
    "배경색·배경 이미지까지 가두는 것 — 배경은 끝까지 가고 <b>내용만</b> 가둡니다",
    "표·그리드까지 좁은 상한에 넣는 것 — 열이 다닥다닥 붙습니다",
    "양옆 패딩을 빠뜨리는 것 — 폰에서 글이 <b>가장자리에 닿습니다</b>",
  ]),
  instead='글줄 길이 자체는 <a href="../items/typescale.html">타입 스케일</a>과 함께 보고, 칸을 나누는 일은 <a href="grid.html">그리드</a>가 맡습니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;background:var(--bg);border-radius:6px;padding:6px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:7px;max-width:140px;margin-inline:auto">
                  <span style="font-size:10.5px;font-weight:700;display:block">기사 제목</span>
                  <span style="font-size:9.5px;color:var(--fg-muted);line-height:1.7">본문이 65ch 를 넘지 않습니다.</span>
                </div>
              </div>''',
     "읽는 글", "<code>65ch</code>. <b>글꼴이 커지면 상한도 같이</b> 커진다"),
    ('''              <div style="width:100%;max-width:190px;background:var(--bg);border-radius:6px;padding:6px">
                <div style="max-width:175px;margin-inline:auto;display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px">
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                </div>
              </div>''',
     "카드 그리드", "같은 페이지라도 <b>상한을 더 넓게</b>"),
    ('''              <div style="width:100%;max-width:190px;border-radius:6px;overflow:hidden">
                <div style="height:24px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 6px,var(--ink-050) 6px 12px)"></div>
                <div style="background:var(--bg);padding:6px">
                  <div style="max-width:130px;margin-inline:auto;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:6px;font-size:9.5px">내용만 가둔다</div>
                </div>
              </div>''',
     "배경은 끝까지", "<b>배경은 화면 전체, 내용만 가운데.</b> 가장 흔한 짜임"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="사이트의 뼈대 두 줄",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="거의 모든 사이트가 <b>이 네 줄</b>을 갖고 있습니다.",
  code='''<span class="t">.container</span> {
  <span class="a">max-width</span>: <span class="a">1200px</span>;        <span class="c">/* width 가 아니다 */</span>
  <span class="a">margin-inline</span>: auto;      <span class="c">/* 가운데로 */</span>
  <span class="a">padding-inline</span>: <span class="a">16px</span>;    <span class="c">/* 좁은 화면의 양옆 */</span>
}

<span class="c">/* 읽는 글은 더 좁게 — 한 줄 45~75자 */</span>
<span class="t">.prose</span> { <span class="a">max-width</span>: <span class="a">65ch</span>; }

<span class="c">/* 요즘 방식 — 한 줄로 */</span>
<span class="t">.container</span> { <span class="a">width</span>: <span class="t">min</span>(<span class="a">100%</span> - <span class="a">32px</span>, <span class="a">1200px</span>); <span class="a">margin-inline</span>: auto; }

<span class="c">/* 안에서 하나만 끝까지 내보내기 */</span>
<span class="t">.full-bleed</span> { <span class="a">margin-inline</span>: <span class="t">calc</span>(<span class="a">50%</span> - <span class="a">50vw</span>); }''',
  keys=kbd([
    ("<code>max-width</code>를 쓴다", "<code>width</code>로 못 박으면 <b>좁은 화면에서 가로 스크롤</b>이 생긴다"),
    ("양옆 패딩을 잊지 않는다", "없으면 폰에서 글이 <b>가장자리에 닿는다</b>"),
    ("읽는 글은 <code>ch</code>로", "글꼴 크기가 바뀌면 상한도 같이 바뀐다. px 로 적으면 안 따라온다"),
    ("상한은 여러 겹", "글은 좁게, 표·그리드는 넓게. <b>하나로 통일하지 않는다</b>"),
    ("배경은 가두지 않는다", "배경색·배경 이미지는 화면 전체, <b>내용만</b> 컨테이너 안에"),
    ("<code>margin-inline</code>", "<code>margin: 0 auto</code>보다 또렷하고, 글 방향이 바뀌어도 맞는다"),
  ]),
  backend=rows([
    ("컨테이너 = 레이아웃의 상수", "폭 값 하나가 <b>모든 화면</b>에 걸립니다. 토큰으로 빼 두면(<code>--container</code>) 나중에 한 번에 조일 수 있습니다."),
    ("글 길이와 읽기", "한 줄 45~75자는 오래된 조판 경험칙입니다. 한글은 한 글자가 넓어 <b>영문 기준보다 조금 짧게</b> 잡습니다."),
    ("이메일·PDF", "메일은 보통 <b>600px</b> 고정이 관례입니다. 웹의 컨테이너 값을 그대로 쓰면 잘립니다."),
    ("사진 크기", "컨테이너 폭이 1200px 이면 <b>2400px 짜리</b>를 보낼 필요가 없습니다. 상한을 알면 내려줄 크기도 정해집니다."),
  ]),
  plat_lede="앱은 화면 폭이 뻔해서 상한을 덜 쓰고, 태블릿에서만 필요해집니다.",
  plats=plats([
    ("웹", "max-width",
     cont("70%", "120px", "내용", "max-width"),
     "<code>max-width</code> + <code>margin-inline: auto</code> 두 줄. 요즘은 <code>min()</code>으로 한 줄로도 씁니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.frame(maxWidth: 700)<br>readableContentGuide</div>''',
     "<b>readableContentGuide</b> 라는 이름으로 OS 가 읽기 좋은 폭을 알려 줍니다. 아이패드에서 특히 중요합니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">WindowSizeClass<br>Compact / Medium<br>Expanded</div>''',
     "<b>윈도 크기 클래스</b>로 나눕니다. 폭이 넓어지면 가운데로 모으거나 <b>두 칸으로 나누라</b>고 권합니다."),
  ]),
  plat_note="폰만 보던 앱이 <b>태블릿·폴더블</b>에 올라가면 이 문제가 갑자기 생깁니다. \"넓은 화면에서 어떻게 보일지\"를 안 정해 두면 글이 끝까지 늘어난 화면이 그대로 나갑니다 — 웹에서 늘 하던 고민이 앱에서는 뒤늦게 오는 셈입니다.",
  siblings=siblings("container"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/center.html"><b>가운데 맞추기</b><em>1부</em></a></li>
        <li><span class="na"><b>브레이크포인트</b><em>11부</em></span></li>''',
)
