# -*- coding: utf-8 -*-
from ax2 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def box(px, name, use):
    return ('              <div style="display:grid;gap:6px;justify-items:center">'
            '<span style="display:block;width:%spx;height:26px;border-radius:4px;background:var(--accent-soft);'
            'border:1px solid var(--accent);box-sizing:border-box"></span>'
            '<span style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">%s</span>'
            '<span style="font-size:10.5px;color:var(--fg-faint);text-align:center">%s</span></div>'
            ) % (px, name, use)

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:14px 10px 14px 0">
                <div style="padding-left:26px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px">
                    <div style="padding-left:26px;display:grid;gap:16px">
                      <div class="pin-out" data-pin="2" style="display:grid;gap:8px">
                        <span style="font-size:13px;font-weight:700;display:block">정산 요청 #4821</span>
                        <span style="font-size:11.5px;color:var(--fg-muted);display:block">11월 1일 ~ 11월 7일</span>
                      </div>
                      <div class="pin-out" data-pin="3" style="display:grid;gap:8px">
                        <span style="font-size:13px;font-weight:700;display:block">정산 요청 #4820</span>
                        <span style="font-size:11.5px;color:var(--fg-muted);display:block">10월 25일 ~ 10월 31일</span>
                      </div>
                      <div class="pin-out" data-pin="4" style="display:flex;gap:8px">
                        <span style="background:var(--accent);color:#fff;border-radius:7px;padding:6px 12px;font-size:11.5px;font-weight:700">확정</span>
                        <span style="border:1px solid var(--line-strong);border-radius:7px;padding:6px 12px;font-size:11.5px">나중에</span>
                      </div>
                      <div class="pin-out" data-pin="5" style="font-size:11px;color:var(--fg-muted);line-height:1.9">행간도 간격입니다. 글줄 사이가<br>묶음 사이보다 넓으면 묶음이 안 보입니다.</div>
                    </div>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="spacing", ko="간격 체계", en="Spacing scale · spacing system",
  desc="여백을 4px·8px 배수로 정해 두는 간격 체계와, 가까운 것끼리 묶여 보이는 근접성 규칙을 보여주는 항목.",
  lede="여백을 <b>정해 둔 배수에서만</b> 고르는 약속. 보통 4px 또는 8px 의 배수를 씁니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 <b>값의 약속</b>입니다. 이 네 가지만 물어보면 어떤 약속인지 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>8px 격자 보기</b>를 켜면 줄이 8px 마다 그어집니다. 여백이 모두 8의 배수라 테두리와 글줄이 줄에 떨어집니다.<br>
          <b>눈대중 값으로</b>를 켜면 7·13·19가 섞입니다. 한눈에 틀린 데를 짚기는 어려운데 <b>전체가 어수선해집니다</b> —
          간격 체계가 막으려는 것이 정확히 이 느낌입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "간격 체계, 여백 체계, 스페이싱 스케일, 8포인트 그리드"),
    ("영어", "spacing scale, spacing system, 8-point grid"),
    ("같이 쓰는 말",
     "안쪽 여백은 <b>패딩</b>, 바깥 여백은 <b>마진</b>, 플렉스·그리드에서 사이를 띄우는 것은 <b>갭</b>입니다. "
     "열 사이의 홈은 <b>거터</b>(gutter), 화면 양옆의 여백은 <b>마진</b> 또는 <b>거터</b>라고 부르는데 팀마다 다릅니다. "
     "4px 단위로 잡는 것을 <b>4포인트 그리드</b>라고 합니다."),
    ("자주 잘못 부름",
     "<b>그리드</b> — 레이아웃 그리드(열을 나누는 것)와 간격 그리드(여백 단위)는 다른 것입니다.<br>"
     "<b>여백</b> — 디자인에서 <b>여백</b>(white space)은 '비워 둔 공간'이라는 더 넓은 뜻입니다.<br>"
     "<b>패딩</b> — 패딩은 <b>자리</b>를 가리키고 간격 체계는 <b>값</b>을 가리킵니다."),
  ]),
  axes=ax("간격 체계"),
  oneline="간격 체계는 <b>값을 줄이는 일</b>입니다. 쓸 수 있는 여백이 여섯 개뿐이면 고민도 줄고 어긋남도 사라집니다.",
  s4_title="단", s4_hint="단마다 맡은 자리가 있다",
  states=states([
    (box(4, "space-1 · 4px", "아이콘과 글자 사이"), "4px", "<b>붙어 있어야</b> 하는 것. 더 줄이면 닿아 보인다"),
    (box(8, "space-2 · 8px", "한 묶음 안의 줄 사이"), "8px", "제목과 부제처럼 <b>같은 덩어리</b>"),
    (box(16, "space-4 · 16px", "카드 안쪽 여백"), "16px", "가장 많이 쓰는 단. 기본값으로 삼는다"),
    (box(24, "space-6 · 24px", "묶음과 묶음 사이"), "24px", "여기서부터 <b>다른 덩어리</b>로 읽힌다"),
    (box(40, "space-10 · 40px", "구역 사이"), "40px", "화면 안의 큰 단락 나눔"),
    (box(64, "space-16 · 64px", "화면 위아래"), "64px+", "PC 에서 쓰는 큰 숨. 폰에서는 절반쯤으로 줄인다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바깥 여백", "padding · 안쪽 여백", "카드 테두리와 내용 사이. <b>사방이 같아야</b> 안정돼 보인다"),
    ("묶음 안 간격", "gap · 8px", "제목과 부제처럼 <b>한 덩어리</b>인 것들. 좁게 둔다"),
    ("묶음 사이", "gap · 16~24px", "덩어리와 덩어리. <b>안쪽보다 반드시 넓게</b> — 이 비율이 묶음을 만든다"),
    ("버튼 사이", "gap · 8px", "나란한 버튼은 붙여 둔다. 멀어지면 관계없는 것으로 보인다"),
    ("글줄 사이", "line-height", "행간도 간격이다. 행간이 묶음 간격보다 넓으면 <b>묶음이 흩어진다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          간격의 진짜 일은 '예쁘게'가 아니라 <b>무엇이 한 묶음인지 말하는 것</b>입니다(근접성).
          사람은 <b>가까운 것끼리 한 덩어리로</b> 봅니다. 그래서 라벨을 자기 입력창보다 윗 칸에 더 가깝게 두면
          누구의 라벨인지 설명하지 않아도 알게 됩니다. 반대로 안쪽이 바깥쪽보다 넓으면
          아무리 줄을 맞춰도 읽는 사람은 묶음을 못 찾습니다.</p>''',
  do=ul([
    "화면을 여럿이 만들 때 — 같은 카드가 사람마다 달라지지 않습니다",
    "목록·표처럼 <b>같은 모양이 반복</b>되는 화면",
    "폰과 PC 를 같이 만들 때 — 단만 바꿔 끼우면 됩니다",
  ]),
  dont=ul([
    "타이포그래피 안쪽 미세 조정 — 글자 사이는 <b>시각 보정</b>이 필요해 배수에 안 맞을 수 있습니다",
    "사진·아이콘의 <b>시각 중심</b> 맞추기 — 숫자보다 눈이 맞습니다",
    "단을 너무 촘촘히 두는 것(2·4·6·8·10·12…) — 결국 아무 값이나 쓰는 것과 같아집니다",
  ]),
  instead='글줄 사이는 <a href="typescale.html">타입 스케일</a>에 딸려 있고, 화면을 열로 나누는 일은 레이아웃 그리드(1부)가 맡습니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:16px;width:100%;max-width:220px">
                <div style="display:grid;gap:4px"><span style="font-size:11px;color:var(--fg-muted)">예금주</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">홍길동</span></div>
                <div style="display:grid;gap:4px"><span style="font-size:11px;color:var(--fg-muted)">계좌번호</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">110-***-****21</span></div>
              </div>''',
     "라벨과 입력창", "라벨은 <b>4px</b>, 필드 사이는 <b>16px</b>. 라벨이 누구 것인지 안 헷갈린다"),
    ('''              <div style="display:grid;gap:4px;width:100%;max-width:220px">
                <div style="display:grid;gap:12px"><span style="font-size:11px;color:var(--fg-muted)">예금주</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">홍길동</span></div>
                <div style="display:grid;gap:12px"><span style="font-size:11px;color:var(--fg-muted)">계좌번호</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">110-***-****21</span></div>
                <div style="font-size:11px;color:var(--danger);margin-top:4px">라벨이 아래 입력창에 붙어 보인다</div>
              </div>''',
     "뒤집힌 간격", "안쪽이 바깥쪽보다 넓으면 <b>묶음이 한 칸 밀려</b> 읽힌다"),
    ('''              <div style="display:grid;gap:8px;width:100%;max-width:220px">
                <div style="display:flex;gap:8px"><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span></div>
                <div style="font-size:11px;color:var(--fg-muted);font-family:var(--mono)">gap: 8px · padding: 16px</div>
              </div>''',
     "카드 그리드", "카드 사이(gap)는 카드 안쪽(padding)보다 <b>좁거나 같게</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 체계의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="단은 숫자가 아니라 <b>이름</b>으로 부릅니다. <code>16px</code>이 아니라 <code>--space-4</code>를 쓰면 나중에 전부 한 번에 조일 수 있습니다.",
  code='''<span class="t">:root</span> {
  <span class="a">--space-1</span>: <span class="s">4px</span>;    <span class="a">--space-2</span>: <span class="s">8px</span>;
  <span class="a">--space-3</span>: <span class="s">12px</span>;   <span class="a">--space-4</span>: <span class="s">16px</span>;
  <span class="a">--space-6</span>: <span class="s">24px</span>;   <span class="a">--space-10</span>: <span class="s">40px</span>;
}

<span class="t">.card</span> {
  <span class="a">padding</span>: <span class="t">var</span>(<span class="a">--space-4</span>);
  <span class="a">display</span>: grid;
  <span class="a">gap</span>: <span class="t">var</span>(<span class="a">--space-2</span>);   <span class="c">/* 묶음 안 */</span>
}
<span class="t">.card</span> + <span class="t">.card</span> { <span class="a">margin-top</span>: <span class="t">var</span>(<span class="a">--space-4</span>); } <span class="c">/* 묶음 사이 */</span>

<span class="c">/* 폰에서는 한 단씩 줄인다 */</span>
<span class="t">@media</span> (<span class="a">max-width</span>: 600px) {
  <span class="t">.card</span> { <span class="a">padding</span>: <span class="t">var</span>(<span class="a">--space-3</span>); }
}''',
  keys=kbd([
    ("8의 배수를 기본으로", "4px 은 작은 것(아이콘·글자 사이)에만. 나머지는 8·16·24·40"),
    ("묶음 안 &lt; 묶음 사이", "<b>이 한 줄이 간격 규칙의 전부</b>입니다. 어긋나면 묶음이 밀려 읽힙니다"),
    ("한 방향으로만 민다", "마진을 위·아래 양쪽에 주면 겹치거나(<b>마진 겹침</b>) 두 배가 된다. <code>gap</code>을 먼저 쓴다"),
    ("폰에서는 한 단 줄인다", "PC 의 40px 이 폰에서는 24px. 단을 바꿔 끼우지 새 값을 만들지 않는다"),
    ("터치 자리는 간격이 아니다", "버튼은 서로 떼는 것과 별개로 <b>44px 이상</b>의 누를 자리가 있어야 한다"),
  ]),
  backend=rows([
    ("간격 토큰 = 열거형", "자유로운 정수 대신 <b>정해진 값만</b> 받게 하는 것과 같습니다. 타입으로 막아 두면 23px 이 끼어들 수 없습니다."),
    ("디자인 도구와 맞추기", "피그마의 오토 레이아웃도 같은 단을 씁니다. 디자이너와 개발자가 <b>같은 이름</b>으로 말하면 \"여기 조금만 띄워 주세요\"가 \"space-4 로\"가 됩니다."),
    ("목록 성능", "줄마다 여백이 다르면 높이를 미리 알 수 없어 <b>가상 스크롤</b>을 못 씁니다. 같은 단을 쓰면 줄 높이가 고정돼 수만 줄도 그릴 수 있습니다."),
    ("빈 값 처리", "데이터가 없어 요소가 빠지면 <code>gap</code>은 알아서 줄어들지만 <code>margin</code>은 남습니다. 목록 화면에서 생기는 이상한 빈칸의 대부분이 이것입니다."),
  ]),
  plat_lede="단위는 다르지만 '배수로 정해 둔다'는 생각은 같습니다.",
  plats=plats([
    ("웹", "CSS · px · rem",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--space-2: 8px<br>gap: var(--space-2)</div>''',
     "<code>gap</code>이 들어오면서 마진 겹침 문제가 거의 사라졌습니다. 새로 짜는 화면은 <b>gap 을 먼저</b> 씁니다."),
    ("iOS", "points (pt)",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.padding(16)<br>spacing: 8</div>''',
     "단위가 <b>포인트</b>입니다. 1pt 가 화면에 따라 1~3픽셀이라, 디자이너의 '16'은 px 이 아니라 pt 일 수 있습니다."),
    ("안드로이드", "dp",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">16.dp<br>Arrangement<br>.spacedBy(8.dp)</div>''',
     "단위가 <b>dp</b>이고 Material 은 <b>8dp 그리드</b>를 권합니다. 아이콘 자리만 4dp 단위로 씁니다."),
  ]),
  plat_note="<b>px · pt · dp 가 서로 다릅니다.</b> 시안에 '16'이라고만 적혀 있으면 어느 단위인지 반드시 확인하세요. 같은 16이라도 iOS 의 16pt 는 고해상도 기기에서 32~48 실제 픽셀입니다. 앱 쪽에 웹 시안을 그대로 넘기면 여백이 <b>세 배로</b> 벌어진 화면이 나올 수 있습니다.",
  siblings=siblings("spacing"),
  related='''        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><span class="na"><b>박스 모델</b><em>1부</em></span></li>
        <li><span class="na"><b>그리드와 거터</b><em>1부</em></span></li>
        <li><span class="na"><b>터치 타깃</b><em>11부</em></span></li>''',
)
