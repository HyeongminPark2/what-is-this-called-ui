# -*- coding: utf-8 -*-
from ax5 import ax
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

def tl(items, w="180px"):
    out = []
    for i, (when, title, dot, dim) in enumerate(items):
        last = i == len(items) - 1
        color = {"now": "var(--accent)", "bad": "var(--danger)", "done": "var(--line-strong)", "next": "var(--line-strong)"}[dot]
        ring = ';box-shadow:0 0 0 3px var(--accent-soft)' if dot == "now" else ''
        out.append(
            '<div style="display:grid;grid-template-columns:44px 12px 1fr;gap:0 6px%s">'
            '<span style="font-size:9px;color:var(--fg-muted);text-align:right;padding-top:1px">%s</span>'
            '<span style="position:relative;display:flex;justify-content:center">'
            '<span style="position:absolute;top:%s;bottom:%s;width:2px;background:var(--line)"></span>'
            '<span style="position:relative;width:8px;height:8px;border-radius:99px;margin-top:3px;background:%s%s"></span></span>'
            '<span style="font-size:10.5px;%spadding-bottom:%s;display:block">%s</span></div>'
            % (';opacity:.45' if dim else '', when,
               '5px' if i == 0 else '0', 'auto;height:5px' if last else '0',
               color, ring,
               'font-weight:700;' if dot in ("now", "bad") else '',
               '0' if last else '10px', title))
    return '              <div style="width:100%%;max-width:%s">%s</div>' % (w, "".join(out))

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:16px">
                  <div class="pin-out" data-pin="1" style="background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 13px">
                    <div style="display:grid;grid-template-columns:58px 14px 1fr;gap:0 8px;align-items:start">
                      <span style="font-size:10px;color:var(--fg-muted);text-align:right">11월 8일<br>09:21</span>
                      <span style="position:relative;display:flex;justify-content:center;align-self:stretch">
                        <span style="position:absolute;top:6px;bottom:0;width:2px;background:var(--line)"></span>
                        <span style="position:relative;width:9px;height:9px;border-radius:99px;margin-top:3px;background:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)"></span>
                      </span>
                      <span style="display:grid;gap:2px;padding-bottom:11px">
                        <span style="font-size:12px;font-weight:700">담당자 검토</span>
                        <span style="font-size:10.5px;color:var(--fg-muted)">홍길동이 보고 있습니다</span>
                      </span>
                      <span style="font-size:10px;color:var(--fg-muted);text-align:right;opacity:.5">예정</span>
                      <span style="position:relative;display:flex;justify-content:center;align-self:stretch;opacity:.5">
                        <span style="position:absolute;top:0;height:6px;width:2px;background:var(--line)"></span>
                        <span style="position:relative;width:9px;height:9px;border-radius:99px;margin-top:3px;background:var(--line-strong)"></span>
                      </span>
                      <span style="font-size:12px;font-weight:600;opacity:.5">승인</span>
                    </div>
                  </div>
                  <div class="pin-out" data-pin="2" style="font-size:10.5px;color:var(--fg-muted);font-variant-numeric:tabular-nums">11월 8일 09:21 — <b style="color:var(--fg)">왼쪽에 가지런히</b></div>
                  <div class="pin-out" data-pin="3" style="display:flex;align-items:center;gap:10px;font-size:11px;color:var(--fg-muted)">
                    <span style="display:block;width:2px;height:22px;background:var(--line-strong);flex:none;margin-left:10px"></span>
                    <span>점들을 잇는 선 — <b style="color:var(--fg)">양 끝을 자른다</b></span>
                  </div>
                  <div class="pin-out" data-pin="4" style="display:flex;align-items:center;gap:10px;font-size:11px;color:var(--fg-muted)">
                    <span style="width:9px;height:9px;border-radius:99px;background:var(--accent);box-shadow:0 0 0 3px var(--accent-soft);flex:none;margin-left:7px"></span>
                    <span>사건 하나 — 지금은 테를 두른다</span>
                  </div>
                  <div class="pin-out" data-pin="5" style="font-size:12px;font-weight:700">담당자 검토</div>
                  <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted)">홍길동이 보고 있습니다</div>
                </div>
              </div>'''

D = dict(
  slug="timeline", ko="타임라인", en="Timeline · activity feed · stepper",
  desc="타임라인의 레일과 점, 지금 단계 표시, 흐름이 멈췄을 때의 처리를 실물과 해부도로 보여주는 항목.",
  lede="사건들을 <b>일어난 순서대로 꿴</b> 줄. 배송 추적, 결재 단계, 활동 기록이 다 같은 모양입니다.",
  axes_lede="표시 부품은 '보여 주기만 한다'는 점이 같습니다. 이 네 가지만 물어보면 갈립니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>다음 단계로</b>를 눌러 보세요. 지난 것은 조용하게, <b>지금</b>은 또렷하게,
          앞으로 올 것은 흐리게 그립니다. 화면을 못 보는 사람에게는 <code>aria-current="step"</code>이 그 말을 대신합니다.<br>
          <b>거절당하기</b>도 눌러 보세요. 흐름은 늘 끝까지 가지 않습니다 —
          <b>멈춘 자리</b>와 그 이유를 그 자리에 적어야 어디서 멈췄는지 다시 찾지 않습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "타임라인, 진행 단계, 이력, 활동 기록, 배송 추적"),
    ("영어", "timeline, activity feed, stepper, progress tracker, audit log"),
    ("같이 쓰는 말",
     "세로로 내려가는 선을 <b>레일</b>(rail · line · connector), 사건마다 찍히는 동그라미를 "
     "<b>노드</b>(node · dot · marker)라 합니다. 단계가 정해져 있고 끝이 있으면 <b>스테퍼</b>(stepper), "
     "끝없이 쌓이는 기록이면 <b>활동 피드</b>(activity feed)라 따로 부릅니다."),
    ("자주 잘못 부름",
     "<b>스테퍼</b> — 스테퍼는 <b>끝이 정해진</b> 단계이고(결제 1·2·3단계), 타임라인은 끝이 없을 수도 있습니다.<br>"
     "<b>프로그레스 바</b> — 프로그레스는 <b>얼마나 왔는지</b>를 한 줄로 말하고, 타임라인은 <b>무엇이 있었는지</b>를 말합니다.<br>"
     "<b>리스트</b> — 리스트는 순서가 바뀌어도 됩니다. 타임라인은 <b>순서가 뜻</b>입니다."),
  ]),
  axes=ax("타임라인"),
  oneline="타임라인은 <b>순서가 내용인 목록</b>입니다. 순서를 바꿔도 말이 되면 그건 그냥 리스트입니다.",
  s4_title="상태", s4_hint="그림 한 장으로는 못 배운다",
  states=states([
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("09:21", "담당자 검토", "now", False), ("예정", "승인", "next", True)], w="170px"),
     "진행 중", "지난 것 · <b>지금</b> · 앞으로. 셋이 다르게 보여야 한다"),
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("09:21", "거절됨", "bad", False), ("—", "승인", "next", True)], w="170px"),
     "멈춤", "<b>그 자리에서</b> 빨개진다. 맨 아래에 따로 적지 않는다"),
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("10:40", "입금 완료", "done", False)], w="170px"),
     "끝남", "마지막 점까지 다 찼다. <b>레일이 거기서 끝난다</b>"),
    (tl([("방금", "홍길동이 금액을 고쳤습니다", "now", False), ("1시간 전", "김철수이 댓글을 남겼습니다", "done", False), ("어제", "정산이 등록되었습니다", "done", False)], w="170px"),
     "활동 피드", "끝이 없다. <b>최근 것이 위</b>로 온다 — 방향이 반대다"),
    ('''              <div style="width:100%;max-width:170px;display:grid;gap:9px">
                <div style="display:flex;gap:7px;align-items:flex-start"><span class="skl" style="width:8px;height:8px;border-radius:99px;margin-top:3px;flex:none"></span><span class="skl" style="height:9px;flex:1"></span></div>
                <div style="display:flex;gap:7px;align-items:flex-start"><span class="skl" style="width:8px;height:8px;border-radius:99px;margin-top:3px;flex:none"></span><span class="skl" style="height:9px;width:70%"></span></div>
              </div>''',
     "로딩", "점과 글줄의 뼈대. <b>레일은 그리지 않는다</b> — 몇 개가 올지 모른다"),
    ('''              <div style="width:100%;max-width:170px;display:grid;gap:6px;text-align:center;color:var(--fg-muted)">
                <span style="font-size:10.5px">아직 기록이 없습니다</span>
                <span style="font-size:9.5px;color:var(--fg-faint)">정산을 올리면 여기에 쌓입니다</span>
              </div>''',
     "빈 상태", "점 하나도 없을 때. <b>무엇을 하면 쌓이는지</b>를 적는다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("타임라인", "timeline", "사건들을 담는 세로 목록. <code>&lt;ol&gt;</code>이라야 '순서가 있다'가 읽힌다"),
    ("시각", "timestamp", "<b>왼쪽에 가지런히</b>. 본문에 섞으면 훑어 내려갈 때 눈이 걸린다"),
    ("레일", "rail · connector", "점들을 잇는 선. <b>첫 점 위와 마지막 점 아래는 잘라</b> 둬야 끝이 또렷하다"),
    ("점", "node · dot", "사건 하나. 지금은 테를 둘러 키우고, 멈춘 자리는 빨갛게"),
    ("제목", "title", "무슨 일이 있었는지. 한 줄로 끝낸다"),
    ("본문", "detail", "누가·왜. <b>멈춘 이유도 여기</b>에 적는다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          레일은 점을 <b>잇는</b> 선이지 테두리가 아닙니다. 그래서 첫 점 위쪽과 마지막 점 아래쪽은
          잘라 내야 '여기서 시작해서 여기서 끝난다'가 보입니다. 선을 끝까지 그어 두면
          <b>더 있을 것 같은</b> 인상을 줘서, 실제로 "다음 단계가 안 보여요"라는 제보로 돌아옵니다.</p>''',
  do=ul([
    "<b>순서가 곧 뜻</b>일 때 — 배송, 결재, 상태 변화",
    "'지금 어디인지'가 가장 궁금할 때",
    "누가 언제 무엇을 했는지 <b>되짚어야</b> 할 때 — 감사 기록",
  ]),
  dont=ul([
    "순서가 상관없는 목록 → <a href=\"listitem.html\">리스트 아이템</a>",
    "단계가 둘뿐일 때 — 선을 그릴 만한 일이 아닙니다",
    "진행률만 알면 될 때 → <a href=\"../items/progress.html\">프로그레스 바</a> 한 줄이 낫습니다",
    "수백 건을 한 번에 — <b>묶어서 접거나</b> 날짜로 나눕니다",
  ]),
  instead='끝이 정해진 단계면 스테퍼(7부), 진행률이면 <a href="../items/progress.html">프로그레스 바</a>, 순서가 상관없으면 <a href="listitem.html">리스트 아이템</a>.',
  cases=cases([
    (tl([("11월 7일", "주문 접수", "done", False), ("11월 8일", "상품 준비", "done", False), ("11월 9일", "배송 중", "now", False), ("예정", "배송 완료", "next", True)]),
     "배송 추적", "가장 익숙한 자리. <b>지금 어디</b>가 전부다"),
    (tl([("방금", "홍길동이 승인했습니다", "now", False), ("2시간 전", "김철수이 금액을 고쳤습니다", "done", False), ("어제", "이영희이 등록했습니다", "done", False)]),
     "활동 기록", "<b>최근이 위</b>. 점은 다 같은 모양이고 끝이 없다"),
    (tl([("1단계", "계정 정보", "done", False), ("2단계", "계좌 확인", "now", False), ("3단계", "완료", "next", True)]),
     "스테퍼", "끝이 정해져 있다. <b>남은 단계가 몇 개인지</b> 보인다"),
  ]),
  s8_title="최소 마크업과 규칙", s8_hint="이 부품의 계약서",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="순서가 뜻이므로 <code>&lt;ol&gt;</code>을 씁니다. 지금 단계에는 <code>aria-current=\"step\"</code> 하나면 충분합니다.",
  code='''&lt;<span class="t">ol</span> <span class="a">class</span>=<span class="s">"tl"</span>&gt;
  &lt;<span class="t">li</span>&gt;
    &lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-07T14:02"</span>&gt;11월 7일 14:02&lt;/<span class="t">time</span>&gt;
    &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"tl__dot"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;&lt;/<span class="t">span</span>&gt;
    &lt;<span class="t">span</span>&gt;&lt;<span class="t">b</span>&gt;정산 요청&lt;/<span class="t">b</span>&gt;&lt;<span class="t">span</span>&gt;모란상회가 올렸습니다&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">span</span>&gt;
  &lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;…&lt;/<span class="t">li</span>&gt;   <span class="c">&lt;!-- 지금 단계 --&gt;</span>
&lt;/<span class="t">ol</span>&gt;

<span class="c">/* 레일은 점을 잇는 선 — 첫 점 위와 마지막 점 아래를 자른다 */</span>
<span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">content</span>: <span class="s">""</span>; <span class="a">position</span>: absolute; <span class="a">top</span>: <span class="a">0</span>; <span class="a">bottom</span>: <span class="a">0</span>; <span class="a">width</span>: <span class="a">2px</span>; }
<span class="t">li</span>:first-child <span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">top</span>: <span class="a">7px</span>; }
<span class="t">li</span>:last-child  <span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">bottom</span>: auto; <span class="a">height</span>: <span class="a">7px</span>; }''',
  keys=kbd([
    ("<code>&lt;ol&gt;</code>로 감싼다", "순서가 뜻이다. <code>&lt;ul&gt;</code>이면 '순서 없는 목록'으로 읽힌다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계 <b>하나</b>에만. 둘이면 어디인지 알 수 없다"),
    ("<code>&lt;time datetime&gt;</code>", "기계가 읽을 수 있는 시각을 따로 적는다. '방금'만 있으면 언제인지 모른다"),
    ("점은 숨긴다", "<code>aria-hidden</code> — 동그라미는 소리로 읽을 것이 없다"),
    ("멈춘 자리에 이유를", "맨 아래 따로 적지 말고 <b>그 항목 안에</b> 쓴다"),
    ("레일 끝을 자른다", "첫 점 위와 마지막 점 아래를 남기면 <b>더 있을 것처럼</b> 보인다"),
  ]),
  backend=rows([
    ("타임라인 = 이벤트 로그", "상태를 <code>status</code> 한 칸으로 덮어쓰면 <b>지나온 길이 사라집니다.</b> 상태가 바뀔 때마다 한 줄씩 쌓는 표가 따로 있어야 타임라인을 그릴 수 있습니다."),
    ("시각은 UTC 로", "저장은 UTC, 보여 줄 때 사용자 시간대로 바꿉니다. 섞이면 <b>같은 사건이 두 시간 다르게</b> 보입니다."),
    ("'방금'은 화면에서", "서버가 '2시간 전'을 보내면 화면을 오래 켜 둔 사람에게는 틀린 말이 됩니다. <b>절대 시각</b>을 보내고 화면에서 바꿔 적습니다."),
    ("몇 개까지", "활동 기록은 끝없이 쌓입니다. 최근 20건만 주고 <b>더 보기</b>로 이어 받습니다 — <a href=\"../items/infinite.html\">무한 스크롤</a>과 같은 문제입니다."),
    ("누가 했는지", "시스템이 한 일과 사람이 한 일을 구별해 두면 '자동 검증'과 '담당자 검토'를 <b>다르게 그릴</b> 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 전용 부품은 없고, 가까운 것이 조금씩 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     tl([("14:02", "요청", "done", False), ("09:21", "검토", "now", False), ("예정", "승인", "next", True)], w="120px"),
     "<code>&lt;ol&gt;</code>에 선과 점을 직접 그립니다. 선은 보통 <code>::before</code>로 만듭니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 단계 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:10px;right:8px;top:28px;display:grid;gap:6px">
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center"><span style="width:5px;height:5px;border-radius:99px;background:var(--line-strong)"></span>주문 접수</span>
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center;font-weight:700"><span style="width:5px;height:5px;border-radius:99px;background:var(--accent)"></span>배송 중</span>
                </div>
              </div></div>''',
     "전용 부품이 없습니다. 배송 추적류는 <b>직접 그리고</b>, 단계는 페이지를 넘기는 방식으로 푸는 일이 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 단계 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:10px;right:8px;top:28px;display:grid;gap:6px">
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center"><span style="width:5px;height:5px;border-radius:99px;background:var(--line-strong)"></span>주문 접수</span>
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center;font-weight:700"><span style="width:5px;height:5px;border-radius:99px;background:var(--accent)"></span>배송 중</span>
                </div>
              </div></div>''',
     "M3 에는 타임라인이 없습니다. 예전 가이드의 <b>스테퍼</b>가 가장 가깝고, 요즘은 직접 만듭니다."),
  ]),
  plat_note="정해진 부품이 없어서 <b>이름이 가장 많이 갈리는</b> 자리입니다 — 타임라인·진행 단계·스테퍼·이력·추적이 모두 같은 것을 가리킬 수 있습니다. <b>끝이 정해져 있는지</b>부터 물으면 스테퍼인지 활동 피드인지가 바로 갈립니다.",
  siblings=siblings("timeline"),
  related='''        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>스테퍼</b><em>7부</em></span></li>''',
)
