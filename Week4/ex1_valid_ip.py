#!/usr/bin/env python
'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

Prompt a user to input an IP address.  Re-using some of the code from class3,
exercise4--determine if the IP address is valid.  Continue prompting the user
to re-input an IP address until a valid IP address is input.

'''

import sys

# Set valid_ip to false to enter the while loop
valid_ip = False

while valid_ip is False:
    # Now that we're in the loop, we're going to assume the correct IP address is entered until proven wrong
    valid_ip = True

    ip_addr = raw_input("Enter IP Address: ")
    octets = ip_addr.split(".")

    # This is needed if the user enters an IP address with an invalid syntax.
    while len(octets) != 4:
        ip_addr = raw_input("Invalid syntax for IP Address. IP address must use the syntax X.X.X.X. Re-enter IP: ")
        octets = ip_addr.split('.')

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

    if valid_ip is not False:
        print "The IP address %s is valid. Exiting" % ip_addr
        break
    else:
        print "The IP address %s is invalid.  Re-enter IP address. " % ip_addr
