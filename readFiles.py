import pandas as pd

def openPopdict(path, country):
    return

def openUS(path): #for US data
    raw = pd.read_csv(path)
    raw = raw.values.tolist() #convert data to list
   
    col = len(raw[0])
    row = len(raw)
 
    for i in range(col):
        if raw[1][i] == 0: #search for column where cases start
            off = i
            break

    sel = [None] * (len(raw[0]) - off)

    for i in range(off, col):
        sum = 0
        for j in range(1, row):
            sum += raw[j][i]
        sel[i - off] = sum
        
    return sel

def openWorld(path, country):
    raw = pd.read_csv(path)
    coCol = raw["Country/Region"] #country column
    row = 1
    for each in coCol:
        if each == country:
            endRow = row
            while(coCol[endRow] == country):
                endRow += 1
            break
            if coCol[row + 1] != country: #check if one or multiple rows reserved
                endRow = row
                break
        row += 1
 
    #now have the start and end rows of the sequence
    raw = raw.values.tolist() #convert data to list

    sel = [None] * (len(raw[0]) - 4)

    for i in range(4, len(raw[0])): #For each column
        sum = 0
        for j in range(row, endRow + 1): #For each row
            sum += raw[j][i]
        sel[i - 4] = sum

    return sel