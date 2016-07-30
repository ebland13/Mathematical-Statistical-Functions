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


def areaundercurve(func, x1, x2, stepper):
    area = 0
    while(True):
        if round(x1, 4) == x2:
            print("area under the curve is {}".format(area))
            break
        area += ((func(x1) + func(x1 + stepper)) / 2) * stepper
        x1 += stepper







    






