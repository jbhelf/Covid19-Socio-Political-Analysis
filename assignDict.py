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
            #print(coCol[i])
            dct[coCol[i]] = modelData(openWorld(path, coCol[i]))
        except (RuntimeError, RuntimeWarning): #in the case of failed regression
            pass
        while coCol[i] == coCol[i+1]: #skip through state/provinces of each country
            i += 1
        i += 1

    return dct

def scalePresent(dct, path): 
    #scaling all country data by population
    raw = pd.read_csv(path).values.tolist()
    new = {}
    for i in range(len(raw)): #filtration
        if raw[i][3] == "Medium" and raw[i][4] == 2020 and raw[i][1] in dct:
            pop = raw[i][8] * 10 ** 3
            new[raw[i][1]] = [dct[raw[i][1]][0] / pop, dct[raw[i][1]][1] / pop, dct[raw[i][1]][2], dct[raw[i][1]][3], dct[raw[i][1]][4]] 
    
    return new
    
def cutoffHelper(data):
    low = np.percentile(data, 33.333)
    high = np.percentile(data, 66.667)
    return low, high

def categorize(dct, slc, gBou, bBou):
    #gBou being the 'good' bound, and bBou the 'bad'
    for i, j in enumerate(slc[1][:]):
        if slc[0][i] in dct and j != '..':
            if float(j) <= gBou: #lower 3rd
                c='L'
            elif float(j) > bBou: #middle 3rd
                c='H'
            else: #upper 3rd
                c='M'
            dct[slc[0][i]][2] = c
    return dct

def determineCutoffs(dct, HDI, PFI, EDU):
    #Please note that only PFI is desired to be small
    
    #HDI Section:
    raw = pd.read_csv(HDI)
    slc = [raw["Country"].values.tolist(), raw["2018"].values.tolist()] #sliced set 
    data = [float(i) for i in slc[1][:] if i != '..']
    hdiL, hdiH = cutoffHelper(data)

    dct = categorize(dct, slc, hdiL, hdiH)

    #PFI Section:
    raw = pd.read_csv(PFI)
    slc = [raw["Country Name"].values.tolist(), raw["2019"].values.tolist()]
    data = [float(i) for i in slc[1][:] if not np.isnan(i)]
    pfiL, pfiH = cutoffHelper(data)

    for i, j in enumerate(slc[1][:]):
        if slc[0][i] in dct:
            if float(j) < pfiL: #lower 3rd
                c='H'
            elif float(j) >= pfiH: #middle 3rd
                c='L'
            else: #upper 3rd
                c='M'
            dct[slc[0][i]][3] = c

    #EDU Section:
    raw = pd.read_csv(EDU)
    slc = [raw["Country"].values.tolist(), raw["Value"].values.tolist()]
    cLis = list()
    data = list()
    for i in range(len(slc[0][:])):
        if i+1 == len(slc[0][:]) or slc[0][i] != slc[0][i+1]: #if this is the lowermost (most recent) entry
            cLis.append(slc[0][i])
            data.append(slc[1][i])
    eduL, eduH = cutoffHelper(data)

    dct = categorize(dct, slc, eduL, eduH)

    return dct