import yaml

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


if __name__ == '__main__':

    stream = open("roles.yaml", 'r')
    roleList = yaml.safe_load(stream)
    for key, value in roleList.items():
        print (key + " : " + str(value))