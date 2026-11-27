# -*- coding: utf-8 -*-
from ax13 import ax
from _tx import one, code, txt, mono
from tmpl import siblings, states, cases, pins, plats, rows, ul, kbd

L13 = "화면 단위 패턴은 부품이 아니라 <b>끝내야 하는 일</b>입니다. 이 네 가지만 물어보면 갈립니다."

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
                  <div class="pin-out" data-pin="1" style="color:var(--fg-muted)">받는 조건을 <b>미리</b> 적는다 — 형식 · 크기</div>
                  <div class="pin-out" data-pin="2" style="color:var(--accent)">보내기 전에 거른다 — 헛되이 올리지 않는다</div>
                  <div class="pin-out" data-pin="3" style="color:var(--fg-muted)">파일마다 줄 하나 — 이름 · 진척 · 상태</div>
                  <div class="pin-out" data-pin="4" style="color:var(--danger)">한 장이 실패해도 <b>나머지는 살린다</b></div>
                  <div class="pin-out" data-pin="5" style="color:var(--fg-muted)">실패한 줄에 이유와 '다시 시도'</div>
                  <div class="pin-out" data-pin="6" style="color:var(--fg-muted)">끌어다 놓기 말고 <b>고르기 단추</b>도 둔다</div>
                </div>
              </div>'''

D = dict(
  slug="upload", ko="파일 올리기", en="File upload",
  desc="파일을 건네는 화면. 보내기 전 거르기, 파일마다 따로 처리, 실패한 줄 되살리기.",
  lede="올리기의 핵심은 <b>언제 실패를 알려 주느냐</b>입니다. 다 올린 뒤에 거절하면 기다린 시간이 통째로 버려집니다.",
  axes_lede=L13,
  live_note='''        <div class="note" style="margin-bottom:0">
          <p>10MB 가 넘거나 받지 않는 형식이면 <b>보내기 전에</b> 그 자리에서 알려 줘야 합니다 —
          데모가 <b>헛되이 올린 양(MB)</b>을 재서 적습니다. 미리 거르기를 끄면 그 숫자가 올라갑니다.<br>
          <b>파일마다 따로</b> 처리해야 합니다. 한 장이 실패했다고 나머지까지 되돌리면
          멀쩡한 네 장을 다시 올려야 합니다 — '파일마다 따로 처리'를 끄면 그렇게 동작합니다.<br>
          실패한 줄에는 <b>왜 실패했는지와 다시 시도</b>가 같이 있어야 합니다.</p>
        </div>''',
  names=rows([
    ("한국어", "파일 올리기, 업로드, 첨부, 파일 첨부"),
    ("영어", "file upload, attachment, drag and drop upload"),
    ("같이 쓰는 말",
     "끌어다 놓는 자리를 <b>드롭존</b>(dropzone), 큰 파일을 토막 내 보내는 방식을 "
     "<b>청크 업로드</b>(chunked), 끊겼다가 이어 보내는 것을 <b>이어 올리기</b>(resumable)라 합니다. "
     "서버를 거치지 않고 저장소로 바로 보내는 길은 <b>프리사인 URL</b>(presigned URL)입니다."),
    ("자주 잘못 부름",
     "<b>드롭존</b> — 드롭존은 <b>끌어다 놓는 자리</b>일 뿐, 올리기 전체가 아닙니다.<br>"
     "<b>내보내기</b> — <a href=\"exportdata.html\">내보내기</a>는 <b>반대 방향</b>입니다.<br>"
     "<b>프로그레스 바</b> — <a href=\"progress.html\">프로그레스 바</a>는 그 안에 들어가는 <b>부품</b>입니다."),
  ]),
  axes=ax("파일 올리기"),
  oneline="<b>보내기 전에 거르세요.</b> 크기와 형식은 브라우저가 이미 알고 있습니다.",
  s4_title="상태", s4_hint="실패까지 다 만들어야 한다",
  states=states([
    (files([], "152px", "받는 조건을 미리 적는다", True, drop=False),
     "처음", "<b>형식과 크기</b>를 적어 둔다"),
    (files([], "152px", "놓을 수 있다는 표시", True, drop=True),
     "끌어온 중", "<b>놓을 자리</b>가 밝아진다"),
    (files([("영수증_01.jpg", "62%", 62, ""), ("영수증_02.jpg", "28%", 28, "")], "152px", "파일마다 따로 센다", True),
     "올리는 중", "<b>줄마다</b> 진척"),
    (files([("영수증_01.jpg", "완료", 100, ""), ("정산내역.pdf", "안 보냄", 0, "10MB 가 넘습니다 (14.8MB)")],
           "152px", "보내기 전에 걸렀다", True),
     "미리 거름", "<b>한 바이트도</b> 안 올렸다"),
    (files([("영수증_01.jpg", "완료", 100, ""), ("정산내역.pdf", "거절됨", 100, "다 올리고 거절당했다")],
           "152px", "14.8MB 를 헛되이 올렸다", False),
     "뒤늦은 거절", "<b>기다린 시간이 버려진다</b>"),
    (files([("영수증_01.jpg", "되돌림", 0, ""), ("정산내역.pdf", "거절됨", 100, "한 장 때문에 전부 취소")],
           "152px", "멀쩡한 것까지 다시", False),
     "묶음 되돌림", "<b>나머지까지</b> 날아간다"),
  ]),
  anat=ANAT,
  pins=pins([
    ("받는 조건", "미리 적기", "형식 · 크기 · 장수"),
    ("미리 거르기", "보내기 전", "브라우저가 <b>이미 안다</b>"),
    ("줄마다", "이름·진척·상태", "<b>파일 단위</b>로 본다"),
    ("따로 처리", "나머지 살리기", "한 장 실패가 <b>전부를 망치지 않게</b>"),
    ("실패한 줄", "이유 + 다시 시도", "무엇을 고쳐야 하는지"),
    ("고르기 단추", "같이 두기", "끌어다 놓기만으로는 <b>키보드가 못 쓴다</b>"),
  ]),
  anat_note='''        <p style="font-size:13px;color:var(--fg-muted);margin:var(--s3) 0 0">
          <b>끌어다 놓기만</b> 만들어 두는 실수가 흔합니다.
          마우스가 없는 사람은 파일을 올릴 길이 없어집니다 —
          드롭존 안에 <b>'파일 고르기' 단추</b>를 같이 두면 그 길이 생기고,
          만드는 품도 거의 안 듭니다(원래 있던 <code>&lt;input type="file"&gt;</code> 입니다).<br>
          그리고 올리는 중에는 <b>떠나지 못하게</b> 하기보다
          <b>떠나면 어떻게 되는지</b>를 알려 주는 편이 낫습니다 —
          '올리는 중입니다. 지금 나가면 멈춥니다' 한 줄이면 충분합니다.</p>''',
  do=ul([
    "<b>형식·크기·장수</b>를 드롭존에 적어 두기",
    "보내기 전에 <b>거르고</b> 그 자리에서 이유 말하기",
    "드롭존 안에 <b>'파일 고르기' 단추</b> 같이 두기",
  ]),
  dont=ul([
    "다 올린 뒤에 거절하기 — <b>기다린 시간이 버려진다</b>",
    "한 장이 실패했다고 <b>전부 되돌리기</b>",
    "끌어다 놓기만 만들기 — <b>키보드로는 못 올린다</b>",
    "진척을 <b>전체 합계</b>로만 보여 주기 — 어느 파일이 문제인지 모른다",
  ]),
  instead='반대 방향은 <a href="exportdata.html">내보내기</a>, 진척 막대 자체는 <a href="progress.html">프로그레스 바</a>, 칸 검사 규칙은 <a href="validation.html">입력 검증</a>, 오류 문구는 <a href="errortext.html">오류 문구</a>.',
  cases=cases([
    (files([("영수증_01.jpg", "완료", 100, ""), ("영수증_02.jpg", "완료", 100, "")], "150px", "", True),
     "영수증 첨부", "여러 장을 <b>한 번에</b>"),
    (files([("프로필.png", "완료", 100, "")], "150px", "", True),
     "사진 한 장", "<b>미리보기</b>를 같이 보인다"),
    (files([("거래내역_11월.csv", "검사 중", 100, "")], "150px", "", None),
     "데이터 올리기", "올린 뒤 <b>내용 검사</b>가 더 있다"),
  ]),
  s8_title="최소 마크업과 키보드", s8_hint="이 화면의 계약서",
  code_lede="원래 있는 <code>&lt;input type=\"file\"&gt;</code> 이 뼈대입니다. 끌어다 놓기는 그 위에 얹습니다.",
  code='''&lt;<span class="t">label</span> <span class="a">for</span>=<span class="s">"f"</span>&gt;영수증 올리기&lt;/<span class="t">label</span>&gt;
