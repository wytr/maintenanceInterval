from stanzmaschine import Stanzmaschine
import glob
import datetime


class MachineController:

    path = ""
    machineList = []

    def __init__(self, path):
        self.path = path
        self.setMachines(path)

    def setMachines(self, path):

        files = glob.glob(path, recursive=True)
        for file in files:
            self.machineList.append(Stanzmaschine(file))

    def addMachineExplicit(self, path):
        self.machineList.append(Stanzmaschine(path))

    def removeMachineByPlacement(self, halle, platz):
        foundMachine = False
        for element in self.machineList:

            if element.data["Standort"]["Halle"] == halle and element.data["Standort"]["Platz"] == platz:
                foundMachine = True
                print("removed machine:")
                print("-------------------")
                element.showHeader()
                print("-------------------")
                self.machineList.remove(element)

        if foundMachine == False:
            print("no machine with given parameters")

    def getLastMaintainedMachine(self):

        lastMaintainedMachine = self.machineList[0]

        for machine in self.machineList:

            if (datetime.datetime.strptime(machine.getLastMaintenanceDate(), "%d.%m.%Y") > datetime.datetime.strptime(lastMaintainedMachine.getLastMaintenanceDate(), "%d.%m.%Y")):
                lastMaintainedMachine = machine

        return lastMaintainedMachine

    def getMachinesByMaintainer(self, name):

        maintainedByList = []
        for machine in self.machineList:
            for wartung in machine.data["Wartung"]:
                if wartung["von"] == name:
                    maintainedByList.append(machine)
                    break

        return maintainedByList

    def getMachineCount(self):
        return len(self.machineList)

    def showIds(self):

        for element in self.machineList:
            print(element.data["Standort"])


if __name__ == "__main__":

    control = MachineController('*.json')

    # steuerung.machineList[0].showAllData()
    # smaschinenPark.removeMachineByPlacement(2, 19)
    print(f"Die Maschine: {control.getLastMaintainedMachine().getLocation()} wurde zuletzt am {control.getLastMaintainedMachine().getLastMaintenanceDate()} gewartet.")
    print("----------------------------------------------------------------------")
    print("Folgende Maschinen wurden von Meier gewartet:")
    for machine in control.getMachinesByMaintainer("Meier"):
        print(
            f"{machine.getIdentifier()} - {machine.getManufacturer()} - {machine.getLocation()}")
    print("----------------------------------------------------------------------")
    print(control.getMachineCount())
