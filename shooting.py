import math


def rl_func(x):
    return x + 1 - math.exp(x) * math.cos(x)


def shooting(a, b, n, p, q, f, real_func, o):
    h = (b - a) / n
    y0 = [0.0] * (n + 1)
    y1 = [0.0] * (n + 1)
    y0[0], y0[1] = real_func(a), real_func(a) + o(h)
    y1[0], y1[1] = 0, o(h)

    for i in range(1, n):
        y0[i+1] = (f(a + h*i) * h*h + (2 - q*h*h) * y0[i] - (1 - p*h/2) * y0[i-1]) / (1 + p*h/2)
        y1[i+1] = ((2 - q*h*h) * y1[i] - (1 - p*h/2) * y1[i-1]) / (1 + p*h/2)

    C1 = (real_func(b) - y0[n]) / y1[n]

    y = [0.0] * (n + 1)
    for i in range(0, n + 1):
        y[i] = y0[i] + C1 * y1[i]
    return y


a = 0
b = 1
n = 10
y = shooting(a, b, n, -2, 2, lambda x: 2 * x, rl_func, lambda h: math.pow(h, 3))

for i in range(0, n + 1):
    print(abs(rl_func(a + i * (b - a) / n) - y[i]))