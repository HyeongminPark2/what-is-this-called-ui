# -*- coding: utf-8 -*-
"""항목 카드 열 칸 틀. 모든 항목이 같은 틀을 써야 100번째에서도 어디를 볼지 안다."""

PARTS = {
    "15부 현장 용어": [
        ("wireframe", "와이어프레임과 목업과 시안"), ("designsystem", "디자인 시스템"), ("component", "컴포넌트와 인스턴스"),
        ("variant", "배리언트와 프롭"), ("autolayout", "오토 레이아웃"), ("prototype", "프로토타입"),
        ("handoff", "핸드오프"), ("assets", "에셋 내보내기"),
        ("review", "디자인 리뷰"), ("versioning", "버전 관리"),
    ],
    "14부 말투": [
        ("buttontext", "버튼 문구"), ("errortext", "오류 문구"), ("emptytext", "빈 상태 문구"),
        ("placeholder", "자리글과 헬퍼 텍스트"), ("koreanui", "한국어 UI"), ("datetime", "날짜와 시간 쓰기"),
        ("numbertext", "숫자와 단위 쓰기"), ("voice", "말투와 높임"),
    ],
    "13부 화면 단위 패턴": [
        ("login", "로그인"), ("onboarding", "온보딩"), ("searchresults", "검색 결과 화면"),
        ("settings", "설정 화면"), ("checkout", "결제 흐름"), ("permission", "권한 요청"),
        ("notifications", "알림 센터"), ("destructive", "위험한 동작"),
        ("profile", "프로필"), ("dashboard", "대시보드"), ("share", "공유하기"),
        ("upload", "파일 올리기"),
    ],
    "11부 플랫폼": [
        ("breakpoint", "브레이크포인트"), ("touchtarget", "터치 타깃"), ("hover", "호버가 없는 세계"),
        ("systemback", "시스템 백"), ("dpr", "화면 밀도"), ("viewport", "뷰포트 단위"),
        ("softkeyboard", "폰 키보드"), ("platformdiff", "HIG와 Material의 차이"),
    ],
    "9부 움직임": [
        ("easing", "이징 곡선"), ("duration", "지속 시간"), ("enterexit", "진입과 퇴장"),
        ("cheap", "무엇을 움직이나"), ("spring", "스프링"), ("stagger", "차례로 들어오기"),
        ("gesture", "제스처"), ("reducedmotion", "모션 줄이기"),
        ("sharedelement", "공유 요소 전환"), ("scrolllink", "스크롤 연동"),
    ],
    "10부 데이터 다루는 화면": [
        ("table", "데이터 테이블"), ("filter", "필터와 패싯"), ("search", "검색"),
        ("form", "폼 설계"), ("validation", "입력 검증"), ("bulk", "일괄 선택"),
        ("virtual", "가상 스크롤"), ("chart", "차트 고르기"),
        ("exportdata", "내보내기"), ("daterange", "날짜 범위"),
    ],
    "12부 접근성": [
        ("focus", "포커스"), ("focustrap", "포커스 트랩"), ("keyboard", "키보드 조작"),
        ("name", "이름 붙이기"), ("screenreader", "스크린 리더가 읽는 것"),
        ("live", "라이브 리전"), ("contrast", "대비비"), ("semantics", "시맨틱 태그"),
        ("alttext", "대체 텍스트"), ("textzoom", "확대와 글자 크기"),
    ],
    "1부 뼈대": [
        ("box", "박스 모델"), ("flex", "플렉스"), ("grid", "그리드"),
        ("center", "가운데 맞추기"), ("overflow", "넘침"), ("sticky", "스티키"),
        ("container", "컨테이너와 최대 폭"), ("safearea", "세이프 에어리어"),
        ("position", "포지션"), ("aspectratio", "종횡비"), ("scrollbehavior", "스크롤 동작"),
        ("sizing", "크기 정하기"), ("margincollapse", "여백 붕괴"), ("order", "보이는 순서와 읽는 순서"),
    ],
    "2부 꾸미는 규칙": [
        ("color", "색 토큰"), ("dark", "다크 모드"), ("typescale", "타입 스케일"),
        ("spacing", "간격 체계"), ("elevation", "고도"), ("zindex", "z-index"),
        ("radius", "모서리"), ("border", "테두리와 구분선"), ("opacity", "불투명도"),
        ("iconsize", "아이콘 크기"), ("statecolor", "상태 색"), ("tokenname", "토큰 이름 짓기"),
    ],
    "5부 표시 부품": [
        ("card", "카드"), ("listitem", "리스트 아이템"), ("avatar", "아바타"),
        ("badge", "배지"), ("chip", "칩"), ("stat", "스탯 타일"),
        ("timeline", "타임라인"), ("rating", "별점"),
        ("icon", "아이콘"), ("thumbnail", "썸네일"), ("tablerow", "테이블 행"),
        ("keyvalue", "키-값 목록"), ("media", "미디어 오브젝트"), ("accordion", "접히는 글"),
        ("tag", "태그"),
    ],
    "6부 겹치는 것들": [
        ("modal", "모달"), ("dialog", "다이얼로그"), ("sheet", "바텀시트"),
        ("drawer", "드로어"), ("popover", "팝오버"), ("tooltip", "툴팁"),
        ("toast", "토스트 · 스낵바"),
        ("actionsheet", "액션 시트"), ("banner", "배너"), ("inlinealert", "인라인 얼럿"),
        ("commandpalette", "커맨드 팔레트"), ("lightbox", "라이트박스"), ("menu", "드롭다운 메뉴"),
        ("contextmenu", "컨텍스트 메뉴"), ("coachmark", "코치마크"), ("fullscreen", "전체 화면 레이어"),
    ],
    "3부 글자": [
        ("weight", "글자 굵기"), ("lineheight", "행간"), ("letterspacing", "자간"),
        ("hangul", "한글 조판"), ("numerals", "숫자 꼴"), ("truncate", "말줄임"),
        ("webfont", "웹폰트"), ("hierarchy", "글자 위계"),
        ("casing", "대소문자"), ("iconfont", "아이콘 글꼴"),
    ],
    "4부 조작 부품": [
        ("field", "텍스트 필드"), ("select", "셀렉트"), ("combobox", "콤보박스"),
        ("checkbox", "체크박스"), ("radio", "라디오 그룹"), ("switch", "스위치"),
        ("segmented", "세그먼티드 컨트롤"), ("slider", "슬라이더"),
        ("buttonlevel", "버튼 위계"), ("linkbutton", "링크와 버튼"), ("datepicker", "날짜 선택기"),
        ("timepicker", "시간 선택기"), ("quantity", "수량 스테퍼"), ("textarea", "여러 줄 입력"),
        ("password", "비밀번호 칸"), ("numberinput", "숫자 입력"), ("formatted", "자동 서식 입력"),
        ("multiselect", "여러 개 고르기"), ("rangeslider", "범위 슬라이더"), ("colorinput", "색 고르기"),
        ("disabledstate", "비활성과 읽기 전용"), ("splitbutton", "분할 버튼"),
    ],
    "7부 길 안내": [
        ("appbar", "앱바 · 헤더"), ("sidebar", "사이드바 내비게이션"), ("tabs", "탭"),
        ("breadcrumb", "브레드크럼"), ("pagination", "페이지네이션"),
        ("infinite", "무한 스크롤"), ("bottomnav", "바텀 탭바"),
        ("stepper", "스테퍼"), ("treeview", "트리뷰"), ("anchornav", "앵커 내비"),
        ("backnav", "뒤로가기"), ("megamenu", "메가 메뉴"),
    ],
    "8부 피드백과 상태": [
        ("spinner", "스피너"), ("skeleton", "스켈레톤"), ("progress", "프로그레스 바"),
        ("optimistic", "낙관적 UI"), ("empty", "빈 상태"), ("error", "에러 상태"),
        ("undo", "되돌리기"), ("partialload", "부분 로딩"), ("success", "성공 확인"),
        ("retry", "재시도"), ("offline", "오프라인"), ("stale", "오래된 데이터"),
    ],
}

