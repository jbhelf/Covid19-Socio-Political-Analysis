import pandas as pd
import numpy as np
from readFiles import *
from detResponse import *

def initDict(dct, path):
    raw = pd.read_csv(path)
    coCol = raw["Country/Region"] #country column
    i = 0
    while i == 0  or coCol[i] != "Zimbabwe": #disincluding minor territories
        try:
            dct[coCol[i]] = modelData(openWorld(path, coCol[i]))
        except RuntimeError: #in the case of failed regression
            dct[coCol[i]] = None
        while coCol[i] == coCol[i+1]: #skip through state/provinces of each country
            i += 1
        i += 1

    return dct

def pullPop(dct, path):
    cLis = [i for i in dct]#list of countries in dictionary
    raw = pd.read_csv(path).values.tolist()
    scaled = {}
    for i in range(len(raw)): #filtration
        if raw[i][3] == "Medium" and raw[i][4] == 2020 and raw[i][1] in cLis:
            if dct[raw[i][1]] != None: #a temporary fix until regression patched
                scaled[raw[i][1]] = dct[raw[i][1]][0] / raw[i][8]
    return scaled

def pullHDI(dct, path):
    cLis = [i for i in dct]#list of countries in dictionary
    
    raw = pd.read_csv(path)
    slc = [raw["HDI Rank (2018)"].values.tolist(), raw["Country"].values.tolist(), raw["2018"].values.tolist()] #sliced set 
    weighted = {}
    for i in range(len(slc[1])): #incorporating HDI
        if slc[1][i] in cLis and slc[2][i] != '..':
            c = slc[1][i]
            if dct[c] != None: #a temporary fix until regression patched
                weighted[c] = dct[c] * (1 - float(slc[2][i]))
    return weighted