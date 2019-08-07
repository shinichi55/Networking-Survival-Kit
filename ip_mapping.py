#!/usr/bin/python3

# IP Mapping - This tool will return the corresponding IP address of any domain entered.
# This tool will make use of the socket module.
# It will take stdin form the user and return the IP address in the format of: "The IP address of target is: 58.65.22.14"

import socket
import argparse
import data_collector

parser = argparse.ArgumentParser (
    prog="IP Mapping",
    description="This tool will return the corresponding IP address of any domain entered."
)

parser.add_argument("domain", help="domain name of ip address")
parser.add_argument("-C", action="store_true", help="capture output to file")

args = parser.parse_args()

def ip_mapping():
    try:
        if args.C == True:
            socket.gethostbyname( args.domain )
            print( "The IP address of target is: {}".format( socket.gethostbyname( args.domain ) ) )
            return( data_collector.data_collector( "The IP address of target is: {}\n".format( socket.gethostbyname( args.domain ) ) ) )
        else:
            socket.gethostbyname( args.domain )
            print( "The IP address of target is: {}".format( socket.gethostbyname( args.domain ) ) )

    except socket.gaierror:
        print( "Check domain name input..." )

if __name__ == "__main__":
    ip_mapping()
