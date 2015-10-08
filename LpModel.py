from __future__ import print_function
__author__ = 'Elliot, David, Jacob'
import numpy as np

class LpModel:
    def __init__(self, numConstraints, numVars):
        self.numConstraints = numConstraints
        self.numVars = numVars
        self.constrNames = np.zeros((self.numConstraints,1))
        self.Constraints = np.zeros((self.numConstraints, self.numVars))
        self.RHS = np.zeros((self.numConstraints, 1))
        self.objectiveFunction = np.zeros((1, self.numVars))
        self.listOfColumns = []
        self.__makeIndexes(self.numVars)

    def setColumn(self, colNum, values):
        # self.listOfColumns[colNum]= np.matrix(values)
        self._addRow(self.indexes, colNum, values)

    def setObjfn(self, values):
        self.Objfn = np.zeros((1, self.numVars))
        for a in range(0, self.numVars):
            self.Objfn.put(a, values[a])

    def setDimNames(self,dimNames):
        self.constrNames = dimNames

    def setConstrType(self, constrType):
        self.ConstrType = np.zeros((self.numConstraints, 1))
        for a in range(0, self.numConstraints):
            ctype = constrType[a]
            if ctype == '<=':
                const = -2
            if ctype == '>=':
                const = 2
            if ctype == '<':
                const = -1
            if ctype == '>':
                const = 1
            if ctype == '=':
                const = 0
            self.ConstrType.put(a,const)

    def setRHS(self, values):
        self.RHS = np.zeros((self.numConstraints, 1))
        for a in range(0, self.numConstraints):
            self.RHS.put(a, values[a])

    def lpControl(self, minmax):
        if minmax.lower == 'min':
            self.lpControl = 0
        if minmax.lower == 'max':
            self.lpControl = 1

    def __makeIndexes(self, numValues):
        self.indexes = np.zeros((1, numValues))
        for a in range(numValues):
            self.indexes.put(a, a)
        self.indexes = self.indexes.astype(int)

    def _addRow(self, indexes, rowNumber, values):
        indexes += ((rowNumber - 1) * self.numVars)
        low = ((rowNumber - 1) * self.numVars)
        high = (rowNumber * self.numVars)
        counter = 0
        # for a in indexes:
        for a in range(low, high):
            self.Constraints.put(a, values[counter])
            counter += 1

    def printLp(self):

        for i in range(0, self.numVars):
            print("\t\t"+self.constrNames[i], end="")
        if self.lpControl== 1:
            print("\nMax",end="\t")
        else:
            print("\nMin",end="\t")
        for i in range(0, self.numVars):
            if len(str(self.Objfn[0][i]))<4:
                print("\t\t"+str(self.Objfn[0][i]), end="")
            else:
                print("\t"+str(self.Objfn[0][i]), end="")
        print("\r")
        for i in range(0, self.numConstraints):
            if len(str(i))<4:
                print("R"+str(i)+"", end="\t\t")
            else:
                print("R"+str(i)+"", end="\t")
            for j in range(0, self.numVars):
                if len(str(self.Constraints[i][j]))<4:
                    print(self.Constraints[i][j], end="\t\t")
                else:
                    print(self.Constraints[i][j], end="\t")
            if self.ConstrType[i]== 0:
                print("=", end="")
            elif self.ConstrType[i]== 1:
                print(">", end="")
            elif self.ConstrType[i]== 2:
                print(">=", end="")
            elif self.ConstrType[i]== -1:
                print("<", end="")
            elif self.ConstrType[i]== -2:
                print("<=", end="")
            print("\r")


"""test = LpModel(4, 2)
test.setColumn(1, [3, 4])
test.setColumn(2, [5, 5])
test.setColumn(3, [1, 1])
test.setColumn(4, [-5, 0])
test.setObjfn([444, 567])
test.lpControl("max")
test.setRHS([15, 20, 50, 1000])
test.setConstrType(["=","<=",">","<"])
test.setDimNames(["x","y"])
test.printLp()"""
