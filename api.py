from requests import get


class API():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'api.fantasywgl.com/request/'

    def _format_url(self, path):
        return self.base_url + self.api_key + path

    def request(self, endpoint, params):
        url = self._format_url(endpoint)

        return get(url, params=params).json()