AXES = [
    ("모달",            "막는다",          "가둔다",        "잠긴다",      "가운데"),
    ("다이얼로그(비모달)", "안 막는다",      "안 가둔다",      "그대로",      "가운데 · 띄워 둠"),
    ("바텀시트",         "막거나 안 막는다", "막을 때만",      "막을 때만",   "아래에서"),
    ("드로어",           "보통 막는다",     "가둔다",        "잠긴다",      "옆에서"),
    ("팝오버",           "안 막는다",       "가두기도 한다",  "그대로",      "누른 것 옆에"),
    ("툴팁",            "안 막는다",       "안 가둔다",      "그대로",      "가리킨 것 옆에"),
    ("토스트",          "안 막는다",       "안 가둔다",      "그대로",      "구석 · 저절로 사라짐"),
]
NONE = {"안 막는다", "안 가둔다", "그대로", "모른다", "안 잡는다", "없다", "해당 없음", "—", "안 된다", "없음", "안 보여 준다"}


def axis_table(me):
    rows = []
    for name, a, b, c, d in AXES:
        cells = "".join(
            '<td%s>%s</td>' % (' class="none"' if v in NONE else "", v)
            for v in (a, b, c, d)
        )
        label = "<b>%s</b>" % name if name.startswith(me) else name
        rows.append("            <tr%s><td>%s</td>%s</tr>" %
                    (' class="me"' if name.startswith(me) else "", label, cells))
    return """        <div class="scroll-x">
        <table class="grid axes">
          <thead><tr><th></th><th>뒤를 막나</th><th>포커스를 가두나</th><th>배경 스크롤</th><th>어디서 뜨나</th></tr></thead>
          <tbody>
%s
          </tbody>
        </table>
        </div>""" % "\n".join(rows)


