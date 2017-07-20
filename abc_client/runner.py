import argparse

from abc_client.client import rest


def get_parser():
    parser = argparse.ArgumentParser(description="Abc client")
    parser.add_argument('--init', default=False, action='store_true',
                        help="Init basic config")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    rest_client = rest.REST()

    if args.init:
        rest_client.init()
