"""Erzeugt die Produktvorlage templates/product.dekasyl.json (Vision) als einfache Spezifikation:
[{type, settings:{id:wert}, blocks:[{type, settings:{}}]}]. Das Browser-Skript 03_apply_template.js
ergänzt daraus die Setting-Typen (aus den Vision-Schemas) und speichert über den Theme-Editor.
Inhalte: aufgabe1/04_pdp_texte.md, Aufbau/Begründung: aufgabe1/03_pdp_bauplan.md."""
import json, pathlib
RED, INK, SOFT = "#D42A3B", "#262626", "#F4F4F4"
GREEN, YELLOW = "#2E8B57", "#E8B400"
TINT = "#FBEAEC"

# Strich-Icons (24er Raster), eingefärbt über currentColor
ICON = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "thermo": '<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    "brush": '<path d="M9.06 11.9l8.07-8.06a2.85 2.85 0 1 1 4.03 4.03l-8.06 8.08"/><path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1.08 1.1 2.49 2.02 4 2.02 2.2 0 4-1.8 4-4.04a3.01 3.01 0 0 0-3-3.02z"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
    "package": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.29 7 12 12l8.71-5"/><path d="M12 22V12"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "alert": '<path d="M12 9v4"/><path d="M12 17h.01"/><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
}
def ico(name, size=18, sw=2.2):
    return (f'<span class="dk-ico"><svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg></span>')

