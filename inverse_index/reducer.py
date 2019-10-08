#!/usr/bin/python3

import sys

nodeSet = list()
oldKey = None



# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNode = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", sorted(nodeSet), "\t" ,len(nodeSet))
        nodeSet.clear()

    oldKey = thisKey
    nodeSet.append(int(thisNode))

if oldKey != None:
    print(oldKey, "\t", sorted(nodeSet), "\t" ,len(nodeSet))
