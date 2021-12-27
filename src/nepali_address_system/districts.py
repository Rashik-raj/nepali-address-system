from .provinces import Province


class District(Province):
    __excluded__ = ["_Address__addresses", "get_all_addresses", "_District__temp_districts_dict",
                    "get_all_provinces", "check_province_exist", "_get_province_detail",
                    "get_districts", "get_municipalities", ]

    def __init__(self):
        super().__init__()
        self.__temp_districts_dict = self._provinces_dict.values()
        self._districts_dict = {}
        for each_district_dict in self.__temp_districts_dict:
            self._districts_dict.update(each_district_dict)
        self._districts = list(self._districts_dict.keys())

    def __dir__(self):
        dir = super().__dir__()
        for name in self.__excluded__:
            if name in dir:
                dir.remove(name)
        return dir

    def get_all_districts(self):
        '''
            Returns all district name in Nepal.
        '''
        return self._districts

    def check_district_exist(self, district_name):
        '''
            check if district exist.
        '''
        return district_name in self._districts

    def _get_district_detail(self, district_name):
        '''
            Returns the district detail in the district.
        '''
        return self._districts_dict.get(district_name)

    def get_municipalities(self, district_name):
        '''
            Returns all municipalities in the district.
        '''
        district_detail = self._get_district_detail(district_name)
        if district_detail is not None:
            return district_detail
        else:
            return []

    def get_province(self, district_name):
        '''
            Returns province of the district.
        '''
        for each_province in self.get_all_provinces():
            if district_name in self._provinces_dict[each_province]:
                return each_province
        return None

    def check_province_exist(self, province_name):
        raise NotImplementedError

    def get_districts(self, province_name):
        raise NotImplementedError
