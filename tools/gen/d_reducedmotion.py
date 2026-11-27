# -*- coding: utf-8 -*-
from ax9 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def card(inner, verdict, keep, w="150px"):
    col = "var(--accent)" if keep else "var(--danger)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:4px">'
            '<div style="height:52px;border-radius:6px;background:var(--bg);border:1px solid var(--line);position:relative;overflow:hidden">'
            + inner + '</div>'
            '<span style="font-size:9.5px;font-weight:700;color:' + col + '">' + verdict + '</span></div>')

BOX = '<span style="position:absolute;top:14px;left:12px;width:22px;height:22px;border-radius:5px;background:var(--accent)"></span>'
BOXR = '<span style="position:absolute;top:14px;right:12px;width:22px;height:22px;border-radius:5px;background:var(--accent)"></span>'
ARROW = ('<span style="position:absolute;top:23px;left:40px;right:40px;height:2px;background:var(--danger)"></span>'
         '<span style="position:absolute;top:19px;right:38px;width:8px;height:8px;border-top:2px solid var(--danger);border-right:2px solid var(--danger);transform:rotate(45deg)"></span>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">@media (prefers-reduced-motion: reduce)</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">끈다 — 큰 거리 이동 · 확대 축소 · 시차 스크롤</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--warn)">줄인다 — 끝없이 도는 것 · 자동 재생</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">남긴다 — 투명도 · 색 · 아주 짧은 미끄러짐</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">기본값은 no-preference — 켠 사람만 reduce</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">*{animation:none} 으로 다 끄면 변화를 못 읽는다</div>
                </div>
              </div>'''

D = dict(
  slug="reducedmotion", ko="모션 줄이기", en="Reduced motion",
  desc="어지럼증을 피하려 OS 에서 켜는 설정. 전부 끄는 것이 아니라 무엇을 끄고 무엇을 남길지의 문제.",
  lede="OS 설정 하나로 \"움직임을 줄여 달라\"는 말이 옵니다. <b>전부 끄라는 뜻이 아닙니다.</b>",
  axes_lede="움직임은 장식이 아니라 <b>말</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>여섯 가지가 움직이고 있습니다. <b>줄이기를 켠 사람으로 보기</b>를 눌러 보세요 —
          셋은 멎고 셋은 그대로입니다.<br>
          멎는 쪽은 <b>큰 거리를 지나가는 이동·확대·끝없이 도는 것</b>이고,
          남는 쪽은 <b>투명도·색·아주 짧은 미끄러짐</b>입니다.
          남는 것이 있어야 <b>무엇이 바뀌었는지</b>를 알 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "모션 줄이기, 동작 줄이기, 애니메이션 효과 감소"),
    ("영어", "reduced motion, prefers-reduced-motion"),
    ("같이 쓰는 말",
     "맥·아이폰 설정에서는 <b>'동작 줄이기'</b>, 윈도우에서는 <b>'애니메이션 표시'</b> 끄기, "
     "안드로이드에서는 <b>'애니메이션 삭제'</b>입니다. "
     "브라우저에는 <code>prefers-reduced-motion: reduce</code>로 전해집니다. "
     "비슷한 설정으로 <code>prefers-reduced-transparency</code>·<code>prefers-reduced-data</code>도 있습니다."),
    ("자주 잘못 부름",
     "<b>접근성 설정</b> — 맞지만 범위가 넓습니다. 이것은 <b>움직임 하나</b>에 대한 설정입니다.<br>"
     "<b>저사양 모드</b> — 성능 문제가 아니라 <b>몸의 문제</b>입니다. 빠른 기기에서도 켭니다.<br>"
     "<b>다크 모드</b>처럼 디자인 선택이 아닙니다 — <b>어지럼증·멀미</b>를 피하려고 켭니다."),
  ]),
  axes=ax("모션 줄이기"),
  oneline="끄는 기준은 <b>'이게 멀미를 일으킬까'</b>입니다. 큰 거리·확대·시차·끝없이 도는 것은 끄고, <b>자리를 거의 안 옮기는 것은 남깁니다</b>.",
  s4_title="끌 것과 남길 것", s4_hint="전부 끄는 것이 아니다",
  states=states([
    (card(BOX + ARROW + BOXR, "끈다 — 큰 거리를 빠르게", False), "가로지르는 이동", "<b>멀미의 가장 큰 원인</b>"),
    (card('<span style="position:absolute;inset:6px;border-radius:6px;background:var(--accent);opacity:.9"></span>'
          '<span style="position:absolute;inset:16px;border-radius:5px;border:2px dashed var(--surface)"></span>', "끈다 — 덮쳐 오는 느낌", False),
     "확대하며 열기", "화면이 <b>달려드는</b> 것처럼 보인다"),
    (card('<span style="position:absolute;left:50%;top:14px;transform:translateX(-50%);width:22px;height:22px;border-radius:50%;border:3px solid var(--line);border-top-color:var(--accent)"></span>', "줄인다 — 계속 도는 것", False),
     "끝없이 도는 스피너", "<b>세 점이 차례로 밝아지는</b> 꼴로 바꾼다"),
    (card('<span style="position:absolute;inset:12px;border-radius:5px;background:var(--accent);opacity:.3"></span>', "남긴다 — 자리를 안 옮긴다", True),
     "투명도만 바뀜", "<b>페이드는 안전하다.</b> 남겨야 한다"),
    (card('<span style="position:absolute;inset:12px;border-radius:5px;background:var(--warn)"></span>', "남긴다 — 움직임이 아니다", True),
     "색 바뀜 · 테두리", "상태가 바뀐 것을 <b>알릴 유일한 길</b>일 수도 있다"),
    (card('<span style="position:absolute;top:14px;left:18px;width:22px;height:22px;border-radius:5px;background:var(--accent)"></span>'
          '<span style="position:absolute;top:14px;left:28px;width:22px;height:22px;border-radius:5px;background:var(--accent);opacity:.25"></span>', "남겨도 된다 — 8px 남짓", True),
     "짧은 미끄러짐", "거리를 더 줄이거나 그대로 둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("질의", "prefers-reduced-motion", "값은 <code>no-preference</code>와 <code>reduce</code> 둘뿐"),
    ("끄는 것", "큰 이동 · 확대 · 시차", "<b>화면이 나를 움직이는</b> 느낌을 주는 것들"),
    ("줄이는 것", "도는 것 · 자동 재생", "아예 없애면 <b>진행 중</b>임을 알 길이 없다"),
    ("남기는 것", "투명도 · 색", "자리를 안 옮긴다. <b>안전하고 필요하다</b>"),
    ("기본값", "no-preference", "<b>켠 사람만</b> reduce 다. 모르면 안 켠 것으로 본다"),
    ("과잉 대응", "전부 끄기", "<code>*{animation:none}</code>은 <b>변화를 못 읽게</b> 만든다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>전부 끄는 한 줄</b>이 인터넷에 많이 돌아다닙니다 —
          <code>*{animation-duration:.01ms!important}</code>.
          안 하는 것보다는 낫지만, <b>나타남과 사라짐까지 사라져</b>
          토스트가 번쩍하고 없어지거나 메뉴가 순간이동합니다.
          제대로 하려면 <b>거리를 줄이고 투명도는 남기는</b> 쪽으로 항목마다 정해야 합니다.
          CSS 변수 하나로 거리를 0 에 가깝게 만드는 방법이 품이 가장 적습니다.</p>''',
  do=ul([
    "<b>움직이는 것을 만들 때마다</b> 함께 — 나중에 몰아서 하면 빠뜨린다",
    "자동 재생 영상·배너 — <b>멈춰 둔다</b>",
    "시차 스크롤·스크롤로 따라 움직이는 것 — <b>가장 먼저 끈다</b>",
  ]),
  dont=ul([
    "<b>전부 끄기</b> — 무엇이 바뀌었는지 못 읽게 된다",
    "줄이기를 켠 사람에게 <b>기능을 덜 주는</b> 것",
    "<b>성능 설정</b>으로 오해해 저사양 기기에만 적용하기",
    "<code>!important</code>로 덮어쓰기 — 필요한 전환까지 죽는다",
  ]),
  instead='길이를 줄이는 것은 <a href="duration.html">지속 시간</a>, 흔들림을 없애는 것은 <a href="spring.html">스프링</a>의 튕김 0, 자동으로 도는 것은 <a href="../items/spinner.html">스피너</a> 쪽에서.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>@media (prefers-reduced-motion: reduce) {</span>
                <span>&nbsp;&nbsp;:root { <span style="color:var(--accent)">--move: 0px; --dur: 1ms</span> }</span>
                <span>}</span>
              </div>''',
     "변수 두 개로", "거리와 길이를 변수로 두면 <b>한 곳에서</b> 끝난다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;font-size:9.5px">
                <b>자동 재생 중</b> · <span style="color:var(--accent);text-decoration:underline">멈추기</span><br>
                <span style="font-size:8.5px;color:var(--fg-muted)">줄이기에서는 처음부터 멈춤</span>
              </div>''',
     "멈출 길을 둔다", "자동으로 도는 것에는 <b>멈춤 버튼</b>이 함께 있어야 한다"),
    ('''              <div style="width:100%;max-width:152px;display:flex;gap:4px;align-items:center">
                <span style="width:7px;height:7px;border-radius:50%;background:var(--accent)"></span>
                <span style="width:7px;height:7px;border-radius:50%;background:var(--accent);opacity:.5"></span>
                <span style="width:7px;height:7px;border-radius:50%;background:var(--accent);opacity:.2"></span>
                <span style="font-size:9px;color:var(--fg-muted)">도는 대신 밝아지기</span>
              </div>''',
     "도는 것을 바꾼다", "<b>없애지 말고</b> 안 도는 꼴로 바꾼다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 설정의 계약서",
  code_lede="거리와 길이를 <b>변수</b>로 두면 질의 하나로 전부 처리됩니다.",
  code=''':root { <span class="a">--move</span>: <span class="a">8px</span>; <span class="a">--dur</span>: <span class="a">220ms</span>; }

.card { <span class="a">transform</span>: translateY(<span class="a">var</span>(--move)); <span class="a">transition</span>: <span class="a">var</span>(--dur) <span class="a">var</span>(--ease-out); }

@media (prefers-reduced-motion: reduce) {
  :root { <span class="a">--move</span>: <span class="a">0px</span>; <span class="a">--dur</span>: <span class="a">1ms</span>; }
  .parallax { <span class="a">transform</span>: none !important; }   <span class="c">/* 시차는 아예 끈다 */</span>
  .spinner  { <span class="a">animation</span>: pulse <span class="a">1.2s</span> ease-in-out infinite; }  <span class="c">/* 돌지 말고 깜빡 */</span>
}

<span class="c">// 자바스크립트 애니메이션도 물어본다</span>
<span class="k">const</span> calm = matchMedia(<span class="s">'(prefers-reduced-motion: reduce)'</span>);
<span class="k">if</span> (calm.matches) el.scrollIntoView();
<span class="k">else</span> el.scrollIntoView({ behavior: <span class="s">'smooth'</span> });''',
  keys=kbd([
    ("<code>matchMedia</code>로 물어본다", "CSS 밖의 애니메이션(캔버스·자바스크립트)도 <b>같이 줄여야</b> 한다"),
    ("<code>scroll-behavior: smooth</code>", "부드러운 스크롤도 멀미를 일으킨다. 줄이기에서는 <code>auto</code>로"),
    ("<code>.addEventListener('change')</code>", "설정은 <b>쓰는 중에도</b> 바뀐다. 한 번 읽고 끝내지 않는다"),
    ("켠 사람에게 <b>덜 주지 않는다</b>", "기능은 그대로고 <b>움직임만</b> 줄인다"),
    ("자동 재생에는 멈춤 버튼", "WCAG 는 5초 넘게 자동으로 움직이는 것에 <b>멈출 길</b>을 요구한다"),
    ("시험하는 법", "개발자 도구에서 <code>prefers-reduced-motion</code>을 <b>흉내 낼 수</b> 있다"),
  ]),
  backend=rows([
    ("서버는 알 수 없다", "이 설정은 <b>요청 헤더로 오지 않습니다.</b> 서버가 미리 렌더링해 보내는 화면에서는 CSS 질의로만 처리됩니다."),
    ("클라이언트 힌트", "<code>Sec-CH-Prefers-Reduced-Motion</code> 헤더가 있지만 <b>지원이 고르지 않아</b> 기대지 않는 편이 낫습니다."),
    ("자동 재생 영상", "줄이기를 켠 사람에게는 <b>포스터 이미지만</b> 보내면 데이터도 아낍니다."),
  ]),
  plat_lede="세 OS 모두 설정에 있고, <b>이름만 다릅니다</b>.",
  plats=plats([
    ("웹", "prefers-reduced-motion",
     '''              <div style="width:100%;max-width:110px;font-family:var(--mono);font-size:8.5px;color:var(--accent);border:1px solid var(--line);border-radius:6px;background:var(--bg);padding:6px">@media (prefers-<br>reduced-motion:<br>reduce) { … }</div>''',
     "OS 설정을 그대로 받습니다. <b>따로 켤 것이 없고</b> 안 쓰면 그냥 무시되는 것뿐입니다."),
    ("iOS", "동작 줄이기",
     '''              <div class="phone" role="img" aria-label="iOS 설정 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;align-items:center;gap:4px;font-size:6px"><span style="flex:1">동작 줄이기</span><span style="width:14px;height:8px;border-radius:999px;background:var(--accent)"></span></div></div></div>''',
     "손쉬운 사용 › 동작. 켜면 <b>앱 열기 확대 효과</b>가 페이드로 바뀝니다."),
    ("안드로이드", "애니메이션 삭제",
     '''              <div class="phone" role="img" aria-label="안드로이드 설정 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;align-items:center;gap:4px;font-size:6px"><span style="flex:1">애니메이션 삭제</span><span style="width:14px;height:8px;border-radius:999px;background:var(--accent)"></span></div></div></div>''',
     "접근성 › 애니메이션 삭제. 개발자 옵션의 <b>애니메이션 배율</b>과는 다른 설정입니다."),
  ]),
  plat_note="\"접근성 챙겨 주세요\"에서 가장 싸게 끝나는 항목입니다 — 거리와 길이를 변수로 둔 프로젝트라면 <b>질의 한 번</b>이면 됩니다. 반대로 숫자를 화면마다 박아 둔 프로젝트에서는 수십 군데를 뒤져야 합니다. <b>토큰으로 둘 이유</b>가 여기에 하나 더 있습니다.",
  siblings=siblings("reducedmotion"),
  related='''        <li><a href="duration.html"><b>지속 시간</b><em>9부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>
        <li><a href="../items/spinner.html"><b>스피너</b><em>8부</em></a></li>
        <li><a href="../items/screenreader.html"><b>스크린 리더가 읽는 것</b><em>12부</em></a></li>''',
)
