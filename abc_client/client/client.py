from requests import get
from requests import post


class Client(object):
    def __init__(self):
        self.host = 'http://127.0.0.1:5000'

    def _post(self, *args, **kwargs):
        return post(*args, **kwargs)

    def _get(self, *args):
        return get(*args)

    def post(self, prefix, *args, **kwargs):
        request = self._post(self.get_url(prefix), *args, **kwargs)
        return request.json()

    def get_url(self, prefix):
        return "{}/{}".format(self.host, prefix)
