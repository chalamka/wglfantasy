from api import API


class Tanks(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def directory(self, search=None):
        endpoint = 'dir_vehicles'
        params = {'search': search}

        return self.request(endpoint, params)