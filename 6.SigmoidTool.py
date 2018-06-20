#Multiplies by the newly found thetas in order to obtain new scores.
import math
import numpy as np
import re

def sigmoid(x):
  return np.divide(1,(1 + np.exp(-x)))

def mapScore(p):
        return int(round(-10*np.log10(1-p)))

finalScores= open("mapScoresWithoutMissing.txt", "w")
thetas= open("thetas.txt", "r")

numberOfThetas = 0
#countNumberofThetas
for x in thetas:
        numberOfThetas = numberOfThetas +1


matrixPredictors = [[0 for x in range(numberOfThetas)] for y in range(1)]
matrixTheta = [[0 for x in range(1)] for y in range(numberOfThetas)]

position = 0

thetas= open("thetas.txt", "r") #re-open to reset list

for y in thetas:
        matrixTheta[position][0] = float(y)
        position = position+1

#   matrixPredictors
finalTheta = np.matrix(matrixTheta)

#goes through, does matrix multiplication
with open('mergedPredAndZeros.txt') as sample:
        matrixPredictors[0][0] = 1.0
        for x in sample:
                for z in range (1,numberOfThetas):
                        matrixPredictors[0][z] = (float((x.split(',')[z-1])))

                finalPredictors = np.matrix(matrixPredictors)

                multipliedArray = finalPredictors * (finalTheta)
                p = sigmoid(multipliedArray)

                finalScores.write(str(mapScore(sigmoid(multipliedArray))))
                finalScores.write("\n")

