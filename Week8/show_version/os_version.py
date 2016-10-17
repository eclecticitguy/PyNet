'''
1. Function1 = obtain_os_version -- process the show version output and
return the OS version (Version 15.0(1)M4) else return None.
'''

import re


def obtain_os_version(show_ver):

    match = re.search(r"Cisco IOS Software.* (Version .+?),", show_ver)
    if match:
        return match.group(1)
    else:
        return None


def main():

    with open("../show_version.txt") as show_ver_file:

        show_ver = show_ver_file.read()

    print obtain_os_version(show_ver)

if __name__ == "__main__":
    main()
