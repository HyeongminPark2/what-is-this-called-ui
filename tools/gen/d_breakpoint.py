# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def mini(cols, w="152px", note="", warn=False):
    cells = ''.join('<span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;'
                    'padding:4px 5px;font-size:8.5px;min-width:0;overflow:hidden">가맹점</span>' for _ in range(cols * 2))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--bg);padding:6px;'
            'display:grid;gap:4px;grid-template-columns:repeat(' + str(cols) + ',1fr)">' + cells + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@media (min-width: 560px)로 좁은 화면부터 쌓음</div>
                  <div class="pin-out" data-pin="2" style="max-width:230px">''' + mini(2, "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">기준은 기기 이름이 아니라 <b>내용이 깨지는 폭</b></div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">끊는 자리는 서넛, 많으면 관리가 어려움</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@container는 창 대신 <b>감싼 상자</b>의 폭을 봄</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">375 / 768 / 1024처럼 기기 폭으로 잡는 실수</div>
                </div>
              </div>'''

D = dict(
  slug="breakpoint", ko="브레이크포인트", en="Breakpoint",
  desc="화면 폭이 얼마일 때 배치를 바꿀지 정하는 지점과, 그 지점을 기기 이름이 아니라 내용이 깨지는 폭에서 잡아야 하는 까닭을 보여 주는 항목입니다.",
  lede="브레이크포인트는 화면 폭이 얼마일 때 <b>배치를 바꿀지</b> 정하는 지점입니다. 이 지점은 기기 이름이 아니라 <b>내용이 깨지기 시작하는 폭</b>을 기준으로 잡습니다.",
  axes_lede="PC와 폰의 차이는 기계 자체보다 화면을 쓰는 <b>전제</b>에 있습니다. 아래 네 가지를 물어보면 두 환경이 어디서 갈리는지 알 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 폭을 바꿔 보세요. 폭에 따라 단 수와 메뉴 모양이 함께 바뀝니다.<br>
          <b>기기 폭을 기준으로 끊기</b>를 켜면 흔히 쓰는 기기 폭(375 / 768 / 1024)에서 단을 바꾸는데,
          그러면 390px 폰에서부터 두 단이 되어 <b>가게 이름이 두 줄로 접힙니다.</b>
          아래 숫자는 어림한 값이 아니라 화면에서 <b>실제로 접힌 칸을 센 결과</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "브레이크포인트, 분기점, 중단점"),
    ("영어", "breakpoint, media query breakpoint"),
    ("같이 쓰는 말",
     "화면 폭에 따라 다른 CSS 규칙을 적용하는 문법을 <b>미디어 쿼리</b>(media query)라고 하고, "
     "가장 좁은 화면을 기본으로 두고 넓은 화면용 규칙을 덧붙여 가는 방식을 <b>모바일 퍼스트</b>라고 합니다. "
     "브라우저 창 대신 <b>요소를 감싼 상자</b>의 폭을 기준으로 삼는 문법은 <b>컨테이너 쿼리</b>(@container)입니다. "
     "단계마다 이름을 붙일 때는 흔히 <b>sm · md · lg · xl</b>처럼 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>반응형</b> — 반응형은 화면 폭에 맞춰 배치가 바뀌는 결과를 가리키고, 브레이크포인트는 그 결과를 만드는 <b>여러 수단 가운데 하나</b>입니다. 브레이크포인트로 끊지 않고도 반응형 화면을 만들 수 있습니다.<br>"
     "<b>중단점</b> — 디버거에서 실행을 멈추는 breakpoint와 영어 단어가 같아서, 이 말로 검색하면 디버거 자료가 섞여 나옵니다.<br>"
     "<b>해상도</b> — 브레이크포인트의 폭은 기기 화소 수가 아니라 <b>CSS px</b>로 잽니다. 기기 화소 수는 <a href=\"dpr.html\">화면 밀도</a>에서 다루는 다른 값입니다."),
  ]),
  axes=ax("브레이크포인트"),
  oneline="브레이크포인트는 <b>기기 폭에 맞춰 정하지 않습니다.</b> 브라우저 창을 조금씩 줄여 가다가 <b>글이 깨지기 시작하는 폭</b>을 찾으면, 그 폭이 그 화면의 브레이크포인트입니다.",
  s4_title="폭에 따라 달라지는 배치", s4_hint="폭마다 바뀌는 단 수와 메뉴 모양",
  do_title="브레이크포인트로 배치를 바꾸는 경우",
  dont_title="브레이크포인트를 잘못 잡는 경우",
  states=states([
    (mini(1, "152px", "~560px · 한 단"), "폭이 좁을 때", "한 단으로 놓고 메뉴는 <b>접어 둡니다</b>"),
    (mini(2, "152px", "560~900px · 두 단"), "폭이 중간일 때", "두 단으로 놓고, 이때부터 메뉴를 펼쳐 보입니다"),
    (mini(3, "152px", "900~1180px · 세 단"), "폭이 넓을 때", "세 단에 <a href=\"../items/sidebar.html\">사이드바</a>를 더합니다"),
    (mini(4, "152px", "1180px~ · 네 단"), "폭이 아주 넓을 때", "단을 더 늘리기보다 <b>최대 폭</b>을 정해 내용 폭을 묶어 두는 편이 낫습니다"),
    (mini(2, "152px", "390px에서 두 단이 되어 이름이 접힘", True), "기기 폭을 기준으로 끊었을 때", "390px 폰에서부터 <b>두 단</b>이 되어 버립니다"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:4px">
                <div style="border:1px solid var(--accent);border-radius:6px;background:var(--bg);padding:6px;display:grid;gap:4px;grid-template-columns:1fr 1fr">
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:4px 5px;font-size:8.5px">카드</span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:4px 5px;font-size:8.5px">카드</span>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--accent)">@container로 창 대신 이 상자 폭을 봄</span>
              </div>''',
     "컨테이너 쿼리를 쓸 때", "같은 카드가 <b>사이드바에서는 한 단, 본문에서는 두 단</b>으로 놓입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("질의", "@media (min-width)", "<b>좁은 화면을 기본</b>으로 두고, 넓어질 때 필요한 규칙을 덧붙입니다"),
    ("단 수", "1 → 2 → 3", "폭이 늘면 칸 수가 늘어나야 합니다. 칸 수는 그대로 두고 <b>칸만 넓어지게</b> 두면 안 됩니다"),
    ("기준", "내용이 깨지는 폭", "창을 줄여 가다가 <b>글이 접히기 시작하는 폭</b>입니다"),
    ("개수", "서넛", "다섯 개를 넘기면 폭마다 <b>화면이 어떻게 보이는지</b> 파악하기 어려워집니다"),
    ("컨테이너 쿼리", "@container", "요소를 감싼 상자의 폭을 기준으로 삼기 때문에, <b>부품을 다른 자리로 옮겨도</b> 그 자리 폭에 맞게 배치가 바뀝니다"),
    ("기기 폭으로 끊은 자리", "기기 폭", "375 · 768 · 1024처럼 기기 폭으로 끊으면 <b>그 폭의 기기에서만</b> 화면이 맞습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          미디어 쿼리를 <b>모바일 퍼스트</b>로 적는 데에는 이유가 있습니다.
          <code>max-width</code>로 적으면 기본 규칙이 넓은 화면용이 되기 때문에,
          새 기기나 작은 창에서 좁은 화면용 규칙이 빠진 폭이 생기면 <b>넓은 화면 배치가 덮어써지지 않고</b> 그대로 나옵니다.
          반면 <code>min-width</code>로 쌓으면 기본 규칙이 가장 좁은 화면용이고 넓어질 때마다 규칙을 덧붙이는 구조라서,
          규칙 하나를 빠뜨려도 <b>좁은 화면의 배치</b>로 보입니다.
          좁은 화면 배치는 넓은 창에서도 읽는 데 문제가 없으므로, 실수했을 때 화면이 덜 망가집니다.</p>''',
  do=ul([
    "<b>지금 배치가 더는 맞지 않는</b> 폭을 창을 줄여 가며 재 보고 정할 때",
    "메뉴를 접거나 펴고, 단 수를 바꿀 때",
    "부품 하나가 여러 자리에 들어갈 때. 이때는 <b>컨테이너 쿼리</b>를 씁니다",
  ]),
  dont=ul([
    "기기 이름에 맞춰 끊을 때. <b>새 기기가 계속 나오기</b> 때문에 금방 맞지 않게 됩니다",
    "끊는 자리를 여섯 개 넘게 둘 때. 무엇이 어느 폭에서 바뀌는지 알 수 없게 됩니다",
    "<b>세로 높이</b>로 끊을 때. 폰에서는 주소창이 나타났다 사라지면서 높이가 계속 바뀝니다",
    "폭마다 <b>다른 내용</b>을 보여 줄 때. 같은 주소를 공유해도 받는 사람의 화면 폭에 따라 다른 내용이 보입니다",
  ]),
  instead='끊는 자리 없이 폭에 따라 칸 수를 늘리려면 <a href="../items/grid.html">그리드</a>의 <code>auto-fit</code>을 쓰고, 글줄 길이를 묶으려면 <a href="../items/container.html">컨테이너</a>를 씁니다. 부품 하나를 놓인 자리의 폭에 맞춰 바꾸려면 컨테이너 쿼리가 맞습니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--accent)">--bp-sm: 560px</span>
                <span style="color:var(--accent)">--bp-md: 900px</span>
                <span style="color:var(--accent)">--bp-lg: 1180px</span>
              </div>''',
     "끊는 폭 셋에 이름 붙이기", "폭마다 이름을 붙여 두면 <b>팀 전체가 같은 폭</b>을 기준으로 씁니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted)">
                grid-template-columns:<br>
                &nbsp;&nbsp;<span style="color:var(--accent)">repeat(auto-fit,<br>&nbsp;&nbsp;&nbsp;&nbsp;minmax(220px, 1fr))</span>
              </div>''',
     "미디어 쿼리 없이 칸 수 바꾸기", "칸의 최소 폭만 정해 두면 <b>미디어 쿼리 없이도</b> 폭에 따라 칸 수가 바뀝니다"),
    (mini(1, "152px", "사이드바 안에서는 한 단"), "놓인 자리에 맞춰 카드 접기", "같은 카드가 <b>놓인 자리의 폭에 따라</b> 다르게 접힙니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="가장 좁은 화면의 규칙을 기본으로 두고, 넓은 화면용 규칙은 <code>min-width</code> 미디어 쿼리로 덧붙입니다.",
  code=''':root { <span class="a">--bp-sm</span>: <span class="a">560px</span>; <span class="a">--bp-md</span>: <span class="a">900px</span>; <span class="a">--bp-lg</span>: <span class="a">1180px</span>; }

.list { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">12px</span>; }          <span class="c">/* 기본 = 가장 좁은 화면 */</span>

@media (min-width: 560px) { .list { <span class="a">grid-template-columns</span>: <span class="a">1fr</span> <span class="a">1fr</span>; } }
@media (min-width: 900px) { .list { <span class="a">grid-template-columns</span>: <span class="a">repeat</span>(<span class="a">3</span>, <span class="a">1fr</span>); } }

<span class="c">/* 브레이크포인트 없이도 칸 수가 바뀐다 */</span>
.cards { <span class="a">grid-template-columns</span>: <span class="a">repeat</span>(auto-fit, <span class="a">minmax</span>(<span class="a">220px</span>, <span class="a">1fr</span>)); }

<span class="c">/* 창 대신 감싼 상자의 폭을 본다 */</span>
.slot { <span class="a">container-type</span>: inline-size; }
@container (min-width: 420px) { .card { <span class="a">flex-direction</span>: row; } }''',
  keys=kbd([
    ("<code>&lt;meta name=\"viewport\"&gt;</code> 태그 넣기", "이 태그가 없으면 폰 브라우저가 화면을 <b>폭 980px짜리 창</b>으로 여기고 그립니다. 그러면 좁은 화면용 미디어 쿼리가 하나도 적용되지 않습니다"),
    ("<code>min-width</code>로 쌓기", "규칙을 빠뜨려도 <b>좁은 화면 배치</b>로 보이기 때문에 화면이 덜 망가집니다"),
    ("폭 단위는 <code>px</code>로 적기", "<code>em</code>으로 적으면 사용자의 글자 크기 설정에 따라 끊는 자리가 움직입니다. 일부러 그렇게 하려는 게 아니라면 px로 적습니다"),
    ("<code>@container</code>를 쓸 때", "부모 요소에 <code>container-type: inline-size</code>가 있어야 합니다. 없으면 오류 없이 규칙만 적용되지 않습니다"),
    ("좁은 폭에서 내용을 숨기지 않기", "<code>display:none</code>으로 숨긴 내용은 <b>그 폭의 화면에서는 볼 방법이 없습니다</b>"),
    ("<a href=\"../items/keyboard.html\">키보드</a>로도 같은 일을 할 수 있게", "좁은 폭에서 메뉴를 접었다면, <b>접힌 메뉴를 여는 버튼</b>에도 Tab으로 포커스가 가야 합니다"),
  ]),
  backend=rows([
    ("폭에 따라 다른 HTML을 보내지 않기", "서버가 기기를 보고 서로 다른 HTML을 보내면 같은 주소의 <b>캐시를 기기별로 나눠야</b> 하고, 공유한 주소를 연 사람마다 다른 화면을 보게 됩니다."),
    ("그림은 화면 폭에 맞는 크기로 보내기", "<code>srcset</code>과 <code>sizes</code>를 써서 브라우저가 <b>화면 폭에 맞는 크기</b>의 그림을 골라 받게 합니다. 큰 그림 한 벌만 두면 폰도 그 큰 파일을 받아야 합니다."),
    ("한 쪽에 담는 목록 건수", "폰에서 한 쪽에 50건씩 보여 주면 너무 많습니다. 폭에 맞춰 배치만 바꾸기보다 한 쪽에 담는 건수인 <b>쪽 크기</b>를 조절하는 편이 낫습니다."),
    ("<code>User-Agent</code>로 기기를 가르지 않기", "User-Agent 문자열은 브라우저가 바뀔 때마다 달라지고, 실제 기기와 다른 값이 오는 경우도 있습니다. 화면 폭은 <b>브라우저가 미디어 쿼리로 직접 판단</b>하므로 서버가 기기를 짐작할 필요가 없습니다."),
  ]),
  plat_lede="플랫폼마다 화면 폭을 나누는 방식과 <b>기본값</b>이 조금씩 다릅니다.",
  plats=plats([
    ("웹", "@media · @container",
     mini(2, "110px"),
     "끊는 폭을 CSS에 직접 적습니다. CSS 프레임워크마다 기본값(640·768·1024·1280 등)이 있으니 <b>팀에서 한 가지로 정해</b> 쓰면 됩니다."),
    ("iOS", "Size Class",
     '''              <div class="phone" role="img" aria-label="iOS 사이즈 클래스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:10px;border-radius:2px;background:var(--line)"></span><span style="height:10px;border-radius:2px;background:var(--line)"></span></div></div></div>''',
     "폭을 숫자로 나누지 않고 <b>compact / regular</b> 두 등급으로 나눕니다. 아이패드의 분할 화면도 같은 등급 규칙으로 다룹니다."),
    ("안드로이드", "Window Size Class",
     '''              <div class="phone" role="img" aria-label="안드로이드 윈도 클래스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px;grid-template-columns:1fr 1fr"><span style="height:10px;border-radius:2px;background:var(--line)"></span><span style="height:10px;border-radius:2px;background:var(--line)"></span></div></div></div>''',
     "창 폭을 <b>compact(600dp 미만) · medium · expanded</b> 세 등급으로 나눕니다. 접었다 펴는 폴더블 기기가 나오면서 폭을 숫자 대신 등급으로 다루는 방식이 자리를 잡았습니다."),
  ]),
  plat_note="\"아이폰이랑 아이패드에서 잘 되게\"라는 요청을 그대로 받으면 <b>그 두 기기 폭</b>에만 맞는 화면이 됩니다. 폴더블 기기, 분할 화면, 반으로 줄인 브라우저 창처럼 새로운 폭은 계속 생기므로, 요청을 기기 이름 대신 <b>'이 화면은 몇 px부터 두 단'</b>처럼 폭으로 바꿔 적어 두면 기기가 바뀌어도 그대로 쓸 수 있습니다.",
  siblings=siblings("breakpoint"),
  related='''        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/sidebar.html"><b>사이드바</b><em>7부</em></a></li>
        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>''',
)
