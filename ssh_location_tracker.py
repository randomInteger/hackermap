#!/usr/bin/env python3
"""
ssh login attempt location tracker (by country)

This tool runs on any debian linux system and dependds on the geoiplookup tool
existing on the host system.

To install that tool, run:  sudo apt-get install geoip-bin

If you are disturbed by the results, please consider installing a tool like
fail2ban.

Author:  Christopher Gleeson
"""
from operator import itemgetter
import subprocess
import pprint
import string
import sys
import re

#Rip out the failed ssh connection attempts
grep_log = 'sudo grep sshd.\*Failed /var/log/auth.log | uniq'
process = subprocess.Popen(grep_log, shell=True, stdout=subprocess.PIPE)
output = process.communicate()[0]
regex = re.compile("for invalid user .+ from (\d+.\d+.\d+.\d+)")
if process.returncode == 0:
    print('Info: Command ' + grep_log + ' successful.')
else:
    print('Warning: Command ' + grep_log + ' failed!')

#get all the ips that tried to connect to this box
ips = regex.findall(str(output, 'utf-8'))

country_histogram = {}
#Do a geoiplookup for each one and record the country
for ip in ips:
    geo_lookup = 'geoiplookup ' + ip
    process = subprocess.Popen(geo_lookup, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    output_str = str(output, 'utf-8')
    if process.returncode == 0:
        print("GEOIPLOOKUP for IP %s was: %s" % (ip, output_str))
        if output_str in country_histogram.keys():
            country_histogram[output_str] += 1
        else:
            country_histogram[output_str] = 1
    else:
        print('Warning: Command ' + geo_lookup + ' failed!')

#Print out the historgram of values
pp = pprint.PrettyPrinter(indent=4)
for (country, count) in sorted(country_histogram.items(), key=itemgetter(1), reverse=True):
        print("Country:", country.rstrip('\n'))
        print("\tCount:", count)
