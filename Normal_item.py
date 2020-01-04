from Item import Item
from Updatable import Updatable
class Normal_item(Item, Updatable):
    def comprobar_quality(self):
        if self.quality <= 0:
            self.quality = 0
        elif self.quality >= 50:
            self.quality = 50
        return self.quality

    def set_sell_in(self):
        self.sell_in -= 1
        return self.sell_in
    def update_quality(self):
        if self.sell_in >= 0:
            self.quality -= 1
        elif self.sell_in < 0:
            self.quality -= 2
        self.comprobar_quality()
        return self.quality