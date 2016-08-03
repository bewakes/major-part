from sklearn import datasets
import numpy
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
my_data = numpy.genfromtxt('ChitraData.csv',delimiter=',')
new_data = [x[1:] for x in my_data[1:]]

X = numpy.asarray([x[1:] for x in new_data])
Y = [x[0] for x in new_data]

nclasses= 4

yrange = max(Y) - min(Y)

classes = [(min(Y), 11), (11, 15), (15, 25)]

target = []
for val in Y:
    for i, c in enumerate(classes):
        if val>= c[0] and val < c[1]:
            print(val, c[0], c[1], True)
            target.append(i)
        else:
            print(val, c[0], c[1], False)




y_pred = gnb.fit(X,target).predict(X)
print("Number of mislabeled points out of a total %d points: %d" %(X.shape[0],(target != y_pred).sum()))
