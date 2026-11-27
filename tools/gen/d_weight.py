# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def wt(w, label, note="", size=16):
    return ('              <div style="display:grid;gap:5px;justify-items:center;text-align:center">'
            '<span style="font-size:' + str(size) + 'px;font-weight:' + str(w) + ';line-height:1.3">정산 확정</span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">' + label + '</span>'
            + ('<span style="font-size:10px;color:var(--fg-faint)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="font-size:17px;font-weight:400">정산이 확정되었습니다</div>
                  <div class="pin-out" data-pin="2" style="font-size:17px;font-weight:500">정산이 확정되었습니다</div>
                  <div class="pin-out" data-pin="3" style="font-size:17px;font-weight:700">정산이 확정되었습니다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">@font-face { font-weight: 400 }   — 굵기마다 파일 한 벌</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">가짜 굵게(synthetic bold)   — 파일이 없으면 흉내 낸다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">가변 글꼴(variable)   — 한 파일로 100~900</div>
                </div>
              </div>'''

D = dict(
  slug="weight", ko="글자 굵기", en="Font weight",
  desc="굵기 아홉 단과 실제로 쓰는 세 단, 가짜 굵게와 가변 글꼴을 실물과 해부도로 보여 주는 항목입니다.",
  lede="글자 굵기는 글자 획의 <b>두께</b>입니다. 굵기를 쓰면 크기를 키우지 않고도 강조할 수 있고, 굵기를 바꿔도 줄 높이는 그대로라서 레이아웃이 흔들리지 않습니다.",
  axes_lede="글자를 다루는 항목들은 값 하나를 바꾸면 글 전체가 함께 바뀐다는 점이 같습니다. 서로 구별하려면 아래 네 가지를 물어보면 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>체크를 풀어 아홉 단을 모두 펼쳐 보세요. 그러면 아래에 <b>실제로 다르게 보이는 단이 몇 개인지</b> 재서 알려 줍니다.
          받아 온 파일이 없는 단은 브라우저가 흉내 내서 그리거나 옆 단과 똑같이 그리기 때문에, 아홉 단이 모두 다르게 보이지는 않습니다.<br>
          <b>이 화면의 글꼴에서 몇 단이 진짜인지</b>는 글꼴마다 다릅니다. 시안에 '세미볼드'라고 적혀 있어도
          그 굵기의 파일을 받아 오지 않았다면 화면에서는 볼드와 구별되지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "글자 굵기, 굵기, 웨이트"),
    ("영어", "font weight, weight, bold, regular"),
    ("같이 쓰는 말",
     "100~900 사이의 숫자로 나타낸 굵기를 <b>웨이트</b>라고 하며, 이름으로 부르면 가는 것부터 <b>Thin · Light · Regular · Medium · "
     "SemiBold · Bold · Black</b> 순입니다. 글꼴 파일이 없어서 브라우저가 만들어 내는 굵기는 "
     "<b>가짜 굵게</b>(synthetic bold · faux bold), 파일 하나로 모든 굵기를 내는 글꼴은 "
     "<b>가변 글꼴</b>(variable font)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>&lt;b&gt;</code>와 <code>&lt;strong&gt;</code></b> — 굵기는 생김새일 뿐이지만 "
     "<code>strong</code>은 <b>중요하다는 뜻</b>을 나타내기 때문에 스크린 리더가 둘을 다르게 읽습니다.<br>"
     "<b>볼드</b> — 보통 700을 가리키지만, 글꼴에 따라서는 600을 '볼드'라고 부르기도 합니다.<br>"
     "<b>굵기와 크기</b> — 둘 다 강조 수단이지만, 크기와 달리 <b>굵기는 바꿔도 줄 높이가 그대로입니다</b>."),
  ]),
  axes=ax("글자 굵기"),
  oneline="굵기는 400·500·700, <b>세 단이면 충분합니다</b>. 단을 하나 늘릴 때마다 내려받을 글꼴 파일도 한 벌씩 늘어나기 때문입니다.",
  s4_title="단", s4_hint="실제로 쓰는 것은 세 단",
  states=states([
    (wt(400, "400 · Regular", "본문"), "400", "기본 굵기입니다. <b>글의 대부분</b>을 이 굵기로 씁니다"),
    (wt(500, "500 · Medium", "살짝 강조"), "500", "라벨과 줄 제목에 써서 <b>살짝 강조</b>합니다"),
    (wt(700, "700 · Bold", "제목 · 버튼"), "700", "제목과 버튼에 씁니다. 이보다 더 굵게 쓸 일은 드뭅니다"),
    (wt(300, "300 · Light", "얇게"), "300", "큰 제목에만 씁니다. <b>본문에 쓰면 글자가 흐려 보입니다</b>"),
    (wt(900, "900 · Black", "아주 굵게", 18), "900", "표지나 큰 숫자에 씁니다. 한글은 획이 많아서 조금만 굵어져도 <b>뭉개져 보입니다</b>"),
    ('''              <div style="display:grid;gap:5px;justify-items:center;text-align:center">
                <span style="font-size:16px;font-weight:700;-webkit-text-stroke:0.3px currentColor">정산 확정</span>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">가짜 굵게</span>
                <span style="font-size:10px;color:var(--fg-faint)">파일이 없어 흉내 낸 것</span>
              </div>''',
     "가짜 굵게", "획이 <b>뭉개지고 번져</b> 보이는데, 획이 많은 한글에서 특히 눈에 띕니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("400 Regular", "font-weight: 400", "본문에 쓰는 <b>기본값</b>으로, 글의 대부분이 이 굵기입니다"),
    ("500 Medium", "font-weight: 500", "줄 제목이나 라벨처럼 살짝 강조할 곳에 씁니다"),
    ("700 Bold", "font-weight: 700", "제목과 버튼에 씁니다. <code>&lt;b&gt;</code>와 <code>&lt;strong&gt;</code>도 기본으로 이 굵기입니다"),
    ("파일 한 벌", "@font-face", "굵기 하나마다 <b>파일이 하나</b>씩 필요해서, 굵기를 늘리면 그만큼 더 내려받아야 합니다"),
    ("가짜 굵게", "synthetic bold", "파일이 없으면 브라우저가 획을 <b>부풀려</b> 만들어 내기 때문에 글자가 뭉개져 보입니다"),
    ("가변 글꼴", "variable font", "<b>파일 하나로 100~900</b>을 모두 냅니다. 요즘은 한글 글꼴도 가변 글꼴로 나옵니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          한글에서는 <b>가짜 굵게가 특히 나쁘게 보입니다.</b> 한글은 획이 많아서 브라우저가 획을 부풀리면 자음 안쪽의
          빈 공간이 메워지고, 글자가 덩어리처럼 뭉개집니다. 영문은 가짜 굵게로 그려도 어느 정도 읽을 만하지만
          한글은 바로 티가 나기 때문에, <b>쓸 굵기의 파일은 반드시 받아 와야</b> 합니다.</p>''',
  do=ul([
    "<b>크기를 바꾸지 않고</b> 강조할 때. 굵기만 바꾸면 줄 높이가 그대로라 레이아웃이 흔들리지 않습니다",
    "표의 머리글이나 줄 제목, 버튼 글자를 본문과 구별할 때",
    "같은 글자 크기 안에서 <b>위계를 한 단계 더</b> 만들고 싶을 때",
  ]),
  dont=ul([
    "<b>굵기를 다섯 단 넘게</b> 둘 때. 내려받을 파일만 늘고, 화면에서는 단끼리 구별되지 않습니다",
    "본문 전체를 300(Light)으로 쓸 때. 작은 글자에서는 획이 <b>흐려 보여 읽기 힘듭니다</b>",
    "중요한 내용을 <code>&lt;b&gt;</code>로 굵게만 할 때. 중요하다는 뜻을 담으려면 <code>&lt;strong&gt;</code>을 씁니다",
    "받아 오지 않는 굵기를 시안에 적을 때. 화면에서는 그 굵기가 <b>가짜 굵게</b>로 그려집니다",
  ]),
  instead='크기로 위계를 만들려면 <a href="../items/typescale.html">타입 스케일</a>, 크기·굵기·색을 함께 쓰려면 <a href="hierarchy.html">글자 위계</a>, 파일 문제는 <a href="webfont.html">웹폰트</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:3px">
                <span style="font-size:14px;font-weight:700">정산 요청 #4821</span>
                <span style="font-size:12px;font-weight:400;color:var(--fg-muted)">11월 1일 ~ 11월 7일</span>
              </div>''',
     "줄 제목", "<b>700과 400</b> 두 단만으로도 제목과 부가 정보의 위계를 만들 수 있습니다"),
    ('''              <div style="width:100%;max-width:180px;display:flex;gap:6px">
                <span style="background:var(--accent);color:#fff;border-radius:6px;padding:7px 13px;font-size:12px;font-weight:700">확정</span>
                <span style="border:1px solid var(--line-strong);border-radius:6px;padding:7px 13px;font-size:12px;font-weight:500">나중에</span>
              </div>''',
     "버튼", "주 버튼은 700, 보조 버튼은 500으로 써서 <b>색뿐 아니라 굵기로도</b> 둘을 나눕니다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:4px;font-size:11.5px">
                <span style="font-weight:700;color:var(--fg-muted);letter-spacing:.04em">가맹점</span>
                <span style="font-weight:400">모란상회</span>
                <span style="font-weight:400">한빛아웃도어</span>
              </div>''',
     "표 머리글", "머리글만 굵게 씁니다. 굵기를 바꿔도 <b>줄 높이가 그대로라</b> 표의 행 높이가 흔들리지 않습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="굵기를 적고 받아 오는 규칙",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="굵기는 <b>숫자로</b> 적습니다. <code>bold</code>는 700을 가리키는 다른 이름이라서 500이나 600 같은 중간 단은 나타낼 수 없습니다.",
  code='''<span class="c">/* 받아 올 굵기만 적는다. 굵기 하나에 파일 하나가 필요하다 */</span>
<span class="t">@font-face</span> {
  <span class="a">font-family</span>: <span class="s">"Pretendard"</span>;
  <span class="a">font-weight</span>: <span class="a">400</span>;
  <span class="a">src</span>: <span class="t">url</span>(<span class="s">"pretendard-400.woff2"</span>) <span class="t">format</span>(<span class="s">"woff2"</span>);
}
<span class="t">@font-face</span> { <span class="a">font-weight</span>: <span class="a">700</span>; <span class="a">src</span>: <span class="t">url</span>(<span class="s">"pretendard-700.woff2"</span>); … }

<span class="c">/* 가변 글꼴이면 한 벌로 끝난다 */</span>
<span class="t">@font-face</span> {
  <span class="a">font-weight</span>: <span class="a">100 900</span>;          <span class="c">/* 범위로 적는다 */</span>
  <span class="a">src</span>: <span class="t">url</span>(<span class="s">"pretendard-var.woff2"</span>) <span class="t">format</span>(<span class="s">"woff2-variations"</span>);
}

<span class="c">/* 브라우저가 가짜 굵게를 만들지 못하게 막을 수도 있다 */</span>
<span class="t">body</span> { <span class="a">font-synthesis</span>: none; }''',
  keys=kbd([
    ("숫자로 적는다", "<code>700</code>처럼 숫자로 씁니다. <code>bold</code>로는 중간 단을 가리킬 수 없기 때문입니다"),
    ("쓸 굵기만 받는다", "굵기 하나마다 <b>파일이 하나</b>씩 필요하고, 한글 글꼴은 한 벌이 수백 KB나 됩니다"),
    ("가변 글꼴을 본다", "파일 하나로 모든 굵기를 낼 수 있으면 <b>굵기를 늘려도 내려받을 파일이 늘지 않습니다</b>"),
    ("<code>&lt;strong&gt;</code>은 뜻", "굵게 보이게만 하려면 CSS로 굵기를 주고, <b>중요하다는 뜻</b>을 담을 때만 strong을 씁니다"),
    ("가짜 굵게를 확인한다", "파일이 없는 굵기를 쓰면 <b>한글이 뭉개지므로</b>, 화면에서 직접 눈으로 확인합니다"),
    ("단을 세 개로", "400·500·700 세 단으로 시작하고, 단을 늘리기 전에 화면에서 <b>정말 구별되는지</b> 확인합니다"),
  ]),
  backend=rows([
    ("굵기 = 파일 수", "굵기를 하나 늘리면 내려받을 글꼴 파일도 한 벌 늘어납니다. 한글 글꼴은 한 벌이 <b>수백 KB</b>나 되기 때문에, 굵기를 늘릴수록 첫 화면이 뜨는 속도가 느려집니다."),
    ("가변 글꼴의 손익", "가변 글꼴은 파일 하나로 모든 굵기를 내지만, 굵기 하나짜리 파일보다 <b>파일 자체가 더 큽니다.</b> 그래서 굵기를 셋 이상 쓸 때부터 이득입니다."),
    ("시안과 현실", "디자인 도구에서는 글꼴의 모든 굵기를 고를 수 있지만, 웹 화면에는 받아 온 굵기만 제대로 나옵니다. <b>실제로 받아 오는 굵기 목록</b>을 디자이너와 먼저 합의해 두면 '세미볼드가 안 나와요' 같은 일이 생기지 않습니다."),
    ("메일·PDF", "메일이나 PDF처럼 웹폰트를 쓸 수 없는 곳에서는 <b>굵기 두 단</b>(400·700)만 제대로 나온다고 보고 화면을 짭니다."),
  ]),
  plat_lede="세 플랫폼 모두 굵기를 단으로 나누지만, 기본 글꼴에 들어 있는 단의 수가 서로 다릅니다.",
  plats=plats([
    ("웹", "font-weight",
     wt(700, "700", "", 14),
     "100~900 사이의 숫자로 적고, 그 굵기의 파일이 없으면 브라우저가 <b>가짜 굵게</b>로 흉내 냅니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.fontWeight(.semibold)<br>.bold( )</div>''',
     "굵기를 <b>이름</b>으로 고릅니다(.regular/.medium/.semibold/.bold). 시스템 글꼴에 모든 단이 들어 있어서 가짜 굵게가 생기지 않습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FontWeight.Medium<br>FontWeight.W500</div>''',
     "<b>이름과 숫자</b>를 모두 씁니다. 기기에 없는 단은 안드로이드도 흉내 내서 그리므로, 쓸 굵기의 폰트 파일을 앱에 함께 넣습니다."),
  ]),
  plat_note="<b>\"굵기를 하나 더 쓰면 파일도 하나 더 받아야 한다\"</b>는 비용은 웹에서만 눈에 띕니다. 두 모바일 OS는 시스템 글꼴에 단이 모두 들어 있어서 \"세미볼드로 해 주세요\"라는 요청에 따로 드는 비용이 없습니다. 그래서 같은 요청이라도 웹에서는 <b>화면이 뜨는 속도</b>까지 함께 따져야 합니다.",
  siblings=siblings("weight"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/hierarchy.html"><b>글자 위계</b><em>3부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>''',
)
