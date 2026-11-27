# -*- coding: utf-8 -*-
from ax13 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def steps(cur, w="152px", note=""):
    NS = ['장바구니', '배송', '결제', '완료']
    es = []
    for i, n in enumerate(NS):
        on, done = i == cur, i < cur
        es.append('<span style="display:flex;align-items:center;gap:3px;font-size:8px;'
                  + ('color:var(--accent);font-weight:700' if on else 'color:var(--fg-muted)') + '">'
                  '<span style="width:13px;height:13px;border-radius:50%;display:grid;place-items:center;font-size:7px;'
                  + ('background:var(--accent);color:#fff' if on else
                     'background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)' if done else
                     'background:var(--surface);border:1px solid var(--line)')
                  + '">' + ('✓' if done else str(i + 1)) + '</span>' + n + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:flex;align-items:center;gap:4px;flex-wrap:wrap">' + ''.join(es) + '</div>'
            + ('<span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def sumbox(lines, w="152px", warn=False):
    rs = ''.join('<div style="display:flex;font-size:9px' + (';font-weight:700;border-top:1px solid var(--line);padding-top:3px;margin-top:2px' if t else '') + '">'
                 '<span style="flex:1">' + a + '</span><span style="font-variant-numeric:tabular-nums">' + b + '</span></div>'
                 for a, b, t in lines)
    return ('              <div style="width:100%;max-width:' + w + ';border:1px solid '
            + ('var(--danger)' if warn else 'var(--line)') + ';border-radius:6px;background:var(--bg);padding:6px;display:grid;gap:1px">'
            + rs + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px">
                  <div class="pin-out" data-pin="1" style="max-width:230px">''' + steps(1, "230px").strip() + '''</div>
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">배송비를 포함한 금액이 처음부터 끝까지 보임</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이전으로 가도 적은 값이 남음</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">결제 버튼은 누르는 순간 잠김</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">같은 주문 키로 두 번 와도 한 건만 만듦</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">마지막에 드러난 비용이 가장 큰 이탈 이유</div>
                </div>
              </div>'''

D = dict(
  slug="checkout", ko="결제 흐름", en="Checkout",
  desc="돈을 내기까지 거치는 여러 단계입니다. 비용을 처음부터 보여 주는 법, 이전 단계로 돌아가도 값을 남기는 법, 결제 버튼이 두 번 눌리는 일을 막는 법을 다룹니다.",
  lede="결제 흐름에서는 실제로 돈이 오가기 때문에, 여기서 생긴 사고는 화면 오류로 끝나지 않고 <b>이중 결제나 환불 같은 돈 문제</b>로 남습니다.",
  axes_lede="화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 오가며 <b>이전</b>으로 돌아가 보세요. 앞에서 적은 값이 그대로 남아 있어야 합니다.<br>
          <b>금액을 늘 보여 주기</b>를 끄면 마지막 단계에서야 총액이 나옵니다. 배송비가 그때 처음 드러나면
          많은 사람이 그 자리에서 결제를 그만둡니다.<br>
          마지막 단계에서 <b>결제</b>를 빠르게 두 번 눌러 보세요. 막기를 끄면 <b>주문이 두 건</b> 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "결제 흐름, 주문하기, 체크아웃"),
    ("영어", "checkout, checkout flow, payment flow"),
    ("같이 쓰는 말",
     "모든 입력을 한 화면에 넣는 방식을 <b>원페이지 체크아웃</b>, 여러 화면으로 나눈 방식을 <b>멀티스텝</b>이라고 합니다. "
     "가입하지 않고 사는 것은 <b>게스트 체크아웃</b>이라 하고, "
     "중간에 떠나서 장바구니만 남는 것은 <b>장바구니 이탈</b>(cart abandonment)이라고 합니다. "
     "같은 요청이 두 번 와도 한 번만 처리되게 하려고 요청마다 붙이는 고유한 값을 <b>멱등 키</b>(idempotency key)라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>결제</b> — 카드 승인만 가리킬 때도 있고 흐름 전체를 가리킬 때도 있으므로, <b>어디까지를 말하는지</b> 먼저 정하고 씁니다.<br>"
     "<b>장바구니</b> — 장바구니는 상품을 담아 두는 곳이고, 결제 흐름은 그다음 단계입니다.<br>"
     "<b>폼</b> — 결제 흐름은 <a href=\"form.html\">폼</a> 여러 개가 이어진 모양이지만, <b>돈과 재고</b>가 걸려 있어서 다루는 법이 다릅니다."),
  ]),
  axes=ax("결제 흐름"),
  oneline="<b>비용을 숨기지 말고, 결제 버튼이 두 번 눌리는 일을 막으세요.</b> 숨긴 비용은 이탈로 이어지고, 두 번 눌린 결제는 환불 처리로 이어집니다.",
  do_title="결제 흐름을 여러 단계로 나누는 경우",
  dont_title="결제 흐름을 잘못 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  s4_title="결제 흐름의 단계", s4_hint="사용자가 어디서 떠나는가",
  states=states([
    (steps(0, "152px", "1 / 4로 끝이 보임"), "장바구니 단계", "전체가 <b>몇 단계인지</b> 처음부터 보여 줍니다"),
    (sumbox([('상품', '129,000원', False), ('배송', '3,000원', False), ('합계', '132,000원', True)]),
     "금액을 처음부터 보여 줄 때 ✓", "<b>처음부터</b> 배송비까지 포함한 금액을 보여 줍니다"),
    (sumbox([('합계', '132,000원', True), ('배송비 3,000원 추가됨', '', False)], "152px", True),
     "비용을 마지막에 드러낼 때 ✕", "<b>마지막에야 드러난 비용</b>은 결제를 그만두는 가장 큰 이유입니다"),
    (steps(1, "152px", "이전으로 가도 값이 남음"), "이전 단계로 되돌아갈 때", "적은 값을 다시 입력하게 하면 사용자가 <b>그 자리에서 떠납니다</b>"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:4px">
                <span style="display:block;text-align:center;background:var(--fg-muted);color:#fff;border-radius:4px;padding:4px 0;font-size:9px">결제 중…</span>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">버튼이 잠김</span>
              </div>''',
     "결제 요청을 보내는 중", "버튼을 <b>잠그지 않으면</b> 두 번 눌릴 수 있습니다"),
    (steps(3, "152px", "주문번호 2026-1001"), "결제를 마쳤을 때", "<b>주문번호</b>와 다음에 할 일을 알려 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계 표시", "2 / 4", "남은 단계가 <b>몇 개인지 보여야</b> 사용자가 끝까지 갑니다"),
    ("금액", "처음부터 끝까지", "배송비·수수료까지 포함해 보여 줍니다. 이 비용이 <b>마지막에야 드러나면</b> 사용자가 떠납니다"),
    ("되돌아가기", "적은 값 유지", "앞 단계를 고치러 갔다 와도 <b>다시 입력하지 않게</b> 합니다"),
    ("버튼 잠그기", "누르는 순간", "버튼이 두 번 눌리면 <b>결제가 두 건</b> 생기므로 누르는 순간 잠급니다"),
    ("멱등 키", "같은 주문은 한 건만", "화면에서 막지 못한 중복 요청도 <b>서버에서 걸러 냅니다</b>"),
    ("뒤늦은 비용", "가장 큰 이탈 이유", "배송비·수수료·필수 가입처럼 마지막에 나타나는 부담이 주된 이탈 이유입니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>중복 결제는 화면만으로는 막을 수 없습니다.</b>
          버튼을 잠가도 네트워크가 끊겼다가 재시도되거나,
          사용자가 새로고침하거나, 뒤로 갔다가 다시 보내면 요청이 두 번 가기 때문입니다.
          그래서 화면은 <b>주문마다 고유한 키</b>를 하나 만들어 요청과 함께 보내고,
          서버는 <b>같은 키로 두 번째 요청이 오면 첫 번째 결과를 그대로 돌려줍니다</b>.
          이렇게 하면 요청을 몇 번 보내도 주문은 한 건만 생기므로, 결제 흐름에는 이 장치를 반드시 넣어야 합니다.</p>''',
  do=ul([
    "돈·재고가 걸린 <b>여러 단계</b> 흐름일 때",
    "입력이 많아 <b>한 화면에 다 들어가지 않을</b> 때",
    "중간에 떠난 사람이 <b>돌아올 수</b> 있어야 할 때",
  ]),
  dont=ul([
    "비용을 <b>마지막에</b> 드러낼 때",
    "사려면 <b>가입부터</b> 하게 할 때. 가입하지 않고도 게스트로 살 수 있게 둡니다",
    "이전 단계로 돌아가면 적은 값이 지워질 때",
    "버튼만 잠그고 <b>서버 쪽 장치</b>를 만들지 않을 때",
  ]),
  instead='입력 칸을 묶는 방법은 <a href="form.html">폼 설계</a>에서, 입력값을 검사하는 방법은 <a href="validation.html">입력 검증</a>에서 다룹니다. 결제 결과를 짧게 알릴 때는 <a href="../items/toast.html">토스트</a>를 씁니다.',
  cases=cases([
    (steps(2, "150px", "3 / 4"), "여러 단계로 나눈 결제", "입력이 많을 때 씁니다. 남은 단계가 <b>몇 개인지 보이게</b> 합니다"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">
                <span style="font-size:9px;font-weight:700">한 화면에 다 넣기</span>
                <span style="font-size:8.5px;color:var(--fg-muted)">배송 · 결제 · 확인이 한 장에</span>
                <span style="font-size:8px;color:var(--fg-muted)">입력이 적을 때는 이쪽이 빠르다</span>
              </div>''',
     "한 화면에 모은 원페이지 결제", "입력 칸이 적으면 <b>단계를 나누지 않는 편</b>이 낫습니다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>POST /orders</span>
                <span><span style="color:var(--accent)">Idempotency-Key: 9f2a…</span></span>
                <span style="font-size:8px">두 번 와도 주문은 하나</span>
              </div>''',
     "멱등 키로 중복 결제 막기", "화면만으로는 중복 요청을 다 막지 못하므로 <b>서버에서 한 번 더 막습니다</b>"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="단계마다 주소를 두고, 흐름에 들어올 때 <b>주문 키</b>를 만들어 결제 요청과 함께 보냅니다.",
  code='''&lt;<span class="t">nav</span> <span class="a">aria-label</span>=<span class="s">"주문 단계"</span>&gt;
  &lt;<span class="t">ol</span>&gt;
    &lt;<span class="t">li</span>&gt;&lt;<span class="t">a</span> <span class="a">href</span>=<span class="s">"/checkout/cart"</span>&gt;장바구니&lt;/<span class="t">a</span>&gt;&lt;/<span class="t">li</span>&gt;
    &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;배송&lt;/<span class="t">li</span>&gt;
  &lt;/<span class="t">ol</span>&gt;
&lt;/<span class="t">nav</span>&gt;

&lt;<span class="t">aside</span> <span class="a">aria-label</span>=<span class="s">"주문 금액"</span>&gt;…합계 132,000원…&lt;/<span class="t">aside</span>&gt;

<span class="c">// 주문 키는 흐름에 들어올 때 한 번 만든다</span>
<span class="k">const</span> key = sessionStorage.getItem(<span class="s">'orderKey'</span>) || crypto.randomUUID();
sessionStorage.setItem(<span class="s">'orderKey'</span>, key);

payBtn.addEventListener(<span class="s">'click'</span>, <span class="k">async</span> () =&gt; {
  payBtn.disabled = <span class="k">true</span>;                       <span class="c">// 화면 쪽 잠금</span>
  <span class="k">await</span> fetch(<span class="s">'/api/orders'</span>, {
    method: <span class="s">'POST'</span>,
    headers: { <span class="s">'Idempotency-Key'</span>: key },      <span class="c">// 서버 쪽 잠금</span>
    body: JSON.stringify(order)
  });
});''',
  keys=kbd([
    ("단계마다 주소 두기", "<code>/checkout/shipping</code>처럼 단계마다 주소를 두면 뒤로가기를 눌렀을 때 전 단계로 갑니다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계를 알립니다"),
    ("금액은 <code>&lt;aside&gt;</code>에 담기", "이름을 붙여 두면 스크린 리더 사용자가 <b>언제든 그 구역으로 건너뛰어</b> 금액을 확인할 수 있습니다"),
    ("<code>autocomplete</code>", "<code>shipping street-address</code>·<code>cc-number</code>를 적어 둡니다. 입력이 번거로운 폰에서 특히 효과가 큽니다"),
    ("초점을 옮길 자리", "단계가 바뀌면 <b>새 제목</b>으로 초점을 옮깁니다. 옮기지 않으면 Tab을 눌렀을 때 페이지 처음부터 다시 돕니다"),
    ("결제 버튼을 잠글 때", "<code>disabled</code> 대신 <code>aria-busy</code>를 쓰면 버튼에 있던 <b>초점이 그대로 유지</b>됩니다"),
  ]),
  backend=rows([
    ("멱등 키로 중복 요청 걸러 내기", "같은 키로 요청이 두 번 오면 <b>첫 번째 결과를 그대로</b> 돌려줍니다. 결제 기능에는 반드시 넣어야 합니다."),
    ("금액은 서버에서 다시 계산하기", "화면이 보낸 금액을 그대로 믿으면 사용자가 요청을 조작해 <b>금액을 바꿔 보낼 수</b> 있습니다. 그래서 상품 ID와 수량만 받고 금액은 서버에서 계산합니다."),
    ("재고는 결제 직전에 다시 확인하기", "장바구니에 담을 때 확인한 재고는 결제할 무렵이면 이미 달라져 있을 수 있으므로 <b>결제 시점에 다시</b> 확인합니다."),
    ("결제사 응답이 끊겼을 때", "결제사에서 승인은 됐는데 우리 서버가 응답을 받지 못하는 일이 실제로 일어납니다. 그래서 <b>결제사에 결과를 다시 조회해</b> 주문 상태를 맞추는 절차가 필요합니다."),
    ("결제가 끝나면 다른 주소로 보내기", "POST 응답으로 그린 완료 화면에 머물면 새로고침할 때 재전송 경고가 뜹니다. 그래서 결제가 끝나면 <b>주문 상세 주소로 이동시킵니다</b>."),
    ("어느 단계까지 했는지 저장하기", "사용자가 떠난 장바구니를 나중에 되살리려면 <b>어느 단계까지 진행했는지</b> 서버에 남아 있어야 합니다."),
  ]),
  plat_lede="플랫폼마다 쓸 수 있는 <b>결제 수단</b>이 다릅니다.",
  plats=plats([
    ("웹", "카드 · 간편결제",
     sumbox([('합계', '132,000원', True)], "112px"),
     "결제창이 뜨거나 결제사 사이트로 갔다가 돌아옵니다. 그래서 사용자가 <b>돌아왔을 때</b> 주문 상태를 맞추는 일이 큰 몫을 차지합니다."),
    ("iOS", "Apple Pay",
     '''              <div class="phone" role="img" aria-label="애플페이 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px;font-size:6px;text-align:center"> Pay</div></div></div>''',
     "버튼을 한 번 누르고 생체 인증만 거치면 결제가 끝납니다. 입력 <b>단계가 거의 없어서</b> 중간에 떠나는 사람도 거의 없습니다."),
    ("안드로이드", "Google Pay",
     '''              <div class="phone" role="img" aria-label="구글페이 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px;font-size:6px;text-align:center">G Pay</div></div></div>''',
     "애플페이와 같은 방식입니다. 두 서비스 모두 <b>주소와 카드 정보를 OS가 저장해 두고</b> 있어서 사용자가 입력할 것이 거의 없습니다."),
  ]),
  plat_note="결제 흐름은 화면을 그리는 일보다 <b>경계 상황</b>을 처리하는 데 품이 더 듭니다. 두 번 눌림, 끊긴 응답, 바뀐 재고, 돌아오지 않은 결제창이 그런 경우입니다. 화면 시안은 하루면 그리지만 이 네 가지를 처리하는 데는 그보다 오래 걸리고, <b>처리하지 않으면 나중에 환불 업무</b>가 늘어납니다. 그래서 일정을 잡을 때 이 네 가지를 따로 적어 두는 편이 낫습니다.",
  siblings=siblings("checkout"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