def part_of(me):
    for part, items in PARTS.items():
        if any(slug == me for slug, _ in items):
            return part
    raise KeyError(me)


def siblings(me):
    rows = []
    part = part_of(me)
    short = part.split()[0]
    for slug, ko in PARTS[part]:
        if slug == me:
            continue
        rows.append('        <li><a href="%s.html"><b>%s</b><em>%s</em></a></li>' % (slug, ko, short))
    return "\n".join(rows)


def table(heads, body, me=None):
    """제목줄과 내용줄로 표 하나. me 와 첫 칸이 같은 줄은 굵게."""
    hs = "".join("<th>%s</th>" % h for h in heads)
    rows = []
    for cells in body:
        hit = me is not None and cells[0].startswith(me)
        tds = "".join('<td%s>%s</td>' % (' class="none"' if v in NONE else "", v) for v in cells[1:])
        label = "<b>%s</b>" % cells[0] if hit else cells[0]
        rows.append('            <tr%s><td>%s</td>%s</tr>' % (' class="me"' if hit else "", label, tds))
    return """        <div class="scroll-x">
        <table class="grid axes">
          <thead><tr><th></th>%s</tr></thead>
          <tbody>
%s
          </tbody>
        </table>
        </div>""" % (hs, "\n".join(rows))


def states(items):
    out = []
    for shot, title, desc in items:
        out.append('''          <figure class="state" style="margin:0">
            <div class="shot">
%s
            </div>
            <figcaption>%s<span>%s</span></figcaption>
          </figure>''' % (shot, title, desc))
    return "\n".join(out)


def cases(items):
    out = []
    for shot, title, desc in items:
        out.append('''          <figure class="case" style="margin:0">
            <div class="shot">
%s
            </div>
            <figcaption><b>%s</b>%s</figcaption>
          </figure>''' % (shot, title, desc))
    return "\n".join(out)


def pins(items):
    out = []
    for name, en, desc in items:
        em = ' <em>%s</em>' % en if en else ""
        out.append('            <li><b>%s%s</b><span>%s</span></li>' % (name, em, desc))
    return "\n".join(out)


