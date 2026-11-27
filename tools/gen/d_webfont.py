# -*- coding: utf-8 -*-
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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">font-display: swap   글을 먼저 보여 주기</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">unicode-range   필요한 조각만 나눠 받기</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">woff2   이것 하나면 되는 압축 형식</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">&lt;link rel="preload"&gt;   미리 받아 두기</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">size-adjust   글꼴이 바뀔 때 밀림을 줄임</div>
                </div>
              </div>'''

D = dict(
  slug="webfont", ko="웹폰트", en="Web font · font loading",
  desc="웹폰트를 받는 동안 글이 어떻게 보이는지(FOIT·FOUT)와 한글 폰트의 파일 크기 문제를 보여 주는 항목입니다.",
  lede="웹폰트는 글꼴 파일을 서버에서 <b>받아 와서</b> 쓰는 방식입니다. 파일을 받는 데 시간이 걸리기 때문에, 받는 동안 글을 어떻게 보여 줄지까지 정해야 합니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>버튼을 눌러 <b>느린 네트워크</b>를 흉내 내 보세요. 위 칸은 <b>글이 아예 보이지 않고</b>(FOIT),
          아래 칸은 <b>기본 글꼴로 먼저 보이다가 바뀝니다</b>(FOUT).<br>
          글을 읽지 못한 시간과, 글꼴이 바뀌면서 <b>레이아웃이 밀린 폭</b>을 재서 알려 줍니다.
          두 현상 모두 실제 사용자가 겪는 일이고, 웹폰트를 쓰면 둘 중 하나는 반드시 골라야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "웹폰트, 글꼴 파일, 폰트 로딩"),
    ("영어", "web font, font loading, FOIT, FOUT, subsetting"),
    ("같이 쓰는 말",
     "글꼴을 받는 동안 글이 보이지 않는 현상을 <b>FOIT</b>(Flash of Invisible Text), "
     "기본 글꼴로 보이다가 바뀌는 현상을 <b>FOUT</b>(Flash of Unstyled Text)라고 합니다. "
     "필요한 글자만 추려 파일을 줄이는 작업은 <b>서브셋</b>(subsetting), "
     "글꼴을 여러 조각으로 나눠 두고 화면에 쓰인 글자가 든 조각만 받는 방식은 <b>동적 서브셋</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>폰트와 서체</b> — 엄밀히 말하면 <b>서체</b>(typeface)는 글자의 디자인이고 <b>폰트</b>(font)는 그 디자인을 담은 파일이지만, 실무에서는 섞어 씁니다.<br>"
     "<b>시스템 폰트</b> — 기기에 이미 깔려 있는 글꼴입니다. <b>받을 파일이 없어서</b> 웹폰트의 로딩 문제가 아예 생기지 않습니다.<br>"
     "<b>woff와 woff2</b> — 지금은 <b>woff2 하나만</b> 준비해도 충분합니다."),
  ]),
  s4_title="글꼴을 받는 동안의 상태", s4_hint="받는 동안 화면에 보이는 것",
  states=states([
    (fb("visibility:hidden", "block · FOIT", note="글이 아예 안 보임"), "글을 숨기는 FOIT", "<b>최대 3초</b> 동안 글을 전혀 읽을 수 없습니다"),
    (fb("font-family:Georgia,serif", "swap · FOUT", note="기본 글꼴로 먼저"), "기본 글꼴로 먼저 보이는 FOUT", "<b>글은 바로 읽을 수 있지만</b>, 글꼴을 다 받으면 모양이 바뀝니다"),
    (fb("", "다 받은 뒤", note="원하던 글꼴"), "글꼴을 다 받았을 때", "FOIT와 FOUT 모두 글꼴을 다 받으면 이 상태가 됩니다"),
    (fb("font-family:Georgia,serif;font-size:11.4px", "size-adjust", note="크기를 맞춰 둔 대체 글꼴"),
     "대체 글꼴 크기를 맞춰 두었을 때", "대체 글꼴의 크기를 맞춰 두면 <b>글꼴이 바뀔 때 레이아웃이 덜 밀립니다</b>"),
    (fb("", "시스템 글꼴", "정산이 확정되었습니다", "150px", "받을 파일이 없음"),
     "시스템 글꼴을 쓸 때", "받을 파일이 없어서 <b>이런 문제가 아예 생기지 않습니다.</b> 가장 빠른 선택입니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px;font-family:var(--mono);font-size:10px;color:var(--fg-muted)">
                <div style="display:flex;justify-content:space-between"><span>영문 한 벌</span><span>약 20KB</span></div>
                <div style="display:flex;justify-content:space-between"><span>한글 한 벌</span><span style="color:var(--danger);font-weight:700">약 1~2MB</span></div>
                <div style="display:flex;justify-content:space-between"><span>한글 서브셋</span><span style="color:#1f8a4c;font-weight:700">조각당 10KB</span></div>
              </div>''',
     "한글 글꼴 파일의 크기", "한글 글꼴은 영문보다 <b>수십 배</b> 큽니다. 그래서 서브셋이 거의 필수입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("글꼴 선언", "@font-face", "글꼴 이름과 굵기, 파일 위치를 적습니다. <b>굵기마다 한 벌씩</b> 적습니다"),
    ("받는 동안의 표시 방식", "font-display: swap", "글을 <b>대체 글꼴로 먼저 보여 줍니다.</b> 요즘 가장 많이 쓰는 기본 선택입니다"),
    ("쪼개기", "unicode-range", "글자 범위별로 파일을 나눠서 <b>화면에 쓰인 조각만</b> 받게 합니다"),
    ("파일 형식", "woff2", "압축률이 가장 높은 형식이라 <b>이것만 적으면 됩니다</b>. 옛 형식은 이제 필요 없습니다"),
    ("먼저 받기", "preload", "중요한 한 벌에만 겁니다. 많이 걸면 <b>다른 자원을 받는 순서가 뒤로 밀립니다</b>"),
    ("밀림 줄이기", "size-adjust · ascent-override", "대체 글꼴의 크기를 웹폰트에 맞춰 두어 <b>글꼴이 바뀔 때 덜 흔들리게</b> 합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>한글 폰트 파일은 영문의 수십 배</b>입니다. 영문은 대소문자와 숫자, 기호를 합쳐 수백 자면 충분하지만,
          한글은 완성형만 1만 1172자입니다. 이 글자를 모두 받으면 한 벌에 1~2MB라서 첫 화면이 그만큼 늦게 뜹니다.
          그래서 글꼴을 <b>글자 범위별로 100여 조각</b>으로 나눠 두고, 화면에 실제로 쓰인 글자가 든 조각만
          받게 하는 방식(동적 서브셋)이 한국어 사이트에서 사실상 표준으로 자리 잡았습니다.</p>''',
  do=ul([
    "<b>브랜드 글꼴</b>이 정해져 있을 때",
    "시스템 글꼴로는 <b>필요한 굵기가 모자랄</b> 때",
    "여러 OS에서 글자가 <b>똑같이 보여야</b> 할 때",
  ]),
  dont=ul([
    "굵기를 <b>다섯 벌 이상</b> 받을 때. 한글 글꼴은 한 벌이 1MB 가까이 됩니다",
    "<code>font-display</code>를 정하지 않을 때. <b>브라우저가 대신 정하는데</b>, 보통 최대 3초 동안 글을 숨깁니다",
    "본문 글꼴을 바꾸려고 웹폰트를 쓸 때. 본문은 <b>시스템 글꼴로 충분한</b> 경우가 많습니다",
    "서브셋 없이 한글 글꼴 전체를 받을 때. 첫 화면이 그만큼 늦게 뜹니다",
  ]),
  instead_title="웹폰트와 이어지는 주제를 다루는 항목",
  instead='받아 올 굵기 수를 줄이는 방법은 <a href="weight.html">글자 굵기</a>에서, 글꼴이 바뀌어도 숫자 자리가 흔들리지 않게 하는 방법은 <a href="numerals.html">숫자 꼴</a>에서 다룹니다. 내용을 불러오는 동안 화면 자리를 잡아 두는 방법은 <a href="../items/skeleton.html">스켈레톤</a>을 보세요.',
  cases=cases([
    (fb("font-family:Georgia,serif", "swap", "정산이 확정되었습니다", "190px", "먼저 보이고 나중에 바뀜"),
     "기사와 블로그는 FOUT로", "글을 읽는 것이 목적이므로 바로 읽을 수 있는 <b>FOUT이 맞습니다</b>"),
    (fb("visibility:hidden", "block", "정산이 확정되었습니다", "190px", "로고·표지처럼 모양이 중요한 곳"),
     "모양이 중요한 표지와 로고", "모양이 중요한 곳에서는 잠깐 보이지 않는 편이 나을 때도 있습니다"),
    (fb("", "시스템 글꼴", "정산이 확정되었습니다", "190px", "받을 파일이 없어 바로 보임"),
     "내부 관리 도구는 시스템 글꼴로", "내부 도구는 웹폰트 없이 <b>시스템 글꼴</b>만 쓰는 경우가 흔합니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="글꼴 선언과 받아 오기 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="웹폰트 설정은 <code>@font-face</code> 한 덩어리와 <code>&lt;link&gt;</code> 한 줄로 이루어집니다.",
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
    ("<code>font-display: swap</code> 적기", "정하지 않으면 브라우저가 글을 <b>최대 3초 동안 숨깁니다</b>"),
    ("<code>woff2</code> 형식만 준비하기", "지금은 woff2만 적으면 됩니다. 옛 형식을 함께 적으면 준비할 파일만 늘어납니다"),
    ("서브셋으로 나눠 받기", "한글은 글꼴을 쪼개서 <b>화면에 쓰인 조각만</b> 받습니다. 직접 호스팅할 때도 마찬가지입니다"),
    ("받아 올 굵기 줄이기", "한 벌이 수백 KB에서 1MB나 되므로 <b>400·700</b> 두 굵기로 시작합니다"),
    ("<code>preload</code>는 한두 벌에만 걸기", "많이 걸면 <b>다른 자원을 받는 순서가 뒤로 밀립니다</b>"),
    ("<code>crossorigin</code> 빠뜨리지 않기", "폰트를 preload할 때는 꼭 필요합니다. 빠뜨리면 같은 파일을 <b>두 번 받습니다</b>"),
  ]),
  backend=rows([
    ("글꼴 파일을 받아 오는 곳", "외부 CDN은 편하지만 브라우저가 <b>그 도메인에 따로 연결</b>해야 합니다. 직접 호스팅하면 연결이 하나로 줄어서 보통 더 빠릅니다."),
    ("글꼴 파일의 캐시 기간", "글꼴 파일은 거의 바뀌지 않으므로 <b>아주 길게</b>(1년) 캐시합니다. 글꼴을 바꿀 때는 파일 이름에 해시를 넣어 새 파일을 받게 합니다."),
    ("웹 전용 라이선스", "웹폰트에는 <b>웹 전용 라이선스</b>가 따로 있습니다. 같은 글꼴을 앱이나 이미지에 쓰려면 라이선스 범위를 확인해야 합니다."),
    ("서버 렌더링에서 글꼴 선언 읽히기", "첫 HTML에서 <code>@font-face</code>를 늦게 읽으면 글꼴도 그만큼 늦게 받기 시작합니다. 그래서 <b>CSS를 HTML 안에 인라인</b>으로 넣기도 합니다."),
    ("글꼴 로딩을 재는 지표", "'글이 처음 보인 시각'은 <b>FCP</b>로, '레이아웃이 밀린 정도'는 <b>CLS</b>로 잽니다. 두 지표 모두 웹폰트 설정에 따라 크게 달라집니다."),
  ]),
  plat_lede="앱은 글꼴을 <b>앱 안에 넣어</b> 배포하기 때문에 글꼴 로딩 문제가 거의 없습니다.",
  plats=plats([
    ("웹", "@font-face",
     fb("", "woff2 + swap", "정산 확정", "120px"),
     "글꼴을 받아 오는 동안 글을 어떻게 보여 줄지 <b>직접 정해야</b> 합니다. 특히 한글은 파일 크기를 줄이는 일이 큰 과제입니다."),
    ("iOS", "앱 번들",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Info.plist<br>UIAppFonts<br>.custom("…", size:)</div>''',
     "글꼴을 <b>앱에 넣어</b> 배포합니다. 글꼴을 받는 시간이 없으므로 FOIT나 FOUT도 생기지 않습니다."),
    ("안드로이드", "앱 번들 · Downloadable Fonts",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">res/font/<br>Downloadable Fonts</div>''',
     "안드로이드도 글꼴을 <b>앱에 넣습니다</b>. 글꼴을 내려받아 쓰는 방식도 있지만 첫 화면에는 잘 쓰지 않습니다."),
  ]),
  plat_note="앱은 글꼴이 앱 안에 들어 있어서 <b>글꼴 로딩 문제가 아예 없습니다</b>. 그래서 \"글꼴 바꿔 주세요\"라는 요청이 앱에서는 앱 용량이 몇 MB 늘어나는 일이지만, 웹에서는 <b>첫 화면 속도와 레이아웃 밀림</b>을 따져야 하는 일이 됩니다. 같은 요청이라도 플랫폼마다 걱정하는 지점이 다릅니다.",
  siblings=siblings("webfont"),
  related='''        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><a href="../items/numerals.html"><b>숫자 꼴</b><em>3부</em></a></li>''',
)
