# -*- coding: utf-8 -*-
from parts import *
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

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
  desc="프로그레스 바가 무엇인지, 스피너와는 어떻게 다르고 결정형과 비결정형은 어떻게 갈리는지를 실물과 상태, 해부도로 보여 주는 항목입니다.",
  lede="프로그레스 바는 작업이 <b>얼마나 진행됐고 얼마나 남았는지</b>를 보여 주는 막대입니다. 끝나는 때를 알 때만 쓸 수 있으며, 진행률을 모르면서 막대를 채우면 사실과 다른 정보를 보여 주게 됩니다.",
  live_note='''        <div class="note" style="margin-bottom:0">
          <p><b>세 개 올리기</b>를 눌러 보세요. 두 번째 파일은 올리기가 끝난 뒤 <b>서버 변환</b> 단계로 넘어가는데, 이때
          퍼센트가 사라지고 막대가 좌우로 왔다 갔다 합니다. 프로그레스 바가 <b>결정형</b>에서 <b>비결정형</b>으로 바뀐 것입니다.
          세 번째 파일은 일부러 실패하게 해 두어서, 막대가 빨갛게 바뀌고 <b>그 자리에</b> 다시 시도 버튼이 붙습니다.</p>
        </div>''',
  names=rows([
    ("한국어", "프로그레스 바, 진행 표시줄, 진행률 막대"),
    ("영어", "progress bar, progress indicator"),
    ("같이 쓰는 말", "진행률을 퍼센트로 알 수 있는 것은 <b>결정형</b>(determinate), 알 수 없는 것은 <b>비결정형</b>(indeterminate)이라고 합니다. 연한 바닥은 <b>트랙</b>, 차오르는 부분은 <b>채움</b>(fill)이라고 부릅니다."),
    ("자주 잘못 부르는 이름",
     "<b>로딩 바</b> — 말은 통하지만 결정형인지 비결정형인지가 드러나지 않습니다.<br>"
     "<b>스피너</b> — 끝나는 때를 아는지에 따라 스피너와 프로그레스 바가 갈립니다. 끝나는 때를 모르는데 퍼센트를 지어내면 안 됩니다.<br>"
     "<b>슬라이더</b> — 생김새는 닮았지만 슬라이더는 <b>사용자가 움직이는</b> 입력 부품이고, 프로그레스 바는 사용자가 조작할 수 없습니다."),
  ]),
  states=states([
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:0%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", label="아직 시작 안 한 막대"), "막 시작했을 때(0%)", "막 시작한 상태입니다. 막대가 0에서 한동안 움직이지 않으면 사용자는 멈춘 줄 압니다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span><div style="font-size:7px;color:var(--fg-muted);margin-top:4px">62% · 12초 남음</div></div>', bars="68", label="진행 중인 결정형 막대"), "진행률을 알 때(결정형)", "퍼센트와 남은 시간을 함께 보여 줍니다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line);overflow:hidden"><i style="display:block;height:100%;width:36%;margin-left:28%;background:var(--accent);border-radius:99px"></i></span><div style="font-size:7px;color:var(--fg-muted);margin-top:4px">변환 중… (끝을 모름)</div></div>', bars="68", label="비결정형 막대"), "끝을 모르는 단계(비결정형)", "끝을 모르는 단계에서는 <b>퍼센트를 지우고</b> 막대가 좌우로 왔다 갔다 합니다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:100%;background:#1f8a4c;border-radius:99px"></i></span><div style="font-size:7px;color:#1f8a4c;margin-top:4px;font-weight:700">✓ 끝났습니다</div></div>', bars="68", label="끝난 막대"), "작업이 끝났을 때", "100%에서 잠깐 머문 뒤 결과 화면으로 바뀝니다"),
    (mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:48%;background:var(--danger);border-radius:99px"></i></span><div style="font-size:7px;color:var(--danger);margin-top:4px;font-weight:700">실패 · 다시 시도</div></div>', bars="68", label="실패한 막대"), "작업이 실패했을 때", "멈춘 자리에서 막대가 빨갛게 바뀌므로 어디까지 진행됐었는지 알 수 있습니다"),
    (mini('<div style="margin-top:10px;display:grid;gap:5px"><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:100%;background:#1f8a4c;border-radius:99px"></i></span><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:44%;background:var(--accent);border-radius:99px"></i></span><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:0%;background:var(--accent);border-radius:99px"></i></span></div>', bars="6", label="여러 개가 동시에 도는 모습"), "여러 작업이 함께 진행될 때", "작업마다 막대를 하나씩 둡니다. 전체 진행률 막대를 따로 둘지도 정해야 합니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("이름", "label", "무엇이 진행 중인지 적습니다. 여러 작업이 동시에 진행될 때 이름이 없으면 어느 막대가 어느 작업인지 가릴 수 없습니다"),
    ("퍼센트", "value", "진행률을 숫자로도 보여 줍니다. 막대만 보고는 70%와 75%를 구별하기 어렵습니다"),
    ("취소", "cancel", "시작한 작업을 멈출 수 있게 합니다. 오래 걸리는 작업일수록 꼭 있어야 합니다"),
    ("트랙", "track", "작업 전체의 길이를 나타내며, 채워지지 않은 부분을 보고 남은 양을 읽습니다"),
    ("채움", "fill · bar", "지금까지 진행된 만큼 채웁니다. 채움이 <b>뒤로 가면 안 됩니다</b>. 한 번이라도 줄어들면 사용자가 막대를 믿지 않게 됩니다"),
    ("보조 설명", "detail", "6.2MB / 10MB나 남은 시간을 적습니다. 퍼센트만으로는 얼마나 더 기다려야 할지 가늠하기 어렵습니다"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          남은 시간은 <b>보여 주지 않는 편이 나을 때</b>가 많습니다. 남은 시간이 틀리면 사용자가 바로 알아차리기 때문인데,
          예를 들어 '약 12초'라고 적었는데 30초를 넘기면 사용자는 퍼센트 같은 다른 숫자도 믿지 않게 됩니다.</p>''',
  do=ul([
    "전체 바이트 수를 아는 업로드나 내려받기를 보여 줄 때",
    "'3단계 중 2단계'처럼 전체 단계 수를 아는 작업을 보여 줄 때",
    "10초를 넘기는 일을 기다릴 때. 언제 끝날지 보여야 사용자가 기다릴 수 있습니다",
  ]),
  dont=ul([
    "끝나는 때를 모를 때. 지어낸 퍼센트는 90% 근처에서 멈춰 버립니다",
    "1초 안에 끝나는 일을 기다릴 때. 막대가 깜빡이기만 하고 사라집니다",
    "채움이 <b>뒤로 가게</b> 둘 때. 한 번만 줄어들어도 사용자가 막대를 믿지 않게 됩니다",
    "여러 작업을 막대 하나에 묶어 보여 줄 때. 어느 작업이 막혔는지 알 수 없습니다",
  ]),
  instead='끝나는 때를 모르면 <a href="spinner.html">스피너</a>를 쓰고, 들어올 내용의 모양만 안다면 <a href="skeleton.html">스켈레톤</a>을 씁니다. 기다림 자체를 없앨 수 있으면 <a href="optimistic.html">낙관적 UI</a>가 낫고, 작업이 실패했다면 <a href="error.html">에러 상태</a>로 알립니다.',
  cases=cases([
    (mini('<div style="margin-top:10px"><div style="font-size:7px;margin-bottom:3px">거래내역.csv · 62%</div><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", tall=False, label="업로드 진행 재현"),
     "파일을 올리는 진행률 보여 주기", "전체 바이트 수를 알기 때문에 진행률을 정확하게 보여 줄 수 있습니다"),
    (mini('<div style="margin-top:12px;display:flex;align-items:center;gap:4px"><span style="flex:1;height:4px;border-radius:99px;background:var(--accent)"></span><span style="flex:1;height:4px;border-radius:99px;background:var(--accent)"></span><span style="flex:1;height:4px;border-radius:99px;background:var(--line)"></span></div><div style="font-size:7px;color:var(--fg-muted);margin-top:4px;text-align:center">3단계 중 2단계</div>', bars="68", tall=False, label="단계 표시 재현"),
     "몇 단계 중 몇 번째인지 보여 주기", "진행률을 퍼센트 대신 칸으로 보여 줍니다. 위저드나 가입 흐름에서 흔히 씁니다"),
    (mini('<div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--line)"><i style="display:block;height:100%;width:44%;background:var(--accent)"></i></div>', bars="684", tall=False, label="꼭대기 띠 재현"),
     "화면 전환을 맨 위 띠로 알리기", "화면을 전환할 때 씁니다. 내용이 들어갈 자리를 차지하지 않고, 결정형과 비결정형 모두로 쓸 수 있습니다"),
  ]),
  code_lede="HTML에는 <code>&lt;progress&gt;</code> 요소가 있지만 모양을 바꾸기가 까다롭습니다. 그래서 막대를 직접 그리고 <code>role</code>과 값을 붙이는 방식을 많이 씁니다.",
  code='''<span class="c">&lt;!-- 값을 빼면 비결정형이 된다 --&gt;</span>
&lt;<span class="t">span</span> <span class="a">role</span>=<span class="s">"progressbar"</span>
      <span class="a">aria-valuemin</span>=<span class="s">"0"</span> <span class="a">aria-valuemax</span>=<span class="s">"100"</span> <span class="a">aria-valuenow</span>=<span class="s">"62"</span>
      <span class="a">aria-label</span>=<span class="s">"거래내역 올리는 중"</span>&gt;
  &lt;<span class="t">i</span> <span class="a">style</span>=<span class="s">"width:62%"</span>&gt;&lt;/<span class="t">i</span>&gt;
&lt;/<span class="t">span</span>&gt;

<span class="c">// 끝을 모르는 단계로 넘어가면 값을 지어내지 말고 지운다</span>
bar.removeAttribute(<span class="s">'aria-valuenow'</span>);
bar.classList.add(<span class="s">'prg--ind'</span>);

<span class="c">// 채움은 뒤로 가지 않게 한다</span>
p = Math.max(p, next);''',
  keys_heads="<th>상황</th><th>그때 일어나야 하는 일</th>",
  keys=kbd([
    ("<kbd>Tab</kbd>", "막대 자체는 <b>포커스를 받지 않고</b>, 취소 버튼만 포커스를 받습니다"),
    ("스크린 리더로 읽을 때", "<code>role=\"progressbar\"</code>와 <code>aria-valuenow</code>를 씁니다. 값이 바뀔 때마다 읽어 주면 너무 시끄러우므로 10% 단위로 끊어서 알립니다"),
    ("비결정형으로 바뀌었을 때", "<code>aria-valuenow</code>를 <b>지웁니다.</b> 값을 남겨 두면 그 값에서 멈춘 것처럼 읽힙니다"),
    ("작업을 취소할 때", "<kbd>Esc</kbd>로도 취소할 수 있게 하면 좋습니다"),
    ("끝났을 때", "막대를 결과로 바꿉니다. 100%가 된 막대를 그대로 남겨 두지 않습니다"),
  ]),
  backend=rows([
    ("전체 크기를 아는 전송이면 결정형", "응답에 <code>Content-Length</code>가 있으면 결정형으로, 스트리밍이라 전체 크기를 모르면 비결정형으로 그립니다. <b>막대의 모양이 서버 응답에 전체 크기가 있는지를 그대로 보여 주는 셈입니다.</b>"),
    ("단계마다 바뀌는 결정형과 비결정형", "업로드(결정형)를 마치면 서버 변환(비결정형)을 거쳐 저장(결정형)으로 넘어가는 것처럼, 한 작업 안에서도 단계마다 결정형과 비결정형이 바뀝니다. 데모의 두 번째 파일이 이런 경우입니다."),
    ("남은 시간은 추정치라는 점", "남은 시간은 남은 양을 최근 전송 속도로 나눈 추정치라서, 네트워크 속도가 들쭉날쭉하면 금방 틀립니다. <b>틀린 추정치는 보여 주지 않는 편이 낫습니다.</b>"),
    ("취소하면 요청도 실제로 끊기", "취소를 누르면 AbortController 등으로 요청을 실제로 끊어야 합니다. 화면에서 막대만 지우고 서버는 작업을 계속하면 쓸데없이 비용과 자원을 씁니다."),
  ]),
  plat_lede="플랫폼 대부분은 결정형과 비결정형을 <b>한 부품의 두 모드</b>로 다룹니다.",
  plats=plats([
    ("웹", "<code>&lt;progress&gt;</code>",
     mini('<div style="margin-top:12px"><span style="display:block;height:5px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', bars="68", label="웹 프로그레스 바 재현"),
     "<b>프로그레스 바</b> · 값을 빼면 비결정형이 됩니다. 기본 모양을 꾸미기가 까다로워서 직접 그리는 일이 많습니다."),
    ("iOS", "Apple HIG",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px"><span style="display:block;height:3px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:#0a84ff;border-radius:99px"></i></span></div>', "iOS 프로그레스 바 재현"),
     "<b>프로그레스 바</b>(Progress bar) · 막대가 아주 얇습니다. 끝을 모르는 기다림에는 <b>액티비티 인디케이터</b>라는 다른 이름의 부품을 씁니다."),
    ("안드로이드", "Material 3",
     phone('<div style="position:absolute;left:10px;right:10px;top:44px"><span style="display:block;height:4px;border-radius:99px;background:var(--line)"><i style="display:block;height:100%;width:62%;background:var(--accent);border-radius:99px"></i></span></div>', "안드로이드 프로그레스 인디케이터 재현"),
     "<b>프로그레스 인디케이터</b>(Progress indicator) · <b>Linear</b>(띠)와 <b>Circular</b>(원) 두 가지 모양이 있고, 모양마다 결정형과 비결정형 두 모드가 있습니다."),
  ]),
  plat_note="iOS에서는 <b>끝을 아는 표시와 모르는 표시의 이름이 다르고</b>(프로그레스 바와 액티비티 인디케이터), 안드로이드에서는 <b>같은 이름의 부품에 두 모드</b>가 있습니다. 그래서 iOS 개발자에게 \"프로그레스 띄워 주세요\"라고 하면 '퍼센트를 알 수 있느냐'는 질문이 먼저 돌아옵니다.",
  siblings=siblings("progress"),
  related='''        <li><a href="slider.html"><b>슬라이더</b><em>4부</em></a></li>
        <li><a href="upload.html"><b>파일 업로더와 드롭존</b><em>13부</em></a></li>
        <li><a href="stepper.html"><b>스테퍼(위저드)</b><em>7부</em></a></li>
        <li><span class="na"><b>미터</b><em>5부</em></span></li>''',
)