# Gemeinsames Stylesheet der Produktseite (steht im ersten Block des Hauptbereichs und gilt für alle Sections darunter)
CSS = f"""<style>
.product-title{{font-weight:700!important;letter-spacing:-.01em}}
.badge.bestseller{{text-transform:capitalize}}
.dk-ico{{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;background:{TINT};color:{RED};flex:none}}
.dk-info{{display:flex;gap:10px;align-items:center;background:{SOFT};border-left:4px solid {RED};border-radius:8px;padding:10px 14px;font-weight:600;font-size:15px;line-height:1.35}}
.dk-info .dk-ico{{width:30px;height:30px;background:#fff}}
.dk-usp{{list-style:none;padding:0;margin:6px 0 18px;display:grid;gap:10px;font-size:15px}}
.dk-usp li{{display:flex;gap:10px;align-items:flex-start;line-height:1.4}}
.dk-usp .dk-ico{{width:22px;height:22px;margin-top:1px}}
.product-form__input--color input[data-handle="weiss"]+label{{--option-color:#ffffff !important}}
.product-form__input--color input[data-handle="cremeweiss"]+label{{--option-color:#F3ECD9 !important}}
.product-form__input--color input[data-handle="schwarz"]+label{{--option-color:#1E1E1E !important}}
.product-form__input--color input[data-handle="grau"]+label{{--option-color:#8A8D91 !important}}
.product-form__input--color input[data-handle="hellgrau"]+label{{--option-color:#C9CBCD !important}}
.product-form__input--color input[data-handle="anthrazit"]+label{{--option-color:#3A3D40 !important}}
.product-form__input--color label::after{{box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}}
.dk-tiers-h{{font-size:14px;font-weight:600;margin:4px 0 14px}}
.dk-tiers{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:0 0 16px}}
.dk-tier{{position:relative;border:1.5px solid #E2E2E2;border-radius:12px;padding:18px 6px 10px;text-align:center;cursor:pointer;background:#fff;color:{INK};font:inherit;transition:border-color .15s}}
.dk-tier:hover{{border-color:#bbb}}
.dk-tier.on{{border-color:{RED};background:#FDF4F5;box-shadow:0 0 0 1px {RED}}}
.dk-tier .tag{{position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:{RED};color:#fff;font-size:11px;font-weight:700;padding:2px 9px;border-radius:20px;white-space:nowrap}}
.dk-tier .q{{display:block;font-size:13px;font-weight:600;color:#555}}
.dk-tier .p{{display:block;font-size:20px;font-weight:800;margin:2px 0 0}}
.dk-tier .u{{display:block;font-size:11px;color:#888}}
.dk-tier .t{{display:block;border-top:1px solid #eee;margin-top:8px;padding-top:6px;font-size:13px;font-weight:700;color:{RED}}}
.dk-trust{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;border:1px solid #E5E5E5;border-radius:12px;padding:14px 8px;margin:16px 0 12px}}
.dk-trust div{{display:flex;flex-direction:column;align-items:center;text-align:center;gap:7px;font-size:12.5px;line-height:1.3;font-weight:600}}
.dk-trust .dk-ico{{width:38px;height:38px}}
.dk-setcard{{display:flex;gap:14px;align-items:center;background:{TINT};border-radius:12px;padding:14px 16px;text-decoration:none;color:{INK};margin:0 0 8px}}
.dk-setcard img{{width:68px;height:68px;border-radius:10px;object-fit:cover;background:#fff;flex:none}}
.dk-setcard strong{{display:block;font-size:15px;margin-bottom:2px}}
.dk-setcard span{{font-size:14px;line-height:1.4}}
.dk-setcard em{{font-style:normal;color:{RED};font-weight:700;white-space:nowrap}}
.dk-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px;text-align:left;margin-top:26px}}
.dk-grid.c3{{grid-template-columns:repeat(3,1fr)}}
.dk-grid.c4{{grid-template-columns:repeat(4,1fr)}}
@media (max-width:989px){{.dk-grid.c3,.dk-grid.c4{{grid-template-columns:repeat(2,1fr)}}}}
@media (max-width:599px){{.dk-grid.c3,.dk-grid.c4{{grid-template-columns:1fr}}}}
.dk-card{{background:#fff;border-radius:16px;padding:24px;box-shadow:0 2px 16px rgba(0,0,0,.05)}}
.dk-card.line{{box-shadow:none;border:1px solid #E8E8E8}}
.dk-card .dk-ico{{width:50px;height:50px;margin-bottom:16px}}
.dk-card h3{{font-size:18px;margin:0 0 6px;line-height:1.3}}
.dk-card p{{margin:0;font-size:15px;line-height:1.5;color:#4A4A4A}}
.dk-card a{{display:inline-block;margin-top:10px;font-weight:700;color:{RED};text-decoration:none}}
.dk-step{{display:flex;flex-direction:column}}
.dk-price [hidden]{{display:none!important}}
.rich-text--transparent-false{{padding-top:56px!important;padding-bottom:56px!important}}
.rich-text--transparent-false .rich-text__inner{{padding-top:0!important;padding-bottom:0!important}}
.rich-text .rte:last-child{{margin-bottom:0!important}}
.shopify-section:has(.rich-text--transparent-false) + .shopify-section:has(.rich-text--transparent-false){{margin-top:32px}}
@media (max-width:767px){{.rich-text--transparent-false{{padding-top:36px!important;padding-bottom:36px!important}}}}
.dk-grau{{margin-bottom:16px!important}}
.dk-amp{{background:#fff;border-radius:16px;padding:24px;border-top:6px solid;box-shadow:0 2px 16px rgba(0,0,0,.05);text-align:left}}
.dk-amp .hd{{display:flex;align-items:center;gap:12px;font-weight:800;font-size:18px;margin-bottom:10px}}
.dk-amp p{{margin:0;font-size:15px;line-height:1.55;color:#4A4A4A}}
.dk-amp a{{color:{RED}}}
.dk-set{{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;text-align:left}}
.dk-set .hero{{width:100%;border-radius:18px;display:block}}
.dk-set h2{{margin:0 0 10px;font-size:34px;line-height:1.15}}
.dk-si-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px}}
.dk-si{{display:flex;align-items:center;gap:10px;background:#fff;border-radius:12px;padding:8px;text-decoration:none;color:{INK};font-size:14px;line-height:1.3}}
.dk-si img{{width:52px;height:52px;border-radius:8px;object-fit:cover;background:{SOFT};flex:none}}
.dk-si b{{color:{RED}}}
.dk-set-btns{{display:flex;flex-wrap:wrap;align-items:center;gap:18px}}
.dk-add.dk-add-set{{width:auto;height:auto;border-radius:8px;padding:15px 30px;font-size:16px;font-weight:700}}
.dk-add.dk-add-set.ok{{font-size:16px}}
.dk-si,.dk-si *,.dk-sp a{{text-decoration:none!important}}
.dk-si span{{color:{INK}}}
.dk-step .dk-pill{{align-self:flex-start}}
.dk-set-btns a{{color:{INK};font-weight:700}}
@media (max-width:899px){{.dk-set{{grid-template-columns:1fr;gap:24px}}.dk-set h2{{font-size:26px}}}}
@media (max-width:420px){{.dk-si-grid{{grid-template-columns:1fr}}}}
.dk-sps{{margin-top:auto;padding-top:16px;display:grid;gap:8px}}
.dk-sp{{display:flex;align-items:center;gap:10px;background:{SOFT};border-radius:10px;padding:8px;font-size:13px;line-height:1.3}}
.dk-sp img{{width:44px;height:44px;border-radius:6px;object-fit:cover;background:#fff;display:block}}
.dk-sp span{{flex:1}}.dk-sp span a{{display:block;font-weight:700;color:{INK};text-decoration:none;margin-bottom:2px}}
.dk-add{{width:32px;height:32px;flex:none;border:0;border-radius:50%;background:{RED};color:#fff;font-size:20px;line-height:1;cursor:pointer}}
.dk-add.ok{{background:#2E8B57;font-size:15px}}
.dk-step .n{{font-size:44px;font-weight:800;color:{RED};line-height:1}}
.dk-pill{{display:inline-block;background:{INK};color:#fff;font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px;margin:12px 0 10px}}
.dk-time{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;text-align:left;margin-top:26px}}
.dk-time>div{{background:#333;border-radius:16px;padding:24px;border-top:4px solid {RED}}}
.dk-time .yr{{font-size:34px;font-weight:800;color:#fff;line-height:1}}
.dk-time h3{{color:#fff;font-size:18px;margin:12px 0 6px}}
.dk-time p{{color:#D6D6D6;font-size:15px;line-height:1.5;margin:0}}
.dk-time a{{display:inline-block;margin-top:12px;color:#fff;font-weight:700;text-decoration:none;border-bottom:2px solid {RED}}}
.dk-fbt{{margin:18px 0 12px}}
.dk-fbt-h{{font-size:16px;font-weight:700;margin:0 0 10px}}
.dk-fbt-i{{display:flex;gap:12px;align-items:center;border:1.5px solid #E2E2E2;border-radius:12px;padding:8px 12px;margin:0 0 6px;cursor:pointer;background:#fff}}
.dk-fbt-i:has(input:checked){{border-color:{RED};background:#FDF4F5}}
.dk-fbt-i input{{width:18px;height:18px;accent-color:{RED};flex:none;margin:0}}
.dk-fbt-i img{{width:44px;height:44px;border-radius:8px;object-fit:cover;background:{SOFT};flex:none}}
.dk-fbt-i span{{font-size:14px;line-height:1.35}}
.dk-fbt-i b{{display:block;font-weight:600}}
.dk-fbt-i.me{{cursor:default;opacity:.85}}
.dk-fbt-b{{width:100%;margin-top:4px;padding:14px;border:2px solid {RED};border-radius:8px;background:#fff;color:{RED};font:inherit;font-weight:700;font-size:15px;cursor:pointer}}
.dk-fbt-b:hover{{background:{RED};color:#fff}}
.dk-more{{margin-top:28px;border-top:1px solid #E5E5E5}}
.dk-more details{{border-bottom:1px solid #E5E5E5}}
.dk-more summary{{display:flex;justify-content:space-between;align-items:center;padding:18px 0;font-weight:700;font-size:17px;cursor:pointer;list-style:none}}
.dk-more summary::-webkit-details-marker{{display:none}}
.dk-more summary::after{{content:'+';font-size:22px;font-weight:400;color:{RED}}}
.dk-more details[open] summary::after{{content:'–'}}
.dk-more .rte{{padding:0 0 20px;font-size:15px;line-height:1.6}}
.dk-more .rte table{{margin:0}}
.product-grid-container{{margin-bottom:64px}}
@media (max-width:767px){{.product-grid-container{{margin-bottom:40px}}}}
.product-gallery-sticky:has(.dk-more){{position:relative!important;top:auto!important}}
@media (max-width:767px){{.dk-card,.dk-time>div{{padding:20px}}.dk-tier .p{{font-size:17px}}}}
</style>"""

def sec(type, settings=None, blocks=None): return {"type": type, "settings": settings or {}, "blocks": blocks or []}
def blk(type, **s): return {"type": type, "settings": s}
def liquid(html): return blk("custom_liquid", custom_liquid=html)
def spacer(d=60, m=36): return sec("spacer", {"spacer_desktop": d, "spacer_mobile": m})
CLEAN = {"color_bg": "rgba(0,0,0,0)", "color_heading": INK, "color_text": INK, "color_links": RED,
         "disable_top_spacing": True, "disable_bottom_spacing": True}
