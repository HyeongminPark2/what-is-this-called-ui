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
  desc="overflow 네 값의 차이와 말줄임, 가로 스크롤이 생기는 진짜 원인을 실물과 해부도로 보여주는 항목.",
  lede="상자보다 내용이 클 때 <b>무엇을 할지 고르는 것</b>. 안 고르면 기본값(삐져나오기)이 고른 셈이 됩니다.",
  axes_lede="뼈대를 다루는 것들은 '눈에 안 보이는데 자리를 정한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 글이 네 가지 <code>overflow</code>에서 어떻게 다른지 나란히 두었습니다.
          <code>scroll</code>은 <b>안 넘쳐도 스크롤바 자리를 잡는 것</b>을 보세요.<br>
          아래는 <b>가로 스크롤 범인 찾기</b>입니다. 체크를 켜고 끄면서
          <code>scrollWidth - clientWidth</code>가 어떻게 변하는지 보세요 —
          범인은 거의 늘 <b>줄어들지 못하는 칸 하나</b>입니다.</p>
        </div>''',
  names=rows([
    ("한국어", "넘침, 오버플로, 말줄임"),
    ("영어", "overflow, clipping, scroll container, text-overflow"),
    ("같이 쓰는 말",
     "스크롤이 생긴 상자를 <b>스크롤 컨테이너</b>(scroll container), 잘라 내는 것을 <b>클리핑</b>(clipping), "
     "끝을 <code>…</code>으로 줄이는 것을 <b>말줄임</b>(ellipsis · truncation)이라 합니다. "
     "가로만 따로 정하려면 <code>overflow-x</code>, 세로만은 <code>overflow-y</code>입니다."),
    ("자주 잘못 부름",
     "<b><code>hidden</code>과 말줄임</b> — <code>hidden</code>은 <b>그냥 자릅니다.</b> "
     "<code>…</code>이 나오려면 <code>text-overflow: ellipsis</code>와 <code>white-space: nowrap</code>이 같이 있어야 합니다.<br>"
     "<b><code>auto</code>와 <code>scroll</code></b> — auto 는 넘칠 때만, scroll 은 <b>늘</b> 스크롤바 자리를 잡습니다.<br>"
     "<b>'가로 스크롤이 생겼다'</b> — overflow 설정 문제가 아니라 <b>안에 안 줄어드는 것이 있다</b>는 뜻입니다."),
  ]),
  axes=ax("넘침"),
  oneline="넘침은 <b>고르는 일</b>입니다. 안 고르면 '삐져나오기'를 고른 것이고, <code>hidden</code>은 '안 읽혀도 된다'를 고른 것입니다.",
  s4_title="갈래", s4_hint="네 값이 다 다르게 동작한다",
  states=states([
    (ob("visible"), "visible", "기본값. <b>밖으로 삐져나온다</b> — 부모에 가려 안 보일 수도"),
    (ob("hidden"), "hidden", "<b>잘린다.</b> 읽을 방법이 없어진다"),
    (ob("auto"), "auto", "넘칠 때<b>만</b> 스크롤바. 가장 무난하다"),
    (ob("scroll", "짧은 글."), "scroll", "<b>안 넘쳐도</b> 스크롤바 자리를 잡는다. 자리가 흔들리면 안 될 때"),
    (ob("hidden", "한 줄이 길어도 끝까지 가지 않고 말줄임", "150px", "34px", "text-overflow:ellipsis;white-space:nowrap"),
     "말줄임", "<b>세 속성이 한 세트</b> — overflow + text-overflow + white-space"),
    ('''              <div style="width:100%;max-width:150px;height:46px;border:1px solid var(--line-strong);border-radius:5px;background:var(--surface);padding:7px;overflow-x:auto">
                <div style="display:flex;gap:5px">
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 하나</span>
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 둘</span>
                  <span style="flex:none;background:var(--accent-soft);color:var(--accent);border-radius:4px;padding:4px 7px;font-size:10px;white-space:nowrap">칩 셋</span>
                </div>
              </div>''',
     "일부러 가로로", "칩 줄·탭 줄은 <b>가로 스크롤이 맞는 답</b>일 때가 있다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("스크롤 컨테이너", "scroll container", "<code>overflow</code>가 visible 이 아닌 상자. <b>여기서부터 안쪽이 따로 굴러간다</b>"),
    ("visible", "overflow: visible", "기본값. 자르지도 굴리지도 않는다 — <b>부모가 대신 가릴 수는 있다</b>"),
    ("hidden", "overflow: hidden", "자른다. 쉬워 보이지만 <b>읽을 방법을 없애는</b> 선택이다"),
    ("auto", "overflow: auto", "넘칠 때만 스크롤. 길이를 모를 때의 기본 선택"),
    ("말줄임", "text-overflow: ellipsis", "<b>혼자서는 안 된다.</b> overflow·white-space 와 세 개가 한 세트"),
    ("안 줄어드는 칸", "min-width: 0", "가로 스크롤의 진짜 원인. <b>overflow 를 고쳐도 안 낫는다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <code>overflow</code>를 visible 이 아닌 값으로 바꾸면 <b>다른 일들도 같이 바뀝니다.</b>
          그 안의 <code>position: sticky</code>가 그 상자 기준으로 바뀌고(그래서 '스티키가 안 먹어요'),
          밖으로 나간 그림자·배지·드롭다운이 잘립니다. 그래서 <b>"일단 hidden 으로 막자"</b>가
          다른 자리에서 새 버그로 돌아오는 일이 잦습니다.</p>''',
  do=ul([
    "길이를 <b>모르는</b> 내용을 담을 때 — <code>auto</code>",
    "목록의 제목처럼 <b>한 줄로 맞춰야</b> 할 때 — 말줄임 세 줄",
    "칩 줄·탭 줄처럼 <b>옆으로 미는 것이 맞는</b> 때 — <code>overflow-x: auto</code>",
  ]),
  dont=ul([
    "<b>원인을 모른 채 <code>hidden</code>으로 덮는 것</b> — 가로 스크롤은 대개 안쪽에 범인이 있습니다",
    "말줄임만 쓰고 <b>전체를 볼 방법을 안 주는</b> 것 — 툴팁이나 상세로 이어 줍니다",
    "<code>scroll</code>을 기본으로 쓰는 것 — 안 넘쳐도 스크롤바 자리가 남습니다",
    "<code>body</code>에 <code>overflow: hidden</code> — 스크롤이 통째로 막힙니다",
  ]),
  instead='한 줄로 줄이려면 말줄임, 안 줄어드는 칸은 <a href="flex.html">플렉스</a>·<a href="grid.html">그리드</a>의 <code>min-width: 0</code>, 굴리면서 붙여 두려면 <a href="sticky.html">스티키</a>.',
  cases=cases([
    (ob("hidden", "환불 확인 요청 — 카드 승인 취소가 늦어져", "190px", "30px", "text-overflow:ellipsis;white-space:nowrap"),
     "목록 제목", "한 줄로 자른다. <b>줄 높이가 일정해야</b> 목록이 산다"),
    ('''              <div style="width:100%;max-width:190px;height:62px;border:1px solid var(--line-strong);border-radius:5px;background:var(--surface);padding:7px;overflow-y:auto;font-size:10.5px;line-height:1.7">
                약관 전문은 길어서 상자 안에서 굴립니다. 화면 전체가 길어지는 것보다 낫습니다. 이 글은 일부러 넘치게 적어 둔 것입니다.
              </div>''',
     "약관 상자", "<code>overflow-y: auto</code>. 화면을 길게 만들지 않는다"),
    ('''              <div style="width:100%;max-width:190px;overflow-x:auto;border:1px dashed var(--line-strong);border-radius:5px;padding:6px">
                <div style="display:flex;gap:5px">
                  <span style="flex:none;background:var(--accent);color:#fff;border-radius:99px;padding:4px 9px;font-size:10px">전체</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">미처리</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">이번 주</span>
                  <span style="flex:none;background:var(--surface);border:1px solid var(--line-strong);border-radius:99px;padding:4px 9px;font-size:10px">₩10만 이상</span>
                </div>
              </div>''',
     "칩 줄", "폰에서 <b>일부러</b> 가로로 민다. 끝이 잘린 것이 보여야 민다는 걸 안다"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 상자의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="말줄임은 <b>세 줄이 한 세트</b>입니다. 하나라도 빠지면 아무 일도 안 일어납니다.",
  code='''<span class="c">/* 한 줄 말줄임 — 세 줄이 한 세트 */</span>
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

<span class="c">// 범인 찾기 — 콘솔에 붙여 넣는다</span>
[...document.querySelectorAll(<span class="s">'*'</span>)].filter(el =&gt;
  el.scrollWidth &gt; document.documentElement.clientWidth);''',
  keys=kbd([
    ("말줄임은 세 줄", "<code>overflow</code> + <code>text-overflow</code> + <code>white-space</code>. 하나만 써도 안 된다"),
    ("<code>min-width: 0</code>을 잊지 않는다", "플렉스·그리드 자식이면 이 줄이 없을 때 <b>말줄임이 영영 안 걸린다</b>"),
    ("<code>hidden</code> 전에 원인을 본다", "가로 스크롤은 대개 <b>안 줄어드는 칸</b> 때문이다. 덮으면 다른 데서 터진다"),
    ("자른 글은 볼 길을 준다", "<code>title</code> 속성이나 상세 화면으로. <b>잘린 채 끝나면 정보가 사라진다</b>"),
    ("스크롤 상자에는 높이가 있어야", "<code>overflow: auto</code>만으로는 안 굴러간다. <b>높이나 최대 높이</b>가 필요하다"),
    ("<code>hidden</code>은 부작용이 있다", "안쪽 <code>sticky</code>가 그 상자 기준이 되고, 밖으로 나간 배지·그림자가 잘린다"),
  ]),
  backend=rows([
    ("자르기는 화면에서, 자료는 그대로", "서버가 미리 잘라 보내면 <b>툴팁에도 전체가 없습니다.</b> 전체를 보내고 화면에서 줄이는 편이 낫습니다 — 양이 아주 많을 때만 서버에서 자릅니다."),
    ("가장 긴 값으로 한 번", "말줄임이 걸리는지는 <b>실제로 긴 데이터</b>로만 알 수 있습니다. 개발 중의 짧은 더미 데이터로는 평생 안 드러납니다."),
    ("스크롤 상자와 무한 스크롤", "상자 안에서 굴리면 <code>window</code>의 스크롤 이벤트가 안 옵니다. <a href=\"../items/infinite.html\">무한 스크롤</a>을 붙이려면 <b>그 상자를 기준</b>으로 잡아야 합니다."),
    ("가로 스크롤 자동 검사", "<code>scrollWidth &gt; clientWidth</code> 한 줄이면 됩니다. CI 에 넣어 두면 <b>좁은 화면이 깨지는 것</b>을 사람이 안 봐도 잡힙니다."),
  ]),
  plat_lede="'넘치면 어떻게'는 세 플랫폼 모두 있지만, 기본값이 다릅니다.",
  plats=plats([
    ("웹", "CSS overflow",
     ob("auto", TXT, "120px", "50px"),
     "기본값이 <b>삐져나오기</b>(visible)입니다. 자르거나 굴리려면 직접 적어야 합니다."),
    ("iOS", "SwiftUI",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">.lineLimit(1)<br>.truncationMode(.tail)<br>ScrollView { }</div>''',
     "기본값이 <b>자르기</b>에 가깝습니다. <code>.lineLimit(1)</code> 한 줄로 말줄임이 되고 세 속성을 묶을 필요가 없습니다."),
    ("안드로이드", "Compose",
     '''              <div style="font-family:var(--mono);font-size:9.5px;color:var(--fg-muted);line-height:1.8;text-align:left">maxLines = 1<br>overflow = TextOverflow<br>&nbsp;.Ellipsis</div>''',
     "<code>maxLines</code> 와 <code>overflow</code> 두 값이면 끝입니다. 스크롤은 <code>verticalScroll</code> 을 붙입니다."),
  ]),
  plat_note="앱 쪽에서는 <b>말줄임이 한 줄</b>이라, 웹에서 세 속성을 맞춰야 하는 사정이 낯섭니다. 또 웹에서만 <b>\"일단 hidden 으로 막았더니 다른 게 잘렸다\"</b>는 일이 생깁니다 — 같은 속성이 자르기·스크롤·쌓임 맥락에 다 걸려 있기 때문입니다.",
  siblings=siblings("overflow"),
  related='''        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/flex.html"><b>플렉스</b><em>1부</em></a></li>
        <li><a href="../items/zindex.html"><b>z-index</b><em>2부</em></a></li>
        <li><span class="na"><b>말줄임</b><em>3부</em></span></li>''',
)
