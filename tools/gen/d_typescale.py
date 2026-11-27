# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def step(px, name, use, w=700):
    return ('              <div style="display:grid;gap:5px;justify-items:center;text-align:center">'
            '<span style="font-size:%spx;font-weight:%s;line-height:1.2">가나다</span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">%s</span>'
            '<span style="font-size:10.5px;color:var(--fg-faint)">%s</span></div>') % (px, w, name, use)

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:14px 10px 14px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-size:22px;font-weight:800;line-height:1.25;letter-spacing:-.02em">정산이 확정되었습니다</div>
                  <div class="pin-out" data-pin="2" style="font-size:13.5px;line-height:1.75;color:var(--fg-muted);max-width:250px">행간은 글자 크기에 딸려 옵니다. 큰 글자는 좁게, 작은 글자는 넓게 둡니다.</div>
                  <div class="pin-out" data-pin="3" style="font-size:13.5px;letter-spacing:.06em;color:var(--fg-muted)">자간을 넓힌 작은 제목</div>
                  <div class="pin-out" data-pin="4" style="font-size:13.5px;font-weight:800">굵기로 주는 강조</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:13.5px;font-variant-numeric:tabular-nums">₩1,284,000<br>₩&nbsp;&nbsp;982,500</div>
                </div>
              </div>'''

D = dict(
  slug="typescale", ko="타입 스케일", en="Type scale · typographic scale",
  desc="글자 크기를 비율로 정해 단계를 만드는 방법과, 크기 하나가 아니라 행간·자간·굵기가 한 묶음이라는 것을 보여주는 항목.",
  lede="글자 크기를 <b>비율로 쌓아 만든 사다리</b>. 17·19·23을 그때그때 고르지 않고, 정해 둔 단 중에서 고릅니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>비율을 바꾸면 <b>모든 단이 같이</b> 움직입니다 — 기준 16px 에 비율을 거듭 곱한 값이기 때문입니다.
          <b>규칙 없이</b>를 켜면 17·19·23처럼 손으로 고른 값이 됩니다. 각각은 멀쩡한데
          나란히 놓으면 <b>어느 쪽이 더 중요한지가 안 읽힙니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "타입 스케일, 글자 크기 체계, 폰트 스케일"),
    ("영어", "type scale, typographic scale, modular scale"),
    ("같이 쓰는 말",
     "곱하는 값을 <b>비율</b>(ratio · 1.125·1.25·1.333), 기준이 되는 크기를 <b>기준 크기</b>(base) 라고 합니다. "
     "단 하나를 <b>스텝</b>(step) 또는 <b>타입 토큰</b>이라 하고, 크기·행간·굵기를 묶은 것을 "
     "<b>텍스트 스타일</b>(text style · type style)이라 합니다."),
    ("자주 잘못 부름",
     "<b>폰트 크기</b> — 크기 하나만 가리키는 말입니다. 스케일은 <b>단들 사이의 관계</b>입니다.<br>"
     "<b>헤딩 레벨</b> — <code>h1~h6</code>은 문서의 <b>구조</b>이고 크기와는 별개입니다. "
     "<code>h2</code>를 작게 쓰는 화면도 정상입니다.<br>"
     "<b>모듈러 스케일</b> — 같은 뜻으로 쓰이지만, 엄밀히는 비율을 거듭 곱해 만든 것만 가리킵니다."),
  ]),
  axes=ax("타입 스케일"),
  oneline="타입 스케일은 <b>크기 목록이 아니라 비율</b>입니다. 두 단을 나란히 놓았을 때 차이가 늘 같은 몫이면 스케일이고, 들쭉날쭉하면 그냥 값 모음입니다.",
  s4_title="단", s4_hint="단마다 맡은 일이 있다",
  states=states([
    (step(10, "text-xs", "라벨 · 캡션", 600), "10~11px", "표의 머리글, 사진 설명. <b>본문으로 쓰면 안 된다</b>"),
    (step(13, "text-sm", "보조 글", 500), "13px", "날짜, 메타 정보. 한국어는 영문보다 한 단 크게 본다"),
    (step(16, "text-base", "본문", 500), "16px", "기본. 폰에서 16px 보다 작으면 <b>확대가 일어난다</b>"),
    (step(20, "text-lg", "작은 제목", 700), "20px", "카드 제목, 구역 제목"),
    (step(25, "text-xl", "화면 제목", 800), "25px", "한 화면에 하나"),
    (step(31, "text-2xl", "표지 · 숫자", 800), "31px+", "금액처럼 <b>한눈에 보여야 하는</b> 숫자"),
  ]),
  anat=ANAT,
  pins=pins([
    ("크기", "font-size", "사다리에서 고른 단. <b>이것 하나만 토큰이 아니다</b>"),
    ("행간", "line-height", "줄 사이. 큰 글자는 <b>좁게</b>(1.2), 본문은 <b>넓게</b>(1.6~1.8). 한국어는 영문보다 더 넓게 본다"),
    ("자간", "letter-spacing", "글자 사이. 큰 제목은 좁히고(-0.02em), 작은 대문자 라벨은 넓힌다"),
    ("굵기", "font-weight", "400·500·700 세 단이면 보통 충분하다. 굵기로 주는 강조가 크기보다 조용하다"),
    ("숫자 꼴", "tabular-nums", "금액을 세로로 쌓을 때 자릿수가 맞게. <b>표에서 거의 필수</b>인데 가장 안 알려져 있다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          타입 토큰은 <b>크기 하나가 아니라 다섯 개의 묶음</b>입니다. 크기만 바꾸고 행간을 그대로 두면
          제목이 답답해지고 본문이 흩어집니다. 그래서 디자인 시스템은 <code>text-lg</code> 한 이름 안에
          크기와 행간을 함께 담아 둡니다.</p>''',
  do=ul([
    "제목·본문·보조 글의 <b>위계를 눈으로</b> 알게 하고 싶을 때",
    "여러 사람이 화면을 만들 때 — 매번 고르지 않아도 됩니다",
    "글이 많은 화면 — 문서, 기사, 설명",
  ]),
  dont=ul([
    "단을 <b>열 개 넘게</b> 두는 것 — 고를 수 없게 되고 결국 아무 값이나 쓰게 됩니다",
    "비율을 크게(1.5 이상) 잡고 단을 많이 두는 것 — 가운데가 비어 쓸 단이 없어집니다",
    "본문 크기를 14px 아래로 — 한국어는 획이 많아 같은 크기라도 더 작게 보입니다",
    "크기만으로 모든 위계를 주는 것 — 굵기와 색이 더 조용하고 잘 듣습니다",
  ]),
  instead='줄 간격과 묶음 간격은 <a href="spacing.html">간격 체계</a>가 맡고, 글자색의 위계는 <a href="color.html">색 토큰</a>이 맡습니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:3px;width:100%;max-width:230px">
                <div style="font-size:19px;font-weight:800;line-height:1.3">11월 정산 내역</div>
                <div style="font-size:13px;color:var(--fg-muted)">2026년 11월 1일 ~ 11월 7일</div>
                <div style="font-size:14px;line-height:1.7;margin-top:6px">확정하면 영업일 기준 2일 안에 입금됩니다.</div>
              </div>''',
     "제목 · 부제 · 본문", "세 단이면 위계가 선다. <b>네 단 이상 쌓지 않는다</b>"),
    ('''              <div style="display:grid;gap:4px;width:100%;max-width:230px;font-variant-numeric:tabular-nums">
                <div style="font-size:11px;color:var(--fg-muted);letter-spacing:.06em">이번 주 매출</div>
                <div style="font-size:28px;font-weight:800;line-height:1.1">₩1,284,000</div>
                <div style="font-size:12px;color:#1f8a4c">지난주보다 +12.4%</div>
              </div>''',
     "스탯 타일", "라벨은 작게, 숫자는 크게. <b>차이가 클수록</b> 잘 읽힌다"),
    ('''              <div style="display:grid;gap:5px;width:100%;max-width:230px">
                <div style="font-size:17px;font-weight:700">17px 제목</div>
                <div style="font-size:15px">15px 부제</div>
                <div style="font-size:13px;color:var(--fg-muted)">13px 본문</div>
                <div style="font-size:11px;color:var(--danger);margin-top:4px">단 사이가 너무 좁아 위계가 안 보인다</div>
              </div>''',
     "흔한 실패", "17·15·13은 차이가 2px 씩이라 <b>셋이 거의 같아 보인다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 사다리의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="단마다 <b>크기와 행간을 한 묶음</b>으로 둡니다. 크기만 토큰으로 두면 쓰는 쪽에서 행간을 매번 다시 고르게 됩니다.",
  code='''<span class="t">:root</span> {
  <span class="c">/* 16px 에 1.25 를 거듭 곱한다 */</span>
  <span class="a">--text-sm</span>: <span class="s">12.8px</span>;   <span class="a">--lh-sm</span>: <span class="s">1.7</span>;
  <span class="a">--text-base</span>: <span class="s">16px</span>;   <span class="a">--lh-base</span>: <span class="s">1.65</span>;
  <span class="a">--text-lg</span>: <span class="s">20px</span>;     <span class="a">--lh-lg</span>: <span class="s">1.4</span>;
  <span class="a">--text-xl</span>: <span class="s">25px</span>;     <span class="a">--lh-xl</span>: <span class="s">1.25</span>;
}

