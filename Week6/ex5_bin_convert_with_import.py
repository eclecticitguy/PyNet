#!/usr/bin/env python

from ex3_valid_ip_func import valid_ip
from ex4_binary_conv_func import ip_to_bin

ip_addr = raw_input("Enter IP Address: ")

if valid_ip(ip_addr):
    print ip_to_bin(ip_addr)
else:
    print "Invalid IP Address!"
