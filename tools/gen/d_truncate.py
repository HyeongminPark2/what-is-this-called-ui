# -*- coding: utf-8 -*-
from ax3 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

LONG = "환불 확인 요청 — 카드 승인 취소가 늦어져 고객이 두 번 문의했고 담당자가 바뀌면서 한 번 더 늦어진 건입니다."

def tb(style="", txt=LONG, w="160px", label=""):
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid var(--line);border-radius:5px;'
            'background:var(--surface);padding:8px;font-size:11px;line-height:1.7;' + style + '">' + txt + '</div>'
            + ('<div style="font-family:var(--mono);font-size:10px;color:var(--fg-muted);text-align:center;margin-top:6px">' + label + '</div>' if label else ''))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:240px">
                    <div style="border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:9px;font-size:12px;line-height:1.7;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">환불 확인 요청 — 카드 승인 취소가 늦어져 고객이 두 번 문의했고</div>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">overflow: hidden</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">text-overflow: ellipsis</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">white-space: nowrap</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">-webkit-line-clamp: 2   여러 줄 말줄임</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">scrollWidth &gt; clientWidth   잘렸는지 알아내는 비교</div>
                </div>
              </div>'''

D = dict(
  slug="truncate", ko="말줄임", en="Truncation · line clamp",
  desc="한 줄 말줄임과 여러 줄 line-clamp, 글이 잘렸는지 알아내는 법과 전체를 보여 줄 방법을 다루는 항목입니다.",
  lede="말줄임은 칸을 넘친 글의 끝을 <code>…</code>으로 줄여 보여 주는 방식입니다. 잘린 부분은 화면에서 <b>보이지 않게 되므로</b>, '어디서 자를지'보다 '전체를 어떻게 보게 할지'를 먼저 정해야 합니다.",
  axes_lede="글자를 다루는 항목들은 값 하나를 바꾸면 글 전체가 함께 바뀐다는 점이 같습니다. 서로 구별하려면 아래 네 가지를 물어보면 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>한 줄로 줄이기</b>, <b>여러 줄까지 보여 주기</b>, <b>끝을 흐리게 지우기</b>, 세 가지 방식을 나란히 두었습니다.
          줄 수 막대를 움직이면 상자 높이가 따라 바뀝니다.<br>
          아래에는 <code>scrollWidth</code>·<code>scrollHeight</code> 값을 재서 <b>지금 글이 잘렸는지</b>를 보여 줍니다.
          이 값을 쓰면 <b>잘렸을 때만</b> 툴팁을 붙일 수 있습니다. 잘리지 않은 글에 툴팁이 뜨면 같은 내용을 한 번 더 보여 주는 셈이라 거슬립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "말줄임, 줄임표, 생략, 더보기"),
    ("영어", "truncation, ellipsis, line clamp, text overflow"),
    ("같이 쓰는 말",
     "한 줄로 줄이는 것을 <b>엘립시스</b>(ellipsis), 정한 줄 수까지만 보여 주는 것을 <b>라인 클램프</b>(line clamp)라고 합니다. "
     "끝을 흐리게 지우는 방식은 <b>페이드 아웃</b>, 뒷부분을 눌러서 펼치게 하는 방식은 <b>더 보기</b>(read more)라고 부릅니다. "
     "<code>…</code> 글자 자체의 이름은 <b>줄임표</b>(horizontal ellipsis)입니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>overflow: hidden</code></b> — 이 속성만 쓰면 글이 <code>…</code> 없이 <b>그냥 잘립니다.</b> <code>…</code>이 나오려면 세 속성이 모두 있어야 합니다.<br>"
     "<b>글자 수로 자르기</b> — <code>slice(0, 20)</code>은 <b>화면 폭과 상관없이</b> 자르기 때문에, 넓은 화면에서도 똑같이 잘립니다.<br>"
     "<b><code>text-overflow</code></b> — 이 속성 하나만으로는 아무 변화도 일어나지 않습니다."),
  ]),
  axes=ax("말줄임"),
  oneline="한 줄 말줄임에는 <b>세 속성이 한 세트</b>로 필요합니다. 그보다 더 중요한 것은 잘린 글의 <b>전체를 볼 방법</b>을 남겨 두는 것입니다.",
  s4_title="글을 줄이는 여러 방법", s4_hint="방법마다 달라지는 모습",
  states=states([
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", label="한 줄"),
     "한 줄로 줄일 때", "끝에 <code>…</code>이 붙습니다. <b>목록 제목에 기본으로</b> 쓰는 방식입니다"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden", label="두 줄"),
     "여러 줄까지 보여 줄 때", "<code>-webkit-line-clamp</code>로 보여 줄 줄 수를 정합니다"),
    (tb("max-height:38px;overflow:hidden;position:relative", label="흐려서 끊기"),
     "끝을 흐리게 지울 때", "<code>…</code> 없이 끝을 흐리게 해서 <b>뒤에 글이 더 있다는 것</b>만 알려 줍니다"),
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", "환불 확인 요청", label="안 잘림"),
     "글이 짧아 잘리지 않을 때", "글이 짧으면 아무 변화가 없습니다. 이때는 <b>툴팁도 붙이지 않습니다</b>"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden",
        LONG, "160px", "+ 더 보기") + '''
              <div style="text-align:center;margin-top:4px"><span style="font-size:10px;color:var(--accent);text-decoration:underline">더 보기</span></div>''',
     "더 보기로 펼치게 할 때", "잘린 글을 <b>펼쳐 볼 수 있게</b> 합니다. 사용자가 전체를 가장 쉽게 볼 수 있는 방법입니다"),
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", "TX99120KR2026SETTLEMENTCONFIRMATION", label="가운데를 지우고 싶을 때"),
     "앞뒤가 중요할 때", "파일명이나 코드는 끝부분이 중요하므로 <b>가운데를 지우는</b> 방법을 따로 써야 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잘린 글", "truncated text", "줄 수가 정해진 상자 안에 들어가는 글입니다"),
    ("넘침 숨기기", "overflow: hidden", "<b>혼자 쓰면 글이 그냥 잘리고</b> … 은 붙지 않습니다"),
    ("줄임표", "text-overflow: ellipsis", "잘린 끝에 <code>…</code>을 붙입니다. 이 속성 하나만으로는 아무 변화도 없습니다"),
    ("줄바꿈 막기", "white-space: nowrap", "<b>한 줄 말줄임에만</b> 씁니다. 줄바꿈을 막아야 글이 가로로 넘치면서 … 이 생깁니다"),
    ("줄 수 묶기", "-webkit-line-clamp", "여러 줄 말줄임에 씁니다. 이름에 <code>-webkit-</code>이 붙었지만 <b>모든 브라우저가 지원</b>합니다"),
    ("잘렸는지 알기", "scrollWidth > clientWidth", "이 비교 결과로 <b>툴팁을 붙일지 말지</b>를 정합니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          플렉스·그리드 자식에서는 세 속성을 모두 써도 <b>말줄임이 적용되지 않습니다.</b>
          자식의 자동 최소 너비가 '내용 길이만큼'으로 잡혀서, 상자가 글 길이에 맞춰 늘어나기 때문입니다.
          그래서 <b><code>min-width: 0</code></b> 한 줄을 더 적어야 합니다. 이 도감에서 가장 자주 다루는 실수이고,
          <a href="../items/flex.html">플렉스</a>·<a href="../items/overflow.html">넘침</a> 항목에서도 같은 내용을 설명합니다.</p>''',
  do=ul([
    "목록의 제목이나 보조 글처럼 <b>줄 높이가 일정해야</b> 할 때",
    "카드 설명처럼 <b>두세 줄까지만 보여 줘야</b> 할 때",
    "툴팁이나 상세 화면, 더 보기처럼 전체를 볼 방법이 <b>있을</b> 때",
  ]),
  dont=ul([
    "<b>전체를 볼 방법 없이</b> 자를 때. 잘린 정보를 사용자가 볼 수 없게 됩니다",
    "글자 수로 자를 때. 화면 폭과 상관없이 똑같이 잘립니다",
    "잘리지 않은 글에 툴팁을 붙일 때. 이미 보이는 내용이 한 번 더 떠서 거슬립니다",
    "<b>중요한 정보의 끝</b>을 자를 때. 파일명이나 코드는 끝부분이 중요합니다",
  ]),
  instead_title="말줄임과 이어지는 주제를 다루는 항목",
  instead='칸을 넘친 내용 전체를 어떻게 처리할지는 <a href="../items/overflow.html">넘침</a>에서 다룹니다. 플렉스 안에서 글이 줄어들지 않으면 <a href="../items/flex.html">플렉스</a> 항목의 <code>min-width: 0</code>을 보고, 잘린 글 전체를 띄워 보여 주려면 <a href="../items/tooltip.html">툴팁</a>을 씁니다.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft);flex:none"></span>
                <span style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:11.5px;font-weight:600">''' + LONG + '''</span>
                <span style="font-size:10px;color:var(--fg-muted);flex:none">₩48,000</span>
              </div>''',
     "목록 제목을 한 줄로 줄이기", "한 줄 말줄임에 <code>min-width: 0</code>을 더해서 <b>뒤쪽 값이 밀려나지 않습니다</b>"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden", LONG, "190px"),
     "카드 설명을 두 줄로 맞추기", "두 줄까지만 보여 주므로 <b>카드 높이가 고르게</b> 맞습니다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <div style="border:1px solid var(--line);border-radius:5px;background:var(--surface);padding:8px;font-size:11px;line-height:1.7;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">''' + LONG + '''</div>
                <span style="font-size:10.5px;color:var(--accent);text-decoration:underline;justify-self:start">더 보기</span>
              </div>''',
     "잘린 글에 더 보기 붙이기", "글이 잘렸을 때<b>만</b> 더 보기 버튼을 보여 줍니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="한 세트로 적는 세 속성",
  keys_heads="<th>지킬 규칙</th><th>지키는 방법</th>",
  code_lede="한 줄 말줄임에는 <b>세 속성</b>이 필요하고 플렉스 자식이면 한 줄을 더 적습니다. 여러 줄 말줄임에는 <b>네 속성</b>이 필요합니다.",
  code='''<span class="c">/* 한 줄 */</span>
<span class="t">.title</span> {
  <span class="a">overflow</span>: hidden;
  <span class="a">text-overflow</span>: ellipsis;
  <span class="a">white-space</span>: nowrap;
  <span class="a">min-width</span>: <span class="a">0</span>;        <span class="c">/* 플렉스·그리드 자식이면 */</span>
}

<span class="c">/* 여러 줄 */</span>
<span class="t">.desc</span> {
  <span class="a">display</span>: -webkit-box;
  -webkit-line-clamp: <span class="a">2</span>;
  -webkit-box-orient: vertical;
  <span class="a">overflow</span>: hidden;
}

<span class="c">// 잘렸을 때만 툴팁을 붙인다</span>
<span class="t">if</span> (el.scrollWidth &gt; el.clientWidth) el.title = el.textContent;''',
  keys=kbd([
    ("세 속성을 한 세트로 적기", "하나라도 빠지면 <code>…</code>이 나오지 않습니다"),
    ("<code>min-width: 0</code> 더하기", "플렉스·그리드 자식에서는 <b>이 줄이 없으면 말줄임이 적용되지 않습니다</b>"),
    ("잘렸을 때만 툴팁 붙이기", "<code>scrollWidth &gt; clientWidth</code>로 잘렸는지 확인한 뒤에 붙입니다"),
    ("전체를 볼 방법 남기기", "툴팁, 상세 화면, 더 보기 가운데 하나는 둡니다. <b>그런 방법이 없으면 잘린 정보는 아무도 볼 수 없습니다</b>"),
    ("글자 수로 자르지 않기", "어디서 자를지는 화면 폭에 맡깁니다. 서버에서 글자 수로 자르면 <b>넓은 화면에서도 글이 짧게 잘립니다</b>"),
    ("끝이 중요하면 가운데 지우기", "파일명이나 코드는 앞뒤를 남기고 <b>가운데를 지웁니다</b>"),
  ]),
  backend=rows([
    ("글은 화면에서 자르기", "서버가 글을 미리 자르면 <b>툴팁에도 전체를 보여 줄 수 없습니다.</b> 그래서 전체를 보내고 화면에서 줄이는 편이 낫고, 서버에서는 글이 아주 길 때만 자릅니다."),
    ("가장 긴 값으로 화면 확인하기", "개발 중에 쓰는 짧은 더미 데이터로는 말줄임 문제가 <b>드러나지 않습니다.</b> 그래서 운영 데이터에서 가장 긴 값으로 화면을 한 번 그려 봅니다."),
    ("검색 결과 하이라이트가 잘리는 문제", "글을 자른 뒤에 하이라이트를 넣으면 <b>찾은 낱말이 잘린 부분에 들어가 보이지 않을</b> 수 있습니다. 그래서 찾은 자리 앞뒤를 남기고 자르는 처리가 따로 필요합니다."),
    ("스크린 리더가 읽는 내용", "화면에서 잘린 글도 DOM에는 전체가 들어 있어서 스크린 리더는 <b>전체를 읽습니다</b>. 그래서 같은 내용을 <code>title</code>로 한 번 더 붙이면 두 번 읽힙니다."),
  ]),
  plat_lede="앱에서는 말줄임을 <b>한 줄</b>로 설정하기 때문에, 앱 개발자에게는 웹의 세 속성 조합이 낯섭니다.",
  plats=plats([
    ("웹", "text-overflow · line-clamp",
     tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", LONG, "120px"),
     "한 줄 말줄임은 <b>세 속성</b>이 한 세트이고, 여러 줄은 <code>-webkit-line-clamp</code>로 처리합니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineLimit(2)<br>.truncationMode(.middle)</div>''',
     "<code>.lineLimit(2)</code> 한 줄로 끝나고, <b>가운데를 지우는 모드</b>도 기본으로 들어 있습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">maxLines = 2<br>overflow =<br>&nbsp;TextOverflow.Ellipsis</div>''',
     "<code>maxLines</code>와 <code>overflow</code> 두 값으로 정하며, 가운데를 지우는 <code>MiddleEllipsis</code>도 있습니다."),
  ]),
  plat_note="두 OS에는 <b>가운데를 지우는 모드가 기본으로</b> 들어 있어서 파일명이나 코드를 자를 때 바로 쓸 수 있습니다. 반면 웹에는 이런 기능이 없어 직접 만들어야 하므로, \"파일명 가운데를 … 으로 줄여 주세요\"라는 요청이 웹에서는 손이 많이 가는 작업이 됩니다.",
  siblings=siblings("truncate"),
  related='''        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>''',
)
