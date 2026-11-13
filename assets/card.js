/* 카드 안의 폭 토글. 같은 부품을 폰 폭과 데스크톱 폭에서 번갈아 보게 한다. */
(function () {
  document.querySelectorAll('[data-stage]').forEach(function (stage) {
    var seg   = document.querySelector('[data-seg="' + stage.dataset.stage + '"]');
    var meta  = document.querySelector('[data-meta="' + stage.dataset.stage + '"]');
    var frame = stage.querySelector('iframe');
    if (!seg || !frame) return;

    function report() {
      if (!meta) return;
      var w = Math.round(frame.getBoundingClientRect().width);
      meta.textContent = w + 'px 폭';
    }

    function set(w) {
      stage.dataset.w = w;
      seg.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.w === w));
      });
      // 애니메이션이 끝난 뒤 실제 폭을 읽는다
      setTimeout(report, 320);
    }

    seg.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-w]');
      if (b) set(b.dataset.w);
    });

    // 좁은 화면에서는 폰 폭으로 시작하는 게 자연스럽다
    set(window.innerWidth < 760 ? 'full' : (stage.dataset.w || 'full'));
    window.addEventListener('resize', report);
    frame.addEventListener('load', report);
    report();
  });
})();

/* 해부도 번호. ::before 로 그리면 겹쳐도 비켜 줄 수가 없고,
   빈 태그나 변형된 요소에서는 아예 안 그려진다. 실제 요소로 넣고 겹치면 옆으로 민다. */
(function () {
  document.querySelectorAll('.anat').forEach(function (anat) {
    var targets = Array.prototype.slice.call(anat.querySelectorAll('[data-pin]'));
    if (!targets.length) return;
    var badges = targets.map(function (t) {
      t.insertAdjacentHTML('beforeend', '<span class="pinno" aria-hidden="true">' + t.dataset.pin + '</span>');
      return t.lastElementChild;
    });

    function spread() {
      var placed = [];
      badges.forEach(function (n) {
        n.style.top = ''; n.style.transform = '';
        for (var k = 0; k < 4; k++) {
          var r = n.getBoundingClientRect();
          var hit = placed.some(function (p) {
            var q = p.getBoundingClientRect();
            return r.right > q.left - 3 && r.left < q.right + 3 &&
                   r.bottom > q.top - 3 && r.top < q.bottom + 3;
          });
          if (!hit) break;
          // 옆으로 밀면 판 밖으로 나가기 쉽다. 아래로 비킨다.
          n.style.top = (parseFloat(getComputedStyle(n).top) + 24) + 'px';
          n.style.transform = 'none';
        }
        placed.push(n);
      });
    }
    spread();
    window.addEventListener('resize', spread);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(spread);
    window.addEventListener('load', spread);
  });
})();
