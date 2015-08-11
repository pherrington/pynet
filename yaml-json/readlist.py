#!/bin/env python

import yaml
import json
from pprint import pprint as pp

def main():

    with open("devicelist.yml", "r") as f:
        my_yaml_list = yaml.load(f)
    f.close()

    with open("devicelist.json", "r") as f:
        my_json_list = json.load(f)
    f.close()

    print 'YAML list\n'
    pp(my_yaml_list)
    print '\n'

    print 'JSON list\n'
    pp(my_json_list)
    print '\n'

if __name__ == "__main__":
    main()





