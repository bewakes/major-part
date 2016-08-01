import sys
import re
from helpers import *

'''
    This script merges the specified csv files and stores the merged result file
    where the first file is located
'''

firstpath = sys.argv[1]
secondpath = sys.argv[2]

firstsplitted = firstpath[:-4].split('/')
secondsplitted = secondpath[:-4].split('/')

mergedpath = '/'.join(firstsplitted[:-1])+'/'+firstsplitted[-1]+'--'+secondsplitted[-1]+'-merged'+firstpath[-4:]
print(mergedpath)

firstfile = open(firstpath, 'r')
secondfile = open(secondpath, 'r')

cols1 = firstfile.readline()
cols2 = secondfile.readline()

print('columns for first file:')
colslist1 = cols1.strip().split(',')
print(showColumns(colslist1))

print()

print('columns for second file:')
colslist2 = cols2.strip().split(',')
print(showColumns(colslist2))

print()

print('Enter the columns respectively from first and second file, one from each, on which you want to perform join, separated by comma:')

joincols = [int(x.strip()) for x in input().strip().split(',')]

joinedcols = ','.join(colslist1 + [x for (i, x) in enumerate(colslist2) if i!=joincols[1]])

# create dictionaries based on the join columns
firstdict = {}
for line in firstfile:
    vals = [x.strip() for x in line.strip().split(',')]
    if ''.join(vals)=='':
        continue
    firstdict[vals[joincols[0]].strip()] = [x.strip() for (i, x) in enumerate(vals) if i!=joincols[0]]

seconddict = {}
for line in secondfile:
    vals = [x.strip() for x in line.strip().split(',')]
    if ''.join(vals)=='':
        continue
    seconddict[vals[joincols[1]].strip()] = [x.strip() for (i, x) in enumerate(vals) if i!=joincols[1]]

# dictionaries are created
# now write to file

with open(mergedpath, 'w') as mergedfile:
    mergedfile.write(joinedcols)
    mergedfile.write('\n')
    for key in firstdict.keys():
        vals = [str(key)]
        if key in seconddict.keys():
            vals = vals + firstdict[key] + seconddict[key]
            mergedfile.write(','.join(vals))
            mergedfile.write('\n')
