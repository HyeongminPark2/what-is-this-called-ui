# -*- coding: utf-8 -*-
from ax3 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">문장형 — Export settlements. 첫 글자만</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">제목형 — Export Settlements. 단어마다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">대문자 — EXPORT SETTLEMENTS. 윤곽이 사라진다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">text-transform 은 보이기만 바꾼다 — 값은 그대로</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">자간을 조금 벌린다 — 대문자는 빽빽해 보인다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한국어에는 대소문자가 없다 — 한 줄 안에서 결이 어긋난다</div>
                </div>
              </div>'''

D = dict(
  slug="casing", ko="대소문자", en="Letter case",
  desc="영어의 네 가지 꼴과 쓰는 자리. 한국어에는 없는 구분이라 섞어 쓸 때 결이 어긋난다.",
  lede="영어에는 <b>네 가지 꼴</b>이 있고 자리마다 관례가 다릅니다. 한국어에는 <b>없는 구분</b>이라 섞으면 어긋납니다.",
  axes_lede="글자는 읽히려고 있습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>꼴을 바꿔 가며 네 자리를 봐 보세요. 요즘 OS 지침은 <b>문장형</b>을 기본으로 권합니다 —
          읽기 쉽고 번역해도 덜 깨지기 때문입니다.<br>
          <b>한국어도 함께 보기</b>를 켜 두면 알 수 있습니다 — 영어만 바뀌고
          <b>한국어는 그대로</b>라, 한 줄 안에서 결이 어긋납니다.</p>
        </div>''',
  names=rows([
    ("한국어", "대소문자, 문장형, 제목형, 전부 대문자"),
    ("영어", "sentence case, title case, UPPERCASE / all caps, lowercase"),
    ("같이 쓰는 말",
     "첫 글자만 대문자가 <b>문장형</b>(sentence case), 단어마다가 <b>제목형</b>(title case), "
     "전부 대문자가 <b>올 캡스</b>(all caps)입니다. "
     "높이가 같은 작은 대문자는 <b>스몰 캡스</b>(small caps)라 하고 "
     "CSS 에서는 <code>font-variant-caps</code>로 켭니다."),
    ("자주 잘못 부름",
     "<b>볼드</b> — 굵기는 <a href=\"../items/weight.html\">글자 굵기</a>입니다. 강조 수단이 다릅니다.<br>"
     "<b>캡스락</b> — 키보드 키 이름입니다. 글자 꼴 이야기와는 다릅니다.<br>"
     "<b>대문자화</b> — <code>capitalize</code>는 <b>단어마다 첫 글자</b>를 올립니다. 제목형의 규칙(관사 처리)까지는 못 합니다."),
  ]),
  axes=ax("대소문자"),
  oneline="<b>문장형을 기본으로.</b> 전부 대문자는 눈에 띄는 대신 <b>단어 윤곽</b>을 지워 읽기를 느리게 합니다.",
  s4_title="네 가지 꼴", s4_hint="어느 자리에 맞나",
  states=states([
    (one(txt('Export settlements', "13px"), "문장형", True, "읽기 쉽고 번역해도 덜 깨진다"), "문장형", "<b>요즘 지침의 기본값</b>"),
    (one(txt('Export Settlements', "13px"), "제목형", None, "a · of · the 를 어떻게 할지가 또 규칙이다"), "제목형", "짧은 제목·메뉴에"),
    (one('<span style="font-size:13px;text-transform:uppercase;letter-spacing:.04em">Export settlements</span>', "대문자", False, "단어 윤곽이 사라진다"),
     "전부 대문자", "<b>읽기가 느려진다</b>"),
    (one('<span style="font-size:13px;text-transform:lowercase">Export Settlements</span>', "소문자", False, "고유명사까지 내려간다"),
     "전부 소문자", "브랜드 느낌을 노리지만 어색해진다"),
    (one(txt('EXPORT 정산 내보내기', "13px"), "섞였을 때", False, "영어만 바뀌고 한국어는 그대로"),
     "한국어와 섞으면", "<b>한 줄 안에서 결이 어긋난다</b>"),
    (one(mono('ABC', 'var(--fg)') + ' ' + '<span style="font-size:13px;font-variant-caps:all-small-caps">ABC</span>', "스몰 캡스", None, "높이를 낮춘 대문자"),
     "스몰 캡스", "약자·단위에. <b>글꼴이 지원해야</b> 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("문장형", "첫 글자만", "<b>기본으로 삼는다.</b> 번역해도 덜 깨진다"),
    ("제목형", "단어마다", "관사·전치사를 어떻게 할지 <b>규칙이 또 필요</b>하다"),
    ("전부 대문자", "윤곽이 사라짐", "글자가 다 네모가 되어 <b>단어 모양</b>으로 못 읽는다"),
    ("<code>text-transform</code>", "보이기만", "<b>값은 그대로</b>다. 복사하면 원래 글자가 나온다"),
    ("자간", "조금 벌린다", "대문자는 빽빽해 보인다 — <a href=\"../items/letterspacing.html\">자간</a>"),
    ("한국어", "구분이 없다", "<b>섞으면 결이 어긋난다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b><code>text-transform</code>은 보이기만 바꿉니다.</b>
          값은 원래 글자 그대로라서, 복사해 붙이면 소문자가 나오고
          검색도 원래 글자로 걸립니다 — 대개는 이게 좋은 일입니다.
          다만 <b>스크린 리더가 대문자를 약자로 읽어 버리는</b> 경우가 있어
          'EXPORT' 를 '이엑스피오알티'로 읽기도 합니다.
          그래서 전부 대문자가 필요하면 <b>글자는 문장형으로 쓰고
          CSS 로만 올리는</b> 쪽이 안전합니다.</p>''',
  do=ul([
    "<b>문장형</b>을 기본값으로 정해 두기",
    "짧은 레이블·메뉴에만 제목형",
    "대문자를 쓸 때는 <b>자간을 조금</b> 벌리기",
  ]),
  dont=ul([
    "본문이나 긴 제목에 전부 대문자 — <b>읽기가 느려진다</b>",
    "글자 자체를 대문자로 적기 — <b>CSS 로</b> 한다",
    "한국어와 섞인 줄에 <code>text-transform</code>을 전역으로 걸기",
    "제목형을 손으로 — 관사 규칙이 사람마다 다르다",
  ]),
  instead='강조는 <a href="../items/weight.html">글자 굵기</a>, 크기 차이는 <a href="../items/typescale.html">타입 스케일</a>, 줄 사이는 <a href="../items/lineheight.html">행간</a>.',
  cases=cases([
    (one(txt('Export settlements', "12px"), "버튼", True, "문장형"), "버튼", "<b>짧아도 문장형</b>이 안전하다"),
    (one('<span style="font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--fg-muted)">SETTLEMENTS</span>', "표 머리글", None, "작고 짧을 때만"),
     "표 머리글", "짧고 작으면 <b>대문자도 쓸 만하다</b>"),
    (one(txt('정산 내보내기', "12px"), "한국어", True, "바꿀 것이 없다"), "한국어 화면", "<b>꼴을 안 정해도 된다</b>"),
  ]),
  s8_title="최소 코드와 규칙", s8_hint="이 꼴의 계약서",
  code_lede="글자는 문장형으로 적고, 보이기만 CSS 로 올립니다.",
  code='''<span class="c">&lt;!-- 글자는 그대로 — 복사·검색이 멀쩡하다 --&gt;</span>
&lt;<span class="t">th</span> <span class="a">class</span>=<span class="s">"col"</span>&gt;Settlements&lt;/<span class="t">th</span>&gt;

.col {
  <span class="a">text-transform</span>: uppercase;
  <span class="a">letter-spacing</span>: .<span class="a">06em</span>;   <span class="c">/* 대문자는 빽빽해 보인다 */</span>
  <span class="a">font-size</span>: <span class="a">11px</span>;
}

<span class="c">/* 한국어가 섞이는 줄에는 걸지 않는다 — 영어만 바뀌어 결이 어긋난다 */</span>
.title { <span class="a">text-transform</span>: none; }''',
  keys=kbd([
    ("값은 안 바뀐다", "<code>text-transform</code>은 <b>보이기만</b>. 복사하면 원래 글자가 나온다"),
    ("약자로 읽힐 수 있다", "대문자를 <b>한 글자씩</b> 읽는 스크린 리더가 있다"),
    ("<code>capitalize</code>의 한계", "단어마다 첫 글자만 올린다. <b>관사 규칙</b>은 못 한다"),
    ("<code>font-variant-caps</code>", "스몰 캡스는 <b>글꼴이 지원해야</b> 한다. 없으면 억지로 줄인 가짜가 나온다"),
    ("한국어 줄", "바뀌는 것이 없다. <b>전역으로 걸면</b> 영어만 튄다"),
    ("번역", "영어 기준으로 꼴을 정하면 다른 말에서 <b>규칙이 다르다</b> — 독일어는 명사가 늘 대문자다"),
  ]),
  backend=rows([
    ("저장은 원래 꼴로", "화면에서 올려 보일 뿐 <b>값은 그대로</b> 둡니다. 대문자로 저장하면 되돌릴 수 없습니다."),
    ("검색·정렬", "대소문자를 무시하고 비교할지 정해 둡니다. DB 설정(collation)에 따라 다릅니다."),
    ("아이디·이메일", "대소문자를 가릴지가 <b>로그인에 영향</b>을 줍니다 — 이메일은 보통 안 가립니다."),
  ]),
  plat_lede="세 곳 모두 <b>문장형</b>으로 수렴했습니다.",
  plats=plats([
    ("웹", "text-transform",
     one(txt('Export settlements', "11px"), "", True, "", "110px"),
     "표준이 없어 팀이 정합니다. <b>문장형</b>을 기본으로 두는 곳이 많습니다."),
    ("iOS", "문장형",
     '''              <div class="phone" role="img" aria-label="iOS 문장형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:6px">Export settlements</div></div></div>''',
     "HIG 가 <b>문장형</b>을 권합니다. 예전에는 제목형이었다가 바뀌었습니다."),
    ("안드로이드", "문장형",
     '''              <div class="phone" role="img" aria-label="Material 문장형 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:6px">Export settlements</div></div></div>''',
     "M3 도 <b>문장형</b>입니다. 버튼의 대문자 관례는 M2 에서 사라졌습니다."),
  ]),
  plat_note="한국어만 쓰는 화면이라면 이 항목은 <b>신경 쓸 일이 거의 없습니다</b>. 문제는 영어가 섞일 때고, 특히 <b>버튼·표 머리글</b>처럼 두 말이 한 줄에 오는 자리입니다. 전역으로 <code>text-transform</code>을 걸어 두면 영어만 튀므로, 쓸 자리를 좁게 정해 두는 편이 낫습니다.",
  siblings=siblings("casing"),
  related='''        <li><a href="../items/letterspacing.html"><b>자간</b><em>3부</em></a></li>
        <li><a href="../items/weight.html"><b>글자 굵기</b><em>3부</em></a></li>
        <li><a href="buttontext.html"><b>버튼 문구</b><em>14부</em></a></li>
        <li><a href="koreanui.html"><b>한국어 UI</b><em>14부</em></a></li>''',
)
