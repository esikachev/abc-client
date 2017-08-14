from abc_client import settings
from abc_client import utils


def add(user_file):
    user_file = utils.check_path(user_file)
    with utils.YamlEditor(settings.CONFIG_PATH) as yaml:
        if user_file not in yaml['watch']:
            yaml['watch'].append(user_file)
