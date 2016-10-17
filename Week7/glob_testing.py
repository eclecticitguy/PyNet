#!/usr/bin/env python

from glob import glob
import re

rancid_data = glob("./CDP_DATA/*.txt")

for input_file in rancid_data:

    with open(input_file) as file:

        hostname_list = []

        for line in file:

            hostname = re.search(r'(.+?)>.?show cdp neighbors', line)
            if hostname:
                hostname_list.append(hostname.group(1))

        print hostname_list