<span class="t">.card-title</span> {
  <span class="a">font-size</span>: <span class="t">var</span>(<span class="a">--text-lg</span>);
  <span class="a">line-height</span>: <span class="t">var</span>(<span class="a">--lh-lg</span>);
  <span class="a">word-break</span>: keep-all;   <span class="c">/* 한국어는 어절로 끊는다 */</span>
}

<span class="c">/* 폰에서 본문이 16px 아래면 입력 중 화면이 확대된다 */</span>
<span class="t">input</span>, <span class="t">select</span>, <span class="t">textarea</span> { <span class="a">font-size</span>: <span class="s">16px</span>; }''',
  keys=kbd([
    ("기준과 비율을 먼저", "기준 16px, 비율 1.2~1.333 사이. <b>두 수만 정하면</b> 나머지는 계산이다"),
    ("크기와 행간을 함께", "<code>--text-lg</code> 하나를 쓰면 행간도 따라오게 묶어 둔다"),
    ("단은 6~8개", "열 개가 넘으면 고를 수 없고, 넷 이하면 위계가 모자란다"),
    ("한국어는 한 단 크게", "같은 px 이라도 한글은 획이 많아 작아 보인다. 영문 기준 시안을 그대로 쓰면 빽빽해진다"),
    ("<code>rem</code>으로 적는다", "사용자가 브라우저 글자 크기를 키웠을 때 같이 커진다. <code>px</code>로 박으면 안 커진다"),
    ("입력창은 16px 이상", "iOS 사파리는 그보다 작으면 <b>입력할 때 화면을 확대</b>한다"),
  ]),
  backend=rows([
    ("스케일 = 상수 테이블", "매직 넘버를 상수로 뽑은 것과 같습니다. 다른 점은 값들 사이에 <b>계산식이 있다</b>는 것이라, 기준 하나를 바꾸면 전부 따라 움직입니다."),
    ("글자 길이는 데이터가 정한다", "'상품명'이 12자일 때와 60자일 때 화면이 다릅니다. <b>가장 긴 값</b>으로 한 번 그려 보지 않으면 제목 칸이 터집니다."),
    ("다국어", "같은 문장이 독일어에서 1.3배, 한국어에서 0.8배가 됩니다. 크기를 줄여 맞추지 말고 <b>줄바꿈과 말줄임</b>을 준비합니다."),
    ("폰트 파일", "굵기 하나가 파일 하나입니다. 400·700만 쓰면 두 벌, 거기에 500을 더하면 세 벌을 더 받습니다 — <b>굵기를 늘리는 것은 공짜가 아닙니다.</b>"),
  ]),
  plat_lede="세 플랫폼 모두 '이름 붙은 단'을 쓰지만, 이름과 개수가 다릅니다.",
  plats=plats([
    ("웹", "CSS · rem",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--text-sm<br>--text-base<br>--text-lg</div>''',
     "정해진 이름이 없어 팀마다 다릅니다. Tailwind 의 <code>text-sm · text-base · text-lg</code> 가 사실상 공통어가 됐습니다."),
    ("iOS", "Dynamic Type",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.largeTitle<br>.body<br>.caption</div>''',
     "<b>텍스트 스타일</b>이 OS 에 11단 정해져 있고, 사용자가 글자 크기를 키우면 <b>앱이 따라 커져야</b> 합니다(Dynamic Type)."),
    ("안드로이드", "Material 3 type scale",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">headlineLarge<br>bodyMedium<br>labelSmall</div>''',
     "<b>타입 스케일</b>이 Display·Headline·Title·Body·Label 다섯 갈래 × 세 크기로 규격화돼 있습니다."),
  ]),
  plat_note="두 OS 모두 사용자가 <b>시스템 글자 크기를 키울 수 있습니다.</b> 그 설정을 무시하고 px 로 박아 두면 접근성 심사에서 걸리고, 실제로 글자를 키워 쓰는 사람에게는 앱이 망가진 것처럼 보입니다. 시안에 \"16px\"이라고만 적혀 있으면 그게 <b>기본 설정일 때의 크기</b>라는 뜻인지 확인하세요.",
  siblings=siblings("typescale"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>행간과 글줄 길이</b><em>3부</em></span></li>
        <li><span class="na"><b>말줄임</b><em>3부</em></span></li>
        <li><span class="na"><b>한글 조판</b><em>3부</em></span></li>''',
)
