from requests import get
from requests import post


class Client(object):
    def __init__(self):
        self.host = 'http://127.0.0.1:5000'

    @staticmethod
    def _post(*args, **kwargs):
        return post(*args, **kwargs)

    @staticmethod
    def _get(*args):
        return get(*args)

    def post(self, prefix, *args, **kwargs):
        request = Client._post(self.get_url(prefix), *args, **kwargs)
        return request.json()

    def get_url(self, prefix):
        return "{}/{}".format(self.host, prefix)
