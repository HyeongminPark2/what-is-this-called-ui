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
  desc="칸 이름·형식의 보기·규칙은 각각 다른 자리에 적는다. 자리글을 레이블로 쓰면 안 되는 이유.",
  lede="레이블 · 자리글 · 헬퍼는 <b>서로 다른 일</b>을 합니다. 하나로 때우면 다른 둘이 사라집니다.",
  axes_lede="화면의 말은 꾸미는 것이 아니라 <b>일하는 것</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>레이블을 자리글로 쓰기</b>를 켜고 <b>세 칸 채우기</b>를 눌러 보세요 —
          글자를 치는 순간 <b>그 칸이 무슨 칸이었는지</b>가 사라집니다.<br>
          자리글의 일은 <b>형식의 보기를 드는 것</b>입니다. 칸 이름은 레이블이,
          규칙은 헬퍼 텍스트가 맡습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "자리글, 플레이스홀더, 힌트, 헬퍼 텍스트, 보조 설명"),
    ("영어", "placeholder, hint text, helper text, supporting text"),
    ("같이 쓰는 말",
     "<code>placeholder</code> 속성으로 넣는 흐린 글자가 <b>자리글</b>이고, "
     "칸 밑에 늘 보이는 설명이 <b>헬퍼 텍스트</b>·<b>서포팅 텍스트</b>입니다. "
     "칸 이름이 칸 안에 있다가 치면 위로 올라가는 것을 <b>플로팅 레이블</b>이라 합니다."),
    ("자주 잘못 부름",
     "<b>레이블</b> — 자리글은 레이블이 아닙니다. 치면 <b>사라지기</b> 때문입니다.<br>"
     "<b>툴팁</b> — <a href=\"../items/tooltip.html\">툴팁</a>은 올려야 보입니다. <a href=\"hover.html\">폰에서는 못 봅니다</a>.<br>"
     "<b>오류 문구</b> — <a href=\"errortext.html\">오류</a>는 틀린 <b>뒤</b>, 헬퍼는 틀리기 <b>전</b>입니다."),
  ]),
  axes=ax("자리글과 헬퍼 텍스트"),
  oneline="<b>자리글은 보기, 헬퍼는 규칙, 레이블은 이름.</b> 셋 다 필요하고 서로 대신하지 못합니다.",
  s4_title="셋을 가르면", s4_hint="무엇이 사라지나",
  states=states([
    (fld('사업자번호', '1248100998', '', '- 없이 10자리', "152px", "셋이 다 있다", True),
     "제대로", "이름 · 보기 · 규칙이 <b>따로</b> 있다"),
    (fld('', '사업자번호', '', '', "152px", "레이블을 자리글로 썼다", False),
     "자리글만", "비어 있을 때는 멀쩡해 보인다"),
    (fld('', '사업자번호', '1248100998', '', "152px", "치는 순간 이름이 사라졌다", False),
     "치고 나면", "<b>무슨 칸이었는지 모른다</b>"),
    (fld('사업자번호', '', '', '- 없이 10자리', "152px", "보기가 없다"),
     "자리글 없이", "규칙은 알지만 <b>어떻게 생겼는지</b> 모른다"),
    (fld('사업자번호', '1248100998', '', '', "152px", "규칙이 없다"),
     "헬퍼 없이", "<b>틀린 뒤에야</b> 알게 된다"),
    (fld('사업자번호', '', '124', '10자리를 채워 주세요', "152px", "헬퍼 자리에 오류가 들어왔다"),
     "틀렸을 때", "<a href=\"validation.html\">검증</a>이 <b>같은 자리</b>를 쓴다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("레이블", "칸의 이름", "<b>늘 보인다.</b> 치든 안 치든 사라지지 않는다"),
    ("자리글", "형식의 보기", "<code>1248100998</code>처럼 <b>진짜 같은 값</b>을"),
    ("헬퍼", "규칙", "'- 없이 10자리'. <b>틀리기 전에</b> 알려 준다"),
    ("오류", "헬퍼 자리에", "틀린 뒤 같은 자리에 들어온다. <b>칸이 안 움직인다</b>"),
    ("자리글 색", "흐리게, 그러나", "너무 흐리면 <a href=\"../items/contrast.html\">대비비</a>에 걸린다"),
    ("자리글을 이름으로", "치면 사라진다", "<b>가장 흔한 실수.</b> 고치러 돌아오면 못 읽는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>'비어 있을 때는 멀쩡해 보인다'</b>는 것이 이 실수가 오래 사는 이유입니다.
          시안은 대개 <b>빈 칸</b>으로 그려지고, 거기서는 자리글이 레이블 노릇을 잘합니다.
          문제는 <b>값이 들어간 뒤</b>에만 나타납니다 —
          고치러 돌아온 화면, 자동완성이 채운 칸, 오류를 고치는 중.
          전부 <b>처음 쓸 때가 아니라 두 번째부터</b>라, 시안 검토에서는 거의 안 걸립니다.</p>''',
  do=ul([
    "셋을 <b>따로</b> 두기 — 이름 · 보기 · 규칙",
    "자리글에는 <b>진짜 같은 값</b>을 넣기",
    "규칙은 <b>틀리기 전에</b> 보여 주기",
  ]),
  dont=ul([
    "자리글을 레이블로 — <b>치면 사라진다</b>",
    "자리글에 ‘입력하세요’ — <b>아무 정보가 없다</b>",
    "설명을 <a href=\"../items/tooltip.html\">툴팁</a>에만 — 폰에서 못 본다",
    "자리글을 너무 흐리게 — 대비비가 모자란다",
  ]),
  instead='칸 자체는 <a href="../items/field.html">입력 필드</a>, 틀린 뒤 문구는 <a href="validation.html">입력 검증</a>, 칸이 많으면 <a href="form.html">폼 설계</a>.',
  cases=cases([
    (fld('정산 계좌', '110-123-456789', '', '예금주가 상호와 같아야 합니다', "150px"), "형식이 있는 칸", "<b>보기와 규칙</b>이 둘 다 필요하다"),
    (fld('검색', '가맹점 이름이나 번호', '', '', "150px"), "검색칸", "<b>무엇을 칠 수 있는지</b>가 곧 보기다"),
    (fld('메모', '', '', '내부에서만 보입니다', "150px"), "자유로운 칸", "보기가 없어도 된다. <b>규칙만</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 글자들의 계약서",
  code_lede="레이블은 <code>&lt;label&gt;</code>, 헬퍼는 <code>aria-describedby</code>로 묶습니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"no"</span>&gt;사업자번호&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"no"</span> <span class="a">name</span>=<span class="s">"no"</span>
       <span class="a">placeholder</span>=<span class="s">"1248100998"</span>
       <span class="a">inputmode</span>=<span class="s">"numeric"</span>
       <span class="a">aria-describedby</span>=<span class="s">"no-help"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"no-help"</span> <span class="a">class</span>=<span class="s">"help"</span>&gt;- 없이 10자리&lt;/<span class="t">p</span>&gt;

<span class="c">/* 자리글은 흐리되 읽을 수는 있게 */</span>
<span class="t">input</span>::placeholder { <span class="a">color</span>: <span class="a">var</span>(--fg-muted); }   <span class="c">/* 4.5:1 을 지킨다 */</span>''',
  keys=kbd([
    ("<code>&lt;label for&gt;</code>", "<b>자리글은 이름이 못 된다.</b> 보조기기가 읽는 것은 레이블이다"),
    ("<code>aria-describedby</code>", "헬퍼를 칸에 묶는다. 안 묶으면 <b>그냥 옆에 있는 글</b>이다"),
    ("오류와 헬퍼를 같은 자리에", "칸이 위아래로 안 움직인다. <b>글이 덜컥거리지 않는다</b>"),
    ("<code>::placeholder</code> 대비비", "브라우저 기본값은 <b>4.5:1 에 못 미친다</b>. 직접 정한다"),
    ("자리글에 <b>단위</b>를 넣지 않는다", "'원'을 자리글에 두면 치는 순간 사라진다. <b>칸 밖에</b> 적는다"),
    ("<code>title</code> 속성", "호버로만 뜬다. <a href=\"hover.html\">폰에서는 못 본다</a> — 헬퍼로 뺀다"),
  ]),
  backend=rows([
    ("형식을 한곳에 적어 둔다", "자리글·헬퍼·<a href=\"validation.html\">검증</a>·서버 검사가 <b>따로 놀면</b> 서로 다른 규칙을 말하게 됩니다."),
    ("서버 오류도 같은 자리에", "서버가 돌려준 문구를 <b>헬퍼 자리</b>에 넣으면 화면이 안 흔들립니다."),
    ("보기 값을 진짜로 쓰지 않는다", "자리글에 넣은 번호가 <b>실제 사업자번호</b>면 곤란합니다. 만든 값을 씁니다."),
  ]),
  plat_lede="<b>플로팅 레이블</b>을 쓰느냐가 갈립니다.",
  plats=plats([
    ("웹", "label + placeholder",
     fld('사업자번호', '1248100998', '', '- 없이 10자리', "110px"),
     "레이블은 칸 위, 헬퍼는 칸 밑. <b>가장 안 깨지는</b> 꼴입니다."),
    ("iOS", "이름을 왼쪽에",
     '''              <div class="phone" role="img" aria-label="iOS 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;display:flex;font-size:6px;border-bottom:1px solid var(--line);padding-bottom:2px"><span style="width:38%;color:var(--fg-muted)">사업자번호</span><span style="color:var(--fg-faint)">1248100998</span></div></div></div>''',
     "설정 화면처럼 <b>왼쪽 이름 · 오른쪽 값</b>. 자리글이 값 자리에 흐리게 들어갑니다."),
    ("안드로이드", "플로팅 레이블",
     '''              <div class="phone" role="img" aria-label="Material 입력 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;background:var(--bg);border-radius:4px 4px 0 0;border-bottom:1px solid var(--accent);padding:3px"><div style="font-size:5px;color:var(--accent)">사업자번호</div><div style="font-size:6px">1248100998</div></div>
                <div style="position:absolute;left:6px;top:50px;font-size:5px;color:var(--fg-muted)">- 없이 10자리</div></div></div>''',
     "이름이 <b>칸 안에서 위로 올라갑니다.</b> 사라지지 않으므로 자리글 문제를 피합니다."),
  ]),
  plat_note="시안이 깔끔해 보이려고 <b>레이블을 지우고 자리글만</b> 남기는 일이 흔합니다. 이건 취향 문제가 아니라 <b>두 번째 사용부터 깨지는</b> 설계라, 시안을 받을 때 <b>값이 채워진 상태</b>를 한 장 더 달라고 하면 그 자리에서 드러납니다.",
  siblings=siblings("placeholder"),
  related='''        <li><a href="../items/field.html"><b>입력 필드</b><em>4부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>''',
)
