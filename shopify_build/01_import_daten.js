// Schritt 1 – Shop-Daten über die Admin GraphQL API anlegen (läuft im Admin-Tab nach 00_session_setup.js).
// Eingaben: products.json (aus gen_products.py) und navigation.json (aus gen_navigation.py), per Staged Upload
// in den Shop geladen und dort per fetch gelesen (die Admin-Seite darf wegen CSP nicht auf localhost zugreifen).
//
// Warum per API statt CSV-Import: Produkte, Metafelder, Kollektionen, Seiten und Menüs hängen über IDs zusammen
// (Menüpunkt -> Kollektion/Seite). Per Skript entsteht alles in einem Durchlauf, reproduzierbar und ohne Klickfehler.

window.importDaten = async (products, nav) => {
  const log = [];
  // 1) Metafeld-Definitionen (Storefront-Zugriff, damit das Theme sie per Liquid lesen darf)
  for (const [key, name, acc] of [['usp_zeile', 'USP-Zeile', 'PUBLIC_READ'], ['klartext_untertitel', 'Klartext-Untertitel', 'PUBLIC_READ'],
    ['infobox_text', 'Infobox-Text über Titel', 'PUBLIC_READ'], ['lieferhinweis', 'Lieferhinweis', 'PUBLIC_READ'], ['interne_notiz', 'Interne Notiz', 'NONE']])
    await gql(`mutation($d:MetafieldDefinitionInput!){metafieldDefinitionCreate(definition:$d){userErrors{message}}}`,
      { d: { namespace: 'custom', key, name, type: 'single_line_text_field', ownerType: 'PRODUCT', access: { storefront: acc } } });

  // 2) Produkte inkl. Optionen, Varianten, Metafeldern (productSet = idempotent über den Handle)
  const os = (await gql(`{publications(first:10){nodes{id name}}}`)).data.publications.nodes.find(p => p.name === 'Onlineshop').id;
  const publish = id => gql(`mutation($id:ID!,$p:ID!){publishablePublish(id:$id,input:[{publicationId:$p}]){userErrors{message}}}`, { id, p: os });
  for (const p of products) {
    const r = await gql(`mutation($i:ProductSetInput!,$h:String!){productSet(input:$i,identifier:{handle:$h},synchronous:true){product{id} userErrors{message}}}`, { i: p, h: p.handle });
    await publish(r.data.productSet.product.id); log.push('Produkt ' + p.handle);
  }

  // 3) Smart-Kollektionen: Regel "Produkt-Tag = welt:… / anwendung:…" – neue Produkte sortieren sich selbst ein
  const ids = { col: {}, page: {} };
  for (const c of nav.collections) {
    const r = await gql(`mutation($i:CollectionInput!){collectionCreate(input:$i){collection{id}}}`,
      { i: { title: c.title, handle: c.handle, ruleSet: { appliedDisjunctively: false, rules: [{ column: 'TAG', relation: 'EQUALS', condition: c.tag }] } } });
    ids.col[c.handle] = r.data.collectionCreate.collection.id; await publish(ids.col[c.handle]);
  }

  // 4) Seiten-Stubs, damit kein Menülink ins Leere führt (Inhalt = Platzhalter, als solcher gekennzeichnet)
  for (const [h, t] of Object.entries(nav.pages)) {
    const r = await gql(`mutation($p:PageCreateInput!){pageCreate(page:$p){page{id}}}`,
      { p: { title: t, handle: h, isPublished: true, body: `<p>${t} – diese Seite ist im Navigationskonzept vorgesehen. Inhalt folgt (Platzhalter für die Challenge-Vorschau).</p>` } });
    ids.page[h] = r.data.pageCreate.page.id;
  }
  const blogId = (await gql(`mutation{blogCreate(blog:{title:"Anleitungen",handle:"anleitungen"}){blog{id}}}`)).data.blogCreate.blog.id;

  // 5) Menüs: Links als echte Ressourcen-Verknüpfung (COLLECTION/PAGE/BLOG), damit Umbenennungen nicht brechen
  const conv = it => { const [, kind, h] = it.url.split('/'); let o = { title: it.title };
    if (kind === 'collections' && ids.col[h]) o = { ...o, type: 'COLLECTION', resourceId: ids.col[h] };
    else if (kind === 'pages' && ids.page[h]) o = { ...o, type: 'PAGE', resourceId: ids.page[h] };
    else if (kind === 'blogs') o = { ...o, type: 'BLOG', resourceId: blogId };
    else o = { ...o, type: 'HTTP', url: it.url.startsWith('#') ? '/pages/datenschutz' : it.url };
    o.items = (it.items || []).map(conv); return o; };
  const existing = (await gql(`{menus(first:20){nodes{id handle}}}`)).data.menus.nodes;
  for (const [h, m] of Object.entries(nav.menus)) {
    const ex = existing.find(x => x.handle === h), items = m.items.map(conv);
    if (ex) await gql(`mutation($id:ID!,$t:String!,$i:[MenuItemUpdateInput!]!){menuUpdate(id:$id,title:$t,items:$i){userErrors{message}}}`, { id: ex.id, t: m.title, i: items });
    else await gql(`mutation($t:String!,$h:String!,$i:[MenuItemCreateInput!]!){menuCreate(title:$t,handle:$h,items:$i){userErrors{message}}}`, { t: m.title, h, i: items });
    log.push('Menü ' + h);
  }
  // Zusatzmenüs für Service-Leiste (Desktop) und Mobile-Drawer
  // service-menu: Beratung · Schulungen · Gewerbe & Händler   |   mobile-extra: Bestseller · Produktfinder · Beratung · Anmelden
  return log;
};

// Schritt 1b – Solar-Montage-Set (Bundle als eigenes Produkt, Preis 69,95 € statt 77,75 € einzeln = Annahme)
// und MS-5 der Vorlage "dekasyl" zuweisen:
//   productUpdate(product:{id:<MS-5>, templateSuffix:"dekasyl"})
