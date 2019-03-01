import math
import matplotlib.pyplot as plt
import random

"""
class Alg(object):
    def ___init___(self, a, b, c, d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def inv(z):



u = Alg(2, -5, 7, 2)

"""
#not work?
def T(Z, alpha):
    a = 0
    b = 0
    k = math.floor((1/abs(Z[0]) - alpha + 2)/2)
    a = 1/abs(Z[0]) - 2 * k
    if (2 * k + Z[1]) != 0:
        b = 1/(2 * k + Z[1])
    else:
        b = 0
    return [a,b]

def addx_toplot(x, P, alpha):
    point = [x, 0]
    x_points = [x]
    y_points = [0]
    a = x
    for i in range(0,200):
        point = T(point, alpha)
        x_points.append(point[0])
        y_points.append(point[1])
        a = point[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

points = [[],[]]

M = 100
alp = 1
for n in range(1,M):
    z = ((n - random.uniform(0,1))/M + alp - 1)
    addx_toplot(z, points, alp)

plt.scatter(points[0],points[1], marker=".")
plt.show()
