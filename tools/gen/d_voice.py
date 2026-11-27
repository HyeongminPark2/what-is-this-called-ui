# -*- coding: utf-8 -*-
from ax14 import ax
from _t14 import ba, one, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def scr(lines, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    body = ''.join('<div style="display:grid;gap:1px"><span style="font-size:8px;color:var(--fg-muted)">' + a + '</span>'
                   '<span style="font-size:9.5px;line-height:1.5">' + b + '</span></div>' for a, b in lines)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:5px">'
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:' + (col if ok is not None else 'var(--fg-muted)') + '">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">합쇼체 — 저장되었습니다. 격식 있고 거리가 있다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">해요체 — 저장했어요. 부드럽고 짧다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">반말 — 저장했어. 화면 전체에 쓸 때만</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">버튼은 말투를 안 탄다 — ‘저장’</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">돈 · 약관 · 사과는 한 단계 올리기도 한다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">한 화면에 두 말투 — 여러 사람이 쓴 티가 난다</div>
                </div>
              </div>'''

D = dict(
  slug="voice", ko="말투와 높임", en="Voice & tone",
  desc="화면 문구의 말투를 합쇼체·해요체·반말 가운데 하나로 정하는 방법을 다룹니다. 말투가 섞이면 여러 사람이 따로 쓴 것처럼 보입니다.",
  lede="어느 말투를 고르든 정답은 없고, 중요한 것은 <b>하나로 정해 지키는 것</b>입니다. 화면마다 말투가 섞이면 여러 사람이 따로 쓴 티가 납니다.",
  axes_lede="화면에 적는 문구는 사용자가 <b>무엇을 하면 되는지</b> 알려 주려고 씁니다. 아래 네 가지를 물어보면 문구마다 알려야 할 것과 자주 틀리는 곳, 고치는 기준이 드러납니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>같은 화면을 세 가지 말투로 써 보았습니다.<br>
          <b>화면마다 다르게 쓰기</b>를 켜면 한 화면 안에서 말투가 섞입니다. 문구를 하나씩 따로 보면 모두 문제없지만,
          한데 모아 놓으면 <b>여러 사람이 쓴 것</b>처럼 보입니다. 실제로 화면 문구는 여러 사람이 나눠 쓰기 때문에 이런 일이 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "말투, 어조, 높임말, 경어체, 문체"),
    ("영어", "voice and tone, microcopy style, writing guidelines"),
    ("같이 쓰는 말",
     "'-습니다'로 끝나는 말투가 <b>합쇼체</b>, '-요'로 끝나는 말투가 <b>해요체</b>입니다. "
     "제품 문구 전체에 늘 유지하는 성격은 <b>보이스</b>(voice), 상황에 따라 달라지는 말의 느낌은 <b>톤</b>(tone)이라고 나눠 부릅니다. "
     "이런 규칙을 적어 둔 문서를 <b>라이팅 가이드</b>·<b>보이스 앤 톤 가이드</b>라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>브랜드 톤</b> — 광고의 말투까지 아우르는 넓은 말입니다. 화면 안 문구는 광고 문구보다 <b>더 짧고 기능적</b>이어야 합니다.<br>"
     "<b>번역투</b> — <a href=\"koreanui.html\">한국어 UI</a>는 번역투처럼 <b>틀린 말</b>을 고치는 일이고, 말투는 여러 바른 말투 가운데 하나를 <b>고르는</b> 일입니다.<br>"
     "<b>친근함</b> — 반말을 쓴다고 해서 친근하게 느껴지지는 않습니다. 특히 <b>사과할 때</b> 반말을 쓰면 가벼워 보입니다."),
  ]),
  axes=ax("말투와 높임"),
  oneline="<b>말투를 정하고 문서로 적어 두세요.</b> 적어 두지 않으면 문구를 쓰는 사람이 바뀔 때마다 화면의 말투도 바뀝니다.",
  s4_title="말투별로", s4_hint="같은 화면, 다른 말투",
  states=states([
    (scr([('안내', '변경 사항이 저장되었습니다.'), ('오류', '정산을 저장하지 못했습니다. 잠시 후 다시 시도해 주십시오.')],
         "152px", "격식 있고 거리가 있다"),
     "합쇼체", "<b>은행·보험·공공</b> 서비스에서 많이 씁니다"),
    (scr([('안내', '바뀐 내용을 저장했어요.'), ('오류', '정산을 저장하지 못했어요. 잠시 뒤 다시 해 주세요.')],
         "152px", "부드럽고 짧다", True),
     "해요체", "요즘 서비스가 <b>기본값</b>으로 많이 쓰는 말투입니다"),
    (scr([('안내', '저장했어'), ('오류', '저장 실패. 좀 있다 다시 해')],
         "152px", "사과할 때 가벼워 보인다"),
     "반말", "반말을 쓰려면 <b>화면 전체에</b> 똑같이 써야 합니다"),
    (scr([('안내', '바뀐 내용을 저장했어요.'), ('오류', '정산을 저장하지 못했습니다. 잠시 후 다시 시도해 주십시오.')],
         "152px", "돈·사과만 한 단계 올렸다"),
     "섞되 규칙 있게", "돈이나 사과처럼 <b>책임이 걸린 말</b>만 높임 단계를 올리는 방식입니다"),
    (scr([('안내', '저장되었습니다.'), ('오류', '저장 실패했어'), ('빈 상태', '등록된 가맹점이 없습니다.')],
         "152px", "규칙 없이 섞였다", False),
     "그냥 섞임", "<b>여러 사람이 쓴 티</b>가 납니다"),
    (scr([('버튼', '저장'), ('버튼', '삭제')], "152px", "버튼은 말투를 안 탄다"),
     "버튼", "<a href=\"buttontext.html\">버튼 문구</a>는 <b>동사 하나</b>로 끝나서 말투가 드러나지 않습니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("합쇼체", "-습니다", "격식이 있지만 문장이 <b>길어지기</b> 쉽습니다"),
    ("해요체", "-요", "짧고 부드러워서 <b>요즘 기본값</b>으로 많이 씁니다"),
    ("반말", "-어 / -해", "쓰려면 화면 <b>전부</b>에 써야 하고, 사과할 때는 가벼워 보입니다"),
    ("버튼", "말투 없음", "<b>동사 하나</b>로 끝나서 어느 말투에서도 같습니다"),
    ("예외", "돈 · 약관 · 사과", "해요체를 쓰는 제품도 이런 문구는 <b>한 단계 올려</b> 씁니다"),
    ("섞임", "두 말투", "<b>여러 사람이 쓴 티</b>가 나는, 가장 흔한 실수입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>말투는 따로 관리하지 않으면 저절로 섞입니다.</b>
          화면 문구는 기획자·디자이너·개발자가 각자 쓰고,
          오류 문구는 서버에서 오고, 약관은 법무 쪽에서 오기 때문입니다.
          아무도 틀리게 쓰지 않았는데도 모아 놓으면 말투가 네 가지가 됩니다.
          그래서 말투를 맞추는 일은 <b>글을 잘 쓰는 문제</b>라기보다
          <b>규칙을 어디에 적어 두고 누가 지키느냐</b>의 문제입니다.
          한 장짜리 규칙이라도 저장소에 있으면 새로 온 사람이 그 규칙을 따라 씁니다.</p>''',
  do=ul([
    "말투를 <b>하나로 정하고 한 장짜리 문서로 적어 두기</b>",
    "돈·사과·약관은 <b>규칙을 따로</b> 두기",
    "서버 문구도 <b>같은 규칙</b>으로 쓰기",
  ]),
  dont=ul([
    "화면마다 말투가 다를 때. <b>여러 사람이 쓴 티</b>가 납니다",
    "사과하면서 반말을 쓸 때. <b>가벼워 보입니다</b>",
    "‘앗!’·‘이런!’처럼 친근함을 과장할 때. <b>실패했을 때</b> 이런 말을 보면 사용자가 더 언짢아집니다",
    "말투만 정하고 <b>적어 두지 않을 때</b>",
  ]),
  instead='번역투를 걷는 것은 <a href="koreanui.html">한국어 UI</a>, 버튼은 <a href="buttontext.html">버튼 문구</a>, 실패했을 때는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (scr([('해요체', '바뀐 내용을 저장했어요.')], "150px"), "보통 안내", "<b>짧고 부드럽게</b> 씁니다"),
    (scr([('합쇼체', '결제가 완료되었습니다.'), ('합쇼체', '영수증을 메일로 보내 드렸습니다.')], "150px"),
     "돈 얘기", "해요체를 쓰는 제품도 돈 이야기는 <b>한 단계 올려</b> 씁니다"),
    (scr([('사과', '저희 쪽 문제로 저장하지 못했습니다.')], "150px"),
     "우리 잘못", "사과는 <b>짧게 한 번</b>만 하고 길게 늘이지 않습니다"),
  ]),
  s8_title="적어 두는 법", s8_hint="한 장짜리 규칙 문서",
  code_lede="말투 규칙은 코드가 아니라 <b>문서와 문구 파일</b>에 적어 둡니다.",
  code='''<span class="c"># 라이팅 규칙 (한 장이면 된다)</span>

기본: 해요체. 짧게, 사용자가 주어.
  ○ 바뀐 내용을 저장했어요.
  ✕ 변경 사항이 성공적으로 저장되었습니다.

예외: 돈 · 약관 · 우리 잘못은 합쇼체.
  ○ 결제가 완료되었습니다.
  ○ 저희 쪽 문제로 저장하지 못했습니다.

버튼: 동사 한두 어절. 마침표 없음.
  ○ 저장 · 내보내기 · 가맹점 삭제
  ✕ 확인 · 제출

금지: ‘성공적으로’ · ‘당신의’ · ‘~하시겠습니까’ · ‘앗!’

<span class="c">// 문구는 코드에 박지 않고 한곳에 모은다</span>
<span class="s">"store.delete.confirm"</span>: <span class="s">"‘{name}’을(를) 지울까요?"</span>''',
  keys=kbd([
    ("규칙을 <b>저장소 안에</b>", "위키보다 코드 옆에 두어야 <b>새로 온 사람도 보게</b> 됩니다"),
    ("보기를 함께 적는다", "'짧게 쓰세요' 같은 설명보다 <b>○ / ✕ 보기 한 쌍</b>을 적어 두는 편이 훨씬 잘 지켜집니다"),
    ("금지어 목록", "'성공적으로'·'당신의' 같은 금지어는 <b>검색으로 찾아낼 수</b> 있어서 실제로 지키기 쉽습니다"),
    ("문구를 한곳에", "문구가 코드 곳곳에 흩어져 있으면 어떤 말투가 몇 개인지 <b>세어 볼 수도</b> 없습니다"),
    ("스크린 리더", "말투가 달라도 스크린 리더가 전하는 내용은 같고, <b>읽는 길이</b>만 달라집니다"),
    ("번역", "해요체·합쇼체 같은 구분은 <b>영어에 없으므로</b> 영어 원문만 보고는 정할 수 없습니다"),
  ]),
  backend=rows([
    ("서버 문구도 규칙을 따른다", "서버가 보낸 <code>message</code>를 그대로 띄우면 화면 문구와 <b>말투가 섞입니다</b>. 오류 코드로 분기해서 화면 쪽에서 문구를 쓰는 편이 낫습니다."),
    ("외부에서 온 문구", "결제사나 배송사가 보내 주는 문장은 우리 화면과 말투가 다르므로, <b>우리 말투로 바꿔</b> 보여 줍니다."),
    ("메일·푸시도 같은 규칙", "화면은 해요체인데 메일만 합쇼체이면, 사용자에게는 <b>다른 회사</b>가 보낸 것처럼 보입니다."),
  ]),
  plat_lede="말투의 <b>높임 단계</b>를 정해야 하는 것은 한국어·일본어 같은 언어에만 있는 문제입니다.",
  plats=plats([
    ("웹", "팀이 정한다",
     scr([('안내', '저장했어요.')], "110px"),
     "따를 표준이 없어서 팀이 규칙을 <b>적어 두지 않으면</b> 반드시 섞입니다."),
    ("iOS", "HIG 라이팅",
     '''              <div class="phone" role="img" aria-label="iOS 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">저장했어요.</div></div></div>''',
     "영어로 쓴 지침은 <b>간결하게, 사용자 중심으로</b> 쓰라고 권할 뿐 높임 단계는 다루지 않습니다."),
    ("안드로이드", "Material 라이팅",
     '''              <div class="phone" role="img" aria-label="안드로이드 문구 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:32px;font-size:6px">저장했어요.</div></div></div>''',
     "Material 지침도 <b>짧고 분명하게</b> 쓰라고 권합니다. 한국어의 높임 단계는 <b>우리가 정해야</b> 합니다."),
  ]),
  plat_note="말투 정리는 <b>'나중에 한 번 훑으면 되는 일'</b>로 미뤄지다가 끝내 하지 못하는 경우가 많습니다. 말투를 맞추는 데 품이 가장 적게 드는 때는 <b>문구를 처음 쓸 때</b>입니다. 이때 필요한 것은 긴 가이드가 아니라 <b>○ / ✕ 보기를 한 쌍씩 적은 한 장짜리 문서</b>이고, 이 문서가 저장소에 있으면 새로 들어온 사람도 같은 말투로 씁니다.",
  siblings=siblings("voice"),
  related='''        <li><a href="koreanui.html"><b>한국어 UI</b><em>14부</em></a></li>
        <li><a href="buttontext.html"><b>버튼 문구</b><em>14부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>
        <li><a href="emptytext.html"><b>빈 상태 문구</b><em>14부</em></a></li>''',
)
