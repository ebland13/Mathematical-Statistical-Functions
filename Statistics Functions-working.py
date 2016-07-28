import math

#Code by Eric Bland

#return the slope & intercept of the best fit linear line
def LinReg(X, Y):
    multsum = sum(list(map(lambda x, y: x * y, X, Y)))
    Xsqrsum = sum(list(map(lambda x: x ** 2, X)))
    Xsum = sum(X)
    Ysum = sum(Y)
    n = len(X)

    B = (n * multsum - (Xsum * Ysum)) / (n * Xsqrsum - Xsum ** 2)
    A = (Ysum / n) - B * (Xsum / n)

    return (A, B)

print(LinReg((1, 5, 20), (60, 200, 800)))

def ANOVA(*args):
    N = 0
    for a in args:
        N += len(a)

    listofmeans = []
    listofn = []
    for a in args:
        listofmeans.append(sum(a) / len(a))
        listofn.append(len(a))

    listofvars = []
    for a in args:
        mean = sum(a) / len(a)
        n = len(a)
        var = 0
        for val in a:
            var += (val - mean) ** 2
        var /= (n - 1)
        listofvars.append(var)

    grndmean = 0
    allargs = []
    for a in args:
        allargs += a
    grndmean = sum(allargs) / N
    
    SSb = sum(list(map(lambda x, p: p * (x - grndmean) ** 2, listofmeans, listofn)))
    SSw = sum(list(map(lambda x, p: (p - 1) * x, listofvars, listofn)))  
    k = len(listofmeans)
    dfN = k - 1
    dfD = N - k
    MSb = SSb / dfN
    MSw = SSw / dfD
    F = MSb / MSw

    return (F, MSb, SSb, dfN, MSw, SSw, dfD)

print(ANOVA((1, 3, 9, 29), (22, 34, 9, 88), (23, 44, 55)))