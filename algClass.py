import math
import matplotlib.pyplot as plt
import numpy as np
import random


class Alg(object):
    # to deal with algebraic numbers of the form (a + b * sqrt(c))/d
    # where a, b, c, d are integers
    # this may not actually help with the problem but I thought it would be interesting to see
    # still a work in progress, the graphs are a little messed up
    # I think it is the simplification function
    def __init__(self, a, b, c, d):
        #constructor
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def inv(self):
        #to take 1/x
        x = self.a * self.d
        y = -1 * self.b * self.d
        z = self.a**2 - (self.b**2) * self.c
        res = Alg(x, y , self.c, z)
        return res

    def mult(self, k):
        #multiple algebraic number by an integer
        x = self.a * k
        y = self.b * k
        res = Alg(x, y, self.c, self.d)
        return res

    def addQ(self, p, q):
        # add a rational number
        # It is possible to add two algebraic nubmers
        # but the formula is long and unnecessary
        x = self.a * q + self.d * p
        y = self.b * q
        z = self.d * q
        res = Alg(x, y, self.c, z)
        return res

    def value(self):
        #get the real value of a number
        #used for plotting
        if self.d != 0:
            v = (self.a + self.b * math.sqrt(self.c))/self.d
        else:
            v = 0
            print("value was error")
        return v

    def aabs(self):
        # |x| function
        if self.value() < 0:
            self.mult(-1)
        return self

    def reduce(self):
        # how to simplify an algebraic number
        # interating the function becomes too computationally intensive otherwise
        # i'm pretty sure something is broken here
        res = self
        reduction = True
        while reduction:
            reduction = False
            for i in range(2, abs(self.a) + 1):
                if res.a % i== 0:
                    if res.b % i== 0:
                        if res.d % i== 0:
                            x = res.a//i
                            y = res.b//i
                            z = res.d//i
                            res = Alg(x, y, self.c, z)
                            reduction = True
                            break
        return res

def T(X, alpha):
    #the natural extension on a list of two algebraic numbers
    k = math.floor((1/abs(X[0].value()) - alpha + 2)/2)
    if X[0].value() < 0:
        e = -1
    else:
        e = 1
    p = X[0].aabs().inv().addQ(-2 * k, 1).reduce()
    q = X[1].mult(e).addQ(2 * k, 1).inv().reduce()
    Y = [p,q]
    return Y

def plotAlg(X, P, alpha):
#X is a list containing two algebraic numbers which are the values to be iterated
#P is a pair of lists, one being the x coordinates and the second being the y coordinates to be plotted later
    x_points = [X[0].value()]
    y_points = [X[1].value()]
    a = X[0]
    for i in range(0,10):
        X = T(X, alpha)
        x_points.append(X[0].value())
        y_points.append(X[1].value())
        a = X[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

points = [[],[]]

alp = 0.8
U = [Alg(-1, 1, 5, 2), Alg(0, 0, 0, 1)]
plotAlg(U, points, alp)

plt.scatter(points[0],points[1], marker=".")
plt.show()
