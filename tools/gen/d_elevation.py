# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def lev(cls, name, use):
    return ('              <div style="display:grid;gap:8px;justify-items:center;padding:6px 0">'
            '<span class="%s" style="display:block;width:74px;height:40px;border-radius:9px;background:var(--surface);border:1px solid transparent"></span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">%s</span>'
            '<span style="font-size:10.5px;color:var(--fg-faint);text-align:center">%s</span></div>'
            ) % (cls, name, use)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:16px 10px 14px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border-radius:10px;padding:14px 12px;box-shadow:0 10px 24px rgba(20,22,26,.12), 0 3px 8px rgba(20,22,26,.08);font-size:12px">그림자 하나는 숫자 네 개와 색 하나입니다</div>
                  <div style="padding-left:26px;display:grid;gap:13px;font-family:var(--mono);font-size:11.5px">
                    <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">0<span style="color:var(--fg-faint)"> ← 가로 치우침</span></div>
                    <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">10px<span style="color:var(--fg-faint)"> ← 아래로 내린 거리</span></div>
                    <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">24px<span style="color:var(--fg-faint)"> ← 번짐</span></div>
                    <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">0<span style="color:var(--fg-faint)"> ← 퍼짐</span></div>
                    <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">rgba(20,22,26,.12)<span style="color:var(--fg-faint)"> ← 색과 진하기</span></div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="elevation", ko="고도", en="Elevation · shadow scale",
  desc="그림자를 단으로 정해 높이를 읽히게 하는 방법과, 그림자 한 개를 이루는 네 숫자를 보여주는 항목.",
  lede="무엇이 <b>얼마나 위에 떠 있는지</b>를 그림자로 말하는 단. 장식이 아니라 신호입니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단이 올라갈수록 그림자가 <b>더 멀리, 더 흐리게</b> 퍼집니다 — 진해지는 것이 아닙니다.
          빛이 위에서 온다고 치고 만들기 때문입니다.<br>
          <b>그림자 대신 테두리로</b>를 켜 보세요. 구역은 여전히 나뉘지만 <b>무엇이 위인지</b>가 사라집니다.
          어두운 화면에서 실제로 일어나는 일입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "고도, 그림자 단계, 그림자 체계"),
    ("영어", "elevation, shadow scale, depth"),
    ("같이 쓰는 말",
     "그림자 자체는 <b>드롭 섀도</b>(drop shadow), 안쪽으로 파인 것은 <b>인너 섀도</b>(inset)입니다. "
     "Material 에서는 높이를 <b>dp 단위의 고도</b>로 말하고(<code>elevation 6dp</code>), "
     "웹 디자인 시스템에서는 보통 <code>shadow-sm · md · lg</code> 같은 이름으로 둡니다."),
    ("자주 잘못 부름",
     "<b>z-index</b> — z-index 는 <b>쌓이는 순서</b>이고 고도는 <b>보이는 높이</b>입니다. "
     "둘을 같이 정해 두지만 같은 것이 아닙니다.<br>"
     "<b>블러</b> — 블러는 흐리게 하는 효과, 번짐은 그림자의 가장자리 처리입니다.<br>"
     "<b>입체</b> — 요즘의 고도는 입체감을 내려는 것이 아니라 <b>층을 구별</b>하려는 것입니다."),
  ]),
  axes=ax("고도"),
  oneline="고도는 <b>\"이게 위에 떠 있다\"는 한마디</b>입니다. 그림자를 예뻐서 넣고 있다면 이미 쓰임이 아닙니다.",
  s4_title="단", s4_hint="단마다 맡은 부품이 있다",
  states=states([
    (lev("elev-0", "elev-0", "표 · 목록"), "0단", "배경에 붙어 있다. <b>테두리로</b> 나눈다"),
    (lev("elev-1", "elev-1", "카드"), "1단", "살짝 떴다. 가장 많이 쓰는 단"),
    (lev("elev-2", "elev-2", "드롭다운 · 팝오버"), "2단", "눌러서 연 것. 곧 닫힌다"),
    (lev("elev-3", "elev-3", "모달 · 시트"), "3단", "화면을 가로막았다. 가림막과 함께 쓴다"),
    (lev("elev-4", "elev-4", "토스트 · 드래그 중"), "4단", "가장 위. <b>여기까지</b>다"),
    ('''              <div style="display:grid;gap:8px;justify-items:center;padding:6px 0">
                <span style="display:block;width:74px;height:40px;border-radius:9px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">border</span>
                <span style="font-size:10.5px;color:var(--fg-faint);text-align:center">어두운 화면</span></div>''',
     "테두리", "어두운 바탕에서는 그림자가 안 보인다. <b>면을 밝혀</b> 높이를 낸다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그림자 한 벌", "box-shadow", "보통 <b>두 겹</b>을 겹친다 — 가까운 짧은 그림자와 멀리 퍼지는 큰 그림자"),
    ("가로 치우침", "offset-x", "<b>거의 늘 0</b>이다. 빛이 바로 위에 있다고 치기 때문"),
    ("아래로 내린 거리", "offset-y", "높이를 말하는 숫자. 단이 올라갈수록 커진다"),
    ("번짐", "blur", "가장자리가 흐려지는 정도. 높을수록 <b>크게</b> 잡는다"),
    ("퍼짐", "spread", "그림자를 통째로 키우거나 줄인다. 보통 0, 테두리를 흉내 낼 때만 쓴다"),
    ("색과 진하기", "color · alpha", "검정 대신 <b>바탕색의 어두운 쪽</b>을 쓰면 덜 탁하다. 진하기는 0.06~0.18 사이"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          단을 올릴 때 <b>진하기를 올리는 것이 아니라 거리와 번짐을 키웁니다.</b>
          멀리 있는 물체일수록 그림자가 흐리고 넓게 퍼지기 때문입니다. 진하기만 올리면
          물체가 뜬 것이 아니라 <b>검댕이 묻은 것</b>처럼 보입니다.</p>''',
  do=ul([
    "겹쳐 뜨는 부품 — 드롭다운, 팝오버, 모달, 토스트",
    "끌어서 옮기는 중인 것 — <b>떴다</b>는 신호가 필요합니다",
    "밝은 바탕에서 카드를 구별할 때",
  ]),
  dont=ul([
    "어두운 화면 — 그림자가 안 보입니다. <b>면을 밝히는</b> 쪽으로 바꿉니다",
    "모든 것에 다 넣는 것 — 다 떠 있으면 아무것도 안 떠 있는 것과 같습니다",
    "글자와 아이콘에 — 읽기만 나빠집니다",
    "인쇄용 화면",
  ]),
  instead='앞뒤 순서를 정하는 일은 <a href="zindex.html">z-index</a>가 맡고, 어두운 쪽에서 높이를 내는 방법은 <a href="dark.html">다크 모드</a>에 있습니다.',
  cases=cases([
    ('''              <div style="position:relative;width:100%;max-width:200px;height:96px">
                <span style="position:absolute;inset:0;border-radius:9px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="position:absolute;left:18px;top:26px;width:120px;border-radius:8px;background:var(--surface);padding:8px 10px;font-size:11px;box-shadow:0 4px 12px rgba(20,22,26,.08), 0 1px 3px rgba(20,22,26,.06)">계정 설정</span>
              </div>''',
     "드롭다운", "<b>2단</b>. 눌러서 열었고 곧 닫힌다"),
    ('''              <div style="position:relative;width:100%;max-width:200px;height:96px">
                <span style="position:absolute;inset:0;border-radius:9px;background:rgba(14,16,20,.45)"></span>
                <span style="position:absolute;left:24px;top:24px;right:24px;border-radius:9px;background:var(--surface);padding:10px;font-size:11px;box-shadow:0 16px 48px rgba(20,22,26,.3)">정산을 확정할까요?</span>
              </div>''',
     "모달", "<b>3단 + 가림막</b>. 그림자만으로는 '가로막았다'가 안 된다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:200px">
                <span style="display:block;height:30px;border-radius:8px;background:var(--surface);box-shadow:0 2px 3px rgba(20,22,26,.35)"></span>
                <span style="display:block;height:30px;border-radius:8px;background:var(--surface);box-shadow:0 10px 24px rgba(20,22,26,.12)"></span>
                <span style="font-size:11px;color:var(--fg-muted)">위: 진하기만 올린 것 · 아래: 거리와 번짐을 키운 것</span>
              </div>''',
     "흔한 실패", "진하기를 올리면 뜨지 않고 <b>때가 탄 것</b>처럼 보인다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 단의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="단마다 그림자를 <b>두 겹</b>으로 둡니다 — 가까운 그림자가 테두리를 또렷하게 하고, 먼 그림자가 높이를 말합니다.",
  code='''<span class="t">:root</span> {
  <span class="a">--e1</span>: <span class="s">0 1px 2px rgba(20,22,26,.06), 0 1px 1px rgba(20,22,26,.04)</span>;
  <span class="a">--e2</span>: <span class="s">0 4px 12px rgba(20,22,26,.08), 0 1px 3px rgba(20,22,26,.06)</span>;
  <span class="a">--e3</span>: <span class="s">0 10px 24px rgba(20,22,26,.12), 0 3px 8px rgba(20,22,26,.08)</span>;
}

<span class="t">.card</span>     { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e1</span>); }
<span class="t">.popover</span>  { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e2</span>); }
<span class="t">.modal</span>    { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e3</span>); }

<span class="c">/* 어두운 모드 — 그림자는 안 보인다. 면을 밝혀 높이를 낸다 */</span>
<span class="t">:root[data-theme="dark"]</span> {
  <span class="a">--e1</span>: none; <span class="a">--e2</span>: none; <span class="a">--e3</span>: none;
  <span class="a">--surface-1</span>: <span class="s">#1c2029</span>; <span class="a">--surface-2</span>: <span class="s">#232834</span>;
}''',
  keys=kbd([
    ("단은 네댓 개", "0·1·2·3·4 면 충분하다. 여섯 단이 넘으면 서로 구별이 안 된다"),
    ("거리와 번짐을 키운다", "진하기는 거의 그대로 둔다. <b>높이 = 멀고 흐리게</b>"),
    ("가로 치우침은 0", "빛이 바로 위에 있다고 정해 두면 화면 전체가 일관된다"),
    ("검정 대신 어두운 바탕색", "<code>rgba(0,0,0,.2)</code>보다 바탕색 계열이 덜 탁하다"),
    ("어두운 모드는 면으로", "그림자를 <code>none</code>으로 두고 <b>면 색을 한 단 밝힌다</b>"),
    ("부품마다 단을 못 박는다", "'카드는 1단, 팝오버는 2단'처럼 정해 두면 매번 고르지 않아도 된다"),
  ]),
  backend=rows([
    ("고도 = 로그 레벨 같은 열거형", "DEBUG·INFO·WARN 처럼 <b>순서가 있는 적은 값</b>입니다. 중간값을 만들고 싶어지면 단 설계가 잘못된 것입니다."),
    ("성능", "그림자는 그릴 때마다 계산합니다. 긴 목록의 <b>줄마다</b> 큰 그림자를 넣으면 스크롤이 눈에 띄게 끊깁니다 — 목록 줄은 테두리로 나눕니다."),
    ("캡처·인쇄", "PDF 로 뽑거나 메일에 넣는 화면에서는 그림자가 <b>회색 띠</b>로 찍히는 일이 있습니다. 인쇄용 스타일에서는 꺼 둡니다."),
    ("고도와 z-index 를 같이 정의", "보이는 높이와 쌓이는 순서가 어긋나면 '위에 보이는데 클릭은 아래가 먹는' 버그가 납니다. <b>한 표에 같이</b> 적어 둡니다."),
  ]),
  plat_lede="안드로이드는 고도를 <b>물리적 높이</b>로 다루고, iOS 와 웹은 그림자 값을 직접 정합니다.",
  plats=plats([
    ("웹", "CSS box-shadow",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--shadow-sm<br>--shadow-md<br>--shadow-lg</div>''',
     "정해진 규격이 없어 팀마다 다릅니다. 두 겹 이상 겹쳐 만드는 것이 요즘 방식입니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.shadow(radius:)<br>.ultraThinMaterial</div>''',
     "그림자를 <b>절제해서</b> 씁니다. 떠 있는 느낌은 그림자보다 <b>머티리얼</b>(반투명 흐림)로 내는 일이 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">elevation = 6.dp<br>tonalElevation</div>''',
     "고도를 <b>dp 높이</b>로 적으면 그림자는 OS 가 계산합니다. M3 는 그림자 대신 <b>색조 고도</b>(면을 밝히는 방식)를 권합니다."),
  ]),
  plat_note="안드로이드에서 <b>고도는 숫자 하나</b>(6dp)이고 그림자는 따라 나옵니다. 웹에서 쓰던 그림자 값을 그대로 건네면 옮길 수가 없습니다. \"그림자 이렇게 해 주세요\" 대신 <b>\"이건 몇 단인가\"</b>로 이야기하면 세 플랫폼이 같은 말을 쓰게 됩니다.",
  siblings=siblings("elevation"),
  related='''        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><span class="na"><b>카드</b><em>5부</em></span></li>
        <li><span class="na"><b>모서리</b><em>2부</em></span></li>''',
)
