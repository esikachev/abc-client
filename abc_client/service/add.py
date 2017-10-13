from abc_client import settings
from abc_client import utils


def add(user_file):
    with utils.YamlEditor(settings.CONFIG_PATH) as yaml:
        try:
            user_file not in yaml['watch']
        except TypeError:
            if yaml is None:
                yaml = {}
            yaml.update({'watch': user_file})
        else:
            yaml['watch'].append(user_file)
