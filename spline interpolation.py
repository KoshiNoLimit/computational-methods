from math import sin


def func(x):
    return sin(x)


def Func(i, a, h):
    return 3 * (func(a+(i+1)*h) + func(a+(i-1)*h) - 2*func(a+i*h)) / h


def interpolate(a, b, n, x):
    h = (b - a) / n
    xi = a
    count = 0

    while xi < x:
        xi += h
        count += 1

    hi = x - xi + h
    ai = func(xi - h)

    Ai = h
    Bi = h
    Ci = 2 * (h + h)

    alpha = -Bi / Ci
    betta = Func(0, a, h) / Ci
    alphas = [alpha]
    betas = [betta]

    for i in range(2, n):
        betta = (Func(i, a, h) - Ai * betta) / (Ai * alpha + Ci)
        betas.append(betta)
        alpha = -Bi / (Ai * alpha + Ci)
        alphas.append(alpha)

    ci = 0
    ci1 = 0
    if xi != b:
        ci = (Func(n, a, h) - Ai * betas[n-2]) / (Ci + Ai * alphas[n-2])
        for i in range(n-1, count-1, -1):
            ci = alphas[i-1] * ci + betas[i-1]
            
    if xi != a + 1:
        ci1 = alphas[count - 2] * ci + betas[count - 2]
        
    bi = (func(a + count * h) - func(a + (count - 1) * h)) / h + (2*ci + ci1) * h / 3
    di = (ci - ci1) / (3 * h)
    f = ai + bi*hi + ci*hi**2 + di*hi**3
    return f


for x in [0.14, 0.2, 0.45, 0.53, 0.61, 1.2, 1.3, 1.48, 1.73, 2, 2.04, 2.14, 2.35, 2.41, 2.67, 2.87]:
    in_y = interpolate(0, 3, 30, x)
    y = func(x)
    print("x:", "%.2f" % x, "  y:", "%.6f" % y, "  y_in:", "%.6f" % in_y, "  fall:", "%.6f" % abs(y - in_y))
