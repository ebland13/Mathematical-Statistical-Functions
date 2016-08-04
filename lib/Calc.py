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

#area under curve using Reinmann Trapezoid formula
def Tareaundercurve(func, x1, x2, stepper):
    area = 0
    while(True):
        if round(x1, 4) == x2:
            print("area under the curve is {}".format(area))
            break
        area += ((func(x1) + func(x1 + stepper)) / 2) * stepper
        x1 += stepper

#area under curve using Simpson's formula
def Sareaundercurve(func, a, b):
    n = 500
    h = (b - a) / n
    iteration, x, area = 1, a + h, func(a)
    while(True):
        if  round(x, 8) == b or iteration == n: 
            area += func(b)
            area *= (h / 3)
            break
        if iteration % 2 == 0:
            area += 2 * func(x)
            x += h
            iteration += 1
        else:
            area += 4 * func(x)
            x += h
            iteration += 1
    return area





    






