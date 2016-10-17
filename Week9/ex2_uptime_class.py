import re


def find_uptime_field(pattern, uptime_str):

    check_pattern = re.search(pattern, uptime_str)
    if check_pattern:
        return int(check_pattern.group(1))
    else:
        return 0


class Uptime(object):

    def __init__(self, uptime_str):

        # Process entire string
        uptime_str = uptime_str.split("uptime is")[1]

        # Uptime list [years, weeks, days, hours, minutes]
        uptime_list = [0, 0, 0, 0, 0]

        # Pattern list for matching
        pattern_list = [
            r" ([0-9]+) year",
            r" ([0-9]+) week",
            r" ([0-9]+) day",
            r" ([0-9]+) hour",
            r" ([0-9]+) minute"
        ]

        # Loop through list and use find_uptime_field function to parse data
        for i, a_pattern in enumerate(pattern_list):
            uptime_list[i] = find_uptime_field(a_pattern, uptime_str)

        # Initialize years, weeks, days, hours and minutes attributes using uptime_list
        (self.years, self.weeks, self.days, self.hours, self.minutes) = uptime_list

    def uptime_seconds(self):

        MINUTES_S = 60
        HOURS_S = MINUTES_S * 60
        DAYS_S = HOURS_S * 24
        WEEKS_S = DAYS_S * 7
        YEARS_S = DAYS_S * 365

        return ((self.years * YEARS_S) + (self.weeks * WEEKS_S) + (self.days * DAYS_S) +
                (self.hours * HOURS_S) + (self.minutes * MINUTES_S))


def main():

    uptime_strings = [
        'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes',
        '3750RJ uptime is 1 hour, 29 minutes',
        'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes',
        'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes',
    ]

    for uptime_str in uptime_strings:

        test_obj = Uptime(uptime_str)

        print
        print uptime_str
        print "%-15s %s" % ("years:", test_obj.years)
        print "%-15s %s" % ("weeks:", test_obj.weeks)
        print "%-15s %s" % ("days:", test_obj.days)
        print "%-15s %s" % ("hours:", test_obj.hours)
        print "%-15s %s" % ("minutes:", test_obj.minutes)

        print "%-15s %s" % ("seconds:", test_obj.uptime_seconds())


if __name__ == "__main__":

    main()