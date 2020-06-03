from math import log, pow


xes = [0.1, 0.198, 0.297, 0.401, 0.502, 0.777, 1.089]
yes = [0.1, 0.199, 0.301, 0.399, 0.504, 0.773, 1.089]


def logarithmic():
    print('\033[94mLOGARITHMIC', '\033[0m')
    xLog = []
    yLog = []
    c_a = int(input('a coefficient -> '))
    c_b = int(input('b coefficient -> '))
    for i in range(0, len(xes)):
        xLog.append(log(xes[i]))
        yLog.append(c_a * xLog[i] + c_b)

    n = len(xes)
    A = 0
    B = 0
    C = 0
    D = 0

    for i in range(0, n):
        A += xLog[i] * xLog[i]
        B += xLog[i]
        C += xLog[i] * yLog[i]
        D += yLog[i]

    coef = n / B
    a = (D - C * coef) / (B - A * coef)
    b = (D - a * B) / n
    print('a =', a, '\n', 'b =', b)

    q = 0
    for i in range(0, len(xes)):
        q += pow(a*xLog[i] + b - yLog[i], 2)

    print('inaccuracy =', q, '\n')


def linear():
    print('\033[94mLINEAR', '\033[0m')
    n = len(xes)
    A = 0
    B = 0
    C = 0
    D = 0

    for i in range(0, n):
        A += xes[i] * xes[i]
        B += xes[i]
        C += xes[i] * yes[i]
        D += yes[i]

    coef = n / B
    a = (D - C * coef) / (B - A * coef)
    b = (D - a * B) / n
    print("%.6f" % a, "%.6f" % b, '\n')


linear()
logarithmic()
