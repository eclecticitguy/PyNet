'''
  C. Write a script that processes the show_version output using this package.  It should return something
  similar to the following:

        model:            881
        os_version:    Version 15.0(1)M4
        uptime:           uptime is 12 weeks, 5 days, 1 hour, 4 minutes
'''

import show_version

def main():

    with open("show_version.txt", "r") as show_ver_file:
        show_ver = show_ver_file.read()

        uptime = show_version.obtain_uptime(show_ver)
        model = show_version.obtain_model(show_ver)
        os_version = show_version.obtain_os_version(show_ver)

    print
    print "%15s %-50s" % ("model:", model)
    print "%15s %-50s" % ("os_version:", os_version)
    print "%15s %-50s" % ("uptime:", uptime)
    print


if __name__ == "__main__":

    main()
