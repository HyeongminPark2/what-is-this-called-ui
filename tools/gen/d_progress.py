# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd, table

WAIT = table(
  ["끝나는 때를 아나", "들어올 자리를 잡나", "사용자가 기다리나", "화면이 덜컥거리나"],
  [["스피너", "모른다", "안 잡는다", "기다린다", "덜컥거린다"],
   ["스켈레톤", "모른다", "잡는다", "기다린다", "안 덜컥거린다"],
   ["프로그레스 바", "안다", "잡기도 한다", "기다린다", "안 덜컥거린다"],
   ["낙관적 UI", "해당 없음", "잡는다", "안 기다린다", "안 덜컥거린다"]],
  me="프로그레스")

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:10px">
                <div style="background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:14px 26px 16px">
                  <div style="display:flex;align-items:center;gap:26px;margin-bottom:14px">
                    <span class="pin-out" data-pin="1" style="flex:1;font-size:11.5px;font-weight:650">거래내역_2026_11.csv</span>
                    <span class="pin-out" data-pin="2" style="font-size:11px;color:var(--fg-muted)">62%</span>
                    <span class="pin-tr" data-pin="3" style="color:var(--fg-muted);font-size:13px;line-height:1">&times;</span>
                  </div>
                  <span class="pin-out" data-pin="4" style="display:block;height:9px;border-radius:99px;background:var(--line)">
                    <i class="pin-tr" data-pin="5" style="display:block;height:100%;width:62%;border-radius:99px;background:var(--accent)"></i>
                  </span>
                  <div class="pin-out" data-pin="6" style="font-size:10.5px;color:var(--fg-muted);margin-top:12px">6.2MB / 10MB · 약 12초 남음</div>
                </div>
              </div>'''

D = dict(
  slug="progress", ko="프로그레스 바", en="Progress bar · Progress indicator",
  desc="프로그레스 바가 무엇이고 스피너와 어떻게 다른지, 결정형과 비결정형의 차이를 실물과 상태와 해부도로 보여주는 항목.",
  lede="<b>얼마나 왔고 얼마나 남았는지</b>를 보여 주는 막대. 끝나는 때를 알 때만 쓸 수 있고, 모르면서 쓰면 거짓말이 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>세 개 올리기</b>를 눌러 보세요. 두 번째 파일은 올리기가 끝난 뒤 <b>서버 변환</b>으로 넘어가면서
          퍼센트가 사라지고 막대가 왔다 갔다 합니다 — <b>결정형</b>에서 <b>비결정형</b>으로 바뀌는 순간입니다.
          세 번째는 일부러 실패합니다. 막대가 빨개지고 <b>그 자리에</b> 다시 시도가 붙습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "프로그레스 바, 진행 표시줄, 진행률 막대"),
    ("영어", "progress bar, progress indicator"),
    ("같이 쓰는 말", "퍼센트를 아는 것이 <b>결정형</b>(determinate), 모르는 것이 <b>비결정형</b>(indeterminate). 연한 바닥이 <b>트랙</b>, 차오르는 부분이 <b>채움</b>(fill)."),
    ("자주 잘못 부름",
     "<b>로딩 바</b> — 통하기는 하지만 결정형인지 아닌지가 안 드러납니다.<br>"
     "<b>스피너</b> — 끝나는 때를 아는가로 갈립니다. 모르면서 퍼센트를 지어내면 안 됩니다.<br>"
     "<b>슬라이더</b> — 생김새는 닮았지만 슬라이더는 <b>사용자가 움직이는</b> 입력 부품입니다. 프로그레스 바는 못 만집니다."),
  ]),
  axes=WAIT,
  oneline="프로그레스 바는 <b>끝나는 때를 알 때만</b> 씁니다. 모르면서 퍼센트를 보여 주면 90%에서 멈춰 사용자를 더 답답하게 만듭니다.",
  states=states([
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:0%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", label="아직 시작 안 한 막대"), "0%", "시작 직후. 0에서 한동안 안 움직이면 멈춘 줄 안다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span><div style="font-size:7px;color:var(--fg-muted);margin-top:4px">62% · 12초 남음</div></div>', bars="68", label="진행 중인 결정형 막대"), "결정형", "퍼센트와 남은 시간을 같이 보여 준다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line);overflow:hidden"><i style="display:block;height:100%;width:36%;margin-left:28%;background:var(--accent);border-radius:99px"></i></span><div style="font-size:7px;color:var(--fg-muted);margin-top:4px">변환 중… (끝을 모름)</div></div>', bars="68", label="비결정형 막대"), "비결정형", "끝을 모르는 단계. <b>퍼센트를 지우고</b> 왔다 갔다 한다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:100%;background:#1f8a4c;border-radius:99px"></i></span><div style="font-size:7px;color:#1f8a4c;margin-top:4px;font-weight:700">✓ 끝났습니다</div></div>', bars="68", label="끝난 막대"), "끝남", "100%에서 잠깐 머문 뒤 결과로 바뀐다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:48%;background:var(--danger);border-radius:99px"></i></span><div style="font-size:7px;color:var(--danger);margin-top:4px;font-weight:700">실패 · 다시 시도</div></div>', bars="68", label="실패한 막대"), "실패", "멈춘 그 자리에서 빨개진다. 어디까지 갔는지가 남는다"),
    (mini('<div style="margin-top:10px;display:grid;gap:5px"><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:100%;background:#1f8a4c;border-radius:99px"></i></span><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:44%;background:var(--accent);border-radius:99px"></i></span><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:0%;background:var(--accent);border-radius:99px"></i></span></div>', bars="6", label="여러 개가 동시에 도는 모습"), "여러 개", "건마다 하나씩. 전체 진행률을 따로 둘지 정해야 한다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이름", "label", "무엇이 진행 중인지. 여러 개가 동시에 돌면 이게 없으면 못 가린다"),
    ("퍼센트", "value", "숫자로도 보여 준다. 막대만으로는 70과 75를 구별 못 한다"),
    ("취소", "cancel", "되돌릴 수 있어야 한다. 긴 작업일수록 꼭 있어야 한다"),
    ("트랙", "track", "전체 길이. 남은 양이 여기서 읽힌다"),
    ("채움", "fill · bar", "지금까지 온 만큼. <b>뒤로 가면 안 된다</b> — 신뢰가 바로 깨진다"),
    ("보조 설명", "detail", "6.2MB / 10MB, 남은 시간. 퍼센트만으로는 체감이 안 온다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          남은 시간은 <b>안 보여 주는 쪽이 나을 때</b>가 많습니다. 틀리면 바로 티가 나서,
          '약 12초'가 30초를 넘기는 순간 나머지 숫자까지 못 믿게 됩니다.</p>''',
  do=ul([
    "바이트 수를 아는 업로드·내려받기",
    "단계 수를 아는 작업 — 3단계 중 2단계",
    "10초를 넘기는 일 — 끝이 보여야 기다릴 수 있습니다",
  ]),
  dont=ul([
    "끝나는 때를 모를 때 — 지어낸 퍼센트는 90%에서 멈춥니다",
    "1초 안에 끝나는 일 — 깜빡임만 남습니다",
    "채움이 <b>뒤로 가게</b> 두기 — 한 번만 그래도 못 믿게 됩니다",
    "여러 작업을 막대 하나에 뭉뚱그리기 — 어느 게 막힌 건지 알 수 없습니다",
  ]),
  instead='끝을 모르면 <a href="spinner.html">스피너</a>, 들어올 모양만 알면 <a href="skeleton.html">스켈레톤</a>, 기다림 자체를 없앨 수 있으면 <a href="optimistic.html">낙관적 UI</a>, 실패했으면 <a href="error.html">에러 상태</a>.',
  cases=cases([
    (mini('<div style="margin-top:10px"><div style="font-size:7px;margin-bottom:3px">거래내역.csv · 62%</div><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", tall=False, label="업로드 진행 재현"),
     "파일 올리기", "바이트 수를 알아 가장 정직하게 쓸 수 있는 자리"),
    (mini('<div style="margin-top:12px;display:flex;align-items:center;gap:4px"><span style="flex:1;height:4px;border-radius:99px;background:var(--accent)"></span><span style="flex:1;height:4px;border-radius:99px;background:var(--accent)"></span><span style="flex:1;height:4px;border-radius:99px;background:var(--line)"></span></div><div style="font-size:7px;color:var(--fg-muted);margin-top:4px;text-align:center">3단계 중 2단계</div>', bars="68", tall=False, label="단계 표시 재현"),
     "단계 표시", "퍼센트가 아니라 칸으로. 위저드·가입 흐름에서 흔하다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--line)"><i style="display:block;height:100%;width:44%;background:var(--accent)"></i></div>', bars="684", tall=False, label="꼭대기 띠 재현"),
     "꼭대기 띠", "화면 전환에 쓴다. 자리를 안 뺏고 결정형·비결정형 둘 다 된다"),
  ]),
  code_lede="<code>&lt;progress&gt;</code>가 있지만 모양을 바꾸기 까다로워서, 직접 그리고 <code>role</code>과 값을 붙이는 쪽을 많이 씁니다.",
  code='''<span class="c">&lt;!-- 값을 빼면 비결정형이 된다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"progressbar"</span>
      <span class="a">aria-valuemin</span>=<span class="s">"0"</span> <span class="a">aria-valuemax</span>=<span class="s">"100"</span> <span class="a">aria-valuenow</span>=<span class="s">"62"</span>
      <span class="a">aria-label</span>=<span class="s">"거래내역 올리는 중"</span>&gt;
  &lt;<span class="t">i</span> <span class="a">style</span>=<span class="s">"width:62%"</span>&gt;&lt;/<span class="t">i</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">// 끝을 모르는 단계로 넘어가면 값을 지운다 — 지어내지 않는다</span>
bar.removeAttribute(<span class="s">'aria-valuenow'</span>);
bar.classList.add(<span class="s">'prg--ind'</span>);

<span class="c">// 채움은 뒤로 가지 않게 한다</span>
p = Math.max(p, next);''',
  keys=kbd([
    ("<kbd>Tab</kbd>", "막대 자체는 <b>포커스를 받지 않는다.</b> 취소 버튼은 받는다"),
    ("스크린 리더", "<code>role=\"progressbar\"</code> + <code>aria-valuenow</code>. 값이 바뀔 때마다 읽으면 시끄러우니 10% 단위로 끊는다"),
    ("비결정형", "<code>aria-valuenow</code>를 <b>지운다.</b> 남겨 두면 그 값에서 멈춘 것처럼 읽힌다"),
    ("취소", "<kbd>Esc</kbd>로도 취소할 수 있게 하면 좋다"),
    ("끝났을 때", "결과로 바꾼다. 100%인 막대를 그대로 두지 않는다"),
  ]),
  backend=rows([
    ("결정형 = 전체 크기를 아는 전송", "<code>Content-Length</code>가 있으면 결정형, 스트리밍이라 모르면 비결정형입니다. <b>모양이 서버 응답의 성질을 그대로 드러냅니다.</b>"),
    ("단계마다 성질이 바뀐다", "업로드(결정형) → 서버 변환(비결정형) → 저장(결정형)처럼 한 작업 안에서도 바뀝니다. 데모의 두 번째 파일이 그 경우입니다."),
    ("남은 시간 = 추정치", "최근 속도로 나눈 값일 뿐입니다. 네트워크가 출렁이면 바로 틀립니다. <b>틀린 추정은 안 보여 주는 쪽이 낫습니다.</b>"),
    ("취소 = 중단 신호", "취소를 누르면 요청을 실제로 끊어야 합니다(AbortController). 화면만 지우고 서버는 계속 돌면 돈과 자원이 샙니다."),
  ]),
  plat_lede="결정형과 비결정형을 <b>한 부품의 두 모드</b>로 보는 곳이 많습니다.",
  plats=plats([
    ("웹", "<code>&lt;progress&gt;</code>",
     mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", label="웹 프로그레스 바 재현"),
     "<b>프로그레스 바</b> · 값을 빼면 비결정형이 됩니다. 기본 모양을 꾸미기 까다로워 직접 그리는 일이 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px"><span style="display:block;height:3px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:#0a84ff;border-radius:99px"></i></span></div>', "iOS 프로그레스 바 재현"),
     "<b>프로그레스 바</b>(Progress bar) · 아주 얇습니다. 끝을 모르는 것은 <b>액티비티 인디케이터</b>로 이름이 아예 갈립니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px"><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', "안드로이드 프로그레스 인디케이터 재현"),
     "<b>프로그레스 인디케이터</b>(Progress indicator) · <b>Linear</b>(띠)와 <b>Circular</b>(원) 두 모양, 각각 결정형·비결정형 두 모드로 정리돼 있습니다."),
  ]),
  plat_note="iOS 는 <b>끝을 아는 것과 모르는 것의 이름이 다르고</b>(프로그레스 바 / 액티비티 인디케이터), 안드로이드는 <b>같은 이름의 두 모드</b>입니다. \"프로그레스 띄워 주세요\"가 iOS 에서는 '퍼센트를 아느냐'는 되물음을 부릅니다.",
  siblings=siblings("progress"),
  related='''        <li><span class="na"><b>슬라이더</b><em>4부</em></span></li>
        <li><span class="na"><b>파일 업로더와 드롭존</b><em>4부</em></span></li>
        <li><span class="na"><b>스테퍼(위저드)</b><em>7부</em></span></li>
        <li><span class="na"><b>미터</b><em>5부</em></span></li>''',
)
