# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ph(kbd_h, cta_bottom, note, warn=False, w="112px", fields=4):
    H = 124
    fs = ''.join('<div style="position:absolute;left:3px;right:3px;top:' + str(6 + i * 14) + 'px;height:11px;'
                 'border:1px solid var(--line);border-radius:3px;background:var(--surface)"></div>' for i in range(fields))
    cta = ('<div style="position:absolute;left:3px;right:3px;bottom:' + str(cta_bottom) + 'px;height:11px;'
           'border-radius:3px;background:var(--accent)"></div>')
    kb = ('<div style="position:absolute;left:0;right:0;bottom:0;height:' + str(kbd_h) + 'px;background:var(--ink-100);'
          'border-top:1px solid var(--line-strong)"></div>') if kbd_h else ''
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:center">'
            '<div style="width:74px;height:' + str(H) + 'px;border:2px solid var(--line-strong);border-radius:10px;'
            'background:var(--surface);position:relative;overflow:hidden">' + fs + cta + kb + '</div>'
            '<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + ';text-align:center">' + note + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">키보드가 화면의 절반을 덮는다 (자동완성 줄 포함)</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">position: fixed 는 키보드를 모른다 — 뒤에 깔린다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">visualViewport.height — 지금 보이는 높이</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">바닥 버튼을 그만큼 올린다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">inputmode · enterkeyhint — 키보드 모양을 정한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">초점이 간 칸은 scrollIntoView 로 끌어 올린다</div>
                </div>
              </div>'''

D = dict(
  slug="softkeyboard", ko="폰 키보드", en="Software keyboard",
  desc="화면 절반을 덮는 키보드. 가려지는 입력칸과 버튼, visualViewport, 키보드 모양 정하기.",
  lede="폰 키보드는 <b>화면의 절반</b>을 덮습니다. 그 아래 있던 것은 전부 사라집니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>입력칸 누르기</b>로 키보드를 올려 보세요. 한글 키보드는 자동완성 줄까지 더해
          화면의 절반을 덮습니다.<br>
          기본 상태에서는 <b>저장 버튼이 키보드 뒤에</b> 숨습니다 — 글자는 쳤는데 보낼 수가 없습니다.
          <b>visualViewport 로 따라 올리기</b>를 켜면 바닥에 붙은 것이 키보드 위로 올라옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "폰 키보드, 소프트 키보드, 가상 키보드, 화상 키보드"),
    ("영어", "software keyboard, on-screen keyboard, virtual keyboard, IME"),
    ("같이 쓰는 말",
     "브라우저 창 안에서 <b>실제로 보이는 영역</b>이 <b>비주얼 뷰포트</b>(visual viewport)이고 "
     "<code>window.visualViewport</code>로 읽습니다. "
     "한글·일본어처럼 글자를 조합해 넣는 장치가 <b>IME</b>(입력기)이고, "
     "조합 중에 오는 이벤트가 <code>compositionstart</code>·<code>compositionend</code>입니다. "
     "엔터 키에 적히는 말을 정하는 것이 <code>enterkeyhint</code>입니다."),
    ("자주 잘못 부름",
     "<b>뷰포트</b> — <a href=\"viewport.html\">뷰포트 단위</a>의 <code>dvh</code>로는 <b>키보드가 안 잡힙니다</b>. 다른 문제입니다.<br>"
     "<b>리사이즈</b> — 키보드가 올라와도 <code>window.resize</code>가 <b>안 오는 기기</b>가 있습니다.<br>"
     "<b>키보드 조작</b> — <a href=\"../items/keyboard.html\">키보드 조작</a>은 PC 의 Tab·Enter 이야기라 완전히 다릅니다."),
  ]),
  axes=ax("폰 키보드"),
  oneline="<b>키보드는 창 크기를 바꾸지 않습니다.</b> 그래서 <code>position: fixed</code>로 바닥에 붙인 것은 그대로 키보드 뒤에 깔립니다.",
  s4_title="키보드가 올라오면", s4_hint="무엇이 가려지나",
  states=states([
    (ph(0, 4, "내려감 — 다섯 칸과 버튼이 다 보인다", False, "112px", 5), "내려갔을 때", "흔한 폼. <b>PC 에서 보는 모습</b>"),
    (ph(56, 4, "올라감 — 버튼이 키보드 뒤에", True, "112px", 5), "올라갔을 때", "<b>저장 버튼이 사라진다</b>"),
    (ph(56, 60, "visualViewport 로 올렸다", False, "112px", 5), "따라 올리면", "버튼이 <b>키보드 위</b>에 붙는다"),
    (ph(56, 60, "아래 칸들도 가려진다 — 굴려야 보인다", True, "112px", 5), "그래도 남는 문제", "버튼은 보여도 <b>입력칸이 가려진다</b>"),
    (ph(56, 60, "초점 간 칸을 끌어 올린다", False, "112px", 3), "초점 따라가기", "<code>scrollIntoView</code>로 <b>치는 칸이 보이게</b>"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:74px;height:124px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:3px;right:3px;top:6px;height:11px;border:1px solid var(--accent);border-radius:3px;background:var(--surface)"></div>
                  <div style="position:absolute;left:0;right:0;bottom:0;height:68px;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                  <div style="position:absolute;left:0;right:0;bottom:56px;height:12px;background:var(--bg);border-top:1px solid var(--line);font-size:6px;color:var(--fg-muted);display:grid;place-items:center">모란 · 모란상회 · 모래</div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted);text-align:center">한글은 자동완성 줄이 더 붙는다</span>
              </div>''',
     "한글은 더 높다", "자동완성 줄까지 더해 <b>화면의 절반을 넘기도</b> 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("덮는 높이", "화면의 45~55%", "한글은 <b>자동완성 줄</b>까지 붙어 더 높다"),
    ("fixed 는 모른다", "position: fixed", "창 크기가 안 바뀌어서 <b>그대로 깔린다</b>"),
    ("지금 보이는 높이", "visualViewport.height", "유일하게 믿을 만한 값"),
    ("올려 주기", "bottom: 덮인 높이", "바닥에 붙은 것을 그만큼 올린다"),
    ("키보드 모양", "inputmode · enterkeyhint", "숫자 칸에 글자 키보드가 뜨면 짜증 난다"),
    ("초점 따라가기", "scrollIntoView", "치고 있는 칸이 <b>안 보이면</b> 아무 소용 없다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>기기마다 다르게 움직입니다.</b>
          안드로이드 크롬은 기본적으로 창을 줄여 <code>resize</code>를 보내지만,
          iOS 사파리는 창 크기를 그대로 두고 <b>안쪽만</b> 밀어 올립니다.
          그래서 <code>window.innerHeight</code>로 재면 iOS 에서 아무 변화가 없습니다.
          <code>visualViewport</code>만이 두 곳에서 같은 답을 주고,
          이 한 가지가 \"내 폰에서는 되는데\"라는 말이 나오는 가장 흔한 이유입니다.</p>''',
  do=ul([
    "바닥에 <b>버튼이 붙는</b> 폼 — 가장 자주 당한다",
    "채팅처럼 <b>입력칸이 아래</b>에 있는 화면",
    "긴 폼 — <b>초점 간 칸</b>을 보이게 끌어 올린다",
  ]),
  dont=ul([
    "<code>100dvh</code>면 해결된다고 믿기 — <b>키보드는 다른 문제</b>다",
    "<code>window.resize</code>만 듣기 — iOS 에서 <b>안 온다</b>",
    "숫자 칸에 글자 키보드 — <code>inputmode</code> 한 줄이면 된다",
    "키보드를 <b>강제로 내리기</b> — 치려는 사람을 막는다",
  ]),
  instead='화면 높이 자체는 <a href="viewport.html">뷰포트 단위</a>, 칸 묶음은 <a href="form.html">폼 설계</a>, 바닥 고정은 <a href="../items/sticky.html">스티키</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>&lt;input <span style="color:var(--accent)">inputmode="numeric"</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">enterkeyhint="next"</span>&gt;</span>
              </div>''',
     "키보드 모양 정하기", "<b>한 줄로</b> 숫자판이 뜨고 엔터가 '다음'이 된다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>visualViewport</span>
                <span>&nbsp;&nbsp;.addEventListener('resize', fit)</span>
                <span style="color:var(--accent)">bar.style.bottom = covered + 'px'</span>
              </div>''',
     "바닥 막대 올리기", "<b>두 OS 에서 같은 답</b>을 주는 유일한 길"),
    (ph(56, 60, "채팅은 입력칸이 아래에 붙는다", False, "152px", 3), "채팅 화면", "입력칸이 <b>키보드 바로 위</b>에 붙어야 한다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 키보드의 계약서",
  code_lede="<code>visualViewport</code>로 재서 바닥에 붙은 것을 올립니다.",
  code='''&lt;<span class="t">input</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">enterkeyhint</span>=<span class="s">"next"</span>
       <span class="a">autocomplete</span>=<span class="s">"tel"</span> <span class="a">name</span>=<span class="s">"phone"</span>&gt;

<span class="c">// 키보드가 덮은 높이를 잰다 — 두 OS 에서 같은 답</span>
<span class="k">const</span> vv = window.visualViewport;
<span class="k">function</span> fit() {
  <span class="k">const</span> covered = window.innerHeight - vv.height - vv.offsetTop;
  document.documentElement.style.setProperty(<span class="s">'--kbd'</span>, Math.max(covered, <span class="a">0</span>) + <span class="s">'px'</span>);
}
vv.addEventListener(<span class="s">'resize'</span>, fit);
vv.addEventListener(<span class="s">'scroll'</span>, fit);
fit();

<span class="c">/* 바닥 막대를 그만큼 올린다 */</span>
.cta-bar { <span class="a">position</span>: fixed; <span class="a">bottom</span>: <span class="a">calc</span>(<span class="a">var</span>(--kbd, <span class="a">0px</span>) + <span class="a">env</span>(safe-area-inset-bottom)); }''',
  keys=kbd([
    ("<code>inputmode</code>", "<code>numeric</code>·<code>tel</code>·<code>email</code>·<code>decimal</code>. <b>키보드 모양</b>만 바꾼다"),
    ("<code>type</code>과 다르다", "<code>type=\"number\"</code>는 값까지 숫자로 다뤄 <b>앞의 0 이 사라진다</b>. 전화번호·계좌는 <code>inputmode</code>만"),
    ("<code>enterkeyhint</code>", "<code>next</code>·<code>done</code>·<code>send</code>. 엔터 키에 적히는 말이 바뀐다"),
    ("<code>autocomplete</code>", "이름·전화·주소. <b>폰에서 효과가 가장 큰 한 줄</b>이다"),
    ("한글 조합 중", "<code>compositionstart</code>~<code>compositionend</code> 사이에는 <code>input</code>마다 검사하지 않는다 — <b>조합 중인 글자가 틀렸다고</b> 뜬다"),
    ("<code>env(safe-area-inset-bottom)</code>", "키보드 높이와 <b>함께</b> 더한다. <a href=\"../items/safearea.html\">세이프 에어리어</a>"),
  ]),
  backend=rows([
    ("검증 시점", "한글 조합 중에 서버로 확인 요청을 보내면 <b>미완성 글자</b>가 갑니다. <code>compositionend</code> 뒤에 보냅니다."),
    ("자동완성 값", "브라우저가 채운 값은 <code>input</code> 이벤트 없이 들어오기도 합니다. <b>제출 시점에</b> 다시 읽습니다."),
    ("폰 입력은 짧다", "키보드가 불편해 사람들이 <b>덜 적습니다.</b> 긴 메모 칸은 폰에서 거의 비어 옵니다 — 필수로 두지 않습니다."),
  ]),
  plat_lede="<b>덮는 방식</b>이 OS 마다 달라 같은 코드가 다르게 움직입니다.",
  plats=plats([
    ("웹", "visualViewport",
     ph(56, 60, "", False, "105px", 3),
     "창 크기가 바뀌는지 아닌지가 브라우저마다 다릅니다. <b>visualViewport</b>만 양쪽에서 같습니다."),
    ("iOS", "창을 안 줄인다",
     '''              <div class="phone" role="img" aria-label="iOS 키보드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:46%;height:8px;background:var(--bg);border-top:1px solid var(--line)"></div></div></div>''',
     "창 크기는 그대로 두고 <b>안쪽만 밀어 올립니다.</b> <code>innerHeight</code>로는 아무 변화가 없습니다."),
    ("안드로이드", "창을 줄인다",
     '''              <div class="phone" role="img" aria-label="안드로이드 키보드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:50%;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div></div></div>''',
     "기본적으로 <b>창을 줄여</b> <code>resize</code>를 보냅니다. 앱에서는 <code>windowSoftInputMode</code>로 고릅니다."),
  ]),
  plat_note="\"폰에서 저장 버튼이 안 보여요\"는 PC 에서 재현이 안 됩니다. 개발자 도구의 기기 흉내 모드에도 <b>키보드는 안 뜹니다</b>. 입력칸이 있는 화면은 <b>실제 폰에서 한 번</b> 열어 보는 것 말고는 확인할 길이 없고, 그 한 번에 대부분이 걸립니다.",
  siblings=siblings("softkeyboard"),
  related='''        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
