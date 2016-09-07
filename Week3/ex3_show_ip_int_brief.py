import pprint

show_ip_int_brief = '''
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
'''

# Break lines into long string using newline as delimiter
show_ip_lines = show_ip_int_brief.split('\n')

# Need list to store appended items into
show_ip_list = []

# Iterate over items in 'show ip int brief'
for line in show_ip_lines:

    # Skip first line header
    if 'Interface' in line:
        continue

    # Break lines into clean words
    line_split = line.split()

    # Discard any lines that aren't the correct format
    if len(line_split) == 6:

        # Set variable names for each item in line for easier reference based on line index
        int_name, ip_addr, discard, discard, int_status, int_protocol = line_split

        # Check if interface status and protocol are 'up'. If they are, append data to show_ip_list list created earlier
        # Append data to list using tuple to prevent accidental overwriting or reassignment
        if (int_status == 'up') and (int_protocol == 'up'):
            show_ip_list.append((int_name, ip_addr, int_status, int_protocol))


# Print output to screen#
pprint.pprint(show_ip_list)
