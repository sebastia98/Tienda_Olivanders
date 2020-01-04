from Normal_item import Normal_item


class Conjured(Normal_item):

    NAME = "Conjured"

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.quality -= 2
        else:
            self.quality -= 4

        self.comprobar_quality()

        return self.quality
