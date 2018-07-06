## data logger

import time
import matplotlib.pyplot as plt


column41 = []
column70 = []
column52 = []
column53 = []


def removeExtraData():
    # Removes bad data from logs and puts [macAddress, tempreture, moisture, epocTime] on data list

    try:
        file = open("DATALOG.TXT", "r")
    except:
        print("Could not open the file :(")

    data = []

    for i in file.readlines():
        if(i.split(" ")[0][0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            _, mac, temp, moisture, epoc, _ = i.split(", ")
            data.append([mac, temp, moisture, epoc])

    file.close()

    return data


def convertEpocTime(epTime):
    # Convers epoc time to a string as data and time

    newTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epTime))
    return newTime


def makeColumns():
    # Makes 4 column for each of mac addresses includes tempreture, moisture, dataTime

    data = removeExtraData()

    for i in data:

        if i[0].split(":")[-1] == "41":
            column41.append([i[1], i[2], convertEpocTime(int(i[-1]))])

        elif i[0].split(":")[-1] == "70":
            column70.append([i[1], i[2], convertEpocTime(int(i[-1]))])

        if i[0].split(":")[-1] == "52":
            column52.append([i[1], i[2], convertEpocTime(int(i[-1]))])

        if i[0].split(":")[-1] == "53":
            column53.append([i[1], i[2], convertEpocTime(int(i[-1]))])

    # Deletes extra data from RAM
    del data[:]


def addStar(column):
    # Puts * for columns that dont have data after one minute from last column

    dataTime = column[0][2].split(" ")[1]
    tmp = int(dataTime.split(":")[1])

    columnS = column[:]

    for i in columnS:

        dataTime = i[2].split(" ")[1]
        minutes = int(dataTime.split(":")[1])

        if abs(tmp - minutes) > 1:
            columnS.insert(columnS.index(i), ['*', '*', '*'])

        tmp = minutes

    return columnS


def showData(column, mac):
    # Shows data of each mac address in a column

    c = 0
    print("             mac : {0}".format(mac))
    print("------------------------------------")
    for i in column:
        print(str(c) + ") " + i[0] + "  " + i[1] + "  " + i[2])
        c += 1

    print("***************************************")


def showColumns():
    # Gets arranged data and shows them in columns for each mac address

    makeColumns()
    column41S = addStar(column41)
    column70S = addStar(column70)
    column52S = addStar(column52)
    column53S = addStar(column53)

    showData(column41S, 41)
    showData(column70S, 70)
    showData(column52S, 52)
    showData(column53S, 53)

    # Deletes extra data from RAM
    del column41S[:]
    del column70S[:]
    del column52S[:]
    del column53S[:]

    plotData()


def getRangeOfPlot(column):
    # Gets range of X and Y from user and makes them for each mac addresses logs

    Y = []
    fromRow = int(input("From: "))
    toRow = int(input("To: "))

    if fromRow >= 0 and toRow < len(column41):

        X = range(fromRow, toRow)

        for i in range(fromRow, toRow):
            Y.append(column[i][0])

    else:
        plotData()

    return X, Y


def plotData():
    # Draws plot for each mac address

    exitNum = input("Exit(y/n)? ")

    if(exitNum.upper() == 'Y'):
        exit()

    elif(exitNum.upper() == 'N'):

        columnMacForPlot = input("Enter column mac address: ")

        if columnMacForPlot == "41":

            X, Y = getRangeOfPlot(column41)

        elif columnMacForPlot == "70":

            X, Y = getRangeOfPlot(column70)

        elif columnMacForPlot == "52":

            X, Y = getRangeOfPlot(column52)

        elif columnMacForPlot == "53":

            X, Y = getRangeOfPlot(column53)

        else:
            plotData()

    else:
        plotData()

    plt.plot(X, Y, 'r')
    plt.xlabel("range")
    plt.ylabel("tempreture")
    plt.title('Tempreture plot')
    plt.show()

    plotData()


showColumns()