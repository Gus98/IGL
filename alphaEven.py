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
    k = math.floor((1/abs(Z[0]) - alpha + 2)/2)
    a = 1/abs(Z[0]) - 2 * k
    if (2 * k + e * Z[1]) != 0:
        b = 1/(2 * k + e * Z[1])
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
    for i in range(0, 150):
        point = T(point, alpha)
        x_points.append(point[0])
        y_points.append(point[1])
        a = point[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

def bound(x, alpha):
    #this is the function that is graphed
    y = (2 + (x+1) * ((1 + alpha)/(1 - alpha)))/(2 + (x + 1) * ((3 * alpha - 1)/(1 - alpha)))
    return y
def f(x, alpha):
    #this uses the bound function to generate the list of points to plot later
    y = []
    for i in x:
        y = y + [bound(i, alpha)]
    return y

points = [[],[]]

M = 1000
#the number of points to be tested

alp = 0.5
#the alpha value used in the natural extension

t1 = np.arange(alp - 2, alp, 0.001)
for n in range(1,M):
    z = ((n - random.uniform(0,1))/M + alp - 1)
    addx_toplot(z, points, alp)

plt.scatter(points[0],points[1], marker=".")
#this plots the natural extension

plt.plot(t1, f(t1, alp), 'r')
#this plots the function that would ideally be the left bound

plt.show()
