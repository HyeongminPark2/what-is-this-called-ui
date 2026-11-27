# -*- coding: utf-8 -*-
from ax13 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L13 = "화면 단위 패턴은 부품 하나가 아니라 사용자가 <b>끝내야 하는 일</b> 하나를 기준으로 나눕니다. 그래서 아래 네 가지를 따져 보면 화면끼리 구별할 수 있습니다."

def files(rows_, w="152px", note="", ok=None, drop=None):
    c = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    out = []
    if drop is not None:
        st = ('border-color:var(--accent);background:var(--accent-soft);color:var(--accent);' if drop else
              'border-color:var(--line);color:var(--fg-muted);')
        out.append('<span style="display:block;border:1.5px dashed ' + st +
                   'border-radius:5px;padding:7px;text-align:center;font-size:7.5px">' +
                   ('여기에 놓으면 됩니다' if drop else '끌어다 놓거나 고르기') + '</span>')
    for name, st, pct, err in rows_:
        cl = 'color:var(--danger);' if err else ''
        bar = ('<span style="display:block;height:3px;border-radius:999px;background:var(--bg);overflow:hidden">'
               '<span style="display:block;height:100%;width:' + str(pct) + '%;border-radius:999px;background:'
               + ('var(--danger)' if err else 'var(--accent)') + '"></span></span>')
        out.append('<span style="display:grid;gap:2px;padding:3px 0;border-top:1px solid var(--line)">'
                   '<span style="display:flex;gap:5px;font-size:8px;' + cl + '">'
                   '<span style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + name + '</span>'
                   '<span style="font-size:7px;white-space:nowrap">' + st + '</span></span>'
                   + bar
                   + ('<span style="font-size:7px;color:var(--danger)">' + err + ' · <u>다시 시도</u></span>' if err else '')
                   + '</span>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="display:grid;gap:2px;border:1px solid ' + c + ';border-radius:6px;'
            'background:var(--surface);padding:6px">' + ''.join(out) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

ANAT = '''              <div class="anat--wide" style="background:var(--bg);border-radius:var(--r2);padding:18px 10px 16px 0">
                <div style="padding-left:26px;display:grid;gap:14px;font-family:var(--mono);font-size:10.5px">
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">형식 · 크기 같은 받는 조건을 <b>미리</b> 적음</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">보내기 전에 걸러 헛되이 올리지 않음</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">파일마다 이름 · 진척 · 상태를 한 줄로</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">한 장이 실패해도 <b>나머지는 그대로 올림</b></div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">실패한 줄에 이유와 '다시 시도'를 표시</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">끌어다 놓기와 함께 <b>고르기 단추</b>도 둠</div>
                </div>
              </div>'''

D = dict(
  slug="upload", ko="파일 올리기", en="File upload",
  desc="파일을 서버에 건네는 화면입니다. 보내기 전에 거르는 법, 파일마다 따로 처리하는 법, 실패한 파일을 다시 올리게 하는 법을 다룹니다.",
  lede="파일 올리기에서 가장 중요한 것은 <b>실패를 언제 알려 주느냐</b>입니다. 파일을 다 올린 뒤에야 거절하면 사용자가 기다린 시간이 모두 헛수고가 됩니다.",
  axes_lede=L13,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>10MB가 넘거나 받지 않는 형식이면 <b>보내기 전에</b> 그 자리에서 알려 줘야 합니다.
          데모는 <b>헛되이 올린 양(MB)</b>을 재서 적는데, 미리 거르기를 끄면 그 숫자가 올라갑니다.<br>
          또 파일은 <b>하나씩 따로</b> 처리해야 합니다. 한 장이 실패했다고 나머지까지 되돌리면
          멀쩡한 네 장을 다시 올려야 하는데, '파일마다 따로 처리'를 끄면 데모가 그렇게 동작합니다.<br>
          실패한 줄에는 <b>왜 실패했는지와 다시 시도</b> 버튼이 함께 있어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "파일 올리기, 업로드, 첨부, 파일 첨부"),
    ("영어", "file upload, attachment, drag and drop upload"),
    ("같이 쓰는 말",
     "파일을 끌어다 놓는 자리를 <b>드롭존</b>(dropzone)이라 하고, 큰 파일을 여러 토막으로 나눠 보내는 방식을 "
     "<b>청크 업로드</b>(chunked), 끊긴 곳부터 이어 보내는 방식을 <b>이어 올리기</b>(resumable)라고 합니다. "
     "서버를 거치지 않고 저장소로 바로 보내도록 발급하는 주소는 <b>프리사인 URL</b>(presigned URL)이라고 합니다."),
    ("자주 잘못 부르는 이름",
     "<b>드롭존</b> — 드롭존은 파일을 <b>끌어다 놓는 자리</b>이고, 파일 올리기 흐름 전체를 가리키는 말이 아닙니다.<br>"
     "<b>내보내기</b> — <a href=\"exportdata.html\">내보내기</a>는 데이터가 <b>반대 방향</b>으로 나가는 일입니다.<br>"
     "<b>프로그레스 바</b> — <a href=\"progress.html\">프로그레스 바</a>는 올리기 화면 안에 들어가는 <b>부품</b>입니다."),
  ]),
  axes=ax("파일 올리기"),
  oneline="<b>파일은 보내기 전에 거르세요.</b> 파일의 크기와 형식은 고르는 순간 브라우저가 이미 알고 있습니다.",
  do_title="파일 올리기 화면을 만들 때 할 일",
  dont_title="파일 올리기를 잘못 만드는 경우",
  instead_title="함께 보면 좋은 항목",
  s4_title="파일 올리기의 상태", s4_hint="실패한 경우까지 모두 만들어야 하는 상태",
  states=states([
    (files([], "152px", "받는 조건을 미리 적음", True, drop=False),
     "처음 열었을 때", "받을 수 있는 <b>형식과 크기</b>를 적어 둡니다"),
    (files([], "152px", "놓을 수 있다는 표시", True, drop=True),
     "파일을 끌어오는 중", "파일을 <b>놓을 자리</b>가 밝아집니다"),
    (files([("영수증_01.jpg", "62%", 62, ""), ("영수증_02.jpg", "28%", 28, "")], "152px", "파일마다 따로 셈", True),
     "파일을 올리는 중", "파일 <b>줄마다</b> 진척을 따로 보여 줍니다"),
    (files([("영수증_01.jpg", "완료", 100, ""), ("정산내역.pdf", "안 보냄", 0, "10MB 가 넘습니다 (14.8MB)")],
           "152px", "보내기 전에 걸러 냄", True),
     "보내기 전에 걸렀을 때", "조건에 맞지 않는 파일은 <b>한 바이트도</b> 올리지 않습니다"),
    (files([("영수증_01.jpg", "완료", 100, ""), ("정산내역.pdf", "거절됨", 100, "다 올린 뒤 거절당함")],
           "152px", "14.8MB를 헛되이 올림", False),
     "다 올린 뒤 거절당했을 때", "다 올린 뒤에 거절당해 <b>기다린 시간이 헛수고가 됩니다</b>"),
    (files([("영수증_01.jpg", "되돌림", 0, ""), ("정산내역.pdf", "거절됨", 100, "한 장 때문에 전부 취소")],
           "152px", "멀쩡한 것까지 다시 올림", False),
     "한 장 때문에 묶음 전체를 되돌릴 때", "한 장 때문에 <b>나머지 파일까지</b> 취소됩니다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("받는 조건", "미리 적기", "형식 · 크기 · 장수를 미리 적어 둡니다"),
    ("미리 거르기", "보내기 전", "크기와 형식은 브라우저가 <b>이미 알고 있으므로</b> 보내기 전에 거릅니다"),
    ("파일별 줄", "이름·진척·상태", "진척과 상태를 <b>파일 단위</b>로 보여 줍니다"),
    ("따로 처리", "나머지는 그대로 올리기", "한 장이 실패해도 <b>나머지는 그대로 올라가게</b> 합니다"),
    ("실패한 줄", "이유 + 다시 시도", "무엇을 고쳐야 하는지 알려 주고 다시 시도할 수 있게 합니다"),
    ("고르기 단추", "드롭존과 같이 두기", "끌어다 놓기만 있으면 <b>키보드로는 올릴 수 없습니다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>끌어다 놓기만</b> 만들어 두는 실수가 흔한데,
          그러면 마우스를 쓰지 않는 사람은 파일을 올릴 방법이 없습니다.
          드롭존 안에 <b>'파일 고르기' 단추</b>를 같이 두면 키보드로도 올릴 수 있고,
          원래 있던 <code>&lt;input type="file"&gt;</code>을 쓰면 되므로 만드는 품도 거의 들지 않습니다.<br>
          또 올리는 중에는 사용자가 <b>떠나지 못하게</b> 막기보다
          <b>떠나면 어떻게 되는지</b> 알려 주는 편이 낫습니다.
          '올리는 중입니다. 지금 나가면 멈춥니다' 한 줄이면 충분합니다.</p>''',
  do=ul([
    "받는 <b>형식·크기·장수</b>를 드롭존에 적어 둘 때",
    "보내기 전에 <b>거르고</b> 그 자리에서 이유를 알려 줄 때",
    "드롭존 안에 <b>'파일 고르기' 단추</b>를 같이 둘 때",
  ]),
  dont=ul([
    "다 올린 뒤에야 거절할 때. 사용자가 <b>기다린 시간이 헛수고가 됩니다</b>",
    "한 장이 실패했다고 <b>전부 되돌릴</b> 때",
    "끌어다 놓기만 만들 때. <b>키보드로는 올릴 수 없습니다</b>",
    "진척을 <b>전체 합계</b>로만 보여 줄 때. 어느 파일이 문제인지 알 수 없습니다",
  ]),
  instead='데이터가 반대 방향으로 나가는 일은 <a href="exportdata.html">내보내기</a>에서, 진척 막대 부품은 <a href="progress.html">프로그레스 바</a>에서 다룹니다. 입력값을 검사하는 규칙은 <a href="validation.html">입력 검증</a>에서, 오류를 알리는 문장은 <a href="errortext.html">오류 문구</a>에서 설명합니다.',
  cases=cases([
    (files([("영수증_01.jpg", "완료", 100, ""), ("영수증_02.jpg", "완료", 100, "")], "150px", "", True),
     "영수증 여러 장 첨부하기", "여러 장을 <b>한 번에</b> 올립니다"),
    (files([("프로필.png", "완료", 100, "")], "150px", "", True),
     "사진 한 장 올리기", "올린 사진의 <b>미리보기</b>를 함께 보여 줍니다"),
    (files([("거래내역_11월.csv", "검사 중", 100, "")], "150px", "", None),
     "데이터 파일 올리고 검사하기", "올린 뒤에 <b>내용 검사</b> 단계가 한 번 더 있습니다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="구현할 때 지킬 최소 규칙",
  keys_heads="<th>키와 마크업</th><th>처리하는 방법</th>",
  code_lede="원래 있는 <code>&lt;input type=\"file\"&gt;</code>을 기본으로 두고, 끌어다 놓기는 그 위에 덧붙입니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"f"</span>&gt;영수증 올리기&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"f"</span> <span class="a">type</span>=<span class="s">"file"</span> <span class="a">multiple</span>
       <span class="a">accept</span>=<span class="s">"image/jpeg,image/png,application/pdf"</span>
       <span class="a">aria-describedby</span>=<span class="s">"rule"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"rule"</span>&gt;JPG · PNG · PDF · 한 장 10MB 까지&lt;/<span class="t">p</span>&gt;

&lt;<span class="t">ul</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;…올린 파일 목록…&lt;/<span class="t">ul</span>&gt;

<span class="c">// 브라우저가 이미 크기와 형식을 아니까 보내기 전에 거른다</span>
<span class="t">for</span> (<span class="t">const</span> f <span class="t">of</span> input.files) {
  <span class="t">if</span> (f.size &gt; <span class="a">10</span> * <span class="a">1024</span> * <span class="a">1024</span>) { reject(f, <span class="s">'10MB 가 넘습니다'</span>); <span class="t">continue</span>; }
  upload(f);                       <span class="c">// 파일마다 따로 보낸다</span>
}''',
  keys=kbd([
    ("Tab · Enter", "<code>&lt;input type=\"file\"&gt;</code>은 <b>따로 만들지 않아도</b> 키보드로 열립니다"),
    ("<code>accept</code>", "파일 고르기 창에서 맞는 형식만 <b>미리 걸러</b> 보여 줍니다. 다만 사용자가 다른 파일을 고를 수도 있으므로 검사는 따로 해야 합니다"),
    ("<code>aria-describedby</code>", "받는 조건을 입력 칸과 <b>연결해</b> 함께 읽히게 합니다"),
    ("<code>aria-live=\"polite\"</code>", "올린 결과를 스크린 리더로 <b>소리 내어</b> 알립니다. 진척률은 계속 바뀌므로 넣지 않습니다"),
    ("드롭존에 파일을 놓게 하기", "<code>dragover</code>에서 <b><code>preventDefault()</code></b>를 불러야 파일을 놓을 수 있습니다"),
    ("확인하는 방법", "마우스를 쓰지 않고 <b>Tab만으로</b> 파일을 올려 봅니다"),
  ]),
  backend=rows([
    ("브라우저와 서버에서 두 번 검사하기", "브라우저에서 거르는 것은 사용자를 위한 <b>안내</b>이고, 실제로 막는 것은 <b>서버 검사</b>입니다. 브라우저 검사는 우회할 수 있으므로 둘 다 필요합니다."),
    ("저장소로 바로 보내기", "파일이 서버를 거치지 않고 저장소로 바로 가게 하려면 <b>프리사인 URL</b>을 내려 줍니다. 그러면 서버가 쓰는 대역폭이 크게 줄어듭니다."),
    ("큰 파일은 나눠 보내기", "100MB를 넘는 파일은 <b>토막으로 나눠</b> 보내고, 중간에 끊기면 끊긴 곳부터 이어 올립니다."),
    ("올린 뒤 바이러스·내용 검사하기", "올린 뒤에 검사가 더 있다면 <b>'검사 중'</b> 상태를 따로 둬야 합니다. 검사 중인 파일은 아직 완료된 것이 아니기 때문입니다."),
  ]),
  plat_lede="플랫폼마다 파일을 <b>고르는 창</b>을 누가 띄우는지가 다릅니다.",
  plats=plats([
    ("웹", "input[type=file]",
     files([("영수증_01.jpg", "완료", 100, "")], "110px", "", True, drop=False),
     "세 플랫폼 가운데 끌어다 놓기가 <b>자연스럽게</b> 쓰이는 곳은 웹뿐이라서, 데스크톱에서는 기본으로 둡니다."),
    ("iOS", "포토 피커 · 파일 앱",
     '''              <div class="phone" role="img" aria-label="iOS 사진 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>PHPickerViewController</code>는 <b>앱에 사진 권한을 주지 않고도</b> 사용자가 고른 사진만 앱에 건넵니다."),
    ("안드로이드", "Photo Picker · SAF",
     '''              <div class="phone" role="img" aria-label="안드로이드 파일 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;gap:3px">
                  <span style="height:7px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:7px;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<b>Photo Picker</b>와 <b>SAF</b>가 같은 일을 하며, 마찬가지로 권한 없이 사용자가 고른 파일만 건넵니다."),
  ]),
  plat_note="모바일 OS가 <b>권한 없이 고른 것만 건네는</b> 방식을 만들어 둔 것은 그대로 본받을 만합니다. 사진 전체에 접근하게 하는 대신 <b>필요한 파일만</b> 받기 때문입니다. 웹의 <code>&lt;input type=\"file\"&gt;</code>은 원래 이렇게 동작하므로, 웹에서는 따로 애쓰지 않아도 같은 효과를 얻습니다. 대신 웹에는 <b>끌어다 놓기</b>가 있는데, 폰에서는 파일을 끌어다 놓을 수 없으니 <b>고르기 단추를 늘 같이</b> 두는 것이 안전합니다.",
  siblings=siblings("upload"),
  related='''        <li><a href="progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
