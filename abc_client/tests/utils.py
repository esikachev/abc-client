import os


def from_home_dir(string):
    return "{}/{}".format(os.environ['HOME'], string)
