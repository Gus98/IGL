import math
import matplotlib.pyplot as plt
from decimal import*
import random

getcontext().prec = 100

def T(Z):
    a = Decimal(Decimal('1')/Z[0]) - Decimal(math.floor(Decimal('1')/Z[0]))
    # 1/x - floor(1/x)
    b = Decimal('1')/(Z[1] + Decimal(math.floor(Decimal('1')/Z[0])))
    return [a,b]
#  a = Decimal(Z[0]*10) - Decimal(math.floor(Z[0]*10))
#  b = (Decimal(Z[1]) + Decimal(math.floor(Z[0]*10)))/10
#  return [a,b]

def addx_toplot(x, P):
    point = [Decimal(x),Decimal('0')]
    x_points = [Decimal(x)]
    y_points = [Decimal('0')]
    a = Decimal(x)
    while a > 1E-2:
        point = T(point)
        print(point[0])
        print(str(point[1]) + "\n")
        x_points.append(point[0])
        y_points.append(point[1])
        a = point[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

points = [[],[]]
#addx_toplot(Decimal(2/3), points)
"""
M = 2000
for n in range(1,M):
    z = Decimal(((n - random.uniform(0,1))/M))
    addx_toplot(z,points)
"""
addx_toplot(0.4625348752973409502734985267834950189327435984, points)
plt.scatter(points[0],points[1], marker=".")
plt.show()
