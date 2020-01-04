from Item import Item
from Updatable import Updatable
class Normal_item(Item, Updatable):
    def set_sell_in(self):
        self.sell_in -= 1
    def update_quality(self):
        self.quality -= 1