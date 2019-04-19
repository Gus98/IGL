import math
import matplotlib.pyplot as plt
import random

def T(Z, alpha):
    e = 0
    a = 0
    b = 0
    if Z[0] >= 0:
        e = 1
    else:
        e = -1
    if Z[0] != 0:
        k = math.floor(1/abs(Z[0]) + 1 - alpha)
        a = e/Z[0] - k
        if (k + e * Z[1]) != 0:
            b = 1/(k + e * Z[1])
        else:
            b = 0
    else:
        a = 0
        b = 1/(1 - alpha + Z[1])
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

M = 1500
alp = 0.9
for n in range(1,M):
    z = ((n - random.uniform(0,1))/M + alp - 1)
    addx_toplot(z, points, alp)

plt.scatter(points[0],points[1], marker=".")
plt.show()
