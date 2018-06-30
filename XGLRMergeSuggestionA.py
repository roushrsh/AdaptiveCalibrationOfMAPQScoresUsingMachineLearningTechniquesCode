XGBoostScore = open("finalScores60MaxXG.txt", "r")
Beauty = open("finalScores60MaxForFinalBeauty.txt", "w")
mergedResult = open("MERGED60MaxXGBoostLogistic.txt", "r")

from itertools import izip

for x, y in izip(XGBoostScore, mergedResult):
        x = x.strip()
        y = y.strip()
        if (int(y) < 21):
                Beauty.write(x)
                Beauty.write("\n")
        else:
                Beauty.write(y)
                Beauty.write("\n")
