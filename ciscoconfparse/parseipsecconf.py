#!/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

map_list = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for cryptoMap in map_list:
    print cryptoMap.text
    mapChildren = cryptoMap.children
    for child in mapChildren:
        print child.text

print '\nCrypto maps using PFS group 2:\n'
pfs2_list = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")
for cryptoMap in pfs2_list:
    print cryptoMap.text

print '\nCrypto maps not using AES:\n'
noaes_list = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")
for cryptoMap in noaes_list:
    print cryptoMap.text
    mapChildren = cryptoMap.children
    transformSetLine = mapChildren[1]
    (head,transformSet) = transformSetLine.text.split('set transform-set') 
    print transformSet





