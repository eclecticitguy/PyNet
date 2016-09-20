

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
