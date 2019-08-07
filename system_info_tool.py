#!/usr/bin/python3

# System Info Tool - This tool will grab the hostname of the target machine.
# This tool will need to use the socket module.
# It will print th ehostname to stdout in the format of: "The hostname is: NoSoupForYou"

import socket
import argparse
import data_collector

parser = argparse.ArgumentParser(
    prog="System Info Tool",
    description="This tool will grab the hostname of the target machine."
)

parser.add_argument("target", help="target machine")
parser.add_argument("-C", action="store_true", help="capture output to file")

args = parser.parse_args()

def system_info_tool():
    try:
        if args.C == True:
            socket.gethostbyaddr( args.target )
            print( "The hostname is: {}".format( socket.gethostbyaddr( args.target )[0] ) )
            return( data_collector.data_collector( "The hostname is: {}\n".format( socket.gethostbyaddr( args.target )[0] ) ) )
        else:
            socket.gethostbyaddr( args.target )
            print( "The hostname is: {}".format( socket.gethostbyaddr( args.target )[0] ) )

    except socket.gaierror:
        print( "Check input information..." )

if __name__ == "__main__":
    system_info_tool()