def eyebrow(t): return f'<p style="color:{RED};font-weight:700;letter-spacing:.08em;font-size:13px;margin:0 0 6px">{t}</p>'
def rich(heading, html, eyebrow_text=None, width="grid", align="left"):
    bl = []
    if eyebrow_text: bl.append(blk("text", text="", custom_liquid=eyebrow(eyebrow_text)))
    if heading: bl.append(blk("heading", text=heading, size="h2", marker_color=RED, marker_style="style1"))
    bl.append(blk("text", text="", custom_liquid=html))
    return sec("rich-text", {**CLEAN, "text_width": width, "text_position": "center", "text_alignment": align}, bl)

# ---------- 1. Hauptbereich (Above the fold) ----------
usp = '<p style="font-size:17px;line-height:1.45;margin:-4px 0 4px;color:#262626"><strong>{{ product.metafields.custom.usp_zeile }}</strong></p>'
def usp_li(b, t): return f'<li>{ico("check", 13, 3)}<span><strong>{b}</strong> {t}</span></li>'
bullets = ('<ul class="dk-usp">' + usp_li("Hält sofort:", "Hohe Anfangsfestigkeit – Klemmen und Abstützen kannst du dir oft sparen.") +
    usp_li("Ohne Primer:", "Haftet auf Aluminium, GFK, Glas, PVC und lackiertem Metall.") +
    usp_li("Für heiße Dächer gemacht:", "dauerelastisch von −40 bis +120 °C, kurzzeitig bis 180 °C.") +
    usp_li("Unsichtbar machbar:", "Nach der Hautbildung nass in nass überlackierbar.") + "</ul>")
# Farb-Hinweis direkt unter den Farbpunkten (Skript hängt ihn dort ein und nach jedem Variantenwechsel wieder an)
grundpreis = """<p class="dk-grau" style="font-size:13px;color:#555;margin:8px 0 0">Grau gesucht? MS-5 gibt es nur in Weiß und Schwarz – in Grau gibt es <a href="/products/dekasyl-ms-2-kleb-dichtstoff" style="color:#D42A3B;font-weight:600">DEKAsyl MS-2 ›</a> (etwas weniger Klebkraft, ohne Sofort-Haftung).</p>
<script>(()=>{const h=document.currentScript.previousElementSibling;const put=()=>{const c=document.querySelector('.product-information .product-form__input--color');if(c&&c.nextElementSibling!==h)c.after(h)};put();document.addEventListener('change',()=>setTimeout(put,300));})();</script>"""
liefer = f'<p style="margin:0;font-weight:600;color:{GREEN}">● {{{{ product.metafields.custom.lieferhinweis }}}}</p>'
icons = ('<div class="dk-trust">' + f'<div>{ico("truck", 19)}Versand in 1–3 Werktagen</div>'
    f'<div>{ico("shield", 19)}Anwendungs&shy;versprechen: hält nicht = Ersatz</div>' + f'<a href="/pages/beratung" style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:7px;font-size:12.5px;line-height:1.3;font-weight:600;color:inherit;text-decoration:none">{ico("chat", 19)}Kostenlose Anwendungs&shy;beratung ›</a></div>')
# "Oft zusammen gekauft": dieses Produkt + abgestimmtes Zubehör, ein Klick legt alles in den Warenkorb (Cart-AJAX-API)
FBT = [("dekaclean-ultra-haftreiniger", "last"), ("dekavator-22-nf-haftvermittler", "first"), ("kartuschenpresse-290-310-ml", "first")]
fbt = ('<div class="dk-fbt"><p class="dk-fbt-h">Oft zusammen gekauft</p>'
    '{%- assign mv = product.selected_or_first_available_variant -%}'
    '<label class="dk-fbt-i me"><input type="checkbox" checked disabled><img src="{{ product.featured_image | image_url: width: 120 }}" alt="">'
    '<span><b>Dieser Artikel: {{ product.title | split: " " | slice: 0, 2 | join: " " }}</b><span class="dk-fbt-mp">{{ mv.price | money }}</span></span></label>' +
    "".join('{%- assign fp = all_products["' + h + '"] -%}{%- assign fv = fp.variants.' + w + ' -%}'
        '<label class="dk-fbt-i"><input type="checkbox" checked value="{{ fv.id }}" data-p="{{ fv.price }}"><img src="{{ fp.featured_image | image_url: width: 120 }}" alt="" loading="lazy">'
        '<span><b>{{ fp.title }}</b>{% unless fp.variants.size == 1 %}{{ fv.title }} · {% endunless %}{{ fv.price | money }}</span></label>' for h, w in FBT) +
    '<button type="button" class="dk-fbt-b">Alle zusammen in den Warenkorb · <span></span></button></div>'
    """<script>(()=>{const P={ {%- for v in product.variants -%}"{{ v.id }}":{{ v.price }}{%- unless forloop.last -%},{%- endunless -%}{%- endfor -%} };
const box=document.currentScript.previousElementSibling,btn=box.querySelector('.dk-fbt-b'),fmt=c=>'€'+(c/100).toFixed(2).replace('.',',');
const mid=()=>document.getElementById('product-form-{{ section.id }}')?.querySelector('[name=id]')?.value||'{{ product.selected_or_first_available_variant.id }}';
const upd=()=>{const m=P[mid()]??0;box.querySelector('.dk-fbt-mp').textContent=fmt(m);let t=m;box.querySelectorAll('input[value]:checked').forEach(i=>t+=+i.dataset.p);btn.querySelector('span').textContent=fmt(t)};
box.addEventListener('change',upd);document.addEventListener('change',()=>setTimeout(upd,120));
btn.addEventListener('click',async()=>{btn.disabled=true;const items=[{id:+mid(),quantity:1},...[...box.querySelectorAll('input[value]:checked')].map(i=>({id:+i.value,quantity:1}))];
await fetch('/cart/add.js',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({items})});location.href='/cart'});upd();})();</script>""")

# Beschreibung (offen) + Versand: auf dem Desktop unter der Galerie, damit die linke Spalte nicht leer bleibt; mobil an Ort und Stelle
MORE = ('<div class="dk-more"><details open><summary>Beschreibung</summary><div class="rte">{{ product.description }}</div></details>'
    '<!--MEHR--><details><summary>Versand &amp; Rückgabe</summary><div class="rte"><p>Versand in 1–3 Werktagen mit DHL, ab 49 € versandkostenfrei. 14 Tage Widerrufsrecht für ungeöffnete Ware.</p></div></details></div>'
    """<script>(()=>{const m=document.currentScript.previousElementSibling,home=m.parentElement;
const place=()=>{const g=document.querySelector('.product-gallery-sticky'),i=document.querySelector('.product-information');
const side=g&&i&&g.getBoundingClientRect().right<=i.getBoundingClientRect().left+1;
if(side&&m.parentElement!==g)g.appendChild(m);else if(!side&&m.parentElement!==home)home.appendChild(m)};
place();addEventListener('resize',place);})();</script>""")

