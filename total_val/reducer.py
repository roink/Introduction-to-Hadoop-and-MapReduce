#!/usr/bin/python

import sys

totalVal = 0
numSales = 0


# Loop around the data
# It will be in the format key\tval
# Where key=1, val is the sale amount
#
# All the sales will be presented,
# we count the sales and the total of the Value

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    _, thisSale = data_mapped
    thisSale = float(thisSale)

    totalVal += thisSale
    numSales +=1

#if oldKey != None:
print numSales, "\t", totalVal

