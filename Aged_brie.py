from Normal_item import Normal_item 
class Aged_brie(Normal_item):

    NAME = "Aged Brie"

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        self.quality += 1
