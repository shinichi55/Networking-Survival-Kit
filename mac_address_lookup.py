#!/usr/bin/python3

# Mac Address Lookup - This tool will return information on mac addresses.
# This tool will use the urllib2, json, and codecs modules.
# This tool will make an api call with mac address to http://macvendors.co/api
# It will take stdin from user.
# It will return a report in format of: "Company Name, Address".

import argparse
import urllib.request
import json
import codecs

def mac_address_lookup():
    parser = argparse.ArgumentParser (
        prog="Mac Address Lookup",
        description="This tool will return information on mac addresses."
    )

    parser.add_argument("mac", help="Mac address to lookup")

    args = parser.parse_args()

    webUrL = urllib.request.urlopen( "http://macvendors.co/api/" + args.mac )
    json_dict = json.load( webUrL )

    return( ( "Company name: {}, Address: {}\n".format( json_dict["result"]["company"], json_dict["result"]["address"] ) ) )

if __name__ == "__main__":
    mac_address_lookup()