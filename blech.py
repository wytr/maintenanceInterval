class Blech:

    n = 10
    raster = []
    programm = []

    def __init__(self):

        self.programm = [1]
        self.initRaster()

    def initRaster(self):

        self.raster = [[1 for x in range(self.n)] for y in range(self.n)]

    def showPattern(self):

        for x in range(self.n):
            for y in range(self.n):

                if(self.raster[x][y] == 1):
                    print('\u2588', end="")
                else:
                    print(' ', end="")
            print()

    def getProgram(self):
        print("program ready")

    def setPattern(self, pattern):

        if len(pattern) == 10:
            for x in range(self.n):
                for y in range(self.n):
                    print("TODO")
            print()
        else:
            print("pattern file not compatible")

    def remove(self, x, y):
        try:
            self.raster[x][y] = 0
            print(f"removed {x},{y}")
        except:
            print("WRONK!")


if __name__ == "__main__":

    testPattern = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    testblech = Blech()
    testblech.showPattern()
    testblech.remove(2, 7)
    testblech.showPattern()
    testblech.setPattern(testPattern)
