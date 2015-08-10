#!/bin/env python
import yaml
import json

my_list = range (2)
my_list.append('yaml-json test')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['hostname'] = 'myrouter'
my_list[-1]['netmask'] = '255.255.255.0'
my_list[-1]['gateway'] = '10.10.10.1'

with open("devicelist.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
f.close()
with open("devicelist.json", "w") as f:
    json.dump(my_list, f)
f.close()

