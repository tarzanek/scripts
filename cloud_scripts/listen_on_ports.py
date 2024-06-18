#!/usr/bin/python3

import argparse
import socket
import os, sys
from threading import Thread
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("up", "utf-8"))

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def serve_on_port(address,port):
    server = ThreadingHTTPServer((address,port), Handler)
    server.serve_forever()

################################################################################
argp = argparse.ArgumentParser(description = "Open http server on addresses and ports.", formatter_class=argparse.RawDescriptionHelpFormatter,
                               epilog=
'''
Listens on the given set of TCP ports and given addresses with http server. Replies with "up"
''')
argp.add_argument('-a','--address', help='addresses list to bind to', default=["localhost"], action='append', dest='address_set')
argp.add_argument('-p','--port', help='ports to listen on', default=[], action='append', dest='ports_set')

args = argp.parse_args()

# Remove duplicates
address_set = set(args.address_set)
ports_set = set(args.ports_set)
success = True

for addr in address_set:
    print("Starting on address {}".format(addr))

    for port in ports_set:
        checked = True

        print("  Starting on port {}".format(port))
        try:
            Thread(target=serve_on_port, args=[addr,int(port)]).start()
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            print("  Cannot listen on addr:port: {}:{}".format(addr, port))
            success = False

if success:
    input("All ports are listening, press ENTER key to stop and exit.")
    os._exit(0)
else:
    print("Wasn't able to listen on all ports. Exit.")
    os._exit(1)

