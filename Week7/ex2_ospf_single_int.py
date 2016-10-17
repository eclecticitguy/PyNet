#!/usr/bin/env python

'''

Open the ./OSPF_DATA/ospf_single_interface.txt and extract the interface, IP
address, area, type, cost, hello timer, and dead timer.  Use regular expressions
to accomplish your extraction.
Your output should look similar to the following:
Int:    GigabitEthernet0/1
IP:     172.16.13.150/29
Area:   303953
Type:   BROADCAST
Cost:   1
Hello:  10
Dead:   40

'''

import re

ospf_dict = {}

with open('ospf_single_interface.txt', 'r') as f:

    ospf_data = f.read()

    intf = re.search(r'(.+?) is up', ospf_data)
    if intf:
        ospf_dict['Int'] = intf.group(1)

    ip_addr = re.search(r'Internet Address (.+?),', ospf_data)
    if ip_addr:
        ospf_dict['IP'] = ip_addr.group(1)

    area = re.search(r'Area (.+),', ospf_data)
    if area:
        ospf_dict['Area'] = area.group(1)

    net_type = re.search(r'Network Type (.+),', ospf_data)
    if net_type:
        ospf_dict['Type'] = net_type.group(1)

    cost = re.search(r'Cost: (.+)', ospf_data)
    if cost:
        ospf_dict['Cost'] = cost.group(1)

    hello = re.search(r'Hello (.+?),', ospf_data)
    if hello:
        ospf_dict['Hello'] = hello.group(1)

    dead = re.search(r'Dead (.+?),', ospf_data)
    if dead:
        ospf_dict['Dead'] = dead.group(1)

    # Ordering output using dictionary key as the order attribute
    field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
    for k in field_order:
        print "%10s: %-20s" % (k, ospf_dict[k])
