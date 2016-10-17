#!/usr/bin/env python

'''

Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote
hostnames, remote IP addresses, and remote platforms.  Your output should look
similar to the following:
 remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
          IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
     platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']

'''

import re

with open('sw1_cdp.txt', 'r') as f:

    cdp_data = f.read()

    remote_hosts = re.findall(r'Device ID: (.+)', cdp_data)
    ip_addr = re.findall(r'IP address: (.+)', cdp_data)
    platform = re.findall(r'Platform: (.+),', cdp_data)

    print "%15s %s" % ("remote_hosts: ", remote_hosts)
    print "%15s %s" % ("IPs: ", ip_addr)
    print "%15s %s" % ("platform: ", platform)