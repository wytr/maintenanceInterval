import json
import datetime


def readData(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except:
        print("no file found")
    return data


def showAllData(data):
    try:
        print(json.dumps(data, indent=4))
    except:
        print("failed")


def checkMaintenanceInterval(datalist, minInterval):
    if (minInterval <= 0):
        print("invalid time interval - needs at least 1 day")
        return 0
    try:
        previousIterationDateEntry = datetime.datetime.strptime(
            datalist[0]["Datum"], "%d.%m.%Y")

        for element in datalist:

            thisIterationDateEntry = datetime.datetime.strptime(
                element["Datum"], "%d.%m.%Y")

            if (abs((previousIterationDateEntry - thisIterationDateEntry).days) >= minInterval):
                print(thisIterationDateEntry.strftime("%Y-%m-%d"), end="")
                print(
                    f" - {str(abs((previousIterationDateEntry - thisIterationDateEntry).days + minInterval))} Tage")
            previousIterationDateEntry = thisIterationDateEntry

    except:
        print("failed looping through data")


databuffer = readData("datensatz.json")

# showAllData(databufer)
checkMaintenanceInterval(databuffer["Wartung"], 30)
