# -*- coding: utf-8 -*-
from _tx import one, code, txt, mono
from tmpl import axis_table, siblings, states, cases, pins, plats, rows, ul, kbd

L6 = "겹쳐 뜨는 부품들은 모양만 보고는 구별하기 어렵지만, 아래 네 가지를 따져 보면 어느 부품인지 가려낼 수 있습니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">Ctrl/⌘ + K로 어디서나 열림</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">치기 전에는 최근 쓴 것을 먼저 보임</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">띄엄띄엄 쳐도 찾아 줌</div>
                  <div class="pin-out" data-pin="4" style="color:var(--fg-muted)">단축키를 오른쪽에 적어 알려 줌</div>
                  <div class="pin-out" data-pin="5" style="color:var(--accent)">role="combobox"와 listbox로 스크린 리더 지원</div>
                  <div class="pin-out" data-pin="6" style="color:var(--danger)">여기에만 있는 기능은 두지 않음</div>
                </div>
              </div>'''

D = dict(
  slug="commandpalette", ko="커맨드 팔레트", en="Command palette",
  desc="Ctrl+K로 열고 글자를 쳐서 기능을 찾는 겹침 부품입니다. 띄엄띄엄 친 글자로 찾기, 최근 쓴 것 먼저 보여 주기, 팔레트에만 숨은 기능의 함정을 다룹니다.",
  lede="커맨드 팔레트는 <b>글자를 쳐서 기능을 찾는 메뉴</b>입니다. 기능이 수십 개를 넘어가면 메뉴를 하나씩 여는 것보다 빠르지만, 팔레트가 <b>있는 줄 모르는 사람</b>은 그 안의 기능을 쓸 수 없습니다.",
  axes_lede=L6,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>팔레트를 열고 <b>정내</b>처럼 글자를 띄엄띄엄 쳐 보세요.
          '띄엄띄엄 쳐도 찾기'를 켜 두면 <b>정산 내역 내보내기</b>가 목록에 잡히고, 끄면 잡히지 않습니다.
          데모는 두 방식으로 <b>찾은 개수</b>를 모두 세어 보여 줍니다.<br>
          아무것도 치지 않았을 때 목록에 무엇이 보이는지도 중요합니다. <b>최근 쓴 것</b>을 먼저 보여 주면
          대부분은 글자를 치지 않고도 원하는 명령을 고르고, 이 기능을 끄면 빈 목록이 뜹니다.</p>
        </div>''',
  names=rows([
    ("한국어", "커맨드 팔레트, 명령 팔레트, 빠른 실행"),
    ("영어", "command palette, quick open, spotlight, omnibox"),
    ("같이 쓰는 말",
     "VS Code가 널리 퍼뜨린 이름입니다. 맥의 <b>스포트라이트</b>, "
     "Slack의 <b>퀵 스위처</b>, Notion·Linear의 <b>Cmd+K</b>가 모두 같은 부품입니다. "
     "띄엄띄엄 친 글자로 찾는 방식은 <b>퍼지 검색</b>(fuzzy search)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>검색</b> — <a href=\"search.html\">검색</a>은 <b>내용</b>을 찾는 반면, 팔레트는 <b>기능</b>을 찾습니다.<br>"
     "<b>콤보박스</b> — <a href=\"combobox.html\">콤보박스</a>는 목록에서 <b>값을 골라 칸을 채우는</b> 부품이고, 팔레트는 고른 명령을 실행합니다.<br>"
     "<b>모달</b> — 팔레트도 모달의 한 종류이지만, 기능을 찾아 실행하는 일로 쓰임이 아주 좁게 정해져 있습니다."),
  ]),
  axes=axis_table("커맨드 팔레트"),
  oneline="<b>팔레트에만 있는 기능을 두지 마세요.</b> 팔레트는 메뉴로도 갈 수 있는 기능에 <b>더 빨리 닿는 길</b>이어야 하고, 유일한 길이 되면 안 됩니다.",
  states=states([
    (pal("", [("정산 내역 내보내기", "", True), ("새 가게 등록", "", False)], "", "치기 전에도 고를 것이 보임", True, "152px", "최근 쓴 것"),
     "열자마자 보이는 목록", "글자를 치기 전에 <b>최근 쓴 것</b>부터 보여 줍니다"),
    (pal("정내", [("정산 내역 내보내기", "내보내기", True)], "", "띄엄띄엄 쳐도 찾음", True),
     "띄엄띄엄 쳤을 때", "'정내'만 쳐도 <b>정</b>산 <b>내</b>역을 찾습니다"),
    (pal("정내", [], "", "이어진 글자만 찾으면 놓침", False),
     "이어진 글자만 찾을 때", "글자가 이어져 있어야 찾기 때문에 '정내'로는 <b>놓칩니다</b>"),
    (pal("", [], "", "최근 쓴 것이 없으면 빈 목록", False, "152px", ""),
     "목록이 비어 있을 때", "보이는 것이 없으니 사용자가 <b>무엇을 칠지</b> 모릅니다"),
    (pal("ㅋㅋㅋ", [("‘ㅋㅋㅋ’에 맞는 명령이 없습니다", "", False)], "", "다음에 해 볼 일을 알려 줌", None),
     "맞는 결과가 없을 때", "맞는 명령이 없다고 알리고 <b>다음에 해 볼 일</b>을 보여 줍니다"),
    (pal("정산", [("정산 내역 내보내기", "⌘E", True), ("정산 설정 열기", "⌘,", False)], "", "단축키를 알려 줌", True),
     "단축키를 함께 적었을 때", "단축키를 적어 두면 <b>다음에는 팔레트를 열지 않고</b> 바로 실행할 수 있습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("Ctrl/⌘ + K", "어디서나 여는 키", "어느 화면에서든 <b>한 손</b>으로 누를 수 있습니다"),
    ("최근 쓴 것", "치기 전에 보임", "대부분은 <b>글자를 치지 않고</b> 여기서 고릅니다"),
    ("띄엄띄엄 찾기", "퍼지 검색", "<b>정내</b>만 쳐도 정산 내역을 찾습니다"),
    ("단축키", "오른쪽에 적음", "단축키를 적어 두면 다음에는 팔레트를 <b>열지 않아도</b> 됩니다"),
    ("역할", "combobox + listbox", "역할을 붙여 스크린 리더로도 <b>쓸 수 있게</b> 합니다"),
    ("다른 길", "메뉴에도 두기", "팔레트가 <b>있는 줄 모르는</b> 사람은 여기에만 있는 기능을 쓸 수 없습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          팔레트에서 가장 빠지기 쉬운 함정은 <b>팔레트에만 있는 기능</b>입니다.
          Ctrl+K를 모르는 사람은 그 기능을 <b>찾을 방법이 없기</b> 때문에,
          팔레트는 늘 <b>빠른 길</b>로만 두고
          같은 기능을 메뉴나 화면 어딘가에 <b>반드시 하나 더</b> 두어야 합니다.<br>
          단축키를 익히게 하려면 <b>목록 오른쪽에 단축키를 적어 두는 방법</b>이 가장 좋습니다.
          팔레트로 같은 명령을 두어 번 실행하다 보면 옆에 적힌 단축키가 눈에 익고,
          그 뒤로는 팔레트를 열지 않고 단축키로 바로 실행하게 됩니다.</p>''',
  do_title="커맨드 팔레트를 만들 때 지킬 것",
  dont_title="커맨드 팔레트를 만들 때 피할 것",
  do=ul([
    "아무것도 치지 않았을 때 <b>최근 쓴 것</b>을 먼저 보여 주기",
    "글자를 <b>띄엄띄엄 쳐도</b> 찾게 하기",
    "같은 기능을 <b>메뉴에도</b> 두기",
  ]),
  dont=ul([
    "<b>팔레트에만</b> 있는 기능 두기",
    "열자마자 <b>빈 목록</b> 보여 주기",
    "결과가 0건일 때 <b>'없습니다'</b>만 적기. 다음에 해 볼 일을 함께 보여 줍니다",
    "<code>&lt;div&gt;</code>로만 만들기. 역할이 없으면 <b>스크린 리더로는 쓸 수 없습니다</b>",
  ]),
  instead='기능이 아니라 내용을 찾게 하려면 <a href="search.html">검색</a>을 쓰고, 입력칸에서 값을 고르게 하려면 <a href="combobox.html">콤보박스</a>가 맞습니다. 단추 옆에 목록을 띄우려면 <a href="menu.html">드롭다운 메뉴</a>를 쓰고, 처음 쓰는 사람에게 기능을 알려 주려면 <a href="coachmark.html">코치마크</a>를 씁니다.',
  cases=cases([
    (pal("", [("정산 내역 내보내기", "", True), ("새 가게 등록", "", False)], "", "", True, "150px", "최근 쓴 것"),
     "기능이 많은 관리 도구에서 쓰기", "<b>기능이 많은</b> 관리 화면에서 씁니다"),
    (pal("모란", [("모란상회", "가게", True), ("모란상회 2호점", "가게", False)], "", "", True),
     "기능과 데이터를 함께 찾기", "<b>기능과 가게 이름</b>을 한 입력칸에서 섞어 찾습니다"),
    (pal("정산", [("정산 설정 열기", "⌘,", True)], "", "", True), "고른 화면으로 바로 이동하기", "고른 <b>화면으로 바로 이동</b>합니다"),
  ]),
  code_lede="콤보박스 패턴을 그대로 씁니다. 입력칸에 <code>aria-controls</code>를 달아 아래 목록과 연결합니다.",
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
    ("Ctrl/⌘ + K", "팔레트를 엽니다. 다른 <b>입력칸에 커서가 있을 때도</b> 열리게 할지 미리 정해 둡니다"),
    ("↑ ↓", "<b>초점은 입력칸에 둔 채</b> 고른 줄만 옮깁니다"),
    ("Enter", "고른 명령을 실행합니다"),
    ("Esc", "팔레트를 닫으면 초점이 <b>열기 전 자리</b>로 돌아갑니다"),
    ("<code>aria-activedescendant</code>", "초점을 옮기지 않고도 스크린 리더에 <b>지금 고른 줄</b>을 알립니다"),
    ("확인하는 방법", "화면을 끄고 <b>스크린 리더 소리만</b> 들으며 명령 하나를 실행해 봅니다"),
  ]),
  backend=rows([
    ("명령 목록을 내려 주는 곳", "명령 목록은 화면 쪽 코드에 두어도 되지만, 사용자 <b>권한에 따라</b> 보여 줄 명령이 달라진다면 서버가 걸러서 내려 줍니다."),
    ("데이터도 함께 찾을 때", "가게·주문처럼 <b>내용</b>까지 함께 찾으려면 검색 API를 같이 씁니다. 이때는 <a href=\"search.html\">검색</a>에서 다루는 디바운스 규칙이 그대로 필요합니다."),
    ("최근 쓴 명령을 저장하는 곳", "최근 쓴 명령을 기기에만 저장하면 기기마다 목록이 달라지므로, <b>계정에 저장</b>해 두면 어느 기기에서나 같은 목록이 보입니다."),
  ]),
  plat_lede="커맨드 팔레트는 <b>PC 화면의 부품</b>입니다. 폰에는 키보드 단축키를 누를 방법이 없기 때문입니다.",
  plats=plats([
    ("웹", "직접 만듦",
     pal("정내", [("정산 내역 내보내기", "⌘E", True)], "", "", True, "110px"),
     "라이브러리가 많지만, 어떤 것을 쓰든 <b>역할과 키보드 조작</b>은 직접 챙겨야 합니다."),
    ("iOS", "따로 없고 검색이 대신함",
     '''              <div class="phone" role="img" aria-label="iOS 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:999px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "앱 안에 두는 경우는 드물고, OS의 <b>스포트라이트</b>가 같은 일을 맡습니다."),
    ("안드로이드", "따로 없고 검색이 대신함",
     '''              <div class="phone" role="img" aria-label="안드로이드 검색 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:24px;height:9px;border-radius:999px;background:var(--bg);border:1px solid var(--line)"></div>
                <div style="position:absolute;left:5px;right:5px;top:38px;height:6px;border-radius:2px;background:var(--accent-soft)"></div></div></div>''',
     "안드로이드 앱에서도 드물고, 앱 안의 <b>검색 바</b>가 같은 일을 대신합니다."),
  ]),
  plat_note="팔레트가 폰에 없는 것은 <b>Ctrl+K를 누를 키보드가 없기</b> 때문입니다. 폰에서는 <b>검색 바</b>가 같은 일을 맡아 기능과 내용을 함께 찾게 합니다. 그래서 웹에서도 <b>팔레트와 검색을 입력칸 하나로</b> 묶어 두면 PC와 폰에서 같은 방식으로 찾을 수 있고, 실제로 그렇게 만드는 서비스가 늘고 있습니다.",
  siblings=siblings("commandpalette"),
  related='''        <li><a href="search.html"><b>검색</b><em>10부</em></a></li>
        <li><a href="combobox.html"><b>콤보박스</b><em>4부</em></a></li>
        <li><a href="modal.html"><b>모달</b><em>6부</em></a></li>
        <li><a href="keyboard.html"><b>키보드 조작</b><em>12부</em></a></li>''',
)
