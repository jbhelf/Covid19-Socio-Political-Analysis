import math
from sklearn import linear_model
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import random

def sigmoid(x, L ,x0, k):
    try:    
        y = L / (1 + np.exp(-k*(x-x0)))
    except (OverflowError, RuntimeWarning):
        y = (L / 2)
    return (y)

def fitSig(yTrain, xTrain):
    initial = [max(yTrain), np.median(xTrain), 1] #initial guess
    popt, pcov = curve_fit(sigmoid, xTrain, yTrain, p0=initial)
    return popt

def predict(x, L ,x0, k):
    return [sigmoid(i, L ,x0, k) for i in x]

def modelData(data):
    fmx = [i for i in range(len(data))]
    rbest = 0

    bestModel = []
    for i in range(6):
        random.seed()
        seed = random.getrandbits(8)
        [xTrain, xTest, yTrain, yTest] = train_test_split(fmx, data, test_size=0.2, random_state=seed)
        [L, x0, k] = fitSig(yTrain, xTrain)

        yPred = predict(xTest, L ,x0, k)
        c = r2_score(yTest, yPred) #scoring
        if c > rbest:
            bestModel = [L, x0, k]
            rbest = c

    return bestModel