# Preisblock: ersetzt die Preiszeile des Themes. Zeigt den Gesamtpreis der gewählten Staffel (mit Streichpreis und Ersparnis)
# und direkt darunter den Grundpreis je Liter (PAngV: klar erkennbar beim Gesamtpreis) – beides rechnet bei Staffel- und Variantenwechsel neu.
preis = ("""<style>.product-price-container{display:none}
.dk-price{margin:4px 0 14px}.dk-price .dk-row{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px}
.dk-price .now{font-size:30px;font-weight:800;line-height:1.1}.dk-price .was{font-size:18px;color:#8a8a8a}
.dk-price .save,.dk-price .bs{background:""" + RED + """;color:#fff;font-size:12px;font-weight:700;padding:3px 9px;border-radius:20px}
.dk-price .sub{font-size:14px;color:#444;margin-top:6px}.dk-price .sub b{font-weight:700;color:#262626}.dk-price .sub a{color:inherit}</style>"""
    '<div class="dk-price"><div class="dk-row"><s class="was" hidden></s><span class="now"></span><span class="save" hidden></span>'
    '{%- if product.tags contains "bestseller" -%}<span class="bs">Bestseller</span>{%- endif -%}</div>'
    '<div class="sub"><b class="gp"></b> · inkl. MwSt., zzgl. <a href="/policies/shipping-policy">Versand</a> · ab 49 € versandkostenfrei</div></div>'
    """<script>(()=>{const V={ {%- for v in product.variants -%}"{{ v.id }}":[{{ v.price }},{% if v.option2 contains '600' %}0.6{% else %}0.29{% endif %}]{%- unless forloop.last -%},{%- endunless -%}{%- endfor -%} };
const box=document.currentScript.previousElementSibling,t=document.querySelector('.product-title-container .product-title');
if(t)t.after(box);
const f=()=>document.getElementById('product-form-{{ section.id }}'),fmt=c=>'€'+(c/100).toFixed(2).replace('.',',');
let q=1,d=0;
const upd=()=>{const id=f()?.querySelector('[name=id]')?.value;const [p,l]=V[id]??[{{ product.selected_or_first_available_variant.price }},0.29];
const u=p-Math.floor(p*d/100);box.querySelector('.now').textContent=fmt(u*q);
const was=box.querySelector('.was'),sv=box.querySelector('.save');was.hidden=sv.hidden=!d;was.textContent=fmt(p*q);sv.textContent='Spare '+d+' %';
box.querySelector('.gp').textContent=fmt(Math.round(u/l))+' / 1 l'};
document.addEventListener('dk:tier',e=>{q=e.detail.q;d=e.detail.d;upd()});document.addEventListener('change',()=>setTimeout(upd,150));upd();})();</script>""")

# Mengenstaffel: setzt die Menge im Produktformular; die Rabatte selbst sind automatische Rabatte im Shop
# (ab 3 Stück 5 %, ab 6 Stück 10 %), damit der Preis im Warenkorb stimmt. Preise je Variante rechnet das Skript neu.
TIERS = [(1, 0, "1 Stück", ""), (3, 5, "3 Stück", "Spare 5 %"), (6, 10, "6 Stück · Karton", "Spare 10 %")]
staffel = ('<p class="dk-tiers-h">Menge wählen – mehr sparen</p><div class="dk-tiers">' + "".join(
    f'<button type="button" class="dk-tier{" on" if n == 1 else ""}" data-q="{n}" data-d="{d}">' + (f'<span class="tag">{tag}</span>' if tag else "") +
    f'<span class="q">{lab}</span><span class="p"></span><span class="u">pro Stück</span><span class="t"></span></button>' for n, d, lab, tag in TIERS) +
    '</div><input type="hidden" name="quantity" value="1" form="product-form-{{ section.id }}">'
    """<script>(()=>{const P={ {%- for v in product.variants -%}"{{ v.id }}":{{ v.price }}{%- unless forloop.last -%},{%- endunless -%}{%- endfor -%} };
const s=document.currentScript,root=s.previousElementSibling.previousElementSibling,qi=s.previousElementSibling,
f=()=>document.getElementById('product-form-{{ section.id }}'),fmt=c=>'€'+(c/100).toFixed(2).replace('.',',');
const upd=()=>{const id=f()?.querySelector('[name=id]')?.value;const p=P[id]??{{ product.selected_or_first_available_variant.price }};
root.querySelectorAll('.dk-tier').forEach(b=>{const n=+b.dataset.q,u=p-Math.floor(p*b.dataset.d/100);b.querySelector('.p').textContent=fmt(u);b.querySelector('.t').textContent=fmt(u*n)})};
root.querySelectorAll('.dk-tier').forEach(b=>b.addEventListener('click',()=>{root.querySelectorAll('.dk-tier').forEach(x=>x.classList.remove('on'));b.classList.add('on');qi.value=b.dataset.q;document.dispatchEvent(new CustomEvent('dk:tier',{detail:{q:+b.dataset.q,d:+b.dataset.d}}))}));
document.addEventListener('change',()=>setTimeout(upd,120));upd();})();</script>""")
main_blocks = [
    # Infobox als Custom Liquid: Vision rendert info_box-Blöcke auf dem Desktop unter der Galerie – sie soll aber über dem Titel stehen
    # keine Infobox über dem Titel mehr: sagte fast dasselbe wie die USP-Zeile darunter – die USP-Zeile direkt am Titel trägt die Botschaft allein
    liquid(CSS),
    # kein Vendor-Text: im eigenen Markenshop ist jedes Produkt von Dekalin
    blk("title", show_products_rating=True, show_products_rating_average=True, show_custom_badges=True),
    liquid(preis),
    liquid(usp),
    liquid(bullets),
    blk("variant_picker", picker_type="button", color_picker=True, variant_is_disabled=True, sizing_guide_variant="", sizing_guide_text=""),
    liquid(grundpreis),
    liquid(staffel),   # statt freiem Mengenfeld: drei feste Stufen mit sichtbarer Ersparnis
    liquid(liefer),
    blk("buy_buttons", show_dynamic_checkout=False, show_gift_card_recipient=False),
    liquid(icons),
    liquid(fbt),
    # Set-Karte bewusst nicht in der Kaufbox: direkt unter "Oft zusammen gekauft" wären es zwei konkurrierende Zubehör-Angebote;
    # das Set hat seine eigene Section weiter unten und steht im Mega-Menü.
    liquid(MORE),
]
main = sec("main-product", {"enable_sticky_add_to_cart": False, "show_taxes_included": True, "thumbnail_position": "left",
                            "media_aspect_ratio": "square", "display_captions": False, "lightbox": True,
                            "media_fullwidth_mobile": True, "mobile_thumbnails": False}, main_blocks)

