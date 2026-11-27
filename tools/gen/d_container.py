# -*- coding: utf-8 -*-
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
                    <div class="pin-out" data-pin="2" style="max-width:160px;margin-inline:auto;background:var(--accent-soft);border:1px dashed var(--accent);border-radius:5px;padding:8px;font-size:10.5px;line-height:1.8;color:var(--accent);margin-left:26px">글줄이 너무 길면 다음 줄의 첫 글자를 찾기 어렵습니다.</div>
                  </div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">max-width: 65ch</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">margin-inline: auto</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">padding-inline: 16px   좁은 화면의 양옆 여백</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">width: 1200px   좁은 화면에서 가로 스크롤이 생김</div>
                </div>
              </div>'''

D = dict(
  slug="container", ko="컨테이너와 최대 폭", en="Container · max-width",
  desc="내용이 들어가는 가운데 칸을 만드는 두 줄과 글줄 길이 상한, width와 max-width의 차이를 보여 주는 항목입니다.",
  lede="컨테이너는 화면에서 내용이 들어가는 <b>가운데 칸</b>입니다. 대부분의 사이트가 폭에 상한을 걸고 가운데에 두는 <b>같은 두 줄</b>로 이 칸을 만듭니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 움직이면 <b>한 줄에 실제로 몇 글자가 들어가는지</b> 재서 알려 줍니다.
          읽는 글은 한 줄에 <b>45~75자</b>일 때 읽기 편합니다.<br>
          <b>상한 없애기</b>를 켜 보세요. 넓은 화면에서 글줄이 끝까지 늘어나면
          한 줄을 다 읽고 돌아올 때 다음 줄의 첫 글자를 찾기 어려워집니다. 긴 글이 읽기 힘든 이유는 글꼴보다
          <b>줄 길이</b>에 있을 때가 많습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "컨테이너, 최대 폭, 가운데 칸, 래퍼"),
    ("영어", "container, wrapper, max-width, measure, line length"),
    ("같이 쓰는 말",
     "한 줄의 글자 수는 <b>글줄 길이</b>(measure · line length)라고 하고, "
     "폭을 재는 단위 <b><code>ch</code></b>는 그 글꼴에서 '0' 한 글자의 너비입니다. "
     "화면 양옆에 남기는 여백은 <b>거터</b>나 <b>페이지 마진</b>이라고 부르고, "
     "폭에 따라 짜임을 바꾸는 기능은 <b>컨테이너 쿼리</b>(container query)라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>width</code>와 <code>max-width</code></b> — <code>width: 1200px</code>은 <b>좁은 화면에서도 1200px</b>을 유지해서 "
     "가로 스크롤이 생깁니다. 반면 <code>max-width</code>는 이 값보다 커지지만 않게 막습니다.<br>"
     "<b>컨테이너 쿼리</b> — 부모 폭에 따라 스타일을 바꾸는 기능으로, 이름만 비슷하고 컨테이너와는 다른 것입니다.<br>"
     "<b>컨테이너</b>(도커) — 서버에서 쓰는 도커 컨테이너는 이름만 같고 전혀 다른 개념입니다."),
  ]),
  s4_title="화면 폭에 따른 모습", s4_hint="화면 폭과 상한에 따라 달라지는 칸의 너비",
  instead_title="컨테이너와 함께 보면 좋은 항목",
  states=states([
    (cont("100%", "170px", "넓은 화면에서 상한에 걸린 모습", "max-width에서 멈춤"), "넓은 화면에서", "폭이 <b>상한에서 멈추고</b> 양옆에 여백이 남습니다"),
    (cont("100%", "120px", "좁아지면 상한이 걸리지 않음", "폭을 모두 씀"), "좁은 화면에서", "화면이 상한보다 좁아서 상한이 걸리지 않고, <b>양옆 패딩만</b> 남습니다"),
    (cont("100%", "170px", "상한이 없으면 끝까지 늘어나 읽기 힘들어집니다. 다음 줄의 시작을 찾기 어렵습니다.", "상한 없음"), "상한을 걸지 않았을 때", "글줄이 길어져서 <b>다음 줄의 시작을 찾기 어렵습니다</b>"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;overflow-x:auto">
                <div style="width:230px;background:var(--warn-soft);border:1px dashed var(--warn);border-radius:4px;padding:6px;font-size:9.5px;color:var(--warn)">width: 230px로 고정함</div>
              </div>''',
     "<code>width</code>로 폭을 고정했을 때", "<b>좁은 화면에서 가로 스크롤</b>이 생깁니다. 거의 항상 잘못된 선택입니다"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px;display:grid;gap:5px">
                <div style="background:var(--accent-soft);border:1px dashed var(--accent);border-radius:4px;padding:5px;font-size:9px;color:var(--accent);text-align:center">읽는 글 · 65ch</div>
                <div style="background:var(--bg);border:1px dashed var(--line-strong);border-radius:4px;padding:5px;font-size:9px;color:var(--fg-muted);text-align:center">표는 더 넓게</div>
              </div>''',
     "상한을 두 겹으로 둘 때", "읽는 글은 좁게, <b>표나 그리드는 넓게</b> 잡습니다. 상한이 하나일 필요는 없습니다"),
    ('''              <div style="width:100%;max-width:170px;background:var(--bg);border:1px dashed var(--line-strong);border-radius:6px;padding:7px">
                <div style="background:var(--accent-soft);border:1px dashed var(--accent);border-radius:4px;padding:6px;font-size:9.5px;color:var(--accent)">사진만 칸 밖 끝까지 넓힘</div>
                <div style="margin:5px -7px 0;height:22px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 6px,var(--ink-050) 6px 12px);border-radius:2px"></div>
              </div>''',
     "사진만 상한 밖으로 넓힐 때", "사진이나 배경만 <b>상한을 넘겨</b> 화면 끝까지 넓히는 기법입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바깥 칸", "page", "화면 전체입니다. 여기에는 폭 제한을 두지 않습니다"),
    ("컨테이너", "container · wrapper", "내용이 들어가는 가운데 칸으로, <b>사이트 레이아웃의 뼈대</b>가 됩니다"),
    ("최대 폭", "max-width", "칸이 이 값보다 넓어지지 않게 막습니다. 읽는 글은 <code>65ch</code> 정도로 잡습니다"),
    ("가운데 두기", "margin-inline: auto", "남은 자리를 양옆에 똑같이 나눕니다. <b>가로 방향에만</b> 작동합니다"),
    ("양옆 패딩", "padding-inline", "좁은 화면에서 글이 <b>가장자리에 붙지 않게</b> 합니다. 빠뜨리기 쉬운 줄입니다"),
    ("고정된 폭", "width (쓰지 않음)", "<code>width: 1200px</code>은 좁은 화면에서 <b>가로 스크롤</b>을 만듭니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          상한은 <b>하나일 필요가 없습니다.</b> 읽는 글은 65ch 정도로 좁게, 카드 그리드나 표는
          1200px 정도로 넓게 잡아서 같은 페이지 안에서 상한을 <b>두세 겹</b> 쓰는 것이 보통입니다.
          컨테이너 하나에 모든 내용을 담으면 글이 너무 넓어지거나 표가 너무 좁아집니다.</p>''',
  do=ul([
    "기사, 설명, 약관처럼 <b>읽는 글</b>이 있는 화면을 만들 때",
    "넓은 모니터에서 내용이 <b>끝까지 늘어나면 안 될</b> 때",
    "화면마다 양옆 여백을 <b>똑같이</b> 맞추고 싶을 때",
  ]),
  dont=ul([
    "<code>width</code>로 폭을 고정할 때. <b>좁은 화면에서 가로 스크롤</b>이 생깁니다",
    "배경색이나 배경 이미지까지 컨테이너에 가둘 때. 배경은 화면 끝까지 채우고 <b>내용만</b> 가둡니다",
    "표나 그리드까지 좁은 상한에 넣을 때. 열이 다닥다닥 붙습니다",
    "양옆 패딩을 빠뜨릴 때. 폰에서 글이 <b>화면 가장자리에 닿습니다</b>",
  ]),
  instead='글줄 길이 자체는 <a href="../items/typescale.html">타입 스케일</a>과 함께 보고, 칸을 나누는 일은 <a href="grid.html">그리드</a>에서 다룹니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;background:var(--bg);border-radius:6px;padding:6px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:7px;max-width:140px;margin-inline:auto">
                  <span style="font-size:10.5px;font-weight:700;display:block">기사 제목</span>
                  <span style="font-size:9.5px;color:var(--fg-muted);line-height:1.7">본문이 65ch를 넘지 않습니다.</span>
                </div>
              </div>''',
     "읽는 글의 폭 제한하기", "상한을 <code>65ch</code>로 잡으면 <b>글꼴이 커질 때 상한도 함께</b> 커집니다"),
    ('''              <div style="width:100%;max-width:190px;background:var(--bg);border-radius:6px;padding:6px">
                <div style="max-width:175px;margin-inline:auto;display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px">
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;height:26px"></span>
                </div>
              </div>''',
     "카드 그리드는 더 넓게 잡기", "같은 페이지 안에서도 카드 그리드는 <b>상한을 더 넓게</b> 잡습니다"),
    ('''              <div style="width:100%;max-width:190px;border-radius:6px;overflow:hidden">
                <div style="height:24px;background:repeating-linear-gradient(135deg,var(--ink-100) 0 6px,var(--ink-050) 6px 12px)"></div>
                <div style="background:var(--bg);padding:6px">
                  <div style="max-width:130px;margin-inline:auto;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:6px;font-size:9.5px">내용만 가둠</div>
                </div>
              </div>''',
     "배경은 끝까지 깔고 내용만 가두기", "<b>배경은 화면 전체에 깔고 내용만 가운데</b> 칸에 둡니다. 가장 흔한 짜임입니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="사이트 뼈대를 만드는 두 줄과 지킬 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="대부분의 사이트 스타일시트에는 <b>이 네 줄</b>이 들어 있습니다.",
  code='''<span class="t">.container</span> {
  <span class="a">max-width</span>: <span class="a">1200px</span>;        <span class="c">/* width가 아니다 */</span>
  <span class="a">margin-inline</span>: auto;      <span class="c">/* 가운데로 */</span>
  <span class="a">padding-inline</span>: <span class="a">16px</span>;    <span class="c">/* 좁은 화면의 양옆 */</span>
}

