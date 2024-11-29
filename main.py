class Pharmacy:
    def __init__(self, name, location, is_open24_hours, opening_time=None, closing_time=None):
        self.__name = name
        self.__location = location
        self.__is_open24_hours = is_open24_hours
        self.__opening_time = opening_time
        self.__closing_time = closing_time

    @staticmethod
    def pharmacy_info():
        return "Pharmacies provide medical supplies and medication."

    def get_name(self):
        return self.__name

class Province:
    def __init__(self, name):
        self.__name = name
        self.__pharmacies = []

    def add_pharmacy(self, pharmacy):
        self.__pharmacies.append(pharmacy)

    def get_all_pharmacies(self):
        return self.__pharmacies

    def get_province(self, province_name):
        for province in self.provinces:
            if province.name == province_name:
                return province
        return None
class PharmacyFinder:
    def __init__(self):
        self.__provinces = {}

    @classmethod
    def finder_info(cls):
        return "Pharmacy Finder helps locate pharmacies in various provinces."

    def add_province(self, province):
        self.__provinces[province.get_name()] = province

    def search_in_province(self, province_name):
        province = self.__provinces.get(province_name)
        if province:
            return province.get_all_pharmacies()
        else:
            return []

if __name__ == "__main__":
    pharmacy1 = Pharmacy("الامل", "شارع بغداد", False)
    pharmacy2 = Pharmacy("الحياة", "شارع الزهور", True)
    pharmacy3 = Pharmacy("الصحة", "شارع الكرامة", False)
    pharmacy4 = Pharmacy("الشفاء", "شارع الجامعة", False)

    province_baghdad = Province("بغداد")
    province_basra = Province("البصرة")

    province_baghdad.add_pharmacy(pharmacy1)
    province_baghdad.add_pharmacy(pharmacy2)
    province_basra.add_pharmacy(pharmacy3)
    province_basra.add_pharmacy(pharmacy4)

    pharmacy_finder = PharmacyFinder()
    pharmacy_finder.add_province(province_baghdad)
    pharmacy_finder.add_province(province_basra)

    all_pharmacies_in_baghdad = pharmacy_finder.search_in_province("بغداد")
    all_pharmacies_in_basra = pharmacy_finder.search_in_province("البصرة")

    print(f"All pharmacies in Baghdad: {[pharmacy.get_name() for pharmacy in all_pharmacies_in_baghdad]}")
    print(f"All pharmacies in Basra: {[pharmacy.get_name() for pharmacy in all_pharmacies_in_basra]}")


