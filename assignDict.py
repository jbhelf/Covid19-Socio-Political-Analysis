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
        except (RuntimeError, RuntimeWarning): #in the case of failed regression
            pass
        while coCol[i] == coCol[i+1]: #skip through state/provinces of each country
            i += 1
        i += 1

    return dct

def scalePresent(dct, path): #scaling all country data by population
    raw = pd.read_csv(path).values.tolist()
    for i in range(len(raw)): #filtration
        if raw[i][3] == "Medium" and raw[i][4] == 2020 and raw[i][1] in dct:
            dct[raw[i][1]][0] /= raw[i][8] #confirmed scaling
            dct[raw[i][1]][1] /= raw[i][8] #death scaling
    
    return dct
    
def cutoffHelper(data):
    low = np.percentile(data, 33.333)
    high = np.percentile(data, 66.667)
    return low, high

def determineCutoffs(dct, HDI, PFI, EDU):
    """HDI Section"""
    raw = pd.read_csv(HDI)
    slc = [raw["Country"].values.tolist(), raw["2018"].values.tolist()] #sliced set 
    data = [float(i) for i in slc[1][:] if i != '..']
    hdiL, hdiH = cutoffHelper(data)

    """PFI Section"""
    raw = pd.read_csv(PFI)
    slc = [raw["Country Name"].values.tolist(), raw["2019"].values.tolist()]
    data = [float(i) for i in slc[1][:] if not np.isnan(i)]
    pfiL, pfiH = cutoffHelper(data)

    """EDU Section"""
    raw = pd.read_csv(EDU)
    slc = [raw["Country"].values.tolist(), raw["Value"].values.tolist(), raw["Country"].values.tolist()]
    edData = list()
    data = list()
    for i in range(len(slc[0][:])):
        if i+1 == len(slc[0][:]) or slc[0][i] != slc[0][i+1]: #if this is the lowermost (most recent) entry
            edData.append([slc[0][i], slc[1][i]])
            data.append(slc[1][i])
    eduL, eduH = cutoffHelper(data)
    
    