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
                  <div class="pin-out" data-pin="2" style="font-family:var(--mono);font-size:10.5px;color:var(--accent)">금액은 처음부터 끝까지 보인다 — 배송비 포함</div>
                  <div class="pin-out" data-pin="3" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">이전으로 가도 적은 값이 남는다</div>
                  <div class="pin-out" data-pin="4" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">결제 버튼은 누르는 순간 잠긴다</div>
                  <div class="pin-out" data-pin="5" style="font-family:var(--mono);font-size:10.5px;color:var(--fg-muted)">같은 주문 키로 두 번 와도 한 건만 만든다</div>
                  <div class="pin-out" data-pin="6" style="font-family:var(--mono);font-size:10.5px;color:var(--danger)">마지막에 드러난 비용 — 가장 큰 이탈 이유</div>
                </div>
              </div>'''

D = dict(
  slug="checkout", ko="결제 흐름", en="Checkout",
  desc="돈을 내는 여러 단계. 비용을 처음부터 보여 주기, 돌아가도 값이 남기, 두 번 눌림 막기.",
  lede="돈이 오가는 흐름. 여기서 생기는 사고는 <b>화면이 아니라 돈</b>으로 남습니다.",
  axes_lede="화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>단계를 오가며 <b>이전</b>으로 돌아가 보세요 — 적은 값이 그대로 남아야 합니다.<br>
          <b>금액을 늘 보여 주기</b>를 끄면 마지막에야 총액이 나옵니다. 배송비가 거기서 처음 드러나면
          사람들은 그 자리에서 나갑니다.<br>
          마지막 단계에서 <b>결제</b>를 빠르게 두 번 눌러 보세요 — 막기를 끄면 <b>주문이 둘</b> 생깁니다.</p>
        </div>''',
  names=rows([
    ("한국어", "결제 흐름, 주문하기, 체크아웃"),
    ("영어", "checkout, checkout flow, payment flow"),
    ("같이 쓰는 말",
     "한 화면에 다 넣는 것이 <b>원페이지 체크아웃</b>, 나눈 것이 <b>멀티스텝</b>입니다. "
     "가입 없이 사는 것이 <b>게스트 체크아웃</b>, "
     "중간에 떠나 장바구니가 남는 것이 <b>장바구니 이탈</b>(cart abandonment)입니다. "
     "같은 요청이 두 번 와도 한 번만 처리되게 하는 열쇠가 <b>멱등 키</b>(idempotency key)입니다."),
    ("자주 잘못 부름",
     "<b>결제</b> — 카드 승인만을 가리키기도 하고 흐름 전체를 가리키기도 합니다. <b>어디까지인지</b> 정하고 말합니다.<br>"
     "<b>장바구니</b> — 담아 두는 곳이고, 결제 흐름은 그다음입니다.<br>"
     "<b>폼</b> — <a href=\"form.html\">폼</a>이 여럿 이어진 것이지만, <b>돈과 재고</b>가 걸려 성격이 다릅니다."),
  ]),
  axes=ax("결제 흐름"),
  oneline="<b>비용을 숨기지 말고, 두 번 눌림을 막으세요.</b> 전자는 이탈을 만들고 후자는 환불을 만듭니다.",
  s4_title="단계", s4_hint="어디서 떨어지나",
  states=states([
    (steps(0, "152px", "1 / 4 — 끝이 보인다"), "장바구니", "<b>몇 단계인지</b> 처음부터 보인다"),
    (sumbox([('상품', '129,000원', False), ('배송', '3,000원', False), ('합계', '132,000원', True)]),
     "금액 ✓", "<b>처음부터</b> 배송비까지 보인다"),
    (sumbox([('합계', '132,000원', True), ('배송비 3,000원 추가됨', '', False)], "152px", True),
     "금액 ✕", "<b>마지막에 드러난 비용.</b> 가장 큰 이탈 이유"),
    (steps(1, "152px", "이전으로 가도 값이 남는다"), "되돌아가기", "다시 치게 하면 <b>거기서 나간다</b>"),
    ('''              <div style="width:100%;max-width:152px;display:grid;gap:4px">
                <span style="display:block;text-align:center;background:var(--fg-muted);color:#fff;border-radius:4px;padding:4px 0;font-size:9px">결제 중…</span>
                <span style="font-family:var(--mono);font-size:9px;color:var(--fg-muted)">버튼이 잠겼다</span>
              </div>''',
     "보내는 중", "<b>잠그지 않으면</b> 두 번 눌린다"),
    (steps(3, "152px", "주문번호 2026-1001"), "완료", "<b>주문번호</b>와 다음에 할 일을 준다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("단계 표시", "2 / 4", "<b>끝이 보여야</b> 끝까지 간다"),
    ("금액", "처음부터 끝까지", "배송비·수수료까지. <b>마지막에 드러나면</b> 나간다"),
    ("되돌아가기", "값이 남는다", "고치러 갔다 와도 <b>다시 치지 않게</b>"),
    ("잠그기", "누르는 순간", "두 번 눌림은 <b>결제 두 건</b>이 된다"),
    ("멱등 키", "같은 주문 하나", "화면이 못 막아도 <b>서버가 막는다</b>"),
    ("뒤늦은 비용", "가장 큰 이탈", "배송비·수수료·필수 가입"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>두 번 눌림은 화면만으로 못 막습니다.</b>
          버튼을 잠가도 네트워크가 끊겼다 재시도하거나,
          사용자가 새로고침하거나, 뒤로 갔다 다시 보내면 요청이 두 번 갑니다.
          그래서 화면은 <b>주문마다 고유한 키</b>를 하나 만들어 함께 보내고,
          서버는 <b>같은 키로 온 두 번째 요청에 첫 번째 결과를 돌려줍니다</b>.
          이러면 몇 번을 보내도 주문은 하나입니다 — 결제 흐름에서 이 장치는 선택이 아닙니다.</p>''',
  do=ul([
    "돈·재고가 걸린 <b>여러 단계</b> 흐름",
    "입력이 많아 <b>한 화면에 안 들어갈</b> 때",
    "중간에 떠난 사람이 <b>돌아올 수</b> 있어야 할 때",
  ]),
  dont=ul([
    "비용을 <b>마지막에</b> 드러내기",
    "사려면 <b>가입부터</b> 하게 하기 — 게스트로 사게 둔다",
    "돌아가면 값이 지워지게 두기",
    "버튼만 잠그고 <b>서버 쪽 장치</b>를 안 만들기",
  ]),
  instead='칸 묶음은 <a href="form.html">폼 설계</a>, 값 검사는 <a href="validation.html">입력 검증</a>, 결과 알림은 <a href="../items/toast.html">토스트</a>.',
  cases=cases([
    (steps(2, "150px", "3 / 4"), "여러 단계", "입력이 많을 때. <b>끝이 보이게</b>"),
    ('''              <div style="width:100%;max-width:150px;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">
                <span style="font-size:9px;font-weight:700">한 화면에 다 넣기</span>
                <span style="font-size:8.5px;color:var(--fg-muted)">배송 · 결제 · 확인이 한 장에</span>
                <span style="font-size:8px;color:var(--fg-muted)">입력이 적을 때는 이쪽이 빠르다</span>
              </div>''',
     "원페이지", "칸이 적으면 <b>나누지 않는 쪽</b>이 낫다"),
    ('''              <div style="width:100%;max-width:150px;font-family:var(--mono);font-size:9px;color:var(--fg-muted);display:grid;gap:2px">
                <span>POST /orders</span>
                <span><span style="color:var(--accent)">Idempotency-Key: 9f2a…</span></span>
                <span style="font-size:8px">두 번 와도 주문은 하나</span>
              </div>''',
     "멱등 키", "<b>서버가 막는다.</b> 화면만으로는 부족하다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 흐름의 계약서",
  code_lede="단계마다 주소를 두고, <b>주문 키</b>를 만들어 함께 보냅니다.",
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
    ("단계마다 주소", "<code>/checkout/shipping</code>. 뒤로가기가 전 단계가 된다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계를 알린다"),
    ("금액은 <code>&lt;aside&gt;</code>", "이름을 붙여 두면 <b>언제든 건너뛰어 확인</b>할 수 있다"),
    ("<code>autocomplete</code>", "<code>shipping street-address</code>·<code>cc-number</code>. 폰에서 효과가 크다"),
    ("초점", "단계가 바뀌면 <b>새 제목</b>으로. 안 그러면 Tab 이 처음부터 돈다"),
    ("잠긴 버튼", "<code>disabled</code> 대신 <code>aria-busy</code>를 쓰면 <b>초점이 유지</b>된다"),
  ]),
  backend=rows([
    ("멱등 키", "같은 키로 두 번 오면 <b>첫 번째 결과를 그대로</b> 돌려줍니다. 결제에서는 선택이 아닙니다."),
    ("금액은 서버가 다시 계산", "화면이 보낸 금액을 믿으면 <b>값을 바꿔 보낼 수</b> 있습니다. 상품 ID 와 수량만 받습니다."),
    ("재고는 결제 직전에", "장바구니에 담을 때 확인한 재고는 이미 낡았습니다. <b>결제 시점에 다시</b> 봅니다."),
    ("결제사 응답이 끊길 수 있다", "승인은 됐는데 응답을 못 받는 일이 실제로 납니다. <b>결제사에 다시 물어</b> 맞추는 절차가 필요합니다."),
    ("POST 뒤에는 다른 주소로", "완료 화면에 머물면 새로고침에서 재전송 경고가 뜹니다. <b>주문 상세로 보냅니다</b>."),
    ("중간 상태를 저장", "떠난 장바구니를 되살리려면 <b>어디까지 했는지</b>가 남아 있어야 합니다."),
  ]),
  plat_lede="<b>결제 수단</b>이 플랫폼마다 다릅니다.",
  plats=plats([
    ("웹", "카드 · 간편결제",
     sumbox([('합계', '132,000원', True)], "112px"),
     "결제창이 뜨거나 다른 사이트로 갔다 돌아옵니다. <b>돌아왔을 때</b> 상태를 맞추는 일이 큽니다."),
    ("iOS", "Apple Pay",
     '''              <div class="phone" role="img" aria-label="애플페이 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px;font-size:6px;text-align:center"> Pay</div></div></div>''',
     "한 번 눌러 생체 인증으로 끝납니다. <b>단계가 사라지므로</b> 이탈도 거의 없습니다."),
    ("안드로이드", "Google Pay",
     '''              <div class="phone" role="img" aria-label="구글페이 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:5px;right:5px;bottom:10px;background:var(--ink-900);color:#fff;border-radius:4px;padding:4px;font-size:6px;text-align:center">G Pay</div></div></div>''',
     "같은 방식입니다. 둘 다 <b>주소·카드를 OS 가 쥐고</b> 있어 입력이 거의 없습니다."),
  ]),
  plat_note="결제 흐름은 <b>화면보다 경계 상황</b>에 품이 들어갑니다 — 두 번 눌림, 끊긴 응답, 바뀐 재고, 돌아오지 않은 결제창. 화면 시안은 하루면 그리지만 이 넷을 다루는 데 그보다 오래 걸리고, <b>안 다루면 환불 업무로</b> 돌아옵니다. 일정을 잡을 때 이것을 따로 적어 두는 편이 낫습니다.",
  siblings=siblings("checkout"),
  related='''        <li><a href="form.html"><b>폼 설계</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="../items/optimistic.html"><b>낙관적 UI</b><em>8부</em></a></li>
        <li><a href="systemback.html"><b>시스템 백</b><em>11부</em></a></li>''',
)
