__author__ = 'wblack'

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

ios_version = cisco_ios.split(",")[2]
ios_version = ios_version.split("Version ")[1]

print "The Cisco IOS version is %s" % ios_version