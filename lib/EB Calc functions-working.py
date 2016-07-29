#!/usr/bin/python3
import math

#CODE BY ERIC BLAND

#Uses Midpoint Theorem to find zeros of the function (with 50 iterations)
def zero(func, x1, x2, dec = 1):
    if dec == 100 or func(x2) == 0:
        print("the zero in the interval is: {}".format(x2))
    elif func(x1) == 0:
        print("the zero in the interval is: {}".format(x1))
    elif not ((func(x1) > 0 and func(x2) < 0) or (func(x1) < 0 and func(x2) > 0)):
        print("function does not have a zero between specified parameters {}, {}".format(x1, x2))
    elif (func(x1) + func(x2)) / 2 < 0:
        x1 = (x1 + x2) / 2
        dec += 1
        zero(func, x1, x2, dec)
    else:
        x2 = (x1 + x2) / 2
        dec += 1
        zero(func, x1, x2, dec)


def thisfunc(x):
    var = (x**2) + (20 * x) - 5
    return var

zero(thisfunc, 0, 10)


def areaundercurve(func, x1, x2, stepper):
    area = 0
    while(True):
        if round(x1, 4) == x2:
            print("area under the curve is {}".format(area))
            break
        area += ((func(x1) + func(x1 + stepper)) / 2) * stepper
        x1 += stepper


def normalpdf(x, m, std):
    var = (1 / (std * (2 * math.pi) ** .5)) * math.exp(-.5 * (((x - m) / std) ** 2))
    return var

def normcdf(x1, x2, m, std):
    normpdf = lambda x: normalpdf(x, m, std)
    var = areaundercurve(normpdf, x1, x2, .0005)
    return var

normcdf(5, 10, 5, 5)





    






