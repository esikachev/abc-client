import os

import testtools

from abc_client.client import rest
from abc_client.tests import utils


class TestScenario(testtools.TestCase):
    def init(self):
        self.rest_client = rest.REST()
        self.rest_client.init()

    def test_init(self):
        if os.path.exists(utils.from_home_dir(".abc")):
            self.skipTest(".abc is exist in home-dir")
        self.init()
        self.assertTrue(os.path.exists(utils.from_home_dir(".abc")))
