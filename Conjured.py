from Normal_item import Normal_item
class Conjured(Normal_item):
    NAME = "Conjured"

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        self.quality -= 2