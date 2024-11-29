import datetime
class Pharmacy:
    def init(self, name, location, is_open24_hours, opening_time=None, closing_time=None):
        self.__name = name
        self.__location = location
        self.__is_open24_hours = is_open24_hours
        self.__opening_time = opening_time
        self.__closing_time = closing_time

    @staticmethod
    def pharmacy_info():
        return "Pharmacies provide medical supplies and medication."

    def is_open_now(self, current_time):
        if self.__is_open24_hours:
            return True
        if self.opening_time and self.closing_time:
            return self.opening_time <= current_time <= self.closing_time
        return False

    @property
    def name(self):
        return self.__name

class Province:
    def init(self, name):
        self.__name = name
        self.__pharmacies = []

    def add_pharmacy(self, pharmacy):
        self.__pharmacies.append(pharmacy)

    def find_open_pharmacies(self, current_time):
        return [pharmacy for pharmacy in self.__pharmacies if pharmacy.is_open_now(current_time)]

class PharmacyFinder:
    def init(self):
        self.__Provinces = {}

    @classmethod
    def finder_info(cls):
        return "Pharmacy Finder helps locate open pharmacies in various provinces."

    def add_Province(self, Province):
        self.__Provinces[Province.name] = Province

    def search_in_Province(self, Province_name, current_time):
        Province = self.__Provinces.get(Province_name)
        if Province:
            return Province.find_open_pharmacies(current_time)
        else:
            return []
        if name == "main":

pharmacy1 =Pharmacy("الامل","شارع بغداد")
pharmacy2 = Pharmacy("الحياة", "شارع الزهور", True)
pharmacy3 = Pharmacy("الصحة", "شارع الكرامة", False, datetime.time(8, 0), datetime.time(18, 0))
pharmacy4 = Pharmacy("الشفاء", "شارع الجامعة", False, datetime.time(10, 0), datetime.time(22, 0))



province_baghdad = Province("بغداد")
province_basra = Province("البصرة")
province_erbil = Province("أربيل")

province_baghdad.add_pharmacy(pharmacy1)
province_baghdad.add_pharmacy(pharmacy2)
province_basra.add_pharmacy(pharmacy3)
province_erbil.add_pharmacy(pharmacy4)


pharmacy_finder = PharmacyFinder()
pharmacy_finder.add_Province(province_baghdad)
pharmacy_finder.add_Province(province_basra)
pharmacy_finder.add_Province(province_erbil)



current_time = datetime.datetime.now().time()



open_pharmacies_in_baghdad = pharmacy_finder.search_in_Province("بغداد", current_time)
open_pharmacies_in_basra = pharmacy_finder.search_in_Province("البصرة", current_time)
open_pharmacies_in_erbil = pharmacy_finder.search_in_Province("أربيل", current_time)

print(f"Open pharmacies in Baghdad: {[pharmacy.name for pharmacy in open_pharmacies_in_baghdad]}")
print(f"Open pharmacies in Basra: {[pharmacy.name for pharmacy in open_pharmacies_in_basra]}")
print(f"Open pharmacies in Erbil: {[pharmacy.name for pharmacy in open_pharmacies_in_erbil]}")
