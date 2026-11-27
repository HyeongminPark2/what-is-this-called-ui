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
  desc="여백을 4px이나 8px의 배수로 정해 두는 간격 체계와, 가까운 것끼리 한 묶음으로 보이는 근접성 규칙을 보여 주는 항목입니다.",
  lede="간격 체계는 여백 값을 <b>정해 둔 배수 가운데서만</b> 고르도록 한 규칙입니다. 보통 4px이나 8px의 배수를 씁니다.",
  axes_lede="토큰은 눈에 보이는 부품이 아니라 값을 어떻게 쓸지 <b>정해 둔 규칙</b>입니다. 그래서 생김새 대신 아래 네 가지를 물어보면 토큰끼리 무엇이 다른지 가려집니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>8px 격자 보기</b>를 켜면 8px마다 가로줄이 그어집니다. 여백이 모두 8의 배수라서 테두리와 글줄이 격자선에 딱 맞습니다.<br>
          <b>눈대중 값으로 바꾸기</b>를 켜면 7, 13, 19 같은 값이 섞이는데, 어디가 틀렸는지 한눈에 짚기는 어렵지만 <b>화면 전체가 어수선해 보입니다</b>.
          간격 체계는 이렇게 값이 조금씩 어긋나서 생기는 어수선함을 막으려고 씁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "간격 체계, 여백 체계, 스페이싱 스케일, 8포인트 그리드"),
    ("영어", "spacing scale, spacing system, 8-point grid"),
    ("같이 쓰는 말",
     "안쪽 여백은 <b>패딩</b>, 바깥 여백은 <b>마진</b>, 플렉스나 그리드에서 항목 사이를 띄우는 간격은 <b>갭</b>입니다. "
     "열과 열 사이의 간격은 <b>거터</b>(gutter)라고 하고, 화면 양옆의 여백은 팀에 따라 <b>마진</b>이라고도 하고 <b>거터</b>라고도 부릅니다. "
     "4px 단위로 잡는 방식은 <b>4포인트 그리드</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>그리드</b> — 화면을 열로 나누는 레이아웃 그리드와 여백 단위를 정하는 간격 그리드는 서로 다른 것입니다.<br>"
     "<b>여백</b> — 디자인에서 말하는 <b>여백</b>(white space)은 '비워 둔 공간' 전체를 가리키는 더 넓은 뜻입니다.<br>"
     "<b>패딩</b> — 패딩은 여백이 들어가는 <b>자리</b>를 가리키고, 간격 체계는 그 자리에 넣을 <b>값</b>을 정한 것입니다."),
  ]),
  axes=ax("간격 체계"),
  oneline="간격 체계는 <b>쓸 수 있는 여백 값의 개수를 줄이는 일</b>입니다. 고를 수 있는 여백이 여섯 개뿐이면 값을 고르는 고민이 줄고, 화면마다 여백이 조금씩 어긋나는 일도 없어집니다.",
  s4_title="여백 단계별 쓰는 자리", s4_hint="단마다 여백을 넣는 자리",
  states=states([
    (box(4, "space-1 · 4px", "아이콘과 글자 사이"), "4px 가장 좁은 간격", "아이콘과 글자처럼 <b>붙어 있어야</b> 하는 것 사이에 씁니다. 이보다 줄이면 서로 닿아 보입니다"),
    (box(8, "space-2 · 8px", "한 묶음 안의 줄 사이"), "8px 묶음 안 간격", "제목과 부제처럼 <b>같은 덩어리</b> 안의 요소 사이에 씁니다"),
    (box(16, "space-4 · 16px", "카드 안쪽 여백"), "16px 기본 여백", "가장 많이 쓰는 단이라 기본값으로 삼습니다"),
    (box(24, "space-6 · 24px", "묶음과 묶음 사이"), "24px 묶음 사이 간격", "이 정도부터는 <b>다른 덩어리</b>로 읽힙니다"),
    (box(40, "space-10 · 40px", "구역 사이"), "40px 구역 사이 간격", "화면 안에서 큰 구역을 나눌 때 씁니다"),
    (box(64, "space-16 · 64px", "화면 위아래"), "64px 이상 화면 위아래 여백", "PC 화면의 위아래에 두는 큰 여백입니다. 폰에서는 절반쯤으로 줄입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바깥 여백", "padding · 안쪽 여백", "카드 테두리와 내용 사이의 여백입니다. <b>네 방향이 같아야</b> 안정돼 보입니다"),
    ("묶음 안 간격", "gap · 8px", "제목과 부제처럼 <b>한 덩어리</b>인 요소 사이의 간격이라 좁게 둡니다"),
    ("묶음 사이", "gap · 16~24px", "덩어리와 덩어리 사이의 간격입니다. 묶음 안 간격보다 <b>반드시 넓게</b> 두어야 어디까지가 한 묶음인지 보입니다"),
    ("버튼 사이", "gap · 8px", "나란히 놓인 버튼은 가깝게 둡니다. 사이가 멀어지면 서로 관계없는 버튼처럼 보입니다"),
    ("글줄 사이", "line-height", "행간도 간격의 하나입니다. 행간이 묶음 사이 간격보다 넓으면 <b>어디까지가 한 묶음인지 알아보기 어렵습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          간격이 하는 일은 화면을 보기 좋게 꾸미는 것보다 <b>무엇이 한 묶음인지 보여 주는 것</b>입니다(근접성).
          사람은 <b>가까이 있는 것끼리 한 덩어리로</b> 보기 때문에, 라벨을 윗 칸보다 자기 입력창에 더 가깝게 두면
          따로 설명하지 않아도 어느 입력창의 라벨인지 알 수 있습니다. 반대로 묶음 안 간격이 묶음 사이 간격보다 넓으면
          줄을 잘 맞춰 두어도 읽는 사람은 어디까지가 한 묶음인지 찾지 못합니다.</p>''',
  do=ul([
    "여러 사람이 화면을 만들 때. 같은 카드를 누가 만들어도 여백이 같아집니다",
    "목록이나 표처럼 <b>같은 모양이 반복</b>되는 화면일 때",
    "폰과 PC 화면을 함께 만들 때. 새 값을 만들 필요 없이 쓰는 단만 바꾸면 됩니다",
  ]),
  dont=ul([
    "글자 사이처럼 타이포그래피 안쪽을 미세하게 조정할 때. 눈으로 보고 맞추는 <b>시각 보정</b>이 필요해서 배수에 맞지 않을 수 있습니다",
    "사진이나 아이콘의 <b>시각 중심</b>을 맞출 때. 이때는 숫자로 잰 가운데보다 눈으로 본 가운데가 더 정확합니다",
    "단을 2·4·6·8·10·12…처럼 너무 촘촘히 둘 때. 고를 수 있는 값이 너무 많아져서 아무 값이나 쓰는 것과 다르지 않게 됩니다",
  ]),
  instead_title="간격 체계와 함께 보면 좋은 항목",
  instead='글줄 사이 간격은 <a href="typescale.html">타입 스케일</a>에서 글자 크기와 함께 정하고, 화면을 열로 나누는 방법은 1부의 레이아웃 그리드 항목에서 다룹니다.',
  cases=cases([
    ('''              <div style="display:grid;gap:16px;width:100%;max-width:220px">
                <div style="display:grid;gap:4px"><span style="font-size:11px;color:var(--fg-muted)">예금주</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">홍길동</span></div>
                <div style="display:grid;gap:4px"><span style="font-size:11px;color:var(--fg-muted)">계좌번호</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">110-***-****21</span></div>
              </div>''',
     "라벨과 입력창을 한 묶음으로 보이기", "라벨과 입력창 사이는 <b>4px</b>, 필드와 필드 사이는 <b>16px</b>로 두면 라벨이 어느 입력창의 것인지 헷갈리지 않습니다"),
    ('''              <div style="display:grid;gap:4px;width:100%;max-width:220px">
                <div style="display:grid;gap:12px"><span style="font-size:11px;color:var(--fg-muted)">예금주</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">홍길동</span></div>
                <div style="display:grid;gap:12px"><span style="font-size:11px;color:var(--fg-muted)">계좌번호</span><span style="border:1px solid var(--line-strong);border-radius:7px;padding:7px 9px;font-size:12px">110-***-****21</span></div>
                <div style="font-size:11px;color:var(--danger);margin-top:4px">라벨이 아래 입력창에 붙어 보임</div>
              </div>''',
     "묶음 안 간격을 더 넓게 잡은 실패", "묶음 안 간격이 묶음 사이 간격보다 넓으면 라벨이 아래 입력창과 묶여서 <b>묶음이 한 칸씩 밀려</b> 읽힙니다"),
    ('''              <div style="display:grid;gap:8px;width:100%;max-width:220px">
                <div style="display:flex;gap:8px"><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span><span style="flex:1;height:30px;border-radius:6px;background:var(--bg);border:1px solid var(--line)"></span></div>
                <div style="font-size:11px;color:var(--fg-muted);font-family:var(--mono)">gap: 8px · padding: 16px</div>
              </div>''',
     "카드 사이 간격과 안쪽 여백 맞추기", "카드 사이 간격(gap)은 카드 안쪽 여백(padding)보다 <b>좁거나 같게</b> 둡니다"),
  ]),
  s8_title="최소 코드와 지킬 규칙", s8_hint="간격을 코드로 옮기는 방법",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법과 이유</th>",
  code_lede="코드에서는 단을 숫자 대신 <b>이름</b>으로 부릅니다. <code>16px</code> 대신 <code>--space-4</code>를 써 두면 나중에 여백 전체를 한 번에 좁히거나 넓힐 수 있습니다.",
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
    ("8의 배수를 기본으로 쓰기", "4px은 아이콘과 글자 사이처럼 작은 간격에만 쓰고, 나머지는 8·16·24·40을 씁니다"),
    ("묶음 안 간격을 묶음 사이보다 좁게 두기", "묶음 안 간격은 늘 묶음 사이 간격보다 좁아야 합니다. <b>간격 규칙에서 가장 중요한 조건</b>으로, 이 관계가 뒤집히면 묶음이 한 칸씩 밀려 읽힙니다"),
    ("여백은 한 방향으로만 주기", "마진을 위아래 양쪽에 주면 두 마진이 겹쳐 하나가 되거나(<b>마진 겹침</b>) 두 배로 벌어집니다. 그래서 <code>gap</code>을 먼저 씁니다"),
    ("폰에서는 한 단 줄이기", "PC에서 40px이던 간격은 폰에서 24px로 줄입니다. 이때 새 값을 만들지 않고 정해 둔 단 가운데서 바꿔 고릅니다"),
    ("누를 자리는 간격과 따로 확보하기", "버튼끼리 떼어 두는 간격과 별개로, 버튼마다 <b>44px 이상</b>의 누를 자리가 있어야 합니다"),
  ]),
  backend=rows([
    ("열거형과 같은 역할", "아무 정수나 받지 않고 <b>정해진 값만</b> 받도록 하는 열거형과 같습니다. 타입으로 막아 두면 23px 같은 값이 끼어들 수 없습니다."),
    ("디자인 도구와 같은 이름 쓰기", "피그마의 오토 레이아웃에도 같은 단을 씁니다. 디자이너와 개발자가 <b>같은 이름</b>으로 이야기하면 \"여기 조금만 띄워 주세요\" 대신 \"space-4로 해 주세요\"처럼 정확하게 요청할 수 있습니다."),
    ("여백이 목록 성능에 주는 영향", "줄마다 여백이 다르면 줄 높이를 미리 알 수 없어서 <b>가상 스크롤</b>을 쓸 수 없습니다. 모든 줄이 같은 단을 쓰면 줄 높이가 고정되므로 수만 줄도 그릴 수 있습니다."),
    ("데이터가 빠진 자리의 여백", "데이터가 없어 요소가 빠지면 <code>gap</code>은 그 자리만큼 저절로 줄어들지만 <code>margin</code>은 그대로 남습니다. 목록 화면에 생기는 이상한 빈칸은 대부분 이렇게 남은 마진 때문입니다."),
  ]),
  plat_lede="플랫폼마다 단위는 다르지만, 여백을 배수로 정해 둔다는 생각은 같습니다.",
  plats=plats([
    ("웹", "CSS · px · rem",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">--space-2: 8px<br>gap: var(--space-2)</div>''',
     "<code>gap</code> 속성이 생기면서 마진 겹침 문제는 거의 사라졌습니다. 그래서 새로 짜는 화면에서는 <b>gap을 먼저</b> 씁니다."),
    ("iOS", "points (pt)",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.padding(16)<br>spacing: 8</div>''',
     "단위는 <b>포인트</b>(pt)입니다. 1pt가 화면에 따라 1~3픽셀이므로, 디자이너가 적은 '16'은 px이 아니라 pt일 수 있습니다."),
    ("안드로이드", "dp",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">16.dp<br>Arrangement<br>.spacedBy(8.dp)</div>''',
     "단위는 <b>dp</b>이고, Material은 <b>8dp 그리드</b>를 권합니다. 아이콘 자리에만 4dp 단위를 씁니다."),
  ]),
  plat_note="<b>px과 pt, dp는 서로 다른 단위입니다.</b> 그래서 시안에 '16'이라고만 적혀 있으면 어느 단위인지 반드시 확인하세요. 같은 16이라도 iOS의 16pt는 고해상도 기기에서 실제 픽셀 32~48개에 해당합니다. 앱 쪽에 웹 시안을 그대로 넘기면 여백이 <b>세 배로</b> 벌어진 화면이 나올 수 있습니다.",
  siblings=siblings("spacing"),
  related='''        <li><a href="../items/field.html"><b>텍스트 필드</b><em>4부</em></a></li>
        <li><a href="box.html"><b>박스 모델</b><em>1부</em></a></li>
        <li><a href="grid.html"><b>그리드와 거터</b><em>1부</em></a></li>
        <li><a href="touchtarget.html"><b>터치 타깃</b><em>11부</em></a></li>''',
)
