from Gilded_rose import Gilded_rose
from Item import Item
from Normal_item import Normal_item
from Aged_brie import Aged_brie
from Sulfuras import Sulfuras
from Backstage_pass import Backstage_pass
from Conjured import Conjured

def generar_html_items(items):
    html = ""
    for item in gilded_rose.get_items():
        html += "<h1>" + str(item) + "</h1>"
    return html

def anadir_item(item, sellin, quality):
    if item == "Aged Brie":
        gilded_rose.set_items(Aged_brie(int(sellin), int(quality)))
    elif item == "Sulfuras":
        gilded_rose.set_items(Sulfuras(int(sellin), int(quality)))
    elif item == "Backstage Pass":
        gilded_rose.set_items(Backstage_pass(int(sellin), int(quality)))
    elif item == "Conjured":
        gilded_rose.set_items(Conjured(int(sellin), int(quality)))
    else:
        gilded_rose.set_items(Normal_item(item, int(sellin), int(quality)))
    return None

gilded_rose = Gilded_rose([])