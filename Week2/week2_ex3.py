__author__ = 'wblack'

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

## Split without any arguments splits in all whitespace ##
entry1_slice = entry1.split()
entry2_slice = entry2.split()
entry3_slice = entry3.split()
entry4_slice = entry4.split()

## Need to assign IP list element to separate variable to extract string from list element
entry1_ip = entry1_slice[1:2]
entry2_ip = entry2_slice[1:2]
entry3_ip = entry3_slice[1:2]
entry4_ip = entry4_slice[1:2]

print "%-20s %-20s" % ('ip_prefix', 'as_path')
print "%-20s %-20s" % (entry1_ip[0], entry1_slice[4:-1])
print "%-20s %-20s" % (entry2_ip[0], entry2_slice[4:-1])
print "%-20s %-20s" % (entry3_ip[0], entry3_slice[4:-1])
print "%-20s %-20s" % (entry4_ip[0], entry4_slice[4:-1])