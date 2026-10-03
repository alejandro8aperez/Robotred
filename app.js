/* =========================================================
   ROBOTRED — app.js
   Navegación, scroll, animaciones, pestañas, FAQ y formulario
   ========================================================= */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- año dinámico ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------- topbar: sombra + progreso + botón arriba ---------- */
  var topbar = document.getElementById('topbar');
  var progress = document.querySelector('#progress span');
  var toTop = document.getElementById('toTop');

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;

    if (topbar) topbar.classList.toggle('scrolled', y > 24);

    if (progress) {
      var doc = document.documentElement;
      var max = (doc.scrollHeight - doc.clientHeight) || 1;
      progress.style.width = Math.min(100, (y / max) * 100) + '%';
    }

    if (toTop) toTop.hidden = y < 600;

    updateActiveLink();
  }

  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------- menú móvil ---------- */
  var navToggle = document.getElementById('navToggle');
  var nav = document.getElementById('nav');

  function closeNav() {
    if (!nav || !navToggle) return;
    nav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Abrir menú');
    document.body.style.overflow = '';
  }

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      navToggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.body.style.overflow = open ? 'hidden' : '';
    });

    nav.addEventListener('click', function (e) {
      if (e.target && e.target.tagName === 'A') closeNav();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeNav();
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 1024) closeNav();
    });
  }

  /* ---------- animaciones del hero en pausa cuando no se ven ---------- */
  var hero = document.querySelector('.hero');

  if (hero && 'IntersectionObserver' in window) {
    var heroObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        hero.classList.toggle('is-idle', !entry.isIntersecting);
      });
    }, { threshold: 0 });

    heroObserver.observe(hero);
  }

  /* ---------- enlace activo según sección visible ---------- */
  var navLinks = nav ? nav.querySelectorAll('a') : [];
  var sections = document.querySelectorAll('main section[id]');

  function updateActiveLink() {
    var current = '';
    var offset = (topbar ? topbar.offsetHeight : 72) + 60;

    sections.forEach(function (section) {
      if (section.getBoundingClientRect().top <= offset) current = section.id;
    });

    navLinks.forEach(function (link) {
      var href = link.getAttribute('href') || '';
      /* Los enlaces que apuntan a otra pagina (p. ej. tutorial.html) llevan ya
         su estado .active en el HTML: no se tocan al calcular la seccion. */
      if (href.charAt(0) !== '#') return;
      link.classList.toggle('active', href === '#' + current);
    });
  }

  /* ---------- revelado al hacer scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');

  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  } else {
    var revealObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var delay = parseInt(entry.target.getAttribute('data-delay') || '0', 10);
        setTimeout(function () { entry.target.classList.add('in'); }, delay);
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    revealEls.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ---------- contadores de métricas ---------- */
  var metrics = document.querySelectorAll('[data-count]');

  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1200;
    var start = performance.now();

    function frame(now) {
      var p = Math.min(1, (now - start) / duration);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }

    requestAnimationFrame(frame);
  }

  if (metrics.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      metrics.forEach(function (el) {
        el.textContent = (el.getAttribute('data-prefix') || '') +
          el.getAttribute('data-count') + (el.getAttribute('data-suffix') || '');
      });
    } else {
      var countObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animateCount(entry.target);
          obs.unobserve(entry.target);
        });
      }, { threshold: 0.6 });
      metrics.forEach(function (el) { countObserver.observe(el); });
    }
  }

  /* ---------- pestañas (Robot X) ---------- */
  var tablists = document.querySelectorAll('[role="tablist"]');

  tablists.forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));

    function select(tab) {
      tabs.forEach(function (t) {
        var selected = t === tab;
        t.setAttribute('aria-selected', selected ? 'true' : 'false');
        t.classList.toggle('active', selected);
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) {
          panel.hidden = !selected;
          panel.classList.toggle('active', selected);
        }
      });
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        var dir = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!dir) return;
        e.preventDefault();
        var next = tabs[(i + dir + tabs.length) % tabs.length];
        next.focus();
        select(next);
      });
    });
  });

  /* ---------- acordeón FAQ ---------- */
  var faqButtons = document.querySelectorAll('.faq-q');

  faqButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var panel = item ? item.querySelector('.faq-a') : null;
      if (!panel) return;

      var isOpen = btn.getAttribute('aria-expanded') === 'true';

      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        if (openItem === item) return;
        openItem.classList.remove('open');
        var openBtn = openItem.querySelector('.faq-q');
        var openPanel = openItem.querySelector('.faq-a');
        if (openBtn) openBtn.setAttribute('aria-expanded', 'false');
        if (openPanel) openPanel.hidden = true;
      });

      btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
      item.classList.toggle('open', !isOpen);
      panel.hidden = isOpen;
    });
  });

  /* ---------- formulario de contacto ---------- */
  var form = document.getElementById('form');
  var success = document.getElementById('formSuccess');
  var submitBtn = document.getElementById('formSubmit');
  var EMAIL = 'info@robotred.co';

  var UTM_PARAMS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];

  function captureContext() {
    var params = new URLSearchParams(window.location.search);

    UTM_PARAMS.forEach(function (key) {
      var input = document.getElementById(key);
      if (input) input.value = params.get(key) || '';
    });

    var origen = document.getElementById('origen');
    if (origen) origen.value = document.referrer || 'directo';

    var pagina = document.getElementById('pagina');
    if (pagina) pagina.value = window.location.pathname + window.location.hash;
  }

  function setFieldError(field, hasError) {
    var wrap = field.closest('.field');
    if (wrap) wrap.classList.toggle('invalid', hasError);
    field.setAttribute('aria-invalid', hasError ? 'true' : 'false');
  }

  function mailtoFallback(data) {
    var subject = '[ROBOT-RED] ' + (data.get('tipo') || 'Solicitud') +
      ' — ' + (data.get('empresa') || '');
    var body = [
      'Nombre: ' + (data.get('nombre') || ''),
      'Empresa: ' + (data.get('empresa') || ''),
      'Correo: ' + (data.get('email') || ''),
      'Teléfono: ' + (data.get('telefono') || ''),
      'Tipo de solicitud: ' + (data.get('tipo') || ''),
      'Tipo de red: ' + (data.get('red') || ''),
      '',
      'Mensaje:',
      (data.get('mensaje') || '')
    ].join('\n');

    window.location.href = 'mailto:' + EMAIL +
      '?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(body);
  }

  function setSending(isSending) {
    if (!submitBtn) return;
    submitBtn.disabled = isSending;
    submitBtn.classList.toggle('is-loading', isSending);
  }

  if (form) {
    captureContext();

    var fields = form.querySelectorAll('input:not([type="hidden"]), select, textarea');

    fields.forEach(function (field) {
      field.addEventListener('input', function () {
        var wrap = field.closest('.field');
        if (wrap && wrap.classList.contains('invalid')) {
          setFieldError(field, !field.checkValidity());
        }
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var invalid = null;
      fields.forEach(function (field) {
        var bad = !field.checkValidity();
        setFieldError(field, bad);
        if (bad && !invalid) invalid = field;
      });

      if (invalid) {
        invalid.focus();
        if (success) success.hidden = true;
        return;
      }

      if (form.querySelector('[name="bot-field"]') &&
          form.querySelector('[name="bot-field"]').value) {
        return;
      }

      captureContext();

      var payload = new URLSearchParams();
      new FormData(form).forEach(function (value, key) {
        if (key === 'bot-field') return;
        payload.append(key, value);
      });

      setSending(true);
      if (success) success.hidden = true;

      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: payload.toString()
      }).then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        window.location.href = form.getAttribute('action') || '/gracias.html';
      }).catch(function () {
        setSending(false);
        mailtoFallback(new FormData(form));
      });
    });
  }

  /* ---------- arranque ---------- */
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', updateActiveLink);
  onScroll();
})();
