// Delegación: un listener central que redirige según el atributo `data-href`
document.addEventListener('click', function (e) {
  const btn = e.target.closest('[data-href]');
  if (!btn) return;
  e.preventDefault();
  const href = btn.dataset.href || btn.getAttribute('href');
  if (href) window.location.href = href;
});