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
  desc="굵기 아홉 단과 실제로 쓰는 세 단, 가짜 굵게와 가변 글꼴을 실물과 해부도로 보여주는 항목.",
  lede="글자의 <b>두께</b>. 크기보다 조용한 강조 수단이고, 줄 높이를 안 바꿔서 레이아웃이 흔들리지 않습니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>체크를 풀어 아홉 단을 다 펼쳐 보세요. 아래에 <b>실제로 다르게 보이는 단이 몇 개인지</b> 재서 알려 줍니다 —
          받아 온 파일이 없는 단은 브라우저가 흉내 내거나 그냥 옆 단과 똑같이 그립니다.<br>
          <b>이 화면의 글꼴에서 몇 단이 진짜인지</b>는 글꼴마다 다릅니다. 시안에서 '세미볼드'라고 적혀 있어도
          그 파일을 안 받아 왔으면 화면에서는 볼드와 구별이 안 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "글자 굵기, 굵기, 웨이트"),
    ("영어", "font weight, weight, bold, regular"),
    ("같이 쓰는 말",
     "100~900의 숫자를 <b>웨이트</b>라 하고, 이름으로는 <b>Thin · Light · Regular · Medium · "
     "SemiBold · Bold · Black</b> 순입니다. 파일이 없어 브라우저가 만들어 내는 굵기를 "
     "<b>가짜 굵게</b>(synthetic bold · faux bold), 한 파일로 모든 굵기를 내는 것을 "
     "<b>가변 글꼴</b>(variable font)이라 합니다."),
    ("자주 잘못 부름",
     "<b><code>&lt;b&gt;</code>와 <code>&lt;strong&gt;</code></b> — 굵기는 생김새이고 "
     "<code>strong</code>은 <b>중요하다는 뜻</b>입니다. 스크린 리더가 다르게 읽습니다.<br>"
     "<b>볼드</b> — 보통 700을 가리키지만 글꼴에 따라 600이 '볼드'인 경우도 있습니다.<br>"
     "<b>굵기와 크기</b> — 둘 다 강조 수단이지만 <b>굵기는 줄 높이를 안 바꿉니다</b>."),
  ]),
  axes=ax("글자 굵기"),
  oneline="굵기는 <b>세 단이면 충분합니다</b> — 400·500·700. 단을 늘리면 글꼴 파일이 한 벌씩 따라옵니다.",
  s4_title="단", s4_hint="실제로 쓰는 것은 세 단",
  states=states([
    (wt(400, "400 · Regular", "본문"), "400", "기본. <b>글의 대부분</b>이 이 굵기다"),
    (wt(500, "500 · Medium", "살짝 강조"), "500", "라벨·줄 제목. <b>조용한 강조</b>"),
    (wt(700, "700 · Bold", "제목 · 버튼"), "700", "제목과 버튼. 더 굵게 갈 일은 드물다"),
    (wt(300, "300 · Light", "얇게"), "300", "큰 제목에만. <b>본문에 쓰면 흐려 보인다</b>"),
    (wt(900, "900 · Black", "아주 굵게", 18), "900", "표지·숫자. 한글은 획이 많아 <b>금세 뭉개진다</b>"),
    ('''              <div style="display:grid;gap:5px;justify-items:center;text-align:center">
                <span style="font-size:16px;font-weight:700;-webkit-text-stroke:0.3px currentColor">정산 확정</span>
                <span style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">가짜 굵게</span>
                <span style="font-size:10px;color:var(--fg-faint)">파일이 없어 흉내 낸 것</span>
              </div>''',
     "가짜 굵게", "획이 <b>뭉개지고 번져</b> 보인다. 한글에서 특히 티가 난다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("400 Regular", "font-weight: 400", "본문. <b>기본값</b>이고 글의 대부분을 차지한다"),
    ("500 Medium", "font-weight: 500", "살짝 강조. 줄 제목·라벨에 쓴다"),
    ("700 Bold", "font-weight: 700", "제목·버튼. <code>&lt;b&gt;</code>와 <code>&lt;strong&gt;</code>의 기본값"),
    ("파일 한 벌", "@font-face", "굵기 하나가 <b>파일 하나</b>다. 늘리면 그만큼 더 받아야 한다"),
    ("가짜 굵게", "synthetic bold", "파일이 없으면 브라우저가 획을 <b>부풀려</b> 만든다 — 뭉개져 보인다"),
    ("가변 글꼴", "variable font", "<b>한 파일로 100~900</b> 전부. 요즘 한글 글꼴도 가변으로 나온다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          한글은 <b>가짜 굵게가 특히 나쁩니다.</b> 획이 많아서 브라우저가 부풀리면 자음 안쪽의
          빈 공간이 메워져 글자가 덩어리로 뭉개집니다. 영문은 어느 정도 봐줄 만하지만
          한글은 바로 티가 나서, <b>쓸 굵기의 파일은 반드시 받아 와야</b> 합니다.</p>''',
  do=ul([
    "<b>크기를 안 바꾸고</b> 강조할 때 — 줄 높이가 안 흔들립니다",
    "표의 머리글, 줄 제목, 버튼 글자",
    "같은 크기 안에서 <b>층을 하나 더</b> 만들고 싶을 때",
  ]),
  dont=ul([
    "<b>굵기를 다섯 단 넘게</b> 두는 것 — 파일만 늘고 구별은 안 됩니다",
    "본문 전체를 300(Light)으로 — 작은 글자에서 <b>흐려 읽기 힘듭니다</b>",
    "<code>&lt;b&gt;</code>를 뜻 없이 쓰는 것 — 중요하면 <code>&lt;strong&gt;</code>입니다",
    "파일 없는 굵기를 시안에 적는 것 — 화면에서는 <b>가짜 굵게</b>가 됩니다",
  ]),
  instead='크기로 층을 만들려면 <a href="../items/typescale.html">타입 스케일</a>, 셋을 함께 쓰려면 <a href="hierarchy.html">글자 위계</a>, 파일 문제는 <a href="webfont.html">웹폰트</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:3px">
                <span style="font-size:14px;font-weight:700">정산 요청 #4821</span>
                <span style="font-size:12px;font-weight:400;color:var(--fg-muted)">11월 1일 ~ 11월 7일</span>
              </div>''',
     "줄 제목", "<b>700과 400</b> 두 단만으로 위계가 선다"),
    ('''              <div style="width:100%;max-width:180px;display:flex;gap:6px">
                <span style="background:var(--accent);color:#fff;border-radius:6px;padding:7px 13px;font-size:12px;font-weight:700">확정</span>
                <span style="border:1px solid var(--line-strong);border-radius:6px;padding:7px 13px;font-size:12px;font-weight:500">나중에</span>
              </div>''',
     "버튼", "주 버튼 700, 보조 500. <b>색만이 아니라 굵기로도</b> 나눈다"),
    ('''              <div style="width:100%;max-width:180px;display:grid;gap:4px;font-size:11.5px">
                <span style="font-weight:700;color:var(--fg-muted);letter-spacing:.04em">가맹점</span>
                <span style="font-weight:400">모란상회</span>
                <span style="font-weight:400">한빛아웃도어</span>
              </div>''',
     "표 머리글", "머리글만 굵게. <b>줄 높이가 안 바뀌어</b> 표가 안 흔들린다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 글꼴의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="굵기는 <b>숫자로</b> 적습니다. <code>bold</code>는 700의 다른 이름일 뿐이고, 중간 단을 못 가리킵니다.",
  code='''<span class="c">/* 받아 올 굵기만 적는다 — 하나가 파일 하나다 */</span>
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

<span class="c">/* 흉내 내지 말라고 막을 수도 있다 */</span>
<span class="t">body</span> { <span class="a">font-synthesis</span>: none; }''',
  keys=kbd([
    ("숫자로 적는다", "<code>700</code>이라고 쓴다. <code>bold</code>는 중간 단을 못 가리킨다"),
    ("쓸 굵기만 받는다", "굵기 하나가 <b>파일 하나</b>. 한글은 한 벌이 수백 KB 다"),
    ("가변 글꼴을 본다", "한 파일로 전부 되면 <b>굵기를 늘려도 공짜</b>가 된다"),
    ("<code>&lt;strong&gt;</code>은 뜻", "굵게 보이려면 CSS 로. <b>중요하다는 뜻</b>일 때만 strong"),
    ("가짜 굵게를 확인한다", "파일 없는 굵기를 쓰면 <b>한글이 뭉개진다</b>. 눈으로 한 번 본다"),
    ("단을 세 개로", "400·500·700. 늘리기 전에 <b>정말 구별되는지</b> 재 본다"),
  ]),
  backend=rows([
    ("굵기 = 파일 수", "굵기를 하나 늘리면 내려받을 파일이 한 벌 늘어납니다. 한글 한 벌이 <b>수백 KB</b>라 첫 화면 속도에 바로 영향이 옵니다."),
    ("가변 글꼴의 손익", "한 파일로 모든 굵기를 내지만 <b>파일 자체는 더 큽니다.</b> 굵기를 셋 이상 쓸 때부터 이득입니다."),
    ("시안과 현실", "디자인 도구에는 모든 굵기가 보입니다. <b>실제로 받아 오는 굵기 목록</b>을 디자이너와 먼저 합의해 두면 '세미볼드가 안 나와요'가 없어집니다."),
    ("메일·PDF", "웹폰트를 못 쓰는 곳에서는 <b>굵기 두 단</b>(400·700)만 믿을 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 숫자 단을 쓰고, 기본 글꼴이 가진 단 수가 다릅니다.",
  plats=plats([
    ("웹", "font-weight",
     wt(700, "700", "", 14),
     "100~900. 파일이 없으면 <b>가짜 굵게</b>로 흉내 냅니다."),
    ("iOS", "Apple HIG",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.fontWeight(.semibold)<br>.bold( )</div>''',
     "<b>이름</b>으로 고릅니다(.regular/.medium/.semibold/.bold). 시스템 글꼴에 단이 다 들어 있어 가짜 굵게가 없습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FontWeight.Medium<br>FontWeight.W500</div>''',
     "<b>이름과 숫자</b>를 다 씁니다. 기기에 없는 단은 역시 흉내 내므로 폰트를 함께 넣습니다."),
  ]),
  plat_note="웹에서만 <b>\"굵기 하나 더 쓰면 파일이 하나 더\"</b>라는 비용이 눈에 띕니다. 두 OS 는 시스템 글꼴에 단이 다 들어 있어서 \"세미볼드로 해 주세요\"가 공짜입니다. 같은 요청인데 웹에서만 <b>속도 이야기</b>가 되는 이유입니다.",
  siblings=siblings("weight"),
  related='''        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="../items/hierarchy.html"><b>글자 위계</b><em>3부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/hangul.html"><b>한글 조판</b><em>3부</em></a></li>''',
)
