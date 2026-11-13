# 검사

```sh
node tools/check.js                                                    # 레포의 파일
node tools/check.js https://hyeongminpark2.github.io/what-is-this-called-ui/   # 배포본
```

Playwright와 node 20+ 가 필요하다. 이 머신에서는

```sh
NODE_PATH=/data/work/verbatim/node_modules /data/tools/node20/bin/node tools/check.js
```

## 무엇을 보나

기능(모달이 열리나 닫히나)뿐 아니라 **레이아웃이 무너졌는지**를 본다. 기능 검사만
돌리면 해부도가 세로로 한 글자씩 쌓여 칸 높이가 10,000px가 돼도 통과한다.

- 글이 세로로 쌓였는지 (폭 46px 미만인데 높이 170px 초과)
- 그림이 칸 밖으로 잘렸는지
- 390px에서 가로로 넘치는지
- 페이지 전체 높이가 터무니없이 긴지
- 폭 토글이 실제로 390 / 768을 만드는지
- 좁은 폭에서 모달이 바텀시트가 되는지
- 포커스가 **배경의 누를 수 있는 것에 닿지 않는지**, 배경이 정말 비활성인지,
  닫은 뒤 포커스가 부른 버튼으로 돌아오는지

포커스 갇힘은 iframe 밖에서만 검사할 수 있어서 `demos/modal.html`을 직접 연다.

**단정문이 전부 통과해도 스크린샷을 눈으로 본다.**
