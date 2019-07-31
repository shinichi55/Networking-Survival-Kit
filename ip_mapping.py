#!/usr/bin/python3

# IP Mapping - This tool will return the corresponding IP address of any domain entered.
# This tool will make use of the socket module.
# It will take stdin form the user and return the IP address in the format of: "The IP address of target is: 58.65.22.14"

import socket
import argparse

parser = argparse.ArgumentParser (
    prog="IP Mapping",
    description="This tool will return the corresponding IP address of any domain entered."
)

parser.add_argument("domain", help="Hostname of IP address")

args = parser.parse_args()

try:
    socket.gethostbyname( args.domain )

except OSError:
    print( "Input valid domain name")

else:
    print( "The IP address of target is: {}".format( socket.gethostbyname( args.domain ) ) )
