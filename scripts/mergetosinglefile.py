import re
import sys
import os

def main():
    folder = '../merged_districts/'
    filenames = os.popen("ls "+folder).read().strip().split('\n')
    writefile = open('allmerged.csv', 'w')
    for i, name in enumerate(filenames):
        f = open(folder+name, 'r')
        if i==0:
            writefile.write(f.readline())
        else:f.readline() # omit first line
        for line in f:
            writefile.write(line)
        f.close()
    writefile.close()

if __name__=="__main__":
    main()
