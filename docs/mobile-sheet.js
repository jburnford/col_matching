/* mobile-sheet.js — turns the parchment panel into a draggable bottom sheet on
   phones, so the map keeps most of the screen and the register is one thumb-drag
   away. Self-contained: no ATLAS dependency, works on both atlases (it finds
   #register on the careers atlas or #panel on the education atlas). Active only
   under the mobile media query; on wider screens the desktop side-panel returns. */
(function () {
  const panel = document.getElementById('register') || document.getElementById('panel');
  if (!panel) return;
  // match the per-page CSS breakpoint: careers (#register) folds at 820, the
  // education atlas (#panel) at 860.
  const mq = window.matchMedia('(max-width: ' + (panel.id === 'panel' ? 860 : 820) + 'px)');
  const body = document.getElementById('reg-body') || document.getElementById('panel-body');

  let state = 'peek';          // peek | half | full
  let handle = null, hintEl = null, active = false, moved = false;

  const vh = () => window.innerHeight;
  // snap targets in px, low → high; kept in sync with the CSS heights below
  const targets = () => [['peek', 58], ['half', vh() * 0.54], ['full', vh() * 0.92]];

  function setState(s) {
    state = s;
    panel.style.height = '';                 // hand height back to the class
    panel.classList.remove('sheet-peek', 'sheet-half', 'sheet-full');
    panel.classList.add('sheet-' + s);
    if (hintEl) hintEl.textContent = s === 'peek' ? 'Records & search' : '';
    if (s === 'peek' && body) body.scrollTop = 0;
  }

  function snapNearest() {
    const h = panel.getBoundingClientRect().height;
    let best = targets()[0];
    for (const t of targets()) if (Math.abs(t[1] - h) < Math.abs(best[1] - h)) best = t;
    setState(best[0]);
  }

  function wireDrag() {
    let startY = 0, startH = 0, dragging = false;
    handle.addEventListener('pointerdown', (e) => {
      dragging = true; moved = false;
      startY = e.clientY; startH = panel.getBoundingClientRect().height;
      panel.style.transition = 'none';
      try { handle.setPointerCapture(e.pointerId); } catch (_) {}
    });
    handle.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      const h = Math.min(vh() * 0.92, Math.max(54, startH + (startY - e.clientY)));
      panel.style.height = h + 'px';
      if (Math.abs(e.clientY - startY) > 6) moved = true;
    });
    const end = () => {
      if (!dragging) return;
      dragging = false;
      panel.style.transition = '';           // re-enable the snap animation
      snapNearest();
    };
    handle.addEventListener('pointerup', end);
    handle.addEventListener('pointercancel', end);
  }

  function buildHandle() {
    handle = document.createElement('div');
    handle.className = 'sheet-handle';
    handle.innerHTML = '<span class="sheet-grip"></span><span class="sheet-hint"></span>';
    hintEl = handle.querySelector('.sheet-hint');
    panel.insertBefore(handle, panel.firstChild);
    wireDrag();
    // a tap (no drag) toggles between peek and half
    handle.addEventListener('click', () => {
      if (moved) { moved = false; return; }
      setState(state === 'peek' ? 'half' : 'peek');
    });
    wireAutoReveal();
  }

  // Selecting a career, place, school or bridge fills the register — on a phone
  // that content is hidden behind the peeking sheet, so raise it to half. We hook
  // the actual selection entry points (not a blanket content observer) so the
  // intro tour's summary render doesn't force the sheet open on first load.
  function wireAutoReveal() {
    const app = window.ATLAS && window.ATLAS.App;
    if (!app) return;
    ['selectPerson', 'openPerson', 'selectPlace', 'selectBridge', 'selectInstitution']
      .forEach((m) => {
        if (typeof app[m] !== 'function') return;
        const orig = app[m].bind(app);
        app[m] = function () {
          if (active && state === 'peek') setState('half');
          return orig.apply(this, arguments);
        };
      });
  }

  function enable() {
    if (active) return;
    active = true;
    document.body.classList.add('mobile-sheet');
    if (!handle) buildHandle(); else handle.style.display = '';
    setState('peek');
  }
  function disable() {
    if (!active) return;
    active = false;
    document.body.classList.remove('mobile-sheet');
    panel.classList.remove('sheet-peek', 'sheet-half', 'sheet-full');
    panel.style.height = ''; panel.style.transition = '';
    if (handle) handle.style.display = 'none';
  }
  const sync = () => (mq.matches ? enable() : disable());
  mq.addEventListener ? mq.addEventListener('change', sync) : mq.addListener(sync);
  sync();
})();
