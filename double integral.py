from math import exp


def trap_method(f, a, b, ph1, ph2, h):
    S = 0.0
    for i in range(0, int((b-a)/h)):
        x = a + i*h
        for j in range(0, int((ph2(x) - ph1(x))/h)):
            q = 1
            if i == 0 or i == int((b-a)/h) - 1:
                q /= 2
            if j == 0 or j == int(ph2(x) - ph1(x))/h - 1:
                q /= 2
            y = (j*h)/(ph2(x)-ph1(x))
            S += q*f(x, y)
    return S * h**2 


def cells_method(f, a, b, ph1, ph2, h):
    S = 0.0
    for i in range(0, int((b-a)/h)):
        x = a + i*h
        for j in range(0, int((ph2(x) - ph1(x))/h)):
            y = (j*h)/(ph2(x)-ph1(x))
            S += f(x + h/2, y + h/2)
    return S * h**2  


def method_testing(method, f, a, b, ph1, ph2, eps):
    In = 0.0
    count = 0
    h = eps ** 0.5
    while True:
        count += 1
        new_In = method(f, a, b, ph1, ph2, h)
        if abs(In - new_In) / 3 < eps:
            break
        In = new_In
        h /= 2
    print(method.__name__, 'iterations:', count)
    print(method.__name__, 'value =', new_In)


a = 0.25
b = 1.0
ph1 = lambda x: 0
ph2 = lambda x: x**0.5
f = lambda x, y: x**1.5 * exp(x*y)

method_testing(cells_method, f, a, b, ph1, ph2, 0.001)
method_testing(trap_method, f, a, b, ph1, ph2, 0.001)

        
    