# ---------- 2. Below the fold ----------
def col(title, text, link_label="", link=""): return blk("column", title=title, text=f"<p>{text}</p>", link_label=link_label, link=link)
def card(icon, title, text, link_label="", link="", cls="dk-card"):
    return (f'<div class="{cls}">{ico(icon, 24, 2)}<h3>{title}</h3><p>{text}</p>' + (f'<a href="{link}">{link_label} ›</a>' if link else "") + "</div>")
vorteile = rich("Klebt. Dichtet. Hält.", '<p>Ein Kraftkleber für alles, was ohne Bohrloch aufs Fahrzeug soll.</p><div class="dk-grid c3">' +
    card("bolt", "Hält sofort", "Hohe Anfangsfestigkeit: Das Bauteil sitzt schon beim Andrücken.") +
    card("layers", "Ohne Primer", "Haftet direkt auf Alu, GFK, Glas, PVC und lackiertem Metall.") +
    card("thermo", "Hitze & Frost", "Dauerelastisch von −40 bis +120 °C, kurzzeitig 180 °C.") +
    card("sun", "Sonnenfest", "Sehr gute UV- und Alterungsbeständigkeit – auch nach Jahren auf dem Dach.") +
    card("brush", "Überlackierbar", "Nach der Hautbildung nass in nass lackieren – die Naht verschwindet.") +
    card("leaf", "Angenehm zu verarbeiten", "Ohne Lösemittel, Isocyanat und PVC. Neutral und geruchlos.") + "</div>",
    "DARUM MS-5", "grid", "center")
vorteile["settings"]["color_bg"] = SOFT

chip = 'display:inline-block;margin:4px;padding:10px 16px;border:1px solid #ddd;border-radius:30px;font-weight:600;text-decoration:none;color:#262626;background:#fff'
anw = [("Solarmodul & Spoiler", "solarmodul-kleben"), ("SAT-Anlage & Antenne", "sat-anlage-antenne-kleben"),
       ("Markise, Dachträger & Anbauteile", "markise-dachtraeger-anbauteile-kleben"), ("Fenster & Dachdurchführungen", "fenster-scheiben-einkleben"),
       ("Kantenprofile an Anhängern", "kantenleisten-keder"), ("Halter & Abdeckungen im Ausbau", "halter-leisten-innenausbau-kleben")]
anwendungen = rich("Wofür Profis MS-5 nehmen",
    '<p>Klick auf dein Projekt – wir zeigen dir, was du dafür brauchst.</p><div style="margin-top:10px">' +
    "".join(f'<a href="/collections/{h}" style="{chip}">{t} ›</a>' for t, h in anw) + "</div>", "ANWENDUNGEN", "grid", "center")

# Haftgrund-Ampel: drei Karten nebeneinander über die volle Breite (statt schmaler Spalte mit viel Leerraum)
def ampel(color, tint, icon, title, text):
    svg = ico(icon, 19, 2.6).split(">", 1)[1][:-len("</span>")]   # nur das SVG, eigener Kreis in Ampelfarbe
    return (f'<div class="dk-amp" style="border-top-color:{color}"><div class="hd"><span class="dk-ico" style="background:{tint};color:{color};width:38px;height:38px">'
            f'{svg}</span>{title}</div><p>{text}</p></div>')
ampel_html = ('<p>Die häufigste Frage vor dem Kauf – hier die ehrliche Antwort.</p><div class="dk-grid c3">' +
    ampel(GREEN, "#E3F3EA", "check", "Hält ohne Primer", "Aluminium, Edelstahl, verzinkter Stahl, Zink, Kupfer, Messing, pulverbeschichtetes und lackiertes Metall, Glas, PVC, GFK/Polyester, gestrichenes und lackiertes Holz.") +
    ampel("#C99A00", "#FBF3D6", "alert", "Mit Haftvermittler sicherer", 'Bei hoher Hitze, Vibration oder Last – besonders bei Feuchtigkeit – vorher <a href="/products/dekavator-22-nf-haftvermittler">DEKAVATOR 22 NF</a> auftragen.') +
    ampel(RED, TINT, "x", "Hält nicht", 'PE, PP und Teflon. <a href="/pages/beratung">Schreib uns</a> – wir finden eine Lösung für dein Material.') +
    '</div><p style="font-size:14px;margin-top:18px">Immer gilt: Fläche sauber, trocken, staub- und fettfrei machen – am besten mit <a href="/products/dekaclean-ultra-haftreiniger">DEKACLEAN Ultra</a>. Im Zweifel vorher an einer unauffälligen Stelle testen.</p>')
haftgrund = rich("Hält es auf deinem Material?", ampel_html, "HAFTGRUND-CHECK", "grid", "center")
haftgrund["settings"]["color_bg"] = SOFT; haftgrund["settings"]["disable_top_spacing"] = False; haftgrund["settings"]["disable_bottom_spacing"] = False

def era(year, title, text, link_label="", link=""):
    return f'<div><div class="yr">{year}</div><h3>{title}</h3><p>{text}</p>' + (f'<a href="{link}">{link_label} ›</a>' if link else "") + "</div>"
story = rich("Kleben auf Meisterniveau – seit 1907", '<p>Über 100 Jahre Werkstatt-Wissen stecken in jeder Kartusche – auch in MS-5.</p><div class="dk-time">' +
    era(1907, "Deutsche Klebstoffwerke", "Angefangen hat alles mit den „Deutschen Klebstoffwerken“.", "Unsere Geschichte", "/pages/ueber-dekalin") +
    era(1935, "Partner der Autobauer", "Ab 1935 arbeiten wir mit dem Automobilbau zusammen – daher kommt unser Anspruch an Haltbarkeit.") +
    era(2012, "Vom Werkstattprofi aufs Wohnmobildach", "Lösungen für Caravaning, Schritt für Schritt erklärt: Solarmodul, SAT-Anlage, Markise.") +
    era(2014, "Wir bringen Kleben bei", "Schulungen nach DIN 2304 und das Buch „Klebt nicht gibt's nicht!“ vom „Klebepapst“ Michael Windecker.", "Mehr über Schulungen", "/pages/schulungen") +
    "</div>", "UNSERE GESCHICHTE", "grid", "center")
