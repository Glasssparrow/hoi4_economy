

class Order:

    def __init__(self, region_name, building_type, quantity):
        self.target_region = region_name
        self.target_region_id = None
        self.building_type = building_type
        self.quantity = quantity

    def finish_one(self):
        empty = False
        self.quantity -= 1
        if self.quantity <= 0:
            self.quantity = 0
            empty = True
        return empty
