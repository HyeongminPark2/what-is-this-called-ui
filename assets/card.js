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
