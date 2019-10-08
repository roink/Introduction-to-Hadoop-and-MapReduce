#!/usr/bin/python3

import sys

oldKey = None
sumSales = 0.0;
numSales = 0;

# Loop around the data
# It will be in the format key\tval
# Where key is the item description, val is the sale amount
#
# All the sales for a particular item will be presented,
# then the key will change and we'll be dealing with the next item

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = eval(thisSale)
    if len(thisSale) != 2:
        #print(thisSale)
        continue
    numSalesIn, cost = thisSale
    

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", (numSales,round(sumSales*100)*0.01))
        sumSales = 0.0
        numSales = 0

    oldKey = thisKey
    numSales +=numSalesIn;
    sumSales += cost;

if oldKey != None:
    print(oldKey, "\t", (numSales,round(sumSales*100)*0.01))

