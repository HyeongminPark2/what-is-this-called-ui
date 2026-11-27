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
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">글꼴에 tnum 기능이 없으면 효과 없음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">text-align: right   끝자리를 오른쪽에 맞춤</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">toLocaleString('ko-KR')   천 단위 쉼표 넣기</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">등폭 글꼴   기능이 없는 글꼴의 대안</div>
                </div>
              </div>'''

D = dict(
  slug="numerals", ko="숫자 꼴", en="Numerals · tabular figures",
  desc="숫자 너비가 글꼴마다 다른 이유와 tabular-nums를 켜도 효과가 없는 경우를 직접 재서 보여 주는 항목입니다.",
  lede="숫자 꼴은 숫자 하나하나가 차지하는 <b>너비</b>를 다룹니다. 세로로 쌓이는 표나 1초마다 바뀌는 값에서 숫자마다 너비가 다르면 자릿수가 흔들려 읽기 어렵습니다.",
  axes_lede="글자를 다루는 항목들은 값 하나를 바꾸면 글 전체가 함께 바뀐다는 점이 같습니다. 서로 구별하려면 아래 네 가지를 물어보면 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>가운데 표는 <b>글꼴마다 숫자 너비를 직접 재서</b> '원래 고름'인지, '켜니 고르게 됨'인지,
          <b>'켜도 안 바뀌니 기능 없음'</b>인지 알려 줍니다.<br>
          <code>tabular-nums</code>는 <b>글꼴에 그 기능이 있을 때만</b> 효과가 있습니다. 세리프 계열 글꼴에는 대개 그 기능이 없어서
          켜도 아무 변화가 없습니다. 위의 큰 숫자에서 <b>흔들린 폭</b>이 실시간으로 쌓이는 것도 확인해 보세요.</p>
        </div>''',
  names=rows([
    ("한국어", "숫자 꼴, 등폭 숫자, 고정폭 숫자"),
    ("영어", "tabular figures, tabular-nums, lining figures, oldstyle figures"),
    ("같이 쓰는 말",
     "모든 숫자의 너비가 같은 것을 <b>등폭 숫자</b>(tabular figures), 숫자마다 너비가 다른 것을 "
     "<b>비례 숫자</b>(proportional figures)라고 합니다. 높이가 숫자마다 다른 옛 스타일 숫자는 "
     "<b>올드스타일</b>(oldstyle · text figures), 높이가 고른 숫자는 <b>라이닝</b>(lining)이라고 부릅니다. "
     "글꼴 안에서 이 기능을 가리키는 이름은 <code>tnum</code>·<code>pnum</code>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>등폭 글꼴</b> — 코드에 쓰는 등폭 글꼴은 <b>모든 글자</b>의 너비가 같은 글꼴이고, 등폭 숫자는 <b>숫자만</b> 너비를 같게 맞추는 기능이라 서로 다릅니다.<br>"
     "<b><code>text-align: right</code></b> — 오른쪽 맞춤은 숫자를 <b>끝자리에서</b> 맞출 뿐이고, 숫자의 너비 자체는 바꾸지 않습니다.<br>"
     "<b>천 단위 쉼표</b> — 자릿수를 읽기 쉽게 해 주지만, 숫자 너비가 달라 생기는 <b>흔들림은 막지 못합니다</b>."),
  ]),
  axes=ax("숫자 꼴"),
  oneline="<code>tabular-nums</code>는 <b>글꼴이 지원할 때만</b> 효과가 있습니다. 그래서 숫자가 중요한 자리라면 켜 두기만 하지 말고, 숫자 너비를 <b>직접 재 보고</b> 정해야 합니다.",
  s4_title="숫자 자리가 맞는 경우와 어긋나는 경우", s4_hint="글꼴과 설정에 따라 달라지는 결과",
  states=states([
    (nums("font-variant-numeric:tabular-nums", label="고른 숫자"), "숫자 너비가 고를 때", "자릿수가 <b>세로로 맞습니다.</b> 표에서는 이 상태가 기본입니다"),
    (nums("font-family:Georgia,serif", label="비례 숫자"), "숫자 너비가 서로 다를 때", "'1'의 너비가 좁아서 <b>쉼표 자리가 줄마다 어긋납니다</b>"),
    (nums("font-family:Georgia,serif;font-variant-numeric:tabular-nums", label="켜도 안 바뀜"),
     "글꼴에 기능이 없을 때", "<b>켜도 그대로입니다.</b> 글꼴에 그 기능이 없기 때문입니다"),
    (nums("font-family:var(--mono)", label="등폭 글꼴"), "등폭 글꼴로 바꿨을 때", "<b>확실한 대안</b>입니다. 숫자 부분만 등폭 글꼴로 바꿔 쓰기도 합니다"),
    (nums("font-variant-numeric:tabular-nums", ("1,284,000", "982,500", "11,100"), label="자릿수가 다르면"),
     "자릿수가 서로 다를 때", "등폭 숫자라도 <b>자릿수가 다르면</b> 길이가 달라지기 때문에 오른쪽 맞춤이 함께 필요합니다"),
    (nums("font-variant-numeric:tabular-nums;text-align:right", ("1,284,000", "982,500", "11,100"), label="+ 오른쪽 맞춤"),
     "오른쪽 맞춤을 더했을 때", "<b>등폭 숫자와 오른쪽 맞춤</b>을 함께 써야 자릿수가 한눈에 읽힙니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("바뀌는 숫자", "value", "금액, 시간, 카운트다운처럼 <b>값이 바뀌어도 자리가 흔들리지 않아야</b> 하는 숫자입니다"),
    ("등폭 켜기", "tabular-nums", "모든 숫자가 <b>같은 너비</b>를 쓰게 합니다"),
    ("글꼴 지원", "tnum feature", "<b>글꼴에 이 기능이 없으면 켜도 아무 변화가 없습니다.</b> 한글 글꼴에서 특히 흔한 일입니다"),
    ("오른쪽 맞춤", "text-align: right", "숫자를 <b>끝자리에서</b> 맞춥니다. 등폭 숫자와 함께 써야 표의 숫자가 잘 읽힙니다"),
    ("천 단위 쉼표", "toLocaleString", "큰 숫자를 읽기 쉽게 해 줍니다. 통화와 소수점 규칙도 같은 함수로 맞춥니다"),
    ("등폭 글꼴", "monospace", "글꼴에 등폭 숫자 기능이 없을 때 쓸 수 있는 <b>확실한 대안</b>입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          가장 흔한 실수는 <code>tabular-nums</code>를 켜 두기만 하고 <b>적용된 줄 아는 것</b>입니다.
          이 속성은 <b>글꼴 안에 들어 있는 기능을 켜기만</b> 하기 때문에, 그 기능이 없는 글꼴에서는
          아무 변화도 없고 경고도 나오지 않습니다. 글꼴을 바꿀 때도 아무 경고 없이 숫자 정렬이 어긋날 수 있으므로,
          <b>개발자 도구에서 숫자 너비를 직접 재 보는 것</b>이 유일한 확인 방법입니다.</p>''',
  do=ul([
    "표의 금액 열이나 목록의 값처럼 <b>세로로 쌓이는 숫자</b>를 보여 줄 때",
    "타이머, 카운트다운, 실시간 집계처럼 <b>자주 바뀌는 숫자</b>를 보여 줄 때",
    "자릿수가 같은 값들을 비교해야 할 때",
  ]),
  dont=ul([
    "읽는 글의 <b>문장 속 숫자</b>에 쓸 때. 문장 안에서는 비례 숫자가 더 자연스럽습니다",
    "켜 두기만 하고 확인하지 않을 때. <b>글꼴이 지원하는지 직접 재 봐야</b> 합니다",
    "오른쪽 맞춤 없이 등폭 숫자만 쓸 때. 자릿수가 다르면 여전히 어긋납니다",
    "숫자만 다른 글꼴로 바꿀 때. <b>글자와 숫자의 높이</b>가 맞지 않을 수 있습니다",
  ]),
  instead_title="숫자 꼴과 이어지는 주제를 다루는 항목",
  instead='표 전체를 어떻게 짜는지는 데이터 테이블(10부)에서 다루고, 큰 숫자 하나를 돋보이게 보여 주는 방법은 <a href="../items/stat.html">스탯 타일</a>에 있습니다. 글꼴 파일을 받아 오는 문제는 <a href="webfont.html">웹폰트</a>를 보세요.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;overflow:hidden;font-variant-numeric:tabular-nums">
                <div style="display:flex;padding:5px 8px;background:var(--bg);font-size:10px;font-weight:700;color:var(--fg-muted)"><span style="flex:1">가맹점</span><span>매출</span></div>
                <div style="display:flex;padding:5px 8px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">모란상회</span><span>1,284,000</span></div>
                <div style="display:flex;padding:5px 8px;font-size:11px;border-top:1px solid var(--line)"><span style="flex:1">새벽상사</span><span>11,100</span></div>
              </div>''',
     "표의 금액 열 자릿수 맞추기", "<b>등폭 숫자와 오른쪽 맞춤</b>을 함께 씁니다. 둘 다 있어야 자릿수가 한눈에 읽힙니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:3px;text-align:center">
                <span style="font-size:11px;color:var(--fg-muted)">남은 시간</span>
                <span style="font-size:22px;font-weight:800;font-variant-numeric:tabular-nums">02:41:08</span>
              </div>''',
     "카운트다운 숫자가 흔들리지 않게 하기", "1초마다 값이 바뀌는데, <b>등폭 숫자를 켜지 않으면 숫자가 좌우로 흔들립니다</b>"),
    ('''              <div style="width:100%;max-width:190px;font-size:12px;line-height:1.8">
                이번 주에는 <b>42</b>건이 들어왔고 그중 <b>7</b>건이 아직 검토 중입니다.
              </div>''',
     "문장 속 숫자는 그대로 두기", "문장 안에서는 <b>기본값(비례 숫자)</b>이 더 자연스럽습니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="기능을 켠 뒤 직접 재 보기",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="한 줄로 기능을 켜고, <b>정말 적용됐는지 재 보는</b> 코드를 한 줄 더 둡니다.",
  code='''<span class="c">/* 표·타이머처럼 자릿수가 맞아야 하는 곳 */</span>
<span class="t">.amount</span>, <span class="t">.timer</span>, <span class="t">td</span> {
  <span class="a">font-variant-numeric</span>: tabular-nums;
  <span class="a">text-align</span>: right;      <span class="c">/* 둘 다 있어야 자릿수가 읽힌다 */</span>
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
    ("표와 타이머에 켜기", "세로로 쌓이거나 자주 바뀌는 숫자에 켭니다"),
    ("오른쪽 맞춤과 함께 쓰기", "등폭 숫자만으로는 <b>자릿수가 다른 값</b>끼리 끝이 맞지 않습니다"),
    ("실제로 적용됐는지 재 보기", "글꼴에 기능이 없으면 <b>경고 없이 아무 변화도 일어나지 않습니다</b>"),
    ("기능이 없으면 등폭 글꼴 쓰기", "숫자 부분만 <code>font-family</code>를 바꾸는 방법도 있습니다"),
    ("문장 속 숫자는 그대로 두기", "읽는 글에서는 비례 숫자가 더 자연스럽습니다"),
    ("쉼표는 <code>Intl</code>로 넣기", "통화 기호와 소수점, 자릿수 규칙이 나라마다 다르기 때문입니다"),
  ]),
  backend=rows([
    ("숫자 서식을 입히는 곳", "서버는 <code>1284000</code>처럼 숫자만 내려 주고, <b>서식은 화면에서</b> 입히는 편이 낫습니다. 서버가 '₩1,284,000' 같은 문자열을 보내면 화면에서 정렬도 계산도 할 수 없습니다."),
    ("금액의 소수점과 반올림", "금액은 <b>정수로</b> 다루고, 나누는 계산은 화면에 보여 줄 때만 합니다. 부동소수점으로 돈을 계산하면 반올림 오차 때문에 1원이 어긋날 수 있습니다."),
    ("통화 기호와 로케일 맞추기", "<code>Intl.NumberFormat</code>을 쓰면 통화 기호 위치와 쉼표, 소수 자릿수를 한 번에 맞출 수 있습니다."),
    ("큰 수를 줄여 보여 주기", "'₩12.8억'처럼 줄여 보여 줄지는 화면에서 정합니다. 다만 <b>어디서 반올림할지</b>를 한 곳에 모아 두지 않으면 화면마다 숫자가 달라집니다."),
  ]),
  plat_lede="두 OS에서는 숫자 꼴을 <b>글꼴 설정</b>으로 고릅니다.",
  plats=plats([
    ("웹", "font-variant-numeric",
     nums("font-variant-numeric:tabular-nums", ("1,284,000", "11,100"), "120px"),
     "<code>tabular-nums</code>로 켭니다. 다만 <b>글꼴이 지원할 때만</b> 효과가 있다는 점을 놓치기 쉽습니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.monospacedDigit( )<br>.font(.body<br>&nbsp;.monospacedDigit( ))</div>''',
     "<b><code>.monospacedDigit()</code></b> 한 줄로 켭니다. 시스템 글꼴이 이 기능을 지원하기 때문에 <b>늘 적용됩니다</b>."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">FontFeature("tnum")<br>fontFeatureSettings</div>''',
     "<code>fontFeatureSettings = &quot;tnum&quot;</code>으로 켭니다. 웹과 마찬가지로 글꼴에 그 기능이 있어야 합니다."),
  ]),
  plat_note="iOS는 <b>시스템 글꼴이 늘 지원</b>하므로 한 줄로 끝나지만, 웹에서는 <b>쓰는 한글 글꼴에 그 기능이 있는지</b>부터 확인해야 합니다. \"숫자가 흔들려요\"라는 제보를 받은 앱 개발자가 무슨 문제인지 잘 모르는 것도 이 때문입니다.",
  siblings=siblings("numerals"),
  related='''        <li><a href="../items/stat.html"><b>스탯 타일</b><em>5부</em></a></li>
        <li><a href="../items/webfont.html"><b>웹폰트</b><em>3부</em></a></li>
        <li><a href="../items/typescale.html"><b>타입 스케일</b><em>2부</em></a></li>
        <li><a href="table.html"><b>데이터 테이블</b><em>10부</em></a></li>''',
)
