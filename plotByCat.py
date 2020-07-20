import matplotlib.pyplot as plt
import math

def detDist(l, m, h):
    dist = {'L':0, 'M':0, 'H':0, 'N':0} #cumulative distances

    for i in l:
        dist['L'] += math.sqrt(l[i][0] ** 2 + l[i][1] ** 2)
    for i in m:
        dist['M'] += math.sqrt(m[i][0] ** 2 + m[i][1] ** 2)
    for i in h:
        dist['H'] += math.sqrt(h[i][0] ** 2 + h[i][1] ** 2)

    #print(dist)  
        

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

        mxC = 0 #recording maximum confirmed percentage

        for i in high:
            g = plt.scatter(high[i][0], high[i][1], color='green', label='Upper Tertile')
            if mxC < high[i][0]:
                mxC = high[i][0]
        for i in mid:
            o = plt.scatter(mid[i][0], mid[i][1], color='orange', label='Middle Tertile')
            if mxC < mid[i][0]:
                mxC = mid[i][0]
        for i in low:
            r = plt.scatter(low[i][0], low[i][1], color='red', label='Lower Tertile')
            if mxC < low[i][0]:
                mxC = low[i][0]
        plt.xlabel("Confirmed Cases (Scaled by Population)")
        plt.ylabel("Deaths (Scaled by Population)")
        if j == 2:
            plt.title("Confirmed Cases vs. Deaths (HDI)")
        elif j == 3:
            plt.title("Confirmed Cases vs. Deaths (PFI)")
        else:
            plt.title("Confirmed Cases vs. Deaths (Education)")
        plt.legend(handles=[g,o,r])
        mxC *= 10
        mxC = math.ceil(mxC + 1) #rounding
        dr = 603697/14394056 #7/19/20 rough death rate percentage estimate (total deaths/total infected) from google
        plt.plot([i/10 for i in range(0,mxC,1)], [i*dr/10 for i in range(0,mxC,1)], color='blue')
        plt.show()
        detDist(low, mid, high)
         