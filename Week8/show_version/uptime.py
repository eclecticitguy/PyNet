'''
2. Function2 = obtain_uptime -- process the show version output and return the network device's uptime
string (uptime is 12 weeks, 5 days, 1 hour, 4 minutes) else return None.
'''

import re


def obtain_uptime(show_ver):

    match = re.search(r".* (uptime is .+)", show_ver)
    if match:
        return match.group(1)
    else:
        return None


def main():

    with open("../show_version.txt") as show_ver_file:

        show_ver = show_ver_file.read()

    print obtain_uptime(show_ver)

if __name__ == "__main__":
    main()
