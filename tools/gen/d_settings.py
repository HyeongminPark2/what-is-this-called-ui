# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def sw(on=True):
    return ('<span style="width:20px;height:12px;border-radius:999px;position:relative;flex:none;'
            + ('background:var(--accent)' if on else 'background:var(--line-strong)') + '">'
            '<span style="position:absolute;top:1px;' + ('right:1px' if on else 'left:1px') +
            ';width:10px;height:10px;border-radius:50%;background:#fff"></span></span>')

def cb(on=False):
    return ('<span style="width:11px;height:11px;border-radius:2px;flex:none;'
            + ('background:var(--accent);border:1px solid var(--accent);color:#fff;font-size:8px;line-height:10px;text-align:center' if on
               else 'border:1px solid var(--line)') + '">' + ('✓' if on else '') + '</span>')

def row(lab, ctl, sub="", dirty=False):
    return ('<div style="display:flex;align-items:center;gap:6px;padding:5px 0;border-top:1px solid var(--line)">'
            '<span style="flex:1;min-width:0;font-size:9.5px' + (';font-weight:700' if dirty else '') + '">' + lab
            + ('<span style="display:block;font-size:8px;color:var(--fg-muted);font-weight:400">' + sub + '</span>' if sub else '')
            + ('<span style="color:var(--warn);font-size:8px;font-weight:700"> · 바뀜</span>' if dirty else '')
            + '</span>' + ctl + '</div>')

