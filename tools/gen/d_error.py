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
  desc="에러 상태가 무엇이고 칸·폼·화면·연결 네 단계가 어떻게 다른지, 실물과 상태와 해부도로 보여주는 항목.",
  lede="뭔가 <b>안 됐다는 것</b>과 <b>이제 뭘 하면 되는지</b>를 알리는 화면. 어디에 붙이느냐로 네 단계가 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>네 단계를 번갈아 눌러 보세요.</b> 같은 실패라도 붙는 자리가 다릅니다.
          <b>단계를 올릴수록 사용자가 할 수 있는 일이 줄어듭니다</b> — 칸 하나면 고쳐서 바로 보내면 되지만,
          화면 전체면 할 수 있는 게 '다시 불러오기'뿐입니다. 그래서 올릴 이유가 없으면 올리지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "에러 상태, 오류 상태, 오류 화면"),
    ("영어", "error state, error message, inline error, error page"),
    ("같이 쓰는 말", "칸 아래 붙는 것을 <b>인라인 에러</b>, 폼 위에 뜨는 상자를 <b>얼럿</b>이나 <b>배너</b>, 화면 전체를 덮는 것을 <b>에러 페이지</b>(404·500)라 부릅니다."),
    ("자주 잘못 부름",
     "<b>얼럿</b> — 웹에서 얼럿은 <code>alert()</code>나 인라인 경고 상자를 뜻합니다. 모달과 섞입니다.<br>"
     "<b>토스트</b> — 에러를 토스트로만 보내면 <b>사라져서 못 읽습니다.</b> 고쳐야 하는 에러는 화면에 남아야 합니다.<br>"
     "<b>빈 상태</b> — 비어 있는 것은 잘못이 아닙니다. 빨갛게 칠하지 않습니다."),
  ]),
  axes=LEVELS,
  oneline="에러는 <b>고칠 수 있는 가장 가까운 자리</b>에 붙입니다. 올릴 이유가 없으면 단계를 올리지 않습니다.",
  states=states([
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">자릿수가 모자랍니다</div></div>', bars="4", label="칸 하나 에러"), "칸 하나", "그 칸 아래. <b>무엇이 틀렸고 어떻게 고치는지</b>까지"),
    (mini('<div style="margin-top:7px;padding:0 6px"><div style="border:1px solid color-mix(in srgb,var(--danger) 45%,transparent);background:color-mix(in srgb,var(--danger) 8%,var(--surface));border-radius:3px;padding:4px 5px"><div style="font-size:7px;font-weight:700">등록하지 못했습니다</div><div style="font-size:6px;color:var(--fg-muted)">잠시 뒤 다시 해 주세요</div></div><div style="height:9px;border:1px solid var(--line-strong);border-radius:3px;margin-top:5px"></div></div>', bars="", label="폼 전체 에러"), "폼 전체", "폼 맨 위. <b>입력값은 지운다 말고 그대로 둔다</b>"),
    (mini('<div style="position:absolute;inset:0;display:grid;place-items:center;gap:4px;text-align:center;padding:8px"><span style="font-size:14px;font-weight:800;color:var(--fg-faint);letter-spacing:-.04em">500</span><span style="font-size:7.5px;font-weight:700">화면을 열지 못했습니다</span><span class="mini__btn" style="font-size:7px;padding:2px 6px">다시 불러오기</span></div>', bars="", label="화면 전체 에러"), "화면 전체", "할 수 있는 게 거의 없다. <b>돌아갈 길</b>을 꼭 둔다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--ink-900);color:#fff;font-size:6.5px;padding:3px 5px">연결이 끊겼습니다 · 다시 시도 중…</div><div class="mini__bg" style="padding-top:16px;opacity:.6"><div class="mini__bar mini__bar--w80"></div><div class="mini__bar mini__bar--w60"></div></div>', bars="", label="연결 끊김 띠"), "연결 끊김", "앱 꼭대기 띠. <b>읽기는 되게</b> 두고 쓰기만 막는다"),
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--warn);border-radius:3px"></div><div style="font-size:6.5px;color:var(--warn);font-weight:700;margin-top:3px">이 계좌는 이미 등록돼 있습니다</div></div>', bars="4", label="경고 수준"), "경고", "틀린 건 아니지만 짚고 갈 것. <b>빨강을 아껴 둬야</b> 빨강이 통한다"),
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid #1f8a4c;border-radius:3px"></div><div style="font-size:6.5px;color:#1f8a4c;font-weight:700;margin-top:3px">✓ 확인했습니다</div></div>', bars="4", label="고친 뒤"), "고친 뒤", "고쳐지면 <b>즉시</b> 풀어 준다. 보내야만 풀리면 답답하다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("경고 상자", "alert · callout", "빨강은 <b>진짜 막힌 것</b>에만. 아끼지 않으면 눈에 안 들어온다"),
    ("아이콘", "icon", "색만으로 알리지 않으려는 장치. 색각 이상인 사람에게는 이게 전부다"),
    ("무엇이 안 됐나", "title", "<b>사용자의 말로.</b> '요청 실패'가 아니라 '등록하지 못했습니다'"),
    ("왜 · 어떻게", "description", "원인과 <b>다음에 할 일</b>. 둘 중 하나만 있으면 반쪽이다"),
    ("다시 할 길", "retry · action", "에러 화면에서 가장 중요한 칸. 없으면 막다른 길이다"),
    ("오류 번호", "error code", "문의할 때 쓴다. 사용자에게는 뜻이 없어도 <b>고객센터에는 전부</b>다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          적지 말아야 할 것도 있습니다 — <b>스택 트레이스, 내부 주소, SQL.</b>
          사용자에게는 쓸모가 없고 공격자에게는 쓸모가 있습니다. 자세한 것은 오류 번호로 잇습니다.</p>''',
  do=ul([
    "고칠 수 있는 <b>가장 가까운 자리</b>에 붙일 때",
    "<b>다시 할 길</b>을 같이 줄 때 — 다시 시도, 돌아가기, 문의하기",
    "원인을 사용자의 말로 적을 때 — '은행 점검 시간입니다'",
  ]),
  dont=ul([
    "에러를 토스트로만 보내기 — 사라져서 못 읽습니다",
    "폼이 실패했는데 <b>입력값을 지우기</b> — 가장 미움받는 처리입니다",
    "\"오류가 발생했습니다\"만 적기 — 무엇을 하라는 건지 알 수 없습니다",
    "스택 트레이스·내부 주소 노출 — 쓸모없고 위험합니다",
    "빨강을 아무 데나 쓰기 — 진짜 빨강이 안 보이게 됩니다",
  ]),
  instead='알려만 주면 되면 <a href="toast.html">토스트</a>, 답을 꼭 받아야 하면 <a href="modal.html">모달</a>, 아직 불러오는 중이면 <a href="spinner.html">스피너</a>, 원래 없는 것이면 <a href="empty.html">빈 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:8px;padding:0 6px"><div style="font-size:6.5px;margin-bottom:2px">계좌번호</div><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">11~12자리입니다</div></div>', bars="", tall=False, label="인라인 에러 재현"),
     "인라인 에러", "가장 좋은 에러. 고칠 곳 바로 옆에 있고 나머지는 그대로다"),
    (mini('<div style="margin-top:7px;padding:0 6px"><div style="border:1px solid color-mix(in srgb,var(--danger) 45%,transparent);background:color-mix(in srgb,var(--danger) 8%,var(--surface));border-radius:3px;padding:4px 5px"><div style="font-size:7px;font-weight:700">보내지 못했습니다</div><div style="font-size:6px;color:var(--accent);font-weight:700;margin-top:2px">다시 시도</div></div></div>', bars="4", tall=False, label="폼 위 경고 재현"),
     "폼 위 경고", "칸은 다 맞는데 보내기가 실패했을 때. 입력값은 그대로 둔다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;background:var(--ink-900);color:#fff;font-size:6.5px;padding:3px 5px;display:flex;gap:4px"><span style="width:4px;height:4px;border-radius:50%;background:#e0a800;margin-top:3px"></span><span>연결이 끊겼습니다</span></div><div class="mini__bg" style="padding-top:16px;opacity:.6"><div class="mini__bar mini__bar--w80"></div></div>', bars="", tall=False, label="오프라인 띠 재현"),
     "연결 끊김 띠", "화면 전체를 못 쓰게 막지 않는다. 읽기는 되게 둔다"),
  ]),
  code_lede="에러를 <b>칸과 이어 두는 것</b>이 핵심입니다. 색만으로 알리면 스크린 리더와 색각 이상인 사람에게는 아무 일도 안 일어납니다.",
  code='''<span class="c">&lt;!-- 칸과 설명을 이어 둔다. 색만으로는 안 된다 --&gt;</span>
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"acct"</span> <span class="a">aria-invalid</span>=<span class="s">"true"</span> <span class="a">aria-describedby</span>=<span class="s">"e1"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"e1"</span> <span class="a">class</span>=<span class="s">"field-err"</span>&gt;자릿수가 모자랍니다. 11~12자리입니다.&lt;/<span class="t">p</span>&gt;

<span class="c">&lt;!-- 폼 전체 실패는 읽던 말을 끊고 알린다 --&gt;</span>
&lt;<span class="t">div</span> <span class="a">role</span>=<span class="s">"alert"</span>&gt;등록하지 못했습니다…&lt;/<span class="t">div</span>&gt;

<span class="c">// 보낸 뒤가 아니라 '고쳐지는 즉시' 풀어 준다</span>
input.addEventListener(<span class="s">'input'</span>, () =&gt; <span class="a">{</span>
  <span class="a">if</span> (valid(input.value)) clearError(input);
<span class="a">}</span>);

<span class="c">// 사용자에게는 번호만, 자세한 것은 로그로</span>
log.error(<span class="a">{</span> id: <span class="s">'a4f21c'</span>, err <span class="a">}</span>);''',
  keys=kbd([
    ("보낼 때", "<b>첫 번째 틀린 칸으로 포커스를 옮긴다.</b> 어디가 틀렸는지 찾아 헤매지 않게"),
    ("<code>aria-invalid</code>", "틀린 칸에 <code>true</code>. 설명은 <code>aria-describedby</code>로 잇는다"),
    ("<code>role=\"alert\"</code>", "폼 전체 실패처럼 <b>지금 알려야 하는 것</b>에만. 칸 하나에는 쓰지 않는다"),
    ("고쳐질 때", "다시 보내기를 기다리지 말고 <b>입력 중에</b> 풀어 준다"),
    ("색", "빨강만으로 알리지 않는다. 아이콘과 글자를 같이 둔다"),
  ]),
  backend=rows([
    ("단계 = 실패한 층", "검증 실패(<code>400</code>)는 칸으로, 일시적 실패(<code>503</code>)는 폼 위로, 렌더 실패(<code>500</code>)는 화면으로, 연결 실패는 꼭대기 띠로 갑니다. <b>응답이 화면의 단계를 정합니다.</b>"),
    ("필드 단위 에러를 내려 준다", "<code>{ field: 'account', message: '…' }</code> 형태로 주면 화면이 칸에 붙일 수 있습니다. 문장 하나만 주면 폼 위로 올릴 수밖에 없습니다."),
    ("다시 시도 = 멱등성", "'다시 시도'를 누르면 같은 요청이 또 갑니다. 멱등 키가 없으면 두 번 등록됩니다. <b>버튼 하나가 서버 설계를 요구합니다.</b>"),
    ("오류 번호 = 상관관계 ID", "요청마다 ID를 달아 응답과 로그에 함께 남깁니다. 사용자가 'a4f21c'만 말해도 그 요청을 찾아낼 수 있습니다."),
    ("노출 범위", "스택 트레이스와 내부 주소는 공격자에게 지도를 주는 것과 같습니다. 바깥에는 번호만, 안에는 전부 남깁니다."),
  ]),
  plat_lede="네 단계라는 틀은 비슷하고, 이름과 부품만 갈립니다.",
  plats=plats([
    ("웹", "표준 지침 없음",
     mini('<div style="margin-top:8px;padding:0 6px"><div style="height:11px;border:1px solid var(--danger);border-radius:3px"></div><div style="font-size:6.5px;color:var(--danger);font-weight:700;margin-top:3px">자릿수가 모자랍니다</div></div>', bars="4", label="웹 인라인 에러 재현"),
     "<b>인라인 에러</b> · 칸 아래가 기본이고, 화면 전체는 <b>에러 페이지</b>(404·500)로 따로 다룹니다."),
    ("iOS", "Apple HIG",
     phone('<div class="ios-alert"><div class="ios-alert__box"><div><b>등록하지 못했습니다</b><p>잠시 뒤 다시 해 주세요.</p></div><div class="ios-alert__btns"><span>취소</span><span>다시 시도</span></div></div></div>', "iOS 얼럿 재현"),
     "<b>얼럿</b>으로 띄우는 관례가 강합니다. 폼 안쪽 에러는 <b>칸 아래 빨간 글씨</b>로 두고, 지침은 '<b>무엇을 하라고 알려 주라</b>'를 특히 강조합니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:40px"><div style="height:14px;border:1px solid var(--danger);border-radius:4px"></div><div style="font-size:7px;color:var(--danger);margin-top:3px">자릿수가 모자랍니다</div></div><div style="position:absolute;left:6px;right:6px;bottom:10px;background:#2e3238;border-radius:5px;padding:5px 7px;font-size:7.5px;color:#fff">보내지 못했습니다</div>', "안드로이드 에러 재현"),
     "<b>서포팅 텍스트</b>(supporting text)가 에러일 때 빨개지는 구조입니다. 일시적 실패는 <b>스낵바</b>로 알리는 것이 관례입니다."),
  ]),
  plat_note="\"에러 띄워 주세요\"는 <b>네 가지 중 어느 것인지</b>가 빠진 말입니다. 그대로 만들면 대개 가장 쉬운 토스트로 가는데, 토스트는 <b>사라져서 못 읽는</b> 통로입니다. 고쳐야 하는 에러는 화면에 남아야 합니다.",
  siblings=siblings("error"),
  related='''        <li><span class="na"><b>에러 메시지 문구</b><em>14부</em></span></li>
        <li><span class="na"><b>폼 설계</b><em>10부</em></span></li>
        <li><span class="na"><b>라이브 리전</b><em>12부</em></span></li>
        <li><span class="na"><b>대비비</b><em>12부</em></span></li>''',
)
