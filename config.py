#-*- encoding: utf-8 -*-
__author__ = 'abykov'

#Число итераций, в течении которых существует фотон
LIFETIME = 10000000

#Число фоторнов
NUMBERS_OF_PHOTONS = 1000000

#Поглащение фотона
LIFE_OR_DEATH = [True, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False,
                 False, False, False]

#максимальная длинна свободного пробега
FREE_PATH = 50

#максимальный угол отклонения
ANGLE = 120

#ширина пробитки
WIDTH = 1000

#высота пробирки
HEIGHT = 300

PLOT_BY = None
#PLOT_BY = 'matplotlib'
PLOT_BY = 'mayavi'