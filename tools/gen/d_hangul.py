# -*- coding: utf-8 -*-
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def krbox(style="", txt="정산 요청이 승인되면 영업일 기준 2일 안에 입금됩니다.", w="146px"):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px dashed var(--line-strong);'
            'border-radius:5px;padding:8px;background:var(--surface)">'
            '<p style="margin:0;font-size:11px;line-height:1.85;max-width:none;' + style + '">' + txt + '</p></div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:230px;border:1px dashed var(--line-strong);border-radius:6px;padding:9px;background:var(--surface)">
                    <p style="margin:0;font-size:12px;line-height:1.85;max-width:none;word-break:keep-all">정산 요청이 승인되면 영업일 기준 2일 안에 등록하신 계좌로 입금됩니다.</p>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">word-break: keep-all</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">overflow-wrap: break-word</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">line-height: 1.8   받침 때문에 더 넓게 잡음</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">letter-spacing: 0   한글은 건드리지 않음</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">lang="ko"   줄바꿈과 글꼴을 고르는 기준</div>
                </div>
              </div>'''

D = dict(
  slug="hangul", ko="한글 조판", en="Korean typography",
  desc="한글 줄바꿈(word-break: keep-all)과 행간, 영문 혼용, lang 속성까지 한국어 화면에서 지킬 글자 규칙을 보여 주는 항목입니다.",
  lede="브라우저의 기본 줄바꿈 규칙은 <b>영문 기준</b>이라서, 설정을 그대로 두면 한글은 <b>어절 한가운데서</b> 줄이 넘어갑니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>칸 너비를 줄여 보세요. 세 상자 아래에 <b>어절이 몇 군데 쪼개졌는지</b> 재서 알려 줍니다.
          기본값(normal)과 <code>break-all</code>은 '입금됩 / 니다'처럼 어절 중간에서 끊기고,
          <code>keep-all</code>만 어절을 지킵니다.<br>
          아래 두 상자는 <b>긴 영문 덩어리</b>가 섞인 경우입니다. <code>keep-all</code>만 쓰면
          영문 덩어리가 칸을 밀어내는데(넘친 px을 재서 보여 줍니다), <code>overflow-wrap</code>을 함께 써야 넘치지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "한글 조판, 한글 타이포그래피, 줄바꿈"),
    ("영어", "Korean typography, word-break, line breaking, CJK"),
    ("같이 쓰는 말",
     "띄어쓰기로 나뉘는 덩어리를 <b>어절</b>이라고 하고, 줄을 넘길 수 있는 자리를 "
     "<b>줄바꿈 기회</b>(line break opportunity)라고 합니다. 한중일 글자는 묶어서 <b>CJK</b>라고 부르며, "
     "글자가 네모 칸을 꽉 채우기 때문에 <b>전각</b>(full-width) 글자라고도 합니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>word-break: break-all</code></b> — 이름 때문에 '단어를 지킨다'로 오해하기 쉽지만 "
     "실제로는 <b>반대로 아무 데서나 쪼갭니다</b>. 그래서 한국어 화면에 쓰면 안 됩니다.<br>"
     "<b><code>white-space: nowrap</code></b> — 줄바꿈을 <b>아예 막는</b> 속성이라서, 어절에서만 줄을 넘기는 어절 보호와는 다릅니다.<br>"
     "<b>자간</b> — 한글이 답답해 보이는 이유는 대개 자간이 아니라 <b>행간</b>입니다."),
  ]),
  s4_title="줄바꿈 설정에 따른 차이", s4_hint="같은 글을 줄바꿈 설정만 바꿔 본 모습",
  states=states([
    (krbox(), "기본값(normal)을 그대로 둘 때", "<b>'입금됩 / 니다'</b>처럼 어절 한가운데서 끊깁니다"),
    (krbox("word-break:keep-all"), "keep-all로 어절을 지킬 때", "<b>어절을 지킵니다.</b> 한국어 화면에서는 이 값을 기본으로 씁니다"),
    (krbox("word-break:break-all"), "break-all을 썼을 때", "아무 데서나 쪼갭니다. <b>이름과 달리</b> 단어를 지키지 않습니다"),
    (krbox("word-break:keep-all;overflow-wrap:normal", "확인 코드는 TX99120KR2026SETTLEMENTCONFIRM 입니다."),
     "긴 영문이 섞였을 때", "<b>keep-all만으로는 넘침을 막지 못합니다.</b> 띄어쓰기 없는 영문 덩어리가 칸을 밀어냅니다"),
    (krbox("word-break:keep-all;overflow-wrap:anywhere", "확인 코드는 TX99120KR2026SETTLEMENTCONFIRM 입니다."),
     "overflow-wrap을 함께 썼을 때", "<b>한글은 어절 단위로 넘기고, 칸에 들어가지 않는 영문만</b> 쪼갭니다"),
    (krbox("word-break:keep-all;line-height:1.35"), "행간이 좁을 때",
     "줄바꿈이 맞아도 <b>행간이 좁으면</b> 여전히 답답해 보입니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("한국어 문단", "paragraph", "이 네댓 줄짜리 문단에 아래 다섯 가지 값이 함께 적용됩니다"),
    ("어절 지키기", "word-break: keep-all", "<b>한국어 화면에서 가장 먼저 적는 줄</b>로, 띄어쓰기 자리에서만 줄을 넘깁니다"),
    ("긴 덩어리 쪼개기", "overflow-wrap: break-word", "주문번호나 URL처럼 <b>띄어쓰기 없는 영문</b>이 칸에 들어가지 않을 때만 쪼갭니다"),
    ("행간", "line-height", "한글은 받침이 있어 글자가 아래로 길기 때문에 <b>영문 기준보다 한 단계 넓게</b> 잡습니다"),
    ("자간", "letter-spacing", "본문은 0으로 둡니다. 한글은 조금만 벌려도 <b>낱글자로 흩어져</b> 보입니다"),
    ("언어 표시", "lang=\"ko\"", "브라우저는 <b>이 값을 보고</b> 줄바꿈 규칙과 글꼴, 스크린 리더 발음을 정합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>keep-all</code>과 <code>overflow-wrap</code>은 <b>둘 다 있어야</b> 합니다.
          keep-all만 있으면 긴 영문 한 덩어리가 칸을 밀어내 가로 스크롤이 생기고,
          overflow-wrap만 있으면 한글이 여전히 어절 한가운데서 끊깁니다.
          그래서 이 도감도 <code>base.css</code> 맨 위에 <b>두 줄을 함께</b> 적어 두고 시작합니다.</p>''',
  do=ul([
    "<b>한국어가 들어가는 모든 화면</b>을 만들 때. 예외가 없습니다",
    "카드 제목이나 알림, 빈 상태 문구처럼 좁은 칸에 긴 문장이 들어갈 때",
    "영문이나 주문번호, URL이 섞인 글을 보여 줄 때",
  ]),
  dont=ul([
    "어절을 지키려고 <code>break-all</code>을 고를 때. 이름만 보고 고르면 <b>정반대</b>로 동작합니다",
    "문장을 <code>&lt;br&gt;</code>로 직접 끊을 때. 화면 폭이 바뀌면 <b>엉뚱한 자리에서</b> 끊깁니다",
    "자간을 벌려 '시원하게' 보이게 하려 할 때. 한글은 흩어져 보입니다",
    "<code>lang</code>을 적지 않을 때. 브라우저가 어느 언어의 규칙을 써야 할지 알 수 없습니다",
  ]),
  do_title="한글 조판 규칙을 적용할 때", dont_title="한글 조판에서 피할 것",
  instead_title="한글 조판과 이어지는 주제를 다루는 항목",
  instead='줄과 줄 사이의 거리는 <a href="lineheight.html">행간</a>에서, 글자와 글자 사이의 거리는 <a href="letterspacing.html">자간</a>에서 다룹니다. 칸을 넘친 글의 끝을 처리하는 방법은 <a href="truncate.html">말줄임</a>에 있습니다.',
  cases=cases([
    (krbox("word-break:keep-all", "환불 확인 요청 — 카드 승인 취소가 늦어진 건", "160px"),
     "좁은 카드 제목에서 어절 지키기", "칸이 좁을수록 줄바꿈 차이가 크게 드러나는데, <b>어절이 지켜져야</b> 제대로 읽힙니다"),
    (krbox("word-break:keep-all;line-height:1.85", "정산 요청이 승인되면 영업일 기준 2일 안에 등록하신 계좌로 입금됩니다.", "160px"),
     "긴 안내 문구를 읽기 편하게", "줄바꿈과 행간이 함께 맞아야 <b>읽기 편합니다</b>"),
    (krbox("word-break:keep-all;overflow-wrap:anywhere", "코드 TX99120KR2026SETTLE 를 입력하세요.", "160px"),
     "코드가 섞인 글 줄바꿈하기", "<b>두 속성을 함께</b> 써서 한글은 어절 단위로 넘기고, 코드만 쪼갭니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="한국어 화면에 먼저 적는 두 줄",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="한글 조판은 CSS <b>두 줄</b>로 대부분 해결됩니다. 문서 맨 위에 한 번 적어 두고 시작합니다.",
  code='''&lt;<span class="t">html</span> <span class="a">lang</span>=<span class="s">"ko"</span>&gt;   <span class="c">&lt;!-- 줄바꿈·글꼴·발음의 기준 --&gt;</span>

<span class="t">body</span> {
  <span class="a">word-break</span>: keep-all;        <span class="c">/* 어절을 지킨다 */</span>
  <span class="a">overflow-wrap</span>: break-word;   <span class="c">/* 긴 영문 덩어리만 쪼갠다 */</span>
  <span class="a">line-height</span>: <span class="a">1.7</span>;             <span class="c">/* 받침 때문에 넓게 */</span>
}

<span class="c">/* 제목은 좁게, 자간만 살짝 */</span>
<span class="t">h1</span>, <span class="t">h2</span> { <span class="a">line-height</span>: <span class="a">1.3</span>; <span class="a">letter-spacing</span>: -<span class="a">0.02em</span>; }

<span class="c">/* 본문 자간은 건드리지 않는다 */</span>
<span class="t">p</span> { <span class="a">letter-spacing</span>: <span class="a">0</span>; }''',
  keys=kbd([
    ("<code>keep-all</code>을 기본으로 적기", "한국어 화면이면 <b>예외 없이</b> 씁니다. 이름이 헷갈리는 <code>break-all</code>과는 반대로 동작합니다"),
    ("<code>overflow-wrap</code>을 함께 적기", "둘 중 하나만 쓰면 어절 쪼개짐과 영문 넘침 가운데 <b>하나만</b> 해결됩니다"),
    ("<code>lang=\"ko\"</code> 적어 두기", "브라우저가 이 값을 보고 줄바꿈 규칙과 글꼴, 스크린 리더 발음을 정합니다"),
    ("행간을 한 단계 넓게 잡기", "영문 기준이 1.5라면 한글은 1.7~1.8을 씁니다"),
    ("<code>&lt;br&gt;</code>로 직접 끊지 않기", "화면 폭이 바뀌면 <b>엉뚱한 자리</b>에서 끊기므로, 줄바꿈은 브라우저에 맡깁니다"),
    ("본문 자간은 0으로 두기", "본문에서 벌리면 <b>낱글자로 흩어져</b> 보입니다. 큰 제목만 조금 좁힙니다"),
  ]),
  backend=rows([
    ("데이터에 따라 달라지는 글 길이", "'가맹점명'이 3자일 때와 30자일 때는 화면이 달라집니다. 그래서 적어도 한 번은 <b>가장 긴 값</b>을 넣어 화면을 그려 봐야 합니다."),
    ("문장을 한 덩어리로 보내기", "'…되면'과 '입금됩니다'를 따로 내려보내 화면에서 이어 붙이면 <b>번역과 줄바꿈이 둘 다 어긋납니다.</b> 그래서 문장은 한 덩어리로 보냅니다."),
    ("언어마다 다른 글 길이", "같은 문장이라도 영어로는 길이가 1.3배쯤 되고, 일본어로는 비슷합니다. 칸 크기를 한국어 기준으로만 잡으면 <b>다른 언어에서는 글이 칸을 넘칩니다.</b>"),
    ("한글을 가나다순으로 정렬하기", "한글은 <code>localeCompare('ko')</code>로 정렬해야 'ㄱㄴㄷ' 순이 됩니다. 바이트 순으로 정렬하면 자모 순서가 뒤섞입니다."),
    ("한글 글꼴 파일의 크기", "한글은 완성형만 1만 1172자라서 글꼴 <b>파일이 수 MB</b>나 됩니다. 그래서 쓰는 글자만 남기는 서브셋이 거의 필수입니다. 자세한 내용은 <a href=\"webfont.html\">웹폰트</a> 항목을 보세요."),
  ]),
  plat_lede="두 OS는 한글 줄바꿈을 <b>기본 설정에서 맞게</b> 처리하기 때문에, 따로 설정이 필요한 것은 웹뿐입니다.",
  plats=plats([
    ("웹", "word-break: keep-all",
     krbox("word-break:keep-all", "정산 요청이 승인되면 입금됩니다.", "118px"),
     "기본값이 <b>영문 규칙</b>이라서 직접 켜야 합니다. 이 한 줄을 빠뜨리면 모든 문단이 어절 한가운데서 끊깁니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 한글 줄바꿈 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;font-size:7px;line-height:1.9">정산 요청이<br>승인되면<br>입금됩니다.</div>
              </div></div>''',
     "<b>기본으로 어절을 지킵니다.</b> 따로 설정할 것이 없고, 한글 글꼴도 OS에 들어 있어서 웹폰트 같은 문제가 생기지 않습니다."),
    ("안드로이드", "Android",
     '''              <div class="phone" role="img" aria-label="안드로이드 한글 줄바꿈 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;font-size:7px;line-height:1.9">정산 요청이<br>승인되면<br>입금됩니다.</div>
              </div></div>''',
     "안드로이드도 <b>기본으로 어절 단위</b>로 줄을 넘깁니다. <code>breakStrategy</code>로 줄바꿈을 더 다듬을 수 있습니다."),
  ]),
  plat_note="두 OS 모두 기본으로 어절을 지키기 때문에, 앱 개발자에게 <b>\"한글이 중간에서 끊겨요\"는 낯선 증상</b>입니다. 웹에서만 생기는 문제라서 같은 화면을 웹과 두 앱에서 만들면 <b>웹만 줄바꿈이 다르게</b> 보이는 일이 흔합니다.",
  siblings=siblings("hangul"),
  related='''        <li><a href="../items/lineheight.html"><b>행간</b><em>3부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><a href="koreanui.html"><b>한국어 UI 문구</b><em>14부</em></a></li>''',
)
