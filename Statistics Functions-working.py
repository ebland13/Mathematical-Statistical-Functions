import math

#Code by Eric Bland

#return the slope & intercept of the best fit linear line
def LinReg(X, Y):
    multsum = sum(list(map(lambda x, y: x * y, X, Y)))
    Xsqrsum = sum(list(map(lambda x: x ** 2, X)))
    Xsum, Ysum = sum(X), sum(Y)
    n = len(X)

    B = (n * multsum - (Xsum * Ysum)) / (n * Xsqrsum - Xsum ** 2)
    A = (Ysum / n) - B * (Xsum / n)

    return (A, B)

print(LinReg((1, 5, 20), (60, 200, 800)))


def ANOVA(*args):
    #initialize
    listofmeans, listofn, listofvars, alldatapoints, N = [], [], [], [], 0

    #Get mean, n, and variance for each sample. Then calc N and grand mean
    for sample in args:
        mean = sum(sample) / len(sample)   #calc mean
        n = len(sample)   #calc number of data points in samp
        var = 0
        for val in sample:   #calc variances
            var += (val - mean) ** 2
        var /= (n - 1)
        
        listofvars.append(var)
        listofmeans.append(mean)
        listofn.append(n)
        N += n   #sum total number of data points
        alldatapoints += sample   #combine sample sets of data points for grand mean

    #Calculate ANOVA test
    grndmean = sum(alldatapoints) / N   #calc grand mean
    SSb = sum(list(map(lambda x, ni: ni * (x - grndmean) ** 2, listofmeans, listofn)))   #sum of squares between samples
    SSw = sum(list(map(lambda x, ni: (ni - 1) * x, listofvars, listofn)))   #sum of squares within samples
    k = len(args)   #total count of samples
    dfN, dfD = k - 1, N - k   #Numerator and Denominator degrees of Freedom
    MSb, MSw =  SSb / dfN, SSw / dfD   #Mean squares between and within
    F = MSb / MSw   #F-statistic

    return (F, MSb, SSb, dfN, MSw, SSw, dfD, grndmean)

print(ANOVA((1, 3, 9, 29), (22, 34, 9, 88), (23, 44, 55), (8, 99, 22, 10, 22, 30, 44)))