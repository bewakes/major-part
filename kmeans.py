import numpy as np
from sklearn.cluster import KMeans
'''
function: kmeans which calculates the kmeans algorithm on the given dataset
input: source->the source of the file which must be a csv
       totalClusters->the number of clusters we need to use
       usecols-> the index of the columns which is needed to be used 
                 in that csv 
                 for instance usecols=(1,2,4)
                 will read only the 2nd,3rd and 5th column of the provided csv
                 note: the usecols must be provided as tuple but not as array
        aggregateField-> it is a must for district data to visualize in map
output: prints the basic parameters of the cluster
        and returns the calculated centers of the given dataset as array
'''
def kmeans(source,totalClusters,usecols=None, aggregateField=None):
    data = np.loadtxt(source,float,delimiter=',',skiprows=1,usecols=usecols)
    kmeans = KMeans(init='k-means++',n_clusters=totalClusters,n_init=10)
    kmeans.fit(data)
    print(kmeans.get_params(deep=True))

    # since the clusters have formed, aggregate them now.
    finalresult = {}
    sourcefile = open(source, 'r')
    sourcefile.readline() # omitting first line
    for each_line in sourcefile:
        attributes = parseAttributes(each_line, usecols)
        output = kmeans.predict(attributes)

        splitted = each_line.split(',')

        key = splitted[aggregateField].strip()

        if finalresult.get(key):
            finalresult[key][output]+=1
        else:
            finalresult[key] = [0]*totalClusters

    sourcefile.close()
    # Now, clusters have formed
    return finalresult

def parseAttributes(line, usecols):
    return [float(x) for i,x in enumerate(line.strip().split(',')) if i in usecols]

if __name__=="__main__":
    print(kmeans("test.csv",3,(1,2,3),0))
