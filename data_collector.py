#!/usr/bin/python3

# Data Collector - This tool will automate transfering of data for all your findings.
# This tool will make use of the open() method.
# It will be able to save your findings to a standard .txt file when invoked with apporopriate formatting in a report format.
# HINT: You will need to store results of other tools for tool to work.

def data_collector( function ):
    file = open( "data_collector.txt", "a" )
    file.write( function )
    file.close()
