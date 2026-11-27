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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">보이는 아이콘 — 24px 여도 된다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">눌리는 넓이 — 44 × 44px 이상</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">가운데 맞춤 — 아이콘은 그대로 두고 여백만 키운다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이웃과의 간격 8px — 원이 안 겹치게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">화면 가장자리 16px — 쓸기 제스처와 안 다투게</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">손가락 끝 약 9mm — 화면에서 44px 남짓</div>
                </div>
              </div>'''

D = dict(
  slug="touchtarget", ko="터치 타깃", en="Touch target",
  desc="누를 수 있는 넓이. 보이는 크기와 눌리는 넓이를 따로 두는 법, 간격, 가장자리.",
  lede="<b>누를 수 있는 넓이.</b> 보이는 크기와 같을 필요가 없고, 대개 같으면 안 됩니다.",
  axes_lede="PC와 폰은 다른 기계가 아니라 <b>다른 전제</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>점선 원이 <b>손가락 끝이 닿는 넓이</b>(약 9mm ≈ 44px)입니다. 네모가 원보다 작으면
          옆을 누르게 됩니다.<br>
          <b>보이는 크기는 두고 누를 넓이만 키우기</b>를 켜 보세요 — 아이콘은 그대로 24px 인데
          눌리는 범위만 44px 이 됩니다. <b>디자인을 안 바꾸고</b> 고치는 방법입니다.
          아래쪽에서는 크기만큼 <b>간격</b>도 중요하다는 것을 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "터치 타깃, 누를 수 있는 넓이, 터치 영역"),
    ("영어", "touch target, hit area, tap target, hit slop"),
    ("같이 쓰는 말",
     "눌리는 범위를 보이는 것보다 넓히는 것을 <b>히트 슬롭</b>(hit slop)·<b>히트 영역 확장</b>이라 합니다. "
     "WCAG 에서는 <b>타깃 크기</b>(target size) 기준으로 나오고, "
     "iOS 는 <b>44pt</b>, 안드로이드는 <b>48dp</b>를 최소로 적어 두었습니다."),
    ("자주 잘못 부름",
     "<b>버튼 크기</b> — 버튼이 커 보일 필요는 없습니다. <b>눌리는 넓이만</b> 넓으면 됩니다.<br>"
     "<b>패딩</b> — 패딩은 수단 가운데 하나입니다. <code>::before</code>로 넓히는 방법도 있습니다.<br>"
     "<b>아이콘 크기</b> — 아이콘은 <b>보이는 크기</b>입니다. 둘을 같은 값으로 묶으면 화면이 둔해집니다."),
  ]),
  axes=ax("터치 타깃"),
  oneline="<b>보이는 크기와 눌리는 넓이를 따로 두세요.</b> 아이콘 24px, 눌리는 넓이 44px — 이 한 줄이 거의 모든 경우를 해결합니다.",
  s4_title="크기별로", s4_hint="원 안에 네모가 들어가나",
  states=states([
    (tgt(20, 20, "보이는 20 · 눌리는 20 ✕", True), "20px", "<b>옆이 눌린다.</b> 가장 흔한 사고"),
    (tgt(24, 24, "보이는 24 · 눌리는 24 ✕", True), "24px", "PC 에서는 되지만 <b>손가락으로는 안 된다</b>"),
    (tgt(24, 44, "보이는 24 · 눌리는 44 ✓"), "24 + 여백", "<b>이게 정답이다.</b> 아이콘은 그대로"),
    (tgt(44, 44, "보이는 44 · 눌리는 44 ✓"), "44px", "iOS 최소. <b>버튼이 커 보인다</b>"),
    (tgt(48, 48, "보이는 48 · 눌리는 48 ✓"), "48px", "안드로이드 최소. 주 동작 버튼에 맞는다"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:5px;justify-items:center">
                <div style="display:flex">
                  <span style="position:relative;width:44px;height:44px;display:grid;place-items:center">
                    <span style="position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:2px dashed var(--danger)"></span>
                    <span style="width:26px;height:26px;border-radius:5px;background:var(--accent)"></span></span>
                  <span style="position:relative;width:44px;height:44px;display:grid;place-items:center">
                    <span style="position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:2px dashed var(--danger)"></span>
                    <span style="width:26px;height:26px;border-radius:5px;background:var(--accent)"></span></span>
                </div>
                <span style="font-family:var(--mono);font-size:9px;color:var(--danger)">간격 0 — 원이 겹친다</span>
              </div>''',
     "붙여 놓으면", "크기가 맞아도 <b>가운데를 누르면</b> 어느 쪽인지 모른다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("보이는 것", "아이콘 24px", "작아도 된다. <b>작아야 화면이 깔끔</b>하다"),
    ("눌리는 넓이", "44 × 44px", "투명한 여백으로 넓힌다. <b>눈에는 안 보인다</b>"),
    ("가운데 맞춤", "place-items: center", "아이콘을 키우지 말고 <b>상자를 키운다</b>"),
    ("이웃과의 간격", "8px 이상", "붙여 두면 가운데를 누를 때 <b>어느 쪽인지 모른다</b>"),
    ("가장자리", "16px 안쪽", "너무 붙으면 <b>OS 의 쓸기 제스처</b>와 다툰다"),
    ("기준", "약 9mm", "손가락 끝의 평균. 화면에서 44~48px 남짓이다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>WCAG 2.2 의 기준(24 × 24px)과 OS 기준(44~48px)이 다릅니다.</b>
          24px 은 '법적 최소'이고 48px 은 '쓸 만한 크기'입니다.
          게다가 WCAG 쪽은 <b>간격으로 대신할 수</b> 있다고 적어 두었습니다 —
          24px 짜리라도 둘레에 충분한 빈틈이 있으면 통과입니다.
          실무에서는 <b>44px 을 기본으로 잡고</b> 빽빽한 표 안의 아이콘만 예외로 두는 쪽이 간단합니다.</p>''',
  do=ul([
    "<b>손가락으로 누르는 모든 것</b> — 아이콘 버튼, 닫기 ✕, 체크박스",
    "표나 목록 안의 작은 버튼 — <b>가장 자주 빠진다</b>",
    "줄 전체를 누르게 할 수 있으면 <b>줄을 통째로</b>",
  ]),
  dont=ul([
    "아이콘을 키워서 해결하기 — 화면이 <b>둔해진다</b>",
    "44px 짜리를 <b>딱 붙여</b> 늘어놓기",
    "화면 <b>맨 가장자리</b>에 붙이기 — 쓸기 제스처와 다툰다",
    "PC 에서만 재 보기 — 마우스는 1px 도 정확히 누른다",
  ]),
  instead='누를 것이 많으면 <a href="../items/listitem.html">리스트 아이템</a>처럼 줄 전체를 누르게, 숨겨도 되면 <a href="../items/popover.html">메뉴</a>로 모으기.',
  cases=cases([
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                <div style="display:flex;align-items:center;gap:6px;padding:9px 8px;font-size:10px;background:var(--accent-soft)">
                  <span style="flex:1">모란상회</span><span style="color:var(--fg-muted)">›</span></div>
              </div>''',
     "줄 전체를 누르게", "가장 쉬운 해법. <b>44px 이 저절로</b> 넘는다"),
    ('''              <div style="width:100%;max-width:152px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>.icon-btn::before {</span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">content: ""; position: absolute;</span></span>
                <span>&nbsp;&nbsp;<span style="color:var(--accent)">inset: -10px;</span></span>
                <span>}</span>
              </div>''',
     "배치를 안 건드리고", "<code>::before</code>로 범위만 넓힌다. <b>간격은 그대로</b>"),
    ('''              <div style="width:100%;max-width:152px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:flex;gap:10px;justify-content:flex-end">
                <span style="width:30px;height:30px;border-radius:5px;background:var(--bg);display:grid;place-items:center;font-size:11px">✎</span>
                <span style="width:30px;height:30px;border-radius:5px;background:var(--bg);display:grid;place-items:center;font-size:11px">🗑</span>
              </div>''',
     "표 안의 아이콘", "<b>가장 자주 빠지는 자리.</b> 간격을 넉넉히 둔다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 넓이의 계약서",
  code_lede="보이는 크기는 두고 <b>상자만</b> 키웁니다.",
  code='''.icon-btn {
  <span class="a">min-width</span>: <span class="a">44px</span>; <span class="a">min-height</span>: <span class="a">44px</span>;   <span class="c">/* 눌리는 넓이 */</span>
  <span class="a">display</span>: grid; <span class="a">place-items</span>: center;
  <span class="a">padding</span>: <span class="a">0</span>; <span class="a">border</span>: <span class="a">0</span>; <span class="a">background</span>: none;
}
.icon-btn <span class="t">svg</span> { <span class="a">width</span>: <span class="a">24px</span>; <span class="a">height</span>: <span class="a">24px</span>; }   <span class="c">/* 보이는 크기 */</span>

<span class="c">/* 배치를 못 건드릴 때 — 범위만 넓힌다 */</span>
.tight-btn { <span class="a">position</span>: relative; }
.tight-btn::before { <span class="a">content</span>: <span class="s">""</span>; <span class="a">position</span>: absolute; <span class="a">inset</span>: <span class="a">-10px</span>; }

<span class="c">/* 손가락 기기에서만 키우고 싶다면 */</span>
@media (pointer: coarse) { .icon-btn { <span class="a">min-width</span>: <span class="a">48px</span>; <span class="a">min-height</span>: <span class="a">48px</span>; } }''',
  keys=kbd([
    ("<code>min-width</code>·<code>min-height</code>", "<code>width</code>로 박으면 글자가 길어질 때 넘친다"),
    ("<code>&lt;button&gt;</code>에 <code>aria-label</code>", "아이콘만 있으면 <b>이름이 없다</b>. <a href=\"../items/name.html\">이름 붙이기</a>로"),
    ("초점 테두리도 같이 커진다", "상자를 키우면 <a href=\"../items/focus.html\">포커스</a> 테두리가 아이콘에서 멀어진다. <code>outline-offset</code>으로 당긴다"),
    ("<code>@media (pointer: coarse)</code>", "손가락 기기에서만 키울 수 있다. <b>PC 는 작게 둬도 된다</b>"),
    ("<code>::before</code>로 넓힐 때", "부모에 <code>position: relative</code>가 있어야 하고, <code>overflow:hidden</code>이 걸리면 잘린다"),
    ("<kbd>Tab</kbd> 순서", "범위를 넓혀도 <b>순서는 그대로</b>다. 눈에 보이는 차례와 맞는지 따로 본다"),
  ]),
  backend=rows([
    ("잘못 눌린 요청", "작은 버튼은 <b>옆 것이 눌립니다.</b> '지우려다 보냈다' 같은 민원은 서버 로그로는 정상 요청으로 보입니다."),
    ("되돌릴 길", "실수로 눌리기 쉬운 동작일수록 <a href=\"../items/toast.html\">되돌리기</a>가 필요합니다."),
    ("두 번 눌림", "손가락은 미끄러져 두 번 눌리기 쉽습니다. <b>같은 요청을 한 번만</b> 처리하는 장치가 필요합니다."),
  ]),
  plat_lede="숫자만 다릅니다 — <b>44 · 48 · 24</b>.",
  plats=plats([
    ("웹", "WCAG 2.2",
     tgt(24, 44, "24 보이고 44 눌린다", False, "110px"),
     "최소 <b>24 × 24px</b>이고 간격으로 대신할 수 있습니다. 실무 기준으로는 느슨해 44px 을 쓰는 편이 많습니다."),
    ("iOS", "44 × 44pt",
     '''              <div class="phone" role="img" aria-label="iOS 터치 타깃 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:22px;height:22px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:6px;top:30px;width:22px;height:22px;border:1px dashed var(--danger);border-radius:4px;transform:scale(2)"></span></div></div>''',
     "HIG 에 <b>44 × 44pt</b>로 못 박혀 있습니다. 시스템 부품은 처음부터 그 크기입니다."),
    ("안드로이드", "48 × 48dp",
     '''              <div class="phone" role="img" aria-label="Material 터치 타깃 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:6px;top:30px;width:24px;height:24px;border-radius:4px;background:var(--accent)"></div>
                <span style="position:absolute;left:4px;top:28px;width:28px;height:28px;border:1px dashed var(--danger);border-radius:4px"></span></div></div>''',
     "<b>48 × 48dp</b>. 아이콘은 24dp 로 두고 <b>둘레에 12dp 씩</b> 여백을 주라고 그림까지 그려 두었습니다."),
  ]),
  plat_note="\"폰에서 버튼이 잘 안 눌려요\"의 거의 전부가 이것입니다. 그런데 <b>디자인 시안에서는 안 보입니다</b> — 눌리는 넓이는 투명하기 때문입니다. 시안을 받을 때 '이 아이콘의 눌리는 넓이는 몇 px 입니까'를 한 번 묻고, 44px 을 기본값으로 적어 두면 나중에 다시 안 돌아옵니다.",
  siblings=siblings("touchtarget"),
  related='''        <li><a href="../items/focus.html"><b>포커스</b><em>12부</em></a></li>
        <li><a href="../items/name.html"><b>이름 붙이기</b><em>12부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/safearea.html"><b>세이프 에어리어</b><em>1부</em></a></li>''',
)
