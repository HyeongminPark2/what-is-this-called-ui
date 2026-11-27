# -*- coding: utf-8 -*-
from ax11 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def tgt(seen, hit, note, warn=False, w="152px"):
    pad = max((hit - seen) // 2, 0)
    ring = ('<span style="position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;'
            'border-radius:50%;border:2px dashed var(--danger)"></span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:center">'
            '<div style="position:relative;width:' + str(max(hit, 48)) + 'px;height:' + str(max(hit, 48)) + 'px;display:grid;place-items:center">'
            + ring +
            '<span style="width:' + str(seen) + 'px;height:' + str(seen) + 'px;border-radius:5px;background:var(--accent);'
            'color:#fff;display:grid;place-items:center;font-size:' + str(max(seen // 2, 8)) + 'px">✕</span></div>'
            '<span style="font-family:var(--mono);font-size:9px;color:' + ('var(--danger)' if warn else 'var(--fg-muted)') + '">' + note + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">보이는 아이콘은 24px여도 됨</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">눌리는 넓이는 44 × 44px 이상</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">아이콘은 가운데 그대로 두고 여백만 키움</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이웃과 8px 띄워 원이 겹치지 않게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가장자리에서 16px 띄워 쓸기 제스처를 피함</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">손가락 끝 약 9mm는 화면에서 44px 남짓</div>
                </div>
              </div>'''

D = dict(
  slug="touchtarget", ko="터치 타깃", en="Touch target",
  desc="손가락으로 누를 수 있는 넓이와, 보이는 크기와 눌리는 넓이를 따로 두는 법, 이웃과의 간격, 화면 가장자리 처리를 보여 주는 항목입니다.",
  lede="터치 타깃은 화면에서 <b>손가락으로 누를 수 있는 넓이</b>입니다. 눈에 보이는 크기와 같을 필요가 없고, 작은 아이콘이라면 대개 보이는 크기보다 넓게 잡아야 합니다.",
  axes_lede="PC와 폰은 기계보다 <b>쓰는 전제</b>가 다릅니다. 아래 네 가지로 두 환경을 견줍니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>점선 원은 <b>손가락 끝이 닿는 넓이</b>(약 9mm ≈ 44px)입니다. 네모가 원보다 작으면
          손가락이 네모 바깥까지 닿아서 옆의 것을 누르게 됩니다.<br>
          <b>보이는 크기는 두고 누를 넓이만 키우기</b>를 켜 보세요. 아이콘은 그대로 24px인데
          눌리는 범위만 44px로 넓어지므로, <b>디자인을 바꾸지 않고</b> 고칠 수 있습니다.
          아래쪽 예에서는 크기만큼 <b>간격</b>도 중요하다는 것을 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "터치 타깃, 누를 수 있는 넓이, 터치 영역"),
    ("영어", "touch target, hit area, tap target, hit slop"),
    ("같이 쓰는 말",
     "눌리는 범위를 보이는 크기보다 넓히는 것을 <b>히트 슬롭</b>(hit slop) 또는 <b>히트 영역 확장</b>이라고 합니다. "
     "WCAG에서는 <b>타깃 크기</b>(target size)라는 기준으로 다루고, "
     "iOS는 <b>44pt</b>, 안드로이드는 <b>48dp</b>를 최소 크기로 적어 두었습니다."),
    ("자주 잘못 부르는 이름",
     "<b>버튼 크기</b> — 터치 타깃을 넓히려고 버튼이 커 보일 필요는 없습니다. <b>눌리는 넓이만</b> 넓으면 됩니다.<br>"
     "<b>패딩</b> — 패딩은 눌리는 넓이를 키우는 여러 방법 가운데 하나이고, <code>::before</code>로 넓히는 방법도 있습니다.<br>"
     "<b>아이콘 크기</b> — 아이콘 크기는 <b>보이는 크기</b>를 가리킵니다. 아이콘 크기와 눌리는 넓이를 같은 값으로 묶으면 아이콘이 커져서 화면이 둔해 보입니다."),
  ]),
  axes=ax("터치 타깃"),
  oneline="<b>보이는 크기와 눌리는 넓이를 따로 두세요.</b> 아이콘은 24px로 두고 눌리는 넓이만 44px로 잡으면, 작은 버튼이 잘 안 눌리는 문제는 대부분 해결됩니다.",
  s4_title="크기별로 비교한 누르는 넓이", s4_hint="손가락 원보다 네모가 넓은지 비교",
  do_title="터치 타깃을 챙겨야 하는 경우",
  dont_title="터치 타깃을 잘못 다루는 경우",
  instead_title="누를 것이 많아 넓이를 확보하기 어려운 경우",
  states=states([
    (tgt(20, 20, "보이는 20 · 눌리는 20 ✕", True), "20px짜리 버튼", "<b>옆의 것이 눌립니다.</b> 가장 흔하게 일어나는 실수입니다"),
    (tgt(24, 24, "보이는 24 · 눌리는 24 ✕", True), "24px짜리 버튼", "마우스로는 누를 수 있지만 <b>손가락으로는 정확히 누르기 어렵습니다</b>"),
    (tgt(24, 44, "보이는 24 · 눌리는 44 ✓"), "24px에 여백을 더한 버튼", "<b>권장하는 방식입니다.</b> 아이콘은 그대로 두고 여백으로 넓이를 채웁니다"),
    (tgt(44, 44, "보이는 44 · 눌리는 44 ✓"), "44px짜리 버튼", "iOS의 최소 크기입니다. 보이는 크기까지 키우면 <b>버튼이 커 보입니다</b>"),
    (tgt(48, 48, "보이는 48 · 눌리는 48 ✓"), "48px짜리 버튼", "안드로이드의 최소 크기입니다. 주 동작 버튼에 알맞습니다"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px;justify-items:center">
                <div style="display:flex">
                  <span style="position:relative;width:44px;height:44px;display:grid;place-items:center">
                    <span style="position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:2px dashed var(--danger)"></span>
                    <span style="width:26px;height:26px;border-radius:5px;background:var(--accent)"></span></span>
                  <span style="position:relative;width:44px;height:44px;display:grid;place-items:center">
                    <span style="position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:2px dashed var(--danger)"></span>
                    <span style="width:26px;height:26px;border-radius:5px;background:var(--accent)"></span></span>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--danger)">간격이 0이라 원이 겹침</span>
              </div>''',
     "버튼을 간격 없이 붙였을 때", "크기가 충분해도 둘 사이 <b>가운데를 누르면</b> 어느 쪽이 눌릴지 알 수 없습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보이는 아이콘", "아이콘 24px", "작아도 됩니다. 아이콘이 <b>작아야 화면이 깔끔</b>합니다"),
    ("눌리는 넓이", "44 × 44px", "투명한 여백으로 넓히기 때문에 <b>눈에는 보이지 않습니다</b>"),
    ("가운데 맞춤", "place-items: center", "아이콘을 키우지 않고 <b>아이콘을 감싼 상자를 키운</b> 뒤 아이콘을 가운데에 놓습니다"),
    ("이웃과의 간격", "8px 이상", "붙여 두면 둘 사이 가운데를 눌렀을 때 <b>어느 쪽이 눌릴지 알 수 없습니다</b>"),
    ("가장자리", "16px 안쪽", "가장자리에 너무 붙으면 누르려던 동작이 <b>OS의 쓸기 제스처</b>로 처리될 수 있습니다"),
    ("손가락 끝 너비", "약 9mm", "손가락 끝의 평균 너비로, 화면에서는 44~48px 남짓입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>WCAG 2.2의 기준(24 × 24px)과 OS의 기준(44~48px)은 서로 다릅니다.</b>
          24px은 접근성 기준을 통과하기 위한 최소값이고, 48px은 실제로 쓰기 편한 크기입니다.
          게다가 WCAG는 크기가 모자라면 <b>간격으로 대신할 수</b> 있다고 적어 두었기 때문에,
          24px보다 작은 버튼이라도 둘레에 충분한 빈틈이 있으면 기준을 통과합니다.
          실무에서는 <b>44px을 기본으로 잡고</b> 빽빽한 표 안의 아이콘만 예외로 두는 편이 간단합니다.</p>''',
  do=ul([
    "아이콘 버튼, 닫기 ✕, 체크박스처럼 <b>손가락으로 누르는 모든 것</b>을 만들 때",
    "표나 목록 안에 작은 버튼을 둘 때. 터치 타깃을 챙기는 일이 <b>가장 자주 빠지는</b> 자리입니다",
    "줄 전체를 누르게 할 수 있을 때. 이때는 <b>줄을 통째로</b> 터치 타깃으로 삼습니다",
  ]),
  dont=ul([
    "아이콘 자체를 키워서 해결하려 할 때. 화면이 <b>둔해 보입니다</b>",
    "44px짜리 버튼을 간격 없이 <b>딱 붙여</b> 늘어놓을 때",
    "버튼을 화면 <b>맨 가장자리</b>에 붙일 때. 누르려던 동작이 쓸기 제스처로 처리될 수 있습니다",
    "PC에서만 눌러 보고 확인할 때. 마우스로는 1px짜리도 정확히 누를 수 있어서 문제가 드러나지 않습니다",
  ]),
  instead='누를 것이 많으면 <a href="../items/listitem.html">리스트 아이템</a>처럼 줄 전체를 누르게 하고, 숨겨도 되는 것은 <a href="../items/popover.html">메뉴</a>로 모읍니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="display:flex;align-items:center;gap:6px;padding:9px 8px;font-size:10px;background:var(--accent-soft)">
                  <span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">›</span></div>
              </div>''',
     "줄 전체를 누르게 하기", "가장 쉬운 방법입니다. 줄 높이만으로 <b>44px을 저절로</b> 넘습니다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.icon-btn::before {</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">content: ""; position: absolute;</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">inset: -10px;</span></span>
                <span>}</span>
              </div>''',
     "배치를 건드리지 않고 넓히기", "<code>::before</code>로 눌리는 범위만 넓히기 때문에 <b>간격은 그대로</b>입니다"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:flex;gap:10px;justify-content:flex-end">
                <span style="width:30px;height:30px;border-radius:5px;background:var(--bg);display:grid;place-items:center;font-size:11px">✎</span>
                <span style="width:30px;height:30px;border-radius:5px;background:var(--bg);display:grid;place-items:center;font-size:11px">🗑</span>
              </div>''',
     "표 안의 아이콘 버튼 챙기기", "터치 타깃을 <b>가장 자주 빠뜨리는 자리입니다.</b> 아이콘 사이 간격을 넉넉히 둡니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="빠뜨리기 쉬운 설정까지 담은 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 까닭</th>",
  code_lede="아이콘의 보이는 크기는 그대로 두고 <b>아이콘을 감싼 상자만</b> 키웁니다.",
  code='''.icon-btn {
  <span class="a">min-width</span>: <span class="a">44px</span>; <span class="a">min-height</span>: <span class="a">44px</span>;   <span class="c">/* 눌리는 넓이 */</span>
  <span class="a">display</span>: grid; <span class="a">place-items</span>: center;
  <span class="a">padding</span>: <span class="a">0</span>; <span class="a">border</span>: <span class="a">0</span>; <span class="a">background</span>: none;
}
.icon-btn <span class="t">svg</span> { <span class="a">width</span>: <span class="a">24px</span>; <span class="a">height</span>: <span class="a">24px</span>; }   <span class="c">/* 보이는 크기 */</span>

<span class="c">/* 배치를 못 건드릴 때는 범위만 넓힌다 */</span>
.tight-btn { <span class="a">position</span>: relative; }
.tight-btn::before { <span class="a">content</span>: <span class="s">""</span>; <span class="a">position</span>: absolute; <span class="a">inset</span>: <span class="a">-10px</span>; }

<span class="c">/* 손가락 기기에서만 키우고 싶다면 */</span>
@media (pointer: coarse) { .icon-btn { <span class="a">min-width</span>: <span class="a">48px</span>; <span class="a">min-height</span>: <span class="a">48px</span>; } }''',
  keys=kbd([
    ("<code>min-width</code>·<code>min-height</code>로 크기 잡기", "<code>width</code>로 크기를 고정하면 글자가 길어질 때 상자 밖으로 넘칩니다"),
    ("<code>&lt;button&gt;</code>에 <code>aria-label</code> 달기", "아이콘만 있는 버튼은 스크린 리더가 읽을 <b>이름이 없습니다</b>. <a href=\"../items/name.html\">이름 붙이기</a>로 이름을 달아 줍니다"),
    ("포커스 테두리 위치 맞추기", "상자를 키우면 <a href=\"../items/focus.html\">포커스</a> 테두리가 아이콘에서 멀어지므로 <code>outline-offset</code>으로 안쪽으로 당깁니다"),
    ("<code>@media (pointer: coarse)</code>로 가르기", "손가락으로 쓰는 기기에서만 크기를 키울 수 있습니다. <b>PC에서는 작게 둬도 됩니다</b>"),
    ("<code>::before</code>로 넓힐 때", "부모에 <code>position: relative</code>가 있어야 하고, <code>overflow:hidden</code>이 걸려 있으면 넓힌 범위가 잘립니다"),
    ("<kbd>Tab</kbd> 순서 확인하기", "눌리는 범위를 넓혀도 <b>Tab 순서는 바뀌지 않습니다</b>. 눈에 보이는 차례와 맞는지는 따로 확인합니다"),
  ]),
  backend=rows([
    ("잘못 눌려 들어온 요청", "버튼이 작으면 <b>옆의 것이 눌립니다.</b> '지우려다 보내 버렸다' 같은 민원이 들어와도, 서버 로그에는 정상 요청으로만 남습니다."),
    ("실수를 되돌리는 기능", "실수로 눌리기 쉬운 동작일수록 <a href=\"../items/toast.html\">되돌리기</a>를 마련해 두어야 합니다."),
    ("두 번 눌린 요청 막기", "손가락이 미끄러지면 버튼이 두 번 눌리기 쉽기 때문에, 서버에서 <b>같은 요청을 한 번만</b> 처리하도록 막아 두어야 합니다."),
  ]),
  plat_lede="원리는 같고 최소 크기를 적은 숫자만 <b>44 · 48 · 24</b>로 다릅니다.",
  plats=plats([
    ("웹", "WCAG 2.2",
     tgt(24, 44, "24로 보이고 44로 눌림", False, "110px"),
     "최소 <b>24 × 24px</b>이고, 크기가 모자라면 간격으로 대신할 수 있습니다. 이 값은 실무 기준으로 쓰기에는 느슨해서 44px을 쓰는 경우가 많습니다."),
    ("iOS", "44 × 44pt",
     '''              <div class="phone" role="img" aria-label="iOS 터치 타깃 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:22px;height:22px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:6px;top:30px;width:22px;height:22px;border:1px dashed var(--danger);border-radius:4px;transform:scale(2)"></span></div></div>''',
     "HIG에 <b>44 × 44pt</b>로 정해져 있고, 시스템이 제공하는 부품은 처음부터 그 크기로 만들어져 있습니다."),
    ("안드로이드", "48 × 48dp",
     '''              <div class="phone" role="img" aria-label="Material 터치 타깃 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:24px;height:24px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:4px;top:28px;width:28px;height:28px;border:1px dashed var(--danger);border-radius:4px"></span></div></div>''',
     "최소 크기는 <b>48 × 48dp</b>입니다. 아이콘은 24dp로 두고 <b>둘레에 12dp씩</b> 여백을 주라고 그림으로 설명해 두었습니다."),
  ]),
  plat_note="\"폰에서 버튼이 잘 안 눌려요\"라는 문의는 대부분 터치 타깃이 좁아서 생깁니다. 그런데 눌리는 넓이는 투명해서 <b>디자인 시안에서는 보이지 않습니다</b>. 시안을 받을 때 '이 아이콘의 눌리는 넓이는 몇 px입니까'를 한 번 묻고 44px을 기본값으로 적어 두면, 같은 문제로 다시 고칠 일이 줄어듭니다.",
  siblings=siblings("touchtarget"),
  related='''        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
