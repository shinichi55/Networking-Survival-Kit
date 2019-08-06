#!/usr/bin/python3

# Data Collector - This tool will automate transfering of data for all your findings.
# This tool will make use of the open() method.
# It will be able to save your findings to a standard .txt file when invoked with apporopriate formatting in a report format.
# HINT: You will need to store results of other tools for tool to work.

import argparse
import subprocess
import system_info_tool
import ip_mapping
import client_browser

parser = argparse.ArgumentParser (
    prog="Data Collector",
    description="This tool will automate transfering of data for all your findings."
)

parser.add_argument("domain", help="Domain name you are looking up")
parser.add_argument("port", nargs="?", help="Port(s) to scan")

args = parser.parse_args()

file = open( "data_collector.txt", "w" )

file.write( system_info_tool.system_info_tool() )
file.write( ip_mapping.ip_mapping() )
file.write( client_browser.client_browser() )

file.close()