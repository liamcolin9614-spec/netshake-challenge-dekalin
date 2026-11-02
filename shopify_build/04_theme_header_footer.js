// Schritt 4 – Theme-Einstellungen, Header-, Overlay- und Footer-Gruppe über die Editor-API.
// Typen der Settings liest das Skript aus dem Theme (sectionGroup(type) / themeSettingsCategories),
// geschrieben wird mit denselben Mutationen, die der Theme-Editor beim Speichern nutzt.
window.THEME_SETTINGS = {           // CI Dekalin: Rot #D42A3B, Text #262626, Schrift Barlow
  heading_font: 'barlow_n7', body_font: 'barlow_n4', heading_font_letter_spacing: 0, navigation_font_source: 'heading', button_font_source: 'heading',
  color_body_bg: '#FFFFFF', color_body: '#262626', color_heading: '#262626', color_accent: '#D42A3B', color_border: '#E2E2E2',
  color_header_bg: '#FFFFFF', color_header_text: '#262626', color_header_links: '#262626', color_header_links_hover: '#D42A3B', color_header_icons: '#262626',
  color_secondary_menu_bg: '#F4F4F4', color_secondary_menu_text: '#262626', color_announcement_bar_bg: '#262626', color_announcement_bar_text: '#FFFFFF',
  solid_button_background: '#D42A3B', solid_button_label: '#FFFFFF', white_button_label: '#262626', color_price: '#262626', color_price_discounted: '#D42A3B',
  color_stars: '#F5A623', color_footer_bg: '#262626', color_footer_heading: '#FFFFFF', color_footer_text: '#E6E6E6', color_footer_link: '#CFCFCF',
  color_footer_link_hover: '#FFFFFF', color_footer_border: '#555555', color_badge_sale: '#D42A3B', block_shadows: false, block_border_radius: 12,
  button_border_radius: 8, show_products_inventory: false, custom_product_badge_group_1_tag_names: 'bestseller', custom_product_badge_group_1_color: '#D42A3B',
  search_product_heading: 'Gerade gefragt', animations: true };
// Mutation Theme-Einstellungen: onlineStoreThemeSettingsDataUpdateV2(id, settings:[{type,settingId,value}], sessionId, …)
// Mutation Section-Gruppen:     onlineStoreThemeSectionGroupUpdate(themeId, sessionId, sectionGroupType, sections)
// Speichern (= Klick auf "Speichern"): onlineStoreThemeEditorSessionPublish(sessionId)
window.HEADER = {
  announcement: ['✓ Versand in 1–3 Werktagen · ab 49 € versandkostenfrei', '✓ Direkt vom Hersteller – Kleb- & Dichtstoffe seit 1907', '✓ Kostenlose Anwendungsberatung vom Dekalin-Team'],
  secondary_menu: 'service-menu',   // Section 'header-secondary-menu' ist deaktiviert (Konzept: keine Doppel-Leiste); Menü bleibt angelegt menu: 'main-menu', logo: 'shopify://shop_images/logo_dekalin.png',
  menu_badge: { badge_position: '2', text: 'TOP', color_bg: '#D42A3B', color_text: '#ffffff' },
  // je Hauptpunkt ein Mega-Menü-Block mit einer Promo-Kachel (Text aus 04_pdp_texte.md, Abschnitt 8).
  // Bilder: aufgabe1/06_shopify_bilder/promo/promo_*.png (aus promo.html), Kleben & Montieren nutzt galerie_02.png –
  // je Kachel ein Motiv, das zum Text passt; Ziel jeweils eine Kollektion/Seite mit Inhalt (keine leere Kollektion).
  megamenu_promos: [
    ['Abdichten', 'Damit Wasser draußen bleibt. Welche Dichtmasse für die Dachluke? Zur Anleitung ›', 'shopify://collections/fenster-dachluken-abdichten'],
    ['Kleben & Montieren', 'Hält. Ohne Bohren. Solar-Montage-Set: alles in einem Paket ›', 'shopify://products/solar-montage-set'],
    ['Reparieren & Schützen', 'Undicht? Wasserschaden stoppen – Schritt für Schritt reparieren ›', 'shopify://collections/wasserschaden-reparieren'],
    ['Reinigen & Zubehör', 'Damit es hält. Bestseller: Was Profis immer dabeihaben ›', 'shopify://collections/bestseller'],
    ['Ratgeber', "Richtig machen, beim ersten Mal. Das Buch vom Klebepapst: Klebt nicht gibt's nicht! ›", 'shopify://pages/klebepapst-buch'],
    ['Warum Dekalin', 'Kleben & Dichten seit 1907. Frag uns: kostenlose Anwendungsberatung ›', 'shopify://pages/beratung']],
  mobile_nav: 'main-menu', mobile_secondary_menu: 'mobile-extra', mobile_bg: '#262626' };
window.FOOTER = {
  brand_text: '<p>Kleben & Dichten seit 1907. Profi-Know-how für Wohnmobil, Caravan und Werkstatt – direkt vom Hersteller.</p><p>Fragen zur Anwendung? <a href="mailto:support@dekalin.de">support@dekalin.de</a></p>',
  menus: [['Shop', 'footer-shop'], ['Hilfe', 'footer-hilfe'], ['Wissen & Dekalin', 'footer-dekalin']],
  signup: ['Klebe-Tipps vom Profi', '<p>Anleitungen, Projektideen und neue Produkte – ein- bis zweimal im Monat.</p>'],
  copyright: 'DEKALIN · Alle Preise inkl. MwSt., zzgl. Versandkosten', footer_reveal_animation: false };
// Overlay-Gruppe: "mobile_dock" (Leiste am unteren Bildschirmrand) deaktiviert – laut Konzept kein zusätzliches
// Sticky-Element auf der PDP (Sticky-ATC verdeckt mobil Inhalt und lenkt ab, Platz für Inhalt).