story["settings"].update({"color_bg": INK, "color_heading": "#ffffff", "color_text": "#E6E6E6", "color_links": "#ffffff"})

# Schritt-Karten mit dem Produkt, das man in diesem Schritt braucht (Bild, Preis, direkt in den Warenkorb)
def sp(handle, which="first"):
    return ('{%- assign sp = all_products["' + handle + '"] -%}{%- assign sv = sp.variants.' + which + ' -%}'
            '<div class="dk-sp"><a href="{{ sp.url }}"><img src="{{ sp.featured_image | image_url: width: 120 }}" alt="" loading="lazy"></a>'
            '<span><a href="{{ sp.url }}">{{ sp.title }}</a>{% unless sp.variants.size == 1 %}{{ sv.title }} · {% endunless %}{{ sv.price | money }}</span>'
            '<button type="button" class="dk-add" data-id="{{ sv.id }}" aria-label="In den Warenkorb">+</button></div>')
def step(n, t, badge, text, prods=()):
    return (f'<div class="dk-card line dk-step"><div class="n">{n}</div><span class="dk-pill">{badge}</span><h3>{t}</h3><p>{text}</p>'
            + (f'<div class="dk-sps">{"".join(sp(*x) for x in prods)}</div>' if prods else "") + "</div>")
add_js = """<script>document.addEventListener('click',async e=>{const b=e.target.closest('.dk-add');if(!b||b.disabled)return;b.disabled=true;
await fetch('/cart/add.js',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({items:[{id:+b.dataset.id,quantity:1}]})});
b.textContent=b.dataset.ok||'✓';b.classList.add('ok');});</script>"""
schritte = rich("So klebst du ein Solarmodul in 4 Schritten", '<p><a href="/pages/anleitung-solarmodul-kleben">Ganze Anleitung ansehen ›</a></p><div class="dk-grid c4">' +
    step(1, "Reinigen", "5 min", "Fläche mit DEKACLEAN Ultra sauber, trocken und fettfrei machen. Bei Feuchte oder hoher Last DEKAVATOR 22 NF auftragen.",
         [("dekaclean-ultra-haftreiniger", "last"), ("dekavator-22-nf-haftvermittler",)]) +
    step(2, "Raupe ziehen", "7-mm-Raupe", "Düse auf ca. 7 mm schneiden und mit der Presse eine gleichmäßige Raupe auf Spoiler oder Halter ziehen. Verarbeite bei +5 bis +35 °C.",
         [("kartuschenpresse-290-310-ml",)]) +
    step(3, "Fügen", "&lt; 15 min", "Bauteil innerhalb von 15 Minuten aufsetzen und andrücken, bis eine 3–5 mm dicke Klebenaht entsteht. Austretende Naht mit DEKAFINISHER glätten.",
         [("dekafinisher-glaettmittel",)]) +
    step(4, "Aushärten", "24–48 h", "Haut nach ca. 12 Minuten, 4 mm durchgehärtet nach 24 Stunden. Voll belastbar nach 24–48 Stunden.") + "</div>" + add_js,
    "ANLEITUNG", "grid", "center")

