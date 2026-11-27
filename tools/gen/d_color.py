# -*- coding: utf-8 -*-
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
  desc="색을 #2f6df6 같은 값 대신 --accent 같은 쓰임의 이름으로 정해 두는 방법을 실물과 해부도로 보여 주는 항목입니다.",
  lede="색 토큰은 색을 <b>값</b> 대신 <b>쓰임</b>의 이름으로 부르기로 정해 둔 것입니다. 화면 코드에는 <code>#2f6df6</code> 같은 값을 적지 않고 <code>--accent</code> 같은 이름만 적습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>1단은 색 자체의 이름(<code>blue-500</code>), 2단은 쓰임의 이름(<code>--accent</code>), 3단은 부품 전용 이름(<code>button-bg</code>)입니다.
          <b>어두운 화면으로</b>를 켜면 2단의 <b>화살표만</b> 다른 색을 가리키도록 바뀝니다.
          1단의 색은 그대로이고 3단도 손대지 않았지만, 3단이 2단을 가리키고 있기 때문에 버튼 색이 함께 바뀝니다. 한 곳만 고쳐서 화면 전체의 색을 바꿀 수 있다는 점이 토큰을 쓰는 이유입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "색 토큰, 시맨틱 색, 의미 색"),
    ("영어", "color token, semantic color, design token"),
    ("같이 쓰는 말",
     "<b>원시 토큰</b>(raw · primitive · global)은 <code>blue-500</code>처럼 색 그 자체를 가리키고, "
     "<b>시맨틱 토큰</b>(semantic · alias)은 <code>--accent</code>처럼 쓰임을 가리킵니다. "
     "<b>컴포넌트 토큰</b>(component)은 <code>button-bg</code>처럼 한 부품에만 쓰는 토큰입니다. "
     "같은 색을 10단으로 늘어놓은 묶음은 <b>색 램프</b>(ramp · scale)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>테마</b> — 테마는 토큰 <b>한 벌</b> 전체를 가리키는 말이고, 토큰은 그 안의 항목 하나입니다.<br>"
     "<b>CSS 변수</b> — CSS 변수는 값을 저장하는 수단이고, 토큰은 그 값을 어디에 쓸지 정한 <b>규칙</b>입니다. 그래서 CSS 변수를 쓴다고 해서 저절로 토큰이 되지는 않습니다.<br>"
     "<b>팔레트</b> — 팔레트는 쓸 수 있는 색을 모아 둔 목록이고, 토큰은 그 색을 어디에 쓸지까지 정한 것입니다."),
  ]),
  s4_title="쓰임에 따라 나눈 색", s4_hint="쓰임마다 정해 둔 색과 그 색을 쓰는 자리",
  states=states([
    (chip("var(--accent)", "--accent", "강조 · 주요 동작"), "강조할 때", "누를 수 있는 것과 선택된 것을 표시합니다. 강조색을 쓴 주요 동작은 <b>한 화면에 하나</b>만 두는 것이 원칙입니다"),
    (chip("var(--danger)", "--danger", "되돌릴 수 없음"), "위험한 동작을 알릴 때", "삭제나 거절처럼 <b>되돌리기 어려운</b> 동작에만 씁니다"),
    (chip("var(--warn)", "--warn", "주의"), "주의를 줄 때", "진행을 막지는 않지만 사용자가 알아 두어야 할 내용에 씁니다"),
    (chip("#1f8a4c", "--success", "완료 알림"), "성공을 알릴 때", "확인이나 완료를 알립니다. 색맹인 사람에게는 초록이 빨강과 비슷해 보이므로 <b>글자도 함께</b> 적습니다"),
    (chip("var(--fg-muted)", "--fg-muted", "보조 글"), "덜 중요한 글에", "덜 중요한 글에 씁니다. 흐린 색이라도 바탕과의 대비비 4.5:1은 지켜야 합니다"),
    (chip("var(--line)", "--line", "선 · 경계"), "칸을 나누는 선에", "칸을 나누는 선에 씁니다. 글자가 아니므로 대비비는 3:1이면 충분합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("면", "surface", "카드의 바탕색입니다. 페이지 바탕(<code>--bg</code>)과 <b>한 단계 다른</b> 색으로 둡니다"),
    ("본문 글", "fg · text-primary", "가장 진한 글자색입니다. 바탕과의 대비비가 <b>4.5:1</b> 이상이어야 합니다"),
    ("보조 글", "fg-muted · text-secondary", "덜 중요한 글에 씁니다. 글자를 흐리게 만들다 보면 대비비 기준을 놓치기 쉬운 자리입니다"),
    ("위험 글", "danger · text-error", "빨간색만으로 알리지 않고, 무엇이 문제인지 글로도 적습니다"),
    ("주요 버튼", "accent · primary", "한 화면에 하나만 둡니다. 두 개가 되면 어느 쪽이 주요 동작인지 알기 어려워집니다"),
    ("약한 강조", "accent-soft · subtle", "강조색과 짝을 이루는 <b>연한 색</b>입니다. 배지나 선택된 줄에 씁니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          색 토큰은 쓰임 하나에 색 하나씩 정하지 않고 여러 색을 <b>짝</b>으로 묶어 정합니다. 예를 들어 강조색에는 그 위에 올릴 글자색(<code>on-accent</code>)과
          연한 바탕색(<code>accent-soft</code>)이 함께 있어야 합니다. 이 짝을 미리 만들어 두지 않으면
          화면을 만들 때마다 <code>rgba(…, .1)</code> 같은 색을 손으로 섞게 되는데, 이렇게 섞은 색은 토큰을 거치지 않아서 다크 모드로 바꿔도 따라 바뀌지 않습니다.</p>''',
  do=ul([
    "같은 색을 <b>두 번 이상</b> 쓸 때. 한 번만 쓰는 색은 토큰으로 만들 필요가 없습니다",
    "다크 모드나 고대비 모드를 <b>지원할 계획이 있을</b> 때",
    "브랜드 색이 바뀔 수 있을 때. 토큰을 쓰면 1단의 값만 고치면 됩니다",
    "여러 사람이 같은 화면을 만들 때",
  ]),
  dont=ul([
    "일러스트나 그래프 색을 정할 때. 이런 색은 의미를 전하기보다 서로 <b>구별</b>되는 것이 목적이라 규칙이 다릅니다",
    "토큰 이름에 색 이름을 넣을 때. <code>--blue-button</code>은 다크 모드에서 파란색이 아니게 될 수 있어 이름과 실제 색이 어긋납니다",
    "쓰임이 겹치는 토큰을 자꾸 늘릴 때. <code>--accent2</code> 같은 이름이 생겼다면 이미 쓰임의 구분이 흐려졌다는 뜻입니다",
  ]),
  instead_title="색 토큰과 함께 보면 좋은 항목",
  instead='밝은 화면과 어두운 화면에 쓸 값을 두 벌 마련해야 하면 <a href="dark.html">다크 모드</a> 항목을 함께 봅니다. 부품이 떠 있는 느낌은 색을 바꿔서 내지 않고 <a href="elevation.html">고도</a>로 표현합니다.',
  cases=cases([
    ('''              <div style="display:flex;gap:3px;width:100%%;max-width:220px">%s</div>''' %
     "".join('<span style="flex:1;height:40px;background:%s;display:block"></span>' % c
             for c in ["#eaf1ff", "#c5d9ff", "#8fb4ff", "#5b90f9", "#2f6df6", "#2254c7", "#1a3f94", "#132c66"]),
     "색 램프에서 값 고르기", "같은 색을 10단으로 나눈 묶음입니다. 여기서 값을 골라 쓰임에 연결합니다"),
    ('''              <div class="tok" style="width:100%;max-width:230px">
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name">blue-500</span></div>
                <div style="text-align:center;color:var(--fg-faint);font-size:12px">↓</div>
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name"><b>--accent</b></span></div>
                <div style="text-align:center;color:var(--fg-faint);font-size:12px">↓</div>
                <div class="tok__row" style="padding:6px 8px;font-size:12px"><span class="tok__chip" style="width:22px;height:22px;background:#2f6df6"></span><span class="tok__name">button-bg</span></div>
              </div>''',
     "값에서 부품까지 3단으로 잇기", "값에서 쓰임으로, 쓰임에서 부품으로 이어집니다. 화면 코드는 맨 아래의 부품 토큰만 씁니다"),
    ('''              <div style="display:grid;gap:7px;width:100%;max-width:230px">
                <div style="display:flex;align-items:center;gap:8px;font-size:12px"><span style="width:16px;height:16px;border-radius:5px;background:var(--danger);display:block"></span>거절됨<span style="margin-left:auto;color:var(--fg-faint);font-size:11px">색 + 글자</span></div>
                <div style="display:flex;align-items:center;gap:8px;font-size:12px"><span style="width:16px;height:16px;border-radius:5px;background:#1f8a4c;display:block"></span>승인됨<span style="margin-left:auto;color:var(--fg-faint);font-size:11px">색 + 글자</span></div>
                <div style="font-size:11px;color:var(--fg-muted);border-top:1px solid var(--line);padding-top:6px">점 색만 다르면 색맹에게는 같은 줄입니다</div>
              </div>''',
     "상태를 색과 글자로 함께 알리기", "빨강과 초록은 색맹인 사람이 <b>가장 흔하게 구별하지 못하는</b> 조합입니다"),
  ]),
  s8_title="최소 코드와 이름 규칙", s8_hint="코드로 옮기는 법과 지킬 규칙",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
  code_lede="세 단의 토큰은 CSS 변수 세 겹으로 그대로 옮길 수 있습니다. <b>화면 코드에서는 2단과 3단만 씁니다.</b>",
  code='''<span class="c">/* 1단. 색 그 자체이고 쓰임은 정하지 않는다 */</span>
<span class="t">:root</span> {
  <span class="a">--blue-500</span>: <span class="s">#2f6df6</span>;
  <span class="a">--blue-300</span>: <span class="s">#6f9bff</span>;
  <span class="a">--gray-900</span>: <span class="s">#14161a</span>;

  <span class="c">/* 2단. 쓰임을 정한다. 화면은 여기부터 쓴다 */</span>
  <span class="a">--accent</span>: <span class="t">var</span>(<span class="a">--blue-500</span>);
  <span class="a">--on-accent</span>: <span class="s">#fff</span>;
  <span class="a">--fg</span>: <span class="t">var</span>(<span class="a">--gray-900</span>);
}

<span class="c">/* 어두운 모드에서는 2단의 연결만 바꾼다 */</span>
<span class="t">:root[data-theme="dark"]</span> {
  <span class="a">--accent</span>: <span class="t">var</span>(<span class="a">--blue-300</span>);
  <span class="a">--fg</span>: <span class="s">#e8ebf0</span>;
}

<span class="t">.btn</span> { <span class="a">background</span>: <span class="t">var</span>(<span class="a">--accent</span>); <span class="a">color</span>: <span class="t">var</span>(<span class="a">--on-accent</span>); }''',
  keys=kbd([
    ("이름에 색 이름을 넣지 않기", "<code>--brand-blue</code>(✗) 대신 <code>--accent</code>(✓)처럼 짓습니다. 이렇게 지어야 색이 바뀌어도 이름과 실제 색이 어긋나지 않습니다"),
    ("쓰임, 자리, 강도 순서로 짓기", "<code>--text-danger-strong</code>처럼 <b>무엇에 / 어디에 / 얼마나</b> 순서로 읽히도록 짓습니다"),
    ("짝이 되는 색을 함께 만들기", "바탕색을 정할 때는 그 위에 올릴 글자색(<code>--on-*</code>)도 늘 함께 정의합니다"),
    ("화면 코드에서 1단 토큰을 쓰지 않기", "컴포넌트에서 <code>var(--blue-500)</code>을 직접 쓰면 그 자리만 다크 모드에서 색이 바뀌지 않습니다"),
    ("토큰 값마다 대비비 확인하기", "본문은 4.5:1, 큰 글자와 아이콘은 3:1 이상이어야 하고, 토큰 값을 고칠 때마다 대비비를 다시 잽니다"),
  ]),
  backend=rows([
    ("설정 파일의 상수와 같은 역할", "코드 여기저기에 직접 적힌 매직 넘버를 <code>config</code>로 빼내는 것과 같은 일입니다. 다만 토큰은 밝은 화면용과 어두운 화면용처럼 <b>값이 여러 벌</b>이라는 점이 다릅니다."),
    ("토큰 원본을 저장하는 곳", "보통 <b>W3C Design Tokens</b> 형식의 JSON 한 벌을 원본으로 두고, 거기서 CSS와 iOS, 안드로이드용 파일을 <b>생성</b>합니다. 세 플랫폼의 파일을 손으로 따로 고치면 결국 값이 서로 어긋나기 때문입니다."),
    ("토큰 하나를 바꿀 때 영향이 미치는 범위", "2단 토큰 하나를 고치면 그 토큰을 가리키는 3단 토큰이 모두 함께 바뀝니다. 그래서 <b>2단은 개수를 적게</b> 두고 이름의 뜻을 또렷하게 지어야 합니다."),
    ("서버가 색 값을 보내면 생기는 문제", "서버는 <code>APPROVED</code> 같은 상태 코드만 보내고, 색은 화면 쪽에서 고릅니다. 서버가 <code>#1f8a4c</code> 같은 색 값을 직접 보내면 화면에서는 다크 모드에 맞게 색을 바꿀 방법이 없습니다."),
  ]),
  plat_lede="세 플랫폼 모두 색을 쓰임으로 정한다는 생각은 같지만, 부르는 이름과 단의 수가 다릅니다.",
  plats=plats([
    ("웹", "CSS 사용자 지정 속성",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">--accent<br>--fg<br>--surface</div>''',
     "<b>CSS 변수</b>로 정의합니다. <code>:root</code>에 기본값을 두고 <code>[data-theme]</code> 속성에 따라 값을 바꾸는 방식이 가장 흔합니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">.label<br>.secondaryLabel<br>.systemBackground</div>''',
     "<b>시맨틱 컬러</b>가 OS에 들어 있습니다. <code>Color.primary</code>처럼 쓰면 다크 모드와 고대비 설정에 맞춰 색이 <b>저절로</b> 바뀝니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);line-height:1.8;text-align:left">primary<br>onPrimary<br>surfaceVariant</div>''',
     "<b>색 역할</b>(color roles)이라고 부르며, <code>primary</code>와 <code>onPrimary</code> 같은 짝이 규격에 정해져 있습니다."),
  ]),
  plat_note="iOS와 안드로이드에는 <b>시맨틱 색이 OS에 이미 정해져 있습니다.</b> 그 위에 브랜드 색을 억지로 덮어쓰면 다크 모드와 고대비, 돋보기 설정에 맞춰 색이 제대로 바뀌지 않습니다. 또 디자이너가 \"primary로 해 주세요\"라고 할 때, 안드로이드에서는 primary가 <b>이미 정해진 역할 이름</b>이라 디자이너가 생각한 뜻과 다를 수 있습니다.",
  siblings=siblings("color"),
  related='''        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="contrast.html"><b>대비비</b><em>12부</em></a></li>
        <li><span class="na"><b>배지와 칩</b><em>5부</em></span></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>''',
)
