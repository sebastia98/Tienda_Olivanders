from Normal_item import Normal_item
class Sulfuras(Normal_item):
    NAME = "Sulfuras, Hand of Ragnaros"

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)
    
    def update_quality(self):
        pass
    def set_sell_in(self):
        pass