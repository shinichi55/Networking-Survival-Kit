#!/usr/bin/python3

# System Info Tool - This tool will grab the hostname of the target machine.
# This tool will need to use the socket module.
# It will print th ehostname to stdout in the format of: "The hostname is: NoSoupForYou"

import socket
import argparse

parser = argparse.ArgumentParser(
    prog="System Info Tool",
    description="This tool will grab the hostname of the target machine."
)

parser.add_argument("ip", help="Hostname IP address.")

args = parser.parse_args()

ip = args.ip
hostname = socket.gethostbyaddr( ip )
print( "The hostname is: {}".format( hostname[0] ) )