<span class="c">/* 읽는 글은 한 줄 45~75자로 더 좁게 */</span>
<span class="t">.prose</span> { <span class="a">max-width</span>: <span class="a">65ch</span>; }

<span class="c">/* 요즘 방식. 한 줄로 적는다 */</span>
<span class="t">.container</span> { <span class="a">width</span>: <span class="t">min</span>(<span class="a">100%</span> - <span class="a">32px</span>, <span class="a">1200px</span>); <span class="a">margin-inline</span>: auto; }

<span class="c">/* 안에서 하나만 끝까지 내보내기 */</span>
<span class="t">.full-bleed</span> { <span class="a">margin-inline</span>: <span class="t">calc</span>(<span class="a">50%</span> - <span class="a">50vw</span>); }''',
  keys=kbd([
    ("폭은 <code>max-width</code>로 제한하기", "<code>width</code>로 폭을 고정하면 <b>좁은 화면에서 가로 스크롤</b>이 생깁니다"),
    ("양옆 패딩 빠뜨리지 않기", "패딩이 없으면 폰에서 글이 <b>화면 가장자리에 닿습니다</b>"),
    ("읽는 글의 상한은 <code>ch</code>로 적기", "ch로 적으면 글꼴 크기가 바뀔 때 상한도 함께 바뀌지만, px로 적으면 따라 바뀌지 않습니다"),
    ("내용에 따라 상한을 여러 겹 두기", "글은 좁게, 표와 그리드는 넓게 잡고 <b>상한을 하나로 통일하지 않습니다</b>"),
    ("배경은 컨테이너에 가두지 않기", "배경색과 배경 이미지는 화면 전체에 깔고, <b>내용만</b> 컨테이너 안에 둡니다"),
    ("가운데 두기는 <code>margin-inline</code>으로", "<code>margin: 0 auto</code>보다 뜻이 분명하고, 글 방향이 바뀌어도 맞게 동작합니다"),
  ]),
  backend=rows([
    ("모든 화면에 함께 쓰는 값 하나", "컨테이너 폭 값 하나가 <b>모든 화면</b>에 적용됩니다. 그래서 이 값을 <code>--container</code> 같은 토큰으로 빼 두면 나중에 한 번에 바꿀 수 있습니다."),
    ("글줄 길이와 읽기 편한 정도", "한 줄 45~75자는 조판에서 오래 써 온 경험칙입니다. 한글은 한 글자가 영문보다 넓어서 <b>영문 기준보다 조금 짧게</b> 잡습니다."),
    ("이메일과 PDF의 폭", "메일은 폭을 <b>600px</b>로 고정하는 것이 관례라서, 웹의 컨테이너 값을 그대로 쓰면 내용이 잘립니다."),
    ("내려 줄 사진 크기 정하기", "컨테이너 폭이 1200px이면 <b>2400px짜리</b>를 보낼 필요가 없습니다. 상한을 알면 내려줄 크기도 정해집니다."),
  ]),
  plat_lede="앱은 화면 폭이 크게 달라지지 않아서 상한을 덜 쓰고, 태블릿에서만 필요해집니다.",
  plats=plats([
    ("웹", "max-width",
     cont("70%", "120px", "내용", "max-width"),
     "<code>max-width</code>와 <code>margin-inline: auto</code> 두 줄로 만듭니다. 요즘은 <code>min()</code>을 써서 한 줄로 적기도 합니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.frame(maxWidth: 700)<br>readableContentGuide</div>''',
     "OS가 <b>readableContentGuide</b>라는 이름으로 읽기 좋은 폭을 알려 줍니다. 화면이 넓은 아이패드에서 특히 중요합니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">WindowSizeClass<br>Compact / Medium<br>Expanded</div>''',
     "화면을 <b>윈도 크기 클래스</b>로 나눠 다룹니다. 폭이 넓어지면 내용을 가운데로 모으거나 <b>두 칸으로 나누라</b>고 권합니다."),
  ]),
  plat_note="폰 화면만 생각하고 만든 앱을 <b>태블릿이나 폴더블</b>에서 실행하면 이 문제가 갑자기 생깁니다. \"넓은 화면에서 어떻게 보일지\"를 정해 두지 않으면 글이 화면 끝까지 늘어난 채로 출시됩니다. 웹에서는 늘 하던 고민을 앱에서는 뒤늦게 하게 되는 셈입니다.",
  siblings=siblings("container"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/center.html"><b>가운데 맞추기</b><em>1부</em></a></li>
        <li><a href="breakpoint.html"><b>브레이크포인트</b><em>11부</em></a></li>''',
)
