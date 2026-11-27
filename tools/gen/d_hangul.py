# -*- coding: utf-8 -*-
from ax3 import ax
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
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">line-height: 1.8   — 받침 때문에 더 넓게</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">letter-spacing: 0   — 한글은 건드리지 않는다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">lang="ko"   — 줄바꿈·글꼴 고르기의 기준</div>
                </div>
              </div>'''

D = dict(
  slug="hangul", ko="한글 조판", en="Korean typography",
  desc="한글 줄바꿈(word-break: keep-all)과 행간, 영문 혼용, lang 속성까지 한국어 화면의 글자 규칙을 보여주는 항목.",
  lede="브라우저의 기본 줄바꿈은 <b>영문 기준</b>입니다. 그대로 두면 한글은 <b>어절 한가운데서</b> 줄이 넘어갑니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>칸 너비를 줄여 보세요. 세 상자 아래에 <b>어절이 몇 군데 쪼개졌는지</b> 재서 알려 줍니다 —
          기본값(normal)과 <code>break-all</code>은 '입금됩 / 니다'처럼 끊기고,
          <code>keep-all</code>만 어절을 지킵니다.<br>
          아래 두 상자는 <b>긴 영문 덩어리</b>가 섞였을 때입니다. <code>keep-all</code>만 쓰면
          칸을 밀어내고(넘친 px 을 재서 보여 줍니다), <code>overflow-wrap</code>을 함께 써야 막힙니다.</p>
        </div>''',
  names=rows([
    ("한국어", "한글 조판, 한글 타이포그래피, 줄바꿈"),
    ("영어", "Korean typography, word-break, line breaking, CJK"),
    ("같이 쓰는 말",
     "띄어쓰기로 나뉘는 덩어리를 <b>어절</b>이라 하고, 줄을 넘길 수 있는 자리를 "
     "<b>줄바꿈 기회</b>(line break opportunity)라 합니다. 한중일 글자를 묶어 <b>CJK</b>라 부르고, "
     "글자가 네모 칸에 꽉 차는 성질 때문에 <b>전각</b>(full-width)이라 합니다."),
    ("자주 잘못 부름",
     "<b><code>word-break: break-all</code></b> — 이름 때문에 '단어를 지킨다'로 오해하기 쉬운데 "
     "<b>반대로 아무 데서나 쪼갭니다</b>. 한국어 화면에 쓰면 안 됩니다.<br>"
     "<b><code>white-space: nowrap</code></b> — 줄바꿈을 <b>아예 막는</b> 것입니다. 어절 보호와 다릅니다.<br>"
     "<b>자간</b> — 한글이 답답해 보이는 이유는 대개 자간이 아니라 <b>행간</b>입니다."),
  ]),
  axes=ax("한글 조판"),
  oneline="한국어 화면이면 <b><code>word-break: keep-all</code>을 기본으로 깔고</b> 시작합니다. 안 깔면 모든 문단이 어절 한가운데서 끊깁니다.",
  s4_title="갈래", s4_hint="같은 글, 다른 줄바꿈",
  states=states([
    (krbox(), "기본값", "어절 한가운데서 끊긴다. <b>'입금됩 / 니다'</b>"),
    (krbox("word-break:keep-all"), "keep-all", "<b>어절을 지킨다.</b> 한국어 화면의 기본값으로 삼는다"),
    (krbox("word-break:break-all"), "break-all", "아무 데서나 쪼갠다. <b>이름과 달리</b> 단어를 안 지킨다"),
    (krbox("word-break:keep-all;overflow-wrap:normal", "확인 코드는 TX99120KR2026SETTLEMENTCONFIRM 입니다."),
     "긴 영문", "<b>keep-all 만으로는 안 막힌다.</b> 영문 덩어리가 칸을 밀어낸다"),
    (krbox("word-break:keep-all;overflow-wrap:anywhere", "확인 코드는 TX99120KR2026SETTLEMENTCONFIRM 입니다."),
     "+ overflow-wrap", "<b>한글은 어절로, 어쩔 수 없는 영문만</b> 쪼갠다"),
    (krbox("word-break:keep-all;line-height:1.35"), "행간이 좁을 때",
     "줄바꿈이 맞아도 <b>행간이 좁으면</b> 여전히 답답하다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("한국어 문단", "paragraph", "이 네댓 줄에 걸리는 값이 아래의 다섯 가지다"),
    ("어절 지키기", "word-break: keep-all", "<b>한국어 화면의 첫 줄.</b> 띄어쓰기에서만 줄을 넘긴다"),
    ("긴 덩어리 쪼개기", "overflow-wrap: break-word", "주문번호·URL 처럼 <b>띄어쓰기 없는 영문</b>만 어쩔 수 없이 쪼갠다"),
    ("행간", "line-height", "한글은 받침이 있어 글자가 아래로 길다. <b>영문 기준보다 한 단계 넓게</b>"),
    ("자간", "letter-spacing", "본문은 0. 한글은 조금만 벌려도 <b>낱글자로 흩어진다</b>"),
    ("언어 표시", "lang=\"ko\"", "줄바꿈 규칙·글꼴 고르기·스크린 리더 발음이 <b>이것부터</b> 갈린다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>keep-all</code>과 <code>overflow-wrap</code>은 <b>둘 다 있어야</b> 합니다.
          keep-all 만 있으면 긴 영문 한 덩어리가 칸을 밀어내 가로 스크롤을 만들고,
          overflow-wrap 만 있으면 한글이 여전히 어절 한가운데서 끊깁니다.
          이 도감도 <code>base.css</code> 맨 위에 <b>두 줄을 함께</b> 깔아 두고 시작합니다.</p>''',
  do=ul([
    "<b>한국어가 들어가는 모든 화면</b> — 예외가 없습니다",
    "좁은 칸에 긴 문장이 들어갈 때 — 카드 제목, 알림, 빈 상태 문구",
    "영문·주문번호·URL 이 섞이는 글",
  ]),
  dont=ul([
    "<code>break-all</code>을 쓰는 것 — 이름만 보고 고르면 <b>정반대</b>가 됩니다",
    "문장을 <code>&lt;br&gt;</code>로 손수 끊는 것 — 화면 폭이 바뀌면 <b>엉뚱한 데서</b> 끊깁니다",
    "자간을 벌려 '시원하게' 만드는 것 — 한글은 흩어져 보입니다",
    "<code>lang</code>을 안 적는 것 — 브라우저가 어느 규칙을 쓸지 모릅니다",
  ]),
  instead='줄 사이는 <a href="lineheight.html">행간</a>, 글자 사이는 <a href="letterspacing.html">자간</a>, 넘친 글의 끝은 <a href="truncate.html">말줄임</a>이 맡습니다.',
  cases=cases([
    (krbox("word-break:keep-all", "환불 확인 요청 — 카드 승인 취소가 늦어진 건", "160px"),
     "카드 제목", "좁은 칸일수록 티가 난다. <b>어절이 지켜져야</b> 읽힌다"),
    (krbox("word-break:keep-all;line-height:1.85", "정산 요청이 승인되면 영업일 기준 2일 안에 등록하신 계좌로 입금됩니다.", "160px"),
     "안내 문구", "줄바꿈 + 행간이 같이 맞아야 <b>비로소 읽기 편하다</b>"),
    (krbox("word-break:keep-all;overflow-wrap:anywhere", "코드 TX99120KR2026SETTLE 를 입력하세요.", "160px"),
     "코드가 섞인 글", "<b>두 속성을 함께</b> — 한글은 어절로, 코드만 쪼갠다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="한국어 화면의 첫 두 줄",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="<b>두 줄</b>이면 거의 끝납니다. 문서 맨 위에 한 번 깔고 시작합니다.",
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
    ("<code>keep-all</code>을 깐다", "한국어 화면이면 <b>예외 없이</b>. 이름이 헷갈리는 <code>break-all</code>과 반대다"),
    ("<code>overflow-wrap</code>을 함께", "둘 중 하나만 쓰면 <b>절반만</b> 해결된다"),
    ("<code>lang=\"ko\"</code>", "줄바꿈 규칙과 글꼴 고르기, 스크린 리더 발음이 여기서 갈린다"),
    ("행간을 한 단계 넓게", "영문 기준 1.5 면 한글은 1.7~1.8"),
    ("<code>&lt;br&gt;</code>로 끊지 않는다", "폭이 바뀌면 <b>엉뚱한 자리</b>에서 끊긴다. 줄바꿈은 브라우저에 맡긴다"),
    ("자간은 0", "본문에서 벌리면 <b>낱글자로 흩어진다</b>. 큰 제목만 조금 좁힌다"),
  ]),
  backend=rows([
    ("글 길이는 데이터가 정한다", "'가맹점명'이 3자일 때와 30자일 때 화면이 다릅니다. <b>가장 긴 값</b>으로 한 번 그려 보는 것이 최소 테스트입니다."),
    ("문장을 쪼개 보내지 않는다", "'…되면'과 '입금됩니다'를 따로 내려 화면에서 이어 붙이면 <b>번역과 줄바꿈이 둘 다 깨집니다.</b> 문장 단위로 보냅니다."),
    ("다국어", "같은 문장이 영어로는 1.3배, 일본어로는 비슷합니다. 칸 크기를 한국어 기준으로만 잡으면 <b>다른 언어에서 터집니다.</b>"),
    ("검색과 정렬", "한글 정렬은 <code>localeCompare('ko')</code>를 써야 'ㄱㄴㄷ' 순이 됩니다. 바이트 순으로 하면 자모가 뒤섞입니다."),
    ("글꼴 파일", "한글은 완성형만 1만 1172자라 <b>파일이 수 MB</b>입니다. 서브셋이 거의 필수입니다 — <a href=\"webfont.html\">웹폰트</a> 참고."),
  ]),
  plat_lede="두 OS 는 한글 줄바꿈을 <b>기본으로 맞게</b> 처리합니다. 웹만 설정이 필요합니다.",
  plats=plats([
    ("웹", "word-break: keep-all",
     krbox("word-break:keep-all", "정산 요청이 승인되면 입금됩니다.", "118px"),
     "기본값이 <b>영문 규칙</b>이라 직접 켜야 합니다. 이 한 줄을 모르면 모든 문단이 어절 한가운데서 끊깁니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 한글 줄바꿈 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;font-size:7px;line-height:1.9">정산 요청이<br>승인되면<br>입금됩니다.</div>
              </div></div>''',
     "<b>기본으로 어절을 지킵니다.</b> 설정할 것이 없고, 한글 글꼴도 OS 에 들어 있어 웹폰트 문제가 없습니다."),
    ("안드로이드", "Android",
     '''              <div class="phone" role="img" aria-label="안드로이드 한글 줄바꿈 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;font-size:7px;line-height:1.9">정산 요청이<br>승인되면<br>입금됩니다.</div>
              </div></div>''',
     "역시 <b>기본이 어절 단위</b>입니다. <code>breakStrategy</code> 로 더 다듬을 수 있습니다."),
  ]),
  plat_note="앱 개발자에게 <b>\"한글이 중간에서 끊겨요\"는 낯선 증상</b>입니다. 두 OS 모두 기본으로 어절을 지키기 때문입니다. 웹에서만 생기는 문제라, 같은 화면을 세 쪽에서 만들면 <b>웹만 줄바꿈이 다르게</b> 보이는 일이 흔합니다.",
  siblings=siblings("hangul"),
  related='''        <li><a href="../items/lineheight.html"><b>행간</b><em>3부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/container.html"><b>컨테이너와 최대 폭</b><em>1부</em></a></li>
        <li><span class="na"><b>한국어 UI 문구</b><em>14부</em></span></li>''',
)
