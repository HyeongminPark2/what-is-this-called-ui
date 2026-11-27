# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양으로는 구별이 안 됩니다. 이 네 가지만 물어보면 갈립니다."

def pal(q, items, label, note="", ok=None, w="152px", grp=""):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    lis = ''.join('<span style="display:flex;gap:5px;align-items:center;padding:2px 5px;border-radius:3px;'
                  'font-size:7.5px;' + ('background:var(--accent-soft);color:var(--accent);' if on else '') + '">'
                  + t + ('<small style="margin-left:auto;font-family:var(--mono);font-size:6.5px;color:var(--fg-muted)">'
                         + s + '</small>' if s else '') + '</span>'
                  for t, s, on in items)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="position:relative;height:72px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--bg);overflow:hidden">'
            '<span style="position:absolute;inset:0;background:color-mix(in srgb, var(--fg) 38%, transparent)"></span>'
            '<span style="position:absolute;left:8px;right:8px;top:7px;border-radius:5px;background:var(--surface);'
            'overflow:hidden;box-shadow:0 6px 16px rgba(20,22,26,.2)">'
            '<span style="display:block;border-bottom:1px solid var(--line);padding:4px 6px;font-size:7.5px;color:'
            + ('var(--fg)' if q else 'var(--fg-faint)') + '">' + (q or '무엇을 할까요') + '</span>'
            + ('<span style="display:block;padding:3px 6px 1px;font-size:6.5px;color:var(--fg-muted)">' + grp + '</span>' if grp else '')
            + '<span style="display:grid;gap:1px;padding:3px">' + lis + '</span></span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">Ctrl/⌘ + K — 어디서나 열린다</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">안 쳤을 때 — 최근 쓴 것을 먼저 보인다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">띄엄띄엄 쳐도 찾는다</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단축키를 오른쪽에 적어 가르친다</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">role="combobox" + listbox — 소리로도 쓸 수 있게</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">여기에만 있는 기능을 두지 않는다</div>
                </div>
              </div>'''

D = dict(
  slug="commandpalette", ko="커맨드 팔레트", en="Command palette",
  desc="Ctrl+K 로 열어 쳐서 기능을 찾는 겹침. 띄엄띄엄 찾기, 최근 쓴 것, 숨은 기능의 함정.",
  lede="<b>쳐서 찾는 메뉴</b>입니다. 기능이 수십 개를 넘어가면 메뉴보다 빠르지만, <b>있는 줄 모르면</b> 없는 것과 같습니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>팔레트를 열고 <b>정내</b> 처럼 띄엄띄엄 쳐 보세요 —
          '띄엄띄엄 쳐도 찾기'를 켜면 <b>정산 내역 내보내기</b>가 잡히고, 끄면 안 잡힙니다.
          데모가 <b>찾은 개수</b>를 둘 다 세서 적습니다.<br>
          목록이 비어 있을 때 보이는 것이 중요합니다 — <b>최근 쓴 것</b>을 먼저 보여 주면
          대부분 치지 않고도 고릅니다. 끄면 아무것도 없는 목록이 뜹니다.</p>
        </div>''',
  names=rows([
    ("한국어", "커맨드 팔레트, 명령 팔레트, 빠른 실행"),
    ("영어", "command palette, quick open, spotlight, omnibox"),
    ("같이 쓰는 말",
     "VS Code 가 퍼뜨린 이름입니다. 맥의 <b>스포트라이트</b>, "
     "Slack 의 <b>퀵 스위처</b>, Notion·Linear 의 <b>Cmd+K</b> 가 모두 같은 것입니다. "
     "띄엄띄엄 친 글자로 찾는 방식을 <b>퍼지 검색</b>(fuzzy search)이라 합니다."),
    ("자주 잘못 부름",
     "<b>검색</b> — <a href=\"search.html\">검색</a>은 <b>내용</b>을 찾고, 팔레트는 <b>기능</b>을 찾습니다.<br>"
     "<b>콤보박스</b> — <a href=\"combobox.html\">콤보박스</a>는 <b>값을 고르는 칸</b>입니다.<br>"
     "<b>모달</b> — 모달의 한 종류이긴 하지만, 쓰임이 아주 좁게 정해져 있습니다."),
  ]),
  axes=axis_table("커맨드 팔레트"),
  oneline="<b>여기에만 있는 기능을 두지 마세요.</b> 팔레트는 <b>빠른 길</b>이지 유일한 길이 아닙니다.",
  states=states([
    (pal("", [("정산 내역 내보내기", "", True), ("새 가게 등록", "", False)], "", "안 쳐도 쓸 게 보인다", True, "152px", "최근 쓴 것"),
     "열자마자", "<b>최근 쓴 것</b>부터"),
    (pal("정내", [("정산 내역 내보내기", "내보내기", True)], "", "띄엄띄엄 쳐도 찾는다", True),
     "띄엄띄엄", "<b>정</b>산 <b>내</b>역"),
    (pal("정내", [], "", "이어진 글자만 찾으면 안 잡힌다", False),
     "엄격한 찾기", "<b>놓친다</b>"),
    (pal("", [], "", "최근 쓴 것이 없으면 빈 목록", False, "152px", ""),
     "빈 목록", "<b>뭘 칠지</b> 모른다"),
    (pal("ㅋㅋㅋ", [("‘ㅋㅋㅋ’에 맞는 명령이 없습니다", "", False)], "", "다음 할 일을 준다", None),
     "결과 없음", "<b>다음 길</b>을 준다"),
    (pal("정산", [("정산 내역 내보내기", "⌘E", True), ("정산 설정 열기", "⌘,", False)], "", "단축키를 가르친다", True),
     "단축키 표시", "<b>다음엔 안 열어도</b> 되게"),
  ]),
  anat=ANAT,
  pins=pins([
    ("Ctrl/⌘ + K", "어디서나", "<b>한 손</b>으로 눌린다"),
    ("최근 쓴 것", "안 쳤을 때", "대부분 <b>치지 않고</b> 고른다"),
    ("띄엄띄엄", "퍼지 검색", "<b>정내</b> → 정산 내역"),
    ("단축키", "오른쪽에", "다음엔 <b>안 열어도</b> 되게"),
    ("역할", "combobox + listbox", "소리로도 <b>쓸 수 있게</b>"),
    ("유일한 길 금지", "메뉴에도 두기", "<b>있는 줄 모르면</b> 없는 것"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          팔레트의 가장 큰 함정은 <b>여기에만 있는 기능</b>입니다 —
          Ctrl+K 를 모르는 사람에게는 그 기능이 <b>없는 것과 같습니다</b>.
          그래서 팔레트는 늘 <b>빠른 길</b>로만 두고,
          같은 기능을 메뉴나 화면 어딘가에 <b>반드시 또</b> 두어야 합니다.<br>
          익히게 하는 가장 좋은 방법은 <b>단축키를 목록 오른쪽에 적어 두는 것</b>입니다 —
          팔레트로 두어 번 쓰다 보면 손이 단축키를 외웁니다.
          그 순간 팔레트는 자기 할 일을 한 셈입니다.</p>''',
  do=ul([
    "안 쳤을 때 <b>최근 쓴 것</b>을 먼저 보이기",
    "<b>띄엄띄엄 쳐도</b> 찾게 하기",
    "같은 기능을 <b>메뉴에도</b> 두기",
  ]),
  dont=ul([
    "<b>여기에만</b> 있는 기능 두기",
    "열자마자 <b>빈 목록</b> 보이기",
    "결과 0건에 <b>'없습니다'</b>만 적기 — 다음 길을 준다",
    "<code>&lt;div&gt;</code> 로만 만들기 — <b>소리로는 못 쓴다</b>",
  ]),
  instead='내용을 찾으면 <a href="search.html">검색</a>, 값을 고르는 칸이면 <a href="combobox.html">콤보박스</a>, 단추 옆 목록이면 <a href="menu.html">드롭다운 메뉴</a>, 처음 쓰는 사람에게는 <a href="coachmark.html">코치마크</a>.',
  cases=cases([
    (pal("", [("정산 내역 내보내기", "", True), ("새 가게 등록", "", False)], "", "", True, "150px", "최근 쓴 것"),
     "관리 도구", "<b>기능이 많은</b> 화면"),
    (pal("모란", [("모란상회", "가게", True), ("모란상회 2호점", "가게", False)], "", "", True),
     "데이터도 함께", "<b>기능 + 가게</b> 섞어 찾기"),
    (pal("정산", [("정산 설정 열기", "⌘,", True)], "", "", True), "이동", "<b>화면으로 데려가기</b>"),
  ]),
  code_lede="콤보박스 패턴을 그대로 씁니다 — 입력칸이 목록을 가리킵니다.",
  code='''&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"dialog"</span> <span class="a">aria-modal</span>=<span class="s">"true"</span> <span class="a">aria-label</span>=<span class="s">"명령 찾기"</span>&gt;
  &lt;<span class="t">input</span> <span class="a">role</span>=<span class="s">"combobox"</span> <span class="a">aria-expanded</span>=<span class="s">"true"</span>
         <span class="a">aria-controls</span>=<span class="s">"cmds"</span> <span class="a">aria-activedescendant</span>=<span class="s">"c-2"</span>
         <span class="a">aria-autocomplete</span>=<span class="s">"list"</span> <span class="a">placeholder</span>=<span class="s">"무엇을 할까요"</span>&gt;
  &lt;<span class="t">ul</span> <span class="a">id</span>=<span class="s">"cmds"</span> <span class="a">role</span>=<span class="s">"listbox"</span>&gt;
    &lt;<span class="t">li</span> <span class="a">id</span>=<span class="s">"c-2"</span> <span class="a">role</span>=<span class="s">"option"</span> <span class="a">aria-selected</span>=<span class="s">"true"</span>&gt;
      정산 내역 내보내기 &lt;<span class="t">kbd</span>&gt;⌘E&lt;/<span class="t">kbd</span>&gt;
    &lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ul</span>&gt;
&lt;/<span class="t">div</span>&gt;

<span class="c">// 띄엄띄엄 친 글자가 차례대로 들어 있으면 맞는 것으로 본다</span>
<span class="t">const</span> fuzzy = (name, q) =&gt; {
  <span class="t">let</span> i = <span class="a">0</span>;
  <span class="t">for</span> (<span class="t">const</span> ch <span class="t">of</span> name) <span class="t">if</span> (ch === q[i]) i++;
  <span class="t">return</span> i === q.length;
};''',
  keys=kbd([
    ("Ctrl/⌘ + K", "연다. <b>입력칸에서도</b> 열리게 할지 정해 둔다"),
    ("↑ ↓", "고른 줄을 옮긴다 — <b>초점은 입력칸에 둔 채</b>"),
    ("Enter", "고른 것을 실행한다"),
    ("Esc", "닫고 초점을 <b>부른 자리</b>로"),
    ("<code>aria-activedescendant</code>", "초점을 안 옮기고도 <b>고른 줄</b>을 알린다"),
    ("확인하는 법", "화면을 끄고 <b>소리만</b>으로 명령 하나를 실행해 본다"),
  ]),
  backend=rows([
    ("명령 목록", "화면이 들고 있어도 되지만, <b>권한에 따라</b> 보일 명령이 다르면 서버가 걸러 줍니다."),
    ("데이터도 섞을 때", "가게·주문처럼 <b>내용</b>까지 찾으려면 검색 API 와 같이 씁니다 — <a href=\"search.html\">검색</a>의 디바운스 규칙이 그대로 필요합니다."),
    ("최근 쓴 것", "기기마다 다를 수 있으니 <b>계정에 저장</b>하면 어디서나 같습니다."),
  ]),
  plat_lede="<b>PC 의 부품</b>입니다. 폰에는 키보드 단축키가 없습니다.",
  plats=plats([
    ("웹", "직접 만듦",
     pal("정내", [("정산 내역 내보내기", "⌘E", True)], "", "", True, "110px"),
     "라이브러리도 많지만 <b>역할과 키보드</b>는 직접 챙겨야 합니다."),
    ("iOS", "없다 — 검색",
     '''              <div class="phone" role="img" aria-label="iOS 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:999px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱 안에는 드뭅니다. OS 의 <b>스포트라이트</b>가 같은 자리를 맡습니다."),
    ("안드로이드", "없다 — 검색",
     '''              <div class="phone" role="img" aria-label="안드로이드 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:999px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "역시 드뭅니다. <b>검색 바</b>가 그 자리를 대신합니다."),
  ]),
  plat_note="팔레트가 폰에 없는 이유는 단순합니다 — <b>Ctrl+K 를 누를 키보드가 없기</b> 때문입니다. 폰에서는 같은 일을 <b>검색 바</b>가 맡고, 기능과 내용을 함께 찾게 둡니다. 그래서 웹에서도 <b>팔레트와 검색을 한 입구로</b> 묶으면 PC·폰 양쪽에서 같은 길이 됩니다 — 실제로 그렇게 만든 서비스가 늘고 있습니다.",
  siblings=siblings("commandpalette"),
  related='''        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>
        <li><a href="combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>''',
)
