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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">키보드가 화면의 절반을 덮음 (자동완성 줄 포함)</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">position: fixed로 붙인 것은 키보드 뒤에 가려짐</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">visualViewport.height는 지금 보이는 높이</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">바닥 버튼을 그만큼 올림</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">inputmode·enterkeyhint로 키보드 모양을 정함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">포커스가 간 칸은 scrollIntoView로 끌어 올림</div>
                </div>
              </div>'''

D = dict(
  slug="softkeyboard", ko="폰 키보드", en="Software keyboard",
  desc="화면 절반을 덮는 폰 키보드 때문에 가려지는 입력칸과 버튼을 visualViewport로 다루는 법과, 키보드 모양을 정하는 법을 보여 주는 항목입니다.",
  lede="폰 키보드는 올라오면 <b>화면의 절반쯤</b>을 덮기 때문에, 그 자리에 있던 입력칸과 버튼은 모두 키보드에 가려집니다.",
  axes_lede="PC와 폰은 기계보다 <b>쓰는 전제</b>가 다릅니다. 아래 네 가지로 두 환경을 견줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>입력칸 누르기</b>로 키보드를 올려 보세요. 한글 키보드는 자동완성 줄까지 더해
          화면의 절반을 덮습니다.<br>
          기본 상태에서는 <b>저장 버튼이 키보드 뒤에</b> 가려져서, 글자를 다 쳐도 저장할 방법이 없습니다.
          <b>visualViewport로 버튼을 키보드 위로 올리기</b>를 켜면 바닥에 붙어 있던 버튼이 키보드 위로 올라옵니다.</p>
        </div>''',
  names=rows([
    ("한국어", "폰 키보드, 소프트 키보드, 가상 키보드, 화상 키보드"),
    ("영어", "software keyboard, on-screen keyboard, virtual keyboard, IME"),
    ("같이 쓰는 말",
     "브라우저 창 안에서 <b>실제로 보이는 영역</b>을 <b>비주얼 뷰포트</b>(visual viewport)라고 하며 "
     "<code>window.visualViewport</code>로 크기를 읽습니다. "
     "한글이나 일본어처럼 글자를 조합해 넣는 장치는 <b>IME</b>(입력기)라고 하고, "
     "조합이 시작되고 끝날 때 <code>compositionstart</code>와 <code>compositionend</code> 이벤트가 옵니다. "
     "엔터 키에 적히는 말은 <code>enterkeyhint</code> 속성으로 정합니다."),
    ("자주 잘못 부르는 이름",
     "<b>뷰포트</b> — <a href=\"viewport.html\">뷰포트 단위</a>의 <code>dvh</code>에는 <b>키보드가 덮은 높이가 반영되지 않으므로</b>, 키보드는 뷰포트 단위와 따로 다뤄야 하는 문제입니다.<br>"
     "<b>리사이즈</b> — 키보드가 올라와도 <code>window.resize</code> 이벤트가 <b>오지 않는 기기</b>가 있습니다.<br>"
     "<b>키보드 조작</b> — <a href=\"../items/keyboard.html\">키보드 조작</a>은 PC에서 Tab과 Enter로 화면을 다루는 이야기라서 이 항목과는 다른 주제입니다."),
  ]),
  axes=ax("폰 키보드"),
  oneline="<b>키보드가 올라와도 창 크기는 바뀌지 않습니다.</b> 그래서 <code>position: fixed</code>로 바닥에 붙인 것은 제자리에 남은 채 키보드 뒤에 가려집니다.",
  s4_title="키보드가 올라올 때 생기는 일", s4_hint="키보드에 가려지는 것",
  do_title="폰 키보드를 챙겨야 하는 화면",
  dont_title="폰 키보드를 다룰 때 피할 것",
  instead_title="관련 주제는 다른 항목에서 다룹니다",
  states=states([
    (ph(0, 4, "내려가 있으면 다섯 칸과 버튼이 다 보임", False, "112px", 5), "키보드가 내려가 있을 때", "흔히 보는 폼입니다. <b>PC에서 보는 모습</b>과 같습니다"),
    (ph(56, 4, "올라오면 버튼이 키보드 뒤에 가려짐", True, "112px", 5), "키보드가 올라왔을 때", "<b>저장 버튼이 키보드에 가려집니다</b>"),
    (ph(56, 60, "visualViewport로 버튼을 올림", False, "112px", 5), "버튼을 키보드 위로 올렸을 때", "버튼이 <b>키보드 바로 위</b>에 붙습니다"),
    (ph(56, 60, "아래 칸들은 가려져 굴려야 보임", True, "112px", 5), "버튼을 올려도 가려지는 입력칸", "버튼은 보여도 아래쪽 <b>입력칸은 여전히 가려집니다</b>"),
    (ph(56, 60, "포커스가 간 칸을 끌어 올림", False, "112px", 3), "포커스가 간 칸 끌어 올리기", "<code>scrollIntoView</code>로 <b>글자를 치는 칸이 보이게</b> 끌어 올립니다"),
    ('''              <div style="width:100%;max-width:112px;display:grid;gap:5px;justify-items:center">
                <div style="width:74px;height:124px;border:2px solid var(--line-strong);border-radius:10px;background:var(--surface);position:relative;overflow:hidden">
                  <div style="position:absolute;left:3px;right:3px;top:6px;height:11px;border:1px solid var(--accent);border-radius:3px;background:var(--surface)"></div>
                  <div style="position:absolute;left:0;right:0;bottom:0;height:68px;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                  <div style="position:absolute;left:0;right:0;bottom:56px;height:12px;background:var(--bg);border-top:1px solid var(--line);font-size:6px;color:var(--fg-muted);display:grid;place-items:center">모란 · 모란상회 · 모래</div>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted);text-align:center">한글은 자동완성 줄이 더 붙음</span>
              </div>''',
     "한글 키보드를 쓸 때", "자동완성 줄까지 더해지면 <b>화면의 절반을 넘기도</b> 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("덮는 높이", "화면의 45~55%", "한글 키보드는 위에 <b>자동완성 줄</b>이 붙어서 더 높습니다"),
    ("fixed로 붙인 요소", "position: fixed", "키보드가 올라와도 창 크기가 바뀌지 않으므로 <b>제자리에 남아 키보드 뒤에 가려집니다</b>"),
    ("지금 보이는 높이", "visualViewport.height", "키보드에 덮이지 않고 보이는 높이를 알려 주는, 유일하게 믿을 만한 값입니다"),
    ("올려 주기", "bottom: 덮인 높이", "바닥에 붙은 것을 키보드가 덮은 높이만큼 올립니다"),
    ("키보드 모양", "inputmode · enterkeyhint", "숫자를 넣는 칸에 글자 키보드가 뜨면 사용자가 키보드를 직접 바꿔야 해서 번거롭습니다"),
    ("포커스 따라가기", "scrollIntoView", "키보드를 올려도 글자를 치고 있는 칸이 <b>보이지 않으면</b> 무엇을 쳤는지 확인할 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          키보드가 올라올 때 화면이 어떻게 바뀌는지는 <b>기기마다 다릅니다.</b>
          안드로이드 크롬은 기본적으로 창을 줄이고 <code>resize</code> 이벤트를 보내지만,
          iOS 사파리는 창 크기를 그대로 두고 <b>보이는 영역만</b> 밀어 올립니다.
          그래서 <code>window.innerHeight</code>로 재면 iOS에서는 값이 바뀌지 않습니다.
          두 브라우저에서 같은 답을 주는 것은 <code>visualViewport</code>뿐이고,
          이 차이 때문에 \"내 폰에서는 되는데\"라는 말이 가장 자주 나옵니다.</p>''',
  do=ul([
    "바닥에 <b>버튼이 붙는</b> 폼을 만들 때. 키보드에 버튼이 가려지는 일이 가장 자주 생깁니다",
    "채팅처럼 <b>입력칸이 아래</b>에 있는 화면을 만들 때",
    "긴 폼을 만들 때. <b>포커스가 간 칸</b>을 보이는 자리로 끌어 올립니다",
  ]),
  dont=ul([
    "<code>100dvh</code>만 쓰면 해결된다고 여길 때. <b>키보드가 덮은 높이는 dvh에 반영되지 않습니다</b>",
    "<code>window.resize</code> 이벤트만 기다릴 때. iOS에서는 이 이벤트가 <b>오지 않습니다</b>",
    "숫자를 넣는 칸에 글자 키보드를 띄울 때. <code>inputmode</code> 한 줄이면 숫자 키보드가 뜹니다",
    "키보드를 <b>강제로 내릴</b> 때. 글자를 치려던 사용자가 다시 칸을 눌러야 합니다",
  ]),
  instead='화면 높이를 다루는 법은 <a href="viewport.html">뷰포트 단위</a>에서, 입력칸을 묶는 법은 <a href="form.html">폼 설계</a>에서 설명합니다. 바닥에 고정하는 법은 <a href="../items/sticky.html">스티키</a> 항목을 봅니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>&lt;input <span style="color:var(--accent)">inputmode="numeric"</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">enterkeyhint="next"</span>&gt;</span>
              </div>''',
     "키보드 모양 정하기", "속성 <b>한 줄로</b> 숫자판이 뜨고, 엔터 키에는 '다음'이 적힙니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>visualViewport</span>
                <span>&nbsp;&nbsp;.addEventListener('resize', fit)</span>
                <span style="color:var(--accent)">bar.style.bottom = covered + 'px'</span>
              </div>''',
     "바닥 막대를 키보드 위로 올리기", "<b>두 OS에서 같은 높이 값</b>을 주는 유일한 방법입니다"),
    (ph(56, 60, "채팅은 입력칸이 아래에 붙음", False, "152px", 3), "채팅 화면의 입력칸 붙이기", "입력칸이 <b>키보드 바로 위</b>에 붙어 있어야 합니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="<code>visualViewport</code>로 키보드가 덮은 높이를 재고, 바닥에 붙은 것을 그만큼 올립니다.",
  code='''&lt;<span class="t">input</span> <span class="a">inputmode</span>=<span class="s">"numeric"</span> <span class="a">enterkeyhint</span>=<span class="s">"next"</span>
       <span class="a">autocomplete</span>=<span class="s">"tel"</span> <span class="a">name</span>=<span class="s">"phone"</span>&gt;

<span class="c">// 키보드가 덮은 높이를 잰다. 두 OS에서 같은 값이 나온다</span>
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
    ("<code>inputmode</code>로 키보드 모양 바꾸기", "<code>numeric</code>·<code>tel</code>·<code>email</code>·<code>decimal</code> 같은 값을 주며, <b>키보드 모양</b>만 바꿉니다"),
    ("<code>type</code>과 구분하기", "<code>type=\"number\"</code>는 값까지 숫자로 다루기 때문에 <b>맨 앞의 0이 사라집니다</b>. 전화번호나 계좌번호에는 <code>inputmode</code>만 씁니다"),
    ("<code>enterkeyhint</code>로 엔터 키 글자 바꾸기", "<code>next</code>·<code>done</code>·<code>send</code> 같은 값을 주면 엔터 키에 적히는 말이 바뀝니다"),
    ("<code>autocomplete</code> 달기", "이름, 전화번호, 주소를 자동으로 채워 줍니다. 폰에서는 글자를 치기가 번거로워서 <b>효과가 특히 큰 한 줄</b>입니다"),
    ("한글을 조합하는 동안", "<code>compositionstart</code>부터 <code>compositionend</code>까지는 <code>input</code> 이벤트마다 검사하지 않습니다. 검사하면 <b>조합 중인 글자를 틀렸다고</b> 표시하게 됩니다"),
    ("<code>env(safe-area-inset-bottom)</code> 더하기", "키보드 높이에 <b>함께</b> 더합니다. 자세한 내용은 <a href=\"../items/safearea.html\">세이프 에어리어</a>를 봅니다"),
  ]),
  backend=rows([
    ("서버 확인 요청을 보내는 시점", "한글을 조합하는 도중에 서버로 확인 요청을 보내면 <b>조합이 덜 된 글자</b>가 전송됩니다. 요청은 <code>compositionend</code> 뒤에 보냅니다."),
    ("자동완성으로 채운 값 읽기", "브라우저가 자동으로 채운 값은 <code>input</code> 이벤트 없이 들어오기도 하므로, 값은 <b>제출할 때</b> 다시 읽습니다."),
    ("폰에서 짧아지는 입력", "폰 키보드는 치기가 불편해서 사용자가 <b>글을 짧게 적습니다.</b> 폰에서는 긴 메모 칸이 거의 빈 채로 들어오므로, 이런 칸은 필수로 두지 않습니다."),
  ]),
  plat_lede="키보드가 화면을 <b>덮는 방식</b>이 OS마다 달라서, 같은 코드라도 OS에 따라 다르게 움직입니다.",
  plats=plats([
    ("웹", "visualViewport",
     ph(56, 60, "", False, "105px", 3),
     "키보드가 올라올 때 창 크기가 바뀌는지는 브라우저마다 다르고, <b>visualViewport</b>만 양쪽에서 같은 값을 줍니다."),
    ("iOS", "창을 줄이지 않음",
     '''              <div class="phone" role="img" aria-label="iOS 키보드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div>
                <div style="position:absolute;left:4px;right:4px;bottom:46%;height:8px;background:var(--bg);border-top:1px solid var(--line)"></div></div></div>''',
     "창 크기는 그대로 두고 <b>보이는 영역만 밀어 올리기</b> 때문에, <code>innerHeight</code> 값은 바뀌지 않습니다."),
    ("안드로이드", "창을 줄임",
     '''              <div class="phone" role="img" aria-label="안드로이드 키보드 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:50%;background:var(--ink-100);border-top:1px solid var(--line-strong)"></div></div></div>''',
     "기본적으로 <b>창을 줄이고</b> <code>resize</code> 이벤트를 보냅니다. 앱에서는 <code>windowSoftInputMode</code> 설정으로 동작을 고릅니다."),
  ]),
  plat_note="\"폰에서 저장 버튼이 안 보여요\"라는 문제는 PC에서 재현되지 않고, 개발자 도구의 기기 흉내 모드에서도 <b>키보드가 뜨지 않습니다</b>. 입력칸이 있는 화면은 <b>실제 폰에서 한 번</b> 열어 보는 것 말고는 확인할 방법이 없지만, 그 한 번만으로도 문제를 대부분 찾을 수 있습니다.",
  siblings=siblings("softkeyboard"),
  related='''        <li><a href="viewport.html"><b>뷰포트 단위</b><em>11부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
