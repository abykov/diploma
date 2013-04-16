import numpy as nu
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
def f(x, y):
    z = nu.sin(x) * nu.sin(y) / (x * y)
    return z

points = nu.random.rand(100, 2)
data = f(points[:, 1], points[:, 0])
grid_x, grid_y = nu.mgrid[-5:5:100j, -5:5:200j]

grid_z0 = griddata(points, data, (grid_x, grid_y), method='nearest')
plt.imshow(f(grid_x, grid_y).T, extent=(-5,5,-5,5), origin='lower')
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
#plt.show()

import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
def makeData ():
    xx = numpy.arange (-10, 10, 0.1)
    yx = numpy.arange (-10, 10, 0.1)
    xgrid, ygrid = numpy.meshgrid(xx, yx)

    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid)/(xgrid * ygrid)
    return xgrid, ygrid, zgrid

x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(x, y, z)

pylab.show()