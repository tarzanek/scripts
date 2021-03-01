#!/usr/bin/python3

import argparse
import socket
import sys

################################################################################
argp = argparse.ArgumentParser(description = "Check that given ports are open on remote addresses.", formatter_class=argparse.RawDescriptionHelpFormatter,
                               epilog=
'''
Tries to connect to the given set of TCP ports on given addresses set.
''')
argp.add_argument('-r','--remote-address', help='remote addresses list', default=[], action='append', dest='remote_address_set')
argp.add_argument('-p','--port', help='Remote ports to check', default=[], action='append', dest='ports_set')
argp.add_argument('-t','--timeout', help='timeout for making the connection', default=2, action='store', type=int, dest='timeout')

args = argp.parse_args()

# Remote duplicates
remote_address_set = set(args.remote_address_set)
ports_set = set(args.ports_set)
timeout = args.timeout
checked = False
success = True

for addr in remote_address_set:
    print("Checking address {}".format(addr))

    for port in ports_set:
        checked = True

        print("  Checking port {}".format(port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((addr, int(port)))
            print("  {}:{} is ok".format(addr, port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            print("  {}:{} is not open: {}".format(addr, port, sys.exc_info()))
            success = False

if checked:
    if success:
        print("Checks passed")
        sys.exit(0)
    else:
        print("One or more ports were not open")
        sys.exit(1)
else:
    print("Nothing checked")
    sys.exit(1)

