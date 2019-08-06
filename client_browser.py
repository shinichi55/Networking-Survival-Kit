#!/usr/bin/python3

# Client Browser - This tool will act as your client browser to pull html from any domain.
# This tool will make use of the urllib module.
# It will be able to print the url, status code of request, request header info, server info, and the html.

import socket
import argparse
import urllib.request

def client_browser():
    parser = argparse.ArgumentParser (
        prog="Client Browser",
        description="This tool will act as your client browser to pull html from any domain."
    )

    parser.add_argument("domain", help="Domain to pull html info from")

    args = parser.parse_args()

    try:
        socket.gethostbyname( args.domain )

    except OSError:
        return( "Please check domain name...\n")

    else:
        url = urllib.request.urlopen( "http://" + args.domain )
        return( "Url: \n {}\n".format( url.geturl() ) + "Status code: \n {}\n".format( url.getcode() ) + "Header/Server info: \n {}\n".format( url.info() ) + "Html: \n {}\n".format( url.read() ) )

if __name__ == "__main__":
    client_browser()
