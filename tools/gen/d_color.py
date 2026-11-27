# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def chip(c, t, sub=""):
    return ('              <div style="display:grid;gap:6px;justify-items:center">'
            '<span style="width:44px;height:44px;border-radius:10px;background:%s;border:1px solid rgba(0,0,0,.08);display:block"></span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">%s</span>%s</div>'
            ) % (c, t, '<span style="font-size:10px;color:var(--fg-faint)">%s</span>' % sub if sub else "")

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:14px 10px 14px 0">
                <div style="padding-left:26px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:13px 13px 14px">
                    <div style="padding-left:26px;display:grid;gap:11px">
                      <div class="pin-out" data-pin="2" style="font-size:13px;font-weight:700">정산 요청 #4821</div>
                      <div class="pin-out" data-pin="3" style="font-size:11.5px;color:var(--fg-muted)">11월 1일 ~ 11월 7일 · ₩1,284,000</div>
                      <div class="pin-out" data-pin="4" style="font-size:11.5px;color:var(--danger)">계좌 확인이 필요합니다</div>
                      <div class="pin-out" data-pin="5" style="display:inline-block;background:var(--accent);color:#fff;border-radius:7px;padding:6px 12px;font-size:11.5px;font-weight:700;justify-self:start">확정하기</div>
                      <div class="pin-out" data-pin="6" style="display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:99px;padding:3px 9px;font-size:10.5px;font-weight:700;justify-self:start">검토 중</div>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="color", ko="색 토큰", en="Color tokens · semantic color",
  desc="색을 #2f6df6 같은 값이 아니라 --accent 같은 쓰임으로 정해 두는 방법을 실물과 해부도로 보여주는 항목.",
  lede="색을 <b>값</b>이 아니라 <b>쓰임</b>으로 부르는 약속. 화면은 <code>#2f6df6</code>을 모르고 <code>--accent</code>만 압니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>1단은 색 이름표(<code>blue-500</code>), 2단은 쓰임표(<code>--accent</code>), 3단은 부품표(<code>button-bg</code>)입니다.
          <b>어두운 화면으로</b>를 켜면 2단의 <b>화살표만</b> 다른 색을 가리키게 바뀝니다 —
          1단의 색은 그대로이고 3단은 손대지 않았는데 버튼 색이 따라옵니다. 이것이 토큰을 쓰는 이유 전부입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "색 토큰, 시맨틱 색, 의미 색"),
    ("영어", "color token, semantic color, design token"),
    ("같이 쓰는 말",
     "<b>원시 토큰</b>(raw · primitive · global)은 <code>blue-500</code>처럼 색 그 자체이고, "
     "<b>시맨틱 토큰</b>(semantic · alias)은 <code>--accent</code>처럼 쓰임입니다. "
     "<b>컴포넌트 토큰</b>(component)은 <code>button-bg</code>처럼 부품 전용입니다. "
     "색을 가로로 늘어놓은 10단 묶음을 <b>색 램프</b>(ramp · scale)라고 합니다."),
    ("자주 잘못 부름",
     "<b>테마</b> — 테마는 토큰 <b>한 벌</b>을 가리키는 말이고, 토큰은 그 안의 항목 하나입니다.<br>"
     "<b>CSS 변수</b> — 변수는 담는 그릇이고 토큰은 그 안에 담긴 <b>약속</b>입니다. 변수를 쓴다고 토큰이 되지는 않습니다.<br>"
     "<b>팔레트</b> — 팔레트는 쓸 수 있는 색의 목록, 토큰은 어디에 쓸지까지 정한 것입니다."),
  ]),
  axes=ax("색 토큰"),
  oneline="색 토큰은 <b>'이 색을 어디에 쓰는가'</b>에 이름을 붙인 것입니다. 이름에 <code>blue</code>가 들어가면 아직 쓰임이 아닙니다.",
  s4_title="쓰임", s4_hint="색은 예쁘라고 고르는 것이 아니다",
  states=states([
    (chip("var(--accent)", "--accent", "강조 · 주요 동작"), "강조", "누를 것과 고른 것. <b>한 화면에 하나</b>가 원칙이다"),
    (chip("var(--danger)", "--danger", "되돌릴 수 없음"), "위험", "삭제·거절처럼 <b>되돌리기 어려운</b> 것에만"),
    (chip("var(--warn)", "--warn", "주의"), "주의", "막지는 않지만 알아 둘 것"),
    (chip("#1f8a4c", "--success", "끝남"), "성공", "확인됨·완료. 초록은 색맹에게 빨강과 겹치니 <b>글자도 함께</b>"),
    (chip("var(--fg-muted)", "--fg-muted", "보조 글"), "보조", "덜 중요한 글. 대비비 4.5:1 은 지켜야 한다"),
    (chip("var(--line)", "--line", "선 · 경계"), "경계", "칸을 나누는 선. 글자가 아니므로 3:1 이면 된다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("면", "surface", "카드의 바탕. 페이지 바탕(<code>--bg</code>)과 <b>한 단계 다르게</b> 둔다"),
    ("본문 글", "fg · text-primary", "가장 진한 글. 바탕과 대비비 <b>4.5:1</b> 이상"),
    ("보조 글", "fg-muted · text-secondary", "덜 중요한 글. 흐리게 하다 대비를 놓치기 가장 쉬운 자리"),
    ("위험 글", "danger · text-error", "빨강 하나로 알리지 않는다 — 글로도 말한다"),
    ("주요 버튼", "accent · primary", "한 화면에 하나. 둘이 되면 둘 다 안 눌린다"),
    ("약한 강조", "accent-soft · subtle", "같은 강조색의 <b>연한 짝</b>. 배지·선택된 줄에 쓴다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          쓰임 하나에 색 하나가 아니라 <b>짝</b>으로 갑니다 — 강조색에는 글자색(<code>on-accent</code>)과
          연한 바탕(<code>accent-soft</code>)이 함께 있어야 합니다. 이 짝을 안 만들어 두면
          결국 화면에서 <code>rgba(…, .1)</code> 같은 것을 손으로 섞게 되고, 다크 모드에서 그게 전부 깨집니다.</p>''',
  do=ul([
    "색을 <b>두 번 이상</b> 쓸 때 — 한 번 쓰는 색은 토큰이 아닙니다",
    "다크 모드나 고대비 모드를 <b>할 생각이 있을</b> 때",
    "브랜드 색이 바뀔 수 있을 때 — 1단만 고치면 끝납니다",
    "여러 사람이 같은 화면을 만들 때",
  ]),
  dont=ul([
    "일러스트나 그래프 색 — 의미가 아니라 <b>구별</b>이 목적이라 규칙이 다릅니다",
    "토큰 이름에 색 이름을 넣는 것 — <code>--blue-button</code>은 다크 모드에서 파랗지 않게 됩니다",
    "쓰임이 겹치는 토큰을 자꾸 늘리는 것 — <code>--accent2</code>가 생기면 이미 무너진 것입니다",
  ]),
  instead='밝고 어두운 두 벌이 필요하면 <a href="dark.html">다크 모드</a>, 떠 있는 느낌은 색이 아니라 <a href="elevation.html">고도</a>로 냅니다.',
  cases=cases([
    ('''              <div style="display:flex;gap:3px;width:100%%;max-width:220px">%s</div>''' %
     "".join('<span style="flex:1;height:40px;background:%s;display:block"></span>' % c
             for c in ["#eaf1ff", "#c5d9ff", "#8fb4ff", "#5b90f9", "#2f6df6", "#2254c7", "#1a3f94", "#132c66"]),
     "색 램프", "같은 색의 10단. 여기서 골라 쓰임에 연결한다"),
    ('''              <div class="tok" style="width:100%;max-width:230px">
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name">blue-500</span></div>
                <div style="text-align:center;color:var(--fg-faint);font-size:12px">↓</div>
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name"><b>--accent</b></span></div>
                <div style="text-align:center;color:var(--fg-faint);font-size:12px">↓</div>
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name">button-bg</span></div>
              </div>''',
     "3단 연결", "값 → 쓰임 → 부품. 화면은 맨 아래만 본다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:230px">
                <div style="display:flex;align-items:center;gap:8px;font-size:12px"><span style="width:16px;height:16px;border-radius:5px;background:var(--danger);display:block"></span>거절됨<span style="margin-left:auto;color:var(--fg-faint);font-size:11px">색 + 글자</span></div>
                <div style="display:flex;align-items:center;gap:8px;font-size:12px"><span style="width:16px;height:16px;border-radius:5px;background:#1f8a4c;display:block"></span>승인됨<span style="margin-left:auto;color:var(--fg-faint);font-size:11px">색 + 글자</span></div>
                <div style="font-size:11px;color:var(--fg-muted);border-top:1px solid var(--line);padding-top:6px">점 색만 다르면 색맹에게는 같은 줄입니다</div>
              </div>''',
     "상태 색", "빨강·초록 한 쌍은 <b>가장 흔한 색맹 조합</b>이다"),
  ]),
  s8_title="최소 코드와 이름 규칙", s8_hint="이 토큰의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="CSS 변수 세 겹으로 그대로 옮겨집니다. <b>화면은 2단·3단만 봅니다.</b>",
  code='''<span class="c">/* 1단 — 색 그 자체. 쓰임을 모른다 */</span>
<span class="t">:root</span> {
  <span class="a">--blue-500</span>: <span class="s">#2f6df6</span>;
  <span class="a">--blue-300</span>: <span class="s">#6f9bff</span>;
  <span class="a">--gray-900</span>: <span class="s">#14161a</span>;

  <span class="c">/* 2단 — 쓰임. 화면이 보는 것은 여기부터 */</span>
  <span class="a">--accent</span>: <span class="t">var</span>(<span class="a">--blue-500</span>);
  <span class="a">--on-accent</span>: <span class="s">#fff</span>;
  <span class="a">--fg</span>: <span class="t">var</span>(<span class="a">--gray-900</span>);
}

<span class="c">/* 어두운 모드 — 2단의 연결만 갈아 끼운다 */</span>
<span class="t">:root[data-theme="dark"]</span> {
  <span class="a">--accent</span>: <span class="t">var</span>(<span class="a">--blue-300</span>);
  <span class="a">--fg</span>: <span class="s">#e8ebf0</span>;
}

<span class="t">.btn</span> { <span class="a">background</span>: <span class="t">var</span>(<span class="a">--accent</span>); <span class="a">color</span>: <span class="t">var</span>(<span class="a">--on-accent</span>); }''',
  keys=kbd([
    ("이름에 색을 넣지 않는다", "<code>--brand-blue</code> ✗ → <code>--accent</code> ✓. 색이 바뀌어도 이름이 안 거짓말하게"),
    ("쓰임 + 자리 + 강도", "<code>--text-danger-strong</code>처럼 <b>무엇에 / 어디에 / 얼마나</b> 순으로 읽히게 짓는다"),
    ("짝을 함께 만든다", "바탕색에는 늘 그 위 글자색(<code>--on-*</code>)을 같이 정의한다"),
    ("화면에서 1단 금지", "<code>var(--blue-500)</code>을 컴포넌트에서 쓰면 다크 모드가 거기서 깨진다"),
    ("대비비를 값으로 못 박는다", "본문 4.5:1, 큰 글자·아이콘 3:1. 토큰을 고칠 때마다 다시 잰다"),
  ]),
  backend=rows([
    ("토큰 = 설정 파일의 상수", "코드 여기저기 박힌 매직 넘버를 <code>config</code>로 뺀 것과 같은 일입니다. 다른 점은 <b>값이 여러 벌</b>(밝게·어둡게)이라는 것뿐입니다."),
    ("어디에 저장하나", "보통 JSON 한 벌을 원본으로 두고(<b>W3C Design Tokens</b> 형식) 거기서 CSS·iOS·안드로이드 파일을 <b>생성</b>합니다. 손으로 세 군데 고치면 반드시 어긋납니다."),
    ("바꿀 때 영향 범위", "2단 하나를 고치면 그것을 가리키는 모든 3단이 따라 바뀝니다. 그래서 <b>2단은 적게</b> 두고 뜻을 또렷하게 지어야 합니다."),
    ("서버가 색을 보내는 경우", "상태 코드(<code>APPROVED</code>)를 보내고 색은 화면이 고릅니다. 서버가 <code>#1f8a4c</code>를 보내면 다크 모드에서 고칠 방법이 없습니다."),
  ]),
  plat_lede="세 플랫폼 모두 같은 생각을 하지만 부르는 말과 단 수가 다릅니다.",
  plats=plats([
    ("웹", "CSS 사용자 지정 속성",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">--accent<br>--fg<br>--surface</div>''',
     "<b>CSS 변수</b>로 둡니다. <code>:root</code>에 두고 <code>[data-theme]</code>로 갈아 끼우는 꼴이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">.label<br>.secondaryLabel<br>.systemBackground</div>''',
     "<b>시맨틱 컬러</b>가 OS 에 내장돼 있습니다. <code>Color.primary</code>처럼 쓰면 다크 모드·고대비가 <b>저절로</b> 따라옵니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">primary<br>onPrimary<br>surfaceVariant</div>''',
     "<b>색 역할</b>(color roles)이라 부르고 <code>primary</code>/<code>onPrimary</code> 짝이 규격에 박혀 있습니다."),
  ]),
  plat_note="iOS 와 안드로이드는 <b>시맨틱 색이 OS 에 이미 있습니다.</b> 거기에 브랜드 색을 억지로 덮으면 다크 모드·고대비·돋보기 설정이 한꺼번에 어긋납니다. 디자이너가 \"primary 로 해 주세요\"라고 할 때, 안드로이드 쪽에는 그게 <b>이미 정해진 이름</b>이라 뜻이 다를 수 있습니다.",
  siblings=siblings("color"),
  related='''        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>
        <li><span class="na"><b>배지와 칩</b><em>5부</em></span></li>
        <li><span class="na"><b>디자인 시스템</b><em>15부</em></span></li>''',
)
