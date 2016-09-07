#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./ex1_binary_converter.py <ip address>")

# Store input argument as ip_addr
ip_addr = sys.argv.pop()

# Split IP address into octets and convert to Integer
octets = ip_addr.split('.')

# Set valid_ip bit to True and adjust to False if needed
valid_ip = True

if len(octets) != 4:
    sys.exit("Invalid syntax for IP Address. IP address must use the syntax X.X.X.X")

# Convert octet list entries to Integers
for i, octet in enumerate(octets):
    try:
        octets[i] = int(octet)
    except ValueError:
        # Couldn't convert octet to an integer
        sys.exit("\nInvalid address: %s" % ip_addr)

# Map variable names to octets
first_octet, second_octet, third_octet, fourth_octet = octets

# Perform check on IP addresses
# First rule: First octet between 1 and 223
# Second rule: First octet not 127
# Third rule: Cannot be in 169.254.X.X
# Fourth rule: Second, third, and fourth octet between 0 - 255

if (first_octet < 1) or (first_octet > 223):
    valid_ip = False
elif first_octet == 127:
    valid_ip = False
elif (first_octet == 169) and (second_octet == 254):
    valid_ip = False

for octet in (second_octet, third_octet, fourth_octet):
    if (octet < 0) or (octet > 255):
        valid_ip = False

if valid_ip is True:
    print "The IP address %s is valid" % ip_addr
else:
    sys.exit("The IP Address %s is not valid" % ip_addr)
