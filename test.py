def f(x):
    w = 3
    z = w + x
    return z

a = [[2, 3]]
a.append([1, 2])

import numpy
HEIGHT = 10
WIDTH = 5

def make_grid():
    points = numpy.zeros((HEIGHT * WIDTH, 2))
    #print len(points)
    data = []
    for i in xrange(HEIGHT):
        for j in xrange(WIDTH):
            points[i * WIDTH + j][0] = i
            points[i * WIDTH + j][1] = j
    return points

import datetime
start = datetime.datetime.now()
for i in xrange(100):
    i = i + i
stop = datetime.datetime.now()
stop - start
