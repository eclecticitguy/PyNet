#!/usr/bin/env python
'''

Create a program that converts the following uptime strings to a time in
seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name
as the key.

During this conversion process, you will have to convert strings to integers.
For these string to integer conversions use try/except to catch any string to
integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.

'''

import pprint

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

# Set constants for calculating seconds on each period of time
SECOND = 1
MINUTES = SECOND * 60
HOURS = MINUTES * 60
DAYS = HOURS * 24
WEEKS = DAYS * 7
YEARS = WEEKS * 52

# Initialize uptime dictionary
uptime_dict = {}

# Put each uptime string into list
uptime_list = [uptime1, uptime2, uptime3, uptime4]

# Loop through list of uptime strings
for item in uptime_list:

    # For each list item, split on the string ' uptime is ' to separate the hostname from uptime
    uptime_item = item.split(' uptime is ')

    # Set the first split item to the hostname
    uptime_host = uptime_item[0]

    # Set the second split item to the uptime
    uptime_time = uptime_item[1].split(',')

    # Initialize variables that will be used to store uptime data
    item_minutes = 0
    item_hours = 0
    item_days = 0
    item_weeks = 0
    item_years = 0

    # Loop through uptime list and parse through strings to determine years, weeks, days, hours, and minutes
    for listitem in uptime_time:
        if 'years' in listitem:
            try:
                item_years = int(listitem.split()[0]) * YEARS
            except ValueError:
                print "Unable to convert year to integer for host %s" % uptime_host
        elif 'weeks' in listitem:
            try:
                item_weeks = int(listitem.split()[0]) * WEEKS
            except ValueError:
                print "Unable to convert weeks to integer for host %s" % uptime_host
        elif 'days' in listitem:
            try:
                item_days = int(listitem.split()[0]) * DAYS
            except ValueError:
                print "Unable to convert days to integer for host %s" % uptime_host
        elif 'hours' in listitem:
            try:
                item_hours = int(listitem.split()[0]) * HOURS
            except ValueError:
                print "Unable to convert hours to integer for host %s" % uptime_host
        elif 'minutes' in listitem:
            try:
                item_minutes = int(listitem.split()[0]) * MINUTES
            except ValueError:
                print "Unable to convert minutes to integer for host %s" % uptime_host

    # Calculate total time and store into variable
    item_total_time = item_years + item_weeks + item_days + item_hours + item_minutes

    # Add the key 'hostname' with the value of the total time into the uptime dictionary
    uptime_dict[uptime_host] = item_total_time

# Print the uptime dictionary
pprint.pprint(uptime_dict)
