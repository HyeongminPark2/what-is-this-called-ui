/* 화면 지도 — 이름표에서 가짜 앱 화면의 해당 부분까지 지시선을 긋는다.
   좌표를 손으로 박으면 폭이 바뀔 때마다 어긋나므로 매번 계산한다. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';

  document.querySelectorAll('.mapfig').forEach(function (fig) {
    var svg    = fig.querySelector('.mapfig__lines');
    var labels = Array.prototype.slice.call(fig.querySelectorAll('.lbl[data-t]'));
    if (!svg || !labels.length) return;

    // 번호 매기기 — 좁은 화면에서 선 대신 번호로 잇는다
    labels.forEach(function (lbl, i) {
      var n = i + 1;
      var target = fig.querySelector('[data-p="' + lbl.dataset.t + '"]');
      if (!target) return;
      lbl.insertAdjacentHTML('afterbegin', '<span class="no" aria-hidden="true">' + n + '</span>');
      // 배지를 앉힐 기준 상자. 이미 떠 있는 것(absolute)은 건드리지 않는다.
      if (getComputedStyle(target).position === 'static') target.style.position = 'relative';
      target.insertAdjacentHTML('beforeend', '<span class="partno" aria-hidden="true">' + n + '</span>');
      lbl._target = target;

      function on()  { lbl.classList.add('is-on');    target.classList.add('is-on');    mark(lbl, true); }
      function off() { lbl.classList.remove('is-on'); target.classList.remove('is-on'); mark(lbl, false); }
      lbl.addEventListener('mouseenter', on);
      lbl.addEventListener('mouseleave', off);
      lbl.addEventListener('focus', on);
      lbl.addEventListener('blur', off);
    });

    function mark(lbl, isOn) {
      if (lbl._g) lbl._g.setAttribute('class', isOn ? 'on' : '');
    }

    function draw() {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      labels.forEach(function (l) { l._g = null; });

      var box = svg.getBoundingClientRect();
      if (box.width < 2) return;              // 좁은 화면에서는 선을 안 그린다
      svg.setAttribute('viewBox', '0 0 ' + box.width + ' ' + box.height);

      labels.forEach(function (lbl) {
        var t = lbl._target;
        if (!t) return;
        var lr = lbl.getBoundingClientRect(), tr = t.getBoundingClientRect();
        if (!tr.width) return;

        var onLeft = (lr.left + lr.right) / 2 < (tr.left + tr.right) / 2;
        var ax = (onLeft ? lr.right : lr.left) - box.left;
        var ay = (lr.top + lr.height / 2) - box.top;
        var tx = (onLeft ? tr.left : tr.right) - box.left;
        var ty = Math.max(tr.top + 5, Math.min(tr.bottom - 5, lr.top + lr.height / 2)) - box.top;

        var g = document.createElementNS(NS, 'g');
        var line = document.createElementNS(NS, 'line');
        line.setAttribute('x1', ax); line.setAttribute('y1', ay);
        line.setAttribute('x2', tx); line.setAttribute('y2', ty);
        var dot = document.createElementNS(NS, 'circle');
        dot.setAttribute('cx', tx); dot.setAttribute('cy', ty); dot.setAttribute('r', 2.5);
        g.appendChild(line); g.appendChild(dot);
        svg.appendChild(g);
        lbl._g = g;
      });
    }

    draw();
    window.addEventListener('resize', draw);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
    fig._redraw = draw;
  });
})();
