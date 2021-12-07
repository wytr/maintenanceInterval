import json
import datetime


class Stanzmaschine:
    # Attribute
    filename = ""
    data = 0
    minInterval = 20
    intervalDelayList = []

    # Konstruktor
    def __init__(self, filename, minInterval):
        self.filename = filename
        self.minInterval = minInterval
        self.setData()
        self.calcIntervalList()

    # Methoden

    def getBezeichner(self):
        return self.data["Bezeichner"]

    def getHersteller(self):
        return self.data["Hersteller"]

    def getStandort(self):
        return self.data["Standort"]

    def getAnzahlWartungen(self):
        return len(self.data["Wartung"])

    def getDatumLetzteWartung(self):
        return self.data["Wartung"][-1]["Datum"]

    def getDatumErsteWartung(self):
        return self.data["Wartung"][0]["Datum"]

    def getIntervalDelayList(self):
        return(self.intervalDelayList)

    def calcIntervalList(self):

        for element in range(len(self.data["Wartung"])):

            thisIterationDateEntry = datetime.datetime.strptime(
                self.data["Wartung"][element]["Datum"], "%d.%m.%Y")
            if (element >= 1):
                self.intervalDelayList.append(
                    (previousIterationDateEntry - thisIterationDateEntry).days)

            previousIterationDateEntry = thisIterationDateEntry

    def setData(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except:
            print("no file found")
            return self.data

    def showAllData(self):
        try:
            print(json.dumps(self.data, indent=4))
        except:
            print("failed")

    def checkMaintenanceInterval(self):
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

                    if (abs((previousIterationDateEntry - thisIterationDateEntry).days) >= self.minInterval):
                        print(thisIterationDateEntry.strftime(
                            "%Y-%m-%d"), end="")
                        print(
                            f" - {str(abs((previousIterationDateEntry - thisIterationDateEntry).days + self.minInterval))} Tage")
                    previousIterationDateEntry = thisIterationDateEntry

        except:
            print("failed looping through data")


maschiiiiiisch = Stanzmaschine("datensatz.json", 30)

# maschiiiiiisch.showAllData()

maschiiiiiisch.checkMaintenanceInterval()


print(maschiiiiiisch.getIntervalDelayList())