def box(inner, w="152px", head="설정", foot=""):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:6px;'
            'background:var(--surface);overflow:hidden">'
            '<div style="padding:5px 8px;border-bottom:1px solid var(--line);background:var(--bg);font-size:9px;font-weight:700">' + head + '</div>'
            '<div style="padding:3px 8px 7px">' + inner + '</div>'
            + ('<div style="padding:5px 8px;border-top:1px solid var(--line);font-size:8.5px;color:var(--fg-muted)">' + foot + '</div>' if foot else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">스위치 = 바로 적용 · 체크박스 = 저장 버튼</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + box(row('새 정산 알림', sw(True), '정산이 들어오면'), "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">묶음 이름 — 알림 · 화면 · 계정</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">줄마다 한 줄 설명 — 켜면 무슨 일이 나는가</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">스무 줄이 넘으면 검색이 묶음보다 빠르다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">위험 구역은 맨 아래 따로 — 빨간 테두리로 가둔다</div>
                </div>
              </div>'''

D = dict(
  slug="settings", ko="설정 화면", en="Settings",
  desc="값을 바꾸는 화면. 바로 적용과 저장 버튼의 약속, 묶음과 검색, 위험 구역 가두기.",
  lede="값을 바꾸는 화면. <b>바로 적용할지 저장을 누르게 할지</b>를 먼저 정해야 나머지가 따라옵니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>스위치는 바로 적용, 체크박스는 저장</b> — 이 약속이 셋 모두 같습니다. 위 체크로 두 방식을 바꿔 보세요.<br>
          저장 버튼 방식에서는 바꾼 줄에 '바뀜'이 붙고 누르기 전엔 적용되지 않습니다.
          바로 적용 방식에는 <b>저장 버튼이 아예 없어야</b> 합니다 — 있는데 안 눌러도 적용되면
          무엇이 저장됐는지 알 수 없습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "설정, 환경설정, 기본 설정, 계정 설정"),
    ("영어", "settings, preferences, options, account settings"),
    ("같이 쓰는 말",
     "맥·iOS 는 <b>Preferences</b>·<b>Settings</b>, 윈도는 <b>Options</b>를 많이 씁니다. "
     "되돌릴 수 없는 것들을 따로 모은 자리가 <b>위험 구역</b>(danger zone)이고, "
     "바꾼 뒤 저장하지 않은 상태를 <b>더티</b>(dirty)라 합니다."),
    ("자주 잘못 부름",
     "<b>프로필</b> — 남에게 보이는 정보이고, 설정은 <b>내 쪽 동작</b>을 바꿉니다. 섞어 두면 어느 쪽인지 헷갈립니다.<br>"
     "<b>관리자 설정</b> — 조직 전체 설정과 개인 설정은 <b>다른 화면</b>입니다. 같은 자리에 두면 권한 사고가 납니다.<br>"
     "<b>폼</b> — <a href=\"form.html\">폼</a>은 한 번 보내고 끝나지만, 설정은 <b>계속 고치러</b> 돌아옵니다."),
  ]),
  axes=ax("설정 화면"),
  oneline="<b>저장 버튼이 있으면 체크박스, 없으면 스위치.</b> 이 둘이 어긋나면 사용자는 저장됐는지를 영영 확신하지 못합니다.",
  s4_title="상태", s4_hint="저장됐는지 알 수 있나",
  states=states([
    (box(row('새 정산 알림', sw(True), '정산이 들어오면 알려 줍니다') + row('주간 요약 메일', sw(False), '월요일 아침에 한 번')),
     "바로 적용", "스위치. <b>저장 버튼이 없다</b>"),
    (box(row('새 정산 알림', cb(True)) + row('주간 요약 메일', cb(False)), "152px", "설정", "저장 · 되돌리기"),
     "저장 버튼 방식", "체크박스. <b>누르기 전엔</b> 안 바뀐다"),
    (box(row('새 정산 알림', cb(False), '', True) + row('주간 요약 메일', cb(False)), "152px", "설정", "2개 바뀜 — 저장하지 않았습니다"),
     "바꿨지만 저장 전", "<b>바뀐 줄</b>을 표시한다"),
    (box(row('새 정산 알림', sw(True)) + row('주간 요약 메일', sw(False)), "152px", "설정 · 검색: 알림"),
     "검색으로 찾기", "스무 줄이 넘으면 <b>묶음보다 빠르다</b>"),
    (box('<div style="font-size:8px;color:var(--fg-muted);padding:4px 0">알림</div>' + row('새 정산 알림', sw(True))
         + '<div style="font-size:8px;color:var(--fg-muted);padding:4px 0;margin-top:4px">계정</div>' + row('2단계 인증', sw(True))),
     "묶어 두기", "<b>성격이 같은 것</b>끼리. 이름을 붙인다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--danger);border-radius:6px;padding:7px;display:grid;gap:4px">
                <span style="font-size:9px;font-weight:700;color:var(--danger)">위험 구역</span>
                <span style="font-size:8px;color:var(--fg-muted)">계정을 지우면 되돌릴 수 없습니다</span>
                <span style="justify-self:start;border:1px solid var(--danger);color:var(--danger);border-radius:4px;padding:2px 7px;font-size:8.5px">계정 삭제</span>
              </div>''',
     "위험 구역", "<b>맨 아래 따로.</b> 실수로 닿지 않게 가둔다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("약속", "스위치 ↔ 체크박스", "<b>바로 적용이냐 저장이냐.</b> 이걸 먼저 정한다"),
    ("줄", "이름 + 한 줄 설명", "켜면 <b>무슨 일이 나는지</b> 적는다"),
    ("묶음", "알림 · 화면 · 계정", "성격이 같은 것끼리. <b>이름을 붙인다</b>"),
    ("설명", "작게, 늘 보이게", "툴팁에 숨기면 <a href=\"hover.html\">폰에서 못 본다</a>"),
    ("검색", "스무 줄 넘으면", "묶음을 아무리 잘 짜도 <b>찾는 게 더 빠르다</b>"),
    ("위험 구역", "맨 아래, 따로", "되돌릴 수 없는 것만. <a href=\"destructive.html\">위험한 동작</a>으로 이어진다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>둘을 섞는 것</b>이 가장 흔한 사고입니다 —
          스위치를 늘어놓고 아래에 저장 버튼을 두는 화면이 그렇습니다.
          사용자는 스위치를 넘기고 <b>이미 저장됐다고 믿은 채</b> 나가고,
          실제로는 아무것도 안 바뀝니다.
          반대로 바로 적용인데 저장 버튼이 있으면,
          눌러도 아무 일이 안 일어나 <b>버튼이 고장 난 것</b>처럼 보입니다.
          둘 중 하나를 정하고 <b>화면 전체가 그 하나를 따르게</b> 하는 것이 전부입니다.</p>''',
  do=ul([
    "값을 <b>계속 고치러</b> 돌아오는 화면",
    "켜고 끄는 것이 많을 때 — <b>묶고 설명을 단다</b>",
    "되돌릴 수 없는 것은 <b>위험 구역</b>으로 가둔다",
  ]),
  dont=ul([
    "스위치 + 저장 버튼 — <b>가장 흔한 사고</b>",
    "설명 없는 이름만 — '고급 모드'가 뭔지 아무도 모른다",
    "기본값 없이 비워 두기 — <b>무엇이 보통인지</b> 알려 준다",
    "계정 삭제를 다른 것들 사이에 끼워 두기",
  ]),
  instead='한 번 보내고 끝이면 <a href="form.html">폼 설계</a>, 켜고 끄는 부품 자체는 <a href="../items/switch.html">스위치</a>·<a href="../items/checkbox.html">체크박스</a>, 지우는 흐름은 <a href="destructive.html">위험한 동작</a>.',
  cases=cases([
    (box(row('다크 모드 따라가기', sw(True), '기기 설정을 따릅니다'), "150px"),
     "바로 적용", "<b>스위치 하나에 설명 한 줄.</b> 가장 흔한 꼴"),
    (box(row('표시 이름', cb(False), '다른 사람에게 보입니다'), "150px", "프로필", "저장"),
     "저장 버튼 방식", "<b>여러 칸을 한 번에</b> 바꿀 때"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:4px">
                <div style="border:1px solid var(--line);border-radius:999px;padding:3px 8px;font-size:9px;color:var(--fg-muted)">🔍 설정 검색</div>
                <span style="font-size:8.5px;color:var(--fg-muted)">‘알림’ → 4개</span>
              </div>''',
     "설정 검색", "<b>묶음을 못 외운 사람</b>을 구한다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="묶음은 <code>&lt;fieldset&gt;</code>, 바로 적용은 <code>role=\"switch\"</code>로 적습니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;알림&lt;/<span class="t">legend</span>&gt;

  <span class="c">&lt;!-- 바로 적용 --&gt;</span>
  &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"row"</span>&gt;
    &lt;<span class="t">span</span> <span class="a">id</span>=<span class="s">"n1"</span>&gt;새 정산 알림&lt;/<span class="t">span</span>&gt;
    &lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"n1d"</span>&gt;정산이 들어오면 알려 줍니다&lt;/<span class="t">p</span>&gt;
    &lt;<span class="t">button</span> <span class="a">role</span>=<span class="s">"switch"</span> <span class="a">aria-checked</span>=<span class="s">"true"</span>
            <span class="a">aria-labelledby</span>=<span class="s">"n1"</span> <span class="a">aria-describedby</span>=<span class="s">"n1d"</span>&gt;&lt;/<span class="t">button</span>&gt;
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;

&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;저장했습니다&lt;/<span class="t">p</span>&gt;

<span class="c">// 저장 버튼 방식이면 나가기 전에 물어본다</span>
window.addEventListener(<span class="s">'beforeunload'</span>, e =&gt; { <span class="k">if</span> (dirty) e.preventDefault(); });''',
  keys=kbd([
    ("<code>role=\"switch\"</code> + <code>aria-checked</code>", "'켜짐/꺼짐'으로 읽힌다. 체크박스는 '선택됨'이다 — <b>뜻이 다르다</b>"),
    ("<code>aria-describedby</code>", "줄 밑 설명을 묶는다. 안 묶으면 <b>이름만</b> 읽힌다"),
    ("<code>&lt;fieldset&gt;&lt;legend&gt;</code>", "묶음 이름이 함께 읽힌다 — '알림 묶음, 새 정산 알림 스위치'"),
    ("<code>role=\"status\"</code>", "바로 적용이면 <b>저장됐다는 말</b>이 필요하다. 색만 바뀌면 모른다"),
    ("저장 전 이탈", "<code>beforeunload</code>. 다만 <a href=\"systemback.html\">뒤로가기</a>엔 안 통할 수 있어 직접 묻는다"),
    ("위험 구역", "<b>Tab 으로 쉽게 닿는 자리</b>에 두지 않는다. 맨 아래로"),
  ]),
  backend=rows([
    ("바로 적용은 요청이 잦다", "스위치를 넘길 때마다 요청이 갑니다. <b>묶어 보내거나</b> 짧게 디바운스합니다."),
    ("실패했을 때 되돌린다", "요청이 실패했는데 스위치가 켜진 채면 <b>거짓말</b>이 됩니다. <a href=\"../items/optimistic.html\">낙관적 UI</a>의 되돌리기가 필요합니다."),
    ("기본값은 서버가 쥔다", "'아직 안 고른 것'과 '꺼 둔 것'은 다릅니다. <b>null 과 false</b>를 가려 두면 나중에 기본값을 바꿀 수 있습니다."),
    ("설정이 늘어난다", "칸을 하나씩 늘리면 저장 구조가 금방 넓어집니다. <b>키-값</b>으로 두는 편이 오래갑니다."),
    ("기기별 설정", "다크 모드처럼 <b>기기마다 달라야</b> 하는 것은 계정에 저장하면 안 됩니다."),
  ]),
  plat_lede="<b>스위치냐 체크박스냐</b>의 관례가 다릅니다.",
  plats=plats([
    ("웹", "둘 다 쓴다",
     box(row('알림', cb(True)), "112px", "설정", "저장"),
     "저장 버튼이 있는 화면이 많아 <b>체크박스</b>도 흔합니다. 둘을 섞지만 않으면 됩니다."),
    ("iOS", "거의 스위치",
     '''              <div class="phone" role="img" aria-label="iOS 설정 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;align-items:center;font-size:6px"><span style="flex:1">알림</span><span style="width:14px;height:8px;border-radius:999px;background:var(--accent)"></span></div></div></div>''',
     "설정 앱이 전부 스위치라 <b>저장 버튼이 거의 없습니다.</b> 그 관례를 따르는 편이 자연스럽습니다."),
    ("안드로이드", "Preference 화면",
     '''              <div class="phone" role="img" aria-label="안드로이드 설정 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:6px"><span style="display:block">알림</span><span style="display:block;color:var(--fg-muted);font-size:5px">정산이 들어오면</span></div></div></div>''',
     "이름 + <b>요약 줄</b>이 규격으로 정해져 있습니다. 설정 검색도 OS 가 거들어 줍니다."),
  ]),
  plat_note="\"설정에 옵션 하나만 추가해 주세요\"가 쌓이면 서른 줄짜리 화면이 됩니다. 늘릴 때마다 <b>'이게 정말 사람마다 달라야 하나'</b>를 한 번 묻는 편이 좋습니다 — 대개는 좋은 기본값 하나로 끝나고, 설정은 <b>고르게 만든 쪽이 책임을 미룬 자리</b>인 경우가 많습니다.",
  siblings=siblings("settings"),
  related='''        <li><a href="../items/switch.html"><b>스위치</b><em>4부</em></a></li>
        <li><a href="../items/checkbox.html"><b>체크박스</b><em>4부</em></a></li>
        <li><a href="destructive.html"><b>위험한 동작</b><em>13부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>''',
)
