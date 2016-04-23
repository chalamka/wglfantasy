from .api import API


class Matches(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def schedule(self, matchid=None):
        endpoint = 'schedule'
        params = {'matchid': matchid}

        return self.request(endpoint, params)

    def information(self, matchid=None):
        endpoint = 'match'
        params = {'matchid': matchid}

        return self.request(endpoint, params)
