#!/usr/bin/python3

#CODE BY ERIC BLAND

#Uses Midpoint Theorem to find zeros of the function (with 50 iterations)
def zero(func, x1, x2, dec = 1):
    if dec == 50:
        print(x2)
    else:
        if not ((func(x1) > 0 and func(x2) < 0) or (func(x1) < 0 and func(x2) > 0)):
            print("function does not have a zero between specified parameters {}, {}".format(x1, x2))
        else:
            if (func(x1) + func(x2)) / 2 < 0:
                x1 = (x1 + x2) / 2
            else:
                x2 = (x1 + x2) / 2
            dec += 1
            zero(func, x1, x2, dec)


def thisfunc(n):
    var = (n**3) + (n * 2) - 1
    return var

print(zero(thisfunc, 0, 10))


def areaundercurve(func, x1, x2, stepper):
    CDFarea = 0
    while(True):
        if round(x1, 4) == x2:
            print("area under the curve is {}".format(CDFarea))
            break
        CDFarea += ((func(x1) + func(x1 + stepper)) / 2) * stepper
        x1 += stepper


#normal pdf, needs pi and exp constants from 'math' pack
def normalpdf(x, m, std):
    var = (1 / (std * (2 * 3.141592654) ** .5)) * 2.718281828 ** (-.5 * (((x - m) / std) ** 2))
    return var

def normcdf(x1, x2, m, std):
    normpdf = lambda x: normalpdf(x, m, std)
    var = areaundercurve(normpdf, x1, x2, .0005)
    return var

print(normcdf(5, 10, 5, 5))

    






