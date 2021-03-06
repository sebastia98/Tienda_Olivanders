from Normal_item import Normal_item


class Backstage_pass(Normal_item):

    NAME = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        elif self.sell_in <= 5 and self.sell_in >= 0:
            self.quality += 3
        elif self.sell_in < 0:
            self.quality = 0

        self.comprobar_quality()

        return self.quality
