from .api import API


class Teams(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def directory(self, search=None):
        endpoint = 'dir_teams'
        params = {'search': search}

        return self.request(endpoint, params)

    def information(self, team=None):
        endpoint = 'info_team'
        params = {'team': team}

        return self.request(endpoint, params)