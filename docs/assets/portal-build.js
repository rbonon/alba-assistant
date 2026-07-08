(() => {
  const el = document.getElementById('portal-build-meta');
  const script = document.currentScript;
  if (!el || !script) return;

  fetch(new URL('build-info.json', script.src))
    .then((r) => (r.ok ? r.json() : null))
    .then((info) => {
      if (!info) return;
      const when = new Date(info.date).toLocaleString('en-US', {
        timeZone: 'America/Sao_Paulo',
        dateStyle: 'medium',
        timeStyle: 'short',
      });
      el.innerHTML =
        `Updated ${when} · <a href="${info.url}" target="_blank" rel="noopener">${info.hash}</a>`;
    })
    .catch(() => {});
})();
