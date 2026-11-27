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
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">-webkit-line-clamp: 2   — 여러 줄</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">scrollWidth &gt; clientWidth   — 잘렸는지 아는 법</div>
                </div>
              </div>'''

D = dict(
  slug="truncate", ko="말줄임", en="Truncation · line clamp",
  desc="한 줄 말줄임과 여러 줄 line-clamp, 잘렸는지 알아내는 법과 전체를 보여줄 방법을 다루는 항목.",
  lede="넘친 글의 끝을 <code>…</code>으로 줄이는 것. <b>정보를 지우는 일</b>이라 '어디서 자를지'보다 '전체를 어떻게 보게 할지'가 먼저입니다.",
  axes_lede="글자를 다루는 것들은 '값 하나가 글 전체에 걸린다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>세 가지를 나란히 뒀습니다 — <b>한 줄</b>, <b>여러 줄</b>, <b>흐려서 끊기</b>.
          줄 수 막대를 움직이면 상자 높이가 따라 바뀝니다.<br>
          아래에 <code>scrollWidth</code>·<code>scrollHeight</code> 값을 재서 <b>지금 잘렸는지</b>를 보여 줍니다.
          이걸 쓰면 <b>잘렸을 때만</b> 툴팁을 붙일 수 있습니다 — 안 잘렸는데 툴팁이 뜨면 거슬립니다.</p>
        </div>''',
  names=rows([
    ("한국어", "말줄임, 줄임표, 생략, 더보기"),
    ("영어", "truncation, ellipsis, line clamp, text overflow"),
    ("같이 쓰는 말",
     "한 줄로 줄이는 것을 <b>엘립시스</b>(ellipsis), 여러 줄로 묶는 것을 <b>라인 클램프</b>(line clamp)라 합니다. "
     "끝을 흐리게 지우는 방식은 <b>페이드 아웃</b>, 뒷부분을 눌러서 펼치는 것은 <b>더 보기</b>(read more)입니다. "
     "<code>…</code> 글자 자체는 <b>줄임표</b>(horizontal ellipsis)입니다."),
    ("자주 잘못 부름",
     "<b><code>overflow: hidden</code></b> — 그것만으로는 <b>그냥 잘립니다.</b> <code>…</code>이 나오려면 세 속성이 다 있어야 합니다.<br>"
     "<b>글자 수로 자르기</b> — <code>slice(0, 20)</code>은 <b>폭과 상관없이</b> 자릅니다. 넓은 화면에서도 똑같이 잘립니다.<br>"
     "<b><code>text-overflow</code></b> — 혼자서는 아무 일도 안 합니다."),
  ]),
  axes=ax("말줄임"),
  oneline="말줄임은 <b>세 속성이 한 세트</b>이고, 그보다 중요한 것은 <b>전체를 볼 길</b>을 남기는 것입니다.",
  s4_title="갈래", s4_hint="자르는 방법마다 주는 느낌이 다르다",
  states=states([
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", label="한 줄"),
     "한 줄", "<code>…</code>이 끝에 붙는다. <b>목록 제목의 기본</b>"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden", label="두 줄"),
     "여러 줄", "<code>-webkit-line-clamp</code>. 줄 수를 정해 묶는다"),
    (tb("max-height:38px;overflow:hidden;position:relative", label="흐려서 끊기"),
     "페이드", "<code>…</code> 없이 <b>'더 있다'는 느낌</b>만 준다"),
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", "환불 확인 요청", label="안 잘림"),
     "안 잘림", "짧으면 아무 일도 안 일어난다. <b>툴팁도 붙이면 안 된다</b>"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden",
        LONG, "160px", "+ 더 보기") + '''
              <div style="text-align:center;margin-top:4px"><span style="font-size:10px;color:var(--accent);text-decoration:underline">더 보기</span></div>''',
     "더 보기", "<b>펼칠 수 있게</b> 한다. 가장 친절한 방법"),
    (tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", "TX99120KR2026SETTLEMENTCONFIRMATION", label="가운데를 지우고 싶을 때"),
     "앞뒤가 중요할 때", "파일명·코드는 끝이 중요하다. <b>가운데를 지우는</b> 방법을 따로 써야 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("잘린 글", "truncated text", "줄 수가 정해진 상자 안의 글"),
    ("넘침 숨기기", "overflow: hidden", "<b>혼자 쓰면 그냥 잘린다</b> — … 이 안 붙는다"),
    ("줄임표", "text-overflow: ellipsis", "끝에 <code>…</code>을 붙인다. 혼자서는 아무 일도 안 한다"),
    ("줄바꿈 막기", "white-space: nowrap", "<b>한 줄짜리에만.</b> 이게 있어야 가로로 넘쳐 … 이 생긴다"),
    ("줄 수 묶기", "-webkit-line-clamp", "여러 줄용. 이름에 <code>-webkit-</code>이 붙었지만 <b>모든 브라우저가 지원</b>한다"),
    ("잘렸는지 알기", "scrollWidth > clientWidth", "<b>툴팁을 붙일지 말지</b>를 이걸로 정한다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          플렉스·그리드 자식에서는 세 속성을 다 써도 <b>말줄임이 안 걸립니다.</b>
          자식의 자동 최소 너비가 '내용만큼'이라 상자가 글에 밀려 늘어나기 때문입니다 —
          <b><code>min-width: 0</code></b> 한 줄이 더 필요합니다. 이 도감에서 가장 자주 나오는 사고이고,
          <a href="../items/flex.html">플렉스</a>·<a href="../items/overflow.html">넘침</a>에서도 같은 이야기가 나옵니다.</p>''',
  do=ul([
    "<b>줄 높이가 일정해야</b> 하는 목록 — 제목, 보조 글",
    "카드 설명처럼 <b>두세 줄로 묶어야</b> 할 때",
    "전체를 볼 길(툴팁·상세·더 보기)이 <b>있을</b> 때",
  ]),
  dont=ul([
    "<b>전체를 볼 길 없이</b> 자르는 것 — 정보가 그냥 사라집니다",
    "글자 수로 자르는 것 — 화면 폭과 상관없이 똑같이 잘립니다",
    "안 잘렸는데 툴팁을 붙이는 것 — 거슬립니다",
    "<b>중요한 정보의 끝</b>을 자르는 것 — 파일명·코드는 끝이 중요합니다",
  ]),
  instead='넘침 자체의 처리는 <a href="../items/overflow.html">넘침</a>, 줄이 안 줄어들면 <a href="../items/flex.html">플렉스</a>의 <code>min-width: 0</code>, 전체를 띄우려면 <a href="../items/tooltip.html">툴팁</a>.',
  cases=cases([
    ('''              <div style="width:100%;max-width:190px;border:1px solid var(--line);border-radius:6px;background:var(--surface);display:flex;align-items:center;gap:7px;padding:8px">
                <span style="width:22px;height:22px;border-radius:99px;background:var(--accent-soft);flex:none"></span>
                <span style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:11.5px;font-weight:600">''' + LONG + '''</span>
                <span style="font-size:10px;color:var(--fg-muted);flex:none">₩48,000</span>
              </div>''',
     "목록 제목", "한 줄 + <code>min-width: 0</code>. <b>뒤쪽 값이 안 밀린다</b>"),
    (tb("display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden", LONG, "190px"),
     "카드 설명", "두 줄로 묶는다. <b>카드 높이가 고르게</b> 맞는다"),
    ('''              <div style="width:100%;max-width:190px;display:grid;gap:4px">
                <div style="border:1px solid var(--line);border-radius:5px;background:var(--surface);padding:8px;font-size:11px;line-height:1.7;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">''' + LONG + '''</div>
                <span style="font-size:10.5px;color:var(--accent);text-decoration:underline;justify-self:start">더 보기</span>
              </div>''',
     "더 보기", "잘렸을 때<b>만</b> 버튼을 보여 준다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="세 속성이 한 세트",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="한 줄은 <b>세 속성</b>(+ 플렉스면 한 줄 더), 여러 줄은 <b>네 속성</b>입니다.",
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
    ("세 속성이 한 세트", "하나라도 빠지면 <code>…</code>이 안 나온다"),
    ("<code>min-width: 0</code>", "플렉스·그리드 자식이면 <b>이게 없으면 영영 안 걸린다</b>"),
    ("잘렸을 때만 툴팁", "<code>scrollWidth &gt; clientWidth</code>로 확인하고 붙인다"),
    ("전체를 볼 길을 준다", "툴팁·상세·더 보기 중 하나. <b>없으면 정보를 지운 것</b>이다"),
    ("글자 수로 자르지 않는다", "폭이 정하게 둔다. 서버에서 자르면 <b>넓은 화면에서도 짧다</b>"),
    ("끝이 중요하면 가운데를", "파일명·코드는 앞뒤를 남기고 <b>가운데를 지운다</b>"),
  ]),
  backend=rows([
    ("자르기는 화면에서", "서버가 미리 자르면 <b>툴팁에도 전체가 없습니다.</b> 전체를 보내고 화면이 줄이는 쪽이 낫습니다 — 글이 아주 길 때만 서버에서 자릅니다."),
    ("가장 긴 값으로 테스트", "개발 중의 짧은 더미 데이터로는 <b>평생 안 드러납니다.</b> 운영 데이터의 최댓값으로 한 번 그려 봅니다."),
    ("검색 결과 하이라이트", "자른 뒤에 하이라이트를 넣으면 <b>찾은 낱말이 잘려 안 보일</b> 수 있습니다. 찾은 자리 앞뒤를 남기고 자르는 처리가 따로 필요합니다."),
    ("접근성", "잘린 글도 스크린 리더에는 <b>전체가 읽힙니다</b>(DOM 에는 다 있으므로). 그래서 <code>title</code>을 중복으로 붙이면 두 번 읽힙니다."),
  ]),
  plat_lede="앱 쪽은 <b>한 줄</b>로 끝나서, 웹의 세 속성 조합이 낯섭니다.",
  plats=plats([
    ("웹", "text-overflow · line-clamp",
     tb("overflow:hidden;text-overflow:ellipsis;white-space:nowrap", LONG, "120px"),
     "<b>세 속성</b>이 한 세트입니다. 여러 줄은 <code>-webkit-line-clamp</code>."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineLimit(2)<br>.truncationMode(.middle)</div>''',
     "<code>.lineLimit(2)</code> 한 줄. <b>가운데를 지우는 모드</b>까지 기본으로 있습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">maxLines = 2<br>overflow =<br>&nbsp;TextOverflow.Ellipsis</div>''',
     "<code>maxLines</code> + <code>overflow</code> 두 값. <code>MiddleEllipsis</code> 도 있습니다."),
  ]),
  plat_note="두 OS 에는 <b>가운데를 지우는 모드가 기본으로</b> 있어서 파일명·코드를 자를 때 바로 씁니다. 웹에는 없어서 직접 만들어야 합니다 — \"파일명 가운데를 … 으로\"라는 요청이 웹에서만 큰일이 되는 이유입니다.",
  siblings=siblings("truncate"),
  related='''        <li><a href="../items/overflow.html"><b>넘침</b><em>1부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/tooltip.html"><b>툴팁</b><em>6부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>''',
)
