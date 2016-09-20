#!/usr/bin/env python


def ip_to_bin(ip_address):

    # Create input variables for later use
    octets = ip_address.split('.')
    ip_addr_bin = []

    # Perform main conversion
    for octet in octets:
        bin_octet = bin(int(octet))

        # Strip 0b from each binary octet
        bin_octet = bin_octet[2:]

        # Pad to 8 digits
        bin_octet = pad_binary_ip(bin_octet)

        # Append to ip_addr_bin list
        ip_addr_bin.append(bin_octet)

    # Convert binary list back into dotted-binary format and
    return '.'.join(ip_addr_bin)


# Function to pad an binary IP address to 8 digits
def pad_binary_ip(ip_address):

    while True:
        if len(ip_address) >= 8:
            break
        ip_address = '0' + ip_address

    return ip_address