def plats(items):
    out = []
    for head, sub, shot, foot in items:
        out.append('''          <div class="plat">
            <header><b>%s</b><span>%s</span></header>
            <div class="shot">
%s
            </div>
            <footer>%s</footer>
          </div>''' % (head, sub, shot, foot))
    return "\n".join(out)


def rows(pairs):
    return "\n".join('            <tr><th>%s</th><td>%s</td></tr>' % p for p in pairs)


def ul(items):
    return "\n".join("              <li>%s</li>" % i for i in items)


def kbd(pairs):
    return "\n".join('            <tr><td>%s</td><td>%s</td></tr>' % p for p in pairs)


SLOTS = ["실물", "이름", "가르는 기준", "상태", "해부도", "쓸 때", "사례", "마크업", "백엔드 메모", "플랫폼"]


def page(d):
    d = dict(d)
    d.setdefault("part", part_of(d["slug"]))
    # 칸 이름은 부마다 조금씩 다르다. 토큰에는 '키보드'도 '상태'도 그대로 맞지 않는다.
    # 부마다 비교 축의 첫 줄이 다르다. 안 적은 카드는 그 부의 것을 쓴다.
    PART_LEDE = {
        "4부 조작 부품": "조작 부품은 모두 '값을 받는다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
        "6부 겹치는 것들": "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다.",
    }
    d.setdefault("axes_lede", PART_LEDE.get(d["part"],
                 "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."))
    d.setdefault("s4_title", "상태")
    d.setdefault("s4_hint", "그림 한 장으로는 못 배운다")
    d.setdefault("s8_title", "최소 마크업과 키보드")
    d.setdefault("s8_hint", "이 부품의 계약서")
    d.setdefault("keys_heads", "<th>키</th><th>일어나야 하는 일</th>")
    jump = "".join('<a href="#s%d">%s %s</a>' % (i + 1, "①②③④⑤⑥⑦⑧⑨⑩"[i], n)
                   for i, n in enumerate(SLOTS))
    return '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ko} — 이름표</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../assets/base.css">
<link rel="stylesheet" href="../assets/card.css">
<link rel="stylesheet" href="../assets/demo.css">
</head>
<body>
<a class="skip" href="#main">본문으로</a>

<header class="topbar">
  <a class="brand" href="../index.html">이름표<small>화면 속 그게 뭔지 알려주는 도감</small></a>
  <nav>
    <a href="../index.html#map">화면 지도</a>
    <a href="../index.html#pairs">혼동 쌍</a>
    <a href="../index.html#toc">목차</a>
    <a href="../appendix.html">색인</a>
  </nav>
</header>

