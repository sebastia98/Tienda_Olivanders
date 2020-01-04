from Gilded_rose import Gilded_rose
from Item import Item
from Normal_item import Normal_item
from Aged_brie import Aged_brie
from Sulfuras import Sulfuras
from Backstage_pass import Backstage_pass
from Conjured import Conjured
from Gilded_rose import Gilded_rose


def test_agedbrie():
    queso = Aged_brie(10, 10)
    sellin = 10
    quality = 10

    for _ in range(sellin + 2):
        sellin -= 1
        quality += 1
        queso.update_quality()
        queso.set_sell_in()

        if quality < 0:
            quality = 0
        elif quality > 50:
            quality = 50

        assert queso.sell_in == sellin
        assert queso.quality == quality


def test_sulfuras():
    sulfura = Sulfuras(10, 10)
    sellin = 10
    quality = 10

    for i in range(sellin + 2):
        sulfura.set_sell_in()
        sulfura.update_quality()

        assert sulfura.sell_in == sellin
        assert sulfura.quality == quality


def test_backstage_pass():
    backstage = Backstage_pass(10, 10)
    sellin = 10
    quality = 10

    for _ in range(sellin + 2):
        sellin -= 1
        if sellin > 10:
            quality += 1
        elif sellin <= 10 and sellin > 5:
            quality += 2
        elif sellin <= 5 and sellin >= 0:
            quality += 3
        elif sellin < 0:
            quality = 0

        if quality < 0:
            quality = 0
        elif quality > 50:
            quality = 50

        backstage.set_sell_in()
        backstage.update_quality()

        assert backstage.sell_in == sellin
        assert backstage.quality == quality


def test_conjured():
    conjured = Conjured(10, 10)
    sellin = 10
    quality = 10

    for _ in range(sellin + 2):
        sellin -= 1
        if sellin >= 0:
            quality -= 2
        else:
            quality -= 4
        if quality < 0:
            quality = 0

        if quality < 0:
            quality = 0
        elif quality > 50:
            quality = 50

        conjured.set_sell_in()
        conjured.update_quality()

        assert conjured.sell_in == sellin
        assert conjured.quality == quality


def test_Normal_item():
    normal = Normal_item("Objeto", 10, 10)
    sellin = 10
    quality = 10

    for _ in range(sellin + 2):
        sellin -= 1
        quality -= 1

        if quality < 0:
            quality = 0
        elif quality > 50:
            quality = 50

        normal.set_sell_in()
        normal.update_quality()

        assert normal.sell_in == sellin
        assert normal.quality == quality
