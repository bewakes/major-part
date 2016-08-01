import sys
import re

csvpath = sys.argv[1]

data = {}
rename = []
delete = []
addafter = []
addnames = []
addafterExp =[]

with open(csvpath, 'r') as csvfile:
    cols = csvfile.readline()
    colslist = cols.strip().split(',')
    print('Columns with indices: ' + ', '.join([str(i)+'='+x for (i, x) in enumerate(colslist)]))
    print()
    print('Enter the columns you want to delete separated by comma(press Enter for none): ')
    deletelist = input().strip()
    print()
    print('Enter the columns you want to add along with operation on cols separated by comma[E.g:- addafter=newcolname=expression(press Enter for none): ')
    print()

    addlist = input().strip()
    if addlist!='':
        for x in addlist.split(','):
            splitted = x.strip().split('=')
            addafter.append(int(splitted[0].strip()))
            addnames.append(splitted[1].strip())
            addafterExp.append(splitted[2].strip())

    if deletelist!='':
        delete = [int(x.strip()) for x in deletelist.split(',')]

    # deletelist update : because first we add and then delete
    for i in range(len(delete)):
        n = 0
        for x in addafter:
            if x<delete[i]:
                n+=1
        delete[i]+=n
    
    ## now write to new file
    filename = None
    match = re.match(r'(.*)/([^/]+)', csvpath)
    if match:
        filename = match.group(2)
        path = match.group(1)
    else:
        filename=csvpath
        path = '.'

    tempfile = input('Enter the output file name, (press enter for default "new-'+filename+'") : ').strip()
    if not tempfile=='':
        newfilepath = path+'/'+tempfile
    else:
        newfilepath = path+'/new-'+filename
    print(newfilepath)
    assert False

    with open(newfilepath, 'w') as newfile:

        # first write the modified columns

        
        # begin with added columns
        for (i, x) in enumerate(addafter):
            colslist.insert(addafter[i]+1, addnames[i])

        # then go for deleted columns
        newcols = [x for (i, x) in enumerate(colslist) if i not in delete]

        newfile.write(','.join(newcols)+'\n')

        cnt = 1
        for line in csvfile:
            vals = [x.strip() for x in line.strip().split(',')]

            print('linecount: ', cnt)
            cnt+=1
            if ''.join(vals)=='':
                continue

            # first consider added cols
            for (i, x) in enumerate(addafterExp):
                try:
                    exp = re.sub(r'(c)(\d+)', r'float(vals[\2])', x)
                    print(exp)
                    print(eval(exp))
                    vals.insert(addafter[i]+1, format(eval(exp), '0.2f'))
                except ZeroDivisionError:
                    vals.insert(addafter[i]+1, '0.00')
            
            # then consider deleted ones
            newvals = [ x for (i, x) in enumerate(vals) if i not in delete]

            # write to newfile
            newfile.write(','.join(newvals)+ '\n')
