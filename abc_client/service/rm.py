import os

from abc_client import settings
from abc_client import utils


def rm(user_file):
    os.remove(user_file)
    user_file = utils.check_path(user_file)
    with utils.YamlEditor(settings.CONFIG_PATH) as yaml:
        yaml['watch'].remove(user_file)