<main id="main" class="wrap">

  <div class="item-head">
    <p class="crumb"><a href="../index.html">이름표</a> › <a href="../index.html#toc">{part}</a> › {ko}</p>
    <h1>{ko}</h1>
    <p class="en">{en}</p>
    <p class="lede" style="margin-top:var(--s3)">{lede}</p>
    <nav class="jump" aria-label="이 항목 안에서 이동">{jump}</nav>
  </div>

  <div class="card-layout">
    <div>

      <section class="slot" id="s1">
        <h2 class="slot-label"><span class="n">1</span> 실물 — 직접 만져 보기</h2>
        <div class="preview-bar">
          <div class="seg" data-seg="{slug}" role="group" aria-label="미리보기 폭">
            <button type="button" data-w="390" aria-pressed="false">390 폰</button>
            <button type="button" data-w="768" aria-pressed="false">768 태블릿</button>
            <button type="button" data-w="full" aria-pressed="true">넓게</button>
          </div>
          <span class="preview-meta" data-meta="{slug}"></span>
          <a class="preview-open" href="../demos/{slug}.html" target="_blank" rel="noopener">새 탭에서 열기 ↗</a>
        </div>
        <div class="stage" data-stage="{slug}" data-w="full">
          <iframe src="../demos/{slug}.html" title="{ko} 실물 예시"></iframe>
        </div>
{live_note}
      </section>

      <section class="slot" id="s2">
        <h2 class="slot-label"><span class="n">2</span> 이름<span class="hint">부르는 말이 여러 개다</span></h2>
        <div class="scroll-x">
        <table class="grid">
          <tbody>
{names}
          </tbody>
        </table>
        </div>
      </section>

      <section class="slot" id="s3">
        <h2 class="slot-label"><span class="n">3</span> 가르는 기준<span class="hint">형제들과 비교하는 네 축</span></h2>
        <p>{axes_lede}</p>
{axes}
        <div class="note" style="margin-bottom:0">
          <p><b>한 줄로</b> — {oneline}</p>
        </div>
      </section>

      <section class="slot" id="s4">
        <h2 class="slot-label"><span class="n">4</span> {s4_title}<span class="hint">{s4_hint}</span></h2>
        <div class="states">
{states}
        </div>
      </section>

      <section class="slot" id="s5">
        <h2 class="slot-label"><span class="n">5</span> 해부도<span class="hint">부분 이름이 제일 안 알려진 지식</span></h2>
        <div class="anatomy">
          <div class="pinboard">
            <div class="anat" role="img" aria-label="{ko}의 부분마다 번호를 붙인 그림. 오른쪽 목록에 번호별 이름이 있다.">
{anat}
            </div>
          </div>
          <ol class="pin-list">
{pins}
          </ol>
        </div>
{anat_note}
      </section>

      <section class="slot" id="s6">
        <h2 class="slot-label"><span class="n">6</span> 쓸 때 / 안 쓸 때</h2>
        <div class="twoup">
          <div class="do">
            <h3>이럴 때 쓴다</h3>
            <ul>
{do}
            </ul>
          </div>
          <div class="dont">
            <h3>이럴 때는 안 쓴다</h3>
            <ul>
{dont}
            </ul>
          </div>
        </div>
        <p style="margin:var(--s4) 0 0"><b>대신 이걸</b> — {instead}</p>
      </section>

      <section class="slot" id="s7">
        <h2 class="slot-label"><span class="n">7</span> 자주 보는 모습<span class="hint">구조만 흉내 낸 재현 그림</span></h2>
        <div class="cases">
{cases}
        </div>
      </section>

      <section class="slot" id="s8">
        <h2 class="slot-label"><span class="n">8</span> {s8_title}<span class="hint">{s8_hint}</span></h2>
        <p>{code_lede}</p>
<pre class="code">{code}</pre>
        <div class="scroll-x">
        <table class="grid kbd-table">
          <thead><tr>{keys_heads}</tr></thead>
          <tbody>
{keys}
          </tbody>
        </table>
        </div>
      </section>

      <section class="slot slot--backend" id="s9">
        <h2 class="slot-label"><span class="n">9</span> 서버 쪽으로 치면<span class="hint">백엔드 감각으로 번역</span></h2>
        <div class="scroll-x">
        <table class="grid">
          <tbody>
{backend}
          </tbody>
        </table>
        </div>
      </section>

      <section class="slot" id="s10">
        <h2 class="slot-label"><span class="n">10</span> 플랫폼마다 다른 이름<span class="hint">같은 부품, 다른 말</span></h2>
        <p>{plat_lede}</p>
        <div class="platforms">
{plats}
        </div>
        <div class="note note--warn" style="margin-bottom:0">
          <p><b>자주 생기는 사고</b> — {plat_note}</p>
        </div>
      </section>

    </div>

    <aside class="siblings">
      <h2>헷갈리는 형제</h2>
      <ol>
{siblings}
      </ol>
      <h2>같이 보면 좋은 것</h2>
      <ol>
{related}
      </ol>
      <p style="font-size:12.5px;color:var(--fg-muted)">아직 안 쓴 항목은 회색입니다.</p>
    </aside>
  </div>
</main>

<footer class="site-foot wrap">
  <p>이름표 — 화면 속 그게 뭔지 알려주는 도감. 모든 그림은 직접 그린 재현이고 특정 제품의 화면 캡처가 아닙니다.</p>
</footer>

<script src="../assets/card.js"></script>
</body>
</html>
'''.format(jump=jump, **d)
