'''
3. Function3 = obtain_model -- process the show version output and return the model (881) else return None.
'''

import re


def obtain_model(show_ver):

    match = re.search(r"Cisco (.+?) .* bytes of memory", show_ver)
    if match:
        return match.group(1)
    else:
        return None


def main():

    with open("../show_version.txt") as show_ver_file:

        show_ver = show_ver_file.read()

    print obtain_model(show_ver)

if __name__ == "__main__":
    main()
