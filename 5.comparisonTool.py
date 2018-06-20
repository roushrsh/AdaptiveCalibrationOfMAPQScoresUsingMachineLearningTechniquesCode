from itertools import izip  #Required tool for better run time, instead of loop in loop
#import matplotlib.pyplot as plt
import numpy as np
import sys

#lots of calculations are done which have been editted out for time, but can be uneditted for personal use.. All you really need is the score variable for most calculations.
#If you're running this for more or less than a map range of 60, you will have to change the 60 and 61s accordingly.
#mapScore here is referencing the mapScore for the GEM Tool, but you can put any tools mapScores, so long as they're sorted in the same order and are from the same DNA sequences, you will go a proper comparison.

oneZero = open("oneZeroWithLeeway.txt", "r")
mapScores = open("mapScores.txt", "r")

score = [[0 for x in range(3)] for y in range(61)] # the actual scores being generated per score. Positives and negatives
#posCutOffUnder = [[0 for x in range(1)] for y in range(61)]
#negCutOffOver = [[0 for x in range(1)] for y in range(61)]
#truePos = [[0 for x in range(1)] for y in range(61)]
#trueNeg = [[0 for x in range(1)] for y in range(61)]
#falsePos = [[0 for x in range(1)] for y in range(61)]
#toPlot = [[0 for x in range(2)] for y in range(61)]

###
##OTHER Graph. Prob vs score
#posProbScore = [[0 for x in range(1)] for y in range(61)]
#negProbScore = [[0 for x in range(1)] for y in range(61)]
#HITSOverMISS = [[0 for x in range(1)] for y in range(61)]

#percentHits = [[0 for x in range(1)] for y in range(61)]
##

#totalPos = 0
#totalNeg = 0


for mapScore in range(0, 61): #Goes through the list and inserts the corresponding scores
        score[mapScore][0] = mapScore
#        posCutOffUnder[mapScore][0] = 0
#        negCutOffOver[mapScore][0] = 0

for x, y in izip(oneZero, mapScores):
        x = x.strip()
        y = y.strip()

        if (x == "1"):
                        score[int(y)][1] = (score[int(y)][1]) +1
#                        totalPos = totalPos + 1
        else:
                        score[int(y)][2] = (score[int(y)][2]) +1
#                        totalNeg = totalNeg + 1

#for num in range (0, 61):
#        if (num > 0):
#                posCutOffUnder[num][0] = posCutOffUnder[num - 1][0] + score[num][1]
#                negCutOffOver[60- num][0] = negCutOffOver[60 - num + 1][0] + score[60 - num][2]
#        else:
#                posCutOffUnder[num][0] = posCutOffUnder[num][0] + score[num][1]
#                negCutOffOver[60][0] = negCutOffOver[60][0] + score [60][2]

#        if ((score[num][1] + score[num][2])) != 0:
#                posProbScore[num][0] = float(score[num][1])/ (score[num][1] + score[num][2]) * 100
#                negProbScore[num][0] = float(score[num][2])/ (score[num][1] + score[num][2]) * 100
#        else:
#                posProbScore[num][0] = 1
#                negProbScore[num][0] = 1

#true Positives (sensitivity)
#for num in range (0, 61):
#        truePos[num][0] = float(posCutOffUnder[num][0]) / totalPos
#        trueNeg[num][0] = float(negCutOffOver[num][0]) / totalNeg
#        falsePos[num][0] = 1 - trueNeg[num][0]
#        toPlot[num][0] = truePos[num][0]
#        toPlot[num][1] = falsePos[num][0]

#        if (score[num][2] != 0):
#                HITSOverMISS[num][0] = float(score[num][1]) / score[num][2]

#        if ((score[num][1] + score[num][2]) != 0):
#                percentHits[num][0] = float(score[num][1]) / (score[num][1] + score[num][2])
#        else:
#                percentHits[num][0] = 1
#false positive (1-specificity)


print(score)
#print "\n"
#print totalPos
#print "\n"
#print totalNeg
#print "\n"
#print posCutOffUnder
#print "\n"
#print negCutOffOver
#print "\n"
#print truePos
#print "\n"
#print trueNeg
#print "\n"
#print falsePos
#print "\n"
#print toPlot

#plt.scatter(xAxis,yAxis)
#plt.savefig('test1.png')
###############ROC Calcs

#print "\n"
#np.savetxt(sys.stdout, toPlot)
#print "\n"
#np.savetxt(sys.stdout, posProbScore)
#print "\n"
#np.savetxt(sys.stdout, negProbScore)
#print "\n"
#np.savetxt(sys.stdout, HITSOverMISS)
#print "\n"
#np.savetxt(sys.stdout, percentHits)


