__author__ = 'wblack'

ip_addr = raw_input("Enter IP: ")

octets = ip_addr.split('.')

print "%-20s %-20s %-20s %-20s" % ('first_octet', 'second_octet', 'third_octet', 'fourth_octet')
print "%-20s %-20s %-20s %-20s" % (bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3])))