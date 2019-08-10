#!/usr/bin/python3

# Client Browser - This tool will act as your client browser to pull html from any domain.
# This tool will make use of the urllib module.
# It will be able to print the url, status code of request, request header info, server info, and the html.

import socket
import argparse
import urllib.request
import data_collector

parser = argparse.ArgumentParser (
    prog="Client Browser",
    description="This tool will act as your client browser to pull html from any domain."
)

parser.add_argument("domain", help="domain to pull html info from")
parser.add_argument("-C", action="store_true", help="capture output to file")

args = parser.parse_args()

def client_browser():
    try:
        socket.gethostbyname( args.domain )
        if args.C == True:
            url = urllib.request.urlopen( "http://" + args.domain )
            print( "Url:\n{}\nStatus code:\n{}\nHeader/Server info:\n{}Html:\n{}".format( url.geturl(), url.getcode(), url.info(), url.read().decode("utf-8") ) )
            return( data_collector.data_collector( "Url:\n{}\nStatus code:\n{}\nHeader/Server info:\n{}Html:\n{}\n".format( url.geturl(), url.getcode(), url.info(), url.read().decode("utf-8") ) ) )
        else:
            url = urllib.request.urlopen( "http://" + args.domain )
            print( "Url:\n{}\nStatus code:\n{}\nHeader/Server info:\n{}Html:\n{}".format( url.geturl(), url.getcode(), url.info(), url.read().decode("utf-8") ) )

    except socket.gaierror:
        print( "Please check domain name...")

if __name__ == "__main__":
    client_browser()
