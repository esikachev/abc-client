from requests import get
from requests import post


class Client(object):
    @staticmethod
    def _post(*args, **kwargs):
        return post(*args, **kwargs)

    @staticmethod
    def _get(*args):
        return get(*args)
