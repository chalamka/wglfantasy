from .api import API


class Standings(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def wgl(self):
        endpoint = 'wgl_standings'

        return self.request(endpoint, params=None)

    def fantasy_league(self, limit=50, offset=0, search=None):
        endpoint = 'fantasy_standings'
        params = {'limit': limit,
                  'offset': offset,
                  'search': search}

        return self.request(endpoint, params)