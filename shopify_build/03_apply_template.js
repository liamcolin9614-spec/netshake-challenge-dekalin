// Speichert eine Vorlagen-Spezifikation (template_dekasyl.json) als Theme-Vorlage, z. B. product.dekasyl.
// Die Setting-Typen (CHECKBOX, COLOR, RICHTEXT ...) liest das Skript aus den bestehenden Vorlagen des Themes
// (product + product.dekasyl), damit die Spezifikation selbst nur Werte enthalten muss.
// Voraussetzung: 00_session_setup.js (stellt osw() bereit) und eine Editor-Session-ID (window.__edSession).
window.THEME = 'gid://shopify/OnlineStoreTheme/198427443533';
const SIMPLE = ['Checkbox','Color','Number','Range','Select','Text','Textarea','RichText','InlineRichtext','Liquid','TextAlignment','Radio','HTML'];
const FRAG = 'settingId type ' + SIMPLE.map(t => `... on OnlineStoreThemeSetting${t}{ v_${t}: value }`).join(' ');
window.readTemplate = async (basename) => (await osw('JT', `query JT($id:ID!,$b:String!){ onlineStore{ theme(id:$id){ jsonTemplate(basename:$b){ sections{ sectionId type disabled settings{ ${FRAG} } blocks{ blockId type settings{ ${FRAG} } } } } } } }`,
  { id: THEME, b: basename })).data.onlineStore.theme.jsonTemplate.sections;
window.applyTemplate = async (spec, basename, sessionId) => {
  const types = {};                                     // "sectionType/blockType/settingId" -> TYPE
  for (const b of ['product', basename]) for (const s of await readTemplate(b)) {
    for (const x of s.settings) types[`${s.type}//${x.settingId}`] = x.type;
    for (const bl of s.blocks) for (const x of bl.settings) types[`${s.type}/${bl.type}/${x.settingId}`] = x.type;
  }
  // Sections, die noch in keiner Vorlage vorkommen: Typen aus den Section-Presets des Themes
  for (const p of (window.__presets || [])) for (const x of p.section.settings) types[`${p.section.type}//${x.settingId}`] ??= x.type;
  const EXTRA = { collection: 'COLLECTION', custom_liquid: 'LIQUID', content: 'RICHTEXT', image: 'IMAGE_PICKER', button_link: 'URL', link: 'URL', page: 'PAGE' };
  const typed = (key, values) => Object.entries(values).map(([id, v]) => ({
    type: types[`${key}/${id}`] || EXTRA[id] || 'TEXT', settingId: id,
    value: v === null ? null : (typeof v === 'boolean' || typeof v === 'number' ? String(v) : v) }));
  const fixedId = { 'breadcrumbs': 'breadcrumbs', 'main-product': 'main-product', 'product-recommendations': 'product-recommendations' };
  const sections = spec.map(s => ({ sectionId: fixedId[s.type] || crypto.randomUUID(), type: s.type, disabled: false, customCss: null,
    settings: typed(`${s.type}/`, s.settings),
    blocks: s.blocks.map(b => ({ blockId: crypto.randomUUID(), type: b.type, disabled: false, blocks: [], settings: typed(`${s.type}/${b.type}`, b.settings) })) }));
  const r = await osw('TemplateUpdate', `mutation TemplateUpdate($themeId:ID!,$templateBasename:String!,$sections:[OnlineStoreThemeSettingsDataSectionInput!],$sessionId:String!){
    onlineStoreThemeJsonTemplateUpdate(themeId:$themeId,templateBasename:$templateBasename,sections:$sections,sessionId:$sessionId){ userErrors{ field message } } }`,
    { themeId: THEME, templateBasename: basename, sections, sessionId });
  return r.errors || r.data.onlineStoreThemeJsonTemplateUpdate.userErrors;
};
window.saveTheme = async (sessionId) => (await osw('SaveTheme', `mutation SaveTheme($sessionId:String!){ onlineStoreThemeEditorSessionPublish(sessionId:$sessionId){ conflicts{ resourceId } userErrors{ field message } } }`, { sessionId })).data;
