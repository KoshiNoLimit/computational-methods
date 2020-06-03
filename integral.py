import math


def trap(f, a, b, n):
    In = 0.0
    h = (b - a) / n
    In += (f(a) + f(b)) / 2
    for i in range(1, n):
        In += f(a + i*h)
    return In * h


def simpson(f, a, b, n):
    In = 0.0
    h = (b - a) / n
    In += f(a) + f(b)
    for i in range(1, n):
        In += (2 + ((i % 2) << 1)) * f(a + i*h)
    return In * h / 3


def method_testing(method, f, a, b, eps, p):
    In = 0.0
    count = 0
    n = 1
    while 1:
        count += 1
        new_In = method(f, a, b, n)
        if abs(In - new_In) / (pow(2, p) - 1) < eps:
            break
        In = new_In
        n *= 2
    print(method.__name__, 'iterations:', count)
    print(method.__name__, 'value =', "%.6f" % new_In)
    rich_In = new_In + (pow(n/2, p)/(pow(n, p) - pow(n/2, p))) * (new_In - In)
    print(method.__name__, 'value of Richardson =', "%.6f" % rich_In)
    print(method.__name__, 'Richardson correction =', "%.6f" % (rich_In - new_In), '\n')


f = lambda x: math.log(2 * x)
eps = 0.001
a = 0.5
b = 2 * math.e

method_testing(trap, f, a, b, eps, 2)
method_testing(simpson, f, a, b, eps, 4)