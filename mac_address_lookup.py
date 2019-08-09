#!/usr/bin/python3

# Mac Address Lookup - This tool will return information on mac addresses.
# This tool will use the urllib2, json, and codecs modules.
# This tool will make an api call with mac address to http://macvendors.co/api
# It will take stdin from user.
# It will return a report in format of: "Company Name, Address".

import argparse
import urllib.request
import json
import data_collector

parser = argparse.ArgumentParser (
    prog="Mac Address Lookup",
    description="This tool will return information on mac addresses."
)

parser.add_argument("mac", help="mac address to lookup")
parser.add_argument("-C", action="store_true", help="capture output to file")

args = parser.parse_args()

def mac_address_lookup():
    webUrL = urllib.request.urlopen( "http://macvendors.co/api/" + args.mac )
    json_dict = json.load( webUrL )
    if args.C == True:
        print( ( "Company name: {}\nAddress: {}".format( json_dict["result"]["company"], json_dict["result"]["address"] ) ) )
        return( data_collector.data_collector( "Company name: {}\nAddress: {}\n".format ( json_dict["result"]["company"], json_dict["result"]["address"] ) ) )
    else:
        print( ( "Company name: {}\nAddress: {}".format( json_dict["result"]["company"], json_dict["result"]["address"] ) ) )

if __name__ == "__main__":
    mac_address_lookup()