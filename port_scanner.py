#!/usr/bin/python3

# Port Scanner - This tool will scan for open ports on any domain or IP and return a report when completed.
# This tool will make use of the socket and sys modules.
# It will be able to scan any range of ports.
# It will generate a report in the format of: "Port 80: OPEN"

import socket
import argparse
import data_collector

parser = argparse.ArgumentParser (
    prog="Port Scanner",
    description="This tool will scan for open ports on any domain or IP and return a report when completed."
)

parser.add_argument("ip", help="IP to scan")
parser.add_argument("port1", help="scan starting port")
parser.add_argument("port2", nargs="?", help="scan ending port")
parser.add_argument("-C", action="store_true", help="capture output to file")

args = parser.parse_args()

def port_scanner():
    try:
        file = open( "port_scanner.txt", "w" )
        if args.C == True:
            socket.gethostbyname( args.ip )
            if args.port2 != None:
                begin = int( args.port1 )
                end = int( args.port2 )
                for ip in range( begin, end ):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( ip ) ) )
                    if result == 0:
                        print( "Port {}: Open".format( ip ) )
                        file.write( "Port {}: Open\n".format( ip ) )
                        return( data_collector.data_collector( "Port {}: Open\n".format( ip ) ) )
                    else:
                        print( "Port {}: Closed".format( ip ) )
                        file.write( "Port {}: Closed\n".format( ip ) )
                        return( data_collector.data_collector( "Port {}: Closed\n".format( ip ) ) )
                    sock.close()
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( args.port1 ) ) )
                if result == 0:
                    print( "Port {}: Open".format( args.port1 ) )
                    file.write( "Port {}: Open\n".format( args.port1 ) )
                    return( data_collector.data_collector( "Port {}: Open\n".format( args.port1 ) ) )
                else:
                    print( "Port {}: Closed".format( args.port1 ) )
                    file.write( "Port {}: Closed\n".format( args.port1 ) )
                    return( data_collector.data_collector( "Port {}: Closed\n".format( args.port1 ) ) )
                sock.close()
        else:
            socket.gethostbyname( args.ip )
            if args.port2 != None:
                x = int( args.port1 )
                y = int( args.port2 )
                for ip in range( x, y ):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( ip ) ) )
                    if result == 0:
                        print( "Port {}: Open".format( ip ) )
                        file.write( "Port {}: Open\n".format( ip ) )
                    else:
                        print( "Port {}: Closed".format( ip ) )
                        file.write( "Port {}: Closed\n".format( ip ) )
                    sock.close()
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex( ( socket.gethostbyname( args.ip ), int( args.port1 ) ) )
                if result == 0:
                    print( "Port {}: Open".format( args.port1 ) )
                    file.write( "Port {}: Open\n".format( args.port1 ) )
                else:
                    print( "Port {}: Closed".format( args.port1 ) )
                    file.write( "Port {}: Closed\n".format( args.port1 ) )
                sock.close()
        file.close()

    except socket.gaierror:
        print( "Check input information..." )

if __name__ == "__main__":
    port_scanner()
