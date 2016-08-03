import matplotlib.pyplot as plot
import numpy
from sklearn import tree, preprocessing
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


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,target)
print clf.predict(X[:1, :])
from sklearn.externals.six import StringIO
with open("tree.dot",'w') as f:
    f = tree.export_graphviz(clf,out_file=f)

