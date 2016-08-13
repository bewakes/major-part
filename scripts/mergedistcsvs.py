import re
import sys
import os
import subprocess

def main():
    districts_folder = sys.argv[1].replace(' ', '\ ')

    if not districts_folder[-1]=='/':
        districts_folder+='/'

    output = os.popen("ls "+districts_folder).read()
    individual = [x for x in output.split('\n') if x.strip()!='']
    #print(individual)

    for district in individual:
        matched = re.match(r'.*District (.+)', district)
        if matched:
            dist_name = matched.group(1).strip()

            dist_path = districts_folder+district.replace(' ','\ ')
            #print(dist_path)
            if dist_path[-1]!='/':dist_path+='/'

            datafilenames = os.popen("ls "+dist_path).read().split('\n')
            datafilenameslst = [x.strip() for x in datafilenames if x.strip()!='']
            # now open each file and do manipulation
            merged_headers = ['DISTRICT']

            numrows = 0
            rows = []
            rows_initialized = False
            for i, datafile in enumerate(datafilenameslst):
                f = open(dist_path.replace('\ ',' ')+datafile, 'r')
                columns = f.readline().strip().split(',')
                if datafile=='COOKING_FUEL':
                    columns.insert(-2, 'OTHERS')
                if i!=0:
                    merged_headers+=columns[1:]
                else:
                    merged_headers+=columns
                # now read data rows
                counter = 0
                tempflag = False
                for line in f:
                    vals = line.strip().split(',')
                    if len(vals)!=len(columns):
                        print(columns)
                        print(vals)
                        print('not equsl')
                    if vals[0].upper()!='TOTAL' and vals[0].upper()!='INSTITUTIONAL':
                        if not rows_initialized:
                            tempflag=True
                            numrows+=1
                            rows.append(vals)
                        else:
                            if counter<numrows:
                                rows[counter]+=vals[1:]
                        counter+=1
                if (not rows_initialized) and tempflag:
                    rows_initialized=True
                f.close()
            for i, row in enumerate(rows):
                rows[i] = [dist_name.upper()]+rows[i] 

            mergedfilepath = '../merged_districts/'+dist_name+'.csv'
            f = open(mergedfilepath, 'w')
            f.write(','.join(merged_headers)+'\n')
            for row in rows:
                f.write(','.join(row)+'\n')
            f.close()
            print('written to:'+ dist_name)


if __name__=="__main__":
    main()
