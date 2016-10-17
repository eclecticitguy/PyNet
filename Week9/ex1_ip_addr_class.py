class IPAddress(object):
    '''
    A class representing an IP Address
    '''

    def __init__(self, ip):


        self.ip_addr = ip


    def display_in_binary(self):

        '''
        Display the IP address in dotted binary format padded to eight digits:

        11000000.10101000.00000001.00000001

        '''

        octets = self.ip_addr.split('.')
        ip_addr_bin = []

        # Perform main conversion
        # Check that there are four octets to convert, otherwise error has occured
        if len(octets) == 4:
            for octet in octets:
                bin_octet = bin(int(octet))

                # Strip 0b from each binary octet
                bin_octet = bin_octet[2:]

                # Pad octet so that the total length is 8 bits
                bin_octet = bin_octet.rjust(8, '0')
                ip_addr_bin.append(bin_octet)

        return '.'.join(ip_addr_bin)


    def display_in_hex(self):

        '''
        Display the IP address in dotted hex form padded to two digits:

        c0.a8.01.01

        '''

        octets = self.ip_addr.split('.')
        ip_addr_hex = []

        # Perform main conversion
        # Check that there are four octets to convert, otherwise error has occured
        if len(octets) == 4:
            for octet in octets:
                hex_octet = hex(int(octet))

                # Strip 0x from each binary octet
                hex_octet = hex_octet[2:]

                # Pad octet so that the total length is 2 bits
                hex_octet = hex_octet.rjust(8, '0')
                ip_addr_hex.append(hex_octet)

            return '.'.join(ip_addr_hex)


    def is_valid(self):

        '''
        Check if the IP address is valid

        :return: either True or False
        '''

        # This is needed if the user enters an IP address with an invalid syntax.
        octets = self.ip_addr.split(".")

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


def main():

    ip1 = IPAddress('127.0.0.1')
    print ip1.ip_addr
    ip1.display_in_binary()
    ip1.display_in_hex()
    print ip1.is_valid()


if __name__ == "__main__":
    main()
