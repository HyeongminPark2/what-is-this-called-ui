# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">선 · 글자는 SVG로, 어느 배율에서나 선명함</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">사진은 WebP · AVIF로, SVG로는 못 만듦</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">비트맵은 배율마다 1x · 2x · 3x로 뽑음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">srcset으로 브라우저가 고르게 함</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">글꼴을 윤곽선으로 안 바꾸면 깨짐</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">SVG도 점이 많으면 비트맵보다 커짐</div>
                </div>
              </div>'''

D = dict(
  slug="assets", ko="에셋 내보내기", en="Exporting assets",
  desc="아이콘과 로고, 사진을 어떤 형식으로 넘길지 다루는 항목입니다. SVG와 배율별 비트맵 가운데 무엇을 쓰고, 파일 포맷은 어떻게 고르는지 보여 줍니다.",
  lede="에셋 내보내기는 시안에 쓴 그림을 개발에서 쓸 파일로 꺼내는 일이고, 무엇을 내보내느냐에 따라 <b>골라야 할 형식이 달라집니다</b>. 선으로 된 그림은 SVG로, 사진은 배율별 비트맵으로 내보냅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>무엇을 내보낼지 골라 보세요. 선으로 된 아이콘과 로고는 <b>SVG 파일 하나</b>만 있으면 어느 배율에서나
          선명하고 파일도 작습니다. 반면 사진은 SVG로 만들 수 없기 때문에 <b>배율별 비트맵</b>이 필요합니다.<br>
          파일 크기는 어림한 값이므로, 숫자 자체보다 <b>어느 쪽이 몇 배 차이 나는지</b>를 보면 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "에셋, 내보내기, 익스포트, 이미지 추출"),
    ("영어", "assets, export, asset export, slicing"),
    ("같이 쓰는 말",
     "개발 쪽에 넘기는 그림 파일을 통틀어 <b>에셋</b>이라고 하고, 시안 도구에서 파일로 꺼내는 일을 <b>익스포트</b>라고 합니다. "
     "배율별로 뽑은 파일은 <b>1x · 2x · 3x</b>로 구분하고, 여러 아이콘을 한 파일에 모은 것은 "
     "<b>스프라이트</b> 또는 <b>아이콘 폰트</b>라고 부릅니다. "
     "SVG를 HTML 안에 직접 적어 넣는 방식은 <b>인라인 SVG</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>이미지</b> — SVG는 점으로 찍힌 그림이 아니라 <b>그림을 그리는 명령</b>을 적은 파일이라서 다른 이미지 파일과 성격이 다릅니다.<br>"
     "<b>해상도</b> — 배율과 섞어 부르는 일이 많습니다. 둘의 차이는 <a href=\"dpr.html\">화면 밀도</a> 항목에 있습니다.<br>"
     "<b>슬라이스</b> — 큰 그림을 잘라 쓰던 옛 방식의 이름이 지금까지 남은 말입니다."),
  ]),
  s4_title="내보내는 그림의 종류", s4_hint="종류마다 알맞은 형식",
  states=states([
    (bars([('SVG', 1, (True, '2 KB')), ('PNG 2x', 3.4, (False, '7 KB')), ('PNG 3x', 7.1, (False, '14 KB'))],
          "152px", "선 몇 개로 된 아이콘"),
     "아이콘", "<b>SVG 한 벌</b>이면 되고, 색도 CSS로 바꿀 수 있습니다"),
    (bars([('SVG', 1, (True, '6 KB')), ('PNG 2x', 3.2, (False, '19 KB')), ('PNG 3x', 6.8, (False, '41 KB'))],
          "152px", "글자가 들어간 로고"),
     "로고", "로고 속 글꼴을 <b>윤곽선으로</b> 바꿔서 내보냅니다"),
    (bars([('JPG 1x', 1, (False, '120 KB')), ('JPG 2x', 3.1, (False, '372 KB')), ('WebP 2x', 1.6, (True, '192 KB'))],
          "152px", "SVG로는 못 만드는 사진"),
     "사진", "배율을 줄이는 것보다 <b>포맷을 바꾸는 쪽</b>이 파일 크기를 줄이는 효과가 큽니다"),
    (bars([('SVG', 4.2, (False, '168 KB')), ('PNG 2x', 3.3, (False, '132 KB')), ('WebP 2x', 1.4, (True, '56 KB'))],
          "152px", "그라데이션이 많은 일러스트"),
     "일러스트", "그라데이션이 많으면 <b>SVG가 비트맵보다 더 클 수</b> 있습니다"),
    (card('<span style="font-size:9px">아이콘 24개</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">한 파일에 모으면 요청이 한 번</span>', "152px", "스프라이트"),
     "아이콘이 여러 개일 때", "여러 아이콘을 한 파일로 <b>묶어서</b> 한 번에 받습니다"),
    (card('<span style="font-size:9px;color:var(--danger)">1배짜리만 받음</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">3배 화면에서 뭉개짐</span>', "152px", "가장 흔한 실수"),
     "1배 파일만 받았을 때", "<a href=\"dpr.html\">화면 밀도</a>가 높은 기기에서 그림이 흐릿하게 보입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("선 · 글자", "SVG", "어느 배율에서나 선명하고, 파일도 <b>대개 가장 작습니다</b>"),
    ("사진", "WebP · AVIF", "사진은 SVG로 만들 수 없으니 <b>포맷부터</b> 고릅니다"),
    ("배율별 파일", "1x · 2x · 3x", "비트맵은 지원할 <b>배율마다</b> 한 장씩 필요합니다"),
    ("브라우저가 고르게 하기", "srcset", "브라우저가 그 기기의 <b>배율에 맞는 파일</b>만 골라 받습니다"),
    ("글꼴", "윤곽선으로 변환", "윤곽선으로 바꾸지 않으면 <b>그 글꼴이 설치되지 않은 곳</b>에서 글자가 깨집니다"),
    ("SVG 의 한계", "점이 많으면 커짐", "그라데이션이나 패턴이 많은 그림은 <b>비트맵이 더 작습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>SVG는 코드이기 때문에 CSS와 HTML로 다룰 수 있는 것이 많습니다.</b>
          <code>fill="currentColor"</code>로 두면 아이콘 색이 CSS의 글자색을 따라가므로
          <a href="../items/dark.html">다크 모드</a>용 색을 따로 만들지 않아도 되고,
          <code>aria-hidden</code>이나 <code>&lt;title&gt;</code>로 스크린 리더가 읽는 방식도 정할 수 있습니다.
          반대로 코드이기 때문에 <b>남이 만든 SVG를 그대로 붙이면</b>
          그 안의 <code>id</code>나 <code>style</code>이 함께 들어와 페이지의 다른 그림과 충돌하기도 합니다.
          그래서 SVG를 받으면 안의 코드를 한 번 훑어보는 편이 좋습니다.</p>''',
  do_title="에셋을 내보낼 때 지킬 것",
  dont_title="에셋을 내보낼 때 피할 것",
  do=ul([
    "아이콘과 로고는 <b>SVG</b>로 받습니다",
    "사진은 WebP나 AVIF로 <b>포맷부터</b> 바꿉니다",
    "비트맵은 <b>배율별</b>로 받아 <code>srcset</code>으로 브라우저가 고르게 합니다",
  ]),
  dont=ul([
    "1배짜리 파일만 받을 때. <b>3배 화면에서는 그림이 뭉개져</b> 보입니다",
    "모든 그림을 3배짜리로만 넣을 때. <b>1배 기기는 쓰지도 않을 큰 파일을</b> 받게 됩니다",
    "로고의 글꼴을 윤곽선으로 바꾸지 않을 때. 글꼴이 없는 곳에서 <b>글자가 깨집니다</b>",
    "아이콘을 PNG로 받을 때. CSS로 <b>색을 바꿀 수 없고</b> 파일도 더 큽니다",
  ]),
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  instead='배율에 관한 자세한 내용은 <a href="dpr.html">화면 밀도</a>에서, 시안을 넘기는 일 전체는 <a href="handoff.html">핸드오프</a>에서, 글꼴 파일은 <a href="../items/webfont.html">웹폰트</a>에서 다룹니다.',
  cases=cases([
    (code(['&lt;svg fill="currentColor"&gt;', '  &lt;path d="…"/&gt;', '&lt;/svg&gt;'], "150px", "글자색을 따라감", True),
     "아이콘 색을 글자색에 맞추기", "글자색을 따라가므로 <b>다크 모드</b>용 색을 따로 만들지 않아도 됩니다"),
    (code(['&lt;img src="c-800.jpg"', '  srcset="c-400.jpg 400w,', '    c-1200.jpg 1200w"', '  sizes="(min-width:900px) 33vw, 100vw"&gt;'],
          "150px", "브라우저가 고름", True),
     "사진을 폭과 배율에 맞게 고르기", "화면 <b>폭과 배율</b>에 맞는 파일을 브라우저가 함께 따져서 고릅니다"),
    (card('<span style="font-size:9px;color:var(--danger)">logo@1x.png 만 받음</span>'
          '<span style="font-size:8.5px;color:var(--fg-muted)">“로고가 흐릿해요”</span>', "150px"),
     "로고가 흐릿하다는 민원 막기", "로고를 받을 때 <b>2배·3배 파일도 함께</b> 달라고 합니다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="SVG와 비트맵을 넣는 법",
  code_lede="SVG는 코드로 직접 넣고, 비트맵은 <code>srcset</code>으로 여러 파일을 적어 브라우저가 고르게 합니다.",
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
  keys_heads="<th>지킬 규칙</th><th>그렇게 하는 이유</th>",
  keys=kbd([
    ("<code>fill=\"currentColor\"</code>", "아이콘 색이 글자색을 따라가므로 <b>다크 모드용 색을 따로 만들지 않아도</b> 됩니다"),
    ("장식용이면 <code>aria-hidden</code> 달기", "아이콘 옆에 같은 뜻의 글자가 있으면 스크린 리더가 <b>두 번 읽지 않도록</b> 아이콘을 숨깁니다"),
    ("뜻이 있는 그림에 이름 붙이기", "로고나 상태 아이콘에는 <code>role=\"img\"</code>와 <code>aria-label</code>로 이름을 붙입니다(<a href=\"../items/name.html\">이름 붙이기</a> 참고)"),
    ("<code>width</code>·<code>height</code>", "크기를 미리 적어 두면 그림을 불러오는 동안 <b>주변 내용이 밀리지 않습니다</b>"),
    ("<code>alt</code>", "사진이 전하는 뜻을 적습니다. 장식용 사진이면 <code>alt=\"\"</code>로 비워 둡니다"),
    ("받은 SVG 코드 훑어보기", "받은 SVG에 딸려 온 <code>id</code>나 <code>style</code>이 <b>페이지의 다른 그림과 충돌</b>할 수 있습니다"),
  ]),
  backend=rows([
    ("크기와 포맷 변환은 서버에서 하기", "원본 하나만 올려 두고 요청에 따라 <b>필요한 크기와 포맷으로</b> 바꿔 내려주면, 크기별 파일을 따로 관리하는 것보다 비용이 적게 듭니다."),
    ("배율보다 효과가 큰 포맷 변경", "사진을 WebP나 AVIF로 바꾸면 파일 크기가 절반 아래로 줄어듭니다. 그래서 배율을 따지기 <b>전에 포맷부터</b> 확인합니다."),
    ("크기와 포맷마다 주소 나누기", "크기와 포맷마다 주소를 따로 두면 CDN이 다른 파일을 잘못 내주는 일이 생기지 않습니다."),
    ("업로드한 사진 줄여 저장하기", "휴대폰으로 찍은 사진은 폭이 4000px을 넘기도 하므로, 업로드를 받자마자 <b>실제로 쓸 크기로 줄여서</b> 저장합니다."),
    ("사용자가 올린 SVG 걸러 내기", "SVG 안에는 <b>스크립트를 넣을 수</b> 있기 때문에, 사용자가 올린 SVG는 위험한 내용을 걸러 내거나 비트맵으로 바꿔서 저장합니다."),
  ]),
  plat_lede="<b>벡터 파일 한 벌</b>을 쓸지 <b>배율별 비트맵</b>을 쓸지 고르는 일은 어느 플랫폼에서나 같습니다.",
  plats=plats([
    ("웹", "SVG · srcset",
     code(['icon.svg', 'photo@2x.webp'], "110px", "", True),
     "SVG를 코드로 직접 넣을 수 있다는 것이 큰 이점입니다. 덕분에 아이콘의 <b>색과 접근성</b>을 CSS와 HTML 속성으로 다룰 수 있습니다."),
    ("iOS", "@2x @3x · SF Symbols",
     '''              <div class="phone" role="img" aria-label="iOS 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">icon@2x.png<br>icon@3x.png</div></div></div>''',
     "<code>icon@2x.png</code>처럼 파일 이름에 배율을 붙입니다. OS가 제공하는 시스템 아이콘(<b>SF Symbols</b>)은 따로 내보낼 필요가 없습니다."),
    ("안드로이드", "벡터 드로어블",
     '''              <div class="phone" role="img" aria-label="안드로이드 에셋 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">drawable/ic_store.xml</div></div></div>''',
     "<b>벡터 드로어블</b>이 웹의 SVG에 해당하며, 벡터 드로어블을 쓰면 배율별 폴더를 따로 두지 않아도 됩니다."),
  ]),
  plat_note="\"아이콘 파일 주세요\"라고만 요청하면 나중에 <b>색을 바꿀 수 없는 PNG</b> 파일이 쌓입니다. 요청할 때 <b>SVG로, 색은 currentColor로</b> 달라고 한 번만 말해 두면 다크 모드와 상태별 색을 따로 만들 필요가 없어집니다. 사진은 <b>원본 한 장</b>만 받아 서버에서 줄여 쓰는 쪽이 크기별 파일을 관리하는 것보다 훨씬 적은 비용이 듭니다.",
  siblings=siblings("assets"),
  related='''        <li><a href="dpr.html"><b>화면 밀도</b><em>11부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>''',
)
