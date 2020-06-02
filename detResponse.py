import math
from sklearn import linear_model
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import random

def sigmoid(x, L ,x0, k, b):
    try:    
        y = L / (1 + np.exp(-k*(x-x0))) + b
    except (OverflowError, RuntimeWarning):
        y = (L / 2) + b
    return (y)

def fitSig(yTrain, xTrain):
    initial = [max(yTrain), np.median(xTrain), 1, 0] #initial guess
    popt, pcov = curve_fit(sigmoid, xTrain, yTrain, p0=initial, method="dogbox")
    return popt

def predict(x, L ,x0, k, b):
    return [sigmoid(i, L ,x0, k, b) for i in x]

def modelData(data):
    fmx = [i for i in range(len(data))]
    rbest = 0

    bestModel = []
    for i in range(6):
        random.seed()
        seed = random.getrandbits(8)
        [xTrain, xTest, yTrain, yTest] = train_test_split(fmx, data, test_size=0.2, random_state=seed)
        [L, x0, k, b] = fitSig(yTrain, xTrain)

        yPred = predict(xTest, L ,x0, k, b)
        c = r2_score(yTest, yPred) #scoring
        if c > rbest:
            bestModel = [L, x0, k, b]
            rbest = c

    return bestModel
