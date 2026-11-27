# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def fld(lab, ph, val="", help="", w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:2px">'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + lab + '</span>' if lab else '')
            + '<div style="border:1px solid var(--line);border-radius:4px;background:var(--surface);padding:4px 7px;'
              'font-size:9.5px;' + ('' if val else 'color:var(--fg-faint)') + '">' + (val or ph or '&nbsp;') + '</div>'
            + ('<span style="font-size:8px;color:var(--fg-muted)">' + help + '</span>' if help else '')
            + '</div>'
            + ('<span style="font-size:8.5px;color:' + (col if ok is not None else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">레이블 — 칸의 이름. 늘 보인다</div>
                  <div class="pin-out" data-pin="2" style="max-width:220px">''' + fld('사업자번호', '1248100998', '', '- 없이 10자리', "220px").strip() + '''</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">자리글 — 형식의 보기. 치면 사라진다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">헬퍼 — 규칙. 틀리기 전에 미리 알려 준다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">오류 — 틀린 뒤. 헬퍼 자리에 들어간다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자리글을 레이블로 쓰면 치는 순간 이름이 사라진다</div>
                </div>
              </div>'''

D = dict(
  slug="placeholder", ko="자리글과 헬퍼 텍스트", en="Placeholder & helper text",
  desc="칸 이름과 형식의 보기, 입력 규칙을 각각 다른 자리에 적는 방법과, 자리글을 레이블 대신 쓰면 안 되는 이유를 다룹니다.",
  lede="레이블은 칸 이름을, 자리글은 형식의 보기를, 헬퍼 텍스트는 입력 규칙을 알려 주기 때문에 셋은 <b>서로 다른 일</b>을 합니다. 하나로 셋을 대신하면 나머지 두 정보가 화면에서 빠집니다.",
  axes_lede="화면에 적는 문구는 사용자가 <b>무엇을 하면 되는지</b> 알려 주려고 씁니다. 아래 네 가지를 물어보면 문구마다 알려야 할 것과 자주 틀리는 곳, 고치는 기준이 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>레이블을 자리글로 쓰기</b>를 켜고 <b>세 칸 채우기</b>를 눌러 보세요.
          글자가 들어가는 순간 자리글이 사라지면서 <b>그 칸이 무슨 칸이었는지</b>도 알 수 없게 됩니다.<br>
          자리글에는 <b>입력할 값의 형식을 보기로</b> 보여 주고, 칸 이름은 레이블에,
          규칙은 헬퍼 텍스트에 적습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자리글, 플레이스홀더, 힌트, 헬퍼 텍스트, 보조 설명"),
    ("영어", "placeholder, hint text, helper text, supporting text"),
    ("같이 쓰는 말",
     "<code>placeholder</code> 속성으로 넣는 흐린 글자가 <b>자리글</b>이고, "
     "칸 밑에 늘 보이는 설명이 <b>헬퍼 텍스트</b>·<b>서포팅 텍스트</b>입니다. "
     "칸 이름이 칸 안에 있다가 글자를 치면 위로 올라가는 것은 <b>플로팅 레이블</b>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>레이블</b> — 자리글은 글자를 치면 <b>사라지기</b> 때문에 레이블이 될 수 없습니다.<br>"
     "<b>툴팁</b> — <a href=\"../items/tooltip.html\">툴팁</a>은 마우스를 올려야 보이기 때문에 <a href=\"hover.html\">폰에서는 볼 수 없습니다</a>.<br>"
     "<b>오류 문구</b> — <a href=\"errortext.html\">오류</a> 문구는 값이 틀린 <b>뒤</b>에 보여 주고, 헬퍼 텍스트는 틀리기 <b>전</b>에 미리 보여 줍니다."),
  ]),
  axes=ax("자리글과 헬퍼 텍스트"),
  oneline="<b>자리글은 보기를, 헬퍼는 규칙을, 레이블은 이름을 알려 줍니다.</b> 셋 다 필요하고, 어느 하나가 다른 것을 대신할 수 없습니다.",
  s4_title="셋을 가르면", s4_hint="무엇이 사라지나",
  states=states([
    (fld('사업자번호', '1248100998', '', '- 없이 10자리', "152px", "셋이 다 있다", True),
     "제대로", "이름과 보기, 규칙이 <b>각자 자리에</b> 있습니다"),
    (fld('', '사업자번호', '', '', "152px", "레이블을 자리글로 썼다", False),
     "자리글만", "칸이 비어 있을 때는 문제가 없어 보입니다"),
    (fld('', '사업자번호', '1248100998', '', "152px", "치는 순간 이름이 사라졌다", False),
     "치고 나면", "값을 치고 나면 <b>무슨 칸이었는지 알 수 없습니다</b>"),
    (fld('사업자번호', '', '', '- 없이 10자리', "152px", "보기가 없다"),
     "자리글 없이", "규칙은 알 수 있지만 값이 <b>어떻게 생겼는지</b>는 알 수 없습니다"),
    (fld('사업자번호', '1248100998', '', '', "152px", "규칙이 없다"),
     "헬퍼 없이", "규칙을 <b>틀린 뒤에야</b> 알게 됩니다"),
    (fld('사업자번호', '', '124', '10자리를 채워 주세요', "152px", "헬퍼 자리에 오류가 들어왔다"),
     "틀렸을 때", "<a href=\"validation.html\">검증</a> 오류 문구가 헬퍼와 <b>같은 자리</b>에 들어갑니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("레이블", "칸의 이름", "<b>늘 보입니다.</b> 값을 쳐도 사라지지 않습니다"),
    ("자리글", "형식의 보기", "<code>1248100998</code>처럼 <b>진짜 같은 값</b>을 보기로 넣습니다"),
    ("헬퍼", "규칙", "'- 없이 10자리'처럼 지켜야 할 규칙을 <b>틀리기 전에</b> 알려 줍니다"),
    ("오류", "헬퍼 자리에", "값이 틀리면 헬퍼 자리에 오류 문구가 들어오므로 <b>칸이 위아래로 움직이지 않습니다</b>"),
    ("자리글 색", "흐리게, 그러나", "흐리게 쓰되, 너무 흐리면 <a href=\"../items/contrast.html\">대비비</a> 기준을 지키지 못합니다"),
    ("자리글을 이름으로", "치면 사라진다", "<b>가장 흔한 실수</b>입니다. 값을 고치러 돌아왔을 때 칸 이름을 읽을 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이 실수가 오래 고쳐지지 않는 까닭은 칸이 <b>비어 있을 때는 멀쩡해 보이기</b> 때문입니다.
          시안은 대개 <b>빈 칸</b>으로 그리는데, 빈 칸에서는 자리글이 레이블 역할을 충분히 합니다.
          문제는 값을 고치러 돌아온 화면, 자동완성이 채운 칸, 오류를 고치는 중처럼
          <b>값이 들어간 뒤</b>에만 나타납니다.
          모두 <b>처음 입력할 때가 아니라 두 번째부터</b> 겪는 상황이라서 시안 검토에서는 거의 드러나지 않습니다.</p>''',
  do=ul([
    "이름 · 보기 · 규칙을 <b>따로</b> 두기",
    "자리글에는 <b>진짜 같은 값</b>을 넣기",
    "규칙은 <b>틀리기 전에</b> 보여 주기",
  ]),
  dont=ul([
    "자리글을 레이블 대신 쓸 때. 값을 <b>치면 사라집니다</b>",
    "자리글에 ‘입력하세요’라고 적을 때. <b>아무 정보도 주지 않습니다</b>",
    "설명을 <a href=\"../items/tooltip.html\">툴팁</a>에만 넣을 때. 폰에서는 볼 수 없습니다",
    "자리글을 너무 흐리게 쓸 때. 대비비가 모자랍니다",
  ]),
  instead='칸 자체는 <a href="../items/field.html">입력 필드</a>, 틀린 뒤 문구는 <a href="validation.html">입력 검증</a>, 칸이 많으면 <a href="form.html">폼 설계</a>.',
  cases=cases([
    (fld('정산 계좌', '110-123-456789', '', '예금주가 상호와 같아야 합니다', "150px"), "형식이 있는 칸", "<b>보기와 규칙</b>이 둘 다 필요합니다"),
    (fld('검색', '가맹점 이름이나 번호', '', '', "150px"), "검색칸", "<b>무엇으로 찾을 수 있는지</b>를 자리글에 보기로 적습니다"),
    (fld('메모', '', '', '내부에서만 보입니다', "150px"), "자유로운 칸", "형식이 정해지지 않은 칸이라 보기 없이 <b>규칙만</b> 적어도 됩니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="코드로 옮길 때 지킬 것",
  code_lede="레이블은 <code>&lt;label&gt;</code>로 칸에 연결하고, 헬퍼는 <code>aria-describedby</code>로 칸에 묶습니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"no"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"no"</span> <span class="a">name</span>=<span class="s">"no"</span>
       <span class="a">placeholder</span>=<span class="s">"1248100998"</span>
       <span class="a">inputmode</span>=<span class="s">"numeric"</span>
       <span class="a">aria-describedby</span>=<span class="s">"no-help"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"no-help"</span> <span class="a">class</span>=<span class="s">"help"</span>&gt;- 없이 10자리&lt;/<span class="t">p</span>&gt;

<span class="c">/* 자리글은 흐리되 읽을 수는 있게 */</span>
<span class="t">input</span>::placeholder { <span class="a">color</span>: <span class="a">var</span>(--fg-muted); }   <span class="c">/* 4.5:1 을 지킨다 */</span>''',
  keys=kbd([
    ("<code>&lt;label for&gt;</code>", "보조기기는 레이블을 칸 이름으로 읽으므로 <b>자리글로는 이름을 대신할 수 없습니다</b>"),
    ("<code>aria-describedby</code>", "헬퍼 텍스트를 칸에 연결합니다. 연결하지 않으면 보조기기에게는 칸과 상관없는 <b>그냥 옆에 있는 글</b>이 됩니다"),
    ("오류와 헬퍼를 같은 자리에", "오류 문구가 헬퍼 자리에 들어가므로 칸이 위아래로 움직이지 않고, <b>글이 밀려 흔들리지도 않습니다</b>"),
    ("<code>::placeholder</code> 대비비", "브라우저 기본 자리글 색은 대비비가 <b>4.5:1에 못 미치므로</b> 색을 직접 정합니다"),
    ("자리글에 <b>단위</b>를 넣지 않는다", "'원' 같은 단위를 자리글에 두면 값을 치는 순간 사라지므로 <b>칸 밖에</b> 적습니다"),
    ("<code>title</code> 속성", "마우스를 올려야만 뜨기 때문에 <a href=\"hover.html\">폰에서는 볼 수 없습니다</a>. 설명은 헬퍼 텍스트로 옮깁니다"),
  ]),
  backend=rows([
    ("형식을 한곳에 적어 둔다", "자리글, 헬퍼, <a href=\"validation.html\">검증</a>, 서버 검사가 형식을 <b>각자 따로 정해 두면</b> 서로 다른 규칙을 말하게 됩니다."),
    ("서버 오류도 같은 자리에", "서버가 돌려준 오류 문구도 <b>헬퍼 자리</b>에 넣으면 칸이 밀리지 않아 화면이 흔들리지 않습니다."),
    ("보기 값을 진짜로 쓰지 않는다", "자리글에 넣은 번호가 누군가의 <b>실제 사업자번호</b>이면 곤란하므로, 형식만 맞춘 지어낸 값을 씁니다."),
  ]),
  plat_lede="플랫폼마다 <b>플로팅 레이블</b>을 쓰는지가 다릅니다.",
  plats=plats([
    ("웹", "label + placeholder",
     fld('사업자번호', '1248100998', '', '- 없이 10자리', "110px"),
     "레이블은 칸 위에, 헬퍼는 칸 밑에 둡니다. 여러 상황에서 <b>가장 덜 깨지는</b> 배치입니다."),
    ("iOS", "이름을 왼쪽에",
     '''              <div class="phone" role="img" aria-label="iOS 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;font-size:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="width:38%;color:var(--fg-muted)">사업자번호</span><span style="color:var(--fg-faint)">1248100998</span></div></div></div>''',
     "설정 화면처럼 <b>왼쪽에 이름, 오른쪽에 값</b>을 두고, 자리글은 값 자리에 흐리게 들어갑니다."),
    ("안드로이드", "플로팅 레이블",
     '''              <div class="phone" role="img" aria-label="Material 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-radius:4px 4px 0 0;border-bottom:1px solid var(--accent);padding:3px"><div style="font-size:5px;color:var(--accent)">사업자번호</div><div style="font-size:6px">1248100998</div></div>
                <div style="position:absolute;left:6px;top:50px;font-size:5px;color:var(--fg-muted)">- 없이 10자리</div></div></div>''',
     "값을 치면 칸 이름이 <b>칸 안에서 위로 올라갑니다.</b> 이름이 사라지지 않으므로 자리글을 레이블로 쓸 때의 문제가 생기지 않습니다."),
  ]),
  plat_note="시안을 깔끔하게 보이려고 <b>레이블을 지우고 자리글만</b> 남기는 일이 흔합니다. 이런 설계에서는 <b>두 번째 사용부터 칸 이름을 읽을 수 없으므로</b> 취향으로 넘길 문제가 아닙니다. 시안을 받을 때 <b>값이 채워진 상태</b>의 화면을 한 장 더 달라고 하면 이 문제가 그 자리에서 드러납니다.",
  siblings=siblings("placeholder"),
  related='''        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
