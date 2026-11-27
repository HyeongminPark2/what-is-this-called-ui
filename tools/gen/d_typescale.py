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
  desc="글자 크기를 비율로 정해 단계를 만드는 방법과, 각 단계가 크기 하나가 아니라 행간·자간·굵기까지 묶은 것이라는 점을 보여 주는 항목입니다.",
  lede="타입 스케일은 기준 글자 크기에 <b>일정한 비율을 거듭 곱해 만든 크기 단계</b>입니다. 글자 크기가 필요할 때마다 17, 19, 23처럼 그때그때 고르지 않고, 미리 정해 둔 단 가운데서 고릅니다.",
  axes_lede="토큰은 부품이 아니라 <b>값을 쓰는 규칙</b>입니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>비율을 바꾸면 <b>모든 단이 함께</b> 바뀝니다. 각 단이 기준 16px에 비율을 거듭 곱한 값이기 때문입니다.
          <b>규칙 없이</b>를 켜면 17, 19, 23처럼 손으로 고른 값으로 바뀌는데, 값 하나하나는 문제가 없어도
          나란히 놓으면 단 사이의 차이가 들쭉날쭉해서 <b>어느 쪽이 더 중요한지 알아보기 어렵습니다.</b></p>
        </div>''',
  names=rows([
    ("한국어", "타입 스케일, 글자 크기 체계, 폰트 스케일"),
    ("영어", "type scale, typographic scale, modular scale"),
    ("같이 쓰는 말",
     "거듭 곱하는 값은 <b>비율</b>(ratio · 1.125·1.25·1.333), 출발점이 되는 크기는 <b>기준 크기</b>(base)라고 합니다. "
     "단 하나하나는 <b>스텝</b>(step) 또는 <b>타입 토큰</b>이라 부르고, 크기와 행간, 굵기를 한데 묶은 것은 "
     "<b>텍스트 스타일</b>(text style · type style)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>폰트 크기</b> — 폰트 크기는 글자 크기 값 하나를 가리키는 말이고, 스케일은 <b>단과 단 사이의 관계</b>까지 정한 것입니다.<br>"
     "<b>헤딩 레벨</b> — <code>h1~h6</code>은 문서의 <b>구조</b>를 나타낼 뿐 글자 크기와는 별개입니다. "
     "그래서 <code>h2</code>를 작은 글자로 보여 주는 화면도 잘못된 것이 아닙니다.<br>"
     "<b>모듈러 스케일</b> — 타입 스케일과 같은 뜻으로 쓰이기도 하지만, 엄밀히는 비율을 거듭 곱해 만든 스케일만 가리킵니다."),
  ]),
  axes=ax("타입 스케일"),
  oneline="타입 스케일의 핵심은 <b>크기 목록이 아니라 비율</b>입니다. 이웃한 두 단을 나란히 놓았을 때 큰 쪽이 늘 작은 쪽의 같은 배수라면 스케일이고, 배수가 들쭉날쭉하면 스케일이 아니라 크기 값을 모아 둔 목록입니다.",
  s4_title="크기 단계별 쓰임", s4_hint="단마다 정해 둔 크기와 그 크기를 쓰는 자리",
  states=states([
    (step(10, "text-xs", "라벨 · 캡션", 600), "10~11px 라벨", "표의 머리글이나 사진 설명에 씁니다. 너무 작아서 <b>본문에는 쓰지 않습니다</b>"),
    (step(13, "text-sm", "보조 글", 500), "13px 보조 글", "날짜나 메타 정보에 씁니다. 한국어는 영문보다 한 단 크게 잡습니다"),
    (step(16, "text-base", "본문", 500), "16px 본문", "본문의 기본 크기입니다. 폰에서는 입력창 글자가 16px보다 작으면 <b>화면이 저절로 확대됩니다</b>"),
    (step(20, "text-lg", "작은 제목", 700), "20px 작은 제목", "카드 제목이나 구역 제목에 씁니다"),
    (step(25, "text-xl", "화면 제목", 800), "25px 화면 제목", "한 화면에 하나만 씁니다"),
    (step(31, "text-2xl", "표지 · 숫자", 800), "31px 이상 큰 숫자", "금액처럼 <b>한눈에 보여야 하는</b> 숫자에 씁니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("크기", "font-size", "스케일에서 고른 단입니다. 다만 <b>크기 하나만으로 타입 토큰이 되지는 않습니다</b>"),
    ("행간", "line-height", "줄과 줄 사이의 간격입니다. 큰 글자는 <b>좁게</b>(1.2), 본문은 <b>넓게</b>(1.6~1.8) 두고, 한국어는 영문보다 더 넓게 잡습니다"),
    ("자간", "letter-spacing", "글자와 글자 사이의 간격입니다. 큰 제목은 좁히고(-0.02em), 작은 대문자 라벨은 넓힙니다"),
    ("굵기", "font-weight", "보통 400·500·700 세 단이면 충분합니다. 굵기로 주는 강조는 크기를 키우는 것보다 덜 두드러집니다"),
    ("숫자 꼴", "tabular-nums", "금액을 세로로 늘어놓을 때 자릿수가 맞도록 숫자 폭을 고르게 합니다. <b>표에서는 거의 필수</b>인데도 잘 알려져 있지 않습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          타입 토큰은 크기 하나가 아니라 위의 <b>다섯 가지 값을 한데 묶은 것</b>입니다. 크기만 바꾸고 행간을 그대로 두면
          제목은 답답해 보이고 본문은 줄이 흩어져 보입니다. 그래서 디자인 시스템은 <code>text-lg</code> 같은 이름 하나에
          크기와 행간을 함께 담아 둡니다.</p>''',
  do=ul([
    "제목과 본문, 보조 글의 <b>위계가 눈으로 바로</b> 드러나게 하고 싶을 때",
    "여러 사람이 화면을 만들 때. 정해 둔 단에서 고르면 되므로 사람마다 크기를 따로 정하지 않아도 됩니다",
    "문서나 기사, 설명처럼 글이 많은 화면일 때",
  ]),
  dont=ul([
    "단을 <b>열 개 넘게</b> 둘 때. 어느 단을 골라야 할지 정할 수 없어서 결국 아무 값이나 쓰게 됩니다",
    "비율을 1.5 이상으로 크게 잡고 단을 많이 둘 때. 이웃한 단의 차이가 너무 커서 자주 쓰는 중간 크기에 맞는 단이 없어집니다",
    "본문 크기를 14px보다 작게 잡을 때. 한국어는 획이 많아서 같은 크기라도 더 작게 보입니다",
    "크기만으로 모든 위계를 나타낼 때. 굵기와 색으로 위계를 주면 크기를 키우는 것보다 덜 요란하면서도 차이가 잘 드러납니다",
  ]),
  instead_title="타입 스케일과 함께 정하는 규칙",
  instead='글줄과 글줄 묶음 사이의 간격은 <a href="spacing.html">간격 체계</a>에서 정하고, 글자색으로 주는 위계는 <a href="color.html">색 토큰</a>에서 정합니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:3px;width:100%;max-width:230px">
                <div style="font-size:19px;font-weight:800;line-height:1.3">11월 정산 내역</div>
                <div style="font-size:13px;color:var(--fg-muted)">2026년 11월 1일 ~ 11월 7일</div>
                <div style="font-size:14px;line-height:1.7;margin-top:6px">확정하면 영업일 기준 2일 안에 입금됩니다.</div>
              </div>''',
     "제목과 부제, 본문을 세 단으로 나누기", "세 단이면 위계가 충분히 드러납니다. 한 덩어리 안에 <b>네 단 이상 쌓지 않습니다</b>"),
    ('''              <div style="display:grid;gap:4px;width:100%;max-width:230px;font-variant-numeric:tabular-nums">
                <div style="font-size:11px;color:var(--fg-muted);letter-spacing:.06em">이번 주 매출</div>
                <div style="font-size:28px;font-weight:800;line-height:1.1">₩1,284,000</div>
                <div style="font-size:12px;color:#1f8a4c">지난주보다 +12.4%</div>
              </div>''',
     "스탯 타일에서 숫자를 크게 보여 주기", "라벨은 작게, 숫자는 크게 씁니다. 두 크기의 <b>차이가 클수록</b> 숫자가 잘 읽힙니다"),
    ('''              <div style="display:grid;gap:5px;width:100%;max-width:230px">
                <div style="font-size:17px;font-weight:700">17px 제목</div>
                <div style="font-size:15px">15px 부제</div>
                <div style="font-size:13px;color:var(--fg-muted)">13px 본문</div>
                <div style="font-size:11px;color:var(--danger);margin-top:4px">단 사이가 너무 좁아 위계가 안 보임</div>
              </div>''',
     "단 사이를 너무 좁게 잡은 실패", "17·15·13px은 2px씩밖에 차이가 나지 않아서 <b>세 단이 거의 같아 보입니다</b>"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="스케일을 코드로 옮기는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
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
    ("기준 크기와 비율부터 정하기", "기준은 16px, 비율은 1.2~1.333 사이에서 고릅니다. <b>이 두 수만 정하면</b> 나머지 단은 계산으로 나옵니다"),
    ("크기와 행간을 한 토큰으로 묶기", "<code>--text-lg</code> 하나만 쓰면 행간도 함께 적용되도록 묶어 둡니다"),
    ("단은 6~8개로 두기", "열 개가 넘으면 어느 단을 써야 할지 고르기 어렵고, 넷 이하이면 위계를 나타내기에 단이 모자랍니다"),
    ("한국어는 한 단 크게 잡기", "같은 px이라도 한글은 획이 많아 작아 보이기 때문에, 영문 기준으로 만든 시안을 그대로 쓰면 글자가 빽빽해 보입니다"),
    ("<code>rem</code> 단위로 적기", "<code>rem</code>으로 적으면 사용자가 브라우저 글자 크기를 키웠을 때 함께 커지지만, <code>px</code>로 적으면 커지지 않습니다"),
    ("입력창 글자는 16px 이상으로 두기", "iOS 사파리는 입력창 글자가 16px보다 작으면 <b>입력할 때 화면을 확대</b>합니다"),
  ]),
  backend=rows([
    ("상수 테이블과 같은 역할", "코드의 매직 넘버를 상수로 뽑아 두는 것과 같은 일입니다. 다만 타입 스케일은 값들 사이에 <b>계산식이 있어서</b>, 기준 크기 하나를 바꾸면 모든 단이 함께 바뀝니다."),
    ("데이터에 따라 달라지는 글자 길이", "같은 '상품명' 칸이라도 12자일 때와 60자일 때 화면이 달라집니다. 그래서 들어올 수 있는 <b>가장 긴 값</b>으로 한 번 그려 보지 않으면 제목 칸이 넘쳐 레이아웃이 깨집니다."),
    ("언어마다 달라지는 글자 길이", "같은 문장이라도 언어에 따라 길이가 달라서 독일어에서는 1.3배, 한국어에서는 0.8배가 됩니다. 길어진 글을 글자 크기를 줄여 맞추지 말고 <b>줄바꿈과 말줄임</b>을 준비해 둡니다."),
    ("굵기마다 늘어나는 폰트 파일", "웹 폰트는 굵기 하나가 파일 하나입니다. 400과 700만 쓰면 파일 두 벌을 받고, 거기에 500을 더하면 세 벌을 받아야 합니다. 이처럼 <b>굵기를 하나 늘릴 때마다 내려받을 파일도 늘어납니다.</b>"),
  ]),
  plat_lede="세 플랫폼 모두 이름을 붙인 단을 쓰지만, 그 이름과 개수는 서로 다릅니다.",
  plats=plats([
    ("웹", "CSS · rem",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--text-sm<br>--text-base<br>--text-lg</div>''',
     "표준으로 정해진 이름이 없어서 팀마다 다르게 짓습니다. 다만 Tailwind의 <code>text-sm · text-base · text-lg</code>가 사실상 여러 팀이 함께 쓰는 이름이 되었습니다."),
    ("iOS", "Dynamic Type",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.largeTitle<br>.body<br>.caption</div>''',
     "<b>텍스트 스타일</b> 11단이 OS에 정해져 있습니다. 사용자가 시스템 글자 크기를 키우면 <b>앱의 글자도 함께 커져야</b> 합니다(Dynamic Type)."),
    ("안드로이드", "Material 3 type scale",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">headlineLarge<br>bodyMedium<br>labelSmall</div>''',
     "<b>타입 스케일</b>이 Display·Headline·Title·Body·Label 다섯 갈래마다 크기 세 가지씩으로 규격화돼 있습니다."),
  ]),
  plat_note="iOS와 안드로이드 모두 사용자가 <b>시스템 글자 크기를 키울 수 있습니다.</b> 이 설정을 무시하고 글자 크기를 px로 고정해 두면 접근성 심사에서 걸리고, 실제로 글자를 키워 쓰는 사람에게는 앱 화면이 깨진 것처럼 보입니다. 그래서 시안에 \"16px\"이라고만 적혀 있다면, 그 값이 <b>기본 설정일 때의 크기</b>라는 뜻인지 확인하세요.",
  siblings=siblings("typescale"),
  related='''        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><a href="lineheight.html"><b>행간과 글줄 길이</b><em>3부</em></a></li>
        <li><a href="truncate.html"><b>말줄임</b><em>3부</em></a></li>
        <li><a href="hangul.html"><b>한글 조판</b><em>3부</em></a></li>''',
)
