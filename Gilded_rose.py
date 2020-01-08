from Aged_brie import Aged_brie
from Normal_item import Normal_item


class Gilded_rose():

    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items
    
    def set_items(self, item):
        self.items.append(item)
        return None

    def update_quality(self):
        for item in self.items:
            item.set_sell_in()
            item.update_quality()
