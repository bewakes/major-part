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
output: prints the basic parameters of the cluster
        and returns the calculated centers of the given dataset as array
'''
def kmeans(source,totalClusters,usecols=None):
    data = np.loadtxt(source,float,delimiter=',',skiprows=1,usecols=usecols)
    kmeans = KMeans(init='k-means++',n_clusters=totalClusters,n_init=10)
    kmeans.fit(data)
    print kmeans.get_params(deep=True)
    print kmeans.cluster_centers_
    return kmeans.cluster_centers_
