def dihotomic(f, a, b, eps):
    counter = 0
    while(b - a > eps):
        counter += 1
        x = (a + b) / 2
        f1, f2 = f(x-eps), f(x+eps)
        if f1 < f2:
            b = x
        else: a = x
    return (a+b)/2, counter


def golden(f, a, b, eps):
    x1 = b - 2*(b-a)/(1 + 5**0.5)
    x2 = a + 2*(b-a)/(1 + 5**0.5)
    counter = 0
    while (b-a)/2 > eps:
        counter += 1
        f1, f2 = f(x1), f(x2)
        if f1 > f2: 
            a = x1
            x1 = x2
            x2 = b - (x1-a)
        else:
            b = x2
            x2 = x1
            x1 = a + (b-x2)
    return (a+b)/2, counter


def parabolic(f, a, b, eps):
    x = (a+b)/2
    counter = 0
    while True:
        counter += 1
        new_x = x - (((x-a)**2)*(f(x)-f(b)) - ((x-b)**2)*(f(x)-f(a)) ) / (2*((x-a)*(f(x)-f(b)) - (x-b)*(f(x)-f(a))) )
        if abs(new_x-x) < eps: return new_x, counter
        x = new_x


f = lambda x: 3*x**4 - 10*x**3 + 21*x**2 + 12*x

answer, iterations = dihotomic(f, 0.0, 0.5, 0.01)
print('Dihotomic Answer: {}   Iterations: {}'.format(answer, iterations))

answer, iterations = golden(f, 0.0, 0.5, 0.01)
print('Golden Answer: {}   Iterations: {}'.format(answer, iterations))

answer, iterations = parabolic(f, 0.0, 0.5, 0.01)
print('Parabolic Answer: {}   Iterations: {}'.format(answer, iterations))


from matplotlib import pyplot
import numpy
fig = pyplot.subplots()
x = numpy.linspace(-1, 1, 100)
pyplot.plot(x, f(x))
pyplot.show()
