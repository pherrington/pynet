#!/usr/bin/env python

import snmp_helper
from datetime import datetime
import time

snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

IP = '50.76.53.27'

a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

snmp_user = (a_user, auth_key, encrypt_key)

pynet_rtr1 = (IP, 7961)
pynet_rtr2 = (IP, 8061)

for desc,an_oid,is_count in snmp_oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=an_oid)
    output = snmp_helper.snmp_extract(snmp_data)
    print "{0} {1}".format(desc,output)



