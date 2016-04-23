from api import API


class Players(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def directory(self, search=None, wotid=None, personalid=None):
        endpoint = 'dir_players'
        params = {'search': search,
                  'wotid': wotid,
                  'personalid': personalid}

        return self.request(endpoint, params)

    def statistics(self, player=None):
        endpoint = 'stat_player'
        params = {'player': player}

        return self.request(endpoint, params)

    def fantasy_league(self, player=None):
        endpoint = 'fantasy_player'
        params = {'player': player}

        return self.request(endpoint, params)