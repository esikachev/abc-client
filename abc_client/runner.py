import argparse

from abc_client.client import rest
from abc_client.service import add
from abc_client.service import rm


def get_parser():
    parser = argparse.ArgumentParser(description="Abc client")
    parser.add_argument('--init', default=False, action='store_true',
                        help="Init basic config")
    parser.add_argument('--add', default=None, nargs='?',
                        help='Specify the files for adding')
    parser.add_argument('--rm', default=None, nargs='?',
                        help='Stop watching for files')
    parser.add_argument('--sync', default=False, action='store_true',
                        help='Upload local files to remote')
    parser.add_argument('--apply', default=False, action='store_true',
                        help='Apply files to your host')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    init_cmd = args.init
    add_cmd = args.add
    rm_cmd = args.rm
    sync_cmd = args.sync
    apply_cmd = args.apply

    rest_client = rest.REST()

    if init_cmd:
        rest_client.init()
    elif add_cmd:
        add.add(add_cmd)
    elif rm_cmd:
        rm.rm(rm_cmd)
    elif sync_cmd:
        rest_client.sync()
    elif apply_cmd:
        rest_client.apply()
