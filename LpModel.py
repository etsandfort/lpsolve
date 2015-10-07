__author__ = 'Elliot, David, Jacob'
import numpy as np


class LpModel:
    def __init__(self, numConstraints, numVars):
        self.numConstraints = numConstraints
        self.numVars = numVars
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
        print "Objective function"
        print self.Objfn

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
        print "Constraint Types"
        print self.ConstrType

    def setRHS(self, values):
        self.RHS = np.zeros((self.numConstraints, 1))
        for a in range(0, self.numConstraints):
            self.RHS.put(a, values[a])
        print "RHS Values"
        print self.RHS

    def lpControl(self, minmax):
        if minmax == 'min':
            self.lpControl = 0
        if minmax == 'max':
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
        print "Constraints"
        print self.Constraints

    def printLp(self):
        # matrices: constraints, rhs, objectivefunction
        pass


test = LpModel(4, 2)
test.setColumn(1, [3, 4])
test.setColumn(2, [5, 5])
test.setColumn(3, [1, 1])
test.setColumn(4, [-5, 0])

test.setObjfn([444, 567])
test.setRHS([15, 20, 50, 1000])
test.setConstrType(["=","<=",">","<"])
