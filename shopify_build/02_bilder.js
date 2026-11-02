// Schritt 2 – Bilder.
// a) MS-5-Galerie: 5 Grafiken aus dem Prototyp (aufgabe1/06_shopify_bilder/galerie_0X.png, 1120 px),
//    per stagedUploadsCreate + curl hochgeladen und über productSet(files:[…]) mit Alt-Texten angehängt.
//    Warum Grafiken statt Fotos: Es gibt keine freigegebenen Produktfotos; die Grafiken tragen die Kaufargumente
//    direkt im Bild (Callouts, Haftgrund-Ampel, 4 Schritte) – Prinzip "Information ins Bild".
// b) Packshots der Cross-Sell-Produkte + Logo: direkt im Browser per <canvas> gezeichnet (gleicher Stil wie die
//    MS-5-Kartusche), als PNG zum Staged-Upload-Ziel hochgeladen und per productUpdate(media:[…]) angehängt.
//    Das Logo ist eine Platzhalter-Wortmarke in Dekalin-Rot (#D42A3B) mit Barlow – kein Original-Logo.
window.uploadBlobs = async (blobs /* {name: Blob} */) => {
  const keys = Object.keys(blobs);
  const st = await gql(`mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl}}}`,
    { i: keys.map(k => ({ filename: k + '.png', mimeType: 'image/png', resource: 'IMAGE', httpMethod: 'PUT' })) });
  const T = st.data.stagedUploadsCreate.stagedTargets;
  for (let i = 0; i < keys.length; i++) await fetch(T[i].url, { method: 'PUT', headers: { 'content-type': 'image/png' }, body: blobs[keys[i]] });
  return Object.fromEntries(keys.map((k, i) => [k, T[i].resourceUrl]));
};
window.attachImage = async (handle, url, alt) => {
  const p = (await gql(`query($h:String!){productByHandle(handle:$h){id}}`, { h: handle })).data.productByHandle;
  return gql(`mutation($p:ProductUpdateInput!,$m:[CreateMediaInput!]){productUpdate(product:$p,media:$m){userErrors{message}}}`,
    { p: { id: p.id }, m: [{ originalSource: url, mediaContentType: 'IMAGE', alt }] });
};
