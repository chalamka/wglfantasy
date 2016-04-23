from api import API


class Information(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def languages(self):
        endpoint = 'languages'

        return self.request(endpoint, params=None)