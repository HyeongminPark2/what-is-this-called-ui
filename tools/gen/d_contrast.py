# -*- coding: utf-8 -*-
from ax12 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def ct(fg, bg, ratio, verdict, size="14px", weight="400", label="정산 확정", w="150px", border=""):
    color = "#1f8a4c" if "통과" in verdict else "var(--danger)"
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:6px">'
            '<div style="background:' + bg + ';color:' + fg + ';border-radius:6px;padding:11px;' + border + '">'
            '<span style="font-size:' + size + ';font-weight:' + weight + '">' + label + '</span></div>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:' + color + ';font-weight:700;text-align:center">'
            + ratio + ' · ' + verdict + '</span></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:230px;background:#ffffff;border:1px solid var(--line);border-radius:7px;padding:11px;display:grid;gap:5px">
                    <span style="font-size:18px;font-weight:800;color:#14161a">큰 글자</span>
                    <span style="font-size:13px;color:#14161a">본문 — 정산이 확정되었습니다</span>
                    <span style="font-size:11px;color:#8a93a3">보조 글</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">본문 4.5 : 1</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">큰 글자(18.66px 굵게 · 24px) 3 : 1</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">테두리 · 아이콘 3 : 1</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자리글 · 비활성   — 가장 자주 넘긴다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">눈으로 판단하지 않는다 — 재면 숫자가 나온다</div>
                </div>
              </div>'''

D = dict(
  slug="contrast", ko="대비비", en="Color contrast",
  desc="대비비 기준 셋(4.5:1, 3:1)과 크기에 따라 판정이 갈리는 것을 재서 보여주는 항목.",
  lede="글자색과 바탕색의 <b>밝기 차이</b>를 1~21로 잰 값. 이 부에서 <b>유일하게 눈으로 보이는</b> 항목입니다.",
  axes_lede="접근성은 '눈으로는 안 보이는 것을 챙기는 일'입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꾸면 <b>세 크기가 각각 통과인지</b> 바로 나옵니다.
          같은 색인데 큰 글자는 통과하고 본문은 미달하는 것을 보세요 —
          기준이 하나가 아니라서 <b>"이 회색 써도 되나요"의 답은 "어디에 쓰는데요"</b>입니다.<br>
          아래 네 칸은 이 도감이 실제로 쓰는 색입니다. <b>자리글</b>이 유독 아슬아슬합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대비비, 명도 대비, 색 대비"),
    ("영어", "contrast ratio, color contrast, WCAG AA / AAA"),
    ("같이 쓰는 말",
     "기준을 정한 문서가 <b>WCAG</b>이고 수준이 <b>AA</b>(4.5:1)와 <b>AAA</b>(7:1)로 나뉩니다. "
     "글자 아닌 것(테두리·아이콘)의 기준은 <b>비텍스트 대비</b>(non-text contrast, 3:1)입니다. "
     "큰 글자는 <b>18.66px 굵게</b> 또는 <b>24px</b> 부터입니다."),
    ("자주 잘못 부름",
     "<b>밝기</b> — 대비비는 <b>두 색의 관계</b>이지 한 색의 성질이 아닙니다.<br>"
     "<b>AA 와 AAA</b> — AAA 는 더 엄격한 선택 기준입니다. 보통 <b>AA 를 목표</b>로 합니다.<br>"
     "<b>'보기에 충분한'</b> — 모니터·밝기·나이에 따라 다릅니다. <b>재야</b> 알 수 있습니다."),
  ]),
  axes=ax("대비비"),
  oneline="기준은 셋입니다 — <b>본문 4.5:1 · 큰 글자 3:1 · 테두리와 아이콘 3:1</b>. 눈으로 판단하지 않고 잽니다.",
  s4_title="기준", s4_hint="같은 색이 크기 따라 갈린다",
  states=states([
    (ct("#14161a", "#ffffff", "16.1:1", "통과", "14px", "400", "본문", "150px", "border:1px solid var(--line)"),
     "본문 · 진한 색", "넉넉히 통과. <b>기본 글자색</b>"),
    (ct("#8a93a3", "#ffffff", "3.4:1", "미달 (4.5 필요)", "14px", "400", "본문", "150px", "border:1px solid var(--line)"),
     "본문 · 흐린 색", "<b>흐릴수록 예뻐 보여</b> 가장 자주 넘긴다"),
    (ct("#8a93a3", "#ffffff", "3.4:1", "통과 (3.0 필요)", "19px", "800", "큰 글자", "150px", "border:1px solid var(--line)"),
     "큰 글자 · 같은 색", "<b>같은 색인데 통과</b>한다 — 기준이 다르다"),
    (ct("#ffffff", "#2f6df6", "4.6:1", "통과", "14px", "700", "확정하기"),
     "버튼", "바탕이 색이면 <b>흰 글자</b>로 넘기는 일이 많다"),
    (ct("#aeb6c2", "#ffffff", "1.9:1", "미달", "13px", "400", "계좌번호를 입력하세요", "150px", "border:1px solid var(--line-strong)"),
     "자리글", "<b>거의 늘 미달</b>이다. 그래서 자리글에 정보를 담으면 안 된다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:6px">
                <div style="background:#ffffff;border:1px solid #e4e8ee;border-radius:6px;padding:11px">
                  <span style="font-size:13px;color:#14161a">테두리가 1.3:1</span>
                </div>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--danger);font-weight:700;text-align:center">1.3:1 · 미달 (3.0 필요)</span>
              </div>''',
     "테두리", "글자만이 아니다. <b>입력칸 테두리도 3:1</b> 이어야 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("한 덩어리", "color + background", "대비비는 <b>두 색의 관계</b>다. 한 색만 보고는 알 수 없다"),
    ("본문 기준", "4.5 : 1", "대부분의 글이 여기 해당한다"),
    ("큰 글자 기준", "3 : 1", "<b>18.66px 굵게</b> 또는 <b>24px</b> 부터. 획이 굵어 덜 흐려 보인다"),
    ("글자 아닌 것", "3 : 1", "입력칸 테두리·아이콘·그래프 — <b>잊기 쉬운 자리</b>"),
    ("자주 넘기는 자리", "자리글 · 비활성", "흐릴수록 예뻐 보여서 <b>기준을 넘기기 쉽다</b>"),
    ("재는 법", "개발자 도구 · 대비비 계산기", "<b>눈으로 판단하지 않는다.</b> 숫자가 바로 나온다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>비활성(disabled)은 기준에서 빠집니다.</b> WCAG 가 비활성 요소를 예외로 두기 때문입니다 —
          하지만 '규칙에 안 걸린다'와 '읽을 수 있다'는 다릅니다. 비활성 버튼이 무슨 버튼인지
          아예 안 보이면 <b>왜 못 누르는지</b>도 알 수 없습니다.
          규칙을 핑계로 지나치게 흐리게 두지 않는 편이 낫습니다.</p>''',
  do=ul([
    "<b>모든 글자</b> — 본문 4.5:1, 큰 글자 3:1",
    "<b>입력칸 테두리와 아이콘</b> — 3:1. 가장 자주 잊는 자리",
    "다크 모드 — <b>두 벌을 각각</b> 재야 합니다",
    "색 위에 얹은 흰 글자 — 브랜드 색이 밝으면 자주 미달합니다",
  ]),
  dont=ul([
    "<b>눈으로 판단</b>하는 것 — 모니터·밝기·나이에 따라 다릅니다",
    "자리글에 <b>중요한 정보</b>를 담는 것 — 거의 늘 미달입니다",
    "색<b>만으로</b> 상태를 말하는 것 — 대비를 맞춰도 색맹에게는 같습니다",
    "AAA(7:1)를 모든 곳에 요구하는 것 — 보통 <b>AA 가 목표</b>입니다",
  ]),
  instead='색을 쓰임으로 정리하는 것은 <a href="../items/color.html">색 토큰</a>, 두 벌 관리는 <a href="../items/dark.html">다크 모드</a>, 글자 크기 기준은 <a href="../items/typescale.html">타입 스케일</a>.',
  cases=cases([
    (ct("#697180", "#ffffff", "4.9:1", "통과", "13px", "400", "11월 1일 ~ 11월 7일", "190px", "border:1px solid var(--line)"),
     "보조 글", "흐리게 하되 <b>4.5 는 넘긴다</b>. 이 도감의 보조 글 색"),
    (ct("#ffffff", "#2f6df6", "4.6:1", "통과", "13px", "700", "확정하기", "190px"),
     "주요 버튼", "브랜드 색이 <b>밝으면 미달</b>한다. 색을 한 단 어둡게 하거나 글자를 키운다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:6px">
                <div style="background:#15181e;color:#9aa3b2;border-radius:6px;padding:11px">
                  <span style="font-size:13px">다크 모드의 보조 글</span>
                </div>
                <span style="font-family:var(--mono);font-size:10.5px;color:#1f8a4c;font-weight:700;text-align:center">6.99:1 · 통과</span>
              </div>''',
     "다크 모드", "<b>밝은 쪽에서 통과했다고 어두운 쪽도 통과하지는 않는다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="재는 법과 기준",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="브라우저 개발자 도구에서 색을 누르면 바로 나옵니다. 코드로 재야 할 때는 공식이 짧습니다.",
  code='''<span class="c">// 상대 밝기 → 대비비. WCAG 공식 그대로다</span>
<span class="t">const</span> lum = (hex) =&gt; {
  <span class="t">const</span> n = parseInt(hex.slice(<span class="a">1</span>), <span class="a">16</span>);
  <span class="t">const</span> c = [(n &gt;&gt; <span class="a">16</span>) &amp; <span class="a">255</span>, (n &gt;&gt; <span class="a">8</span>) &amp; <span class="a">255</span>, n &amp; <span class="a">255</span>]
    .map(v =&gt; (v /= <span class="a">255</span>) &lt;= <span class="a">.03928</span> ? v / <span class="a">12.92</span>
                                 : ((v + <span class="a">.055</span>) / <span class="a">1.055</span>) ** <span class="a">2.4</span>);
  <span class="t">return</span> <span class="a">.2126</span> * c[<span class="a">0</span>] + <span class="a">.7152</span> * c[<span class="a">1</span>] + <span class="a">.0722</span> * c[<span class="a">2</span>];
};
<span class="t">const</span> ratio = (a, b) =&gt; {
  <span class="t">const</span> [x, y] = [lum(a), lum(b)];
  <span class="t">return</span> (Math.max(x, y) + <span class="a">.05</span>) / (Math.min(x, y) + <span class="a">.05</span>);
};

ratio(<span class="s">'#697180'</span>, <span class="s">'#ffffff'</span>);   <span class="c">// 4.91 → 본문 통과</span>''',
  keys=kbd([
    ("본문 4.5:1", "대부분의 글. <b>기본 기준</b>"),
    ("큰 글자 3:1", "18.66px 굵게 또는 24px 부터"),
    ("테두리·아이콘 3:1", "입력칸 테두리를 가장 자주 잊는다"),
    ("다크 모드는 따로 잰다", "밝은 쪽 통과가 어두운 쪽 통과를 보장하지 않는다"),
    ("색만으로 말하지 않는다", "대비를 맞춰도 <b>색맹에게는 같은 회색</b>이다"),
    ("토큰에서 한 번 정한다", "색을 쓸 때마다 재지 말고 <b>토큰을 만들 때</b> 재 둔다"),
  ]),
  backend=rows([
    ("토큰에서 한 번", "색을 <a href=\"../items/color.html\">토큰</a>으로 정리해 두면 <b>토큰 수만큼만</b> 재면 됩니다. 화면마다 재는 것과 일이 열 배 차이 납니다."),
    ("CI 에서 검사", "<code>axe-core</code>·Lighthouse 가 대비비를 자동으로 잽니다. <b>접근성 항목 중 자동화가 가장 잘 되는</b> 쪽입니다."),
    ("그림 위의 글자", "사진 위에 글을 얹으면 <b>사진마다 대비가 다릅니다.</b> 반투명 막을 깔거나 글자에 그림자를 넣습니다."),
    ("브랜드 색과 충돌", "브랜드 색이 밝으면 흰 글자가 미달합니다. <b>흰 글자용으로 한 단 어두운 색</b>을 토큰에 따로 두는 것이 흔한 해법입니다."),
  ]),
  plat_lede="기준은 셋 다 WCAG 를 따르고, 재는 도구가 다릅니다.",
  plats=plats([
    ("웹", "WCAG AA",
     ct("#697180", "#ffffff", "4.9:1", "통과", "12px", "400", "보조 글", "120px", "border:1px solid var(--line)"),
     "개발자 도구에서 색을 누르면 바로 나옵니다. Lighthouse 가 전체를 훑어 줍니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Accessibility<br>Inspector<br>Increase Contrast</div>''',
     "기준은 같고, <b>Accessibility Inspector</b> 로 잽니다. 사용자가 '대비 높이기'를 켤 수 있습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Accessibility<br>Scanner<br>고대비 텍스트</div>''',
     "<b>Accessibility Scanner</b> 앱으로 화면을 찍으면 미달한 곳을 표시해 줍니다."),
  ]),
  plat_note="기준(4.5:1 · 3:1)이 <b>세 플랫폼 모두 같습니다</b>. 그래서 \"이 회색은 본문에 못 씁니다\"가 그대로 통합니다. 다만 두 OS 에는 사용자가 켜는 <b>고대비 모드</b>가 있어서, 그때 어떻게 보일지까지 보는 편이 좋습니다.",
  siblings=siblings("contrast"),
  related='''        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>''',
)
