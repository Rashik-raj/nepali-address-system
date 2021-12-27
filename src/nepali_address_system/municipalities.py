from .districts import District


class Municipality(District):
    __excluded__ = ["_Address__addresses", "get_all_addresses", "_District__temp_districts_dict",
                    "get_all_provinces", "check_province_exist", "_get_province_detail",
                    "get_districts", "get_municipalities", "_Municipality__temp_municipalities_list",
                    "_provinces", "_provinces_dict", "_districts", "_districts_dict",
                    "check_district_exist", "_get_district_detail"]

    def __init__(self):
        super().__init__()
        self.__temp_municipalities_list = self._districts_dict.values()
        self._municipalities = []
        for each_municipality_list in self.__temp_municipalities_list:
            for each_municipality in each_municipality_list:
                self._municipalities.append(each_municipality)

    def __dir__(self):
        dir = super().__dir__()
        for name in self.__excluded__:
            if name in dir:
                dir.remove(name)
        return dir

    def get_all_municipalities(self):
        '''
            Returns all municipalities of Nepal.
        '''
        return self._municipalities

    def check_municipality_exist(self, municipality_name):
        '''
            check if municipality exist.
        '''
        return municipality_name in self._municipalities

    def get_district(self, municipality_name):
        '''
            Returns district of the municipality.
        '''
        for each_district in self._districts_dict.keys():
            if municipality_name in self._districts_dict[each_district]:
                return each_district
        return None

    def get_province(self, municipality_name):
        '''
            Returns province of the municipality.
        '''
        district = self.get_district(municipality_name)
        if district is None:
            return None
        for each_province in self._provinces:
            if district in self._provinces_dict[each_province]:
                return each_province
        return None

    def check_district_exist(self, district_name):
        raise NotImplementedError

    def check_province_exist(self, province_name):
        raise NotImplementedError

    def get_all_provinces(self):
        raise NotImplementedError

    def get_all_districts(self):
        raise NotImplementedError

    def get_districts(self, province_name):
        raise NotImplementedError

    def get_municipalities(self, district_name):
        return NotImplementedError
