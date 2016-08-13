from kmeans import kmeans
from kprototype import kprototype
usecols = (1,2)
kmeans('ChitraData.csv',5,usecols)
kprototype(source='ChitraData.csv',n_clusters=5,usecols=usecols,categorical=[1])
