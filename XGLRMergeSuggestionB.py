XGBoostScore = open("finalScores60MaxXG.txt", "r")
LogisticScore = open("finalScores60Max.txt", "r")
mergedResult = open("MERGED60MaxXGBoostLogisticRAWR.txt", "w")

from itertools import izip

for x, y in izip(XGBoostScore, LogisticScore):
        x = x.strip()
        y = y.strip()
        if (int(x) > 30):
                mergedResult.write(x)
                mergedResult.write("\n")
        elif (int(x) < 20):
                mergedResult.write(x)
                mergedResult.write("\n")
        else:
                mergedResult.write(y)
                mergedResult.write("\n")