&lt;<span class="t">input</span> <span class="a">id</span>=<span class="s">"f"</span> <span class="a">type</span>=<span class="s">"file"</span> <span class="a">multiple</span>
       <span class="a">accept</span>=<span class="s">"image/jpeg,image/png,application/pdf"</span>
       <span class="a">aria-describedby</span>=<span class="s">"rule"</span>&gt;
&lt;<span class="t">p</span> <span class="a">id</span>=<span class="s">"rule"</span>&gt;JPG · PNG · PDF · 한 장 10MB 까지&lt;/<span class="t">p</span>&gt;

&lt;<span class="t">ul</span> <span class="a">aria-live</span>=<span class="s">"polite"</span>&gt;…올린 파일 목록…&lt;/<span class="t">ul</span>&gt;

<span class="c">// 보내기 전에 거른다 — 브라우저가 이미 크기와 형식을 안다</span>
<span class="t">for</span> (<span class="t">const</span> f <span class="t">of</span> input.files) {
  <span class="t">if</span> (f.size &gt; <span class="a">10</span> * <span class="a">1024</span> * <span class="a">1024</span>) { reject(f, <span class="s">'10MB 가 넘습니다'</span>); <span class="t">continue</span>; }
  upload(f);                       <span class="c">// 파일마다 따로 보낸다</span>
}''',
  keys=kbd([
    ("Tab · Enter", "<code>&lt;input type=\"file\"&gt;</code> 가 <b>원래</b> 키보드로 열린다"),
    ("<code>accept</code>", "고르기 창에서 <b>미리 걸러</b> 보여 준다 — 검사는 따로 해야 한다"),
    ("<code>aria-describedby</code>", "받는 조건을 칸에 <b>묶어</b> 읽히게 한다"),
    ("<code>aria-live=\"polite\"</code>", "올린 결과를 <b>소리로</b> 알린다 — 진척은 넣지 않는다"),
    ("드롭존", "<code>dragover</code> 에서 <b><code>preventDefault()</code></b> 를 해야 놓을 수 있다"),
    ("확인하는 법", "마우스를 안 쓰고 <b>Tab 만으로</b> 파일을 올려 본다"),
  ]),
  backend=rows([
    ("두 번 검사", "브라우저에서 거르는 것은 <b>친절</b>이고, 서버 검사가 <b>진짜</b>입니다 — 둘 다 필요합니다."),
    ("저장소로 바로", "서버를 거치지 않고 올리려면 <b>프리사인 URL</b> 을 내려 줍니다 — 서버 대역폭이 크게 줍니다."),
    ("큰 파일", "100MB 를 넘으면 <b>토막 내어</b> 보내고 끊기면 이어 올립니다."),
    ("바이러스·내용 검사", "올린 뒤 검사가 더 있으면 <b>'검사 중'</b> 상태를 따로 둬야 합니다 — 완료와 다릅니다."),
  ]),
  plat_lede="<b>고르는 창</b>을 누가 띄우느냐가 다릅니다.",
  plats=plats([
    ("웹", "input[type=file]",
     files([("영수증_01.jpg", "완료", 100, "")], "110px", "", True, drop=False),
     "끌어다 놓기가 <b>자연스러운</b> 유일한 자리입니다. 데스크톱에서는 기본으로 둡니다."),
    ("iOS", "포토 피커 · 파일 앱",
     '''              <div class="phone" role="img" aria-label="iOS 사진 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:11px;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<code>PHPickerViewController</code> 는 <b>앱에 사진 권한을 안 주고도</b> 고른 것만 건넵니다."),
    ("안드로이드", "Photo Picker · SAF",
     '''              <div class="phone" role="img" aria-label="안드로이드 파일 고르기 재현"><span class="phone__notch"></span><span class="phone__home"></span><div class="phone__screen">
                <div style="position:absolute;left:4px;right:4px;top:26px;display:grid;gap:3px">
                  <span style="height:7px;border-radius:2px;background:var(--accent-soft)"></span>
                  <span style="height:7px;border-radius:2px;background:var(--accent-soft)"></span></div></div></div>''',
     "<b>Photo Picker</b> 와 <b>SAF</b> 가 같은 일을 합니다 — 역시 권한 없이 고른 것만 건넵니다."),
  ]),
  plat_note="앱 쪽이 <b>권한 없이 고른 것만 건네는</b> 길을 만들어 둔 것은 그대로 본받을 만한 생각입니다 — 사진 전체를 열어 주는 대신 <b>필요한 것만</b> 받습니다. 웹의 <code>&lt;input type=\"file\"&gt;</code> 이 원래 그렇게 동작하고 있어서, 웹에서는 이 부분을 공짜로 얻습니다. 대신 웹에는 <b>끌어다 놓기</b>가 있는데, 폰에는 놓을 자리가 없으니 <b>단추를 늘 같이</b> 두는 것이 안전합니다.",
  siblings=siblings("upload"),
  related='''        <li><a href="progress.html"><b>프로그레스 바</b><em>8부</em></a></li>
        <li><a href="exportdata.html"><b>내보내기</b><em>10부</em></a></li>
        <li><a href="validation.html"><b>입력 검증</b><em>10부</em></a></li>
        <li><a href="errortext.html"><b>오류 문구</b><em>14부</em></a></li>''',
)
