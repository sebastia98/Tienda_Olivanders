from Item import Item
class Normal_item(Item):
    def set_sell_in(self):
        self.sell_in -= 1
    def update_quality(self):
        self.quality -= 1