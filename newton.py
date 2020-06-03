import numpy
from sympy import *


var('x, y')

def slae(f1, f2, a, b):
    f1x, f1y, = diff(f1, x), diff(f1, y)
    f2x, f2y, = diff(f2, x), diff(f2, y)

    calc = lambda f, a, b: float(f.subs({x:a, y:b}))

    M = numpy.array([[calc(f1x, a, b), calc(f1y, a, b)], [calc(f2x, a, b), calc(f2y, a, b)]])
    v = numpy.array([calc(-f1, a, b), calc(-f2, a, b)])
  
    return numpy.linalg.solve(M, v)


def newton(f1, f2, x0, y0, eps):
    counter = 0
    while 1:
        counter += 1
        g, h = slae(f1, f2, x0, y0)
        x0 += g
        y0 += h 
        if(abs(g) < eps):
            if(abs(h) < eps):
                return x0, y0, counter


f1 = cos(y-1) + x - 0.5
f2 = y - cos(x) - 3
a, b, iterations = newton(f1, f2, 1.2, 3.4, 0.01)
print('x = {}, y = {}, iterations = {}'.format(a, b, iterations))
