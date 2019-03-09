import math
import matplotlib.pyplot as plt
import numpy as np
import random

def T(Z, alpha):
    #this is the natural extension funtion with the input being a 2 element list
    a = 0
    b = 0
    if Z[0] > 0:
        e = 1
    else:
        e = -1
    k = math.floor((1/abs(Z[0]) - alpha + 3)/2)
    a = 1/abs(Z[0]) - 2 * k + 1
    if (2 * k - 1 + e * Z[1]) != 0:
        b = 1/(2 * k - 1 + e * Z[1])
    else:
        b = 0
    return [a,b]

def addx_toplot(x, P, alpha):
    #this function is used to add all the (x,y) coordinates for the first
    #100 iterations of (x,0) to the list of points to be plotted
    point = [x, 0]
    x_points = [x]
    y_points = [0]
    a = x
    for i in range(0,100):
        point = T(point, alpha)
        x_points.append(point[0])
        y_points.append(point[1])
        a = point[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

points = [[],[]]

M = 200
#the number of points to be tested

alp = 0.8
#the alpha value used in the natural extension

for n in range(1,M):
    z = ((n - random.uniform(0,1))/M + alp - 1)
    addx_toplot(z, points, alp)

plt.scatter(points[0],points[1], marker=".")
#this plots the natural extension

plt.show()
