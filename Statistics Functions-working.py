import math

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




