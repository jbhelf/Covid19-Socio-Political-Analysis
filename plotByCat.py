import matplotlib.pyplot as plt

def detDist(dct):
    hDist = {'L':0, 'M':0, 'H':0, 'N':0} #cumulative hdi distances
    pDist = {'L':0, 'M':0, 'H':0, 'N':0} #cumulative pfi distances
    eDist = {'L':0, 'M':0, 'H':0, 'N':0} #cumulative education distances

    for i in dct:
        d = (dct[i][0] ** 2 + dct[i][0] ** 2) ** (1/2) #distance
        hDist[dct[i][2]] += d
        pDist[dct[i][3]] += d
        eDist[dct[i][4]] += d
    
    print(hDist)
    print(pDist)
    print(eDist)
        

def plotMetrics(dct):
    low = dict()
    mid = dict()
    high = dict()
    for j in range(2,5):
        for i in dct: 
            if dct[i][j] == 'H':
                high[i] = [dct[i][0], dct[i][1]]
            elif dct[i][j] == 'M':
                 mid[i] = [dct[i][0], dct[i][1]]
            elif dct[i][j] == 'L':
                 low[i] = [dct[i][0], dct[i][1]]

       
        for i in high:
            g = plt.scatter(high[i][0], high[i][1], color='green', label='Upper Tertile')
        for i in mid:
            o = plt.scatter(mid[i][0], mid[i][1], color='orange', label='Middle Tertile')
        for i in low:
            r = plt.scatter(low[i][0], low[i][1], color='red', label='Lower Tertile')
        plt.xlabel("Confirmed Cases (Scaled by Population)")
        plt.ylabel("Deaths (Scaled by Population)")
        if j == 2:
            plt.title("Confirmed Cases vs. Deaths (HDI)")
        elif j == 3:
            plt.title("Confirmed Cases vs. Deaths (PFI)")
        else:
            plt.title("Confirmed Cases vs. Deaths (Education)")
        plt.legend(handles=[g,o,r])
        plt.show()
         