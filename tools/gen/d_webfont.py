# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fb(style="", label="", txt="정산이 확정되었습니다", w="150px", note=""):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:5px;'
            'background:var(--surface);padding:9px;min-height:44px;display:grid;align-content:center">'
            '<span style="font-size:12px;line-height:1.6;' + style + '">' + txt + '</span></div>'
            + ('<div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center;margin-top:6px">' + label + '</div>' if label else '')
            + ('<div style="font-size:10px;color:var(--fg-faint);text-align:center">' + note + '</div>' if note else ''))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@font-face { font-family: "Pretendard" }</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">font-display: swap   — 먼저 보여 주기</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">unicode-range   — 쪼개서 필요한 조각만</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">woff2   — 압축 형식. 이것만 쓰면 된다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;link rel="preload"&gt;   — 먼저 받기</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">size-adjust   — 바뀔 때 밀리는 것을 줄인다</div>
                </div>
              </div>'''

D = dict(
  slug="webfont", ko="웹폰트", en="Web font · font loading",
  desc="웹폰트가 받아지는 동안 글이 어떻게 보이는지(FOIT·FOUT)와 한글 폰트의 크기 문제를 보여주는 항목.",
  lede="글꼴 파일을 <b>받아 와서</b> 쓰는 것. 받는 동안 글을 어떻게 보여 줄지까지 정해야 끝납니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>버튼을 눌러 <b>느린 네트워크</b>를 흉내 내 보세요. 위 칸은 <b>글이 아예 안 보이고</b>(FOIT),
          아래 칸은 <b>기본 글꼴로 먼저 보이다 바뀝니다</b>(FOUT).<br>
          못 읽은 시간과, 글꼴이 바뀌며 <b>레이아웃이 밀린 폭</b>을 재서 알려 줍니다 —
          둘 다 실제 사용자가 겪는 것이고, 둘 중 하나는 반드시 고르게 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "웹폰트, 글꼴 파일, 폰트 로딩"),
    ("영어", "web font, font loading, FOIT, FOUT, subsetting"),
    ("같이 쓰는 말",
     "받는 동안 글이 안 보이는 것을 <b>FOIT</b>(Flash of Invisible Text), "
     "기본 글꼴로 보이다 바뀌는 것을 <b>FOUT</b>(Flash of Unstyled Text)라 합니다. "
     "필요한 글자만 추려 파일을 줄이는 것은 <b>서브셋</b>(subsetting), "
     "조각으로 나눠 쓰는 글자만 받는 것은 <b>동적 서브셋</b>입니다."),
    ("자주 잘못 부름",
     "<b>폰트와 서체</b> — 엄밀히는 <b>서체</b>(typeface)가 디자인이고 <b>폰트</b>(font)가 파일입니다. 실무에서는 섞어 씁니다.<br>"
     "<b>시스템 폰트</b> — 기기에 이미 있는 글꼴입니다. <b>받을 게 없어</b> 이 문제가 통째로 없습니다.<br>"
     "<b>woff 와 woff2</b> — 지금은 <b>woff2 하나면</b> 충분합니다."),
  ]),
  axes=ax("웹폰트"),
  oneline="웹폰트는 <b>'받는 동안 어떻게 보일지'</b>까지가 한 세트입니다. 그걸 안 정하면 브라우저가 대신 정합니다.",
  s4_title="상태", s4_hint="받는 동안 무엇이 보이나",
  states=states([
    (fb("visibility:hidden", "block · FOIT", note="글이 아예 안 보인다"), "FOIT", "<b>최대 3초</b> 동안 아무것도 못 읽는다"),
    (fb("font-family:Georgia,serif", "swap · FOUT", note="기본 글꼴로 먼저"), "FOUT", "<b>읽을 수는 있다.</b> 대신 나중에 모양이 바뀐다"),
    (fb("", "다 받은 뒤", note="원하던 글꼴"), "완료", "둘 다 결국 여기로 온다"),
    (fb("font-family:Georgia,serif;font-size:11.4px", "size-adjust", note="크기를 맞춰 둔 대체 글꼴"),
     "밀림 줄이기", "대체 글꼴 크기를 맞춰 두면 <b>바뀔 때 덜 밀린다</b>"),
    (fb("", "시스템 글꼴", "정산이 확정되었습니다", "150px", "받을 게 없다"),
     "시스템 글꼴", "<b>이 문제가 통째로 없다.</b> 가장 빠른 선택"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px;font-family:var(--mono);font-size:10px;color:var(--fg-muted)">
                <div style="display:flex;justify-content:space-between"><span>영문 한 벌</span><span>약 20KB</span></div>
                <div style="display:flex;justify-content:space-between"><span>한글 한 벌</span><span style="color:var(--danger);font-weight:700">약 1~2MB</span></div>
                <div style="display:flex;justify-content:space-between"><span>한글 서브셋</span><span style="color:#1f8a4c;font-weight:700">조각당 10KB</span></div>
              </div>''',
     "파일 크기", "한글은 <b>수십 배</b>다. 서브셋이 거의 필수인 이유"),
  ]),
  anat=ANAT,
  pins=pins([
    ("글꼴 선언", "@font-face", "이름·굵기·파일 위치를 적는다. <b>굵기마다 한 벌</b>"),
    ("받는 동안", "font-display: swap", "<b>먼저 보여 주기.</b> 요즘의 기본 선택"),
    ("쪼개기", "unicode-range", "글자 범위별로 파일을 나눠 <b>쓰는 조각만</b> 받게 한다"),
    ("파일 형식", "woff2", "가장 작다. <b>이것만 적으면 된다</b> — 옛 형식은 이제 필요 없다"),
    ("먼저 받기", "preload", "중요한 한 벌만. 많이 걸면 <b>다른 것이 밀린다</b>"),
    ("밀림 줄이기", "size-adjust · ascent-override", "대체 글꼴의 크기를 맞춰 둬 <b>바뀔 때 덜 흔들리게</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>한글 폰트는 영문의 수십 배</b>입니다. 영문은 대소문자·숫자·기호 해서 수백 자면 끝나지만,
          한글은 완성형만 1만 1172자입니다. 그대로 받으면 한 벌에 1~2MB 라 첫 화면이 그만큼 늦어집니다.
          그래서 <b>글자 범위별로 100여 조각</b>으로 쪼개 두고, 화면에 실제로 쓰인 글자가 든 조각만
          받게 하는 방식(동적 서브셋)이 한국어 사이트의 사실상 표준이 됐습니다.</p>''',
  do=ul([
    "<b>브랜드 글꼴</b>이 정해져 있을 때",
    "시스템 글꼴로는 <b>굵기가 모자랄</b> 때",
    "여러 OS 에서 <b>똑같이 보여야</b> 할 때",
  ]),
  dont=ul([
    "굵기를 <b>다섯 벌 이상</b> 받는 것 — 한글은 한 벌이 1MB 급입니다",
    "<code>font-display</code>를 안 정하는 것 — <b>브라우저가 대신 정합니다</b>(보통 최대 3초 숨김)",
    "본문 글꼴을 바꾸려고 웹폰트를 쓰는 것 — <b>시스템 글꼴로 충분한</b> 경우가 많습니다",
    "서브셋 없이 한글 전체를 받는 것",
  ]),
  instead='굵기 수를 줄이려면 <a href="weight.html">글자 굵기</a>, 글꼴이 바뀌어도 숫자가 안 흔들리게 하려면 <a href="numerals.html">숫자 꼴</a>, 로딩 중 화면은 <a href="../items/skeleton.html">스켈레톤</a>.',
  cases=cases([
    (fb("font-family:Georgia,serif", "swap", "정산이 확정되었습니다", "190px", "먼저 보이고 나중에 바뀐다"),
     "기사·블로그", "읽는 게 목적이라 <b>FOUT 이 맞다</b>"),
    (fb("visibility:hidden", "block", "정산이 확정되었습니다", "190px", "로고·표지처럼 모양이 중요한 곳"),
     "표지·로고", "잠깐 안 보이는 쪽이 나을 때도 있다"),
    (fb("", "시스템 글꼴", "정산이 확정되었습니다", "190px", "받을 게 없어 즉시 보인다"),
     "관리 도구", "내부 도구는 <b>시스템 글꼴</b>로 끝내는 선택이 흔하다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 글꼴의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="<code>@font-face</code> 한 덩어리와 <code>&lt;link&gt;</code> 한 줄입니다.",
  code='''<span class="t">@font-face</span> {
  <span class="a">font-family</span>: <span class="s">"Pretendard"</span>;
  <span class="a">font-weight</span>: <span class="a">400</span>;
  <span class="a">font-display</span>: swap;                 <span class="c">/* 먼저 보여 준다 */</span>
  <span class="a">src</span>: <span class="t">url</span>(<span class="s">"pretendard-400.woff2"</span>) <span class="t">format</span>(<span class="s">"woff2"</span>);
  <span class="a">unicode-range</span>: U+AC00-D7A3;          <span class="c">/* 한글 음절만 */</span>
}

<span class="c">/* 대체 글꼴 크기를 맞춰 두면 바뀔 때 덜 밀린다 */</span>
<span class="t">@font-face</span> {
  <span class="a">font-family</span>: <span class="s">"Pretendard-fallback"</span>;
  <span class="a">src</span>: <span class="t">local</span>(<span class="s">"Apple SD Gothic Neo"</span>);
  <span class="a">size-adjust</span>: <span class="a">96%</span>;
}

&lt;<span class="t">link</span> <span class="a">rel</span>=<span class="s">"preload"</span> <span class="a">as</span>=<span class="s">"font"</span> <span class="a">type</span>=<span class="s">"font/woff2"</span>
      <span class="a">href</span>=<span class="s">"pretendard-400.woff2"</span> <span class="a">crossorigin</span>&gt;''',
  keys=kbd([
    ("<code>font-display: swap</code>", "안 정하면 브라우저가 <b>최대 3초 숨깁니다</b>"),
    ("<code>woff2</code>만", "지금은 이것만 적으면 된다. 옛 형식은 파일만 늘린다"),
    ("서브셋을 쓴다", "한글은 <b>쪼개서 쓰는 조각만</b> 받는다. 직접 호스팅할 때도 마찬가지"),
    ("굵기를 줄인다", "한 벌이 수백 KB~1MB. <b>400·700</b>만으로 시작한다"),
    ("<code>preload</code>는 한둘만", "많이 걸면 <b>다른 자원이 밀린다</b>"),
    ("<code>crossorigin</code>을 잊지 않는다", "폰트 preload 에는 꼭 필요하다. 없으면 <b>두 번 받는다</b>"),
  ]),
  backend=rows([
    ("어디서 받아 오나", "외부 CDN 은 편하지만 <b>그 도메인에 또 연결</b>해야 합니다. 직접 호스팅하면 연결이 하나로 줄어 보통 더 빠릅니다."),
    ("캐시", "글꼴은 거의 안 바뀌므로 <b>아주 길게</b> 캐시합니다(1년). 바꿀 때는 파일 이름에 해시를 넣습니다."),
    ("라이선스", "웹폰트는 <b>웹 전용 라이선스</b>가 따로입니다. 앱이나 이미지에 쓰려면 범위를 확인해야 합니다."),
    ("서버 렌더링", "첫 HTML 에 <code>@font-face</code>가 늦게 오면 그만큼 늦게 받기 시작합니다. <b>CSS 를 인라인</b>으로 넣는 선택을 하기도 합니다."),
    ("측정", "'글이 처음 보인 시각'과 '레이아웃이 밀린 정도'는 각각 <b>FCP</b>와 <b>CLS</b>로 잽니다. 둘 다 웹폰트가 크게 움직입니다."),
  ]),
  plat_lede="앱은 글꼴을 <b>앱 안에 넣어</b> 배포해서, 이 문제 자체가 거의 없습니다.",
  plats=plats([
    ("웹", "@font-face",
     fb("", "woff2 + swap", "정산 확정", "120px"),
     "받아 오는 동안의 상태를 <b>직접 정해야</b> 합니다. 한글 파일 크기가 큰 숙제입니다."),
    ("iOS", "앱 번들",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Info.plist<br>UIAppFonts<br>.custom("…", size:)</div>''',
     "글꼴을 <b>앱에 넣어</b> 배포합니다. 받는 동안이 없어 FOIT·FOUT 가 없습니다."),
    ("안드로이드", "앱 번들 · Downloadable Fonts",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">res/font/<br>Downloadable Fonts</div>''',
     "역시 <b>앱에 넣습니다</b>. 받아 쓰는 방식도 있지만 첫 화면에는 잘 안 씁니다."),
  ]),
  plat_note="앱에는 <b>이 문제가 통째로 없습니다</b> — 글꼴이 앱 안에 들어 있으니까요. 그래서 \"글꼴 바꿔 주세요\"가 앱에서는 용량 몇 MB 늘어나는 일이고, 웹에서는 <b>첫 화면 속도와 레이아웃 밀림</b> 이야기가 됩니다. 같은 요청인데 걱정하는 지점이 다릅니다.",
  siblings=siblings("webfont"),
  related='''        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>''',
)
