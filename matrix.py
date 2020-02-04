#!/usr/bin/env python
import sys


print "argument 1 is the file with all items to search for."
print " argument 2 is a comma separated list [no spaces] of filenames to check"
print " argument 3 is the output file name"
print " the output is a matrix with rows as many item in file argument 1 and X columns, one per file in argument 2"
print " cells will have value 1 if the item is present in file X or 0 if not"
print " there's a header so you know which column corresponds to which file"


items = []
with open(sys.argv[1]) as rd:
    for line in rd:
        items.append(line.strip())

files = sys.argv[2].split(',')

items = set(items)
items= list(items)

files_items=dict()

for f in files:
        with open(f) as fd:
            files_items[f]=list()
            for line in fd:
                files_items[f].append(line.strip())
# now I filled the items and the file items
print 'filling the matrix'

print len(items)
with open(sys.argv[3],'w') as wr:
    #print headers
    header = ['Items']
    kk = files_items.keys()
    header.extend(kk)
    wr.write('\t'.join(header)+'\n')

    for i in items:
        #print i
        ## build line
        outline= [i]
        for k in kk:
            if i in files_items[k]:
                outline.append('1')
            else:
                outline.append('0')
        wr.write('\t'.join(outline)+'\n')
