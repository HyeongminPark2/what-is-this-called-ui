# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

LEVELS = table(
  ["무엇이 실패했나", "어디에 붙나", "사용자가 할 수 있는 일", "나머지 화면"],
  [["칸 하나", "입력값 하나가 규칙에 안 맞다", "<b>그 칸 바로 아래</b>", "고쳐서 다시 보낸다", "그대로 쓴다"],
   ["폼 전체", "보내기 자체가 실패했다", "<b>폼 맨 위</b>", "다시 시도하거나 나중에", "입력값은 지키고 그대로"],
   ["화면 전체", "화면을 못 그린다", "<b>화면 한가운데</b>", "다시 불러오거나 돌아간다", "쓸 수 없다"],
   ["연결 끊김", "서버에 닿지 못한다", "<b>앱 꼭대기 띠</b>", "기다리거나 오프라인으로 쓴다", "읽기는 되게 둔다"]])

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:12px">
                <div data-pin="1" style="background:color-mix(in srgb,var(--danger) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--danger) 40%,transparent);border-radius:8px;padding:14px 26px 16px">
                  <span class="pin-tr" data-pin="2" style="display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--danger);color:#fff;font-size:12px;font-weight:800;margin-bottom:14px">!</span>
                  <div class="pin-out" data-pin="3" style="font-size:12px;font-weight:750;margin-bottom:14px">등록하지 못했습니다</div>
                  <div class="pin-out" data-pin="4" style="font-size:11px;color:var(--fg-muted);line-height:1.65;margin-bottom:18px">은행 점검 시간(02:00~04:00)에는<br>계좌를 확인할 수 없습니다.</div>
                  <div style="display:flex;gap:40px;align-items:center">
                    <span data-pin="5" style="background:var(--accent);color:#fff;border-radius:5px;padding:5px 12px;font-size:10.5px;font-weight:700">다시 시도</span>
                    <span class="pin-out" data-pin="6" style="font-size:10px;color:var(--fg-faint)">오류 a4f21c</span>
                  </div>
                </div>
              </div>'''

D = dict(
  slug="error", ko="에러 상태", en="Error state",
  desc="에러 상태가 무엇인지, 칸·폼·화면·연결 네 단계가 서로 어떻게 다른지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="에러 상태는 사용자가 하려던 일이 <b>실패했다는 것</b>과 <b>이제 무엇을 하면 되는지</b>를 알리는 화면입니다. 에러를 어디에 붙이느냐에 따라 네 단계로 나뉩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>네 단계를 번갈아 눌러 보세요.</b> 같은 실패라도 단계마다 에러가 붙는 자리가 다릅니다.
          <b>단계가 올라갈수록 사용자가 할 수 있는 일은 줄어듭니다.</b> 예를 들어 칸 하나에 붙은 에러는 그 칸을 고쳐서 바로 다시 보내면 되지만,
          화면 전체에 띄운 에러 앞에서는 '다시 불러오기'밖에 할 수 없습니다. 그래서 꼭 필요하지 않으면 에러의 단계를 올리지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "에러 상태, 오류 상태, 오류 화면"),
    ("영어", "error state, error message, inline error, error page"),
    ("같이 쓰는 말", "입력 칸 아래 붙는 에러는 <b>인라인 에러</b>, 폼 위에 뜨는 상자는 <b>얼럿</b>이나 <b>배너</b>, 화면 전체를 덮는 에러는 <b>에러 페이지</b>(404·500)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>얼럿</b> — 웹에서 얼럿은 <code>alert()</code> 창을 가리키기도 하고 인라인 경고 상자를 가리키기도 해서, 모달과 혼동하기 쉽습니다.<br>"
     "<b>토스트</b> — 에러를 토스트로만 알리면 <b>토스트가 금방 사라져서 사용자가 다 읽지 못합니다.</b> 사용자가 고쳐야 하는 에러는 화면에 남아 있어야 합니다.<br>"
     "<b>빈 상태</b> — 비어 있다고 해서 무언가 잘못된 것은 아니므로 빈 상태는 빨갛게 칠하지 않습니다."),
  ]),
  axes=LEVELS,
  oneline="에러는 사용자가 <b>문제를 고칠 수 있는 가장 가까운 자리</b>에 붙입니다. 꼭 필요하지 않으면 에러의 단계를 올리지 않습니다.",
  states=states([
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">자릿수가 모자랍니다</div></div>', bars="4", label="칸 하나 에러"), "칸 하나", "틀린 칸 바로 아래에 붙이고, <b>무엇이 틀렸고 어떻게 고치는지</b>까지 적습니다"),
    (mini('<div style="margin-top:7px;padding:0 6px"><div style="border:1px solid color-mix(in srgb,var(--danger) 45%,transparent);background:color-mix(in srgb,var(--danger) 8%,var(--surface));border-radius:3px;padding:4px 5px"><div style="font-size:7px;font-weight:700">등록하지 못했습니다</div><div style="font-size:6px;color:var(--fg-muted)">잠시 뒤 다시 해 주세요</div></div><div style="height:9px;border:1px solid var(--line-strong);border-radius:3px;margin-top:5px"></div></div>', bars="", label="폼 전체 에러"), "폼 전체", "폼 맨 위에 띄웁니다. <b>사용자가 입력한 값은 지우지 말고 그대로 둡니다</b>"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;text-align:center;padding:8px"><span style="font-size:14px;font-weight:800;color:var(--fg-faint);letter-spacing:-.04em">500</span><span style="font-size:7.5px;font-weight:700">화면을 열지 못했습니다</span><span class="mini__btn" style="font-size:7px;padding:2px 6px">다시 불러오기</span></div>', bars="", label="화면 전체 에러"), "화면 전체", "사용자가 할 수 있는 일이 거의 없으므로 <b>이전 화면으로 돌아가는 방법</b>을 꼭 둡니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--ink-900);color:#fff;font-size:6.5px;padding:3px 5px">연결이 끊겼습니다 · 다시 시도 중…</div><div class="mini__bg" style="padding-top:16px;opacity:.6"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="연결 끊김 띠"), "연결 끊김", "앱 꼭대기에 띠를 띄웁니다. <b>읽기는 그대로 되게</b> 두고 쓰기만 막습니다"),
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--warn);border-radius:3px"></div><div style="font-size:6.5px;color:var(--warn);font-weight:700;margin-top:3px">이 계좌는 이미 등록돼 있습니다</div></div>', bars="4", label="경고 수준"), "경고", "틀린 것은 아니지만 사용자가 한 번 확인할 내용입니다. <b>빨강을 아껴 써야</b> 진짜 에러에 쓴 빨강이 눈에 띕니다"),
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid #1f8a4c;border-radius:3px"></div><div style="font-size:6.5px;color:#1f8a4c;font-weight:700;margin-top:3px">✓ 확인했습니다</div></div>', bars="4", label="고친 뒤"), "고친 뒤", "값을 고치면 에러를 <b>즉시</b> 풀어 줍니다. 다시 보내야만 풀리면 사용자가 답답해합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("경고 상자", "alert · callout", "빨강은 <b>진행이 정말 막혔을 때</b>만 씁니다. 빨강을 아무 데나 쓰면 정작 중요한 에러가 눈에 들어오지 않습니다"),
    ("아이콘", "icon", "색만으로 에러를 알리지 않으려고 둡니다. 색각 이상인 사람은 색 대신 아이콘을 보고 에러임을 알아챕니다"),
    ("무엇이 안 됐나", "title", "<b>사용자가 쓰는 말로</b> 적습니다. '요청 실패'가 아니라 '등록하지 못했습니다'처럼 씁니다"),
    ("왜 · 어떻게", "description", "원인과 <b>다음에 할 일</b>을 함께 적습니다. 둘 중 하나만 있으면 사용자가 상황을 이해하거나 해결하기 어렵습니다"),
    ("다시 할 길", "retry · action", "에러 화면에서 특히 중요한 요소입니다. 다시 할 방법이 없으면 사용자는 그 화면에서 더 할 수 있는 일이 없습니다"),
    ("오류 번호", "error code", "고객센터에 문의할 때 씁니다. 사용자에게는 의미 없는 글자지만 <b>고객센터는 이 번호로 어떤 요청이 실패했는지 찾습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          에러 화면에 적지 말아야 할 것도 있습니다. <b>스택 트레이스와 내부 주소, SQL</b>은 사용자에게는 쓸모가 없지만
          공격자에게는 시스템 구조를 알려 주는 정보가 됩니다. 자세한 내용은 서버 로그에 남기고, 화면에는 그 로그를 찾을 수 있는 오류 번호만 적습니다.</p>''',
  do=ul([
    "사용자가 고칠 수 있는 <b>가장 가까운 자리</b>에 붙일 때",
    "다시 시도, 돌아가기, 문의하기처럼 <b>다시 할 방법</b>을 함께 줄 때",
    "'은행 점검 시간입니다'처럼 원인을 사용자가 쓰는 말로 적을 때",
  ]),
  dont=ul([
    "에러를 토스트로만 알릴 때. 토스트가 금방 사라져서 다 읽지 못합니다",
    "폼 전송이 실패했는데 <b>입력값을 지울 때</b>. 사용자가 처음부터 다시 입력해야 해서 가장 불만이 많은 처리입니다",
    "\"오류가 발생했습니다\"만 적을 때. 사용자가 무엇을 해야 하는지 알 수 없습니다",
    "스택 트레이스나 내부 주소를 보여 줄 때. 사용자에게는 쓸모가 없고 보안상 위험합니다",
    "빨강을 아무 데나 쓸 때. 정작 중요한 에러의 빨강이 눈에 띄지 않게 됩니다",
  ]),
  instead='알려만 주면 되면 <a href="toast.html">토스트</a>, 답을 꼭 받아야 하면 <a href="modal.html">모달</a>, 아직 불러오는 중이면 <a href="spinner.html">스피너</a>, 원래 없는 것이면 <a href="empty.html">빈 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">계좌번호</div><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">11~12자리입니다</div></div>', bars="", tall=False, label="인라인 에러 재현"),
     "인라인 에러", "에러를 알리는 방법 가운데 가장 낫습니다. 고칠 곳 바로 옆에 붙고, 나머지 화면은 그대로 쓸 수 있기 때문입니다"),
    (mini('<div style="margin-top:7px;padding:0 6px"><div style="border:1px solid color-mix(in srgb,var(--danger) 45%,transparent);background:color-mix(in srgb,var(--danger) 8%,var(--surface));border-radius:3px;padding:4px 5px"><div style="font-size:7px;font-weight:700">보내지 못했습니다</div><div style="font-size:6px;color:var(--accent);font-weight:700;margin-top:2px">다시 시도</div></div></div>', bars="4", tall=False, label="폼 위 경고 재현"),
     "폼 위 경고", "칸은 모두 맞게 채웠는데 보내기가 실패했을 때 씁니다. 입력값은 그대로 둡니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--ink-900);color:#fff;font-size:6.5px;padding:3px 5px;display:flex;gap:4px"><span style="width:4px;height:4px;border-radius:50%;background:#e0a800;margin-top:3px"></span><span>연결이 끊겼습니다</span></div><div class="mini__bg" style="padding-top:16px;opacity:.6"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="오프라인 띠 재현"),
     "연결 끊김 띠", "화면 전체를 막지 않고, 이미 불러온 내용은 계속 읽을 수 있게 둡니다"),
  ]),
  code_lede="구현에서 중요한 것은 에러 설명을 <b>해당 입력 칸과 연결해 두는 것</b>입니다. 색만으로 에러를 알리면 스크린 리더 사용자와 색각 이상인 사람은 에러가 났다는 것을 알 수 없습니다.",
  code='''<span class="c">&lt;!-- 칸과 설명을 이어 둔다. 색만으로는 안 된다 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"acct"</span> <span class="a">aria-invalid</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"e1"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"e1"</span> <span class="a">class</span>=<span class="s">"field-err"</span>&gt;자릿수가 모자랍니다. 11~12자리입니다.&lt;/<span class="t">p</span>&gt;

<span class="c">&lt;!-- 폼 전체 실패는 읽던 말을 끊고 알린다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;등록하지 못했습니다…&lt;/<span class="t">div</span>&gt;

<span class="c">// 다시 보낼 때까지 기다리지 말고 고쳐지는 즉시 풀어 준다</span>
input.addEventListener(<span class="s">'input'</span>, () =&gt; <span class="a">{</span>
  <span class="a">if</span> (valid(input.value)) clearError(input);
<span class="a">}</span>);

<span class="c">// 사용자에게는 번호만, 자세한 것은 로그로</span>
log.error(<span class="a">{</span> id: <span class="s">'a4f21c'</span>, err <span class="a">}</span>);''',
  keys=kbd([
    ("보낼 때", "<b>첫 번째 틀린 칸으로 포커스를 옮깁니다.</b> 그래야 사용자가 어디가 틀렸는지 찾아 헤매지 않습니다"),
    ("<code>aria-invalid</code>", "틀린 칸에 <code>true</code>로 겁니다. 에러 설명은 <code>aria-describedby</code>로 칸과 연결합니다"),
    ("<code>role=\"alert\"</code>", "폼 전체 실패처럼 <b>지금 바로 알려야 하는 것</b>에만 씁니다. 칸 하나의 에러에는 쓰지 않습니다"),
    ("고쳐질 때", "다시 보낼 때까지 기다리지 말고 <b>입력하는 도중에</b> 풀어 줍니다"),
    ("색", "빨강만으로 알리지 않고 아이콘과 글자를 함께 둡니다"),
  ]),
  backend=rows([
    ("단계 = 실패한 층", "검증 실패(<code>400</code>)는 칸에, 일시적 실패(<code>503</code>)는 폼 위에, 렌더 실패(<code>500</code>)는 화면 전체에, 연결 실패는 꼭대기 띠에 표시합니다. <b>서버 응답의 종류에 따라 에러를 보여 줄 단계가 정해지는 셈입니다.</b>"),
    ("필드 단위 에러를 내려 준다", "에러를 <code>{ field: 'account', message: '…' }</code> 형태로 내려 주면 화면에서 해당 칸에 붙일 수 있습니다. 에러 문장 하나만 내려 주면 어느 칸의 문제인지 알 수 없어 폼 위에 띄울 수밖에 없습니다."),
    ("다시 시도 = 멱등성", "'다시 시도'를 누르면 같은 요청이 한 번 더 서버로 가는데, 멱등 키가 없으면 같은 내용이 두 번 등록될 수 있습니다. <b>그래서 다시 시도 버튼을 두려면 서버도 같은 요청을 한 번만 처리하도록 설계해야 합니다.</b>"),
    ("오류 번호 = 상관관계 ID", "요청마다 ID를 붙여 응답과 로그에 함께 남깁니다. 그러면 사용자가 'a4f21c'라는 번호만 알려 줘도 로그에서 그 요청을 찾아낼 수 있습니다."),
    ("노출 범위", "스택 트레이스와 내부 주소를 보여 주면 공격자가 시스템 구조를 파악할 수 있습니다. 바깥으로는 오류 번호만 내보내고, 자세한 내용은 모두 내부 로그에 남깁니다."),
  ]),
  plat_lede="에러를 네 단계로 나누는 틀은 플랫폼마다 비슷하고, 부르는 이름과 쓰는 부품만 다릅니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">자릿수가 모자랍니다</div></div>', bars="4", label="웹 인라인 에러 재현"),
     "<b>인라인 에러</b> · 칸 아래에 붙이는 것이 기본이고, 화면 전체 에러는 <b>에러 페이지</b>(404·500)로 따로 다룹니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-alert"><div class="ios-alert__box"><div><b>등록하지 못했습니다</b><p>잠시 뒤 다시 해 주세요.</p></div><div class="ios-alert__btns"><span>취소</span><span>다시 시도</span></div></div></div>', "iOS 얼럿 재현"),
     "에러를 <b>얼럿</b>으로 띄우는 관례가 강합니다. 폼 안의 에러는 <b>칸 아래 빨간 글씨</b>로 두며, 지침은 '<b>사용자가 무엇을 하면 되는지 알려 주라</b>'는 점을 특히 강조합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><div style="height:14px;border:1px solid var(--danger);border-radius:4px"></div><div style="font-size:7px;color:var(--danger);margin-top:3px">자릿수가 모자랍니다</div></div><div style="position:absolute;left:6px;right:6px;bottom:10px;background:#2e3238;border-radius:5px;padding:5px 7px;font-size:7.5px;color:#fff">보내지 못했습니다</div>', "안드로이드 에러 재현"),
     "칸 아래의 <b>서포팅 텍스트</b>(supporting text)가 에러일 때 빨갛게 바뀌는 구조입니다. 일시적인 실패는 <b>스낵바</b>로 알리는 것이 관례입니다."),
  ]),
  plat_note="\"에러 띄워 주세요\"라는 요청에는 <b>네 단계 가운데 어느 것인지</b>가 빠져 있습니다. 요청대로만 만들면 대개 가장 만들기 쉬운 토스트를 쓰게 되는데, 토스트는 <b>금방 사라져서 사용자가 다 읽지 못합니다.</b> 사용자가 고쳐야 하는 에러는 화면에 남아 있어야 합니다.",
  siblings=siblings("error"),
  related='''        <li><span class="na"><b>에러 메시지 문구</b><em>14부</em></span></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>
        <li><span class="na"><b>라이브 리전</b><em>12부</em></span></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>''',
)
