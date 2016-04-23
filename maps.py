from api import API


class Maps(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def directory(self, lang='en-us', search=None):
        endpoint = 'dir_maps'
        params = {'lang': lang,
                  'search': search}

        return self.request(endpoint, params)