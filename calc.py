import numpy
from datetime import datetime

featsdim = 99120
size = 500

datalist = [i for i in range(featsdim)]
datalist = numpy.array(datalist)
#print datalist

dataset = numpy.random.rand(size, featsdim)
dataset = dataset / numpy.linalg.norm(dataset, axis = 1).reshape(size, 1)
#print dataset
datalist = dataset[200]*2

time1 = datetime.now()
#for i in range(size):
#    datalist.dot(dataset[i])
datalist = datalist.reshape(featsdim, 1)

print numpy.argmax(dataset.dot(datalist))

time2 = datetime.now()
print str(time2-time1)
