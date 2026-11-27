# -*- coding: utf-8 -*-
from ax3 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">문장형 Export settlements, 첫 글자만 대문자</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">제목형 Export Settlements, 단어마다 대문자</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">대문자 EXPORT SETTLEMENTS, 단어 윤곽이 사라짐</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">text-transform 은 보이는 모양만 바꾸고 값은 그대로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">대문자는 빽빽해 보여 자간을 조금 벌림</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한국어는 대소문자가 없어 섞으면 모양이 어긋남</div>
                </div>
              </div>'''

D = dict(
  slug="casing", ko="대소문자", en="Letter case",
  desc="영어 대소문자의 네 가지 꼴과 각각을 쓰는 자리, 대소문자 구분이 없는 한국어와 섞어 쓸 때 생기는 문제를 보여 주는 항목입니다.",
  lede="영어 글자에는 대소문자를 섞는 방식에 따라 <b>네 가지 꼴</b>이 있고, 자리마다 쓰는 관례가 다릅니다. 한국어에는 <b>대소문자 구분이 없어서</b>, 두 언어를 한 줄에 섞으면 영어만 꼴이 바뀌어 모양이 어긋납니다.",
  axes_lede="글자 항목은 모두 글을 잘 읽히게 하려고 씁니다. 아래 네 가지로 서로 가릅니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>꼴을 바꿔 가며 네 자리를 살펴보세요. 요즘 OS 지침은 <b>문장형</b>을 기본으로 권하는데,
          읽기 쉽고 번역해도 덜 어색하기 때문입니다.<br>
          <b>한국어도 함께 보기</b>를 켜 두면 영어만 바뀌고
          <b>한국어는 그대로</b>라서, 한 줄 안에서 두 언어의 글자 모양이 어긋나는 것을 볼 수 있습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대소문자, 문장형, 제목형, 전부 대문자"),
    ("영어", "sentence case, title case, UPPERCASE / all caps, lowercase"),
    ("같이 쓰는 말",
     "첫 글자만 대문자로 쓰는 꼴을 <b>문장형</b>(sentence case), 단어마다 첫 글자를 대문자로 쓰는 꼴을 <b>제목형</b>(title case), "
     "모든 글자를 대문자로 쓰는 꼴을 <b>올 캡스</b>(all caps)라고 합니다. "
     "소문자와 높이가 같은 작은 대문자는 <b>스몰 캡스</b>(small caps)라고 하며, "
     "CSS에서는 <code>font-variant-caps</code>로 켭니다."),
    ("자주 잘못 부르는 이름",
     "<b>볼드</b> — 볼드는 대소문자가 아니라 <a href=\"../items/weight.html\">글자 굵기</a>에 속하는 강조 수단입니다.<br>"
     "<b>캡스락</b> — 키보드 키의 이름이라서, 글자 꼴을 가리키는 말과는 다릅니다.<br>"
     "<b>대문자화</b> — <code>capitalize</code>는 <b>단어마다 첫 글자</b>를 대문자로 바꿀 뿐이라서, 관사를 소문자로 두는 제목형의 규칙까지는 처리하지 못합니다."),
  ]),
  axes=ax("대소문자"),
  oneline="<b>문장형을 기본으로</b> 씁니다. 전부 대문자로 쓰면 눈에 띄기는 하지만 <b>단어의 윤곽</b>이 사라져 읽는 속도가 느려집니다.",
  s4_title="네 가지 꼴", s4_hint="꼴마다 알맞은 자리",
  states=states([
    (one(txt('Export settlements', "13px"), "문장형", True, "읽기 쉽고 번역해도 덜 어색함"), "첫 글자만 대문자인 문장형", "<b>요즘 OS 지침에서 기본으로 권하는</b> 꼴입니다"),
    (one(txt('Export Settlements', "13px"), "제목형", None, "a · of · the 처리 규칙이 따로 필요"), "단어마다 대문자인 제목형", "짧은 제목이나 메뉴에 씁니다"),
    (one('<span style="font-size:13px;text-transform:uppercase;letter-spacing:.04em">Export settlements</span>', "대문자", False, "단어 윤곽이 사라짐"),
     "모두 대문자로 쓸 때", "단어 윤곽이 사라져 <b>읽기가 느려집니다</b>"),
    (one('<span style="font-size:13px;text-transform:lowercase">Export Settlements</span>', "소문자", False, "고유명사까지 소문자가 됨"),
     "모두 소문자로 쓸 때", "브랜드 분위기를 내려고 쓰지만, 고유명사까지 소문자가 되어 어색합니다"),
    (one(txt('EXPORT 정산 내보내기', "13px"), "섞였을 때", False, "영어만 바뀌고 한국어는 그대로"),
     "한국어와 섞어 쓸 때", "영어만 바뀌어서 <b>한 줄 안에서 글자 모양이 어긋납니다</b>"),
    (one(mono('ABC', 'var(--fg)') + ' ' + '<span style="font-size:13px;font-variant-caps:all-small-caps">ABC</span>', "스몰 캡스", None, "높이를 낮춘 대문자"),
     "높이를 낮춘 스몰 캡스", "약자나 단위에 씁니다. <b>글꼴이 지원해야</b> 제대로 나옵니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("문장형", "첫 글자만 대문자", "<b>기본으로 삼습니다.</b> 번역해도 덜 어색합니다"),
    ("제목형", "단어마다 대문자", "관사와 전치사를 대문자로 쓸지 정하는 <b>규칙이 따로 필요</b>합니다"),
    ("전부 대문자", "단어 윤곽이 사라짐", "모든 글자가 네모난 윤곽이 되어서 <b>단어 모양</b>만 보고 읽을 수 없습니다"),
    ("<code>text-transform</code>", "보이는 모양만 바꿈", "보이는 모양만 바뀌고 <b>값은 그대로</b>라서, 복사하면 원래 글자가 나옵니다"),
    ("자간", "조금 벌림", "대문자는 빽빽해 보여서 <a href=\"../items/letterspacing.html\">자간</a>을 조금 벌립니다"),
    ("한국어", "대소문자 구분 없음", "영어와 <b>섞으면 영어만 바뀌어 모양이 어긋납니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>text-transform</code>은 보이는 모양만 바꿉니다.</b>
          값은 원래 글자 그대로라서, 복사해 붙이면 원래 쓴 소문자가 나오고
          검색도 원래 글자로 걸리는데, 대개는 이쪽이 더 편리합니다.
          다만 <b>스크린 리더가 대문자 낱말을 약자로 읽는</b> 경우가 있어서
          'EXPORT'를 '이엑스피오알티'처럼 한 글자씩 읽기도 합니다.
          그래서 전부 대문자가 필요하면 <b>글자는 문장형으로 적고
          CSS로 보이는 모양만 대문자로 바꾸는</b> 편이 안전합니다.</p>''',
  do=ul([
    "<b>문장형</b>을 기본값으로 정해 둘 때",
    "짧은 레이블이나 메뉴에 제목형을 쓸 때",
    "대문자를 쓰면서 <b>자간을 조금</b> 벌릴 때",
  ]),
  dont=ul([
    "본문이나 긴 제목을 전부 대문자로 쓸 때. <b>읽기가 느려집니다</b>",
    "글자 자체를 대문자로 적을 때. 대문자는 <b>CSS로</b> 바꿉니다",
    "한국어와 섞인 줄에 <code>text-transform</code>을 전역으로 걸 때. 영어만 바뀌어 모양이 어긋납니다",
    "제목형을 사람이 손으로 적을 때. 관사를 어떻게 쓸지 사람마다 달라집니다",
  ]),
  do_title="대소문자 꼴을 알맞게 쓰는 경우", dont_title="대소문자 꼴을 잘못 쓰는 경우",
  instead='대문자 대신 다른 방법으로 강조하려면 <a href="../items/weight.html">글자 굵기</a>를 바꾸고, 크기 차이로 구별하려면 <a href="../items/typescale.html">타입 스케일</a>을 씁니다. 줄 사이 간격은 <a href="../items/lineheight.html">행간</a>에서 다룹니다.',
  cases=cases([
    (one(txt('Export settlements', "12px"), "버튼", True, "문장형"), "버튼 글자는 문장형으로", "글이 <b>짧아도 문장형</b>으로 쓰는 편이 안전합니다"),
    (one('<span style="font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--fg-muted)">SETTLEMENTS</span>', "표 머리글", None, "작고 짧을 때만"),
     "짧은 표 머리글은 대문자로", "글이 짧고 작으면 <b>대문자로 써도 괜찮습니다</b>"),
    (one(txt('정산 내보내기', "12px"), "한국어", True, "바꿀 것이 없음"), "한국어만 쓰는 화면", "대소문자가 없으므로 <b>꼴을 정하지 않아도 됩니다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="글자는 문장형으로 적고 모양은 CSS로 바꾸기",
  keys_heads="<th>구현할 때 알아 둘 점</th><th>자세한 내용</th>",
  code_lede="글자는 문장형으로 적고, 대문자로 보여야 할 때는 CSS로 보이는 모양만 바꿉니다.",
  code='''<span class="c">&lt;!-- 글자는 그대로 둔다. 복사와 검색이 원래 글자로 된다 --&gt;</span>
&lt;<span class="t">th</span> <span class="a">class</span>=<span class="s">"col"</span>&gt;Settlements&lt;/<span class="t">th</span>&gt;

.col {
  <span class="a">text-transform</span>: uppercase;
  <span class="a">letter-spacing</span>: .<span class="a">06em</span>;   <span class="c">/* 대문자는 빽빽해 보인다 */</span>
  <span class="a">font-size</span>: <span class="a">11px</span>;
}

<span class="c">/* 한국어가 섞이는 줄에는 걸지 않는다. 영어만 바뀌어 모양이 어긋난다 */</span>
.title { <span class="a">text-transform</span>: none; }''',
  keys=kbd([
    ("값은 원래 글자 그대로 남음", "<code>text-transform</code>은 <b>보이는 모양만</b> 바꿉니다. 복사하면 원래 글자가 나옵니다"),
    ("스크린 리더가 약자로 읽을 수 있음", "대문자 낱말을 <b>한 글자씩</b> 읽는 스크린 리더가 있습니다"),
    ("<code>capitalize</code>가 처리하지 못하는 관사", "단어마다 첫 글자만 대문자로 바꾸고, <b>관사 규칙</b>은 처리하지 못합니다"),
    ("<code>font-variant-caps</code>는 글꼴 지원이 필요", "스몰 캡스는 <b>글꼴이 지원해야</b> 합니다. 지원하지 않으면 브라우저가 대문자를 줄여 흉내 낸 글자가 나옵니다"),
    ("한국어가 섞인 줄", "한국어는 바뀌는 것이 없어서, <b>전역으로 걸면</b> 영어만 바뀌어 눈에 띕니다"),
    ("언어마다 다른 대소문자 규칙", "영어 기준으로 꼴을 정해도 다른 언어는 <b>규칙이 다릅니다</b>. 예를 들어 독일어는 명사를 늘 대문자로 시작합니다"),
  ]),
  backend=rows([
    ("저장은 원래 꼴 그대로", "대문자는 화면에서만 바꿔 보여 주고 <b>저장하는 값은 그대로</b> 둡니다. 대문자로 바꿔 저장하면 원래 꼴로 되돌릴 수 없습니다."),
    ("대소문자를 무시하는 검색과 정렬", "대소문자를 무시하고 비교할지 미리 정해 둡니다. 비교 방식은 DB 설정(collation)에 따라 달라집니다."),
    ("아이디와 이메일의 대소문자", "대소문자를 가릴지에 따라 <b>로그인 결과가 달라집니다</b>. 이메일은 보통 대소문자를 가리지 않습니다."),
  ]),
  plat_lede="세 플랫폼 모두 지금은 <b>문장형</b>을 기본으로 씁니다.",
  plats=plats([
    ("웹", "text-transform",
     one(txt('Export settlements', "11px"), "", True, "", "110px"),
     "정해진 표준이 없어서 팀마다 정합니다. <b>문장형</b>을 기본으로 두는 곳이 많습니다."),
    ("iOS", "문장형",
     '''              <div class="phone" role="img" aria-label="iOS 문장형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:6px">Export settlements</div></div></div>''',
     "HIG는 <b>문장형</b>을 권합니다. 예전에는 제목형을 권했다가 바뀌었습니다."),
    ("안드로이드", "문장형",
     '''              <div class="phone" role="img" aria-label="Material 문장형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:6px">Export settlements</div></div></div>''',
     "M3도 <b>문장형</b>을 씁니다. 버튼 글자를 대문자로 쓰던 관례는 M2에서 사라졌습니다."),
  ]),
  plat_note="한국어만 쓰는 화면이라면 이 항목은 <b>신경 쓸 일이 거의 없습니다</b>. 문제는 영어가 섞일 때이고, 특히 <b>버튼이나 표 머리글</b>처럼 두 언어가 한 줄에 오는 자리에서 생깁니다. <code>text-transform</code>을 전역으로 걸어 두면 영어만 바뀌어 눈에 띄므로, 적용할 자리를 좁게 정해 두는 편이 낫습니다.",
  siblings=siblings("casing"),
  related='''        <li><a href="../items/letterspacing.html"><b>자간</b><em>3부</em></a></li>
        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="buttontext.html"><b>버튼 문구</b><em>14부</em></a></li>
        <li><a href="koreanui.html"><b>한국어 UI</b><em>14부</em></a></li>''',
)
