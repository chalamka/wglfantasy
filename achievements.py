from api import API


class Achievements(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def list(self, lang="en-us"):
        endpoint = 'achievements'
        params = {'lang': lang}

        return self.request(endpoint, params)