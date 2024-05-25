from simulation_code.create_a_country import get_data, get_country
from math import floor


class ComplianceTest:
    name = "Проверка контроля (Франция)"

    def __init__(self):
        data = get_data()
        self.country = get_country(data=data, name_or_tag="FRA", by_tag=True)
        self.data = {
            364: 77.6,
            365: 77.7,
        }
        self.result = {}

    def check(self, text=False):
        successful = True
        for day in range(367):
            self.country.calculate_day(day=day)
            target_region = None
            for region in self.country.non_core_regions:
                if region.global_id == 781:
                    target_region = region
            compliance = floor(target_region.compliance*10)/10
            if day in self.data.keys():
                self.result[day] = compliance
                if self.data[day] != compliance:
                    successful = False
        if (
            successful
        ):
            return True
        else:
            if text:
                print(
                    f"Целевые показатели {self.data}\n"
                    f"Получили - {self.result}"
                )
            return False
