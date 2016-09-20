__author__ = 'wblack'

ip_addr = raw_input("Enter IP: ")
octets = ip_addr.split(".")
octets = octets[:3]
octets.append('0')

print "%-20s %-20s %-20s" % ('NETWORK_NUMBER', 'FIRST_OCTET_BINARY', 'FIRST OCTET_HEX')
print "%-20s %-20s %-20s" % ('.'.join(octets), bin(int(octets[0])), hex(int(octets[0])))

