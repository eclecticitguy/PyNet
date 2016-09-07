#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./ex1_binary_converter.py <ip address>")

# Create input variables for later use
ip_addr = sys.argv.pop()
octets = ip_addr.split('.')
ip_addr_bin = []

# Check for a complete IP Address with no missing digits.  If missing, exit
for octet in octets:
    if len(octet) == 0:
        sys.exit("IP Address formatted incorrectly")

# Perform main conversion
# Check that there are four octets to convert, otherwise error has occured
if len(octets) == 4:
    for octet in octets:
        bin_octet = bin(int(octet))

        # Strip 0b from each binary octet
        bin_octet = bin_octet[2:]

        # Pad octet so that the total length is 8 bits
        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet[:]

        # Add converted octet to list
        ip_addr_bin.append(bin_octet)

    # Convert binary list back into dotted-binary format
    ip_addr_bin = '.'.join(ip_addr_bin)

    # Print output to screen
    print "%-20s %-20s" % ('IP Address', 'Binary')
    print "%-20s %-20s" % (ip_addr, ip_addr_bin)

else:
    print "Invalid IP address entered"
