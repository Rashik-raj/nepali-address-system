from .districts import District

class Municipality(District):

    def __init__(self):
        super().__init__()
        self.__temp_municipalities_list = self._districts_dict.values()
        self._municipalities = []
        for each_municipality_list in self.__temp_municipalities_list:
            for each_municipality in each_municipality_list:
                self._municipalities.append(each_municipality)

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
        for each_province in self.get_all_provinces():
            if district in self._provinces_dict[each_province]:
                return each_province
        return None