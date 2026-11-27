# -*- coding: utf-8 -*-
from ax10 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def scroller(rowstxt, note="", w="160px", h="62px"):
    body = ''.join('<div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px;border-bottom:1px solid var(--line);white-space:nowrap;overflow:hidden">' + r + '</div>' for r in rowstxt)
    return ('              <div style="width:100%;max-width:' + w + '">'
            '<div style="height:' + h + ';border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">' + body + '</div>'
            + ('<span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:3px">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">바깥 상자 — 높이가 정해져 있고 여기서 굴린다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">받침대 height = 20000 × 36px — 막대 길이를 만든다</div>
                  <div class="pin-out" data-pin="3" style="max-width:230px">''' + scroller(['… 9,980', '… 9,981', '… 9,982', '… 9,983'], "", "230px", "60px").strip() + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">실제로 그린 것은 12줄뿐</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">transform: translateY(첫 줄 번호 × 36px)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">줄 높이가 제각각이면 이 계산이 전부 무너진다</div>
                </div>
              </div>'''

D = dict(
  slug="virtual", ko="가상 스크롤", en="Virtual scrolling",
  desc="수만 줄을 보이는 만큼만 그려 버티는 기법. 받침대 높이, 창 계산, 고정 줄 높이의 제약과 대안.",
  lede="목록이 수만 줄이어도 <b>보이는 만큼만</b> 그려 버티는 기법. 공짜는 아니고 <b>잃는 것</b>이 분명합니다.",
  axes_lede="데이터를 다루는 화면은 '건수가 늘면 어떻게 되나'가 설계의 전부입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>가상 스크롤</b>을 끄고 2만 줄을 그려 보세요. 그리는 데 걸린 시간과
          <b>실제로 만들어진 DOM 노드 수</b>가 아래에 나옵니다.<br>
          켜면 노드 수가 <b>열몇 개</b>로 떨어집니다. 스크롤 막대 길이는 그대로인데,
          받침대 하나로 <b>길이만 흉내</b>내기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "가상 스크롤, 가상화, 창 띄우기"),
    ("영어", "virtual scrolling, virtualization, windowing"),
    ("같이 쓰는 말",
     "보이는 구간만 그리는 것을 <b>윈도잉</b>(windowing), "
     "길이를 흉내 내는 빈 상자를 <b>스페이서</b>·<b>사이저</b>(sizer), "
     "위아래로 조금 더 그려 두는 여유분을 <b>오버스캔</b>(overscan)이라 합니다. "
     "리액트 쪽 라이브러리 이름이 그대로 쓰이기도 합니다(react-window, TanStack Virtual)."),
    ("자주 잘못 부름",
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 <b>더 받아오는</b> 것, 가상 스크롤은 <b>덜 그리는</b> 것입니다. 둘은 같이 쓰기도 합니다.<br>"
     "<b>페이지네이션</b> — <a href=\"../items/pagination.html\">페이지네이션</a>은 화면을 끊고, 가상 스크롤은 <b>한 줄로 이어 둡니다</b>.<br>"
     "<b>레이지 로딩</b> — 이미지를 늦게 받는 것과는 다른 얘기입니다."),
  ]),
  axes=ax("가상 스크롤"),
  oneline="가상 스크롤은 <b>마지막 수단</b>입니다. 줄을 줄이거나 쪽을 나눠서 되면 그쪽이 늘 낫습니다.",
  s4_title="상태", s4_hint="줄이 늘 때 무슨 일이 나는가",
  states=states([
    (scroller(['모란상회', '한빛아웃도어', '새벽상사', '대림유통'], "200줄 — 그냥 다 그려도 된다"),
     "작은 목록", "<b>가상 스크롤이 필요 없다.</b> 복잡함만 는다"),
    (scroller(['… 1', '… 2', '… 3', '… 4'], "20,000줄 전부 그림 — 멈칫한다"),
     "큰 목록을 그냥", "노드 2만 개. 처음 그릴 때 <b>화면이 멎는다</b>"),
    (scroller(['… 9,980', '… 9,981', '… 9,982', '… 9,983'], "보이는 12줄만 — 노드 12개"),
     "가상 스크롤", "막대 길이는 같고 <b>그린 것만 줄었다</b>"),
    (scroller(['…', '<span class="skl" style="height:8px;width:60%;display:inline-block"></span>', '<span class="skl" style="height:8px;width:45%;display:inline-block"></span>', '…'], "빠르게 굴리면 빈 줄이 스친다"),
     "빨리 굴릴 때", "따라잡기 전에 <b>빈 자리</b>가 보인다. 뼈대로 메운다"),
    ('''              <div style="width:100%;max-width:160px">
                <div style="height:62px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px;border-bottom:1px solid var(--line)">짧은 줄</div>
                  <div style="padding:2px 7px 3px;font-size:9.5px;line-height:12px;border-bottom:1px solid var(--line)">두 줄짜리 긴 설명이<br>들어간 줄</div>
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px;border-bottom:1px solid var(--line)">짧은 줄</div>
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px">…</div>
                </div>
                <span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:3px">높이가 제각각 — 계산이 어긋난다</span>
              </div>''',
     "줄 높이가 다를 때", "<b>재야 한다.</b> 난이도가 몇 배로 뛴다"),
    (scroller(['… 19,998', '… 19,999', '… 20,000', ''], "끝에 다다름 — 더 받을 것이 있나"),
     "끝", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 붙으면 여기서 다음 묶음을 받는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("굴리는 상자", "height 고정", "높이가 안 정해지면 <b>몇 줄이 보이는지</b>를 모른다"),
    ("받침대", "sizer", "전체 줄 수 × 줄 높이. <b>막대 길이만</b> 만든다"),
    ("보이는 창", "window", "<code>scrollTop / 줄높이</code>로 첫 줄을 구한다"),
    ("그린 줄", "12개 남짓", "위아래로 <b>두세 줄 더</b>(overscan) 그려 두면 덜 깜빡인다"),
    ("자리 옮기기", "translateY", "<code>top</code>보다 <code>transform</code>이 싸다"),
    ("고정 줄 높이", "전제 조건", "제각각이면 <b>다 재야</b> 하고 난이도가 뛴다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>잃는 것을 먼저 세어 보세요.</b> 안 그린 줄은
          <kbd>Ctrl</kbd>+<kbd>F</kbd> 로 못 찾고, 스크린 리더가 못 읽고,
          인쇄하면 열몇 줄만 나오고, 검색 엔진도 못 봅니다.
          <code>Ctrl</code>+<code>A</code> 로 전체 복사하면 보이는 것만 복사됩니다.
          그래서 <b>공개 페이지에는 거의 쓰지 않고</b> 로그인 뒤 관리 도구에만 씁니다.</p>''',
  do=ul([
    "줄이 <b>수천을 넘고</b> 끊어 보여 줄 수 없을 때 — 로그, 시세, 채팅",
    "줄 높이가 <b>모두 같을</b> 때",
    "로그인 뒤 <b>관리 도구</b> — 검색·인쇄를 안 써도 되는 화면",
  ]),
  dont=ul([
    "줄이 몇백일 때 — <b>그냥 다 그린다</b>. 요즘 브라우저는 버틴다",
    "공개 페이지 — <b>검색 엔진이 못 본다</b>",
    "줄 높이가 제각각인데 직접 만들기 — <b>라이브러리를 쓴다</b>",
    "쪽을 나눌 수 있는데 굳이 — <a href=\"../items/pagination.html\">페이지네이션</a>이 더 쉽고 더 친절하다",
  ]),
  instead='끊어도 되면 <a href="../items/pagination.html">페이지네이션</a>, 이어 받으면 <a href="../items/infinite.html">무한 스크롤</a>, 줄이 적으면 그냥 <a href="table.html">데이터 테이블</a>.',
  cases=cases([
    (scroller(['10:21:08 OK', '10:21:09 OK', '10:21:09 WARN', '10:21:10 OK'], "", "150px"),
     "로그 보기", "줄 높이가 같고 수만 줄. <b>가장 잘 맞는 자리</b>"),
    (scroller(['삼성전자 71,200', 'SK하이닉스 183,000', 'NAVER 192,400', '카카오 38,650'], "", "150px"),
     "시세 표", "줄이 많고 <b>자주 바뀐다</b>. 안 보이는 줄은 안 고쳐도 된다"),
    (scroller(['모란상회', '한빛아웃도어', '새벽상사'], "120줄 — 이건 그냥 그린다", "150px"),
     "이건 안 쓴다", "몇백 줄에 가상 스크롤을 넣으면 <b>잃기만</b> 한다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 기법의 계약서",
  code_lede="받침대로 길이를 만들고, 보이는 구간만 그려 <code>transform</code>으로 밀어 둡니다.",
  code='''&lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"scroller"</span> <span class="a">role</span>=<span class="s">"list"</span>
     <span class="a">aria-label</span>=<span class="s">"정산 20,000건"</span>&gt;
  &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"sizer"</span>&gt;             <span class="c">&lt;!-- 막대 길이만 만든다 --&gt;</span>
    &lt;<span class="t">div</span> <span class="a">class</span>=<span class="s">"window"</span>&gt;…12줄…&lt;/<span class="t">div</span>&gt;
  &lt;/<span class="t">div</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="k">const</span> H = <span class="a">36</span>, N = <span class="a">20000</span>;
sizer.style.height = N * H + <span class="s">'px'</span>;

scroller.onscroll = () =&gt; {
  <span class="k">const</span> first = Math.floor(scroller.scrollTop / H);
  <span class="k">const</span> count = Math.ceil(scroller.clientHeight / H) + <span class="a">2</span>;  <span class="c">// 여유분</span>
  win.style.transform = <span class="s">`translateY(${</span>first * H<span class="s">}px)`</span>;
  render(first, count);
};''',
  keys=kbd([
    ("<kbd>PageDown</kbd>·<kbd>Home</kbd>·<kbd>End</kbd>", "브라우저 기본 스크롤이 그대로 돌아야 한다. <b>직접 가로채지 않는다</b>"),
    ("<kbd>Tab</kbd>", "안 그린 줄에는 못 간다. <b>초점이 있던 줄을 지우면</b> 초점이 <code>&lt;body&gt;</code>로 튄다"),
    ("<code>role=\"list\"</code> + 건수", "'20,000건'을 레이블에 적는다. 12줄만 읽히면 열두 건인 줄 안다"),
    ("<code>aria-setsize</code>·<code>aria-posinset</code>", "줄마다 '20,000개 중 9,981번째'를 알린다"),
    ("<kbd>Ctrl</kbd>+<kbd>F</kbd> 는 안 된다", "브라우저 찾기가 안 그린 줄을 못 본다. <b>검색 칸을 따로</b> 둔다"),
    ("인쇄", "보이는 열몇 줄만 나온다. 인쇄가 필요하면 <b>별도 내보내기</b>를 만든다"),
  ]),
  backend=rows([
    ("2만 건을 한 번에 보내지 않는다", "그릴 줄은 줄었어도 <b>받는 양은 그대로</b>입니다. 응답이 5MB 면 느린 건 여전합니다."),
    ("커서 페이징", "<code>OFFSET 19000</code>은 앞의 19,000줄을 세고 버립니다. <b>마지막 줄의 키</b>를 기준으로 다음을 받는 편이 빠릅니다."),
    ("중간으로 뛰면", "막대를 끌어 한가운데로 가면 그 구간을 <b>따로 요청</b>해야 합니다. 커서 방식과는 잘 안 맞아 설계가 갈립니다."),
    ("전체 건수", "받침대 높이를 만들려면 <b>총 줄 수</b>가 필요합니다. <code>COUNT(*)</code>가 비싸면 어림수를 쓰고 끝에서 보정합니다."),
    ("줄이 바뀌면", "안 보이는 줄이 서버에서 바뀌어도 화면은 모릅니다. <b>언제 다시 받을지</b>를 정해 둡니다."),
  ]),
  plat_lede="<b>앱 쪽은 처음부터 이것이 기본</b>입니다. 웹만 직접 만듭니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     scroller(['… 9,981', '… 9,982', '… 9,983'], "", "120px", "48px"),
     "표준 부품이 없어 <b>직접 만들거나</b> 라이브러리를 씁니다. 줄 높이가 다르면 거의 라이브러리를 씁니다."),
    ("iOS", "UITableView",
     '''              <div class="phone" role="img" aria-label="iOS 테이블뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,981</div><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,982</div></div></div></div>''',
     "<b>셀 재사용</b>(cell reuse)이 OS 기본입니다. 2007년부터 그래 왔고, 따로 켤 것이 없습니다."),
    ("안드로이드", "RecyclerView",
     '''              <div class="phone" role="img" aria-label="RecyclerView 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,981</div><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,982</div></div></div></div>''',
     "이름부터 <b>재활용</b>입니다. 안 보이는 뷰를 모아 뒀다 다시 씁니다."),
  ]),
  plat_note="\"목록이 느려요\"에 바로 가상 스크롤을 꺼내지 마세요. 줄이 몇백이면 느린 원인은 보통 <b>줄마다의 그림자·이미지·계산</b>이지 줄 수가 아닙니다. 수천 줄이 확실하고 줄 높이가 같을 때만 꺼내고, 그 순간부터 <b>찾기·인쇄·스크린 리더</b>를 따로 챙겨야 한다는 것을 일정에 넣으세요.",
  siblings=siblings("virtual"),
  related='''        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
