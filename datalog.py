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


def addStar41():
    # Puts * for columns that dont have data after one minute from last column in column41

    dataTime = column41[0][2].split(" ")[1]
    tmp = int(dataTime.split(":")[1])

    column41S = column41[:]

    for i in column41S:

        dataTime = i[2].split(" ")[1]
        minutes = int(dataTime.split(":")[1])

        if abs(tmp - minutes) > 1:
            column41S.insert(column41S.index(i), ['*', '*', '*'])

        tmp = minutes

    return column41S


def addStar70():
    # Puts * for columns that dont have data after one minute from last column in column70

    dataTime = column70[0][2].split(" ")[1]
    tmp = int(dataTime.split(":")[1])

    column70S = column70[:]

    for i in column70S:

        dataTime = i[2].split(" ")[1]
        minutes = int(dataTime.split(":")[1])

        if abs(tmp - minutes) > 1:
            column70S.insert(column70S.index(i), ['*', '*', '*'])

        tmp = minutes

    return column70S


def addStar52():
    # Puts * for columns that dont have data after one minute from last column in column52

    dataTime = column52[0][2].split(" ")[1]
    tmp = int(dataTime.split(":")[1])

    column52S = column52[:]

    for i in column52S:

        dataTime = i[2].split(" ")[1]
        minutes = int(dataTime.split(":")[1])

        if abs(tmp - minutes) > 1:
            column52S.insert(column52S.index(i), ['*', '*', '*'])

        tmp = minutes

    return column52S


def addStar53():
    # Puts * for columns that dont have data after one minute from last column in column53

    dataTime = column53[0][2].split(" ")[1]
    tmp = int(dataTime.split(":")[1])

    column53S = column53[:]

    for i in column53S:

        dataTime = i[2].split(" ")[1]
        minutes = int(dataTime.split(":")[1])

        if abs(tmp - minutes) > 1:
            column53S.insert(column53S.index(i), ['*', '*', '*'])

        tmp = minutes

    return column53S


def showColumns():
    # Gets arranged data and shows them in columns for each mac address

    makeColumns()
    column41S = addStar41()
    column70S = addStar70()
    column52S = addStar52()
    column53S = addStar53()

    c = 0
    print("             mac : 41")
    print("------------------------------------")
    for i in column41S:
        print(str(c) + ") " + i[0] + "  " + i[1] + "  " + i[2])
        c += 1

    print("***************************************\n")

    c = 0
    print("             mac : 70")
    print("------------------------------------")
    for i in column70S:
        print(str(c) + ") " + i[0] + "  " + i[1] + "  " + i[2])
        c += 1

    print("***************************************\n")

    c = 0
    print("             mac : 52")
    print("------------------------------------")
    for i in column52S:
        print(str(c) + ") " + i[0] + "  " + i[1] + "  " + i[2])
        c += 1

    print("***************************************\n")

    c = 0
    print("             mac : 53")
    print("------------------------------------")
    for i in column53S:
        print(str(c) + ") " + i[0] + "  " + i[1] + "  " + i[2])
        c += 1

    # Deletes extra data from RAM
    del column41S[:]
    del column70S[:]
    del column52S[:]
    del column53S[:]

    plotData()


def plotData():
    # Draws plot for each mac address

    print("\n")
    exitNum = input("Exit(y/n)? ")

    if(exitNum.upper() == 'Y'):
        exit()

    elif(exitNum.upper() == 'N'):

        Y = []
        columnMacForPlot = input("Enter column mac address: ")

        if columnMacForPlot == "41":

            fromRow = int(input("From: "))
            toRow = int(input("To: "))

            if fromRow >= 0 and toRow < len(column41):

                X = range(fromRow, toRow)

                for i in range(fromRow, toRow):
                    Y.append(column41[i][0])

            else:
                plotData()

        elif columnMacForPlot == "70":

            fromRow = int(input("From: "))
            toRow = int(input("To: "))

            if fromRow >= 0 and toRow < len(column70):

                X = range(fromRow, toRow)

                for i in range(fromRow, toRow):
                    Y.append(column70[i][0])

            else:
                plotData()

        elif columnMacForPlot == "52":

            fromRow = int(input("From: "))
            toRow = int(input("To: "))

            if fromRow >= 0 and toRow < len(column52):

                X = range(fromRow, toRow)

                for i in range(fromRow, toRow):
                    Y.append(column52[i][0])

            else:
                plotData()

        elif columnMacForPlot == "53":

            fromRow = int(input("From: "))
            toRow = int(input("To: "))

            if fromRow >= 0 and toRow < len(column53):

                X = range(fromRow, toRow)

                for i in range(fromRow, toRow):
                    Y.append(column53[i][0])

            else:
                plotData()

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