import math
import matplotlib.pyplot as plt
import numpy as np
import random
# this code is the same as algClass except the y values are just taken as floats
# this is because they generate very large irreducable fractions that prevent interatingthe function many times
# using floats for y values does not make the solutions less exact because the y value does not affect the x values
# this means that all the k values are exact
# this code can often run 30+  iterations faster than the other one can do roughly 10

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
            print("value was error " + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d))
        return v

    def aabs(self):
        # |x| function
        res = self
        if self.value() < 0:
            res = self.mult(-1)
        return res

    def reduce(self):
        # how to simplify an algebraic number
        # interating the function becomes too computationally intensive otherwise
        # i'm pretty sure something is broken here
        res = self
        reduction = True
        while reduction:
            reduction = False
            for i in range(2, abs(self.a) + 1):
                if res.a % i == 0:
                    if res.b % i == 0:
                        if res.d % i == 0:
                            reduction = True
                            res.a = res.a//i
                            res.b = res.b//i
                            res.d = res.d//i
        return res

def T(X, alpha):
    #the natural extension on a list of two algebraic numbers
    print(X[0].a)
    print(X[0].b)
    print(X[0].c)
    print(X[0].d)
    print(X[0].value())
    print(X[1])
    k = math.floor((1/abs(X[0].value()) - alpha + 2)/2)
    print("k is " + str(k))
    if X[0].value() < 0:
        e = -1
    else:
        e = 1
    p = X[0].aabs().inv().addQ(-2 * k, 1).reduce()
    q = 1/(X[1] * e + 2 * k)
    print("goes to")
    Y = [p,q]
    return Y

def plotAlg(X, P, alpha):
#X is a list containing two algebraic numbers which are the values to be iterated
#P is a pair of lists, one being the x coordinates and the second being the y coordinates to be plotted later
    x_points = [X[0].value()]
    y_points = [X[1]]
    a = X[0]
    for i in range(0, 20):
    #gets very copmutationally difficult very fast after i = 10 due to irreducable fractions
        print("----- i is " + str(i) + " -----")
        X = T(X, alpha)
        x_points.append(X[0].value())
        y_points.append(X[1])
        a = X[0]
    P[0] = P[0] + x_points
    P[1] = P[1] + y_points

points = [[],[]]

alp = 0.5
#this is the alpha value used
#to change number of interations, adjuct the range of the for loop in plotAlg
U = [Alg(8, -3, 11, 3), 0]
plotAlg(U, points, alp)

plt.scatter(points[0],points[1], marker=".")
plt.show()
