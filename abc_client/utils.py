import os

import yaml


HOME = os.environ.get('HOME')


def from_home_dir(path=None):
    if not path:
        return HOME
    return "{0}/{1}".format(HOME, path)


def write_to_file(file_name, data):
    with open(file_name, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False)


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        return yaml.load(f)


class YamlEditor(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def __enter__(self):
        self.content = read_from_file(self.yaml_file)
        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb):
        write_to_file(self.yaml_file, self.content)


def check_path(path):
    if not path:
        return

    path = os.path.abspath(path)

    if HOME in path:
        path = path.replace(HOME, '')
        return "~{}".format(path)

    return path
