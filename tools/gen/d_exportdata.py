# -*- coding: utf-8 -*-
from ax10 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">범위는 이 쪽 / 조건에 맞는 전부 / 전체</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">파일 꼴은 CSV · XLSX · PDF</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">건수를 128건처럼 미리 보여 줌</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">오래 걸리면 파일을 다 만든 뒤에 알림</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">CSV에 BOM을 붙여 엑셀에서 한글이 안 깨지게</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">파일 이름에 조건과 날짜를 적음</div>
                </div>
              </div>'''

D = dict(
  slug="exportdata", ko="내보내기", en="Export",
  desc="화면의 자료를 파일로 꺼내는 일을 범위·꼴·건수와 오래 걸릴 때의 처리까지 다루는 항목입니다.",
  lede="내보내기는 화면에 보이는 자료를 <b>파일로 꺼내는</b> 기능입니다. 설계할 때는 내보낼 범위를 어떻게 물을지와 파일을 만드는 데 <b>오래 걸릴 때</b> 어떻게 할지를 특히 따져야 합니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>건수를 올려 보세요. 건수가 <b>적으면 그 자리에서</b> 파일을 받지만, 많으면 파일을 만드는 데 시간이 걸려서
          <b>메일로 보내거나 나중에 받게</b> 해야 합니다.<br>
          범위를 '이 쪽'과 '조건에 맞는 전부'로 나눠 묻는 이유는 <a href="bulk.html">일괄 선택</a>과 같습니다.
          사용자가 내보내기를 누를 때는 거의 언제나 <b>조건에 맞는 전부</b>를 원합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "내보내기, 다운로드, 추출, 엑셀 받기"),
    ("영어", "export, download, data export, report"),
    ("같이 쓰는 말",
     "파일을 만드는 데 시간이 걸려 나중에 건네주는 방식은 <b>비동기 내보내기</b>·<b>작업 큐</b>라고 합니다. "
     "파일 맨 앞에 붙여 인코딩을 알려 주는 표식은 <b>BOM</b>이라고 하는데, "
     "엑셀이 UTF-8 CSV를 제대로 열게 하려고 붙입니다. "
     "내보낼 열을 사용자가 고르게 하는 기능은 <b>필드 선택</b>이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>백업</b> — 백업은 나중에 <b>되돌리려고</b> 만드는 사본이고, 내보내기는 자료를 <b>다른 곳에서 쓰려고</b> 꺼내는 것입니다.<br>"
     "<b>인쇄</b> — 인쇄물은 눈으로 보기 위한 것이고, 내보낸 파일은 <b>다시 계산할 수 있는</b> 자료입니다.<br>"
     "<b>API</b> — API는 다른 프로그램이 자료를 가져가는 통로라서, 사람이 버튼을 눌러 파일을 받는 내보내기와는 다릅니다."),
  ]),
  axes=ax("내보내기"),
  oneline="<b>내보낼 범위가 '이 쪽'인지 '조건에 맞는 전부'인지 묻고, 파일을 만드는 데 오래 걸리면 사용자를 그 자리에서 기다리게 하지 마세요.</b>",
  s4_title="정할 것과 건수별 처리", s4_hint="건수가 늘면 달라지는 처리",
  states=states([
    (one(txt('이 쪽 20건<br>조건에 맞는 128건<br>전체 3,120건', "9.5px"), "범위 고르기", True, "사용자는 거의 늘 가운데를 원함"),
     "내보낼 범위 묻기", "범위를 <b>나눠서 묻습니다</b>. <a href=\"bulk.html\">일괄 선택</a>과 같은 방식입니다"),
    (one(txt('CSV · XLSX · PDF', "10px"), "꼴 고르기", None, "다시 계산할 수 있는지로 갈림"),
     "파일 꼴 고르기", "CSV·XLSX는 다시 계산할 수 있지만 PDF는 <b>보기용</b>이라서 성격이 다릅니다"),
    (one(mono('settlements_2026-11_승인됨.csv', 'var(--accent)'), "파일 이름", True, "조건과 날짜를 적음"),
     "파일 이름 정하기", "파일을 받은 뒤에도 이름만 보고 <b>무슨 자료인지</b> 알 수 있어야 합니다"),
    (one(txt('<b>128건</b> · 어림 15 KB<br><span style="color:var(--fg-muted)">바로 받을 수 있음</span>', "9.5px"), "작을 때", True, "그 자리에서 바로 줌"),
     "건수가 적을 때", "버튼을 누르면 <b>바로</b> 파일을 받습니다"),
    (one(txt('<b>200,000건</b> · 어림 24 MB<br><span style="color:var(--danger)">만드는 데 22초쯤</span>', "9.5px"), "클 때", False, "그 자리에서 바로 못 줌"),
     "건수가 많을 때", "파일을 <b>다 만든 뒤에 알려</b> 줍니다"),
    (one(txt('만들고 있습니다<br><span style="color:var(--fg-muted)">다 되면 메일로 보내 드립니다</span>', "9.5px"), "비동기 처리", True, "사용자를 기다리게 하지 않음"),
     "만드는 데 오래 걸릴 때", "사용자가 창을 닫아도 파일은 서버에서 <b>계속 만들어집니다</b>"),
  ]),
  anat=ANAT,
  pins=pins([
    ("범위", "이 쪽 / 조건 / 전체", "범위를 <b>나눠서 묻습니다.</b> 묻지 않으면 사용자가 원하지 않은 범위의 파일을 받게 됩니다"),
    ("꼴", "CSV · XLSX · PDF", "받은 자료를 <b>다시 계산할 수 있는지</b>에 따라 고릅니다"),
    ("건수", "미리 보여 주기", "버튼을 누르기 전에 <b>몇 건이 나올지</b> 알려 줍니다"),
    ("오래 걸리면", "다 만든 뒤 알리기", "사용자를 기다리게 하지 않고, <b>창을 닫아도</b> 파일 만들기는 계속됩니다"),
    ("BOM", "CSV에서 놓치기 쉬운 점", "BOM을 붙이지 않으면 엑셀에서 <b>한글이 깨집니다</b>"),
    ("파일 이름", "조건 + 날짜", "받은 뒤에도 <b>무슨 자료인지</b> 알 수 있도록 조건과 날짜를 넣습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>CSV는 만들기 쉬워 보이지만 놓치기 쉬운 문제가 많습니다.</b>
          엑셀은 UTF-8 CSV를 열 때 <b>BOM</b>이 없으면 한글을 깨뜨리고,
          <code>010-1234</code> 같은 값을 <b>날짜나 수식</b>으로 바꿔 버립니다.
          <code>=</code>·<code>+</code>로 시작하는 값은 아예 <b>수식으로 실행</b>될 수 있어서
          보안 문제(CSV 인젝션)가 되기도 합니다.
          값 안에 쉼표나 줄바꿈이 있으면 따옴표로 감싸야 하는데,
          이런 규칙을 직접 짜면 빠뜨리는 경우가 많으므로 <b>검증된 라이브러리</b>를 쓰는 편이 낫습니다.</p>''',
  do_title="내보내기가 필요한 경우와 지킬 것",
  dont_title="내보내기를 만들 때 피할 것",
  instead_title="내보내기와 함께 보면 좋은 항목",
  do=ul([
    "표가 있는 화면이라면 거의 언제나 필요합니다. 관리 도구에서 <b>가장 많이 요청받는 기능</b>입니다",
    "내보낼 범위를 <b>나눠서 묻기</b>",
    "건수가 많으면 파일을 <b>다 만든 뒤 알리기</b>",
  ]),
  dont=ul([
    "범위를 묻지 않고 <b>지금 보이는 쪽만</b> 내보낼 때",
    "오래 걸리는 작업인데 사용자가 <b>창을 떠나지 못하게</b> 할 때",
    "CSV에 BOM을 붙이지 않을 때. 엑셀에서 <b>한글이 깨집니다</b>",
    "<code>export.csv</code> 같은 이름을 붙일 때. 받고 나면 무슨 자료인지 알 수 없습니다",
  ]),
  instead='화면에서 자료를 살펴보는 방법은 <a href="table.html">데이터 테이블</a>에서 다루고, 내보낼 범위를 고르는 방법은 <a href="bulk.html">일괄 선택</a>에서, 기간을 고르는 방법은 <a href="daterange.html">날짜 범위</a>에서 다룹니다.',
  cases=cases([
    (one(txt('조건에 맞는 <b>128건</b>', "10px") + '<br>' + mono('CSV'), "표 위 버튼", True, "지금 걸린 조건을 그대로 적용"),
     "표에 걸린 조건대로 내보내기", "지금 걸린 <a href=\"filter.html\">필터</a> 조건을 그대로 적용해 내보냅니다"),
    (one(txt('만들고 있습니다 · 42%', "10px"), "진행률", True, "오래 걸릴 때"),
     "파일 만드는 진행 상황 알리기", "파일을 만드는 진행 상황을 <a href=\"../items/progress.html\">프로그레스</a>로 알립니다"),
    (one(mono('Idempotency-Key', 'var(--accent)') + '<br>' + txt('같은 요청이 두 번 와도 파일은 하나', "9px"), "두 번 누를 때", True, ""),
     "두 번 눌러도 파일은 하나만 만들기", "<a href=\"checkout.html\">결제</a>에서 쓰는 것과 같은 장치로 중복 요청을 막습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="내보내기를 만들 때 꼭 갖출 것",
  code_lede="범위는 라디오 버튼으로 묻고, 오래 걸리는 작업이면 서버에서 <b>작업 번호</b>를 돌려받습니다.",
  code='''&lt;<span class="t">fieldset</span>&gt;
  &lt;<span class="t">legend</span>&gt;무엇을 내보낼까요&lt;/<span class="t">legend</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"range"</span> <span class="a">value</span>=<span class="s">"page"</span>&gt; 이 쪽 20건&lt;/<span class="t">label</span>&gt;
  &lt;<span class="t">label</span>&gt;&lt;<span class="t">input</span> <span class="a">type</span>=<span class="s">"radio"</span> <span class="a">name</span>=<span class="s">"range"</span> <span class="a">value</span>=<span class="s">"filter"</span> <span class="a">checked</span>&gt; 조건에 맞는 128건&lt;/<span class="t">label</span>&gt;
&lt;/<span class="t">fieldset</span>&gt;
&lt;<span class="t">p</span> <span class="a">role</span>=<span class="s">"status"</span>&gt;128건 · 어림 15 KB&lt;/<span class="t">p</span>&gt;

<span class="c">// 오래 걸리면 작업 번호를 받아 두고 알림으로 잇는다</span>
<span class="k">const</span> { jobId } = <span class="k">await</span> (<span class="k">await</span> fetch(<span class="s">'/api/exports'</span>, {
  method: <span class="s">'POST'</span>,
  headers: { <span class="s">'Idempotency-Key'</span>: key },
  body: JSON.stringify({ range: <span class="s">'filter'</span>, filter, format: <span class="s">'csv'</span> })
})).json();

<span class="c">// 엑셀이 한글을 제대로 열도록 맨 앞에 BOM을 붙인다</span>
<span class="k">const</span> blob = <span class="k">new</span> Blob([<span class="s">'\\uFEFF'</span>, csv], { type: <span class="s">'text/csv;charset=utf-8'</span> });''',
  keys=kbd([
    ("범위는 <code>&lt;fieldset&gt;</code>으로 묶기", "스크린 리더가 '무엇을 내보낼까요 묶음, 조건에 맞는 128건 선택됨'처럼 읽습니다"),
    ("<code>role=\"status\"</code>", "건수가 바뀐 것을 알립니다. 화면의 <b>숫자만 바뀌면</b> 화면을 보지 않는 사람은 알 수 없습니다"),
    ("오래 걸릴 때", "버튼을 잠그고 <b>무슨 일이 일어나고 있는지</b> 알립니다. 아무 반응이 없으면 사용자가 버튼을 또 누릅니다"),
    ("<code>download</code> 속성", "<code>&lt;a download=\"settlements.csv\"&gt;</code>처럼 쓰면 받을 파일 이름을 정할 수 있습니다"),
    ("창이 닫힌 뒤의 포커스", "내보내기 창이 닫히면 포커스를 <b>창을 연 버튼</b>으로 되돌립니다"),
    ("파일을 받으려고 새 창 열지 않기", "파일을 받으려고 새 탭이 열렸다 닫히면 <b>포커스가 사라집니다</b>"),
  ]),
  backend=rows([
    ("오래 걸리면 작업으로 돌리기", "큰 파일을 요청 하나로 만들어 돌려주려 하면 <b>타임아웃</b>이 납니다. 작업 번호를 먼저 돌려주고, 파일이 다 되면 알립니다."),
    ("범위는 조건으로 받기", "20만 건의 ID를 모두 담아 보낼 수는 없으므로 <b>필터 조건을 그대로</b> 보냅니다. <a href=\"bulk.html\">일괄 선택</a>과 같은 방식입니다."),
    ("메모리에 다 올리지 않고 스트리밍하기", "모든 행을 메모리에 올리면 서버 메모리가 모자라 작업이 실패합니다. <b>스트리밍</b>으로 한 줄씩 읽어 파일에 씁니다."),
    ("내보낼 때도 권한 확인하기", "사용자가 화면에서 볼 수 없는 줄이 파일에 섞이면 <b>정보 유출</b>이 됩니다. 내보낼 때도 화면과 같은 권한 조건을 겁니다."),
    ("CSV 인젝션", "<code>=</code>·<code>+</code>·<code>-</code>·<code>@</code>로 시작하는 값은 <b>앞에 작은따옴표</b>를 붙여서 엑셀이 수식으로 실행하지 않게 합니다."),
    ("내려받기 링크의 만료", "내려받기 링크를 계속 열어 두면 <b>링크를 얻은 다른 사람도 파일을 받을 수 있습니다</b>. 링크는 짧은 시간 뒤에 만료시키고, 받을 때 로그인을 확인합니다."),
  ]),
  plat_lede="내보내기는 <b>웹에서 가장 흔하고</b>, 앱에서는 OS의 공유 기능을 씁니다.",
  plats=plats([
    ("웹", "download · Blob",
     one(mono('settlements.csv', 'var(--accent)'), "", True, "", "110px"),
     "파일을 바로 받고, 오래 걸리면 <b>메일이나 알림</b>으로 나중에 전달합니다."),
    ("iOS", "공유 시트",
     '''              <div class="phone" role="img" aria-label="iOS 공유 시트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:var(--surface);border-radius:8px 8px 0 0;border-top:1px solid var(--line);padding:4px;font-size:5px">공유</div></div></div>''',
     "파일을 바로 저장하기보다 <b>공유 시트</b>로 넘기고, 어디에 둘지는 사용자가 고릅니다."),
    ("안드로이드", "Storage Access",
     '''              <div class="phone" role="img" aria-label="안드로이드 파일 저장 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:28px;font-size:5px;color:var(--fg-muted)">파일 앱에 저장</div></div></div>''',
     "앱이 저장소 아무 곳에나 파일을 쓸 수 없어서, 저장할 위치를 OS가 사용자에게 묻습니다."),
  ]),
  plat_note="\"엑셀로 받게 해 주세요\"는 가장 자주 받는 요청이면서, 일정이 가장 자주 <b>작게 잡히는</b> 요청입니다. 범위 묻기, 큰 건수 처리, 권한 확인, 한글 깨짐, 두 번 눌림 대응까지 함께 만들어야 하기 때문에, 버튼 하나 다는 일로 보고 일정을 잡으면 거의 언제나 시간이 모자랍니다.",
  siblings=siblings("exportdata"),
  related='''        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="bulk.html"><b>일괄 선택</b><em>10부</em></a></li>
        <li><a href="daterange.html"><b>날짜 범위</b><em>10부</em></a></li>
        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>''',
)
