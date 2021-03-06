import json
import datetime
import time

class PunchingMachine:
    # Attribute
    filename = ""
    data = 0
    minInterval = 20
    intervalDelayList = []
    users = {}

    patternNumber = 0
    pattern = [0][0]


    # Konstruktor

    def __init__(self, filename):
        self.filename = filename
        self.openJsonFile()
        self.calcIntervalList()
        self.setPattern()

    # Methoden
    def process(self, metalsheet):
        if self.getPatternNumber() in metalsheet.program:
            metalsheet.setPattern(self.pattern)
            print(f"Finished program: {self.getPatternNumber()}")
            time.sleep(2)

    def getIdentifier(self):
        return self.data["Bezeichner"]

    def getPatternNumber(self):
        return self.patternNumber

    def getManufacturer(self):
        return self.data["Hersteller"]

    def getLocation(self):
        return self.data["Standort"]

    def getMaintenanceCount(self):
        return len(self.data["Wartung"])

    def getLastMaintenanceDate(self):
        return self.data["Wartung"][-1]["Datum"]

    def getFirstMaintenanceDate(self):
        return self.data["Wartung"][0]["Datum"]

    def getIntervalDelayList(self):
        return(self.intervalDelayList)

    def getMaintenanceListLen(self):
        return (len(self.data["Wartung"]))

    def setPattern(self):

        self.pattern = self.data["Muster"]
        self.patternNumber = self.data["MusterNr"]

    def getPattern(self):
        return self.pattern

    def getPatternNumber(self):
        return self.patternNumber

    def setSheet(self, sheet):
        print("sheet set")

    def getSheet(self):
        print("get sheet")

    def calcIntervalList(self):

        for element in range(len(self.data["Wartung"])):

            thisIterationDateEntry = datetime.datetime.strptime(
                self.data["Wartung"][element]["Datum"], "%d.%m.%Y")
            if (element >= 1):
                self.intervalDelayList.append(
                    (previousIterationDateEntry - thisIterationDateEntry).days)

            previousIterationDateEntry = thisIterationDateEntry

    def openJsonFile(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except:
            print("no file found")
            return self.data

    def setMaintenance(self, name):
        tempDict = {
            "Datum": datetime.date.today().strftime("%d.%m.%Y"),
            "Name": name
        }
        print(tempDict)
        self.data["Wartung"].append(tempDict)

    def showAllData(self):
        try:
            print(json.dumps(self.data, indent=4))
        except:
            print("failed")

    def showHeader(self):
        print(json.dumps(self.data["Bezeichner"]))
        print(json.dumps(self.data["Hersteller"]))
        print(json.dumps(self.data["Standort"], indent=4))

    def saveJsonFile(self):
        try:
            with open(self.filename, "w") as outfile:
                json.dump(self.data, outfile, indent=4)
        except:
            print("no file found")
            return self.data

    def checkMaintenanceInterval(self, minInterval):
        if (self.minInterval <= 0):
            print("invalid time interval - needs at least 1 day")
            return 0
        try:
            previousIterationDateEntry = datetime.datetime.strptime(
                self.data["Wartung"][0]["Datum"], "%d.%m.%Y")
            for element in range(len(self.data["Wartung"])):
                if (element >= 1):
                    thisIterationDateEntry = datetime.datetime.strptime(
                        self.data["Wartung"][element]["Datum"], "%d.%m.%Y")

                    if (abs((previousIterationDateEntry - thisIterationDateEntry).days) >= minInterval):
                        print(thisIterationDateEntry.strftime(
                            "%Y-%m-%d"), end="")
                        print(
                            f" - {str(abs((previousIterationDateEntry - thisIterationDateEntry).days + minInterval))} Tage")
                    previousIterationDateEntry = thisIterationDateEntry

        except:
            print("failed looping through data")

if __name__ == "__main__":

    testMachine = PunchingMachine("machine_config_1.json")

    print(testMachine.getPattern())