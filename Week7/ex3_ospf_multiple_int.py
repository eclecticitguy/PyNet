#!/usr/bin/env python

'''
The file 'OSPF_DATA/ospf_data.txt' contains the output from 'show ip ospf
interface'.  Using some functions and some regular expressions, parse this
output to display the following (note, I ended up using re.split() as part of
the solution to this problem):
Int:    Loopback0
IP:     10.90.3.38/32
Area:   30395
Type:   LOOPBACK
Cost:   1

Int:    GigabitEthernet0/1
IP:     172.16.13.150/29
Area:   30395
Type:   BROADCAST
Cost:   1
Hello:  10
Dead:   40

Int:    GigabitEthernet0/0.2561
IP:     10.22.0.117/30
Area:   30395
Type:   POINT_TO_POINT
Cost:   1
Hello:  10
Dead:   40
'''

import re

def separate_interface_data(ospf_data):

    ospf_data = re.split(r'(.+ is up, line protocol is up)', ospf_data)

    ospf_data.pop(0)

    ospf_list = []

    while True:
        if len(ospf_data) >= 2:
            intf = ospf_data.pop(0)
            section = ospf_data.pop(0)

            # reunify because it was split up in the re.split
            ospf_string = intf + section
            ospf_list.append(ospf_string)

        else:
            break

    return ospf_list


def generic_ospf_parser(pattern, ospf_data):
    '''
    Takes a generic regular expression pattern that has a group(1) match
    pattern and returns this
    Else returns None
    '''

    a_match = re.search(pattern, ospf_data)
    if a_match:
        return a_match.group(1)
    else:
        return None


def print_ospf_output(a_dict):

    # Ordering output using dictionary key as the order attribute
    field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')

    print
    for key in field_order:
        if a_dict.get(key) is not None:
            print "%10s: %-20s" % (key, a_dict[key])


if __name__ == '__main__':

    f = open('./OSPF_DATA/ospf_data.txt', 'r')

    ospf_output = f.read()
    ospf_data_sections = separate_interface_data(ospf_output)
    f.close()

    ospf_int_patterns = {

        'Int': r'(.+?) is up',
        'IP': r'Internet Address (.+?),',
        'Area': r'Area (.+),',
        'Type': r'Network Type (.+),',
        'Cost': r'Cost: (.+)',
        'Hello': r'Hello (.+?),',
        'Dead': r'Dead (.+?),'
    }

    for int_sections in ospf_data_sections:

        tmp_dict = {}

        for k, ospf_pattern in ospf_int_patterns.items():
            return_val = generic_ospf_parser(ospf_pattern, int_sections)
            if return_val is not None:
                tmp_dict[k] = return_val

        print_ospf_output(tmp_dict)
