from .data import addresses

class Address:

    def __init__(self):
        self.__addresses = addresses
    
    def get_all_addresses(self):
        '''
        Returns all the addresses in Nepal.
        '''
        return self.__addresses
