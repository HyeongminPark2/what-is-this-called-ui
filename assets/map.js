/* 화면 지도.
   선을 열다섯 개 늘 그어 두면 어지럽다. 기본은 번호 배지 + 옆 목록이고,
   짚은 것 하나만 지시선을 긋는다. 좌표는 손으로 박지 않고 매번 계산한다. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';

  document.querySelectorAll('.mapfig').forEach(function (fig) {
    var svg    = fig.querySelector('.mapfig__lines');
    var labels = Array.prototype.slice.call(fig.querySelectorAll('.lbl[data-t]'));
    if (!svg || !labels.length) return;

    labels.forEach(function (lbl, i) {
      var target = fig.querySelector('[data-p="' + lbl.dataset.t + '"]');
      if (!target) return;
      lbl._target = target;
      target._label = lbl;

      lbl.insertAdjacentHTML('afterbegin', '<span class="no" aria-hidden="true">' + (i + 1) + '</span>');
      // 배지를 앉힐 기준 상자. 이미 떠 있는 것(absolute)은 건드리지 않는다.
      if (getComputedStyle(target).position === 'static') target.style.position = 'relative';
      target.insertAdjacentHTML('beforeend', '<span class="partno" aria-hidden="true">' + (i + 1) + '</span>');
      // 낮은 부품은 모서리 배지가 글자를 덮는다 — 옆 바깥으로 뺀다.
      // 화면 오른쪽 끝에 붙은 작은 것은 왼쪽에도 자리가 없으니 오른쪽으로.
      var tr = target.getBoundingClientRect();
      var mr = fig.querySelector('.appmock').getBoundingClientRect();
      if (tr.width < 60 && mr.right - tr.right < 28) {
        target.lastElementChild.classList.add('partno--right');
      } else if (tr.height < 26) {
        target.lastElementChild.classList.add('partno--out');
      }

      lbl.addEventListener('mouseenter', function () { on(lbl); });
      lbl.addEventListener('mouseleave', off);
      lbl.addEventListener('focus', function () { on(lbl); });
      lbl.addEventListener('blur', off);

      // 화면에서 부품을 짚어도 이름이 밝아진다 — '이게 뭐지' 방향
      target.addEventListener('mouseenter', function (e) {
        e.stopPropagation();          // 겹쳐 있으면 안쪽 것이 이긴다
        on(lbl);
      });
      target.addEventListener('mouseleave', off);
    });

    function off() {
      fig.querySelectorAll('.is-on').forEach(function (el) { el.classList.remove('is-on'); });
      while (svg.firstChild) svg.removeChild(svg.firstChild);
    }

    function on(lbl) {
      off();
      var t = lbl._target;
      if (!t) return;
      lbl.classList.add('is-on');
      t.classList.add('is-on');
      drawTo(lbl, t);
    }

    function drawTo(lbl, t) {
      var box = svg.getBoundingClientRect();
      if (box.width < 2) return;
      if (getComputedStyle(svg).display === 'none') return;   // 좁은 화면에서는 번호로만 잇는다
      svg.setAttribute('viewBox', '0 0 ' + box.width + ' ' + box.height);

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
      dot.setAttribute('cx', tx); dot.setAttribute('cy', ty); dot.setAttribute('r', 3);
      g.appendChild(line); g.appendChild(dot);
      svg.appendChild(g);
    }
  });
})();
