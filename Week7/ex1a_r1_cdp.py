import re

with open('r1_cdp.txt', 'r') as f:

    cdp_data = f.read()

    hostname = re.search(r'Device ID: (.+)', cdp_data).group(1)
    ip_addr = re.search(r'  IP address: (.+)', cdp_data).group(1)
    capability = re.search(r'Platform: (.+?) (.+?),  Capabilities: (.+?) ', cdp_data)
    vendor = capability.group(1)
    model = capability.group(2)
    device_type = capability.group(3)

    print hostname
    print ip_addr
    print vendor
    print model
    print device_type