TS = 'width:100%;border-collapse:collapse;font-size:14px;text-align:left;margin-top:12px'
def table(head, rows, hl=3):
    th = "".join(f'<th style="padding:10px;border-bottom:2px solid #262626;{"background:#FBEAEC;" if i == hl else ""}">{h}</th>' for i, h in enumerate(head))
    tr = "".join("<tr>" + "".join(f'<td style="padding:10px;border-bottom:1px solid #e5e5e5;{"background:#FBEAEC;font-weight:600;" if i == hl else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div style="overflow-x:auto"><table style="{TS}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
fam = table(["", "MS-1 · Einsteiger", "MS-2 · Fortgeschrittene", "MS-5 · Profi"], [
    ["Klebkraft", "●○○○○", "●●●○○", "●●●●●"],
    ["Ideal für", "Fugen, Dichtnähte, Überlappungen", "Verbindungen, Dichtnähte, Solaranlagen", "Solarmodule, SAT-Anlagen, Spoiler, Dachkonstruktionen"],
    ["Hält sofort (High Tack)", "–", "–", "✓"], ["Farben", "weiß, grau, schwarz", "weiß, grau, schwarz", "weiß, schwarz"],
    ["Gebinde", "290 ml", "290 ml, 600 ml", "290 ml, 600 ml (weiß)"],
    ["", '<a href="/products/dekasyl-ms-1-dichtstoff" style="color:#D42A3B">Zum MS-1 ›</a>', '<a href="/products/dekasyl-ms-2-kleb-dichtstoff" style="color:#D42A3B">Zum MS-2 ›</a>', "Du bist hier"]])
sika = table(["Datenblatt-Wert", "DEKAsyl MS-5", "Sikaflex-554"], [
    ["Basis", "MS-Polymer", "STP (silanterminiertes Polymer)"], ["Hautbildung", "ca. 12 min (20 °C)", "25 min (23 °C)"],
    ["Shore-A-Härte", "ca. 55", "55"], ["Zugscherfestigkeit", "ca. 2,5 MPa", "2,5 MPa"], ["Zugfestigkeit", "ca. 2,8 MPa", "3,5 MPa"],
    ["Bruchdehnung", "ca. 210 %", "500 %"], ["Temperaturbeständigkeit", "−40 bis +120 °C, kurz 180 °C", "−50 bis +90 °C"],
    ["Verarbeitung", "+5 bis +35 °C", "+5 bis +40 °C"], ["Lagerfähigkeit", "18 Monate (Kartusche)", "12 Monate"], ["Nachweise", "keine genannt", "DIN EN 45545-2, ISEGA"]], hl=1)
vergleich = rich("Welcher DEKAsyl passt zu deinem Projekt?",
    "<p>Drei Stufen, ein Prinzip: Je mehr ein Bauteil halten muss, desto höher die Stufe.</p>" + fam +
    '<h3 style="margin-top:36px">MS-5 und Sikaflex-554 im Datenblatt-Vergleich</h3><p>Fair verglichen: nur Herstellerangaben aus den Technischen Datenblättern.</p>' + sika +
    "<p><strong>Fazit:</strong> Beide kleben bei Scherung gleich fest (2,5 MPa). MS-5 bildet schneller eine Haut und ist für höhere Dachtemperaturen ausgelegt (bis +120 °C). Sikaflex-554 ist dehnfähiger und hat Nachweise für Bahn- und Lebensmittelbereich.</p>"
    '<p style="font-size:12px;color:#666">Quellen: Technisches Datenblatt DEKAsyl MS-5 (07/2024); Produktdatenblatt Sikaflex-554 (Sika Deutschland). Prüfnormen können abweichen. Sikaflex ist eine Marke der Sika AG.</p>',
    "DIE RICHTIGE WAHL", "large")

# Set als Produktkarte: großes Bild, Bestandteile als Mini-Kacheln mit Bild, Preis mit Ersparnis, direkt in den Warenkorb
def set_item(qty, handle, which, label):
    return ('{%- assign si = all_products["' + handle + '"] -%}'
            '<a class="dk-si" href="{{ si.url }}"><img src="{{ si.featured_image | image_url: width: 160 }}" alt="" loading="lazy"><span><b>' + qty + '</b> ' + label + '</span></a>')
set_html = ('{%- assign st = all_products["solar-montage-set"] -%}<div class="dk-set">'
    '<img class="hero" src="{{ st.featured_image | image_url: width: 900 }}" alt="Solar-Montage-Set" loading="lazy">'
    '<div><p style="color:' + RED + ';font-weight:700;letter-spacing:.08em;font-size:13px;margin:0 0 6px">SOLAR-MONTAGE-SET</p>'
    '<h2>Alles für ein Solarmodul in einem Paket</h2><p>Damit dein Modul hält, zählt die Vorbereitung. Im Set ist alles drin – aufeinander abgestimmt.</p>'
    '<div class="dk-si-grid">' + set_item("2 ×", "dekasyl-ms-5-kleb-dichtstoff", "first", "DEKAsyl MS-5, 290 ml") +
    set_item("1 ×", "dekaclean-ultra-haftreiniger", "last", "DEKACLEAN Reinigungstücher") +
    set_item("1 ×", "dekavator-22-nf-haftvermittler", "first", "DEKAVATOR 22 NF, 30 ml") + set_item("1 ×", "kartuschenpresse-290-310-ml", "first", "Kartuschenpresse") + '</div>'
    '<div class="dk-price" style="margin:18px 0 14px"><div class="dk-row"><span class="now">{{ st.price | money }}</span><s class="was">{{ st.compare_at_price | money }}</s><span class="save">Spare 10 %</span></div></div>'
    '<div class="dk-set-btns"><button type="button" class="dk-add dk-add-set" data-id="{{ st.selected_or_first_available_variant.id }}" data-ok="✓ Im Warenkorb">Set in den Warenkorb</button>'
    '<a href="{{ st.url }}">Farbe wählen &amp; Details ›</a></div></div></div>')
setsec = rich(None, set_html, None, "grid", "left")
setsec["settings"]["color_bg"] = TINT

tech_rows = [("Basis", "MS-Polymer"), ("Aushärtung", "durch Luftfeuchtigkeit"), ("Farben", "weiß, schwarz"), ("Dichte", "ca. 1,4 kg/l"),
    ("Hautbildungszeit (20 °C / 50 % r. F.)", "ca. 12 min"), ("Offene Zeit (Fügen)", "< 15 min"), ("Durchhärtung nach 24 h", "ca. 4 mm"),
    ("Shore-A-Härte (DIN 53505)", "ca. 55"), ("Volumenänderung (DIN 52451)", "< 3 %"), ("Standfestigkeit (Rheometer)", "ca. 700 Pa"),
    ("Zugspannung bei 100 % Dehnung", "ca. 1,7 MPa"), ("Zugspannung bei Bruch", "ca. 2,8 MPa"), ("Bruchdehnung", "ca. 210 %"),
    ("Scherspannung (DIN 53283)", "ca. 2,5 MPa"), ("Weiterreißfestigkeit", "ca. 14 N/mm"), ("Lösemittel / Isocyanat", "0 % / 0 %"),
    ("Temperaturbeständigkeit", "−40 °C bis +120 °C, kurzzeitig +180 °C (max. 20 min)"), ("Verarbeitungstemperatur", "+5 °C bis +35 °C"),
    ("UV- und Witterungsbeständigkeit", "hervorragend"), ("Lagerung", "ungeöffnet, trocken, +10 bis +30 °C: Kartusche 18 Monate, Schlauchbeutel 12 Monate"),
    ("Gebinde / Art.-Nr.", "290 ml weiß 62522 34 · 600 ml weiß 62523 12 · 290 ml schwarz 62524 34")]
tech_table = '<table style="width:100%;border-collapse:collapse;font-size:14px">' + "".join(
    f'<tr><td style="padding:8px 10px;border-bottom:1px solid #e5e5e5;width:45%;color:#555">{a}</td><td style="padding:8px 10px;border-bottom:1px solid #e5e5e5;font-weight:600">{b}</td></tr>' for a, b in tech_rows) + "</table>"
def tab(label, text="", cl=""): return blk("tab", tab_label=label, icon="none", text=text, text_columns="1", custom_liquid=cl)
technik = sec("tabbed-content", {"heading": "Technik & Downloads", "marker_style": "style1", "description": "", "text_size": "small", "tab_alignment": "left",
    "text_alignment": "left", "color_bg": "rgba(0,0,0,0)", "color_tabs": INK, "color_text": INK, "marker_color": RED,
    "disable_top_spacing": True, "disable_bottom_spacing": True}, [
    tab("Technische Daten", "", tech_table),
    tab("Haftgründe", "<p>Ohne Primer auf sauberen, trockenen, staub- und fettfreien Flächen aus Aluminium, Edelstahl, verzinktem Stahl, Zink, Kupfer, Messing, pulverbeschichtetem Metall, den meisten lackierten Metallen, Glas, PVC, Polyester (GFK) sowie gestrichenem und lackiertem Holz.</p><p>Keine Haftung ohne Vorbehandlung auf PE, PP und Teflon. Reinigung mit DEKACLEAN Ultra und Haftungstest empfohlen. Bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit: DEKAVATOR 22 NF.</p>"),
    tab("Verarbeitung", "<ul><li><strong>Verarbeiten:</strong> mit Hand- oder Druckluftpistole bei +5 bis +35 °C.</li><li><strong>Abdichten:</strong> innerhalb von 12 Minuten mit einem in DEKAFINISHER getauchten Spachtel glätten.</li><li><strong>Kleben:</strong> Teile innerhalb von 15 Minuten fügen. Empfohlene Klebeschicht 2 mm.</li><li><strong>Lackieren:</strong> nach 10 Minuten möglich, beste Lackhaftung nach etwa 4 Stunden.</li><li><strong>Reinigen:</strong> unausgehärtete Reste mit DEKACLEAN Ultra entfernen.</li></ul>"),
    tab("Downloads & Sicherheit", "<ul><li><a href=\"https://www.dekalin.de\">Technisches Datenblatt DEKAsyl MS-5 (PDF)</a></li><li>Sicherheitsdatenblatt DEKAsyl MS-5 (PDF, auf Anfrage)</li><li>Chemische Resistenz DEKAsyl MS-Polymer (PDF)</li></ul><p>Kennzeichnung: Nicht als gefährlich eingestuft nach CLP-Verordnung. EUH210: Sicherheitsdatenblatt auf Anfrage erhältlich.</p><p>Hersteller: Dekalin – support@dekalin.de</p>")])

service = rich("Wir lassen dich nicht allein", '<div class="dk-grid c4">' +
    card("chat", "Kostenlose Anwendungsberatung", "Schick uns ein Foto deines Projekts. Das Dekalin-Team sagt dir, welches Produkt hält.", "Beratung anfragen", "/pages/beratung", "dk-card line") +
    card("shield", "Anwendungsversprechen", "Hält MS-5 bei Verarbeitung nach Anleitung nicht, ersetzen wir dir das Material.", cls="dk-card line") +
    card("truck", "Schnell bei dir", "Versand in 1–3 Werktagen, ab 49 € versandkostenfrei.", cls="dk-card line") +
    card("award", "Original vom Hersteller", "Frische Ware direkt aus unserem Lager. Ungeöffnet 18 Monate lagerfähig.", cls="dk-card line") + "</div>",
    "SERVICE", "grid", "center")

faq_md = (pathlib.Path(__file__).parent.parent / "aufgabe1/04_pdp_texte.md").read_text(encoding="utf-8")
import re
faq_part = faq_md.split("### Section 12 – FAQ")[1].split("### Section 13")[0]
faqs = re.findall(r"\*\*\d+\. (.+?)\*\*\n(.+?)\n", faq_part)
faq = sec("collapsible-content", {"heading": "Häufige Fragen zu DEKAsyl MS-5", "description": '<p>Deine Frage ist nicht dabei? <a href="/pages/beratung">Schreib uns – wir antworten persönlich ›</a></p>',
    "color_bg": SOFT, "color_heading": INK, "marker_color": RED, "color_text": INK, "color_links": RED, "color_border": "#dddddd",
    "disable_top_spacing": False, "disable_bottom_spacing": False},
    [blk("collapsible_tab", heading=q, open=False, content=f"<p>{a.replace(' [A]', '')}</p>", custom_liquid="") for q, a in faqs])

stars = lambda n: "★" * n + "☆" * (5 - n)
rev = lambda n, t: f'<div style="background:#fff;border:1px solid #e5e5e5;border-radius:12px;padding:18px"><div style="color:{RED};font-size:18px">{stars(n)}</div><p style="margin:8px 0 6px">„{t}“</p><p style="font-size:12px;color:#888;margin:0">Beispielbewertung (Mockup)</p></div>'
reviews = rich("Das sagen Kunden über MS-5",
    '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;text-align:left">' +
    rev(5, "Zwei Solarmodule mit Spoilern aufs Alu-Dach geklebt, nach 2.000 km sitzt alles bombenfest.") +
    rev(5, "Hält sofort, ich musste nichts abstützen. Anleitung war klar.") + rev(4, "Super Haftung, bei Kälte etwas zäh aus der Kartusche.") +
    '</div><p style="font-size:12px;color:#888">Hinweis: Beispielbewertungen für die Challenge-Vorschau – im Live-Shop kommen hier echte Bewertungen aus einer Review-App (z. B. Judge.me).</p>',
    "BEWERTUNGEN", "large", "center")

# Cross-Sell: feste Zubehör-Kollektion statt automatischer "Ähnliche Produkte" (die zeigen sonst andere Dichtstoffe statt Zubehör)
recs = sec("featured-collection", {"heading": "Das brauchst du dazu", "description": "<p>Ohne saubere Fläche hält kein Kleber – diese Produkte machen deine Klebung sicher.</p>",
    "collection": "reinigen-zubehoer", "display_type": "grid", "product_limit": 4, "columns_desktop": 4, "show_view_all": True, "marker_color": RED})
# Bewusst kein "Zuletzt angesehen": Fokus bleibt auf passendem Zubehör statt auf Alternativen

# Zubehör direkt nach der Anleitung, in der es vorkommt, statt erst am Seitenende
# Technik & Downloads als zugeklappte Akkordeons in der Beschreibungs-Spalte (Desktop: links unter der Galerie)
# statt als eigene Tab-Section am Seitenende – füllt die linke Spalte, Profis finden die Daten direkt neben der Kaufbox.
tech_details = "".join(f'<details><summary>{b["settings"]["tab_label"]}</summary><div class="rte">{b["settings"]["custom_liquid"] or b["settings"]["text"]}</div></details>'
                       for b in technik["blocks"])
for b in main["blocks"]:
    if b["settings"].get("custom_liquid") == MORE:
        b["settings"]["custom_liquid"] = MORE.replace("<!--MEHR-->", tech_details)
# Bewusst nicht (mehr) auf der MS-5-Seite, weil sie wiederholen, was oben schon steht:
#   vorteile (= 4 Bullets + Bild-Callouts), recs (= "Oft zusammen gekauft"), service (= Trust-Leiste)
# Set direkt nach den Schritten: wer gerade gesehen hat, was er braucht, bekommt sofort alles in einem Paket
sections = [sec("breadcrumbs"), main, anwendungen, haftgrund, schritte, setsec, story, vergleich, reviews, faq]
# Shopify erlaubt max. 25 Sections pro Vorlage -> keine Spacer-Sections, stattdessen die eingebauten Abstände der Sections nutzen
for s in sections[2:]:
    s["settings"]["disable_top_spacing"] = False; s["settings"]["disable_bottom_spacing"] = False
out = pathlib.Path(__file__).parent / "template_dekasyl.json"
json.dump(sections, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(sections), "Sections,", len(faqs), "FAQ,", out.stat().st_size, "Bytes")
