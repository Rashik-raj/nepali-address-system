from .addresses import Address


class Province(Address):
    __excluded__ = ["_Address__addresses", "get_all_addresses"]

    def __init__(self):
        super().__init__()
        self._provinces_dict = self.get_all_addresses()
        self._provinces = list(self._provinces_dict.keys())

    def __dir__(self):
        dir = super().__dir__()
        for name in self.__excluded__:
            if name in dir:
                dir.remove(name)
        return dir

    def get_all_provinces(self):
        '''
            Returns all provinces name in Nepal.
        '''
        return self._provinces

    def check_province_exist(self, province_name):
        '''
            check if province exist.
        '''
        return province_name in self._provinces

    def _get_province_detail(self, province_name):
        '''
            Returns the province detail in the province.
        '''
        return self._provinces_dict.get(province_name)

    def get_districts(self, province_name):
        '''
            Returns all districts in the province.
        '''
        province_detail = self._get_province_detail(province_name)
        if province_detail is not None:
            return list(province_detail.keys())
        else:
            return []

    def get_municipalities(self, province_name):
        '''
            Returns all municipalities in the province.
        '''
        province_detail = self._get_province_detail(province_name)
        if province_detail is None:
            return []
        municipalities = []
        for each_municipality_list in province_detail.values():
            for each_municipality in each_municipality_list:
                municipalities.append(each_municipality)
        return municipalities
