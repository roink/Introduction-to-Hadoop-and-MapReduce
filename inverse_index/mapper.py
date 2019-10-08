#!/usr/bin/python3

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
continued = False;
old_line=None;

for line in sys.stdin:
    if continued:
        line = old_line + line;
    data = line.split("\t")
    if len(data)==19:
        node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line.split("\t")
        continued=False;
    else:
        continued=True;
        old_line = line;
        continue;
    #print(data.groups())
    #print(body)
    
    body = body.replace('"'," ")
    
    body = body.replace("'"," ")
    body = body.replace('.'," ")
    body = body.replace(','," ")
    body = body.replace('!'," ")
    body = body.replace('?'," ")
    body = body.replace(':'," ")
    body = body.replace(';'," ")
    body = body.replace('('," ")
    body = body.replace(')'," ")
    body = body.replace('<'," ")
    body = body.replace('>'," ")
    body = body.replace('['," ")
    body = body.replace(']'," ")
    body = body.replace('#'," ")
    body = body.replace('$'," ")
    body = body.replace('='," ")
    body = body.replace('-'," ")
    body = body.replace('/'," ")    
    
    try:
        node_id = int(node_id.replace('"',""))
    except:
        continue;
    

    for word in body.split():
        if "fantastic".upper() in word.upper():
            print("{0}\t{1}".format(word.upper(), node_id))

#for key in hits.keys():
#    print "{0}\t{1}".format(key, hits[key])

