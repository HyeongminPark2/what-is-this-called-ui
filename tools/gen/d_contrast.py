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
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">자리글 · 비활성   — 기준을 가장 자주 어김</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">눈으로 판단하지 말고 도구로 재서 숫자로 확인</div>
                </div>
              </div>'''

D = dict(
  slug="contrast", ko="대비비", en="Color contrast",
  desc="대비비 기준 세 가지(4.5:1, 3:1)와, 같은 색이라도 글자 크기에 따라 판정이 달라지는 모습을 직접 재서 보여 주는 항목입니다.",
  lede="대비비는 글자색과 바탕색의 <b>밝기 차이</b>를 1에서 21 사이의 값으로 잰 것입니다. 이 부의 항목 가운데 <b>눈으로 보고 확인할 수 있는 것</b>은 대비비 하나뿐입니다.",
  axes_lede="접근성은 눈에 안 보이는 부분까지 챙기는 일입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>색을 바꾸면 <b>세 가지 크기의 글자가 각각 기준을 통과하는지</b> 바로 나옵니다.
          같은 색인데도 큰 글자는 통과하고 본문 글자는 미달하는 경우를 살펴보세요.
          글자 크기에 따라 기준이 다르기 때문에 <b>"이 회색 써도 되나요"라는 질문에는 "어디에 쓰는데요"라고 되물어야</b> 답할 수 있습니다.<br>
          아래 네 칸은 이 도감에서 실제로 쓰는 색입니다. 그중 <b>자리글</b> 색이 기준에 가장 가깝게 걸쳐 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대비비, 명도 대비, 색 대비"),
    ("영어", "contrast ratio, color contrast, WCAG AA / AAA"),
    ("같이 쓰는 말",
     "대비비 기준을 정한 문서는 <b>WCAG</b>이고, 기준 수준은 <b>AA</b>(4.5:1)와 <b>AAA</b>(7:1)로 나뉩니다. "
     "테두리나 아이콘처럼 글자가 아닌 요소에 적용하는 기준은 <b>비텍스트 대비</b>(non-text contrast, 3:1)라고 합니다. "
     "WCAG에서 큰 글자는 <b>굵은 글씨 18.66px</b> 이상이거나 <b>24px</b> 이상인 글자를 말합니다."),
    ("자주 잘못 부르는 이름",
     "<b>밝기</b> — 밝기는 한 색의 성질이지만, 대비비는 글자색과 바탕색 <b>두 색 사이의 관계</b>입니다.<br>"
     "<b>AA와 AAA</b> — AAA는 AA보다 엄격한 기준으로, 필요할 때 골라서 적용합니다. 보통은 <b>AA를 목표</b>로 합니다.<br>"
     "<b>'보기에 충분한'</b> — 보기에 충분한지는 모니터와 화면 밝기, 보는 사람의 나이에 따라 달라지므로 <b>직접 재야</b> 알 수 있습니다."),
  ]),
  axes=ax("대비비"),
  oneline="대비비 기준은 <b>본문 4.5:1, 큰 글자 3:1, 테두리와 아이콘 3:1</b> 세 가지입니다. 통과 여부는 눈으로 판단하지 않고 도구로 재서 확인합니다.",
  s4_title="글자 크기와 쓰임별 판정", s4_hint="같은 색이라도 글자 크기에 따라 판정이 달라지는 모습",
  states=states([
    (ct("#14161a", "#ffffff", "16.1:1", "통과", "14px", "400", "본문", "150px", "border:1px solid var(--line)"),
     "본문에 진한 색을 쓸 때", "기준을 넉넉히 통과합니다. <b>기본 글자색</b>으로 씁니다"),
    (ct("#8a93a3", "#ffffff", "3.4:1", "미달 (4.5 필요)", "14px", "400", "본문", "150px", "border:1px solid var(--line)"),
     "본문에 흐린 색을 쓸 때", "글자색이 <b>흐릴수록 화면이 깔끔해 보여서</b> 기준을 가장 자주 어기는 경우입니다"),
    (ct("#8a93a3", "#ffffff", "3.4:1", "통과 (3.0 필요)", "19px", "800", "큰 글자", "150px", "border:1px solid var(--line)"),
     "같은 흐린 색을 큰 글자에 쓸 때", "큰 글자에는 다른 기준이 적용되기 때문에 <b>같은 색인데도 통과</b>합니다"),
    (ct("#ffffff", "#2f6df6", "4.6:1", "통과", "14px", "700", "확정하기"),
     "색 바탕 버튼의 흰 글자", "바탕에 색이 있는 버튼은 <b>흰 글자</b>를 써서 기준을 통과하는 경우가 많습니다"),
    (ct("#aeb6c2", "#ffffff", "1.9:1", "미달", "13px", "400", "계좌번호를 입력하세요", "150px", "border:1px solid var(--line-strong)"),
     "입력칸의 자리글", "자리글은 <b>거의 언제나 기준에 미달</b>하기 때문에 자리글에 정보를 담으면 안 됩니다"),
    ('''              <div style="width:100%;max-width:150px;display:grid;gap:6px">
                <div style="background:#ffffff;border:1px solid #e4e8ee;border-radius:6px;padding:11px">
                  <span style="font-size:13px;color:#14161a">테두리가 1.3:1</span>
                </div>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--danger);font-weight:700;text-align:center">1.3:1 · 미달 (3.0 필요)</span>
              </div>''',
     "입력칸 테두리", "대비 기준은 글자에만 적용되지 않습니다. <b>입력칸 테두리도 3:1</b> 이상이어야 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("두 색의 조합", "color + background", "대비비는 <b>두 색 사이의 관계</b>이므로 한 색만 보고는 알 수 없습니다"),
    ("본문 기준", "4.5 : 1", "화면의 글 대부분이 이 기준에 해당합니다"),
    ("큰 글자 기준", "3 : 1", "<b>굵은 글씨 18.66px</b> 이상이거나 <b>24px</b> 이상인 글자에 적용합니다. 획이 굵어서 같은 색이라도 덜 흐려 보이기 때문입니다"),
    ("글자가 아닌 요소", "3 : 1", "입력칸 테두리, 아이콘, 그래프에 적용합니다. 글자가 아니어서 <b>기준을 잊기 쉬운 자리</b>입니다"),
    ("기준을 자주 어기는 자리", "자리글 · 비활성", "색이 흐릴수록 깔끔해 보여서 <b>기준에 미달하기 쉽습니다</b>"),
    ("재는 방법", "개발자 도구 · 대비비 계산기", "<b>눈으로 판단하지 않고</b> 도구로 잽니다. 재면 숫자가 바로 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>비활성(disabled) 요소는 대비 기준에서 빠집니다.</b> WCAG가 비활성 요소를 예외로 두기 때문입니다.
          하지만 규칙에 걸리지 않는다고 해서 읽을 수 있다는 뜻은 아닙니다. 비활성 버튼이 무슨 버튼인지
          아예 보이지 않으면 사용자는 <b>그 버튼을 왜 누를 수 없는지</b>도 알 수 없습니다.
          그러니 예외 규정이 있더라도 비활성 요소를 지나치게 흐리게 두지 않는 편이 낫습니다.</p>''',
  do=ul([
    "<b>모든 글자</b>의 색을 정할 때. 본문은 4.5:1, 큰 글자는 3:1을 넘겨야 합니다",
    "<b>입력칸 테두리와 아이콘</b>의 색을 정할 때. 3:1을 넘겨야 하는데, 가장 자주 잊는 자리입니다",
    "다크 모드를 만들 때. 밝은 색과 어두운 색 <b>두 벌을 각각</b> 재야 합니다",
    "색 바탕 위에 흰 글자를 얹을 때. 브랜드 색이 밝으면 기준에 미달하는 경우가 많습니다",
  ]),
  dont=ul([
    "대비를 <b>눈으로 판단</b>할 때. 보이는 정도는 모니터와 화면 밝기, 보는 사람의 나이에 따라 다릅니다",
    "자리글에 <b>중요한 정보</b>를 담을 때. 자리글은 거의 언제나 대비 기준에 미달합니다",
    "색<b>만으로</b> 상태를 구별할 때. 대비를 맞춰도 색을 구별하지 못하는 사람에게는 똑같이 보입니다",
    "AAA(7:1)를 모든 곳에 요구할 때. 보통은 <b>AA를 목표</b>로 합니다",
  ]),
  do_title="대비비를 재야 하는 경우",
  dont_title="대비비를 다룰 때 피할 것",
  instead_title="대비비와 이어지는 주제는 다른 항목에서 다룹니다",
  instead='색을 쓰임별로 정리하는 방법은 <a href="../items/color.html">색 토큰</a>에서, 밝은 색과 어두운 색 두 벌을 관리하는 방법은 <a href="../items/dark.html">다크 모드</a>에서 다룹니다. 글자 크기를 정하는 기준은 <a href="../items/typescale.html">타입 스케일</a>을 보세요.',
  cases=cases([
    (ct("#697180", "#ffffff", "4.9:1", "통과", "13px", "400", "11월 1일 ~ 11월 7일", "190px", "border:1px solid var(--line)"),
     "보조 글의 색 정하기", "본문보다 흐리게 하되 <b>4.5:1은 넘깁니다</b>. 이 도감의 보조 글에 쓰는 색입니다"),
    (ct("#ffffff", "#2f6df6", "4.6:1", "통과", "13px", "700", "확정하기", "190px"),
     "주요 버튼의 글자색 정하기", "브랜드 색이 <b>밝으면 기준에 미달</b>합니다. 그럴 때는 바탕색을 한 단계 어둡게 하거나 글자를 키웁니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:6px">
                <div style="background:#15181e;color:#9aa3b2;border-radius:6px;padding:11px">
                  <span style="font-size:13px">다크 모드의 보조 글</span>
                </div>
                <span style="font-family:var(--mono);font-size:10.5px;color:#1f8a4c;font-weight:700;text-align:center">6.99:1 · 통과</span>
              </div>''',
     "다크 모드에서 다시 재기", "<b>밝은 모드에서 통과한 색 조합이라도 다크 모드에서는 따로 재야 합니다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="대비비를 재는 방법과 기준",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="대비비는 브라우저 개발자 도구에서 색을 누르면 바로 나옵니다. 코드로 재야 할 때도 아래처럼 짧은 공식으로 계산할 수 있습니다.",
  code='''<span class="c">// 상대 밝기를 구한 뒤 대비비를 계산한다. WCAG 공식 그대로다</span>
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
    ("본문은 4.5:1 이상", "화면의 글 대부분에 적용하는 <b>기본 기준</b>입니다"),
    ("큰 글자는 3:1 이상", "굵은 글씨 18.66px 이상이거나 24px 이상인 글자에 적용합니다"),
    ("테두리와 아이콘은 3:1 이상", "이 기준 가운데 입력칸 테두리를 가장 자주 잊습니다"),
    ("다크 모드는 따로 재기", "밝은 모드에서 통과했다고 다크 모드에서도 통과한다는 보장이 없습니다"),
    ("색만으로 상태를 구별하지 않기", "대비를 맞춰도 <b>색을 구별하지 못하는 사람에게는 같은 회색</b>으로 보입니다"),
    ("토큰을 만들 때 한 번 재기", "색을 쓸 때마다 재지 말고 <b>토큰을 만들 때</b> 미리 재 둡니다"),
  ]),
  backend=rows([
    ("토큰 단위로 한 번만 재기", "색을 <a href=\"../items/color.html\">토큰</a>으로 정리해 두면 <b>토큰 개수만큼만</b> 재면 되므로, 화면마다 재는 것보다 일이 훨씬 적습니다."),
    ("CI에서 자동으로 검사하기", "<code>axe-core</code>나 Lighthouse가 대비비를 자동으로 재 줍니다. 접근성 항목 가운데 <b>자동 검사가 가장 잘 되는</b> 편입니다."),
    ("사진 위에 얹은 글자", "사진 위에 글을 얹으면 <b>사진마다 대비가 달라지기</b> 때문에, 사진과 글자 사이에 반투명 막을 깔거나 글자에 그림자를 넣습니다."),
    ("브랜드 색이 기준에 미달할 때", "브랜드 색이 밝으면 그 위에 얹은 흰 글자가 기준에 미달합니다. 이럴 때는 <b>흰 글자 바탕용으로 한 단계 어두운 색</b>을 토큰에 따로 두는 방법을 흔히 씁니다."),
  ]),
  plat_lede="웹, iOS, 안드로이드 모두 WCAG 기준을 따르고, 재는 도구만 다릅니다.",
  plats=plats([
    ("웹", "WCAG AA",
     ct("#697180", "#ffffff", "4.9:1", "통과", "12px", "400", "보조 글", "120px", "border:1px solid var(--line)"),
     "개발자 도구에서 색을 누르면 대비비가 바로 나오고, Lighthouse를 돌리면 페이지 전체를 검사해 줍니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Accessibility<br>Inspector<br>Increase Contrast</div>''',
     "기준은 웹과 같고, <b>Accessibility Inspector</b>로 잽니다. 사용자가 설정에서 '대비 높이기'를 켤 수도 있습니다."),
    ("안드로이드", "Material 3",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">Accessibility<br>Scanner<br>고대비 텍스트</div>''',
     "<b>Accessibility Scanner</b> 앱으로 화면을 찍으면 기준에 미달한 곳을 표시해 줍니다."),
  ]),
  plat_note="기준(4.5:1 · 3:1)이 <b>세 플랫폼 모두 같기</b> 때문에 \"이 회색은 본문에 못 씁니다\"라는 말이 어느 플랫폼에서나 같은 뜻으로 통합니다. 다만 iOS와 안드로이드에는 사용자가 직접 켜는 <b>고대비 모드</b>가 있으니, 고대비 모드에서 화면이 어떻게 보이는지까지 확인하는 편이 좋습니다.",
  siblings=siblings("contrast"),
  related='''        <li><a href="../items/color.html"><b>색 토큰</b><em>2부</em></a></li>
        <li><a href="../items/dark.html"><b>다크 모드</b><em>2부</em></a></li>
        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="../items/badge.html"><b>배지</b><em>5부</em></a></li>''',
)
