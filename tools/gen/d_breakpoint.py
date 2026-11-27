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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@media (min-width: 560px) — 작은 쪽부터 쌓는다</div>
                  <div class="pin-out" data-pin="2" style="max-width:230px">''' + mini(2, "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">기준은 기기 이름이 아니라 <b>내용이 깨지는 폭</b></div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">끊는 자리는 서넛 — 많을수록 어긋난다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@container — 창이 아니라 <b>제 상자</b>를 본다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">375 / 768 / 1024 — 기기 폭으로 잡은 흔한 실수</div>
                </div>
              </div>'''

D = dict(
  slug="breakpoint", ko="브레이크포인트", en="Breakpoint",
  desc="폭이 얼마일 때 배치를 바꿀지. 기기 이름이 아니라 내용이 깨지는 지점에서 끊는다.",
  lede="폭이 얼마일 때 <b>배치를 바꿀지</b> 정하는 지점. 기준은 기기 이름이 아니라 <b>내용이 깨지는 폭</b>입니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>막대를 끌어 폭을 바꿔 보세요. 단 수와 메뉴 모양이 함께 바뀝니다.<br>
          <b>잘못 잡은 기준으로</b>를 켜면 흔히 쓰는 기기 폭(375 / 768 / 1024)에 맞춰 끊습니다 —
          390px 폰에서 벌써 두 단이 되어 <b>가게 이름이 두 줄로 접힙니다.</b>
          아래 숫자는 짐작이 아니라 <b>실제로 접힌 칸을 센 것</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "브레이크포인트, 분기점, 중단점"),
    ("영어", "breakpoint, media query breakpoint"),
    ("같이 쓰는 말",
     "폭에 따라 다른 규칙을 주는 것이 <b>미디어 쿼리</b>(media query)이고, "
     "좁은 쪽부터 쌓아 올리는 방식이 <b>모바일 퍼스트</b>입니다. "
     "창이 아니라 <b>제가 들어앉은 상자</b>의 폭을 보는 것이 <b>컨테이너 쿼리</b>(@container)입니다. "
     "단계마다 이름을 붙이면 <b>sm · md · lg · xl</b>처럼 됩니다."),
    ("자주 잘못 부름",
     "<b>반응형</b> — 반응형은 결과이고, 브레이크포인트는 <b>그 안의 한 수단</b>입니다. 안 끊고도 반응형이 됩니다.<br>"
     "<b>중단점</b> — 디버거의 breakpoint 와 같은 영어 단어라 검색이 섞입니다.<br>"
     "<b>해상도</b> — 폭은 <b>CSS px</b>이지 기기 화소 수가 아닙니다. <a href=\"dpr.html\">화면 밀도</a>와 섞지 않습니다."),
  ]),
  axes=ax("브레이크포인트"),
  oneline="끊는 자리는 <b>기기가 정하지 않습니다.</b> 창을 조금씩 줄이다가 <b>글이 깨지는 그 폭</b>이 그 화면의 브레이크포인트입니다.",
  s4_title="폭에 따라", s4_hint="단 수만 바뀌는 게 아니다",
  states=states([
    (mini(1, "152px", "~560px · 한 단"), "좁을 때", "한 단. 메뉴는 <b>접는다</b>"),
    (mini(2, "152px", "560~900px · 두 단"), "보통", "두 단. 메뉴가 펼쳐지기 시작한다"),
    (mini(3, "152px", "900~1180px · 세 단"), "넓을 때", "세 단 + <a href=\"../items/sidebar.html\">사이드바</a>"),
    (mini(4, "152px", "1180px~ · 네 단"), "아주 넓을 때", "더 늘리기보다 <b>최대 폭</b>으로 묶는 편이 낫다"),
    (mini(2, "152px", "390px 에 두 단 — 이름이 접힌다", True), "기기 폭으로 끊으면", "<b>폰에서 벌써 두 단</b>이 된다"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:4px">
                <div style="border:1px solid var(--accent);border-radius:6px;background:var(--bg);padding:6px;display:grid;gap:4px;grid-template-columns:1fr 1fr">
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:4px 5px;font-size:8.5px">카드</span>
                  <span style="background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:4px 5px;font-size:8.5px">카드</span>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--accent)">@container — 창이 아니라 이 상자 폭</span>
              </div>''',
     "컨테이너 쿼리", "같은 카드가 <b>사이드바에선 한 단, 본문에선 두 단</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("질의", "@media (min-width)", "<b>좁은 쪽을 기본</b>으로 두고 넓어질 때 덧붙인다"),
    ("단 수", "1 → 2 → 3", "폭이 늘면 칸이 늘어난다. <b>칸이 넓어지기만 하면</b> 안 된다"),
    ("기준", "내용이 깨지는 폭", "창을 줄이다가 <b>글이 접히는 그 자리</b>"),
    ("개수", "서넛", "다섯을 넘으면 <b>어디가 어떻게 보이는지</b> 아무도 모른다"),
    ("컨테이너 쿼리", "@container", "제가 들어앉은 상자를 본다. <b>부품을 옮겨 심을 수</b> 있다"),
    ("흔한 실수", "기기 폭", "375 · 768 · 1024. <b>그 폭의 기기만</b> 맞는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>모바일 퍼스트</b>로 적는 이유는 취향이 아닙니다.
          <code>max-width</code>로 적으면 기본값이 '넓은 화면'이라,
          새 기기나 작은 창에서 <b>덮어쓰기가 빠진 구멍</b>이 생깁니다.
          <code>min-width</code>로 쌓으면 기본값이 가장 좁은 화면이고
          넓어질 때마다 덧붙이는 꼴이라, 빠뜨려도 <b>좁은 화면의 배치</b>로 떨어집니다.
          망가지는 쪽이 안전한 쪽입니다.</p>''',
  do=ul([
    "<b>배치가 더는 안 통하는</b> 폭에서 — 재 보고 정한다",
    "메뉴를 접고 펼 때 · 단 수를 바꿀 때",
    "부품 하나가 여러 자리에 들어간다면 <b>컨테이너 쿼리</b>",
  ]),
  dont=ul([
    "기기 이름으로 끊기 — <b>기기는 계속 나온다</b>",
    "끊는 자리를 여섯 개 넘게 — 무엇이 어디서 바뀌는지 모르게 된다",
    "<b>세로 높이</b>로 끊기 — 폰 주소창 때문에 계속 흔들린다",
    "폭마다 <b>다른 내용</b>을 보여 주기 — 공유한 주소가 다른 화면이 된다",
  ]),
  instead='단을 안 끊고 늘리려면 <a href="../items/grid.html">그리드</a>의 <code>auto-fit</code>, 글줄 길이를 묶으려면 <a href="../items/container.html">컨테이너</a>, 부품 단위로 바꾸려면 컨테이너 쿼리.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span style="color:var(--accent)">--bp-sm: 560px</span>
                <span style="color:var(--accent)">--bp-md: 900px</span>
                <span style="color:var(--accent)">--bp-lg: 1180px</span>
              </div>''',
     "셋이면 충분하다", "이름을 붙여 두면 <b>팀이 같은 폭</b>을 쓴다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted)">
                grid-template-columns:<br>
                &nbsp;&nbsp;<span style="color:var(--accent)">repeat(auto-fit,<br>&nbsp;&nbsp;&nbsp;&nbsp;minmax(220px, 1fr))</span>
              </div>''',
     "안 끊고 되는 것", "칸 최소 폭만 정하면 <b>미디어 쿼리가 필요 없다</b>"),
    (mini(1, "152px", "사이드바 안에서는 한 단"), "컨테이너 쿼리", "같은 카드가 <b>자리에 따라</b> 달리 접힌다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 기준의 계약서",
  code_lede="좁은 쪽을 기본으로 두고 <code>min-width</code>로 덧붙입니다.",
  code=''':root { <span class="a">--bp-sm</span>: <span class="a">560px</span>; <span class="a">--bp-md</span>: <span class="a">900px</span>; <span class="a">--bp-lg</span>: <span class="a">1180px</span>; }

.list { <span class="a">display</span>: grid; <span class="a">gap</span>: <span class="a">12px</span>; }          <span class="c">/* 기본 = 가장 좁은 화면 */</span>

@media (min-width: 560px) { .list { <span class="a">grid-template-columns</span>: <span class="a">1fr</span> <span class="a">1fr</span>; } }
@media (min-width: 900px) { .list { <span class="a">grid-template-columns</span>: <span class="a">repeat</span>(<span class="a">3</span>, <span class="a">1fr</span>); } }

<span class="c">/* 아예 안 끊고도 된다 */</span>
.cards { <span class="a">grid-template-columns</span>: <span class="a">repeat</span>(auto-fit, <span class="a">minmax</span>(<span class="a">220px</span>, <span class="a">1fr</span>)); }

<span class="c">/* 창이 아니라 제 상자를 본다 */</span>
.slot { <span class="a">container-type</span>: inline-size; }
@container (min-width: 420px) { .card { <span class="a">flex-direction</span>: row; } }''',
  keys=kbd([
    ("<code>&lt;meta name=\"viewport\"&gt;</code>", "이게 없으면 폰이 <b>980px 짜리 창</b>인 척한다. 미디어 쿼리가 통째로 헛돈다"),
    ("<code>min-width</code>로 쌓는다", "빠뜨려도 <b>좁은 화면 배치</b>로 떨어진다. 안전한 쪽으로 망가진다"),
    ("폭 단위는 <code>px</code>", "<code>em</code>으로 적으면 글자 크기 설정에 따라 끊는 자리가 움직인다. 그걸 노린 게 아니면 px"),
    ("<code>@container</code>", "부모에 <code>container-type: inline-size</code>가 있어야 한다. 없으면 조용히 안 먹는다"),
    ("폭만 숨기지 않는다", "<code>display:none</code>으로 지운 내용은 <b>그 폭에서 영영 못 본다</b>"),
    ("<a href=\"../items/keyboard.html\">키보드</a>로도 같은 일", "좁은 폭에서 메뉴를 접었다면 <b>접힌 버튼</b>도 Tab 으로 닿아야 한다"),
  ]),
  backend=rows([
    ("폭에 따라 다른 것을 보내지 않는다", "서버가 기기를 보고 다른 HTML 을 주면 <b>캐시가 갈라지고</b> 공유한 주소가 사람마다 다른 화면이 됩니다."),
    ("그림은 폭에 맞춰", "<code>srcset</code>·<code>sizes</code>로 <b>그 폭에 맞는 크기</b>를 받게 합니다. 한 벌만 주면 폰이 큰 파일을 받습니다."),
    ("목록 건수", "폰에서 한 쪽에 50건은 과합니다. 폭이 아니라 <b>쪽 크기</b>를 조절하는 편이 낫습니다."),
    ("<code>User-Agent</code>로 가르지 않는다", "기기 문자열은 계속 바뀌고 거짓말도 합니다. <b>폭은 브라우저가 알고 있습니다.</b>"),
  ]),
  plat_lede="끊는 자리의 <b>기본값</b>이 조금씩 다릅니다.",
  plats=plats([
    ("웹", "@media · @container",
     mini(2, "110px"),
     "폭을 직접 적습니다. 프레임워크마다 기본값이 있고(640·768·1024·1280 등), <b>팀이 하나를 정하면</b> 됩니다."),
    ("iOS", "Size Class",
     '''              <div class="phone" role="img" aria-label="iOS 사이즈 클래스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px"><span style="height:10px;border-radius:2px;background:var(--line)"></span><span style="height:10px;border-radius:2px;background:var(--line)"></span></div></div></div>''',
     "숫자가 아니라 <b>compact / regular</b> 두 등급입니다. 아이패드 분할 화면까지 같은 규칙으로 다룹니다."),
    ("안드로이드", "Window Size Class",
     '''              <div class="phone" role="img" aria-label="안드로이드 윈도 클래스 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:grid;gap:3px;grid-template-columns:1fr 1fr"><span style="height:10px;border-radius:2px;background:var(--line)"></span><span style="height:10px;border-radius:2px;background:var(--line)"></span></div></div></div>''',
     "<b>compact(600dp 미만) · medium · expanded</b> 세 등급. 폴더블 때문에 등급으로 다루는 쪽이 굳었습니다."),
  ]),
  plat_note="\"아이폰이랑 아이패드에서 잘 되게\"라는 요청을 그대로 받으면 <b>그 두 기기 폭</b>에만 맞는 화면이 됩니다. 폴더블·분할 화면·브라우저 창 반쪽 같은 폭이 계속 나오므로, 기기 이름 대신 <b>'이 화면은 몇 px 부터 두 단'</b>으로 바꿔 적어 두는 편이 오래갑니다.",
  siblings=siblings("breakpoint"),
  related='''        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="../items/grid.html"><b>그리드</b><em>1부</em></a></li>
        <li><a href="../items/sidebar.html"><b>사이드바</b><em>7부</em></a></li>
        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>''',
)
