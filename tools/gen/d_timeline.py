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
  desc="타임라인의 레일과 점, 지금 단계를 표시하는 법, 흐름이 중간에 멈췄을 때의 처리를 실물과 해부도로 보여 주는 항목입니다.",
  lede="타임라인은 사건들을 <b>일어난 순서대로 이어 놓은</b> 세로 목록입니다. 배송 추적, 결재 단계, 활동 기록이 모두 이 모양으로 그려집니다.",
  axes_lede="표시 부품은 모두 무언가를 보여 주기만 한다는 점이 같아서, 아래 네 가지를 물어봐야 서로 구별됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>다음 단계로</b>를 눌러 보세요. 지난 단계는 눈에 덜 띄게, <b>지금 단계</b>는 또렷하게,
          앞으로 올 단계는 흐리게 그립니다. 화면을 보지 못하는 사람에게는 <code>aria-current="step"</code>이 지금 단계를 알려 줍니다.<br>
          <b>거절당하기</b>도 눌러 보세요. 흐름이 늘 끝까지 가는 것은 아니어서, 중간에 멈추면
          <b>멈춘 단계</b>에 그 이유를 바로 적어 둡니다. 그래야 사용자가 어디서 멈췄는지 따로 찾지 않아도 됩니다.</p>
        </div>''',
  names=rows([
    ("한국어", "타임라인, 진행 단계, 이력, 활동 기록, 배송 추적"),
    ("영어", "timeline, activity feed, stepper, progress tracker, audit log"),
    ("같이 쓰는 말",
     "세로로 내려가는 선은 <b>레일</b>(rail · line · connector), 사건마다 찍히는 동그라미는  "
     "<b>노드</b>(node · dot · marker)라고 부릅니다. 단계가 정해져 있고 끝이 있으면 <b>스테퍼</b>(stepper),  "
     "끝없이 쌓이는 기록이면 <b>활동 피드</b>(activity feed)라고 따로 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>스테퍼</b> — 스테퍼는 결제 1·2·3단계처럼 <b>끝이 정해진</b> 단계를 보여 주고, 타임라인은 끝이 없을 수도 있습니다.<br>"
     "<b>프로그레스 바</b> — 프로그레스 바는 <b>얼마나 진행됐는지</b>를 막대 하나로 보여 주고, 타임라인은 <b>그동안 무슨 일이 있었는지</b>를 보여 줍니다.<br>"
     "<b>리스트</b> — 리스트는 항목 순서를 바꿔도 되지만, 타임라인은 <b>순서 자체가 정보</b>라서 바꿀 수 없습니다."),
  ]),
  axes=ax("타임라인"),
  oneline="타임라인은 <b>순서 자체가 내용인 목록</b>입니다. 항목 순서를 바꿔도 뜻이 달라지지 않는다면 그건 타임라인이 아니라 리스트입니다.",
  s4_title="상태", s4_hint="그림 한 장으로는 못 배운다",
  states=states([
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("09:21", "담당자 검토", "now", False), ("예정", "승인", "next", True)], w="170px"),
     "진행 중", "지난 단계, <b>지금 단계</b>, 앞으로 올 단계가 서로 다르게 보여야 합니다"),
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("09:21", "거절됨", "bad", False), ("—", "승인", "next", True)], w="170px"),
     "멈춤", "멈춘 단계가 <b>그 자리에서</b> 빨갛게 바뀝니다. 맨 아래에 따로 적지 않습니다"),
    (tl([("14:02", "정산 요청", "done", False), ("14:03", "자동 검증", "done", False), ("10:40", "입금 완료", "done", False)], w="170px"),
     "끝남", "마지막 점까지 모두 칠해지고, <b>레일도 마지막 점에서 끝납니다</b>"),
    (tl([("방금", "홍길동이 금액을 고쳤습니다", "now", False), ("1시간 전", "김철수가 댓글을 남겼습니다", "done", False), ("어제", "정산이 등록되었습니다", "done", False)], w="170px"),
     "활동 피드", "끝이 없이 쌓이고, 진행 단계와는 방향이 반대로 <b>최근 기록이 위</b>에 옵니다"),
    ('''              <div style="width:100%;max-width:170px;display:grid;gap:9px">
                <div style="display:flex;gap:7px;align-items:flex-start"><span class="skl" style="width:8px;height:8px;border-radius:99px;margin-top:3px;flex:none"></span><span class="skl" style="height:9px;flex:1"></span></div>
                <div style="display:flex;gap:7px;align-items:flex-start"><span class="skl" style="width:8px;height:8px;border-radius:99px;margin-top:3px;flex:none"></span><span class="skl" style="height:9px;width:70%"></span></div>
              </div>''',
     "로딩", "점과 글줄의 뼈대만 그리고, 항목이 몇 개 올지 모르므로 <b>레일은 그리지 않습니다</b>"),
    ('''              <div style="width:100%;max-width:170px;display:grid;gap:6px;text-align:center;color:var(--fg-muted)">
                <span style="font-size:10.5px">아직 기록이 없습니다</span>
                <span style="font-size:9.5px;color:var(--fg-faint)">정산을 올리면 여기에 쌓입니다</span>
              </div>''',
     "빈 상태", "기록이 하나도 없을 때입니다. <b>무엇을 하면 기록이 쌓이는지</b>를 적어 줍니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("타임라인", "timeline", "사건들을 담는 세로 목록입니다. <code>&lt;ol&gt;</code>로 만들어야 순서가 있는 목록이라고 읽힙니다"),
    ("시각", "timestamp", "<b>왼쪽에 가지런히</b> 둡니다. 본문에 섞어 두면 시각을 훑어 내려가며 읽기 어렵습니다"),
    ("레일", "rail · connector", "점들을 잇는 선입니다. <b>첫 점 위와 마지막 점 아래는 잘라</b> 두어야 시작과 끝이 또렷하게 보입니다"),
    ("점", "node · dot", "점 하나가 사건 하나입니다. 지금 단계는 테를 둘러 크게 보이게 하고, 멈춘 단계는 빨갛게 칠합니다"),
    ("제목", "title", "무슨 일이 있었는지 한 줄로 적습니다"),
    ("본문", "detail", "누가, 왜 했는지 적습니다. <b>흐름이 멈춘 이유도 여기</b>에 적습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          레일은 점과 점을 <b>잇는</b> 선이고 목록을 감싸는 테두리가 아닙니다. 그래서 첫 점 위쪽과 마지막 점 아래쪽을
          잘라 내야 어디서 시작해서 어디서 끝나는지가 보입니다. 선을 목록 끝까지 그어 두면
          뒤에 <b>단계가 더 있는 것처럼</b> 보여서, 실제로 "다음 단계가 안 보여요"라는 제보가 들어옵니다.</p>''',
  do=ul([
    "배송, 결재, 상태 변화처럼 <b>순서 자체가 정보</b>일 때",
    "사용자가 지금 어느 단계에 있는지를 가장 궁금해할 때",
    "감사 기록처럼 누가 언제 무엇을 했는지 <b>되짚어 봐야</b> 할 때",
  ]),
  dont=ul([
    "순서가 상관없는 목록일 때.  <a href=\"listitem.html\">리스트 아이템</a>을 씁니다",
    "단계가 둘뿐일 때. 선으로 이어 보여 줄 만큼 단계가 많지 않습니다",
    "진행률만 알면 될 때.  <a href=\"../items/progress.html\">프로그레스 바</a> 한 줄이 더 낫습니다",
    "수백 건을 한 번에 보여 줘야 할 때. 이럴 때는 <b>묶어서 접어 두거나</b> 날짜별로 나눕니다",
  ]),
  instead='끝이 정해진 단계면 스테퍼(7부), 진행률이면 <a href="../items/progress.html">프로그레스 바</a>, 순서가 상관없으면 <a href="listitem.html">리스트 아이템</a>.',
  cases=cases([
    (tl([("11월 7일", "주문 접수", "done", False), ("11월 8일", "상품 준비", "done", False), ("11월 9일", "배송 중", "now", False), ("예정", "배송 완료", "next", True)]),
     "배송 추적", "타임라인을 가장 흔히 보는 자리입니다. 사용자는 무엇보다 택배가 <b>지금 어디 있는지</b>를 궁금해합니다"),
    (tl([("방금", "홍길동이 승인했습니다", "now", False), ("2시간 전", "김철수가 금액을 고쳤습니다", "done", False), ("어제", "이영희가 등록했습니다", "done", False)]),
     "활동 기록", "<b>최근 기록이 위</b>에 옵니다. 점은 모두 같은 모양이고 기록은 끝없이 쌓입니다"),
    (tl([("1단계", "계정 정보", "done", False), ("2단계", "계좌 확인", "now", False), ("3단계", "완료", "next", True)]),
     "스테퍼", "끝이 정해져 있어서 <b>남은 단계가 몇 개인지</b> 보입니다"),
  ]),
  s8_title="최소 마크업과 규칙",
  keys_heads="<th>규칙</th><th>지켜야 하는 것</th>",
  code_lede="순서 자체가 정보이므로 순서 있는 목록인 <code>&lt;ol&gt;</code>을 씁니다. 지금 단계를 알리는 데는 <code>aria-current=\"step\"</code> 하나면 충분합니다.",
  code='''&lt;<span class="t">ol</span> <span class="a">class</span>=<span class="s">"tl"</span>&gt;
  &lt;<span class="t">li</span>&gt;
    &lt;<span class="t">time</span> <span class="a">datetime</span>=<span class="s">"2026-11-07T14:02"</span>&gt;11월 7일 14:02&lt;/<span class="t">time</span>&gt;
    &lt;<span class="t">span</span> <span class="a">class</span>=<span class="s">"tl__dot"</span> <span class="a">aria-hidden</span>=<span class="s">"true"</span>&gt;&lt;/<span class="t">span</span>&gt;
    &lt;<span class="t">span</span>&gt;&lt;<span class="t">b</span>&gt;정산 요청&lt;/<span class="t">b</span>&gt;&lt;<span class="t">span</span>&gt;모란상회가 올렸습니다&lt;/<span class="t">span</span>&gt;&lt;/<span class="t">span</span>&gt;
  &lt;/<span class="t">li</span>&gt;
  &lt;<span class="t">li</span> <span class="a">aria-current</span>=<span class="s">"step"</span>&gt;…&lt;/<span class="t">li</span>&gt;   <span class="c">&lt;!-- 지금 단계 --&gt;</span>
&lt;/<span class="t">ol</span>&gt;

<span class="c">/* 레일은 점을 잇는 선이므로 첫 점 위와 마지막 점 아래를 자른다 */</span>
<span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">content</span>: <span class="s">""</span>; <span class="a">position</span>: absolute; <span class="a">top</span>: <span class="a">0</span>; <span class="a">bottom</span>: <span class="a">0</span>; <span class="a">width</span>: <span class="a">2px</span>; }
<span class="t">li</span>:first-child <span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">top</span>: <span class="a">7px</span>; }
<span class="t">li</span>:last-child  <span class="t">.tl__rail</span>::<span class="t">before</span> { <span class="a">bottom</span>: auto; <span class="a">height</span>: <span class="a">7px</span>; }''',
  keys=kbd([
    ("<code>&lt;ol&gt;</code>로 감싼다", "순서가 정보이기 때문입니다. <code>&lt;ul&gt;</code>로 만들면 순서 없는 목록으로 읽힙니다"),
    ("<code>aria-current=\"step\"</code>", "지금 단계 <b>하나</b>에만 붙입니다. 두 곳에 붙이면 어느 쪽이 지금 단계인지 알 수 없습니다"),
    ("<code>&lt;time datetime&gt;</code>", "프로그램이 읽을 수 있는 시각을 따로 적어 둡니다. '방금'이라고만 적혀 있으면 실제로 언제인지 알 수 없습니다"),
    ("점은 숨긴다", "<code>aria-hidden</code>을 붙입니다. 동그라미에는 스크린 리더가 읽어 줄 내용이 없습니다"),
    ("멈춘 자리에 이유를", "맨 아래에 따로 적지 말고 <b>멈춘 항목 안에</b> 씁니다"),
    ("레일 끝을 자른다", "첫 점 위와 마지막 점 아래에 선을 남겨 두면 <b>단계가 더 있는 것처럼</b> 보입니다"),
  ]),
  backend=rows([
    ("타임라인 = 이벤트 로그", "상태를 <code>status</code> 칸 하나에 덮어쓰면 <b>이전 상태 기록이 남지 않습니다.</b> 상태가 바뀔 때마다 한 줄씩 쌓는 표가 따로 있어야 타임라인을 그릴 수 있습니다."),
    ("시각은 UTC 로", "시각은 UTC로 저장하고, 화면에 보여 줄 때 사용자 시간대로 바꿉니다. 두 방식이 섞이면 <b>같은 사건이 서로 다른 두 시각으로</b> 보입니다."),
    ("'방금'은 화면에서", "서버가 '2시간 전'이라는 글을 보내면, 화면을 오래 켜 둔 사람에게는 시간이 지나면서 틀린 정보가 됩니다. 그래서 서버는 <b>절대 시각</b>을 보내고, 화면에서 '2시간 전' 같은 표현으로 바꿔 적습니다."),
    ("몇 개까지", "활동 기록은 끝없이 쌓이므로 최근 20건만 먼저 보내고, 나머지는 <b>더 보기</b>로 이어 받게 합니다.  <a href=\"../items/infinite.html\">무한 스크롤</a>에서 다루는 것과 같은 문제입니다."),
    ("누가 했는지", "시스템이 한 일과 사람이 한 일을 데이터에서 구별해 두면, '자동 검증'과 '담당자 검토'를 화면에서 <b>다르게 그릴</b> 수 있습니다."),
  ]),
  plat_lede="세 플랫폼 모두 타임라인 전용 부품은 없고, 플랫폼마다 비슷한 부품이 조금씩 다릅니다.",
  plats=plats([
    ("웹", "표준 부품 없음",
     tl([("14:02", "요청", "done", False), ("09:21", "검토", "now", False), ("예정", "승인", "next", True)], w="120px"),
     "<code>&lt;ol&gt;</code>에 선과 점을 직접 그리고, 선은 보통 <code>::before</code>로 만듭니다."),
    ("iOS", "Apple HIG",
     '''              <div class="phone" role="img" aria-label="iOS 단계 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:10px;right:8px;top:28px;display:grid;gap:6px">
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center"><span style="width:5px;height:5px;border-radius:99px;background:var(--line-strong)"></span>주문 접수</span>
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center;font-weight:700"><span style="width:5px;height:5px;border-radius:99px;background:var(--accent)"></span>배송 중</span>
                </div>
              </div></div>''',
     "전용 부품이 없어서 배송 추적 같은 화면은 <b>직접 그리고</b>, 단계는 페이지를 넘기는 방식으로 만드는 일이 많습니다."),
    ("안드로이드", "Material 3",
     '''              <div class="phone" role="img" aria-label="Material 단계 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:10px;right:8px;top:28px;display:grid;gap:6px">
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center"><span style="width:5px;height:5px;border-radius:99px;background:var(--line-strong)"></span>주문 접수</span>
                  <span style="font-size:6.5px;display:flex;gap:4px;align-items:center;font-weight:700"><span style="width:5px;height:5px;border-radius:99px;background:var(--accent)"></span>배송 중</span>
                </div>
              </div></div>''',
     "M3에는 타임라인이 없습니다. 예전 가이드에 있던 <b>스테퍼</b>가 가장 비슷하고, 요즘은 직접 만듭니다."),
  ]),
  plat_note="정해진 부품이 없어서 <b>부르는 이름이 특히 많이 갈리는</b> 부품입니다. 타임라인, 진행 단계, 스테퍼, 이력, 추적이 모두 같은 것을 가리킬 수 있습니다. 그래서 먼저 <b>끝이 정해져 있는지</b>를 물으면 스테퍼인지 활동 피드인지 바로 가를 수 있습니다.",
  siblings=siblings("timeline"),
  related='''        <li><a href="../items/progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="../items/listitem.html"><b>리스트 아이템</b><em>5부</em></a></li>
        <li><a href="../items/empty.html"><b>빈 상태</b><em>8부</em></a></li>
        <li><span class="na"><b>스테퍼</b><em>7부</em></span></li>''',
)
