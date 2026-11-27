# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def bars(items, w="152px", note=""):
    mx = max(v for _, v, _ in items) or 1
    body = ''.join('<div style="display:grid;grid-template-columns:46px 1fr 44px;gap:5px;align-items:center;font-size:8.5px">'
                   '<span>' + n + '</span>'
                   '<span style="height:8px;border-radius:3px;background:' + ('var(--accent)' if ok else 'var(--line-strong)') +
                   ';width:' + str(max(v / mx * 100, 5)) + '%"></span>'
                   '<span style="font-family:var(--mono);text-align:right;' + ('color:var(--accent);font-weight:700' if ok else '') + '">' + s + '</span></div>'
                   for n, v, (ok, s) in [(n, v, t) for n, v, t in items])
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">'
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">선 · 글자 → SVG. 어느 배율에서나 선명하다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">사진 → WebP · AVIF. SVG 로는 못 만든다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">비트맵은 배율별로 — 1x · 2x · 3x</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">srcset 으로 브라우저가 고르게 한다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글꼴은 윤곽선으로 — 없는 곳에서 깨진다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">SVG 가 늘 작은 것은 아니다 — 점이 많으면 커진다</div>
                </div>
              </div>'''

D = dict(
  slug="assets", ko="에셋 내보내기", en="Exporting assets",
  desc="아이콘·로고·사진을 어떤 꼴로 넘길지. SVG와 배율별 비트맵, 그리고 포맷 고르기.",
  lede="무엇을 내보내느냐에 따라 <b>고를 것이 달라집니다</b>. 선은 SVG, 사진은 배율별 비트맵입니다.",
  axes_lede="현장 용어는 말이 아니라 <b>일하는 단계</b>를 가리킵니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>무엇을 내보낼지 골라 보세요 — 선으로 된 아이콘·로고는 <b>SVG 하나</b>면 어느 배율에서나
          선명하고 파일도 작습니다. 사진은 SVG 로 만들 수 없으니 <b>배율별 비트맵</b>이 필요합니다.<br>
          크기는 어림한 값입니다 — 요점은 숫자가 아니라 <b>어느 쪽이 몇 배 차이나는지</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "에셋, 내보내기, 익스포트, 이미지 추출"),
    ("영어", "assets, export, asset export, slicing"),
    ("같이 쓰는 말",
     "넘기는 그림 파일을 통틀어 <b>에셋</b>이라 하고, 꺼내는 일이 <b>익스포트</b>입니다. "
     "배율별로 뽑는 것을 <b>1x · 2x · 3x</b>, 여러 아이콘을 한 파일에 모은 것을 "
     "<b>스프라이트</b>·<b>아이콘 폰트</b>라 합니다. "
     "SVG 를 HTML 안에 직접 적어 넣는 것은 <b>인라인 SVG</b>입니다."),
    ("자주 잘못 부름",
     "<b>이미지</b> — SVG 는 그림이 아니라 <b>그리는 명령</b>이라 성격이 다릅니다.<br>"
     "<b>해상도</b> — 배율과 섞입니다. <a href=\"dpr.html\">화면 밀도</a>를 참고합니다.<br>"
     "<b>슬라이스</b> — 옛 방식(큰 그림을 잘라 쓰기)의 이름이 남은 말입니다."),
  ]),
  axes=ax("에셋 내보내기"),
  oneline="<b>선이면 SVG, 사진이면 배율별 비트맵.</b> 그리고 포맷을 바꾸는 쪽이 배율보다 효과가 큽니다.",
  s4_title="무엇을 내보내나", s4_hint="고를 것이 달라진다",
  states=states([
    (bars([('SVG', 1, (True, '2 KB')), ('PNG 2x', 3.4, (False, '7 KB')), ('PNG 3x', 7.1, (False, '14 KB'))],
          "152px", "아이콘 — 선 몇 개"),
     "아이콘", "<b>SVG 한 벌.</b> 색도 CSS 로 바꾼다"),
    (bars([('SVG', 1, (True, '6 KB')), ('PNG 2x', 3.2, (False, '19 KB')), ('PNG 3x', 6.8, (False, '41 KB'))],
          "152px", "로고 — 글자 포함"),
     "로고", "글꼴을 <b>윤곽선으로</b> 바꿔 내보낸다"),
    (bars([('JPG 1x', 1, (False, '120 KB')), ('JPG 2x', 3.1, (False, '372 KB')), ('WebP 2x', 1.6, (True, '192 KB'))],
          "152px", "사진 — SVG 로는 못 만든다"),
     "사진", "<b>포맷을 바꾸는 쪽</b>이 효과가 크다"),
    (bars([('SVG', 4.2, (False, '168 KB')), ('PNG 2x', 3.3, (False, '132 KB')), ('WebP 2x', 1.4, (True, '56 KB'))],
          "152px", "일러스트 — 그라데이션이 많다"),
     "일러스트", "<b>SVG 가 더 클 수</b> 있다"),
    (card('<span style="font-size:9px">아이콘 24개</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">한 파일에 모아 두면 요청이 하나</span>', "152px", "스프라이트"),
     "여러 개일 때", "<b>묶어서</b> 한 번에 받는다"),
    (card('<span style="font-size:9px;color:var(--danger)">1배짜리만 받았다</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">3배 화면에서 뭉갠다</span>', "152px", "가장 흔한 사고"),
     "1배만 받으면", "<a href=\"dpr.html\">화면 밀도</a>에서 드러난다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("선 · 글자", "SVG", "어느 배율에서나 선명하고 <b>대개 가장 작다</b>"),
    ("사진", "WebP · AVIF", "SVG 로는 못 만든다. <b>포맷이 먼저</b>"),
    ("배율별", "1x · 2x · 3x", "비트맵은 <b>배율만큼</b> 필요하다"),
    ("고르게 하기", "srcset", "브라우저가 <b>자기 배율에 맞는 것</b>만 받는다"),
    ("글꼴", "윤곽선으로", "안 바꾸면 <b>그 글꼴이 없는 곳</b>에서 깨진다"),
    ("SVG 의 한계", "점이 많으면 커진다", "그라데이션·패턴이 많으면 <b>비트맵이 낫다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>SVG 는 코드라서 다룰 수 있는 것이 많습니다.</b>
          <code>fill="currentColor"</code>로 두면 CSS 의 글자색을 따라가
          <a href="../items/dark.html">다크 모드</a>에서 색을 따로 안 만들어도 되고,
          <code>aria-hidden</code>·<code>&lt;title&gt;</code>로 읽히는 방식도 정할 수 있습니다.
          다만 그만큼 <b>남이 만든 SVG 를 그대로 붙이면</b>
          엉뚱한 <code>id</code>·<code>style</code>이 따라 들어와 다른 그림과 부딪히기도 합니다 —
          받으면 한 번 훑어보는 편이 좋습니다.</p>''',
  do=ul([
    "아이콘·로고는 <b>SVG</b>로 받기",
    "사진은 <b>포맷부터</b> 바꾸기 — WebP·AVIF",
    "비트맵은 <b>배율별</b>로 받고 <code>srcset</code> 으로 고르게 하기",
  ]),
  dont=ul([
    "1배짜리만 받기 — <b>3배 화면에서 뭉갠다</b>",
    "모든 그림을 3배로만 — <b>1배 기기가 손해</b>를 본다",
    "글꼴을 윤곽선으로 안 바꾸기 — <b>깨진다</b>",
    "아이콘을 PNG 로 — <b>색을 못 바꾸고</b> 더 크다",
  ]),
  instead='배율 이야기는 <a href="dpr.html">화면 밀도</a>, 넘기는 일 전체는 <a href="handoff.html">핸드오프</a>, 글꼴 파일은 <a href="../items/webfont.html">웹폰트</a>.',
  cases=cases([
    (code(['&lt;svg fill="currentColor"&gt;', '  &lt;path d="…"/&gt;', '&lt;/svg&gt;'], "150px", "글자색을 따라간다", True),
     "아이콘", "<b>다크 모드</b>가 공짜로 해결된다"),
    (code(['&lt;img src="c-800.jpg"', '  srcset="c-400.jpg 400w,', '    c-1200.jpg 1200w"', '  sizes="(min-width:900px) 33vw, 100vw"&gt;'],
          "150px", "브라우저가 고른다", True),
     "사진", "<b>폭과 배율</b>을 함께 다룬다"),
    (card('<span style="font-size:9px;color:var(--danger)">logo@1x.png 만 받음</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">“로고가 흐릿해요”</span>', "150px"),
     "흔한 민원", "<b>2배·3배를 함께</b> 달라고 한다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 파일의 계약서",
  code_lede="SVG 는 코드로 넣고, 비트맵은 <code>srcset</code> 으로 고르게 합니다.",
  code='''<span class="c">&lt;!-- 아이콘: 색을 CSS 가 정하고, 장식이면 숨긴다 --&gt;</span>
&lt;<span class="t">svg</span> <span class="a">width</span>=<span class="s">"24"</span> <span class="a">height</span>=<span class="s">"24"</span> <span class="a">fill</span>=<span class="s">"currentColor"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;
  &lt;<span class="t">path</span> <span class="a">d</span>=<span class="s">"…"</span>/&gt;
&lt;/<span class="t">svg</span>&gt;

<span class="c">&lt;!-- 뜻이 있는 그림이면 이름을 준다 --&gt;</span>
&lt;<span class="t">svg</span> <span class="a">role</span>=<span class="s">"img"</span> <span class="a">aria-label</span>=<span class="s">"이름표 로고"</span>&gt;…&lt;/<span class="t">svg</span>&gt;

<span class="c">&lt;!-- 사진: 폭과 배율을 브라우저가 고르게 --&gt;</span>
&lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"c-800.webp"</span>
     <span class="a">srcset</span>=<span class="s">"c-400.webp 400w, c-800.webp 800w, c-1200.webp 1200w"</span>
     <span class="a">sizes</span>=<span class="s">"(min-width: 900px) 33vw, 100vw"</span>
     <span class="a">width</span>=<span class="s">"800"</span> <span class="a">height</span>=<span class="s">"450"</span> <span class="a">alt</span>=<span class="s">"모란상회 매장 사진"</span>&gt;''',
  keys=kbd([
    ("<code>fill=\"currentColor\"</code>", "글자색을 따라간다. <b>다크 모드에서 색을 또 안 만들어도</b> 된다"),
    ("장식이면 <code>aria-hidden</code>", "아이콘 옆에 글자가 있으면 <b>두 번 읽히지 않게</b>"),
    ("뜻이 있으면 이름", "로고·상태 아이콘은 <code>role=\"img\"</code> + <code>aria-label</code> — <a href=\"../items/name.html\">이름 붙이기</a>"),
    ("<code>width</code>·<code>height</code>", "미리 적으면 <b>자리가 안 덜컥거린다</b>"),
    ("<code>alt</code>", "사진의 뜻. 장식이면 <code>alt=\"\"</code>로 비운다"),
    ("받은 SVG 를 훑는다", "엉뚱한 <code>id</code>·<code>style</code>이 따라와 <b>다른 그림과 부딪힌다</b>"),
  ]),
  backend=rows([
    ("변환은 서버에서", "원본 하나를 올려 두고 <b>필요한 크기·포맷으로</b> 내려주는 쪽이 파일을 따로 관리하는 것보다 쌉니다."),
    ("포맷이 더 큰 몫", "WebP·AVIF 로 바꾸면 절반 아래로 떨어집니다 — <b>배율보다 먼저</b> 볼 일입니다."),
    ("캐시", "주소를 크기·포맷마다 따로 두면 CDN 이 안 어긋납니다."),
    ("업로드한 사진", "폰 사진은 4000px 이 넘습니다. 받자마자 <b>쓸 크기로 줄여</b> 저장합니다."),
    ("SVG 를 그대로 올리지 않는다", "사용자가 올린 SVG 에는 <b>스크립트가 들어갈 수</b> 있습니다. 걸러 내거나 비트맵으로 바꿉니다."),
  ]),
  plat_lede="<b>벡터 한 벌 vs 배율별 비트맵</b>이라는 선택은 어디나 같습니다.",
  plats=plats([
    ("웹", "SVG · srcset",
     code(['icon.svg', 'photo@2x.webp'], "110px", "", True),
     "SVG 를 코드로 넣을 수 있는 것이 큰 이점입니다. <b>색·접근성</b>을 CSS 로 다룹니다."),
    ("iOS", "@2x @3x · SF Symbols",
     '''              <div class="phone" role="img" aria-label="iOS 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">icon@2x.png<br>icon@3x.png</div></div></div>''',
     "파일 이름에 배율을 붙입니다. 시스템 아이콘(<b>SF Symbols</b>)은 내보낼 필요가 없습니다."),
    ("안드로이드", "벡터 드로어블",
     '''              <div class="phone" role="img" aria-label="안드로이드 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">drawable/ic_store.xml</div></div></div>''',
     "<b>벡터 드로어블</b>이 SVG 자리입니다. 쓰면 배율별 폴더가 필요 없습니다."),
  ]),
  plat_note="\"아이콘 파일 주세요\"로 끝나면 나중에 <b>색을 못 바꾸는 PNG</b>가 쌓입니다. 받을 때 <b>SVG 로, 색은 currentColor 로</b>를 한 번 말해 두면 다크 모드·상태 색이 전부 공짜로 해결되고, 사진은 <b>원본 한 장</b>만 받아 서버에서 줄이는 쪽이 파일 관리보다 훨씬 쌉니다.",
  siblings=siblings("assets"),
  related='''        <li><a href="dpr.html"><b>화면 밀도</b><em>11부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>''',
)
