# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def nums(style="", vals=("1,284,000", "9,827,500", "1,111,100"), w="150px", label=""):
    cells = "".join('<div style="text-align:right;font-size:12px;' + style + '">' + v + '</div>' for v in vals)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:3px;'
            'border:1px dashed var(--line-strong);border-radius:5px;padding:8px;background:var(--surface)">'
            + cells + '</div>'
            + ('<div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center;margin-top:6px">' + label + '</div>' if label else ''))

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="font-size:20px;font-weight:800;font-variant-numeric:tabular-nums">₩1,284,000</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">font-variant-numeric: tabular-nums</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">글꼴에 tnum 기능이 없으면 안 먹는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">text-align: right   — 자릿수를 오른쪽에 맞춘다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">toLocaleString('ko-KR')   — 천 단위 쉼표</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">등폭 글꼴   — 기능 없는 글꼴의 대안</div>
                </div>
              </div>'''

D = dict(
  slug="numerals", ko="숫자 꼴", en="Numerals · tabular figures",
  desc="숫자 너비가 글꼴마다 다른 이유와 tabular-nums 가 안 먹는 경우를 재서 보여주는 항목.",
  lede="숫자의 <b>너비</b>. 세로로 쌓이는 표나 1초마다 바뀌는 값에서 자릿수가 흔들리면 읽을 수 없습니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>가운데 표가 <b>글꼴마다 직접 재서</b> 알려 줍니다 — '원래 고름'인지, '켜니 고르게 됨'인지,
          <b>'켜도 안 바뀜 — 기능 없음'</b>인지.<br>
          <code>tabular-nums</code>는 <b>글꼴에 그 기능이 있을 때만</b> 먹습니다. 세리프 계열에는 대개 없어서
          켜도 아무 일이 일어나지 않습니다. 위의 큰 숫자에서 <b>흔들린 폭</b>이 실시간으로 쌓이는 것도 보세요.</p>
        </div>''',
  names=rows([
    ("한국어", "숫자 꼴, 등폭 숫자, 고정폭 숫자"),
    ("영어", "tabular figures, tabular-nums, lining figures, oldstyle figures"),
    ("같이 쓰는 말",
     "너비가 다 같은 숫자를 <b>등폭 숫자</b>(tabular figures), 글자마다 다른 것을 "
     "<b>비례 숫자</b>(proportional figures)라 합니다. 높이가 들쭉날쭉한 옛 스타일 숫자는 "
     "<b>올드스타일</b>(oldstyle · text figures), 키가 고른 것은 <b>라이닝</b>(lining)입니다. "
     "글꼴 안의 기능 이름은 <code>tnum</code>·<code>pnum</code>입니다."),
    ("자주 잘못 부름",
     "<b>등폭 글꼴</b> — <b>모든 글자</b>가 같은 너비인 글꼴(코드용)과, <b>숫자만</b> 같은 너비인 기능은 다릅니다.<br>"
     "<b><code>text-align: right</code></b> — 오른쪽 맞춤은 자릿수를 <b>끝에서</b> 맞출 뿐, 너비 자체는 안 바꿉니다.<br>"
     "<b>천 단위 쉼표</b> — 자릿수 읽기를 돕지만 <b>흔들림은 못 막습니다</b>."),
  ]),
  axes=ax("숫자 꼴"),
  oneline="<code>tabular-nums</code>는 <b>글꼴이 지원할 때만</b> 먹습니다. 중요한 자리라면 켜 놓고 끝내지 말고 <b>재 보고</b> 정해야 합니다.",
  s4_title="갈래", s4_hint="글꼴마다 사정이 다르다",
  states=states([
    (nums("font-variant-numeric:tabular-nums", label="고른 숫자"), "고름", "자릿수가 <b>세로로 맞는다.</b> 표의 기본"),
    (nums("font-family:Georgia,serif", label="비례 숫자"), "흔들림", "'1'이 좁아 <b>쉼표 자리가 줄마다 어긋난다</b>"),
    (nums("font-family:Georgia,serif;font-variant-numeric:tabular-nums", label="켜도 안 바뀜"),
     "기능 없음", "<b>켜도 그대로.</b> 글꼴에 그 기능이 없다"),
    (nums("font-family:var(--mono)", label="등폭 글꼴"), "등폭 글꼴", "<b>확실한 대안.</b> 숫자만 등폭으로 바꿔 쓰기도 한다"),
    (nums("font-variant-numeric:tabular-nums", ("1,284,000", "982,500", "11,100"), label="자릿수가 다르면"),
     "자릿수 차이", "등폭이어도 <b>자릿수가 다르면</b> 길이는 다르다 — 오른쪽 맞춤이 함께 필요"),
    (nums("font-variant-numeric:tabular-nums;text-align:right", ("1,284,000", "982,500", "11,100"), label="+ 오른쪽 맞춤"),
     "+ 오른쪽 맞춤", "<b>등폭 + 오른쪽 맞춤</b>이라야 비로소 자릿수가 읽힌다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바뀌는 숫자", "value", "금액·시간·카운트다운. <b>값이 바뀌어도 자리가 안 흔들려야</b> 한다"),
    ("등폭 켜기", "tabular-nums", "숫자마다 <b>같은 너비</b>를 쓰게 한다"),
    ("글꼴 지원", "tnum feature", "<b>글꼴에 이 기능이 없으면 아무 일도 안 일어난다.</b> 한글 글꼴에 특히 흔하다"),
    ("오른쪽 맞춤", "text-align: right", "자릿수를 <b>끝에서</b> 맞춘다. 등폭과 둘 다 있어야 표가 읽힌다"),
    ("천 단위 쉼표", "toLocaleString", "읽기를 돕는다. 통화·소수점 규칙도 이걸로 맞춘다"),
    ("등폭 글꼴", "monospace", "기능이 없는 글꼴을 만났을 때의 <b>확실한 대안</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>tabular-nums</code>를 켜 두고 <b>된 줄 아는 것</b>이 가장 흔한 실수입니다.
          이 속성은 <b>글꼴 안의 기능을 켜는 스위치</b>일 뿐이라, 그 기능이 없는 글꼴에서는
          아무 일도 일어나지 않고 경고도 없습니다. 글꼴을 바꾸는 날 조용히 깨지는 자리이기도 합니다 —
          <b>개발자 도구에서 숫자 너비를 재 보는 것</b>이 유일한 확인 방법입니다.</p>''',
  do=ul([
    "<b>세로로 쌓이는 숫자</b> — 표의 금액 열, 목록의 값",
    "<b>자주 바뀌는 숫자</b> — 타이머, 카운트다운, 실시간 집계",
    "자릿수가 같은 값들을 비교해야 할 때",
  ]),
  dont=ul([
    "읽는 <b>문장 속 숫자</b> — 비례 숫자가 더 자연스럽습니다",
    "켜 놓고 확인 안 하는 것 — <b>글꼴이 지원하는지 재 봐야</b> 합니다",
    "오른쪽 맞춤 없이 등폭만 — 자릿수가 다르면 여전히 어긋납니다",
    "숫자만 다른 글꼴로 바꾸는 것 — <b>글자와 숫자의 높이</b>가 안 맞을 수 있습니다",
  ]),
  instead='표 전체의 짜임은 데이터 테이블(10부), 큰 숫자 하나는 <a href="../items/stat.html">스탯 타일</a>, 글꼴 파일 문제는 <a href="webfont.html">웹폰트</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;overflow:hidden;font-variant-numeric:tabular-nums">
                <div style="display:flex;padding:5px 8px;background:var(--bg);font-size:10px;font-weight:700;color:var(--fg-muted)"><span style="flex:1">가맹점</span><span>매출</span></div>
                <div style="display:flex;padding:5px 8px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">모란상회</span><span>1,284,000</span></div>
                <div style="display:flex;padding:5px 8px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">새벽상사</span><span>11,100</span></div>
              </div>''',
     "표의 금액 열", "<b>등폭 + 오른쪽 맞춤</b>. 둘 다 있어야 자릿수가 읽힌다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:3px;text-align:center">
                <span style="font-size:11px;color:var(--fg-muted)">남은 시간</span>
                <span style="font-size:22px;font-weight:800;font-variant-numeric:tabular-nums">02:41:08</span>
              </div>''',
     "카운트다운", "1초마다 바뀐다. <b>안 켜면 숫자가 춤춘다</b>"),
    ('''              <div style="width:100%;max-width:190px;font-size:12px;line-height:1.8">
                이번 주에는 <b>42</b>건이 들어왔고 그중 <b>7</b>건이 아직 검토 중입니다.
              </div>''',
     "문장 속 숫자", "여기는 <b>기본값(비례 숫자)</b>이 더 자연스럽다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="켜고 나서 재 본다",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="한 줄로 켜고, <b>정말 먹었는지 재 보는</b> 한 줄을 더 둡니다.",
  code='''<span class="c">/* 표·타이머처럼 자릿수가 맞아야 하는 곳 */</span>
<span class="t">.amount</span>, <span class="t">.timer</span>, <span class="t">td</span> {
  <span class="a">font-variant-numeric</span>: tabular-nums;
  <span class="a">text-align</span>: right;      <span class="c">/* 둘 다 있어야 읽힌다 */</span>
}

<span class="c">// 천 단위 쉼표와 통화는 로케일에 맡긴다</span>
<span class="t">new</span> Intl.NumberFormat(<span class="s">'ko-KR'</span>,
  { style: <span class="s">'currency'</span>, currency: <span class="s">'KRW'</span> }).format(<span class="a">1284000</span>);

<span class="c">// 글꼴이 정말 지원하는지 재 본다</span>
<span class="t">const</span> p = document.createElement(<span class="s">'span'</span>);
p.style.cssText = <span class="s">'position:absolute;visibility:hidden;font-variant-numeric:tabular-nums'</span>;
document.body.append(p);
p.textContent = <span class="s">'1111'</span>; <span class="t">const</span> a = p.offsetWidth;
p.textContent = <span class="s">'0000'</span>; <span class="t">const</span> ok = (a === p.offsetWidth);''',
  keys=kbd([
    ("표와 타이머에 켠다", "세로로 쌓이거나 자주 바뀌는 숫자"),
    ("오른쪽 맞춤과 함께", "등폭만으로는 <b>자릿수가 다른 값</b>이 안 맞는다"),
    ("정말 먹는지 재 본다", "글꼴에 기능이 없으면 <b>조용히 아무 일도 안 일어난다</b>"),
    ("안 되면 등폭 글꼴", "숫자만 <code>font-family</code>를 바꾸는 방법도 있다"),
    ("문장 속 숫자는 그대로", "읽는 글에서는 비례 숫자가 더 자연스럽다"),
    ("쉼표는 <code>Intl</code>로", "통화 기호·소수점·자릿수 규칙이 나라마다 다르다"),
  ]),
  backend=rows([
    ("서식은 어디서 하나", "<code>1284000</code>을 내려주고 <b>화면에서 서식</b>을 입히는 쪽이 낫습니다. 서버가 '₩1,284,000' 문자열을 보내면 정렬도 계산도 못 합니다."),
    ("소수점과 반올림", "금액은 <b>정수로</b> 다루고 화면에서만 나눕니다. 부동소수점으로 돈을 세면 1원이 사라집니다."),
    ("통화와 로케일", "<code>Intl.NumberFormat</code>이 통화 기호 위치·쉼표·소수 자릿수를 한 번에 맞춰 줍니다."),
    ("큰 수 줄이기", "'₩12.8억'처럼 줄일지는 화면이 정합니다. <b>어디서 반올림할지</b>를 한 군데에 모아 두지 않으면 화면마다 숫자가 달라집니다."),
  ]),
  plat_lede="두 OS 는 숫자 꼴을 <b>글꼴 설정</b>으로 고릅니다.",
  plats=plats([
    ("웹", "font-variant-numeric",
     nums("font-variant-numeric:tabular-nums", ("1,284,000", "11,100"), "120px"),
     "<code>tabular-nums</code>. <b>글꼴이 지원할 때만</b> 먹는다는 점이 함정입니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.monospacedDigit( )<br>.font(.body<br>&nbsp;.monospacedDigit( ))</div>''',
     "<b><code>.monospacedDigit()</code></b> 한 줄입니다. 시스템 글꼴이 지원해서 <b>늘 먹습니다</b>."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FontFeature("tnum")<br>fontFeatureSettings</div>''',
     "<code>fontFeatureSettings = &quot;tnum&quot;</code>. 역시 글꼴에 기능이 있어야 합니다."),
  ]),
  plat_note="iOS 는 <b>시스템 글꼴이 늘 지원</b>해서 한 줄로 끝나지만, 웹에서는 <b>쓰는 한글 글꼴에 그 기능이 있는지</b>부터 확인해야 합니다. \"숫자가 흔들려요\"라는 제보에 앱 개발자가 공감하지 못하는 이유이기도 합니다.",
  siblings=siblings("numerals"),
  related='''        <li><a href="../items/stat.html"><b>스탯 타일</b><em>5부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><span class="na"><b>데이터 테이블</b><em>10부</em></span></li>''',
)
