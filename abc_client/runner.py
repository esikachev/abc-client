import argparse

from abc_client import utils
from abc_client.service import add
from abc_client.client import rest


def get_parser():
    parser = argparse.ArgumentParser(description="Abc client")
    parser.add_argument('--init', default=False, action='store_true',
                        help="Init basic config")
    parser.add_argument('--add', default=None, nargs='?',
                        help='Specify the files for adding')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    init_cmd = args.init
    add_cmd = args.add
    add_cmd = utils.check_path(add_cmd)

    rest_client = rest.REST()

    if init_cmd:
        rest_client.init()
    elif add_cmd:
        add.add(add_cmd)
