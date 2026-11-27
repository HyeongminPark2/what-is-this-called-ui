# -*- coding: utf-8 -*-
from ax1 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

TXT = "상자보다 글이 길어지면 무엇을 할지는 고르는 것이지 저절로 정해지지 않습니다."

def ob(ov="visible", txt=TXT, w="150px", h="58px", extra=""):
    return ('              <div style="width:100%;max-width:' + w + ';height:' + h + ';border:1px solid var(--line-strong);'
            'border-radius:5px;background:var(--surface);padding:7px;font-size:10.5px;line-height:1.65;'
            'overflow:' + ov + ';' + extra + '">' + txt + '</div>')

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:15px">
                  <div class="pin-out" data-pin="1" style="max-width:230px">
                    <div style="height:60px;border:1px solid var(--line-strong);border-radius:6px;background:var(--surface);padding:8px;font-size:11px;line-height:1.7;overflow:auto">상자보다 글이 길어지면 무엇을 할지는 고르는 것이지 저절로 정해지지 않습니다. 네 가지 중 하나를 골라야 합니다.</div>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">overflow: visible   — 기본값. 삐져나온다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">overflow: hidden   — 잘린다. 읽을 방법이 없다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">overflow: auto   — 넘칠 때만 스크롤</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">text-overflow: ellipsis   — 한 줄을 … 으로</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">min-width: 0   — 가로 스크롤의 진짜 원인</div>
                </div>
              </div>'''

D = dict(
  slug="overflow", ko="넘침", en="Overflow",
  desc="overflow 네 값의 차이와 말줄임, 그리고 가로 스크롤이 생기는 실제 원인을 실물과 해부도로 보여 주는 항목입니다.",
  lede="넘침은 상자보다 내용이 클 때 넘친 부분을 <b>어떻게 처리할지 고르는 일</b>입니다. 아무것도 고르지 않으면 기본값인 visible이 적용되어 내용이 상자 밖으로 삐져나옵니다.",
  axes_lede="뼈대를 다루는 항목들은 눈에 보이지 않으면서 요소의 자리를 정한다는 점이 같아서 생김새로는 구별하기 어렵습니다. 대신 아래 네 가지를 물어 보면 서로 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 글을 네 가지 <code>overflow</code> 값으로 나란히 두었습니다.
          <code>scroll</code>은 글이 <b>넘치지 않아도 스크롤바 자리를 잡는다</b>는 점을 눈여겨보세요.<br>
          아래는 <b>가로 스크롤의 원인을 찾는</b> 실험입니다. 체크를 켜고 끄면서
          <code>scrollWidth - clientWidth</code> 값이 어떻게 바뀌는지 보세요.
          가로 스크롤은 거의 항상 <b>줄어들지 못하는 칸 하나</b> 때문에 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "넘침, 오버플로, 말줄임"),
    ("영어", "overflow, clipping, scroll container, text-overflow"),
    ("같이 쓰는 말",
     "스크롤이 생긴 상자는 <b>스크롤 컨테이너</b>(scroll container), 넘친 부분을 잘라 내는 것은 <b>클리핑</b>(clipping), "
     "글 끝을 <code>…</code>으로 줄이는 것은 <b>말줄임</b>(ellipsis · truncation)이라고 부릅니다. "
     "가로만 따로 정할 때는 <code>overflow-x</code>, 세로만 정할 때는 <code>overflow-y</code>를 씁니다."),
    ("자주 잘못 부르는 이름",
     "<b><code>hidden</code>과 말줄임</b> — <code>hidden</code>은 넘친 부분을 <b>그냥 잘라 낼 뿐</b>이라서, "
     "<code>…</code>이 나오려면 <code>text-overflow: ellipsis</code>와 <code>white-space: nowrap</code>이 함께 있어야 합니다.<br>"
     "<b><code>auto</code>와 <code>scroll</code></b> — auto는 넘칠 때만 스크롤바 자리를 잡고, scroll은 <b>항상</b> 잡습니다.<br>"
     "<b>'가로 스크롤이 생겼다'</b> — overflow 설정 문제가 아니라 <b>안쪽에 줄어들지 않는 요소가 있다</b>는 뜻입니다."),
  ]),
  axes=ax("넘침"),
  oneline="넘침은 넘친 내용을 어떻게 할지 <b>고르는 일</b>입니다. 아무것도 고르지 않으면 내용이 삐져나오고, <code>hidden</code>을 고르면 잘린 내용은 읽지 못해도 된다고 정한 셈이 됩니다.",
  s4_title="갈래", s4_hint="네 값이 다 다르게 동작한다",
  states=states([
    (ob("visible"), "visible", "기본값입니다. 내용이 <b>상자 밖으로 삐져나오고</b>, 부모가 잘라 내면 안 보일 수도 있습니다"),
    (ob("hidden"), "hidden", "넘친 부분이 <b>잘려서</b> 읽을 방법이 없어집니다"),
    (ob("auto"), "auto", "넘칠 때<b>만</b> 스크롤바가 생기는, 가장 무난한 값입니다"),
    (ob("scroll", "짧은 글."), "scroll", "<b>넘치지 않아도</b> 스크롤바 자리를 잡습니다. 레이아웃이 흔들리면 안 될 때 씁니다"),
    (ob("hidden", "한 줄이 길어도 끝까지 가지 않고 말줄임", "150px", "34px", "text-overflow:ellipsis;white-space:nowrap"),
     "말줄임", "overflow, text-overflow, white-space <b>세 속성을 함께</b> 써야 말줄임이 됩니다"),
    ('''              <div style="width:100%;max-width:150px;height:46px;border:1px solid var(--line-strong);border-radius:5px;background:var(--surface);padding:7px;overflow-x:auto">
                <div style="display:flex;gap:5px">
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 하나</span>
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 둘</span>
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 셋</span>
                </div>
              </div>''',
     "일부러 가로로", "칩 줄이나 탭 줄은 <b>가로 스크롤로 두는 편이 맞을</b> 때가 있습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크롤 컨테이너", "scroll container", "<code>overflow</code>가 visible이 아닌 상자입니다. <b>이 상자 안쪽은 바깥과 따로 스크롤됩니다</b>"),
    ("visible", "overflow: visible", "기본값이며, 자르지도 스크롤하지도 않습니다. 다만 <b>부모가 대신 잘라 낼 수는 있습니다</b>"),
    ("hidden", "overflow: hidden", "넘친 부분을 자릅니다. 쓰기는 쉽지만 <b>잘린 내용을 읽을 방법이 사라집니다</b>"),
    ("auto", "overflow: auto", "넘칠 때만 스크롤됩니다. 내용 길이를 모를 때 기본으로 고르는 값입니다"),
    ("말줄임", "text-overflow: ellipsis", "<b>이 속성 하나만으로는 말줄임이 되지 않고</b>, overflow·white-space와 함께 세 개를 써야 합니다"),
    ("안 줄어드는 칸", "min-width: 0", "가로 스크롤을 만드는 실제 원인입니다. <b>overflow를 고쳐서는 해결되지 않습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>overflow</code>를 visible이 아닌 값으로 바꾸면 <b>다른 동작도 함께 바뀝니다.</b>
          그 안의 <code>position: sticky</code>는 이 상자를 기준으로 붙게 되는데, '스티키가 안 먹어요'라는 문제가 흔히 여기서 생깁니다.
          또 상자 밖으로 나간 그림자·배지·드롭다운도 잘립니다. 그래서 <b>"일단 hidden으로 막자"</b>고 넘어가면
          다른 자리에서 새 버그가 생기는 일이 잦습니다.</p>''',
  do=ul([
    "길이를 <b>알 수 없는</b> 내용을 담을 때. <code>auto</code>를 씁니다",
    "목록의 제목처럼 <b>한 줄로 맞춰야</b> 할 때. 말줄임 세 줄을 씁니다",
    "칩 줄이나 탭 줄처럼 <b>옆으로 밀어 보는 편이 맞을</b> 때. <code>overflow-x: auto</code>를 씁니다",
  ]),
  dont=ul([
    "<b>원인을 모른 채 <code>hidden</code>으로 가릴 때</b>. 가로 스크롤은 대개 안쪽의 줄어들지 않는 요소 때문에 생깁니다",
    "말줄임만 쓰고 <b>전체를 볼 방법을 주지 않을</b> 때. 툴팁이나 상세 화면에서 전체 글을 볼 수 있게 합니다",
    "<code>scroll</code>을 기본으로 쓸 때. 넘치지 않아도 스크롤바 자리가 남습니다",
    "<code>body</code>에 <code>overflow: hidden</code>을 줄 때. 페이지 스크롤이 통째로 막힙니다",
  ]),
  instead='한 줄로 줄이려면 말줄임, 안 줄어드는 칸은 <a href="flex.html">플렉스</a>·<a href="grid.html">그리드</a>의 <code>min-width: 0</code>, 스크롤하면서 붙여 두려면 <a href="sticky.html">스티키</a>.',
  cases=cases([
    (ob("hidden", "환불 확인 요청 — 카드 승인 취소가 늦어져", "190px", "30px", "text-overflow:ellipsis;white-space:nowrap"),
     "목록 제목", "제목을 한 줄로 자릅니다. 항목마다 <b>줄 높이가 일정해야</b> 목록을 훑어보기 쉽습니다"),
    ('''              <div style="width:100%;max-width:190px;height:62px;border:1px solid var(--line-strong);border-radius:5px;background:var(--surface);padding:7px;overflow-y:auto;font-size:10.5px;line-height:1.7">
                약관 전문은 길어서 상자 안에서 굴립니다. 화면 전체가 길어지는 것보다 낫습니다. 이 글은 일부러 넘치게 적어 둔 것입니다.
              </div>''',
     "약관 상자", "<code>overflow-y: auto</code>로 상자 안에서 스크롤해서 화면 전체가 길어지지 않게 합니다"),
    ('''              <div style="width:100%;max-width:190px;overflow-x:auto;border:1px dashed var(--line-strong);border-radius:5px;padding:6px">
                <div style="display:flex;gap:5px">
                  <span style="flex:none;background:var(--accent);color:#fff;border-radius:99px;padding:4px 9px;font-size:10px">전체</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">미처리</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">이번 주</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">₩10만 이상</span>
                </div>
              </div>''',
     "칩 줄", "폰에서는 <b>일부러</b> 가로로 밀어 보게 합니다. 끝의 칩이 잘려 보여야 사용자가 옆으로 밀 수 있다는 것을 압니다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="넘침을 다룰 때 지킬 것",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="말줄임은 <b>세 줄을 함께</b> 적어야 하고, 하나라도 빠지면 말줄임표가 나오지 않습니다.",
  code='''<span class="c">/* 한 줄 말줄임. 세 줄을 함께 쓴다 */</span>
<span class="t">.title</span> {
  <span class="a">overflow</span>: hidden;
  <span class="a">text-overflow</span>: ellipsis;
  <span class="a">white-space</span>: nowrap;
  <span class="a">min-width</span>: <span class="a">0</span>;        <span class="c">/* 플렉스·그리드 자식이면 이것도 */</span>
}

<span class="c">/* 여러 줄 말줄임 */</span>
<span class="t">.desc</span> {
  <span class="a">display</span>: -webkit-box;
  -webkit-line-clamp: <span class="a">2</span>;
  -webkit-box-orient: vertical;
  <span class="a">overflow</span>: hidden;
}

<span class="c">// 가로 스크롤 원인 찾기. 콘솔에 붙여 넣는다</span>
[...document.querySelectorAll(<span class="s">'*'</span>)].filter(el =&gt;
  el.scrollWidth &gt; document.documentElement.clientWidth);''',
  keys=kbd([
    ("말줄임은 세 줄", "<code>overflow</code> + <code>text-overflow</code> + <code>white-space</code>를 함께 써야 하고, 하나만 써서는 말줄임이 되지 않습니다"),
    ("<code>min-width: 0</code>을 잊지 않는다", "플렉스·그리드 자식은 이 줄이 없으면 <b>말줄임이 걸리지 않습니다</b>"),
    ("<code>hidden</code> 전에 원인을 본다", "가로 스크롤은 대개 <b>줄어들지 않는 칸</b> 때문에 생깁니다. 원인을 그대로 둔 채 가리면 다른 곳에서 문제가 다시 생깁니다"),
    ("자른 글은 볼 길을 준다", "<code>title</code> 속성이나 상세 화면으로 전체 글을 보여 줍니다. <b>잘린 채로 두면 사용자는 나머지 내용을 볼 수 없습니다</b>"),
    ("스크롤 상자에는 높이가 있어야", "<code>overflow: auto</code>만으로는 스크롤이 생기지 않고, <b>높이나 최대 높이</b>를 함께 줘야 합니다"),
    ("<code>hidden</code>은 부작용이 있다", "안쪽 <code>sticky</code>가 그 상자를 기준으로 붙게 되고, 상자 밖으로 나간 배지·그림자가 잘립니다"),
  ]),
  backend=rows([
    ("자르기는 화면에서, 자료는 그대로", "서버가 글을 미리 잘라 보내면 <b>툴팁에도 전체 글을 보여 줄 수 없습니다.</b> 그래서 전체를 보내고 화면에서 줄이는 편이 낫고, 서버에서 자르는 것은 양이 아주 많을 때뿐입니다."),
    ("가장 긴 값으로 한 번", "말줄임이 제대로 걸리는지는 <b>실제로 긴 데이터</b>를 넣어 봐야 알 수 있습니다. 개발 중에 쓰는 짧은 더미 데이터로는 문제가 드러나지 않습니다."),
    ("스크롤 상자와 무한 스크롤", "상자 안에서 스크롤하면 <code>window</code>에는 스크롤 이벤트가 오지 않기 때문에, <a href=\"../items/infinite.html\">무한 스크롤</a>을 붙이려면 <b>그 상자를 기준</b>으로 잡아야 합니다."),
    ("가로 스크롤 자동 검사", "<code>scrollWidth &gt; clientWidth</code> 한 줄로 검사할 수 있습니다. 이 검사를 CI에 넣어 두면 사람이 일일이 보지 않아도 <b>좁은 화면에서 레이아웃이 깨지는 것</b>을 잡아냅니다."),
  ]),
  plat_lede="넘친 내용을 처리하는 방법은 세 플랫폼 모두 있지만, 기본값이 서로 다릅니다.",
  plats=plats([
    ("웹", "CSS overflow",
     ob("auto", TXT, "120px", "50px"),
     "기본값이 <b>삐져나오기</b>(visible)라서, 자르거나 스크롤하게 하려면 직접 적어야 합니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineLimit(1)<br>.truncationMode(.tail)<br>ScrollView { }</div>''',
     "기본 동작이 <b>자르기</b>에 가깝습니다. <code>.lineLimit(1)</code> 한 줄로 말줄임이 되기 때문에 웹처럼 세 속성을 묶을 필요가 없습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">maxLines = 1<br>overflow = TextOverflow<br>&nbsp;.Ellipsis</div>''',
     "<code>maxLines</code>와 <code>overflow</code> 두 값만 주면 말줄임이 됩니다. 스크롤이 필요하면 <code>verticalScroll</code>을 붙입니다."),
  ]),
  plat_note="앱에서는 <b>말줄임이 코드 한 줄</b>이라서, 앱 개발자에게는 웹에서 세 속성을 맞춰야 하는 사정이 낯섭니다. 또 <b>\"일단 hidden으로 막았더니 다른 게 잘렸다\"</b>는 일은 웹에서만 생기는데, overflow 속성 하나가 자르기·스크롤·쌓임 맥락에 모두 영향을 주기 때문입니다.",
  siblings=siblings("overflow"),
  related='''        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><span class="na"><b>말줄임</b><em>3부</em></span></li>''',
)
