from readFiles import *
from detResponse import *
from assignDict import *
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #US data paths
    usConf = "CovidData/time_series_covid19_confirmed_US.csv" #Path to US confirmed cases data
    usDeath = "CovidData/time_series_covid19_deaths_US.csv" #Path to US deaths data

    #World data paths
    wConf = "CovidData/time_series_covid19_confirmed_global.csv" #Path to world confirmed cases data    
    wDeath = "CovidData/time_series_covid19_deaths_global.csv" #Path to world deaths data
    wRec = "CovidData/time_series_covid19_recovered_global.csv" #Path to world recovery data
    
    #Socio-Political metrics paths
    pop = "CovidData/WPP2019_TotalPopulationBySex.csv" #Path to world population data
    hdi = "CovidData/Human development index (HDI).csv" #Path to HDI data
    pfi = "CovidData/PressFreedomIndex.csv"#Path to Press Freedom Index
    edu = "CovidData/EducationTable.csv"#Path to Education data


    """END FILE PATHS SECTION
    Below code is related to the interperetation of the data
    """
    
    #Confirmed cases section
    cDat = {}
    cDat["United States of America"] = modelData(openUS(usConf)) #US confirmed equation

    cDat = initDict(cDat, wConf)

    #Deaths section
    dDat = {}
    dDat["United States of America"] = modelData(openUS(usDeath))

    dDat = initDict(dDat, wDeath)
    
    prCou = dict()#present countries with statistics

    #format: [Lconfirmed, Ldeath, HDI, PFI, Education]

    for i in dDat:
        if i in cDat:
            prCou[i] = [cDat[i][0]+cDat[i][3], dDat[i][0]+dDat[i][3], 'l', 'l', 'l']

    dct = scalePresent(prCou, pop)
    d = {}
    determineCutoffs(d, hdi, pfi, edu)