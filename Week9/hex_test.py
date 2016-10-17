ip_addr = raw_input("IP Address: ")

octets = ip_addr.split('.')
ip_addr_hex = []

# Perform main conversion
# Check that there are four octets to convert, otherwise error has occured
if len(octets) == 4:
    for octet in octets:
        hex_octet = hex(int(octet))

        # Strip 0x from each binary octet
        hex_octet = hex_octet[2:]

        # Pad octet so that the total length is 2 bits
        while True:
            if len(hex_octet) >= 2:
                break
            hex_octet = '0' + hex_octet[:]

        # Add converted octet to list
        ip_addr_hex.append(hex_octet)

    # Convert binary list back into dotted-binary format
    ip_addr_hex = '.'.join(ip_addr_hex)

    # Print final result
    print ip_addr_hex