import time
import os

class MetalSheet:

    n = 10
    pattern = []
    program = []

    def __init__(self):
        self.initPattern()

    def addProgramPattern(self, number):

        if number not in self.program:
            self.program.append(number)
        else:
            print("yikes! already added.")

    def clearProgram(self):
        
        self.program = []

    def initPattern(self):

        self.pattern = [[1 for x in range(self.n)] for y in range(self.n)]

    def showPattern(self):

        for x in range(self.n):
            for y in range(self.n):

                if(self.pattern[x][y] == 1):
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
                    
                    if self.pattern[x][y] == 1 and pattern[x][y] == 0:
                        self.remove(x,y)
                        print("KLNONK!")
                        self.showPattern()
                        time.sleep(0.1)
                        os.system('cls')
            self.showPattern()


            print()
        else:
            print("pattern file not compatible")


    def remove(self, x, y):
        try:
            self.pattern[x][y] = 0
            #print(f"removed {x},{y}")
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

    testblech = MetalSheet()
    testblech.setPattern(testPattern)
