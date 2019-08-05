#!/usr/bin/python3

# Data Collector - This tool will automate transfering of data for all your findings.
# This tool will make use of the open() method.
# It will be able to save your findings to a standard .txt file when invoked with apporopriate formatting in a report format.
# HINT: You will need to store results of other tools for tool to work.

import system_info_tool
import ip_mapping
import client_browser

def data_collector():
    print( "data collector" )

if __name__ == "__main__":
    data_collector()
    system_info_tool.system_info_tool()
    ip_mapping.ip_mapping()
    client_browser.client_browser()