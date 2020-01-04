from Normal_item import Normal_item
class Backstage_pass(Normal_item):
    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in =< 10 and self.sell_in > 5:
            self.quality += 2
        elif self.sell_in =< 5 and self.sell_in > 0:
            self.quality += 3
            