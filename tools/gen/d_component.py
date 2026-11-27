# -*- coding: utf-8 -*-
from ax15 import ax
from _t15 import code, card, btn
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def inst(label="저장", tag="인스턴스", color="var(--accent)", w="152px", note="", r="6px", ok=None):
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px;justify-items:center">'
            '<span style="background:' + color + ';color:#fff;border-radius:' + r + ';padding:5px 13px;font-size:9.5px">' + label + '</span>'
            '<span style="font-family:var(--mono);font-size:8.5px;color:' + ('var(--accent)' if tag == '마스터' else ('var(--danger)' if tag == '떼어냄' else 'var(--fg-muted)')) + '">' + tag + '</span>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted);text-align:center">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">마스터 — 원본 하나. 여기만 고친다</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">인스턴스 — 복제본. 마스터를 따라간다</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">덮어쓰기 — 글자·아이콘만 바꾼다. 연결은 남는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">떼어내기(디태치) — 연결이 끊긴다. 되돌리기 어렵다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">코드로는 컴포넌트 정의와 사용</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">떼어낸 것은 눈으로 찾아야 한다</div>
                </div>
              </div>'''

D = dict(
  slug="component", ko="컴포넌트와 인스턴스", en="Component & instance",
  desc="원본 하나와 그 복제본들의 관계를 보여 주고, 덮어쓰기와 떼어내기(디태치)가 어떻게 다른지, 코드의 컴포넌트와는 어떤 점이 같은지 설명하는 항목입니다.",
  lede="컴포넌트는 <b>원본 하나</b>이고, 인스턴스는 그 원본에서 만든 <b>복제본</b>입니다. 원본을 고치면 연결된 복제본이 모두 같이 바뀐다는 점이 핵심입니다.",
  axes_lede="15부에서 다루는 현장 용어는 화면 부품의 이름 대신 디자인과 개발이 <b>함께 일하는 단계</b>를 가리킵니다. 아래 네 가지를 물어보면 이 용어들을 서로 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>맨 왼쪽이 <b>마스터</b>(원본), 나머지가 <b>인스턴스</b>(복제본)입니다.
          마스터의 글자나 모서리를 바꿔 보면 인스턴스가 모두 같이 바뀝니다.<br>
          인스턴스에서 <b>떼어내기</b>를 누르면 그 하나만 마스터와의 연결이 끊기기 때문에,
          그 뒤에 마스터를 고치면 <b>떼어낸 것만 옛 모습으로</b> 남습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "컴포넌트, 마스터, 인스턴스, 복제본, 떼어내기"),
    ("영어", "component, main component, instance, override, detach"),
    ("같이 쓰는 말",
     "원본을 <b>마스터 컴포넌트</b> 또는 <b>메인 컴포넌트</b>라고 하고, 복제본을 <b>인스턴스</b>라고 합니다. "
     "인스턴스에서 글자나 아이콘만 바꾸는 것을 <b>오버라이드</b>(덮어쓰기), "
     "마스터와의 연결을 끊는 것을 <b>디태치</b>(떼어내기)라고 부릅니다. "
     "여러 마스터를 모아 하나로 만든 것은 <b>컴포넌트 세트</b>이고, 그 안의 칸들이 <a href=\"variant.html\">배리언트</a>입니다."),
    ("자주 잘못 부르는 이름",
     "<b>컴포넌트</b> — 개발 쪽의 리액트 컴포넌트와 <b>개념은 같지만</b> 같은 물건은 아닙니다. 시안의 컴포넌트는 코드가 아니라 <b>그림</b>입니다.<br>"
     "<b>심볼</b> — 다른 도구에서 쓰던 옛 이름이고, 뜻은 컴포넌트와 같습니다.<br>"
     "<b>복사·붙여넣기</b> — 그냥 복사해 붙인 것은 마스터와 <b>연결이 없으므로</b> 인스턴스가 아닙니다."),
  ]),
  axes=ax("컴포넌트와 인스턴스"),
  oneline="<b>떼어낸 인스턴스는 떼어냈다는 표시가 남지 않습니다.</b> 그래서 급할 때 떼어낸 하나가 몇 달 뒤 마스터를 고쳤을 때 혼자 옛 모습으로 남아 있게 됩니다.",
  s4_title="연결 상태", s4_hint="마스터를 따라오나",
  states=states([
    (inst('저장', '마스터', "var(--accent)", "152px", "여기만 고친다"), "마스터", "<b>원본 하나</b>입니다. 마스터 자체는 화면에 쓰지 않기도 합니다"),
    (inst('저장', '인스턴스', "var(--accent)", "152px", "마스터를 따라간다"), "인스턴스", "마스터의 복제본입니다. 마스터를 <b>고치면 같이 바뀝니다</b>"),
    (inst('내보내기', '인스턴스 · 글자만 덮어씀', "var(--accent)", "152px", "연결은 남아 있다"),
     "덮어쓰기", "글자나 아이콘만 바꿉니다. 마스터와의 <b>연결은 그대로</b> 남습니다"),
    (inst('저장', '떼어냄', "var(--fg-muted)", "152px", "그때 모습으로 굳었다"), "떼어내기", "마스터와의 <b>연결이 끊긴 상태입니다.</b> 다시 잇기 어렵습니다"),
    (inst('저장하기', '마스터', "var(--accent)", "152px", "마스터를 고쳤다", "16px"),
     "마스터를 고치면", "연결된 인스턴스가 <b>모두 같이 바뀝니다</b>"),
    (inst('저장', '떼어냄', "var(--fg-muted)", "152px", "혼자 옛 모습으로 남았다"),
     "떼어낸 것은", "마스터를 고쳐도 <b>바뀌지 않습니다.</b> 그런 인스턴스는 눈으로 찾아야 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("마스터", "원본 하나", "고칠 때는 마스터만 고칩니다. 마스터 자체는 <b>화면에 쓰지 않기도</b> 합니다"),
    ("인스턴스", "복제본", "마스터가 바뀌면 같이 바뀝니다"),
    ("덮어쓰기", "글자 · 아이콘", "글자나 아이콘만 바꾸고 <b>연결은 남겨 둡니다.</b> 인스턴스를 고칠 때는 이렇게 쓰는 것이 정상입니다"),
    ("떼어내기", "연결 끊기", "급할 때 쓰지만, 떼어냈다는 <b>표시가 남지 않습니다</b>"),
    ("코드로는", "정의와 사용", "<code>function Button()</code>이 마스터, <code>&lt;Button /&gt;</code>이 인스턴스에 해당합니다"),
    ("찾기", "눈으로", "떼어낸 인스턴스를 <b>목록으로 뽑기 어렵습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          인스턴스를 떼어내고 싶어진다면 <b>대개 마스터에 필요한 자리가 없는 것</b>입니다.
          '이 버튼에만 아이콘을 넣고 싶은데 마스터에 아이콘 자리가 없다' 같은 때에 떼어내게 되는데,
          그럴 때 필요한 일은 떼어내기가 아니라 <b>마스터에 아이콘 자리를 추가하는</b> 것입니다.
          코드에서도 마찬가지로, 컴포넌트를 복사해 조금 고친 버전을 만드는 것보다
          <b>props를 하나 추가하는</b> 쪽이 거의 늘 낫습니다.
          이런 판단을 모아 마스터에 변형을 미리 정해 두는 것이 <a href="variant.html">배리언트</a> 설계입니다.</p>''',
  do=ul([
    "같은 모양이 <b>여러 번</b> 나올 때",
    "나중에 <b>한꺼번에 고칠</b> 일이 있을 때",
    "<b>덮어쓰기</b>로 되는 범위까지만 바꿀 때",
  ]),
  dont=ul([
    "급하다고 <b>떼어낼</b> 때. 떼어냈다는 표시가 남지 않습니다",
    "복사·붙여넣기로 개수를 늘릴 때. 복사본은 마스터와 <b>연결이 없습니다</b>",
    "한 번만 쓰는 것을 컴포넌트로 만들 때. 쓰는 곳에 비해 <b>일이 과합니다</b>",
    "마스터를 <b>화면 안에</b> 그대로 쓸 때. 화면을 고치다가 마스터까지 실수로 고치게 됩니다",
  ]),
  instead='변형이 여럿이면 <a href="variant.html">배리언트</a>, 값이 흩어지면 <a href="designsystem.html">디자인 시스템</a>의 토큰, 배치는 <a href="autolayout.html">오토 레이아웃</a>.',
  cases=cases([
    (inst('저장', '마스터', "var(--accent)", "150px", "따로 모아 둔다"), "마스터 모음", "마스터는 <b>화면과 떨어진 자리</b>에 모아 둡니다"),
    (inst('내보내기', '덮어씀', "var(--accent)", "150px", "글자만 바꿨다"), "정상적인 쓰임", "글자만 덮어쓰고 마스터와의 <b>연결은 유지</b>합니다"),
    (inst('저장', '떼어냄', "var(--fg-muted)", "150px", "급해서 떼어냈다"), "흔한 사고", "급해서 떼어낸 것이 <b>몇 달 뒤</b> 마스터를 고칠 때 드러납니다"),
  ]),
  s8_title="코드와 맞춰 보기", s8_hint="시안과 코드의 짝",
  code_lede="시안의 마스터와 인스턴스는 코드에서 컴포넌트를 <b>정의하는 곳과 쓰는 곳</b>에 해당합니다.",
  code='''<span class="c">// 마스터 = 컴포넌트 정의 — 한 곳에만 있다</span>
<span class="k">function</span> Button({ label, tone = <span class="s">'primary'</span>, size = <span class="s">'md'</span> }) {
  <span class="k">return</span> &lt;<span class="t">button</span> <span class="a">className</span>={<span class="s">`btn btn--${</span>tone<span class="s">} btn--${</span>size<span class="s">}`</span>}&gt;{label}&lt;/<span class="t">button</span>&gt;;
}

<span class="c">// 인스턴스 = 쓰는 곳 — 덮어쓰기는 props 로</span>
&lt;<span class="t">Button</span> <span class="a">label</span>=<span class="s">"내보내기"</span> /&gt;
&lt;<span class="t">Button</span> <span class="a">label</span>=<span class="s">"삭제"</span> <span class="a">tone</span>=<span class="s">"danger"</span> /&gt;

<span class="c">// ✕ 떼어내기에 해당하는 코드 — 복사해서 조금 고친 것</span>
<span class="k">function</span> ButtonWithIcon({ label }) {     <span class="c">// 마스터와 멀어진다</span>
  <span class="k">return</span> &lt;<span class="t">button</span> <span class="a">className</span>=<span class="s">"btn btn--primary"</span>&gt;◆ {label}&lt;/<span class="t">button</span>&gt;;
}''',
  keys=kbd([
    ("마스터는 <b>한 곳</b>에", "화면 안에 두면 화면을 고치다 <b>마스터까지 고치기 쉬우므로</b> 따로 모아 둡니다"),
    ("덮어쓰기는 <b>props</b>", "글자와 아이콘, 상태는 props로 바꿉니다. 모양 자체를 바꾸려면 마스터를 고칩니다"),
    ("접근성도 마스터에", "<code>role</code>·<code>aria-*</code>·키보드 동작을 마스터에 넣어 두면 인스턴스를 쓰는 쪽은 <b>따로 손대지 않아도</b> 접근성을 갖추게 됩니다"),
    ("떼어내면 <b>그것도 끊긴다</b>", "떼어낸 때의 접근성 속성이 그대로 남아서, 마스터에서 고친 접근성이 반영되지 않습니다"),
    ("이름을 쓰임으로", "<code>Button/Primary</code>보다 <code>Button/주동작</code>처럼 <b>언제 쓰는지</b>가 드러나게 짓습니다"),
    ("찾기", "코드에서는 <b>검색으로</b> 쓰인 곳을 모두 찾을 수 있지만, 시안에서는 찾기 어렵습니다"),
  ]),
  backend=rows([
    ("부품 묶음에 버전", "마스터를 고치면 그 부품을 쓰는 화면이 모두 바뀌므로, 배포할 때 <b>무엇이 바뀌는지</b> 적어 함께 내보냅니다."),
    ("쓰인 곳 세기", "코드에서는 부품이 쓰인 곳을 검색으로 셀 수 있으니, 세어 보고 <b>쓰이지 않는 부품</b>은 지웁니다."),
    ("복사된 부품 찾기", "<code>btn-primary-2</code>처럼 비슷한 클래스 이름을 찾아보면 부품을 복사해 고친 곳, 곧 시안의 <b>떼어낸 자리</b>에 해당하는 곳이 드러납니다."),
  ]),
  plat_lede="플랫폼마다 부르는 이름은 다르지만 <b>원본 하나를 정의해 여러 곳에서 쓰는 개념은 같습니다</b>.",
  plats=plats([
    ("웹", "컴포넌트",
     inst('저장', '정의 / 사용', "var(--accent)", "110px"),
     "<code>function Button()</code>으로 정의하고 <code>&lt;Button /&gt;</code>으로 씁니다. 시안의 마스터, 인스턴스와 <b>그대로 짝이 맞습니다</b>."),
    ("iOS", "SwiftUI View",
     '''              <div class="phone" role="img" aria-label="iOS 컴포넌트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">struct PrimaryButton: View</div></div></div>''',
     "<code>View</code> 하나가 컴포넌트 하나이고, 쓰는 쪽에서는 <b>값만 넘깁니다</b>."),
    ("안드로이드", "Composable",
     '''              <div class="phone" role="img" aria-label="안드로이드 컴포넌트 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;top:30px;font-size:5px;color:var(--fg-muted)">@Composable fun PrimaryButton()</div></div></div>''',
     "<code>@Composable</code> 함수가 컴포넌트 역할을 합니다."),
  ]),
  plat_note="시안에서 <b>떼어낸 부품</b>과 코드에서 <b>복사해 고친 컴포넌트</b>는 같은 문제를 일으킵니다. 둘 다 그때는 가장 빨리 끝나는 방법이지만, 몇 달 뒤 원본을 고칠 때 그것만 바뀌지 않고 남습니다. \"이거 떼어낸 건가요\"와 \"이거 복사한 건가요\"는 같은 질문이고, 둘 다 <b>원본에 자리를 하나 더 만들어 두면</b> 하지 않아도 되는 일입니다.",
  siblings=siblings("component"),
  related='''        <li><a href="variant.html"><b>배리언트와 프롭</b><em>15부</em></a></li>
        <li><a href="designsystem.html"><b>디자인 시스템</b><em>15부</em></a></li>
        <li><a href="autolayout.html"><b>오토 레이아웃</b><em>15부</em></a></li>
        <li><a href="handoff.html"><b>핸드오프</b><em>15부</em></a></li>''',
)
