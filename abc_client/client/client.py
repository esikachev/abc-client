from requests import get
from requests import post


class Client(object):
    def _post(self, *args, **kwargs):
        return post(*args, **kwargs)

    def _get(self, *args):
        return get(*args)
