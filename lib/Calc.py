import math

#CODE BY ERIC BLAND

#Uses Midpoint Theorem to find zeros of the function
def zero(func, x1, x2, iteration = 1):
    while(True):
        if iteration == 1000 or func(x2) == 0:
            break
        elif not ((func(x1) > 0 and func(x2) < 0) or (func(x1) < 0 and func(x2) > 0)):
            return None
        elif func((x1 + x2) / 2) > 0:
            if func(x2) > 0:
                x2 = (x1 + x2) / 2
            else:
                x1 = (x1 + x2) / 2
            iteration += 1
        else:
            if func(x2) > 0:
                x1 = (x1 + x2) / 2
            else:
                x2 = (x1 + x2) / 2
            iteration += 1
    return x2

#area under curve using Reinmann Trapezoid formula
def Tareaundercurve(func, x1, x2):
    area = 0
    step = (x2 - x1) / 1000
    while(True):
        if round(x1, 4) == x2:
            return area
            break
        area += ((func(x1) + func(x1 + step)) / 2) * step
        x1 += step

#area under curve using Simpson's formula
def Sareaundercurve(func, a, b):
    n = 1000
    h = (b - a) / n
    iteration, x, area = 1, a + h, func(a)
    while(True):
        if  x == b or iteration == n: 
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

if __name__ == '__main__':
    func = lambda x: x**2 - 10
    print(Tareaundercurve(func, 2, 10))
    print(Sareaundercurve(func, 2, 10))
    print(zero(func,-4,1))



    






