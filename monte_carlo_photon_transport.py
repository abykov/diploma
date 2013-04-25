#-*- encoding: utf-8 -*-
__author__ = 'abykov'
from config import *
import math
import random
import numpy
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mayavi import mlab
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import datetime

start = datetime.datetime.now()


class PhotonTransport(object):
    '''
    Этот класс реализует метод Монде-Карло для фотонов
    '''
    def __init__(self):
        self.NUMBERS = NUMBERS_OF_PHOTONS
        self.LIFETIME = LIFETIME
        self.FREE_PATH = FREE_PATH
        self.ANGLE = ANGLE
        self.LIFE_OR_DEATH = LIFE_OR_DEATH
        self.tube = []
        for _ in xrange(WIDTH):
            self.tube.append([0] * HEIGHT)

    def random_angle(self):
        '''
        Этот метод расчитывает случайный угол отражения фотона
        '''
        return random.randint(0, ANGLE)

    def random_mean_free_path(self):
        '''
        Этот метод расчитывает случайную длину свободного пробега
        фотона
        '''
        return random.randint(0, FREE_PATH)

    def random_start(self, min, max):
        '''
        Этот метод расчитывает случайную точку входа фотона в объект
        '''
        return random.randint(min, max)

    def life_or_death(self):
        '''
        Этот метод случайным образом определяе поглотился фотон
        или отразился
        '''
        return random.choice(LIFE_OR_DEATH)

    def main(self):
        '''
        Этот метод определяет распределение фотонов
        '''
        j = 0
        for photon in xrange(self.NUMBERS):
            if photon % 1000 == 0:
                print str(photon) + " of " + str(self.NUMBERS)
            self.x = self.random_start(int(HEIGHT / 2) - 2, int(HEIGHT / 2) + 2)
            self.y = 0
            for i in xrange(self.LIFETIME):
                angle = self.random_angle()
                length = self.random_mean_free_path()
                self.x += int(round(length * math.sin(
                    float(angle - ANGLE / 2) / 180.0 * math.pi)))
                self.y += int(round(length * math.cos(
                    float(angle - ANGLE / 2) / 180.0 * math.pi)))

                if self.x > len(self.tube[0]) - 1 or self.x < 0 or \
                   self.y > len(self.tube) - 1 or self.y < 0:
                    break

                if i > 0 and self.life_or_death():
                    j += 1
                    self.tube[self.y][self.x] += 20
                    break
        return (self.tube, j)


MK = PhotonTransport()


def make_data():
    x = numpy.arange(0, HEIGHT)
    y = numpy.arange(0, WIDTH)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid, f_count = MK.main()
    return xgrid, ygrid, zgrid, f_count


def make_grid(z):
    points = numpy.zeros((HEIGHT * WIDTH, 2))
    data = numpy.zeros(HEIGHT * WIDTH)
    for i in xrange(HEIGHT):
        for j in xrange(WIDTH):
            points[i * WIDTH + j][0] = i
            points[i * WIDTH + j][1] = j
            data[i * WIDTH + j]= z[j][i]
    return points, data


def print_to_file():
    file = open("data.dat", 'w')
    for i in xrange(HEIGHT):
        for j in xrange(WIDTH):
            file.write(str(i) + '\t' + str(j) + '\t' + str(z[j][i]) + '\n')


def plot_data(x, y, z):
    if PLOT_BY == 'matplotlib':
        fig = pylab.figure()
        axes = Axes3D(fig)
        #axes.plot_surface(y, x, z)
        axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap = cm.jet )
        pylab.show()
    elif PLOT_BY == 'mayavi':
        mlab.mesh(x, y, z, colormap='YlGnBu', )
        mlab.view(.0, -5.0, 4)
        mlab.show()

x, y, z, f_count = make_data()
print str(f_count) + ' photons is absorbed (' + str(float(f_count) / NUMBERS_OF_PHOTONS * 100.0) +' %)'

points, data = make_grid(z)

grid_z0 = griddata(points, data, (x, y), method='cubic')

stop = datetime.datetime.now()
print 'operation time: ' + str(stop - start)

plot_data(x, y, z)
plt.imshow(z)
plt.show()
#print y, len(y), len(y[1])
