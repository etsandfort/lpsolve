__author__ = 'Elliot, David, Jacob'
import numpy
class LpModel:
    def __init__(self, numConstraints, numVars):
        self.numConstraints = numConstraints
        self.numVars = numVars
        self.listOfColumns = []
    def setColumn(self, colNum, values):
        self.listOfColumns[colNum]= numpy.matrix(values)
    def setObjfn(self, values):
        self.objfn = numpy.matrix(values)
    def setConstrType(self,constrType):
        if constrType == '<=' :
            self.ConstrType = 1
        if constrType == '>=':
            self.ConstrType = 2
        if constrType == '<':
            self.ConstrType = 3
        if constrType == '>':
            self.ConstrType = 4
        if constrType == '=':
            self.ConstrType = 5
    def setRHS(self, values):
        self.rhs = numpy.matrix(values)
    def lpControl(self, minmax):
        if minmax == 'min':
            self.lpControl=0
        if minmax == 'max':
            self.lpControl=1
    def printLp(self):
        #matrices: constraints, rhs, objectivefunction