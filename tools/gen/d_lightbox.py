# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양만 보고는 구별하기 어렵지만, 아래 네 가지를 따져 보면 어느 부품인지 가려낼 수 있습니다."

def lb(label, note="", ok=None, w="152px", nav=True, cnt="3 / 8", grid=False):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    if grid:
        cells = ''.join('<span style="aspect-ratio:4/3;border-radius:3px;background:var(--accent-soft)"></span>'
                        for _ in range(8))
        inner = ('<span style="display:grid;grid-template-columns:repeat(4,1fr);gap:3px;padding:6px">'
                 + cells + '</span>')
    else:
        inner = ('<span style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 55%, transparent)"></span>'
                 '<span style="position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);width:66%;'
                 'aspect-ratio:4/3;border-radius:4px;background:var(--accent-soft);display:grid;place-items:center;'
                 'font-size:7.5px;color:var(--accent)">영수증 3</span>'
                 '<span style="position:absolute;right:4px;top:4px;width:12px;height:12px;border-radius:999px;'
                 'background:rgba(0,0,0,.4);color:#fff;font-size:7px;display:grid;place-items:center">✕</span>'
                 + ('<span style="position:absolute;left:4px;top:48%;transform:translateY(-50%);width:12px;height:12px;'
                    'border-radius:999px;background:rgba(0,0,0,.4);color:#fff;font-size:7px;display:grid;place-items:center">‹</span>'
                    '<span style="position:absolute;right:4px;top:48%;transform:translateY(-50%);width:12px;height:12px;'
                    'border-radius:999px;background:rgba(0,0,0,.4);color:#fff;font-size:7px;display:grid;place-items:center">›</span>'
                    if nav else '')
                 + ('<span style="position:absolute;left:0;right:0;bottom:4px;text-align:center;color:#fff;font-size:6.5px">'
                    + cnt + '</span>' if cnt else ''))
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);overflow:hidden">' + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">어두운 가림막 — 그림에 눈이 가게</div>
                  <div class="pin-out" data-pin="2" style="color:var(--fg-muted)">닫기(✕) · ← → · 몇 번째인지</div>
                  <div class="pin-out" data-pin="3" style="color:var(--accent)">닫으면 눌렀던 칸으로 초점이 돌아간다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--accent)">주소에 남긴다 — 링크로 보낼 수 있다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">Esc · 가림막 · ✕ — 닫는 길 셋</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">작은 그림을 억지로 늘리지 않는다</div>
                </div>
              </div>'''

D = dict(
  slug="lightbox", ko="라이트박스", en="Lightbox",
  desc="그림 하나를 크게 보는 동안 뒤 화면을 덮는 겹침 부품입니다. 닫은 뒤 초점 돌려주기와 주소에 남기기를 다룹니다.",
  lede="라이트박스는 그림 <b>하나를 크게 보는 동안</b> 뒤 화면을 덮는 부품입니다. 모달과 같은 규칙을 따르고, 여기에 그림을 <b>앞뒤로 넘기는 기능</b>이 더해집니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>그림을 눌러 크게 열어 보세요. ← →로 그림을 옮기고 Esc로 닫습니다.<br>
          라이트박스를 닫으면 <b>초점이 눌렀던 칸으로 돌아가야</b> 합니다. 그렇지 않으면 키보드 사용자의 초점이
          목록 맨 처음으로 가 버리기 때문입니다. 데모는 <b>닫은 뒤 초점이 어디에 있는지</b>를 재서 보여 줍니다.<br>
          열린 그림을 <b>주소에 남겨 두면</b> 그 그림을 링크로 보낼 수 있고 뒤로가기로도 닫을 수 있습니다.
          데모는 지금 주소도 함께 보여 줍니다.</p>
        </div>''',
  names=rows([
    ("한국어", "라이트박스, 사진 크게 보기, 이미지 뷰어"),
    ("영어", "lightbox, image viewer, photo viewer, gallery overlay"),
    ("같이 쓰는 말",
     "2005년 무렵에 나온 자바스크립트 라이브러리 이름에서 온 말입니다. "
     "여러 장을 넘겨 보는 형태는 <b>갤러리</b>(gallery), 아래에 작은 그림을 늘어놓은 띠는 "
     "<b>필름스트립</b>(filmstrip)이라고 부릅니다. "
     "작은 그림이 이어서 큰 그림으로 커지는 움직임은 <a href=\"sharedelement.html\">공유 요소 전환</a>이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>모달</b> — <a href=\"modal.html\">모달</a>은 더 넓은 말이고, 라이트박스는 그중 <b>그림을 보는 데만</b> 쓰는 모달입니다.<br>"
     "<b>캐러셀</b> — 캐러셀도 그림을 넘기지만, 화면 위에 <b>겹쳐 뜨지 않고</b> 화면 안의 제자리에서 넘깁니다.<br>"
     "<b>썸네일</b> — <a href=\"thumbnail.html\">썸네일</a>은 라이트박스를 열기 전 목록에 보이는 <b>작은 그림</b>을 가리킵니다."),
  ]),
  axes=axis_table("라이트박스"),
  oneline="<b>모달의 규칙을 그대로 지키세요.</b> 그림을 보여 주는 부품이라고 해서 초점 관리와 Esc 닫기, 주소에 남기기를 빼도 되는 것은 아닙니다.",
  states=states([
    (lb("", "목록 — 작은 그림들", True, "152px", True, "", True), "닫힘", "목록에 <b>작은 그림</b>만 보입니다"),
    (lb("", "뒤를 덮고 그림만 보인다", True), "열림", "<b>어두운 가림막</b>으로 뒤를 덮습니다"),
    (lb("", "앞뒤로 넘긴다", True, "152px", True, "3 / 8"), "여러 장", "<b>← →</b> 버튼과 몇 번째 그림인지를 보여 줍니다"),
    (lb("", "한 장뿐이면 화살표를 안 둔다", True, "152px", False, ""), "한 장", "<b>넘길 그림이 없으니</b> 화살표를 두지 않습니다"),
    (one(txt('<span style="display:block;font-size:8px;color:var(--fg-muted)">닫았다</span>'
             '<span style="display:block;font-size:8px;margin-top:2px">초점이 <b>눌렀던 칸</b>으로</span>'),
         "닫은 뒤", True, "", "152px"),
     "닫은 뒤", "눌렀던 칸으로 <b>초점을 돌려줍니다</b>"),
    (one(txt('<span style="display:block;font-size:7.5px;font-family:var(--mono)">/receipts?photo=3</span>'
             '<span style="display:block;font-size:8px;color:var(--fg-muted);margin-top:3px">링크로 보낼 수 있다</span>'),
         "주소", True, "뒤로가기로도 닫힌다", "152px"),
     "주소에 남김", "주소를 보내면 같은 그림을 <b>공유할 수 있습니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("가림막", "어둡게", "뒤 화면을 어둡게 덮어 <b>그림에 눈이 가게</b> 합니다"),
    ("조작", "✕ · ← → · 몇/몇", "마우스나 손가락으로도, 키보드로도 <b>모두</b> 다룰 수 있어야 합니다"),
    ("초점", "돌려주기", "닫으면 눌렀던 칸으로 초점을 돌려줍니다"),
    ("주소", "남기기", "주소에 남겨 두면 <b>링크로</b> 보낼 수 있습니다"),
    ("닫는 길", "셋", "Esc, 가림막, ✕ 세 가지로 닫을 수 있습니다"),
    ("크기", "원본까지만", "작은 그림을 원본보다 <b>억지로</b> 늘리지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          라이트박스는 <b>모달인데도 모달처럼 다루지 않는</b> 경우가 많은 부품입니다.
          그림을 보여 줄 뿐이라는 생각에 초점 가둠과 Esc 닫기, 초점 돌려주기를 빠뜨리기 쉽습니다.
          그런데 여덟 장짜리 목록에서 세 번째 그림을 열었다 닫았을 때 초점이 맨 앞으로 가 버리면,
          키보드 사용자는 원래 자리로 돌아가려고 <b>Tab을 다시 세 번</b> 눌러야 합니다.<br>
          반면 <b>주소에 남기기</b>는 들이는 품에 비해 얻는 것이 많습니다.
          그림을 링크로 보낼 수 있고, 폰에서는 <b>시스템 백</b>으로 닫히며,
          새로 고침해도 같은 그림이 열려 있습니다.</p>''',
  do=ul([
    "닫으면 <b>눌렀던 칸</b>으로 초점 돌려주기",
    "<b>주소에 남겨</b> 링크 공유와 뒤로가기 닫기가 되게 하기",
    "원본보다 <b>크게 늘리지</b> 않기",
  ]),
  dont=ul([
    "초점을 <b>가두지 않기</b>. Tab을 누르면 초점이 뒤 화면의 링크로 나갑니다",
    "Esc로 <b>닫히지 않게</b> 두기",
    "한 장뿐인데 <b>화살표</b> 두기",
    "그림 설명(<code>alt</code>)을 <b>빠뜨리기</b>",
  ]),
  instead='더 넓은 겹침은 <a href="modal.html">모달</a>, 작은 그림은 <a href="thumbnail.html">썸네일</a>, 이어 붙는 움직임은 <a href="sharedelement.html">공유 요소 전환</a>, 전체 화면이면 <a href="fullscreen.html">전체 화면 레이어</a>.',
  cases=cases([
    (lb("", "", True, "150px", True, "3 / 8"), "영수증 보기", "<b>여러 장</b>을 넘겨 봅니다"),
    (lb("", "", True, "150px", False, ""), "증빙 한 장", "한 장뿐이라 <b>화살표 없이</b> 보여 줍니다"),
    (lb("", "", True, "150px", True, "1 / 24", True), "사진첩", "목록에서 <b>골라 엽니다</b>"),
  ]),
  code_lede="<code>&lt;dialog&gt;</code>를 쓰면 초점 가둠과 Esc 닫기를 <b>따로 만들지 않아도</b> 됩니다.",
  code='''&lt;<span class="t">dialog</span> <span class="a">id</span>=<span class="s">"lb"</span> <span class="a">aria-label</span>=<span class="s">"영수증 3"</span>&gt;
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"/r/3.jpg"</span> <span class="a">alt</span>=<span class="s">"2026-11-12 모란상회 영수증"</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"prev"</span> <span class="a">aria-label</span>=<span class="s">"이전 그림"</span>&gt;‹&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"next"</span> <span class="a">aria-label</span>=<span class="s">"다음 그림"</span>&gt;›&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">button</span> <span class="a">id</span>=<span class="s">"close"</span> <span class="a">aria-label</span>=<span class="s">"닫기"</span>&gt;✕&lt;/<span class="t">button</span>&gt;
  &lt;<span class="t">p</span>&gt;3 / 8&lt;/<span class="t">p</span>&gt;
&lt;/<span class="t">dialog</span>&gt;

<span class="c">// 주소에 남기면 링크 공유와 뒤로가기 닫기가 따라온다</span>
<span class="t">function</span> open(i, fromBtn) {
  last = fromBtn;
  history.pushState({ photo: i }, <span class="s">''</span>, <span class="s">`?photo=${i + 1}`</span>);
  lb.showModal();                    <span class="c">// 초점 가둠 · Esc 가 따라온다</span>
}
lb.addEventListener(<span class="s">'close'</span>, () =&gt; last &amp;&amp; last.focus());   <span class="c">// 초점 돌려주기</span>''',
  keys=kbd([
    ("Esc", "라이트박스를 닫습니다. <code>&lt;dialog&gt;</code>를 쓰면 <b>저절로</b> 됩니다"),
    ("← →", "앞뒤 그림으로 넘깁니다. 이 키는 <b>직접</b> 붙여야 합니다"),
    ("Tab", "초점이 라이트박스 안에 <b>갇혀</b> 밖으로 나가지 않습니다"),
    ("초점", "열면 <b>닫기</b> 버튼으로, 닫으면 <b>눌렀던 칸</b>으로 옮깁니다"),
    ("<code>alt</code>", "크게 보는 그림에도 <b>설명이 필요</b>합니다"),
    ("확인하는 법", "세 번째 그림을 Tab으로 찾아 열었다 닫은 뒤 <b>초점이 어디에 있는지</b> 봅니다"),
  ]),
  backend=rows([
    ("큰 그림은 따로", "목록에는 작은 그림을, 라이트박스에는 <b>큰 그림</b>을 따로 내려 줍니다."),
    ("이웃 그림", "지금 보는 그림의 <b>앞뒤 한 장씩</b>을 미리 받아 두면 넘길 때 기다리지 않습니다."),
    ("원본 크기", "그림의 원본 <code>width</code>·<code>height</code>를 함께 내려 주면 원본보다 <b>억지로 늘리는 것</b>을 막을 수 있습니다."),
  ]),
  plat_lede="라이트박스는 <b>어느 플랫폼에서나 생김새가 같고</b>, 폰에서는 손짓 조작이 더해집니다.",
  plats=plats([
    ("웹", "&lt;dialog&gt; 또는 직접",
     lb("", "", True, "110px", True, "3 / 8"),
     "<code>&lt;dialog&gt;</code>를 쓰면 초점 가둠과 Esc 닫기가 함께 따라옵니다."),
    ("iOS", "QuickLook · 사진",
     '''              <div class="phone" role="img" aria-label="iOS 사진 보기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:#111"></div>
                <div style="position:absolute;left:5px;right:5px;top:30%;height:36%;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:0;right:0;bottom:5px;text-align:center;font-size:5px;color:#fff">3 / 8</div></div></div>''',
     "<b>아래로 쓸어</b> 닫는 손짓이 표준이고, 두 손가락을 벌려 확대합니다."),
    ("안드로이드", "전체 화면 뷰어",
     '''              <div class="phone" role="img" aria-label="안드로이드 사진 보기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;inset:0;background:#111"></div>
                <div style="position:absolute;left:5px;right:5px;top:30%;height:36%;border-radius:3px;background:var(--accent-soft)"></div>
                <div style="position:absolute;left:0;right:0;bottom:5px;text-align:center;font-size:5px;color:#fff">3 / 8</div></div></div>''',
     "사용자는 <b>시스템 백</b>으로 닫히기를 기본으로 기대합니다. 그래서 라이트박스를 열 때 방문 기록에 넣어 둡니다."),
  ]),
  plat_note="폰에서는 <b>아래로 쓸어 닫기</b>가 거의 표준이 되었습니다. 웹에도 붙여 둘 만하지만, <b>그 손짓만</b> 두면 PC에서 마우스나 키보드로는 닫을 수 없습니다. 안드로이드에서는 <b>시스템 백으로 닫히는 것</b>을 꼭 맞춰야 하는데, 열린 그림을 주소나 방문 기록에 넣어 두면 이 문제도 함께 해결됩니다.",
  siblings=siblings("lightbox"),
  related='''        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="thumbnail.html"><b>썸네일</b><em>5부</em></a></li>
        <li><a href="focustrap.html"><b>포커스 트랩</b><em>12부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
