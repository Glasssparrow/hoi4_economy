

class Order:

    def __init__(self, region_name, building_type, quantity):
        self.target_region = region_name
        self.target_region_id = 0
        self.building_type = building_type
        self.quantity = quantity
