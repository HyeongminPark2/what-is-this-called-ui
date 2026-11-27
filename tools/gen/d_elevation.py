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
  desc="그림자를 단으로 정해 화면 요소의 높이를 알아볼 수 있게 하는 방법과, 그림자 하나를 이루는 숫자 네 개를 보여 주는 항목입니다.",
  lede="고도는 화면 요소가 <b>얼마나 위에 떠 있는지</b>를 그림자로 나타내도록 정해 둔 단입니다. 그림자는 꾸미려고 넣는 것이 아니라 높이를 알려 주려고 넣습니다.",
  axes_lede="토큰은 부품이 아니라 <b>값을 쓰는 규칙</b>입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단이 올라갈수록 그림자는 진해지지 않고 <b>더 멀리, 더 흐리게</b> 퍼집니다.
          빛이 위에서 비춘다고 가정하고 만들기 때문입니다.<br>
          <b>그림자 대신 테두리로 나누기</b>를 켜 보세요. 구역은 여전히 나뉘지만 <b>무엇이 위에 있는지</b>는 알 수 없게 됩니다.
          그림자가 잘 보이지 않는 어두운 화면에서도 같은 일이 일어납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "고도, 그림자 단계, 그림자 체계"),
    ("영어", "elevation, shadow scale, depth"),
    ("같이 쓰는 말",
     "그림자 자체는 <b>드롭 섀도</b>(drop shadow), 안쪽으로 파인 듯 보이게 하는 그림자는 <b>인너 섀도</b>(inset)라고 합니다. "
     "Material에서는 높이를 <b>dp 단위의 고도</b>로 나타내고(<code>elevation 6dp</code>), "
     "웹 디자인 시스템에서는 보통 <code>shadow-sm · md · lg</code> 같은 이름을 붙여 둡니다."),
    ("자주 잘못 부르는 이름",
     "<b>z-index</b> — z-index는 요소가 <b>쌓이는 순서</b>이고, 고도는 눈에 <b>보이는 높이</b>입니다. "
     "둘을 함께 정해 두기는 하지만 같은 것은 아닙니다.<br>"
     "<b>블러</b> — 블러는 대상을 흐리게 만드는 효과이고, 번짐은 그림자 가장자리를 흐리게 처리하는 값입니다.<br>"
     "<b>입체</b> — 요즘 쓰는 고도는 입체감을 내려는 것이 아니라 화면의 <b>층을 구별</b>하려는 것입니다."),
  ]),
  axes=ax("고도"),
  oneline="고도는 <b>\"이 요소가 위에 떠 있다\"는 것을 알리는 표시</b>입니다. 보기 좋아서 그림자를 넣고 있다면 고도를 쓰임에 맞게 쓰고 있지 않은 것입니다.",
  s4_title="고도 단계별 쓰는 부품", s4_hint="단마다 그 높이를 주는 부품",
  states=states([
    (lev("elev-0", "elev-0", "표 · 목록"), "0단, 배경에 붙은 면", "배경에 붙어 있는 단이라 그림자 대신 <b>테두리로</b> 구역을 나눕니다"),
    (lev("elev-1", "elev-1", "카드"), "1단, 살짝 뜬 면", "배경에서 살짝 떠 있는 단으로, 가장 많이 씁니다"),
    (lev("elev-2", "elev-2", "드롭다운 · 팝오버"), "2단, 눌러서 여는 부품", "눌러서 열었다가 곧 닫히는 부품에 씁니다"),
    (lev("elev-3", "elev-3", "모달 · 시트"), "3단, 화면을 가로막는 부품", "화면을 가로막는 부품에 쓰며, 가림막과 함께 씁니다"),
    (lev("elev-4", "elev-4", "토스트 · 드래그 중"), "4단, 가장 위에 놓이는 것", "가장 위에 놓이는 단이고, 단은 <b>여기까지만</b> 둡니다"),
    ('''              <div style="display:grid;gap:8px;justify-items:center;padding:6px 0">
                <span style="display:block;width:74px;height:40px;border-radius:9px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">border</span>
                <span style="font-size:10.5px;color:var(--fg-faint);text-align:center">어두운 화면</span></div>''',
     "어두운 화면에서 쓰는 테두리", "어두운 바탕에서는 그림자가 잘 보이지 않으므로 <b>면을 밝게 칠해</b> 높이를 나타냅니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("그림자 한 벌", "box-shadow", "보통 가까이 붙는 짧은 그림자와 멀리 퍼지는 큰 그림자, <b>두 겹</b>을 겹쳐 씁니다"),
    ("가로 치우침", "offset-x", "빛이 바로 위에 있다고 가정하기 때문에 <b>거의 늘 0</b>으로 둡니다"),
    ("아래로 내린 거리", "offset-y", "높이를 나타내는 숫자로, 단이 올라갈수록 커집니다"),
    ("번짐", "blur", "그림자 가장자리가 흐려지는 정도입니다. 높은 단일수록 <b>크게</b> 잡습니다"),
    ("퍼짐", "spread", "그림자 전체를 키우거나 줄입니다. 보통 0으로 두고, 테두리처럼 보이게 할 때만 씁니다"),
    ("색과 진하기", "color · alpha", "검정 대신 <b>바탕색 계열의 어두운 색</b>을 쓰면 덜 탁해 보입니다. 진하기는 0.06~0.18 사이로 둡니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          단을 올릴 때는 <b>진하기를 올리지 않고 거리와 번짐을 키웁니다.</b>
          바닥에서 멀리 떨어진 물체일수록 그림자가 흐리고 넓게 퍼지기 때문입니다. 진하기만 올리면
          물체가 떠 보이지 않고 <b>둘레에 짙은 회색 테두리가 생긴 것</b>처럼 보입니다.</p>''',
  do=ul([
    "드롭다운, 팝오버, 모달, 토스트처럼 다른 요소 위에 겹쳐 뜨는 부품일 때",
    "끌어서 옮기는 중인 요소일 때. 바닥에서 <b>들어 올렸다</b>는 표시가 필요합니다",
    "밝은 바탕에서 카드를 구별할 때",
  ]),
  dont=ul([
    "어두운 화면일 때. 그림자가 잘 보이지 않으므로 <b>면을 밝히는</b> 방식으로 바꿉니다",
    "모든 요소에 그림자를 넣을 때. 전부 떠 있으면 어느 것이 위에 있는지 구별할 수 없습니다",
    "글자와 아이콘에 넣을 때. 높이는 드러나지 않고 읽기만 어려워집니다",
    "인쇄용 화면일 때",
  ]),
  instead_title="고도와 함께 보면 좋은 항목",
  instead='요소가 쌓이는 앞뒤 순서는 <a href="zindex.html">z-index</a>로 정하고, 어두운 화면에서 높이를 나타내는 방법은 <a href="dark.html">다크 모드</a> 항목에서 다룹니다.',
  cases=cases([
    ('''              <div style="position:relative;width:100%;max-width:200px;height:96px">
                <span style="position:absolute;inset:0;border-radius:9px;background:var(--surface);border:1px solid var(--line)"></span>
                <span style="position:absolute;left:18px;top:26px;width:120px;border-radius:8px;background:var(--surface);padding:8px 10px;font-size:11px;box-shadow:0 4px 12px rgba(20,22,26,.08), 0 1px 3px rgba(20,22,26,.06)">계정 설정</span>
              </div>''',
     "드롭다운에 2단 쓰기", "눌러서 열었다가 곧 닫히는 부품이므로 <b>2단</b>을 씁니다"),
    ('''              <div style="position:relative;width:100%;max-width:200px;height:96px">
                <span style="position:absolute;inset:0;border-radius:9px;background:rgba(14,16,20,.45)"></span>
                <span style="position:absolute;left:24px;top:24px;right:24px;border-radius:9px;background:var(--surface);padding:10px;font-size:11px;box-shadow:0 16px 48px rgba(20,22,26,.3)">정산을 확정할까요?</span>
              </div>''',
     "모달에 3단과 가림막 쓰기", "<b>3단에 가림막</b>을 더합니다. 그림자만으로는 모달이 화면을 가로막았다는 것이 드러나지 않습니다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:200px">
                <span style="display:block;height:30px;border-radius:8px;background:var(--surface);box-shadow:0 2px 3px rgba(20,22,26,.35)"></span>
                <span style="display:block;height:30px;border-radius:8px;background:var(--surface);box-shadow:0 10px 24px rgba(20,22,26,.12)"></span>
                <span style="font-size:11px;color:var(--fg-muted)">위는 진하기만 올림 · 아래는 거리와 번짐을 키움</span>
              </div>''',
     "그림자 진하기만 올린 실패", "진하기만 올리면 떠 보이지 않고 <b>둘레가 지저분하게 어두워진 것</b>처럼 보입니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="고도를 코드로 옮기는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
  code_lede="단마다 그림자를 <b>두 겹</b>으로 둡니다. 가까운 그림자는 가장자리를 또렷하게 하고, 먼 그림자는 높이를 나타냅니다.",
  code='''<span class="t">:root</span> {
  <span class="a">--e1</span>: <span class="s">0 1px 2px rgba(20,22,26,.06), 0 1px 1px rgba(20,22,26,.04)</span>;
  <span class="a">--e2</span>: <span class="s">0 4px 12px rgba(20,22,26,.08), 0 1px 3px rgba(20,22,26,.06)</span>;
  <span class="a">--e3</span>: <span class="s">0 10px 24px rgba(20,22,26,.12), 0 3px 8px rgba(20,22,26,.08)</span>;
}

<span class="t">.card</span>     { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e1</span>); }
<span class="t">.popover</span>  { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e2</span>); }
<span class="t">.modal</span>    { <span class="a">box-shadow</span>: <span class="t">var</span>(<span class="a">--e3</span>); }

<span class="c">/* 어두운 모드에서는 그림자가 보이지 않으니 면을 밝혀 높이를 낸다 */</span>
<span class="t">:root[data-theme="dark"]</span> {
  <span class="a">--e1</span>: none; <span class="a">--e2</span>: none; <span class="a">--e3</span>: none;
  <span class="a">--surface-1</span>: <span class="s">#1c2029</span>; <span class="a">--surface-2</span>: <span class="s">#232834</span>;
}''',
  keys=kbd([
    ("단은 네댓 개만 두기", "0·1·2·3·4 다섯 단이면 충분합니다. 여섯 단을 넘으면 단끼리 구별되지 않습니다"),
    ("높은 단일수록 거리와 번짐을 키우기", "진하기는 거의 그대로 두고, 높은 단일수록 그림자를 <b>멀리, 흐리게</b> 둡니다"),
    ("가로 치우침은 0으로 두기", "빛이 바로 위에 있다고 정해 두면 화면 전체의 그림자 방향이 일관됩니다"),
    ("검정 대신 어두운 바탕색 쓰기", "<code>rgba(0,0,0,.2)</code> 같은 검정보다 바탕색 계열의 어두운 색이 덜 탁해 보입니다"),
    ("어두운 모드에서는 면 색으로 높이 나타내기", "그림자를 <code>none</code>으로 두고 <b>면 색을 한 단 밝힙니다</b>"),
    ("부품마다 쓸 단을 정해 두기", "'카드는 1단, 팝오버는 2단'처럼 정해 두면 부품을 만들 때마다 단을 고르지 않아도 됩니다"),
  ]),
  backend=rows([
    ("로그 레벨처럼 순서가 있는 열거형", "고도는 DEBUG·INFO·WARN처럼 <b>순서가 있는 몇 개의 값</b>입니다. 단과 단 사이에 중간값을 만들고 싶어진다면 단을 잘못 설계했다는 뜻입니다."),
    ("그림자가 스크롤 성능에 주는 영향", "브라우저는 화면을 그릴 때마다 그림자를 계산하기 때문에, 긴 목록의 <b>줄마다</b> 큰 그림자를 넣으면 스크롤이 눈에 띄게 끊깁니다. 그래서 목록 줄은 테두리로 나눕니다."),
    ("캡처하거나 인쇄할 때의 그림자", "PDF로 뽑거나 메일에 넣는 화면에서는 그림자가 <b>회색 띠</b>로 찍히는 일이 있으므로, 인쇄용 스타일에서는 그림자를 꺼 둡니다."),
    ("고도와 z-index를 한 표에 정의하기", "눈에 보이는 높이와 실제로 쌓이는 순서가 어긋나면 '위에 있는 것처럼 보이는데 클릭은 아래 요소가 받는' 버그가 생깁니다. 그래서 두 값을 <b>한 표에 함께</b> 적어 둡니다."),
  ]),
  plat_lede="안드로이드는 고도를 <b>물리적인 높이</b>로 다루는 반면, iOS와 웹에서는 그림자 값을 직접 정합니다.",
  plats=plats([
    ("웹", "CSS box-shadow",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--shadow-sm<br>--shadow-md<br>--shadow-lg</div>''',
     "정해진 규격이 없어서 팀마다 값이 다릅니다. 요즘은 그림자를 두 겹 이상 겹쳐 만드는 방식을 많이 씁니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.shadow(radius:)<br>.ultraThinMaterial</div>''',
     "그림자를 <b>아껴서</b> 씁니다. 떠 있는 느낌은 그림자보다 뒤를 반투명하게 흐리는 <b>머티리얼</b>로 내는 일이 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">elevation = 6.dp<br>tonalElevation</div>''',
     "고도를 <b>dp 높이</b>로 적으면 그림자는 OS가 계산해서 그립니다. M3는 그림자 대신 면의 색을 밝혀 높이를 나타내는 <b>색조 고도</b>를 권합니다."),
  ]),
  plat_note="안드로이드에서 <b>고도는 숫자 하나</b>(6dp)이고, 그림자는 그 숫자에 따라 저절로 그려집니다. 그래서 웹에서 쓰던 그림자 값을 그대로 건네면 안드로이드로 옮길 방법이 없습니다. \"그림자를 이렇게 해 주세요\" 대신 <b>\"이건 몇 단인가\"</b>로 이야기하면 세 플랫폼이 같은 기준으로 맞출 수 있습니다.",
  siblings=siblings("elevation"),
  related='''        <li><a href="../items/popover.html"><b>팝오버</b><em>6부</em></a></li>
        <li><a href="../items/modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="card.html"><b>카드</b><em>5부</em></a></li>
        <li><a href="radius.html"><b>모서리</b><em>2부</em></a></li>''',
)
