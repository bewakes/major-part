import numpy as np
from kmodes import kprototypes

'''
function: this is an implementation of k-prototypes model
input: source-> csv file,
       categorical->array of index of columns which might be categorical type of data attributes
       n_clusters->number of clusters needed to be obtained as an output of model
       usecols-> tuple consisting of index of the columns in csv which needs to be used which is 'None' by default
output: returns the array of centroids and the seperate array for the categorical modes.
'''
def kprototype(source,categorical,n_clusters,usecols=None, aggregateField=None):
    syms = np.genfromtxt(source,dtype=str,delimiter=',',usecols=usecols)[0,:]
    data = np.genfromtxt(source,dtype=object,delimiter=',',usecols=usecols)[1:,1:]
    print(syms)
    data = data.astype(float)
    kproto = kprototypes.KPrototypes(n_clusters=n_clusters,init='Cao',verbose=2)
    clusters = kproto.fit_predict(data,categorical=categorical)

    print(kproto.cluster_centroids_)
    print(kproto.enc_map_)

    print(kproto.cost_)
    print(kproto.n_iter_)


    return kproto.cluster_centroids_
