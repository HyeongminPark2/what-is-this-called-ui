# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def av(inner="길동", size=40, sq=False, style="", extra=""):
    return ('<span style="width:%dpx;height:%dpx;border-radius:%s;background:var(--accent-soft);'
            'color:var(--accent);font-size:%dpx;font-weight:700;display:grid;place-items:center;'
            'flex:none;overflow:hidden;position:relative;%s">%s</span>'
            ) % (size, size, '8px' if sq else '99px', max(9, int(size * .34)), style, inner) + extra

def wrap(inner):
    return '              <div style="display:grid;place-items:center">%s</div>' % inner

ANAT = '''              <div style="background:var(--bg);border-radius:var(--r2);padding:16px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:13px">
                  <div class="pin-out" data-pin="1" style="display:flex;align-items:center;gap:10px">
                    <span style="width:40px;height:40px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:14px;font-weight:700;display:grid;place-items:center;flex:none">길동</span>
                    <span style="font-size:11px;color:var(--fg-muted)">사진이 없을 때 보이는 바닥</span>
                  </div>
                  <div class="pin-out" data-pin="2" style="display:flex;align-items:center;gap:10px">
                    <span style="width:40px;height:40px;border-radius:99px;flex:none;background:linear-gradient(135deg,#9fc0ff,#5b90f9 60%,#2254c7)"></span>
                    <span style="font-size:11px;color:var(--fg-muted)">그 위에 덮는 사진</span>
                  </div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:10px">
                    <span style="width:40px;height:40px;border-radius:9px;background:var(--accent-soft);color:var(--accent);font-size:13px;font-weight:700;display:grid;place-items:center;flex:none">모란</span>
                    <span style="font-size:11px;color:var(--fg-muted)">사각은 사람이 아니라 조직·상품</span>
                  </div>
                  <div class="pin-out" data-pin="4" style="display:flex;align-items:center;gap:10px">
                    <span style="position:relative;flex:none;line-height:0"><span style="width:40px;height:40px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:14px;font-weight:700;display:grid;place-items:center">철수</span><span style="position:absolute;right:-1px;bottom:-1px;width:12px;height:12px;border-radius:99px;background:#1f8a4c;box-shadow:0 0 0 2px var(--bg)"></span></span>
                    <span style="font-size:11px;color:var(--fg-muted)">모서리에 붙는 상태 점</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="display:flex;align-items:center;gap:10px">
                    <span style="display:flex;flex:none">
                      <span style="width:32px;height:32px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;display:grid;place-items:center;box-shadow:0 0 0 2px var(--bg)">길동</span>
                      <span style="width:32px;height:32px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;display:grid;place-items:center;box-shadow:0 0 0 2px var(--bg);margin-left:-8px">철수</span>
                      <span style="width:32px;height:32px;border-radius:99px;background:var(--ink-100);color:var(--fg-muted);font-size:11px;font-weight:700;display:grid;place-items:center;box-shadow:0 0 0 2px var(--bg);margin-left:-8px">+6</span>
                    </span>
                    <span style="font-size:11px;color:var(--fg-muted)">겹쳐 쌓고 나머지는 +N</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="avatar", ko="아바타", en="Avatar · profile picture",
  desc="아바타의 갈래와 크기, 사진이 없을 때의 이니셜 바닥, 겹쳐 쌓기와 +N 처리를 실물과 해부도로 보여주는 항목.",
  lede="사람이나 조직 <b>하나를 가리키는 작은 그림</b>. 장식이 아니라 '누구'를 말합니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>사진이 깨진 상태로</b>를 켜 보세요. 사진이 사라지고 <b>밑에 깔린 이니셜</b>이 드러납니다 —
          깨진 그림 아이콘이 아닙니다. 아바타의 기본값은 사진이 아니라 이니셜이고, 사진은 그 위에 덮는 것입니다.<br>
          사람 수를 늘려 보면 그림은 <b>셋까지만</b> 늘고 나머지는 <code>+N</code>이 됩니다.
          화면 아래에 '읽히는 말'이 함께 바뀌는 것도 보세요.</p>
        </div>''',
  names=rows([
    ("한국어", "아바타, 프로필 사진, 프사"),
    ("영어", "avatar, profile picture, user image, gravatar"),
    ("같이 쓰는 말",
     "사진이 없을 때 보이는 글자를 <b>이니셜</b>(initials · monogram), 그 바닥을 <b>폴백</b>(fallback)이라 합니다. "
     "여럿을 겹친 것은 <b>아바타 그룹</b>(avatar group · stack · facepile), "
     "모서리의 작은 점은 <b>프레즌스</b>(presence · status dot)입니다."),
    ("자주 잘못 부름",
     "<b>아이콘</b> — 아이콘은 <b>기능</b>을 가리키고 아바타는 <b>사람</b>을 가리킵니다. 생김새가 아니라 뜻이 다릅니다.<br>"
     "<b>썸네일</b> — 썸네일은 <b>내용을 줄인 그림</b>입니다. 아바타는 내용이 아니라 주체입니다.<br>"
     "<b>배지</b> — 아바타에 붙는 작은 점은 배지가 아니라 <b>상태 점</b>으로 따로 부릅니다."),
  ]),
  axes=ax("아바타"),
  oneline="아바타는 <b>'누구'를 한 조각으로 줄인 것</b>입니다. 사진이 없어도 그 일을 해야 해서, 진짜 기본값은 사진이 아니라 이니셜입니다.",
  s4_title="갈래", s4_hint="사진이 있는 경우가 오히려 드물다",
  states=states([
    (wrap(av('<span style="position:absolute;inset:0;background:linear-gradient(135deg,#9fc0ff,#5b90f9 60%,#2254c7)"></span>')), "사진", "있으면 가장 좋다. <b>그런데 자주 없다</b>"),
    (wrap(av("길동")), "이니셜", "이름에서 딴 한두 글자. <b>한글은 두 글자, 영문은 머리글자</b>"),
    (wrap(av("모란", sq=True)), "사각", "사람이 아닌 것 — 조직·상품·공간. <b>모양으로 종류를 말한다</b>"),
    (wrap(av("철수", extra='<span style="position:absolute;right:-1px;bottom:-1px;width:12px;height:12px;border-radius:99px;background:#1f8a4c;box-shadow:0 0 0 2px var(--surface)"></span>', style="position:relative")),
     "상태 점", "접속 중·자리 비움. <b>색만으로 말하지 않는다</b> — 말로도 적는다"),
    (wrap('<span style="display:flex">' + av("길동", 30, style="box-shadow:0 0 0 2px var(--surface)") +
          av("철수", 30, style="box-shadow:0 0 0 2px var(--surface);margin-left:-7px") +
          av("+6", 30, style="box-shadow:0 0 0 2px var(--surface);margin-left:-7px;background:var(--ink-100);color:var(--fg-muted)") + '</span>'),
     "겹침", "<b>셋까지</b> 보이고 나머지는 +N. 묶어서 한 번 읽힌다"),
    (wrap('<span class="skl" style="width:40px;height:40px;border-radius:99px;display:block"></span>'),
     "로딩", "<b>동그란</b> 뼈대. 네모로 두면 들어올 때 모양이 바뀐다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이니셜 바닥", "fallback · initials", "<b>진짜 기본값</b>. 사진이 못 오면 이게 그대로 보인다"),
    ("사진", "image", "바닥 위에 덮는다. 깨지면 <code>onerror</code>로 숨겨 바닥을 드러낸다"),
    ("모양", "shape", "원은 사람, <b>사각(둥근 모서리)은 조직·상품</b>. 섞어 쓰면 뜻이 흐려진다"),
    ("상태 점", "presence dot", "모서리에 붙는다. 바탕색 테두리를 둘러야 아바타와 안 섞인다"),
    ("겹침과 +N", "avatar group", "셋쯤까지만 보이고 나머지는 숫자로. <b>겹치는 쪽이 앞</b>이 되게 쌓는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          이니셜은 생각보다 어렵습니다. 한국 이름 '홍길동'은 <b>성을 뺀 두 글자</b>가 자연스럽고,
          영문 'Hong Gildong'은 머리글자 두 개(HG)입니다. 이름이 한 글자거나 이모지거나
          비어 있을 수도 있어서, <b>빈 값일 때 무엇을 보여 줄지</b>를 반드시 정해 둬야 합니다 —
          정하지 않으면 운영에서 빈 동그라미가 나옵니다.</p>''',
  do=ul([
    "<b>누가 했는지</b>가 중요한 자리 — 댓글, 대화, 활동 기록",
    "같은 이름이 여럿일 수 있을 때 — 얼굴이 이름보다 빨리 구별됩니다",
    "여럿이 함께 있는 것을 보여 줄 때(겹쳐 쌓기)",
  ]),
  dont=ul([
    "<b>이름이 바로 옆에 있는데</b> 그림까지 크게 둘 때 — 자리만 먹습니다",
    "사진을 꾸밈으로 쓰는 것 — 아바타는 <b>주체를 가리키는</b> 표시입니다",
    "모든 줄에 큰 아바타 — 목록이 느려지고 글이 밀립니다",
    "상태를 <b>색 점 하나로만</b> 말하는 것",
  ]),
  instead='사람이 아니라 기능이면 아이콘(5부), 내용의 축소판이면 썸네일, 숫자를 알리려면 <a href="badge.html">배지</a>.',
  cases=cases([
    ('''              <div style="display:flex;align-items:flex-start;gap:8px;width:100%;max-width:200px">
                ''' + av("철수", 30) + '''
                <div style="display:grid;gap:3px;min-width:0">
                  <span style="font-size:11px;font-weight:700">김철수 <span style="font-weight:400;color:var(--fg-muted)">14:02</span></span>
                  <span style="font-size:11px;background:var(--bg);border-radius:9px;padding:6px 8px">네, 오후에 확인해 볼게요</span>
                </div>
              </div>''',
     "대화", "<b>말한 사람</b>을 가리킨다. 같은 사람이 이어 말하면 두 번째부터 생략하기도 한다"),
    ('''              <div style="display:flex;align-items:center;gap:7px;width:100%;max-width:200px;font-size:11px">
                <span style="display:flex">''' + av("길동", 26, style="box-shadow:0 0 0 2px var(--surface)") +
       av("철수", 26, style="box-shadow:0 0 0 2px var(--surface);margin-left:-6px") +
       av("영희", 26, style="box-shadow:0 0 0 2px var(--surface);margin-left:-6px") + '''</span>
                <span style="color:var(--fg-muted)">외 6명이 보는 중</span>
              </div>''',
     "함께 있는 사람", "협업 도구의 상단. <b>겹쳐 쌓고 숫자로 마무리</b>한다"),
    ('''              <div style="display:grid;justify-items:center;gap:7px;width:100%;max-width:200px">
                ''' + av("길동", 56) + '''
                <span style="font-size:12px;font-weight:700">홍길동</span>
                <span style="font-size:10.5px;color:var(--fg-muted)">모란상회 · 대표</span>
              </div>''',
     "프로필", "가장 큰 자리. 여기서만 아바타가 <b>주인공</b>이 된다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 부품의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="핵심은 <b>순서</b>입니다 — 이니셜을 먼저 깔고 사진을 그 위에 덮습니다. 반대로 하면 사진이 깨졌을 때 아무것도 안 남습니다.",
  code='''&lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"av"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;길동
  &lt;<span class="t">img</span> <span class="a">src</span>=<span class="s">"/u/12.jpg"</span> <span class="a">alt</span>=<span class="s">""</span>
       <span class="a">onerror</span>=<span class="s">"this.remove()"</span>&gt;   <span class="c">&lt;!-- 깨지면 이니셜이 드러난다 --&gt;</span>
&lt;/<span class="t">span</span>&gt;
&lt;<span class="t">span</span>&gt;홍길동&lt;/<span class="t">span</span>&gt;

<span class="c">/* 사진은 바닥을 덮는다 */</span>
<span class="t">.av</span>     { <span class="a">position</span>: relative; <span class="a">overflow</span>: hidden; <span class="a">border-radius</span>: <span class="a">50%</span>; }
<span class="t">.av</span> <span class="t">img</span> { <span class="a">position</span>: absolute; <span class="a">inset</span>: <span class="a">0</span>; <span class="a">width</span>: <span class="a">100%</span>; <span class="a">height</span>: <span class="a">100%</span>;
           <span class="a">object-fit</span>: cover; }

<span class="c">&lt;!-- 겹친 무리는 하나로 읽는다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"img"</span> <span class="a">aria-label</span>=<span class="s">"참여자 9명: 홍길동, 김철수, …"</span>&gt;…&lt;/<span class="t">span</span>&gt;''',
  keys=kbd([
    ("이니셜을 먼저", "사진은 덮개다. 순서를 바꾸면 사진이 깨졌을 때 <b>빈 동그라미</b>가 남는다"),
    ("<code>object-fit: cover</code>", "세로 사진도 가로 사진도 동그라미를 꽉 채운다. 안 쓰면 찌그러진다"),
    ("이름이 옆에 있으면 숨긴다", "<code>aria-hidden=\"true\"</code> — 같은 말을 두 번 읽으면 시끄럽다"),
    ("겹친 무리는 하나로", "<code>role=\"img\"</code> + <code>aria-label</code>로 묶어 한 번만 읽히게 한다"),
    ("상태 점은 말로도", "초록 점에 <code>title</code>이나 보이지 않는 글로 '접속 중'을 적는다"),
    ("누를 수 있으면 <code>&lt;button&gt;</code>", "프로필로 가는 아바타는 <b>진짜 버튼이나 링크</b>여야 키보드로 눌린다"),
  ]),
  backend=rows([
    ("사진은 없을 수 있다", "가입에 사진이 필수가 아니면 <b>대부분 없습니다.</b> 그래서 이니셜 바닥이 기본 화면이고, 사진은 '있으면 좋은 것'입니다."),
    ("이니셜과 색은 서버가 정하지 않는다", "이름에서 따는 규칙과 바탕색은 화면이 정합니다. 다만 <b>같은 사람은 늘 같은 색</b>이 나오게 이름을 해시해 고릅니다."),
    ("크기별로 잘라 둔다", "목록의 28px 자리에 2,000px 원본을 보내면 느려집니다. 업로드 때 <b>몇 가지 크기로 미리 잘라</b> 두고 화면이 골라 씁니다."),
    ("캐시와 바뀐 사진", "사진 주소가 같으면 바꿔도 예전 것이 보입니다. 파일 이름에 <b>버전이나 해시</b>를 넣습니다."),
    ("지운 사용자", "탈퇴한 사람의 아바타는 <b>익명 바닥</b>으로 바뀌어야 합니다. 이름을 그대로 두면 지워지지 않은 셈입니다."),
  ]),
  plat_lede="세 플랫폼 모두 '동그란 사람 그림'이라는 점은 같고, 부품으로 정해져 있는지가 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     '              <div style="display:grid;place-items:center">' + av("길동", 34) + '</div>',
     "<code>&lt;img&gt;</code>에 <code>border-radius: 50%</code>가 전부입니다. 폴백은 직접 만들어야 합니다."),
    ("iOS", "SF Symbols · 직접 그림",
     '''              <div class="phone" role="img" aria-label="iOS 아바타 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;align-items:center;gap:6px">
                  <span style="width:18px;height:18px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:7px;font-weight:700;display:grid;place-items:center">길동</span>
                  <span style="font-size:7.5px">홍길동</span></div>
              </div></div>''',
     "정해진 부품이 없습니다. 연락처 쪽의 <b>모노그램</b> 관례를 따르고, 사진이 없으면 <b>이니셜 원</b>을 그립니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 아바타 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:8px;right:8px;top:30px;display:flex;align-items:center;gap:6px">
                  <span style="width:18px;height:18px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:7px;font-weight:700;display:grid;place-items:center">길동</span>
                  <span style="font-size:7.5px">홍길동</span></div>
              </div></div>''',
     "리스트의 앞자리 규격(<b>leading avatar</b>, 40dp)이 정해져 있고, 이니셜 바닥도 가이드에 있습니다."),
  ]),
  plat_note="세 쪽 다 <b>이니셜 규칙을 각자 정합니다.</b> 웹은 '길동', 안드로이드는 'ㅎ', iOS 는 'HG' 식으로 제품마다 달라져 같은 사람이 플랫폼마다 다르게 보이는 일이 흔합니다. <b>이니셜 만드는 규칙 한 줄</b>을 미리 합의해 두면 그대로 막힙니다.",
  siblings=siblings("avatar"),
  related='''        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/skeleton.html"><b>스켈레톤</b><em>8부</em></a></li>
        <li><span class="na"><b>아이콘</b><em>5부</em></span></li>
        <li><span class="na"><b>스크린 리더가 읽는 것</b><em>12부</em></span></li>''',
)
