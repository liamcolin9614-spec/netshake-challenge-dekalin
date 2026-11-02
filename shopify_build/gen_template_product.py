"""Standard-Produktvorlage (templates/product.json) für alle übrigen Produkte: gleicher Aufbau und Stil wie die
MS-5-Seite, aber nur mit Bausteinen, die für jedes Produkt passen (statt der Demo-Sections des Themes)."""
import json, pathlib
from gen_template_dekasyl import sec, blk, liquid, rich, card, ico, CSS, icons, main, service, RED, MORE

usp = '{%- if product.metafields.custom.usp_zeile != blank -%}<p style="font-size:17px;line-height:1.45;margin:-4px 0 8px"><strong>{{ product.metafields.custom.usp_zeile }}</strong></p>{%- endif -%}'
liefer = '<p style="margin:0;font-weight:600;color:#2E8B57">● {{ product.metafields.custom.lieferhinweis | default: "Auf Lager – in 1–3 Werktagen bei dir" }}</p>'
grundpreis = ('{%- assign v = product.selected_or_first_available_variant -%}{%- if v.unit_price_measurement -%}'
              '<p style="font-size:13px;color:#555;margin:-6px 0 10px">{{ v.unit_price | money }} / {{ v.unit_price_measurement.reference_value }} {{ v.unit_price_measurement.reference_unit }} · inkl. MwSt., zzgl. Versand</p>{%- endif -%}')
blocks = [
    liquid(CSS),
    # kein Vendor-Text: im eigenen Markenshop ist jedes Produkt von Dekalin
    blk("title", show_products_rating=True, show_products_rating_average=True, show_custom_badges=True),
    liquid(usp),
    blk("variant_picker", picker_type="button", color_picker=True, variant_is_disabled=True, sizing_guide_variant="", sizing_guide_text=""),
    liquid(grundpreis),
    liquid(liefer),
    blk("buy_buttons", show_dynamic_checkout=False, show_gift_card_recipient=False),
    liquid(icons),
    liquid(MORE),
]
main_std = sec("main-product", main["settings"], blocks)
recs = sec("featured-collection", {"heading": "Das brauchst du dazu", "description": "<p>Ohne saubere Fläche hält kein Kleber – diese Produkte machen deine Klebung sicher.</p>",
    "collection": "reinigen-zubehoer", "display_type": "grid", "product_limit": 4, "columns_desktop": 4, "show_view_all": True, "marker_color": RED,
    "disable_top_spacing": False, "disable_bottom_spacing": False})
sections = [sec("breadcrumbs"), main_std, recs]   # keine Service-Karten: wiederholen die Trust-Leiste
out = pathlib.Path(__file__).parent / "template_product.json"
json.dump(sections, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(sections), "Sections,", out.stat().st_size, "Bytes")
