from abc_client.client import client


class REST(client.Client):
    def __init__(self):
        self.host = 'http://127.0.0.1:5000'

    def post(self, prefix, *args, **kwargs):
        request = self._post(self.get_url(prefix), *args, **kwargs)
        return request.json()

    def get_url(self, prefix):
        return "{}/{}".format(self.host, prefix)
