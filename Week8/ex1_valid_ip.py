#! /usr/bin/env python

def valid_ip(ip_address):

    # This is needed if the user enters an IP address with an invalid syntax.
    octets = ip_address.split(".")

    if len(octets) != 4:
        return False

    # Convert octet list entries to Integers
    for i, octet in enumerate(octets):
        try:
            octets[i] = int(octet)
        except ValueError:
            # Couldn't convert octet to an integer
            return False

    # Map variable names to octets
    first_octet, second_octet, third_octet, fourth_octet = octets

    # Perform check on IP addresses
    # First rule: First octet between 1 and 223
    # Second rule: First octet not 127
    # Third rule: Cannot be in 169.254.X.X
    # Fourth rule: Second, third, and fourth octet between 0 - 255

    if (first_octet < 1) or (first_octet > 223):
        return False
    elif first_octet == 127:
        return False
    elif (first_octet == 169) and (second_octet == 254):
        return False

    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            return False

    # Passed all the checks.  Return True
    return True

if __name__ == "__main__":

    test_ip_addresses = {
        '192.168.1': False,
        '10.1.1.': False,
        '10.1.1.x': False,
        '0.77.22.19': False,
        '-1.88.99.17': False,
        '241.17.17.9': False,
        '127.0.0.1': False,
        '169.254.1.9': False,
        '192.256.7.7': False,
        '192.168.-1.7': False,
        '10.1.1.256': False,
        '1.1.1.1': True,
        '223.255.255.255': True,
        '223.0.0.0': True,
        '10.200.255.1': True,
        '192.168.17.1': True,
    }

    for ip_addr, expected_result in test_ip_addresses.items():

        dots_to_print = (20 - len(ip_addr)) * '.'

        if valid_ip(ip_addr) is expected_result:
            if expected_result:
                print "Testing %s %s %s" % (ip_addr, dots_to_print, "valid")
            else:
                print "Testing %s %s %s" % (ip_addr, dots_to_print, "invalid")
        else:
            print "Testing %s %s %s" % (ip_addr, dots_to_print, "testing failed")
