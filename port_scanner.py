#!/usr/bin/python3

# Port Scanner - This tool will scan for open ports on any domain or IP and return a report when completed.
# This tool will make use of the socket and sys modules.
# It will be able to scan any range of ports.
# It will generate a report in the format of: "Port 80: OPEN"

import socket
import sys
import argparse

file = open( "port_scanner.txt", "w" )

def port_scanner():
    parser = argparse.ArgumentParser (
        prog="Port Scanner",
        description="This tool will scan for open ports on any domain or IP and return a report when completed."
    )

    parser.add_argument("ip", help="IP to scan")
    parser.add_argument("port", help="Port(s) to scan over")

    args = parser.parse_args()

    try:
        socket.gethostbyname( args.ip )

    except OSError:
        print( "Check input information...\n" )

    else:
        if '-' in args.port:
            ip_range = args.port.split( '-' )
            x = int( ip_range[0] )
            y = int( ip_range[1] )
            for ip in range( x, y ):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( ip ) ) )
                if result == 0:
                    file.write( "Port {}: Open\n".format( ip ) )
                else:
                    file.write( "Port {}: Closed\n".format( ip ) )
                sock.close()
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( args.port ) ) )
            if result == 0:
                file.write( "Port {}: Open\n".format( args.port ) )
            else:
                file.write( "Port {}: Closed\n".format( args.port ) )
            sock.close()

if __name__ == "__main__":
    port_scanner()

file.close()