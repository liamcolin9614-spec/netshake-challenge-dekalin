// Läuft im Browser-Tab des Shopify-Admins (admin.shopify.com) mit der eingeloggten Sitzung.
// Holt das CSRF-Token der Admin-Oberfläche und stellt zwei Helfer bereit:
//   gql(query, vars)   -> Admin GraphQL API (Produkte, Kollektionen, Menüs, Seiten, Dateien)
//   osw(op, query, vars) -> interne Online-Store-Editor-API (Theme-Vorlagen, Section-Gruppen, Theme-Einstellungen)
// Warum so: Die Testversion eines Kauf-Themes erlaubt keinen Code-Editor und keine Asset-API;
// der Theme-Editor speichert aber über diese API – genau so, wie ein Klick auf "Speichern".
(async () => {
  const of = window.__of || window.fetch; window.__of = of;
  // Das Token steht im serialisierten Startzustand der Admin-Seite ("csrfToken":"...").
  const tok = (document.documentElement.innerHTML.match(/csrfToken":"([A-Za-z0-9_\-]+)/) || [])[1];
  window.__csrf = tok;
  const store = location.pathname.split('/')[2];
  window.gql = async (query, variables = {}) => (await of(`/api/shopify/${store}?operation=X&type=${query.trim().startsWith('mutation') ? 'mutation' : 'query'}`,
    { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json', 'x-csrf-token': window.__csrf, 'shopify-proxy-api-enable': 'true' }, body: JSON.stringify({ query, variables }) })).json();
  window.osw = async (operationName, query, variables = {}) => (await of(`/api/app_proxy/${store}?operation=${operationName}&version=unstable`,
    { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json', 'x-csrf-token': window.__csrf, 'x-online-store-web': '1', 'x-shopify-app-id': '580111', 'x-shopify-extension-id': '650f1a14fa979ec5c74d063e968411d4-online_store', 'x-shopify-instance-id': '1' }, body: JSON.stringify({ operationName, variables, query }) })).json();
  window.__ready = !!tok;
})();
