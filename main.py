from machine import PunchingMachine
from sheet import MetalSheet
import glob
import datetime
import time

class MachineController:

    path = ""
    productionLine = []
    
    def __init__(self, path):

        self.path = path
        self.setMachines(path)

    def setMachines(self, path):

        files = glob.glob(path, recursive=True)
        for file in files:
            self.productionLine.append(PunchingMachine(file))

    def addMachineExplicit(self, path):

        self.productionLine.append(PunchingMachine(path))

    def removeMachineByPlacement(self, halle, platz):

        foundMachine = False
        for element in self.productionLine:

            if element.data["Standort"]["Halle"] == halle and element.data["Standort"]["Platz"] == platz:
                foundMachine = True
                print("removed machine:")
                print("-------------------")
                element.showHeader()
                print("-------------------")
                self.productionLine.remove(element)

        if foundMachine == False:
            print("no machine with given parameters")

    def getLastMaintainedMachine(self):

        lastMaintainedMachine = self.productionLine[0]

        for machine in self.productionLine:

            if (datetime.datetime.strptime(machine.getLastMaintenanceDate(), "%d.%m.%Y") > datetime.datetime.strptime(lastMaintainedMachine.getLastMaintenanceDate(), "%d.%m.%Y")):
                lastMaintainedMachine = machine

        return lastMaintainedMachine

    def getMachinesByMaintainer(self, name):

        maintainedByList = []
        for machine in self.productionLine:
            for wartung in machine.data["Wartung"]:
                if wartung["von"] == name:
                    maintainedByList.append(machine)
                    break

        return maintainedByList

    def getMachineCount(self):

        return len(self.productionLine)

    def showIds(self):

        for element in self.productionLine:
            print(element.data["Standort"])

    def produceSheet(self, sheet):

        for machine in self.productionLine:

            machine.process(sheet)


if __name__ == "__main__":

    control = MachineController('*.json')

    sheet = MetalSheet()

    sheet.addProgramPattern(1)
    sheet.addProgramPattern(2)
    sheet.addProgramPattern(3)
    sheet.addProgramPattern(4)
    sheet.addProgramPattern(5)
    
    control.produceSheet(sheet)