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
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">바깥 상자는 높이가 정해져 있고 여기서 스크롤함</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">받침대 height = 20000 × 36px로 막대 길이를 만듦</div>
                  <div class="pin-out" data-pin="3" style="max-width:230px">''' + scroller(['… 9,980', '… 9,981', '… 9,982', '… 9,983'], "", "230px", "60px").strip() + '''</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">실제로 그린 것은 12줄뿐</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">transform: translateY(첫 줄 번호 × 36px)</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">줄 높이가 제각각이면 이 계산이 전부 어긋남</div>
                </div>
              </div>'''

D = dict(
  slug="virtual", ko="가상 스크롤", en="Virtual scrolling",
  desc="수만 줄짜리 목록에서 보이는 줄만 그리는 가상 스크롤을 받침대 높이, 창 계산, 고정 줄 높이라는 제약과 대안까지 다루는 항목입니다.",
  lede="가상 스크롤은 목록이 수만 줄이어도 화면에 <b>보이는 줄만</b> 그려서 브라우저가 느려지지 않게 하는 기법입니다. 대신 안 그린 줄은 찾기·인쇄·스크린 리더에서 빠지므로 <b>잃는 것</b>도 분명합니다.",
  axes_lede="데이터 화면은 '건수가 늘면 어떻게 되나'부터 따집니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>가상 스크롤</b>을 끄고 2만 줄을 그려 보세요. 그리는 데 걸린 시간과
          <b>실제로 만들어진 DOM 노드 수</b>가 아래에 나옵니다.<br>
          가상 스크롤을 켜면 노드 수가 <b>열몇 개</b>로 줄어듭니다. 그런데도 스크롤 막대 길이가 그대로인 것은
          빈 받침대 하나가 <b>전체 목록의 높이만 차지하고</b> 있기 때문입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "가상 스크롤, 가상화, 창 띄우기"),
    ("영어", "virtual scrolling, virtualization, windowing"),
    ("같이 쓰는 말",
     "보이는 구간만 그리는 것은 <b>윈도잉</b>(windowing), "
     "전체 목록의 높이만 차지하는 빈 상자는 <b>스페이서</b>·<b>사이저</b>(sizer), "
     "보이는 구간 위아래로 조금 더 그려 두는 여유분은 <b>오버스캔</b>(overscan)이라고 합니다. "
     "리액트 쪽 라이브러리 이름(react-window, TanStack Virtual)을 기법 이름처럼 쓰기도 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>무한 스크롤</b> — <a href=\"../items/infinite.html\">무한 스크롤</a>은 데이터를 <b>더 받아오는</b> 기법이고, 가상 스크롤은 받은 데이터를 <b>덜 그리는</b> 기법입니다. 둘을 함께 쓰기도 합니다.<br>"
     "<b>페이지네이션</b> — <a href=\"../items/pagination.html\">페이지네이션</a>은 목록을 쪽으로 끊어 보여 주고, 가상 스크롤은 목록 전체를 <b>하나로 이어 둡니다</b>.<br>"
     "<b>레이지 로딩</b> — 레이지 로딩은 이미지를 필요할 때 늦게 받는 기법이라 가상 스크롤과는 다릅니다."),
  ]),
  axes=ax("가상 스크롤"),
  oneline="가상 스크롤은 다른 방법이 통하지 않을 때 꺼내는 <b>마지막 수단</b>입니다. 줄 수를 줄이거나 쪽을 나눠서 해결된다면 언제나 그쪽이 낫습니다.",
  s4_title="상태", s4_hint="줄이 늘어날 때 일어나는 일",
  states=states([
    (scroller(['모란상회', '한빛아웃도어', '새벽상사', '대림유통'], "200줄이면 그냥 다 그려도 됨"),
     "줄이 몇백 개인 작은 목록", "<b>가상 스크롤이 필요 없습니다.</b> 넣으면 코드만 복잡해집니다"),
    (scroller(['… 1', '… 2', '… 3', '… 4'], "20,000줄을 다 그려 잠시 멈춤"),
     "큰 목록을 전부 그렸을 때", "노드가 2만 개 만들어져서 처음 그릴 때 <b>화면이 잠시 멈춥니다</b>"),
    (scroller(['… 9,980', '… 9,981', '… 9,982', '… 9,983'], "보이는 12줄만 그려 노드 12개"),
     "가상 스크롤을 켰을 때", "스크롤 막대 길이는 같고 <b>그린 줄만 줄어듭니다</b>"),
    (scroller(['…', '<span class="skl" style="height:8px;width:60%;display:inline-block"></span>', '<span class="skl" style="height:8px;width:45%;display:inline-block"></span>', '…'], "빠르게 굴리면 빈 줄이 잠깐 보임"),
     "빠르게 스크롤할 때", "새 줄을 그리기 전에 <b>빈 자리</b>가 잠깐 보입니다. 이 자리는 뼈대로 채웁니다"),
    ('''              <div style="width:100%;max-width:160px">
                <div style="height:62px;border:1px solid var(--line);border-radius:6px;background:var(--surface);overflow:hidden">
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px;border-bottom:1px solid var(--line)">짧은 줄</div>
                  <div style="padding:2px 7px 3px;font-size:9.5px;line-height:12px;border-bottom:1px solid var(--line)">두 줄짜리 긴 설명이<br>들어간 줄</div>
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px;border-bottom:1px solid var(--line)">짧은 줄</div>
                  <div style="height:14px;padding:0 7px;font-size:9.5px;line-height:14px">…</div>
                </div>
                <span style="display:block;font-size:8.5px;color:var(--fg-muted);margin-top:3px">높이가 제각각이라 계산이 어긋남</span>
              </div>''',
     "줄 높이가 다를 때", "줄마다 높이를 <b>재야 합니다.</b> 그래서 구현하기가 몇 배 어려워집니다"),
    (scroller(['… 19,998', '… 19,999', '… 20,000', ''], "끝에 다다르면 더 받을지 확인"),
     "목록 끝에 다다랐을 때", "<a href=\"../items/infinite.html\">무한 스크롤</a>과 함께 쓰면 여기서 다음 묶음을 받습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("굴리는 상자", "height 고정", "상자 높이가 정해져 있어야 <b>몇 줄이 보이는지</b> 계산할 수 있습니다"),
    ("받침대", "sizer", "높이를 전체 줄 수 × 줄 높이로 잡아 <b>스크롤 막대 길이만</b> 만듭니다"),
    ("보이는 창", "window", "<code>scrollTop / 줄높이</code>로 화면에 보이는 첫 줄 번호를 구합니다"),
    ("그린 줄", "12개 남짓", "보이는 줄 위아래로 <b>두세 줄 더</b>(overscan) 그려 두면 스크롤할 때 덜 깜빡입니다"),
    ("자리 옮기기", "translateY", "<code>top</code>을 바꾸는 것보다 <code>transform</code>으로 옮기는 편이 브라우저 부담이 적습니다"),
    ("고정 줄 높이", "전제 조건", "줄 높이가 제각각이면 줄마다 <b>높이를 재야</b> 해서 구현이 훨씬 어려워집니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>가상 스크롤을 넣기 전에 잃는 것부터 따져 보세요.</b> 그리지 않은 줄은
          <kbd>Ctrl</kbd>+<kbd>F</kbd>로 찾을 수 없고, 스크린 리더도 읽지 못합니다.
          인쇄하면 화면에 보이던 열몇 줄만 나오고, 검색 엔진도 그 줄을 보지 못합니다.
          <code>Ctrl</code>+<code>A</code>로 전체를 복사해도 보이는 줄만 복사됩니다.
          그래서 <b>공개 페이지에는 거의 쓰지 않고</b> 로그인한 뒤에 쓰는 관리 도구에만 씁니다.</p>''',
  do=ul([
    "로그, 시세, 채팅처럼 줄이 <b>수천 개를 넘고</b> 쪽으로 끊어 보여 줄 수 없을 때",
    "줄 높이가 <b>모두 같을</b> 때",
    "검색이나 인쇄를 쓰지 않아도 되는, 로그인 뒤의 <b>관리 도구</b>일 때",
  ]),
  dont=ul([
    "줄이 몇백 개일 때. 요즘 브라우저는 이 정도는 무리 없이 그리므로 <b>전부 그립니다</b>",
    "공개 페이지일 때. 그리지 않은 줄은 <b>검색 엔진이 보지 못합니다</b>",
    "줄 높이가 제각각인데 직접 만들려고 할 때. 이 경우에는 <b>라이브러리를 씁니다</b>",
    "쪽을 나눌 수 있을 때. <a href=\"../items/pagination.html\">페이지네이션</a>이 만들기 쉽고 사용자도 쓰기 편합니다",
  ]),
  instead='목록을 쪽으로 끊어 보여 줘도 되면 <a href="../items/pagination.html">페이지네이션</a>을 쓰고, 스크롤하는 대로 데이터를 이어서 받아야 하면 <a href="../items/infinite.html">무한 스크롤</a>이 맞습니다. 줄이 몇백 개 정도라면 평범한 <a href="table.html">데이터 테이블</a>로 전부 그려도 됩니다.',
  cases=cases([
    (scroller(['10:21:08 OK', '10:21:09 OK', '10:21:09 WARN', '10:21:10 OK'], "", "150px"),
     "로그 화면에 쓰기", "줄 높이가 같고 줄이 수만 개라서 <b>가상 스크롤이 가장 잘 맞습니다</b>"),
    (scroller(['삼성전자 71,200', 'SK하이닉스 183,000', 'NAVER 192,400', '카카오 38,650'], "", "150px"),
     "시세 표에 쓰기", "줄이 많고 값이 <b>자주 바뀝니다</b>. 보이지 않는 줄은 화면을 고칠 필요가 없어서 이득이 큽니다"),
    (scroller(['모란상회', '한빛아웃도어', '새벽상사'], "120줄이라 그냥 다 그림", "150px"),
     "몇백 줄짜리 목록에는 쓰지 않기", "몇백 줄짜리 목록에 가상 스크롤을 넣으면 얻는 것 없이 찾기·인쇄 같은 기능만 <b>잃습니다</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="가상 스크롤을 만들 때 꼭 갖출 것",
  code_lede="받침대로 전체 길이를 만들고, 보이는 구간만 그린 뒤 <code>transform</code>으로 그 자리까지 내려 둡니다.",
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
    ("<kbd>PageDown</kbd>·<kbd>Home</kbd>·<kbd>End</kbd>", "브라우저 기본 스크롤이 그대로 동작해야 합니다. 키 입력을 <b>직접 가로채지 않습니다</b>"),
    ("<kbd>Tab</kbd>", "그리지 않은 줄로는 포커스가 갈 수 없습니다. <b>포커스가 있던 줄을 지우면</b> 포커스가 <code>&lt;body&gt;</code>로 넘어갑니다"),
    ("<code>role=\"list\"</code>에 전체 건수 적기", "'20,000건'처럼 전체 건수를 레이블에 적습니다. 그러지 않으면 스크린 리더가 그려진 12줄만 읽어서 사용자는 열두 건뿐이라고 생각합니다"),
    ("<code>aria-setsize</code>·<code>aria-posinset</code>", "줄마다 '20,000개 중 9,981번째'처럼 전체에서 몇 번째인지 알립니다"),
    ("<kbd>Ctrl</kbd>+<kbd>F</kbd>로 찾지 못하는 문제", "브라우저 찾기 기능은 그리지 않은 줄을 찾지 못하므로 <b>검색 칸을 따로</b> 둡니다"),
    ("인쇄할 때", "화면에 보이는 열몇 줄만 인쇄됩니다. 인쇄가 필요하면 <b>별도 내보내기</b>를 만듭니다"),
  ]),
  backend=rows([
    ("2만 건을 한 번에 보내지 않기", "그리는 줄은 줄었어도 서버에서 <b>받는 데이터 양은 그대로</b>입니다. 응답이 5MB라면 받는 동안 느린 것은 여전합니다."),
    ("커서 페이징", "<code>OFFSET 19000</code>을 쓰면 데이터베이스가 앞의 19,000줄을 읽어 세고 버립니다. 그래서 받은 <b>마지막 줄의 키</b>를 기준으로 다음 묶음을 받는 편이 빠릅니다."),
    ("목록 중간으로 건너뛸 때", "스크롤 막대를 끌어 목록 한가운데로 가면 그 구간을 <b>따로 요청</b>해야 합니다. 이런 요청은 커서 방식과 잘 맞지 않아서, 중간으로 뛰는 것을 허용할지에 따라 설계가 달라집니다."),
    ("받침대 높이에 필요한 전체 건수", "받침대 높이를 정하려면 <b>전체 줄 수</b>가 필요합니다. <code>COUNT(*)</code>가 오래 걸리면 어림수로 높이를 잡고, 목록 끝에 다다랐을 때 실제 줄 수로 고칩니다."),
    ("보이지 않는 줄의 데이터가 바뀔 때", "보이지 않는 줄의 데이터가 서버에서 바뀌어도 화면은 알 수 없습니다. 그래서 <b>언제 다시 받을지</b> 정해 둡니다."),
  ]),
  plat_lede="<b>iOS와 안드로이드는 처음부터 목록 부품이 이 방식으로 동작</b>하고, 웹만 직접 만들어야 합니다.",
  plats=plats([
    ("웹", "직접 또는 라이브러리",
     scroller(['… 9,981', '… 9,982', '… 9,983'], "", "120px", "48px"),
     "표준 부품이 없어서 <b>직접 만들거나</b> 라이브러리를 씁니다. 줄 높이가 제각각이면 대개 라이브러리를 씁니다."),
    ("iOS", "UITableView",
     '''              <div class="phone" role="img" aria-label="iOS 테이블뷰 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,981</div><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,982</div></div></div></div>''',
     "OS가 기본으로 <b>셀 재사용</b>(cell reuse)을 합니다. 2007년부터 이렇게 동작해 왔고, 따로 켤 설정이 없습니다."),
    ("안드로이드", "RecyclerView",
     '''              <div class="phone" role="img" aria-label="RecyclerView 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:0;right:0;top:26px"><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,981</div><div style="padding:4px 6px;font-size:6px;border-bottom:1px solid var(--line)">… 9,982</div></div></div></div>''',
     "이름에 <b>재활용</b>(recycle)이 들어 있듯이, 화면 밖으로 나간 뷰를 모아 두었다가 새로 보일 줄에 다시 씁니다."),
  ]),
  plat_note="\"목록이 느려요\"라는 말을 듣자마자 가상 스크롤을 꺼내지 마세요. 줄이 몇백 개라면 느린 원인은 보통 줄 수가 아니라 <b>줄마다 들어간 그림자·이미지·계산</b>입니다. 가상 스크롤은 줄이 수천 개인 것이 확실하고 줄 높이가 같을 때만 쓰고, 쓰기로 했다면 <b>찾기·인쇄·스크린 리더</b> 대응을 따로 만들어야 한다는 것까지 일정에 넣으세요.",
  siblings=siblings("virtual"),
  related='''        <li><a href="../items/infinite.html"><b>무한 스크롤</b><em>7부</em></a></li>
        <li><a href="../items/pagination.html"><b>페이지네이션</b><em>7부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>''',
)
