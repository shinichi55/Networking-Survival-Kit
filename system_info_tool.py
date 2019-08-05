#!/usr/bin/python3

# System Info Tool - This tool will grab the hostname of the target machine.
# This tool will need to use the socket module.
# It will print th ehostname to stdout in the format of: "The hostname is: NoSoupForYou"

import socket
import argparse

def system_info_tool():
    parser = argparse.ArgumentParser(
        prog="System Info Tool",
        description="This tool will grab the hostname of the target machine."
    )

    parser.add_argument("ip", help="IP address of Hostname.")

    args = parser.parse_args()

    try:
        socket.gethostbyaddr( args.ip )

    except OSError:
        print( "Input valid IP address" )

    else:
        print( "The hostname is: {}".format( socket.gethostbyaddr( args.ip )[0] ) )

if __name__ == "__main__":
    system_info_tool()
