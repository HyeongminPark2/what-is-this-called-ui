/* 화면 지도.
   선을 열다섯 개 늘 그어 두면 어지럽다. 기본은 번호 배지 + 아래 목록이다.
   목록의 이름을 짚으면 부품까지 지시선을 긋고, 부품을 짚으면 마우스 옆에 이름을 띄운다.
   좌표는 손으로 박지 않고 매번 계산한다. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';

  // 화면에서 부품을 짚으면 이름을 마우스 옆에 띄운다.
  // 지도가 길어 아래 목록이 화면 밖에 있을 때가 많아서, 목록까지 선을 그어도 이름이 안 보인다.
  var tip = document.createElement('div');
  tip.className = 'maptip';
  tip.setAttribute('aria-hidden', 'true');
  tip.hidden = true;
  document.body.appendChild(tip);

  function showTip(lbl, x, y) {
    if (!tip._for || tip._for !== lbl) {
      var body = lbl.querySelector(':scope > span:not(.no)') || lbl;
      tip.innerHTML = '<span class="no">' + lbl.querySelector('.no').textContent + '</span>' +
                      '<span>' + body.innerHTML + '</span>';
      tip._for = lbl;
    }
    tip.hidden = false;
    var w = tip.offsetWidth, h = tip.offsetHeight;
    var left = Math.min(x + 14, window.innerWidth - w - 8);
    var top = y + 18 + h > window.innerHeight - 8 ? y - h - 12 : y + 18;
    tip.style.left = Math.max(8, left) + 'px';
    tip.style.top = Math.max(8, top) + 'px';
  }
  function hideTip() { tip.hidden = true; tip._for = null; }

  // 터치로 누르면 브라우저가 마우스 이벤트를 흉내 내며 곧바로 mouseleave 까지 보낸다.
  // 손가락으로 누른 직후의 mouseleave 는 무시하고, 다른 곳을 누르면 거둔다.
  var lastTouch = 0;
  function clearAll() {
    hideTip();
    document.querySelectorAll('.mapfig .is-on').forEach(function (el) { el.classList.remove('is-on'); });
    document.querySelectorAll('.mapfig__lines').forEach(function (svg) {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
    });
  }
  document.addEventListener('pointerdown', function (e) {
    if (e.pointerType === 'mouse') return;
    lastTouch = Date.now();
    if (!e.target.closest('.mapfig [data-p], .mapfig .lbl')) clearAll();
  });
  // 고정 위치라 스크롤하면 엉뚱한 곳에 남는다. 마우스는 다시 움직이면 돌아온다.
  window.addEventListener('scroll', hideTip, { passive: true });

  document.querySelectorAll('.mapfig').forEach(function (fig) {
    var svg    = fig.querySelector('.mapfig__lines');
    var labels = Array.prototype.slice.call(fig.querySelectorAll('.lbl[data-t]'));
    if (!svg || !labels.length) return;

    var badges = [];

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
      } else if (tr.height < 26 && tr.width < mr.width - 44) {
        // 화면 폭을 다 쓰는 띠는 왼쪽에 뺄 자리가 없다 — 모서리에 둔다
        target.lastElementChild.classList.add('partno--out');
      }

      badges.push(target.lastElementChild);

      lbl.addEventListener('mouseenter', function () { on(lbl); });
      lbl.addEventListener('mouseleave', off);
      lbl.addEventListener('focus', function () { on(lbl); });
      lbl.addEventListener('blur', off);

      // 화면에서 부품을 짚어도 이름이 밝아진다 — '이게 뭐지' 방향
      // 부품 쪽에서는 선 대신 마우스 옆에 이름을 띄운다.
      target.addEventListener('mouseenter', function (e) {
        e.stopPropagation();          // 겹쳐 있으면 안쪽 것이 이긴다
        if (Date.now() - lastTouch < 1000) return;      // 터치는 pointerup 에서 처리했다
        on(lbl, true);
        showTip(lbl, e.clientX, e.clientY);
      });
      target.addEventListener('mousemove', function (e) {
        if (!lbl.classList.contains('is-on')) return;   // 안쪽 부품이 이긴 상태면 바깥 것은 가만히
        if (Date.now() - lastTouch < 1000) return;      // 터치가 흉내 낸 움직임
        e.stopPropagation();
        showTip(lbl, e.clientX, e.clientY);
      });
      target.addEventListener('pointerup', function (e) {
        if (e.pointerType === 'mouse') return;
        e.stopPropagation();          // 겹쳐 있으면 안쪽 것이 이긴다
        lastTouch = Date.now();
        on(lbl, true);
        showTip(lbl, e.clientX, e.clientY);
      });
      target.addEventListener('mouseleave', function () {
        if (Date.now() - lastTouch < 1000) return;
        off();
      });
    });

    // 두 부품의 모서리가 같은 자리면 번호끼리 겹쳐 하나가 안 보인다. 겹치면 옆으로 비킨다.
    function spread() {
      var placed = [];
      badges.forEach(function (n) {
        n.style.left = ''; n.style.right = '';
        var right = n.classList.contains('partno--right');
        for (var k = 0; k < 4; k++) {
          var r = n.getBoundingClientRect();
          // 아슬아슬하게 비껴간 것도 글꼴·줄높이가 바뀌면 겹친다. 3px 넉넉히 보고 떼어 놓는다.
          var hit = placed.some(function (p) {
            var q = p.getBoundingClientRect();
            return r.right > q.left - 3 && r.left < q.right + 3 &&
                   r.bottom > q.top - 3 && r.top < q.bottom + 3;
          });
          if (!hit) break;
          var cs = getComputedStyle(n);
          if (right) n.style.right = (parseFloat(cs.right) + 24) + 'px';
          else       n.style.left  = (parseFloat(cs.left)  + 24) + 'px';
        }
        placed.push(n);
      });
    }
    spread();
    window.addEventListener('resize', spread);
    // 글꼴이 자리잡으면 줄 높이가 바뀌어 몇 px 움직인다. 그때 다시 센다.
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(spread);
    window.addEventListener('load', spread);

    function off() {
      hideTip();
      fig.querySelectorAll('.is-on').forEach(function (el) { el.classList.remove('is-on'); });
      while (svg.firstChild) svg.removeChild(svg.firstChild);
    }

    function on(lbl, fromPart) {
      off();
      var t = lbl._target;
      if (!t) return;
      lbl.classList.add('is-on');
      t.classList.add('is-on');
      if (!fromPart) drawTo(lbl, t);
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
