from readFiles import *
from detResponse import *
from other import *
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

if __name__ == "__main__":
    """US data paths"""
    usConf = "CovidData/time_series_covid19_confirmed_US.csv" #Path to US confirmed cases data
    usDeath = "CovidData/time_series_covid19_deaths_US.csv" #Path to US deaths data

    """Question 1: Determine the Steady-state solution for country"""

    usCEQ = modelData(openUS(usConf))

    """World data paths"""
    wConf = "CovidData/time_series_covid19_confirmed_global.csv" #Path to world confirmed cases data    
    wDeath = "CovidData/time_series_covid19_deaths_global.csv" #Path to world deaths data
    wRec = "CovidData/time_series_covid19_recovered_global.csv" #Path to world recovery data
    
    """Socio-Political metrics paths"""
    pop = "CovidData/WPP2019_TotalPopulationBySex.csv" #Path to world population data
    hdi = "CovidData/Human development index (HDI).csv" #Path to HDI data

    cDat = {}
    cDat["United States of America"] = usCEQ

    cDat = initDict(cDat, wConf)
    weighted = pullHDI(pullPop(cDat, pop), hdi)
    
    """WORRY ABOUT USING THE DEATH AND RECOVERY DATA ANOTHER TIME
    """

    