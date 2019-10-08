#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
regex = '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)\n'
hits = {}

for line in sys.stdin:
    #print(line)

    data = re.match(regex,line)
    if not data:
        continue;
    #print(data.groups())
    clientIP, ignore , clientID, time, request, status, size = data.groups()
    if clientIP in hits:
        hits[clientIP] += 1.0;
    else:
        hits[clientIP] = 1.0

for key in hits.keys():
    print "{0}\t{1}".format(key, hits[key])

